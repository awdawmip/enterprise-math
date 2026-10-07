<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-PUBLIC-MATH-129-REENTRY-SUMMARY-20261007",
  "title": "Family129二向重入边界摘要与BRC保真证书",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "HIGH",
  "frontier": "已定位 family129 的符号局部接线与有限重入核心；四方向端口摘要的闭包组合、独立证书及向 EM 资源模型的类型化迁移尚未验证。",
  "next_action": "从固定公开源码提取 Network 的机器转移和逐字母 sourceAttach 接线，列出 L→L、L→R、R→L、R→R 端口及 stay/无出口环语义；对照现有关系组合方向并构造首个多次重入精确样例。",
  "dependencies": [],
  "source_refs": [
    "https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a",
    "https://github.com/awdawmip/enterprise-math/blob/9800fa40569c9541ffa8f0c917050cfb067418a3/src/enterprise_math/admissible_support.py",
    "https://github.com/awdawmip/enterprise-math/blob/9800fa40569c9541ffa8f0c917050cfb067418a3/src/enterprise_math/relation_future_powerset.py",
    "https://github.com/awdawmip/enterprise-math/blob/9800fa40569c9541ffa8f0c917050cfb067418a3/src/enterprise_math/relation_observable_composition.py",
    "https://github.com/awdawmip/enterprise-math/blob/9800fa40569c9541ffa8f0c917050cfb067418a3/src/enterprise_math/operation_quotient.py",
    "https://github.com/awdawmip/enterprise-math/blob/9800fa40569c9541ffa8f0c917050cfb067418a3/src/enterprise_math/material_word_quotient.py",
    "https://github.com/awdawmip/enterprise-math/blob/9800fa40569c9541ffa8f0c917050cfb067418a3/enterprise_toolbox_registry.json",
    "https://github.com/awdawmip/enterprise-math/blob/9800fa40569c9541ffa8f0c917050cfb067418a3/research_method_inventory.json",
    "https://github.com/awdawmip/enterprise-math/blob/9800fa40569c9541ffa8f0c917050cfb067418a3/tool_invocation_policy.json",
    "https://github.com/awdawmip/enterprise-math/blob/9800fa40569c9541ffa8f0c917050cfb067418a3/definitions/ENTERPRISE_BRC_MULTIPATH_ENRICHMENT_BRIDGE_20260821.md",
    "https://github.com/awdawmip/enterprise-math/blob/9800fa40569c9541ffa8f0c917050cfb067418a3/definitions/ENTERPRISE_JOINT_RELATION_OBSERVER_PRESERVATION_20260905.json",
    "research_notes/public_math_intake_20261007/LITERATURE_INTAKE.md",
    "research_notes/public_math_intake_20261007/SOURCE_LEDGER.json"
  ],
  "evidence_status": "EXTERNAL_SOURCE_EXPOSED_UNREVIEWED_THEOREM_NOT_ASSUMED",
  "last_progress_ref": null,
  "last_progress_at": null,
  "hard_block": null,
  "tags": [
    "public-literature-intake",
    "family129",
    "two-way-automata",
    "boundary-reentry",
    "BRC",
    "typed-transfer"
  ],
  "claim_lease_minutes": 120,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-PUBLIC-MATH-129-REENTRY-SUMMARY-20261007",
  "parent_objective_id": "OBJ-PUBLIC-MATH-ABSORPTION-20261007",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "PUBLICMATH129",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "NEW_DIRECTION",
  "parent_task_id": null,
  "successor_gate": null,
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:d74aad6dd53d0df42d950f7b1207b27d80696f23410bd06f53a038c459577bb2",
    "review_state": "PASS",
    "temporary_overrides": []
  },
  "parent_objective_generation_id": "OG-9C0E1497D407F544BF64",
  "hard_target": "FAMILY129_REENTRY_BOUNDARY_CERTIFICATE_AND_TYPED_TRANSFER_OR_EXACT_OBSTRUCTION",
  "mathematical_source_refs": [
    "https://github.com/awdawmip/enterprise-math/blob/9800fa40569c9541ffa8f0c917050cfb067418a3/src/enterprise_math/admissible_support.py",
    "https://github.com/awdawmip/enterprise-math/blob/9800fa40569c9541ffa8f0c917050cfb067418a3/src/enterprise_math/relation_future_powerset.py",
    "https://github.com/awdawmip/enterprise-math/blob/9800fa40569c9541ffa8f0c917050cfb067418a3/src/enterprise_math/relation_observable_composition.py",
    "https://github.com/awdawmip/enterprise-math/blob/9800fa40569c9541ffa8f0c917050cfb067418a3/src/enterprise_math/operation_quotient.py",
    "https://github.com/awdawmip/enterprise-math/blob/9800fa40569c9541ffa8f0c917050cfb067418a3/src/enterprise_math/material_word_quotient.py",
    "https://github.com/awdawmip/enterprise-math/blob/9800fa40569c9541ffa8f0c917050cfb067418a3/enterprise_toolbox_registry.json",
    "https://github.com/awdawmip/enterprise-math/blob/9800fa40569c9541ffa8f0c917050cfb067418a3/research_method_inventory.json",
    "https://github.com/awdawmip/enterprise-math/blob/9800fa40569c9541ffa8f0c917050cfb067418a3/tool_invocation_policy.json",
    "https://github.com/awdawmip/enterprise-math/blob/9800fa40569c9541ffa8f0c917050cfb067418a3/definitions/ENTERPRISE_BRC_MULTIPATH_ENRICHMENT_BRIDGE_20260821.md",
    "https://github.com/awdawmip/enterprise-math/blob/9800fa40569c9541ffa8f0c917050cfb067418a3/definitions/ENTERPRISE_JOINT_RELATION_OBSERVER_PRESERVATION_20260905.json"
  ]
}
-->

