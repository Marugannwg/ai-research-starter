# Search

**Goal:** Find credible seeds fast, document the trail, and keep only what you can verify.

**Procedure**
1. Open a fresh chat named `SEARCH_[topic]_[date]`.
2. Paste the prompt from `prompts/SEARCH_generic.yaml`; specify venues and date range.
3. Require a CSV (title, year, venue, DOI/URL, method, key finding, why it matters).
4. Import results into Zotero; verify DOIs; check for retractions; tag themes.
5. Save the CSV and your triage notes to `logs/ai/`.

**What “good” looks like**
- Each item has a **working DOI/URL** and a one‑sentence **why it matters** in *your words*.
- Retractions/Expressions of Concern flagged.
- 2–3 **hubs** identified for forward/backward snowballing.

**Artifacts to save**
- `prompts/SEARCH_generic.yaml` (your edited version)
- `logs/ai/search_[date].md` (paste CSV + notes)
- `references/library.bib` (Zotero export)

Keep it boring and traceable.
