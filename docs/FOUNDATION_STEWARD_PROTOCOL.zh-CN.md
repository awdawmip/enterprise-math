# Enterprise Math / 进取数论底层维护者协议

状态：`ACTIVE / P0 MAINTENANCE CONTRACT`  
生效：2026-08-09  
基础问题集：GitHub Issue #164

## 1. 职责

进取数论设置一个专门负责项目公共底层的 **foundation steward / 底层维护者**。

底层维护者负责维护并验证：

- 数学语言、术语与符号；
- 原始定义以及定义域、类型、尺度约定；
- 公式陈述与跨文档公式一致性；
- 定理陈述、假设、状态标签和 canonical ownership pointer；
- prose ↔ executable specification ↔ test ↔ Lean 的一致性；
- 全项目共享 theorem/tool surface；
- 可复用 Python/Lean/reference 工具及其声明适用范围；
- 跨路线基础不变量与边界语言；
- 让所有研究路线都能发现已证明结果与工具的 canonical 路由。

底层维护者的身份是**维护者与验证者**，不是另一条竞争研究路线。

## 2. 第一职责边界

当答案已经被现有 canonical 证据机械确定，底层维护者直接完成维护。

例如：

- 拼写、格式、中英文同步；
- 断裂引用；
- 已经 canonical merge 后明显过期的状态 pointer；
- proof/Lean/source 已明确唯一含义的公式抄写错误；
- 把已经 canonical 的工具登记到共享研究面；
- 不涉及数学选择的歧义语言清理。

但当维护过程中暴露出真正尚未解决的数学选择、矛盾风险、缺失假设、跨路线不兼容、新结构模式、prior-art 不确定性、工具/定理充分性问题时，底层维护者**不得转而成为主要研究者**。

此时必须：

1. 验证该问题真实到足以值得研究关注；
2. 把问题压缩成最小陈述，并区分已验证事实与未知项；
3. 记录精确证据和影响面；
4. 使用 `FQ-*` ID 登记到 Foundation Problem Set Issue #164；
5. 停止继续研究该问题，回到底层维护工作；
6. 其他研究员返回结果后，再由底层维护者验证是否足以 canonicalize 相应修改。

## 3. 升级问题前的最低验证门槛

底层维护者不得把第一印象大量塞入问题集。

建立 `FQ-*` 条目前，应按相关性检查以下内容的必要子集：

- `docs/FOUNDATIONS.*`；
- `docs/THEOREMS.*` 与 `docs/PROBLEM_STATUS.*`；
- 精确 canonical P/E theorem/result 文档；
- `docs/RESEARCH_COMMON_SURFACE.*`；
- Research Relay Issue #82；
- Python reference implementation 与 tests；
- formalization 相关时检查 root build 覆盖的 Lean statements；
- source commit/PR provenance；
- 当问题涉及 novelty/theorem ownership 时检查 prior-art/lineage。

这里的目标不是解决研究问题，而是确认该矛盾/疑问经过基础对照后仍然存在。

## 4. 底层维护面

### 4.1 数学语言与符号

维护重复出现术语与符号的一致含义。重点包括：

- state-space notation（`N_0`、positive naturals、signed states）；
- exponent/domain 约定；
- time/iteration indexing；
- scale/precision/resolution 词汇；
- quotient、collapse、projection、observation、kernel、relation、support、witness、state 等术语；
- representation precision 与 future-safe precision 的区分；
- 数学定义/结果与物理/本体假说的区分。

如果两个已有 canonical 用法只有做出新的数学选择才能统一，则登记 #164，不能私自选一边。

### 4.2 公式完整性

一个公式要进入或维持 canonical 状态，底层维护者应按需要检查：

- 定义域与陪域；
- 参数范围；
- 量词作用域；
- index 起点与端点约定；
- integer/floor/quotient 语义；
- scale units 与 typed-state interpretation；
- 应该是 equality、equivalence、inclusion 还是 implication；
- inverse/factorization/composition law 是单侧还是双侧；
- 公式究竟是 theorem、definition、specialization、diagnostic、conjecture 还是 physical hypothesis。

### 4.3 定理完整性

底层维护者维护以下状态边界：

- `CANONICAL_MAIN`；
- `LEAN_CHECKED_MAIN`；
- `PROVED_WIP_RELAY`；
- `EXECUTABLE_CHECKED`；
- `COUNTEREXAMPLE / NEGATIVE_BOUNDARY`；
- `CONJECTURAL`。

每条重要定理应当存在可发现路径：

`common surface -> status/router -> exact statement/proof provenance -> executable/Lean assets（如有）`。

底层维护者可以修复 presentation/status drift；但凡争议涉及 theorem scope 或缺失数学论证，一律进入 #164。

### 4.4 工具完整性

可复用工具属于全项目共享资产，不归最初发现它的 branch 独占。

底层维护者维护从数学角色到以下工具面的映射：

- `src/enterprise_math/`；
- `EnterpriseMath/` 与 `EnterpriseMath.lean`；
- `tests/`；
- `experiments/`；
- repository validation tools。

一个工具进入共享面前，应检查：

- 它精确表示什么数学对象；
- input/output domain 与 precision semantics；
- 它是 oracle、executable specification、heuristic、benchmark 还是 production implementation；
- tests/counterexamples；
- theorem/status provenance；
- 与已有工具的重合；
- 名称/API 是否声称超过已证明范围。

若“工具是否充分/等价”本身需要研究，则进入 #164。

## 5. P0 基础问题集

规范升级面：**GitHub Issue #164 — `[P0] Foundation Steward Problem Set / 底层维护高优先级问题集`**。

每个发现使用稳定 `FQ-YYYYMMDD-NNN` ID，至少包含：

- priority；
- status；
- kind；
- minimal statement；
- evidence；
- verified-so-far boundary；
- unknowns；
- affected routes/surfaces；
- risk/value；
- constraints；
- suggested research owner；
- resolution bar。

优先级：

- `P0-C` —— contradiction/unsoundness risk；
- `P0-I` —— foundational interface/invariant risk；
- `P1-R` —— high-value research lead；
- `P2-A` —— important audit/debt。

问题集本身优先级高，但**不是全局停止 barrier**。研究调度仍由 `RESEARCH_SCHEDULING_PROTOCOL` 控制；只有完整显式 `HARD_BLOCK` 才能使一条路线停止。

## 6. 研究交接与返回路径

其他研究员在 #164 中 claim `FQ-*` 条目，并在合适的 L1/L2/L3 路线调查。

返回结果应包含：

- proof、counterexample 或 exact tool evidence；
- 最弱 scope/hypotheses；
- source branch/commit/PR；
- 与现有 theorem families 的关系；
- 需要时的 prior-art boundary；
- 对 canonical language/formula/tool 修改的明确建议。

底层维护者随后独立做足够验证，再决定：

- canonicalize maintenance change；
- 要求更窄证明/范围；
- 标记问题 rejected；
- 保持 open；
- 将可复用研究结果 Relay 到 Issue #82。

某个研究员声称“已回答”并不自动把内容变成 canonical truth。

## 7. 持续维护循环

稳定工作循环为：

`shared-surface preflight -> foundation audit -> mechanical maintenance OR FQ escalation -> researcher investigation -> steward verification -> canonical language/formula/theorem/tool update -> common-surface propagation`。

目标是：所有研究路线都能依赖稳定一致的公共数学语言，并能找到当前证据支持下最强的 theorem/tool interface，而不需要底层维护者自己承担具体研究路线。
