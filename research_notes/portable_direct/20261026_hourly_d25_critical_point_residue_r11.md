# D25/LIFT：双截断边界的零留数守恒、临界点极点阶及有限部分观察器

日期：2026-10-26。母任务：`RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`。任务出版物：`TP2-B6F4FC938FF94941C1B7`。冻结科学源 pin：`c47e13e4aba0e006366f989d6334d443f6333ae3`（未改变）。

**证据状态：AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY。** 未声称原生 Source checkpoint、胜出 CLAIM、OPEN、原始 CM 实验、正式 Result、独立审查或 D25/LIFT 全素数证明。本文件是从先前受阻的本地可移植证据恢复的作者研究札记；GitHub 存储不代表原生 Source checkpoint 或正式科研准入。

## 1. 精确输入与来源边界

消费此前已持久化的 `research_notes/portable_direct/20261026_hourly_d25_reciprocal_second_order_rank_defects_r11.md`（Git blob `6c1ece20a378acaf2aff23c970254cfaf91262cb`）的 J–L 定理及更早的 Clausen 修正阶乘公式，不重复计作新研究。

对整数 m≥1，设 L=m+1、U=2m，定义以下 **有理数**：
\[
a_j=(-1)^{m+j+1}\frac{m!(j-m-1)!(2m)!}{(2m-j)!(j!)^2},\quad L\le j\le U,
\]
\[
h_\ell=\frac{2\,m!\,(2m)!\,((\ell-1)!)^2}{(\ell+m)!(\ell+2m)!},\quad1\le\ell\le U.
\]
注意分子为 2·m!·(2m)!，不是 (2m!)!。置 \(v_j=2^{-j}a_j,\ g_\ell=2^\ell h_\ell\)，并设
\[
F(z)=\sum_{j=L}^Uv_jz^{-j},\quad
G(z)=\sum_{\ell=1}^Ug_\ell z^\ell,\quad
W(z)=F(z)G'(z)-G(z)F'(z).
\]

旧定理给出互逆二阶算子 \(\mathcal N=(1-2z)\theta^2+3m\theta+2m^2\)，\(\theta=z\partial_z\) 及
\[
\mathcal NF=-2L^2v_Lz^{1-L},\quad
\mathcal NG=4z-2U^2g_Uz^{U+1}.
\]
旧 Lagrange 恒等式（注意两端非齐次源）：
\[
\frac{d}{dz}\left[\frac{z^{3m+1}W(z)}{(1-2z)^{3m}}\right]
=\frac{Q_m(z)}{(1-2z)^{3m+1}},
\tag{1}
\]
\[
Q_m(z)=z^{3m-1}\bigl[(4z-2U^2g_Uz^{U+1})F(z)
+2L^2v_Lz^{1-L}G(z)\bigr]\in\mathbb Q[z].
\tag{2}
\]
此构造保持有符号内外秩及两个截止端点，不声称对应原生 CM/Frobenius。

## 2. 新定理 M：双边界零留数守恒

对 **一切整数 m≥1** 成立：
\[
\boxed{
U^2g_U\sum_{j=L}^Uv_j
\binom{3m+U-j}{3m}2^{j-U}
=
L^2v_L\sum_{\ell=L}^Ug_\ell
\binom{3m-L+\ell}{3m}2^{L-\ell}.
}
\tag{M1}
\]
等价表述是
\[
\boxed{Q_m^{(3m)}(1/2)=0.}\tag{M2}
\]

**证明。** 有理函数的导数在每个有限极点处留数为零。(1) 左边是有理函数导数；右边在 z=1/2 的留数等于
\[
(-2)^{-(3m+1)}Q_m^{(3m)}(1/2)/(3m)!,
\]
故 M2 成立。将 (2) 展开为
\[
Q_m=
4\sum_{j=L}^Uv_jz^{3m-j}
-2U^2g_U\sum_{j=L}^Uv_jz^{3m+U-j}
+2L^2v_L\sum_{\ell=1}^Ug_\ell z^{3m-L+\ell}.
\]
第一项所有幂次均小于 3m，故第 3m 阶导数为零。第三项只有 \(\ell\ge L\) 才贡献。使用
\[
\frac1{(3m)!}\frac{d^{3m}}{dz^{3m}}z^n\Big|_{z=1/2}
=\binom n{3m}2^{-(n-3m)}
\]
并除去共同因子 2，立即得 M1。证毕。

