# R291 — BRC 清洁纤维负平移外尾的双参数全长度正性锥

日期：2026-10-26。证据等级：作者侧形式幂级数证明，依赖 R288/R290 的精确核，未经独立 Driver 审核或原生 Source 数学接纳。

## 1. 精确数学对象

采用 R268–R290 的正权、有序、无相邻 00 六边 BRC 辅助自动机，初始控制态 q=0、仿射效果 (+1,0)，终控制态 q=0，右复合 (ε,k)★(η,c)=(ηε,ηk+c)。原始来源词每条权 1，完整效果不合并。P_n(ε,k) 是上述限制下的原始词计数。x、y 仅是形式长度变量，并非原生空间轴或时间。

沿用 R288/R290 作者侧的精确代数恒等式，置 y=x²，令唯一 h∈y⁴ ℕ[[y]] 满足

$$
h=y^4+(y+2y^2+y^3+y^4)h+y(1+y)^2h^2,
\qquad w=(1+y)(1+h)=1+y+O(y^4).
$$

右侧递推逐级提升 y 阶数且系数非负，因此 h、w 的系数均非负。定义

$$
\Delta_m^\epsilon(x)=\sum_{n\ge0}\bigl(P_n(\epsilon,-m)-P_n(\epsilon,-m-2)\bigr)x^n
=x^{m+2}G_m^\epsilon(y).
$$

精确公式为

$$
G_m^-(y)=(1+h)w^{m-2}(1-yw),\quad m\ge2;
\qquad
G_m^+(y)=(1+h)w^m(1-y+y^2-yw),\quad m\ge1.
$$

它们是 R290 的 G_m^- = w^{m-1}(1-yw)/(1+y)、G_m^+ = w^{m+1}(1-y+y²-yw)/(1+y) 利用 w=(1+y)(1+h) 的代数改写，不改变计数语义。

## 2. 一般系数比较引理（对所有长度）

设任意形式级数 W(y)=1+y+Σ_{d≥2}a_d y^d，a_d∈ℕ，令 t=W−1，A_{r,j}=[y^j]W^r。若整数 j≥1、r≥j、q≥1 且

$$
\boxed{(r-j+1)(r-j+2)\ge qj(r+1)},\tag{C_q}
$$

则对全部 1≤i≤j，有

$$
A_{r,i}\ge qA_{r+1,i-1}.
$$

若 (C_q) 严格，则对应不等式全部严格。

证明：令 c_{\ell,d}=[y^d]t^\ell。t_1=1 且 t 全系数非负，故 c_{\ell+1,d+1}≥c_{\ell,d}。逐项展开：

$$
A_{r+1,i-1}
=\sum_{\ell=1}^{i}\binom{r+1}{\ell-1}c_{\ell-1,i-1}
\le\sum_{\ell=1}^{i}\binom{r+1}{\ell-1}c_{\ell,i},
$$

$$
A_{r,i}=\sum_{\ell=1}^{i}\binom r\ell c_{\ell,i},\qquad
\frac{\binom r\ell}{\binom{r+1}{\ell-1}}
=\frac{(r-\ell+1)(r-\ell+2)}{\ell(r+1)}.
$$

右端比率随 ℓ 递减，因此 (C_q) 在 ℓ=j 成立就保证所有 ℓ≤i≤j 的比较。严格性来自 c_{i,i}=1 及末端严格的二项式系数比较。证毕。

便于使用的统一、严格充分条件是 r≥3j 对 q=1、r≥4j 对 q=2；直接代入得到 (2j+1)(2j+2)>j(3j+1) 和 (3j+1)(3j+2)>2j(4j+1)。

## 3. BRC 双参数高位移正性定理

对所有整数 j≥0，合法 m（负效果符号 m≥2，正效果符号 m≥1）：

$$
\boxed{m\ge3j+2\Longrightarrow[y^j]G_m^->0},\qquad
\boxed{m\ge4j\Longrightarrow[y^j]G_m^+>0}.
$$

更精确的非负系数充分条件：负号 r=m−2≥j 且 (r−j+1)(r−j+2)≥j(r+1)；正号 r=m≥j 且 (r−j+1)(r−j+2)≥2j(r+1)。

证明：令 A_{r,i}=[y^i]w^r，采用上节 W=w。对负号，(C_1) 保证

$$
[y^i]w^r(1-yw)=A_{r,i}-A_{r+1,i-1}\ge0\quad(0\le i\le j).
$$

正号中用 A_{r+1,i-1}≥A_{r,i-1} 和 A_{r,i-2}≥0，(C_2) 保证

