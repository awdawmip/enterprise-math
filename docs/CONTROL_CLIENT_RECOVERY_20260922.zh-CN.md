# 定时客户端：无任务误报与 Driver 续接

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

验证范围：对固定源码中 `require_review_authority` 的原样函数摘录，以显式测试替身代替 Driver authority，执行 11 项隔离测试；本地与 MCP 格式匹配 session 均可通过，缺授权、空／错 session、缺贡献声明及作者重叠均被拒绝。它仅验证该函数契约，不是全库测试、真实授权验收、正式 review 或 native 实验通过。