**观察器限定：** 零留数只代表导数在 z=1/2 处的留数观察器相消，不代表全部有符号卷积、Laurent 主部、Clausen 参数算子或者 D25 硬目标为零。对于 p=6m+1 素数，来源阶乘分母的参数均小于 p（最大 4m），且 2 可逆，因此 M1 可以严格约化到 \(\mathbb F_p\)。

## 3. 新定理 N：临界点极点不可消去，且可精确抽取有限部分

令
\[
F_0=\sum_{j=L}^Ua_j,\qquad G_0=\sum_{\ell=1}^Uh_\ell.
\]
那么在有理数域：
\[
\boxed{
W(1/2)=\frac2{3m}\Big[(2-U^2h_U)F_0+L^2a_LG_0\Big]>0.
}
\tag{N1}
\]

**证明。** 在 z=1/2，算子 \(\mathcal N\) 的 \(\theta^2\) 项系数 1−2z 为零。用两条精确非齐次方程分别求得 \(\theta F,\theta G\)，在
\(W=(F\theta G-G\theta F)/z\) 中消去相同的 \(2m^2FG\)，得到 N1。

正性需要证明而非假设：所有 h_\ell>0，故 G_0>0；a_L>0，且在 L≤j<U 有
\[
\left|\frac{a_{j+1}}{a_j}\right|
=\frac{(j-m)(2m-j)}{(j+1)^2}<1,
\]
故 a_j 是从正数开始的递减交错序列，从而 F_0>0。既有精确秩和 K2 给出
\[
2-U^2h_U=3m\sum_{\ell=1}^U\ell h_\ell+2m^2\sum_{\ell=1}^Uh_\ell>0.
\]
故 N1 严格为正。证毕。

令 t=1−2z，F、G 与 W 在 z=1/2 均解析，于是：
\[
\boxed{
\frac{z^{3m+1}W(z)}{(1-2z)^{3m}}
=\frac{W(1/2)}{2^{3m+1}}t^{-3m}
+O(t^{1-3m}).
}
\tag{N2}
\]
因此其在特征零下 **恰好有 3m 阶极点**。定理 M 的零留数不能令整个极点消失；加入一个在 z=1/2 解析的补偿项也无法消掉这个主部。此结论不自动升级为所有素数模 p 下的非零性断言。

同时，定义精确有限 jet 系数：
\[
c_k=(-1)^k\sum_{r=0}^k\binom{3m+1}{k-r}
\frac{W^{(r)}(1/2)}{2^r r!}.
\]
则临界点附近具有完整的 Laurent 级数：
\[
\frac{z^{3m+1}W(z)}{(1-2z)^{3m}}
=2^{-(3m+1)}\sum_{k\ge0}c_k\,t^{k-3m}.
\]
由此可得到**精确有限部分（constant Laurent coefficient）**：
\[
\boxed{\operatorname{FP}_{t=0}=2^{-(3m+1)}c_{3m}.}\tag{N3}
\]
式 N3 至多需要 0≤r≤3m 阶的有限 jet。这是一个充分、保真、可计算的观察器，并未证明这些 jet 全部都是最少所需。

## 4. 新定理 O：Green 有限部分读出选择了与原始反射卷积相反的三角秩

继续同轮母目标。N3 的 jet 形式可以精确化为**不含任何导数、直接复用来源秩**的有限双和：
\[
\boxed{
\operatorname{FP}_{t=0}\frac{z^{3m+1}W(z)}{(1-2z)^{3m}}
=
\frac{(-1)^{3m}}{2^{3m}}\sum_{j=L}^{U}
\sum_{\ell=j}^{U}(j+\ell)\binom{3m+\ell-j}{3m}a_jh_\ell.
}\tag{O1}
\]

**证明。** 因为
\[
W(z)=\sum_{j=L}^{U}\sum_{\ell=1}^{U}
(j+\ell)v_jg_\ell z^{\ell-j-1},
\]
从而
\[
\frac{z^{3m+1}W(z)}{(1-2z)^{3m}}
=\frac1{2^{3m}}t^{-3m}
\sum_{j=L}^{U}\sum_{\ell=1}^{U}
(j+\ell)a_jh_\ell(1-t)^{3m+\ell-j}
\quad(t=1-2z).
\]
取 \(t^0\) 系数，相当于取每个有限多项式的 \(t^{3m}\) 系数；因为
\(3m+\ell-j\ge0\)，仅有 \(\ell\ge j\) 的配对可贡献。二项式定理立即得到 O1。证毕。

