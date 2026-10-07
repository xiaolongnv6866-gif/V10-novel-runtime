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
