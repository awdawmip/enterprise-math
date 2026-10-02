<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "GV-RESEARCH-SOURCE-INTAKE-AND-DEDUP-20261003",
  "title": "研究来源恢复与既有任务接续：第三同余、D25 LIFT、BRC X6",
  "kind": "GOVERNANCE",
  "owner": "governance",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "第三同余完整原件及formal parent尚未核实；D25 portable与BRC PR1526已有持久原件但尚需精确范围表和既有任务入口。三个来源单元分别处理，不新增数学任务、不重跑已完成数值。",
  "next_action": "先核当前来源与活动归属；对第三同余恢复原件/真实parent或保留精确来源缺口，对D25映射既有LIFT，对BRC1526映射baseline最高代，并把来源清单与去重矩阵持久接入既有任务入口。",
  "dependencies": [],
  "source_refs": [
    "git:awdawmip/enterprise-math@71d836784c9545867955e1c23cb5a964fc2a0482:driver_reviews/portfolio/EM-DVR-E8DCE5/PORTFOLIO_RECHECK_20261002.md",
    "git:awdawmip/enterprise-math@71d836784c9545867955e1c23cb5a964fc2a0482:driver_reviews/portfolio/EM-DVR-3832A0/PORTFOLIO_HEALTH_AND_INTEGRATION_20261002.md",
    "git:awdawmip/enterprise-math@90ce3ede674740f9039cc56da00bc290b9e23594:research_notes/d25_b_chart_complete_p3_observer_criterion_20261001.md",
    "git:awdawmip/enterprise-math@90ce3ede674740f9039cc56da00bc290b9e23594:research_notes/d25_b_chart_lambda_affine_endpoint_bounded_separation_20261001.md",
    "git:awdawmip/enterprise-math@4c154037884c94edc4773e9b9a92552cd805ea30:research_task_records/RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT/TP2-B6F4FC938FF94941C1B7.json",
    "git:awdawmip/enterprise-math@4c154037884c94edc4773e9b9a92552cd805ea30:research_tasks/RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT_610cb297.md",
    "git:awdawmip/enterprise-math@618def7f5db83928023655ddc211fc9a8f09a7c5:experiments/brc_x6_transfer_20261002_9d72ac/REPORT.md",
    "git:awdawmip/enterprise-math@618def7f5db83928023655ddc211fc9a8f09a7c5:experiments/brc_x6_transfer_20261002_9d72ac/REVIEW.md",
    "git:awdawmip/enterprise-math@618def7f5db83928023655ddc211fc9a8f09a7c5:experiments/brc_x6_transfer_20261002_9d72ac/manifest.json",
    "git:awdawmip/enterprise-math@618def7f5db83928023655ddc211fc9a8f09a7c5:research_activity_records/RA-BRCFIT-20261002-9D72AC.json",
    "git:awdawmip/enterprise-math@4c154037884c94edc4773e9b9a92552cd805ea30:research_task_records/RS-BRC-BASELINE-RESIDUAL-20261002/TP2-2923CB208CCC017ED5A4.json",
    "git:awdawmip/enterprise-math@4c154037884c94edc4773e9b9a92552cd805ea30:research_tasks/BRC_BASELINE_RESIDUAL_X6_REPLAY_20261002.md",
    "git:awdawmip/enterprise-math@4c154037884c94edc4773e9b9a92552cd805ea30:p000_reality_foundation.json",
    "git:awdawmip/enterprise-math@4c154037884c94edc4773e9b9a92552cd805ea30:definitions/ENTERPRISE_JOINT_RELATION_OBSERVER_PRESERVATION_20260905.json",
    "git:awdawmip/enterprise-math@5f7b0e6d44f4abc7d4b56f571d69ba0680ebb7e6:AGENTS.md",
    "git:awdawmip/enterprise-math@5f7b0e6d44f4abc7d4b56f571d69ba0680ebb7e6:p000_reality_foundation.json",
    "git:awdawmip/enterprise-math@5f7b0e6d44f4abc7d4b56f571d69ba0680ebb7e6:definitions/HEARTBEAT_WORLD_NATIVE_X6_TIME.json"
  ],
  "evidence_status": "SOURCE_RECOVERY_AND_INTAKE_ONLY_NO_MATHEMATICAL_ACCEPTANCE",
  "hard_target": "THREE_SOURCE_UNITS_HAVE_VERIFIED_DURABLE_INPUTS_OR_EXACT_GAPS_AND_CANONICAL_EXISTING_TASK_ROUTES",
  "hard_block": null,
  "tags": [
    "governance",
    "maintenance",
    "source-recovery",
    "source-intake",
    "deduplication",
    "no-scientific-rerun"
  ],
  "claim_lease_minutes": 360,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "GV-RESEARCH-SOURCE-INTAKE-AND-DEDUP-20261003",
  "parent_objective_id": "OBJ-ORPHAN-RESEARCH-CONTINUITY-20261003",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "GOV",
  "origin_kind": "MAINTENANCE",
  "task_lineage": "MAINTENANCE",
  "parent_task_id": null,
  "successor_gate": null,
  "parent_objective_generation_id": "OG-FF9106B1F6E23783D19A",
  "policy_review": {
    "temporary_overrides": [],
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:d74aad6dd53d0df42d950f7b1207b27d80696f23410bd06f53a038c459577bb2",
    "review_state": "PASS"
  }
}
-->

