# 参与进取数论

感谢你帮助检验这个项目。

[英文版](CONTRIBUTING.md)

## 代理与项目任务入口

`AGENTS.md` 仅提供入口。按当前任务选择适用的公开项目指引，复用仍有效的已读上下文。账户通用要求通过用户授权的账户入口读取；公开贡献者无需访问私有知识库。

| 当前工作 | 公开项目入口 |
|---|---|
| 研究推进与成果保全 | [现行研究协议](docs/PORTABLE_RESEARCH_PROTOCOL.md) |
| 项目原生语义 | [P000](p000_reality_foundation.json) 及其声明的配套契约；研究时的[心跳世界](definitions/HEARTBEAT_WORLD_NATIVE_X6_TIME.json) |
| 候选冻结前的 FREE | [仅原始基底入口](definitions/00_FREE_AXIOM_DISCOVERY_SUBSTRATE.md) |
| 正式任务或控制操作 | [架构与角色](docs/RESEARCH_ARCHITECTURE.md)、[现行控制优先级](control_plane/current_control_authority.json)、[运行状态机](docs/RESEARCH_RUNTIME_STATE_MACHINE.md)、[V2 发布协议](docs/RESEARCH_TASK_PUBLICATION_PROTOCOL.md) |
| 研究身份与活动 | [角色身份](docs/RESEARCH_IDENTITY_PROTOCOL.md)、[活动持久化](docs/RESEARCH_ACTIVITY_PROTOCOL.md) |
| BRC 残差拟合 | [原生 X6 语义对齐](research_notes/BRC_NATIVE_X6_SEMANTIC_ALIGNMENT_20261002_9D72AC.md) |
| Driver 组织与续接 | [研究线职责](docs/CODEX_RESEARCH_ORCHESTRATION.zh-CN.md)、[Source 续接协议](docs/RESEARCH_CONTINUATION_PROTOCOL.md) |
| 工具与来源操作 | [工具复用协议](docs/ENTERPRISE_TOOL_INVOCATION_PROTOCOL.md)、[GitHub 与来源读取协议](docs/GITHUB_INTERACTION_BUDGET.md) |
| 无正式绑定的维护汇报 | [汇报适用范围](docs/CHATGPT_ORDINARY_CONTROL.zh-CN.md#8-最终回复前的只读检查) |

选定任务后，从精确任务书、现行不可变发布及首个必要依赖开始，出现具体需要时再扩展。下方“从小问题开始”的前人工作目录适用于普通定向贡献；FREE Phase A 在冻结前走原始基底入口。既有正式角色、任务与所有权绑定仍按各自规范核验。普通汇报和不改变共享状态的自由推导不宣称取得这些权限。构建、测试命令及贡献操作保留在本指引与引用的项目文档中。

## 你不需要赞同整个理论

最有价值的贡献完全可能是证明某个候选规则错误。

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

每一个实质结论都应标记为以下一种：

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

如果你的变更实质使用了外部来源：

1. 尽可能核验原始来源；
2. 在 `sources.json` 中新增或复用稳定 `SRC-*` 记录；
3. 在 `lineage.json` 中把来源连接到相关 `EM-COMP-*` 构件；
4. 把关系标记为 `ADOPT`、`EXTEND`、`REINTERPRET`、`COMBINE`、`CONTRAST` 或 `INSPIRE`；
5. 如果新来源改变了思想谱系或创新边界，同步更新双语前人工作/创新图。

不能因为一次检索没有发现相同结果，就声称拥有历史优先权。

修改创新表述前，请阅读 `docs/CITATION_POLICY.zh-CN.md`。

## 双语规范文档

Issue 和讨论可以只使用英文或只使用中文。

规范性文字文件必须保持英文和中文语义对同步。贡献者不要求同时掌握两种语言：合并前可以由维护者补齐另一语言版本。

只修改一份规范语言文件、却没有同步另一份的 Pull Request 属于未完成状态。

## 代码规则

v0.1 参考核心只允许整数运算。

在 `src/enterprise_math/core.py` 中：

- 禁止浮点常量；
- 禁止真除法；
- 禁止偷偷调用浮点根函数；
- 行为必须服从文字规范。

运行：

```bash
PYTHONPATH=src python -m unittest discover -s tests -v
python tools/check_bilingual_pairs.py
python tools/check_references.py
```

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
