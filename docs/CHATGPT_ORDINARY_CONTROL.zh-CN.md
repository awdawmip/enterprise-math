# 普通 ChatGPT：通过 GitHub 推进研究

Protocol: `EM_CHAT_CONTROL_V1` · English: [CHATGPT_ORDINARY_CONTROL.en.md](CHATGPT_ORDINARY_CONTROL.en.md)

普通 ChatGPT 使用已有 GitHub 连接提交请求，服务器调用既有 Enterprise Math 原生控制程序，再把回执写回原 Issue。**对话无需 Python、CLI、git clone、完整 checkout 或可见的项目 MCP 工具，也不切换到 Work。** 对话仍负责研究、证据判断和审查意见；控制传输成功不证明数学正确。服务实际开放范围先看 `status` 的 `enabled`。

## 1. 准确入口与请求格式

先建立账户知识库当前有效 `main` 快照，在该固定 SHA 读取 `awdawmip/chatgpt-global-knowledge` 的 `00_BOOTSTRAP.md`、`OPERATING_MANUAL.md` 和 `projects/enterprise-math/00_EM_PROJECT_BOOTSTRAP.md`。**P000 的准确入口是同一个知识库 repository、同一个 SHA 下的 `projects/enterprise-math/P000_REALITY_FOUNDATION.json`。** 不在 Enterprise Math 全树猜 P000 文件名。之后按角色读取当前 `awdawmip/enterprise-math` 的控制合同和精确任务；知识库、当前控制 Source、冻结研究证据分别固定，不相互覆盖。

在私有 `awdawmip/kimi-query-bridge` 一次创建 Issue，带 `em:control` 标签，标题为 `[EM-CONTROL] <request_id>`。**正文必须恰好一个 `json` 代码围栏**，其中一个 JSON 对象；不加说明文字、不用裸 JSON。以下为只读 `status` 示例，使用时替换为本对话稳定标识与新的唯一请求 ID：

```json
{"schema":"EM_CHAT_CONTROL_V1","conversation_id":"chat-example-20260922","request_id":"status-20260922-example-01","operation":"status","payload":{}}
```

| 字段 | 规则 |
|---|---|
| `schema` | 固定 `EM_CHAT_CONTROL_V1` |
| `conversation_id` | 本对话自选稳定逻辑 ID，1–160 字符，字母/数字开头，后可用字母、数字、`: / _ . -`；不是平台认证身份 |
| `request_id` | 一次逻辑操作唯一 ID，1–128 字符，字母/数字开头，后可用字母、数字、`_ . -` |
| `operation` | 下表的实际操作名 |
| `payload` | 只含该操作允许字段；未知字段会拒绝 |
| `sha256` | **可省略，普通对话默认省略**。服务器总是计算并回传；显式提供但错误会拒绝 |

摘要算法是去掉 `sha256` 后，递归排序对象键、紧凑 JSON、非 ASCII 原样 UTF-8、无末尾换行的 SHA-256；客户端不需要计算，更不能猜。重复 JSON 键、NaN/Infinity、凭证字段均拒绝。服务核验私库及受信任 GitHub actor、创建时正文、执行前双读指纹和持久化幂等状态。

创建后不要编辑 Issue 正文、标题或标签，也不要给同一逻辑操作新建重复 Issue。请求首次受理要求创建与更新时间一致且在 24 小时内。每个 conversation 最多 5 个未结束请求，通常逐步发送。普通 payload 最多 16 KiB，规范 envelope 最多 32 KiB；长证据使用分片上传。

## 2. 回读及只读操作

首次等约 30 秒读取原 Issue，执行中约每 15 秒检查。服务评论含 `EM_CHAT_CONTROL_RECEIPT_V1` 和 `<!-- em-control:... -->` 标记。核对 `issue_number`、`conversation_id`、`request_id`、服务端 `request_sha256`；内层 `bridge_receipt` 含 `operation`、`status`、`receipt`、`error`、`next_actions`。**外层 `adapter_status=COMPLETE` 也可能包装 FAILED/OUTCOME_UNKNOWN，不表示研究成功。** 以匹配内层回执及实际 Source readback 为准。

