# P018 —— 有限精度证明演算：补充 07

状态：`ACTIVE RESEARCH NOTE`  
范围：平方盆地 factor proof slack 与固定偶数素数间距之间的精确关系  
依赖：P018 第七阶段与 P017 first-factor shell  
纪律：twin/cousin prime 与 bounded prime gap 都是成熟数论问题。下文使用的外部界明确归功于 D. H. J. Polymath。本文不改进任何素数间距界，也不证明 Legendre 猜想。

## 1. 从 factor horizon 到 factor proof slack

第七阶段定义最小 survivor-prime horizon：

\[
H(k)=\max\{\operatorname{spf}(n): k^2<n<(k+1)^2,\ n\text{ 为合数}\}
\]

以及非负 factor proof slack：

\[
\boxed{\sigma(k)=k-H(k).}
\]

为避免与 bounded-prime-gap 文献中的标准记号 `H_1` 混淆，本补充有时把同一个 horizon 记作

\[
h_{\mathrm{fac}}(k)=H(k).
\]

现在的问题是：如果最后一个 composite shell 只比 universal cutoff `k` 低 `s` 个 precision 单位，会被迫出现什么算术结构？

记

\[
s=\sigma(k),
\qquad
p=k-s.
\]

此时 `p=H(k)` 就是最后一个非空 composite first-decision shell 的 least-prime-factor index。

## 2. P018-T63 —— Near-diagonal shell / fixed-gap 定理

状态：`PROVED`。

设 `s>=0`，令

\[
p=k-s
\]

为奇素数，并假设

\[
\boxed{p>(s+1)^2.}
\]

则

\[
\boxed{
L_p(k)\ne\varnothing
\iff
q:=p+2(s+1)\text{ 为素数}.
}
\]

而且非空时

\[
\boxed{
L_p(k)=\{pq\}.
}
\]

### 第一步：大小条件已经足以迫使 shell 成为 semiprime shell

记 `t=s+1`。由于 `p>t^2` 且 `p>=3`，有 `t<=p-1`、`t^2<=p-1`，所以

\[
2pt+t^2
\le
2p(p-1)+(p-1).
\]

于是

\[
\begin{aligned}
p^3-(p+t)^2
&=p^3-p^2-2pt-t^2\\
&\ge p^3-3p^2+p+1\\
&=p^2(p-3)+p+1>0.
\end{aligned}
\]

又因 `k+1=p+s+1=p+t`，得到

\[
p^3>(k+1)^2>(k+1)^2-1.
\]

因此第七阶段 T62 可用：`L_p(k)` 中每个状态都只能是

\[
n=pq,
\qquad q>p\text{ 为素数}.
\]

### 第二步：cofactor interval 只剩两个整数候选

盆地不等式为

\[
(p+s)^2<pq<(p+s+1)^2.
\]

除以 `p`：

\[
p+2s+\frac{s^2}{p}
<q<
p+2s+2+\frac{(s+1)^2}{p}.
\]

因为 `p>(s+1)^2`，两侧分数都小于 1，所以整数 `q` 只能是

\[
p+2s+1
\quad\text{或}\quad
p+2s+2.
\]

第一项因为 `p` 为奇数而是大于 2 的偶数，不可能为素数。因此必有

\[
q=p+2s+2=p+2(s+1).
\]

必要性与唯一性得到证明。

### 第三步：反向

如果 `p` 与 `q=p+2(s+1)` 都为素数，则

\[
pq-k^2=2p-s^2>0
\]

而

\[
(k+1)^2-pq=(s+1)^2>0.
\]

所以 `pq` 位于开放平方盆地，并且最小素因子就是 `p`，反向成立。∎

因此，靠近 universal factor horizon 的 shell 被一个固定偶数素数间距完全控制。

## 3. P018-T64 —— 零 slack 恰好是 twin-prime stratum

状态：`PROVED`。

对所有 `k>=3`：

\[
\boxed{
\sigma(k)=0
\iff
k\text{ 与 }k+2\text{ 都是素数}.
}
\]

因为 `sigma(k)=0` 即 `H(k)=k`，所以 `L_k(k)` 非空。对 T63 取 `s=0`，唯一可能状态为

\[
k(k+2)=(k+1)^2-1,
\]

它存在当且仅当 `k,k+2` 同为素数。

反之，一对 twin primes `k,k+2` 使 `k(k+2)` 落入 `L_k(k)`，故 `H(k)>=k`；第七阶段已有 `H(k)<=k`，于是相等。∎

