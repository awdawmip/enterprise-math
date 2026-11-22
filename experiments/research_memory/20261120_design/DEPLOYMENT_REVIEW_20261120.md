# Nollm 研究记忆部署前复审

日期：2026-11-20（UTC+08:00）。范围：内部试验组件的实际可用性及接入条件。

## 结论

**可以部署为能调用本地 CLI／skill 的 Codex 或研究 Host 的单写者内部试用组件。** 本轮未发现需要先修复的代码级试用阻碍。用户要求的精简实现保留；无需新增防御性代码、无谓哈希、鉴权或验证平台。

若目标是让现有普通 Chat 定时研究直接调用，部署还需落实现有服务上的薄工具入口和可持续访问的工作场。这个 PR 提供 CLI／skill，没有完成研究中控台／MCP 接入。本次验证是在独立本地目录实际安装运行；没有部署到共享服务或修改调度。

## 固定对象与保存内容

- [Nollm PR #7](https://github.com/awdawmip/Nollm/pull/7)，实现提交 `eddfb7c81aae2981c48c4063c7ac75e272ff15a4`。
- base 为 `experiment/repository-memory@cf10ab849c2b32132de01328061d172377729161`；核对时 PR open、draft、mergeable clean。
- Nollm main 仍为 `bafc6de4e8213d50a5ec64754c7bc87983f853ac`。部署此原型须使用上述实现版本，不能把 main 当作已经包含它。
- [使用说明](https://github.com/awdawmip/Nollm/blob/eddfb7c81aae2981c48c4063c7ac75e272ff15a4/lab/nollm-lab/repository_memory/enterprise_math/README.md)、[实际试用](https://github.com/awdawmip/Nollm/blob/eddfb7c81aae2981c48c4063c7ac75e272ff15a4/lab/nollm-lab/repository_memory/enterprise_math/TRIAL.md)。
- 当前场包含 11 条当前判断和 1 条历史版本，涵盖 CRT、X6、有限生成模及素操作相关材料。语句、绑定及原生场已随分支保存。
- 引用固定在 EM `f16294a5a7ffa435a32b70214d881fd4450eb494` 的明确路径和行区间；这与当前 EM main 是不同来源时点。

## 本轮实际运行

按上述固定 Nollm 提交取出安装器及其运行依赖，在 Python 3.12.14、Git 2.56.1 环境中执行。没有改被测实现，没有将原报告的通过记录充当本次运行。

| 检查 | 实际结果 |
|---|---|
| `python3 -m unittest discover -s lab/nollm-lab/repository_memory -p test_enterprise_math.py -v` | 1 项通过，3.135 秒，exit 0 |
| `python3 -m unittest discover -s lab/nollm-lab/repository_memory -p test_skill_install.py -v` | 2 项通过，2.835 秒，exit 0 |
| `python3 -I lab/nollm-lab/repository_memory/install_skill.py --dest <独立目录>` | 安装成功，exit 0 |
| 从仓库外以 `python3 -I <安装目录>/scripts/memory.py em walk` 打开随安装保存的场 | 返回实际 Surface 和 CRT 提要，exit 0 |
| 选择 Surface，再选择其物理候选 | 得到入口 `[0,-1,-1]`，召回 `CRT.prefix-subsets`，并经 lateral 返回 `NT-SUP-CRT-CARRY` 与 `CRT.repair`，exit 0 |
| `em show X6-QUADRATIC-MODULAR.v2` 与 `em show X6-QUADRATIC-MODULAR.oct` | 新版 `current: true`、旧版 `current: false`，正文、来源和 `revises` 均可读，exit 0 |

科研回归实际通过安装版入口完成新场保存、局部更正、旧新 Git 来源窗口、当前绑定、相邻召回与远格排除。这里的 Git 来源端到端测试使用合成测试仓库；真实 EM 原文和保存语句另按固定来源读取核对。本轮未在目标部署主机验证 EM Git 对象可达性。

实际召回还返回了 `budget_exhausted: true`；这是所用有限邻域预算的真实状态，不能将一次未命中解释为资料不存在。后续可按问题继续导航或精确回源。

## 独立材料和实现审查

实现直接复用 Core、Access、Surface、版本化语句和绑定。语义形成与位置选择由 Host 完成；`find` 如实作为字面辅助路径。未见新增防御性框架。安装器携带原生场和运行包，仓库版与安装版使用相同科研入口。

审查读取全部 12 份保存语句及绑定，并对照主要 CRT/X6 原文。未发现影响本轮试用结论的主要公式、前提或出处误记。当前语句保留固定支持、对象域、观察条件和获取费用；X6 的原稿／复核范围未升级为正式接纳。新 `CRT.prefix-subsets` 明示本会话推论及尚无单独评审。该检查属于记忆内容保真审查，不是新的正式数学 Review 或接纳。

原 TRIAL 报告五个真实新会话的开放开发诊断，包括首题三路比较、首位原生读者续写、另一新会话使用新增判断解决改变基线后的第二题。保存状态与报告所述续写一致。本轮复跑安装和软件链路，没有重复运行这五个模型实验；没有获取它们的完整模型账单。

## 效率结果怎样解释

| 计量口径 | 原生记忆工具标准输出 | 普通来源检索 |
|---|---:|---:|
| 两次答题 | 52,828 B | 99,248 B |
| 原生侧再计入实际形成、修订和续写 | 114,703 B | 99,248 B |

后一口径原生侧多 15,455 B，约 15.6%；还存在前期未单独计量阅读与错误输出。首题固定语义内容时，字面路径比 Surface 少返回 9,702 B。两题各路答案均正确。

这些数字是工具端 UTF-8 字节，不能换算为完整模型 token、推理费用或总算力。当前可以认定形成了可继续使用的记忆能力，尚未测出总体成本优势。继续真实试用有价值，无需为了部署资格把负结果调成正结果。

## 建议部署方式

1. 将已验证版本安装到能够运行 Python/Git 的现有研究 Host。首次内部使用可以直接沿现有 skill 安装器完成，不需独立模型服务。
2. 使用已有 `em --field PATH` 指向明确、可持续访问的工作目录；初次可从随分支保存的场开始。后续会话始终使用这一工作场，代码升级保留已续写内容。安装副本与源码中的种子场分别持久，代码不会自动同步它们。
3. 按当前单写者模式使用。供多位研究者复用时，可分发同一已保存视图的独立工作副本，或沿现有 Host 串行访问；续写由同一实际写入者维护，或各自使用独立工作场。现有 PR 没有声称支持多研究进程并发改写同一场。
4. 目标 Host 准备能读取所引用固定提交的 EM Git 工作副本。保存时的 `current` 表示当前记忆版本，不表示全库已自动同步到最新；新成果按需导入和修订。
5. 若部署目标是普通 Chat／现有定时研究，在现有服务中转接这套核心调用，并用真实研究会话验证导航、回源及保存后再读取。无需为此重做记忆算法或搭建另一套控制平台。

上述是目标环境的接入事项，不是新增科研思考步骤。FREE A、全库自动更新、长期多写者协作和大规模成本优势分别按实际后续用途验证；不将这些扩大为当前内部 TASK 试用的全套前置门槛。

## 交付状态

本轮完成源码/资料复审、三项回归复跑、独立安装及实际导航读取，结论为内部 CLI／Codex 试用可部署。PR 合并、共享主机部署及现有 Chat 研究工具接入尚未执行。此文件保留部署决策依据，科学接纳和研究调度不由该结论改变。
