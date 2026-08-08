# Legendre 压力测试 —— 补充 06

状态：`ACTIVE RESEARCH NOTE`  
范围：大横向 support 的盆地命中与 anchor-surviving smooth-cofactor 闭合  
纪律：**本文不证明 Legendre 猜想。**

记

\[
M=k(k+1),
\qquad
I_k=M+\{1-k,\ldots,k\}.
\]

于是 \(I_k\) 恰好是 \(k^2\) 与 \((k+1)^2\) 之间的开放盆地，共有 \(2k\) 个整数状态。

取一组互异的横向素数 \(P\)，其中每个 \(p\le k\) 且 \(p\nmid M\)，记

\[
G_P=\prod_{p\in P}p.
\]

本补充只保留旧四支持聚合路线中**不依赖缺失 graph-tail 实现**的部分。

## 1. L028 —— 大 support product 在盆地中精确零次或一次命中

状态：`PROVED`。

假设

\[
G_P>2k.
\]

则 \(I_k\) 中至多有一个状态被 \(G_P\) 整除。

令

\[
a_P=M\bmod G_P,
\qquad 0\le a_P<G_P.
\]

存在可整除状态，当且仅当满足以下两个条件之一：

\[
\boxed{a_P<k}
\]

或

\[
\boxed{a_P\ge G_P-k}.
\]

存在时，中心偏移 \(s_P\) 为

\[
\boxed{
s_P=
\begin{cases}
-a_P,&a_P<k,\\
G_P-a_P,&a_P\ge G_P-k.
\end{cases}}
\]

对应状态

\[
n_P=M+s_P.
\]

### 证明

允许偏移满足

\[
1-k\le s\le k,
\]

共有 \(2k\) 个整数，其直径为 \(2k-1<G_P\)。因此两个不同允许偏移不可能模 \(G_P\) 同余，所以至多命中一次。

整除条件为

\[
a_P+s\equiv0\pmod{G_P}.
\]

负偏移区间里唯一可能代表元是 \(-a_P\)，它可用当且仅当 \(a_P<k\)；正偏移区间里唯一可能代表元是 \(G_P-a_P\)，它可用当且仅当 \(a_P\ge G_P-k\)。证毕。

### 半尺度 cofactor

若命中存在，写成

\[
n_P=G_Ph_P.
\]

因为 \(G_P\ge2k+1\)，且

\[
n_P\le(k+1)^2-1=k^2+2k,
\]

所以

\[
\boxed{h_P\le\left\lfloor\frac{k+1}{2}\right\rfloor.}
\]

因此一个大 support-product 事件被压缩为“一个余数判据 + 一个处于原尺度一半以内的 cofactor”。

## 2. L029 —— exact-support 闭合必须显式要求 anchor survival

状态：`PROVED`。

令 \(A_k\) 为所有满足 \(p\le k\) 且 \(p\mid M\) 的锚点素数之积。设 L028 给出唯一命中

\[
n_P=G_Ph_P.
\]

则在 **anchor-surviving** 盆地状态中，

\[
\boxed{
\operatorname{Supp}_{\mathrm{tr}}(n_P)=P
\iff
h_P\text{ 为 }P\text{-smooth}.
}
\]

这里 `P-smooth` 指 \(h_P\) 的每个素因子都属于 \(P\)。

### 证明

正向现在明确加入 anchor survival。因为

\[
h_P\le\left\lfloor\frac{k+1}{2}\right\rfloor\le k,
\]

所以任意 \(q\mid h_P\) 都是小素因子。anchor survival 排除 \(q\mid A_k\)，故 \(q\) 必为横向素数；若横向 support 恰为 \(P\)，只能有 \(q\in P\)。

反过来，如果 \(h_P\) 的所有素因子都属于 \(P\)，那么 \(n_P=G_Ph_P\) 的全部素因子都属于横向集合 \(P\)。因此该状态自动通过 anchor sieve，并且横向 support 恰为 \(P\)。证毕。

这里的 anchor-survival 限定不可删除。单纯说“横向 support 恰为 \(P\)”并不能排除 cofactor 里还藏有锚点素因子。

## 3. 修正旧过强表述的边界例

取

\[
k=10,
\qquad M=110,
\qquad P=\{3,7\},
\qquad G_P=21>20.
\]

L028 给出的唯一盆地命中为

\[
105=21\cdot5.
\]

105 的原始横向 support 的确是

\[
\{3,7\},
\]

因为 5 是整除 \(k\) 的锚点素因子。但

\[
\gcd(105,A_{10})>1,
\]

所以这个状态**并不**是 anchor-surviving。由此可见，旧表述“exact transverse support 当且仅当 cofactor 为 P-smooth”如果不加 anchor survival 就是过强的。

正例为

\[
k=16,
\qquad P=\{5,11\},
\qquad G_P=55>32,
\]

唯一命中为

\[
275=55\cdot5.
\]

此时 cofactor 为 \(P\)-smooth，状态通过 anchor sieve，并且横向 support 恰为 \(\{5,11\}\)。

## 4. 旧聚合 Draft 中哪些内容不升级

旧 Supplement-06 Draft 还尝试使用一个 `four_support_square_tail` graph-tail 例程聚合四素数 exact-support 贡献。但该实现甚至不存在于历史分支中，因此相关聚合定理**不在本次进入 canonical**。

本补充只升级两个独立且可以完整审计的事实：

1. 大 support-product 的盆地 incidence 精确为零或一；
2. exact transverse support 通过半尺度 cofactor 闭合时，必须显式加入 anchor-surviving 条件。

四支持 graph-tail 聚合继续作为独立 Draft 义务。单靠 L028–L029 尚不能推出足以证明 Legendre 猜想的消去估计。

## 5. 可执行验证

`src/enterprise_math/support_incidence.py` 与 `tests/test_support_incidence.py` 会审计：

- 余数判据与直接盆地枚举完全一致；
- 有界横向 support 集上的零/一命中；
- 半尺度 cofactor 上界；
- anchor-surviving exact-support 等价；
- `k=10, P={3,7}` 的锚点污染反例；
- `k=16, P={5,11}` 的正向闭合例。
