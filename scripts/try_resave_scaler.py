from pathlib import Path
import joblib, pickle, os

MODEL_DIR = Path(r"C:\Users\Sharon\Documents\python_learning\netherapp\transit_dashboard\models")
SCALER = MODEL_DIR / 'scaler_latest.pkl'
print('Scaler path:', SCALER)
if not SCALER.exists():
    print('Scaler file not found')
else:
    tmp = SCALER.with_suffix('.repack.pkl')
    try:
        try:
            obj = joblib.load(SCALER)
            loader='joblib'
        except Exception:
            with open(SCALER,'rb') as f:
                obj = pickle.load(f)
            loader='pickle'
        print('Loaded scaler via', loader, 'type', type(obj))
        # re-save via joblib to tmp then atomic replace
        joblib.dump(obj, tmp, compress=0)
        os.replace(str(tmp), str(SCALER))
        print('Re-saved scaler to', SCALER)
    except Exception as e:
        print('Failed to re-save scaler:', e)
