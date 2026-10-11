# PCF7 当前 Result 控制修复路径：固定 Source 只读审计

结论：固定 Source `d829b7e48451584bf608ad1389261c95324a74d6` 的 ordinary V1 replacement 无法修复 `RR-F97259D79B7E7EF3F69F`。保留三个旧枚举会被新 Result validator 拒绝；改合法枚举会被 V1 replacement 的 exact-core 等式拒绝。旧 flat ER 不在 canonical execution map，新 Result 的现有 receipt 又要求真实目标 Task 的 winning live CLAIM。当前没有暴露 authenticated result-recovery writer。此处是一个真实控制合同/写入口阻断，未解除；不是数学缺口，也不是研究或 parent 完成。

本次只读审计完成。没有 native 调用、CLAIM/会话/任务接管、远端写入、分支、实现、部署、Source 权限变更、ER alias、quarantine 修改、旧成果重写或数学 checker 执行。Root 的合法 PCF Driver GOV 执行可保存这个阻断并交接，但不能由此给目标历史 Result 补写权。

## 固定证据和核验方式

`CURRENT_SOURCE_PINS.json` 保存 21 个定向完整 Source 文件、共 454,021 UTF-8 bytes 的精确路径、bytes、SHA256、Git blob、固定 URL、原 connector wrapper 和本地只读副本。逐个验证 `SHA1("blob " + length + NUL + bytes)` 等于 connector `sha`；所有 URL 指向同一 d829 提交。没有用旧 Source012 字节冒充当前版本，也没有声称完整仓库 intake 或运行生产 gate。

`STATIC_DIAGNOSTIC_PROOFS.json` 是读取固定源码 AST/数据所得的集合与字节证明，不是 native Result、runtime authority、测试 PASS 或平台签名。`EVIDENCE_PINS.json` 固定已复制的原生只读路由、输出核验、404 和旧 DR 审计证据；`EXPOSED_GATEWAY_TOOL_METADATA.json` 保存本次实际可见 gateway 方法的描述与 schema。backend 路由对照来自已冻结 PR24 本地 candidate tree `7aecfa365a94f4c32c0b4cd99231f2c55e178a9a`，不是生产已部署证明，独立列在 `BACKEND_ROUTE_REFERENCE_PINS.json`。

关键对象：Task `RS-PRIME-COORD-FACTOR-COMPLEXITY-FAILURE-CLASSIFICATION-STATEMENT-CORRECTION`，publication `TP2-1C146C521C5946742C17`，RR `RR-F97259D79B7E7EF3F69F`，ER `ER-E90FEF513B0AEE96C73E`，历史 CLAIM `CLM-PCF7FIX-0BFF2D2CD73646AD`，历史作者 `EM-PCF7FIX-B603FA`。当前固定 Task publication blob `520ec677b26a5cd976a7b05406845e1b0f1f053e`、taskbook blob `6a6219a49ea430ed06ba9796c0037e768c993051` 与 RR/quarantine pins 相同，未发现 generation drift。

研究者保存的真实 continuation 路由为 `BLOCKED / RESULT_CONTROL_AUTHORITY_WITHHELD`，`execution_authorized=false`、`claim_id=null`、`session_id=null`、`terminal=false`，role hint `CONTROL_PLANE_MAINTENANCE`、action `RESOLVE_EXACT_RECORDED_CONTROL_BLOCK`。历史 provenance 仍列出旧 CLAIM/ER/作者；它不是当前 actor authority。原始证据副本为 `evidence/NATIVE02_CURRENT_BLOCK_ROUTE.json`。

旧 RR bytes 3890、SHA256 `a926c55a1aaecac16e4d7e4ca575eb3a3e1dcb5452bf19245de213c4a7e63568`、blob `bba0267ffdc7b685517fec9ac809ab8fc715d408`；旧 ER bytes 3119、SHA256 `b9be17cd24da42f4460d1e1b089db70074fdf923ff007fe6d4251d930dece005`、blob `a0ca32627668c826ae1f9ea6fd0d26cff9658f1a`。RR 五项 output manifest 的 return、statement audit、checker replay、flat ER、checker 原 bytes/hash 均有完整核验证据；本审计另取得 d829 checker 完整字节，blob `b2a53c365f442fb2915cd869b77b62d9ce8a9ec8` 与旧 manifest 相同。没有重新执行或接受数学结论。

