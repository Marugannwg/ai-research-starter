# Scale

**Goal:** Treat the LLM like an **instrument**: define it, test it, freeze it, run it, audit it.

**Pipeline**
- **Codebook v0** — definition, decision rules, edge cases, five gold examples per label.
- **Pilot (n≈50–100)** — two humans + LLM label independently; compute **Krippendorff’s α**.
- **Freeze v1** — save exact prompt, model name/version, temperature/seed, and codebook hash.
- **Run** — batch with low temperature; log JSONL; store outputs in `data/processed/`.
- **QA** — human spot‑check 5–10%; re‑estimate α; document failure modes.

Use `codebooks/construct_v1.md` and `prompts/LABEL_construct_v1.yaml` as your starting point.
Run `scripts/irr_alpha.py` on pilot data to compute α; aim for **≥ 0.80** (strong) or **≥ 0.667** (tentative).

Privacy: if inputs include PII/sensitive text, anonymize or use an approved/on‑prem model.
