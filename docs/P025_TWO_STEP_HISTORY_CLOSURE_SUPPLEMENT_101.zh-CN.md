# P025 补充 101 —— Two-Step Action-History Closure Boundary

状态：`ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation：`program/p025-history-closure-stage101`  
依赖：P025 补充 96–100  
硬阻断：`NONE`

## 1. 问题

Stage 100 已经给出 primitive action 的 natural one-step response signature：一种 action 插入 threshold row `+T`，另一种 action 追加 monotone orbit node `+J`。

Stage 101 问一个严格更强的问题：

> 如果同一个 signature 能预测所有 one-step next area，那么第一次 action 改变 state 以后，它还能继续预测第二步吗？

答案是 **不能**。

## 2. 通用有限模型

设

\[
\rho_0\le\cdots\le\rho_h
\]

为有限 nondecreasing scalar orbit，existing thresholds 为

\[
T_1<\cdots<T_s.
\]

定义

\[
B_{k,j}=\mathbf1_{\{\rho_j\ge T_k\}},
\qquad
A=\sum_{k,j}B_{k,j}.
\]

对 prospective threshold `U` 和 next node value `v>=rho_h`，记

\[
L_U:=\#\{j:\rho_j\ge U\},
\]

\[
R_v:=\#\{k:v\ge T_k\},
\]

并定义 mixed corner bit

\[
\boxed{C_{U,v}:=\mathbf1_{\{v\ge U\}}.}
\]

## 3. P025-T229 —— 精确 mixed two-step law

插入 `U` 并追加 `v`，无论顺序如何，最终都有

\[
\boxed{A''=A+L_U+R_v+C_{U,v}.}
\]

前两个增量就是 Stage 100 的 one-step responses；最后一项是真正的 mixed second-order response。

等价地，

\[
\boxed{
\Delta_v\Delta_U A
=
\Delta_U\Delta_v A
=
C_{U,v}.
}
\]

因此 extension diamond 仍然 commute，但 one-step marginal data 不一定能决定共同的 two-step value。

## 4. P025-CE38 —— 精确 mixed-history collision

取一个 existing threshold

\[
T_1=\frac1{25},
\]

当前只保留 exponent `2` 的一个旧 dyadic node，并取 prospective threshold

\[
U=\frac{11}{20}.
\]

比较两条 exact P025 dyadic difference orbits：

\[
(q,p)=(3,5),
\qquad
(q,p)=(3,41).
\]

在 exponents `2,4` 上 pressures 分别为

\[
(3,5):\quad\left(\frac12,\frac12\right),
\]

\[
(3,41):\quad\left(\frac1{22},\frac{13}{22}\right).
\]

在当前 one-node state 上，两者都有

\[
A=1,
\qquad
j_U=\infty,
\qquad
R_{\rho_1}=1.
\]

因此相对于 action family `{+U,+J}`，Stage-100 one-step signatures 完全相同：

\[
\boxed{(A,j_U,R_{\rho_1})=(1,\infty,1).}
\]

但是 `(3,5)` 有

\[
C_{U,\rho_1}=0,
\]

而 `(3,41)` 有

\[
C_{U,\rho_1}=1.
\]

所以 two-step final areas 分别为

\[
\boxed{2\neq3.}
\]

one-step sufficiency 因而不推出 mixed two-action history closure。

## 5. 条件 mixed closure

如果 `j_U` 在旧 horizon 上有限，那么已有某个 old node 满足 `rho_j>=U`。由 monotonicity，任何 appended node 都满足 `v>=U`，因此

\[
\boxed{C_{U,v}=1.}
\]

所以只有 candidate threshold 在旧 horizon 中仍 unresolved（`j_U=infinity`）时，才需要新 mixed bit。

这是 adaptive precision rule，而不是无条件增加坐标。

## 6. P025-T230 —— threshold-threshold history 已经闭合

对两个不同的新阈值 `U,V`，

\[
\boxed{A_{+U,+V}=A+L_U+L_V.}
\]

不存在 threshold-threshold interaction term，因为两个 action 只是加入互不相同的 rows，并不改变 orbit values。

因此 Stage-100 threshold-response staircase 对固定 candidate family 中任意有限 threshold-insertion sequence 已经闭合。

## 7. P025-CE39 —— repeated-node one-step failure

取当前 threshold set

\[
\{1\},
\]

仍从 exponent `2` 开始比较 `(3,5)` 与 `(3,41)`。

前三个 dyadic pressures 分别为

\[
(3,5):\quad\left(\frac12,\frac12,\frac12\right),
\]

\[
(3,41):\quad\left(\frac1{22},\frac{13}{22},\frac{221}{22}\right).
\]

在初始 node，两者 current area 都为 0；第一个 future-node rank 也都为 0：

\[
\boxed{(A,R_1)=(0,0).}
\]

所以 one-step `+J` signature 相同。

但第二个 future node 上，`(3,5)` 有

\[
R_2=0,
\]

而 `(3,41)` 有

\[
R_2=1.
\]

因此连续追加两个 nodes 后 final areas 分别是

\[
\boxed{0\neq1.}
\]

一个 one-step next-node rank 并不对 repeated node actions 闭合。

## 8. Stage101 边界定理

精确结论是

\[
\boxed{
\text{one-step sufficient response signature}
\not\Rightarrow
\text{finite-history sufficient response signature}.
}
\]

而失败并非任意发生：

- `+T;+T` 不需要新 interaction；
- mixed `+T;+J` 在 unresolved 时需要 corner bit `C_{U,v}`；
- `+J;+J` 需要第二个 future-node rank。

因此 Stage101 不只是负例，也准确定位了下一层 precision。

## 9. 架构含义

一个 declared future language 必须区分：只含 primitive one-step actions，还是允许 finite action histories。两者诱导的 quotient 不同。

Stage101 因而进一步区分：

1. one-step response sufficiency；
2. pairwise interaction sufficiency；
3. history closure。

这正是 Stage91–100 Foundation Feedback Packet 预告的 P025 压力测试。

## 10. Prior-art / novelty 边界

state augmentation、finite differences、pairwise interaction terms 与 finite-history closure 都是广泛 prior ideas。P025 不单独主张这些概念新颖。

项目侧贡献是 exact arithmetic realization、exact collision witnesses，以及利用这些 witnesses 严格区分 one-step future precision 与 history-closed precision。历史新颖性仍为 `NOVELTY_UNVERIFIED`。

## 11. 可执行资产

新增：

- `src/enterprise_math/abc_two_step_history.py`；
- `tests/test_abc_two_step_history.py`。

## 12. 下一前沿

自然问题是：新增信息会不会随 history 长度无界增长，还是在有限 interaction order 上闭合？有限 threshold/node incidence 结构强烈提示存在 exact second-order closure：

\[
A(I,J)
=
A
+\sum_{i\in I}L_i
+\sum_{j\in J}R_j
+\sum_{i\in I,j\in J}C_{ij}.
\]

Stage102 将证明或证伪这个任意 finite action family 公式，并判断所有三阶及以上 action interactions 是否全部消失。