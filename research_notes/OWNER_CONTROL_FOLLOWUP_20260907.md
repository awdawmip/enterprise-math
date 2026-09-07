# Owner 控制面后续检查 — 2026-09-07

## 结论与执行范围

三个 CI 签名均在首轮修复以外的既有源文件中。本地在 `f38fba58619d4764456e2a2db9bec7e67a8b3ca2` 重现三个签名；该提交相对 `ef1893382eb1dcfcd773e19882569e9ff072a8ee` 仅改变第一轮 current-authority checker、其精准测试和 intake 报告，三个失败涉及的原始 checker、dispatch facade/core、cohort 测试以及 6 个任务 publication/taskbook 均未改动。

本轮只在 `D:/em/owner-control-20260907` 修改 legacy-isolation checker、新增精准测试；经 root 后续授权，再修复一份 cohort 测试的当前模块/mock 绑定，并记录本报告。没有触碰研究树、数学 scope、不可变 publication、角色/授权 JSON、实际 dispatch 实现或 legacy scheduler；未提交、未执行 remote/Issue/CLAIM 操作，也未重新分配 Driver-ID。

Root 提供的远端观察是 PR #1363 head `7a1981615495a7099bb472527ad3d3aeef2c685b` 与本地 f38 同树、main 仍为 ef189，以及下面三个 job ID；本助手没有重复远端查询。GLOBAL_KNOWLEDGE 继续使用本轮已验证的 `ccd838a220b00ad44a7f5375fffeee8aa6afaaa0`。

## 1. Legacy isolation checker — 已做最小修复

CI job：`101615290208`。

基线复现命令：

```powershell
python -X utf8 control_plane/check_legacy_control_isolation.py
```

原错误：`live dispatch does not fail closed on bare runtime events`。

根因是该 checker 要求 `tools/research_dispatch.py` 出现连续说明文字 `raw authenticated Issue #240 comment objects`，而公开 facade 的 docstring 将 `raw authenticated` 与 `Issue #240 comment objects` 分成两行。真正的运行入口由 facade 导出 core，`tools/research_dispatch_core.py:909–926` 的 `load_events` 已明确：

- 裸 runtime event 不可作为外部输入；
- 带 `_github` 的调用方自制 normalized envelope 不可作为外部输入；
- raw GitHub comments 与 bare event 混装时拒绝；
- 仅 raw comment 文件走 `events_from_github_comments`，server provenance 与 control authorization 仍由该既有链计算。

已先向 root 报告设计，再把说明文字匹配替换为 `_check_dispatch_event_boundary()`。它通过公开 `research_dispatch.load_events` 读取临时本地 fixture，实际验证上述三种拒绝路径，并验证合法 raw-comment 形状可以解析且保留 server time / comment ID；测试用非授权作者仍须 `control_authorized=false`。它不运行 reducer，不持久化 event，不创建任何真实任务或 claim。

原有 legacy 路径物理隔离、legacy fallback 禁止、policy、runtime guard、prompt、writer 和 semantic quarantine 检查均保留。这里没有通过删去 gate 或只调整换行让 CI 变绿。

新增测试：`tests/test_legacy_control_dispatch_event_boundary.py`。

- 当前 public wrapper 通过 boundary checker。
- 分别模拟 bare / normalized / mixed 任一类错误被接受，checker 都拒绝通过。
- 全部输入一律拒绝的坏入口也不能通过正例检查。
- 非授权 raw-comment 被错误赋予 control authority 时拒绝通过。

实际验证：

```powershell
python -X utf8 control_plane/check_legacy_control_isolation.py
python -X utf8 -m unittest discover -s tests -p test_legacy_control_dispatch_event_boundary.py -v
python -X utf8 -m unittest discover -s tests -p test_research_dispatch_event_envelope.py -v
```

结果：legacy isolation checker PASS；新增 4 项测试 PASS（包含 3 个拒绝子案例）；现有 event-envelope 8 项测试 PASS。Checker 的完整 PASS 输出仍明确保留 `1 exact semantic-preservation fault(s) are locally blocked`，没有把既有隔离故障抹去。

## 2. Post-cutover publication envelope — 24 条既有错误，未改

CI job：`101615291053`。

精确本地复现：

```powershell
python -X utf8 control_plane/check_post_cutover_publication_envelope.py
```

