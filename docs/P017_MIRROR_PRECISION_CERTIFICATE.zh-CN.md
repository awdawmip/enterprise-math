# P017 Mirror Precision Certificate

状态：`ACTIVE RESEARCH NOTE`  
范围：canonical mirror certificate 的方向化细化与有限精度局域化  
依赖：P017 mirror MC01–MC06 与 P018 有限精度 certificate persistence  
创新性：`NOVELTY_UNVERIFIED`

本文只保留已经验证的 program result。它**不证明** Legendre 猜想。

## 1. MC07 — First moment 的方向化细化

对每个 anchor-surviving radius `r`，令

\[
a_r=|\mathcal P_-(r)|,\qquad b_r=|\mathcal P_+(r)|,
\]

分别表示 lower / upper mirror state 上 transverse small-prime supports 的数量。

canonical MC06 会立刻把 first moment 压缩成

\[
J=\sum_r(a_r+b_r).
\]

MC07 保留两个方向：

\[
J_-:=\sum_r a_r,\qquad J_+:=\sum_r b_r.
\]

令 `S=|S_k|`，定义

\[
U_-:=J_--S,\qquad U_+:=J_+-S.
\]

已有 cross-side slack 为

\[
V=E-J_--J_++S
 =\sum_r(a_r-1)(b_r-1).
\]

若平方盆地 prime-free，则每个 surviving mirror side 都必须 composite，所以

\[
a_r\ge1,\qquad b_r\ge1.
\]

令 `x_r=a_r-1`、`y_r=b_r-1`，则它们均为非负整数，从而

\[
\boxed{U_-\ge0,\quad U_+\ge0,\quad V\ge0}
\]

并且

\[
\boxed{
V=\sum_r x_ry_r
\le
\left(\sum_r x_r\right)
\left(\sum_r y_r\right)
=U_-U_+.
}
\]

所以 prime-free 行为必须满足

\[
\boxed{U_-\ge0,\ U_+\ge0,\ 0\le V\le U_-U_+}.
\]

任意违反都构成 sufficient prime certificate。

### MC07 严格细化 MC06

旧 slack 为 `U=U_-+U_+`。

- 若 `U<0`，至少一侧 directional slack 为负；
- 若 `V<0`，MC07 同样直接检测；
- 若 `4V>U^2` 且 `U_-,U_+>=0`，则

\[
U_-U_+\le\frac{(U_-+U_+)^2}{4}=\frac{U^2}{4}<V.
\]

因此每个 MC06 certificate 都自动是 MC07 certificate。

有限压力测试 `3<=k<=1000` 中，MC06 证出 733 个 root，MC07 证出 740 个；新增 7 个为

`137, 171, 233, 293, 336, 470, 570`。

例如 `k=233` 时

\[
U_-=0,\qquad U_+=4,\qquad V=1,
\]

总量化的 MC06 不给矛盾，而 `V>U_-U_+` 立即给出 certificate。

这些计数只是计算压力测试证据，不是全体 `k` 的定理。

## 2. MC08 — 把 radius 作为有限精度轴

MC07 相当于把全部 surviving radii 放在一个 block 中观察。MC08 把 radius 坐标本身变成有限精度轴。

对 level `m>=0`，用

\[
\boxed{
\beta_m(r)
=
\left\lfloor\frac{(r-1)2^m}{k-1}\right\rfloor
}
\]

把整数坐标 `1<=r<k` 划分为 `2^m` 个嵌套 blocks。

这些 partitions 相容：

\[
\boxed{
\beta_m(r)=\left\lfloor\frac{\beta_{m+1}(r)}2\right\rfloor.
}
\]

对每个非空 surviving-radius block `B`，定义局部 observables

\[
J_-^{(B)}=\sum_{r\in B}a_r,\qquad
J_+^{(B)}=\sum_{r\in B}b_r,
\]

\[
E^{(B)}=\sum_{r\in B}a_rb_r,\qquad S_B=|B|,
\]

以及

\[
U_-^{(B)}=J_-^{(B)}-S_B,\qquad
U_+^{(B)}=J_+^{(B)}-S_B,
\]

\[
V^{(B)}=E^{(B)}-J_-^{(B)}-J_+^{(B)}+S_B.
\]

prime-free 行为要求**每一个 block 分别**满足

