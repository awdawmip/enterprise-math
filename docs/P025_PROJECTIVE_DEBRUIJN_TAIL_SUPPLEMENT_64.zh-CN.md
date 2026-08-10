# P025 补充 64 —— Projective Capacity Observable 的 de Bruijn Tail

状态：`ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation：`program/p025-paired-square-tail-stage61`  
依赖：P025 补充 59、61、62  
Hard block：`NONE`

## 1. 从 power threshold 推广到任意 projective threshold

考虑 dyadic 区间

\[
X/2<c\le X
\]

以及

\[
1\le T\le X.
\]

假设

\[
\sigma_{\rm proj}\ge T.
\]

对非 unit triple，Stage 61 的论证并不要求 `T=c^eta`，而是直接给出不同 components `x,y` 满足

\[
\boxed{m(x)m(y)\ge\frac{Tc}{2}.}
\]

于是

\[
\operatorname{rad}(xy)
=
\frac{xy}{m(x)m(y)}
\le
\frac{2xy}{Tc}
<
\boxed{\frac{4X}{T}}.
\]

所以每个大的 projective state 都会产生一个 pair product

\[
xy\le X^2
\]

且其 radical 只有 `X/T` 量级。

对 unit triple，Stage 50 的单 component 论证同样给出一个 `n<=X` 满足

\[
\operatorname{rad}(n)\ll X/T.
\]

## 2. P025-T130 —— 外部 de Bruijn 输入给出 `T^-1` tail

把经典 de Bruijn radical-counting estimate 作用到非 unit pair product 与 unit 单变量状态 [SRC-BERNERT-BROWNING-LICHTMAN-TERAVAINEN-2026-ABC-EXCEPTIONAL-CURRENT; SRC-LICHTMAN-2025-ABC-ALMOST-ALWAYS]。

Pair product 不超过 `X^2`，radical 为 `O(X/T)`；外部 theorem 在任意 `X^epsilon` 损失后只留下

\[
O_\varepsilon\left(\frac{X^{1+\varepsilon}}T\right)
\]

个可能 pair products。再用标准 divisor bound 恢复 labelled factor pair，第三 component 由加法关系确定。

unit slice 同阶或更小。因此

\[
\boxed{
N_X(\sigma_{\rm proj}\ge T)
\ll_\varepsilon
\frac{X^{1+\varepsilon}}T,
\qquad1\le T\le X.
}
\]

这是 explicit P025 projective observable 的无条件 tail theorem；唯一外部输入是作为 prior art 导入的 de Bruijn radical-counting theorem。

它严格强化 Stage 59 的纯初等尾界

\[
N_X(\sigma_{\rm proj}\ge T)
\ll\frac{X^2}{\sqrt T}.
\]

## 3. P025-C13 —— 所有固定阶 `theta<2` 的 normalized moments 都可控制

在 height `X` 上有平凡有限界

\[
0<\sigma_{\rm proj}\le X.
\]

固定

\[
0<\theta<2.
\]

`σ<1` 的部分至多贡献 ambient `O(X^2)` triple count。对 `σ>=1` 使用 layer-cake：

\[
\sum\sigma_{\rm proj}^{\theta}
\ll
X^2
+
X^{1+\varepsilon}
\int_1^X t^{\theta-2}\,dt.
\]

若 `theta<1`，积分有界；`theta=1` 时只有 logarithm；若 `1<theta<2`，积分为 `O(X^(theta-1))`。在每种情况下都可把 `epsilon` 取得相对于 `2-theta` 足够小，从而得到

\[
\boxed{
X^{-2}
\sum_{X/2<c\le X}
\sigma_{\rm proj}^{\theta}
=O_\theta(1),
\qquad0<\theta<2.
}
\]

可进一步限制到 primitive triples。

这里必须严格理解为：**当前 tail estimate 能证明的 moment range** 是 `theta<2`；并不主张真实 analytic critical order 就是 2。

## 4. 与 Stage 59 的比较

Stage 59 只使用 elementary one-square tail，因此只能得到 `theta<1/2` 的 uniform moment statement。

经过 Stage 61 paired reduction 和外部 de Bruijn 输入，已证明范围提升为

\[
\boxed{0<\theta<2.}
\]

提升来自两个独立步骤：

1. 加法关系把一个 residual 升级成 paired residual product；
2. de Bruijn 直接计数 small-radical pair product，而不是对所有 square divisors 做 union bound。

因此外部 theorem 在新架构中改变的不只是某个常数，而是 exceptional-state count 的有效维数。

## 5. 架构解释

整个 tail 路线可以写成

\[
\boxed{
\sigma_{\rm proj}\ge T
\to
\text{paired residual pressure}
\to
\text{pair product }xy
\to
\operatorname{rad}(xy)\ll X/T
\to
\text{de Bruijn count}.
}
\]

每一步都擦除信息，但对 declared future query“超过 projective threshold `T` 的状态有多少”而言，被擦除的坐标都不再需要。

这是一个典型样本：外部 theorem 只有在项目先把 fine witness state 编译到 theorem-native input language 后才真正变得有效。

## 6. Prior-art 边界

Radical-counting theorem、divisor bound、layer-cake identity 以及 classical/modern abc exceptional-set results 都属于 prior mathematics。P025 不做这些结果的优先权主张。

项目侧只保留从 `sigma_proj>=T` 到 pair-product radical state 的 exact compiler，以及把前人 theorem 作用到 P025 observable 后得到的组合后果。历史 novelty 保持 `NOVELTY_UNVERIFIED`。

## 7. 可执行资产

新增：

- `src/enterprise_math/abc_projective_debruijn_tail.py`；
- `tests/test_abc_projective_debruijn_tail.py`。

实现只记录 exact paired reductions 与 rational moment-range calculus，不伪造对外部渐近 de Bruijn theorem 的“代码证明”。

## 8. 下一前沿

Hard block 不存在。继续：

1. 在没有 lower-bound / structured family 之前，不把 `theta=2` 称为真实 moment boundary；
2. 比较 pair-product radical state 与现代 anatomic exponent-layer decomposition；
3. 将 stronger tail 用于 PCC-specific average questions，而不是拿它替代远强的 ordinary abc exceptional-set literature；
4. 把 staged `fine state -> theorem-native coarse state` compiler pattern 回流 A2/P023。
