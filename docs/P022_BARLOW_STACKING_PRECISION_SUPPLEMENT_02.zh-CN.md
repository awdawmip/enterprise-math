# P022 Barlow 堆垛精度补充 02 —— 周期测地增长的统一整数递推

状态：`ACTIVE RESEARCH NOTE / EXACT EVENTUAL RECURRENCE / NOVELTY UNVERIFIED`  
归属：`program/p022-geometry-v2`  
依赖：Barlow BG01–BG03  
先验边界：virtually abelian 等背景下的一般 geodesic growth 已有成熟理论；本文证明的是当前周期 close-packed contact graph 的具体整数递推，在专项审计前不主张历史优先性

## 1. asymptotic growth constant 还不是全部信息

上一份 supplement 已证明：周期为 `L`、drift 为 `D` 的 Barlow stacking，其 shell-total geodesic multiplicity 满足

\[
T_n=\Theta(\lambda^n),
\qquad
\lambda=2+2^{(1+|D|/L)/2}.
\]

这个结果把无限 tail 压成一个 algebraic growth constant，但会擦掉所有 finite oscillations 与 subdominant exponential modes。

exact shell formula 还包含更强结构。周期性把每个 prefix-imbalance term 限制在有限 residue classes，而每个 residue class 都生成 constant-coefficient recurrence。

因此得到更强结论：

> **整个 periodic shell-total sequence 最终是 C-finite，而且存在一个只由 `(L,|D|)` 决定的统一整数 recurrence space。**

period 内 literal order 只改变 amplitudes，并可能使某些 factors 消失，但不会产生这个 universal space 之外的新 eigenmodes。

## 2. 用 signed imbalance 重写 BG01

对非极端层 `q=|k|<n`，BG01 为

\[
L_n(k)=\binom nq
\left[
3\cdot2^n
\left(
2^{-(q+d_k)/2}+2^{-(q-d_k)/2}
\right)-6
\right],
\]

其中 `d_k=|delta_k|`。

两个指数项在 `delta_k -> -delta_k` 下交换，因此可以精确去掉 absolute value，写成

\[
\boxed{
L_n(k)=\binom nq
\left[
3\cdot2^n
\left(
2^{-(q+\delta_k)/2}+2^{-(q-\delta_k)/2}
\right)-6
\right].
}
\]

`q` 与 `delta_k` 奇偶相同，所以所有指数仍是整数。

这个 signed form 很关键：periodic imbalance 在每个 residue class 上从一开始就是 affine 的，不再需要 eventually-positive/negative 的 case split。

## 3. 周期 residue decomposition

对 upward layers，写

\[
q=mL+r,
\qquad0\le r<L.
\]

周期性给出

\[
\delta_q=mD+\delta_r.
\]

于是

\[
2^{-(q-\delta_q)/2}
=
2^{-(r-\delta_r)/2}
\left(2^{-(L-D)/2}\right)^m,
\]

以及

\[
2^{-(q+\delta_q)/2}
=
2^{-(r+\delta_r)/2}
\left(2^{-(L+D)/2}\right)^m.
\]

向下层虽然 finite phase constant 不同，但仍只有同样两种 period multipliers，只是 `D` / `-D` 的角色互换。因此 possible characteristic modes 只依赖 absolute drift。

定义两个整数幂

\[
\boxed{
A_+=2^{(L+|D|)/2},
\qquad
A_-=2^{(L-|D|)/2}.}
\]

由于 `L` 个 ±1 的和 `D` 与 `L` 同奇偶，两个 exponent 都是整数。

## 4. binomial residue sums

所有 weighted layer sums 都化为

\[
S_{r,u}(n)
=
\sum_{m\ge0}\binom n{mL+r}u^m.
\]

引入代数元 `z`，满足

\[
z^L=u,
\]

并取 `L` 次单位根 `omega`。标准 root-of-unity filter 给出

\[
\boxed{
z^r S_{r,u}(n)
=
\frac1L
\sum_{j=0}^{L-1}
\omega^{-rj}(1+z\omega^j)^n.}
\]

所以 `S_{r,u}` 是有限个 exponential sequences 的线性组合，其 bases 全部是

