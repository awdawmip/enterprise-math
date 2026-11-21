# 黎曼猜想新证明材料与进取数论方法提取

Date: 2026-11-21 (Asia/Hong_Kong)
Researcher-ID: EM-DIRECT-B5750A / TASK_RESEARCH
Research-Activity-ID: RA-60C6D083A81B19084A74C5BA
Session: MCP-a062a52181bd433e8f8e1c9c7bacffb7
Status: EXTERNAL_SOURCE_REVIEW_AND_AUTHOR_CHECKED_FINITE_METHOD_HARVEST
Project scientific source: awdawmip/enterprise-math@9fc068244e4f1117f1e75df5eb0285c6697d21d7
Global entry snapshot: awdawmip/chatgpt-global-knowledge@8d85f8ea9284279e5ac5b011eea223414c9719a6
Project Review: NOT_REVIEWED; no Foundation promotion or shared Task completion claimed.

## 1. 找到了什么

2026-11-20，Levent Alpöge 发布四页说明及完整 Lean 工程，主张证明通常的 RH 及 Dirichlet L 函数的 GRH。本轮已读作者说明的检索原文、代码总定理和若干依赖入口，并读取独立核验者发布的具体结果。

本轮核到的 Andrew Sutherland 原始核验页更新时间为 2026-11-20 19:45 UTC，即香港时间 2026-11-21 03:45。该页报告全部 175,187 模块编译、主定理三项标准公理审计、逐模块 Lean 内核检查及 nanoda 完整导出检查通过；其他完整交叉检查仍在推进。这里记录的是核验者的报告；本轮没有在本地重建整个 Lean 工程。更晚二手报道中的新增检查状态尚未与可读一手版本对齐，因此未用于本记录。

材料入口：

- 作者说明：https://alpo.ge/remark.pdf
- 原始 Lean 分卷：https://alpo.ge/lean.tar.gz.part01 至 https://alpo.ge/lean.tar.gz.part14
- 独立核验：https://math.mit.edu/~drew/grh/
- 原码镜像：https://github.com/CocoSgt/riemann-hypothesis-lean/tree/7cbf7a0c32fca1badf05931879a37c3f8a2b03b4
- 另一个核验工程：https://github.com/Deicyde/riemann-hypothesis

作者完整的简明人类可读证明还在整理。本轮取得的是实际形式证明代码和研究路线说明。

## 2. 可直接检查的代码主线

在上面的固定镜像提交：

- src/Statements.lean：只导入 Mathlib，使用真正的 riemannZeta 与 DirichletCharacter.LFunction。
- src/Main.lean：riemannHypothesis : RiemannHypothesis := rhOfAll。
- src/Supplements/Kernels/MainTheorems.lean：allChi 接 UpperTheory.FinalTheorems.everyCharacter，rhOfAll 接 Formalism.VW.rh_of_every。
- src/Development/AutomorphicArithmetic/CharacterBoxes/MainConclusion.lean：将 everyCharacter_of_row 接到 galoisLocalGlobalStrong_recParameter，并消费 every_character_of_literature_of_vWin。
- src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/EveryCharacterOfLiteratureOfVWin.lean：后续精读的承重接口。
- src/Formalism/GammaFactorNonvanishing/CritLine.lean：右半平面非零性到临界线的函数方程桥接。

这里的“GRH”范围为 Dirichlet L 函数。核心目标是 Re(s)>1/2 的非零性，再用函数方程把临界带左侧可能零点反射到右侧；模数为 1 给通常的 ζ 函数。

## 3. 作者路线的简要提炼

作者从有限域路径二次式与角色和出发，用 Parseval 控制非零频率；再以 theta 提升链模拟所需重数。长度 X 的加权和对应约 sqrt(X) 层。提升的范数、层级成本和整除收益必须共同计算；作者记载朴素代价停在 2/3，后续加入跨 Hecke 角色整结构、额外平均和近正交等处理。

可迁移的研究原则是：把强全局约束拆成可以重复组合的局部操作，同时证明每一层的净收益及原观察量的保真性。theta 的消失重数、BRC 的分支条数、矩的阶数与 X6 空间维数各有自己的类型。

