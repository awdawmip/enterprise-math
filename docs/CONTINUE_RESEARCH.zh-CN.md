# 在任意新对话接续研究任务

## 普通 ChatGPT 的直接入口（2026-09-22）

普通 ChatGPT 默认使用 [普通对话控制指南](CHATGPT_ORDINARY_CONTROL.zh-CN.md) 的私有 GitHub 请求入口，不要求可见的项目 MCP 或完整 Source/Python 环境。既有服务器运行同一套规范会话、CLAIM、执行记录、Result 和 Driver writer；客户端不再以缺 checkout/CLI 为默认阻塞，也不手工拼接这些权威记录。P000 应从当前有效的 `awdawmip/chatgpt-global-knowledge` 快照读取 `projects/enterprise-math/P000_REALITY_FOUNDATION.json`，不要在本仓库猜路径。

该入口不授予研究角色或数学接受权，当前任务、作者历史、独立性、活跃所有权和准入门禁照常执行。已存在的项目 MCP/native 路径仍可用。需要原生实验环境的数学任务仍须取得真实实验能力与证据；控制入口可用不等于实验已完成。

默认请求写入私有 `awdawmip/kimi-query-bridge` 的 `em:control` Issue（`EM_CHAT_CONTROL_V1`、正文一个 JSON 围栏），从**原请求 Issue**读取匹配 request/conversation/operation/hash 的内层回执。旧 `control_plane/chatgpt_dispatch_receipts/<request_id>.json` 仅属于显式选择的旧 dispatch bridge 兼容模式，不与新入口混发。下文 `em_*` 调用说明适用于已显式选择直接 MCP 的客户端；普通 GitHub 对话按指南使用对应 operation 和请求依赖，不因后文出现 MCP 名称退回旧入口。


任务和证据保存在 GitHub 状态机；驾驶员、研究员和 MCP 执行会话是可替换的执行者。新对话只需连接本项目 MCP，并具备目标角色的授权，不需要找到原代理或读取它的私聊。

可以直接说：

> 通过 MCP 接续任务 `<Task-ID>`。先核对当前状态、已完成工作和未完单元，使用本次会话的真实身份，按所需角色继续；保留全部来源和数学边界。

不知道 Task-ID 时，先用 `em_control_tasks` 查看任务；已知 Task-ID 时，直接用 `em_control_continuation` 获取该任务的接续包，避免每次全量扫队列。异步操作返回 request_id 后用 `em_control_result` 获取实际结果。列表分页复用同一只读快照，标明 source、事件和观察时刻；准备执行或写入前仍重新核验当前状态。

## 1. 先取证据，再决定动作

接续包包含当前任务书、publication、运行状态、需要的角色、有效结果／审阅、固定证据位置、已知交接和下一动作。通过 `em_control_artifact` 分页读取包中允许的文件。主线的控制版本与研究分支的证据版本分别绑定；固定 GitHub 链接仍须实际读回并核对哈希，不能把分支内容冒标成主线。

| 状态 | 新对话的动作 |
|---|---|
| NEEDS_DISPATCH | 登记自己的会话，核对角色后准备领取；已有前任的先核对其前沿 |
| AWAITING_REVIEW | 激活自己的驾驶员权限，读取精确冻结结果并进行所需审阅 |
| LEASED | 核对真实活动；活跃执行器受保护，失联且达到规则阈值后才准备接管 |
| BLOCKED / DORMANT | 读取具体原因，区分证据／权限／完整性问题与真正数学障碍 |
| COMPLETE | 消费已完成或被替代的记录，不重做已完成单位 |

原角色 ID、署名和来源保留为历史。新对话不能借用旧身份，也不能因为旧人不在就把阻塞任务改为已解决。

部分历史冻结结果仍在旧分支。若接续包返回 `LEGACY_BRANCH_RESULT_INTAKE_REQUIRED`，先按 [旧分支结果接入协议](LEGACY_BRANCH_RESULT_INTAKE.md) 使用已授权 GitHub 连接，定位、核验并接入原始字节，再进入 MCP 原生审阅。仅有 PR／分支提示时仍需查证；不能制造结果记录，也不能重新派发已经冻结的研究。

## 2. 登记本次执行会话

调用 `em_session_start`，显式选择 RESEARCHER 或 RESEARCH_DRIVER，必要时指定任务和既有贡献身份。每次新的执行使用新的唯一 request_id；同一操作的重试才复用该 ID。

MCP 生成真实的服务执行会话和角色 ID，并通过规范工具发布 Source 登记、完成真实回读。它不假装知道或签名证明平台聊天 ID；可选 host session 声明只是来源信息。研究员使用规范 RA；驾驶员使用自己的 session 和独立 DA，不伪造研究员 RA。