因此 Twin Prime Conjecture 等价于：

\[
\boxed{
\sigma(k)=0
\text{ 对无穷多个 }k\text{ 成立}.
}
\]

这只是等价改写，不是 twin-prime 进展。

## 4. P018-T65 —— Slack one 恰好对应 gap-four prime pair

状态：`PROVED`。

对所有 `k>=4`：

\[
\boxed{
\sigma(k)=1
\iff
k-1\text{ 与 }k+3\text{ 都是素数}.
}
\]

`k=4` 可直接检查：`H(4)=3`，同时 `3,7` 为 gap-four prime pair。

对更大 `k`，若 `sigma=1`，则 `p=H=k-1` 为素数。`k>=6` 时 `p>4=(s+1)^2`，T63 迫使 `p+4=k+3` 为素数。

反之若 `k-1,k+3` 都为素数，则

\[
(k-1)(k+3)=(k+1)^2-4
\]

位于 `L_(k-1)(k)`。当 `k>4`，`k-1` 为奇素数迫使 `k` 为偶合数，因此 index `k` 不可能再出现 prime-index shell，故 `H=k-1`。∎

所以 gap-four prime pair 无限多，等价于 `sigma(k)=1` 无限多。

## 5. P018-T66 —— 实际 bounded slack 迫使固定偶数 prime gap

状态：`PROVED`。

若

\[
\sigma(k)=s,
\qquad
p=k-s\ge3,
\qquad
p>(s+1)^2,
\]

则 `p=H(k)`，所以 `L_p(k)` 必非空。由 T63：

\[
\boxed{
p\text{ 与 }p+2(s+1)\text{ 都为素数}.}
\]

因此充分大的区域内，一个实际很小的 factor proof slack 会强制产生精确偶数间距

\[
\boxed{2(s+1)}
\]

的素数对。

## 6. P018-T67 —— 固定 prime gap 产生 bounded-slack 平方盆地

状态：`PROVED`。

设

\[
p,\quad q=p+2m
\]

都是素数，`m>=1`，并且

\[
\boxed{p>m^2.}
\]

取

\[
s=m-1,
\qquad
k=p+s=p+m-1.
\]

于是 `p=k-s`，T63 给出

\[
pq\in L_p(k).
\]

所以

\[
H(k)\ge p=k-s,
\]

从而

\[
\boxed{
\sigma(k)=k-H(k)\le s=m-1.
}
\]

因此，每一个足够大的固定 gap `2m` 素数对都会生成一个 factor proof slack 至多为 `m-1` 的平方盆地。

实际 slack 可能更小，因为还可能存在更靠后的非空 first-factor shell。

## 7. P018-T68 —— 无穷次 bounded factor slack 与某个固定 prime gap 无穷出现等价

状态：`PROVED`。

下列两命题等价：

1. 存在整数 `S>=0`，使 `sigma(k)<=S` 对无穷多个 `k` 成立；
2. 存在整数 `m>=1`，使素数对 `p,p+2m` 出现无穷多次。

### 1 => 2

在无穷多个 `sigma(k)<=S` 中，有限集合

\[
\{0,1,\ldots,S\}
\]

里必有某个精确 slack `s` 出现无穷多次。

对其中充分大的 `k`，有 `p=k-s>(s+1)^2`。T66 于是给出 gap

\[
2(s+1)
\]

的素数对无穷多次。取 `m=s+1`。

### 2 => 1

若 `p,p+2m` 无穷多次出现，则最终必有 `p>m^2`。T67 把每一对充分大的 prime pair 映射到

\[
k=p+m-1
\]

并满足

\[
\sigma(k)\le m-1.
\]

所以 bounded factor proof slack 也出现无穷多次。∎

因此“`liminf sigma(k)` 是否有限”正好是“是否存在某个固定偶数 prime gap 无穷出现”的另一种有限精度表述。

## 8. P018-T69 —— 已知 bounded prime gaps 给出无条件 slack 上界

状态：`PROVED COROLLARY OF ESTABLISHED PRIOR ART`。

D. H. J. Polymath 已证明无条件 bounded-gap 结果

\[
H_1^{\mathrm{gap}}
:=
\liminf_{n\to\infty}(p_{n+1}-p_n)
\le246.
\]

[SRC-POLYMATH-2014-BOUNDED-GAPS]

因此有无穷多对相邻素数间距不超过 `246`。

充分大的素数之间的正间距必为偶数，于是在有限集合

\[
2,4,\ldots,246
\]