| operation | payload 必填 | 可选字段与用途 |
|---|---|---|
| `status` | 无，`{}` | 返回操作名、enabled、当前 conversation 服务会话；不授予研究权限 |
| `dispatch` | 无 | `kind`: `RESEARCH`（默认）、`GOVERNANCE`、`ANY`；可选 `priority`: `P0`、`P1`、`P2`、`P3`；省略保留普通路由，显式 null 拒绝；核对原生 `selection_filter` |
| `pre_final` | `parent_liveness` 和下述对应路径字段 | 只读调用原生最终回复门；注册、freeze、review 或 close 成功不等于允许最终回复 |
| `tasks` | 无 | `limit` 默认 20、1–100；`cursor`、`dispatch_state`；分页复用返回 cursor |
| `task` / `continuation` | `task_id` | 精确任务/续接包；有现存会话时服务自动绑定 |
| `artifact` | `packet_request_id`, `path` | `start_char=0`, `char_count=12000`（最多 24000）、`source_commit`、`related_start=0`；依赖成功的 continuation/artifact/publish_checkpoint 请求，只读允许的证据 |
| `receipt` | `target_request_id` | `start_char=0`, `char_count=12000`（最多 24000）；读取本 conversation 目标回执的完整 JSON 分页 |
| `reconcile` | `target_request_id` | 协调本 conversation 已有请求的未知远端结果，不重复原动作 |

例如接续查询的 payload 为 `{"task_id":"<实际 Task-ID>"}`。长回执有 `receipt_truncated=true` 时，用新的只读 `receipt` 请求分页；按 `next_start_char` 续读，保存 `sha256` 和 `source_status`。分页的文本不是完整结果时不声称已全读。`artifact` 的完整字节哈希核验也不代表对话已经读完所有页。

QUEUED/RUNNING/POSTING/RECONCILE 时继续读原请求；OUTCOME_UNKNOWN 时发 `reconcile`，不换 ID 重做写入。只有实际规范 `NO_DISPATCH` 才支持对应 kind/时刻无派发；没有回执、权限错误、无宿主、活跃 owner 或待审 Result 都不是“无任务”。

## 3. 服务会话与研究员顺序

已有同 conversation 会话先用 `status` 查看并继续，不为每个操作重新创建。确需新执行时，`session_start` 的普通研究员示例为：

```json
{"schema":"EM_CHAT_CONTROL_V1","conversation_id":"chat-example-20260922","request_id":"session-20260922-example-02","operation":"session_start","payload":{"role":"RESEARCHER","research_mode":"TASK_RESEARCH","prior_contribution_ids":[]}}
```

`task_id` 可省略；若有旧贡献身份，必须填入 `prior_contribution_ids`，示例空数组只表示确实没有既往贡献。Driver 用 `role=RESEARCH_DRIVER`、`research_mode=RESEARCH_DRIVER`。角色/模式不允许混搭；一个 conversation 同时只有一个未关闭服务会话。服务生成 session、Researcher/Driver ID、CLAIM、ER、publication/taskbook pin、generation 和授权；**对话只传前一步 request_id，不抄 pin、不手拼身份，不传 session_key。** 私有 session key 保存在服务器，不写 GitHub。

研究员通常执行 `dispatch → session_start → prepare → claim → open → artifact_upload → publish_checkpoint → freeze`。每步必须先拿到前一步 SUCCEEDED 并检查实际任务和约束；注册或 prepare 成功不等于取得 CLAIM。

| operation | payload 必填 | 行为/注意 |
|---|---|---|
| `prepare` | `dispatch_request_id` | 指向成功 dispatch；仅按其合法 route 准备。可选 `execution_branch` 只能是 `main`，`allowed_outputs` 只能为空，通常省略 |
| `prepare_exact` | `task_request_id` | 指向成功 task/continuation；适合已明确 Task，仍执行原生可执行性与所有权检查 |
| `claim` | `prepare_request_id` | 指向成功 prepare/prepare_exact/continuation_prepare；核对真实获胜 CLAIM |
| `open` | `claim_request_id` | 指向成功 claim；取得当前执行授权，**该 open 请求 ID 用作后面的 `run_request_id`** |
| `resume` | `run_request_id` | 同会话恢复已有 open/resume；成功后用新 resume 请求 ID，旧 generation 失效 |
| `artifact_upload` | `upload_id`, `filename`, `part_index`, `content` | `final=false` 默认；末片必须 true。只暂存文本，不执行上传程序 |
| `publish_checkpoint` | `run_request_id`, `upload_request_ids`, `completed_units`, `current_unfinished_unit`, `next_action`, `do_not_repeat` | `release=false` 默认；成功发布后 PROGRESS；`release=true` 则在发布后交 CONTINUATION 并释放。**准备 freeze 时保持 false** |
| `freeze` | `run_request_id`, `publication_request_id`, `return_filename`, `metadata` | publication_request_id 指向本 run 的成功 publish_checkpoint；return_filename 是其中自己的文件名 |
| `session_close` | `reason` | 有待处理请求、活跃 CLAIM 或未发布上传时拒绝；先持久化/合法交接 |

