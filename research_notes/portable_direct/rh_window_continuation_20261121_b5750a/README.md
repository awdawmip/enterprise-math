# 黎曼方法继续提取：多厚度桥、完整窗口证书与尾通量

Date: 2026-11-21 (Asia/Hong_Kong)
Researcher-ID: EM-DIRECT-B5750A / TASK_RESEARCH
Research-Activity-ID: RA-60C6D083A81B19084A74C5BA
Task context: RS-RH-METHOD-TRANSFER-20261121 / TP2-677F61D1BCF81D4E4FE3
Scientific status: AUTHOR_PROVED_BRIDGES_AND_FINITE_CERTIFICATE; UNIFORM_WINDOW_ENERGY_OPEN.

## 本轮推进到哪里

上一轮已把外部材料的完整窗口/单侧能量思路接到项目完整道路上。本轮继续处理这个桥的实际代价：提高有限厚度的逼近阶数，同时精确保留带符号的跨厚度信息，并把连续窗口的检查转成有限证书。

本轮主要成果如下：

| 成果 | 作用 | 证据 |
|---|---|---|
| 任意固定阶多厚度误差桥 | 由一阶误差提升到 m 阶，允许更厚的输入 | 一般证明、精确系数检查及高精度复算 |
| 正凸混合偏差下界及两厚度精确权衡 | 说明该读出族为何需要负权重，并量化输入误差放大 | 一般证明 |
| [25,125] 完整道路反例 | 两个输入正部能量为零，外推正部能量严格为正 | 纯有理数端点包络及连续单元证明 |
| 整数端点的连续窗口证书 | 曲率余量与厚度无关，连续正部能量可由有限数据包络 | 一般证明、严格反例、数值交叉核对 |
| 精确中心化尾表示及有限窗口 Gram | 把研究目标写成窗口内部残差与右端通量的控制 | 一般证明、80位数值交叉核对 |

这里的“已证”指作者给出的数学证明及所注明的精确证书。项目正式 Result 与 Review 的状态见末节。

## 1. 统一对象与来源

完整道路及一阶 jet 沿用项目定义：

\[
R_a(n)=\prod_{p\mid n}(1-p^{-a}),\quad R_a(1)=1,
\qquad \partial_aR_a(n)|_{a=0}=\Lambda(n)\ (n\ge2).
\]

所有有限和保留整个观察范围内的整数及合数贡献。令

\[
\mathscr G_a(y)=\frac1a\sum_{2\le n\le y}R_a(n)(y/n-1)
-y\log y+(1+\gamma)y,
\]

\[
G(y)=\sum_{2\le n\le y}\Lambda(n)(y/n-1)-y\log y+(1+\gamma)y.
\]

G 是固定的极限观察量；每个窗口内部采用固定厚度，窗口之间可以改变厚度。固定 0<θ<1、λ>1，记

\[
E_{\theta;Y,Z}^{+}(f)=\int_Y^Z f(y)_+^2 y^{-2\theta-1}\,dy.
\]

科学输入沿用 enterprise-math@9fc068244e4f1117f1e75df5eb0285c6697d21d7 的 P000/X6、联合观察保真、道路 jet 及道路能量记录。它们是原生世界上的类型化算术读出；厚度和窗口参数不增加空间轴。标量线性组合只对所声明的观察量有效。

