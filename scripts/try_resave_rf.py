from pathlib import Path
import joblib
import pickle

MODEL_DIR = Path(r"C:\Users\Sharon\Documents\python_learning\netherapp\transit_dashboard\models")
RF = MODEL_DIR / 'model_RandomForest.pkl'

print('Attempting to load RF via joblib...')
try:
    m = joblib.load(RF)
    print('Loaded via joblib. Type:', type(m))
    print('Saving back via joblib...')
    joblib.dump(m, RF.with_suffix('.repack.pkl'), compress=0)
    print('Saved to', RF.with_suffix('.repack.pkl'))
except Exception as e:
    print('joblib load failed:', e)
    print('Trying pickle load...')
    try:
        with open(RF, 'rb') as f:
            m = pickle.load(f)
        print('Pickle load type:', type(m))
        joblib.dump(m, RF.with_suffix('.repack.pkl'), compress=0)
        print('Saved to', RF.with_suffix('.repack.pkl'))
    except Exception as e2:
        print('pickle load failed:', e2)
        # Attempt to salvage by treating file as XGBoost binary? skip

