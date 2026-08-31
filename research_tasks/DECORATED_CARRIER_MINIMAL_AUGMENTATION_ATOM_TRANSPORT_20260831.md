<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-DECORATED-CARRIER-MINIMAL-AUGMENTATION-ATOM-TRANSPORT",
  "title": "Decorated carrier 最小增广：从 C2 pairing frame 到 S3/S4 atom transport",
  "kind": "RESEARCH",
  "owner": "research/decorated-carrier-minimal-augmentation-atom-transport",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "After the Seed-6 arithmetic objective closes with flat pairing-frame C2 connections classified by H1 and no intrinsic selector, classify the minimum independent typed information required to obtain full pairing-state S3 transport and then atom-level S4 transport.",
  "next_action": "Build an augmentation hierarchy over the reviewed decorated-carrier reduct; prove necessity with automorphism or same-reduct/different-augmentation witnesses, prove sufficiency by explicit compatible constructions, and distinguish gauge, cohomology, section and V4-breaking atom data.",
  "dependencies": [
    "RR-7FC3258D2D14553F7B2C",
    "DR-7EA1473041B2FCE98EC6",
    "OG-BEBA0993E913AB8E5DA4"
  ],
  "source_refs": [
    "research_returns/SEED6_PAIRING_OPPOSITE_FRAME_AXIOM_COHOMOLOGY_RETURN_20260830.md",
    "driver_reviews/SEED6_PAIRING_OPPOSITE_FRAME_AXIOM_COHOMOLOGY_DRIVER_REVIEW_20260831.md",
    "driver_reviews/SEED6_RESONANCE_OPERATOR_CONNECTION_CANONICALITY_DRIVER_REVIEW_20260830.md"
  ],
  "evidence_status": "SEED6_ARITHMETIC_OBJECTIVE_CLOSED / MINIMAL_TRANSPORT_AUGMENTATION_OPEN",
  "last_progress_ref": null,
  "last_progress_at": null,
  "hard_block": null,
  "tags": [
    "decorated-carrier",
    "transport",
    "minimal-augmentation",
    "C2",
    "S3",
    "S4",
    "V4",
    "torsor",
    "cohomology",
    "atom-frame"
  ],
  "claim_lease_minutes": 240,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-DECORATED-CARRIER-MINIMAL-AUGMENTATION-ATOM-TRANSPORT",
  "parent_objective_id": "OBJ-DECORATED-CARRIER-TRANSPORT-AUGMENTATION-MINIMALITY",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "DCTRMIN",
  "origin_kind": "DRIVER_ROADMAP",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-SEED6-PAIRING-OPPOSITE-FRAME-AXIOM-COHOMOLOGY",
  "successor_gate": {
    "new_information_gap": "The accepted C2 pairing-frame result proves that an explicit minimal connection axiom yields the full H1 gauge space but still does not classify the minimum additional typed data needed for full three-state S3 transport or atom-level S4 transport.",
    "why_parent_result_does_not_close_it": "The parent result closes the Seed-6 arithmetic objective because it shows no further selector is derivable from that arithmetic reduct. It deliberately leaves augmentation design external. The present task studies the necessity and sufficiency of those exogenous augmentation layers, not another attempt to derive them from Seed-6.",
    "discriminating_outcomes": [
      "prove an exact minimal typed augmentation from C2 pairing-frame transport to full S3 pairing-state transport and exhibit matching lower-bound countermodels",
      "prove an exact minimal V4-breaking/twisted-cocycle augmentation from S3 transport to atom-level S4 transport",
      "prove that no support-faithful natural compression exists and classify the irreducible exogenous augmentation torsors/classes instead"
    ],
    "kill_condition": "Kill any route that globally numbers pairing states, chooses an S3 section or atom frame by convention, erases support/row typing, treats gauge choice as structural data, or claims the augmentation is derived from the closed Seed-6 arithmetic reduct.",
    "alternative_route_or_free_exploration_considered": "The Seed-6 parent objective is closed rather than extended. A completely unrelated free search would not answer the exact residual transport-information question. The only justified continuation is to move the unresolved augmentation-minimality question into a separate objective while preserving lineage to the result that exposed it.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "The reviewed task asked what the single new C2 pairing-frame axiom produces and answered exactly H1 gauge freedom. The new task asks a different necessity/sufficiency problem across C2, S3 and S4 layers, requires new countermodel and extension analysis, and is intentionally governed by a new objective so added structure cannot be mistaken for further Seed-6 arithmetic extraction."
  },
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:10ec4f937324069d7af8d77a52c244389ac4cccd957e3685c14c6fe8b8fd367c",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# Decorated carrier 最小增广：从 C2 pairing frame 到 S3/S4 atom transport

Status: `READY / P1 / HIGH`

## Mother question

Seed-6 正向算术几何已经走到一个明确边界：旧 arithmetic/support/resonance reduct 不会自然选出跨 support 的 pairing transport；即便显式加入最小 `PAIRING_OPPOSITE_FRAME_CONNECTION_V1`，模 vertex gauge 后也只是完整的 `H^1(X;F2)` 自由度，并不会自动产生一个首选类。

因此本任务不再问“还能不能从 Seed-6 里挤出一个 transport”。新的问题是：

**若目标确实要求 pairing-level `S3` transport，甚至 atom-level `S4` transport，最少必须额外加入什么 typed information？**

这里的“最少”必须同时有 necessity 与 sufficiency 证明，不能用“我选一个 section/frame 就行”代替。

## Frozen reduct

以下内容作为冻结输入，不得重写：

