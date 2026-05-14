# Shim to expose FastAPI app when running uvicorn from project root
# Import the backend module and expose its FastAPI `app` as the top-level symbol
from transit_dashboard.backend import main as backend_main

app = backend_main.app
