# 新任务启动控制面复核 / Startup context re-audit

Status: `AUDIT_COMPLETE_WITH_CONFIRMED_GAPS`
Conclusion: `BOUNDED_END_TO_END_STARTUP_NOT_ESTABLISHED`
Observed: 2026-09-17
Mode: `CONTROL_PLANE_MAINTENANCE`
Audited source: `awdawmip/enterprise-math@0db088a3b5793269ddcdd15a3d9a7996d3f9fff3`

## 结论与范围

新任务仍有重新触发大量上下文的具体路径，特别是会话存活核验、并行通道、恢复旧进度、字符串依赖和超大任务书。普通新任务并非必然重复此前43次文件读取；本次没有测得新会话的实际延迟或token消耗，不能给出这一保证或预测。

沿入口、派单投影、领取解析、执行授权、恢复、预算和桥接路径进行了源代码/契约核对。精确复原当前任务包生成器及其原有测试，Git blob与连接器返回相同，然后本地运行5项原有核心测试（全部通过）和12项定向探测。没有完整仓库检出及完整当前事件流，没有运行全仓库归约/授权测试，也没有创建真实新会话或真实领取。这里的“审计完成”不表示整个状态机已经被证明正确。

## 已有有效机制

- 上次缺包处理配置修正仍存在，配置blob为`a3f5f2f988c2f5d990468837516658fd9264a299`；它是配置/路由说明，不是新加入的可执行防重发分支。已检查的任务包生成器和预算检查器不消费该fallback字符串。
- 任务书blob不一致时，任务包生成器拒绝生成。
- 任务书投影过大时整体退回原任务书，不截断五个权威章节。
- 对实际序列化后的UTF-8包体检查8192字节上限。
- 大块隔离/活动/事件诊断不默认复制到任务包；未知依赖不自动遍历目录。
- 当前领取解析器仍只接受原始JSON正文；授权守卫仍要求当前真实获胜CLAIM、版本与输出范围匹配。此两项为源码核对，不冒充全运行时测试。

## 已复现缺口

| 编号 | 输入到现有生成器 | 实际输出 | 启动影响 |
|---|---|---|---|
| G1 | 规范派单器的`VERIFY_SESSION_LIVENESS`含`targets` | `task=null`，`targets`未保留 | 小包无法说明核验谁，必须展开完整回执 |
| G2 | 规范`COHORT_LANE`目标含cohort/lane编号 | `surface/target_key/execution_cohort_id/execution_lane_id`未保留 | 无法仅凭小包准确绑定并行执行范围 |
| G3 | ADOPT目标有更新的`last_progress_ref`及`required_guard` | 普通分支不保留这些字段，首依赖仍来自旧publication/metadata | 恢复者可能先读旧进度，再补查控制层；不是证明其一定重跑 |
| G4 | `dependencies=["research_returns/R1.md"]`或加`@main` | 即使本地对应文件存在，首依赖也为null | 已知依赖被漏掉，引发额外检索；字典形式正对照可以识别 |
| G5 | 大任务书且包体投影退回外置文件 | 包1842字节通过，任务书200533字节不纳入此包体限制 | 包体合格不代表端到端输入受控 |

G5是隔离构造样例，不是声称实际新任务有200533字节。至少202375字节的“包+任务书”可以同时存在，而生成器仍成功；任务书内容不得为省预算而删除，正确处理应是显式任务材料预算和有来源的分段读取。

G1/G2的输入形状来自`research_control_dispatch.py:route_from_candidates`；G3来自`_adoption_result`和包生成器的固定字段白名单；G4来自`_first_dependency_ref`只遍历字典依赖的实现。测试探测用隔离fixtures，不宣称这些输入在当前队列中实际获派。

## 仍存在的入口和计量压力

