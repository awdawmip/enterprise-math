# 从 Trace Answer 到 Executable State：Continuation Closure

状态：`RESEARCH BRIDGE / NONCANONICAL`

一个 state representation 可能已经足以回答全部 declared terminal queries，却仍然太粗，无法继续执行 declared future transition language。本文把这个 repair law 精确化。

## 1. Stable-state closure operator

固定有限 state set、relation family、coefficient semiring K 与 initial observation partition `P_0`。

记

`C_K(P)`

为从 partition P 出发，使 K-weighted transition interface 稳定的唯一 coarsest refinement。

令

`E=C_K(P_0)`。

E 就是 initial observation 之下最小的 executable K-branching state。

## 2. Interval absorption theorem

设 T 是任意满足

`E refines T refines P_0`

的中间 partition。

则

`C_K(T)=E`。

证明：

- E 已经 K-stable 且 refine T，所以按 `C_K(T)` 的 coarsest 性，E refine `C_K(T)`；
- `C_K(T)` 又是 K-stable 且 refine `P_0`，所以按 `E=C_K(P_0)` 的 coarsest 性，`C_K(T)` refine E。

故二者相等。

因此，一旦 transition interface 已声明，所有位于 E 与 P_0 之间的 underresolved readout，只要重新要求 continuation，都会修复回同一个 canonical executable state。

## 3. Terminal trace answer 是 canonical intermediate partition

K-branching signature 可以 deterministic 地投影出所有 terminal K-valued word traces，因此

`E_branching refines T_trace`。

而 empty word 保留 current observation，所以

`T_trace refines P_0`。

于是 interval theorem 立即给出：

`C_K(T_trace)=E_branching`。

也就是说，对完整 terminal-trace answer 做最粗 transition-stable refinement，精确恢复原本的 minimal branching state。

## 4. Sufficient answer 不等于 sufficient state

这里得到两个不同概念：

- **answer precision**：当前足以回答 declared terminal queries；
- **state precision**：还必须让 declared transition interface 能继续执行、继续递归使用。

第二种可能严格更细。

## 5. Continuation debt

对任意位于 interval 内的 answer partition，定义：

`continuation debt = #blocks(E_branching) - #blocks(T_answer)`。

它表示：仅仅因为 representation 要继续充当 future state，而不是一次性 readout，必须额外恢复多少 state distinctions。

branch 同时记录从 answer partition 修回 stable state 所需的 strict refinement rounds。

## 6. Boolean support 的 choice-timing witness

使用六状态结构：

`p = a.(b+c)`

与

`q = a.b + a.c`。

所有 terminal Boolean-support literal-word traces 都合并 p/q，因为每一个 word 的 terminal support 相同。

但 support-stable branching state 必须区分它们，因为 b/c choice 发生的层级/位置属于能够继续执行的 structure。

因此 terminal answer 有正 continuation debt；增加一个 block、做一轮 repair 就恢复 executable state。

## 7. Exact natural-count correlation witness

在 count-correlation fixture 中，p/q 的全部 terminal natural path-count traces 相同，但 successor future-count types 的 multiset 不同。

terminal answer 再次合并 p/q，而 exact count-branching state 会区分它们。

因此 continuation debt 不只来自 Boolean support 或 choice timing；terminal summation 丢失 successor count correlation 时同样会发生。

## 8. Answer 已 stable 时 debt 为零

若 T 本身已经 K-stable，则 `C_K(T)=T`。而 interval absorption 又要求 `C_K(T)=E`，所以 T=E。

因此 continuation debt 为0，当且仅当 supplied answer representation 本身已经是合法的 executable K-state。

## 9. Closure-operator interpretation

`C_K` 可以理解成 partition refinement order 上的“闭包到 transition stability”算子，只是本项目约定 finer partition 表示更多 state detail。

interval theorem 表明：canonical stable state E 一旦确定，任何 E 与 original observation 之间的中间 readout 都位于同一个 continuation-repair basin。

所以这不是只针对 trace 的特例 theorem。

## 10. Semantic-precision consequence

声明 future language 后，只问

`这个 quotient 能回答什么？`

不足以判断它能不能作为 reusable state。

还必须问：

`declared future operation 在这个 answer partition 上是否仍然 descend？`

若不能，canonical semantic repair 会精确恢复 E 中为 continuation 所必需的 distinctions。

## Owner-local assets

- `src/enterprise_math/relation_trace_to_state_closure.py`；
- `tests/test_relation_trace_to_state_closure.py`；
- `docs/PRECISION_TRACE_TO_STATE_CONTINUATION_CLOSURE.{en,zh}.md`。

Regression 包括 Boolean choice-timing witness、exact-count correlation witness、zero-debt case、partition-order validation，以及 4-state 全 partition interval absorption 检查。

## Prior art / status

Closure operator、congruence refinement、bisimulation/trace distinction 与 automata minimization 都是标准既有数学/CS。A4 保留 relation/witness ownership；P023/A2 保留 future-signature 与 semantic-precision ownership。本文只拥有 answer→state continuation repair 的显式项目化解释。

不声明 canonical-main 或新的 `EXECUTABLE_CHECKED`。Hard block: `NONE`。