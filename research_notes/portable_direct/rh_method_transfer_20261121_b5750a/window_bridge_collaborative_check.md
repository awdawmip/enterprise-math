# 全道路窗口桥接：协作数学核验

Date: 2026-11-21 (Asia/Hong_Kong)
Collaborator: `/root/rh_deep_source`
Checked manuscript: `FULL_ROAD_WINDOW_BRIDGE.md`，§4 厚度系数为 1 的版本。
Scope: 直接复核有限厚度误差、完整幂窗口量词及正部能量转移；不是独立 Enterprise Math Project Review，没有新领取 Task/CLAIM，没有重建完整 Lean 工程，也没有由本协作者独立重跑数值脚本。

## 1. 结论与来源边界

主稿的引理 1、引理 2、厚度选择及 §5 条件转移均成立。较强误差常数为 `1/2`；后文有意使用较松的 `+1` 常数，逻辑一致。仍未证明的是道路观察量在任意远完整幂窗口上的点态界或次幂正部能量界。

项目已有身份 `R'_0(n)=Λ(n)` 由主会话核对，来源为 `awdawmip/enterprise-math@9fc068244e4f1117f1e75df5eb0285c6697d21d7:research_notes/COMPOSITE_ROAD_RH_PENETRATION_JET_HIERARCHY_20260906.md` §3。本次协作不把它重新主张为发现；以下有限厚度界直接从乘积公式证明。

外部接口固定为 `CocoSgt/riemann-hypothesis-lean@7cbf7a0c32fca1badf05931879a37c3f8a2b03b4`，本协作者读到的对应定义/定理为：

- `src/Development/AutomorphicArithmetic/DedekindLFunctions/CharFamily.lean`：`G`、`Gm`、`WindowHyp`、`ZeroFree`；
- `src/Development/AutomorphicArithmetic/DedekindLFunctions/LandauTheorems/ZeroFreeOfRpowWindow.lean`：`zeroFree_of_rpow_window`；
- `src/Development/AutomorphicArithmetic/DedekindLFunctions/LandauTheorems/lemmaL.lean`：从 `WindowHyp` 到 `ZeroFree` 的调用。

外部零点结论以这些源定理为输入。本核验不升级为对外部完整 RH 工程的证明认证。

## 2. 逐整数误差和有限平滑误差

设 `a>0`、整数 `n≥2`，并令

\[
R_a(n)=\prod_{p\mid n}(1-p^{-a}).
\]

若 `n=p^k`，取 `t=a log p`，由

\[
0\le t-(1-e^{-t})=\int_0^t(1-e^{-u})\,du\le t^2/2
\]

得到 `|R_a(n)/a−Λ(n)|≤a(log n)^2/2`。若 n 有至少两个不同素因子 p,q，其余因子均在 `(0,1)`，故

\[
R_a(n)\le a^2\log p\log q
\le \frac{a^2}{4}(\log p+\log q)^2
\le \frac{a^2}{4}(\log n)^2,
\qquad \Lambda(n)=0.
\]

因此对全部 `a>0,n≥2` 都有

\[
\boxed{|R_a(n)/a-\Lambda(n)|\le\tfrac a2(\log n)^2.}
\]

此步无需额外要求 `a≤1`。对 `y≥2`，主稿的两个平滑对象只在有限和系数上不同。利用非负权重 `y/n−1` 和

\[
\sum_{n=2}^{\lfloor y\rfloor}\frac1n
\le\log\lfloor y\rfloor\le\log y,
\]

可得

\[
\boxed{|\mathscr G_a(y)-G(y)|\le\tfrac{ay}{2}(\log y)^3.}
\]

`n=1` 必须排除，因为 `R_a(1)=1`。相应地，若 `S_a(t)=Σ_{1≤n≤t}R_a(n)`，有限逐项积分精确给出

\[
H_a(y)=\frac ya\int_1^y\frac{S_a(t)-1}{t^2}\,dt.
\]

这里没有使用无限求和换极限。

## 3. 厚度、完整窗口与量词

固定 `0<θ<1`、`λ>1`。对每个 `Y≥e`，取同一窗口内恒定的厚度