# 研究来源恢复、既有任务映射与有界接收

## Mother question

怎样把已经存在但来源或任务入口尚未接齐的三组材料，恢复为可定位、可核验、可由后续执行者消费的持久输入，而不凭摘要创设数学任务、不重复已完成研究、也不把控制接收当作数学接受？

本任务只回答该来源与路由问题。第三同余、D25 LIFT、BRC 原生残差仍是三个不同数学范围；把它们列在同一有界维护批次不建立数学依赖或共同定理。其母目标是本轮真实的研究接续控制目标 OBJ-ORPHAN-RESEARCH-CONTINUITY-20261003，不冒充第三同余的数学 formal parent。

## Frozen inputs and scope

当前全局约束（本轮刷新后的 AGENTS/P000）：所有研究基于心跳世界原生六维立体空间，不存在独立的进取“平面”；历史切片仅作有明确 X6 嵌入或读出桥的受限状态/观察器，并保留声明未来操作所需联合关系。时间按问题需要显式引入并单独定型，静态研究不强制时间字段。旧任务名/旧材料中的 plane 仅作为历史标识保留。

固定 enterprise-math@4c154037884c94edc4773e9b9a92552cd805ea30 与 knowledge@0946b0848601cc59f793de13886903478b72c809；后续执行须另外读取真实当前控制状态，不能以本快照代替 ownership 或权限。P000 固定六个原生空间轴和独立时间。世界及信息缩减语义遵循根 AGENTS、P000、心跳世界与联合关系保真契约。

A. 第三同余来源恢复。两份已固定组合报告记载：作者 portable 摘要不足以恢复完整变量域、四个 follower 约束、证明及真实 formal parent，并提到后续 234-core/Frey 线索。本次审计尚未取得那份原摘要或后续精确原件，因此“24 行”只作为报告中的二手记载，不作为独立实核事实。RS-PRIME-COVER-AP-K3-THIRD-CONGRUENCE-BOUNDARY-20261002 仅是报告所述未出版草稿名，不是本任务可假定存在的研究父任务。禁止从标题猜测 theorem 或 parent。

B. D25 portable 接收。固定 portable/c4d02c-b11-kummer-dilog-20260927@90ce3ede674740f9039cc56da00bc290b9e23594 的既有 23 个独有提交、24 个新增文件。已有数学入口为 RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT / TP2-B6F4FC938FF94941C1B7，目标仍是两类素数 p=13,19 mod24 上 Delta_p=(G_p h-1)/p 与 R_p 的 mod-p 比较。保留 G_p、h 的 mod-p^2 信息、cutoff-sensitive Phi_xx、导数/Frobenius ports 与 provenance；CM0/SIMPLE/UR/JT0 和已接受第一位结果不重开。portable 的 AUTHOR_PORTABLE / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING 不因接收被升级；B11 upper-chart、D24 LIFT 与 1D25/rho_m 不能因名称相近被认作同一对象。

C. BRC 新转移包接收。固定 PR1526 head618def7f5db83928023655ddc211fc9a8f09a7c5，科学原件归档9ab9e44f168c2a36c37c65b950eda13857179677。RA-BRCFIT、RA-BRCAUDIT、RA-BRCMARKOV、RA-BRCWEIGHT 的新 checkpoint 保留旧长区间拟合 checkpoint，并追加六轴传导原件。已有数学入口为 RS-BRC-BASELINE-RESIDUAL-20261002 第7代 TP2-2923CB208CCC017ED5A4，严格匹配重算归档8770476e36a10e79e6b03bdc67af3b5d8d106169已完成。新包是声明核下的条件机制与反例；42 条确定性参数轨迹不等于独立经验样本，TV 不等同 gamma4，三轴投影不等同完整原生态或自动晶包层，reset 与主动宏置换不冒称原生单轴微步。禁止把接收解释为唯一真实核、普遍幂律、Driver/Foundation 接受。

本任务不包含 S15；不得因 xhome RA 空 checkpoint 或记录时间而接管、重跑或判定执行器失活。不得重做已交付图或数值，不新建同义数学任务，不删除原件、不改作者 Result、Claim、Review 或执行归属。

## Hard target and required outputs

硬目标：THREE_SOURCE_UNITS_HAVE_VERIFIED_DURABLE_INPUTS_OR_EXACT_GAPS_AND_CANONICAL_EXISTING_TASK_ROUTES。

