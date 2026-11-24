<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-X6-GAP-ADAPTIVE-TRANSLATION-COST-20261124",
  "title": "X6 具名 gap：自适应整数平移三读的精确控制成本",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "MEDIUM",
  "frontier": "共同固定偏移三读门槛已精确解决；任意逐次自适应整数偏移仅知 max(0,P−251)≤C3*(P)≤P 及首偏移同一下界，有限 P 精确值和最佳加性常数开放。",
  "next_action": "消费冻结报告第二部分3节的六测试向量、七核线和24割证书，研究逐次改变偏移能否严格优于共同偏移的半径P，给出全域协议或改进下界。",
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
    "adaptive-control",
    "integer-translation",
    "three-query",
    "BRC"
  ],
  "claim_lease_minutes": 120,
  "created_by_role": "RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-X6-GAP-ADAPTIVE-TRANSLATION-COST-20261124",
  "parent_objective_id": "PO-X6-UPPER-STRUCTURE-20260906",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "X6G",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-X6-UPPER-STRUCTURE-INTEGRATION-V2",
  "successor_gate": {
    "new_information_gap": "逐次改变整数累计偏移的硬三读协议是否能以小于P的最坏控制半径恢复原始反号类，以及精确有限预算函数和最佳加性常数。",
    "why_parent_result_does_not_close_it": "母任务的操作安全接口目标未确定本观察器的三读资源最优值；直接作者报告证明了渐近首项系数1和共同偏移精确值，尚未闭合一般逐次偏移。",
    "discriminating_outcomes": [
      "给出 C3*(P)<P 的全域三读协议和准确资源收益。",
      "给出新的全协议下界及匹配上界，闭合一个预算范围。",
      "分别确定或改进首偏移障碍常数、最大累计偏移最优常数或现有证书模板常数。"
    ],
    "kill_condition": "候选协议若利用隐藏输入、合法性反馈或遗漏分支，淘汰该构造；下界见证若不整、超预算或落在同一反号类，修正所声称范围。",
    "alternative_route_or_free_exploration_considered": "共同偏移已给出半径P的有效基线，可沿该接口实现；也可改变为仿射增益观察器。该任务保留整数平移类以回答是否真能在同一类中节省控制。",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "这是操作能力固定后的独立资源最优化问题，可并行研究并回馈母任务的操作安全和资源接口，无需等待原生硬件/源法实现。"
  }
}
-->

# X6 具名 gap：自适应整数平移三读的精确控制成本

## 共同输入、来源与观察目标

