import json
from pathlib import Path
from datetime import datetime

RESULTS_PATH = Path("artifacts/results.json")

def save_result(product_name: str, result: dict) -> None:
    RESULTS_PATH.parent.mkdir(parents=True, exist_ok=True)

    if RESULTS_PATH.exists():
        existing = json.loads(RESULTS_PATH.read_text(encoding="utf-8"))
    else:
        existing = []

    existing.append({
        "timestamp": datetime.utcnow().isoformat(),
        "product_name": product_name,
        "result": result
    })

    RESULTS_PATH.write_text(
        json.dumps(existing, indent=2, ensure_ascii=False),
        encoding="utf-8"
    )