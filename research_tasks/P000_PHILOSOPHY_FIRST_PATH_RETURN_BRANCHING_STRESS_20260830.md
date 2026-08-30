<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-P000-PHILOSOPHY-FIRST-PATH-RETURN-BRANCHING-STRESS",
  "title": "哲学先行 Q13：Path-Return 在首个分支 Cell 类上的压力测试",
  "kind": "RESEARCH",
  "owner": "research/p000-phil-q13-path-return-branching-stress",
  "base_state": "READY",
  "priority": "P0",
  "leverage": "HIGH",
  "frontier": "Q9 proves exact reconstruction and representability for anonymous first-return periods on finite simple degree-two native-Cell graphs. Determine whether that completeness survives the first controlled relaxation to branching, or whether degree-two uniqueness is the hidden reason it works.",
  "next_action": "Freeze a smallest finite simple native-Cell class with maximum degree at most three and uniform local decorations; define path-return observations without using Cell identities; then search first for nonisomorphic equal-observation countermodels before attempting any reconstruction theorem.",
  "dependencies": [
    "RR-BCD1FA15FA40C628701F",
    "DR-892818B131C5047A996F"
  ],
  "source_refs": [
    "research_returns/P000_PHILOSOPHY_FIRST_NONLOCAL_PROBE_JOINT_SEPARATION_RETURN_20260830.md",
    "driver_reviews/P000_PHILOSOPHY_FIRST_Q9_Q12_DRIVER_REVIEW_20260830.md"
  ],
  "evidence_status": "DRIVER_ACCEPTED_Q9_DEGREE_TWO_COMPLETENESS_WITH_EXPLICIT_OUT_OF_SCOPE_BRANCHING",
  "last_progress_ref": null,
  "last_progress_at": null,
  "hard_block": null,
  "tags": [
    "P000",
    "philosophy-first",
    "path-return",
    "branching",
    "reconstruction",
    "representability",
    "countermodel"
  ],
  "claim_lease_minutes": 240,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-P000-PHILOSOPHY-FIRST-PATH-RETURN-BRANCHING-STRESS",
  "parent_objective_id": "OBJ-P000-ENTERPRISE-6D-ROTATION-TOMOGRAPHY",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "origin_kind": "DRIVER_ROADMAP",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-P000-PHILOSOPHY-FIRST-NONLOCAL-PROBE-JOINT-SEPARATION",
  "successor_gate": {
    "new_information_gap": "Q9 reconstructs only 2-regular graphs, where every connected component is a cycle and one rootwise return period determines component length. The first branching class can have several competing return routes and therefore may destroy that inverse.",
    "why_parent_result_does_not_close_it": "Q9 explicitly excludes branching and higher-incidence Cell classes and makes no completeness claim there.",
    "discriminating_outcomes": [
      "FIRST_BRANCHING_COUNTERMODEL_EXACTLY_CLASSIFIED",
      "BRANCHING_PATH_RETURN_JOINT_RECONSTRUCTION_PROVED_ON_DECLARED_CLASS",
      "Q9_PERIOD_INTERFACE_NOT_WELL_DEFINED_OUTSIDE_DEGREE_TWO"
    ],
    "kill_condition": "If the Q9 scalar/rootwise period observable ceases to be intrinsically single-valued at branching and no invariant minimal replacement exists without encoding full identity, kill direct period continuation and return the exact ambiguity certificate.",
    "alternative_route_or_free_exploration_considered": "Closure was considered because Q9 is complete on U_2REG; groupoid/descent escalation and unrestricted graph spectroscopy were also considered. They are deferred until the first branching lower-language failure is measured exactly.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "The model class and theorem quantifier change from degree two to the first branching envelope, while Q9 remains frozen as a terminal theorem on U_2REG. A separate task preserves that boundary and can refute the continuation cleanly."
  },
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:10ec4f937324069d7af8d77a52c244389ac4cccd957e3685c14c6fe8b8fd367c",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# 哲学先行 Q13：Path-Return 在首个分支 Cell 类上的压力测试

Status: `READY / P0 / BRANCHING-STRESS`

## Mother question

Q9 的完整性是否来自真正的 P000 path-return 原理，还是仅仅来自 2-regular 图“每个连通分量必为一个环”的特殊性？

先质疑问题本身：进入分支以后，“一个 root 的 first-return period”是否仍是正确对象？如果不是，必须先给出歧义反模型，再决定最小替代观察量；不能直接把经典谱或完整图同构类型搬进输入。

## Frozen inputs and scope

冻结 Q9 在 `U_2REG` 上已经接受的结论，不重做。第一压力类只允许有限简单 native-Cell 邻接，最大度数 `<=3`，保留与 Q9 相同的统一局部 axis/carrier/PF-10 装饰。Cell identity 不得作为 probe 输出。

候选观察必须先以 native path / nonbacktracking return 语言定义，再允许用经典图论名称比较。不得预装 adjacency matrix spectrum、Ihara zeta 或完整 cycle basis 作为答案；若这些后来被证明是最低修复的一部分，必须有 lower-language failure certificate。

## Hard target and required outputs

Hard target: `P000_PATH_RETURN_BRANCHING_RECONSTRUCTION_OR_FAILURE_EXACTLY_CLASSIFIED`

1. 明确定义分支点处 Q9 first-return interface 的单值性、集合值或多重度语义。
2. 优先寻找两个非同构 finite Cell states，它们具有相同的最弱合法 path-return packet；若存在，给出最小反模型与最小缺失信息。
3. 若某个增强 return packet 在声明类上重建整体，证明 injectivity，并给出 formal-packet representability 判据或精确剩余 virtual sector。
4. 同时测试 separation 与 representability，禁止只修复一侧。
5. 比较至少一个更弱候选，证明增强确实必要；任何升级必须通过 Q8 的最低充分抽象门槛。
6. 提供确定性 checker；有限枚举只能支撑声明的有界部分，普遍结论必须有结构证明。

## Research value to preserve

这是 Q9 是否能从 toy-complete theorem 变成真正 native tomography 接口的第一次压力测试。正结果会把“返回路径”推进到有分支的 Cell 几何；负结果同样重要，因为它会精确指出 Q9 完整性的隐藏假设，并告诉我们下一种关系信息究竟缺在哪里。

## Success, kill, and return criteria

有效终态包括：

- `FIRST_BRANCHING_COUNTERMODEL_EXACTLY_CLASSIFIED`；
- `BRANCHING_PATH_RETURN_JOINT_RECONSTRUCTION_PROVED_ON_DECLARED_CLASS`；
- `Q9_PERIOD_INTERFACE_NOT_WELL_DEFINED_OUTSIDE_DEGREE_TWO`。

若最小反模型已经证明当前 return packet 失效，不得用增加到“几乎完整对象描述”的 probe 强行制造成功；应冻结失败并给出下一层最小信息缺口。
