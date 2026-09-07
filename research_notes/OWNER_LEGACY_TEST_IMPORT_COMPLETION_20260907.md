# 遗留测试导入与 V2 入口迁移补全

状态：`CONTROL_PLANE_MAINTENANCE / NO_NEW_MATHEMATICS / TARGETED_TESTS_PASS`。
辅助工作包 `/root/exact_solver`，owner 明确授权的限定测试维护；没有研究角色、claim、review 或发布权限升级。
工作树 `D:/em/integration-owner-control-20260907`，基底 HEAD 为
`16cc5663c191a73e997e3a973f589197d0694c89`，验证时同时包含 owner 的既有控制修复及其他代理已冻结的 fork 隔离改动。
本单元先完成三个运行时测试，随后依 owner 明确续接修复第四个 Foundation backflow 测试，并更新本文。
最终只修改四个测试文件和本文；没有修改生产 dispatcher、权限规则、registry、taskbook 或远端。

## 1. 有界发现及真实基线

在 `tests` 中搜索 `research_scheduler`，实际活跃旧 Python 依赖为：

- `test_research_runtime_claim_authority.py`：直接导入已物理移除的 `tools.research_scheduler`，四处只使用其时间解析。
- `test_research_lane_claims.py`：同样的直接导入，五处时间解析。
- `test_research_control_p0_v2.py`：八处 `dispatch.research_scheduler.parse_time`，并残留 pre-V2 入口与 fixture 假设。

另两个已修测试 `test_research_runtime_lane_authority.py`、`test_research_dispatch_cohort_overlay.py`
已使用 `research_runtime_reducer`，本单元没有修改它们。

真实基线运行命令为：

```powershell
python -X utf8 -B -m unittest tests.test_research_runtime_claim_authority tests.test_research_lane_claims tests.test_research_control_p0_v2 -v
```

前两个模块在 collection 就报
`ImportError: cannot import name 'research_scheduler' from 'tools'`。
P0 模块有多项测试先被未经 bootstrap 的严格 `current_records` 阻断，报
`publication fork for RS-P000-L1-NATIVE-CARRIER-CONTACT-BRIDGE`；这发生在旧时间属性访问之前。
因此不能把“没有直接看到 AttributeError”误判为八个旧属性调用仍然可用。
这也不是 fork 隔离修复尚未落地：测试绕过了正式入口的 bootstrap。

## 2. 现行源码合同与对应修改

已读 `control_plane/current_control_authority.json` 的 V2-only / canonical bootstrap 合同及以下实际实现：

- `tools/research_runtime_reducer.py:37` 的 `parse_time`：接受 ISO 时间并归一化到 UTC。三个测试改为直接使用此现行接口，所有原时间常量不变。
- `research_control_dispatch.py:42`：正式入口先执行 `research_control_bootstrap.install(ROOT)`。
  `control_plane/research_control_bootstrap.py:211` 安装验证过的精确隔离以及 operational audit views。
  claim-authority 与 P0 测试各增加 `setUpModule` 调用相同 bootstrap；不 mock 掉 fork，也不恢复 legacy shim。
- `control_plane/research_runtime_guard_core.py:117` 从仓库当前 publication 获得注册权威；未注册任务最终报
  `has no current immutable V2 publication`。原两个 `assertRaisesRegex` 保留，只更新到现行拒绝语义。
- `tools/research_dispatch_core.py:158` 的任务定义来自 immutable publications，无 legacy definition fallback。
  原“registered 与 legacy 合视图”测试改为验证有效 V2 任务存在、publication 精确相符、task_id 无重复、
  `RS-P017-GLOBAL-CAPACITY` 不在视图。精确 quarantine 行必须为 BLOCKED，经过实际纯 reducer 的空事件投影后仍 BLOCKED，
  且没有 claim_id / researcher_id；空事件是确定性合同探针，不声称当前 live event history 为空。

真实 bootstrap probe 返回：当前 publication 数 155；旧 RS-P017 在 current 与 definitions 中都不存在；
public `records.audit(ROOT)` 返回空错误列表。这个数量只是本次快照诊断，测试没有固定断言 155。

## 3. 导入修复后实际暴露的两个 fixture 边界

第一次三模块完整运行已能执行 28 个测试，其中 26 通过，两个 P0 断言失败。
它们不是生产授权回归，分别是当前措辞和有效 intent fixture 的 generation 缺失：

1. `tools/research_dispatch_core.py:291` 拒绝编辑事件的理由已是
   `edited runtime event is not authority; append a correction event`。
   实际状态仍为 NEEDS_DISPATCH、claim_id 为 None。
   测试更新理由字符串，保留状态断言，并明确增加无 claim 断言。
2. 原“有效 intent 下未审核 DONE”fixture 没有 `publication_id`。
   `tools/research_dispatch.py:104` 的现行绑定检查必须拒绝这种缺失/错误 generation；
   原 CLAIM 因而未获租约，随后 `research_dispatch_core.py:579` 正确阻断无 review 的 DONE，返回 BLOCKED。
   修复在 fixture 中加入实际当前 task 的 publication_id，让它真正表示有效 intent。
   原预期 LEASED 和 review 拒绝断言全部保留，还增加 claim_id=`c1` 与 researcher_id=`EM-QPHJA-ABC123` 的精确保持检查。
   没有把 LEASED 期望改为 BLOCKED 以掩盖 fixture 问题。

