# AI for Computational Social Science — Search · Scaffold · Scale · Sentinel

*Premise:* The best AI should have better sense than you on a task—so instruct it to *ask when uncertain*. Your job is to design the loop, not abdicate the work.

This repo gives you a concrete, reproducible workflow to use LLMs for **serious** research—literature search, theory scaffolding, dataset labeling, and everyday research hygiene—without falling into “let AI do my homework.”

---

## Repo layout
```
ai-research-guide/
├── README.md
├── LICENSE
├── .gitignore
├── requirements.txt
├── Makefile
├── data/
│   ├── raw/        # never commit PII; .gitkeep only
│   ├── interim/
│   └── processed/
├── notebooks/      # optional; keep outputs out of git
├── src/
│   ├── llm_client.py     # thin async client with logging
│   ├── batch_label.py    # JSONL in -> JSONL out
│   ├── audit.py          # session logging
│   └── eval.py           # accuracy/F1/kappa + diagnostics
├── prompts/        # prompt patterns
├── codebooks/      # labeling rules w/ versioning
├── logs/
│   ├── sessions/   # json records of AI interactions
│   └── decisions/  # daily digests of what changed
├── ethics/         # AI use statement, PII/IRB notes
├── references/     # library.bib + PRISMA log
└── templates/      # daily note, schemas, citation
```

---

## Quickstart
1. **Setup**
   ```bash
   python -m venv .venv && source .venv/bin/activate
   pip install -r requirements.txt
   ```

2. **Secrets**  
   Create `.env` with your API credentials (not committed). See `src/llm_client.py` for expected env vars.

3. **First run**
   - Use `prompts/search.md` to design queries; save candidates to `references/` and update `references/prisma_log.md`.
   - Start a design chat with `prompts/scaffold.md`; paste the final one‑pager into `logs/decisions/YYYY-MM-DD.md`.
   - Label 100 rows:
     ```bash
     python src/batch_label.py --input data/raw/texts.jsonl        --codebook codebooks/example_codebook.yaml        --out data/interim/labels_raw.jsonl
     python src/eval.py --gold data/raw/gold.jsonl --pred data/interim/labels_raw.jsonl
     ```

---

## The 4S Practice

### 1) Search — AI as supervised research librarian
- Constrain *journals/years/methods* up front. Demand **three** boolean queries tuned to different indices.
- Require structured output (DOI, year, venue, 1‑line rationale) in JSON.
- Keep receipts: export prompts + results to `logs/sessions/` and track keeps/rejects in a PRISMA‑style note.

**Prompt (`prompts/search.md`)** – returns queries, screening criteria, candidates, and gaps. You verify every DOI before inclusion.

### 2) Scaffold — compress understanding & test ideas
- Ask for a 250‑word distillation (constructs, causal claims, identification).
- Generate rival hypotheses + *discriminating evidence*.
- Request minimal viable designs (obs/exp), assumptions, likely biases, and diagnostics.
- End each session with a one‑page summary + 1‑week plan in `logs/decisions/`.

**Prompt (`prompts/scaffold.md`)** – senior‑tutor voice; ends with a single‑page summary you can paste into notes.

### 3) Scale — label/transform at volume with a codebook
- Write a tight YAML **codebook**: labels, definitions, decision rules, uncertainty policy, output schema.
- Run double‑pass (label → critique → final). Maintain a human‑labeled **gold set** and report accuracy/F1/kappa.
- Store provenance: model, temperature, prompt, codebook version, input hashes, timestamps.

**Scripts**: `src/batch_label.py` (async + cache hooks) and `src/eval.py` (metrics & disagreement analysis).

### 4) Sentinel — habits that keep you honest
- **Daily 15–25 min**: a decision digest (what AI changed), session logs, next actions.
- **Ethics & privacy**: never paste PII to third‑party models without IRB/DUA; redact or synthesize.
- **Reproducibility**: pin package versions; log model names and dates (models change silently).

See `ethics/ai_use_statement.md`, `ethics/pii_checklist.md` and `templates/` for drop‑in text.

---

## Makefile shortcuts
```make
make setup             # venv + install
make label input=... codebook=... out=...   # batch label
make eval  gold=... pred=...                # evaluate
```

---

## Resources (add to your syllabus)
- Wilson et al., *Good Enough Practices in Scientific Computing*.
- The Turing Way (reproducible research).
- PRISMA 2020 (systematic review reporting).
- Your department’s IRB/PII guidance.

---

## Final word
Use AI to **design**, **pressure‑test**, and **scale** your work. Keep receipts. Future‑you (and your reviewers) will ask how you got here—this repo answers cleanly.
