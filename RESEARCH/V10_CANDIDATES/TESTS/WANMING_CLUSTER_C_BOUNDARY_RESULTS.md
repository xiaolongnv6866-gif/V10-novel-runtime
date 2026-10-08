# V10 Wanming Candidate Test — Cluster C Boundary Results

> TEST SANDBOX ONLY — NOT CANON  
> Open counterexample test; not blind.

## C-B1 — One household cannot stand in for all society

**Input**: 一个家庭因新制度获利，作者想用这一家直接证明“全城百姓生活都好了”。

**Expected**: C05 rejects the generalization.

**Result: PASS**

Reason:
- a household can show one causal path, not population-wide distribution;
- at least one cost/uneven-effect indicator must remain visible;
- broader claims require broader evidence, not a symbolic family.

---

## C-B2 — Life scene without downstream effect is filler

**Input**: 连续宏观章节后，插一场吃饭闲聊，人物状态、关系、资源、承诺与后续选择都不变。

**Expected**: S04 rejects it as a valid macro-micro use.

**Result: PASS**

Reason:
- the scene may still be pleasant prose, but it does not satisfy this candidate;
- for promotion value, the life scene must alter at least one later judgment/choice or reveal a cost that the macro line then has to absorb.

---

## C-B3 — Redundant POV must be removed

**Input**: 四个视角在同一地点、听到同一消息、采取同一行动，只为制造“群像感”。

**Expected**: S05 removes/merges redundant POVs.

**Result: PASS**

Reason:
- each retained POV must add new information, action, misread, social position or causal collision;
- repeated camera changes without state gain are noise.

---

## C-B4 — No POV may know facts without a channel

**Input**: 市场里的普通商户在没有任何消息来源时准确知道河边停运的真正原因和官方下一步。

**Expected**: S05 blocks author-knowledge leakage.

**Result: PASS**

Reason:
- knowledge must come from location, witness, message, rumor, document or prior experience;
- reader may know more across cuts, but each character stays locally bounded.

---

## C-B5 — Small event with no persistent state change does not require an aftermath chapter

**Input**: 一次极小误会当天解决，没有资源、关系、职位、信用或生活状态留下变化，作者想硬写三章善后。

**Expected**: C06 compresses it.

**Result: PASS**

Reason:
- aftermath exists to preserve state change, not to satisfy a template;
- if no persistent consequence remains, one line or no dedicated aftermath may be correct.

---

## C-B6 — Aftermath is not an accounting paragraph

**Input**: 作者把人员、钱、关系、家庭、市场五类后果一次性用旁白逐条列完。

**Expected**: C06 rejects the delivery form even if the facts are complete.

**Result: PASS**

Reason:
- state tracking may use a matrix author-side;
-正文 should select consequences that characters must act on;
- remaining items can stay in state tables until triggered.

---

## Boundary conclusion

- C-B1: PASS
- C-B2: PASS
- C-B3: PASS
- C-B4: PASS
- C-B5: PASS
- C-B6: PASS

Boundary pass: **6 / 6**

No Runtime promotion authorized.
