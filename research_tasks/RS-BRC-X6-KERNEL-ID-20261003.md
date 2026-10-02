<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-BRC-X6-KERNEL-ID-20261003",
  "title": "原生 X6 残差传导核的可辨识性与额外观察设计",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "MEDIUM",
  "frontier": "已证投影隐藏与回返，但仅凭单轴读出能识别哪些传播参数、哪些联合观察可分离等价核尚未确定。",
  "next_action": "冻结 13 状态核族及初值 δ_r0，精确计算单轴 x1 概率律在 n=0,1,2 的参数表达式，检验 a↔b 对称并寻找可分离的第二读出。",
  "dependencies": [],
  "source_refs": [
    "awdawmip/enterprise-math@2c56c3618dcbe2d65ad4c34bf1839d350759ac90:research_tasks/BRC_BASELINE_RESIDUAL_EXPANDED_TYPES_20261002.md",
    "awdawmip/enterprise-math@7035c8011938aa0baffbb22f3827322053f520d5:p000_reality_foundation.json",
    "awdawmip/enterprise-math@7035c8011938aa0baffbb22f3827322053f520d5:definitions/HEARTBEAT_WORLD_NATIVE_X6_TIME.json",
    "awdawmip/enterprise-math@7035c8011938aa0baffbb22f3827322053f520d5:research_notes/BRC_NATIVE_X6_SEMANTIC_ALIGNMENT_20261002_9D72AC.md",
    "awdawmip/enterprise-math@9ab9e44f168c2a36c37c65b950eda13857179677:experiments/brc_x6_transfer_20261002_9d72ac/REPORT.md",
    "awdawmip/enterprise-math@9ab9e44f168c2a36c37c65b950eda13857179677:experiments/brc_x6_transfer_20261002_9d72ac/PROTOCOL.md",
    "awdawmip/enterprise-math@9ab9e44f168c2a36c37c65b950eda13857179677:experiments/brc_x6_transfer_20261002_9d72ac/manifest.json",
    "awdawmip/enterprise-math@9ab9e44f168c2a36c37c65b950eda13857179677:experiments/brc_x6_transfer_20261002_9d72ac/REVIEW.md",
    "awdawmip/enterprise-math@2c56c3618dcbe2d65ad4c34bf1839d350759ac90:definitions/RESIDUAL_FAITHFUL_DISCRETE_RELATIONAL_SYSTEM.json",
    "awdawmip/enterprise-math@2c56c3618dcbe2d65ad4c34bf1839d350759ac90:definitions/ENTERPRISE_JOINT_RELATION_OBSERVER_PRESERVATION_20260905.json",
    "awdawmip/enterprise-math@2c56c3618dcbe2d65ad4c34bf1839d350759ac90:enterprise_toolbox_registry.json",
    "awdawmip/enterprise-math@2c56c3618dcbe2d65ad4c34bf1839d350759ac90:lineage_e002_predictive_quotient.json"
  ],
  "evidence_status": "PUBLISHED_RESEARCH_QUESTION_NOT_RESULT",
  "last_progress_ref": null,
  "last_progress_at": null,
  "hard_block": null,
  "tags": [
    "BRC",
    "native-X6",
    "residual-fidelity"
  ],
  "identity_lane": "BRC",
  "created_by_role": "RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "parent_objective_id": "BRC-BASELINE-RESIDUAL-LAWS",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-BRC-BASELINE-RESIDUAL-20261002",
  "successor_gate": {
    "new_information_gap": "从投影时序反推传播核的可辨识参数与不可辨识等价类，以及打破等价所需的最小额外观察。",
    "why_parent_result_does_not_close_it": "母任务和后续 X6 反例给定传播核后展示残差变化，没有证明观察数据可唯一反推出核；相关性也未自动成为因果响应证据。",
    "discriminating_outcomes": "给定观察与初值方案下唯一识别；只能识别参数组合；或精确不同核产生相同全部允许数据，并由新增读出或初值分离。",
    "kill_condition": "出现两个不同参数核在规定全部数据上不可区分，立即终止该方案的唯一识别主张；改交等价类或不可辨识证书。",
    "alternative_route_or_free_exploration_considered": "已考虑闭合母任务并只保留反例、继续无约束加长拟合，以及另开不依赖该条件核族的探索；本任务选择先精确检验当前读出能提供的信息。",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "机制辨识与数值扩样有不同输入、证书和终止判据，可独立有界完成，避免把新增数据量误当机制已识别。"
  },
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-BRC-X6-KERNEL-ID-20261003",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "policy_review": {
    "temporary_overrides": [],
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:d74aad6dd53d0df42d950f7b1207b27d80696f23410bd06f53a038c459577bb2",
    "review_state": "PASS"
  }
}
-->

# 原生 X6 残差传导核的可辨识性与额外观察设计

## Mother question

在固定 X6 内，单轴残差时序究竟能分辨哪些跨维传导机制？先研究完整投影概率律的辨识能力，再比较只保留 TV、方差或标准化累积量时丢失了什么；不得把投影衰减直接解释为六维总残差消失。

## Frozen inputs and scope

