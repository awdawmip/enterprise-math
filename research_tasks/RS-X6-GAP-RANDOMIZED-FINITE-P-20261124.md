<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-X6-GAP-RANDOMIZED-FINITE-P-20261124",
  "title": "X6 具名 gap：有限预算随机查询精确谱与最早稳定阈值",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "MEDIUM",
  "frontier": "已证明 P≥585 时 R0(P)=79/18、硬至多五读类 R0^{≤5}(P)=53/12；137≤P≤584 的两个精确谱及各自最早稳定阈值仍未闭合，585仅为充分阈值。",
  "next_action": "消费冻结报告第一、三部分的上下界与完整竞争态，选择一个尚未闭合的预算区间，构造匹配的全域正确随机协议与下界，或收紧稳定阈值。",
  "dependencies": [
    {
      "target": "awdawmip/enterprise-math@210ab8798f12f4a42feb2d2ac64f88c8dfe860f9:research_notes/20261124_x6_randomized_exact_and_control_b47ea3cd.md",
      "action": "CONSUME",
      "satisfied": true
    }
  ],
  "source_refs": [
    "awdawmip/enterprise-math@210ab8798f12f4a42feb2d2ac64f88c8dfe860f9:research_notes/20261124_x6_randomized_exact_and_control_b47ea3cd.md",
    "awdawmip/enterprise-math@76ca048da602b36236e6e559fa9bf07cc9c542e4:research_notes/20261124_x6_gap_lower_bounds_deepened_b47ea3cd.md",
    "awdawmip/enterprise-math@f8b2361632efee3d844bb1fe78d283a760822d26:p000_reality_foundation.json",
    "awdawmip/enterprise-math@f8b2361632efee3d844bb1fe78d283a760822d26:definitions/HEARTBEAT_WORLD_NATIVE_X6_TIME.json",
    "awdawmip/enterprise-math@f8b2361632efee3d844bb1fe78d283a760822d26:definitions/ENTERPRISE_JOINT_RELATION_OBSERVER_PRESERVATION_20260905.json",
    "awdawmip/enterprise-math@f8b2361632efee3d844bb1fe78d283a760822d26:research_constraints/heartbeat_brc_only.json",
    "awdawmip/enterprise-math@f8b2361632efee3d844bb1fe78d283a760822d26:research_tasks/RS_X6_UPPER_STRUCTURE_INTEGRATION_V2_20260909.md",
    "awdawmip/enterprise-math@f8b2361632efee3d844bb1fe78d283a760822d26:research_task_records/RS-X6-UPPER-STRUCTURE-INTEGRATION-V2/TP2-9AC22B43194DA7427684.json"
  ],
  "evidence_status": "SOURCE_AUTHOR_PROOFS_AND_COLLABORATIVE_CHECKS; INDEPENDENT_REVIEW_NOT_RECORDED; FOLLOWUP_OPEN",
  "last_progress_ref": "awdawmip/enterprise-math@210ab8798f12f4a42feb2d2ac64f88c8dfe860f9:research_notes/20261124_x6_randomized_exact_and_control_b47ea3cd.md",
  "last_progress_at": null,
  "hard_block": null,
  "tags": [
    "X6",
    "labeled-gap",
    "randomized-query",
    "finite-budget",
    "zero-error",
    "BRC"
  ],
  "claim_lease_minutes": 120,
  "created_by_role": "RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-X6-GAP-RANDOMIZED-FINITE-P-20261124",
  "parent_objective_id": "PO-X6-UPPER-STRUCTURE-20260906",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "X6G",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-X6-UPPER-STRUCTURE-INTEGRATION-V2",
  "successor_gate": {
    "new_information_gap": "137≤P≤584 的 R0(P)、R0^{≤5}(P) 及二者各自最早稳定预算未知。",
    "why_parent_result_does_not_close_it": "母任务提供操作安全的上层状态/观察接口整合目标，没有给出本具名间距模型的有限预算随机谱；直接作者前沿只把大预算闭合并给出小预算部分界。",
    "discriminating_outcomes": [
      "闭合精确预算段并给出匹配上下界。",
      "证明更小的充分稳定阈值，并区分是否已证明最早。",
      "给出冻结前沿中受影响命题的同假设反例或精确修正。"
    ],
    "kill_condition": "若对称性、域外竞争者、整数性或预算条件不成立，淘汰受影响证书并保留实际成立范围；有限搜索未命中只报告覆盖范围。",
    "alternative_route_or_free_exploration_considered": "可保持现有大预算结论并结束该分支，或研究另外两项控制/原生实现问题；有限预算精确谱具有独立信息增益，可与其并行。",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "问题固定为一个明确观察模型中的两个有限预算最优化量，便于独立领取与验证，并将精确资源接口回馈母任务而不接管其整体整合工作。"
  }
}
-->

# X6 具名 gap：有限预算随机查询精确谱与最早稳定阈值

## 共同输入、来源与观察目标

