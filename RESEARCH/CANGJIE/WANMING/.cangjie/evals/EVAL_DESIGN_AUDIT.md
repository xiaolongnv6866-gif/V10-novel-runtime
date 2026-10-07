# Stage 4A Eval Design Audit

## Pre-run correction

The first draft of `output-cases.json` checked only one capability-specific result field per normal case. That was rejected **before any test execution** because it could pass on format while omitting most of the card's E contract.

The suite was strengthened to require:

- `status=complete`
- exact `capability`
- 3–5 capability-specific result fields derived from the Stage 2 E output contract

Boundary cases now require:

- exact `capability`
- `status=needs_input|out_of_scope`
- `missing`
- `boundary_reason`

Prompts no longer reveal the capability-specific expected result keys.

## Test-only convention

JSON + English `snake_case` is an evaluation-harness convention for deterministic assertions. It is **not** attributed to 《晚明》 and does not change the capability semantics.

No test had been run before this correction, so there is no post-result threshold changing.


## Pre-run correction 2 — edge_case scorer semantics

The upstream `run_trigger_evals.py` scores `edge_case` the same as a non-trigger case. The initial seven promoted suites used `edge_case` for scenarios where the capability itself should activate and enforce its own B/E boundary.

Because **no trigger run had started**, those seven cases were changed from `edge_case` to `should_trigger` before execution. This avoids rewarding non-activation when the desired behavior is “activate and correctly refuse/limit within the capability.”

This is a scorer-semantics correction, not a post-result expectation change.


## Pre-run correction 3 — source-conflict true negative

The initial `sc-neg-01` asked the capability to decide a source conflict without source text. That is actually a valid boundary invocation of `source-conflict-canon`: the capability should activate and stop rather than silently use model memory.

Before any trigger execution, the case was replaced with a genuinely unrelated prose-writing request. The separate boundary case still covers unresolved source conflict behavior.


## Post-run test repair — three sufficient-information boundary cases

The first 40-case run scored 37/40. The three failures were:

- `scale_restructure_boundary`
- `limited_info_multipov_boundary`
- `aftermath_settlement_boundary`

All three outputs contained a valid capability-level negative decision with sufficient input:
- no observed scale bottleneck → do **not** add management layers;
- redundant POVs with identical information/action → merge/remove them;
- no persistent aftermath state change → do **not** force a multi-chapter aftermath.

The frozen assertion incorrectly required every boundary case to return only `needs_input|out_of_scope`. That contradicts the Stage 2 E/B contracts, where a capability may validly activate and return a completed “no change / compress / remove” decision.

Per Cangjie Stage 4 “fix skill vs fix test”, this is a **test defect**, not a capability defect. Assertions were repaired to require `status=complete` plus the capability-specific negative-decision fields. The already-produced outputs were not changed before rescoring.
