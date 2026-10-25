# R285｜BRC 中央峰隙的显式有效尾界与 Catalan 正权核

状态：AUTHOR_SIDE_EXACT_DERIVATION / ANALYTIC_EFFECTIVE_BOUND / STANDARD_LIBRARY_EXACT_CHECK / DRIVER_UNREVIEWED / NOT_ADMITTED。
日期：2026-10-25；本地研究标记 EM-DIRECT-R285T3（不是原生服务签发的 Researcher-ID 或 CLAIM）；活动 RA-EMT3-20261025-1436-R285TAIL。

## 0. 真实来源、模型和边界

GLOBAL_KNOWLEDGE_V1 当前固定读取快照为私库 awdawmip/chatgpt-global-knowledge main@2487ec77b812748d78d30bf68b3fa407d47a6f70。已经阅读双规范入口、项目 TASK 路由、P000_STARTUP、ACTIVE 我眼中的世界、数学研究、代码、BRC 与活动规则；同一快照内 P000 投影记录的 canonical_blob_sha1=770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc 已与原件文件的 Git blob 完全核对。Enterprise Math Source 基线 main@0cafeda058bb248cfa19bddf02ffeb0f405aff4e，已阅读 portable research、research delivery、activity 和当前控制源合同。

R284 作者侧精确恒等式的不可变研究来源：
https://github.com/awdawmip/enterprise-math/blob/ce4ad0aab996c6310bccb112796325149f75884b/research_notes/r284_unified_central_gap_20261025_t3/R284_UNIFIED_CENTRAL_GAP_AUTHOR_PROOF.zh-CN.md 。
其原始 Laurent 前提追溯 R279/R283；这些是作者侧材料，未经过独立 Driver 数学接纳。

