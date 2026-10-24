# R261 — Fibonacci 来源效果的精确二阶矩与 BRC 三来源共纤维平方根型下界

2026-10-24 · 作者侧解析证明 / 精确整数核验 · UNREVIEWED / NOT_ADMITTED。形式六轴 BRC 仿射辅助模型结果，不是 P000 原生物理定理。

## 1. 来源快照、类型与目标

本轮 GLOBAL_KNOWLEDGE_V1 固定读取快照：awdawmip/chatgpt-global-knowledge main@7b7bd052c42ed6aaa5641eea28b30435ed63c024；P000 原始 blob：770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc。Enterprise Math 读快照：main@4f7169291a872467496de179666f456e67869749。具体 BRC 源码：
- src/enterprise_math/brc_transport.py，blob be1debe367263931bd5e93fd750be3ed54624fe1；
- src/enterprise_math/brc_control_port.py，blob 44def6b8ac787e798d3cc2c6be16f873f91b9db8。
R260 基础证明：不可变提交 43dc61f43a73cf6b0ec535c01efedd5067400fc2，已在本轮实际读取。复用 Affine.then、EffectHistogram.then、ControlPacket 的确切有序正重数作用律，属于 REUSE_APPLIED；原版 Python 包本轮未 import / execute，不能称原生接口测试成功。

