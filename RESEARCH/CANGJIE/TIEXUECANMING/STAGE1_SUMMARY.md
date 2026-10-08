# 《铁血残明》 Cangjie Stage 1 — Candidate Extraction Checkpoint

> Date: 2026-10-08  
> Stage status: **CANDIDATE POOL SAVED / SOURCE-COVERAGE GATE OPEN**  
> This is an auditable checkpoint, not Stage 1.5 tri-verification.

## User confirmation

Stage 0 user confirmed by replying **“继续”**. Stage 1 was then started under the original Cangjie 2.5 method's **serial fallback** for environments without Task sub-agents.

## Five extractor deliverables

| Original extractor | Repository artifact | Raw entries |
|---|---|---:|
| framework | [frameworks.md](./candidates/frameworks.md) | 35 |
| principle | [principles.md](./candidates/principles.md) | 35 |
| case | [cases.md](./candidates/cases.md) | 35 |
| counter-example | [counter-examples.md](./candidates/counter-examples.md) | 23 |
| glossary | [glossary.md](./candidates/glossary.md) | 26 |
| **Total** | | **154** |

All five files were uploaded and GitHub back-read. A byte mismatch initially observed in local-vs-repository Git blob SHA was traced to **the repository text read/upload path removing one final newline**, not to missing candidate content; line counts and 154 IDs agree. Short quote fields are limited to <=30 characters, with physical EPUB file locator.

## Coverage

- EPUB text span: complete bodies through chapter 534, 535 header-only.
- Mechanical index pass: all local chapter records.
- Evidence-anchored chapter records: **42** across the three covered volume ranges.
- Independent Stage 0 task map: **18 of 18 tasks have a raw candidate association**; this is **not evidence all 18 are substantively fulfilled**.
- T17: only one indirect raw candidate — **not enough**; needs targeted source-provenance work.
- Framework/principle full semantic scans: **incomplete**. Keyword indexing and a selection of chapter close-reads are not interchangeable with a complete chapter-by-chapter semantic pass.
- No sub-agents; five roles were executed sequentially and share a developer context. This may introduce correlated omissions.

## Qualitative discoveries so far

- The protagonist's low public status makes formal authority, informal favors, fiscal ability, and social face repeatedly collide.
- Language of righteousness or communal duty may conceal divergent motives; extractors must preserve contradiction rather than convert it to a universal cynical rule.
- A former subordinate or old friend changes behavior after rank changes; the new position does not reset old debts, resentments, or relationship intimacy.
- Institutional growth is constrained by people who interpret, avoid, or redirect instructions rather than faithfully executing a blueprint.
- Public narratives of merit, credit and official legitimacy can diverge from what participants actually experienced.
- Ordinary life, domestic bargaining, embarrassment, desire and humor remain part of long-form causality and cannot be reduced to organization charts.
- Chapters involving monetary or military institutions are **fictional narrative evidence**, not verified historical/current real-life operating manuals.

These are **candidate themes**, not confirmed independent transferable skills.

## Remaining hard work before Stage 1.5

1. Framework extractor: systematically inspect unreviewed chapter batches for a complete one-off framework and for multi-chapter causal dependencies.
2. Principle extractor: systematically inspect unreviewed prose and source notes, differentiate character opinions from consistent narrative rules.
3. Case/negative example/glossary: expand retrieval where a newly discovered method or term needs nearby cases and limits.
4. Task coverage: make a decision for TX-T17 and TX-T18 explicitly; absence of evidence is acceptable, false coverage is not.
5. Save a new audit with raw candidates added/merged, then enter Stage 1.5 V1/V2/V3. Stage 1.5 requires another user light confirmation before the Stage 1.6 promotion gate.

## Do not conclude

- 154 raw items are not 154 independent capabilities.
- 42 source chapters are not 534 semantically fully read chapters.
- Short literal quotation check is not proof that the proposed method is a valid inference.
- This EPUB does not contain the complete published ending.
- No Runtime/Canon promotion or modification has occurred.

Recovery:
- Read `PIPELINE_STATE.md`, this file, `STAGE1_COVERAGE_AUDIT.md`, `BOOK_OVERVIEW.md`, and five candidates.
- Reopen only missing coverage tasks; do not repeat already saved extraction without cause.
