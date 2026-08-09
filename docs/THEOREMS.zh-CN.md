# v0.1 已证明命题

本文件中的状态表示普通数学证明已经从 v0.1 定义推出结论。只有下文明确标注的命题才表示已经通过 Lean 形式化检查。

规范范围约定以 `FOUNDATIONS` 为准：\(\mathbb N=\mathbb N_0=\{0,1,2,\ldots\}\)，而 \(\mathbb N_{>0}\) 表示正整数。物理上非平凡的原始根/坍缩族从 \(p\ge2\) 开始；本定理目录在规律仍然成立时使用完整的正指数代数 \(p\ge1\)，其中恒等成员为 \(R_1=C_1=\operatorname{id}\)。

## T001 —— 根刻画

状态：`PROVED`

对 \(p\ge1\)，

\[
R_p(n)=k\iff k^p\le n<(k+1)^p.
\]

这与定义中的最大值性质等价。

形式化：已由 `EnterpriseMath.IntegerRoot.root_eq_iff` 通过 Lean 检查。

## T002 —— 完全幂精确性

状态：`PROVED`

\[
R_p(k^p)=k.
\]

证明：\(k^p\le k^p<(k+1)^p\)，应用 T001 即可。

形式化：已由 `EnterpriseMath.IntegerRoot.root_pow` 通过 Lean 检查。

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

形式化：已由 `EnterpriseMath.IntegerRoot.collapse_le` 通过 Lean 检查。

## T005 —— 坍缩幂等

状态：`PROVED`

\[
C_p(C_p(n))=C_p(n).
\]

证明：\(C_p(n)\) 已经是完全 \(p\) 次幂，再应用 T002。

形式化：已由 `EnterpriseMath.IntegerRoot.collapse_idempotent` 通过 Lean 检查。

## T006 —— 不动点恰好是完全幂

状态：`PROVED`

\[
C_p(n)=n
\]

当且仅当存在 \(k\in\mathbb N_0\) 使

\[
n=k^p.
\]

特别地，\(0\) 被明确包含，并且对每个正指数都是不动点。

形式化：已由 `EnterpriseMath.IntegerRoot.collapse_eq_self_iff` 通过 Lean 检查。

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

所以 \(141^2=19881\) 的盆地包含 283 个状态。对代数恒等情形 \(p=1\)，每个盆地的基数都是 \(1\)。

## T009 —— 坍缩单调

状态：`PROVED`

如果 \(a\le b\)，则

\[
C_p(a)\le C_p(b).
\]

证明：结合 T003 与 \(\mathbb N_0\) 上 \(k\mapsto k^p\) 的单调性。

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

P008/P014 还通过下文 T015 给出结构性证明。形式化：已由 `EnterpriseMath.Scale.scaledRoot_succ_div` 通过 Lean 检查。

## T011 —— 单侧逆规律

状态：`PROVED`

\[
R_p(k^p)=k,
\]

但对非平凡指数 \(p\ge2\)，一般并不存在

\[
R_p(n)^p=n.
\]

因此当 \(p\ge2\) 时，整数根在完全幂像集上是完全幂构造的左逆，但在所有自然状态上不是双侧逆；当 \(p=1\) 时，两边都是恒等映射。

## T012 —— 确定性前向复合中已经合流的历史不会再次分开

状态：`PROVED`

采用规范时间约定

\[
F_0=\operatorname{id},
\qquad
F_{t+1}=T_t\circ F_t,
\]

等价地，对 \(t\ge1\)，

\[
F_t=T_{t-1}\circ\cdots\circ T_0.
\]

如果

\[
F_t(x)=F_t(y),
\]

那么

\[
F_{t+1}(x)=T_t(F_t(x))=T_t(F_t(y))=F_{t+1}(y).
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

右伴随按反序复合。本结论使用的是成熟 Galois connection 理论，而不是新的序论原理。

形式化：已由 `EnterpriseMath.IntegerRoot.root_mul` 通过 Lean 检查。

## T014 —— 正整数根的迭代顺序可交换

状态：`PROVED`

对 \(p,q\ge1\)，

\[
R_p(R_q(n))=R_q(R_p(n)).
\]

证明：由 T013 和整数乘法交换律，两边都等于 \(R_{pq}(n)\)。

形式化：已由 `EnterpriseMath.IntegerRoot.root_mul_comm` 通过 Lean 检查。

## T015 —— 根与整数除法交换恒等式

状态：`PROVED`

对 \(p\ge1\)、\(b\ge1\) 和 \(n\in\mathbb N_0\)，

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

形式化：已由 `EnterpriseMath.Scale.root_div_comm` 通过 Lean 检查；T010 对应的 `EnterpriseMath.Scale.scaledRoot_succ_div` 也已通过 Lean 检查。

## 验证状态

Python 参考测试在有限范围内计算检查原始算术规律；这些计算支持实现正确性，但不是数学证明来源。

当前固定版本的 Lean/mathlib 层在 CI 中以 warnings fatal 编译。它已经由 Lean 内核检查 T001、T002、T004、T005、T006、T010、T013、T014、T015。T003、T007、T008、T009、T011、T012 仍是普通已证明命题，等待后续独立形式化提升。
