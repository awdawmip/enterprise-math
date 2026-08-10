# Precision 的三种契约：Readout × Executable State × Presentation

状态：`FOUNDATION-FACING RESEARCH BRIDGE / NONCANONICAL`

近期 A2/P023/A4 结果表明，单一术语“precision”正在被要求同时完成三种不同工作：一个 representation 可能足以回答当前 query，却不足以继续执行 declared dynamics；反过来，一个非常小的 local code 又可能足以重建 exact law，并在 exact execution layer 中生成远大于 code range 的 future values。

本文不新增 Foundation Question，也不改变既有五层 diagnostic failure locations；它只细化**所需语义确定之后，representation 应如何分层**。

## 1. Readout precision

**Readout** 指：当前足以精确回答 declared query family 的信息。

例如：

- 每个 literal word 的 terminal support；
- terminal path-count traces；
- 一个 static future-equivalence class label；
- 一组 finite modular answers。

Readout precision 是 task-relative 的，并且可以有意忘掉 answer 是如何生成的。

readout 不必是 reusable world state。

## 2. Executable-state precision

representation 若要成为 future theory T 的**executable state**，必须让 T 中 declared operations / relations 在 coarse state 上真正 descend，并能继续执行，而无需重新读取被删除的 fine detail。

这比 readout sufficiency 更强。

对 finite weighted relation interface，存在 canonical operation-stability closure `C_T`。若

`E=C_T(P_0)`

是 original observation 之下的 minimal executable state，而某 answer partition A 满足

`E refines A refines P_0`，

则

`C_T(A)=E`。

也就是说，任何位于该 interval 内的 underresolved answer，只要重新要求 continuation，就会修回同一个 canonical executable state。

## 3. Continuation debt

answer precision 与 executable-state precision 的差可以量化。

对 finite partitions，一个 exact 指标是：

`continuation debt = #blocks(executable state) - #blocks(answer)`。

positive debt 不表示 answer 错了；它表示 answer 删除的某些 distinctions 只有在 world 必须继续演化时才重新变得必要。

因此必须分开：

`correct one-shot answer`

与

`correct recursively reusable state`。

## 4. Local observation code 又是第三个层次

一个 executable exact model 有时可以从非常小的 finite local code 中重建。

若 world law 的 local coefficients 只来自有限 alphabet L，则 code

`c:L->C`

只需要在 L 上 injective，就足以恢复 exact local values。

C 自己甚至不需要支持 future algebra。

安全路线是：

`finite local code`

`-> exact local reflection / decode`

`-> exact executable law`

`-> 在 exact algebra 中派生 future semantics`。

## 5. 先 reflect generators，再 compose

quotient 可以精确反射全部 bounded local generators，却无法直接反射较大的 derived values。

典型结构：

- local primitive coefficients 只有1与2；
- mod3 完全区分 `{0,1,2}`；
- 两步 derived values4与1却在 mod3 中碰撞。

如果一直在 coarse quotient 内 composition，exact outputs 会丢失。

如果先 decode local coefficients，恢复 exact transition law，再在 exact algebra 中 composition，就能正确生成4与1。

因此：

`exact local code`

不是

`every derived answer 都能被同一个 code 直接 exact readout`。

## 6. Presentation precision

**Presentation** 是一个 finite exact description：它保存 generator/update law，并配一个 evaluator，用来计算 future semantics。

评价 presentation 是否“足够精确”，关键不是每个 future answer 是否已经显式储存在 representation 中，而是它是否 exact 地 presentation 了 declared future theory。

于是出现第三条轴：

- readout representation 存 answers；
- executable-state representation 存 continuation structure；
- presentation representation 存 exact generators/laws + evaluator。

同一个 future law 可以有多种 exact presentations，并具有不同 storage、numeric-range、execution-depth 成本。

## 7. Representation type 可以改变

即使 exact discrete executable state 已恢复，更弱的 future language 仍可能允许完全不同的 state type。

对 exact weighted machine，action matrices 为 B_a、observation rows 为 C，完整 terminal linear trace language 位于：

`W=span_Q{C B_w}`。

若 `r=dim_Q W`，则存在 exact r-dimensional rational predictive state，并具有 induced actions T_a 与 decoder H。

