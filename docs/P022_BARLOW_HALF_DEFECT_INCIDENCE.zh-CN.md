# P022 — support-localized Franel defect incidence

状态：`ACTIVE RESEARCH NOTE / EXACT DECOMPOSITION + NEGATIVE BOUNDARY`  
Owner：`program/p022-geometry-v2`  
依赖：central-binomial A-elimination、integer midpoint companion、Franel zero alphabet

## 1. 精确 valuation 分解

令 `p` 为任意强制中点素数 `p=5 或 7 (mod 8)`，并假定 `p-2` 为合数，记

\[
m=(p-1)/2.
\]

将 canonical A-elimination 写成

\[
A_m=\prod_{j<m}A_j^{\alpha_j},
\]

对应 pure Franel defect 为

\[
D_m=F_m\Big/\prod_{j<m}F_j^{\alpha_j}.
\]

则恒有

\[
\boxed{
v_p(D_m)=v_p(F_m)-\sum_{j<m}\alpha_jv_p(F_j).}
\]

这里不需要任何独立性假设。

## 2. P022-LI37 — support-localized zero signature

在 forced-midpoint window 内，integer companion 给出

\[
p\mid F_j
\iff
p\mid H_{m-j}.
\]

所以一切**可能产生 correction 的位置**恰好是 incidence set

\[
\boxed{
I_p=\{(j,m-j,\alpha_j):\alpha_j\ne0,\ p\mid H_{m-j}\}.}
\]

对“support 是否避开 zero”这个 yes/no future query，完整 Franel zero alphabet 可以合法压缩成它与 canonical A-support 的交集。

若要精确得到 defect valuation，则还必须保留这些命中位置上的 `v_p(F_j)`。zero-set cardinality、first-zero rank 或全局 p-Lucas basin density 都不能替代这一 positional state。

## 3. P022-LI38 — `p=157` 的精确 cancellation

`157` 是 forced-midpoint prime，且 `157-2=155` 为合数，

\[
m=78.
\]

canonical A-support 中有

\[
\alpha_{16}=+1,
\]

而 integer companion 检出

\[
157\mid H_{62}
\iff
157\mid F_{16}.
\]

直接 valuation 为

\[
v_{157}(F_{78})=1,
\qquad
v_{157}(F_{16})=1.
\]

其余 support 项的 `157`-valuation 均为零，因此

\[
\boxed{v_{157}(D_{78})=1-1=0.}
\]

这给出 forced midpoint 本身不足以形成可用 defect witness 的 canonical negative boundary。

## 4. P022-LI39 — zero-alphabet 的大小不足以决定 defect

两个 prime 可以具有完全相同的 zero-alphabet cardinality，却产生相反的 half-defect 结果。

对 `p=157`：

\[
Z_{157}=\{16,75,78,81,140\},
\qquad |Z_{157}|=5,
\]

support 命中 `16`，得到 `v_157(D_78)=0`。

对 `p=389`：

\[
Z_{389}=\{25,176,194,212,363\},
\qquad |Z_{389}|=5,
\]

但 canonical A-support 与这些 midpoint 以下 zeros 完全不相交；并且

\[
v_{389}(F_{194})=1,
\]

所以

\[
\boxed{v_{389}(D_{194})=1.}
\]

因此

\[
\boxed{|Z_p|\not\Rightarrow\text{half-defect survival}.}
\]

决定结果的是 hidden zero information 相对于 declared elimination support 的**位置关系**。

## 5. 精度含义

这是 P023“future computation 决定合法 quotient”的一个非常具体的 P022 specialization：

- 只问 p-Lucas basin 大小时，`z_p=|Z_p|` 可以足够；
- 只问 half-defect support avoidance 时，只需保留 `Z_p intersect supp(alpha)`；
- 要问 exact defect valuation，则需保留 support-localized weighted signature
  \[
  \{(j,\alpha_j,v_p(F_j)):v_p(F_j)>0\}.
  \]

因此一个看起来更“全局”的标量统计，可能严格不如一个更小但与未来 relation 对齐的位置 signature。

## 6. 可执行资产

- `src/enterprise_math/p022_barlow_half_defect_incidence.py`
- `tests/test_p022_barlow_half_defect_incidence.py`

测试同时包含 `p=157` cancellation、`p=173` early-zero 但不命中 support 的负边界，以及 target family 的 no-hit regression。
