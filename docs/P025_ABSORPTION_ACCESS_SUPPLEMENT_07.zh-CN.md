# P025 补充 07 —— Absorption Access Radius 与 Rank-One No-Tradeoff 定理

状态：`ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner：`program/p025-abc-support-collapse`  
依赖：P025 补充 01、04–06  
Hard block：`NONE`

## 1. 三个彼此不同的 witness quantities

前面的阶段已经把 certificate quantity 分成三种：

1. 第一次出现**任意**非退化 witness 的半径，
   \[
   \mu
   =\min\{\|x\|_\infty:x\in T\setminus T^\circ\};
   \]
2. 所有 witness 能达到的最小 arithmetic absorption redundancy，
   \[
   \eta_{\min}
   =\min\{\eta(x):x\in T\setminus T^\circ\};
   \]
3. 第一次真正能够达到该 arithmetic optimum 的半径。

定义第三个量：

\[
\boxed{
\nu
=\min\{\|x\|_\infty:
 x\in T\setminus T^\circ,
 \eta(x)=\eta_{\min}\}.
}
\]

再定义**absorption access delay**

\[
\boxed{
\delta_{\rm abs}=\nu-\mu\ge0.
}
\]

如果第一层可用 certificate 已经 absorption-optimal，则该量为零；若必须在格上继续走更远才能碰到 arithmetic floor，则它为正。

## 2. P025-T21 —— access delay 为零当且仅当二成本 Pareto frontier 是单点

令

\[
\mathcal P
=\operatorname{Min}_{\preceq}
\{(\|x\|_\infty,\eta(x)):
 x\in T\setminus T^\circ\}
\]

为补充 04 的 absorption-aware Pareto frontier。

则

\[
\boxed{
\delta_{\rm abs}=0
\iff
\mathcal P=\{(\mu,\eta_{\min})\}.
}
\]

### 证明

若 `delta_abs=0`，则存在一个 witness 同时实现 radius `mu` 与 absorption `eta_min`。其它任意 witness 的 norm 都至少是 `mu`，absorption redundancy 都至少是 `eta_min`，因此该点支配所有其它 cost pairs，Pareto frontier 只能是这个单点。

反之，假设 frontier 是单点 `(r,e)`。存在 radius 为 `mu` 的 witness，它的 cost 必被某个 Pareto-minimal point 支配，所以 `r<=mu`；由 `mu` 的最小性可知 `r=mu`。同理，存在达到 `eta_min` 的 witness，所以 `e=eta_min`。因此这个单点就是 `(mu,eta_min)`，并且有 witness 同时实现两个最小值，即 `nu=mu`。∎

### 含义

对二阈值 future language 而言，标量 witness radius 何时已经够用，现在有了精确判据：geometric accessibility 与 arithmetic absorption optimality 必须在第一 witness layer 就对齐。

## 3. P025-T22 —— Rank-one witness lattices 不存在 norm/absorption tradeoff

假设

\[
\omega(abc)=2,
\]

即整个 triple 只有两个 distinct prime coordinates。则

\[
\boxed{
\delta_{\rm abs}=0
}
\]

而完整二成本 Pareto frontier 必为单点。

更精确地，把 primitive additive normal 写成

\[
\widehat\alpha=(u,v),
\qquad
\gcd(u,v)=1.
\]

则

\[
T=\ker_{\mathbb Z}\widehat\alpha
=\mathbb Z\,(v,-u).
\]

令

\[
t=(v,-u).
\]

于是

\[
\boxed{
\mu=\|t\|_\infty=\max(|u|,|v|).
}
\]

如果 `d` 是 Wronskian image 在 `T` 上的正生成元，那么

\[
|W(t)|=d,
\]

所以

\[
\boxed{
\eta(t)=\eta_{\min}=d/M.
}
\]

每个非零 witness 都是某个整数 `k!=0` 的 `k t`，因此

\[
\left(
\|k t\|_\infty,
\eta(k t)
\right)
=
|k|
\left(
\mu,
\eta_{\min}
\right).
\]

于是

\[
\boxed{
\mathcal P
=\{(\mu,\eta_{\min})\}.
}
\]

### 证明

primitive row `(u,v)` 的整数 kernel 由 `(v,-u)` 生成。补充 04 已把 Wronskian image 的正生成元识别为 additive row 与 Wronskian row 的 determinant 绝对值；把 Wronskian 作用到 `(v,-u)` 上正好得到该 determinant（差整体符号）。所有非零 lattice points 都是这个 primitive generator 的整数倍，并且两个 cost 都同时按 `|k|` 缩放。∎

## 4. P025-C01 —— Genuine Pareto tradeoff 至少需要三个 prime coordinates

由 P025-T22：

\[
\boxed{
|\mathcal P|>1
\Longrightarrow
\omega(abc)\ge3.
}
\]

反命题不成立。

例如

\[
1+5=6
\]

有三个 prime coordinates `(2,3,5)`，但精确 frontier 仍然是

\[
\boxed{
\mathcal P(1,5,6)=\{(1,1)\}.
}
\]

所以 witness rank 至少为 2 只是 tradeoff 的**必要可能性条件**，并不会强制 tradeoff 出现。

## 5. 显式 tradeoff delays

### `2+3=5`

补充 04 已得

\[
\mathcal P(2,3,5)
=\{(1,2),(2,1)\}.
\]

因此

\[
\mu=1,
\qquad
\eta_{\min}=1,
\qquad
\nu=2,
\qquad
\boxed{\delta_{\rm abs}=1}.
\]

### `2+7=9`

精确 frontier 为

\[
\mathcal P(2,7,9)
=\{(1,3),(4,2),(5,1)\}.
\]

于是

\[
\mu=1,
\qquad
\eta_{\min}=1,
\qquad
\nu=5,
\qquad
\boxed{\delta_{\rm abs}=4}.
\]

这个例子在 arithmetic floor 上没有任何 absorption obstruction（`eta_min=1`），但为了真正达到 perfect absorption，仍要多打开四个 lattice-radius levels。

因此

\[
\boxed{
\text{absorption obstruction 与 absorption access difficulty 是相互独立的两个轴。}
}
\]

一个状态可能因为 Wronskian image 本身具有 nontrivial index 而 `eta_min>1`；也可能 `eta_min=1`，但因为 image generator 在当前 norm 下很难几何实现而有较大的 `delta_abs`。

## 6. 四层 certificate decomposition

P025 witness architecture 现在可以明确区分：

1. **existence geometry** —— `mu`；
2. **arithmetic obstruction** —— `eta_min` / 其 local prime spectrum；
3. **optimal-access geometry** —— `nu` 或 `delta_abs`；
4. **intermediate tradeoffs** —— 完整 Pareto frontier `P`。

一般情况下，没有任何一个标量能决定另外三个。

这比泛泛地说“witness cost 是多维的”更精确：现在已经知道不同 costs 分别在哪一段出现。

## 7. 与 Geometry of Numbers 的关系

Pasten 的外部前人工作使用 Geometry of Numbers 控制 relation-adapted arithmetic derivatives 的 norm。这直接对应 witness problem 的 geometric side。P025 不主张 lattice norm minimization、Siegel lemma、Minkowski theory 或 closest-vector phenomena 是新数学。

项目侧现在的问题变得更精确：

> 当 arithmetic obstruction floor 已经由 exact support/valuation data 固定以后，为了真正**访问**这个 floor，还必须额外付出多少 norm？

这个量是 `nu`，而不仅仅是 `mu`。

在对这组 decomposition 作 historical novelty 判断以前，仍需要定向 prior-art audit。

## 8. 可执行资产

新增：

- `src/enterprise_math/abc_absorption_access.py`
  - absorption-optimal radius `nu`；
  - access delay `delta_abs`；
  - singleton-frontier equivalence audit；
  - exact rank-one witness-ray classification；
  - genuine tradeoff 的 three-prime-coordinate 必要条件。
- `tests/test_abc_absorption_access.py`
  - rank-one samples `1+8=9` 与 `1+3=4`；
  - `2+3=5` 与 `2+7=9` 的正 delay；
  - three-coordinate singleton counterexample `1+5=6`。

## 9. 下一前沿

不存在 hard block，继续：

1. 从 primitive additive row 与 scaled Wronskian functional 推导 `nu` 的上下界；
2. 找出 `nu` 存在 closed Bezout-type formula 的 family；
3. 在已经证明 naive `quality -> eta_min=1` 失败的前提下，再测试 `delta_abs` 与 abc quality 是否存在真正关系；
4. 比较 Pareto frontier 与 additive witness lattice 的 successive minima；
5. 把 classical lattice optimization 与项目特有 certificate-precision interpretation 严格分开；
6. 把 rank-one theorem 当作校准边界：任何 generic multi-cost theorem 在 `omega(abc)=2` 时都必须退化成单 ray。
