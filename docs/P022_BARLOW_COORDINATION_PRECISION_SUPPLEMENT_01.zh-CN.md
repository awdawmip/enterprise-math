# P022 Barlow 配位精度补充 01 —— 周期准多项式与单位根递推

状态：`ACTIVE RESEARCH NOTE / EXACT INTEGER QUASI-POLYNOMIAL / NOVELTY UNVERIFIED`  
归属：`program/p022-geometry-v2`  
依赖：BC04 whole-shell drift-energy formula  
目的：刻画周期 stacking 的完整 future coordination sequence，并与 geodesic witness multiplicity 的代数类型作严格区分

## 1. 起点

对任意 Barlow stacking 与任意正 radius `n`，BC04 已证明

\[
\boxed{
4S_n=42n^2+8-\delta_n^2-\delta_{-n}^2.}
\]

现在假设 interface word 的周期长度为 `L`，signed period drift 为

\[
D=\sum_{j=0}^{L-1}\sigma_j.
\]

此时 shell sequence 比 geodesic-path sequence 简单得多。

## 2. P022-BCR01 —— 每一个 residue subsequence 都是精确二次多项式

写

\[
n=mL+r,
\qquad0\le r<L.
\]

定义有限 phase imbalances

\[
a_r=\delta_r,
\qquad
b_r=\delta_{-r}.
\]

周期性给出

\[
\delta_n=mD+a_r,
\]

以及

\[
\delta_{-n}=-mD+b_r.
\]

代入 BC04：

\[
\boxed{
4S_{mL+r}
=C_{0,r}+C_{1,r}m+C_2m^2,
}
\]

其中

\[
\boxed{
C_2=42L^2-2D^2,}
\]

\[
\boxed{
C_{1,r}=84Lr-2D(a_r-b_r),}
\]

以及

\[
\boxed{
C_{0,r}=42r^2+8-a_r^2-b_r^2.}
\]

对 residue `r=0`，这个 polynomial 用于 `m>=1`；仓库约定 `S_0=1` 是一个单独 initial value，而不是该 polynomial 在零点的延拓。

因此

\[
\boxed{
S_n\text{ 在 }n>0\text{ 上是 period dividing }L\text{ 的精确 quadratic quasi-polynomial。}
}
\]

这比仅知道 leading `n^2` coefficient 强得多。

## 3. finite phase signature

固定 declared period length `L`，定义 coordination phase signature

\[
\boxed{
\mathcal C
=\bigl((C_{0,r},C_{1,r},C_2)\bigr)_{r=0}^{L-1}.}
\]

连同 `S_0=1`，这个 finite integer tuple 能精确重建全部 future shell cardinalities。

所以一个 infinite periodic stacking word 又得到一层合法 task-relative collapse：

\[
\boxed{
\text{periodic literal word}
\longrightarrow
\mathcal C
\longrightarrow
(S_n)_{n\ge0}.}
\]

phase signature 可以严格小于 literal repeated history。这里不主张它在所有 period representation 中绝对最小：一个 word 可能有更小 primitive period，不同 signatures 也可能共享更小 recurrence。

## 4. P022-BCR02 —— universal shell recurrence

固定 residue class `r`。`m` 的二次多项式三阶 forward difference 恒为零：

\[
\Delta_m^3S_{mL+r}=0.
\]

在原 radius variable 中，`m` 前进一步就是 radius 增加 `L`，因此一旦 recurrence 涉及的四个 shell radii 都为正，就有

\[
\boxed{
(E^L-1)^3S=0.
}
\]

显式写成

\[
\boxed{
S_n-3S_{n-L}+3S_{n-2L}-S_{n-3L}=0,
\qquad n>3L.}
\]

这对**所有** period-`L` Barlow coordination sequences 都成立，与 drift / phase 无关。

其 characteristic polynomial 为

\[
\boxed{(x^L-1)^3.}
\]

所有 characteristic roots 都是单位根，multiplicity 至多 3；quadratic quasi-polynomial growth 正对应这些重复 unit-modulus roots。

## 5. P022-BCR03 —— universal ball recurrence

