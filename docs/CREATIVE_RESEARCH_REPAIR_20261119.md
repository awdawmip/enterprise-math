# 创造性研究卡点修复与验证记录

日期：2026-11-19（北京时间）

范围：`CONTROL_PLANE_MAINTENANCE`。本记录说明代码、合同和入口文案的修复及本地验收，不新增科研身份、Task、CLAIM、Result、Review 或 Activity，也不作数学接纳。

开发与复现基线：`awdawmip/enterprise-math@0f10e3500f39066e2d829052bcc6c1f540fec74f`。发布时以实际最新主干为父提交，并核对目标文件及依赖未发生相关漂移；并发科研材料保持原样。

## 六类修复

| 编号 | 原卡点 | 本次结果 |
| --- | --- | --- |
| C1 | 现行规则允许独立方法，工具返回和部分 Driver/编排说明仍要求先证明能力缺口 | coverage 的命中与未命中分支都允许 `ALTERNATIVE_APPROACH_CHOSEN`；同输入输出独立实现无需能力缺口。新颖性与共享工具接纳继续要求相关比较和真实贡献证据 |
| C2 | ASCII 分词丢弃中文条件 | 保留完整中文词段，使用有限、明确的中英数学检索别名，支持混合及繁体查询；未知词不拆成任意单字匹配 |
| C3 | 已审 `DERIVED_NOT_AXIOM` 不能沿真实 FREE 来源发布后续任务 | 将该状态加入既有三个统一资格列表；保留候选 ID、派生分类、父目标、来源和研究价值，不增加 Driver 审批 |
| C4 | 并行综合及下游消费者固定要求两次、按编号指定的参考检查 | 参考数量和方法按命题选择；0、1、3 次以上及不连续编号可用。当前控制仍使用完整实际证据集合，正式终结仍依既有 Result 审查权威 |
| C5 | Phase B 无条件要求反例搜索或小模型测试 | 改为与结论强度相称的验证证据，允许复用适用证明、检查和证书；未决义务继续保留 |
| C6 | 普通续研和 Stage 裁定仍被部分投影要求立即评估后继、形成计划包 | 后继门禁限于发布新的正式 `CONTINUATION` 任务；普通继续、保存和报告不要求新后继包或重复比较记录 |

双语编排、工具协议、FREE 角色/Phase B 说明以及中英文研究架构已同步。Driver 的方法归集说明也与现行规则一致：共享可复用机制或路由实质变化时分类更新，普通返回无需另建分类表单。

## 实际行为验证

### 中文发现与独立方法

真实 CLI 对固定源目录/基础方法清单的查询结果：

| 查询 | 工具族命中数 | 相关首项 |
| --- | ---: | --- |
| 残差 观察 保持 | 2 | `T0_BRC` |
| 分支计数 | 4 | `T1_SCALE_ENUMERATION_VALUATION` |
| 碰撞 纤维 | 8 | `T4_FINITE_FIBER_CAPACITY_COLLISION_MINIMA` |
| BRC 残差 | 4 | `T0_BRC` |
| 量子巧克力 | 0 | 无 |

前三项为此前零命中的复现输入。混合查询另有排序回归，确认中文条件参与评分。别名只是检索提示，不构成数学接口等价。未命中状态改为 `NO_CATALOG_MATCH`，不推断数学能力缺失；依赖旧未命中字符串的外部消费者需要同步。

### FREE 的真实发布函数链

测试运行 `prepare_taskbook -> _prepared -> build_record -> immutable save -> audit`，使用本地临时文件和真实实现。RESEARCHER、RESEARCH_DRIVER 的既有路径保留真实 FREE 来源及派生分类。恢复旧三态合同后，同一函数重新产生 `TB-ORIGIN-CANDIDATE-STATE`，复现原故障。

原始/未完成审计、已证伪、重复、外部类比和实现伪影未因此取得新资格。缺候选字段、错误角色、缺父目标、空或占位正文、缺研究价值、内容漂移和错误授予 Working Truth/promotion 仍被拒绝。Foundation 入口未扩展。

这些是结构及字节绑定检查。既有 V2 函数不认证一个候选审计或数学证明的真伪；本次也没有新增认证链。

### 并行参考、历史和当前控制

`reference_review_status=NOT_PERFORMED` 明确表示未做参考检查；`RECORDED` 只表示有实际参考记录，不证明独立性、充分性或正式接纳。每条参考继续绑定精确 Result/publication 集合、记录作者、方法和上下文披露。

公开追加入口为：

```bash
python research_parallel_evidence.py write-synthesis --record-file <candidate.json>
```

