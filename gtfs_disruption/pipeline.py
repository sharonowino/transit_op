from sklearn.pipeline import Pipeline as Pipeline
from sklearn.pipeline import FeatureUnion as FeatureUnion
from sklearn.compose import ColumnTransformer as ColumnTransformer

# Minimal class stubs to satisfy legacy pickles that reference custom model wrappers.
# These stubs are only used for unpickling and re-serializing to current formats.
class SpatialRFModel:
    def __init__(self, *args, **kwargs):
        pass

class STGATModel:
    def __init__(self, *args, **kwargs):
        pass

class STARNGATModel:
    def __init__(self, *args, **kwargs):
        pass

__all__ = ["Pipeline", "FeatureUnion", "ColumnTransformer", "SpatialRFModel", "STGATModel", "STARNGATModel"]
