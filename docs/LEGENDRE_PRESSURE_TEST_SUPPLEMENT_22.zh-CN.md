# Legendre 压力测试 — 补充 22

状态：`PROVED REDUCTION + OPEN FRONTIER`  
范围：square-of-square 对角线上 realized high-band root repair 的精确 prime-pair normal form  
依赖：P017 L060–L062、P007 dual factor windows、P023-S9 realized repair counting  
纪律：这是一个 reduction theorem，不声称由此得到的受限 Goldbach multiplicity 已经证明无界。

## 1. 设置

固定

\[
K=t^2,
\qquad
t\ge6,
\]

并在外层 square basin

\[
(K^2,K(K+2)]
\]

中只保留 cofactor root `t`。

由 L060，任何能到达 root `t` 的 raw prime shell label 都满足

\[
\boxed{(t-1)^2+3\le p\le K.}
\]

写成

\[
p=K-a,
\qquad
0\le a\le2t-4.
\]

root bucket `t` 内的 quotient 写成

\[
q=K+b,
\qquad
0\le b\le2t.
\]

## 2. L063-A —— 对角 p-rough realizability 等价于 primality

状态：`PROVED`。

对每个 raw diagonal prime label `p`，以及 root bucket `t` 中任意 `q`，都有

\[
\boxed{q\text{ 为 }p\text{-rough}\iff q\text{ 为 prime}.}
\]

### 证明

由 raw factor window，

\[
p\ge(t-1)^2+3.
\]

当 `t>=6` 时，这严格大于 `t+1`。而

\[
q<(t+1)^2,
\]

因此

\[
\sqrt q<t+1<p.
\]

如果 `q` 为 composite，它必有一个不大于 `sqrt(q)` 的素因子，因此存在严格小于 `p` 的素因子，与 `p`-rough 矛盾。

反之若 `q` 为 prime，它没有小于自身的素因子；这里 `q>=K>=p`，故必为 `p`-rough。∎

所以对角线上的 realizability filter 把 rough-shell 问题精确变成了 prime-pair 问题。

## 3. L063-B —— 只可能出现两个中心 offset

状态：`PROVED`。

设 `p=K-a`、`q=K+b` 构成一个 realized diagonal state 的两个 prime factors。定义

\[
c=b-a.
\]

则

\[
\boxed{c\in\{2,4\}.}
\]

### 奇偶性与正性

对 `t>=6`，`p,q` 都是奇素数。因为 `a=K-p`、`b=q-K`，所以 `a,b` 同奇偶，因此 `c` 为偶数。

又

\[
pq-K^2
=K(b-a)-ab
=Kc-ab.
\]

状态严格位于 `K^2` 上方，所以该量为正，故 `c>0`，于是 `c>=2`。

### 排除 c>=6

root bucket 给出 `b<=2t`。若 `c=b-a`，则

\[
a\le2t-c.
\]

因此

\[
ab=a(a+c)\le(2t-c)(2t)=4K-2ct.
\]

basin 上界 `pq<=K(K+2)` 给出

\[
Kc-ab\le2K,
\]

也就是

\[
(c-2)K\le ab.
\]

但若 `c>=6`，

\[
(c-2)K-(4K-2ct)
=(c-6)K+2ct>0,
\]

与上面两个不等式矛盾。因此 `c` 不可能达到 6 或更大。由于它又是正偶数，只剩 `2` 与 `4`。∎

## 4. L063-C —— 精确 two-slice Goldbach 分类

状态：`PROVED`。

令 `K=t^2`，并取 prime `p=K-a`，其中 `0<=a<=2t-4`。

label `p` 在 root `t` 上被真实实现，当且仅当下面两种情况至少有一种成立。

### Slice 2

\[
\boxed{
q=K+a+2\text{ 为 prime},
\qquad
a(a+2)<2K.
}
\]

等价地，

\[
\boxed{p+q=2K+2.}
\]

因为

\[
pq-K^2
=2K-a(a+2),
\]

其上界不超过 `2K` 自动成立；严格为正恰好等价于上述不等式。

### Slice 4

\[
\boxed{
q=K+a+4\text{ 为 prime},
\qquad
2K\le a(a+4)<4K.
}
\]

等价地，

\[
\boxed{p+q=2K+4.}
\]

此时

\[
pq-K^2
=4K-a(a+4),
\]

要求它属于 `(0,2K]`，恰好得到上述双边不等式。

由 L063-B 不存在其他 offset；由 L063-A，`q` 为 prime 又恰好是 realizability 条件。因此这两个 slices 联合起来既必要又充分。∎

## 5. 精确 repair multiplicity 是并集，不是相加

定义两个 left-prime label sets：

\[
\mathcal P_2(t)
=
\{K-a:\ K-a,K+a+2\text{ 为 prime},\ a(a+2)<2K\},
\]

以及

\[
\mathcal P_4(t)
=
\{K-a:\ K-a,K+a+4\text{ 为 prime},\ 2K\le a(a+4)<4K\}.
\]

则

\[
\boxed{
P^{\rm sh}_{t^2,t}
=
\mathcal P_2(t)\cup\mathcal P_4(t)
}
\]

从而

\[
\boxed{
R^{\rm sh}_{t^2,t}
=
|\mathcal P_2(t)\cup\mathcal P_4(t)|.
}
\]

这里必须取并集。`t=11`、`K=121` 时，同一个 shell label

\[
p=107
\]

同时有两个 witness：

\[
107+137=244=2K+2
\]

以及

\[
107+139=246=2K+4.
\]

所以直接把两个 Goldbach representation counts 相加，会对同一个 repair class 重复计数。

这再次给出项目的精确规则：

\[
\boxed{
\text{数 realized state labels，而不是形式 witness tuples}.}
\]

## 6. 对无界性前沿的影响

raw diagonal burden 已由 L061 证明无界。现在 realized diagonal burden 被精确约化成

\[
\boxed{
|\mathcal P_2(t)\cup\mathcal P_4(t)|.
}
\]

因此要证明

\[
\sup_t R^{\rm sh}_{t^2,t}=\infty
\]

等价于证明：沿 square sequence `K=t^2`，这两个受限、near-central Goldbach slices 能产生任意多的不同 left primes。

这比此前“realizability 与 prime pairs 有关”的表述明显更强：现在已经准确识别出缺失的数论对象。

本补充不主张该无界性已经解决。

## 7. 工具反哺

这一 reduction 完整展示了研究工具链：

1. P007 dual window 删除无关 factor labels；
2. p-rough admissibility filter 把 envelope 变成 actual shell states；
3. parity 与 basin inequalities 把剩余 prime-pair geometry 压成两个精确 slices；
4. P023-S9 告诉我们 repair cost 要数**不同 realized shell labels**，因此取并集而不是 witness 数。

最终留下的 hard object 已经是 prime-pair counting problem，而不再是状态语义上的模糊。

## 8. 可执行规格

`diagonal_goldbach_slices(t)` 位于

- `src/enterprise_math/p017_high_band_root_precision.py`

它构造两个 slices，并断言其 label union 与独立编译得到的 realized p-rough shell labels 完全一致。回归覆盖 `6<=t<=100`，并固定 `t=11,p=107` 的双 witness 例子。
