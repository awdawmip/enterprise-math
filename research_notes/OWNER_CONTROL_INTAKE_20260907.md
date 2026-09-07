# Owner 控制面接管记录 — 2026-09-07

## 可立即执行的结论

- 本轮 root 已采用实际分配的 `Driver-ID: EM-DVR-01E1D9 / CONTROL_PLANE`。身份为 `REGISTER_PENDING`；登记失败不是研究阻塞。该身份属于 root 当前会话，本诊断助手不据此取得 Driver 权威。
- 发布正式任务必须使用当前不可变 V2 task publication。单独创建 taskbook、备忘或子代理消息不构成正式任务，也不授权 CLAIM。
- 调度从 `research_control_dispatch.py` 进入；先恢复原有 winning claim 的可恢复执行，再选新任务。不能用 fresh selector 空结果推断没有工作。
- 已发现一个 checker 与当前 dispatch 实现不一致的问题，以及一个可用模块入口绕过的导入问题。未验证远端当前任务、CLAIM、PR 或 CI 状态，不能据本报告宣称它们失败或清空。

## 证据与权限边界

本次本地执行快照：`D:/em/owner-20260907`，`ef1893382eb1dcfcd773e19882569e9ff072a8ee`。

GLOBAL_KNOWLEDGE 读快照：`ccd838a220b00ad44a7f5375fffeee8aa6afaaa0`；已读取该 SHA 的 `00_BOOTSTRAP.md`、`OPERATING_MANUAL.md`、`CODEX_SYNC_PROTOCOL.md`。本轮未写全局知识库。

执行依据：`AGENTS.md`、`control_plane/current_control_authority.json`、`research_role_policy.json`、`research_identity_state_machine.json`、`docs/RESEARCH_DRIVER_OPERATING_CONTRACT.md` 的精确相关部分。

`research_role_policy.json.driver_activation` 要求当前会话显式授权。root 根据用户当前“作为 owner 推进研究、制定研究方向、处理报错、完善架构”的明确职责授权承担本轮研究管理。角色名字、ID 和历史会话本身不能额外授予 Working Truth、Foundation 或 canonical promotion；具体数学决策仍需对应合同及证据。研究员本就能按统一 V2 事务发布任务，发布不是 Driver 独占能力。

`current_control_authority.json` 的狭窄控制优先级不改变数学真值、Driver 组合决策、Foundation、discovery firewall 或 task-local scope。`CONTROL_PLANE_MAINTENANCE` 单独不授权研究发布、评审或 Working Truth。

## 身份分配实测

root 曾调用带 `--dispatch-id` 的 Driver allocation，返回：

```text
ERROR manual dispatch preallocation is a Researcher-ID
```

原因是 manual dispatch preallocation 对应 Researcher-ID。已使用以下命令成功分配 root 当前身份：

```powershell
python -X utf8 -m tools.research_identity allocate --role RESEARCH_DRIVER
```

实际返回的关键字段：

```json
{
  "driver_id": "EM-DVR-01E1D9",
  "identity_source": "DIRECT_AUTO_GENERATED",
  "registration_state": "REGISTER_PENDING",
  "registration_repository": "awdawmip/chatgpt-global-knowledge",
  "registration_path": "projects/enterprise-math/researchers/EM-DVR-01E1D9.json",
  "visible_marker": "Driver-ID: EM-DVR-01E1D9 / CONTROL_PLANE"
}
```

该 ID 已被 root 确认采用，不应再次分配。身份登记需要 root 在真实语义检查点按全局知识库当前写入协议处理。

## 两个可复现故障

### 1. Current authority checker 的陈旧字面断言

```powershell
python control_plane/check_current_control_authority.py
```

在基线 SHA 上退出 `1`：

```text
ERROR: live control router must subordinate ordinary fresh selector
```

`control_plane/check_current_control_authority.py:340` 要求路由器源码含 `research_dispatch.select_task`。当前 `research_control_dispatch.py` 的 `route_control` 已复用一个 `research_dispatch.effective_states(events, now=now, root=root)` 快照，并通过 `research_runtime_reducer.select_state(states, policy, kind=kind)` 选 fresh task，同时把相同 `states` 交给 leased target / fresh lane 分支。

因此，实测证明 checker 与实现形式不一致；它尚不能证明当前路由语义错误。root 后续明确授权本助手只对该 checker 及精准回归做最小整改；需先确认与 fresh selector 的语义等价，再保留守卫强度修复检查。

### 2. Runtime guard 直接脚本入口导入失败

```powershell
python tools/research_runtime_guard.py pre-final --help
```

返回 `ModuleNotFoundError: No module named 'control_plane'`。以下替代命令已实测成功返回帮助，退出 `0`：

```powershell
python -m tools.research_runtime_guard pre-final --help
```

本轮不扩大修改范围；root 对已有真实 runtime state 使用：

```powershell
python -X utf8 -m tools.research_runtime_guard pre-final --state-file <真实-runtime-state.json>
```

