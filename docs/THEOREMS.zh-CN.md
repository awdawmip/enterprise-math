# v0.1 已证明命题

本文件中的状态表示普通数学证明已经从 v0.1 定义推出结论。除非特别注明，目前尚不表示已经通过 Lean 形式化检查。

## T001 —— 根刻画

状态：`PROVED`

对 \(p\ge1\)，

\[
R_p(n)=k\iff k^p\le n<(k+1)^p.
\]

这与定义中的最大值性质等价。

形式化：`EnterpriseMath.Arithmetic.IntegerRoot.root_eq_iff` 已通过 Lean 检查，并直接复用 Mathlib 已有的 `Nat.nthRoot` 定理。

## T002 —— 完全幂精确性

状态：`PROVED`

\[
R_p(k^p)=k.
\]

证明：\(k^p\le k^p<(k+1)^p\)，应用 T001 即可。

## T003 —— 根的单调性

状态：`PROVED`

如果 \(a\le b\)，则

\[
R_p(a)\le R_p(b).
\]

证明：任何满足 \(k^p\le a\) 的 \(k\)，也一定满足 \(k^p\le b\)。

## T004 —— 坍缩向下收缩

状态：`PROVED`

\[
C_p(n)\le n.
\]

证明：定义直接给出 \(R_p(n)^p\le n\)。

## T005 —— 坍缩幂等

状态：`PROVED`

\[
C_p(C_p(n))=C_p(n).
\]

证明：\(C_p(n)\) 已经是完全 \(p\) 次幂，再应用 T002。

## T006 —— 不动点恰好是完全幂

状态：`PROVED`

\[
C_p(n)=n
\]

当且仅当存在 \(k\in\mathbb N\) 使

\[
n=k^p.
\]

## T007 —— 盆地区间

状态：`PROVED`

\[
C_p(n)=k^p
\]

当且仅当

\[
k^p\le n<(k+1)^p.
\]

因此每一个坍缩盆地都是一个连续整数区间。

## T008 —— 盆地状态数量

状态：`PROVED`

\[
|B_{p,k}|=(k+1)^p-k^p.
\]

当 \(p=2\) 时，

\[
|B_{2,k}|=2k+1.
\]

所以 \(141^2=19881\) 的盆地包含 283 个状态。

## T009 —— 坍缩单调

状态：`PROVED`

如果 \(a\le b\)，则

\[
C_p(a)\le C_p(b).
\]

证明：结合 T003 与 \(\mathbb N\) 上 \(k\mapsto k^p\) 的单调性。

## T010 —— 尺度相容

状态：`PROVED`

对整数底数 \(b\ge2\)，

\[
R_{p,b,s+1}(n)\operatorname{//}b=R_{p,b,s}(n).
\]

证明：令 \(k=R_{p,b,s}(n)\)，则

\[
k^p\le nb^{ps}<(k+1)^p.
\]

两边乘以 \(b^p\) 得

\[
(kb)^p\le nb^{p(s+1)}<((k+1)b)^p.
\]

因此更细尺度的根必定位于从 \(kb\) 到 \((k+1)b-1\) 的整数区间中，而这些整数对 \(b\) 做整数除法后的商都等于 \(k\)。

P008 又给出一个结构性证明：幂映射与“乘以 \(b\)”之间的交换方块跨越右伴随后，直接得到下文 T015 的根/整数除法交换恒等式。

## T011 —— 单侧逆规律

状态：`PROVED`

\[
R_p(k^p)=k,
\]

但一般并不存在

\[
R_p(n)^p=n.
\]

因此整数根在完全幂像集上是完全幂构造的左逆，但在所有自然状态上不是双侧逆。

## T012 —— 确定性前向复合中已经合流的历史不会再次分开

状态：`PROVED`

设

\[
F_t=T_t\circ\cdots\circ T_1.
\]

如果

\[
F_t(x)=F_t(y),
\]

那么

\[
F_{t+1}(x)=F_{t+1}(y).
\]

因此

\[
[x]_t\subseteq[x]_{t+1}.
\]

在有限状态域中，

\[
M_t(x)=|[x]_t|
\]

单调不减。

形式化：集合包含关系与有限状态域上的基数单调性均已分别由 `EnterpriseMath.History.mergedClass_subset_next` 和 `mergedMultiplicity_mono` 通过 Lean 检查。

## T013 —— 整数根按指数乘法复合

状态：`PROVED`

对 \(p,q\ge1\)，

\[
R_{pq}(n)=R_p(R_q(n)).
\]

等价地，

\[
R_{pq}=R_p\circ R_q.
\]

证明：幂映射 \(P_p(k)=k^p\) 与 \(P_q(k)=k^q\) 的右伴随分别是相应整数根。由于

\[
P_q\circ P_p=P_{pq},
\]

右伴随按反序复合。本结论是成熟 Galois connection 理论的应用，不是新的序论原理。

形式化：已由 `EnterpriseMath.Arithmetic.IntegerRoot.root_mul` 在固定 mathlib 版本上通过 Lean 内核检查。

## T014 —— 正整数根的迭代顺序可交换

状态：`PROVED`

对 \(p,q\ge1\)，

\[
R_p(R_q(n))=R_q(R_p(n)).
\]

证明：由 T013 和整数乘法交换律，两边都等于 \(R_{pq}(n)\)。

形式化：已由 `EnterpriseMath.Arithmetic.IntegerRoot.root_mul_comm` 通过 Lean 检查。

## T015 —— 根与整数除法交换恒等式

状态：`PROVED`

对 \(p\ge1\)、\(b\ge1\) 和 \(n\in\mathbb N\)，

\[
R_p(n)\operatorname{//}b
=
R_p\!\left(n\operatorname{//}b^p\right).
\]

若记 \(D_b(n)=n\operatorname{//}b\)，则等价地有

\[
D_b\circ R_p=R_p\circ D_{b^p}.
\]

证明：“乘以 \(b\)”的右伴随是对 \(b\) 的向下整数除法，\(p\) 次幂的右伴随是 \(R_p\)，且

\[
P_p\circ M_b=M_{b^p}\circ P_p.
\]

左伴随上的交换方块传递到右伴随。T010 是其直接特例。

形式化：`EnterpriseMath.Scale.root_div_scale` 已通过 Lean 检查；T010 对应的 `EnterpriseMath.Scale.scaledRoot_succ_div` 也已通过 Lean 检查。

## 验证状态

Python 参考测试在有限范围内计算检查 T001 到 T010。这支持实现正确性，但不是数学证明的来源。

P008 Lean 层固定到明确的 mathlib 版本，并直接复用 Mathlib 已有的 `Nat.nthRoot` 与 Galois connection API。目前 Lean 内核已检查 T001、T002、T004、T005、T006、T010、T012、T013、T014、T015，以及项目面向使用的通用伴随坍缩薄包装。Lean CI 已设置为 warning 即失败。