\[
\boxed{
U_-^{(B)}\ge0,\quad U_+^{(B)}\ge0,
\quad 0\le V^{(B)}\le U_-^{(B)}U_+^{(B)}.
}
\]

所以任一 block 的违反都能给出 prime certificate。

## 3. Refinement persistence

设一个 parent block 被细分成 children `B_i`，并假设每个 child 都是 admissible。写

\[
X_i=U_-^{(B_i)},\quad Y_i=U_+^{(B_i)},\quad Z_i=V^{(B_i)}.
\]

则 `X_i,Y_i,Z_i>=0` 且 `Z_i<=X_iY_i`。由于这些 observables 对不交 children 可加，

\[
X=\sum_iX_i,\qquad Y=\sum_iY_i,\qquad Z=\sum_iZ_i.
\]

因此

\[
Z\le\sum_iX_iY_i\le
\left(\sum_iX_i\right)\left(\sum_iY_i\right)=XY.
\]

所以 children 全部 admissible 会推出 parent 也 admissible。取逆否命题：

\[
\boxed{
\text{在精度 }m\text{ 已获得 certificate}
\Longrightarrow
\text{所有更高精度仍存在 certificate。}
}
\]

这是 P018 coarse-certificate persistence 在 P017 中的一个直接实例：提高精度可以解决 UNRESOLVED，但不能推翻已经在低精度完成的证明。

## 4. Terminal precision 就是 exact sieve resolution

令

\[
m_{\rm term}(k)=\left\lceil\log_2(k-1)\right\rceil.
\]

到这一层，每个非空 radius block 都是 singleton。对 `B={r}`，

\[
U_-^{(B)}=a_r-1,\qquad U_+^{(B)}=b_r-1.
\]

singleton block 给 certificate，当且仅当至少一侧没有 transverse small-prime witness。结合 anchor survival 与 square-basin root-factor horizon，该侧就是 prime。

因此 terminal MC08 **不是独立的新证明机制**，而是把 exact small-prime detection 写成有限精度语言。

诊断性地定义

\[
m_*(k)=\min\{m:\text{MC08 在 level }m\text{ 给出 certificate}\},
\]

只要搜索中找到该 level。仅仅证明 `m_*(k)` 在 terminal precision 前存在，等价于原来的 prime-existence 目标；真正有数学价值的问题，是从独立的 square-specific structure 推出 `m_*(k)` 的**非平凡 subterminal 上界**。

## 5. 有限精度压力测试

在 `3<=k<=1000` 中，首次在 levels `0,1,2,3,4,5` 获得 certificate 的数量分别为

\[
\boxed{740,\ 98,\ 94,\ 51,\ 14,\ 1.}
\]

使用 `1,2,4,8,16,32` 个 radius blocks 时，累计覆盖为

\[
\boxed{740,\ 838,\ 932,\ 983,\ 997,\ 998.}
\]

唯一第一次需要 level 5 的是 `k=982`。

这**不表示** 32 blocks 全局足够。固定反例

\[
k=2896
\]

在 level 5 没有 certificate，而 level 6 才出现。更大范围压力测试同样显示所需精度会增长。

因此经验结论只能是：很多 basin 会远早于 singleton resolution 完成证明，值得把 `m_*(k)` 当作新的定量研究量；不能从有限样本跳成 bounded-32 theorem。

## 6. 已主动淘汰的路线

- same-side second moments 加 Cauchy bound，在 `k<=1000` 没有产生任何 MC07 之外的新 certificate，因此不继续无结构 moment expansion；
- 一个曾经覆盖全部 MC06 residuals 的 least-factor-gated CRT union 被判定为循环：在 exact cofactor ordering 下，它重新构造了完整 composite-composite detection；
- terminal MC08 绝不能作为 Legendre 证明报告，因为它就是 exact sieve resolution。

## 7. 实现

Canonical replay 资产：

- `src/enterprise_math/p017_mirror_directional.py`；
- `tests/test_p017_mirror_directional.py`。

MC07 保留 mirror program 已有的方向化 Möbius/CRT observables。MC08 在嵌套 radius blocks 上用 modular incidence marking 计算同一组 support counts，不调用通用整数分解函数。

下一个硬问题，是把所需精度 `m_*(k)` 与独立 canonical P017 结构——例如 L052 stable root-channel separation、L053 full-core capacity 或 L054 exact cofactor-window separation——发生真实耦合，并证明 subterminal bound，而不是把 exact sieve 换一种语言重述。
