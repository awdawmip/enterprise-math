<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-BRC-X6-RETURN-GREEN-FLUX-BRIDGE-20261003",
  "title": "完整 X6 离散 Green 函数与壳边界净流桥",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "MEDIUM",
  "frontier": "父研究的时间返回概率律未给出完整X6空间Green与壳边界净流桥；固定两个正对称核的有限恒等式、尾控及方向依赖待建立。",
  "next_action": "以两个冻结六轴核和锚点X0=0，精确计算N=0..8的G_N以及R=1,2,3壳边界正访问流，先验证有限净流守恒和尾项，再处理Green极限与方向依赖。",
  "dependencies": [],
  "source_refs": [
    "https://github.com/awdawmip/enterprise-math/blob/b61af8438886a3c1eb8ff53297447837bd2ee507/experiments/brc_hidden_residual_20261003_fca717/REPORT.md",
    "https://github.com/awdawmip/enterprise-math/blob/b61af8438886a3c1eb8ff53297447837bd2ee507/experiments/brc_hidden_residual_20261003_fca717/summary.json",
    "https://github.com/awdawmip/enterprise-math/blob/b61af8438886a3c1eb8ff53297447837bd2ee507/experiments/brc_hidden_residual_20261003_fca717/CROSS_REVIEW.md",
    "https://github.com/awdawmip/enterprise-math/blob/b61af8438886a3c1eb8ff53297447837bd2ee507/experiments/brc_hidden_residual_20261003_fca717/ROOT_REVIEW.md",
    "https://github.com/awdawmip/enterprise-math/blob/2c56c3618dcbe2d65ad4c34bf1839d350759ac90/research_task_records/RS-BRC-BASELINE-RESIDUAL-20261002/TP2-20E37C57649A74D4E563.json",
    "https://github.com/awdawmip/enterprise-math/blob/2c56c3618dcbe2d65ad4c34bf1839d350759ac90/research_tasks/BRC_BASELINE_RESIDUAL_HIDDEN_RESIDUAL_20261003.md",
    "https://github.com/awdawmip/enterprise-math/blob/2c56c3618dcbe2d65ad4c34bf1839d350759ac90/research_objective_records/OBJ-GEOMETRY-BRC-RESIDUAL-ACCUMULATION-SYSTEMS/OG-7AE66316D7566C519AE0.json",
    "https://github.com/awdawmip/enterprise-math/blob/2c56c3618dcbe2d65ad4c34bf1839d350759ac90/research_objective_heads/OBJ-GEOMETRY-BRC-RESIDUAL-ACCUMULATION-SYSTEMS.json",
    "https://github.com/awdawmip/enterprise-math/blob/2c56c3618dcbe2d65ad4c34bf1839d350759ac90/research_objective_head_events/OBJ-GEOMETRY-BRC-RESIDUAL-ACCUMULATION-SYSTEMS/OG-7AE66316D7566C519AE0.json",
    "https://github.com/awdawmip/enterprise-math/blob/2c56c3618dcbe2d65ad4c34bf1839d350759ac90/p000_reality_foundation.json",
    "https://github.com/awdawmip/enterprise-math/blob/2c56c3618dcbe2d65ad4c34bf1839d350759ac90/definitions/HEARTBEAT_WORLD_NATIVE_X6_TIME.json",
    "https://github.com/awdawmip/enterprise-math/blob/2c56c3618dcbe2d65ad4c34bf1839d350759ac90/definitions/ENTERPRISE_JOINT_RELATION_OBSERVER_PRESERVATION_20260905.json"
  ],
  "evidence_status": "SOURCE_BACKED_CONTINUATION_NOT_EXECUTED",
  "last_progress_ref": null,
  "last_progress_at": null,
  "hard_block": null,
  "tags": [
    "BRC",
    "X6",
    "CONTINUATION",
    "direct-user-publication",
    "bounded-scope"
  ],
  "claim_lease_minutes": 120,
  "created_by_role": "RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-BRC-X6-RETURN-GREEN-FLUX-BRIDGE-20261003",
  "parent_objective_id": "OBJ-GEOMETRY-BRC-RESIDUAL-ACCUMULATION-SYSTEMS",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "BRC",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-BRC-BASELINE-RESIDUAL-20261002",
  "successor_gate": {
    "new_information_gap": "时间返回律与完整X6的空间Green、边界净流和方向依赖之间缺少声明核下的严格桥。",
    "why_parent_result_does_not_close_it": "父研究证明的是返回事件/隐藏时间概率及响应统计，未建立两个固定核的离散壳边界守恒、尾项及空间访问极限。",
    "discriminating_outcomes": [
      "有限守恒与尾控闭合，得到限定核/方向的Green和壳总净流结论。",
      "有限恒等式成立但无限尾控缺失，给出具体lemma。",
      "方向依赖或局部反例阻止从总流推出点值各向同性。"
    ],
    "kill_condition": "无法控尾时返回精确缺失lemma；不扩大R/N替代证明，不从维数或n^-2预设空间指数。",
    "alternative_route_or_free_exploration_considered": "已考虑只保留时间返回结论、直接拟合空间幂律、调用晶胞层号或FCC/HCP/Barlow任务；前者可关闭但不回答桥问题，后三者混同对象或重复既有线，均排除。",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "用户要求后续发布；固定两核的Green/净流输出是新的可分派有界信息缺口，与已完成baseline和其他几何/层号任务边界清楚。"
  },
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:d74aad6dd53d0df42d950f7b1207b27d80696f23410bd06f53a038c459577bb2",
    "review_state": "PASS",
    "temporary_overrides": []
  },
  "parent_objective_generation_id": "OG-7AE66316D7566C519AE0"
}
-->