## 当前合同为何无解

1. `control_plane/research_result_records_impl.py:37` 的三组合法枚举均不含旧值：`BRC_TYPED_ZERO_FLAG_STATEMENT_REPAIR`、`TASK_LOCAL_PROOF_PLUS_DETERMINISTIC_CHECKER_REPLAY_PLUS_EXHAUSTIVE_SMALL_STATEMENT_AUDIT`、`NONBLIND_DISCLOSED_TASK_RESEARCH`。新 freeze 在 328–333 行拒绝，raw audit 在 478–483 行同样拒绝。
2. `research_result_control_replacements.py:29` 的 `_CORE_EQUAL_FIELDS` 明确包含三个域、execution/claim/researcher、Task/publication/branch/taskbook 等；180–182 行要求 raw old/new 精确相等。对每个域，`new == invalid_old` 与 `new in allowed` 没有交集。新 Driver、reason 或合法新 metadata 不能满足矛盾。
3. V1 还要求共同 return/output blobs 相同、manifest 为严格 path superset、新 owner checkpoint、更晚 frozen_at、有效 Driver DA、非平行且无分叉/循环。零 artifact、只换认证封套不符合 strict-superset 条件；添无关文件也不能解决枚举/身份矛盾。
4. `tools/research_execution_records.py:84` 的 `iter_records` 只枚举 `*/*.json`。旧 flat ER 有正确 `record_schema`，但故意不在 canonical map。`freeze_result` 在 315–319 行首先拒绝未知 ER。当前 quarantine 的 flat 分支还要求旧 ER 不在 map，并把它限定为 manifest-bound 诊断证据。移动/复制到 nested 目录、放宽 glob 或做 alias 会改变当前边界，不能当普通修复。
5. `control_plane/research_result_authority_fault_isolation.py:299` 对同 Task/publication/execution 的新 sibling 要求 validated ordinary replacement 链 sink，拒绝绕 edge 添加清洁同 ER Result。public `task_result_state` 在 `tools/research_result_records.py:349` 对 surviving Result 再运行 strict raw audit；仅改变 view 或跳过三项错误仍不足。

当前 quarantine 精确只容许四项既有 raw audit 错误：`unknown execution record` 与三项 invalid enum；没有 scope/artifact drift 豁免。原 RR 已存在于 `control_plane/continuation_record_cutover.json`，exact legacy blob/SHA 与原字节相同。**补 legacy pin 不是缺失修复**；它已经能过 admission 层，但不豁免原 audit/quarantine。新路径仍需 prospective receipt，旧路径任何改字节都会失去 legacy admission。

旧 ER 按当前 `execution_record_id` 公式复算为 `ER-7255D8C2154B0436C12B`，不同于保存的 `ER-E90FEF513B0AEE96C73E`。这是新发现的历史命名诊断；当前已读 audit 并未因此报错，不把它添加到既有 quarantine 错误集合，也不改名/补造对象。

## 现有可见路径与权限边界

| 路径 | 当前实际合同 | 本目标为何不可用 |
| --- | --- | --- |
| `em_session_start` | schema role 只有 RESEARCHER 或 RESEARCH_DRIVER | 没有可注册的 CONTROL_PLANE_MAINTENANCE 或 SourceSteward 角色；新登录也不恢复旧作者/CLAIM |
| `em_context_manifest(CONTROL_MAINTENANCE)` | routing packet，明确 `authority_granted=false` | profile 与 route hint 不授目标写权 |
| 当前 Driver DA / Root GOV CLAIM-open | 自身 session-bound Driver/GOV 控制执行 | 不满足目标 RESEARCH Task 的旧 claimant/session/epoch，不授权修改目标 RR |
| ordinary freeze | current winning live execution + exact ER/Task/claim/researcher + RESULT receipt + candidate-first transaction | 旧 ER map 缺失、三 enums 非法、无目标 live CLAIM；不能借 Root GOV runtime |
| ordinary Driver review | fresh DA/session/contribution independence + operational `result_map` + RR-byte CAS | 被 withheld 的旧 RR 不在该 map；旧 DR 的 ACCEPTED 无法继承 |
| typed continuation | `prepare_takeover` 只收 LEASED 或 NEEDS_DISPATCH，前驱 exact CAS 与新真实身份 | 当前 BLOCKED，不是可 resume/claim 的 slot；也不能补造已404的前驱正文 |
| ordinary V1 result replacement | validated immutable same-execution edge | 对本 RR 三枚举等式无解；模块 CLI `main:282` 只有 audit，无 authenticated writer |
| `docs/LEGACY_BRANCH_RESULT_INTAKE.md` | 复制真实缺失 original bytes，原审计全过；pre-cutover intake 还需 genuine immutable commit 和 authenticated handoff/publication | RR 已在 main 且原 audit 四项失败；旧 exact comments 404，不能造历史认证/receipt |
| 现有历史 compatibility normalization | 精确 RR blob-pinned 允许的 enum 读视图 | 不索引 flat ER、不撤 authority quarantine；V1 replacement 仍读 raw RR；不能自动变成新写授权 |

