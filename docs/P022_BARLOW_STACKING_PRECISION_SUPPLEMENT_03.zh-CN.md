# P022 Barlow 堆垛精度补充 03 —— 非周期 drift 定理

状态：`ACTIVE RESEARCH NOTE / EXACT FINITE FORMULA + ASYMPTOTIC GENERALIZATION / NOVELTY UNVERIFIED`  
归属：`program/p022-geometry-v2`  
依赖：Barlow BG01 exact target-layer contribution  
范围：具有 one-sided absolute drift density 的任意 bi-infinite Barlow interface words

## 1. growth theorem 真正不需要 periodicity

周期 Barlow stacking 给过我们两个不同收益：

1. prefix imbalance = linear drift + bounded phase，这已经足够决定 shell-total geodesic multiplicity 的 exponential growth rate；
2. finite phase 本身精确重复，这一更强条件才进一步给出 rational generating function 与 constant recurrence。

所以 growth exponent 实际只需要第一条。

因此，只要 long-run absolute prefix drift 存在，drift-controlled growth law 可以直接推广到 aperiodic / disordered stacking，而无需先做 periodic approximation。

## 2. 任意 two-sided stacking word

对每一个 upward interface `j -> j+1`，定义

\[
\sigma_j\in\{-1,+1\},
\qquad j\in\mathbb Z.
\]

定义从根层出发的 effective imbalance：

\[
\delta_0=0,
\]

正方向

\[
\delta_k=\sum_{j=0}^{k-1}\sigma_j
\qquad(k>0),
\]

负方向因为 downward traversal 会反转 interface offsets，定义

\[
\delta_{-q}
=-\sum_{j=-q}^{-1}\sigma_j
\qquad(q>0).
\]

此处不要求 periodicity、stationarity、probability law 或任何 frequency hypothesis。

对任意有限 graph shell radius `n`，只需要有限 imbalance window

\[
(\delta_{-n},\ldots,\delta_n).
\]

## 3. P022-BGA01 —— BG01 本来就是完全 aperiodic 的

对 target layer `k`，记

\[
q=|k|,
\qquad d=|\delta_k|,
\qquad c=(q-d)/2.
\]

Barlow prefix normal form

\[
P_k=(A+3)^cB_\pm^d
\]

只使用有限 interface polynomial product 的 commutativity，从未使用周期性。

因此 exact layer-shell formula 对任意 stacking word 都成立。

若 `q=n`：

\[
\boxed{L_n(k)=3^n.}
\]

若 `q<n`：

\[
\boxed{
L_n(k)=\binom nq
\left(
3\cdot2^{n-q+c}(1+2^d)-6
\right).
}
\]

whole shell 仍是

\[
\boxed{
T_n=\sum_{k=-n}^{n}L_n(k).
}
\]

所以这是一个针对 arbitrary two-sided Barlow stacking 的 exact finite theorem。

## 4. one-sided asymptotic drift densities

假设下面两个极限存在：

\[
\boxed{
\mu_+=\lim_{k\to+\infty}\frac{|\delta_k|}{k},
}
\]

以及

\[
\boxed{
\mu_-=\lim_{q\to+\infty}\frac{|\delta_{-q}|}{q}.
}
\]

因为每次 increment 只能是 ±1，

\[
0\le\mu_+,\mu_-\le1.
\]

两个 limits 允许不同，也就是相对于选定 root layer，正负两侧可以具有不同的长期 drift。

定义

\[
\boxed{
\mu_*=\max(\mu_+,\mu_-).}
\]

## 5. P022-BGA02 —— one-sided shell-growth law

先只看 positive target layers，令

\[
T_n^+=\sum_{k=1}^{n-1}L_n(k),
\]

暂时排除 single extreme layer。

对任意 `epsilon>0`，存在 `Q` 使得所有 `q>=Q` 都满足

\[
(\mu_+-\epsilon)q
\le
|\delta_q|
\le
(\mu_++\epsilon)q.
\]

BG01 中出现的

\[
2^{-q/2}
\left(2^{|\delta_q|/2}+2^{-|\delta_q|/2}\right)
\]

对 `|delta_q|` 单调递增，所以充分高的 positive layers 会被“把实际 drift 替换成 `mu_+-epsilon` / `mu_++epsilon`”所得的两组 binomial sums 精确夹住。

有限个 `q<Q` layers 至多贡献 `2^n` 乘 `n` 的固定次数多项式，其 exponential base 只有 `2`，因此在最终增长率中消失。

对两边 comparison sums 直接应用上一份 periodic proof 的 binomial identity，得到

\[
\liminf_{n\to\infty}(T_n^+)^{1/n}
\ge
2+2^{(1+\mu_+-\epsilon)/2},
\]

以及

\[
\limsup_{n\to\infty}(T_n^+)^{1/n}
\le
2+2^{(1+\mu_++\epsilon)/2}.
\]

