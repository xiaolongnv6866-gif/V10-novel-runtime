# 《铁血残明》Cangjie Pipeline State

- Stage 0 source audit: **COMPLETE**
- Stage 0 Adler whole-book (available EPUB 1–534): **COMPLETE / USER CONFIRMED**
- Stage 0 user confirmation: **CONFIRMED (user replied “继续”)**
- Stage 1 five-extractor candidates: **154 RAW SAVED (35/35/35/23/26); SOURCE-COVERAGE GATE OPEN — NOT FULLY COMPLETE**
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
- Next strict action: **complete full semantic coverage for framework/principle + TX-T17**, then verify Stage 1 coverage; do not prematurely enter Stage 1.5.
- EPUB remains a partial snapshot; no author's final-ending claims
- V10 Runtime/Canon changes: none

## Stage 1 checkpoint

- Stage 0 confirmed by user's “继续”.
- Five raw candidate files uploaded, back-read and matched on content/IDs:
  - frameworks 35
  - principles 35
  - cases 35
  - counter-examples 23
  - glossary 26
- total: 154 raw items (NOT tri-verified).
- candidate chapter anchors: 42 distinct physical EPUB chapter records.
- 18 Stage 0 tasks have raw membership, but TX-T17 is substantively under-evidenced (one indirect record).
- Scope caveat: mechanical full-text indexing + focused source close-reads `!=` complete semantic full-scan required by framework/principle extractors.
- stage documents:
  - `STAGE1_SUMMARY.md`
  - `STAGE1_COVERAGE_AUDIT.md`
  - `candidates/{frameworks,principles,cases,counter-examples,glossary}.md`
- Stage 1.5 V1/V2/V3: NOT STARTED.
- Runtime/Canon modifications: NONE.

Next: close the Stage 1 semantic-coverage gap or mark unresolved source tasks honestly before Stage 1.5.