# Family 129：反复入段时的有限边界摘要与 BRC 观察保真证书

## Mother question

公开 family 129 的二向自动机下界证明，能否提供一个可复用、可检验的有限片段组合证书，准确回答：当后续观察允许从左右边界反复进入同一输入片段时，当前片段摘要究竟必须保留哪些关系？目标是用现有 T0/T6/T8 对实际符号局部接线、停留环与边界重入进行精确重建，并给出适用的状态成本桥或一个明确不满足的假设。不是把标准子集构造、关系复合、词商或经典状态下界换一个名称。

公开论文及配套 Lean 在本任务中都是待核验的外部证据，主定理不作为已接受前提。首轮实际源码精读发现该方向有明确的有限核心；目录同时保留 Partial progress / review unchecked 标记。没有任何内核执行或比较器验收被本任务预先宣告。

## Frozen inputs and scope

公开来源固定 openai/math@adc7f1241b42e322a6451854ab7e4b4c146bf78a，family 129 两篇 September 25 2026 版本：An exponential two-way deterministic state lower bound for one-way liveness；An exponential state lower bound for two-way nondeterministic complementation。完整不可变路径、实际阅读范围和形式化模块映射见同批 research_notes/public_math_intake_20261007/LITERATURE_INTAKE.md 与 SOURCE_LEDGER.json。阅读证明正文、其依赖和实际 Lean 定理声明；标题、宣传、无 sorry 的文本扫描都不等于证明验收。

比较模型：有限集合 X=Fin(h)，h≥2；字母为 X 上二元关系，词按先左后右复合；OWL 的观察为关系积非空。外部二向确定性结论使用一个只读输入头、无可写工作带、完整且随 h 增长的二元关系字母表、所有有限词与存在有限接受运行的语义。目标下界写为 2^floor((h−2)/31) ≤ 4(s+2)^2，s 是该精确定义下的机器状态数。不得把固定 h 的有限检查、状态数、存储比特、时间、输入长度、字母编码长度、预计算表或读写内存互相替代；固定小字母子族和有限词长也不是原 theorem 的全部模型。