令 `epsilon -> 0`：

\[
\boxed{
\lim_{n\to\infty}(T_n^+)^{1/n}
=2+2^{(1+\mu_+)/2}.}
\]

negative half-shell 对 `mu_-` 完全同理。

## 6. P022-BGA03 —— aperiodic two-sided growth theorem

完整 shell total 由以下四部分相加：

- positive half-shell；
- negative half-shell；
- central layer；
- 两个 extreme target layers。

central triangular layer 的 exponential base 是 `2`；extreme vertical layers 的 base 是 `3`。

任意 `mu in [0,1]` 都满足

\[
2+2^{(1+\mu)/2}
\ge
2+\sqrt2
>3.
\]

因此 central/extreme layers 都不会主导最终增长。

positive/negative 两个 half-shell 的和最终由增长更快的一侧支配，所以

\[
\boxed{
\lim_{n\to\infty}T_n^{1/n}
=
2+2^{(1+\mu_*)/2},
\qquad
\mu_*=\max(\mu_+,\mu_-).
}
\]

至此 periodicity 已经从 growth-rate theorem 中完全消失。

## 7. 推论

### balanced but nonperiodic stacking

若两侧都满足

\[
|\delta_k|=o(|k|),
\]

则

\[
\mu_+=\mu_-=0,
\]

所以

\[
\boxed{
\lim T_n^{1/n}=2+\sqrt2.}
\]

因此 HCP 的 geodesic-growth exponent 并不只属于 periodic HCP；任何 asymptotically balanced Barlow word 都共享这一 exponent。

finite shell spectra 仍然可以完全不同。

### fully drifting stacking

若 dominant direction 满足

\[
|\delta_k|/|k|\to1,
\]

则

\[
\boxed{
\lim T_n^{1/n}=4,}
\]

回到 FCC constant-drift exponent。

### asymmetric root environment

若正负两侧 limits 不同，只有较大的 absolute drift 决定总 exponential rate；较低 drift 一侧仍保留在 finite/subdominant structure 中，但不会进入 leading growth exponent。

## 8. 去掉 periodicity 后的精度层级

finite 与 asymptotic future language 的区别现在更清楚。

### exact finite radius `n`

需要状态

\[
(|\delta_{-n}|,\ldots,|\delta_n|).
\]

### infinite asymptotic growth rate

如果 one-sided drift limits 存在，整个 infinite trajectory 可以坍缩成

\[
\boxed{(\mu_+,\mu_-)}
\]

而只问 total growth 时又能进一步坍缩成

\[
\boxed{\mu_*=\max(\mu_+,\mu_-).}
\]

对 periodic word，每个 `mu` 都是 rational，可用整数 numerator/denominator 精确保存。对 arbitrary aperiodic word，limit 可能是 irrational 或无法由单一整数对有限表示；这里的 theorem 是数学 quotient statement，不主张所有 asymptotic drift values 都有有限 exact encoding。

这是一个必须保留的 precision boundary：

> **每个有限 radius 的 exact geometry 仍然完全 finite/integer；而 infinite asymptotic observable 可以合法产生一个本身不再是有限整数 state 的 limit object。**

不能把这两层混为一谈。

## 9. recurrence closure 恰好需要更强的 periodicity

aperiodic drift theorem 保住 dominant exponential rate，但一般不会保住 BG04 的 finite constant recurrence。

periodic stacking 给出精确 residue-affine 关系

\[
\delta_{mL+r}=mD+\delta_r,
\]

这正是 root-of-unity filtering 成立、最终生成 rational generating function 的原因。

如果 arbitrary sequence 只满足

\[
|\delta_k|/|k|\to\mu,
\]

phase coefficients 不一定重复，因此不能仅从 drift limit 推出 constant recurrence。

所以另一个 exact hierarchy 是：

\[
\text{drift limit}
\Rightarrow
\text{growth exponent},
\]

而

\[
\boxed{
\text{periodic finite phase}
\Rightarrow
\text{rational generating function / C-finite recurrence}.}
\]

不主张 converse。

## 10. 与 disordered close packing 的关系

该定理允许 P022 直接处理 deterministic nonperiodic 或 disordered close-packed stacking，而不需要先用周期 approximant 替换它。

本文**不**引入概率模型。若后续应用自己给出 stochastic stacking law，并独立证明 almost-sure drift density，则 BGA03 可按 pathwise 方式应用到 almost every realized stacking word。

任何 probability law 都属于当前 integer graph geometry 之外的额外结构。

## 11. executable support

新增：

- `src/enterprise_math/p022_barlow_aperiodic.py`；
- `tests/test_p022_barlow_aperiodic.py`。

finite executable layer 直接把 BG01 暴露成 `(radius,target_layer,imbalance)` 的函数，并能从任意有限 two-sided imbalance trajectory 重建 whole-shell total。periodic stacking 被验证会精确 factor through 这一更一般的 finite state。