上一轮来源：[完整道路窗口桥及原点端口](https://github.com/awdawmip/enterprise-math/tree/d020e8a51defa2a0e45cd8a9150330805627155c/research_notes/portable_direct/rh_method_transfer_20261121_b5750a)。外部方法来源沿用固定镜像 CocoSgt/riemann-hypothesis-lean@7cbf7a0c32fca1badf05931879a37c3f8a2b03b4；本轮没有重新宣布该外部工程的整体证明状态。

## 2. 从单厚度桥推进到任意固定阶

对 n≥2、a≥0、k≥1，有限乘积的 Leibniz 公式给出

\[
|\partial_a^kR_a(n)|\le(\log\operatorname{rad}n)^k.
\]

令 w_j=(-1)^{j+1}\binom mj，定义

\[
D_{m,h}(n)=\frac1h\sum_{j=1}^{m}\frac{w_j}{j}R_{jh}(n).
\]

导数插值余项给出

\[
\boxed{|D_{m,h}(n)-\Lambda(n)|
\le\frac{h^m}{m+1}(\log\operatorname{rad}n)^{m+1}.}
\]

相应组合 \(\mathscr G_h^{[m]}=\sum_jw_j\mathscr G_{jh}\) 的权重和为1，共同中心项恰保留一次，并满足

\[
|\mathscr G_h^{[m]}(y)-G(y)|
\le\frac{h^m}{m+1}y(\log y)^{m+2}.
\]

因此取

\[
\boxed{h_Y=\left(\frac{m+1}{2}\right)^{1/m}
\frac{Y^{-\lambda(1-\theta)/m}}{(\lambda\log Y)^{1+2/m}}}
\]

即可在整个 [Y,Y^λ] 上保证误差 ≤y^θ/2。需要限制最大厚度时可进一步截帽，这只会缩小误差。m 按固定整数使用。

最实用的二阶式，以最大厚度 A=2h 表示，是

\[
\boxed{D_{2,A/2}(n)=\frac{4R_{A/2}(n)-R_A(n)}A,
\qquad |D_{2,A/2}-\Lambda|\le\frac{A^2}{12}(\log\operatorname{rad}n)^3.}
\]

对应最大厚度可取

\[
A_Y=\sqrt6\,\frac{Y^{-\lambda(1-\theta)/2}}{(\lambda\log Y)^2}.
\]

厚度缩小的幂指数减半，是明确的尺度收益。与此同时，归一化输入的最坏误差放大为 2^m−1；原始 R 输入的误差放大为 h^{-1}\sum_j\binom mj/j。若把 n=1 纳入人口，必须保留减项 H_mR_0(n)/h，H_m=\sum_{j=1}^m1/j。当前平滑和从 n=2 开始，已经遵守这一端口处理。

完整证明及复算：[多厚度桥](rh_continuation_multithickness/NOTES.md)。

## 3. 为什么正混合不够，以及二厚度的可计算权衡

对素数幂 p^k，令 L=log p，则

\[
F_a(p^k):=R_a(p^k)/a=\int_0^L e^{-au}\,du.
\]

F_a 随厚度严格递减。因此正权重归一化混合 P=\sum_jα_jF_{a_j}（α_j≥0、\sumα_j=1）满足 P(p^k)≤F_b(p^k)<L，其中 b=min a_j。若 max a_jL≤1，还有

\[
L-P(p^k)\ge\frac{L^2}{3}\sum_jα_ja_j\ge bL^2/3.
\]

在这一族内，只用与 a 同阶的正厚度不能获得高于一阶的素数幂精度。更薄的输入或带符号外推是具体的改进方向。

任意 0<b<a 的二阶外推为

\[
D_{a,b}=\frac{aF_b-bF_a}{a-b},\qquad
|D_{a,b}-\Lambda|\le\frac{ab}{6}(\log\operatorname{rad}n)^3.
\]

对两个归一化输入各自≤η 的绝对扰动，精确最坏放大为 (a+b)/(a−b)。给定上限 K>1、正预算 L_0>0 和约束 ab≤L_0，最大的最小厚度是

\[
\boxed{b_{\max}=\sqrt{L_0\frac{K-1}{K+1}}.}
\]

K=3 时恰得到 b=a/2。这里的优化针对已声明的两节点族与输入扰动范数，原始道路计算成本还应另计。

证明：[正混合与精确代价](POSITIVITY_AND_COST.md)。

## 4. 实际道路反例：各自的正部会漏掉外推信息

本轮以完整道路、固定厚度 1/10 与 1/5，构造了严格的完整幂窗口证书。对每个实数 y∈[25,125]=[25,25^{3/2}]，都有

\[
\boxed{\mathscr G_{1/10}(y)<0,\quad \mathscr G_{1/5}(y)<0,
\quad 2\mathscr G_{1/10}(y)-\mathscr G_{1/5}(y)>1/6.}
\]

所以 θ=3/4 时两个输入的正部能量均为0，而外推正部能量严格大于1/9000。不能仅由各输入正部能量控制这个带负权重的外推。这里检验的是固定厚度的有限窗口表示；它不反驳匹配 h_Y 的渐近窗口目标。

证书采用 Python Fraction：对数正项级数及有理尾界、素数十次根夹逼、Euler 常数调和和包络。检查全部101个整数端点，再用单元曲率覆盖全部100个连续单元；符号判定不使用浮点数。

这一缺口的直接修复是保留厚度差。以二阶式为例，

\[
2\mathscr G_h-\mathscr G_{2h}=\mathscr G_h+(\mathscr G_h-\mathscr G_{2h}).
\]

锚与厚度差的正部范数之和给出组合正部范数的上界。厚度差中共同中心项抵消，在每个整数单元上精确线性；其单侧能量可以直接分段积分。该充分上界仍可能损失锚负部与厚度差的抵消，因此完整组合的直接正部计算也保留在材料中。

证明与严格证书：[窗口主稿](rh_continuation_window_phase/NOTES.md)、[有理证书](rh_continuation_window_phase/positive_window_certificate.json)、[作者协作核对](rh_continuation_multithickness/WINDOW_CERTIFICATE_CHECK.md)。

## 5. 连续窗口可转成有限端点证书

对任意固定有限厚度族、权重和为1的组合 F，在每个整数单元都有

\[
F(y)=y(d_N-\log y)-b_N,\qquad F''(y)=-1/y.
\]

若 L 是按整数断点及窗口端点构造的线性插值，在单元 [l,r] 上

\[
L(y)\le F(y)\le L(y)+(r-l)^2/(8l).
\]

从而

\[
E_+(L)\le E_+(F)\le(\sqrt{E_+(L)}+\varepsilon_{Y,Z})^2,
\quad
\varepsilon_{Y,Z}\le\frac{1+1/Y}{8\sqrt{2\theta+2}}Y^{-\theta-1}.
\]

曲率余量不随厚度或外推阶数增大；端点自身的求值误差仍须按真实权重传播。窗口前的全部道路作用保留在 d_N,b_N 的累计项中。若以后可以重新选择厚度组合，应分别保存各厚度端口。

因此，对固定 θ、λ，任意远完整窗口的次幂正部能量条件，等价于整数端点插值的同一条件。有限连续窗口的验证已经有明确误差；任意远窗口的存在量词仍是要研究的数学内容。

## 6. 将下一步落到局部残差与边界通量

设 S_a(t)=\sum_{n≤t}R_a(n)、c_a=1/ζ(1+a)，并在 t≥1 定义 U_a(t)=S_a(t)−1−c_at。项目原始全道路能量精确为

\[
\mathcal Q_a=c_a^2+\int_1^\infty U_a(t)^2t^{-2}\,dt.
\]

第一项来自 0<t<1 的连续背景。对每个 a>0，一阶尾积分绝对收敛，且

\[
\kappa_a=\int_1^\infty U_a(t)t^{-2}\,dt=(\gamma-1)c_a+c'_a-1.
\]

令 T_a(y)=\int_y^∞U_a(t)t^{-2}dt，则

\[
\mathscr G_a(y)=y[(c_a/a-1)\log y+1+\gamma+\kappa_a/a]-\frac yaT_a(y).
\]

尾通量也有有限读出式

\[
T_a(z)=\kappa_a-\left[\sum_{2≤n≤z}R_a(n)(1/n-1/z)-c_a\log z\right].
\]

给定背景常数 c_a,c'_a 后，右端由有限完整道路数据给出；这些常数的精度与计算代价也需明确处理。

对 m 阶组合，取 V_{m,h}=\sum_j(w_j/j)U_{jh}、T_{m,h}=\int_y^∞V_{m,h}(t)t^{-2}dt。固定 m 的背景漂移为 O_m(h^m)。有限窗口 [Y,Z] 中

\[
T_{m,h}(y)=T_{m,h}(Z)+\int_y^ZV_{m,h}(t)t^{-2}\,dt.
\]

其平方能量的精确 Gram 核为

\[
K(u,v)=\frac{A_\theta(Y,\min(u,v))}{u^2v^2},\qquad
A_\theta(Y,t)=\frac{t^{2-2\theta}-Y^{2-2\theta}}{2-2\theta}.
\]

展开时必须同时保留右端通量平方及其与窗口内部的带符号交叉项。加权 Hardy 估计给出局部控制常数 (1−θ)^{-2}，在 θ↓1/2 时趋于4。

一个明确的后续充分目标是：固定 m、θ、λ，以以上匹配 h_Y、Z=Y^λ，证明

\[
\boxed{\frac1{h_Y^2}\left[
\int_Y^{Y^\lambda}V_{m,h_Y}(t)^2t^{-2\theta-1}\,dt
+A_\theta(Y,Y^\lambda)T_{m,h_Y}(Y^\lambda)^2
\right]\le Y^{o(1)}}
\]

在任意远完整窗口成立。量词为：对每个 α>0、Y_0，存在 Y≥Y_0，使左式≤Y^α。它由有限窗口内部数据和一个明确边界通量组成，并通过 Hardy 与漂移估计推出需要的组合正部能量条件。它是有用的充分条件，是否达到仍待证明。

尾稿还核对了在项目既有 RH 等价强条件 Q_a≤Ca 下的接口代价：幂指数为 1−2θ+λ(1−θ)/m，阈值 θ≥(m+λ)/(2m+λ)。该比较证明固定阶外推能修复一阶桥的尺度损失；没有以此证明其强前提。详见[中心化尾与窗口能量](rh_continuation_tail/CENTERED_TAIL_AND_WINDOW_ENERGY.md)。

## 7. 复算与证据分类

在包根目录执行：

```bash
python3 rh_continuation_window_phase/verify_positive_window.py
python3 rh_continuation_multithickness/verify_multithickness.py
python3 rh_continuation_tail/verify_tail_window.py
python3 rh_continuation_window_phase/verify_window_formulas.py
```

严格窗口脚本只需 Python 标准库，其证书判定使用 Fraction。其余三个脚本需要 mpmath，分别采用90、80、70位精度；已有 JSON 保存实际运行结果。默认输出文件相对于各脚本目录保存，具体行为以脚本为准。

| 检查 | 实际范围 |
|---|---|
| 多厚度 | 68项精确矩/系数、1,032项有理Peano核采样、440项导数、3,576项整数外推、144项窗口样本 |
| 尾与 Gram | 600个单位格、6个真实道路有限窗口、4个带无条件余界的一阶尾核对，以及 Laurent/漂移检查 |
| 严格符号证书 | 101个整数端点、100个连续单元，全部有理数决策 |
| 窗口公式 | Lambert W 正区间分支、θ=1/2原函数分支、2个实际道路窗口及其跨厚度 Gram/单侧能量 |

一般命题由对应正文的证明支持。数值交叉核对与严格区间证书在状态和文件中分别标明。作者协作核对使用共享上下文，不计为独立项目 Review。插值、Hardy、凹性和 Gram 等一般工具不主张新颖性；本轮成果是这些工具对项目完整道路、端口与完整窗口的精确应用。

## 8. 任务与控制面状态

以下状态锚定于2026-11-21本轮取得的既有请求回执：

- Task RS-RH-METHOD-TRANSFER-20261121 已由上一轮发布。本轮复用同一研究身份和 Activity，继续作者侧推导与 Source 持久化。
- 原交接请求 rh-method-transfer-20261121-0932-handoff-v1 已 SUCCEEDED。Source commit 为 28e616732857272257171444ac7bcc63ac4c19ac，HANDOFF(CONTINUATION) 的 authenticated_readback=true，comment_id=7055376586。原 claim 已交接，不把旧租约或旧 run 元数据作为本轮保护执行授权。
- 原正式冻结请求 rh-method-transfer-20261121-0930-freeze-github-v1 保留 FAILED: NATIVE_GLOBAL_AUDIT_INPUT_BUDGET_EXCEEDED。本轮没有重复提交该失败操作、创建新身份或修改预算。
- 新材料通过项目允许的作者研究笔记和 Activity 证据保存。Source 保存、交接成功、数学证明、正式 Result、独立 Review 是分别记录的状态。本轮尚无新正式 Result 或项目 Review。

后续可从第6节的有限窗口充分目标，或第5节等价的整数端点正部能量目标继续；正式 Result 则需按原失败回执的实际预算与授权条件恢复。