不得为了得到 `FINAL_ALLOWED` 编造或清空 parent/task 状态。

## 最小发布与调度路径

1. 先选择有研究价值且未重复完成的确切问题，写出 taskbook 的 frozen inputs、hard target、研究价值、success / kill / return criteria，保留来源和语义 lineage。选问题后执行现有工具 coverage，再明确 BRC、进取坐标等 typed reuse 或适用边界。
2. 以下 prepare/publish 参数来自本快照实际 CLI 帮助；路径参数需替换为该正式 taskbook：

```powershell
python -X utf8 -m tools.research_task_records prepare --taskbook <taskbook.md> --publisher-role RESEARCH_DRIVER --parent-objective-id <本轮-parent-objective-id>
python -X utf8 -m tools.research_task_records publish --taskbook <taskbook.md> --publisher-role RESEARCH_DRIVER --publisher-id EM-DVR-01E1D9 --research-value <明确的研究价值>
```

3. 如果修改既有同任务 publication，必须使用真实 `--supersedes-publication-id`，不伪造新方向绕过 successor gate。发布前 canonical preflight 不可被“手工 JSON + 等 CI”取代。
4. 在真实协调点，通过 GitHub connector 获取必要的、有限的当前 authenticated Issue #240 事件和确切 owner-scope liveness 证据；由 root 调用 canonical dispatch：

```powershell
python -X utf8 research_control_dispatch.py --events <authenticated-events.json> --session-observations <owner-scope-observations.json> --kind RESEARCH
```

5. `ADOPT_OWNER_CLAIM` 时保留原 winning claim，并验证 taskbook pin、owner branch、remote HEAD、execution stamp 和 durable outputs 后恢复第一个未完成单元。`CLAIM_NEW_OWNER` 才进入新 CLAIM 路径。发布、CLAIM 和数学执行不是同一步。

上述发布、登记和远端协调命令未由本助手执行；本助手未建立 claims/reviews、未写共享 control state、未提交或远端发消息。

## 其他小范围发现

`docs/RESEARCH_DRIVER_OPERATING_CONTRACT.md` 的 V2 publication 节存在自相矛盾的历史迁移文字：它先把当前 task records/tool 列为权威，随后又把相同路径称为非 post-cutover 权威。当前控制优先级及实测 publication facade 可消除执行歧义。该文档不在本轮修复范围内，不能据旧兼容段落倒退到旧控制路径。

FREE Phase A 应由无当前 agenda 的干净上下文从 primitive substrate 启动；已暴露 owner 路线的代理不能仅换名字就声称 clean blind discovery。任务研究、工具提取与跨分支综合则在明确问题后使用 coverage gate，并保存可接续材料。

## 当前前沿

身份已建立，研究可以推进；控制问题不会成为数学 HARD_BLOCK。后续持久化及任何远端 mutation 由 root 审核执行。

## Root 后续授权的最小整改结果

授权范围是 `control_plane/check_current_control_authority.py` 的陈旧字面断言以及精准测试；不修改实际 dispatch、runtime guard、数学权限或共享控制 JSON。

`tools/research_dispatch_core.py:851–860` 已确认 canonical `select_task` 的实现是：先对相同 events / now / root 求 `effective_states`，再 `load_policy(root)`，最后 `select_state(states, policy, kind=kind)`。当前 router 执行同样的链，并把 states 快照用于 owner/lane 两条路径。

已将 checker 的旧单一 `research_dispatch.select_task` 字面要求替换为该当前三步绑定链的检查。保留 canonical state authority、policy 和 reducer selection 三项要求；任一步缺失均拒绝通过。检查器维持原有静态文本检查类型，真正的恢复与选路行为另用回归验证。

新增 `tests/test_current_control_authority_dispatch.py`，覆盖：

- 当前 router 通过 authority gate；缺失三步链任一步时拒绝通过。
- owner/lane 共用一次求得的同一状态对象；priority、kind、已 leased 排除等选择结果与 canonical fresh selector 相同。
- 即使存在可派发的高优先级 fresh task，stale 现有 winning claim 仍优先被恢复，且不生成新 claim。

先运行回归确认基线：语义两项通过，current authority gate 失败于原始陈旧断言。整改后实际验证：

```powershell
python -X utf8 control_plane/check_current_control_authority.py
python -X utf8 -m unittest discover -s tests -p test_current_control_authority_dispatch.py -v
python -X utf8 -m unittest discover -s tests -p test_control_dispatch_session_observation_time.py -v
```

结果：authority checker PASS；新增 4 项测试全部通过（其中包含 3 个拒绝子案例）；现有 session observation time 6 项测试全部通过。没有扩张运行无关全库检查。

Root 下一步：审核这一个 checker 的 diff 与新增测试，并连同所需研究材料按本轮整体持久化流程提交。runtime guard 的直接脚本入口问题仍采用已验证的 `python -m tools.research_runtime_guard` 绕过，本轮未改它。

Global-Knowledge-Sync: main@ccd838a / GLOBAL_KNOWLEDGE_V1