\[
a_Y=\frac{Y^{-\lambda(1-\theta)}}{(\lambda\log Y)^3}.
\]

此时 `0<a_Y<1`、`a_Y→0`，且对全部 `y∈[Y,Y^λ]`，

\[
\frac{|\mathscr G_{a_Y}(y)-G(y)|}{y^\theta}
\le\frac{a_Y}{2}y^{1-\theta}(\log y)^3\le\frac12.
\]

故后续使用 `|mathscr G−G|≤y^θ`、`G≤(C+1)y^θ` 或上包络 `mathscr G_++y^θ` 都有效，只是放松常数。

点态充分条件的完整量词是：固定 θ、λ 后，存在一个 `C≥0`，使对每个 `Y₀≥e`，存在 `Y≥Y₀`，在整个 `[Y,Y^λ]` 上都有 `mathscr G_(a_Y)(y)≤Cy^θ`。C 可依赖 θ、λ，但不能随所选窗口 Y 任意增大。源接口允许任意实数 Y₀，这由先取 `max(Y₀,e)` 满足。取 `δ=λ−1`、模 1 角色及权重 1 的单元素族，得到源 `Gm=G`，从而适用 `zeroFree_of_rpow_window`。

关键是传入 Landau 判据的函数始终是固定的 G。厚度可以随窗口 Y 改变，因为比较误差已在每个完整窗口上统一控制；无需把不同厚度的道路对象拼成新的解析函数，也无需另行假定各个道路对象满足 `PoleData`。

## 4. 正部能量转移

保持固定 θ、λ。假设

\[
\forall\alpha>0\ \forall Y_0\ge e\ \exists Y\ge Y_0:\quad
\mathscr E_\theta(Y):=
\int_Y^{Y^\lambda}(\mathscr G_{a_Y}(y)_+)^2
y^{-2\theta-1}\,dy\le Y^\alpha.
\]

给定源 `WindowHyp` 所要求的 `η>0` 和任意实数 Y₀，先增大起点，使其至少为 e，且对后续所有 Y 有

\[
Y^{\eta/2}\sqrt{(\lambda-1)\log Y}
+(\lambda-1)\log Y\le Y^\eta.
\]

这样的统一后续阈值存在，因为左端除以 `Y^η` 后趋于 0。以 `α=η` 应用能量假设，取得一个满足该阈值的完整窗口，令

\[
R(y)=\mathscr G_{a_Y}(y)_++y^\theta
\quad\text{在该窗口上}.
\]

可在窗口外任意定义 R，形成源接口所需的全域实函数。在窗口上逐点有 `R≥0`、`G≤R`。局部有限的连续 ramp 和给出 `mathscr G_(a_Y)` 的连续性；该正紧区间上的各实幂权重连续，故加权函数可测且可积。Cauchy–Schwarz 给出

\[
\begin{aligned}
\int_Y^{Y^\lambda}R(y)y^{-\theta-1}\,dy
&\le\sqrt{\mathscr E_\theta(Y)}
\sqrt{\int_Y^{Y^\lambda}\frac{dy}{y}}
+\int_Y^{Y^\lambda}\frac{dy}{y}\\
&\le Y^{\eta/2}\sqrt{(\lambda-1)\log Y}
+(\lambda-1)\log Y\le Y^\eta.
\end{aligned}
\]

这满足 `WindowHyp` 的全部正上包络、可积性和量词要求。由源 `lemmaL` 得到相应 `ZeroFree` 条件。若上述条件可对一列趋于 `1/2` 的 `θ>1/2` 建立，再结合标准对称性可导出 RH；本次并未建立该能量前提。

## 5. 本次协作确实增加与未增加的内容

已复核：有限正厚度误差常数、`n=1` 的扣除、`a_Y` 的范围、窗口内统一性、任意远窗口的阈值量词、正部能量到源 `WindowHyp` 的完整转移，以及较松 `+1` 常数的合法性。

未证明：所要求的道路窗口能量界、与既有全尾 `Q_a` 控制之间的等价性、外部 Lean 工程完整无假设闭包或编译通过。本核验只形成主任务的协作证据，不登记为独立 Project Review。
