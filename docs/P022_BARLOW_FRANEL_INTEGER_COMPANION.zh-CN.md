# P022 — Franel 中点伴随序列的纯整数标准形

状态：`ACTIVE RESEARCH NOTE / EXACT NORMALIZATION / SAME MIDPOINT-COMPANION FAMILY`  
Owner：`program/p022-geometry-v2`  
依赖：`P022_BARLOW_FRANEL_MIDPOINT_OFFSET`  
边界：这是同一中点伴随定理族的整数化，不是第二个母定理。

## 1. 回顾有理 companion

对强制中点素数 `p = 5 或 7 (mod 8)`，令

\[
m=(p-1)/2.
\]

已有结果定义

\[
G_0=0,\qquad G_1=1,
\]

并满足

\[
8(2d+1)^2G_{d+1}
=(2d-1)^2G_{d-1}-(28d^2+1)G_d,
\]

以及

\[
F_{m-d}\equiv G_dF_{m-1}\pmod p
\qquad(0\le d<m).
\]

## 2. P022-LI30 — 纯整数 companion

对 `d>=1` 定义

\[
S_d=8^{d-1}((2d-1)!!)^2,
\qquad
H_d=S_dG_d,
\]

并令 `H_0=0`。

利用

\[
\frac{S_{d+1}}{8(2d+1)^2}=S_d,
\qquad
\frac{S_d}{S_{d-1}}=8(2d-1)^2,
\]

有理递推变成

\[
\boxed{
H_{d+1}
=-(28d^2+1)H_d
+8(2d-1)^4H_{d-1}.}
\]

初值为

\[
H_0=0,\qquad H_1=1,
\]

因此递推本身就归纳证明全部 `H_d` 都是整数。

前几项为

\[
0,1,-29,3925,-1138025,586364625,-470774258325,\ldots
\]

## 3. P022-LI31 — 一个整数递推重建全部 zero geometry

若 `0<d<m`，则 `S_d` 的所有素因子都严格小于 `p`，所以

\[
p\nmid S_d.
\]

因此乘上 `S_d` 不改变模 `p` 的零判定：

\[
\boxed{
p\mid F_{m-d}\iff p\mid H_d.}
\]

于是所有强制中点 prime 的整个左半 Franel zero alphabet，都统一变成固定整数序列 `H_d` 的素因子问题。

这一步把分数约分和模逆运算都从 zero query 中消掉了。

## 4. P022-LI32 — 可逆二维 transfer

写成

\[
\binom{H_{d+1}}{H_d}
=
T_d
\binom{H_d}{H_{d-1}},
\qquad
T_d=
\begin{pmatrix}
-(28d^2+1)&8(2d-1)^4\\
1&0
\end{pmatrix}.
\]

则

\[
\boxed{\det T_d=-8(2d-1)^4.}
\]

对 `d<m`，该 determinant 模 `p` 可逆，因此 companion 在整个强制中点窗口内都是一个可逆的二维有限状态演化。

取初值 `(0,1)` 与 `(1,0)` 的两个独立解，其 Casoratian 为

\[
\boxed{
W_d=(-8)^d((2d-1)!!)^4.}
\]

所以在合法窗口内，两维状态不会因为 transfer 本身奇异而同时丢秩。

## 5. 含义与边界

因此 `p|H_d` 不是某一步 transfer 奇异造成的信息坍缩，而是在可逆二维动力中真实穿过第一坐标零层的事件。

这对 P018/P023 的 defect/precision 语言有借鉴价值，但该递推仍是 P022/Franel specialization；这里不宣称一般 Foundation 母定理。

## 6. 可执行资产

- `src/enterprise_math/p022_barlow_franel_integer_companion.py`
- `tests/test_p022_barlow_franel_integer_companion.py`

回归测试核验：与有理 companion 的精确标准化、forced-prime zero alphabet 重建、transfer determinant 以及 Casoratian 乘积恒等式。
