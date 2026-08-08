# P019 补充 12 —— 什么情况下 transport 计数重新足够

状态：`TESTING / 有限充分条件已证明`

补充 11 已证明：一般情况下，cardinality transport matrix 不是 composition-complete 的，因为它忘记了究竟是哪一条 middle incidence 支撑后续 continuation。本文给出一个干净的受限条件，在该条件下，丢失 witness identity 不再影响三步链总数。

设一个中间方向类包含

\[
e_1,\ldots,e_m.
\]

对每条 middle incidence 定义 predecessor / successor witness multiplicity：

\[
l_i=\#\{e^-:e^-\text{ 可以拼接进入 }e_i\},
\qquad
r_i=\#\{e^+:e_i\text{ 可以继续拼接到 }e^+\}.
\]

两侧相邻 transport counts 为

\[
L=\sum_i l_i,
\qquad
R=\sum_i r_i,
\]

而真实三步链数量为

\[
\boxed{N=\sum_i l_i r_i.}
\]

一般情况下，仅知道 \(L,R\) 并不足以确定 \(N\)。

但如果任意一侧 witness profile 完全均匀——即全部 \(l_i\) 相等，或者全部 \(r_i\) 相等——就有

\[
\boxed{mN=LR.}
\]

这个结论不需要做除法。比如若每个 \(l_i=a\)，则 \(L=ma\)，而 \(N=aR\)，所以 \(mN=LR\)。successor-uniform 情况完全对称。

因此 P019 现在得到一条明确的降维规则：

> **一般情况下保留 witness transport；只有当中间方向类至少一侧 witness fibers 均匀时，cardinality transport 才足以恢复精确三步计数。**

这是充分条件，不声称必要。若 predecessor 和 successor profiles 都不均匀，当前实现会拒绝仅根据基数推断精确复合，而不是偷偷做平均化。

这个结果也进一步说明，未来如果 P019 要研究类似连续极限的 coarse regime，那么“均匀”不能只表示总 transport counts 看起来接近，而应至少涉及被聚合的 exact middle incidences 上 witness fibers 的结构均匀性。

本文没有引入概率独立性、平均场假设、连续极限或物理各向同性。