直接数学前沿为 [2026-11-24 完整研究稿](https://github.com/awdawmip/enterprise-math/blob/210ab8798f12f4a42feb2d2ac64f88c8dfe860f9/research_notes/20261124_x6_randomized_exact_and_control_b47ea3cd.md)，Git blob 69beb2320af7067c0d3cd0e2640a6019c8ef2c99，SHA-256 52744d17cb53979e3119636bf50fb4d93ce2b2a071a4e3d62daecdc83aad5b7f。前稿及静态精确谱沿该文引用读取。证据状态是符号作者证明与本次协作交叉核验，尚无对应正式独立 Review。

固定三个有号原生轴上的整数位移 a=(x,y,z)，其余三个相对分量在本声明切片中为零，锚点和轴来源保持。预算
ρ(a)=max(x₊+y₊+z₊, x₋+y₋+z₋)≤P，P 为已知非负整数。四个具名高度为
H=(0,u,v,w)，u=x+3y+6z，v=3x+12y+30z，w=7x+39y+126z。
原六个标签为 01、02、03、12、13、23，每次回执为对应绝对间距。原静态目标是 [a]={a,−a}。

该反号商只定义本次观察目标。完整有号六轴状态、具名来源、支路、占用和历史按各自类型保存；投影对某类未来操作是否充分须按实际接口证明。原生基础与控制规则按 frontmatter 的固定科学来源和执行时适用治理读取。

本任务由用户“把之后的任务发布到状态机”直接授权登记。parent_task_id 记录本子问题在既有 X6 母问题下的谱系；上述作者报告此前未作为该母任务的正式 Result，不据此推定母任务完成或改变其现有执行者。后续研究按问题需要选择方法；实际科学运算使用项目适用的 typed BRC 路径，未执行的运算如实保留。

## 母问题与控制模型

第 j 次查询为 r_j=|ℓ_{e_j}(a+t_j)|，其中 t_j∈Z³ 是相对初态的累计偏移，e_j 是原六标签之一。标签、偏移及停止可依赖此前公开回执。一个历史上的控制须对该历史的全部候选合法；控制是否成功、耗时或合法性不提供额外观察通道。恢复目标仍是原初态 [a]。

对全域正确、硬至多三读的确定性协议定义
C₃*(P)=inf_A max_{ρ(a)≤P, j executed} ρ(t_j)。
研究自适应改变偏移能否严格优于 P，并求有限预算最优值或具有明确范围的改进界。若研究随机变体，单独声明随机支路资源上限和正确性量词。

## 已完成的前沿

直接源稿第二部分3节证明：若 P≥ρ(t₁)+252，任何此类三读协议都不能全域正确，即必须有 ρ(t₁)≥max(0,P−251)，即使后两次偏移任意大且自适应。共同偏移 t=Pe₃ 提供三读上界，因此
max(0,P−251)≤C₃*(P)≤P，且 C₃*(P)/P→1。

共同固定偏移的三读最小半径已经解决：固定一批标签在 P≥63 时为P，自适应标签在 P≥64 时为P；较小预算可用零偏移。一般逐次偏移中的有限 P 精确值仍开放。

现有证明包含六个首读测试向量、七条二形式共同核线和二十四个整数割证书。它们提供可直接接续的证明模板，常数251尚未证明最优。

## 待交付的研究结果

分别判断以下问题，说明它们之间已证明的联系：

1. 首次累计偏移必要下界的最佳加性常数。
2. C₃*(P) 的最优有限预算值或新的严格上下界。
3. 现有测试向量/割证书模板内部的最佳包络。

改进模板常数可作为部分成果；宣称全协议最佳常数需相匹配的上界协议或锐性见证。

新上界逐历史给出所用标签、累计偏移、候选合法性、解码和最坏半径。新下界对任意自适应历史证明回执一致性，核对竞争态整数性、预算及不同 [a]；只对冻结控制序列有效的反例不替代自适应下界。

资源分别报告累计偏移半径、实际控制路径长度、终态保持和返回锚点成本。只有源计价关系已经证明时，才从位移半径推断路径成本。

## 验收与返回

精确闭合要求同一接口、同一预算和同一资源口径上的匹配上下界。严格改进常数、发现半径小于P的有效协议、或识别现有证明的实质缺口均可作为部分返回，保留未解预算范围。

共同整数仿射增益或分数平移属于不同能力模型，可用于比较但不记入本整数平移类最优值。已有“至少四读”的条件下界不自动提供四读上界。

## 与已有任务的关系

本项为 RS-X6-UPPER-STRUCTURE-INTEGRATION-V2 提供具体观察投影在受控未来操作下的辨识与资源条件。其直接前沿来自作者报告，不要求先完成一般上层接口整合。原生实现任务可并行提供计价或许可依据，观察模型内的数学研究保持其明确条件。

## 接续与交付

研究输出保存精确陈述、适用域、证明或反例、计算覆盖与原生执行的实际状态，并给出可直接消费的固定提交和文件位置。足以独立复核的文字证明可以作为证据；只有采用的计算方法确实依赖证书时，才交付相应证书与验证关系。

三个新任务可并行领取；相互之间没有等待完成的硬依赖。已有源稿可直接作为有状态标注的输入。当前发布单元只登记后续工作，执行身份与领取由状态机按实际接续办理。