固定的 R260 有限非空间控制 q∈{0,1,2} 与二元正权来源选择器 a∈{0,1}。每个源边权重1，转移 (q',eta,b) 为：

| q | a=0 | a=1 |
| --- | --- | --- |
| 0 | (2,-1,-1) | (2,+1,-1) |
| 1 | (0,-1,-1) | (0,+1,-1) |
| 2 | (1,+1,+1) | (2,+1,-1) |

边对完整六轴仿射载体施行 diag(eta,eta,1,1,1,1) 及平移 (b,0,0,0,0,0)。子载体的完整作用可忠实记为 (epsilon,k)，按 BRC Affine.then 后续一步更新：

$$
(\epsilon,k)\ \mathrm{then}\ (\eta,b)=(\eta\epsilon,\eta k+b).
$$

来源 DFA r∈{0,1,2} 分别表示：尚无 00 且末位不是0；尚无 00 且末位是0；已出现 00（吸收）。初态 (q,r)=(0,0)。对长度 m 的全部有序二元来源词，以末端原始控制 q 与完整六轴效果 (epsilon,k) 为共同纤维，记三种终态来源模式的正整数词数 n_r(m;q,epsilon,k)，定义

$$
M_m=\max_{q,\epsilon,k}\min(n_0,n_1,n_2).
$$

R260 已证明 log M_m /m→log φ，其中 φ=(1+√5)/2；本轮收紧多项式下界，未改变观察人口、作用顺序或三模式定义。

## 2. 四状态有限 BRC 来源传播和矩递推

记 A_L 为所有长度 L、无连续 00 且末位是1的词，N_L=|A_L|=F_{L+1}，F_0=0,F_1=1。令 k(w) 是完整六轴仿射效果的平移参数，定义 U_L=Σ_{w∈A_L}k(w)，V_L=Σ_{w∈A_L}k(w)^2。

在该词族上，联合 (q,last) 只有四个可达状态，按顺序 A=(0,1), B=(2,0), C=(2,1), D=(1,0)。有向边及 (eta,b)：
A→B:(-1,-1), A→C:(+1,-1), B→C:(+1,-1), C→D:(+1,+1), C→C:(+1,-1), D→A:(+1,-1)。

用行=目的状态、列=起点的顺序 (A,B,C,D)，定义矩阵

$$
T=\begin{pmatrix}0&0&0&1\\1&0&0&0\\1&1&1&0\\0&0&1&0\end{pmatrix},\quad
S=\begin{pmatrix}0&0&0&1\\-1&0&0&0\\1&1&1&0\\0&0&1&0\end{pmatrix},
$$

$$
B=\begin{pmatrix}0&0&0&-1\\-1&0&0&0\\-1&-1&-1&0\\0&0&1&0\end{pmatrix},\quad
C=\begin{pmatrix}0&0&0&-1\\1&0&0&0\\-1&-1&-1&0\\0&0&1&0\end{pmatrix}.
$$

T 汇集边重数，S 汇集 eta，B 汇集 b，C 汇集 eta b。以 n_L,u_L,v_L 分别表示四状态各自的词数、平移一阶和、平移平方和，则取 n_0=e_A、u_0=v_0=0，原生子载体整数律 k'=eta*k+b 严格逐边给出：

$$
n_{L+1}=Tn_L,\quad u_{L+1}=Su_L+Bn_L,\quad
v_{L+1}=Tv_L+2Cu_L+Tn_L.
$$

末位1只在 A、C，故 (1,0,1,0) 点乘这三个向量依次为 N_L、U_L、V_L。把 n(z)=(I-zT)^{-1}e_A、u(z)=z(I-zS)^{-1}Bn(z)、v(z)=z(I-zT)^{-1}(2Cu(z)+Tn(z)) 代入并在有理函数域化简，得到三个**精确形式幂级数恒等式**：

$$
\boxed{N(z)=\sum_{L\ge0}N_Lz^L=\frac1{1-z-z^2}}
$$

$$
\boxed{U(z)=\sum_{L\ge0}U_Lz^L=
\frac{z(z^2-2z-1)}{(1-z)(1-z^3)(1-z-z^2)}}
$$

$$
\boxed{V(z)=\sum_{L\ge0}V_Lz^L=
\frac{z(1+6z+2z^2-z^3)}{(1-z^3)(1-z-z^2)^2}.}
$$

无需独立的随机过程假设，也未把正质量转成复幅抵消。随附验证程序严格校验矩阵、有理函数、正权直方图的相等性。

## 3. 精确均值极限与线性方差率

令 ρ=φ^{-1}=(√5-1)/2。上述有理式所有其他极点模长严格大于 ρ，N(z) 和 U(z) 在 ρ 为单极点，V(z) 在 ρ 为二阶极点。用部分分式或 Binet 系数的主极点项可严格推出：

$$
\boxed{\lim_{L\to\infty}\frac{U_L}{N_L}=-\frac{9+3\sqrt5}{4}}
$$

$$
\boxed{\lim_{L\to\infty}\frac{V_L}{L N_L}=
\sigma^2:=\frac32+\frac{7\sqrt5}{10}.}
$$

第一式由 U/N 在 ρ 的解析因子求值；第二式由 V 的二阶极点首项与 N 的单极点首项之比求得。均值有有限极限，因此

$$
\lim_{L\to\infty}\frac{\mathrm{Var}_{w\in A_L}(k(w))}{L}=\sigma^2.
$$

也可直接由 det(xI-T)=(x²+1)(x²-x-1)、det(xI-S)=(x-1)²(x²+x+1) 及 (S³-I)²=0 验证 ||T^L||=O(φ^L)、||S^L||=O(L+1)，从上述矩递推得到 ||u_L||=O(φ^L)、||v_L||=O(Lφ^L)。因此这个二阶矩界是无限长度定理，不是有限采样外推。尚未证明 k 的局部中心极限定理。

## 4. 单个长词块即得平方根型共纤维下界

因为每个原始来源边 eta,b∈{±1}，k'=eta*k+b 归纳给出 k(w)≡L(mod2)。对于任意 L≥1 令

$$
R_L=\left\lceil\sqrt{\frac{2V_L}{F_{L+1}}}\right\rceil.
$$

对上述**有限正整数路径人口**直接施加 Markov 不等式，至少 F_{L+1}/2 条词满足 |k(w)|≤R_L。在这个区间里，因 k≡L(mod2)，可能 k 值最多 R_L+1 种；epsilon 只有两种，故完整六轴效果最多 2(R_L+1) 种。鸽巢原理给出至少

$$
H_L=\left\lceil\frac{F_{L+1}}{4(R_L+1)}\right\rceil
$$

条不同词共享同一个完整六轴 affine 效果 (epsilon,k)。无需中途 q 也相同。

R260 已逐原始 q 验证同步词 s=1101：从 q=0,1,2 都返回 q=0，完整仿射效果恒为 (+1,-2)；s 以1开头、以1结尾且无 00。上述所选 H_L 条 w∈A_L，追加 s 后均从初态 (q,r)=(0,0) 到同一 (q,r)=(0,0)，且效果变为 (epsilon,k-2)。再追加 R259/R260 已核验的三个长度7后缀：

| 来源模式 | 后缀 |
|---|---|
| r=0 | 1110101 |
| r=1 | 1011010 |
| r=2 | 0000000 |

它们从 (q,r)=(0,0) 出发终止于同一个 q=2、同一完整仿射效果 (-1,+1)，分别保留三种互异的原始来源 r 模式。因此每个选中的 w 在三个模式的同一 (q,epsilon,k) 纤维都贡献1条不同正权来源路径。长度恰为 L+11：

$$
\boxed{
M_{L+11}\ge \left\lceil
\frac{F_{L+1}}
{4\left(\left\lceil\sqrt{2V_L/F_{L+1}}\right\rceil+1\right)}
\right\rceil,\qquad L\ge1.}
$$

这是每个 m≥12 的精确整数构造证书。由 V_L/(L F_{L+1})→σ² 及 F_{L+1}~φ^{L+1}/√5，立即得到

$$
\boxed{\liminf_{m\to\infty}\frac{\sqrt m\,M_m}{\phi^m}
\ge\frac{\phi^{-10}}{4\sqrt5\sqrt{2\sigma^2}}>0.}
$$

即 **M_m=Ω(φ^m/√m)**。这实质加强 R260 仅对固定复位块迭代证明的最优指数率；但上界目前仍只有 M_m≤F_m=O(φ^m)，没有证明匹配的 O(φ^m/√m)，亦不宣称真实最优多项式修正。

## 5. 已执行验证及精确剩余问题

本轮在本地对完整正整数 BRC 六轴 affine 子载体执行：
- SymPy 有理函数等式3项、特征多项式2项和 (S³-I)²=0；
- L=0..256 共257个长度的原始无00词效果直方图与三矩递推逐项一致（并核对奇偶及有限保守下界）；
- 长度0..10 共2047条未经合并的完整原始词与正权递推逐项相等；
- m=12..128 共117个深度的全部三来源共纤维 M_m 与新构造界比对通过。
- 有限检查 V_L≤4 L F_{L+1} 对 L=1..256 成立，但**未**把这257轮提升成普遍不等式。

验证程序保存确切 q、r、epsilon、k 与正整数路径重数，后者是六轴 affine 对角子载体的完整效果参数，不是把原生 X6 空间降为二维。完整原始 enterprise_math Python 包未在本轮执行；本轮 R193 原始来源、查询和时间端口保真映射仍未知，不能称物理心跳证明。

最小下一问题：为每个 m 的 r=1 来源边际证明一致的效果反集中界，研究 M_m=O(φ^m/√m) 是否成立；或者取得 R193 的确切端口、证明/反驳保真嵌入。所有成果保留 AUTHOR_SIDE / DRIVER_UNREVIEWED / NOT_ADMITTED 状态，P000 不修改。
