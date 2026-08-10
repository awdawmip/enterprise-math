# P022 — Franel p-Lucas 整除盆地

状态：`ACTIVE RESEARCH NOTE / EXACT DIGIT COUNT / PRIOR-ART INPUT EXPLICIT`  
Owner：`program/p022-geometry-v2`  
依赖：Franel p-Lucas 分解；半指标见证定理  
跨路线相关：P011 collision fibers；P018/P023 predictive quotients；P024 observation-language precision

## 1. 设置

对素数 `p` 定义 Franel digit-zero set

\[
Z_p=\{1\le d\le p-1:F_d\equiv0\pmod p\},
\qquad
z_p=|Z_p|.
\]

Franel 数的 p-Lucas 分解表明：若

\[
N=n_0+n_1p+\cdots+n_{L-1}p^{L-1},
\qquad0\le n_i<p,
\]

则

\[
\boxed{
F_N\equiv\prod_{i=0}^{L-1}F_{n_i}\pmod p.
}
\]

该 p-Lucas 性质属于 Franel / generalized Apéry sequence 的已有数学。P022 在这里把它解释成一个精确的有限状态计数律。

---

## 2. P022-LI15 — 完整 base-p block 的精确计数

因为

\[
F_0=1,
\]

base-`p` 的一个 digit 恰在属于 `Z_p` 时产生零因子。

因此

\[
p\nmid F_N
\]

当且仅当 `N` 的**每一个** base-`p` digit 都避开 `Z_p`。

在完整区间

\[
0\le N<p^L
\]

中共有 `L` 个独立 digit positions，每个位置恰有

\[
p-z_p
\]

个不会产生零的 digit。故

\[
\boxed{
\#\{0\le N<p^L:p\nmid F_N\}
=(p-z_p)^L.
}
\]

等价地，

\[
\boxed{
\#\{0\le N<p^L:p\mid F_N\}
=p^L-(p-z_p)^L.
}
\]

这对每个 `L>=0` 都是精确整数恒等式。

---

## 3. P022-LI16 — Franel 素数整除的 p-Lucas 零—一律

只存在两种情况。

### Type I：没有 zero digit

若

\[
Z_p=\varnothing,
\]

则 p-Lucas 直接推出

\[
\boxed{p\nmid F_N\quad\text{对所有 }N\ge0.}
\]

也就是说，一个素数若没有出现在第一层 digit table `F_1,...,F_(p-1)` 中，以后整个 Franel sequence 都不会出现它。

### Type II：至少有一个 zero digit

若

\[
z_p\ge1,
\]

则一个完整 `p^L` block 中非零项的比例恰为

\[
\left(1-\frac{z_p}{p}\right)^L,
\]

它随 digit depth 指数趋于 0。因此

\[
\boxed{
\frac{\#\{0\le N<p^L:p\mid F_N\}}{p^L}
\longrightarrow1.
}
\]

再用相邻两个 `p` 的幂之间的 digit 上界即可得到完整自然密度存在且为 1：

\[
\boxed{
\operatorname{dens}\{N\ge0:p\mid F_N\}=1.
}
\]

因此 Franel 的固定素数整除具有一个尖锐的 p-Lucas 二分：

\[
\boxed{
\text{永远不出现}
\quad\text{或}\quad
\text{在密度 1 的指标集合上出现}.}
\]

这里说的是**固定 prime**、令指标趋于无穷的整除频率。

---

## 4. P022-LI17 — 强制半指标素数生成 density-one basin

上一条半指标定理证明：若

\[
p\equiv5,7\pmod8,
\]

则

\[
\frac{p-1}{2}\in Z_p.
\]

因此

\[
z_p\ge1,
\]

LI16 立即给出

\[
\boxed{
\operatorname{dens}\{N:p\mid F_N\}=1
\qquad(p\equiv5,7\pmod8).}
\]

即便只使用那个被强制存在的 midpoint digit，也已经得到有限尺度下界

\[
\boxed{
\#\{0\le N<p^L:p\mid F_N\}
\ge p^L-(p-1)^L.}
\]

如果还存在其他 zero digits，则 LI15 的精确计数更强。

例如

\[
Z_{29}=\{12,14,16\}.
\]

所以每个 `29^L` block 中，

\[
\boxed{
\#\{N<29^L:29\nmid F_N\}=26^L,
}
\]

而不是仅得到 `28^L` 的粗上界。

---

## 5. 镜像对称进一步限制 digit basin

Jarvis--Verrill 给出

\[
F_d\equiv0\pmod p
\iff
F_{p-1-d}\equiv0\pmod p.
\]

因此 `Z_p` 关于反射对称。

当 `p≡5,7 mod 8` 时，中点 `(p-1)/2` 是一个固定零位，其他零位只能成镜像对出现，因此

\[
\boxed{z_p\text{ 为奇数}.}
\]

最小情况是 `z_p=1`；`p=29` 则展示了更大的奇数 zero alphabet。

---

## 6. 对 primitive divisor 的重新理解

`F_n` 的 primitive prime divisor 只是其 p-Lucas basin 的**第一次开启事件**。

一旦素数 `p` 首次在 `r_p` 出现，之后所有 base-`p` 表示中包含 `Z_p` 任一 digit 的整数指标，其 Franel 数都被 `p` 整除。

因此 primitive marker 并不意味着以后会保持“私有”。这也解释了为什么长度 150 证书中的 finite private-marker rows 极其有效，但 p-Lucas 又保证这些 prime 最终必然复现。

正确区分是

\[
\boxed{
\text{首次出现信息}
\neq
\text{长期整除频率}.}
\]

---

## 7. 精度解释

这是一个非常干净的“小状态控制无限未来语言”的例子。

固定 `p` 后，整个未来 observable

\[
N\longmapsto\mathbf1_{p\mid F_N}
\]

只需要有限集合 `Z_p` 就能完全决定；不必保存未来巨大的 Franel 整数，只需读取 `N` 的 base-`p` digits 并判断是否有 digit 落在 `Z_p`。

因此 p-Lucas quotient 把无限数列问题精确压缩成有限状态语言识别：

\[
\boxed{
\text{finite zero-digit set}
\to
\text{exact infinite divisibility language}.}
\]

这是 P022 中 task-relative future-compatible state compression 的一个 specialization。若要提升成一般 automaton / quotient 母定理，应由 A2/P023 owner 负责，而不在 P022 重复造母理论。

---

## 8. Prior-art / novelty 边界

已有数学包括 Lucas 定理以及 Franel/generalized Apéry sequences 的 p-Lucas factorization。

P022 特定贡献，是把它在当前 Franel-defect / precision 路线中改写成精确 block-count 与 density 结构，并与新的强制半指标 witness family 结合。

这一组合的历史新颖性仍为 `NOVELTY_UNVERIFIED`。

## 9. 可执行资产

更新/新增：

- `src/enterprise_math/p022_barlow_franel_lucas_rank.py`；
- `tests/test_p022_barlow_franel_lucas_rank.py`。

实现只使用整数 Franel 数与 base-`p` digit products。测试核验小尺度 p-Lucas 分解，以及 `p=5`、`p=29` 的精确 block counts。