中，至少有一个固定偶数间距 `2m` 出现无穷多次，其中

\[
m\le123.
\]

对这个固定 gap 使用 T67，可得无穷多个对应平方盆地满足

\[
\sigma(k)\le m-1\le122.
\]

所以

\[
\boxed{
\liminf_{k\to\infty}\sigma(k)\le122.
}
\]

这**不**改进 Polymath 的 prime-gap 定理；它只是把已有定理翻译成 P018 factor-precision 语言中的一个无条件结论。

若未来外部结果把 `H_1^gap` 改进到 `<=2M`，同一证明会自动给出

\[
\liminf\sigma(k)\le M-1.
\]

## 9. P018-T70 —— 最后 precision obstruction 定位在 upper square 下方一个平方 offset

状态：`PROVED`。

在 T66 条件下，最后一个非空 composite shell 的唯一状态为

\[
n=p[p+2(s+1)].
\]

代入 `p=k-s`：

\[
\boxed{n=(k-s)(k+s+2).}
\]

围绕上方平方点展开：

\[
\boxed{n=(k+1)^2-(s+1)^2.}
\]

所以 factor precision slack 同时决定三个量：

\[
\boxed{
\begin{aligned}
\text{factor slack} &= s,\\
\text{forced prime gap} &= 2(s+1),\\
\text{upper-square offset} &= (s+1)^2.
\end{aligned}}
\]

这是第八阶段对 P018 最初命题“**精度变化本身就是数学结构**”最直接的体现：一个有限 proof-precision distance 同时变成 prime-pair distance 与 square-basin geometric offset。

## 10. 这些结果解决了什么、又没有解决什么

第八阶段给出了精确等价关系与一个无条件外部定理推论，但没有证明 Legendre 猜想。

特别地：

- bounded `sigma` 只说明最后 composite obstruction 靠近 universal factor cutoff；
- prime survivor 是否存在仍是 Legendre 的核心目标；
- `sigma=0` 无穷多次正好就是 twin-prime conjecture，不是它的证明；
- T69 只导入已建立的 bounded-prime-gap theorem 并做变量翻译，没有提高其界。

真正的增益是结构性的：一个原本作为内部 proof-effort quantity 提出的 P018 precision observable，现在获得了精确的外部数论含义。

## 11. 前人边界

Twin primes、gap-four prime pairs、固定偶数素数间距问题与 bounded gaps between primes 都是成熟数论研究。

本文使用的无条件输入来自 D. H. J. Polymath，*Variants of the Selberg sieve, and bounded intervals containing many primes*，Research in the Mathematical Sciences 1 (2014), Article 12，DOI `10.1186/s40687-014-0012-7`。[SRC-POLYMATH-2014-BOUNDED-GAPS]

进取数论不声称 `246` 界、其背后的 Selberg/Maynard-Tao sieve 技术或 fixed-gap conjecture 是项目创新。

当前要检验的项目特有结果是如下精确变量桥：

\[
\text{factor proof slack}
\longleftrightarrow
\text{near-diagonal first-factor shell}
\longleftrightarrow
\text{fixed even prime gap}
\longleftrightarrow
\text{upper square 下方的 square offset},
\]

以及由此把已有 bounded-gap theorem 翻译成 `liminf sigma(k)` 的无条件上界。

这一翻译的历史创新状态仍为 `NOVELTY_UNVERIFIED`。

## 12. 第八阶段状态

- P018-T63 near-diagonal shell / fixed-gap theorem：`PROVED`
- P018-T64 `sigma=0` iff twin-prime pair：`PROVED`
- P018-T65 `sigma=1` iff gap-four prime pair：`PROVED`
- P018-T66 actual bounded slack forces fixed prime gap：`PROVED`
- P018-T67 fixed prime pair creates bounded slack：`PROVED`
- P018-T68 bounded-slack / fixed-gap infinitude equivalence：`PROVED`
- P018-T69 Polymath `246` => `liminf sigma<=122`：`PROVED COROLLARY OF PRIOR ART`
- P018-T70 square-offset localization：`PROVED`
- `sigma=0` 无穷多次 / Twin Prime Conjecture：`OPEN, EQUIVALENT FORMULATION`
- 对所有充分大 `k` 的 universal bound `sigma(k)<=S`：`OPEN`
- 利用 bounded slack 证明每个平方盆地必有 prime survivor：`OPEN`

可执行有限检查位于 `src/enterprise_math/prime_gap_slack.py` 与 `tests/test_prime_gap_slack.py`。
