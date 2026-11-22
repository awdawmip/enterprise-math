# 现有证据与本轮验证范围

日期：2026-11-20（UTC+08:00）。本文件区分既有公开实验、本轮源代码审查与本轮实际执行的检查。

## 1. 结论边界

本交付形成架构方案和评测工具。**七种记忆模式的新一轮效果比较均为 `NOT_RUN`。** 没有新的模型性能分数、训练收益、真实隔离验收或科研效率提升比例。

现有证据足以支持保留直接来源检索作为基线，分别测量发现和使用阶段，并把 Nollm 作为需要公平比较的候选后端。尚不足以决定某种机制应成为进取数论全部研究的默认入口。

## 2. 已有资料与实际落点

- [EM 研究库](https://github.com/awdawmip/enterprise-math/blob/51a81b442e95717ec941e9acd2382c37d2c07cdb/docs/RESEARCH_LIBRARY.md) 已有 12 个历史分卷、435 个文献整理单元；后续增补另行记录。这些不等于当前定理数量。
- [EM toolbox](https://github.com/awdawmip/enterprise-math/blob/51a81b442e95717ec941e9acd2382c37d2c07cdb/tools/enterprise_toolbox.py) 检索方法名称、描述、别名、触发词等字段，并从 `src/enterprise_math/` 发现公开模块接口。新成果检索工程建议放在 `tools/`，直接适配既有资料。
- [FREE A 精确查询规则](https://github.com/awdawmip/enterprise-math/blob/51a81b442e95717ec941e9acd2382c37d2c07cdb/docs/FOUNDATION_STARTUP_READING.en.md) 允许自主形成相关问题后的必要定义、条件和工具查询；本方案与合成合法例保留该能力。

## 3. Nollm 历史六题比较

来源：[公开原报告](https://github.com/awdawmip/Nollm/blob/cf10ab849c2b32132de01328061d172377729161/lab/nollm-lab/repository_memory/self_study/fair_trial/README.md)。报告使用历史科学/工程源码快照 `691590d…`，不是当前 main 的重新测量。每题每种模式一个独立首答，共 18 次。

| 历史模式 | 完整正确 | 要点命中 | 必需证据召回 | 可见输入与答案 token |
|---|---:|---:|---:|---:|
| 直接源码搜索 | 6/6 | 18/18 | 12/12 | 21,127 |
| 平面 AOCI | 6/6 | 18/18 | 12/12 | 38,096 |
| Surface 浏览后单入口原生召回 | 3/6 | 15/18 | 9/12 | 43,181 |

这些数字是原报告数据，本轮没有重新运行或独立复现其 18 次模型作答。可见 token 不包含完整供应商账单、模型内部推理、工具封装和历史重发等未知量。

原生臂设置为上下 Coverage 两步、beam 64、返回前 10 句柄、一次单入口；lateral 与 Bridge 预算为零。三个缺口中，一个来源在同一召回前沿排第 25，另外两个位于该入口的两步范围外。由此应分别记录物理可达、实际返回、进入模型上下文和最终正确使用。

六题是可用技术词与源码符号定位的工程问题，样本很小，不代表数学跨线综合或全部 Nollm 核组合。题目与答案现在已公开，只适合作为开发/历史回归资料，不能直接再次声称未见题盲测。

## 4. 当前 Nollm 适配风险

源代码审查使用：

- [Access Surface 状态](https://github.com/awdawmip/Nollm/blob/bafc6de4e8213d50a5ec64754c7bc87983f853ac/packages/nollm-access/src/nollm_access/surface_navigation.py)。
- [实验 Coverage CLI](https://github.com/awdawmip/Nollm/blob/cf10ab849c2b32132de01328061d172377729161/lab/nollm-lab/repository_memory/coverage_cli.py)。
- [词法入口与布局实现](https://github.com/awdawmip/Nollm/blob/bafc6de4e8213d50a5ec64754c7bc87983f853ac/lab/nollm-lab/repository_memory/task_recall.py)。

`SurfaceTraversalState` 本身没有场修订字段。实验 CLI 的 `surface` 重放 `--choose` 历史，`recall` 独立接受入口坐标；这条实验链未直接绑定观场、选择与召回所用的同一场快照。对于可变场，应在薄适配中绑定场摘要、来源快照、已显示候选与选择，复用已有状态序列化和导航操作。

这里报告的是源码中可见的适配缺口，并未执行并发场更新实验，也不主张整个 Core 已经发生数据损坏。本交付没有修改 Nollm 实现。

`task_recall.py` 使用键、路径、正文词重合以及共同证据来源辅助入口和放置。它可作为工程上的混合模式；其收益需要与从 Surface 观察选择入口的原生模式分开归因。

## 5. 本轮实际执行

本地运行：

~~~sh
cd experiments/research_memory/20261120_design/evaluation
python3 -m unittest -v test_validation.py
python3 validate_evaluation.py fixtures/synthetic_valid_run.json
~~~

第一行表示发布后的仓库位置。本轮实际运行工作目录为交付包的对应 `evaluation/` 目录。

结果：**38 项针对性检查全部通过；合成有效例 CLI 检查通过。** 本次实际命令输出及运行范围保存于 [VALIDATION_RESULT.json](VALIDATION_RESULT.json)。

覆盖的具体风险包括：

- 合法 FREE A 精确定义查询被误禁，以及目标非必需成果训练助手被误报为相对盲。
- 未来科学材料、答案材料或同依赖族训练材料进入声明的评测范围。
- 现行治理与历史科学回放被错误地使用同一时间截止。
- Nollm 使用答案入口或备用来源，却申报原生独立成功；即使备用来源列表漏填，声明的读取轨迹仍用于检查。
- 私有来源被声明导出到公开产物。
- 作者稿、候选关系或条件合同被擅自升级。
- 仅比较记忆时主模型却发生变化，以及无效运行对象使检查器异常退出。
- 快照名称相同但实际源版本、可见范围或辅助模型配置不同，却被当作同一受控对照。
- FREE A 的标题、预览和错误输出遗漏暴露检查；合法的受限词法视图被后端标签误禁；普通 TASK 输入被误当作 FREE A 必需基础。

架构与评测实现经过分工复核；上述具体误放行或误拒绝在检查器中修正并加入对应正反例。这是本工程提案的检查，不是科学论文的独立接纳或真实模式的效果复现。

检查器只分析传入的记录和轨迹，不证明它们完整或真实。输出固定包含 `scope: DECLARED_CONTRACT_ONLY`，并明确未验证真实访问权限、未声明泄漏、模型历史暴露、数学正确性、检索效果和费用节省。

## 6. 下一轮需要产生的实际证据

按主方案，以现有条目查询建立可用基线，然后使用共同运行记录逐项接入候选模式。真实运行应提供任务与来源快照、模型及适配器版本、资料曝光、工具轨迹、正确使用评价、冷/热/更新成本和失败记录。

旧题可以验证回归；新模式的采用由隔离的新任务和实际工作量决定。训练助手的收益只有在固定主模型、候选池和未训练对照后才可归于训练。