定义

\[
B_n=\sum_{r=0}^{n}S_r.
\]

则按普通 index convention，

\[
(E-1)B=S.
\]

再应用 BCR02：

\[
\boxed{
(E-1)(E^L-1)^3B=0
}
\]

在充分大 index 上成立。

一个统一 characteristic 是

\[
\boxed{
(x-1)(x^L-1)^3,}
\]

degree 为

\[
\boxed{3L+1.}
\]

所以整个 periodic crystal-ball sequence 同样是 C-finite，但只有 unit-modulus characteristic roots。

## 6. rational generating functions

shell ordinary generating function

\[
G_S(z)=\sum_{n\ge0}S_nz^n
\]

的 denominator 整除

\[
\boxed{(1-z^L)^3.}
\]

ball generating function 的 denominator 整除

\[
\boxed{(1-z)(1-z^L)^3.}
\]

包括特殊 radius-zero shell value 在内的有限 initial corrections 只会改变 numerator。

因此 periodic coordination sequence 之所以 rational，比 periodic path-multiplicity sequence 的原因简单得多：前者是 quasi-polynomial，不是 exponential growth system。

## 7. cardinality 与 multiplicity 属于不同 recurrence algebra

对于同一个 periodic Barlow contact graph，我们现在有两套 exact future-sequence structure。

### vertex cardinality

universal shell characteristic：

\[
(x^L-1)^3.
\]

所有 roots 都在 unit circle 上；polynomial growth 来自 repeated unit-modulus roots。

### geodesic path multiplicity

前面的 BG04 theorem 需要 expanding factors，例如

\[
(x-2)^L-A_+,
\]

其 dominant real root 是

\[
2+2^{(1+|D|/L)/2}>3.
\]

因此 witness multiplicity 并不是“同一 sequence type 上更大的 coefficient”。它属于另一类 finite recurrence algebra，带有真正 expanding modes。

这把此前的 precision inequality 提升成结构结论：

\[
\boxed{
\text{support/cardinality shadow}
\text{ 会精确删除 expanding witness modes。}}
\]

信息损失直接出现在 characteristic spectrum 中。

## 8. leading coefficient 相同，finite phase 仍可不同

quadratic coefficient

\[
C_2=42L^2-2D^2
\]

只依赖 `(L,|D|)`。

但 lower-order residue coefficients 仍通过

\[
a_r,\ b_r
\]

保存 finite phase information。

所以两个 period length 与 absolute drift 相同的 stacking words，会共享相同 asymptotic shell coefficient，但 finite coordination sequences 仍可能不同。

例如两个 zero-drift period-four words 都有

\[
C_2=42\cdot4^2,
\]

却可以在 `C_{0,r}` / `C_{1,r}` 上不同，因此某些 finite radii 的 shell count 不同。

这与 path-growth route 完全平行：asymptotic language 所需状态比 exact finite future language 更少。

## 9. 与已知 coordination-sequence 研究的关系

periodic crystal/contact graphs 的 coordination sequence 与 rational generating function 本身已有成熟研究传统。因此本文在 prior-art audit 完成前应视作 concrete Barlow specialization，而不是直接主张新母理论。

本项目里的核心价值是：它从 stacking precision variable `delta` 直接推导出 exact relation，并与 path-multiplicity hierarchy 接在一起：

\[
\text{stacking prefix}
\to
\delta
\to
\delta^2
\to
\text{quadratic quasi-polynomial coordination}
\]

对比

\[
\text{stacking prefix}
\to
|\delta|\text{ trajectory}
\to
\text{expanding geodesic-count recurrence}.
\]

它们是同一 hidden geometry 的两个不同 future-language quotients。

## 10. executable assets

新增：

- `src/enterprise_math/p022_barlow_coordination_recurrence.py`；
- `tests/test_p022_barlow_coordination_recurrence.py`。

测试不是从已生成 sequence 拟合 recurrence，而是直接由 period formula 构造 residue quadratics，并在全部短 ± periods 上验证 shell recurrence、ball recurrence 与 finite phase signature。