以上来自作者路线概述。以下各节是本轮自行展开的有限模型和迁移建议。

## 4. 主项—残差恒等式：有限路径模型

取素数 q，x_i∈F_q，权重 t:F_q→R。定义

Q_k(x)=Σ_{i=1}^{k−1}x_i x_{i+1},
M=Σ_x t(x),
N=Σ_{Q_k(x)=0}∏_i t(x_i),

S_h=Σ_x (∏_i t(x_i)) exp(2πi h Q_k(x)/q),
R=Σ_{h≠0}S_h.

角色正交关系给出

qN=M^k+R.

证明：Σ_{h mod q}exp(2πi h u/q) 在 u=0 时为 q，其他时候为 0。先对 h 求和得到 qN；先分离 h=0 得到 M^k+R。

这是一条精确离散恒等式。主项来自零频率，残差来自全部非零频率。无需假定随机性。

若 |t|≤1，则非零 h 的 Fourier 矩阵 A_h(x,y)=exp(2πi hxy/q) 满足 A_h A_h*=qI。将链和写成两端向量与 k−1 个 Fourier 矩阵及中间对角权重矩阵的乘积，可得 |S_h|≤q^((k+1)/2)，从而 |R|≤(q−1)q^((k+1)/2)。这是本轮的直接粗界，不冒充原工程中的精细 Parseval 估计。

## 5. 有效秩精确控制双线性残差

令 B 为 F_q 上 r×s 矩阵，k=r+s，d=rank(B)，Q(a,b)=aᵀBb。所有变量取遍整个有限域，权重均为 1。记 N_y 为 Q=y 的解数。

对每个 h≠0，

S_h=q^(k−d).

证明：先对 b 求和。Bᵀa≠0 时角色和为 0；Bᵀa=0 时为 q^s。核共有 q^(r−d) 个 a。

反演后，

N_0=q^(k−1)+(q−1)q^(k−d−1),
N_y=q^(k−1)−q^(k−d−1)  (y≠0),

R=qN_0−q^k=(q−1)q^(k−d),
R/q^k=(q−1)q^(−d).

所以在这个明确模型中，决定相对残差的是有效秩 d。该证明对 q=2 也有效，不涉及除以 2。

路径按奇偶顶点分成两部，B 有秩 floor(k/2)，因而

N_0=q^(k−1)+(q−1)q^(ceil(k/2)−1).

这里是标准有限域线性代数的直接应用；本轮贡献是具体提取、与原问题的对接及复算，不宣称一般线性代数公式为项目新发现。

### 四节点的辨识性例子

模数为 5，变量总数为 4，完整赋值有 625 个。

| 耦合 | B | 秩 | 各相位计数 N_0,…,N_4 | R=5N_0−625 |
|---|---|---:|---|---:|
| 四节点路径 | [[1,0],[1,1]] | 2 | [145,120,120,120,120] | 100 |
| 增加闭合边成为四环 | [[1,1],[1,1]] | 1 | [225,100,100,100,100] | 500 |

增加耦合项改变了总观察量，并不等于在原方程之外增加一条独立方程。此例表明更多连接可能产生线性依赖；它给我们一个检查净独立性的精确试验。

## 6. 任意整数模数：Smith 不变量揭示模层结构

令 B 为整数 r×s 矩阵，k=r+s，非零 Smith 不变量为 d_1,…,d_ρ，模数 m≥2。定义

S_h=Σ_{a,b mod m} exp(2πi h aᵀBb/m).

则对全部 h mod m，

S_h=m^(k−ρ)∏_{i=1}^ρ gcd(h d_i,m).

证明：整数可逆变换在模 m 上仍为双射，将 B 化成 Smith 对角形。先对 b 求和后只需计算 hBᵀa=0 的核。每个非零对角项贡献 gcd(hd_i,m) 个解，其余自由变量贡献 m，最后乘上 b 求和给出的 m^s。

因此 N_0=(1/m)Σ_h S_h 可用纯整数计算。这个公式保留合数模数、不可逆因子和各层整除性，适合残差模层研究。

