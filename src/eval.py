import argparse, json
from collections import Counter, defaultdict
from sklearn.metrics import classification_report, cohen_kappa_score

def read_jsonl(path):
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                yield json.loads(line)

def load_preds(path):
    pred = {}
    for row in read_jsonl(path):
        # Expect either row["label"] or row["raw"]["output"]["label"] depending on your LLM response
        label = None
        if "label" in row:
            label = row["label"]
        else:
            # Try a few common shapes
            try:
                label = row["raw"]["output"]["label"]
            except Exception:
                try:
                    label = row["raw"]["choices"][0]["message"]["content"].get("label")
                except Exception:
                    label = None
        pred[row["id"]] = label
    return pred

def load_gold(path):
    gold = {}
    for row in read_jsonl(path):
        gold[row["id"]] = row["label"]
    return gold

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--gold", required=True)
    ap.add_argument("--pred", required=True)
    args = ap.parse_args()

    gold = load_gold(args.gold)
    pred = load_preds(args.pred)

    y_true, y_pred = [], []
    for k, v in gold.items():
        if k in pred and pred[k] is not None:
            y_true.append(v)
            y_pred.append(pred[k])

    labels = sorted(list(set(y_true) | set(y_pred)))
    print("Labels:", labels)
    print(classification_report(y_true, y_pred, labels=labels, zero_division=0))
    print("Cohen's kappa:", cohen_kappa_score(y_true, y_pred))
