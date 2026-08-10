# P025 补充 68 —— Adaptive Projective Precision 的近线性总预算

状态：`ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation：`program/p025-paired-square-tail-stage61`  
依赖：P025 补充 64、67  
Hard block：`NONE`

## 1. 只有跨过 threshold 后才打开下一层精度

对 projective scalar 使用嵌套 dyadic thresholds

\[
1,2,4,8,\dots.
\]

定义 adaptive refinement level

\[
\boxed{
L(\sigma)=
\begin{cases}
0,&0<\sigma<1,\\
1+\lfloor\log_2\sigma\rfloor,&\sigma\ge1.
\end{cases}}
\]

它有 exact threshold-language 解释：

\[
\boxed{
L(\sigma)=\sum_{k\ge0}\mathbf1_{\{\sigma\ge2^k\}}.
}
\]

所以 subunit basin 中 state 不支付 projective refinement cost；只有 activation 后，每跨过一个新的 dyadic threshold 才打开一层额外 precision。

## 2. P025-T136 —— aggregate dyadic refinement budget 近线性

在

\[
X/2<c\le X
\]

上，Stage 64 在导入 de Bruijn radical counting 后给出

\[
N_X(\sigma_{\rm proj}\ge T)
\ll_\varepsilon\frac{X^{1+\varepsilon}}T.
\]

对所有 additive states 求和 exact threshold identity：

\[
\sum L(\sigma_{\rm proj})
=
\sum_{k\ge0}N_X(\sigma_{\rm proj}\ge2^k).
\]

只有 `O(log X)` 个项可能非零，而 tail bound 给出收敛 geometric sum：

\[
\sum L(\sigma_{\rm proj})
\ll_\varepsilon
X^{1+\varepsilon}\sum_{k\ge0}2^{-k}.
\]

因此

\[
\boxed{
\sum_{X/2<c\le X}L(\sigma_{\rm proj})
=O_\varepsilon(X^{1+\varepsilon}).
}
\]

同一有限宇宙中的正整数 additive triples 数量为 `Theta(X^2)`。

所以这个 adaptive threshold language 的**额外精度总预算**近似只随 `X` 线性增长，虽然 ambient finite-state universe 本身是二次规模。

## 3. 平均 refinement depth 趋于零

除以 ambient state count 得

\[
\boxed{
\frac1{\Theta(X^2)}\sum L(\sigma_{\rm proj})
=O_\varepsilon(X^{-1+\varepsilon}).
}
\]

因此均匀抽取一个 additive state 时，所需额外 dyadic projective refinement 平均趋于零：绝大多数 states 在 subunit decision 就直接终止。

这比“activated states 稀疏”更强，因为它还按照 deep activated states 实际跨过多少层 boundary 对其收费。

## 4. Exact finite examples

- `2+3=5` 在 subunit basin，故 `L=0`；
- `1+2=3` 有 `sigma_proj=1`，故 `L=1`；
- `3+125=128` 满足 `4<sigma_proj<8`，故 `L=3`，对应 exactly crossed thresholds `1,2,4`。

## 5. Precision architecture consequence

这给出一个完整的 **adaptive precision allocation** 样本：

\[
\boxed{
\text{coarse bulk state}
\to
\text{sparse activation}
\to
\text{nested refinement only where demanded}.
}
\]

至少要区分三种 complexity：

1. ambient state count：`Theta(X^2)`；
2. activated-state incidence：`O_epsilon(X^(1+epsilon))`；
3. total adaptive dyadic refinement depth：`O_epsilon(X^(1+epsilon))`。

因此 richer precision language 并不意味着每个 state 都支付 worst-case depth；真正成本由各层 boundary 的 incidence 加权。

这应与 P018/P023 precision horizons 及 E002 task-relative observation budgets 对照；若上提为 generic theorem，其 mother layer 不应归 P025。

## 6. Prior-art boundary

Threshold-sum identity 是初等的，tail estimate 导入经典 de Bruijn radical counting。P025 不主张这些一般工具的新颖性。

项目侧贡献是 explicit projective observable 及其 theorem-native sparse tail，使 adaptive precision budget 可以被精确实例化。generic adaptive coding/information-theoretic priority 不作主张。

## 7. 可执行资产

新增：

- `src/enterprise_math/abc_projective_adaptive_precision.py`；
- `tests/test_abc_projective_adaptive_precision.py`。

可执行层只保存 exact dyadic levels 与 threshold bits；渐近 aggregate theorem 仍是 Stage 64 + external prior art 的数学推论。

## 8. 下一前沿

Hard block 不存在。继续：

1. 用 task-optimized threshold schedule 取代 dyadic schedule，但不重复 P023 generic query-language theory；
2. 在 `eta_min`、certificate-index、relation-generation profiles 上测试同一 sparse-adaptive pattern；
3. 将 `ambient size / sparse incidence / aggregate refinement budget` 作为 Foundation-facing precision 区分 Relay；
4. 数论路线继续攻击 classical radical selector 不拥有的 structural information。