退出 1：`post-cutover publication envelope audit: FAIL (24 error(s))`。

六个记录分别缺少相同四个必需正文节：`Frozen inputs and scope`、`Hard target and required outputs`、`Research value to preserve`、`Success, kill, and return criteria`。

| Task ID | Publication ID |
| --- | --- |
| RS-X6-CELL-CHANNEL-INTERNAL-STATE | TP2-B5E2097A3C6418DF42E5 |
| RS-X6-NATIVE-ROTATION-DYNAMICS | TP2-6A1F9D8C2047E3B51C01 |
| RS-X6-NATIVE-TIME-DYNAMICS | TP2-91D4A7C2F63805BE21A3 |
| RS-X6-NONFCC-SLICE-REALIZATION | TP2-A3C8E1D754209B6F31D4 |
| RS-X6-TRIADIC-CLOSURE-DYNAMICS | TP2-8B7E13C5904A2D6F1142 |
| RS-X6-UPPER-STRUCTURE-INTEGRATION | TP2-C7F31A8D520B49E653F6 |

每条精确记录路径为 `research_task_records/<Task ID>/<Publication ID>.json`。

下一动作：由有相应研究权限的 root/owner 从每条记录的真实 `taskbook_path` 和 blob pin 回源，判断是否存在可验证的原始 scope/target/return 内容以及当前 operational 状态。内容缺失不能由控制维护代理补造；若需要修订，必须保持原 publication 不变并走明确来源与 supersedes 的 V2 发布事务。若只有应为非 operational 的历史记录兼容问题，先验证其确切非 operational 状态和已有精确隔离协议，不创建宽泛 grandfathering 或修改 validator 来跳过正文要求。

隔离边界：本轮不改变这六项的数学要求、研究方向、publication bytes、任务执行权或 mandatory-section gate。

## 3. Quality cohort test 的 legacy import — 第三单元已修复

CI job：`101615323322`。

精确本地复现：

```powershell
python -X utf8 -m unittest discover -s tests -p test_research_dispatch_cohort_overlay.py -v
```

`tests/test_research_dispatch_cohort_overlay.py:5` 仍导入已物理移除的 `tools.research_scheduler`，报 `ImportError: cannot import name 'research_scheduler' from 'tools'`。该模块在此文件唯一的实际使用位于第 131 行：`scheduler.parse_time(...)`。

Root 后续明确授权第三单元，只修改 `tests/test_research_dispatch_cohort_overlay.py`。已把时间解析迁到当前 `tools.research_runtime_reducer.parse_time`。同时按 `tools/research_dispatch_core.py:851–860` 的真实调用点，把原先对 facade `load_json` / `effective_states` 的 mock 改为 `dispatch_core.research_runtime_reducer.load_policy` / `dispatch_core.effective_states`。

测试仍通过公开 `dispatch.select_task` 调用生产选择逻辑；原四项行为断言完全保留：active cohort 清除 task-global owner、保留既有 result evidence、没有 active cohort 时保持普通状态、全局 selector 不选择 cohort-active 任务。

按上述同一命令重跑：4 tests，全部 PASS，耗时 0.005 秒。没有修改生产 dispatch、恢复 legacy scheduler 或全库替换 import。

## 4. 六份冻结 taskbook 的一次有界 source 审计

审计只读取第 2 节六条 publication 的 `taskbook_path` / `taskbook_blob_sha1`，再一次完整读取对应六个文件（各 61–69 行）。`git hash-object` 得到的每个当前文件 blob 均与 publication pin 相同；以下都是冻结源本来已有的内容，不是补写方案。