直接数学前沿为 [2026-11-24 完整研究稿](https://github.com/awdawmip/enterprise-math/blob/210ab8798f12f4a42feb2d2ac64f88c8dfe860f9/research_notes/20261124_x6_randomized_exact_and_control_b47ea3cd.md)，Git blob 69beb2320af7067c0d3cd0e2640a6019c8ef2c99，SHA-256 52744d17cb53979e3119636bf50fb4d93ce2b2a071a4e3d62daecdc83aad5b7f。前稿及静态精确谱沿该文引用读取。证据状态是符号作者证明与本次协作交叉核验，尚无对应正式独立 Review。

固定三个有号原生轴上的整数位移 a=(x,y,z)，其余三个相对分量在本声明切片中为零，锚点和轴来源保持。预算
ρ(a)=max(x₊+y₊+z₊, x₋+y₋+z₋)≤P，P 为已知非负整数。四个具名高度为
H=(0,u,v,w)，u=x+3y+6z，v=3x+12y+30z，w=7x+39y+126z。
原六个标签为 01、02、03、12、13、23，每次回执为对应绝对间距。原静态目标是 [a]={a,−a}。

该反号商只定义本次观察目标。完整有号六轴状态、具名来源、支路、占用和历史按各自类型保存；投影对某类未来操作是否充分须按实际接口证明。原生基础与控制规则按 frontmatter 的固定科学来源和执行时适用治理读取。

本任务由用户“把之后的任务发布到状态机”直接授权登记。parent_task_id 记录本子问题在既有 X6 母问题下的谱系；上述作者报告此前未作为该母任务的正式 Result，不据此推定母任务完成或改变其现有执行者。后续研究按问题需要选择方法；实际科学运算使用项目适用的 typed BRC 路径，未执行的运算如实保留。

## 母问题与最优化量

零错误随机协议对每个固定输入全域正确。定义
R₀(P)=inf_A max_{ρ(a)≤P} E_A q_A(a)，期望只对算法随机性取值。
R₀^{≤5}(P) 另要求每个输入的每条有效执行支路至多五读。重合点与零态均在定义域内，标签保持具名。

求 137≤P≤584 内两者的完整精确分段，并分别求它们从何预算起永久等于 79/18 与 53/12。两个稳定阈值允许不同。

## 已完成的前沿

完整源稿第一部分给出统一上界、十八态下界、硬五读类的十二态下界及整数预算转移；第三部分提供较小预算的补充证书。

- 所有 P：R₀(P)≤79/18，R₀^{≤5}(P)≤53/12。
- 127≤P≤136：R₀(P)=4，存在硬四读协议，故硬五读类亦为4。
- 137≤P≤190：4≤R₀(P)≤79/18。
- 191≤P≤584：13/3≤R₀(P)≤79/18。
- P≥585：R₀(P)=79/18，R₀^{≤5}(P)=53/12。

585 是现有全部必要竞争者进入预算域的充分界。127 是文中某固定态失去三读证书的锐门槛，191 是旧六态同时失去三读证书的锐门槛；这两项辅助性质并未确定完整随机谱的相变。

## 待交付的研究结果

每个声称精确的预算段给出匹配上界和下界：上界含协议、提前停止条件及逐输入最坏期望成本；下界覆盖全域正确协议，包含支持集外实际需要的竞争态。每个整数竞争态提供位移、回执一致性、不同反号类及预算依据。

可以改进现有有限支持分布、困难分支证书或预算嵌入，也可以采用其它有效方法。若使用对称性，证明它对所使用的分布、查询树或见证集合成立；原预算球本身没有未经证明的全部标签置换对称性。

最早稳定预算的结论需要阈值处成立以及更早预算不能已达到相同常数的证据。仅改进叶反射见证的包络可形成新的充分界，按该强度报告。

## 验收与返回

完整完成标准是两个目标在声明预算范围内的精确谱及各自最早稳定阈值。部分预算闭合、严格改进上下界或更低充分稳定界可作为明确的部分返回，同时列出剩余区间。

下界中的困难输入分布用于证明 max-input 期望成本，不改成算法的输入先验。全域正确性、硬五读约束和零错误量词在每一项结论中保持。发现同假设反例时修正受影响结论，不以扩大或更换查询接口保留原结论。

## 与已有任务的关系

本项细化 RS-X6-UPPER-STRUCTURE-INTEGRATION-V2 的观察者投影资源接口。RS-X6-MINIMAL-READOUT-INDEPENDENT-AUDIT-20261121 冻结的是四种关系更新法、V5 与 V39 的既有命题；本项固定的是四个具名高度的绝对间距随机查询，两者对象不同。

## 接续与交付

研究输出保存精确陈述、适用域、证明或反例、计算覆盖与原生执行的实际状态，并给出可直接消费的固定提交和文件位置。足以独立复核的文字证明可以作为证据；只有采用的计算方法确实依赖证书时，才交付相应证书与验证关系。

三个新任务可并行领取；相互之间没有等待完成的硬依赖。已有源稿可直接作为有状态标注的输入。当前发布单元只登记后续工作，执行身份与领取由状态机按实际接续办理。