当前 authenticated gateway 方法全集、冻结 backend `ControlJobs.submit` 的 operation allowlist，以及 ordinary chat contract 中均未见 result-control-replacement/recovery/adoption writer。可见 schema 或静态 allowlist证明的是这些明确路径没有该入口，不能推断所有外部未暴露运维能力都不存在。没有调用服务配置/状态或假定隐藏 scope 已授予。

`control_plane/current_control_authority.json` 明确 CONTROL_PLANE_MAINTENANCE 为控制模式，`NO_RESEARCH_ROLE_IDENTITY`、`NO_THEOREM_OR_REVIEW_AUTHORITY`，verification request 不可 self-publish 为 Task。它保留角色拥有者的数学/Driver/Foundation 语义，不授 SourceSteward 权限。`control_plane/executor_succession_policy.json` 实际启用 prospective freeze/review admission；role activation 也不能隐式跨到历史目标写权。

`control_plane/research_continuation.py:39` 的新 RESULT guard 使用当前时间、真实 runtime/events，比较目标 Task、claim/publication/researcher/branch/taskbook 与 live binding；receipt helper 在 100–137 行重放 raw server comments，经真实 authentication/registered filtering/reducer，要求 LEASED winning ownership epoch 与真实 session。`build_receipt` 是本地证据封装，不是平台签名或通用 capability。现 helper 仅有 RESULT 分支、其余当 REVIEW；不得用任意 kind 借 REVIEW 形状创建 repair 权限。

历史 CLAIM/HANDOFF exact GET `5708985481`、`5709174722` 均 404，有原始证据保存。当前 runtime 的历史索引/作者字符串不能替代当时完整认证正文。旧 derived DR `DR-027ED0C06D7B6A76E0FF` 又有 `review artifact digest drift`，其不可操作 ACCEPTED 只作历史，不重绑新 artifact、不赋新 Result 接受权。

## 最小合法下一步：先新增受限 Source 合同，再实现认证 intake

这不是可以由现有 V1 writer 执行的参数修正。需要由真实有权的 Source 修订流程审阅一个独立、prospective、control-only historical-result intake/re-attestation 合同及 validator/writer；当前报告不给它授权，也不执行。可复用当前 byte/blob 校验、DA/session 验证、不可变 transaction、CAS/readback 与贡献独立性组件，但不能复用 RESULT receipt 冒认旧 live execution。

最小设计必须把两种事实分开：旧数学证据/作者/CLAIM/flat ER 只是 exact immutable provenance；新的维护 actor/DA/session/source/action 是当前控制 intake principal。没有旧 auth 正文时，合同必须明确记录历史身份授权不可恢复；不能“证明”旧执行合法。第一阶段若只建立 current authenticated 控制记录而尚无明确 execution-provenance/admission 规则，必须继续 nonoperational/withheld。不能通过 caller-trusted events、空 owner flags 或只读观察器 as-of absence 解开目标。

候选代码范围建议如下，属于设计需进一步 review 的范围，不是已准备 patch：

