# Shim package to satisfy old pickle imports from 'gtfs_disruption'
# This module will attempt to resolve attribute lookups to the
# transit_dashboard.backend.features module so legacy pickles can unpickle.

import importlib
from types import ModuleType

try:
    _features = importlib.import_module("transit_dashboard.backend.features")
except Exception:
    _features = None


def __getattr__(name: str):
    """Dynamically resolve attributes by delegating to transit_dashboard.backend.features.

    If the requested attribute exists in the features module, return it. Otherwise raise
    AttributeError so import machinery behaves normally.
    """
    if _features is not None and hasattr(_features, name):
        return getattr(_features, name)
    raise AttributeError(f"module 'gtfs_disruption' has no attribute '{name}'")


# For introspection tools
__all__ = getattr(_features, "__all__", [])