上传的 `upload_id` 和 `filename` 为 1–96 字符简单名称（字母/数字开头，后用字母、数字、`_ . -`，无目录斜杠）。每个文件从 `part_index=0` 连续递增，最多索引 128；每片最多 16000 UTF-8 字节且 JSON 转义表示不超过 24000 字节，中文长文宜切小片。单文件最多 1 MiB，一次最多 16 文件、共 4 MiB。每片用新的请求 ID；相同文件各片沿用 upload_id/filename。`upload_request_ids` 填每个文件**最后一片 complete 成功请求**的 ID，不填 upload_id，也不填全部片 ID。

checkpoint 中 `completed_units`、`do_not_repeat` 是字符串数组；`current_unfinished_unit`、`next_action` 是非空字符串。如准备最终 Result，明确剩余的是正式封装/独立审查，不填假“全部完成”。证据发布后由服务返回完整 immutable blob URL；不采用“branch@commit + path”自定义串。

`freeze.metadata` **恰好七项，均由研究者根据真实证据明确填写**，由原生合同核验类型/取值；不能把测试样例 PASS 作为默认：

| metadata 字段 | 必须表达的实际内容 |
|---|---|
| `terminal_verdict` | 本任务书范围内实际终局判断，不代替父目标完成 |
| `hard_target_disposition` | 硬目标实际满足、未满足或受限的判断 |
| `unresolved_residue` | 尚未证明、验证或完成的残余及范围 |
| `method_harvest` | 实际方法收获/可复用物或其明确缺失 |
| `independence_status` | 真实独立性与贡献重叠情况 |
| `source_exposure_status` | 真实来源暴露/盲性状态，不因新 ID 清零 |
| `next_control_plane_recommendation` | 按当前任务合同所需审查/续接建议 |

服务从已授权当前 run 派生 ER、正确 taskbook pin 和 write_authorization；原生 Result 通过准入、Source 发布及完整 readback 后，才发 frozen HANDOFF。上传成功、草稿 RR、错误 pin 或无授权回执不能提前冻结。成功 freeze 仍是等待独立 Driver review，不是数学接纳。

## 4. 已有前沿的接续

先用 `continuation` 和允许的 `artifact` 核对已完成/未完/损坏/未知单元；不重做有效成果。`continuation_prepare` 当前只支持**已有规范释放、无 live claim、runtime.dispatch_state=NEEDS_DISPATCH** 的前任；不支持通过客户端自报失活抢占。

必填 `packet_request_id`（成功 continuation）、`reason`。如果包已有 `persisted_checkpoint.state=SOURCE_BYTES_AND_RECORDED_CLAIM_VERIFIED`，只传这两项，服务保存原 frontier，不接受覆盖。旧格式前沿还需 `artifact_request_ids`（已实际完整 hash 核验的 artifact 请求 ID 数组）及 `frontier_notes`（恰好 `completed_units`、`current_unfinished_unit`、`next_action`、`do_not_repeat`）；至少一个证据必须属于包内认证的 last progress，贡献来源由服务继承。准备成功后仍走 claim/open。受限来源/专用 lane 或 frozen/活跃状态按返回路由处理，不能强制 reopen。

## 5. Driver 正式审查

使用独立的 Driver conversation/真实服务会话，保留全部贡献身份；新 ID 不证明独立性。顺序为 `session_start(RESEARCH_DRIVER) → driver_activate → continuation → artifact(精确 Result及证据) → artifact_upload(报告和所需 followup spec) → driver_publish → review`。已有已授权会话继续使用，不反复激活。