- 新独立 historical-result-control-intake contract/schema 与模块（名称待合同确定），规范 exact old RR/ER/Task/pub/taskbook/manifest/quarantine pins、允许的 metadata delta、当前 actor/DA/session、Source/hash/readback、purpose 与 provenance。旧 V1 等式/enum/glob 保持现语义。
- 新 kind 专用 admission/receipt validator 与 candidate-first immutable writer；不走当前 receipt 的 `else -> REVIEW` 路径。原 `research_continuation_write_authority.py` 如接该 kind，必须显式 dispatch，未知 kind 拒绝；既有 RESULT/REVIEW 完整行为保留。
- `tools/research_result_records.py` 与 `control_plane/research_result_authority_fault_isolation.py` 明确消费 fully validated intake linkage；旧 quarantine/原 RR/derived review 仍 immutable/nonoperational，只有独立新对象及专用身份契约成立才进入明示的新 reviewable view。不能仅删 hold、复用同 ER sibling 或跳过 surviving raw audit。
- `control_plane/research_immutable_candidate_validation.py`、当前结果/review 路径需显式辨认新对象的 provenance 类型，不让普通 RESULT_V1 缺 canonical ER 却假装有效。全部 scientific extras、math verdict/strength/constraints、contributor IDs、blindness/exposure 与 Task/lane/output scope 精确保持；新 control handle/ID 及所有下游消费者的兼容性需单独完整核验，当前未完成这一实现级证明。
- 若通过普通/MCP执行，需要 backend actual authenticated handler、ControlJobs/recovery/idempotency/writer 路由、fixed native invocation 对 current genuine actor/DA/session 与 target pins 的同次验证，以及明确 Source 批准的能力/action 映射。公开 profile 不能当 scope；当前 execution:result/review 不能隐式扩权。native code-set reviewed pins 与 Source-authority合同/文档也必须同步审阅，不能自动 update trust map。

允许 delta 应仅是合同列明的三个控制字段和新认证/lineage字段；每个 enum from/to 都需证据、显式保守映射审阅。不要把旧长字符串自动缩成 CLEAN_INDEPENDENT_CONTEXT、BLIND_RAW_FROZEN 或新 tool family。control-only output manifest 可按新合同允许同科学 path/hash 集合，避免捏造 artifact 增量；必须把这种新分支与 V1 strict-superset 分开。mathscope/return/checker/旧 author 和额外保存字段仍全保留。新 Driver 对新 target 的实际独立 review 单独进行，不继承旧 DR，不自动 CLOSED/Working Truth/Foundation/promotion/successor。

写前还需要真实 current-source CAS/non-force transaction、全部 readbacks、适用全入口 fencing/target owner 保护的证明。当前 absence 只是只读 as-of 诊断；若修复改变可领取/ownership 状态，必须证明所有合法 CLAIM ingress 的事务边界或设计为不依赖 absence且遇 owner变化 fail-closed。现有 ControlJobs/control.lock 不是已证明的 all-ingress fence；本报告不把此前 observer/PR1542设计当已 repair。

必要 acceptance：合法 exact pinned intake 只产生合同明示控制效力；三枚举 mapping不足、unknown kind/字段、math/贡献/independence增强、任何 old/scientific byte drift、Task/pub/OG/lane/Source/DA/session漂移、他聊天 live claim、借用旧 receipt/历史时间/角色、别名 ER、无验证 sibling/分叉/循环均拒绝且不写 job/record/hold解除。已有 V1 good paths应保持原结果。丢响应/restart/reconcile只能查原 request/readback，不能重试生成竞争对象。新 review/terminal/followup仍需各自真实原生 gate；intake itself不授这些权限。

## 独立复核与交接

`INDEPENDENT_REPLACEMENT_CONTRACT_REVIEW.md` 为共享上下文、非盲、独立只读子审计；22996 bytes，SHA256 `e163c00539a726c54f4e78926e792023f6fd95cad38763650f9ddec23cf148ac`，blob `0d00ef52212ef0023430d36496d9881b9706ea7f`。它独立核普通 V1/validator/hold/auth receipt 的固定 bytes 与失败路径，没有执行 native或 implementation测试。主审另外核定向政策/真实公开 method schema/Taskpub/当前 cutover 数据；双方均未把设计通过写成实现或权限 PASS。

研究者已经取得的数学证据可完整保存并交给当前合法 Driver 记录阻断；不重做数学、不把旧 self-verdict升格。下一步需要上面的正式 Source 合同/认证 writer设计审阅与新的明确实现授权。当前真实阻断已准确定位并保存，本有界审计及本轮子审计已收尾停止；不停止其他聊天活跃研究，也不把 parent OPEN 改为完成。
