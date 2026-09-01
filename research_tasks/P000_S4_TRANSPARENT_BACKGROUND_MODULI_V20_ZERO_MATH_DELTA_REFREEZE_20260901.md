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
  "title": "P000 S4 透明背景模空间 V20 — D4 并行支线零数学漂移重冻结",
  "frontier": "Classify finite/local presentations and nontrivial moduli of S4-transparent PF10 profiles and independent connections/holonomy, and construct one common non-degenerate enriched Full-Cell S4 model or prove the exact obstruction.",
  "next_action": "Compute PF10 stabilizer-orbit parameterization; classify S4-equivariant K4 connection transports with reverse-edge/gauge laws; search exact nonidentity/nonflat witnesses; integrate them in one model and recheck enriched S4 relations.",
  "dependencies": [
    "research_tasks/P000_S4_TRANSPARENT_BACKGROUND_MODULI_V18_20260831.md@main",
    "research_task_records/RS-P000-L1-NATIVE-CARRIER-CONTACT-BRIDGE/TP2-D4A7C19E5B306F821472.json@main",
    "research_returns/P000_BACKGROUND_S4_EQUIVARIANCE_GATE_V17_RETURN_20260830.md@main",
    "driver_reviews/P000_BACKGROUND_S4_EQUIVARIANCE_GATE_V17_DRIVER_REVIEW_20260831.md@main"
  ],
  "source_refs": [
    "TP2-D4A7C19E5B306F821472",
    "TP2-A7D3C18E5B904F621476"
  ],
  "evidence_status": "ZERO_MATH_DELTA_PUBLICATION_ENVELOPE_REFREEZE / RETAINED_PARALLEL_S4_MODULI_BRANCH",
  "last_progress_ref": "TP2-D4A7C19E5B306F821472",
  "last_progress_at": "2026-08-31T05:10:00+00:00",
  "tags": [
    "P000",
    "native-6D",
    "S4",
    "PF10",
    "connection",
    "holonomy",
    "equivariance",
    "moduli",
    "zero-math-delta",
    "control-repair"
  ],
  "identity_lane": "P000FCC20R",
  "foundation_level": "P000_ROOT_AXIOM_BOUND",
  "p000_required": true
}
-->

# P000 `S4` 透明背景模空间 V20 — D4 并行支线零数学漂移重冻结

Status: `READY / P0 / P000-BOUND / ZERO-MATH-DELTA-REFREEZE`

## Mother question

在不改变原 `TP2-D4A7C19E5B306F821472` 数学内容的前提下，保留其独立的 `S4` 透明背景局部表示与模空间问题，并把该支线重冻结成当前 V2 task envelope 完整、可安全作为并行历史和比较基线的 publication。

## Frozen inputs and scope

冻结原 D4 支线及其上游边界：

- Gen17 已接受 `PF10_STRUCTURAL_AUT_EQ`，以及声明 independent connection 时的 `CONNECTION_STRUCTURAL_AUT_EQ`，二者各自保持原有语义与成本；
- Gen16 裸 `{K4_ADJ}` frontier 的拒绝保持不变；
- `CARRIER_S4 != COMPLETE_NATIVE_P000_ROTATION_GROUP`；
- `NO_KERNEL_QUOTIENT`；
- `TIME_FIXED`；
- 原 D4 对 K4/tetra structural `S4` action 下 PF10 stabilizer-orbit、independent connection、gauge、holonomy 与 common-model 的研究范围保持不变。

本重冻结不新增关系、不修改 gate 成本、不改变 P000 root ontology，也不把 presentation/gauge 数据升级为 native spatial axis。

## Hard target and required outputs

Hard target 保持原 D4：

`P000_S4_TRANSPARENT_BACKGROUND_LOCAL_PRESENTATION_AND_NONTRIVIAL_MODULI_EXACTLY_CLASSIFIED`

所需数学输出仍为：

1. base Cell stabilizer 在 6 channel 与 ordered channel-pair 上的 exact orbit partition；
2. `I`、`O`、`M` 的 stabilizer-fixed 参数化与 global equivariant reconstruction；
3. 至少一个 raw Cell-to-Cell 非恒定但 native-equivariant 的 PF-10 witness，或其 exact obstruction；
4. independent connection 的 typed value universe、oriented-edge stabilizer 条件、reverse-edge law、gauge quotient 与 holonomy classification；
5. nonidentity、优先 nonflat 的 fully equivariant connection，或其 exact obstruction；
6. 在同一 K4/tetra Full-Cell model 中完成 PF10 与 connection 的 common-model integration，并验证完整 enriched `S4` relations；
7. deterministic exact checker 覆盖 stabilizer enumeration、orbit parameterization、connection/gauge/holonomy 与既有 Gen17 regressions。

必须回归原支线数值边界：base tetra Cell stabilizer vector orbits `2`、ordered-pair orbits `8`；full local `S4` vector orbit `1`、ordered-pair orbits `3`。

## Research value to preserve

D4 是 Gen17 后直接形成的并行模空间支线。即使后来的 Gen18 local-to-global 结果给出更强的验证接口，D4 仍保留一个有价值的独立控制视角：它从 stabilizer/local presentation 出发询问透明 gate 是否仍允许非平凡 PF10 与 connection 内容。保留这条支线可用于对照后续主线，防止把“可验证”等同于“只有退化模型”。

本重冻结的价值仅是保持这份数学问题以当前可审核 envelope 存续，不提升其相对于其他 publication 的真理、优先级或基础地位。

## Success, kill, and return criteria

成功标准与原 D4 的有效终态保持一致：

- `NONTRIVIAL_S4_EQUIVARIANT_PF10_AND_NONFLAT_CONNECTION_COMMON_MODEL_CONSTRUCTED`；
- `NONTRIVIAL_PF10_AND_ONLY_FLAT_EQUIVARIANT_CONNECTIONS_CLASSIFIED`；
- `PF10_MODULI_CLASSIFIED_CONNECTION_EQUIVARIANCE_EXACTLY_OBSTRUCTED`；
- `TRANSPARENCY_GATES_FORCE_DEGENERATE_BACKGROUND_EXACTLY_PROVED`。

Kill / stop 条件：

- 任何 P000 root ontology、G15 grammar、Gen17 gate 语义或成本发生改变；
- 将 orbitwise Cell-equivariance 偷换为 pointwise 全局常数；
- 将 `nonflat` 自动解释为 rotation obstruction；
- 用两个彼此分离的 witness 冒充 common-model；
- 任何数学 theorem、domain、counterexample 或 cost 相对原 D4 发生未声明漂移。

若发生上述任一情况，必须返回 substantive revision，而不是把变化隐藏在本零数学漂移重冻结中。
