# 《铁血残明》Cangjie Pipeline State

- Stage 0 source audit: **COMPLETE**
- Stage 0 Adler whole-book (available EPUB 1–534): **COMPLETE / USER CONFIRMED**
- Stage 0 user confirmation: **CONFIRMED (user replied “继续”)**
- Stage 1 five-extractor candidates: **250 RAW SAVED (56/57/62/39/36); SOURCE-COVERAGE GATE OPEN — NOT FULLY COMPLETE**
- Stage 1.5 triple verification: NOT STARTED
- Stage 1.6 promotion gate: NOT STARTED
- Stage 2 RIA++: NOT STARTED
- Stage 3 Zettelkasten: NOT STARTED
- Stage 4 pressure tests: NOT STARTED
- Stage 5 compile/delivery: NOT STARTED
- V10 Runtime/Canon modified: **false**

Source: `SOURCE_AUDIT.md`. Current EPUB is a *partial snapshot*, ending with chapter 534 body and a chapter 535 title stub; no end-of-book claim permitted.

Checkpoint policy: upload after each finished verifiable stage/sub-stage and verify by GitHub back-read. Never upload full copyrighted EPUB/source extraction.

## Stage 0 deliverables

- `SOURCE_AUDIT.md` — EPUB scope, source hash, chapter numbering faults, paratext boundaries
- `BOOK_OVERVIEW.md` — 6-part structural reading, 12 provisional interpretive claims, critical/limitations, 18 independent tasks
- Next strict action: **complete full semantic coverage for framework/principle and adjudicate remaining gaps**, then verify Stage 1 coverage; do not prematurely enter Stage 1.5.
- EPUB remains a partial snapshot; no author's final-ending claims
- V10 Runtime/Canon changes: none

## Stage 1 checkpoint

- Stage 0 confirmed by user's “继续”.
- Five raw candidate files uploaded, back-read and matched on content/IDs:
  - frameworks 56
  - principles 57
  - cases 62
  - counter-examples 39
  - glossary 36
- total: 250 raw items (NOT tri-verified).
- candidate chapter anchors: 70 distinct physical EPUB chapter records (+ 1 reader-compiled timeline).
- 18 Stage 0 tasks have raw membership; TX-T17 now has multiple independently locatable appendix/annotation examples, but historical provenance is still not externally corroborated.
- Scope caveat: mechanical full-text indexing + focused source close-reads `!=` complete semantic full-scan required by framework/principle extractors.
- stage documents:
  - `STAGE1_SUMMARY.md`
  - `STAGE1_COVERAGE_AUDIT.md`
  - `candidates/{frameworks,principles,cases,counter-examples,glossary}.md`
- Stage 1.5 V1/V2/V3: NOT STARTED.
- Runtime/Canon modifications: NONE.

Next: close the Stage 1 semantic-coverage gap or mark unresolved source tasks honestly before Stage 1.5.

## 2026-10-08 Stage 1 expansion

- Added 43 new source-anchored raw items: now 197 total.
- 197 / 197 raw IDs unique, source locators present, quotes literal in same EPUB physical record, task IDs nonempty.
- Repaired 61 old quotes that normalized across line breaks but were not verbatim contiguous.
- `STAGE1_T17_PROVENANCE_REVIEW.md`: 84 annotated EPUB physical records (83 in chapters + 1 reader-prepared timeline), with type classification and 7 examples.
- `STAGE1_CHAPTER_SCAN_MATRIX.tsv`: 532 physical story chapter headings (including duplicates and missing numbers), machine topic scan / review state; **not 532 semantic close-reads**.
- `STAGE1_COVERAGE_UPDATE_2026-10-08.md`: newest coverage audit and remaining hard-gate limits.
- Full semantic framework/principle scanning is still **incomplete**, Stage 1.5 is **NOT STARTED**.
- V10 Runtime / Canon: NOT MODIFIED.


## Stage 1 semantic batch 01 — 2026-10-08

