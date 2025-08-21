# AI Research Ops Starter (for Computational Social Science)

This repo is a **drop‑in starter** to run AI in serious research settings—traceable, auditable, and fast.
Language is kept plain, steps are short, and everything is **ready to paste** into your workflow.

**Four tracks:** Search · Scaffold · Scale · Sentinel  
Use them separately or end‑to‑end. Docs publish to GitHub Pages (in `docs/`).

---

## Quickstart

1. **Use this template**: copy the folder structure below, or download this repo as a ZIP.
2. **Create your GitHub repo** and push this content.
3. **Enable Pages**: *Settings → Pages → Build and deployment → Deploy from branch*, choose your default branch and `/docs` folder.
4. Edit `docs/index.md` and `README.md` to reflect your project. Keep prompts in `prompts/` and logs in `logs/ai/`.
5. When labeling at scale, open `scripts/batch_label.py` and connect it to your preferred LLM provider (one small function).

---

## Repository layout

```
project/
  README.md
  LICENSE
  CITATION.cff
  .gitignore
  docs/
    index.md
    search.md
    scaffold.md
    scale.md
    sentinel.md
  prompts/
    SEARCH_generic.yaml
    SCAFFOLD_generic.yaml
    LABEL_construct_v1.yaml
  codebooks/
    construct_v1.md
  scripts/
    batch_label.py
    irr_alpha.py
    irr_check.R
  notes/
    templates/
      ai_interaction_log.yaml
      weekly_summary.md
      research_charter.md
      datasheet_template.md
      model_card_template.md
  data/
    raw/.keep
    processed/.keep
  logs/
    ai/.keep
```

**Minimal weekly routine**
- Use `docs/search.md` + `prompts/SEARCH_generic.yaml` to gather seeds with citations.
- Run the **Scaffold loop** once per idea; save the one‑pager from `docs/scaffold.md`.
- Pilot labeling with 50–100 items, check **Krippendorff’s α** via `scripts/irr_alpha.py`, then scale.

**Disclosure / provenance**
- Every meaningful AI interaction gets a **3‑line log** using `notes/templates/ai_interaction_log.yaml`.
- Keep weekly summaries in `logs/ai/` with the template provided.

---

## License and attribution

- Code and templates are released under the **MIT License** (`LICENSE`).
- Cite this starter in your work with the provided `CITATION.cff` (or adapt to your lab format).
