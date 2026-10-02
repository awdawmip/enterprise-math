<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-BRC-X6-LONG-HORIZON-20261003",
  "title": "原生 X6 双向传导与多初值残差的长期数据和可辨识拟合",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "MEDIUM",
  "frontier": "已有单向/重置及特定初值结果；双向慢混合、近周期核和环上不同初值差分尚缺预先冻结的长期留出数据与谱误差核验。",
  "next_action": "冻结至多 24 个有理参数/初值案例与训练留出窗口，先用完整 13 状态律验证精确短时值及可达谱模态，再运行至 n=65536 的首批数据。",
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
    "new_information_gap": "区分双向混合、重置、初值可达模态与投影隐藏造成的长期衰减、平台和周期；识别短窗口拟合在何时仍不可判定。",
    "why_parent_result_does_not_close_it": "旧样本主要为单向核和 e1 对锚点，其无重置全状态 TV=1 源于支撑分离；它不能决定环上初值对、双向核或近退化长混合时间的残差形态。",
    "discriminating_outcomes": "观测到并由谱/精确短时证书支持的混合衰减、周期或平台；或在资源与精度界内仍无法区分候选模型，并给出未识别区间。",
    "kill_condition": "检测到数值精度底、训练留出符号错误、未激活的谱模态或同数据多模型不可分离时，停止相应确定性拟合主张；保留原始差分与失败证据。",
    "alternative_route_or_free_exploration_considered": "已考虑简单延长旧 48 路径、仅做谱分析、转向其他机制或闭合母任务；本任务只扩充旧样本未覆盖且可由谱核验的初值/双向传导单元。",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "这是新的可比较数据批，协议、预算、留出和否定判据独立；不是因上一批完成而自动追加无界样本。"
  },
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-BRC-X6-LONG-HORIZON-20261003",
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

# 原生 X6 双向传导与多初值残差的长期数据和可辨识拟合

## Mother question

在固定六维原生支持和明确观察桥下，多积累哪些数据才能区分残差的混合衰减、重置损失与跨维隐藏？拟合是否稳定取决于初值激活的谱模态，而不只是空间维数或短时幂指数？

## Frozen inputs and scope

进取坐标系没有“平面”。本任务从心跳世界原生六维立体离散 Cell 空间 X6 开始；坐标投影只是同一 X6 状态的读出，不能另立低维空间。立体指完整六维；三维若作为晶包术语须满足其层定义，任意三轴读出不自动成为完整晶包层。读取当前 P000、心跳世界、残差保真和联合关系观察保真契约，并保留上述固定来源。空间维度不作为待拟合参数，不从维数套用经典连续壳层定律。本任务研究演化，显式使用整数更新序号 n；它与空间分别定型，不冒充已标定物理时间。

固定有限支持 S={o,r0,...,r11} 嵌入 X6：o 是选定 Cell 锚点，r_(2j)=e_(j+1)，r_(2j+1)=e_(j+1)+e_((j+1 mod 6)+1)，j=0,...,5。e_i 为六个原生基元方向的内部有符号坐标。相邻环节点差为一个 ±e_i。A(r_i)=r_((i+1) mod 12)，A(o)=o，A^-1 为反向移动；I 为停留；R 将全部状态送到 o。R 是另行定型的多对一重置，不是原生单位步。原生最终地址按既有六非负字段 codec 编码，内部有符号图表不能替代地址定义。冻结

K(a,b,d)=a A+b A^-1+(1-a-b-d)I+d R，a,b,d∈Q≥0，a+b+d≤1。

这是条件研究族，不能声称 P000 已唯一决定传播核或真实世界已属于此族。概率律 μ、ν 非负归一化，差分 δ=μ−ν 可以有符号。旧实验参数 K_old=(1-d)[(1-p)I+pA]+dR 对应 a=(1-d)p,b=0；不得把 a 与旧 p 混用。固定坐标与读出标签；raw、can3、can6 若涉及规范化须分别定义，不可互换。分支有序词的生成规则与来源须可恢复；端点核只支持声明为端点可观察的结论，不能代替历史敏感状态。

完整 13 状态概率律是精确基线。优先复用已登记 T0/BRC 的固定权重仿射二阶矩工具及 E002 行为等价/回拉方法，并检查其适用范围；状态相关作用、非线性作用或全分布问题不自动落在二阶矩闭合范围。本任务不以给既有秩或有限马尔可夫方法改名作为新工具成果。