进取坐标系没有“平面”。本任务从心跳世界原生六维立体离散 Cell 空间 X6 开始；坐标投影只是同一 X6 状态的读出，不能另立低维空间。立体指完整六维；三维若作为晶包术语须满足其层定义，任意三轴读出不自动成为完整晶包层。读取当前 P000、心跳世界、残差保真和联合关系观察保真契约，并保留上述固定来源。空间维度不作为待拟合参数，不从维数套用经典连续壳层定律。本任务研究演化，显式使用整数更新序号 n；它与空间分别定型，不冒充已标定物理时间。

固定有限支持 S={o,r0,...,r11} 嵌入 X6：o 是选定 Cell 锚点，r_(2j)=e_(j+1)，r_(2j+1)=e_(j+1)+e_((j+1 mod 6)+1)，j=0,...,5。e_i 为六个原生基元方向的内部有符号坐标。相邻环节点差为一个 ±e_i。A(r_i)=r_((i+1) mod 12)，A(o)=o，A^-1 为反向移动；I 为停留；R 将全部状态送到 o。R 是另行定型的多对一重置，不是原生单位步。原生最终地址按既有六非负字段 codec 编码，内部有符号图表不能替代地址定义。冻结

K(a,b,d)=a A+b A^-1+(1-a-b-d)I+d R，a,b,d∈Q≥0，a+b+d≤1。

这是条件研究族，不能声称 P000 已唯一决定传播核或真实世界已属于此族。概率律 μ、ν 非负归一化，差分 δ=μ−ν 可以有符号。旧实验参数 K_old=(1-d)[(1-p)I+pA]+dR 对应 a=(1-d)p,b=0；不得把 a 与旧 p 混用。固定坐标与读出标签；raw、can3、can6 若涉及规范化须分别定义，不可互换。分支有序词的生成规则与来源须可恢复；端点核只支持声明为端点可观察的结论，不能代替历史敏感状态。

完整 13 状态概率律是精确基线。优先复用已登记 T0/BRC 的固定权重仿射二阶矩工具及 E002 行为等价/回拉方法，并检查其适用范围；状态相关作用、非线性作用或全分布问题不自动落在二阶矩闭合范围。本任务不以给既有秩或有限马尔可夫方法改名作为新工具成果。

以已知、可重复准备的初始点质量集合为输入，至少处理单一 μ0=δ_r0 和增加一个预先声明的初始点两种方案。观察首先为 x1 的完整投影概率律，额外候选为其他单轴及显式联合读出。比较的是同一初值方案下的不同核参数，不可同时任意改变未知核与初值后宣称辨识。冻结观察时窗、采样点及精确/有噪声条件；有限时窗结论不得写成所有时刻结论。

## Hard target and required outputs

1. 给出核、允许初值准备、读出与时间窗口的协议表，以及精确参数到概率律的映射。
2. 证明可识别参数/等价类；不可识别时交付不同有理参数、相同允许观测及验证证书。若声称所有 n 等价，须给出结构证明或有限维可验证判据，不能仅穷举前若干步。
3. 在事先冻结的有限候选读出/初值集合内求最小附加方案，并证明必要性；做不到则只报告一个充分方案。比较同步联合统计与受控初值响应，不能由协方差直接推出因果方向。
4. 在精确证书之外给出近退化点的灵敏度、舍入阈值和可恢复性边界；保存原始投影律与参数，不能只留拟合曲线。

## Research value to preserve

把“未测维度可能接收残差”变成可检验的观察设计与不确定性边界。新增价值是这一原生嵌入条件族的明确参数等价类和分离证据，不是宣称实际物理机制已经识别。

## Success, kill, and return criteria

成功可以是有证明的辨识方案，也可以是准确的不可辨识证书及可分离扩充。若真实测量或传播律未提供，明确返回“仅完成条件模型辨识”；不虚构经验支持。遇到既有同题定理，复用并列出本原生读出实例的增量；若没有增量则结束任务并保留来源。返回已证范围、未决输入和具体可执行下一动作，不默认开启另一阶段。

## Verified frontier and handoff

已有研究可直接接续：11 类扩展结果位于 46bd4dbe07fa0a7b5b92f612b16b68b70d48e45c 的 experiments/brc_expanded_types_20261002_fca717/；旧标量长期拟合位于 1a50f2e4b522e63bdd6dc2d442f5761c14567655 的 experiments/brc_long_horizon_fit_20261002_9d72ac/（48 路径、4,325,376 行，其原生空间桥的适用范围须单列）。原生 X6 条件模型位于上述 science 来源（42 路径、172,074 行，195 条精确联合传导核验，27 个 parity 演化点及独立审查）。该批已展示单轴读出消失后回返、无重置特定初值下全状态 TV=1、重置衰减，以及低阶联合信息不足的反例；这些都是有条件结果，不能推广为所有核或所有初值的普遍律。

先读取 REPORT.md、PROTOCOL.md、JOINT_TRANSFER.md、parity_results.json 和 manifest.json。完整数据由 restore_data.py 从两个 transfer_series.csv.gz.part 文件恢复并核对清单；不要将分片误当完整 gzip。可移植备份：https://drive.google.com/file/d/15KOVzImnRk0l1tjCMpnphy-hnxBIpmWL/view 。接手者报告来源版本、已经复用的完成单元及真正新增单元；复跑旧数据不能算新积累。结果与可复现源码保存在 GitHub，有价值的新数据另存 Google Drive，记录恢复方法、字节数与校验值；没有实测的远程字节校验不得写成已验证。既有同行审查不等于正式结果接受。
