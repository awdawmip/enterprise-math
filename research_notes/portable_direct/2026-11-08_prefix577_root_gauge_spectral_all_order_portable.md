# PREFIX-577/X6-BRC: 根端点变换的谱共轭、闭环保真与全阶累积量

2026-11-08｜作者级可移植数学结果｜`AUTHOR_DERIVED / UNREVIEWED / NOT_ADMITTED`

科学输入 pin：`f42f2906d77f24085c123f3ccfe9667d41caa96d`。严格依赖已发布的 [PREFIX-577-R6 逐边根端点恒等式](https://github.com/awdawmip/enterprise-math/blob/b64eb309fabe71f532faa1ef92c8bb63a48aa792/research_notes/portable_direct/2026-11-08_prefix577_r6_six_axis_gate_covariance.md)，该文件 blob `85be91e54c5c042bd7fb3f31c03ac9907b32c983`；作者原证书 blob `2784c78e6acc2a696f75a011628925223a51ddc3`。当前结果是该前沿的代数扩展，不将现有 R6 数值验证冒充本轮独立复算。

## 定理（原生96端口，保留全部六轴标签和门控位）

原生端口有六条等概率、保留动作标签的转移。根 `r` 的七维边奖励为 `w_r(i,a)=(q_{1,r},...,q_{6,r},k)`。既有已核验边恒等式为

\[
w_r(i,a)=w_0(i,a)+\Phi_r(j(i,a))-\Phi_r(i),\qquad
\Phi_r(i)=(\phi_{1,r}(i),...,\phi_{6,r}(i),0),
\]

其中 `φ_{l,r}(i)=1{c_i=r_l l}`（`r_l=0` 时为0），每一端口只有一个带符号相位轴，故各 `φ` 取0/1且 `Σ_l φ_{l,r}(i)≤1`。此恒等式对项目九个冻结根成立；原作者还检查过全部729个三值代数根，后者不扩大冻结科学输入。

对正实数或形式 Laurent 变量 `x=(x1,...,x7)`，定义

\[
T_r(x)_{ij}=\sum_{a:i\to j}\tfrac16 x^{w_r(i,a)},\qquad
D_r(x)_{ii}=x^{\Phi_r(i)}.
\]

则在 `Q[x_1^{±1},...,x_7^{±1}]` 上

\[
\boxed{T_r=D_r^{-1}T_0D_r}.
\]

**证明：** 每个带标签的边上 `x^{w_r}=x^{w_0}D_r(j)/D_r(i)`。以固定 `i,j` 汇总平行边后即得矩阵逐项恒等式。因而对每个整数 `d≥1`，

\[
\boxed{\operatorname{tr}(T_r^d)=\operatorname{tr}(T_0^d)},\qquad
\boxed{\det(I-zT_r)=\det(I-zT_0)}.
\]

闭环的七维奖励联合生成函数、全部闭环迹以及相应形式有理循环 zeta 因此**有限深度严格相同**。这保留原生端口、动作标签和七个联合观察量，并未把它们降为标量质量。

对从任意固定端口出发的长度 `d` 开放路径，严格有

\[
W_r(d)-W_0(d)=\Phi_r(X_d)-\Phi_r(X_0).
\]

每条轴计数差的绝对值 ≤1，门控总数不变，且 `|Σ_{l=1}^6W_{r,l}(d)-d|≤1`。设 `L(t)=Σ_{l=1}^6|t_l|`，则对每个实参数 `t∈R^7`：

\[
e^{-L(t)}\mathbb E_i e^{t\cdot W_0(d)}
\le\mathbb E_i e^{t\cdot W_r(d)}
\le e^{L(t)}\mathbb E_i e^{t\cdot W_0(d)}.
\]

故两根的每步归一化 log-MGF 误差绝对值 ≤`L(t)/d`。

原作者已按96原生端口验证有限转移图不可约。对任意实 `t`，正赋权的 Perron 根存在，且相似性给出**完全相同的谱压力**：

\[
\boxed{\Lambda_r(t):=\lim_{d\to\infty}d^{-1}\log\mathbb E_i e^{t\cdot W_r(d)}
=\log\rho(T_0(e^t))}.
\]

其凸共轭大偏差速率函数根无关。有限不可约马尔可夫加性过程的实解析 Perron 分支（若有周期，先按周期分解）还给出任意固定阶的渐近联合累积量率为相同的 `∂^m\Lambda(0)`。开放路径的**有限深度分布**可以随根改变，故不主张其精确分布相等。

## 六轴守恒对三阶计算的精确约简

令 `u=(1,1,1,1,1,1,0)`。零根每条原生动作恰好一个轴计数为1，因此 `T_0(e^{t+θu})=e^θT_0(e^t)`。谱共轭给出全部许可根统一的

\[
\boxed{\Lambda(t+\theta u)=\Lambda(t)+\theta}.
\]

从而 `u·∇Λ=1`，对所有 `m≥2`，渐近 m 阶联合累积量张量的任意一个指标与 `u` 收缩均为0。七变量对称三阶张量有 `C(9,3)=84` 个坐标；用六轴守恒消去 `R6`，只需至多 `C(8,3)=56` 个 `(R1,...,R5,K)` 坐标。重建规则为

\[
\kappa^{(3)}_{6,b,c}=-\sum_{a=1}^5\kappa^{(3)}_{a,b,c},
\]

对重复下标6依次递归。56是守恒约束下的结构性上界；额外对称性还可能进一步简化。

## Provenance / 接续

本证明只使用前引原生边恒等式、有限图不可约性和已验证的零根一步守恒，不重复作者的576条边、672条Poisson方程或数值协方差计算。保留原作者和贡献史；本文件是共享来源后的**作者级推导**，不是独立盲审，未取得本次运行的原生 Source session、winning CLAIM、Result、Review 或 Working Truth。

下一有用科学动作是在冻结96端口核上计算/验证56个三阶独立坐标，先与既有 PREFIX-578-R2 的 `q5,q6,gate` 三阶混合项核对并避免无 CLAIM 重复研究。共享合同侧先恢复原请求与 exact continuation，再决定是否纳入正式 Source 前沿。

UR V2 原始 bundle 仍待真实字节恢复：`94687 bytes`，SHA-256=`4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76`。历史四份其他证据并非这个 bundle；Source Gateway 目前 `STATUS_DATABASE_UNAVAILABLE`、研究授权未授予，须由获准维护路径修复后补合法 writer/provenance/checkpoint。此 GitHub 文件是中立作者证明存档，不是正式 Source checkpoint。
