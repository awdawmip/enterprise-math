<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-P000-L1-NATIVE-CARRIER-CONTACT-BRIDGE",
  "kind": "RESEARCH",
  "owner": "research/p000-l1-native-carrier-contact-bridge",
  "base_state": "READY",
  "priority": "P0",
  "leverage": "HIGH",
  "parent_objective_id": "OBJ-P000-ENTERPRISE-6D-ROTATION-TOMOGRAPHY",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-P000-L1-NATIVE-CARRIER-CONTACT-BRIDGE",
  "origin_kind": "MAINTENANCE",
  "task_lineage": "MAINTENANCE",
  "claim_lease_minutes": 240,
  "hard_block": null,
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:10ec4f937324069d7af8d77a52c244389ac4cccd957e3685c14c6fe8b8fd367c",
    "review_state": "PASS",
    "temporary_overrides": []
  },
  "title": "P000 S4 等变 PF10/connection 模空间 V21 — Gen19 语义零数学漂移重冻结",
  "frontier": "Classify the complete nontrivial moduli/gauge/holonomy structure of S4-transparent PF10 families and independent connections and construct one common non-degenerate enriched Full-Cell S4 model.",
  "next_action": "Parameterize PF10 by Cell-stabilizer orbits, classify equivariant K4 connection gauge classes and holonomy, then integrate a nonconstant PF10 family with a nonidentity/nonflat connection in one model and check enriched S4 relations.",
  "dependencies": [
    "research_tasks/P000_S4_EQUIVARIANT_PF10_CONNECTION_MODULI_V19_20260831.md@main",
    "research_task_records/RS-P000-L1-NATIVE-CARRIER-CONTACT-BRIDGE/TP2-E5B7C19A3D604F821583.json@main",
    "research_returns/P000_LOCAL_TO_GLOBAL_BACKGROUND_EQUIVARIANCE_V18_RETURN_20260831.md@main",
    "driver_reviews/P000_LOCAL_TO_GLOBAL_BACKGROUND_EQUIVARIANCE_V18_DRIVER_REVIEW_20260831.md@main",
    "research_returns/P000_BACKGROUND_S4_EQUIVARIANCE_GATE_V17_RETURN_20260830.md@main"
  ],
  "source_refs": [
    "TP2-E5B7C19A3D604F821583",
    "TP2-D6A41E9C3B705F821847",
    "RR-7FED4A83F3922D37319D",
    "DR-7F2A91C5D4B306E82194"
  ],
  "evidence_status": "GEN18_LOCAL_TO_GLOBAL_ACCEPTED / GEN19_MODULI_SCOPE_PRESERVED / ZERO_MATH_DELTA_PUBLICATION_ENVELOPE_REFREEZE",
  "last_progress_ref": "DR-7F2A91C5D4B306E82194",
  "last_progress_at": "2026-08-31T05:18:00+00:00",
  "tags": [
    "P000",
    "native-6D",
    "S4",
    "PF10",
    "connection",
    "holonomy",
    "equivariance",
    "moduli",
    "nonflat",
    "gauge",
    "zero-math-delta",
    "control-repair"
  ],
  "identity_lane": "P000FCC21R",
  "foundation_level": "P000_ROOT_AXIOM_BOUND",
  "p000_required": true
}
-->

# P000 `S4` 等变 PF10/connection 模空间 V21 — Gen19 语义零数学漂移重冻结

Status: `READY / P0 / P000-BOUND / ZERO-MATH-DELTA-REFREEZE`

## Mother question

在不改变 `TP2-E5B7C19A3D604F821583` 的 Gen19 数学问题与已验收 Gen18 前提的条件下，把当前主线重冻结成 V2 task envelope 完整的 publication：精确分类 `S4` 透明 PF10 与 independent connection 的非平凡模空间、gauge/holonomy 类，并构造一个共同的非退化 enriched Full-Cell `S4` model，或者证明精确障碍。

## Frozen inputs and scope

冻结当前已验收边界：

