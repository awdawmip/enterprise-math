# A3 Guard-Image Lattice 补充 01 —— Rank-One Hidden Guard 的精确 Branch Reachability

状态：`RESEARCH WIP / EXACT INTEGER ARITHMETIC-LINE SOLVER`

## 1. 问题

主文把 multi-guard hidden score geometry 写成：

\[
L_G=W(K_A)\subseteq\mathbb Z^r.
\]

已知：

- rank 0：所有 guards 可见；
- full rank `r`：每个 coarse fiber 命中全部 strict orthants；
- partial rank 不能只看 rank。

本补充解决 partial-rank 的第一个完整非平凡层：

\[
\boxed{\operatorname{rank}L_G=1.}
\]

## 2. Rank-one lattice 的 canonical step

任意 rank-one integer subgroup 都可唯一写成：

\[
L_G=\mathbb Z h,
\]

其中 `h` 取第一非零坐标为正的 canonical generator。

从任意 generator family：

\[
v_1,\ldots,v_d\in\mathbb Z^r
\]

构造：

1. 取一个非零 `v`；
2. 除以其 coordinates 的 gcd，得到 primitive direction `p`；
3. 每个 `v_i=t_i p`，取：
   \[
   d=\gcd_i|t_i|;
   \]
4. 得：
   \[
   \boxed{h=d p.}
   \]

全程只有 gcd 与 exact integer division。

## 3. 一个 coarse fiber 就是一条整数等差线

固定 coarse fiber 中某个 fine representative，其 guard-score vector 为：

\[
g\in\mathbb Z^r.
\]

该 fiber 的所有 guard scores 恰为：

\[
\boxed{g+t h,\qquad t\in\mathbb Z.}
\]

因此 branch reachability 从 lattice problem 降成一个单整数参数问题。

## 4. A3-G06 —— threshold pattern = integer interval

每个 guard 使用同一二元 threshold convention：

- `True`：score `>=0`；
- `False`：score `<0`，等价于整数 score `<=-1`。

对第 `j` 个 guard：

\[
g_j+t h_j.
\]

若要求 `True`：

- `h_j>0` 给出一个 lower bound；
- `h_j<0` 给出一个 upper bound；
- `h_j=0` 时由 `g_j` 直接判定恒真/不可达。

若要求 `False`，上下界方向相反。

把所有 guards 的 bounds 求交：

\[
\boxed{
\{t\in\mathbb Z:\text{branch pattern holds}\}
=[L,U]\cap\mathbb Z,
}
\]

其中 `L/U` 可以一侧无界；若 `L>U` 则 pattern 不可达。

所以：

> **rank-one hidden multi-guard 的全部 branch reachability 可以用一个整数 interval 精确表示。**

不枚举 fine states，也不需要 ILP solver。

## 5. Rank 相同不代表 pattern 相同

例如 base score `g=(0,0)`。

### diagonal step

\[
h=(1,1).
\]

两个 guard 同向变化。

### anti-diagonal step

\[
h=(1,-1).
\]

两个 guard 反向变化。

二者 hidden rank 都为 1，但 reachable threshold patterns 不同。

所以主文 G05 的负边界被 executable solver 精确化：

\[
\boxed{
\text{partial hidden precision 需要 lattice direction，不能只保存 rank。}
}
\]

## 6. 对 piecewise quotient 的含义

若每个 branch affine map 已 individually descend，则 rank-one 情形不需要比较所有 `2^r` branch effects。

对给定 coarse state，只需：

1. 计算 base scores `g`；
2. 用 `(g,h)` 求 reachable branch-pattern set；
3. 要求这些**实际可达** branches 的 coarse effects 相同。

与 full-rank 情形相比，这可以显著降低所需精度，因为某些 branch identities 在任何 fine lift 中都不可达，根本不应成为保存 obligation。

注意：reachable pattern set 可以依赖 coarse state 的 base scores `g`。所以 general coarse piecewise program 可能需要保留一个 state-dependent reachable-branch description，而不是一个全局 pattern mask。

## 7. 实现

`guard_image_lattice.py` 新增：

- `rank_one_lattice_step`；
- `guard_rank_one_step`；
- `rank_one_threshold_pattern_interval`；
- `rank_one_threshold_pattern_reachable`。

测试把闭式 interval 与 bounded brute-force arithmetic-line enumeration 逐项比较，并保存 diagonal / anti-diagonal 同 rank 不同 pattern 的反例。

## 8. 下一步

下一个尚未解决的区间是：

\[
1<\operatorname{rank}L_G<r.
\]

优先不做通用黑箱求解，而先研究 rank 2：

1. 用整数 basis / Hermite normal form 把 affine lattice 写成二维参数；
2. 把每个 sign pattern 转成二维 integer half-plane feasibility；
3. 寻找是否存在固定维 `r` 下的有限 certificate；
4. 只在必要时引入一般 Presburger/ILP 工具，并把它们明确作为成熟前人算法，而不是 A3 新本体。
