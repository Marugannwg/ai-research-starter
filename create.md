"""# Citing & Disclosing Generative AI in Research (2025)

**Bottom line:** be transparent, be specific, and keep humans accountable. Don’t list AI as an author; disclose meaningful use; cite AI **only** when you quote or closely paraphrase it; always cite the *sources* for facts.

---

## TL;DR — Rules of Thumb
- **Language polish only?** Treat like a grammar tool. Many venues say no disclosure is needed for *basic* copy editing, but disclose if AI rewrote substantive text or structure (e.g., in Acknowledgments/Methods). See Nature policy and exceptions.  
  Sources: [Nature portfolio policy](https://www.nature.com/nature-portfolio/editorial-policies/ai), [SpringerOpen policy](https://www.springeropen.com/get-published/editorial-policies), [ACM policy (exceptions)](https://www.acm.org/publications/policies/new-acm-policy-on-authorship), [IEEE guidance](https://www.ieee-ras.org/publications/guidelines-for-generative-ai-usage).
- **Search & fact‑checking?** Cite the *papers/data* you use, not the tool that helped you find them. Consider a brief note (“We used an AI assistant to surface literature; all sources were verified”).  
  Sources: [MLA on citing AI outputs](https://style.mla.org/citing-generative-ai/), [APA on citing AI outputs](https://apastyle.apa.org/blog/how-to-cite-chatgpt), [Duke Libraries on fake citations](https://blogs.library.duke.edu/blog/2023/03/09/chatgpt-and-fake-citations/).
- **Idea scaffolding / hypothesis generation?** No formal citation required, but best practice is a **disclosure** (who used what, roughly how). Keep prompts/logs for reproducibility.  
  Sources: [JAMA 2024 guidance](https://jamanetwork.com/journals/jama/fullarticle/2816213), [COPE position](https://publicationethics.org/guidance/cope-position/authorship-and-ai-tools).
- **Coding & analysis?** Acknowledge material AI assistance (tool/model, version/date). You’re responsible for correctness, licensing, and provenance.  
  Sources: [ACM authorship policy](https://www.acm.org/publications/policies/new-acm-policy-on-authorship), [IEEE policy](https://journals.ieeeauthorcenter.ieee.org/become-an-ieee-journal-author/publishing-ethics/guidelines-and-policies/submission-and-peer-review-policies/).
- **Scaling with agentic systems (many AI agents, synthetic data, mass annotation)?** Give a clear **Methods** description (models, prompts, codebook, supervision, QA, versions, seeds), release code/configs when possible, and include an **AI Usage** statement.  
  Sources: [AID Framework](https://crln.acrl.org/index.php/crlnews/article/view/26548/34482), [PLOS policy](https://journals.plos.org/plosone/s/ethical-publishing-practice).
- **Non‑negotiables**: AI **cannot be an author**. Human authors remain accountable for content, accuracy, originality, and citations.  
  Sources: [Nature editorial](https://www.nature.com/articles/d41586-023-00191-1), [ICMJE](https://www.icmje.org/recommendations/browse/roles-and-responsibilities/defining-the-role-of-authors-and-contributors.html), [Science editorial](https://www.science.org/doi/10.1126/science.adg7879), [JAMA 2023](https://jamanetwork.com/journals/jama/fullarticle/2807956).

---

## Scenario Playbook (with sample disclosures)

### 1) Language, tone, narrative optimization
**Do:** Use AI for light edits without citation; disclose if AI rewrote substantial passages or re‑organized sections. Never list AI as an author.  
**Sample disclosure:** “We used ChatGPT (GPT‑4, March 2025) for language clarity on the Introduction; authors reviewed and edited all suggested text.”  
Sources: Nature portfolio policy (copy‑editing need not be declared), ACM/IEEE exception vs. disclosure norms linked above.

### 2) AI‑assisted search / literature triage
**Do:** Cite the **original sources** only. Verify every claim to avoid hallucinated references. Optional one‑line note that an AI assistant was used for discovery.  
**Sample disclosure:** “An AI assistant was used to surface candidate literature; all sources were independently verified and are cited directly.”  
Sources: MLA/APA citation pages; Duke Libraries on fake citations (linked above).

### 3) Idea scaffolding / hypothesis generation
**Do:** Keep a lightweight log (date/tool/prompt/purpose). Disclose meaningful use in Methods/Acknowledgments. Consider appending representative prompts if they materially shaped the study.  
**Sample disclosure:** “AI assistance (GPT‑4) was used to brainstorm alternative hypotheses and refine study questions; final choices were made by the authors.”  
Sources: JAMA 2024; COPE; AID Framework.

### 4) Coding/analysis assistance
**Do:** Acknowledge tool, model/version, and scope (“suggested code for regression, authors validated and refactored”). Track provenance in code comments/README; check licenses.  
**Sample disclosure:** “GitHub Copilot (OpenAI Codex, May 2025) suggested portions of the analysis scripts; authors verified outputs and are responsible for all results.”  
Sources: ACM, IEEE policies.

### 5) Scaling with agentic AI (annotation, synthetic data, hypothesis loops)
**Do:** Treat this like a methods‑heavy contribution—document models, prompts, codebook, guardrails, calibration/QA, error rates, human‑in‑the‑loop checkpoints, versions, and seeds. Release pipeline/code where possible; include a structured **AI Usage** statement (see below).  
**Sample disclosure:** “We orchestrated 1,000 GPT‑4 agents to apply a predefined codebook (v1.2) to 2M posts with human auditing (10% double‑coding; κ = 0.82). Prompts/configs and logs are in `/agents/`.”  
Sources: AID Framework; PLOS ethics; IEEE reviewing cautions.

> **Warning:** Don’t run confidential manuscripts through public AIs during peer review.  
> Source: [IEEE PSPB 8.2.1.C.5](https://www.ieee-ras.org/publications/guidelines-for-generative-ai-usage).

---

## Minimal “AI Usage” Statement (AID‑style)

Include where your venue expects it (Methods, Statements & Declarations, or Acknowledgments).

> **AI tools used:** ChatGPT‑4 (OpenAI, March 2025) for language clarity in the Introduction; GPT‑4 agents (OpenAI) for first‑pass qualitative coding using our codebook v1.2; GitHub Copilot (May 2025) suggested snippets for data wrangling. **Human oversight:** All AI outputs were reviewed/edited by the authors. **Reproducibility:** Prompts, configs, and representative logs are provided in `supplement/ai/` with model/version and timestamps. No confidential or under‑review manuscripts were processed by public AIs.

AID references: [CR&L News article](https://crln.acrl.org/index.php/crlnews/article/view/26548/34482) | [arXiv preprint](https://arxiv.org/abs/2408.01904).

---

## Policy Snapshot (quick links)

- **No AI authorship; disclose meaningful use:**  
  Nature editorial: “Tools such as ChatGPT… ground rules” → https://www.nature.com/articles/d41586-023-00191-1  
  **Nature portfolio policy (LLMs)** → https://www.nature.com/nature-portfolio/editorial-policies/ai  
  **ICMJE** (roles & authorship; disclose use; humans responsible) → https://www.icmje.org/recommendations/browse/roles-and-responsibilities/defining-the-role-of-authors-and-contributors.html  
  **Science** editorial → https://www.science.org/doi/10.1126/science.adg7879  
  **JAMA 2023 guidance** → https://jamanetwork.com/journals/jama/fullarticle/2807956 | **JAMA 2024 update** → https://jamanetwork.com/journals/jama/fullarticle/2816213  
  **COPE** position → https://publicationethics.org/guidance/cope-position/authorship-and-ai-tools

- **Publisher/journal examples:**  
  **ACM** policy (disclose; grammar‑tool exceptions) → https://www.acm.org/publications/policies/new-acm-policy-on-authorship  
  **IEEE** (disclose AI‑generated content; no public AI for peer‑review text) → https://journals.ieeeauthorcenter.ieee.org/become-an-ieee-journal-author/publishing-ethics/guidelines-and-policies/submission-and-peer-review-policies/ and https://www.ieee-ras.org/publications/guidelines-for-generative-ai-usage  
  **PLOS ONE** ethics (AI in peer review & disclosure) → https://journals.plos.org/plosone/s/ethical-publishing-practice  
  **Elsevier** journal policy hub → https://www.elsevier.com/about/policies-and-standards/generative-ai-policies-for-journals  
  **SpringerOpen** (copy‑editing need not be declared) → https://www.springeropen.com/get-published/editorial-policies

- **Style manuals (how to cite AI when you *quote it*):**  
  **APA** → https://apastyle.apa.org/blog/how-to-cite-chatgpt | **MLA** → https://style.mla.org/citing-generative-ai/

- **Why verification matters (hallucinations):**  
  Duke Libraries (fake citations) → https://blogs.library.duke.edu/blog/2023/03/09/chatgpt-and-fake-citations/  
  arXiv study on fabricated references → https://arxiv.org/abs/2309.09401

---

## Replicability Checklist (copy‑paste into your repo)
- **Models & versions:** model name, provider, version/date hashes.  
- **Prompts & configs:** prompts, system messages, temperature/seed, codebook version.  
- **Scope of use:** which sections/tasks AI touched (writing, coding, annotation…).  
- **Human oversight:** review/edit protocol; sampling for QA; error rates.  
- **Data governance:** privacy, consent, and whether any under‑review text was processed.  
- **Artifacts:** code, logs, and minimal examples in `supplement/ai/`.

---

## Attribution vs. Citation (one‑liner)
- **Citation** = you quote/closely paraphrase the AI’s output → cite APA/MLA style.  
- **Attribution/disclosure** = you used AI as a tool that influenced *process* → add a clear statement in Methods/Acknowledgments (AID‑style).

---

*Maintained for interdisciplinary, forward‑looking researchers (last updated: Aug 2025).*  
"""

