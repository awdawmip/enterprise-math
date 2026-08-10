# P025 补充 80 —— 分圆精度地平线与全局周期尾

状态：`ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation：`program/p025-cyclotomic-stage76`  
依赖：P025 补充 78–79  
硬阻断：`NONE`

## 1. 为什么 Stage 79 还不是全局 tail theorem

Stage 79 证明，对一个固定的已激活奇素数同指数 cyclotomic signature，

\[
\frac{\#\text{allowed ratio classes}}{M}
\ll
\frac1T
\left(\frac{\ell-1}{2\ell+1}\right)^k.
\]

这只是 fixed-signature density statement。要得到全局计数，还必须对所有可能 repeated moduli 与 repeated-support patterns 求和。

本补充在 repeated modulus 不超过有限 prime-base observation window 的范围内完成这一步求和，并精确隔离周期密度模型停止继续获益的边界。

## 2. P025-T159 —— cyclotomic residual 唯一决定 repeated modulus

设

\[
F=F_{\ell,\pm}
\]

为非线性 cyclotomic factor，并写其 repeated prime factorization 为

\[
F=\left(\prod_{i=1}^k r_i^{e_i}\right)S,
\qquad e_i\ge2,
\]

其中 `S` squarefree 且与所有 `r_i` 互素。

定义 cyclotomic multiplicity residual

\[
\boxed{d:=m(F)=\prod_{i=1}^k r_i^{e_i-1}.}
\]

full repeated modulus 为

\[
M=\prod_{i=1}^k r_i^{e_i}.
\]

因此

\[
\boxed{M=d\operatorname{rad}(d).}
\]

反过来，`M` 中每个素数的指数都恰好比 `d` 中多 1，所以映射

\[
d\longleftrightarrow M=d\operatorname{rad}(d)
\]

是一一对应。

CRT class count 同样只由 `d` 决定：

\[
\boxed{C_\ell(d):=(\ell-1)^{\omega(d)}.}
\]

因此 repeated cyclotomic signature 可以只用 residual integer `d` 编号，不再需要把 `(M,k)` 当成彼此独立的状态。

## 3. signature-density weight

对 residual `d` 定义

\[
\boxed{w_\ell(d):=\frac{(\ell-1)^{\omega(d)}}{d\operatorname{rad}(d)}.}
\]

由 Stage 79，真正可出现的 `d` 只含满足

\[
r\equiv1\pmod{2\ell}
\]

的素因子。丢掉这个 support restriction 只会放大下面的和，但保留它才是 theorem-native state。

`w_ell(d)` 精确等于

\[
\frac{\text{允许的 CRT ratio classes 数}}
{\text{full repeated modulus}}.
\]

## 4. P025-T160 —— weighted residual tail 可任意逼近 `1/Y`

固定

\[
0<\theta<1.
\]

对仅由 `1 mod 2ell` 素数组成的 residuals，考虑

\[
K_{\ell,\theta}
:=
\sum_d
\frac{(\ell-1)^{\omega(d)}d^\theta}
{d\operatorname{rad}(d)}.
\]

其 Euler product 为

\[
K_{\ell,\theta}
=
\prod_{r\equiv1\,(2\ell)}
\left(
1+(\ell-1)
\sum_{f\ge1}
\frac{r^{f\theta}}{r^{f+1}}
\right).
\]

局部尾为

\[
\sum_{f\ge1}r^{-1-f(1-\theta)}
=
\frac{r^{-(2-\theta)}}{1-r^{-(1-\theta)}}.
\]

因为

\[
2-\theta>1,
\]

Euler product 绝对收敛，所以

\[
\boxed{K_{\ell,\theta}<\infty.}
\]

当 `d>=Y` 时，

\[
1\le(d/Y)^\theta.
\]

于是

\[
\boxed{
\sum_{d\ge Y}w_\ell(d)
\le
K_{\ell,\theta}Y^{-\theta}.
}
\]

因此 aggregate reciprocal signature density 对每个固定 `theta<1` 都有

\[
\boxed{O_{\ell,\theta}(Y^{-\theta})}
\]

的 tail。

这比“每个固定 signature 都很稀”更强：在 periodic regime 内，所有 repeated-support patterns 可以同时求和。

## 5. Endpoint 边界

上面的 Mellin / Euler-product 证明不能直接令 `theta=1`。

在 `theta=1` 时，即使只固定一个允许素数 `r`，局部贡献也变成

\[
(\ell-1)\sum_{f\ge1}\frac1r,
\]

因为可以出现任意 exponent tower `r^f`，所以发散。

这**不**证明精确 `1/Y` tail 为假；它只证明当前 moment 方法存在真实 endpoint obstruction。

因此严格状态应写成

\[
\boxed{
Y^{-1+\varepsilon}\text{-type control 已由该方法证明；}
\quad Y^{-1}\text{ 在此仍未证明。}
}
\]

## 6. P025-T161 —— 有限 observation window 与 periodic regime

固定 prime-base height

\[
1\le p,q\le P.
\]

对一个 repeated residual `d`，令

\[
M=d\operatorname{rad}(d),
\qquad
C=(\ell-1)^{\omega(d)}.
\]

Stage 78 的 finite incidence bound 给出，与这些 ratio classes 相容的 ordered integer pairs 至多为

\[
C P
\left(
\left\lfloor\frac{P-1}{M}\right\rfloor+1
\right).
\]

若

\[
\boxed{M\le P,}
\]

则

\[
\left\lfloor\frac{P-1}{M}\right\rfloor+1
\le
\frac{2P}{M}.
\]

因此该 signature 的贡献至多为

\[
\boxed{
2P^2\frac{C}{M}
=2P^2w_\ell(d).
}
\]

这就是 **periodic precision regime**：observation window 至少容纳一个完整 modulus period，于是 congruence precision 可直接转化为 density reduction。

## 7. P025-T162 —— 全局 periodic activated tail

设 projective threshold

\[
T\ge1.
\]

Stage 79 证明每个 activated state 均满足

\[
d=m(F)\ge2T
\]

（difference branch 保留严格性）。

按照 exact residual `d` 对 periodic regime 中的 activated pairs 分类。由于 `d` 唯一决定 repeated modulus，这些 exact classes 在语义上构成不交 partition，尽管用来上界它们的 divisibility envelopes 可以互相重叠。

对 Stage 161 的上界求和并应用 P025-T160，得到

\[
N^{\rm per}_{\ell,T}(P)
\le
2P^2
\sum_{d\ge2T}w_\ell(d),
\]

因此对每个固定 `0<theta<1`，

\[
\boxed{
N^{\rm per}_{\ell,T}(P)
\ll_{\ell,\theta}
P^2T^{-\theta}.
}
\]

primality、`p>q` ordering 与 exact cyclotomic equation 只会继续减少这个 elementary integer-pair envelope。

所以：**整个 odd-prime equal-exponent activated state 的 periodic 部分，都具有任意逼近 `1/T` 的 aggregate pressure tail。**

## 8. P025-T163 —— supermodular precision 强迫平方根 residual floor

periodic argument 在

\[
\boxed{M>P}
\]

处停止。

这不是坏常数导致的证明失效，而是 finite-window semantics 真正发生改变：当 modulus 超过 `P` 时，对固定 `q`，一个 residue class 在 height-`P` window 内至多只含一个候选 `p`；继续增大 `M` 已不再产生新的 `P/M` 因子。

但 P025-T159 给出

\[
M=d\operatorname{rad}(d).
\]

又因为

\[
\operatorname{rad}(d)\le d,
\]

有

\[
M\le d^2.
\]

所以

\[
\boxed{M>P\Longrightarrow d>\sqrt P.}
\]

因此任何越过 congruence observation horizon 的状态都会自动进入更强的 residual tail：

\[
\boxed{m(F)>\sqrt P.}
\]

再结合 activation，可写成

\[
\boxed{d>\max\{2T,\sqrt P\}}
\]

（按 sum / difference 的严格性约定理解）。

## 9. 精确的 regime split

Stage 80 因而把全局问题分成两个数学性质不同的区域：

\[
\boxed{
M\le P:
\quad
N^{\rm per}_{\ell,T}(P)
\ll_{\ell,\theta}P^2T^{-\theta}
\quad(\theta<1),
}
\]

以及

\[
\boxed{
M>P:
\quad
m(F)>\sqrt P.
}
\]

第二个区域不应继续假装 periodic density formula 仍然有效；它需要一个针对“cyclotomic value 具有极大 multiplicity residual”的 value-side theorem。

这就是新的 hard boundary。

## 10. Precision-horizon 解释

这个算术机制是 finite precision horizon saturation 的一个精确实例。

地平线以下：

\[
M\le P,
\]

observation window 能解析多个完整周期，每增加一层 congruence precision 都会降低 candidate density。

地平线以上：

\[
M>P,
\]

一个 residue class 已经比 observation window 更细。继续增大 modulus 不再按照同一个 `P/M` cost model 付费。正确的 state transition 不再是“继续增加 congruence precision”，而是

\[
\boxed{
\text{congruence precision}
\to
\text{large-residual value state}.
}
\]

这正是 P018/P023/E002 所要捕捉的 theorem-native coordinate switch 类型。

## 11. Prior-art / novelty 边界

Euler product、绝对收敛与 elementary residue-class incidence 都是经典数学，P025 不单独主张其新颖性。

项目侧候选结果是 residual-to-modulus bijection、它与 Stage 79 projective activation threshold 的组合，以及由此得到的 periodic / supermodular precision-horizon split。历史新颖性仍记为 `NOVELTY_UNVERIFIED`。

## 12. 可执行资产

新增：

- `src/enterprise_math/abc_cyclotomic_precision_horizon.py`；
- `tests/test_abc_cyclotomic_precision_horizon.py`。

可执行层检查

\[
M=d\operatorname{rad}(d),
\]

exact finite incidence envelope、fixed-signature pressure bound，以及 cube / fifth-power fixtures 上的

\[
M>P\Rightarrow d^2>P.
\]

## 13. 下一前沿

不存在硬阻断。继续：

1. 不再继续堆 congruence refinement，而是利用 cyclotomic value 的代数结构攻击 supermodular region `m(F)>sqrt(P)`；
2. 对 cube quadratic factors 优先测试 Eisenstein norm / binary quadratic representation 能否给更强 value-side count；
3. 与偶指数四比较，因为那里 hard-state carrier 可以继续停留在 centered linear factors，odd-prime cyclotomic theorem 会失效；
4. 把 horizon-saturation mechanism 作为候选跨路线 law Relay 到 A2/E002，但不把 cyclotomic-specific arithmetic 本身提升进 Foundation。
