# Stage 4C Actual Output Self-Test

> environment: **fallback_self_test**. The same main process executes the tasks; there is no independent clean sub-agent/context. This is a structural/output-contract regression test, not a blind comparative quality claim.

- planned output cases: 40
- completed: 40
- all current assertions passed: 40/40
- missing outputs: 0
- normal cases: 20
- boundary cases: 20

## Regression history

- first score: **37/40**
- three failures were test defects, not output edits: sufficient-information negative decisions were incorrectly forced to `needs_input|out_of_scope`
- repair rationale: `.cangjie/evals/EVAL_DESIGN_AUDIT.md`
- outputs reused unchanged for rescore
- current score: **40/40**

| case | result |
|---|---|
| actionability_ladder_normal | PASS |
| actionability_ladder_boundary | PASS |
| learning_loop_normal | PASS |
| learning_loop_boundary | PASS |
| scale_restructure_normal | PASS |
| scale_restructure_boundary | PASS |
| information_triage_normal | PASS |
| information_triage_boundary | PASS |
| power_contract_normal | PASS |
| power_contract_boundary | PASS |
| delegated_execution_normal | PASS |
| delegated_execution_boundary | PASS |
| decentralized_pilot_normal | PASS |
| decentralized_pilot_boundary | PASS |
| adaptive_opponents_normal | PASS |
| adaptive_opponents_boundary | PASS |
| success_constraints_normal | PASS |
| success_constraints_boundary | PASS |
| micro_life_dashboard_normal | PASS |
| micro_life_dashboard_boundary | PASS |
| macro_micro_rhythm_normal | PASS |
| macro_micro_rhythm_boundary | PASS |
| limited_info_multipov_normal | PASS |
| limited_info_multipov_boundary | PASS |
| aftermath_settlement_normal | PASS |
| aftermath_settlement_boundary | PASS |
| institution_transfer_pilot_normal | PASS |
| institution_transfer_pilot_boundary | PASS |
| repeat_by_delta_normal | PASS |
| repeat_by_delta_boundary | PASS |
| public_memory_recoding_normal | PASS |
| public_memory_recoding_boundary | PASS |
| relationship_multiaxis_normal | PASS |
| relationship_multiaxis_boundary | PASS |
| source_conflict_canon_normal | PASS |
| source_conflict_canon_boundary | PASS |
| resource_power_rebalance_normal | PASS |
| resource_power_rebalance_boundary | PASS |
| structural_conflict_normal | PASS |
| structural_conflict_boundary | PASS |

## Important limitation

The upstream methodology recommends `new_skill` vs `without_skill` in clean contexts. This host cannot provide an uncontaminated “without skill” context inside the same conversation, so no comparative improvement/non-inferiority claim is made. The completed run verifies that every active capability can execute one normal representative task and one boundary/missing-input task against the current audited E/B contract.

## Safety / source boundaries checked

- No output converts novel weapon/combat material into real-world operational instructions.
- `source-conflict-canon` refuses to invent a fixed exposition-length rule for NR01.
- Missing inputs are surfaced rather than silently fabricated.