脚本用 6 个指定整数矩阵及 m∈{4,6,8,9,10,12} 共 36 组，逐一核验全部 h 的核计数，并以直接枚举核对 N_0。一般命题由上述证明支持，实验只覆盖所列范围。

## 7. 与 BRC 的具体连接：保留未来仍会用到的端点与相位

对给定允许集合 A⊆Z/mZ，设 C_j(u,r) 统计长度 j、末端为 u、累计路径相位为 r 的历史条数。精确更新是

C_(j+1)(v,r)=1_A(v) Σ_u C_j(u,r−uv),

初值 C_1(u,0)=1_A(u)。

此状态有 m² 个位置，保留了原路径问题所需的下一步交互。若未来操作仅为按同一规则追加端点、最终只观察累计相位，递推由 (u,r) 唯一决定，故可安全合并具有相同 (u,r) 的历史并保留重数。仅保留 r 时，u=0 与 u=1 在追加 v=1 后产生不同结果，故不能直接合并。

一个与已有权重直方图接口有关的例子：模 5、长度 3、所有分支权重为 1。A={0,1} 与 A={1,2} 的分支数量、权重直方图及全部权重矩相同，但相位分布分别为

[5,2,1,0,0] 和 [0,2,1,3,2].

权重直方图保留它声明的权重信息，算术耦合读出还需要标签/相位。现有 BRC 代码的适用范围因此得到尊重，并明确了应补的状态。

在进取数论中，这些是原生 X6 载体上的有类型辅助观察和记忆字段，不增加空间轴。外部 Fourier 表示作为已声明的计算工具使用；本轮没有把路径 toy model 的边或维数改写为原生空间公理。

## 8. 与我们既有 RH 能量路线的连接

本轮读取的正本：

- research_notes/COMPOSITE_ROAD_RH_PURE_POSITIVE_ENERGY_20260906.md
- research_notes/COMPOSITE_ROAD_RH_RESEARCHER_HANDOFF_20260909.md

共同科学快照为本文件页首的 EM 提交。该路线保留完整整数总体：

R_a(n)=∏_{p|n}(1−p^(−a)),
c_a=1/ζ(1+a),
S_a(x)=Σ_{n≤x}R_a(n),
E_a(x)=S_a(x)−c_ax,

Q_a=∫_0^∞ |E_a(x)−1_[1,∞)(x)|² dx/x².

原研究给出 RH⇔Q_a=O(a) 的等价接口，及离散形式

B_(a,N)=S_a(N)−1−c_a(N+1/2),
Σ_N B_(a,N)²/N²=O(a).

本轮沿用其原研究状态与符号，没有重新审查全部解析依赖；E_a(x) 是误差函数，Q_a 才是能量。

既有记录指出两个具体缺口：

1. fixed-origin/anchored cross-frequency coherence：平移平均会抹掉固定起点下的交叉相位；
2. escaping horizon：要统一控制 N≥M(a)、M(a)→∞ 的无限尾项。

这次最可迁移的想法是让结构提升深度与 a,N 联动，并核算每层的净收益。外部 sqrt(X) 不自动决定我们应取的 k(a,N)。

一种清楚的尾项目标是令 H_j(a)=Σ_{2^j≤N<2^(j+1)}B_(a,N)²，寻求

4^(−j)H_j(a)≤C a 2^(−η(j−J(a)))  (j≥J(a), η>0)

且 C,η 具有所需的统一性。求和即可给出 O(a) 的尾界；前段仍须另行控制。这是本轮提出的充分条件型研究目标，尚未证明该估计。

## 9. 提升应追求什么净收益

一个可手算的整数原型：

A_k∈Z，D_k|A_k，|A_k|<D_k  ⇒  A_k=0.

我们要找的是能增加有效整除阶，同时使大小上界增长较慢的结构。单纯 A_k=2^kA_0 会同时放大整除性与大小，不产生这样的净收益。这个原型说明应记录什么，不声称它已经复现自守证明的具体引理。

可从现有 BRC 复用的接口：

