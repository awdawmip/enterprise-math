# P022 — Barlow 检查点精度与高阶碰撞权衡

状态：`ACTIVE RESEARCH NOTE / EXACT FINITE COMBINATORICS / NOVELTY UNVERIFIED`  
归属：`program/p022-geometry-v2`  
依赖：P011 碰撞谱；P022 Barlow selected-layer 精度

## 1. 设定

长度 `N` 的 microscopic stacking word 为

\[
\sigma\in\{-1,+1\}^N.
\]

未来语言只在

\[
0<k_1<\cdots<k_m\le N
\]

读取 prefix imbalance。令受约束段长度为

\[
\ell_1=k_1,
\qquad
\ell_j=k_j-k_{j-1},
\]

末尾未观察 tail 为

\[
u=N-k_m.
\]

长度 `ell` 的一段在 imbalance `2j-ell` 上的 fiber 大小为

\[
\binom{\ell}{j}.
\]

## 2. P022-HC01 — 相同 observation 的有序高阶元组数精确因子化

定义

\[
\boxed{F_r(\ell)=\sum_{j=0}^{\ell}\binom{\ell}{j}^r.}
\]

若 `M_r` 表示得到完全相同 selected-layer observation 的有序 microscopic `r`-tuple 数，则独立 segment 与未观察 tail 给出

\[
\boxed{
M_r=2^{ru}\prod_{j=1}^{m}F_r(\ell_j).
}
\]

`r=2` 时，由 Vandermonde 恒等式

\[
F_2(\ell)=\binom{2\ell}{\ell}.
\]

`r=3` 对应经典 Franel 数；更高阶属于 generalized binomial power sums。上述对象本身属于既有组合数学，本项目不主张发明这些序列。

## 3. P022-HC02 — 完整 P011 collision spectrum 由 Stirling 变换得到

P011 定义

\[
J_k=\sum_y\binom{m_y}{k}.
\]

利用 falling factorial

\[
(m)_k=\sum_{r=0}^{k}s(k,r)m^r
\]

可得

\[
\boxed{
J_k
=
\frac1{k!}
\sum_{r=1}^{k}s(k,r)M_r.
}
\]

故

\[
\boxed{
J_k
=
\frac1{k!}
\sum_{r=1}^{k}
 s(k,r)2^{ru}\prod_jF_r(\ell_j).
}
\]

因此 selected-layer Barlow quotient 的完整有限 P011 collision spectrum 可仅由 segment lengths 计算，无需枚举 `2^N` 条 microscopic histories。

## 4. P022-HC03 — 普通 balanced schedule 同时优化 image size 与 J2

要求最终层 `N` 被观察，故 `u=0`，并固定 checkpoint 数 `m`。

observation image size 为

\[
|\operatorname{im}O|=\prod_j(\ell_j+1).
\]

若 `a>=b+2`，将 `(a,b)` 平衡为 `(a-1,b+1)`，image factor 增量为

\[
a(b+2)-(a+1)(b+1)=a-b-1>0.
\]

另一方面

\[
M_2=\prod_j\binom{2\ell_j}{\ell_j},
\]

且中央二项式相邻比

\[
\frac{\binom{2n}{n}}{\binom{2n-2}{n-1}}
=4-\frac2n
\]

严格递增，故同一 balancing exchange 严格降低 `M_2`，进而严格降低 `J_2`。

若

\[
N=qm+r,
\qquad0\le r<m,
\]

最优 segment multiset 为 `m-r` 个 `q` 和 `r` 个 `q+1`，并有

\[
\boxed{|\operatorname{im}O|_{\max}=(q+1)^{m-r}(q+2)^r.}
\]

所以近均匀检查点不是经验规则，而是同时最大化 image、最小化 pair ambiguity 的精确有限最优解。

## 5. P022-HC04 — balanced 并不最小化完整 collision spectrum

最小反例：

\[
N=4,\qquad m=2.
\]

balanced `(2,2)` 的 fiber multiset 为

\[
\{1,1,1,1,2,2,2,2,4\},
\]

故

\[
(J_1,J_2,J_3,J_4)=(16,10,4,1).
\]

unbalanced `(1,3)` 的 fiber multiset 为

\[
\{1,1,1,1,3,3,3,3\},
\]

故

\[
(J_1,J_2,J_3,J_4)=(16,12,4,0).
\]

因此 balanced 在 `J_2` 上更优，却在 `J_4` 上更差。完整 P011 spectrum 不存在由同一 schedule 逐分量统一最小化的简单结论。

## 6. 无限族：pair ambiguity 与 four-way collision 的结构性冲突

对任意 `m>=2`，取

\[
N=m+2.
\]

比较

\[
(2,2,1,\ldots,1)
\]

与

\[
(3,1,\ldots,1).
\]

前者 fiber profile 有

\[
c_1=2^m,\quad c_2=2^m,\quad c_4=2^{m-2},
\]

后者有

\[
c_1=2^m,\quad c_3=2^m.
\]

因此

\[
J_2^{bal}=5\cdot2^{m-1}<3\cdot2^m=J_2^{con},
\]

\[
J_3^{bal}=J_3^{con}=2^m,
\]

但

\[
J_4^{bal}=2^{m-2}>0=J_4^{con}.
\]

所以该冲突是一整族结构，不是 `N=4` 的偶然现象。

## 7. P022-HC05 — 最短 balancing exchange 的 power-moment 相变

对 `(1,3)->(2,2)`，精确差值为

\[
\boxed{
F_r(2)^2-F_r(1)F_r(3)
=4\left(4^{r-1}+2^r-3^r\right).
}
\]

它在 `r=1` 为 0，在 `r=2,3,4` 为负，而从 `r=5` 起对所有 `r` 均为正。

因此 balancing 对低阶 moment 有利，却从第五阶开始反向增加这一 power moment。不能把 `r=2` 的 log-convex exchange 机械推广到全部高阶统计。

## 8. 精度含义

同一 microscopic state space 上至少存在多个合理目标：

- 最大化可区分 coarse states；
- 最小化 `J_2`；
- 抑制高阶 `J_k`；
- 保留指定的 fiber-size profile 特征。

这些目标对 schedule 的偏序并不一致。因此在这一有限模型中，`precision` 不能退化为 checkpoint density；它必须由未来真正需要的 collision language 决定。

## 9. 可执行资产

- `src/enterprise_math/p022_barlow_higher_collision_precision.py`；
- `tests/test_p022_barlow_higher_collision_precision.py`。

测试以直接 finite fiber enumeration 交叉验证高阶 tuple moments、Stirling 变换、balanced 的 image/J2 最优性，以及上述完整 spectrum 反例与无限族。