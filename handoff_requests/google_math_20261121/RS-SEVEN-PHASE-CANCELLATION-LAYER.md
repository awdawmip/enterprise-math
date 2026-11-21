<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-SEVEN-PHASE-CANCELLATION-LAYER",
  "title": "一般分母误差下的消去层相位分类与高阶恢复",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "DRAFT",
  "priority": "P2",
  "leverage": "MEDIUM",
  "frontier": "v=0 的六个次阶模板及参数不确定性分类已精确证明；完整系数/平移商首交点界为48/39。一般v的同首项水平纤维及交点处高阶信息尚未解决。",
  "next_action": "在声明的整数误差、观察者信息与参数范围内，确定一般v的次阶有类型观测及跨相位分离/碰撞结构，交回可复算结果和边界。",
  "dependencies": [],
  "source_refs": [
    "https://github.com/awdawmip/enterprise-math/blob/ab4699ad2a80b0e040c5a5f287cd34a537d75e6f/research_notes/portable_direct/2026-11-16_google_math_continuation/joint/joint-seven-proof.md",
    "https://github.com/awdawmip/enterprise-math/blob/ab4699ad2a80b0e040c5a5f287cd34a537d75e6f/research_notes/portable_direct/2026-11-16_google_math_continuation/joint/joint_check.py",
    "https://github.com/awdawmip/enterprise-math/blob/ab4699ad2a80b0e040c5a5f287cd34a537d75e6f/research_notes/portable_direct/2026-11-16_google_math_continuation/joint/shape-seven.md",
    "https://github.com/awdawmip/enterprise-math/blob/7ad53ff4d8168f4800fc49270b197f14defd0b4c/research_notes/portable_direct/google_clue_deepening_20261121/cancellation/THEOREM.md",
    "https://github.com/awdawmip/enterprise-math/blob/7ad53ff4d8168f4800fc49270b197f14defd0b4c/research_notes/portable_direct/google_clue_deepening_20261121/cancellation/CROSSCHECK.md"
  ],
  "evidence_status": "TASKBOOK_DRAFT_V2",
  "last_progress_ref": null,
  "last_progress_at": null,
  "hard_block": null,
  "tags": [],
  "claim_lease_minutes": 120,
  "created_by_role": "RESEARCHER",
  "task_authority": "PENDING_PUBLICATION",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-SEVEN-PHASE-CANCELLATION-LAYER",
  "parent_objective_id": "OBJ-GOOGLE-20261116-ERDOS1063-SEVEN-PHASE",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "NEW_DIRECTION",
  "parent_task_id": null,
  "successor_gate": null
}
-->

# 一般分母误差下的消去层相位分类与高阶恢复

## 任务依据与已完成边界

本任务承接 EM-DIRECT-3DCA45 的原共同误差模型及2026-11-16未发布提案；本轮 EM-DIRECT-949983 已完成 v=0 基准，不再将它列为未知。对 d=0、e=floor((-r^6+lambda*r^5)/25920)，已有

\[
Z_r=-20\mathbf1+K_a(\lambda)/r+O(r^{-2}),\qquad r\equiv a\pmod6.
\]

全部六个K已在来源中给出。已知相同lambda时完整系数始终可分；每个候选相位各取未知lambda且|lambda|≤Lambda时，完整模板首交点界48，平移商首交点界39。两处完整系数交点为 K0(-60)=K1(-69)、K0(-48)=K5(-39)。这是次阶系数结论；交点处的精确有限读数尚未被证明碰撞。

## 研究对象

保持原生成函数C,T、去趋势多项式Q和七点四阶差分H7。共同整数误差在同一窗口固定：

\[
Y_{r,j}=\frac{(r+j)^3(T(r+j)+e_r)}{C(r+j)+d_r}-Q(r+j),\quad Z_r=H_7Y_r.
\]

考虑e_r=floor((-r^6+lambda*r^5)/25920)、d_r=floor(v*r^5/4320)，或另一个明确给出并验证等价精度的整数实现，参数|v|≤delta<1、|lambda|≤Lambda。跟踪参数逼近与取整误差；各相位使用自己的合法整数序列r=6m+a。必须声明观察者实际获得的尺度、读数和参数信息，不能一面已知完整r、一面把r mod6当作未知。

原首项模型在消去层给出共同水平

\[
\beta(v)=-\frac{4(v^4-122v^3+433v^2-189v+5)}{(1+v)^4}.
\]

未知v不能未经证明就由该水平唯一恢复。完整观测的研究对象是有类型的( beta(v), K_a(lambda,v) )及其一致余项；平移商需另列其丢失的共同水平和次阶共同分量。

## 目标与可验收结果

给出一般v的次阶模板或足以判定相位的精确等价表达，并在明确参数域内解决跨相位可辨识性。已知公共参数、候选相位可取独立未知参数是不同量词，须据实分别表述。完整观测比较不同v时，首项相同的beta纤维是相关对象。

可交付全域分类，或具有明确数学内容、来源支撑和剩余边界的参数子域定理/反例。其价值在于实际扩大已知可分域，解释真实障碍或识别更高阶所需精度。只列出数值图、重算v=0基准或报告符号求解未完成不构成该目标的解决。

成果应包含：次阶表达和一致余项依据；声明域内经证明/认证的分离区域或确切系数交点；与完整观测/平移商对应的结论；v=0的48/39回归核对；整数取整和合法起点的复算。若处理已知交点，确定更高阶是否区分以及需要的观测尺度；若声称有限整数碰撞，必须展示两个合法原始假设的精确等值，不能用系数交点代替。

本任务规定对象与验收，不限定研究方法、思考次序或中间结论。采样相位与参数坐标属于原生X6框架内的辅助观察，保留联合关系、符号与残差证据。作者侧证明、控制面保存及独立审查分别按真实状态报告。
