# P025 补充 105 —— Endpoint History Normal Form 与 Trace Boundary

状态：`ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation：`program/p025-history-closure-stage101`  
依赖：P025 补充 104  
硬阻断：`NONE`

## 1. compact endpoint response state

Stage104 已证明 finite endpoint-area future 可由

\[
\boxed{\Gamma=(A;L_1,\ldots,L_a;Q_1,\ldots,Q_b)}
\]

以及静态 labelled merged-threshold order 生成。

其中：

- `A` 是 current activation area；
- `L_i` 是 candidate threshold `U_i` 在 old block 中的 span；
- `Q_j` 是 future node `v_j` 在 old+candidate merged thresholds 中的 rank。

Stage105 进一步把 response state 与 action words 都压成 endpoint normal form。

## 2. P025-T239 —— endpoint action-word normal form

一个 valid action word 可以：

- 每个 candidate threshold `U_i` 最多插入一次；
- 按固定顺序追加 predeclared future nodes。

对 endpoint semantics，word 只通过

\[
\boxed{(I,t)}
\]

起作用，其中：

- `I subset {1,...,a}` 是最终插入的 candidate threshold 集；
- `0<=t<=b` 是已追加 future nodes 的数量。

threshold insertions 的内部顺序，以及它们与这 `t` 个 node appends 的 interleaving，都不会改变最终 threshold set 与 future-node prefix，所以也不会改变 endpoint activation matrix 与 area。

因此每个 valid action word 都坍缩到唯一 endpoint normal form `(I,t)`。

## 3. P025-T240 —— 精确 endpoint class count

candidate-threshold subsets 有

\[
2^a
\]

种，future-prefix lengths 有

\[
b+1
\]

种，因此 endpoint classes 恰有

\[
\boxed{2^a(b+1).}
\]

这通常远小于 raw valid interleavings 数量。

对固定 endpoint，若 `k=|I|` 个 selected thresholds、`t` 个 node appends，则坍缩到该 endpoint 的 valid words 数量为

\[
\boxed{\frac{(k+t)!}{t!}.}
\]

`k` 个 threshold actions 彼此不同，而 `t` 个 sequential node actions 的相对顺序已经固定。

## 4. P025-T241 —— `Gamma` 对 endpoint-area future 完备

对任意 endpoint normal form `(I,t)`，Stage104 可从 `Gamma` 精确计算 final area。

反过来，完整 endpoint-area response family 也能恢复 generator coordinates。

对每个 candidate threshold，

\[
L_i=A(\{i\},0)-A.
\]

对每个 future node increment，先用 empty candidate set 恢复 old-threshold contribution，再与每个 singleton candidate set 下的同一 increment 比较，即可恢复哪些 candidate thresholds 被跨过；它们数量与 old contribution 相加就是 merged rank `Q_j`。

因此

\[
\boxed{
\Gamma
\Longleftrightarrow
\text{declared envelope 中全部 endpoint-area responses}.
}
\]

所以 `(A;L_i;Q_j)` 是这个 future language 的 exact compact response normal form。

## 5. 负边界 —— endpoint semantics 不是 trace semantics

endpoint collapse 不能过度推广。

取 current threshold

\[
T=\frac14,
\]

current node value

\[
\rho_0=\frac12,
\]

candidate threshold

\[
U=\frac34,
\]

future node

\[
v_1=1.
\]

则：

- `+T ; +J` 的 area trace 为
  \[
  \boxed{(1,3)};
  \]
- `+J ; +T` 的 area trace 为
  \[
  \boxed{(2,3)}.
  \]

两个 words endpoint normal form 相同、final area 都是 `3`，但 intermediate responses 不同。

因此

\[
\boxed{
\text{endpoint commutation}
\not\Rightarrow
\text{trace commutation}.
}
\]

## 6. P025-CE40 —— exact arithmetic trace boundary

P025 dyadic pressure model 内部也出现同一现象。

取 `(q,p)=(3,41)`、exponent `2`，此时

\[
\rho_0=\frac1{22},
\qquad
\rho_1=\frac{13}{22}.
\]

old threshold 取

\[
T=\frac1{25},
\]

candidate threshold 取

\[
U=\frac{11}{20}.
\]

则

\[
+T;+J:\quad\boxed{(1,3)},
\]

而

\[
+J;+T:\quad\boxed{(2,3)}.
\]

最终 endpoint 相同，但第一次 observation 不同。

所以这不是 synthetic Boolean artifact。

## 7. future-language split

Stage105 因而分离两种 action languages。

### Endpoint language

future query：

> 执行这个 finite action word 后 final area 是多少？

此时 `(I,t)` 是 word normal form，`Gamma` 是 complete response state。

### Trace language

future query：

> 每个 action prefix 后观察到的 area 是多少？

此时 endpoint normal form 不够；由于 intermediate observations 属于 declared future，action order 必须被保留。

所以即使 underlying final state 相同，正确 quotient 仍然依赖 future language。

## 8. 架构含义

Stage105 把长 action history 分成两个不同对象：

1. **endpoint word quotient** `(I,t)`；
2. **endpoint response quotient** `Gamma`。

二者都不能被静默用于 trace-sensitive tasks。

这给所有试图 collapse operation words 的架构一个 exact pressure test：必须先声明 future-relevant observable 只看 endpoint，还是包含 full intermediate trace。

## 9. Prior-art / novelty 边界

commutative endpoint semantics、trace semantics、word quotients 与 interleaving counts 都是广泛 classical/CS concepts。P025 不单独主张这些概念新颖。

项目侧结果是把这些 distinctions 与 Stage101–104 arithmetic history-precision compiler 精确接起来。历史新颖性仍为 `NOVELTY_UNVERIFIED`。

## 10. 可执行资产

新增：

- `src/enterprise_math/abc_history_response_normal.py`；
- `tests/test_abc_history_response_normal.py`。

## 11. 下一前沿

Stage106 将研究 trace language 自身是否也有 compact response state。endpoint generator 已能预测任意 normal-form state `(I,t)` 的 area；剩余问题是：对 arbitrary ordered prefix traces，是否需要额外 state，还是只需要提高 operation-word precision。