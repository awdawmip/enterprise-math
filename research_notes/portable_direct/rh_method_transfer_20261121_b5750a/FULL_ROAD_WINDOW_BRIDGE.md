# 全整数道路到原证明窗口观察量的定量桥接

Date: 2026-11-21 (Asia/Hong_Kong)
Researcher-ID: EM-DIRECT-B5750A / TASK_RESEARCH
Task: RS-RH-METHOD-TRANSFER-20261121
Status: AUTHOR_PROVED_TRANSFER_LEMMAS_AND_SOURCE_CONDITIONAL_ZERO_FREE_CRITERION

本稿复用项目已有的一阶厚度导数 `R'_0(n)=Λ(n)`，新增有限正厚度到外部实际窗口对象的统一误差估计，并明确一个仍待证明的完整道路窗口能量目标。所有道路和均保留其有限观察范围内的全部整数。

## 1. 已有源与本稿贡献

项目源：`awdawmip/enterprise-math@9fc068244e4f1117f1e75df5eb0285c6697d21d7:research_notes/COMPOSITE_ROAD_RH_PENETRATION_JET_HIERARCHY_20260906.md`，§3 已证明

\[
R_a(n)=\prod_{p\mid n}(1-p^{-a}),\qquad R'_0(n)=\Lambda(n).
\]

其中 `R_a(1)=1`，`Λ(1)=0`。本稿不把此一阶导数身份重新主张为发现。项目原稿对高阶合数层的信息范围保持有效；下面给出适用于完整有限幂窗口的显式误差，从而不靠未经控制的全域换极限。

外部源固定为 `CocoSgt/riemann-hypothesis-lean@7cbf7a0c32fca1badf05931879a37c3f8a2b03b4`：

- `src/Development/AutomorphicArithmetic/DedekindLFunctions/CharFamily.lean` 中 `ramp`、`G`、`WindowHyp`；
- `src/Development/AutomorphicArithmetic/DedekindLFunctions/LandauTheorems/lemmaL.lean`；
- `src/Development/AutomorphicArithmetic/DedekindLFunctions/LandauTheorems/ZeroFreeOfRpowWindow.lean`。

本稿的误差和转移引理由下文直接证明；零点推论消费这些外部源中的 Landau 窗口定理。未在本地重建完整 Lean 工程。

## 2. 逐整数的厚度误差

**引理 1。** 对每个 `a>0`、整数 `n≥2`，

\[
\boxed{\left|\frac{R_a(n)}a-\Lambda(n)\right|
\le \frac a2(\log n)^2.}
\]

若 `n=p^k`，记 `t=a log p`。由 `0≤t-(1-e^{-t})≤t²/2`，

\[
\left|R_a(n)/a-\log p\right|
\le a(\log p)^2/2\le a(\log n)^2/2.
\]

若 n 含至少两个不同素因子 p,q，则 `Λ(n)=0`。其余道路因子均在 `(0,1)`，故

\[
0<R_a(n)\le a^2\log p\log q
\le \frac{a^2}{4}(\log p+\log q)^2
\le \frac{a^2}{4}(\log n)^2.
\]

两类穷尽 n≥2。□

## 3. 完整道路的平滑观察量

对实数 `y≥2`，定义

\[
H_a(y)=\frac1a\sum_{2\le n\le y}R_a(n)\left(\frac yn-1\right),
\]

\[
\mathscr G_a(y)=H_a(y)-y\log y+(1+\gamma)y.
\]

外部代码的模 1 观察量是

\[
G(y)=\sum_{2\le n\le y}\Lambda(n)\left(\frac yn-1\right)
-y\log y+(1+\gamma)y.
\]

**引理 2。** 对全部 a>0、y≥2，

\[
\boxed{|\mathscr G_a(y)-G(y)|\le\frac{ay}{2}(\log y)^3.}
\]

证明：对有限和使用引理 1、`y/n-1≥0`，并用
`Σ_{n=2}^{floor(y)}1/n≤log floor(y)≤log y`，得到

\[
|\mathscr G_a-G|
\le\frac a2\sum_{2\le n\le y}(\log n)^2(y/n-1)
\le\frac{ay}{2}(\log y)^2\sum_{2\le n\le y}\frac1n.
\]

这证明所述界。□

该对象直接来自全部道路累积量。令 `S_a(t)=Σ_{n≤t}R_a(n)`，逐项有限积分给出

\[
\boxed{H_a(y)=\frac ya\int_1^y\frac{S_a(t)-1}{t^2}\,dt.}
\]

`R_a(n)` 在每个 a>0 时仍含所有不同素因子层；本稿只是对其有限窗口平滑读出进行比较，没有删除合数质量。

