# A3 Guard-Image Lattice 补充 03 —— 固定 Hidden Rank、Recession Quotient 与多项式 Branch Geometry

状态：`RESEARCH WIP / GENERAL FIXED-RANK REDUCTION THEOREM + PRIOR-ART COMPLEXITY COROLLARY`

## 1. 从 rank 2 抽象什么

Supplement 02 对 `rank L_G=2` 给出三种 exact certificate：

1. strict recession；
2. recession ray/line；
3. bounded polygon。

这三种情形并不是二维偶然，而是一个一般 quotient 结构的低维表现。

设 hidden guard-image lattice

\[
L_G=W(K_A)\subseteq\mathbb Z^r
\]

的 rank 为：

\[
\boxed{d.}
\]

用成熟的 Hermite/Smith 型整数格 reduction 取 exact basis 后，一个 coarse fiber 的 guard scores 可写成：

\[
\boxed{g+Hz,\qquad z\in\mathbb Z^d,}
\]

其中 `H` 的列（或等价行约定）给出 `L_G` 的整数 basis。

固定一个 threshold pattern `sigma` 后，得到有限整数线性系统：

\[
\boxed{A_\sigma z\ge b_\sigma.}
\]

所以 A3 高秩 branch reachability 本质上是：

> **hidden rank `d` 个整数变量上的线性可行性。**

## 2. homogeneous recession cone

定义 real recession cone：

\[
C_\sigma
=
\{u\in\mathbb R^d:A_\sigma u\ge0\}.
\]

令：

\[
U_\sigma=\operatorname{span}_{\mathbb R}C_\sigma,
\qquad
S_\sigma=U_\sigma\cap\mathbb Z^d.
\]

`S_sigma` 是 `Z^d` 中的 saturated sublattice。

把 constraint row `a_i` 分成两类：

### static rows

\[
a_i|_{U_\sigma}=0.
\]

这类 inequality 沿所有 recession-span directions 都完全不变，因此只依赖 quotient class：

\[
[z]\in\mathbb Z^d/S_\sigma.
\]

### dynamic rows

\[
a_i|_{U_\sigma}\neq0.
\]

这类约束可以沿 recession cone 的 relative-interior direction 最终被严格满足。

## 3. A3-G11 —— Recession-Quotient Feasibility Theorem

对整数系统：

\[
A z\ge b,
\qquad z\in\mathbb Z^d,
\]

令 `C,U,S` 如上。

则：

\[
\boxed{
Az\ge b\text{ 有整数解}
\iff
\exists [z]\in\mathbb Z^d/S
\text{ 满足全部 static inequalities}.
}
\]

### 正向

若 `z` 本身可行，其 quotient class 显然满足 static inequalities。

### 反向

假设某个 quotient class 有整数代表 `z_0` 满足全部 static rows。

`C` 是由整数法向量定义的 rational polyhedral cone。它在自己的 span `U` 中有非空 relative interior，因此可取：

\[
u\in\operatorname{relint}(C)\cap\mathbb Z^d.
\]

对 static row：

\[
a_i u=0.
\]

对 dynamic row，由于它不在整个 `U` 上恒为零，而 `u` 位于 `C` 的 relative interior：

\[
\boxed{a_i u>0.}
\]

所以取足够大的整数 `N`：

\[
z=z_0+Nu
\]

会保持全部 static inequalities 不变，并使全部 dynamic inequalities成立。

故得到整数可行解。∎

## 4. A3-G12 —— quotient 中的 static feasible region 必定 bounded

考虑 static inequalities 在 quotient real space：

\[
\mathbb R^d/U.
\]

其 feasible set 不可能有非零 recession direction。

否则存在 `v notin U`，其 quotient direction 非零，而且所有 static rows满足：

\[
a_i v\ge0.
\]

仍取上节 relative-interior integer/rational recession direction `u in C`。对所有 dynamic rows，`a_i u>0`，所以对足够大的 `T`：

\[
a_i(v+Tu)\ge0
\]

也成立；static rows 同样成立。

于是：

\[
v+Tu\in C\subseteq U.
\]

而 `u in U`，所以：

\[
v=(v+Tu)-Tu\in U,
\]

矛盾。

因此：

\[
\boxed{
\text{剥掉完整 recession span 后，剩余 quotient feasibility 是 bounded 的。}
}
\]

这说明 unboundedness 不是整数可达性的无限复杂来源；它可以被结构性消去。

## 5. A3-G13 —— Pattern Arithmetic Defect Rank

定义：

\[
\boxed{
\delta_\sigma
:=d-\dim U_\sigma.
}
\]

它表示去掉所有 recession directions 后，仍需真正处理 integer holes 的 quotient rank。

这不是新的物理维度，只是 future-language branch pattern 的 arithmetic difficulty index。

低维情形：

- `delta_sigma=0`：recession span 满 rank；static quotient 为 0 维，pattern 自动可达；
- `delta_sigma=1`：只剩一维 bounded/static integer interval/congruence 问题；
- `delta_sigma=2`：真正二维 bounded integer-hole 问题；
- 一般 `delta_sigma`：困难部分只存在于 rank `delta_sigma` 的 bounded quotient。

