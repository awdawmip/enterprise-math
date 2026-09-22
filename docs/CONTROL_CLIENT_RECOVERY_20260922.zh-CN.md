# 定时客户端：无任务误报与 Driver 续接

## 普通 ChatGPT 的直接入口（2026-09-22）

如果当前对话只有 GitHub 工具，没有可调用的项目 MCP 或完整 Source/Python 环境，先用 [普通对话控制指南](CHATGPT_ORDINARY_CONTROL.zh-CN.md) 的私有 GitHub 请求入口。既有服务器运行同一套规范会话、CLAIM、执行记录、Result 和 Driver writer；客户端不再以缺 checkout/CLI 为默认阻塞，也不手工拼接这些权威记录。P000 应从当前有效的 `awdawmip/chatgpt-global-knowledge` 快照读取 `projects/enterprise-math/P000_REALITY_FOUNDATION.json`，不要在本仓库猜路径。

该入口不授予研究角色或数学接受权，当前任务、作者历史、独立性、活跃所有权和准入门禁照常执行。已存在的项目 MCP/native 路径仍可用。需要原生实验环境的数学任务仍须取得真实实验能力与证据；控制入口可用不等于实验已完成。


Status: `ACTIVE_CLIENT_GUIDANCE / NO_NEW_RUNTIME_AUTHORITY / NO_NEW_MATHEMATICS`
Effective: `2026-09-22`
Authority: current `control_plane/current_control_authority.json`, `research_dispatch_contract.json`, `control_plane/research_continuation.py`, and `docs/RESEARCH_DRIVER_OPERATING_CONTRACT.md`. 本文解释现有入口，不修改任务、授权、审查或证据接纳规则。后续源码变更优先。

## 1. 只从本次规范回执判断是否可派发

调用已有 `research_control_dispatch.py`，传入实际完整、稳定的 Issue #240 服务端评论快照；也可使用当前已获准的 MCP 控制入口或现存 ChatGPT dispatch bridge。不得省略事件后运行一个空状态机，也不得把上次聊天、共享 latest receipt、最高优先级任务已被领取或文件搜索为空当成当前无任务证据。

桥接请求与读取必须匹配同一个唯一 request_id；读取 `control_plane/chatgpt_dispatch_receipts/<request_id>.json`，核对 source_sha、kind、generated_at、Issue #240 最后评论和 route。发布 request 不等于收到 receipt，更不等于已领取任务。

客户端必须保留以下区别，不新增 canonical 状态字段：

| 实际观察 | 必须采取的动作／报告 |
|---|---|
| `CLAIM_NEW_OWNER` | 存在可派发目标；按返回的精确任务准备、预检、发布真实 CLAIM 并核验获胜者。不得说无任务。 |
| `PREPARE_SUCCESSOR_CLAIM` | 核验前任 durable frontier，准备真实新执行者和前任 CAS；不是无任务。 |
| `VERIFY_SESSION_LIVENESS` | 核验精确任务／CLAIM 的活动；不是无任务，也不是自动抢占许可。 |
| `SUPPORTED_NATIVE_LANE_ADAPTER_REQUIRED` | 保留 lane 所有权并使用现行专用入口；不是全局无任务。 |
| 真正 `NO_DISPATCH` | 只能说明回执所覆盖的 kind／指定任务／时刻无可派发目标。RESEARCH 不等于 GOVERNANCE，GOVERNANCE 无新任务不等于无待审 RR。 |
| 没有回执、读取失败或运行器不可用 | 报告取得当前状态所缺的具体条件，不能写成无任务。 |
| 已选中任务，但缺少实验宿主或完整验证环境 | 报告任务 ID、精确未完单元、缺失能力及证据；不伪造 BLOCK／DONE，不冒称无任务。 |

研究员不通过 ANY 或 GOVERNANCE 结果自行取得 Driver 权限。Driver 独立检查冻结 Result／review／follow-up，再检查 GOVERNANCE 路由；单个治理目标的宿主障碍不能阻止核验其他独立待审结果。任何替代任务选择仍必须经过当前规范入口，不能人工另建 selector。

### 1.1 能力不匹配的重复派发不是“再次研究”

