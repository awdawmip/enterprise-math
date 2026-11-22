# 参与进取数论

感谢你帮助检验这个项目。

[英文版](CONTRIBUTING.md)

## 代理与项目任务入口

`AGENTS.md` 仅提供入口。按当前任务选择适用的公开项目指引，复用仍有效的已读上下文。账户通用要求通过用户授权的账户入口读取；公开贡献者无需访问私有知识库。

| 当前工作 | 公开项目入口 |
|---|---|
| 研究推进与成果保全 | [现行研究协议](docs/PORTABLE_RESEARCH_PROTOCOL.md) |
| FREE A 以外的项目原生语义 | [P000](p000_reality_foundation.json) 及其声明的配套契约；研究时的[心跳世界](definitions/HEARTBEAT_WORLD_NATIVE_X6_TIME.json) |
| 候选冻结前的 FREE（含 P000） | [A 阶段基础包](definitions/EM_FREE_A_FOUNDATION_STARTUP.json)与[原始基底入口](definitions/00_FREE_AXIOM_DISCOVERY_SUBSTRATE.md) |
| 正式任务或控制操作 | [架构与角色](docs/RESEARCH_ARCHITECTURE.md)、[现行控制优先级](control_plane/current_control_authority.json)、[运行状态机](docs/RESEARCH_RUNTIME_STATE_MACHINE.md)、[V2 发布协议](docs/RESEARCH_TASK_PUBLICATION_PROTOCOL.md) |
| 研究身份与活动 | [角色身份](docs/RESEARCH_IDENTITY_PROTOCOL.md)、[活动持久化](docs/RESEARCH_ACTIVITY_PROTOCOL.md) |
| BRC 残差拟合 | [原生 X6 语义对齐](research_notes/BRC_NATIVE_X6_SEMANTIC_ALIGNMENT_20261002_9D72AC.md) |
| Driver 组织与续接 | [研究线职责](docs/CODEX_RESEARCH_ORCHESTRATION.zh-CN.md)、[Source 续接协议](docs/RESEARCH_CONTINUATION_PROTOCOL.md) |
| 工具与来源操作 | [工具复用协议](docs/ENTERPRISE_TOOL_INVOCATION_PROTOCOL.md)、[GitHub 与来源读取协议](docs/GITHUB_INTERACTION_BUDGET.md) |
| 无正式绑定的维护汇报 | [汇报适用范围](docs/CHATGPT_ORDINARY_CONTROL.zh-CN.md#8-最终回复前的只读检查) |

选定任务后，从精确任务书、现行不可变发布及首个必要依赖开始，出现具体需要时再扩展。下方“从小问题开始”的前人工作目录适用于普通定向贡献；FREE Phase A 在冻结前走原始基底入口。既有正式角色、任务与所有权绑定仍按各自规范核验。普通汇报和不改变共享状态的自由推导不宣称取得这些权限。构建、测试命令及贡献操作保留在本指引与引用的项目文档中。

## 你不需要赞同整个理论

最有价值的贡献完全可能是证明某个候选规则错误。

遇到可复现的冲突，请给出前提、定义、适用域和最短的失败推导或实现。尚未查明原因时，保留该范围内的冲突供复核。P000 作为项目起点的变更由用户直接决定。派生物理模型提出的预测仍可按其声明的观测量和参数接受检验。[物理反证契约](docs/P016_PHYSICAL_FALSIFICATION_CONTRACT.zh-CN.md)

可接受的贡献包括：

- 数学证明；
- 反例；
- 定义改进；
- 前人工作识别；
- 纯整数实现；
- 形式化证明；
- 物理反证方案；
- 文档与翻译。

## 从小问题开始

提出宏大新理论之前，请先阅读：

1. `docs/SPEC_v0.1.zh-CN.md`
2. `docs/THEOREMS.zh-CN.md`
3. `docs/COUNTEREXAMPLES.zh-CN.md`
4. `docs/OPEN_PROBLEMS.zh-CN.md`
5. `docs/PRIOR_ART_AND_NOVELTY.zh-CN.md`

尽可能选择一个已经编号的问题。

## 结论状态

用上下文或定理陈述说明实质结论的状态。同一状态可覆盖一段连贯论证，普通笔记不必给每步推理加标签。规范结果记录沿用以下标签：

- `DEFINITION`
- `PROVED`
- `CONJECTURE`
- `COUNTEREXAMPLE`
- `COMPUTATIONAL`
- `PHYSICAL-HYPOTHESIS`

不能把计算证据写成数学证明。

不能把数学类比写成物理证据。

## 前人工作与引用来源

发现更早的前人工作本身就是一等贡献。

研究笔记、计算、论文草稿和普通讨论，在论证实际使用的位置引用相关论文、定理、页码或稳定链接即可。继续研究和保存草稿，不要求为这些引用另建来源登记、谱系记录或翻译。

将外部来源整合进规范的项目参考文献／定义说明体系时：

1. 尽可能核验原始来源；
2. 在 `sources.json` 中新增或复用稳定 `SRC-*` 记录；
3. 在 `lineage.json` 中把来源连接到相关 `EM-COMP-*` 构件；
4. 把关系标记为 `ADOPT`、`EXTEND`、`REINTERPRET`、`COMBINE`、`CONTRAST` 或 `INSPIRE`；
5. 如果新来源改变了思想谱系或创新边界，同步更新双语前人工作/创新图。

不能因为一次检索没有发现相同结果，就声称拥有历史优先权。

修改创新表述前，请阅读 `docs/CITATION_POLICY.zh-CN.md`。

## 双语规范文档

研究笔记、计算、论文草稿、交接、Issue 和讨论可以只使用英文或只使用中文。交付明确要求翻译，或整合进既有双语规范文档时，再处理对应译文。

规范性文字文件必须保持英文和中文语义对同步。贡献者不要求同时掌握两种语言：合并前可以由维护者补齐另一语言版本。

规范文档对的语义更新在两个版本一致时完成；工作草稿可以先保存，配对要求不扩展到每份研究材料。

## 代码规则

v0.1 参考核心只允许整数运算。

在 `src/enterprise_math/core.py` 中：

- 禁止浮点常量；
- 禁止真除法；
- 禁止偷偷调用浮点根函数；
- 行为必须服从文字规范。

软件改动验证受影响的行为；数学工作复核实际论证或计算。完整书面证明不以 Lean 为前提，计算脚本也不因可执行就必须产品化打包、提供公开 API 或配置全套软件测试。声称形式化验证时，仍须有对应的真实检查结果。质量、引用完整性、双语同步和 Lean 的常规 GitHub 工作流都改为手动触发，日常研究无需等待它们。

如果 Python 集成改动确实需要全套本地回归，用仓库的运行器同时覆盖 unittest 和 pytest 风格的测试：

```bash
python -m pip install pytest==8.4.2 sympy==1.14.0 jsonschema==4.25.1
PYTHONPATH=src python scripts/run_unittest_shard.py --index 0 --count 1
```

双语文件修改提交后，用实际基准提交检查两边是否一起修改。把 `BASE_REF` 设为本地可解析的目标分支或固定基准提交（例如已更新的 `origin/main`）。首条命令会核验它确实指向提交：

```bash
base=$(git rev-parse --verify "${BASE_REF:?请设置本地可解析的比较基准 BASE_REF}^{commit}") &&
python tools/check_bilingual_pairs.py --base "$base"
```

双语命令不带基准时只检查结构。整合规范来源／谱系登记体系的改动时运行 `python tools/check_references.py`。Lean 改动检查受影响的证明与依赖；影响整个证明层时再用 `lake build --wfail -KCI EnterpriseMath`。普通学术引用和纯文字研究修改无需全仓构建。

## Pull Request

一个 Pull Request 尽量只解决一个概念问题。

好的 Pull Request 应写清楚：

- 修改了哪个精确命题或定义；
- 它属于证明、反例、计算还是解释；
- 测试或证明证据；
- 相关的前人工作；
- 使用外部工作时对应的 `SRC-*` / `EM-COMP-*` 谱系变更；
- 它对应哪个开放问题编号。

## 贡献信用

保留来源。

如果一个定理、反例、定义或实现思路来自某个 Issue 或 Pull Request，后续规范文档应在可行时保留该贡献来源。

项目不要求转让版权。被接受的贡献按仓库 MIT 许可证分发。

## 行为规范

可以对命题进行非常尖锐的批评，但应尊重参与研究的人。

详见 `CODE_OF_CONDUCT.zh-CN.md`。
