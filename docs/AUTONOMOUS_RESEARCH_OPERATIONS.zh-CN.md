# 定时研究：自主执行与断点恢复

状态：ACTIVE。用途是执行编排，不新增任务准入、数学结论或角色权限。研究证据是主要交付；状态说明、支持请求和轮询本身不是研究进展。

## 职责

现有三条 Researcher、一条 Driver、一条控制维护定时任务保留原有时刻。角色数量不代替可执行路径：

| 责任 | 每轮必须完成的动作 |
| --- | --- |
| Researcher | 先恢复本会话未完操作和已授权前沿，实际推进最小研究单元，持久化可核验证据及下一步；无已有工作时才领取新任务。 |
| Driver | 消费已冻结 Result 和精确审阅集合，依当前权限完成审阅、reference passes、synthesis、后继物化或范围闭合，并继续下一合法单元。 |
| 控制维护 | 负责恢复编排、接口缺陷和任务运行状态。将阻断归到一个实际负责路径，修复或送达可执行接续包，并验证受影响路径到达下一真实状态。 |

两类 reference pass 不等于必须再找两位审阅者。已有足够的规范审阅时，不为修传输而追加第三份审阅。作者/贡献者不得借新身份独立审自己的结果；共享上下文必须如实披露。

## 每轮入口

1. 复用仍有效的账户知识库读租约和未变文件，按当前控制 authority、P000 及实际角色读取必要入口。只展开下一动作所需材料。
2. 保持本逻辑 conversation 的稳定 ID；同一对话的上下文压缩不要求新建身份。先查服务 `status` 和公开操作合同；有 `recovery_status` 时先读取它。该入口仅列本 subject 的本地请求/会话指针，不证明当前 Source 所有权或对话存活，也不会自行提交请求。
3. 先处理未知副作用和未完事务，再恢复已有工作，最后才进行 canonical dispatch。上下文丢失后不要凭记忆新发 CLAIM、重复上传/发布或重新注册身份。
4. 新对话使用自己的真实执行身份，通过当前 Task 的 Source continuation packet 接续。原逻辑 conversation 能恢复自己的服务 session，不代表任意新对话可以借用他人的私有能力。

## 真实对话与逻辑身份

一个稳定 `conversation_id` 只对应一个真实执行对话。同一对话的上下文压缩沿用原 ID；新建、复制、fork 或另一个定时任务产生的真实对话不能从历史正文继承其身份。能取得平台 thread/chat ID 时，可用该真实 ID 构成稳定逻辑标识；不能取得时，本对话生成并保全自己的唯一标识，不照抄模板里的示例或其他对话标识。定时提示词不得给多个真实对话预置同一个 execution conversation ID。

发现两个真实对话已经声称同一逻辑 ID 时，将旧 ID/session/request 仅作为有待核验的历史来源，不凭创建先后、任务标题或谁最后回复裁定归属；双方先停止依赖该共享标识的 role-bound 写入。各自保全真实平台 ID、已有贡献和未写成果，通过当前 Source 续接合同核验可接续状态；后续获准执行才使用各自独立逻辑标识与新鲜真实身份，不改绑、关闭、撤销或冒用归属未明的旧 session。身份纠偏不清除已有平台拒绝，也不是换 ID 重试被拒动作的依据；新标识本身不授予 CLAIM、接管权或独立审阅资格。

## 恢复决策

