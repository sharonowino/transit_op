import os
import sys
import pickle
import joblib
import traceback
from pathlib import Path

# Ensure project root on sys.path so legacy modules like 'gtfs_disruption' can be imported
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

MODEL_DIR = r"C:\Users\Sharon\Documents\python_learning\netherapp\transit_dashboard\models"

files = [f for f in os.listdir(MODEL_DIR) if f.endswith('.pkl')]
if not files:
    print('No .pkl files found in', MODEL_DIR)
    sys.exit(0)

for fname in files:
    path = os.path.join(MODEL_DIR, fname)
    print('Processing', path)
    try:
        # Try joblib first
        try:
            obj = joblib.load(path)
            loader = 'joblib'
        except Exception:
            with open(path, 'rb') as f:
                obj = pickle.load(f)
            loader = 'pickle'
        # Re-save with joblib if available, fallback to pickle
        tmp_path = path + '.tmp'
        try:
            joblib.dump(obj, tmp_path, compress=0)
            os.replace(tmp_path, path)
            saver = 'joblib'
        except Exception:
            with open(tmp_path, 'wb') as f:
                pickle.dump(obj, f, protocol=pickle.HIGHEST_PROTOCOL)
            os.replace(tmp_path, path)
            saver = 'pickle'
        print(f"Re-saved {fname} (loaded with {loader}, saved with {saver})")
    except Exception as e:
        print(f"Failed to re-save {fname}:", e)
        traceback.print_exc()

print('Done')