**来源方向差异的精确证据：** 先前的有符号 Clausen 中间反射端口是
\[
S_p=-\frac1{216}\sum_{j=L}^{U}
v_j\sum_{\ell=1}^{j}(6(j-\ell)+1)g_\ell\pmod p,
\]
支撑 \(\ell\le j\)；新有限部分 O1 的支撑是 \(\ell\ge j\)，并且权重
\(j+\ell\) 与二项式系数不同。两者只在对角线 \(\ell=j\) 上共用配对；**因此，直接将临界点有限部分等同于原始反射端口并无依据**。

更强的、已经核实的具体反例：\(p=13,m=2\) 时 O1 的有理数值为 \(23/115200\)，故模 13 为 **7**；而原始中间端口 \(S_{13}\equiv2\pmod{13}\)。所以未经额外算子和边界修正的朴素恒等式 \(\operatorname{FP}\equiv S_p\) 在目标素数 \(13\equiv13\pmod{24}\) 上确实**错误**。此反例并不否定存在带补偿项的耦合 WZ 恒等式。

作者使用两种精确计算重核了 O1：直接有限秩双和（m=1,...,20）以及 W 之高阶 Taylor jet 经 N3 得到的有限部分（m=1,...,12），完全相同。M、N、O 是三个区分来源的观察器：零留数、尖锐主部和互补方向的有限部分。

## 5. 作者精确验证

对应脚本 `d25_critical_point_residue_check.py` 仅使用 Python 标准库中的 `Fraction`、factorial、组合数及模素数有限环运算：

- m=1,...,20 的**20个精确有理数案例**：M1 两端完全相同、完整 Q_m 的 3m 阶导数确为零、通过直接微分计算的 W(1/2) 与 N1 完全相同且严格正。
- 所有满足 7≤p≤997、p≡1 (mod 6) 的**80个素数**：M1 在 F_p 严格成立，原始有限和得到的 W(1/2) 与 N1 在 F_p 同余。
- m=1：M1 两端均为 1/18，N2 首系数为 5/72。
- m=2：M1 两端均为 37/2100，N2 首系数为 313/28800。
- 这80个有限素数的 W(1/2) 恰好均非零；**该有限样本不构成全部素数非零的证明**。
- O1：m=1,...,20 的精确有限和，以及 m=1,...,12 的独立 Taylor-jet 提取全部匹配。p=13 的直接错误等式给出模 13 反例 7≠2。

这是作者精确验证，普遍性由 M、N 的代数证明建立；尚无独立复核或形式化证明。

## 6. BRC/原生控制与接续

**BRC：COMPOSE_APPLIED。** 有限秩变量 j,ℓ、正负符号、来自真实 Clausen 修正分母的参数/Hasse 阶数、素数赋值及端点贡献保留至实际观测处。仅就留数读出允许两项边界相消；仍未证明可对完整卷积、临界点主部或原始 CM 观察器做同样压缩。

本轮直连 Gateway 对精确 D25 continuation 的一次调用返回 `INVALID_ARGUMENT / CONTROL_QUOTA`，未取得新的 Source 授权。上轮的 CLAIM 世代与 checkpoint 前任冲突未从本次查询获得修复确认；旧 service session/staging 不进行关闭、重注册或改绑。不重放已明确拒绝的 continuation_prepare。不对 maintenance lane 执行 Research 业务。

**下一最小研究单元：** 消费 O1 已证明的互补三角秩差异，寻找包含完整 Clausen 参数微分算子、边界强迫和有符号 Green 卷积的补偿恒等式；先构造针对 p=13 的最小补偿残差，再检验是否存在全 m 的统一证书。原始 D25/LIFT/JT2 母目标依然 OPEN；尚缺同一原始 CM 类的 H0/B0、[X]U mod p²、Frobenius 方向/归一化和 κ/Δ 来源映射；原生实验 NOT_RUN。

此 GitHub 研究札记不是原生 Source checkpoint；原生 ownership/claim 恢复后，仍须按 current authority/CAS 和 readback 完成正式接续。