| operation | payload 必填 | 可选项/校验 |
|---|---|---|
| `driver_activate` | `reason` | `previous_authority` 默认 null；Chat 接口不支持借此替换现存 Driver，非 null 拒绝 |
| `driver_publish` | `upload_request_ids` | 自己会话的报告及 followup spec 最后完整上传请求 ID |
| `review` | `publication_request_id`, `result_request_id`, `review_filename`, `metadata` | `followup_spec_filename` 可选，但首次规范 review 需要已发布的原生 followup spec；不能用空占位代替 |

`result_request_id` 必须指向 Driver **本 conversation 成功的 `artifact` 请求**，其路径为实际 `research_result_records/<Task-ID>/<Result-ID>.json` 且完整底层字节 hash 已核验；不是 worker 的 freeze 请求。大 Result 分页读完必要内容后再审查。桥服务从这个实际 artifact 自动派生 `result_id`、`expected_result_sha256`；对话不计算 SHA，也不手抄这两个字段。

`review.metadata` 必填 `disposition`、`destination_class`、`reviewer_contribution_ids`，可选 `destination_ref_or_none`（默认 null）。结论由 Driver 独立证据审查决定，服务不会自动填 ACCEPTED 或选择后继。规范 writer 仍检查真实 ACTIVE DA、session 一致、Result 作者/贡献者隔离、最新 Result 字节及 HEAD 并发绑定。报告发布不是正式 review；正式回读后继续核对实际 review/followup，不能因 PASS 自动创造新任务或宣称父目标完成。

## 6. 常见错误的下一步

| 错误/状态 | 下一动作 |
|---|---|
| `ONE_JSON_BLOCK_REQUIRED` / `EXACT_CHAT_OPERATION_FIELDS_REQUIRED` | 核对单 JSON 围栏/字段表；确认未受理后用新请求 ID 修正，别编辑旧 Issue |
| `ENVELOPE_HASH_MISMATCH` / `CHAT_REQUEST_SHA256_MISMATCH` | 不猜 hash；确认拒绝后按新 ID 省略 sha256 |
| `PREREQUISITE_NOT_SUCCEEDED` | 读原依赖请求到成功或明确失败，再决定后续；不跳步 |
| `CHAT_SESSION_START_REQUIRED` | 先完成本 conversation 的 session_start；不借旧 key |
| `CHAT_ACTIVE_SESSION_EXISTS_USE_EXISTING_OR_CLOSE` | status 查看并继续已有会话；确需结束时先完成交接再 close |
| `CHAT_DEPENDENCY_SESSION_MISMATCH` / `CHAT_RUN_SESSION_MISMATCH` | 核对本会话依赖链，不能复制别人的 request_id 或旧 generation |
| `STALE_EXECUTOR_GENERATION` / `CANONICAL_CLAIM_FENCED` | 先读当前 continuation；只按合法所有权恢复，不重发旧写入 |
| `CHAT_CONTINUATION_REQUIRES_NATIVE_RELEASE_NO_LIVE_TAKEOVER` | 保留当前 owner/frozen 状态，走规范控制恢复；不是无任务 |
| `COMPLETE_OWN_UPLOAD_REQUIRED` | 检查末片 final=true/complete 和正确的最后片 request_id |
| `EXACT_NATIVE_FREEZE_FIELDS_REQUIRED` | 补齐恰好七项真实 metadata，不能伪造 PASS |
| `VERIFIED_RESULT_ARTIFACT_REQUIRED` | 从本 Driver continuation 实际读取合法 Result artifact，别直接提交猜测 hash |
| `*_DISABLED` / 权限或原生准入错误 | 记录具体能力/权限和 Task/未完单元；不伪造授权、不改称 NO_DISPATCH |
| `OUTCOME_UNKNOWN` / `SUBMIT_UNKNOWN` | 保存原请求及成果；读原 Issue并 reconcile，不以新 ID重复写入 |
| `receipt_truncated=true` | 用 receipt 分页读取，不把热路径摘要当完整原始材料 |

状态/错误修复不许可修改历史事件或手造 DA/ER/RR/DR。P000、FREE 防火墙、任务范围、Working Truth/Foundation、作者与验证者区分全部保留。

## 7. 验收边界