计数对象是正权、有序、完整仿射效果的 BRC 六边形式辅助自动机，初态控制 q=0、效果 (+1,0)，六条 (q,b)→(q',η,c)：
(0,0)→(2,-1,-1)，(0,1)→(2,+1,-1)，(1,0)→(0,-1,-1)，(1,1)→(0,+1,-1)，(2,0)→(1,+1,+1)，(2,1)→(2,+1,-1)。
右复合为 (ε,k)★(η,c)=(ηε,ηk+c)。P_n(ε,k) 是长度 n、不含连续 00、终点 q=0 且完整仿射效果等于 (ε,k) 的来源词数量。二维效果标签不是 P000 原生二维平面，来源长度不是物理心跳时间；所有来源历史、路径重数与控制状态不予物理化或任意约去。

## 1. 精确代数输入与本轮待证目标

记
\[
q(y)=1+y+y^2,\quad h(y)=1-3y+y^2,\quad
\rho=\frac{3-\sqrt5}{2},\quad
p(y)=1-y-2y^3+y^4.
\]
定义
\[
P_7(y)=y^7-6y^6+11y^5-6y^4+4y^3-8y^2+y-1,
\]
\[
P_8(y)=y^8-5y^7+7y^6-3y^5+6y^4-8y^3+y^2-2y+1,\quad A(y)=(y-1)P_7(y).
\]
R284 已有形式支 g(0)=1 的恒等式
\[
g(y)=\sqrt{h(y)/q(y)},\qquad
K(y)=\frac{A(y)-P_8(y)g(y)}{2y(1+y)}. \tag{1}
\]
两种原始中央差值的生成函数：
\[
E(x)=\sum_n(P_n(+1,-4)-P_n(-1,-4))x^n=x^8 K(x^2), \tag{2a}
\]
\[
O(x)=\sum_n(P_n(-1,-3)-P_n(+1,-5))x^n=x^5p(x^2)K(x^2). \tag{2b}
\]
R284 已证明 eventual 严格为正，但没有有效起点。此处建立明确、保守、可复核的全长度充分阈值。

## 2. 定理一：平方根核有正权 Catalan 树展开

取 R284 二次方程中常数项为1的唯一形式根
\[
r(y)=\frac{1+2y^2-y^3-(1-y)\sqrt{q(y)h(y)}}{2y},\qquad
yr^2-(1+2y^2-y^3)r+1=0.
\]
**定理 1。** 令 s(y)=r(y)-1-y，则
\[
\boxed{s=y^4+(2y+y^3)s+ys^2,} \tag{3}
\]
并在整个形式整数幂级数环中有
\[
\boxed{s(y)=\sum_{j\ge0}C_j\,\frac{y^{5j+4}}{(1-2y-y^3)^{2j+1}},
\qquad C_j=\frac1{j+1}\binom{2j}{j}.} \tag{4}
\]
因此对 s_m=[y^m]s，有
\[
\boxed{s_m\ge 2^{m-4}>0\quad(m\ge4),\qquad s_m\ge2s_{m-1}\quad(m\ge5).} \tag{5}
\]

证明：代入 r=1+y+s，逐项整理 yr²-(1+2y²-y³)r+1=0，得到 ys²+(2y+y³-1)s+y⁴=0，即式(3)。置 B(y)=(1-2y-y³)^{-1}，则 s=y⁴B+yBs²；由标准 Catalan 恒等式 C(z)=1+zC(z)² 得 s=y⁴B C(y⁵B²)，展开就是式(4)。各 Catalan 系数为正整数，B 是正系数形式级数；j=0 项 y⁴B 的 y^m 系数至少为 2^{m-4}。逐次取式(3)的 y^m 系数：
\[
s_m=\mathbf1_{m=4}+2s_{m-1}+s_{m-3}+
\sum_{a+b=m-1}s_as_b,
\]
其中所有项非负，所以对 m≥5 有 s_m≥2s_{m-1}。证毕。

该树只描述形式 Green 根的非负组合载体（可解释为长度4叶节点、两种长度1一元边、一个长度3一元边和长度1有序二叉节点），**没有未经证明的原始 BRC 来源词—树双射**。额外准确身份
\[
\boxed{(1-y^3)g(y)=1+2y^2-y^3-2yr(y)} \tag{6}
\]
来自 2yr=a-(1-y)√(qh) 与 (1-y)q=1-y³，可用来独立整数计算原 R284 的 g 系数。

## 3. 定理二：双中央峰隙的显式有效下界

**定理 2。** 对 Q(y)∈{1,p(y)}，对每个整数 n≥10,000,000：
\[
\boxed{[y^{n-1}]Q(y)K(y)>\frac{\rho^{-n}}{2500 n^{3/2}}>0.} \tag{7}
\]
因此：
\[
\boxed{\forall\ L\ge20,000,006,\ L\ \text{偶数}:
P_L(+1,-4)>P_L(-1,-4);} \tag{8}
\]
\[
\boxed{\forall\ L\ge20,000,003,\ L\ \text{奇数}:
P_L(-1,-3)>P_L(+1,-5).} \tag{9}
\]
充分阈值很大且未宣称最小；结论只涉及两对中央效果，不能单独推出全部效果的峰值排序或六通道共同纤维等式。

### 3.1 代数分解

因 h=(1-y/ρ)(1-ρy)，且 q(y)=(1-y³)/(1-y) 的零点都在模1边界，以下在 |y|<1 中取规范解析分支
\[
H(y)=\sqrt{\frac{1-\rho y}{q(y)}},\ H(0)=1,\quad
W(y)=(1-y/\rho)^{1/2}.
\]
定义
\[
U_Q(y)=\frac{Q(y)A(y)}{2(1+y)},\qquad
V_Q(y)=\frac{Q(y)P_8(y)}{2(1+y)}H(y).
\]
由式(1)恒等
\[
yQK=U_Q-V_Q W. \tag{10}
\]
设 c_Q=V_Q(ρ)，V_{Q,1}(y)=(V_Q(y)-c_Q)/(y-ρ)，ρ处的表面奇点可去，整个 |y|<1 内解析；于是精确重写为
\[
\boxed{yQK=U_Q-c_Q W+\rho V_{Q,1}(y)W^3.} \tag{11}
\]
利用 y-ρ=-ρ(1-y/ρ)，这里最后一项符号严格为正；不依靠渐近符号。

### 3.2 主项常数与 Cauchy 系数界

有 3/8<ρ<2/5，7/5<5^{1/4}<3/2，11/5<√5<9/4。原 R284 的精确代数值得
\[
V_1(\rho)/\rho=\frac{5^{1/4}(5-2\sqrt5)}{20},
\quad p(\rho)=5-2\sqrt5\in(1/2,1).
\]
由有理区间相乘可逐个核对（Q=1 或 p）：
\[
\boxed{1/160<c_Q<1/50.} \tag{12}
\]
具体，下界中使用 ρ>3/8、7/5、p(ρ)>1/2：
(3/8)(7/200)(1/2)=21/3200>1/160；
上界使用 ρ<2/5、3/2、p(ρ)<3/5：
(2/5)(9/200)=9/500<1/50。

在复圆 |z|=1/2 上：
\[
|q(z)|=|(1-z^3)/(1-z)|\ge (1-1/8)/(1+1/2)=7/12,
\quad |1-\rho z|<6/5,
\]
故 |H(z)|<√(72/35)<3/2。P8 系数绝对值带权和为
\[
\sum_{j=0}^8|[y^j]P_8|2^{-j}=991/256<4,
\quad \sum_{j=0}^4|[y^j]p|2^{-j}=29/16<2.
\]
又 2|1+z|≥1，因此 |V_Q(z)|<12；因 |z-ρ|>1/10，结合 c_Q<1/50，
\[
\boxed{\max_{|z|=1/2}|V_{Q,1}(z)|<121,\quad
|[y^j]V_{Q,1}|\le 121\cdot 2^j.} \tag{13}
\]
最后一步是 Cauchy 系数公式和同圆最大模界，适用于每个整数 j≥0。

### 3.3 二项式主项下界

令 C_n=binom(2n,n)/4^n，对 n≥1 定义 a_n=C_n/(2n-1)。
二项式展开给
\[
[y^n]W=-\rho^{-n}a_n,\quad
\frac{1}{4n^{3/2}}\le a_n\le \frac{1}{n^{3/2}}. \tag{14}
\]
这里的初等界由 C_{n+1}/C_n=(2n+1)/(2n+2) 归纳得到
1/(2√n)≤C_n≤1/√(n+1)，再以 2n-1 除之，无未指明常数。结合(12)，
\[
\boxed{-[y^n]c_Q W>\frac{\rho^{-n}}{640n^{3/2}}.} \tag{15}
\]

### 3.4 三次根余项界

写 [y^\ell]W³=ρ^{-\ell}b_\ell。可用 W³=(1-y/ρ)W 确切计算：
\[
b_0=1,\quad b_1=-3/2,\quad
b_\ell=a_{\ell-1}-a_\ell=\frac3{2\ell}a_{\ell-1}>0\ (\ell\ge2).
\]
所以 |b_\ell|≤3/2 对全部 ℓ≥0，且 ℓ≥2 时
\[
\boxed{|b_\ell|\le5/\ell^{5/2}.} \tag{16}
\]
置 θ=2ρ<4/5。由式(13)进行 Cauchy 卷积，按 j≤n/2 与 j>n/2 拆项；在前半，ℓ=n-j≥n/2 用 |b_ℓ|≤5/ℓ^{5/2}，后半用 3/2：
\[
\begin{aligned}
\rho^n|[y^n]\rho V_{Q,1}W^3|
&\le \rho\,121\left[
\frac{30}{n^{5/2}}\sum_{j\ge0}\theta^j+
\frac32\sum_{j>n/2}\theta^j\right]\\
&< \frac{7260}{n^{5/2}}+363(4/5)^{n/2}.
\end{aligned}\tag{17}
\]
因 log(5/4)>1/5，且 e^t≥t⁴/4!，对 n≥10^6 有
\[
363(4/5)^{n/2}<363e^{-n/10}
\le\frac{87,120,000}{n^4}\le\frac1{n^{5/2}},
\]
从而
\[
\boxed{\rho^n|[y^n]\rho V_{Q,1}W^3|<7261/n^{5/2}\quad(n\ge10^6).} \tag{18}
\]

### 3.5 有理函数余项与严格裕度

由 A(-1)=76、p(-1)=5，
U_Q(y)=QA/[2(1+y)] 在 n≥13 的系数分别绝对值为38和190，故统一小于200。又 ρ<1/2<e^{-1/2}，用 e^t≥t⁴/4!：
\[
\boxed{\rho^n|[y^n]U_Q|<200\rho^n
<76800/n^4\le1/(2560n^{3/2})\quad(n\ge10^6).} \tag{19}
\]
合并主项(15)、复解析尾项(18)及有理余项(19)：
\[
\begin{aligned}
\rho^n[y^n](yQK)
&>\frac1{640n^{3/2}}-\frac{7261}{n^{5/2}}-\frac1{2560n^{3/2}}\\
&\ge\frac1{n^{3/2}}
\left(\frac1{640}-\frac{7261}{10^7}-\frac1{2560}\right)\\
&=\frac1{n^{3/2}}\frac{17831}{40000000}
>\frac1{2500n^{3/2}}\qquad(n\ge10^7).
\end{aligned}\tag{20}
\]
由于 [y^n](yQK)=[y^{n-1}]QK，式(7)成立。由(2a)，偶数原始长度 L=8+2(n-1)=2n+6；由(2b)，奇数长度 L=5+2(n-1)=2n+3；获得(8)、(9)。证毕。

## 4. 独立精确执行及证据等级

配套 Python 3 标准库程序 R285_verify_effective_gap.py 实际执行：
1. 非负树递推 s=y⁴+(2y+y³)s+ys² 到 m=240；
2. 使用独立 Catalan 有限和逐系数核对 m=4..150；
3. 通过式(6)从正权树求 g，和 R284 另一条一阶 ODE 整数递推比对到 m=240；
4. 从(1)求 K,pK，再与原始六条边、有序来源词、完整仿射效果动态规划在全部 L=0..160 的中央差值比对（偶77层、奇78层）；
5. 使用 fractions.Fraction 精确核对 P8 加权界、p 加权界、指数界所需整数关系以及严格正裕度 17831/40000000 > 1/2500。

运行结果 PASS；程序把详细数据写入 EXACT_EVIDENCE.json。没有逐一计算 n=10^7 的巨大系数；**无限量词由上述解析证明负责**，整数有限程序仅交叉核验系数和证明中数值常数。未执行 Lean 检查或原生 P000 物理实验。

## 5. 下一数学单元及安全边界

R284 对两对中央效果的最终正性，已推进为明确有效的巨大充分长度阈值；Catalan 正权核额外提供全长度可重用正组合式。下一单元优先对全部非中央效果建立统一、具常数的外尾上界或严格保留原始完整效果的路径注入，证明它们不超过上述偶/奇中央候选，以获得真实的有效 N_peak。也可用式(3)—(4)的单调性寻找远小于 2×10^7 的有限正锥/余项证书。此前有限观察 n≥81 不是对全部未来长度的证明。

原生 em_control_tasks=CONTROL_QUOTA，em_session_start=STATIC_READONLY_SCOPE_DENIED、operation_sent=false；因此无法权威确认活跃 Owner，亦没有原生 CLAIM、Source Result、Driver 审查、Working Truth/Foundation 数学接纳。研究结论严格限于正权有序 BRC 辅助模型，不外推 P000 原生 X6 或心跳时间。存储回读仅证实材料持久化，不是数学审查通过。
