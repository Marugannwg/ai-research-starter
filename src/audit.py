import json, time, uuid
from pathlib import Path

def record_session(task, prompt, model, params, outputs_path):
    Path("logs/sessions").mkdir(parents=True, exist_ok=True)
    rec = {
        "id": str(uuid.uuid4()),
        "ts": time.strftime("%Y-%m-%dT%H:%M:%S"),
        "task": task, "model": model, "params": params,
        "prompt": prompt, "outputs": outputs_path
    }
    with open(f"logs/sessions/{rec['ts']}_{rec['id']}.json", "w", encoding="utf-8") as f:
        json.dump(rec, f, ensure_ascii=False, indent=2)
    return rec
