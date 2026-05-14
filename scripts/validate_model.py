import sys
import pickle
import joblib
import numpy as np

# Usage: python validate_model.py /absolute/path/to/model.pkl
# Exits 0 on success, non-zero on failure

if len(sys.argv) < 2:
    print("Usage: validate_model.py <model_path>")
    sys.exit(2)

path = sys.argv[1]

try:
    try:
        model = joblib.load(path)
    except Exception:
        with open(path, "rb") as f:
            model = pickle.load(f)

    # If wrapper dict, extract
    if isinstance(model, dict):
        model = model.get("model") or model.get("trained_model") or model

    # Build a small synthetic sample matching 12 features
    X = np.array([[35, 5, 30, 50, 70, 0.2, 0.85, 15, 0.1, 1, 0.9, 0.05]])

    if hasattr(model, "predict"):
        _ = model.predict(X)
    elif hasattr(model, "predict_proba"):
        _ = model.predict_proba(X)
    else:
        print("Model has no predict method")
        sys.exit(3)

    print("Model validation successful")
    sys.exit(0)
except Exception as e:
    print("Validation failed:", e)
    sys.exit(4)