| 已核验状态 | 下一动作 |
| --- | --- |
| QUEUED/RUNNING/POSTING | 回读原请求，不重复提交。 |
| OUTCOME_UNKNOWN/RECONCILE | 对原 request_id 协调并核对实际 Source 效果；不换 ID 重发原写操作。 |
| ADMITTED_NOT_SUBMITTED | 使用原请求的 receipt 恢复既有 admission；不新建同一逻辑操作。 |
| 自己 CLAIM 成功、尚未 open | 用原 claim_request_id 请求 open；先核当前原生授权。 |
| 自己已有 open/resume | 使用恢复指针和当前授权检查；需要时 resume 并采用新的 generation，不重领任务。 |
| 文件已上传、未发布 | 使用已完成末片的 request_id；核对文件与目标，再发布已有证据。 |
| 已发布 checkpoint | 消费确切 Source 字节、已完成/不重做单元和下一动作；未知回执先 reconcile。 |
| 已合法释放或租约过期 | 新授权 session 从规范 continuation 准备并赢得新 CLAIM，再 open；保留原任务和最高有效前沿。 |
| FROZEN/待审阅 | 交当前合法 Driver，不能重新领取已冻结数学单元。 |
| 已关闭或被 fence | 本地旧回执不是写权限；使用新身份和当前 canonical continuation，不复用旧 run。 |
| 校验在 admission 前明确拒绝、未产生 native effect | 读取返回的 operation_contract，修正字段后一次新请求；保留原失败记录。 |

普通 Chat 与标准 MCP 的开放能力以当前 `status` 为准。普通接口未提供某项能力时，不编造参数。已规范释放/租约过期的 RESUME 是无需联系旧研究员的自动接续路径。提前接管 live claim 仍需 Source 接受的真实失活证据与 predecessor CAS；仅凭 600 秒没有服务请求或 UI spinner 不能证明旧对话停止。

当前 owner 在平台截止或真实交接前，先持久化成果和恢复包；适合交接时使用规范 `publish_checkpoint(release=true)`。准备 freeze 时保持 `release=false`，按真实 Result 路径完成。正常执行不为轮询而续租；未持久化内容一律标为 UNKNOWN。

## 工具失败时的读写分离

先判断需要的是读取现状、保存证据还是取得/使用执行权限，不把“某个工具不可见”写成永久任务限制。实际提供原生 `em_status` 时，直接使用这个只读入口；没有该工具时，先通过已有 GitHub 连接读取当前 Source、已存在的原请求和回执。读取这些现存材料不需要先创建新的 Issue，也不产生当前 session/claim 授权。普通 `status/recovery_status` 若走 Issue 请求，传输仍包含创建 Issue 的写动作；仅在当前允许该传输且没有相关明确拒绝时使用。

| 实际失败边界 | 可继续的动作 |
| --- | --- |
| 工具未提供、工具名/参数不支持 | 按当前公开合同选择实际可用且已授权的入口；只读诊断可直接读 Source/原回执，不编造工具、参数或凭证。 |
| 服务在 admission 前返回明确 schema/字段拒绝，确认没有副作用 | 修正返回合同指出的字段，再提交一次；不把 schema 校验拒绝解释成平台安全拒绝。 |
| 超时、断连或返回不完整，是否已经写入不明 | 保留原 request_id，先读原回执与实际 Source；有原生未落定请求时才 reconcile，不换 ID 重发同一逻辑写入。 |
| 平台/宿主明确拒绝动作或要求尚未取得的批准 | 保存拒绝的动作、理由及来源；不换工具、通道、身份或措辞重放被拒动作。没有直接错误输出时，只记“原对话报告拒绝”，不宣称已独立核实。 |
| 已验证需要某项计算/验证能力，而当前未提供 | 冻结输入、可移植代码/证据和预期检查，记录尚未执行的检查；按现有授权继续其他不依赖该能力的研究单元，不把未运行检查写成 PASS。 |

明确拒绝只阻止其覆盖的动作，不自动证明全部研究或全部持久化都不可用。在既有研究授权仍有效的范围内，继续推导、整理可移植证据及可独立推进的单元；不能因此假造 CLAIM、恢复已失效授权或代替独立审阅。若当前授权不允许继续正式研究，仍可在允许范围整理已经完成的成果和下一精确动作，不将其升级成新执行记录或正式 Result。

在已有授权的 Source/知识库/文件产物中保全材料时，标明作者与贡献来源、不可变前沿、未落定请求、未执行检查和 `UNREVIEWED / NOT_ADMITTED` 等真实状态。中立成果保全不授 session、claim、Research-Activity、review 或数学准入，也不代做另一个对话被拒的登记。远端写入同样不允许时，交付可复用完整产物与明确待写位置，不能把准备好的正文报成已写回。