若本轮匹配的 canonical `RESEARCH` 回执再次返回同一任务，而该任务最近一次已接纳的 durable `CONTINUATION` 明确满足以下全部条件：

1. 数学／文献／证明等实质研究单元已经标记并有证据支持为 `VERIFIED_COMPLETE`；
2. 唯一 `UNFINISHED` 单元只是现行 canonical execution-record／Result freeze、固定 native 实验、完整 latest-main 全库验证或其他明确依赖特定执行宿主的动作；
3. 最近一次执行已留下精确 durable frontier 并明确记录当前同类 ChatGPT 执行宿主缺少该能力；
4. 自该 handoff 后，任务状态、durable frontier、宿主能力以及相关授权没有出现可验证变化；

则客户端不得仅为了再次证明“本宿主仍做不了”而重复创建 CLAIM、重复发布同义 `CONTINUATION`、重跑已经完成的研究或把它误报成 `NO_DISPATCH`。此时准确分类为 `CAPABILITY_MISMATCH_HEAD_OF_LINE`：保留任务为当前 canonical 目标，保留无 owner 状态和已有 frontier，记录所缺能力，等待真正具备该能力的合法执行器。它不是新的 canonical dispatch state，也不改变任务优先级、claimable、数学状态或 Result 状态。

这一规则只抑制**同能力宿主的无信息 claim→release 循环**，不授权客户端人工跳过 canonical selector。若一个能力匹配的执行器随后出现，仍从本轮真实回执和最高 durable frontier 正常领取。同一任务出现新的数学未完单元、前沿变化或能力变化时，也必须重新走普通 canonical 流程。

若该 head-of-line mismatch 持续阻塞其他研究：只有具备当前 source-backed Driver authority 且其 `AUTHORIZE` 含有适用的 typed `research_task_delegation_scope` 时，Driver 才可使用现有 canonical `assigned_research_task` 入口，将**另一个现有当前任务**定向给独立研究员／session；仍需该入口自己的 publication、parent、assignment、CLAIM 和运行时门禁。没有这类明确授权时，不得由研究员、巡检员或普通客户端自行跳过优先级、伪造 `BLOCKED`、修改依赖或建立第二 selector；此时它是需要如实保留的真实宿主能力阻塞。

GOVERNANCE 同理：如果 canonical 治理目标只剩完整 latest-main checkout 中的全库校验，而当前 Driver 宿主没有该环境，应记录 `LOCAL_VALIDATION_PENDING`，不得通过重复 CLAIM／HANDOFF、伪造 review、增加 AUTHORIZE 或把缺 MCP 等同于权限失败来制造进展。Driver 仍继续检查可独立处理的冻结 Result、review/follow-up 和其他已有权限内控制事项。

## 2. MCP 不是 Driver 写入的唯一执行路径

`control_plane/research_continuation.py::require_review_authority` 在本次核验源码中要求：当前真实声明的执行 session、当前 source-backed ACTIVE Driver authority、授权 source_body 与 reviewer_session_id 精确匹配、显式贡献身份声明且与 Result 作者／贡献者无重叠。它没有要求 session 必须采用 MCP 前缀，也没有要求该函数的调用者只能是 MCP 服务。

因此先核对本次实际可用能力。已连接且获准的 MCP 可使用其原生 session／Driver activation／review 工具；有合法完整本地 Source 环境的 Driver 可使用现行原生授权流程及 `tools/research_result_records.py review`。不能因为缺少 MCP 工具就跳过本地原生路径并宣告权限阻塞。

本地路径仍须真实取得本次 Driver 授权，保留真实执行会话来源，并运行 canonical writer 的全部检查。不得把本地声明伪装成 MCP 服务签发或平台认证身份；不得借用他人 session、ID、key 或已撤销授权；不得手造 DA、RR、DR、write_authorization 或可信快照标记。MCP 专有能力凭证的校验在实际使用 MCP 时仍然适用。

若本地合法完整源码／依赖／所需权限确实不可用，准确记录 `LOCAL_VALIDATION_PENDING` 或当前原生错误，并保留可执行的恢复资料。它是尚未解除的环境／权限阻塞，不能仅靠修改提示词、增加 AUTHORIZE 评论或创建一个新 ID 宣称解决。已经完成的独立证据审查可保存为草稿，但草稿不等于正式 review。

