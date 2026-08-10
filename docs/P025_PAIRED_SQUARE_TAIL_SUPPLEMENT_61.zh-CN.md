# P025 补充 61 —— 成对 residual 压力与双平方因子尾界

状态：`ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation：`program/p025-paired-square-tail-stage61`  
基线：冻结的 Stage-60 语义头 `ff04a826c5ea87c28f769cb378d8189687e686b0`  
依赖：P025 补充 47、50  
Hard block：`NONE`

## 1. Stage 50 丢掉了仍可利用的加法信息

Stage 50 从失败的循环 Projective Capacity Condition 项

\[
\frac{m(n_i)}{K_{jk}}\ge c^\eta
\]

出发，只保留 `K_jk>=1`，因而只得到一个大的 multiplicity residual。

对于非 unit 的 primitive 关系

\[
a+b=c,\qquad a,b>1,
\]

加法结构实际上更强：分母含有另一个 component 的 radical，而这个 radical 可以与一个大的互补 component 的 residual 精确抵消。

因此会得到一个双 component 压力定理。

## 2. P025-T126 —— 每个非 unit PCC failure 都强迫一个大的 residual 对

固定有理指数

\[
\eta=p/q,\qquad0<p<q.
\]

假设 `PCC_eta` 失败。

三个循环 projective ratio 为

\[
\rho_c=\frac{m(c)}{K_{ab}},\qquad
\rho_b=\frac{m(b)}{K_{ac}},\qquad
\rho_a=\frac{m(a)}{K_{bc}}.
\]

至少一个不小于 `c^eta`。

### 情形 1：`c`-oriented 项失败

令 `j` 为 `a,b` 中较大的一个，因此

\[
j\ge c/2.
\]

由于两个互补 block 都非 unit，

\[
K_{ab}=R_b C(a)+R_a C(b)\ge R_j,
\]

其中 `R_j=rad(j)`，每个非 unit block 的 capacity 至少为 1。

于是

\[
m(c)\ge c^\eta R_j.
\]

另一方面

\[
m(j)=\frac j{R_j}\ge\frac c{2R_j}.
\]

两式相乘后互补 radical 消失：

\[
\boxed{m(c)m(j)\ge\frac12c^{1+\eta}.}
\]

### 情形 2：`a`- 或 `b`-oriented 项失败

例如若 `rho_a>=c^eta`，则

\[
K_{bc}\ge R_c,
\]

从而

\[
m(a)\ge c^\eta R_c.
\]

又因为 `m(c)=c/R_c`，所以

\[
\boxed{m(a)m(c)\ge c^{1+\eta}.}
\]

`b` 的情形完全相同。

因此每个非 unit PCC failure 都存在不同 components `x,y` 使

\[
\boxed{m(x)m(y)\ge\frac12c^{1+\eta}.}
\]

这严格强化了 Stage 50 的单 component 结论。

## 3. P025-T127 —— 两个平方因子根的乘积必须很大

定义

\[
q_2(n)=\prod_p p^{\lfloor v_p(n)/2\rfloor}.
\]

Stage 50 已证明

\[
q_2(n)^2\ge m(n).
\]

因此 P025-T126 给出的两个 components 满足

\[
(q_2(x)q_2(y))^2
\ge m(x)m(y)
\ge\frac12c^{1+\eta}.
\]

故

\[
\boxed{
q_2(x)q_2(y)
\ge
\frac1{\sqrt2}c^{(1+\eta)/2}.
}
\]

所以 projective failure 实际需要两个平方因子方向共同承担压力，而不只是一个大平方因子。

## 4. P025-T128 —— 初等 dyadic 双平方尾界

限制在

\[
X/2<c\le X.
\]

当 `eta=p/q` 时，令 `Y=Y_{p/q}(X)` 为满足

\[
\boxed{2^{2q+p}Y^{2q}\ge X^{q+p}}
\]

的最小正整数。

那么每个非 unit PCC failure 都有两个 component square-root divisors `s,t` 满足

\[
st\ge Y.
\]

component 对一共有三种。固定一组 labelled component pair 与固定 `s,t` 后，两个 component 的候选值数至多为

\[
\left\lfloor\frac X{s^2}\right\rfloor
\left\lfloor\frac X{t^2}\right\rfloor.
\]

加法关系只会继续减少这个数量。因此

\[
N^{\rm nonunit}_{\rm fail}(X)
\le
3\sum_{\substack{s,t\le\sqrt X\\st\ge Y}}
\left\lfloor\frac X{s^2}\right\rfloor
\left\lfloor\frac X{t^2}\right\rfloor.
\]

又有经典初等尾估计

\[
\sum_{st\ge Y}\frac1{s^2t^2}
\ll\frac{\log(2Y)}Y.
\]

而

\[
Y\asymp_\eta X^{(1+\eta)/2},
\]

故

\[
\boxed{
N^{\rm nonunit}_{\rm fail}(X/2<c\le X)
=
O_\eta\left(X^{3/2-\eta/2}\log X\right).
}
\]

对于 unit slice，Stage 50 的单平方因子论证不再需要另选一个自由 additive coordinate，因此其贡献只有

\[
O_\eta(X^{1-\eta/2}),
\]

严格更小。dyadic 求和保持相同主幂指数，所以总体得到

\[
\boxed{
N_{\rm fail}(c\le X)
=
O_\eta\left(X^{3/2-\eta/2}\log X\right).
}
\]

相较 Stage 50 的 `2-eta/2` 指数，这在内部初等计数上整整节省了一个 `X^(1/2)` 因子（忽略对数）。

## 5. 小型精确校准：`3+125=128`

取

\[
\eta=1/10.
\]

此时 c-oriented projective ratio 为

\[
\rho_c=32/7>128^{1/10}.
\]

成对 residual witness 为

\[
m(128)=64,\qquad m(125)=25,
\]

所以

\[
m(128)m(125)=1600.
\]

两个最大平方因子根分别为

\[
q_2(128)=8,\qquad q_2(125)=5,
\]

乘积恰为 `40`。

这是双 residual / 双平方机制的紧凑 exact regression fixture。

## 6. 这个结果意味着什么、不意味着什么

P025-T126–T128 只是 explicit PCC state 与加法关系的初等推论。它不证明 pointwise PCC，更不证明 abc。

同时也不能把它包装成有竞争力的 abc exceptional-set 新结果。经典 radical-counting 早已对普通 abc/Oesterlé exceptional set 给出强得多的估计。Stage 62 专门处理这一 prior-art 边界。

项目侧真正值得保留的是：如果不立即把 cyclic denominator 擦除，粗 projective failure 会自动显露出一个**成对隐藏信息证书**，并实际改变有限 exceptional-incidence exponent。

## 7. 可执行资产

新增：

- `src/enterprise_math/abc_projective_paired_square_tail.py`；
- `tests/test_abc_projective_paired_square_tail.py`。

实现只使用整数/有理数判定与显式有限 dyadic 双平方 union envelope。

## 8. 下一前沿

Hard block 不存在。继续：

1. 与 de Bruijn radical counting 正面对照，并将 P025-T128 准确归类为 `ADOPT / WEAK / COMPARABLE`，而不是做原创性主张；
2. 把 paired residual 进一步压成 pair-radical product state；
3. 引入 de Bruijn 后检查该 pair state 能否给 PCC-specific failure 更强的无条件计数；
4. Stage 60 的 almost-all benchmark 只保留为架构内部对照，不宣传为有竞争力的解析数论结果。
