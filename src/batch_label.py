import os, json, time, hashlib, argparse, asyncio, aiohttp, yaml
from pathlib import Path
from llm_client import LLMClient

def cache_key(text, codebook_hash, model):
    return hashlib.sha256((text + codebook_hash + model).encode()).hexdigest()

async def label_item(client, item, codebook, temperature=0, top_p=1.0):
    messages = [
        {"role":"system","content":"You are a meticulous coder. Follow the codebook exactly."},
        {"role":"user","content":{
            "instruction": "Given the codebook and text, output JSON with fields: {id, label ∈ [pro, anti, neutral, unsure], confidence ∈ [0,1], rationale}. If rules conflict or evidence is insufficient, emit 'unsure' with 0.4–0.6 confidence.",
            "codebook": codebook,
            "text": item["text"],
            "id": item["id"]
        }}
    ]
    return await client.chat(messages, temperature=temperature, top_p=top_p)

async def worker(rows, codebook, out_path, tps):
    Path(out_path).parent.mkdir(parents=True, exist_ok=True)
    codebook_hash = hashlib.sha256(json.dumps(codebook, sort_keys=True).encode()).hexdigest()
    client = LLMClient()
    model = client.model
    cache_dir = Path("logs/cache"); cache_dir.mkdir(parents=True, exist_ok=True)

    async with aiohttp.ClientSession():  # session handled inside client
        for i, row in enumerate(rows, 1):
            key = cache_key(row["text"], codebook_hash, model)
            cache_file = cache_dir / f"{key}.json"
            if cache_file.exists():
                result = json.loads(cache_file.read_text(encoding="utf-8"))
            else:
                result = await label_item(client, row, codebook)
                cache_file.write_text(json.dumps(result, ensure_ascii=False), encoding="utf-8")
                await asyncio.sleep(1.0 / max(tps, 0.1))

            with open(out_path, "a", encoding="utf-8") as f:
                f.write(json.dumps({"id": row["id"], "raw": result}) + "\n")

def read_jsonl(path):
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                yield json.loads(line)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Path to JSONL with fields id,text")
    parser.add_argument("--codebook", required=True, help="Path to YAML codebook")
    parser.add_argument("--out", required=True, help="Output JSONL path")
    parser.add_argument("--tps", type=float, default=2.0, help="Target requests per second")
    args = parser.parse_args()

    rows = list(read_jsonl(args.input))
    codebook = yaml.safe_load(open(args.codebook, "r", encoding="utf-8"))
    asyncio.run(worker(rows, codebook, args.out, args.tps))
