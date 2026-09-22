# 自动研究恢复与跨对话接续

日期：2026-09-23（Asia/Shanghai）。状态：0.6.4 服务、Source 修复、定时提示与科研产物已核验；真实普通网页链已完成 CLAIM → open → 科研 artifact → checkpoint/PROGRESS 的 Source 写回验收。研究任务仍在继续，未宣称全任务完成或数学 Driver Acceptance。

本次用户要求恢复原有定时研究，移除使网页或客户端无法开始研究的环境绑定，并由本机先取得真实科学增量，再提供可跨对话接续的任务。该要求改变交付与执行路径，不降低数学标准或替代真实授权。

## 现在从哪里进入

按当前规范读取并固定 GLOBAL_KNOWLEDGE 快照，必读入口、手册、项目入口及其指向的 P000/ACTIVE 世界观；随后解析当前 Source 任务和交付规则。环境、SDK、CLI、完整 checkout 或指定 MCP 不再是任务书的全局研究准入条件。科学对象确实要求的原生实验仍须真实执行，不能由理论界或替代实现冒充完成。[Portable 研究协议](https://github.com/awdawmip/enterprise-math/blob/38d196107bb68e14bda422d37bee97a854e09798/docs/PORTABLE_RESEARCH_PROTOCOL.md)

普通对话通过现有 private GitHub ordinary-control 入口使用真实服务会话和规范回执。Driver 后半程现有 `review_flow_state`、`review_reference`、`review_synthesize`、`followup_materialize` 四个动作；精确操作字段、证据读取和分页边界按当前指南执行，不从此交接摘要推造 payload。[普通操作指南](https://github.com/awdawmip/enterprise-math/blob/56ad8c023de193aefe3b0494e04d38c31e1af6bd/docs/CHATGPT_ORDINARY_CONTROL.zh-CN.md)、[Driver 后半程指南](https://github.com/awdawmip/enterprise-math/blob/56ad8c023de193aefe3b0494e04d38c31e1af6bd/docs/DRIVER_FLOW_OPERATIONS.md)

## 已完成的交付与控制修复

- 现有服务已激活 0.6.4；MCP PR #7 的代码合入点为 `c515315eb773fbbb91936dd2479b5a30a701f8d5`，后续真实网页验收证据已推进 main 至 `7f2f28beb9a73f30f9f15d39fd3b8f61cf0f9804`。发布代码与已测试的 22 个文件逐一匹配；保留上一 release、受保护配置和数据库，没有通过替换生产数据库来通过测试。[MCP PR #7](https://github.com/awdawmip/em-research-mcp/pull/7)、[部署时验收快照](https://github.com/awdawmip/em-research-mcp/blob/c515315eb773fbbb91936dd2479b5a30a701f8d5/docs/evidence/driver-flow-20260923/DEPLOYMENT_ACCEPTANCE_V064.json)
- Source 最终实现为 `31790ee34e48b7b119f058c3a409070aa435908f`。当前真实 Driver 可跨对话 materialize 已有 review 的后续任务；旧 review/RVS 作者与判断保持原样，当前发布者另存为 `materialization_publisher`，新 Task 的 publisher 使用当前 Driver。DA/session、Result 原始字节、exact review 集合及原始记录 hash 和写入边界复核仍保留。兼容 view 可按现行规则修正 `review_sha256`，不能因此改写或丢掉历史 raw-record pin。[Source 实现](https://github.com/awdawmip/enterprise-math/blob/31790ee34e48b7b119f058c3a409070aa435908f/research_driver_followup.py)
- NFHJPA 的前序证据接续、交付能力判断与当前回执/路由字段已接入合法 Source/native 路径。`session_start` 注册成功会实际分配并回读身份，但该身份不自动授予 CLAIM、Driver authority 或数学验收；单独的 status 成功或功能 enabled 则不分配身份。

软件验收分开记录：宿主单元测试为 **161 PASS、11 opt-in SKIP**；隔离的模拟 GitHub 账本中调用真实 native Source 函数，完成两份既有 review → 跨 Driver reference passes → synthesis → portable Task materialization/dispatch/close 的链，**7 PASS，565.01 秒**。原 review 保留，没有第三份 Driver review，测试没有生产数学任务/CLAIM/review mutation。这证明对应软件链在隔离验收中的行为，不能冒充生产科研 Result 或正式审查已完成。[验收范围与原始回执](https://github.com/awdawmip/em-research-mcp/blob/c515315eb773fbbb91936dd2479b5a30a701f8d5/docs/evidence/driver-flow-20260923/DEPLOYMENT_ACCEPTANCE_V064.json)

上述部署快照中网页验收为 pending，是 **21:49 部署时的历史状态**。后续真实网页链已通过验收；当前 `DELIVERY_STATUS` 为 `DEPLOYED_AND_REAL_SCHEDULED_RESEARCH_CHECKPOINT_VERIFIED`。不得把旧快照的 pending 当作当前阻塞。[真实网页最终验收](https://github.com/awdawmip/em-research-mcp/blob/7f2f28beb9a73f30f9f15d39fd3b8f61cf0f9804/docs/evidence/driver-flow-20260923/REAL_WEB_RESEARCH_ACCEPTANCE.json)

## 已发表的真实科学产物

| 路线 | 已发表、可消费的增量 | 明确保留的边界与下一任务 |
| --- | --- | --- |
| T6 | 全部 16 个 relaxed p17 order-1 affine classes 的 EMPTY 证书；Root 独立消费证书，检查 154 个 proof nodes、170 个 pruning edges。产物与输入已在 `994eec103544ac7476112f992e190ab3c2aade74` 读回核验。 | 不等于原全局 T6 Result 的正式 Driver Acceptance。新的 order-2 family 尚未完成；从 `q2-1` 开始，不能重复 order-1 结果或把部分证书冒称全族完成。 |
| CFD | 同 support/energy 的 polarization counterexample，以及冻结范围内 real/complex noncollinear two-mode stationary classification。产物已在 `bc13cc9121778130499c88a6d82c5515336ec1fb` 读回核验。 | 没有执行原生 CFD benchmark，没有取得正式 Driver acceptance；原生实现/实验仍是独立待验证对象。 |

T6 的新任务为 `RS-T6-P17-ORDER2-PORTABLE-CERTIFICATE-20260923`，publication `TP2-33BFE7DD84657DAB803C`。其 canonical task 回执已显示 READY/NEEDS_DISPATCH；这不等于任何后继对话已经取得所有权。[T6 证明](https://github.com/awdawmip/enterprise-math/blob/994eec103544ac7476112f992e190ab3c2aade74/research_artifacts/T6_P17_ORDER1_SUPPORT_20260923/PROOF.md)、[T6 接续任务](https://github.com/awdawmip/enterprise-math/blob/994eec103544ac7476112f992e190ab3c2aade74/research_tasks/T6_P17_ORDER2_PORTABLE_CERTIFICATE_20260923.md)

CFD 的新任务为 `RS-CFD-POLARIZATION-PORTABLE-CERTIFICATE-20260923`，publication `TP2-222DAF3543772D1782A5`。[CFD 证明](https://github.com/awdawmip/enterprise-math/blob/bc13cc9121778130499c88a6d82c5515336ec1fb/research_artifacts/CFD_POLARIZATION_SUPPORT_20260923/PROOF.md)、[CFD 接续任务](https://github.com/awdawmip/enterprise-math/blob/bc13cc9121778130499c88a6d82c5515336ec1fb/research_tasks/CFD_POLARIZATION_PORTABLE_CERTIFICATE_20260923.md)

两组产物均已关联到 `RA-80D4541C1F650872C900480C`，最终活动记录和三个读回条目在 `558758ed30b208851d3775436f1914dc647de9e2` 核验。该活动记录没有创建 CLAIM，也没有把源码持久化提升成数学推广。[Source 活动记录](https://github.com/awdawmip/enterprise-math/blob/558758ed30b208851d3775436f1914dc647de9e2/research_activity_records/RA-80D4541C1F650872C900480C.json)

## 定时任务的实际状态

五条原 Instructions 已保存，并重新打开逐条核对全文；没有新建 scheduler，没有修改原 frequency 控件、相位、模型、思考强度或通知设置。编辑页面未暴露原始 RRULE/隐藏模型覆盖，因此不伪造这些字段；以下保留已观察的频率。

| 原任务 | Scheduled ID | 已核验状态与频率 |
| --- | --- | --- |
| 每小时研究任务 | `6ab0a26b947c8191a8891e38dd439e26` | 启用；Hourly / Every 1 hour / Never |
| 整点研究任务 | `6ab0a3b850d0819180b25f95a66a75ac` | 启用；Hourly / Every 1 hour / Never |
| 错峰每小时研究任务 | `6ab0a2b3f5dc8191b51d2dd1aa651534` | 启用；Hourly / Every 1 hour / Never |
| 每小时驾驶员审核 | `6ab0a3bf9e588191acb2ff8bf44282b6` | 启用；Hourly / Every 1 hour / Never |
| 每小时控制面巡检 | `6ab1129dc9c08191933c7d0d3da91044` | 启用；Monitoring，编辑页 Repeat Hourly |

Root 在 2026-09-22 21:47 UTC 之后再次从 UI 确认三条研究任务均启用。新提示要求固定已验证前沿、推进一个新的科学增量、持久化证据并继续同母问题下一问。可恢复的工具/环境错误不再触发自我 Pause，也不能被解释为 NO_DISPATCH。巡检须修复原因并核验真实研究路径，不能继续“恢复开关—同一错误—再次停用”的振荡。

## 普通网页验收：科研 checkpoint/PROGRESS 已真实写回

最新研究聊天 ID 为 `6ab2f22d-aa64-83ee-b5d5-334a1c715a70`。它自行产生了 **J1 PARTIAL_ANTECEDENT 草稿**，先前被旧 code 准入阻挡写回；该已产生的科学工作被保留，随后在 0.6.4 下经当前 writer 发布为真实科学 checkpoint，而非重跑旧失败轮或重做既有成果。

0.6.4 部署后，Root 在该最新聊天发送了一次继续消息，复用其真实自身 session；不是对旧失败 run 点击 Retry，也没有重发未知结果的旧 mutation。当前已核验的真实 CLAIM 为：

- Task：`RS-NATIVE-FILAMENT-POSTAUDIT-HYPERBOLA-JOUKOWSKI-EXTERNAL-PRIOR-ART-AUDIT`；publication `TP2-39ACFC69F85D8661CFBF`。
- Researcher：`EM-DIRECT-5DD273`；session `MCP-cd2f0d5e07b24117a4493046af3c3777`；claim `MCP-e5657af5b6968f3c51c632ea`。
- Issue #240 原始 server envelope：comment `5784875267`，created `2026-09-22T21:59:22Z`；source/execution branch base `56ad8c023de193aefe3b0494e04d38c31e1af6bd`。[CLAIM 原始证据](https://github.com/awdawmip/enterprise-math/issues/240#issuecomment-5784875267)
- 这是对旧 claim `CLM-NFHJPA-20260922-0658-1A7C9E` / comment `5768697864` 的合法接续；seed artifact 原始 hash 已核对。上述 ID 用于核验已有证据，不授权后继借用该会话或抢占活跃 owner。

Root 已确认 open 成功、run 获授权及 Source execution intent。`RUN-f68a3d2daeb1914f41b6d479` 的 checkpoint 请求 `checkpoint-20260923-0608-c71d-25` 已收到完整 **SUCCEEDED** 回执，`canonical_publication_verified=true`；Root 对 Source `33e6a1ba9c299c7c20a5a9dd9a6be6edeea8d038` 的三个 artifact 逐一核验了 Git blob。相应 PROGRESS 为 Issue #240 comment `5784961711`。[终态回执](https://github.com/awdawmip/kimi-query-bridge/issues/782#issuecomment-5784966379)、[PROGRESS](https://github.com/awdawmip/enterprise-math/issues/240#issuecomment-5784961711)

三项实际产物的 blob 为：J1 审计正文 `13299f94ba47be9e7e1daface3180dcdf88e762a`、本次 `_checkpoint.json` `888b78daf3b9b48d3a046e47e3bf40090c2bc722`、任务 `latest_checkpoint.json` `494807fefa3648b75311ba2c108e3887ee0e2dff`。[已发表 J1 审计正文](https://github.com/awdawmip/enterprise-math/blob/33e6a1ba9c299c7c20a5a9dd9a6be6edeea8d038/research_artifacts/mcp/RS-NATIVE-FILAMENT-POSTAUDIT-HYPERBOLA-JOUKOWSKI-EXTERNAL-PRIOR-ART-AUDIT/MCP-cd2f0d5e07b24117a4493046af3c3777/a6c13cc2576dd668c5da/J1_EXTERNAL_PRIOR_ART_AUDIT_20260923.md)

本轮作者把 **J1 的 generic image mechanism** 定位到精确外部先例，但**整体 J1 仍为 PARTIAL_ANTECEDENT**。这是作者的有来源研究进展，不能冒称独立 Driver review 或最终新颖性判决。`formal_task_complete=false`、`mathematical_acceptance=false`；后续 Result/freeze 与独立审查继续按正常研究流程处理。

GK 普通对话入口也已更新到 0.6.4；后继应按当前入口读取，而不是将较早快照中的服务版本当作唯一现状。[GK 入口更新](https://github.com/awdawmip/chatgpt-global-knowledge/commit/1192e8835267898c6749ca6021b6653deef53d61)

## 下一位执行者应做什么

1. 保持现有定时设置，消费已有证据，不再重复 Run now 或抢占活跃 owner。对最新网页会话只跟踪同一当前请求链；按真实 route 处理并发变化。
2. 消费已确认的 CLAIM/open、run 和已发表 checkpoint，不重新领取或重复发布同一进展。继续审计进取数论特定的 J1 saturation/recombination 层 `Im Λ_s ⊆ J_s`，其中 `J_s={-r,…,r}`、`r=(s-1)/2`；没有在已审计集合中找到匹配最多支持 `NO_MATERIAL_MATCH_IN_AUDITED_SET`，不能据此声称全球新颖性。保持当前任务运行，不 Stop 或关闭它；新增证据经正常持久化与独立 Driver 流程消费。
3. Driver 从已有 Result/review 集合恢复最小缺项，使用当前自己的身份完成必要 reference/synthesis/materialization。环境支持请求和 portable 后续任务沿现有授权路径处理，不改数学 scope、P000、source pin、来源隔离、贡献历史、证明强度或独立审查标准。

本交接分别记录了隔离 native 验收与真实网页科研写回证据，不将前者冒充后者；也不承诺所有数学任务 DONE、未执行实验完成或未经审查的后台成果已获数学验收。