返回的 session_key 是私有能力凭证，不能写到 GitHub、交接材料或公开报告。公开 session/RA 记录不是持有该 key 的证明。重复常见请求名不能重新获得另一会话的 key；丢失首次响应可新建尚未领取任务的空会话。已有会话的幂等恢复需要原有 key。

驾驶员继续调用 `em_driver_activate` 取得相应规范权限。角色登记、准备计划和读取材料都不自动赋予 CLAIM、数学接纳、Working Truth 或 Foundation 权限。

## 3. 领取或接管

对无有效前任的可执行任务，用 `em_task_prepare` 按精确 Task-ID 准备；也可保留全局调度路径。对需要接续的旧执行，用 `em_continuation_prepare` 带入精确前任 CLAIM／服务端事件和已核验前沿，再显式调用 `em_execution_claim`。成功回读获胜者后，用 `em_execution_open` 获取当前执行绑定。

新的执行使用自己的真实身份和 ER，Task-ID、publication、任务硬目标和已完成证据不被重置。接管按认证事件顺序作前任 CAS；只有一个获胜执行，旧 CLAIM 的新写入失权。角色是 Driver 的治理任务使用 Driver session 和当前 DA，不以研究员模式冒充。

活跃会话不能被另一对话自报的“已经失联”抢占。STALE 判断采用实际已接纳的 owner 活动，默认阈值为 600 秒；临近活动会给出 retry_after。已有真实 CONTINUATION HANDOFF 则按释放状态 RESUME。保持同一会话的 transport resume 与真正跨会话接管分开。

## 4. 进度、结果和审阅都能从 MCP 写回

通过 `em_artifact_upload` 分块暂存自己的文本／代码证据，再显式调用 `em_execution_publish`。服务只写固定任务／会话命名空间，核验当前所有权、版本和 Source CAS，完成完整回读后才发 PROGRESS 或 CONTINUATION HANDOFF。已声明完成的单位、最小未完单位、下一动作、不要重跑的内容及贡献来源必须清楚。

提交结果时使用 `em_execution_freeze`，规范 writer 生成绑定当前权限的 RR，Source 成功发布和回读后才发冻结返回 HANDOFF。驾驶员通过 `em_driver_publish` 保存自己的报告与规范 followup spec，再用 `em_driver_review` 运行真正的审阅／后续动作事务。服务不会替审阅者选择数学结论，也不会因 PASS 自动创建后继任务。

这些写回接口不提供任意远程 shell，也不执行上传的数学程序；所需计算／检查能力在任务包中明确。MCP 原有 transport checkpoint 单独存在时，不等于 Source 已同步。

写入响应不明时先用 `em_control_reconcile` 查真实远端结果，不凭超时重复提交。结束时先保存并交接，在 `em_session_close` 中结束自己的能力和适用的 DA；旧成果和历史审阅仍保留。新对话从同一 Task 的最新有效前沿继续。

## 最终回复检查

普通 GitHub 对话结束检查时使用指南中的只读 `pre_final`：正式已冻结/交接任务传 `run_request_id`、`completion_request_id`、真实 `parent_liveness`；无正式 run 的 Driver 传自己的 `session_request_id` 和 parent_liveness；只有从未发行研究 session 的维护会话可用维护模式。读取 `receipt.result.final_allowed` 和 `required_action`，false 时继续指定动作；注册、freeze、review、close 或评估 SUCCEEDED 均不代替此门，不能虚构停止要求或将正式研究降级为维护来结束。

## 保持不变的边界

P000、FREE 信息隔离、作者与验证者区分、任务数学范围、Working Truth／Foundation／晋升门禁全部保留。新 ID 不证明独立性，接续包和文件哈希不证明数学正确。历史 RR/DR 保持原字节和原审计；切换后的新记录需要规范写入授权回执，旧客户端无回执或已失权的写入不能改变规范任务状态。

精确合同见 [续接协议](RESEARCH_CONTINUATION_PROTOCOL.md)、`control_plane/executor_succession_policy.json` 和 `control_plane/current_control_authority.json`。

当前 MCP 接管接口覆盖任务级 CLAIM。若包返回 `SUPPORTED_NATIVE_LANE_ADAPTER_REQUIRED`，保留现有 cohort/lane 权限并按其原生专用入口操作，不能用全局任务接口替代。


## Portable research delivery (2026-09-23)

Follow [PORTABLE_RESEARCH_PROTOCOL.md](PORTABLE_RESEARCH_PROTOCOL.md) for scheduled research and task authoring. A missing execution environment does not prevent mathematical reasoning or automatically disable a schedule. Preserve actual pending native checks and publish a precise portable next question.