## 4. 厚度与幂窗口的显式联动

固定 `0<θ<1`、`λ>1`。对 `Y≥e`，令

\[
\boxed{a_Y=\frac{Y^{-\lambda(1-\theta)}}{(\lambda\log Y)^3}.}
\]

对 Y≥e 有 `0<a_Y<1`，且当 Y→∞，a_Y→0。在整个 `[Y,Y^λ]` 上，引理 2 给出

\[
\frac{|\mathscr G_{a_Y}(y)-G(y)|}{y^\theta}
\le\frac{a_Y}{2}y^{1-\theta}(\log y)^3\le\frac12.
\]

因此

\[
\boxed{|\mathscr G_{a_Y}(y)-G(y)|\le y^\theta
\quad(Y\le y\le Y^\lambda).}
\]

这是显式、保留原点、对完整有限窗口统一的界。窗口内使用同一厚度 a_Y。

### 点态窗口准则

若存在 C≥0，使对每个 Y₀≥e 都存在 Y≥Y₀ 满足

\[
\mathscr G_{a_Y}(y)\le C y^\theta
\quad\text{对全部 }y\in[Y,Y^\lambda],
\]

则该窗口上 `G(y)≤(C+1)y^θ`。对仅含模 1 角色、权重 1 的 `CharFamily`，外部 `zeroFree_of_rpow_window`（δ=λ−1）于是给出 `ζ(s)≠0` 对 `Re(s)>θ`。

若这一条件对趋于 1/2 的 θ>1/2 成立，则经该外部窗口定理与 ζ 的函数方程得到 RH。C 与窗口起点可依赖 θ，λ 可固定为实际外部主路使用的 3/2。当前尚未证明这条道路窗口上界。

## 5. 更贴近能量研究的条件目标

定义正部 `u_+=max(u,0)`，并令

\[
\mathscr E_\theta(Y)
=\int_Y^{Y^\lambda}(\mathscr G_{a_Y}(y)_+)^2
y^{-2\theta-1}\,dy.
\]

**转移定理。** 若对每个 α>0、每个 Y₀≥e，存在 Y≥Y₀ 使

\[
\boxed{\mathscr E_\theta(Y)\le Y^\alpha,}
\]

则外部 `WindowHyp` 对模 1 族成立，因此外部 `lemmaL` 给出 `Re(s)>θ` 的非零性。

证明：给定 η>0，选择 α=η，并把 Y₀ 提高到

\[
Y^{\eta/2}\sqrt{(\lambda-1)\log Y}
+(\lambda-1)\log Y\le Y^\eta
\]

对后续 Y 成立的位置。取假设所给窗口，设

\[
R(y)=\mathscr G_{a_Y}(y)_++y^\theta.
\]

由 §4，逐点有 `R≥0`、`G≤R`。道路和是有限个连续 ramp 的和，故 R 可测，在这个紧窗口上可积。Cauchy–Schwarz 给出

\[
\begin{aligned}
\int_Y^{Y^\lambda}R(y)y^{-\theta-1}\,dy
&\le\sqrt{\mathscr E_\theta(Y)(\lambda-1)\log Y}
+(\lambda-1)\log Y\\
&\le Y^\eta.
\end{aligned}
\]

这正是 `WindowHyp`。□

一个足够的更具体估计是：存在 C,A，使在任意远完整幂窗口上
`mathscr E_θ(Y)≤C(log Y)^A`。本稿交付的是该条件到实际外部零点接口的完整桥接，窗口能量估计仍是研究目标。

## 6. 与既有 Q_a 路线的关系

两者使用同一完整道路 `R_a`，但观察量不同：已有 `Q_a` 控制累计差 `E_a−1` 的全尾；本稿使用由 `S_a−1` 生成的平滑观察量，在随 Y 选定的正厚度 a_Y 上测试完整幂窗口。

从原始 Q_a 直接取绝对值并使用 Cauchy–Schwarz，会在 H_a 的公式中付出 y/a 因子。仅有定性类比不能吸收这一代价。此新路线的实际剩余问题是 `mathscr G_{a_Y}` 的单侧窗口能量控制，同时保留中心化项与道路内部的相关抵消。

本稿使“需要建立原生对象与 G 的对应”推进为一个已给出的具体映射和显式窗口误差；没有把待证明的能量上界隐藏在对象命名中。

## 7. 计算核对范围

`verify_road_window_bridge.py` 使用 mpmath 高精度浮点，对明确的有限样本核对逐整数误差、平滑积分恒等式、窗口统一界和全合数项。输出 `road_window_bridge_results.json`。

计算属于数值交叉核对，未使用区间算术；一般结论由本文证明支持。Project Review 状态保留为未审查。
