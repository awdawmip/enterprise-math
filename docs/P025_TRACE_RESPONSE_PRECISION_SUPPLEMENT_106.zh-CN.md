# P025 补充 106 —— Trace-Sensitive Operation Precision 与不增加 State Precision

状态：`ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation：`program/p025-history-closure-stage101`  
依赖：P025 补充 105  
硬阻断：`NONE`

## 1. 表面上的问题

Stage105 已证明 endpoint semantics 与 trace semantics 不同：两个 action words 可以拥有同一个 final normal form `(I,t)` 与同一个 final area，却产生不同 intermediate area traces。

一个很自然但错误的推论是：

> trace semantics 因而一定需要更细的 state。

Stage106 证明，对 finite activation-area model，这个推论是假的。

state generator 可以完全不变。真正必须变细的是 **operation-word representation**。

## 2. P025-T242 —— endpoint generator 已能预测所有 traces

回忆 compact state generator

\[
\Gamma=(A;L_i;Q_j)
\]

以及静态 labelled merged-threshold order。

给定任意 valid action word

\[
w=a_1a_2\cdots a_m,
\]

令

\[
N_r=(I_r,t_r)
\]

为 prefix

\[
a_1\cdots a_r
\]

的 endpoint normal form。

Stage105 已给出 exact area function

\[
F_\Gamma(I,t).
\]

因此完整 area trace 只是

\[
\boxed{
\operatorname{Trace}_\Gamma(w)
=
\big(
F_\Gamma(N_1),
F_\Gamma(N_2),
\ldots,
F_\Gamma(N_m)
\big).
}
\]

完全不需要新增 state coordinate。

## 3. P025-T243 —— endpoint 与 trace languages 使用同一个 response-state generator

trace future language 比 endpoint language 更强，因为它要求全部 intermediate observations。

但是：

1. `Gamma` 由 P025-T242 能预测每条 trace；
2. trace response family 包含适当 words 的 endpoint responses 作为最后一项；
3. Stage105 已证明 endpoint response family 能恢复 `Gamma`。

因此

\[
\boxed{
\Gamma
\Longleftrightarrow
\text{完整 declared area-trace response family}.
}
\]

所以在这个模型中

\[
\boxed{
\Gamma_{\rm endpoint}
=
\Gamma_{\rm trace}.
}
\]

future-language refinement 并没有强迫 state-precision refinement。

## 4. P025-D49 —— prefix-normal-form path

虽然 state 不必变化，但 endpoint word quotient 已经过粗。

定义 prefix-normal-form path

\[
\boxed{P(w):=(N_1,N_2,\ldots,N_m).}
\]

这条 path 与 arithmetic state 无关，并且在已知 `Gamma` 后足以计算完整 trace。

因此 state-independent trace compiler 可以保存

\[
\boxed{(\Gamma,P(w))}
\]

而不需要保存每一步的 raw activation matrices。

## 5. P025-CE41 —— exact arithmetic operation-order boundary

对 `(q,p)=(3,41)` dyadic fixture，取 old threshold `1/25`、candidate threshold `11/20`，pressures 为

\[
\frac1{22},\frac{13}{22}.
\]

Stage105 已给：

\[
+T;+J:\quad\text{trace }(1,3),
\]

\[
+J;+T:\quad\text{trace }(2,3).
\]

从 current area `A=1` 看，对应 increment sequences 为

\[
\boxed{(0,2)}
\]

与

\[
\boxed{(1,1)}.
\]

state `Gamma` 完全相同，只有 operation order 改变。

这直接证明额外 precision 位于 operation side。

## 6. P025-T244 —— fixed-state trace equivalence 等价于 increment equivalence

对固定 current state `Gamma`，定义 word 上的 area increments

\[
\delta_r:=A_r-A_{r-1},
\qquad A_0=A.
\]

则

\[
A_r=A+\sum_{k=1}^{r}\delta_k.
\]

因此两个 words 有同一 area trace 当且仅当它们有同一 increment sequence：

\[
\boxed{
\operatorname{Trace}_\Gamma(w)
=
\operatorname{Trace}_\Gamma(w')
\iff
\delta_\Gamma(w)=\delta_\Gamma(w').
}
\]

所以 increment sequence 是 fixed-state area-trace output 的 exact semantic coordinate。

## 7. 负边界 —— prefix paths sufficient 但不总是 minimal

state-independent prefix path 保留 action identity 与 order；对固定 arithmetic state，它仍可能 over-precise。

取无 old thresholds、一个 old node value `1`，以及两个 candidate thresholds

\[
\frac12<\frac34.
\]

两个 candidates 都已经在 old node 上 active。因此

\[
+T_1;+T_2
\]

与

\[
+T_2;+T_1
\]

有不同 prefix-normal-form paths，但 area trace 都是

\[
\boxed{(1,2)}
\]

且 increment sequence 都是

\[
\boxed{(1,1).}
\]

所以 `P(w)` 是 canonical state-independent sufficient word representation，但不是每个固定 state 上的 coarsest trace quotient。

## 8. 真正的 precision split

Stages105–106 合起来给出：

### Endpoint future

- state coordinate：`Gamma`；
- operation coordinate：final normal form `(I,t)`。

### Trace future

- state coordinate：仍然是 `Gamma`；
- state-independent operation coordinate：prefix-normal-form path `P(w)`；
- fixed-state semantic operation coordinate：increment sequence `delta_Gamma(w)`。

因此

\[
\boxed{
\text{future-language refinement can refine the operation quotient without refining the state quotient}.
}
\]

## 9. 架构后果

Stage106 对 precision architecture 给出一个直接警告：

> richer future query 并不意味着 system state 的每个部分都必须更细。

precision 应当被加到真正承载丢失区分的对象上。这里丢失的是 action order，不是隐藏 arithmetic state。

future-compatible architecture 因而应允许 state precision 与 operation-word precision 独立演化。

## 10. Prior-art / novelty 边界

trace semantics、increment sequences、path semantics 与 state-versus-input sufficiency 都是广泛 prior concepts。P025 不单独主张这些概念新颖。

项目侧结果是把这些 distinctions 在 arithmetic history-precision pressure test 中精确分离，并提供 executable positive/negative boundaries。历史新颖性仍为 `NOVELTY_UNVERIFIED`。

## 11. 可执行资产

新增：

- `src/enterprise_math/abc_trace_response_precision.py`；
- `tests/test_abc_trace_response_precision.py`。

## 12. 下一前沿

Stages101–106 已形成完整 generation：

1. one-step signatures 不能自动闭合 two-step histories；
2. finite endpoint histories 精确在 second interaction order 闭合；
3. mixed block 具有 adaptive Ferrers structure；
4. expanded tensor 有 merged-rank generator；
5. endpoint words 坍缩为 `(I,t)`；
6. trace language 只细化 operation precision，不要求额外 state precision。

这里是自然 freeze point。下一 generation 应把这套 state/operation precision separation 放到非 monotone incidence-area observable 上压力测试，而不是继续在本 owner 追加 stages。