其余授权断言保留：缺 Issue #240 证据、非授权作者、过期租约、伪造 owner claim、正确 winner 的完整绑定，
同任务两 lane 独立竞争、lane publication、输出前缀、首个有效 claim、伪造注册、stale publication、
不可覆盖 publication、placeholder 正文拒绝、冻结结果和 Driver review 边界。

## 4. 第一阶段真实运行及保留的冻结文件

同一命令最终输出：`Ran 28 tests in 32.617s`，`OK`，退出码 0。
解释器为本机 Python 3.14 系列，使用 `-X utf8 -B`；没有调用全库测试或 CI poll。
其中 lane-claims 单独在仅改时间解析之后也已执行 5 tests，全部通过。
`git diff --check` 对三个测试文件无错误。

下列三个源文件在 Foundation backflow 续接期间逐字节不变，最终 SHA256 仍为：

| 路径 | SHA256 |
| --- | --- |
| `tests/test_research_runtime_claim_authority.py` | `4e2da2a8b32428c0d2f17e09164dd98740903c3a493a31cdce190877860de224` |
| `tests/test_research_lane_claims.py` | `87ddb05edbdce25a8a157533f734b1cb5c596da8cf1e4a94e8ca753a67849391` |
| `tests/test_research_control_p0_v2.py` | `59c6486566b6e02008217ab34f913e6fa02b5edcaf8b5901a2ee96622523a56d` |

## 5. Foundation backflow 数据依赖的明确续接

首次搜索还命中 `test_foundation_backflow.py` 读取已不存在的 `research_scheduler.json`。
这一项是独立的数据 fixture/schema 消费问题，owner 明确追加授权后才修复。
真实基线运行 `python -X utf8 -B -m unittest tests.test_foundation_backflow -v`：
`Ran 9 tests in 0.017s`，`FAILED (errors=9)`，全部在读取该旧文件时报 FileNotFoundError。
当前 `foundation_backflow.json` 的 active links 为零，旧 FQ-20260809-005 已迁入 ANSWERED 历史并绑定 CLOSED publication；
不能重新把它当成 current active FQ，也不能让原负向断言因空列表而不执行。

已实际读取 `check_research_common_surface.py:153–338` 的任务 payload 与 validator：
现行 `validate_backflow(backflow, runtime_policy, dispatch_tasks=None)` 明确允许第三参注入合成任务列表。
主 checker 在 :412–413 使用 `research_dispatch.merged_definitions(ROOT)` 及当前 `research_runtime_policy_v2.json`。
第四个测试文件相应分为两层：

- 集成检查读取实际 backflow 和 V2 runtime policy、安装 canonical bootstrap，传入真实 merged definitions，
  验证 payload 非空与 V2 来源后运行当前 validator；没有创建 scheduler 文件或 legacy task table。
- 单元检查构造明确的内存 RESEARCH/GOVERNANCE 任务、owner、FQ 和 source refs。
  三个活跃 synthetic FQ 分别走 RESEARCH、INTEGRATION、STEWARD_VERIFICATION；另有同 owner 但声明其他 FQ 的无关任务，
  以及 synthetic canonicalized FQ。所有 ID 均标作测试用，未写任何 publication。
  每个负例的 setUp 都先确认三个 active links 非空且完整 fixture 验证无错误，保证不是空集上的假通过。

原八个负向合同全部执行：RESEARCH kind、两种 stewardship/integration 的 GOVERNANCE kind、owner 匹配、
同 owner 不能隐含承接无关 FQ、必须显式声明 FQ、FQ link 唯一性、Issue 权威面与 runtime policy 对齐、
canonicalized FQ 不能重新 active。原仓库正向检查保留，新增明确合成 fixture 的正向检查，合计 10 tests。
没有修改 production validator 来接受不合法 fixture。

第四文件 SHA256：
`tests/test_foundation_backflow.py` → `bbe7cd240eed78219e9712461dd6604cb0edb86c57468e86aab66a5f5f7d1fdd`。

## 6. 最终 Python 3.12 组合验证及范围

最终真实命令：

```powershell
& 'C:/Users/Administrator/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe' -X utf8 -B -m unittest tests.test_research_runtime_claim_authority tests.test_research_lane_claims tests.test_research_control_p0_v2 tests.test_foundation_backflow -v
```

解释器为 Python 3.12.14，输出 `Ran 38 tests in 43.549s`、`OK`，退出码 0。
四个文件的 `git diff --check` 通过；前三文件 SHA 与 §4 完全相同。
最终 `test_foundation_backflow.py` 已无 `research_scheduler` 或历史 FQ-20260809-005 字面引用。
`tests` 内其余 scheduler 搜索命中位于 `test_research_startup_transport.py` 和
`test_role_control_authority_unittest.py`，属于禁止 legacy 引用的负断言，保留。

本报告只声明四个模块的有界修复与 38 tests 组合结果。最终 reference/quality 组合由 owner 统一验证；
本单元没有给共享工作树其他并行改动作测试通过背书，没有提交或推送。

Global-Knowledge-Sync: main@4fa7d7d / GLOBAL_KNOWLEDGE_V1
