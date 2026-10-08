# V10 Wanming Candidate Blind / Non-Regression Protocol v0.1

## Purpose

Decide whether the 15 Wanming-derived V10 candidates should actually enter:
- `RUNTIME/CORE.md`,
- `V10_SKILL.md` / Canon research protocol,
- reference/tool layer only,
- or be rejected as redundant.

This gate must not be run in the same conversation that designed the candidates.

## Required environment

Use **two separate Temporary Chats / Unpersonalized sessions** with:
- no Memory;
- no Custom Instructions carrying V10 context;
- no prior V10 conversation;
- same model/configuration if possible.

Do not give either tested session the scoring file or prior candidate-test results.

## Arm A — Baseline

Provide only:
1. `V10_SKILL.md`
2. `RUNTIME/CORE.md`
3. `CANON/MASTER_SETTING.md`
4. `CURRENT/PROJECT_STATE.md`
5. `INDEX/INDEX.md`
6. `TESTS/BLIND_TESTS.md`
7. `TESTS/WANMING_CANDIDATE_BLIND_TESTS.md`

Instructions:
- execute normal V10 recovery;
- answer standard 40;
- then answer candidate 20;
- no outside project context.

## Arm B — Candidate

Provide the same files plus:
8. `RESEARCH/V10_CANDIDATES/WANMING_CANDIDATE_OVERLAY.md`

Instructions:
- execute normal V10 recovery first;
- then treat Overlay as a **test-only lower-authority candidate layer** under Canon and Runtime;
- answer the same standard 40 and candidate 20.

## Scoring

### Gate 1 — Standard V10 non-regression

Historical strict baseline:
- 2026-10-07 Test A = **40/40**
- hidden adversarial holdout = **60/60**

For candidate promotion:
- Arm B standard 40 should remain **40/40**.
- 39/40 triggers mandatory review; promotion may continue only if the miss is clearly unrelated to the Overlay and no hard-setting/core-principle error occurred.
- <=38/40 = candidate overlay FAIL / repair required.
- any fatal Canon error = FAIL regardless of total.

### Gate 2 — Candidate-specific 20

Each question scored 0 / 1 / 2 using the hidden evaluator rubric.

- 2 = correct decision + candidate-level executable reasoning/boundary
- 1 = directionally correct but vague/incomplete
- 0 = wrong, over-applied, or violates existing V10

Pass threshold:
- **38/40**
- mandatory questions 2, 6, 13, 15, 19, 20 may not score 0.

### Gate 3 — A/B incremental value

Compare Arm A and Arm B on the 20 candidate tests.

For each candidate:
- if Arm A already gives full-quality executable answers on every mapped probe and Arm B adds no meaningful precision, the candidate may be **REDUNDANT / REFERENCE ONLY** even if it passes;
- if Arm B improves one or more mapped probes without degrading standard V10 tests, candidate receives positive promotion evidence;
- if Arm B causes template overuse, bureaucracy, slower prose or loss of character life, candidate fails or must be narrowed.

Overall:
- Arm B total must be >= Arm A total;
- no anti-overuse probe may get worse;
- prose test #20 must be equal or better in scene quality, not merely more mechanistic.

## Gate 4 — Candidate disposition

After scoring, assign each candidate one result:

- `PROMOTE_MERGE` — merge compactly into an existing Runtime section;
- `PROMOTE_NEW` — genuinely missing default author behavior;
- `PROMOTE_PROTOCOL` — add to V10_SKILL / Canon research procedure, not CORE;
- `REFERENCE_ONLY` — useful evidence/tool but Runtime already performs it;
- `REPAIR_RETEST` — useful but causes regression/overuse;
- `REJECT` — no reliable V10 value.

## Candidate-to-question mapping

- S01 actionability → Q1
- S02 power-contract → Q1, Q4
- C01 organization-learning → Q3
- C02 scale-restructure → Q2
- C03 information-triage → Q5
- C04 delegated-execution → Q4
- S03 adaptive-world → Q6
- C08 resource-power-rebalance → Q7
- S06 structural-conflict → Q8, Q18
- C05 micro-life → Q9, Q20
- S04 macro-micro → Q10, Q19
- S05 multi-POV → Q11
- C06 aftermath → Q12, Q17
- C07 institution-transfer → Q13, Q14
- P01 source-conflict protocol → Q15, Q16

## Important

Current conversation results from Cluster A–D are **open-test evidence only** and must not be shown to the blind tested sessions.

Only after this protocol passes may the repository edit Runtime/V10_SKILL for these candidates.