1. decorated carrier/resonance support-typed CW complex 及其合法 resonance pinch 规则；
2. marked pairing cell 的 residual frame group 是 `C2`，旧 reduct 没有 canonical cross-support `S3` selector；
3. 显式 `C2` pairing-frame flat connections 模 vertex gauge 精确分类为 `H^1(X;F2)`；
4. carrier-height parity 是一个 distinguished `C2` cohomology class，但不会强迫 operator class 与之相等；
5. 标准 exact sequence `1 -> V4 -> S4 -> S3 -> 1` split，但旧 reduct 不选择一个 section，也没有 atom-frame `V4`-breaking datum。

本任务研究的是 **augmentation over this reduct**。任何新增 datum 都必须标明是新增结构，不得倒写为上述冻结算术的推论。

## Hard target

`MINIMAL_TRANSPORT_AUGMENTATION_HIERARCHY_CLASSIFIED`

## Required hierarchy

至少区分以下层次，不得合并命名：

- `L0_ARITHMETIC_REDUCT`：只有冻结的 decorated carrier/support/resonance 数据；
- `L1_PAIRING_FRAME_C2`：额外给出 marked opposite-frame `C2` connection；
- `L2_PAIRING_STATE_S3`：足以定义 full three-pairing-state transport 的数据；
- `L3_ATOM_TRANSPORT_S4`：足以定义 atom-level transport 的数据。

对每个 `Li -> Li+1`，必须回答：

1. **Necessity**：若缺少某类 datum，构造两个具有相同 lower-level reduct、但 upper-level transport 不同的模型，或给出 automorphism/fixed-point obstruction，证明 lower-level 数据不能唯一决定 upper-level 数据。
2. **Sufficiency**：给出最小候选 datum 后，构造全局相容 transport，并证明 composition / inverse / typed-cell compatibility。
3. **Gauge audit**：说明哪些差异只是 vertex frame/gauge，哪些是 global cohomology class，哪些是 section/lift choice，哪些才是真正新增 structural datum。
4. **Minimality**：若声称需要 `n` 个 bit、一个 torsor、一个 section、一个 cocycle 或其它对象，必须说明计数对象和等价关系；非阿贝尔情形不得强行压成 bit count。

## C2 -> S3 obligations

当前 `L1` 只固定 marked carrier matching，并对剩余两个 pairing states 给出 `C2` frame transport。研究者必须精确判断：

- 要恢复完整的三 pairing-state `S3` transport，还缺的是局部 carrier-state permutation datum、全局 section datum、某种 associated torsor，还是其它 typed structure；
- `C2` connection 与额外 datum 的组合是否自然形成 `S3` connection；
- 不同增广何时给出 gauge-equivalent `S3` transports；
- 是否存在任何由冻结 support/resonance typing 强迫的压缩。若不存在，冻结 exact no-go。

不能通过给三 pairing states 任意全局编号来伪造最小性。

## S3 -> S4 obligations

对于 atom lift，必须围绕

`1 -> V4 -> S4 -> S3 -> 1`

给出精确分类：

- 选择一个 splitting/section 与选择 atom frame 分别贡献什么；
- relative to a section，残余 `V4` 数据应当是何种 twisted cocycle / torsor / gauge class；
- 哪些 `V4` 差异可由 vertex atom-frame gauge 消去；
- 要得到一个首选 atom-level transport，最低还需什么 symmetry-breaking datum；
- 若不存在 support-faithful natural selector，给出 automorphism obstruction，而不是任意固定一个 complement。

## Exact witnesses and checker

必须有 machine-checkable finite witnesses，至少覆盖：

1. clean backbone、单 pinch、多 pinch；
2. `H^1` 维数至少为 0、1、2 的代表；
3. 两个相同 `L1` reduct 但不同 `L2` augmentation 的最小反例；
4. 两个相同 `L2` reduct 但不同 `L3` atom lift 的最小反例；
5. 所有四个 `S4` complements/sections 的有限群检查；
6. gauge quotient 前后计数，防止把 presentation choice 当结构；
7. equality stratum 的单独处理。

## Prior-art and terminology boundary

有限群扩张、torsor、group cohomology、nonabelian/twisted cocycle、principal bundle/connection 等均视为标准数学工具。不得把这些标准事实本身写成项目创新。

项目局部可接受的新结论只能是：在**当前冻结 typed decorated-carrier interface** 上，哪一层新增信息是必要/充分的，以及哪些自然选择被精确 obstruction 排除。

## Kill rules

以下任一情形必须判为失败或 no-go，而不是包装成成功：

- 把任意 global numbering 当作 arithmetic selector；
- 把一个选定 `S3` section 称为由旧数据自然给出；
- 把 `V4` kernel 元素、section difference 或 vertex frame choice直接称为内禀 holonomy；
- 抹去 support/row/marked-state typing 后制造额外约束；
- 用有限枚举“没找到反例”替代 necessity proof；
- 把非阿贝尔 lift 自由度无证明地压缩成固定 bit 数；
- 引入 factor recovery、endpoint search、additive-distance 或性能目标。

## Success and return criteria

SUCCESS 需要给出一个完整的 augmentation atlas：

- 每个层级的 objects / morphisms / gauge group；
- `L0->L1->L2->L3` 的 necessity/sufficiency；
- 最小 countermodels；
- 精确 global compatibility 条件；
- machine-readable augmentation table；
- deterministic checker；
- 对是否存在 natural compression 的明确结论。

如果正确结论是“在现有 typed reduct 上不存在首选 `S3` 或 `S4` augmentation，任何选择都必须是外加结构”，这也是终局成功；返回最小 exogenous-data classification 即可，不要再机械开启下一层任务。