这种 state 通常不是 raw discrete state set 上的 partition quotient，而是 vector-state space 的 linear quotient。

## 8. State-class count 与 algebraic dimension 是不同资源

一个 sharp weighted example 有11个 trace-distinct discrete source states，但 exact predictive state 只有2维。

这里没有把11个 states 语义上合并：它们仍然是 Q^2 中11个不同 vectors。

信息从

`discrete class 数量`

转移到了

`较低维 algebraic state 中的 exact coordinate values`。

因此 class count、vector dimension 与 numeric range 是不同 precision coordinates。

## 9. Minimality 必须注明 representation class

对 terminal linear traces，rational row-space rank r 在线性 predictive representation 中是最小维数。

这不意味着它在所有 conceivable representation types 中 universally minimal。

同样，一个 relation interface 的 coarsest stable partition 只是在 declared partition/quotient class 内 minimal，不自动比 linear、probabilistic、symbolic 或 witness-enriched representation 更小。

所以任何 minimality theorem 都必须声明 representation class。

## 10. Semantic precision 至少已有四类独立资源

当前 architecture 不应把这些压成一个 scalar：

1. **observational distinction**：哪些 fine states 仍能区分；
2. **continuation capability**：哪些 declared operations/relations 仍能 descend；
3. **algebraic representation size/type**：class count、vector dimension、witness channels 等；
4. **numeric coefficient range / local code capacity**：exact values 如何表示或反射。

若比较同一 law 的不同 presentation，还应继续加入 execution depth / storage。

## 11. Structure 可以替代 direct numeric range

一个 structurally richer exact machine 可以从很小的 local code 中恢复，然后在内部生成很大的 future values。

structurally poorer direct-answer representation 则可能需要大得多的 numeric modulus/range，才能直接 reflect 同样的大 answers。

因此存在真实 resource tradeoff：

`more compositional structure + smaller local numeric code`

versus

`less structure + larger direct answer range`。

这不是 approximation；在各自 certificate 条件下，两条路线都可以 exact。

## 12. Readout join 与 state join 也不同

组合两个 readouts，只需要同时保留两个 labels。

若要让两个 executable interfaces 在同一个 shared state 上继续运行，则常常还需要额外 congruence/closure，因为一个 interface 对 target states 的 refinement 可能重新激活另一个 interface 的 unsafety。

所以“join two precisions”必须声明到底在 join：

- answers；
- reusable state interfaces；
- coefficient codes；
- 还是 complete presentations。

同一个 algebraic product 对一种 contract 可能 overprecision，对另一种 contract 却恰好 minimal。

## 13. Foundation routing rule

当某个 coarse representation 被称为“exact enough”时，必须分别问三个问题：

### Readout

它能否 exact 回答 declared query family？

### Continuation state

所有 declared future operations 能否继续作用，而无需 hidden fine-state access？

### Presentation

若它只是 local generators 的 code，是否存在 exact decoder 与 exact evaluator，使 future semantics 在 decode 后正确生成？

三者不能互相偷换。

## 14. 与既有 diagnostic layers 的关系

本文不新增 failure location。

- DOMAIN 仍负责 definedness / legality；
- RELATION 仍负责 branching / witness multiplicity；
- IMAGE/FIBER 仍负责 existence 与 hidden multiplicity；
- LEDGER 仍负责 retained history / remainder state。

这里新增的是：**这些必要语义确定后，一个 sufficient representation 应采用什么 packaging contract。**

## 15. Prior-art boundary

Automata minimization、sufficient statistics、system realization、weighted quotient、closure operator 与 presentation/evaluation tradeoff 都是标准既有数学/CS。

本项目在这里得到的综合结论是：

> **exact answer、exact reusable state 与 exact generator presentation 是三种不同 precision contracts；哪个更小、哪个更大，取决于 declared future execution。**

## Files

- `docs/PRECISION_READOUT_STATE_PRESENTATION.en.md`
- `docs/PRECISION_READOUT_STATE_PRESENTATION.zh.md`

Executable evidence 仍位于 A2/P023/A4 的 trace-to-state、bounded-local-law 与 linear-predictive child generations。

不声明 canonical-main 或 `EXECUTABLE_CHECKED`。Hard block: `NONE`。