## 3. CLAIM 与成果交接不得在格式错误后假成功

使用当前规范身份生成器／预检，不把轮次或多层语义词拼入 Researcher-ID。发布后的真实服务端评论必须被 canonical reducer 接纳为获胜 CLAIM 才取得执行权；ignored CLAIM 不能通过随后的 HANDOFF 变成有效所有权。

对被忽略事件关联的真实分支／报告，单独核验其 bytes 与来源，保留为 predecessor evidence，不追认非法执行权或倒填历史回执。新的合法执行只消费已核验成果、续接最小未完单元，并保留原作者与暴露历史。完成任务范围内可冻结的回传时，使用规范 Result writer 和冻结 HANDOFF 进入 Driver 审查；不能永久只发 CONTINUATION 来代替应有的 Result。

若前沿只剩固定 native 实验，不把已完成的数学规格重新当成新研究，也不为满足每小时数量而自行扩展任务。没有真实 native 运行就不声称已经测量或通过验证。

## 4. 巡检的修复与完成条件

优先修复已证实的客户端错误：错误入口、过时提示、request/receipt 混用、身份预检遗漏和错误状态表述。仅当当前源码确有缺陷时才提交带回归验证的最小代码修改，不新增权限或降低数学门禁。修复后分别报告：规则／提示已发布、规范回执已实际返回、执行／审查是否完成。

2026-09-22 的诊断证据：`EMREQ-CTRL-20260921T224737Z-DIAG-ANY-6C91B2`，generated_at `2026-09-21T22:49:12Z`，source `86d11cbe9631dac8b5d4b65f5cbc8cefa3c6a086`，940 条评论／最后 `5768510032`。实际返回 `CLAIM_NEW_OWNER`，目标为 P0 `RS-GOV-FOUNDATION-BACKFLOW / TP2-2C438651496A928ADCB7`。这是当次有治理任务的证据，不是永久任务分配或无条件执行许可。

该目标当次剩余条件是完整 current-main 环境中的四项原有验证及最小传播，不能重做已完成 R004，也不能整体合入旧 PR #444。此环境条件尚未被本次客户端修复消除。

2026-09-22 00:28Z 的新巡检回执 `EMREQ-CTRL-20260922T0026Z-RESEARCH-PATROL-1A6C3E` 再次返回 `CLAIM_NEW_OWNER`，目标 `RS-PCF-RESTRICTED-ROUTES-EXTERNAL-PRIOR-ART-DUPLICATION-AUDIT`。该任务在 5769197761 的已接纳 `CONTINUATION` 中已经冻结：20-row 实质审计为 `VERIFIED_COMPLETE`，唯一未完单元是需要 full-current-source host 的 `GEN2_CURRENT_PUBLICATION_EXECUTION_AND_RESULT_FREEZE`，而当前同类 ChatGPT 宿主明确没有该环境。因此它是本节 `CAPABILITY_MISMATCH_HEAD_OF_LINE` 的首个记录实例；不应继续用同能力宿主循环 CLAIM→CONTINUATION，也不应由研究员自行跳到别的普通任务。

同一轮 `GOVERNANCE` 回执 `EMREQ-CTRL-20260922T0029Z-GOV-PATROL-4D7B2C` 返回 `RS-GOV-FOUNDATION-BACKFLOW`，其当前唯一推进条件仍是完整 latest-main checkout 上四项原有全库 gate 和最小 Foundation/Common-Surface 传播。该事实确认 Driver 当前首先面对的是 `LOCAL_VALIDATION_PENDING` 宿主能力缺口，而不是 MCP-only review authority，也不是“无 Driver 工作”。

验证范围：对固定源码中 `require_review_authority` 的原样函数摘录，以显式测试替身代替 Driver authority，执行 11 项隔离测试；本地与 MCP 格式匹配 session 均可通过，缺授权、空／错 session、缺贡献声明及作者重叠均被拒绝。它仅验证该函数契约，不是全库测试、真实授权验收、正式 review 或 native 实验通过。

