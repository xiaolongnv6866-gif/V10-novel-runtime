# 《铁血残明》Cangjie Pipeline State

- Stage 0 source audit: **COMPLETE**
- Stage 0 Adler whole-book (available EPUB 1–534): **COMPLETE / USER CONFIRMED**
- Stage 0 user confirmation: **CONFIRMED (user replied “继续”)**
- Stage 1 five-extractor candidates: **222 RAW SAVED (49/51/54/35/33); SOURCE-COVERAGE GATE OPEN — NOT FULLY COMPLETE**
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
  - frameworks 49
  - principles 51
  - cases 54
  - counter-examples 35
  - glossary 33
- total: 222 raw items (NOT tri-verified).
- candidate chapter anchors: 61 distinct physical EPUB chapter records (+ 1 attached reader timeline).
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