- Gen17 的 `PF10_STRUCTURAL_AUT_EQ` 与 independent connection 的 `CONNECTION_STRUCTURAL_AUT_EQ` 仍是两个独立、各自有成本的 semantic transparency gates；
- Gen18 已验收 local-to-global 定理：必须检查 frozen carrier generators `a,b` 上的完整 structural lift fibers；只检查一组选定 coherent lifts 不足以推出 full transparency；
- Gen18 已给出 nonflat-but-fully-equivariant connection 正例，必须作为 regression 保留；
- G15 grammar、Gen17 gate count/cost、Gen18 full-lift-fiber criterion 均不得改变；
- `NO_KERNEL_QUOTIENT`；
- `CARRIER_S4 != COMPLETE_NATIVE_P000_ROTATION_GROUP`；
- `TIME_FIXED`；
- 不把 gauge/presentation bit 计为新的 native spatial axis。

本重冻结只修复 publication envelope；不新增 theorem，不改变 domain，不修改 P000 root ontology。

## Hard target and required outputs

Hard target 保持 Gen19：

`P000_S4_EQUIVARIANT_PF10_CONNECTION_MODULI_AND_COMMON_NONDEGENERATE_MODEL_EXACTLY_CLASSIFIED`

必需输出保持原 Gen19 范围：

1. 精确给出 base Cell stabilizer 在 6 channel 上的 orbit partition，并分类 `I`、`O` 与 ordered-pair `M` 的全部 stabilizer-fixed 参数；
2. 从 representative Cell profile 通过 structural transport 重建完整 global equivariant PF10 family，并证明参数化完备且无重复，或给出 gauge quotient 后的完备版本；
3. 给出至少一个 raw Cell-to-Cell 非恒定、但 native-equivariant 的 PF10 family；
4. 对冻结的 typed finite connection value universe，分类 oriented-edge stabilizer 条件、reverse-edge law、full-lift-fiber naturality 与 gauge transformation law；
5. 枚举或结构分类全部 `CONNECTION_STRUCTURAL_AUT_EQ` 解，quotient by accepted gauge equivalence，给出 representatives 与 exact counts/parameterization；
6. 对 connection gauge classes 计算 K4 triangle/cycle holonomy，按 conjugacy class 分类 flat/nonflat，并验证 `S4` holonomy conjugacy law；
7. 在同一个 Full-Cell model 中同时实现非恒定 PF10 与 nonidentity、优先 nonflat 的 independent connection，并在完整 enriched data 上验证 `R_a^3=R_b^2=(R_aR_b)^4=id`；
8. deterministic checker 覆盖 S4/Cell/edge stabilizers、PF10 orbit parameterization、global reconstruction、connection/gauge/holonomy、common-model witness 与 Gen17/18 guards。

必须回归：full local `S4` vector orbits=`1`、ordered-pair orbits=`3`；base tetra Cell stabilizer vector orbits=`2`、ordered-pair orbits=`8`；以及 Gen18 的 edge-to-opposite transposition nonflat-equivariant connection。

## Research value to preserve

Gen19 是已验收 Gen18 full-lift-fiber 局部到全局判据后的直接数学前沿。它把问题从“背景等变 gate 是否足够、怎样有限验证”推进到“这些 gate 下究竟存在多丰富的非平凡内容”。这是当前最深的可执行 moduli/common-model 前沿，保留它可以避免重新计算已关闭的 Gen16/17/18 问题。

本重冻结不赋予额外的 Working Truth、Foundation 或数学优先级；它只确保这一已存在的研究问题具有当前协议要求的完整 task envelope。

## Success, kill, and return criteria

有效 terminal classes 保持 Gen19：

- `NONTRIVIAL_PF10_AND_NONFLAT_CONNECTION_MODULI_COMMON_MODEL_CLASSIFIED`；
- `NONTRIVIAL_PF10_AND_ONLY_FLAT_CONNECTION_MODULI_CLASSIFIED`；
- `PF10_MODULI_CLASSIFIED_CONNECTION_COMMON_MODEL_EXACTLY_OBSTRUCTED`；
- `TRANSPARENCY_GATES_FORCE_DEGENERATE_CONTENT_EXACTLY_PROVED`。

Kill / stop 条件：

- 修改 P000 root ontology、G15 grammar、Gen17 gate count/cost 或 Gen18 full-lift-fiber criterion；
- 用 chosen one-pair lift check 偷换 full transparency；
- 把 presentation/gauge freedom 计为 native axis；
- 把 separately constructed PF10 与 connection witnesses 冒充同一 common model；
- 任何 theorem、domain、counterexample、cost 或 accepted guard 相对 Gen19 发生未声明变化。

若重冻结过程中发现上述数学差异，必须停止零数学漂移路径并返回 substantive revision。
