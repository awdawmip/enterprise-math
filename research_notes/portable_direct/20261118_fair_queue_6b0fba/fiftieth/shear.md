# 高斯点阵的力、比能和成形：单空位、方格鞍点与双排滑移

同一个密度为一的高斯二体模型给出两个方向相反的反例。每个 Bravais 格的逐点合力为零，方格在每个势尺度却都能经剪切严格降能。反过来，密度一三角格删去一个格点，极限每粒子能量完全不变，其余每个点的合力却都非零。在固定的双排周期胞中，还可以精确求出实际粒子力流：正方初态严格不动，任意微小的正向排间错位则严格耗散，收敛到一个具体的非三角点阵。

登记题 RS-OAI7-090-E-20261007-6F2A81 要求区分最小能量、唯一性、更新存在性、耗散和可达性。外稿考察外部欧氏平面、密度一、**有序对**的每粒子下极限；其主定理声称对平方距离的非负完全单调势，三角格给出全局最低值，原文明确没有分类全部取等者。Montgomery 的经典格 theta 定理在 Bravais 格范围给出高斯最低值。原稿的有理区间检查器验证插值构造的有限数值界，未给粒子后继规则。下文的能量差、点力、Hessian 与流都直接从单个高斯计算，对外稿任意构型的全局比较无需预先假定。第 31 轮研究过该稿的插值壳证书，本轮讨论的位置更新是另一个问题。[登记题](https://github.com/awdawmip/enterprise-math/blob/7b7c764dd19eacf090dfae3126a6ed819d9d640c/research_tasks/RS-OAI7-090-E-20261007-6F2A81.md) · [原件定义与适用范围](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/An-atomic-certificate-for-triangular-lattice-universal-optimality-September-26-2026/build/main.tex#L42-L130) · [原检查器](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/An-atomic-certificate-for-triangular-lattice-universal-optimality-September-26-2026/verification/check_certificate.py) · [第 31 轮插值研究](https://github.com/awdawmip/enterprise-math/blob/7b7c764dd19eacf090dfae3126a6ed819d9d640c/research_notes/portable_direct/20261118_fair_queue_6b0fba/thirtyfirst/interpolation.md)

## 1. 一个空位分开最低比能与力平衡

固定 $\alpha>0$，记 $s=\pi\alpha$、$G(x)=e^{-s|x|^2}$。对单位面积格 $\Lambda$，原定义中的圆盘极限存在，且 $E_\alpha(\Lambda)=\sum_{v\in\Lambda\setminus0}G(v)$。实际上固定格矢 $v$，盘内点平移 $v$ 后仍留在盘内的比例趋一；以可求和的 $G(v)$ 支配后逐项取极限。有限周期胞作相同的平移计数，得到各基点格和的算术平均。全文能量均保留原有序对计数，无额外因子 $1/2$。

在外部点位置上另声明通常的负势梯度及单位迁移率，

$$
F_{\mathcal C}(x)=2s\sum_{y\in\mathcal C,\ y\ne x}(x-y)G(x-y),\qquad \dot x=F_{\mathcal C}(x).
$$

这是局部成对力的和。对任何 Bravais 格绝对收敛，由 $\pm v$ 逐对抵消。对单位三角格 $A$ 现取 $A'=A\setminus\{0\}$，其中心盘密度仍为一。写 $E_R$ 为有序对能量除以原格盘内点数 $N_R$，$S_R=\sum_{x\in A\cap B_R\setminus\{0\}}G(x)$。删点使分子恰减 $2S_R$，分母减一，故

$$
(N_R-1)\big(E_R(A')-E_R(A)\big)=E_R(A)-2S_R\ \longrightarrow\ -E_\alpha(A).
$$

所以 $E_\alpha(A')=E_\alpha(A)$。可是对每个 $x\in A'$，

$$
F_{A'}(x)=-2s\,x\,e^{-s|x|^2}\ne0 .
$$

若采用原外稿的全局能量比较，$A$ 和 $A'$ 因此给出两个不全等的全局取等构型，后一个不满足任何剩余粒子的点力平衡。即使只接受经典格上的最低值，上述两个集合的比能相等及力差仍各自成立。极限每粒子能量对有限缺陷失敏，有限缺陷的未归一化局部能量变化仍可决定点力。更一般，对两个各自一致离散、中心盘密度一的构型，若对称差在 $B_R$ 中是 $o(R^2)$，则高斯下极限比能相同。每个改变点的盘内总关联能量被某常数一致控制（由一致离散逐环计数），故分子之差为 $o(R^2)$，分母之比趋一。

## 2. 每一尺度的方格形状鞍点

令 $x+iy$ 表示面积一的格，基向量分别为 $(1/\sqrt y,0)$ 和 $(x/\sqrt y,\sqrt y)$。令 $\Theta=1+E_\alpha$。对水平整数坐标作一维 Poisson 求和，

$$
\Theta(x,y)=\sqrt{y/\alpha}\sum_{n,h\in\mathbb Z}
e^{-\pi y(\alpha n^2+h^2/\alpha)}\cos(2\pi hn x).
$$

于是对所有 $x\notin\mathbb Z$ 与 $y>0$，

$$
\Theta(0,y)-\Theta(x,y)\ \ge\
8\sqrt{y/\alpha}\,e^{-\pi y(\alpha+\alpha^{-1})}\sin^2(\pi x)>0 .
$$

所有被略去项都非负，上式取了四个 $|h|=|n|=1$ 项。令 $\theta(t)=\sum_{m\in\mathbb Z}e^{-\pi t m^2}$、$M_j(t)=\sum_m m^j e^{-\pi t m^2}$。方格 $(x,y)=(0,1)$ 的剪切曲率为

$$
E_{xx}(0,1)=-4\pi^2\alpha^{-1/2}M_2(\alpha)M_2(1/\alpha)<0 .
$$

**矩形方向恰相反。** 令 $u=\log y$，则 $\Theta(0,e^u)=\theta(\alpha e^u)\theta(\alpha e^{-u})$。函数 $f(v)=\log\theta(e^v)$ 满足 $f''(v)>0$。给一个初等证明。置 $t=\pi e^v$，令 $m$ 按 $e^{-tm^2}$ 比例分布，$\mu=E(m^2)$。有 $f''(v)=t^2\operatorname{Var}(m^2)-t\mu$。当 $v\ge0$，$t\ge\pi>3$，$e^{-t}<1/20$，故 $\mu\le2\sum_{m\ge1}m^2/20^m<1/2$；又 $m^4\ge m^2$，因此 $f''\ge t\mu(t(1-\mu)-1)>0$。Poisson 恒等式 $f(v)=-v/2+f(-v)$ 给出其余一半。这个 theta 凸性已有精细研究，此处使用的是它对更新轨迹的推论。[Faulhuber–Steinerberger](https://arxiv.org/abs/1601.02972)

$\log\Theta(0,e^u)$ 因此偶且严格凸，二阶导处处为正。$u=0$ 处 $E_{uu}=2\theta(\alpha)^2 f''(\log\alpha)>0$，而由反射 $x\mapsto-x$，该点的 $E_{xu}=0$。面积保持形变的两个 Hessian 特征方向均有严格符号，适用于每个 $\alpha>0$。

**一整族严格耗散却趋向鞍点。** 取上半平面的标准形状度量 $(dx^2+dy^2)/y^2$，令形状沿 $-\operatorname{grad}E_\alpha$ 演化。反射保持能量，$x=0$ 因而是流的不变子空间；其上坐标 $u$ 的度量就是 $du^2$，满足 $\dot u=-\partial_u E_\alpha(0,e^u)$。任一 $u_0\ne0$ 单调向零，全程留在紧区间，光滑性保证存在唯一全局解。若极限非零，能量导数在该邻域有严格固定符号且远离零，矛盾。轨迹在任一有限时刻仍未到零，且 $\dot E=-(\partial_u E)^2<0$，最终却趋向已有下降剪切方向的方格。这个外部形状流允许晶胞改变。

## 3. 固定周期胞中的真正粒子力流与逃逸时间

保持水平周期 $1$ 与竖直周期 $2$，每胞两粒子。偶数行位于 $(m,2j)$，奇数行位于 $(m+\delta,2j+1)$，记构型为 $\mathcal C_\delta$。令 $W_o(t)=\sum_{n\ {\rm odd}}e^{-\pi t n^2}$、$g_\alpha(\delta)=\sum_m e^{-\pi\alpha(m+\delta)^2}$。按两粒子所属行的奇偶拆分，有

$$
E_\alpha(\mathcal C_\delta)=\big(\theta(\alpha)-W_o(\alpha)\big)\theta(\alpha)-1+
W_o(\alpha)g_\alpha(\delta).
$$

同奇偶行的贡献固定；异奇偶行间只出现同一个 $g_\alpha(\delta)=g_\alpha(-\delta)$。由 Poisson 公式，半格错位的**精确**能量降幅为

$$
E_\alpha(\mathcal C_0)-E_\alpha(\mathcal C_{1/2})
=\frac{2}{\sqrt\alpha}W_o(\alpha)W_o(1/\alpha)>0 .
$$

各行格点的竖直力由关于本行的镜像相消。两种行的水平力互为反号，奇行的恒定力为 $-E'(\delta)$，偶行的是 $+E'(\delta)$：例如对奇行粒子直接求导，异奇偶行贡献正是 $-W_o g_\alpha'$。因此在扣除共同水平平移后，单位迁移率的真实成对点力方程在这一周期子族中闭合为

$$
\dot\delta=-2E'(\delta),\qquad \dot E=-2(E'(\delta))^2.
$$

系数 2 来自两排都移动。固定偶行只作计算参照不会把其中一排钉死。在 $\delta=0$ 和 $1/2$，力均为零。对于 $0<\delta<1/2$，Poisson 公式与 Jacobi 三重积给出

$$
g_\alpha(\delta)=\alpha^{-1/2}
\prod_{m\ge1}(1-q^{2m})(1+2q^{2m-1}\cos(2\pi\delta)+q^{4m-2}),
\qquad q=e^{-\pi/\alpha}.
$$

各因子为正，其对数导数一致可和；每个含 $\delta$ 的因子都严格递减。因此 $E'<0$，所有这类初值在任一有限时间严格耗散，单调趋向 $\delta=1/2$。该错列格由 $(1,0),(1/2,1)$ 生成，只有两个最短非零向量，故不是有六个最短向量的三角格。这里不需排除整个平面比较可能有其他极小元。[Jacobi 三重积](https://dlmf.nist.gov/20.5)

**逃逸率。** 零错位的线性不稳定率和到达任意固定 $0<b<1/2$ 的时间为

$$
\lambda_\alpha=-2E''(0)=\frac{8\pi^2}{\sqrt\alpha}W_o(\alpha)M_2(1/\alpha),\qquad
T_{\delta_0\to b}=\lambda_\alpha^{-1}\log(1/\delta_0)+O_{\alpha,b}(1)
\quad(\delta_0\downarrow0).
$$

由解析性和偶性，$\dot\delta=\lambda_\alpha\delta+O_\alpha(\delta^3)$，将倒数从 $\delta_0$ 积分至 $b$ 即得。尺度两端的首项分别为

$$
\lambda_\alpha\sim
\begin{cases}
8\pi^2\alpha^{-1}e^{-\pi/\alpha},&\alpha\downarrow0,\\
8\pi\alpha e^{-\pi\alpha},&\alpha\to\infty.
\end{cases}
$$

小尺度取 $W_o(\alpha)=\theta(\alpha)-\theta(4\alpha)\sim1/(2\sqrt\alpha)$，$M_2(1/\alpha)\sim2e^{-\pi/\alpha}$。大尺度下 $W_o(\alpha)\sim2e^{-\pi\alpha}$，在原坐标直接求导有 $g_\alpha''(0)=-2\pi\alpha\,\theta(\alpha)+4\pi^2\alpha^2 M_2(\alpha)\sim-2\pi\alpha$。该时间常数依赖明确的外部单位迁移率。

即使从**同一**方格出发并始终使用同一能量，点力流永远留在 $\mathcal C_0$。另一条合法的外部离散更新可在同一双排族预先约定候选 $\delta=0,1/2$，每次采用其中严格降低能量的候选，否则保持。它从同一 $\mathcal C_0$ 一步到 $\mathcal C_{1/2}$，由精确降幅可直接检查。候选提案、单位时间和许可变动属于更新关系本身。前两节给出的连续流说明即使施加严格耗散，收敛到全局最优仍须额外条件。

## 4. 从比较定理到可达性需要哪些输入

能量最小值回答一个数值比较。具体取等集合还需要等号条件；在本稿的比能定义下一个空位即保持取等。更新则须指定允许的状态、位移或离散后继、边界、反作用与时间。对一个给定外部梯度系统，若前向解存在且轨迹相对紧、Lyapunov 能量非增，并独立证明零耗散集的最大不变子集位于目标极小集，则由不变性原理可得至该集的距离趋零。若该集在允许对称商中只有一点，可得相应状态收敛。有限步到达还需另有条件，例如离散更新在目标外每步至少下降某个固定正量且能量有下界。方格反例逐项给出了缺少“不变集只含目标”时会发生什么。

原生适配至少要给出哪些六轴离散占位可比较、允许的三元作用与反作用、作用后储存在哪个状态、边界如何交换能量或质量、一个心跳中谁先更新、如何从原生读数推出上述力和耗散，以及极限采用何种归一化。固定占位时场解唯一，只决定该占位的响应。这些输入未由平面二体高斯的傅里叶证书给出。本研究执行的是公开数学模型的格和与有限行移位核验。一个具体待判接口是给定原生可逆配对步及边界后，是否存在可由该步实现且能量严格下降的占位变化。[冻结 P000 分型](https://github.com/awdawmip/chatgpt-global-knowledge/blob/5a13c778840c8eed2ffe200155dc7beec29478ba/projects/enterprise-math/P000_REALITY_FOUNDATION.json)

## 5. 独立有界复算

shear_check.py 用 Python 标准库作 $10^{-50}$ 定点外包，Machin 反正切交错余项包围 $\pi$，缩放后的指数 Taylor 余项及格和几何尾均外向取整。计算在 $\alpha=1/4,1/2,1,2,4$ 检查剪切和矩形伸缩曲率的符号、原坐标和 Poisson 表达的交集、半排错位能差、双排点力逃逸率。面积一平面格的对偶是其直角旋转，故 Bravais 能差及形状 Hessian 满足 $\alpha\leftrightarrow1/\alpha$ 的权 $\alpha^{-1}$，脚本另作核验。$\alpha=1$ 时按小数近似，

| $E_\alpha(\mathcal C_0)$ | $E_{xx}$ | $E_{uu}$ | $\mathcal C_0$ 至 $\mathcal C_{1/2}$ 降幅 | $\lambda_\alpha$ |
|---:|---:|---:|---:|---:|
| 0.180340599016 | −0.295085149754 | 1.118156700334 | 0.014939541854 | 0.589979855092 |

shear_checked.json 保存逐指标严格外区间。程序还在五个三角格圆盘上直接重算删点前后每个平方长度的有序对数，并验证以剩余点为中心的截断力在每个壳上的向量系数。无限格的取等、曲率定号、所有正尺度的轨道及逃逸极限来自上述论证。
