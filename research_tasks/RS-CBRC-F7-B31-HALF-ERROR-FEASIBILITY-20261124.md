<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-CBRC-F7-B31-HALF-ERROR-FEASIBILITY-20261124",
  "title": "Coherent BRC F7：判定 B31 全域坐标重设后的半误差可行性",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "MEDIUM",
  "frontier": "B≤30 精确最优为 1/2；B31 现有 171 条支撑不交证书只对固定 B30 表给出修补下界，允许全部自由坐标重设时仍未定。",
  "next_action": "以原始 B31 四元组定义组装半误差可行性模型，核验 B30 基线，允许全部自由坐标重设，以精确全域见证或原行有理对偶区分。",
  "dependencies": [],
  "source_refs": [
    "900dc3caaea4373ec81e7f58d4856210d662c1be:research_notes/driver/2026-11-22_f7_r493_bounded_gauge_rigidity_and_single_sample_uniqueness.md",
    "fecae6f5fb5bd4277ccb928bfd107e6151cd095a:research_notes/driver/2026-11-22_f7_r492_B31_disjoint_repair_obstruction.md",
    "9a0b3e7c673777e59a9b8efa13ad9c1ac48d5f65:research_notes/driver/2026-11-22_f7_r491_B30_exact_quarter_minimax.md"
  ],
  "evidence_status": "SOURCE_BOUND_OPEN_RESEARCH",
  "last_progress_ref": "900dc3caaea4373ec81e7f58d4856210d662c1be:research_notes/driver/2026-11-22_f7_r493_bounded_gauge_rigidity_and_single_sample_uniqueness.md",
  "last_progress_at": null,
  "hard_block": null,
  "tags": [
    "COHERENT_BRC",
    "F7",
    "EXACT_FINITE_MINIMAX"
  ],
  "claim_lease_minutes": 120,
  "identity_lane": "CBRC-F7-B31",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "INTEGRATION",
  "parent_task_id": null,
  "successor_gate": null,
  "parent_objective_generation_id": "OG-2B73DE837F1927B4D2C2",
  "created_by_role": "RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-CBRC-F7-B31-HALF-ERROR-FEASIBILITY-20261124",
  "parent_objective_id": "COHERENT_BRC_WORKING_EXTENSION",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL"
}
-->

## First unfinished F7 finite box: decide whether `e_31=1/2`

Continue the finite-box defect line under `COHERENT_BRC_WORKING_EXTENSION` (its [current open objective generation `OG-2B73DE837F1927B4D2C2`](https://github.com/awdawmip/enterprise-math/blob/5367901ecfd320a880a332772238b89997d44005/research_objective_records/COHERENT_BRC_WORKING_EXTENSION/OG-2B73DE837F1927B4D2C2.json)). Related earlier mathematical task, not a parent-task binding: `RS-CBRC-F7-RANK-TWO-BALANCED-MIXING-EXISTENCE-AND-SELECTOR-CLASSIFICATION` (publication `TP2-6F3A8C21D4B7095E1F62`). This is a new finite numerical subquestion using the informed Driver evidence, not the parent's blind assignment or the separate frozen `RR-AA38973D56330E59D315` review-routing task.

### Fixed model and evidence

Use `q:Z^2 -> R` with `q(-x,y)=q(x,y)`, `q(0,0)=0`, `q(x,0)=1` for `x != 0`, `q(x,y) >= 1/2` when `y != 0`, and `q(2,1)=q(-1,-1)=1/2`. For each original integer quadruple `(a,b,c,d) in [-31,31]^4`, use `k=a-2b-c+2d` and the signed defect
```text
D_q(a,b,c,d)=q(a+k,b+k)+q(c-k,d-k)-q(a,b)-q(c,d).
```
Here `e_31` is the infimum over all admissible `q` of `max |D_q|` on this box. There is already a lower bound `1/2` from `(1,-1,0,0)`, and the [r491 exact theorem](https://github.com/awdawmip/enterprise-math/blob/9a0b3e7c673777e59a9b8efa13ad9c1ac48d5f65/research_notes/driver/2026-11-22_f7_r491_B30_exact_quarter_minimax.md) proves equality through `B=30`. It pins the [B30 witness](https://github.com/awdawmip/enterprise-math/blob/004f12cbe85d0ac39a1ef92afac298bbda2b0611/research_artifacts/F7_R491_B30_Exact_Quarter_Witness_20261122.b85) and [original-input exact checker](https://github.com/awdawmip/enterprise-math/blob/46372bf6e4b609c0cdf5382a05de528a4e44392d/research_checks/CBRC_F7_R491_B30_EXACT_QUARTER_CERT_20261122.py). [r492](https://github.com/awdawmip/enterprise-math/blob/fecae6f5fb5bd4277ccb928bfd107e6151cd095a/research_notes/driver/2026-11-22_f7_r492_B31_disjoint_repair_obstruction.md) shows that any B31 half-error witness differs from that particular `q_30` on at least 171 evenness-orbit variables and by total absolute mass at least 47 on the certified support; neither restriction rules out a free B31 witness. [r493](https://github.com/awdawmip/enterprise-math/blob/900dc3caaea4373ec81e7f58d4856210d662c1be/research_notes/driver/2026-11-22_f7_r493_bounded_gauge_rigidity_and_single_sample_uniqueness.md) establishes a different, global full-defect-field rigidity result and explicitly leaves B31 open. Preserve original F7 authorship and the r491–r493 Driver contribution separately.

### First research step and resolution

Form the exact half-error feasibility problem on every referenced free orbit `(|x|,y)`, with both signs of each original defect row and the off-axis floor. Check model assembly against the pinned B30 witness and original-input oracle. The r492 rows and B30 values can seed a sparse cutting-plane search; allow **all** free orbits, including old ones, to move. A quarter-grid trial, frozen old coordinates, or a limited repair set may help search, but none can certify a strict lower bound for the actual model. Cache or reduce rows only with an exact implication or reconstruction check. Keep reproducibility tied to the original quadruples and exact orbit-to-value mapping.

- **Equality:** Save a rational `q` witness and independent exact checker, enforcing the marks, axis, evenness and floor and validating both signs over all `63^4=15,752,961` original inputs. Unreferenced free keys can be assigned `1/2`. Combined with the r491 row lower bound, this proves `e_31=1/2`.
- **Strict obstruction:** Save a rational dual/Farkas certificate using original signed rows and admissibility inequalities (or exactly justified equivalents), with original quadruples and independently checked nonnegative weights. Extract an explicit rational lower bound `e_31 >= L>1/2`; a finite infeasible subsystem is sufficient if the certificate proves positive defect-bound dependence and separation.
- **Unresolved:** Preserve exact candidate/witness tests, failing original rows and replayable partial progress; a numerical solver status or a restricted-model obstruction is not a decision.

Stop this unit at the B31 result or a concrete bounded checkpoint. Do not rerun the frozen no-go review, infer the global minimax, or change parent/review status.
