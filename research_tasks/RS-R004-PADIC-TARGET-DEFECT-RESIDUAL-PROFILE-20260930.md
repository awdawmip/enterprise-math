<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-R004-PADIC-TARGET-DEFECT-RESIDUAL-PROFILE-20260930",
  "title": "R004 p-adic 目标缺陷的层级残差与顺序切除组合律",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "MEDIUM",
  "frontier": "早期 R004 已精确定义 p-adic missing-target module D_H 并证明标量修复质量 Δ(H)=log_p|D_H| 单调，但有限反例已否定其一般次模性与超模性。当前带残差离散体系提示不应继续把未来相关模块结构压成一个标量；待判定完整 p-adic 层级残差/不变因子谱是否能在声明的顺序隐藏、细化与目标查询语言下形成可组合的充分载体，并带来严格剪枝或资源收益。",
  "next_action": "从固定早期 R004 证据重放最小 Z/p^KZ 线性实例，构造 D_H 及 c_j(D_H)=dim_Fp(p^{j-1}D_H/p^jD_H)；先证明并机验各层随 H 包含的坐标单调性与不变因子重构，再逐项攻击层级次模性、majorization、顺序切除组合与观察充分性，保留最小反例。",
  "dependencies": [],
  "source_refs": [
    "awdawmip/chatgpt-global-knowledge@8c863c7ec308cfc74dc325af21e41da24d0f10a7:journal/enterprise-math/2026-08-10/20260810T233000+0800-r004-padic-structural-target-defect.md",
    "awdawmip/chatgpt-global-knowledge@8c863c7ec308cfc74dc325af21e41da24d0f10a7:我眼中的世界.md#WORLDVIEW-20260923-RESIDUAL-FIDELITY",
    "awdawmip/enterprise-math@ff1e5a5862eba2eb7cd0c6d9159a7191aa2f8fec:definitions/RESIDUAL_FAITHFUL_DISCRETE_RELATIONAL_SYSTEM.json",
    "awdawmip/enterprise-math@ff1e5a5862eba2eb7cd0c6d9159a7191aa2f8fec:research_notes/TOOL_DISCOVERY_NATIVE_VALUATION_EHRHART_BRION_CALCULUS_REPORT_20260822.md",
    "awdawmip/enterprise-math@ff1e5a5862eba2eb7cd0c6d9159a7191aa2f8fec:research_notes/BRC_TRANSPORT_RESIDUAL_EXTRACTED_RESULT_20260919.md",
    "awdawmip/enterprise-math@ff1e5a5862eba2eb7cd0c6d9159a7191aa2f8fec:research_tasks/R014_EXACT_LAW_REPRESENTATION_RESOURCE_CALCULUS_20260811.md",
    "awdawmip/enterprise-math@ff1e5a5862eba2eb7cd0c6d9159a7191aa2f8fec:research_tasks/R021_BRANCHING_COLLAPSE_TOOL_CALCULUS_20260811.md"
  ],
  "evidence_status": "HISTORICAL_EXACT_DEFECT_AND_NEGATIVE_SCALAR_RESULT_PLUS_CURRENT_PROFILE_LEMMA_UNREVIEWED_NOT_ADMITTED",
  "last_progress_ref": null,
  "last_progress_at": null,
  "hard_block": null,
  "tags": [
    "R004",
    "p-adic",
    "residual-fidelity",
    "invariant-factors",
    "smith-normal-form",
    "BRC",
    "early-bottleneck-revisit"
  ],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-R004-PADIC-TARGET-DEFECT-RESIDUAL-PROFILE-20260930",
  "parent_objective_id": "OBJ-EARLY-BOTTLENECK-REVISIT-20260930",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "R004P",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "NEW_DIRECTION",
  "parent_task_id": null,
  "successor_gate": null,
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:44b2174111ec85b5dd252d07f474772649a4d36936b2c99acbfa2cfba8af7a73",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# R004 p-adic 目标缺陷的层级残差与顺序切除组合律

Status: `READY / PUBLISHED_REGISTERED / SCIENTIFIC_RESULT_NOT_YET_ACCEPTED`

## Mother question

在有限环 `R=Z/p^K Z` 上，早期隐藏目标缺陷由 `D_H=(Row(A_H)+Row(B_H))/Row(A_H)` 精确刻画。旧标量 `Δ(H)=log_p|D_H|` 已被反例证明不足以支撑一般次模或超模优化。现在检验：保留 `D_H` 的 p-adic 层级残差 `c_j(D_H)=dim_Fp(p^{j-1}D_H/p^jD_H)` 或等价不变因子谱，能否在明确声明的顺序隐藏、细化、目标查询与后续组合语言下成为严格可组合的充分载体；若仍不足，最小缺失的关联或来源信息是什么？