EM 数学依赖固定 enterprise-math@9800fa40569c9541ffa8f0c917050cfb067418a3：src/enterprise_math/admissible_support.py，relation_future_powerset.py，relation_observable_composition.py，operation_quotient.py，material_word_quotient.py；enterprise_toolbox_registry.json，research_method_inventory.json，tool_invocation_policy.json；definitions/ENTERPRISE_BRC_MULTIPATH_ENRICHMENT_BRIDGE_20260821.md 与 ENTERPRISE_JOINT_RELATION_OBSERVER_PRESERVATION_20260905.json。采用现有 relation composition 的先左后右约定，显式核对与公开源码方向一致。

已知复用边界：T8 的关系像 R_hat(S)={y:∃x∈S,xRy} 对指定初态、逐字追加与终端可达支持完全精确；T6 已有有限确定性操作族的稳定未来观察分割；material_word_quotient 已有完整函数表的双侧同余。T0 的 PATH_FORMAL_BRC→N_BRC→BOOLEAN_BRC 只允许按声明观察丢掉支路顺序/重数/来源。关系支持和正质量/有符号幅值不可混用。上述工具按输入输出律实际复用，不能以新 family 名义复制。

两个标准回归基线必须分开：(a) 固定初始支持、仅允许追加和非空观察时，至多使用 2^h 个子集状态；若可达所有子集并允许单点后缀测试，该模型的 h 比特区分界是标准子集/未来观察结论。(b) 摘要必须回答任意左、右关系上下文的非空查询时，单点上下文能分辨所有 2^(h²) 个关系，得到该摘要模型的 h² 比特界。这些是经典基线及其有范围的推论，不是新的二向自动机指数定理，也不能把 (b) 强加到只承诺 (a) 的现有编译器。

本任务限定有限、抽象、带类型的 BRC 布尔支持与机器比较接口。全局基础固定 GK main@cde32bc54cccbb9e19da0d54187f4a982848afc4 的 P000_REALITY_FOUNDATION 与 ACTIVE 世界观：原生空间六轴、独立时间、三维切片，无原生二维平面。本任务不宣告这些外部自动机状态就是原生空间坐标，也不改写 P000；若提出原生映射，必须单独定义嵌入/读出、第三切片分量、保持的观察及更新，缺失时保留为外部有限工具。既有残差、D24、U2 等路线不在本任务内。

## Hard target and required outputs

硬目标为 FAMILY129_REENTRY_BOUNDARY_CERTIFICATE_AND_TYPED_TRANSFER_OR_EXACT_OBSTRUCTION。

1. 精确建模：从公开源码取一个机器和一个非空词片段，定义带边界侧、进入/离开方向、机器状态及接受终端信息的有限端口。至少分别保留 L→L、L→R、R→L、R→R 四种有限运行关系，不用单个从指定起点到终点的支持代替。定义 stay 步、停机、拒绝、无出口环与空词的语义，说明有限接受与全局停机的区别。给出符号局部候选槽接线表、确定性 sourceAttach 单射性检查与输入/输出规模。特别核查候选槽的目标接到状态 q，而源只有在该字母的行选择对应转移时接 p，否则接该槽独有的新叶；不能复用同一虚叶，不能读取相邻字母来决定本地接线。

2. 组合定理或反例：为两个相邻片段给出完全显式的有限关系组合算法，内部接缝通过关系闭包处理任意多次往返；证明其与未经压缩机器的有限运行端口关系一致。必须处理重入与 stay 环，不得只验证一次向右经过。若原接线的某项假设不足，给出最小可说明问题的机器/词/端口与具体失败等式，保留所有定义；不要通过悄然加强假设宣布原结论成立。

