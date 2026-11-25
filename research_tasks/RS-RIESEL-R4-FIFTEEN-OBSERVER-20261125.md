<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-RIESEL-R4-FIFTEEN-OBSERVER-20261125",
  "title": "残差嵌合 Riesel：十五预算的前缀与最高必要观察阶",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "MEDIUM",
  "frontier": "固定 R₄ 的十四预算锐阶已证40320；十五预算下界80640，5、13 强制性、共享分支和上界尚未决定。",
  "next_action": "从十四预算的精确容量分支重算十五预算基本对单漏与双漏，先给强制定理或具有真实覆盖的反例。",
  "dependencies": [],
  "source_refs": [
    "5b57c925c33c26b7f79db104e03716e4b3d55ab3:research_notes/portable_direct/riesel_r4_fourteen_sharp_20261125/REPORT.md",
    "89afb234c152b2154ce0ac58a56da5eb02cb1f14:research_notes/portable_direct/riesel_r4_thirteen_sharp_fourteen_shared_20261125/REPORT.md",
    "2ae5de00bf7e8f1e2571ef5666e95f82a25dc429:research_notes/portable_direct/riesel_r4_twelve_observer_lower_20261125/REPORT.md",
    "9b3680ea1c07b1364af5464a3469313ee616d408:research_notes/portable_direct/riesel_nine_frontier_20261124/README.md"
  ],
  "evidence_status": "SOURCE_BOUND_OPEN_RESEARCH",
  "last_progress_ref": "5b57c925c33c26b7f79db104e03716e4b3d55ab3:research_notes/portable_direct/riesel_r4_fourteen_sharp_20261125/REPORT.md",
  "last_progress_at": null,
  "hard_block": null,
  "tags": [
    "RIESEL",
    "RESIDUAL_CHIMERA",
    "EXACT_COVERING_OBSERVER"
  ],
  "claim_lease_minutes": 120,
  "identity_lane": "RIESEL-R4-OBSERVER",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "INTEGRATION",
  "parent_task_id": null,
  "successor_gate": null,
  "parent_objective_generation_id": "OG-4F402E54190FC6F2541D",
  "created_by_role": "RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-RIESEL-R4-FIFTEEN-OBSERVER-20261125",
  "parent_objective_id": "OBJ-RIESEL-R4-FIFTEEN-OBSERVER-20261125",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL"
}
-->

# 残差嵌合 Riesel：十五预算的前缀结构与最高必要观察阶

固定原 `R₄` 根族、旧字典 `P` 及 `δ_P` 的含义，不改成全字典重选成本 `τ`。十三和十四的最高必要阶已分别严格闭合为 20160、40320；此任务保留原作者和直接科学稿的署名，不把这些稿件视为已独立审查。十四首次容许全共享覆盖；原来的两枚基本素数 5、13 仍强制，但要求同一根再使用 19、73 可使成本 14 增到 16。固定输入见下；既有 GRH 兼容素数供给是另一题。

**首个未完单元：** 同时核对“双漏”和“单漏”基本对的容量界，在十五预算上逐一证明是否强制 5 和 13。用固定余孔、真正的圆分阶库存和 CRT 交叉半相位计数；十四单漏常数 6373/180 不能直接多加一类。若强制性失败，给普通整数根的同根可验证覆盖或 CRT 族，并分别处理遗漏者；不能把容量筛未排掉当作反例。

**继续条件：** 只有前缀分支确实闭合，才按相应的规范尾支和全共享分支做候选阶筛与真实覆盖排除。十五预算已有统一下界 80640。给出匹配上界，或提供阶更高的真实必要坐标开关；若尚不能决定，保存严格区间、未排尽的分支和可复跑的最小缺口。共享分支（十五允许比十四多一个共享槽）重新核计，不照搬十四唯一形状。全模板、密度、最小根和旧固定根无穷成本不作为本次完成前提。

以私有点数位界保证全阶候选有限，不以经验素数上限代替；对新上界保留双序或独立复算，必要坐标区分几何实例与实际普通根。该项不重做九至十四，也不改变原调度或前一作者的成果。

## 固定来源

- [十四锐阶、证书与见证](https://github.com/awdawmip/enterprise-math/blob/5b57c925c33c26b7f79db104e03716e4b3d55ab3/research_notes/portable_direct/riesel_r4_fourteen_sharp_20261125/REPORT.md)
- [十四前缀与完整共享分支](https://github.com/awdawmip/enterprise-math/blob/89afb234c152b2154ce0ac58a56da5eb02cb1f14/research_notes/portable_direct/riesel_r4_thirteen_sharp_fourteen_shared_20261125/REPORT.md)
- [统一下界及 CRT 细分](https://github.com/awdawmip/enterprise-math/blob/2ae5de00bf7e8f1e2571ef5666e95f82a25dc429/research_notes/portable_direct/riesel_r4_twelve_observer_lower_20261125/REPORT.md)
- [原根族、旧字典及出处](https://github.com/awdawmip/enterprise-math/blob/9b3680ea1c07b1364af5464a3469313ee616d408/research_notes/portable_direct/riesel_nine_frontier_20261124/README.md)