- 精确权重直方图、原长度与素数赋值坐标：
  definitions/ENTERPRISE_BRC_UNIVERSAL_HISTOGRAM_FOUNDATION_20260903.md
- 有限非负有理递推的势函数与整数证书：
  definitions/ENTERPRISE_BRC_FINITE_RECURRENT_FOUNDATION_20260902.md

对有限 W≥0，Wh<h 可给全深度质量稳定性证书。它适合控制代价上界；相位抵消仍需要其自身的代数关系。若尺度变化，还要控制证书中的常数。例如 W_N=1−1/N 对每个 N 都稳定，但总和为 N；逐个稳定不提供统一尾界。

## 10. 实际复算与本轮完成范围

运行：

python3 verify_finite_models.py

无需第三方库。结果为 finite_model_results.json。

实际覆盖：

- F_2、F_3、F_5 上全部 722 个 2×2 矩阵；
- 共 397,442 次变量赋值，核对每个相位计数；
- 55 组完整有限域路径；
- 模 5 的全部 32 个子集、长度 1 至 5，共 160 组递推与直接枚举比较；
- 36 组合数模数/指定整数矩阵的 Smith 与核计数比较。

全部通过，计算只使用任意精度整数。另有协作推导核对，未作为项目独立 Review。

本轮完成了消息与原始代码定位、实际核验状态核对、有限模型方法提取、数学推导与可复算实验。没有接管已有 RH 共享任务，也没有把本轮提取升级为 RH 的自主证明。

最有价值的后续接口：精读外部“低层 theta 提升的整除增益与范数代价”承重引理，尝试对接 B_(a,N) 的一个完整尺度区间；同时将本轮端点—相位递推及 Smith 残差分解用作小模型比较工具。

## 11. 证据与引用索引

外部：

1. Levent Alpöge, remark.pdf, 2026-11-20：https://alpo.ge/remark.pdf 。本轮经网页检索的原文索引读到说明及研究时间线。
2. Andrew Sutherland, Verification files for the Lean proof of RH, 页面版本 2026-11-20 19:45 UTC：https://math.mit.edu/~drew/grh/ 。本轮读报告页，未自行运行全量 Lean。
3. Main.lean：https://github.com/CocoSgt/riemann-hypothesis-lean/blob/7cbf7a0c32fca1badf05931879a37c3f8a2b03b4/src/Main.lean
4. Statements.lean：https://github.com/CocoSgt/riemann-hypothesis-lean/blob/7cbf7a0c32fca1badf05931879a37c3f8a2b03b4/src/Statements.lean
5. 主桥接：https://github.com/CocoSgt/riemann-hypothesis-lean/blob/7cbf7a0c32fca1badf05931879a37c3f8a2b03b4/src/Supplements/Kernels/MainTheorems.lean
6. 核心入口：https://github.com/CocoSgt/riemann-hypothesis-lean/blob/7cbf7a0c32fca1badf05931879a37c3f8a2b03b4/src/Development/AutomorphicArithmetic/CharacterBoxes/MainConclusion.lean

项目：

7. 正道路能量：https://github.com/awdawmip/enterprise-math/blob/9fc068244e4f1117f1e75df5eb0285c6697d21d7/research_notes/COMPOSITE_ROAD_RH_PURE_POSITIVE_ENERGY_20260906.md
8. RH 研究交接：https://github.com/awdawmip/enterprise-math/blob/9fc068244e4f1117f1e75df5eb0285c6697d21d7/research_notes/COMPOSITE_ROAD_RH_RESEARCHER_HANDOFF_20260909.md
9. BRC 权重直方图：https://github.com/awdawmip/enterprise-math/blob/9fc068244e4f1117f1e75df5eb0285c6697d21d7/definitions/ENTERPRISE_BRC_UNIVERSAL_HISTOGRAM_FOUNDATION_20260903.md
10. 有限递推证书：https://github.com/awdawmip/enterprise-math/blob/9fc068244e4f1117f1e75df5eb0285c6697d21d7/definitions/ENTERPRISE_BRC_FINITE_RECURRENT_FOUNDATION_20260902.md