\[
(x-1)^L-u
\]

的 roots。

BG01 中 residue sum 还整体乘了 `2^n`，因此 eigenvalue 乘 2，对应 characteristic polynomial 变成

\[
\boxed{
(x-2)^L-2^Lu.}
\]

代入两种 Barlow period multipliers 后，`2^Lu` 正好是 `A_+` 或 `A_-`。

因此所有 non-extreme weighted binomial terms 都被

\[
((x-2)^L-A_+)((x-2)^L-A_-)
\]

消去。

## 5. 为什么还会出现 unshifted `x^L-A_±`

root-of-unity filter 的完整 residue sum 会在 `n` 属于该 residue class 时自然包含 `q=n` 项。

但 BG01 只适用于 `q<n`；真实 extreme layers 的 contribution 是

\[
3^n,
\]

不是继续沿用 non-extreme face formula。

从完整 residue sums 中扣除“本来会出现的 q=n term”，会产生与

\[
2^{(n+\delta_n)/2}
\quad\text{和}\quad
2^{(n-\delta_n)/2}
\]

成比例的 sequences。

跨一个完整 period，这些量分别乘上

\[
A_+
\quad\text{或}\quad
A_-.
\]

因此这部分 boundary correction 被

\[
\boxed{
(x^L-A_+)(x^L-A_-)
}
\]

消去。

真实 extreme-layer replacement 本身则贡献纯 `3^n` mode。

## 6. 剩余 scalar modes

每个 non-extreme layer 的 `-6` 部分与 stacking phase 无关。对中央层以及所有正负高度求和后，只产生 constant mode 与 `2^n` mode，对应

\[
(x-1)(x-2).
\]

两个真实 extreme layers 总共贡献

\[
2\cdot3^n,
\]

因此再加入

\[
(x-3).
\]

不需要其他 exponential mode。

## 7. P022-BG04 —— universal eventual characteristic polynomial

定义

\[
\boxed{
\begin{aligned}
Q_{L,D}(x)=\;&(x-1)(x-2)(x-3)\\
&\cdot(x^L-A_+)(x^L-A_-)\\
&\cdot((x-2)^L-A_+)((x-2)^L-A_-),
\end{aligned}}
\]

其中

\[
A_\pm=2^{(L\pm|D|)/2}.
\]

则任何 period length `L`、absolute drift `|D|` 相同的周期 Barlow stacking，其 shell-total geodesic sequence `T_n` 都在 sufficiently large `n` 上满足由 `Q_{L,D}` 编码的 constant-coefficient recurrence。

`Q` 是 monic integer polynomial，次数为

\[
\boxed{4L+3.}
\]

使用当前仓库 `T_0=1` 的 radius-zero convention，可执行公式从 degree 之后的第一个 index 起精确满足：

\[
\boxed{
Q_{L,D}(E)T_n=0
\qquad(n>4L+3),}
\]

其中 `E` 是 forward-shift operator。

这是 uniform upper bound，不主张 recurrence minimality。

## 8. P022-BG05 —— same drift class 共享一个 recurrence space

若两个 periodic stacking words 拥有同一

\[
(L,|D|)
\]

但 period 内 interface order 不同，则 finite prefix phases `delta_r` 可以不同，所以 finite shell totals 也可以不同。

然而 phase 只改变 residue-class exponential modes 的 coefficients；possible bases 本身仅由 `L` 与 `|D|` 决定。

因此

\[
\boxed{
\text{same }(L,|D|)
\Longrightarrow
\text{same universal recurrence space}.}
\]

这比前面的 asymptotic theorem 更强：相同 drift density 只固定 dominant exponential rate；相同整数对 `(L,|D|)` 则固定了一个有限的全部 allowable exponential-mode universe。

不同 period 即使 reduced drift density 相同，也可能具有不同 subdominant mode sets。

## 9. rational generating function

令

\[
G(z)=\sum_{n\ge0}T_nz^n.
\]

eventually constant-coefficient recurrence 等价于 ordinary generating function rational。

一个统一整数 denominator 是 reciprocal characteristic polynomial：

