You are a research librarian. Task: design and (conceptually) run a literature search on:
[TOPIC]. Focus: [METHODS], population: [POP], outcome: [OUTCOME].

Constraints:
- Prioritize journals/sources: [LIST]
- Years: [YYYY–YYYY]
- Exclude: [WHAT TO AVOID]

Deliver:
1) THREE boolean queries tuned to (a) Google Scholar, (b) Crossref/DOI, (c) generic academic DB.
2) Brief recall vs precision trade-offs for each.
3) JSON candidates with DOI, title, year, venue, and 1‑line why-relevant.
4) Screening criteria and gaps to explore.

JSON output:
{
  "queries": {"scholar": "...", "crossref": "...", "generic": "..."},
  "screening_criteria": {"include": [...], "exclude": [...]},
  "candidates": [
    {"doi":"", "title":"", "year":2022, "venue":"", "why_relevant":"..."}
  ],
  "gaps_to_explore": ["..."]
}
If uncertain, ask targeted questions first. If a DOI is missing, state it explicitly.