1. 形成 Source-intake ledger。每个输入记录 repository、不可变 commit、path、Git blob、SHA-256、来源类型与读取范围。区分本轮实读字节、继承的作者/审计声明、尚未取得的材料；保存原作者、有限证据边界与 negative results。仅使用当前获准的两个仓库及已有支持能力；没有来源时记缺口，不扩大网络/权限或猜来源。
2. 对 A 作一次有界来源恢复：从两份报告的精确引用和当前官方来源目录查找 portable 原文及234-core/Frey后续原件。逐项列变量域、四个 follower 约束、结论、证明、后续关系、正式 parent/Objective 的可核实来源。每项标 VERIFIED 或 MISSING；若找到同名不同范围，保留差异，不强拼。完成后给 SOURCE_RECOVERED_AND_SCOPED 或 SOURCE_GAP_PRESERVED，并写出具体还缺的对象与下一个可执行来源动作。原件或 formal parent 未核实前，不发布第三同余数学 READY。
3. 对 B 建逐项映射表：portable 命题/符号/精度/观察器/未来操作 → 现有 LIFT 的 Delta_p-R_p 目标；每项给 EXACTLY_REUSABLE、CONDITIONAL_WITH_NAMED_MISSING_BRIDGE、OUT_OF_SCOPE 三选一及原件行/节。有限高度 endpoint separation 和 p^3 cyclic observer criterion 不自动关闭全部素数 LIFT。缺精确桥只登记本既有研究入口的最小未完单元，不在本维护任务里补写新证明或扩大扫描。
4. 对 C 把新包与第7代按对象、核、时间、初态、读出、保留联合信息、精确/有限证据逐项比较。明确哪些是匹配旧输出的既有结果、哪些是新条件 counterexample、哪些仍无真实核依据；核对 checkpoint 前缀和 manifest。数据分片若未重组/验全量原始数据，明示这一限制。将来源包和范围表接到现有 baseline 任务的当前可执行入口；第7代或之后已吸收同字节时，记录 ALREADY_INTAKEN，不重复出版。
5. 交付一份不可变来源清单、一份三单元范围/去重矩阵和一个接手说明：已完成且禁重跑的单元、当前 Task/TP2、真实归属检查结果、原件位置、未完最小单元、下一控制动作及可执行/不可执行边界。另一会话仅凭 Source 就能恢复。持久 intake 文件须由已有任务的正式 Source/continuation 入口或合法同 Task-ID 新代引用，并回读验证；单独本地临时文件或聊天链接不算任务机接齐。
6. 如果更新既有 Task 入口需要新 publication，只能沿当前最高唯一代、准确 supersedes 和 canonical preflight/CAS；保护活跃 owner。维护任务本身不授予研究 Claim、Result writer、Driver review、数学接受或 Objective closure 权限。当前契约不支持某写操作时，冻结最小控制缺口并返回，不改旧记录绕过。

建议持久产物为 research_notes/RESEARCH_SOURCE_INTAKE_20261003/{SOURCE_LEDGER.json,SCOPE_AND_DEDUP.md,HANDOFF.md}；最终实际路径由执行者记录。这些文件是证据与路由材料，不是第二任务注册表。

## Research value to preserve

保住真实已经付出的研究工作及负结果：第三同余先恢复可核实语境而不造假 lineage；D25 在现成 LIFT 上证明需要的精确桥而不重复第一位研究；BRC 在已完成第7代上保留新条件传导证据和高阶联合关系边界。让任务机看见现成材料和最小未完单元，减少交接丢失与重复计算；不增加任何数学真值、P000、Working Truth 或正式晋升结论。

## Success, kill, and return criteria

SUCCESS / INTAKE_CONNECTED：B、C 各具有可回读的原件清单、明确范围表和现有任务入口；A 的真实来源与 formal parent 获得核验，或在有界查找后把精确未取得对象持久标为 SOURCE_GAP_PRESERVED。后者只表示来源维护阶段完成/已交接，不表示第三同余数学可执行。三个单元的数学强度、作者和无重跑边界均保持。

ALREADY_COMPLETE：若某来源已被当前最高任务代按相同字节和相同范围吸收，消费现有入口与回读，勿制造重复 Task、重复发布或第二次科研。

BLOCKED：缺失具体原件、合法访问、当前授权、唯一 publication head 或必要 scope bridge，仅阻塞相应单元。写明 missing_object、why_needed、last_verified_source、next_allowed_action；继续独立单元。静态 publication/age/空 checkpoint 不证明 owner 死亡。

KILL / RETURN：禁止根据摘要补造数学约束或formalparent、以同名认同型、以有限测试当全域证明、以无root/新环境为由重跑已有数值、删除 provenance、绕过 immutable/V2/Result authority 契约，或把来源接收完成宣布为数学父目标完成。若恢复材料揭示新数学缺口，只交给既有任务的授权 Driver 决定，不在本任务里自行增设研究阶段。

接手者使用自己的真实会话与当前角色授权，不借前任身份；前任私聊和再次联系作者不是唯一恢复条件。最终返回精确输入、产物 commit/hash、三单元处置、任务入口回读与限制。