首批最多 24 个不同的有理参数/初值案例，先冻结清单再计算。必须包含 b>0、d=0 与 d>0、近确定性周期和慢混合情形，并包含环上 r0 对 r6、r0 对 r1 的初值差分；旧 r0 对 o 仅作标记过的比较基线，不算新发现。首批 n=0..65536；仅对预先定义为未决的案例可扩至 n=262144，须记录触发原因与预算。训练和留出区间在运行前冻结，结合可达谱模态估计混合尺度；若最大时域未覆盖相应尺度，就报告未到渐近区而不外推确定指数。任务 RS-BRC-X6-OBSERVER-CLOSURE-20261003 的压缩证书未完成时使用完整 13 状态律；明确已知参数模型不以机制辨识任务完成为前置条件。

## Hard target and required outputs

1. 保存全部 13 状态的 μ_n、ν_n 或可精确恢复的分块数据，同时直接传播 δ_n 以避免两个接近概率律相减的消去误差。保存六个单轴 TV、声明的联合 TV、全状态 TV、非锚点质量、重置/停留账目与可达谱模态。各轴 TV 不能相加冒充守恒量。
2. 对声明的标量读出分别计算方差、四阶累积量 κ4 与标准化 γ；方差为零时 γ 明确未定义，不能填零或与 TV 混为同一残差。
3. 给出独立精确有理短时检查及有限矩阵谱参照，报告舍入/截断界。记录参与拟合的精度阈值、有效样本范围及阈值以下未决点。
4. 比较周期、平台加指数、指数混合及窗口幂律近似，报告训练/留出误差、符号、窗口敏感性和可识别区间；拟合候选不能靠事后更换窗口获得唯一结论。有限图结果不能提升为无限心跳世界的普遍幂律。
5. 交付预登记协议、完整新数据、复现脚本、环境、参数和校验清单、独立审查记录以及 GitHub/Google Drive 的恢复位置。按案例而非只按总行数说明新增信息。

## Research value to preserve

积累能区分机制的新数据，同时保留失败拟合与精度边界；把用户提出的跨维传导因素纳入原生全状态/投影并行记录，而不预设其一定解释所有旧残差。

## Success, kill, and return criteria

成功为至少一组新增条件被可靠区分，或一份有可复现证据的不可辨识/未达渐近报告。到预算上限即返回数据、精度界与未决问题，不无界延长。若模型候选均被证伪，保存结果并回到协议层；不得由短时幂律、符号拟合或原生维数宣布普遍反平方律。完成任务不代表母目标、真实传播律或定理接受已经完成。

## Verified frontier and handoff

已有研究可直接接续：11 类扩展结果位于 46bd4dbe07fa0a7b5b92f612b16b68b70d48e45c 的 experiments/brc_expanded_types_20261002_fca717/；旧标量长期拟合位于 1a50f2e4b522e63bdd6dc2d442f5761c14567655 的 experiments/brc_long_horizon_fit_20261002_9d72ac/（48 路径、4,325,376 行，其原生空间桥的适用范围须单列）。原生 X6 条件模型位于上述 science 来源（42 路径、172,074 行，195 条精确联合传导核验，27 个 parity 演化点及独立审查）。该批已展示单轴读出消失后回返、无重置特定初值下全状态 TV=1、重置衰减，以及低阶联合信息不足的反例；这些都是有条件结果，不能推广为所有核或所有初值的普遍律。

先读取 REPORT.md、PROTOCOL.md、JOINT_TRANSFER.md、parity_results.json 和 manifest.json。完整数据由 restore_data.py 从两个 transfer_series.csv.gz.part 文件恢复并核对清单；不要将分片误当完整 gzip。可移植备份：https://drive.google.com/file/d/15KOVzImnRk0l1tjCMpnphy-hnxBIpmWL/view 。接手者报告来源版本、已经复用的完成单元及真正新增单元；复跑旧数据不能算新积累。结果与可复现源码保存在 GitHub，有价值的新数据另存 Google Drive，记录恢复方法、字节数与校验值；没有实测的远程字节校验不得写成已验证。既有同行审查不等于正式结果接受。