- Review: 31 targeted semantic chapter-passage reviews, focusing on previously sparse intervals.
- Added 25 raw source-bound items, after explicit duplicate/reuse checks.
- Current raw pool: **222** (49 frameworks, 51 principles, 54 cases, 35 counterexamples, 33 glossary).
- Candidate-anchored physical novel chapters: **61**; separately 1 reader compilation timeline.
- 222/222 unique IDs, valid EPUB physical locator, verbatim short quote matched in source record, and task mapping present in local validation.
- `STAGE1_SEMANTIC_BATCH_01.md`: full per-chapter audit and candidate-gain/duplicate rationale.
- `STAGE1_CHAPTER_SCAN_MATRIX.tsv`: regenerated source-anchoring counts, with 31 targeted-passage review flags.
- No claim of all 532 physical chapter entries semantically close-read.
- **Stage 1 source-coverage hard gate: OPEN; Stage 1.5: NOT STARTED.**
- Runtime / Canon changes: **NONE**.


## Stage 1 semantic batch 02 — 2026-10-08

- Continuous EPUB physical chapter window: Text/chapter7.html to Text/chapter38.html (story chapters 1–32).
- Review flags: 5 whole-chapter semantic reads (1,2,3,16,17) + 27 targeted-passage reviews. Partial reading must not be counted as full.
- New source-bound candidates: 15 → **237 raw total** (53 frameworks / 55 principles / 58 cases / 37 counterexamples / 34 glossary).
- New capabilities of interest: family economic ethics vs protagonist desire; locally invalid modern slogans as dialogue comedy; independent neighborhood women's social reporting; publicly visible political praise changing a direct superior's immediate task allocation but not his long-term resentment.
- Discovered and repaired **12 preexisting field-type mismatches**:
  - ce24–ce31 (warning_signs/bound_to/task_ids)
  - g27–g30 (key_distinction/task_ids)
- Strict schema validator: 237 unique IDs, valid source locator + literal short quote, 18 task IDs all properly typed, case bound_to/example_kind and counterexample warning_signs/bound_to well-formed, **0 errors**.
- Previous audit claiming all task mappings valid from "nonempty" alone is superseded for schema correctness.
- Artifacts:
  - `STAGE1_SEMANTIC_BATCH_02.md`
  - `STAGE1_SCHEMA_REPAIR_AUDIT.json`
  - updated five `candidates/*.md`
  - updated `STAGE1_CHAPTER_SCAN_MATRIX.tsv`
- **Stage 1 semantic hard gate: OPEN; Stage 1.5: NOT STARTED.**
- Runtime v0.2 / Canon: NOT MODIFIED.

## Repeatable QA gate

- Validator: `QA/validate_stage1_candidates.py`, available without copyrighted EPUB; supports optional private `--source-jsonl` literal quote check.
- Workflow: `.github/workflows/tiexue-stage1-schema.yml`.
- GitHub Actions run `37771968995`: **SUCCESS** on public repository schema-only validation.
- Distinction: CI success = structured raw candidate fields valid, **not** whole-source semantic coverage or Stage 1.5 tri-verification.
- Next chapter queue: `STAGE1_REVIEW_BACKLOG.md`, start at continuous chapters 33–80 without revisiting the existing B01/B02 passages except when evidence conflicts.


## Stage 1 semantic batch 03 — continuous chapters 33–80

- Book chapter span: 33–80 = **48** source chapters (physical `Text/chapter39.html`–`Text/chapter86.html`).
- Six complete-text reviews: chapters 34, 43, 55, 61, 68, 74.
- Other **42** chapters: targeted scene/excerpt reading, NOT full-chapter semantic reading.
- Added 13 raw entries: 3 framework, 2 principle, 4 case, 2 counterexample, 2 glossary.
- Raw candidate total: **250** (56/57/62/39/36).
- Local schema + literal quote validator: **PASS; 0 issues**, source quotes checked against original EPUB physical records.
- GitHub Actions schema-only check on updated candidate files: **SUCCESS**, run `37773419996`. This never replaces the private-source quote check or source semantics.
- Current distinct source paths: 71 = 70 story-physical sources + 1 reader-produced timeline (separate evidence category).
- Audit: `STAGE1_SEMANTIC_BATCH_03.md`; chapter reading status updated in `STAGE1_CHAPTER_SCAN_MATRIX.tsv`.
- Next continuous first-pass range: **chapters 81–129**. Later revisit chapters flagged targeted-only for full natural-block framework/principle verification.
- **Stage 1 hard gate remains OPEN**; Stage 1.5 V1/V2/V3 **NOT STARTED**.
- V10 Runtime/Canon modifications: **NONE**.
