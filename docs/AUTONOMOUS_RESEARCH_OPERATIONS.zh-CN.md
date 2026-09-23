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

## 可发现的接续包

在现有授权 Source checkpoint、Result/review 或控制维护 handoff 中记录：母目标、Task/publication、输入/权威 pin、最高不可变前沿、已完成和不重做项、最小未完项、下一精确动作、逻辑 conversation_id、真实 session/claim/run、未落定 request_id 及原回执 Issue、支持问题及负责路径。不保存私有 key，也不建立第二套任务注册表。

新轮次必须先消费这些已有记录。刚完成一个语义单元，只要父目标仍开放且存在合法下一动作，就在同轮继续；不要求用户再发“继续”，不自行暂停定时任务。平台强制结束时由下一轮恢复，提示词不承诺永久存活的模型进程。

## 控制维护的验收

每个故障签名只建一条可追踪处置，记录实际失败边界、原请求、负责路径、具体下一动作和验证条件。已修复接口必须验证受影响业务到达下一真实状态；修改提示词或关闭支持 issue 不等于完成恢复。若一个任务暂不可执行，按当前授权继续其他可执行研究，并保留该任务前沿和恢复条件。环境欠项不能改写成数学结论或永久的任务准入门禁。

一般状态未变化时不重复通知；有研究成果、实质修复、失败或确需用户动作时再报告。保留原有定时频率和用户通知设定。

相关入口：[普通 Chat 控制](CHATGPT_ORDINARY_CONTROL.zh-CN.md)、[Driver 操作合同](DRIVER_FLOW_OPERATIONS.md)、[跨对话续接](CONTINUE_RESEARCH.zh-CN.md)、[可移植研究交付](PORTABLE_RESEARCH_PROTOCOL.md)。