3. 可检验证书：制定小型证书格式与一个独立检查关系。有限图闭包可用实际可达性见证及不可达割证书，或等价可审阅证明；给出原始图大小、端口数、闭包证书大小、构造和查询成本。至少提供五种精确样例：直接通过、向左返回、接缝多次重入、stay 后退出、无出口环；另有一个仅保留向右终端支持的错误摘要及其区分上下文。尽量沿现有 T8 组合函数与 T6 分割接口执行；未实际运行的验证器或 Lean 构建明确列为待执行支持工作。

4. 两条证据链核对：逐项说明 Network 的 sourceAttach_injective/graph_reach_state、Diagrams 的 diagram_recognizes_reach、Recognition 的 liveness_rank_bound 与 Syntactic 的 matching_recognition_degree 各自输入、结论和上游依赖，查明本任务的有限证书覆盖哪些环节、未覆盖哪些全参数证明。对应 Lean 根定理、导入闭包、Mathlib/Lean 锁定版本及比较器命题对齐单独记录；不能由一次文本扫描或本地有限样例推断完整形式证明通过。

5. 严格迁移判别：为拟议 EM 摘要写出完整接口与资源模型，再给出保持接受语言和资源的显式归约到论文机器模型，或者冻结一个精确不满足的假设及反模型。新增外部内存、随机访问、压缩字母编码、动态观察器、无限状态、不同接受语义或仅有限时域均须单列。没有该归约，就只交付片段证书工具，绝不声称现有 EM 压缩获得指数下界。标准 h/h² 比特基线只作回归对照，不满足本硬目标。

6. 可续接产物：给出一个带不可变出处的研究返回、定义/定理或反例、精确小型输入、实际验证记录、复用判别和最小未完问题。另一个对话仅凭这些材料即可复验与继续；不依赖前任私聊。贡献、公开源码暴露、未核验事项与历史作者保持可追踪；新身份不构成独立审核。

## Research value to preserve

把一个可能重要但尚未验收的公开结果，转化为 EM 可实际检查的“反复重入是否破坏摘要充分性”接口。具体收益是四方向端口与符号局部接线的有限证书，及区分支持、双侧片段行为、状态数和存储比特的可复用边界。T0/T6/T8 的所有权与现成实现继续保留；候选为现有工具的专项组合/扩展，不增设顶层工具家族。即使指数迁移失败，失败的确切模型假设和反例仍是有价值结果。

去重已检查现行工具注册表、方法表、相关可执行源码、现行任务文件名，以及公开库路径和 automata/complementation 关键词；没有发现同一 family129 接线/重入证书任务。检索无结果不是全库无先例的证明。Prefix Instructions and Incompressible Flows 暂不另立任务：已有 RTASK-RF-ORDERED-PATH-RESIDUAL-20260927 处理有序词与条件观察，且其连续流向原生对象的桥未具备；如后续发现相同已完成任务，消费现有结果并精确记录归属。

## Success, kill, and return criteria

SUCCESS：四方向有限端口组合获得证明和明确可检查证书，包含重入、stay 与无出口环回归；论文 proof/Lean 依赖范围忠实核对；并提供一个满足全部列明条件的迁移归约，或一个具体失败前提/反模型，严格限定可吸收结论。成功不要求任何候选都成立，也不要求残差为零。

PARTIAL：有可验证组合定理或反例，但形式化执行、核心依赖核验或资源归约尚缺。保留实际证据与最小下一问题，不把有限证书升级为 h 全域定理。

KILL / RETURN：只复述标准子集构造或 h/h² 比特界；把外部头模型的限制隐去；把任意关系字母当作定长免费输入而据此声称算法加速；把终端可达支持当作可重入片段行为；把无 sorry 扫描、目录勾选或作者声明当内核验收；把类型化外部关系直接叫原生几何证明。出现这些情况应返回范围错误和可修正入口，不伪造成果。若完全等价工具/已受审结果已存在，直接复用并结束重复分支。