只读 canary 使用 status、精确 continuation/artifact，并省略 sha256；不要为了展示链路新建假任务、领取活跃任务或激活假 Driver。正式闭环仅在原任务当前合法 dispatch/owner 与用户授权下进行，独立区分“请求受理”“研究正式冻结”“Driver正式审查”和“数学/实验验证”。

服务器控制接口不提供任意 shell，也不运行上传的数学代码；pinned spectralDNS/shenfun/MPI/FFTW、Lean 等真正实验仍需实际宿主和任务指定证据。环境缺失时保存前沿与最小未完单元，不重复数学来凑次数。不得仅凭服务测试/提示发布宣称原普通 ChatGPT 已验收成功。

## 8. 最终回复前的只读检查

最终回复前，通过同一 GitHub 通道提交 `pre_final`，由服务器运行已准入 Source 的 `tools/research_runtime_guard.py` 原生判据。freeze/review 成功或 session_close 都不代替 PRE_FINAL。`status=SUCCEEDED` 仅指评估完成；必须读取 `receipt.result.final_allowed` 与 `required_action`。false 时继续指定动作。该检查不授数学或执行权限。

- 正式任务已冻结或已交接：传本会话成功 open/resume 的 `run_request_id`、成功 freeze 或 release=true 的 publish_checkpoint 对应 `completion_request_id`，以及 `parent_liveness`。已经冻结/关闭的历史 run 仍可检查，不重新授权已结束研究。服务器校验真实回执、session 与 Source 执行意图，并从当前 Source 推导父目标是否关闭；客户端填 COMPLETE 不能覆盖。其它正式状态暂不支持，不冒称完成。
- 无正式 run 的 Driver 控制工作：传自己的 `session_request_id` 与 `parent_liveness`；可选 `research_mode` 只能为 `RESEARCH_DRIVER`。该 Driver session 已有正式 run 时必须走正式路径。
- 本逻辑会话从未发行研究 session 的维护工作：传 `research_mode=CONTROL_PLANE_MAINTENANCE` 与 `parent_liveness`。不能删去既有研究绑定降级走维护路径。

`parent_liveness` 保留真实原父目标，严格包含八个布尔字段：`parent_objective_complete`、`user_requested_stop_pause_review_or_wait`、`parent_hard_blocker`、`platform_or_tool_hard_limit`、`independent_safe_work_exhausted`、`same_action_repeated_without_state_change`、`supported_alternative_available`、`parent_state_recomputed_without_change`；另有非负整数 `executable_next_actions`，可选布尔 `continuation_lease_active`。不得为获得 final 而虚构用户停止要求或硬限制。正式父目标完成状态由 Source 独立推导；closure 未核实时明确返回 false 和修复/核对动作。保存回执中的 Source pin 与 evaluated-state hash。


## Portable research delivery (2026-09-23)

Follow [PORTABLE_RESEARCH_PROTOCOL.md](PORTABLE_RESEARCH_PROTOCOL.md) for scheduled research and task authoring. A missing execution environment does not prevent mathematical reasoning or automatically disable a schedule. Preserve actual pending native checks and publish a precise portable next question.

## 2026-09-23 续接修复补充

新回执以 `delivery_requirements` 公开交付要求，不暴露任何私有 capability。若 `continuation_seed.state=CURRENT_TASK_INPUTS_WITH_NO_RECORDED_OWNER_PROGRESS`，表示当前可信 Source 中的任务初始输入仍未被可验证的 owner 进展替代。读取其 `input_artifacts`，将成功的本会话 `artifact` 请求传给 `continuation_prepare.artifact_request_ids`，并提供真实 `frontier_notes`；此路径的 `completed_units` 必须为空，不能把初始输入当作前任完成成果。仍需匹配 Task/publication/前任 CLAIM/comment 并取得新 CLAIM/open；有活跃 owner 或来源隔离时不得绕过原路线。

已关闭、从未 CLAIM/open 的真实 Researcher 会话也可用自己的 `session_request_id` 和真实 `parent_liveness` 请求 `pre_final`。服务保留 Researcher/RA 类型并复核当前 Source；存在下一研究动作时返回 `final_allowed=false` 和 `next_research_route`，继续研究。这个入口不授予完成状态，也不是伪装为维护会话的退出通道。