1. 全局规范入口、操作手册与TASK入口的blob未因上一轮单行修正而改变。此前“5—7份”只是基本入口估算，不能当成包含活动登记、领取协议、工具描述和异常核验的实际承诺。
2. TASK入口要求走紧凑路径；AGENTS在解释/修改控制字段前又要求读取`current_control_authority.json`。对注入AGENTS的宿主，需要明确普通TASK启动与真实控制维护的边界，不能依赖模型自行化解展开压力。本次主动读取AGENTS是控制审计，不是新研究者必须照做的示例。
3. `check_context_budget.py`检查静态文件长度、预算配置值和五项组件上限之和，不接收本次会话的读取事件。`normal_remote_source_reads_before_math_max=2`是配置断言，不是自动拦截第3次读取。
4. `test_researcher_startup_context_envelope.py`检查当前包体和组件上限之和，没有完整计入外置任务书、首依赖、活动/身份流程、工具描述、回读、失败响应及诊断扩展。
5. 本轮一次工具发现返回89个功能schema；这是可见的接口返回观测，不是精确token计量。仓库包体预算不能直接限制宿主工具描述注入；重复发现应避免。
6. 当前桥接工作流源文件及触发方式未变。工作流中处理完整事件流与把完整事件流送入模型是两件事；不应靠省略鉴权事件降低上下文。重网络返回也不自动等于模型必须读完整实现。

## 最小修复顺序（建议，未部署）

A. 先补任务包的必要控制字段和定向回归：存活核验目标、并行范围、恢复guard/最新进度。维持8192字节检查；大目标列表必须有明确的有界诊断读取，不得无条件把完整targets复制进包，也不得隐藏省略或任意改派目标。
B. 修依赖读取兼容性，但保留原ref/commit来源；不得把`path@固定版本`静默改成当前main文件。
C. 给现有校验增加真实读取清单/总字节测量的接口与覆盖范围说明。观测缺失时不声称端到端PASS；保留所有权、盲测、验证和审查门禁。
D. 明确普通TASK入口的触发式读取例外。不新建调度器，不部署新的常驻执行器，不改Actions或保护规则。

本轮没有改运行源代码、预算配置、任务书、CLAIM、授权语义或工作流。仅保存审计证据；上述修复不是已实施结果。

## 本地复现与证据

原有核心测试：5 passed，0 failed；另1项文档/工作流测试未运行，不把它计入通过。
定向探测：12；其中6项有效机制正对照、5项投影缺失观测（G4两种输入）和1项预算覆盖缺口。

完整源文件身份：

- `control_plane/researcher_startup_packet.py`: 13243 bytes; Git blob `f987bd676b07abc2d57ffeda1bd22aae31515108`; SHA256 `c8fabd55bbb961f70468e144ee2cc6c9836fd446ca96326ecd1578553101f744`。
- `tests/test_researcher_startup_packet.py`: 9125 bytes; Git blob `329bbd7c5f7e207004616705e14bd278a4d37894`; SHA256 `8b38ef36de78859b3eb0ce561c89ac4053f4cd8a7e406c110269a861bf94135b`。

`PROBES.py`可对具有上述精确文件的本地检出运行：

```text
python control_plane/audits/startup_context_20260917/PROBES.py --repo-root <exact-local-checkout> --out <local-results.json>
```

它只运行隔离样例并写本地结果，不访问网络、不领取任务。`PROBE_RESULTS.json`保存本次实际结果。

## 源文件定位

以上路径均对应本报告冻结的source commit：

- `research_context_budget.json`
- `control_plane/researcher_startup_packet.py`
- `control_plane/check_context_budget.py`
- `tests/test_researcher_startup_packet.py`
- `tests/test_researcher_startup_context_envelope.py`
- `research_control_dispatch.py`，尤其`_adoption_result`、`route_from_candidates`
- `tools/research_dispatch_core.py:github_comment_event`
- `control_plane/research_runtime_guard_core.py:canonical_live_claim_binding`
- `AGENTS.md`
- `.github/workflows/chatgpt-control-dispatch-bridge.yml`

GitHub官方接口复核仅作传输边界补充：issue comments的`since`针对更新时间、结果有分页；减少上下文不能把不完整或陈旧的事件窗口伪装成完整当前授权状态。
