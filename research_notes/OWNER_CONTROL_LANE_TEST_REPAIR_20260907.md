# Owner 控制维护：lane authority 测试入口修复

状态：`NO_NEW_MATHEMATICS / LOCAL_REPAIR_VERIFIED / REMOTE_NOT_UPDATED`。2026-09-07。内部控制帮助，不是正式评审或新的研究授权。

## 实际缺陷与最小修复

GitHub PR #1363 的 frozen head `b2a66b43b4b02199d972fcfafeaf3c63f2f0d30b` 上，unit-shard (4) 的 job `101622510418` 实际日志指出：`tests/test_research_runtime_lane_authority.py` 导入已删除的 `tools.research_scheduler`，导入失败后退出2。本地原文件独立重现同一 ImportError；这不是本次修复新增的失败。

该文件的 scheduler 唯一用途是三处 `parse_time`。经 root 明确授权，已在隔离 worktree `D:/em/owner-control-20260907`：

- 将导入替换为当前 `tools.research_runtime_reducer as runtime_reducer`；
- 将三处 `scheduler.parse_time` 替换为 `runtime_reducer.parse_time`；
- 保留全部六项权限断言、fixture、mock、生产 guard 调用与预期错误。

没有修改生产授权/dispatch，实现改动仅4处替换。无需额外 mock 修复。原文件 SHA256 为 `dd8a45c95da20465ef4516b309c6093d1ebb3963cef74079db4dee6f97cbbb6e`；修复文件为 **`610b5169da21fd80e1126c4b8baf581b8a8f9795af6ec4d459dd7fdf7550b24f`**。

进入修复前工作树 clean，HEAD 为 `57cc1add4160049cb89dae3fcb788c2a54423dd2`。已有7个 owned control 文件保留。另代理独占的 `tools/enterprise_toolbox.py` Windows 路径修复不属于本助手修改或本节测试结论。

## 真实验证

修复后加载以下六个 test modules 到同一 unittest suite，共 **32 tests，PASS，0.057秒测试执行时间**：

| 模块 | tests |
|---|---:|
| `test_research_runtime_lane_authority.py` | 6 |
| `test_research_dispatch_cohort_overlay.py` | 4 |
| `test_current_control_authority_dispatch.py` | 4 |
| `test_legacy_control_dispatch_event_boundary.py` | 4 |
| `test_research_dispatch_event_envelope.py` | 8 |
| `test_control_dispatch_session_observation_time.py` | 6 |

这些测试继续覆盖：active cohort 拒绝 task-global 执行、精确 lane winner、旧 task-global terminal 不误挡 active lane、terminal synthesis 拦截后续执行、伪造不同 lane owner 被拒绝、半缺 execution_scope 被拒绝，以及原有 dispatch/event/time 边界。未减弱 gate。

同时实际运行：

```text
control_plane/check_current_control_authority.py: PASS
control_plane/check_legacy_control_isolation.py: PASS
  仍明确报告 1 exact semantic-preservation fault locally blocked
control_plane/check_post_cutover_publication_envelope.py: exit 1
  FAIL (24 error(s))
```

24项仍是六份既有 X6 publication 各缺四个 mandatory body sections：`Frozen inputs and scope`、`Hard target and required outputs`、`Research value to preserve`、`Success, kill, and return criteria`。与真实 GitHub job `101622475457` 一致。六份精确记录、pin 和源内容审计已在 `OWNER_CONTROL_FOLLOWUP_20260907.md`，本轮未重写它们或补造研究语义。不能称整个远端 CI 绿色。

## 一次有界远端 intake 与合入边界

本助手通过 GitHub connector 只读取 PR、current main、该 head 的14个 check runs、两项失败 job logs 及 base-to-main compare；未发评论、rerun、CLAIM 或远端 mutation。

- PR head：`b2a66b43b4b02199d972fcfafeaf3c63f2f0d30b`；local `57cc1add…` 与它同 tree **`6cfa43e661d830c34ccb79b79ac6684b26a28c94`**，历史各自保留。
- 独立读取的 current main：`fd532560af31b36c736bb4bd21e75c8326835541`；共同基点为 `ef1893382eb1dcfcd773e19882569e9ff072a8ee`。main 从此基点前进25 commits、24个 changed paths；它们与 PR 原7个 owned paths 完全不交。实际 dispatch/core 与 current authority 的相关依赖文件亦未改变。
- 这份新修复的 lane test 在上述 main、原 PR 相对基点均未变，故基线故障仍适用。
- head 的14个 checks 是3 success、3 failure、7 cancelled、1 skipped；combined legacy statuses为空，不能由此推断没有 checks。
- **接口纠正**：`fetch_pr` normalized 的 `mergeable=false` 对应原始 `GET /pulls/1363` 的 `mergeable=null`、`mergeable_state=unknown`、`rebaseable=null`。它不是已证实的冲突。PR仍open/Draft；其 `base_sha=ef189…` 也不能代替独立 current-main GET。

建议 root 以 latest main 的精确快照重放这一隔离 NO_NEW_MATHEMATICS payload，保留所有非 owned paths并在最终组合树验证。当前无已发现的路径冲突，但不能把这个只读快照当作将来 merge 的 expected-head 授权；24项 mandatory-section 故障、required checks 与其他合入门槛仍须按现行合同处理。本助手不作 bypass、merge 或数学权限决定。

Global-Knowledge-Sync: main@4fa7d7d / GLOBAL_KNOWLEDGE_V1