Supplement 02 的三种 rank-two certificate 因而精确重写为：

\[
\boxed{
delta_\sigma=0,1,2.}
\]

## 6. base-independent pattern 的一般刻画

若：

\[
U_\sigma=\mathbb R^d,
\]

则 quotient rank为 0，没有 nontrivial static inequality obligation。

所以：

\[
\boxed{
\delta_\sigma=0
\Longrightarrow
\text{该 pattern 对任意 affine base score 都可达。}
}
\]

这推广 Supplement 02 的 strict-cone 结论。

反之，若 `delta_sigma>0`，pattern 可达性可能依赖 base score 在 bounded quotient 中留下的 residue / lattice-hole information。

## 7. A3-G14 —— 固定 hidden rank 的 branch-pattern 数为多项式上界

在 exact hidden-lattice basis 中，每个实际变化的 guard 对 parameter `z in R^d` 给一张 affine hyperplane。

设 nonconstant guard 数为：

\[
q.
\]

`q` 个 affine hyperplanes 在 `R^d` 中的总 face 数，在 general/simple arrangement 取得最大值：

\[
\boxed{
F_d(q)
=
\sum_{j=0}^{\min(d,q)}2^j\binom qj.
}
\]

该式满足 deletion/restriction recurrence：

\[
F_d(q)=F_d(q-1)+2F_{d-1}(q-1),
\]

边界：

\[
F_0(q)=1.
\]

binary threshold pattern 在每个 relative-open face 上恒定；integer lattice sampling只会使某些 faces 没有整数点，不能产生新 pattern。

因此：

\[
\boxed{
N_{patterns}
\le
\min\left(2^q,F_d(q)\right).
}
\]

固定 `d` 时：

\[
\boxed{F_d(q)=O(q^d).}
\]

所以 branch geometry 的真正组合维数由 hidden rank 控制，而不是 guard 语法数量本身。

已有特例：

\[
F_1(q)=2q+1,
\]

\[
F_2(q)=2q^2+1.
\]

这使用成熟 hyperplane-arrangement face counting；不是 A3 原创。

## 8. A3-G15 —— 固定 hidden rank 的 exact reachability 属于 fixed-dimension ILP

取 `L_G` 的 exact integer basis 后，每个 branch pattern 是：

\[
A_\sigma z\ge b_\sigma,
\qquad
z\in\mathbb Z^d.
\]

因此 hidden rank `d` 固定时，branch reachability 是固定变量数的 integer linear programming feasibility。

Lenstra 的经典结果已证明：**固定整数变量个数时，ILP 对输入长度是 polynomial-time 可解的。**

所以在算法存在性层：

\[
\boxed{
\text{fixed hidden rank}
\Longrightarrow
\text{exact branch reachability admits a polynomial-time solver in input length},
}
\]

其中指数/高代价依赖可以集中在固定参数 `d` 上。

A3 不复制 Lenstra/后续 fixed-dimension ILP 理论。我们的工作只负责把 future precision problem 规范地 reduce 到 `d=rank W(K_A)` 个整数变量，并在 rank 1/2 给出特别轻量的自有 closed solver。

## 9. 实现

新增：

- `src/enterprise_math/guard_pattern_complexity.py`；
- `tests/test_guard_pattern_complexity.py`。

接口：

- `arrangement_total_face_bound(q,d)`；
- `arrangement_total_face_recurrence(q,d)`；
- `nonconstant_guard_count(...)`；
- `hidden_guard_pattern_bound(...)`。

测试验证：

- `F_1(q)=2q+1`；
- `F_2(q)=2q^2+1`；
- deletion/restriction recurrence；
- `d` 次有限差分为常数 `2^d`，确认固定 `d` 下为 degree-`d` integer-valued polynomial；
- constant guards 不增加 fiber branch multiplicity；
- full hidden rank 时 `2^q` 是更紧的 trivial truth-pattern bound。

## 10. 与 A2/P023 的边界

一般“future programs 对 quotient 的 behavioral equivalence / minimal state”继续由 A2/P023 持有。

A3 当前提供的是特殊但可计算的 integer structure：

\[
K_A
\xrightarrow{W}
L_G
\xrightarrow{\text{basis}}
\mathbb Z^d
\xrightarrow{\text{thresholds}}
\text{integer polyhedral feasibility}.
\]

因此：

- `hidden rank d` 是 A3 future-precision 的自然参数；
- `delta_sigma` 是 pattern-specific residual arithmetic rank；
- general fixed-d solver 应调用成熟 HNF/ILP 工具，不在 A3 另造一个通用优化理论；
- rank-one/rank-two closed solvers 保留为 A3-specific lightweight specializations。

## 11. 下一步

1. 为 `delta_sigma` 做 executable certificate extraction：从 guard halfplanes 求 recession-span rank 与 static rows；
2. rank 3 先只实现 quotient reduction，不重写通用 ILP；
3. 把 actual reachable branch set 与 branch coarse-effect equality 合成 **state-dependent branch-erasure checker**；
4. 将 branch-erasure 所需的最小 partition 与 relation rank/quantum precision cost 直接联结；
5. 用 P021 或 A3→A4 staged-support 的真实 predicate family 做一次跨路线 pressure test。
