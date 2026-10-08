# V10 Wanming Candidate Blind Test Runbook v0.1

## Goal

Run a two-arm blind/non-regression test in two clean Temporary Chats.

Do not use this current development conversation for scoring.

## Arm A — Baseline

Use bundle:
`TESTS/bundles/V10-wanming-baseline-blind-v0.1.zip`

Start a new Temporary Chat / Unpersonalized session and send:

> 这是 V10 候选能力双臂盲测的 Baseline 组。请把自己视为完全不知道任何旧聊天内容，不使用 Memory、旧项目背景或外部资料。先读取压缩包中的 V10_SKILL.md，并严格执行其中完整恢复流程。恢复完成后，一次性回答 TESTS/BLIND_TESTS.md 的 1—40 题，再回答 TESTS/WANMING_CANDIDATE_BLIND_TESTS.md 的 1—20 题。不要寻找或推测评分标准；材料不足时明确写“依据不足”，不得凭模型记忆补写。最后给出不超过200字自检。

Save the full response.

## Arm B — Candidate

Use bundle:
`TESTS/bundles/V10-wanming-candidate-blind-v0.1.zip`

Start a second new Temporary Chat / Unpersonalized session and send:

> 这是 V10 候选能力双臂盲测的 Candidate 组。请把自己视为完全不知道任何旧聊天内容，不使用 Memory、旧项目背景或外部资料。先读取压缩包中的 V10_SKILL.md，并严格执行其中完整恢复流程。恢复完成后，再读取 RESEARCH/V10_CANDIDATES/WANMING_CANDIDATE_OVERLAY.md。该 Overlay 仅为测试候选层，权威低于 Canon 与现有 Runtime，不得修改 Canon/Runtime。然后一次性回答 TESTS/BLIND_TESTS.md 的 1—40 题，再回答 TESTS/WANMING_CANDIDATE_BLIND_TESTS.md 的 1—20 题。不要寻找或推测评分标准；材料不足时明确写“依据不足”，不得凭模型记忆补写。最后给出不超过200字自检。

Save the full response.

## Evaluator

Do **not** give tested sessions:
- `TESTS/WANMING_CANDIDATE_BLIND_SCORING.md`
- Cluster A–D plans/results
- prior V10 blind-test results
- this development chat

After both responses exist, return them to a normal V10 evaluation session and score using:
- `TESTS/WANMING_CANDIDATE_BLIND_PROTOCOL.md`
- `TESTS/WANMING_CANDIDATE_BLIND_SCORING.md`

## Promotion rule

No candidate may enter Runtime/V10_SKILL before:
- standard 40 non-regression gate;
- candidate 20 gate;
- A/B incremental-value comparison;
- anti-overuse checks;
- final merge/de-duplication review.