同一拒绝签名没有状态变化时，不逐轮重放等价写入或发送相同阻塞通知。新的用户授权、平台批准/可用性变化或实质不同且更安全的允许动作出现后，再核对适用边界；新授权仍不覆盖平台禁止。保留原定时任务与最小恢复包，由下一轮从最高已核验前沿接续，不要求用户补发“继续”，不另建重复 scheduler。

## 可发现的接续包

在现有授权 Source checkpoint、Result/review 或控制维护 handoff 中记录：母目标、Task/publication、输入/权威 pin、最高不可变前沿、已完成和不重做项、最小未完项、下一精确动作、逻辑 conversation_id、真实 session/claim/run、未落定 request_id 及原回执 Issue、支持问题及负责路径。不保存私有 key，也不建立第二套任务注册表。

新轮次必须先消费这些已有记录。刚完成一个语义单元，只要父目标仍开放且存在合法下一动作，就在同轮继续；不要求用户再发“继续”，不自行暂停定时任务。平台强制结束时由下一轮恢复，提示词不承诺永久存活的模型进程。

## 控制维护的验收

每个故障签名只建一条可追踪处置，记录实际失败边界、原请求、负责路径、具体下一动作和验证条件。已修复接口必须验证受影响业务到达下一真实状态；修改提示词或关闭支持 issue 不等于完成恢复。若一个任务暂不可执行，按当前授权继续其他可执行研究，并保留该任务前沿和恢复条件。环境欠项不能改写成数学结论或永久的任务准入门禁。

一般状态未变化时不重复通知；有研究成果、实质修复、失败或确需用户动作时再报告。保留原有定时频率和用户通知设定。

相关入口：[普通 Chat 控制](CHATGPT_ORDINARY_CONTROL.zh-CN.md)、[Driver 操作合同](DRIVER_FLOW_OPERATIONS.md)、[跨对话续接](CONTINUE_RESEARCH.zh-CN.md)、[可移植研究交付](PORTABLE_RESEARCH_PROTOCOL.md)。

## 旧暂存阻挡继任身份时（0.6.6 能力发现后）

以实际 `status` 和 `operation_contracts` 为准；此节不证明服务已部署。不要循环“新身份被拒 → close 被未发布上传拒绝”，也不要改绑/删除旧证据。仍绑定旧服务 session 的同一实际逻辑 conversation，先协调原未落定请求；没有当前活跃 CLAIM/run 等阻挡时，按公开合同请求 `session_preserve_staging`。控制维护只编排此恢复，不借旧 conversation_id/能力操作研究身份。

中立 archive 无损保全完整/未完整暂存及原请求来源，不是任务 checkpoint、Result、review、当前任务输入或数学进展；原暂存行不改绑。回读原请求成功回执与 `manifest_read` 指向的不可变清单后，独立通过自己的 `session_close`，再在同一实际逻辑 conversation `session_start` 新服务身份并保留贡献历史。保全不自动关闭/撤销权限；UNKNOWN 只 reconcile 原请求。真正新对话使用自己的 conversation_id，不复制旧标识。

恢复后优先消费 Source 的已验证 checkpoint。D24 这类 native frontier 的 `continuation_prepare` 仅用新成功 packet 的 `packet_request_id` 和 `reason`，不重写 frontier。P11 这类初始 publication 输入 seed 则读取精确 seed pin、保留 `completed_units=[]`，既有父成果放来源/不重做项；没有 seed 不用重复父 Result 阅读替代修复。两路均不提前 CLAIM/open、不重算已完成研究。

验收必须分别记录：中立保全完成、own close/新身份与贡献继承、真实任务 continuation_prepare 成功、后续合法执行恢复。单凭 archive、文档发布或支持单关闭，不得宣称科研恢复或成果验收。