| Task 简称 | taskbook_path | 匹配的 taskbook_blob_sha1 |
| --- | --- | --- |
| CELL-CHANNEL-INTERNAL-STATE | research_tasks/RS_X6_CELL_CHANNEL_INTERNAL_STATE_20260906.md | sha1:72daccfc33a8aa1572a69416a7c2052f38745fc1 |
| NATIVE-ROTATION-DYNAMICS | research_tasks/RS_X6_NATIVE_ROTATION_DYNAMICS_20260906.md | sha1:448120b04ecdadf44d8a06516605bfcca94474a1 |
| NATIVE-TIME-DYNAMICS | research_tasks/RS_X6_NATIVE_TIME_DYNAMICS_20260906.md | sha1:eba80ae0be492033f9eda082aac2b017f7398114 |
| NONFCC-SLICE-REALIZATION | research_tasks/RS_X6_NONFCC_SLICE_REALIZATION_20260906.md | sha1:fab0109c7959faf249ea0c9383f8b12f584fe1c9 |
| TRIADIC-CLOSURE-DYNAMICS | research_tasks/RS_X6_TRIADIC_CLOSURE_DYNAMICS_20260906.md | sha1:218bf9ce05fd2dd79f477ac269fc3590f83f482e |
| UPPER-STRUCTURE-INTEGRATION | research_tasks/RS_X6_UPPER_STRUCTURE_INTEGRATION_20260906.md | sha1:b9a5979e5c10169badf13c0ff643f0a6f8c203bd |

所有文件正文都只有 `Mother question`、`Hard target`、`Hard boundaries` 三个英文二级标题，没有中文替代结构。四个 mandatory 精确标题均不存在。现有内容的映射证据如下；行号指上表对应 taskbook，不是 publication JSON。

| Task 简称 | Frozen inputs / scope 的现有片段 | Hard target / required outputs 的现有片段 | Success / kill / return 的现有片段 |
| --- | --- | --- | --- |
| CELL-CHANNEL-INTERNAL-STATE | metadata dependencies/source_refs 12–21；Hard boundaries 62–64 | Hard target 54–60：decorated state、PF-10/BRC reuse、memory、signed/phase、hidden-state counterexamples | 第 60 行要求产生 hidden-state counterexamples；无独立 success/kill/return 节或显式 kill 条件 |
| NATIVE-ROTATION-DYNAMICS | metadata 12–21；Hard boundaries 63–69 | Hard target 54–61：typed rotation层级、triadic generators、BRC path lift、memory | 第 61 行明确 complete dynamics / maximal exact restricted dynamics / sharp obstruction 三种 return；无显式 kill 条件 |
| NATIVE-TIME-DYNAMICS | metadata 12–21；Hard boundaries 63–65 | Hard target 54–61：time-indexed state、clock separation、common typing、minimal Markov state | 第 60 行包含 obstruction/lower bound，第 61 行包含 reusable tool or sharp no-go；无显式 kill 条件 |
| NONFCC-SLICE-REALIZATION | metadata 12–19；Hard boundaries 59–61 | Hard target 52–57：microcycles、20 selections分类、carrier-specific区分、counterexamples | 第 57 行要求反例；无独立 return 替代路径或显式 kill 条件 |
| TRIADIC-CLOSURE-DYNAMICS | metadata 12–20；Hard boundaries 62–64 | Hard target 53–60：typed force、closure、PERP_E关系、triad分解、exact checker | 第 59 行包含 sharp obstruction 替代，第 60 行要求有限 checker；无显式 kill 条件 |
| UPPER-STRUCTURE-INTEGRATION | metadata 12–22；Hard boundaries 63–65 | Hard target 55–61：typed product、transition composition、covariance、observer maps与quotients | 第 61 行包含 minimality result or irreducibility witnesses；无显式 kill 条件 |

`Research value to preserve`：六份均没有独立对应正文，也没有中文同义节。各自 metadata 第 10–11 行的 `frontier` / `next_action` 和正文母问题表达了问题动机，但本审计不把这些自动视为已满足该 mandatory section。

因此，`Hard target and required outputs` 有明确可追溯的旧标题片段；scope 有 metadata 和边界片段；完整四节不能仅靠标题别名得到。尤其不得据已有部分 return/no-go 句子补造完整 success/kill/return 条件。这里未判断六任务当前 operational/claim 状态，未回证其数学前提，也没有把源文件自带 `CLAIMABLE` 字样提升为当前执行权限。

## Root 的下一执行动作

审核本轮一个 checker、新增精准测试、cohort 测试迁移和本报告。Root 已接受第二 checker 的行为设计，第三单元也已实测通过；所有改动仍待 root 统一提交。六个任务的后续处理应从以上精确 source 映射和现有 V2/隔离权限边界出发，不能把修复 CI 变成补造研究语义。

Global-Knowledge-Sync: main@ccd838a / GLOBAL_KNOWLEDGE_V1