## Frozen inputs and scope

固定早期 R004 的有限线性设定与否定结果：局部已知约束为 `A_H x_H=0`，隐藏目标为 `B_H x_H=0`，missing-target module 为上述 `D_H`；当 `H⊆J` 时存在自然满射 `D_J -> D_H`，从而标量 `Δ` 单调。完整保留已有有限反例：`Δ` 一般既非次模也非超模，本任务不得把更丰富的残差偷换成已经恢复贪心最优性。

当前带残差离散体系只提供研究约束：未来操作或观察可区分的信息不得无证明地丢弃；它不预先保证层级谱充分。BRC、原生 valuation 工具和 residual transport 只在类型接口真正匹配时复用，正质量分支、模上的加法结构、带符号线性消去和 p-adic 滤过不得互相冒充。有限 `Z/p^KZ` 模结构定理、Smith 型分解与滤过维数属于标准数学背景，不把它们本身声称为新定理。

本任务与已登记的 R004 causal-identifiability、R014 表示资源、R021 branching-collapse、有序路径 residual、CFD residual 和首达精度任务区分；唯一母对象是隐藏目标的有限 p-primary module 及其在顺序切除/细化中的未来可辨识结构。

## Hard target and required outputs

重放并独立检查早期最小实例，精确计算 `D_H`、`Δ(H)`、Smith/不变因子与全部 `c_j`。证明或否定：由 `H⊆J` 的满射逐层诱导 `p^{j-1}D_J/p^jD_J -> p^{j-1}D_H/p^jD_H` 的满射，故每个 `c_j` 坐标单调；并证明该层级向量如何重构循环因子指数多重集以及 `Δ(H)=sum_j c_j(D_H)`。

固定至少两类非平凡未来语言：连续增加隐藏坐标或约束后的目标保持查询，以及包含切除、重新组合或细化后再查询的语言。逐类判断层级向量是否为充分状态；若同谱实例可被允许未来区分，给出最小碰撞反例；若受限语言内充分，给出精确组合律与适用边界。

系统攻击逐坐标次模性、前缀和次模性、majorization 单调、边际修复量排序及由其导出的剪枝规则。有限枚举只能证伪或验证声明范围，不能代替全域证明。若性质失败，保存最小 `p,K,|H|` 反例和矩阵/模证书。

实现一个精确小规模检查器，以整数/模算术和 Smith/等价正规形复核结果；对完整模块、层级谱和旧标量三种载体分别报告存储、更新、查询与重构成本。任何节省结论必须把谱计算、更新和必要来源标签一并计费。最小实验从 `p∈{2,3,5}`、`K∈{2,3,4}` 的低维矩阵族开始，并扩展到首次出现结构分离的最小参数。

## Research value to preserve

早期工作已经准确证明：标量修复质量虽单调，却不能承担一般组合优化结构；这一否定结论继续保留。当前真正改变的是可选状态对象：带残差体系要求保留会影响未来的结构，而 p-primary 层级谱给出一个比 `Δ` 严格更细、仍有限可计算、且已有坐标单调命题的天然中间载体。

无论最终结论是层级谱足够、仅在受限未来语言足够，还是必须保留更完整的子模或来源关联，都能把早期模糊的“是否有结构可利用”改写成可证伪的有限代数边界，并为后续 BRC/进取坐标系中的残差压缩提供不依赖连续近似的精确样板。

## Success, kill, and return criteria

成功至少满足一种：证明声明未来语言下的层级残差充分性与精确组合律，并展示相较完整模块表示的非平凡资源或剪枝收益；或给出严格反例证明层级谱仍丢失未来相关关联，并刻画必须增加的最小类型信息；或证明某个次模、majorization 或排序机制在精确有限族中失败，从而关闭该优化分支，同时保留可复用的层级单调定理。

以下不算成功：只重述 `Δ` 旧结论；只引用有限模结构定理而不连接未来操作；只做若干数值扫描；把坐标单调误写成次模性；为了得到正结果改变观察者、未来语言或隐藏目标定义。

返回时必须区分标准代数事实、项目内新组合命题、有限计算证据和未解决缺口，并给出最小复现输入、失败判据与完整资源成本。若发现现有已登记任务已精确覆盖同一母问题，应停止重复实现并记录等价关系。