# 完整 X6 离散 Green 函数与壳边界净流桥

Status: `V2 PUBLICATION / READY UPON IMMUTABLE RECORD / NOT EXECUTED`

## 0. Mother question

两个固定完整 X6 正核的时间访问如何经离散 Green 与壳边界净流联系空间传播？有限守恒与尾项能支持多强的方向/壳总流结论？

## 1. Frozen inputs and scope

P000 固定完整六维立体 X6，无原生平面；三维为晶包层，任意三轴不自动定义完整层。n 显式演化、时间另型；原生步为整数 ±E_i，正支路质量与读出/净流/响应分型。输入为 b61af843… 的 REPORT/summary/CROSS_REVIEW 及所引精确证据（完整链接见元数据）。数学父为 baseline 第8代 TP2-20E37C57649A74D4E563；已完成输入不作未完成依赖。新任务仅组织绑定 OPEN GBRC Objective/OG-7AE66316D7566C519AE0，不改旧 baseline，不冒充 GBRC-R1 后继或 Driver 接受。接手者读取固定来源并取得合法执行绑定后开展本任务；发布本身不授予数学接受。

无记忆对称最近邻核两个：十二方向均匀；轴概率 (1/4,1/4,1/8,1/8,1/8,1/8)，各轴正负均分。X_0=0 为选定 Cell 锚点，不是绝对原点。B_R={X:ΣXi²≤R²}，R=1,2,3；N=0..8，G_N=Σ_{n=0}^N p_n。

边净流为反向两个正访问流之差，是另型读出，不是负 BRC 质量；先定义边界边、累计访问与尾项。无限时间或远距必须有收敛、渐近及误差证明，不从维数或父研究时间n^-2填空间指数。排除 R034/R036 FCC/HCP/Barlow、RS-COORD-LAYER-SHELL 层号及旧隐藏n^-2重跑。

## 2. Hard target and required outputs

交付两核固定R/N的精确表、有限截断守恒恒等式及尾项；证明 Green 极限存在性及空间方向依赖，或返回具体缺失尾控 lemma。写清壳总净流关系与局部结论之间的差距，附精确代码、证明/失败证书和可恢复报告。无限主张不能由有限枚举替代。

## 3. Research value to preserve

父研究的时间返回证据尚不能替代完整X6空间访问与边界输运。本项只建明确两核的离散桥，避免将返回概率时间反平方变为力律或套用未经原生证明的连续球壳公式。

## 4. Success, kill, and return criteria

不能控尾就给具体缺失lemma后停止，不加大半径替代证明。若只得壳总流，局部各向同性和力律明确未识别；方向反例完整保留。固定桥完成即返回，源—探针/物理传播若有新缺口另提，不自动引力研究。发布不授予 Driver 接受、N0 或物理定律。
