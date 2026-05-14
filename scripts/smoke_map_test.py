import json
from pathlib import Path

# Ensure project root is on sys.path for imports
import sys
from pathlib import Path
sys.path.insert(0, str(Path.cwd()))

# Import backend merged feed function and frontend fig builder
from transit_dashboard.backend import main as backend_main
from transit_dashboard.frontend import app as frontend_app

OUT_DIR = Path("transit_dashboard/tests/snapshots")
OUT_DIR.mkdir(parents=True, exist_ok=True)
OUT_FILE = OUT_DIR / "live_map_snapshot.json"

print('Fetching merged_feed (use_live=False)')
data = backend_main.get_merged_feed(use_live=False)
rows = data.get('rows', [])
print(f"Fetched rows: {len(rows)}; source: {data.get('source')}")

import pandas as pd

if not rows:
    print('No rows to plot; writing empty snapshot')
    fig_json = json.dumps({"error":"no_rows"})
else:
    df = pd.DataFrame(rows)
    # Ensure numeric lat/lon
    if 'latitude' in df.columns and 'longitude' in df.columns:
        df['latitude'] = pd.to_numeric(df['latitude'], errors='coerce')
        df['longitude'] = pd.to_numeric(df['longitude'], errors='coerce')
        df = df.dropna(subset=['latitude','longitude'])
    # Limit to 500 for safety
    if len(df) > 500:
        df = df.sample(500, random_state=42)
    fig = frontend_app.fig_vehicle_map_plotly(df)
    fig_json = fig.to_json()

OUT_FILE.write_text(fig_json, encoding='utf-8')
print('Wrote snapshot to', OUT_FILE)
