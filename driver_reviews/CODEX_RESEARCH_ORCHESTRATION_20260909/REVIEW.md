# 方法论治理有界独立审阅

Status: PASS_AT_STATED_READ_ONLY_SCOPE

本审阅属于 CONTROL_PLANE_MAINTENANCE，不是原 RB 作者 claim 的研究进展或 liveness，也不是正式 Driver verdict。审阅基线为 69d5b1ee44360f770257c461115f1b7cef64f100；范围是原十文件与随后的一处 liveness checker 修正。最终三段退出修订按本地冻结字节审阅，其远端发布状态由发布者另行证明。

未发现仍需阻止此方法论整合的决策级矛盾。两项真实问题已在所读最终字节中修正：

- 旧 checker 强制要求“不因 locator 开 PR”的退休文句，与用户允许通常 PR 工作流不一致。control_plane/check_github_flow_liveness.py:91–98 现检查正常工作流与合并门禁保留；:86–90 的 DURABLE_HANDOFF != OPEN_PR 不变。docs/RESEARCHER_DURABLE_HANDOFF_PROTOCOL.md:79–92 保留检查失败则修复或延后合并，未把 pending CI 改成合并授权。
- 原通用退出句可能使 FREE 等待 Driver 回复。中英 orchestration 文档 :83 及 durable handoff :133 现以适用持久化核验为充分交付依据，明确不新增私聊确认等待或 FREE Driver 审批，同时保留原任务/PRE_FINAL 规则。

对其余关键边界的结论：

- Owner 决定跨线合并、分岔、共享控制与超范围事项；line Driver 在委托范围内负责整条线。docs/CODEX_RESEARCH_ORCHESTRATION.en.md:37–41、:97–107 与 templates/RESEARCH_DELEGATION_PACKETS.md:7–13 未互相授予额外角色。当前对话的组织委托仍不能代替research_driver_authority_contract 的真实来源授权：该合同 :26、:33–39 保留 server-backed AUTHORIZE、活动时有效性和 review pins。此处合同实际路径为 research_driver_authority_contract.json。
- 常驻表示责任与可恢复档案，不表示常驻进程或隐藏记忆；作者参与构造时仍需要另一审阅者，并披露共享上下文。orchestration :57–75、templates/RESEARCH_DELEGATION_PACKETS.md:27–29 没有把换代理名称等同独立审查。
- FREE primitive-only/先冻结后检索在 orchestration :93、:115 明确；普通工具检索与路线汇总句不能覆盖该专门防火墙。
- dossier 和 delegation packet 明示不是 Task/claim/review 权威；实际 V2 发布、claim/ER、source-backed Driver 与原 Result 字节仍受既有合同约束。见 templates/RESEARCH_LINE_DOSSIER.md:3、:22 及 orchestration :45–53、:81、:123。
- 多写者使用独立工作树、受限路径、fresh authority 和非强制 CAS；没有主线锁、覆盖他人写入或以 Git 合并替代数学合并的授权。见 orchestration :119–123。两个 JSON 删除本次新增组织字段后与基线完整语义相等。

证据边界：完整读取四个新文件、六个既有文件的 diff，以及必要的激活/授权合同切片和 checker 增量；未遍历整个控制面。逐一校验十一文件的 SHA256/Git blob，八文件与 publication-v2 全文一致，另外三文件精确匹配发布者提供的退出修订 pins。未重跑数学、40 既有测试、128 双语对或 CI；这些执行事实仅作为发布者回执引用。未独立执行远端回读、运行时委托授权或外部 OpenAI 链接核验。本结论不能替代最终发布 SHA 的适用 CI 准入。