它复用已有不可变写入事务，在写前和写后校验当前完整参考集合。遗漏、重复、未知引用或写入过程中新增参考会使本次写入失败；回滚仅针对本次创建且仍为本次字节的文件。该文件操作原语不授予真实研究角色、审查或任务终结权限。

交叉审查发现并修复了两个初版续研问题：

1. 旧综合完成后新增参考，曾使旧不可变记录的审计失败。现按其真实引用快照保存历史，新参考只使当前状态等待新的完整综合。
2. 操作 publication 选择器曾继续采用旧快照。现 Result、cohort 和操作选择器均使用完整当前参考集合；新的完整综合还须由 resolution 显式指向，才能恢复相应当前控制选择。

测试覆盖旧终结综合、晚到参考、等待新综合、新非终结综合继续研究的文件链。旧综合字节始终保留。正式终结既有通过正例，也有缺逐项 review authority、缺适用 follow-up、缺 terminal disposition 的拒绝负例；单独填写 `task_terminal=true` 无法关闭任务。新 Result 到来仍重新打开其完整证据集。

历史手工 JSON 无法证明其写入时的整个参考全集。历史审计验证真实引用，当前 writer 校验当下全集，当前消费者拒绝历史子集；不使用调用者时间戳补造历史先后。

### 续研与正式后继

直接调用实际 lineage 验证器确认：普通 `NEW_DIRECTION` 无 successor gate 可以通过对应检查；正式 `CONTINUATION` 缺父任务或 gate 仍返回 `TB-SUCCESSOR-PARENT` / `TB-SUCCESSOR-GATE`；完整正式后继条件可通过。普通续研不新增规划记录，真实母目标、用户停止及现有共享归属边界继续适用。

## 组合回归结果

同一集成工作区执行 **122 项 unittest + 29 个无 fixture 测试函数，共 151 项，零失败、零错误、零跳过**。不重复累计代理先前运行的同名测试。

| 测试文件 | 执行方式 | 数量 |
| --- | --- | ---: |
| `test_enterprise_toolbox_router.py` | unittest | 13 |
| `test_free_derived_task_publication.py` | unittest | 9 |
| `test_active_turn_liveness_unittest.py` | unittest | 5 |
| `test_active_turn_continuation_liveness.py` | unittest | 19 |
| `test_research_driver_followup.py` | unittest | 18 |
| `test_research_parallel_evidence.py` | unittest | 5 |
| `test_research_parallel_result_runtime.py` | unittest | 4 |
| `test_research_parallel_reference_policy.py` | unittest | 12 |
| `test_research_cohort_runtime.py` | unittest | 6 |
| `test_research_execution_cohorts.py` | unittest | 7 |
| `test_research_operational_publications.py` | unittest | 10 |
| `test_research_parallel_late_result_reopen.py` | unittest | 1 |
| `test_continuation_parallel_results.py` | unittest | 13 |
| `test_free_researcher_axiom_discovery_contract.py` | 直接调用无 fixture 函数 | 7 |
| `test_research_architecture_v2_contract.py` | 直接调用无 fixture 函数 | 19 |
| `test_research_architecture_canonical_status.py` | 直接调用无 fixture 函数 | 3 |

unittest 使用项目根下的 `python -m unittest discover -s tests -p '<表中对应文件>' -v`。当前环境没有 pytest，后面三份文件使用标准库 `runpy.run_path` 加载，检查函数签名无参数后逐一执行 `test_*`，并记录所有异常；不声称运行了 pytest。

其中两个 `Repository*` 测试只是稀疏工作区 smoke 检查，不作为全库审计。正式终结 fixture 隔离历史 follow-up transport 状态；Result/Review 文件读取和集合权威使用真实实现。测试中的身份均是隔离 fixture，不代表线上授权。

另核对了固定 Source 上现存六组并行历史，共 24 份 intake/reference/synthesis 文件，Git blob 全部匹配，旧两轮结构和引用快照可读；并核对现行 27 条 follow-up 旧基线 Review 与冻结树字节一致。这些检查不重新审查原数学成果。

## 范围与剩余生效环节

P000、明确范围内的原生 BRC 要求、实际作者与独立性、CLAIM/CAS、未知写入对账和正式接纳权威保持。未改已有科研历史或运行中的共享任务。

本记录证明源码及本地行为修复。原生中控台使用当前控制数据和固定的已审阅执行代码两套版本；主干发布本身不完成固定代码包升级。本轮没有可调用的受控主机升级入口，未执行线上代码切换，也未用真实科研状态写入代替测试。部署后仍需核对实际执行代码版本和对应入口行为。

检索改善有具体复现结果；研究速度、问题新颖性和整体创造性提升幅度尚未通过行为实验测量。
