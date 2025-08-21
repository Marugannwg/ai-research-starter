# Provider-agnostic batch labeling script.
# Reads data/raw/texts.csv with columns: id,text
# Emits logs/ai/run_<timestamp>.jsonl and data/processed/labels_v1.csv
# To use: implement the single function `call_llm()` to connect to your provider.

import csv, json, time, os, hashlib
from pathlib import Path
from typing import Dict, Any, Iterable

INPUT_CSV = Path("data/raw/texts.csv")
OUTPUT_JSONL = Path(f"logs/ai/run_{int(time.time())}.jsonl")
OUTPUT_CSV = Path("data/processed/labels_v1.csv")
PROMPT_FILE = Path("prompts/LABEL_construct_v1.yaml")

def sha8(s: str) -> str:
    return hashlib.sha256(s.encode()).hexdigest()[:8]

def load_prompt() -> str:
    return PROMPT_FILE.read_text(encoding="utf-8")

def read_items(path: Path) -> Iterable[Dict[str, str]]:
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            yield {"id": row["id"], "text": row["text"]}

# ---- FILL THIS IN ----------------------------------------------------------
def call_llm(text: str, system_prompt: str) -> Dict[str, Any]:
    """
    Connect to your LLM provider here.
    Return a dict with keys: label (POS|NEG|UNSURE), rationale (<=50 chars).
    Keep temperature low (e.g., 0.1) for consistency.

    Example shape to return:
    return {"label": "POS", "rationale": "Direct condemnation present"}
    """
    # TODO: Replace this stub with your provider’s API call.
    # For now, default to UNSURE so you can test the pipeline end-to-end.
    return {"label": "UNSURE", "rationale": "stub"}
# ----------------------------------------------------------------------------

def main():
    system_prompt = load_prompt()
    codebook_hash = sha8(system_prompt)
    OUTPUT_JSONL.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_CSV.parent.mkdir(parents=True, exist_ok=True)

    rows = list(read_items(INPUT_CSV))
    out_rows = []
    with open(OUTPUT_JSONL, "w", encoding="utf-8") as jf:
        for r in rows:
            y = call_llm(r["text"], system_prompt)
            rec = {
                "id": r["id"],
                "label": y.get("label", "UNSURE"),
                "rationale": y.get("rationale", ""),
                "model": os.getenv("LLM_MODEL", "provider/model@version"),
                "temperature": float(os.getenv("LLM_TEMPERATURE", "0.1")),
                "seed": int(os.getenv("LLM_SEED", "0")),
                "codebook": codebook_hash,
                "ts": time.time(),
            }
            jf.write(json.dumps(rec) + "\n")
            out_rows.append(rec)

    # also write a CSV summary for convenience
    with open(OUTPUT_CSV, "w", newline="", encoding="utf-8") as cf:
        writer = csv.DictWriter(cf, fieldnames=["id","label","rationale","model","temperature","seed","codebook","ts"])
        writer.writeheader()
        writer.writerows(out_rows)

    print(f"Wrote {len(out_rows)} records to {OUTPUT_JSONL} and {OUTPUT_CSV}")

if __name__ == "__main__":
    main()