$$
[y^i]w^r(1-y+y^2-yw)
=A_{r,i}-A_{r,i-1}+A_{r,i-2}-A_{r+1,i-1}
\ge A_{r,i}-2A_{r+1,i-1}\ge0.
$$

因 (C_q(r,j)) 蕴含所有 i≤j 的相应条件，两种被乘式在完整前缀 0..j 内均非负。再与 (1+h)∈1+y⁴ℕ[[y]] 相乘，卷积仍非负；严格条件保留常数项1所带来的严格正性。j=0 时 G 的常数项均为1。证毕。

## 4. 在原始长度 n 下的统一负平移单调范围

因为 Δ_m^ε=x^{m+2}G_m^ε(x²)，当 n=m+2+2j 且 j≥0 时，上述严格不等式成为

$$
\boxed{
P_n(-1,-m)>P_n(-1,-m-2)
\quad\text{若 }m\ge2,\ 5m\ge3n-2,\ n\equiv m\pmod2,\ n\ge m+2;
}
$$

$$
\boxed{
P_n(+1,-m)>P_n(+1,-m-2)
\quad\text{若 }m\ge1,\ 3m\ge2n-4,\ n\equiv m\pmod2,\ n\ge m+2.
}
$$

若 n<m+2 或 n−m 奇偶不合，Δ 的该长度系数为0。因此对固定 n，负号从 m≥max(2,ceil((3n−2)/5))、正号从 m≥max(1,ceil((2n−4)/3)) 起（分别选 m≡n mod 2），沿同奇偶 m,m+2,... 单调不增。这给出了随 n 线性增长的、**无条件**负位移搜索截止界。结合 R286 正平移镜像支配可把全局峰值搜索限制到两条明确的线性窗口，但不能将它误称为常数大小的 26 候选窗口。

(C_q) 的精细界带来更小的充分斜率：当 j→∞，r/j 的最小边界分别趋于 (3+√5)/2 ≈2.618034（负号）与 2+√3 ≈3.732051（正号）；对应 m/n 比值的充分下界约为0.566915、0.651085。这不是模型真正符号阈值的最优性主张。

## 5. 可复算证据与证据等级

实际执行 Python 标准库无界整数验证器 R291_verify_coefficient_cones.py：构造 h、w 至 y^70 和 w^r 至 r=286，测试整数二项式不等式4970组、严格线性正锥系数23216项、精细二次正锥系数25009项。独立六边来源词动态规划按完整仿射右复合、禁止相邻00、终态0计算 n≤100，交叉核对12019项 Δ；全部 PASS。G^-_11、G^+_13 首十整数系数与 R290 机器证据一致。

无限长度证明由第2—4节的通用组合引理承担，而不是有限样本外推。基础代数核仍依赖尚未经独立 Driver 接纳的 R288/R290 作者侧证明；两个固定基底 G^-_11 和 G^+_13 的全系数非负性尚未证明。本轮没有给出无条件26效果窗口、N_peak、B_n=Λ_n 或 P000 原生六维 Cell 物理定律。

## 6. 溯源、权限与下一问题

固定账户快照 GLOBAL_KNOWLEDGE_V1 main@e8d65b2492cf35be071c32b0c9852487f100be07；已读两个入口、TASK_RESEARCH 项目路由、P000_STARTUP、原始P000（Git blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc）、ACTIVE 世界观和数学/BRC/研究活动规则。Enterprise Math 控制基准 main@4d28408cef0576cbfed2e8d709d6c1c004ad83e7，已读 portable research 协议及 BRC-only 约束。认证 GitHub 身份 awdawmip，原生控制 em_control_tasks 返回 CONTROL_QUOTA、em_session_start 返回 STATIC_READONLY_SCOPE_DENIED（operation_sent=false），无权威活跃 owner、无正式 CLAIM、Source Result 或独立 Driver 审查。研究活动是独立标明的本地作者活动，不是假冒原生 Researcher 会话。

下一数学单元：用 L=(1−y)h≽0、T_6≽0 与 R285 有理正锥，证明 G^-_11 和 G^+_13 全系数非负。R291 已证的线性外尾锥可直接复用，剩余中低位移区域仍为未决。不得把辅助BRC结论提升为原生物理结论。

状态：R291_UNIFORM_TWO_PARAMETER_CONE_AUTHOR_PROVED / EXACT_INTEGER_AND_RAW_DP_PASS / FIXED_BASE_FULL_POSITIVITY_PENDING / OWNER_UNVERIFIED / DRIVER_UNREVIEWED / NOT_ADMITTED。