\[
\boxed{
\begin{aligned}
R_{L,D}(z)=\;&(1-z)(1-2z)(1-3z)\\
&\cdot(1-A_+z^L)(1-A_-z^L)\\
&\cdot((1-2z)^L-A_+z^L)\\
&\cdot((1-2z)^L-A_-z^L).
\end{aligned}}
\]

具体某一 stacking 可以发生 factor cancellation，因此 actual denominator 可能更小。

所以每个 periodic Barlow stacking 在当前 contact-graph geodesic-count language 下都有

\[
\boxed{G(z)\in\mathbb Q(z).}
\]

这是本具体 close-packed family 的性质，不能误说成所有 exponential geodesic-growth systems 都 rational。

## 10. dominant root 自动回到 drift growth law

`Q` 的最大正实 root 来自

\[
(x-2)^L-A_+.
\]

所以

\[
(x-2)^L=A_+
=2^{(L+|D|)/2},
\]

从而

\[
\boxed{
x=2+2^{(1+|D|/L)/2}.}
\]

因此 BG03 的 drift-controlled growth constant 并不是独立的 asymptotic 偶然现象，而是 exact recurrence space 的 dominant root。

recurrence theorem 因而对 growth theorem 给出了更强的结构解释。

## 11. 例子与 factor cancellation

### FCC

`L=1`、`|D|=1`，因此

\[
A_+=2,
\qquad A_-=1.
\]

universal polynomial 中 `1,2,3` 等 roots 会重复出现，而 actual FCC closed form 只包含

\[
1,2,3,4.
\]

factor cancellation/minimalization 后只剩熟悉的 order-four recurrence。

### HCP

`L=2`、`D=0`，有

\[
A_+=A_-=2.
\]

两个 unshifted factors 相同，两个 shifted factors 也相同，因此 universal polynomial 明显非最小。

实际 HCP sequence 被更小的 characteristic

\[
(x-1)(x-2)(x-3)(x^2-2)(x^2-4x+2)
\]

消去，恰好对应上一份 HCP supplement 的 order-seven recurrence。

### period `(-,-,+)`

这里

\[
L=3,
\quad |D|=1,
\quad A_+=4,
\quad A_-=2.
\]

universal mode factors 为

\[
x^3-4,
\quad x^3-2,
\]

以及

\[
(x-2)^3-4,
\quad (x-2)^3-2,
\]

外加 `1,2,3`。

dominant root 就是

\[
2+2^{2/3}.
\]

## 12. finite-state 含义

对 periodic Barlow stacking 的 shell-total future language，无限未来 shell values 不需要逐一独立保存。

BG04 给出 uniform recurrence-state bound：

\[
\boxed{
\text{有限 warm-up 后，至多 }4L+3
\text{ 个此前整数值足以递归生成全部未来。}}
\]

这个 bound 在 factor cancellation 后通常可以显著下降，但它已经完全显式，并且只依赖 period length。

于是 legal compression chain 又向前延伸一层：

\[
\text{literal stacking word}
\to
\text{queried prefix imbalances}
\to
\text{finite shell trajectory}
\to
(L,|D|)+\text{finite recurrence amplitudes/state}
\to
\text{dominant drift growth constant}.
\]

每一步都对应更弱的 declared future language。

## 13. prior-art discipline

finitely generated / virtually abelian 背景下的一般 geodesic growth 已有成熟研究，包括 holonomicity 以及 polynomial/exponential geodesic growth 的结论。

本 P022 结果更窄也更具体：利用 close-packing interface polynomial，为 periodic Barlow contact graph 给出 explicit rational generating function / integer recurrence family。

在专项 source search 证明历史独立性以前，继续标记

`NOVELTY_UNVERIFIED`。

## 14. executable reference

`p022_barlow_growth.py` 新增：

- `period_exponential_weights`；
- `universal_growth_characteristic_polynomial`；
- `universal_growth_generating_denominator`；
- `recurrence_residual`。

测试先仅由 `(L,|D|)` 构造 recurrence，**随后**才生成 shell sequence，并对 period length 不超过 4 的全部 ± patterns 做验证；还会验证 finite sequences 不同但 `(L,|D|)` 相同的 patterns 确实共享同一个 universal characteristic。
