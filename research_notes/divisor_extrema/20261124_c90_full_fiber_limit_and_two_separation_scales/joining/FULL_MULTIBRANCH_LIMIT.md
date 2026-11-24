# C90：完整多分支的有限分离极限

日期：2026-11-24。延续 C89 的准确有限读数及原整数源平均。

## 0. 原模型、尺度与输入

原目录仍是 \(2\le w\le v\le c\)，总数 \(\binom c2\)。在库存
\(c,c+A,c+B\) 各读一次原来的 \(H(0,1)\)，额外因子 5 全部位于第一次
23 更新之前。三个舍入格原点可分别平移并随 \(c\) 改变。连续坐标
\(X=(v/c,w/c)\in\Delta=\{0<y<x<1\}\) 只表示原路径标签的归一化；
原生 X6 路径、更新次序及观察者的继承范围保持不变。

假设

\[
c^{1/3}\ll B\ll c,\qquad 1\le A<B,\qquad
D=\sqrt{c/B},\quad \ell=D^3/c\to0,
\]
\[
L_c=2^{p-p_*(c,B)}\to L\in(0,\infty),\qquad
\theta=A/B\to0,\qquad A/D\to\tau\in[0,\infty).
\tag{0.1}
\]

使用冻结的 C89 联合格证明及其 C82、C88 输入：

- C89 [双支完整联合极限](https://github.com/awdawmip/enterprise-math/blob/6a6bb85747f6396970b1f54d999822ab710750a4/research_notes/divisor_extrema/20261124_c89_finite_separation_and_sharp_position_criterion/joint/PAIR_LATTICE_LIMIT.md)，尤其 §§1–5；
- C82 准确谱、正规逆图、完整有限纤维与紧图竞争者定位；
- C88 有限分离标记展开、端点 near 极限及 \(O(D^3/c)\) 误差；
- C90 [全局双斜率横截性](../rank/GLOBAL_PAIR_TRANSVERSALITY.md)，用于解除下面定理的横截假设；
- [实际核对的 Ratner 输入](RATNER_JOINING_INPUT.md)：Ratner 1990，Theorem 2 与 Corollary 5(1)。

核心数学先在一个固定有边距的正规源图 \(K\Subset\Delta\) 上证明。设
\(Y_0(X)=X,Y_1(X),\ldots,Y_{r-1}(X)\) 是 \(r\le6\) 条彼此分离的正规逆支，
\(F(Y_j)=F(X)\)，其中 \(F=(G,B_1)\)。令 \(J_j=|\det DF(Y_j)|>0\)。
在局部固定整数源轴后，定义

\[
t_j(X)=\frac{G_y(Y_j(X))}{G_x(Y_j(X))}.
\]

若分母为零，作固定整数轴交换；这仅对相应斜率施加固定分式线性变换。
本节所用条件为

\[
\boxed{\det d(t_i,t_j)(X)\ne0
\quad\text{对所有 }i\ne j\text{，几乎处处于 }K.}
\tag{T}
\]

只有一支时直接使用既有 near 极限；以下完整 joining 论证针对 \(r\ge2\)。
去掉 (T) 的零测例外并穷尽紧子图后，可暂设所有分母与 Jacobian 都有正下界。

## 1. 准确有限状态与主定理

沿用 \(F_c=(U_c,P_c)\) 及准确逆支 \(Y_{j,c}\)，满足
\(F_c(Y_{j,c}(X))=F_c(X)\)。设

\[
\mathsf B_c(Y)=
\begin{pmatrix}\nabla U_c(Y)\\ \nabla P_c(Y)\end{pmatrix},\qquad
M_{j,c}=L_cS\,a_D\,\mathsf B_c(Y_{j,c}),
\]
\[
S=\begin{pmatrix}1&0\\1&1\end{pmatrix},
\qquad a_D=\operatorname{diag}(D,D^{-1}).
\]

源支线性格和所有远支仿射格分别是

\[
\Lambda_{0,c}=M_{0,c}\mathbb Z^2,\qquad
\mathcal A_{j,c}=M_{j,c}(\mathbb Z^2-cY_{j,c}(X)),
\quad 1\le j<r.
\tag{1.1}
\]

记远支底格 \(\Lambda_{j,c}=M_{j,c}\mathbb Z^2\)，真实源相位为
\((\sigma_0,\sigma_1,\sigma_2)\in\mathbb T^3\)，中首相位差为

\[
\varrho_c=\sigma_1-\sigma_0
=\{L_cAD\,P_{A/c,c}(X)+\alpha_1-\alpha_0\}\pmod1.
\tag{1.2}
\]

**定理 1（完整联合极限）。** 在 (0.1)、(T) 下，原离散源平均中的

\[
\bigl(X,\Lambda_{0,c},\mathcal A_{1,c},\ldots,
\mathcal A_{r-1,c},\sigma_0,\sigma_1,\sigma_2\bigr)
\]

具有如下条件于 \(X\) 的极限：

1. \(\Lambda_0\) 是余体积 \(a_0=L^2J_0(X)\) 的线性 Haar 格；
2. 各 \(\mathcal A_j\) 分别是余体积 \(a_j=L^2J_j(X)\) 的仿射 Haar 格；
3. 所有这些格与三个均匀相位共同独立。

宏观源密度仍是 \(2\,dX\)。结论适用于任意固定光滑紧支源权重，对任意
随 \(c\) 变化的三个格原点一致成立。源格删去作为被观察安排的零点；
远支仿射格保留所有点。

## 2. 一个完整的 joining 引理

令 \(\mathcal X=\operatorname{SL}_2(\mathbb R)/
\operatorname{SL}_2(\mathbb Z)\)，\(\mu\) 为 Haar 概率，
\(U_s\) 为任一固定共轭的非平凡 horocycle 一参数流。

**引理 2。** 设 \(r\ge2\)，\(\lambda_0,\ldots,\lambda_{r-1}\) 均非零。
若概率 \(\nu\) 在 \(\mathcal X^r\) 上对
\[
T(z_0,\ldots,z_{r-1})
=(U_{\lambda_0}z_0,\ldots,U_{\lambda_{r-1}}z_{r-1})
\]
不变，且每个两因子边缘均为 \(\mu\times\mu\)，则
\(\nu=\mu^{\otimes r}\)。

**证明。** 对 \(r\) 归纳，\(r=2\) 即假设。每个非零速度的 Haar horocycle
时间一映射混合，有限乘积也混合。因此每个两因子 Haar 乘积在相应时间一
映射下遍历。

将 \(\nu\) 对 \(T\) 作遍历分解。每个两因子边缘是这些遍历分量边缘的
积分，而 Haar 乘积是遍历不变概率、因而是所有不变概率中的极点。
所以几乎每个遍历分量的每个两因子边缘仍恰为 Haar 乘积。分支对数有限，
可在同一个满测集上同时保留它们。固定这样的遍历分量 \(\nu_\omega\)。

由归纳假设，\(\nu_\omega\) 的前 \(r-1\) 因子边缘是
\(\mu^{\otimes(r-1)}\)，末因子边缘是 \(\mu\)。将前 \(r-1\) 因子作为
\[
G_1=\operatorname{SL}_2(\mathbb R)^{r-1}
\]
的一个格商，将末因子作为 \(G_2=\operatorname{SL}_2(\mathbb R)\) 的格商。
两边的时间一元素都是 unipotent 元素，Haar 系统均遍历。
Ratner 1990 Corollary 5(1) 因而使 \(\nu_\omega\) 成为代数 joining。
Theorem 2 给闭正规子群 \(A_i\triangleleft G_i\) 及连续满同态
\[
q:G_1\longrightarrow G_2/A_2,\qquad \ker q=A_1,
\tag{2.1}
\]
并将 joining 纤维表示为有限个对应商纤维。

若 \(\operatorname{Lie}A_2=\mathfrak{sl}_2\)，则由 \(G_2\) 连通有
\(A_2=G_2\)。joining 对最后一个完整 \(G_2\) 因子不变；条件测度只能是
该因子的 Haar 概率，所以 \(\nu_\omega=\mu^{\otimes r}\)。

否则，\(\mathfrak{sl}_2\) 简单性使 \(\operatorname{Lie}A_2=0\)。
闭离散正规子群包含在 \(G_2\) 中心中，故 \(A_2\subseteq\{\pm I\}\) 有限。
微分 (2.1) 得
\[
dq:\mathfrak{sl}_2^{\,r-1}\twoheadrightarrow\mathfrak{sl}_2.
\]
每个直和因子的像为理想，故不是零就是全部 \(\mathfrak{sl}_2\)。
不同因子的像彼此交换，不能有两个同时等于非交换的
\(\mathfrak{sl}_2\)。所以恰有一个因子 \(i\) 映成全部，其余全部映成零。
由于这些群因子连通，\(q\) 在其余各完整群因子上都恒等于单位元。

Theorem 2 的有限商纤维于是只依赖第 \(i\) 因子；\(A_2\) 又是有限群。
joining 的 \((i,r-1)\) 两因子投影因此支撑在一个具有至多可数垂直纤维的
对应上。它对 \(\mu\times\mu\) 为零测，因为末因子 Haar 概率无原子。
这与该两因子边缘为 Haar 乘积矛盾。

故每个遍历分量均为完整 Haar 乘积，积分即得结论。这里明确使用代数
joining 结构，并未将一般概率测度的两两独立当作共同独立。证毕。

## 3. 所有形状的 Haar 乘积及慢源条件化

将每个 \(\mathsf B_c(Y_{j,c})\) 除以行列式绝对值平方根，并作必要的固定
整数反射，使其行列式为一。在固定图上可写成
\[
\widetilde B_{j,c}=\bar u_{b_{j,c}}d_{\eta_{j,c}}u_{t_{j,c}},
\quad \eta_{j,c}>0,
\]
其中系数及所需有限阶导数有界，\(\eta_{j,c}\) 有统一正下界，
各系数在固定阶导数中趋于对应极限。

对任意一对 \(i\ne j\)，(T) 允许以 \((t_{i,c},t_{j,c})\) 作源局部坐标。
C89 §2 的二维换元与两条扩张 horocycle 均值论证直接给出这一对形状的
Haar 乘积，条件于宏观源 \(X\)。这一步不要求其中一支是源支，因为它只
处理线性格形状和连续源积分。离散源 Riemann 误差仍为 \(O(D^2/c)=o(1)\)。

每个形状的边缘均收敛到概率 Haar 测度。给定小 \(\varepsilon>0\)，为每个
形状选一个 Haar 质量至少 \(1-\varepsilon/r\) 的紧集，有限并界保证完整
形状族在这些紧集的乘积上质量至少 \(1-\varepsilon+o(1)\)。所以完整形状
族紧，存在概率弱极限，没有质量逃逸。

在连续源积分中作 \(X\mapsto X+sD^{-2}v\) 的微移。利用
\(a_D\bar u_b=\bar u_{b/D^2}a_D\)，任一形状弱极限在宏观源 \(X\) 处对
\[
(\Lambda_j)_{j<r}\mapsto
\bigl(U_{\lambda_j(X,v)s}\Lambda_j\bigr)_{j<r},
\qquad \lambda_j(X,v)=\eta_j(X)^2\,dt_j(X)[v]
\tag{3.1}
\]
不变；\(U_s=Su_sS^{-1}\)。余体积 \(a_j(X)\) 在微移中不变至 \(o(1)\)，
先按其平方根归一即可统一使用 \(\mathcal X\)。

慢源条件化的细节如下：先取可数稠密的光滑紧支形状测试、源权重、
有理 \(s\) 和有理向量 \(v\)，对全部这些测试取共同的满测源集。
微移积分恒等式乘任意源权重，故条件于几乎每个 \(X\) 后仍成立。
连续性将条件不变性从有理参数延到全部实参数。因 (T) 使每个
\(dt_j(X)\ne0\)，有限条核直线之外存在一个 \(v\)，使全部
\(\lambda_j(X,v)\ne0\)。允许在条件化之后为每个 \(X\) 选择这样的 \(v\)；
这不需要假设同一个向量在全源域都适用。

每对条件边缘已为 Haar 乘积。应用引理 2，完整条件形状测度只能是
\[
\bigotimes_{j=0}^{r-1}\mu_{a_j(X)}.
\tag{3.2}
\]
因此每个弱极限相同，完整形状族收敛到 (3.2)。

## 4. 中首相位差与全部形状共同独立

对包含 \(\varrho_c\) 的光滑紧支测试，离散源和与连续积分的误差是
\(O((D^2+AD)/c)=o(1)\)。单独的 \((X,\varrho_c)\) 边缘为源密度乘均匀
圆周测度：\(AD\to\infty\)，有限谱 \(P_{A/c,c}\to B_1\)，且正规性保证
\(\nabla B_1\ne0\)。局部非驻相估计对任意非零固定 Fourier 模式成立；
格原点只乘一个模为一的常数。

同一个微移除 (3.1) 外，还使
\[
\varrho\mapsto\varrho+s\beta(X,v)\pmod1,\qquad
\beta(X,v)=L\tau\,dB_1(X)[v].
\tag{4.1}
\]
二阶相位误差由 \(AD\,D^{-4}=O(D^{-2})\to0\) 控制。

固定几乎处处的 \(X\) 并选择使全部速度非零的 \(v\)。形状边缘 (3.2)
上的乘积 horocycle 流混合：先对有限乘积测试使用各因子的混合性，再以
张量积稠密性扩展到 \(L^2\)。对非零整数 \(k\)，令
\[
f_k((\Lambda_j))=
\mathbb E[e^{2\pi i k\varrho}\mid(\Lambda_j),X].
\]
由 (4.1)，\(f_k\) 是乘积流的频率 \(k\beta\) 的特征函数。
若 \(\beta\ne0\)，混合性使其为零；若 \(\beta=0\)，遍历性使其为常数，
而 \(\varrho\) 的条件均匀边缘使其均值为零。故所有 \(k\ne0\) 的系数消失：
\[
(X,(\Lambda_{j,c}),\varrho_c)\Longrightarrow
2dX\left(\bigotimes_j\mu_{a_j(X)}\right)d\varrho.
\tag{4.2}
\]
论证包括 \(\tau=0\)。

## 5. 全部远支平移与首末相位的联合均匀

### 5.1 同一个原整数平移同时作用于所有远支

准确恒等式 \(F_c(Y_{j,c}(X))=F_c(X)\) 给
\[
M_{j,c}(X)DY_{j,c}(X)=M_{0,c}(X).
\tag{5.1}
\]
对 \(q\in\mathbb Z^2\) 令 \(v=M_{0,c}q\) 有界，则 \(|q|=O(D|v|)\)。
源整数标签平移 \(n\mapsto n+q\) 后，C89 §4 的估计同时对所有有限个
远支成立：
\[
\Lambda_{j,c}\mapsto\Lambda_{j,c}+o(1),\qquad
\zeta_{j,c}\mapsto\zeta_{j,c}-v+o(1)\quad(j\ge1),
\]
\[
(\sigma_0,\sigma_2)\mapsto(\sigma_0,\sigma_2)+v+o(1)\pmod1,
\qquad \varrho_c\mapsto\varrho_c+o(1).
\tag{5.2}
\]
这里 \(\zeta_j\in\mathbb R^2/\Lambda_j\)。先用近恒等线性映射把新底格
对齐到旧底格，再比较仿射类；不能直接相减两个原始的大平移代表。
对齐后的误差为 \(O(\ell|v|^2)\)，形状相对误差为 \(O(\ell|v|)\)。

固定 \(R\) 后使用 Gaussian 权 \(w(v)=e^{-|v|^2}\) 和光滑截断。
源形状在紧集时，每点只有 \(O_R(1)\) 个有效整数标签。对每个标签作准确
双射重指标化，得到 C89 §4.2 的截断恒等式
\(\int P_Rf=\int m_Rf+o(1)\)。先取库存极限，再令 \(R\to\infty\)，
Gaussian 尾在形状紧集上一致可积，\(m_R\to1\)。最后以形状概率紧性
穷尽。因此完整联合弱极限对如下概率核 stationary：
\[
Pf=\frac1{Z(\Lambda_0)}
\sum_{v\in\Lambda_0}e^{-|v|^2}
f\bigl((\zeta_j-v)_{j\ge1},\,\sigma_{02}+v\bigr),
\quad
Z(\Lambda_0)=\sum_{v\in\Lambda_0}e^{-|v|^2}.
\tag{5.3}
\]
核保持宏观源、全部形状及 \(\varrho\)，故可对这些量条件化。
完整形状紧集之上的仿射环面丛是紧的；源相位环面也紧。因此所用完整
状态族有概率弱极限，(5.3) 并未预设未证明的平移均匀性。

### 5.2 唯一 stationary 环面测度

条件环面为
\[
\left(\prod_{j=1}^{r-1}\mathbb R^2/\Lambda_j\right)
\times(\mathbb R^2/\mathbb Z^2).
\]
字符标记为 \(\eta_j\in\Lambda_j^*\)、\(k\in\mathbb Z^2\)。
核 (5.3) 的字符乘数等于一，当且仅当
\[
k-\sum_{j=1}^{r-1}\eta_j\in\Lambda_0^*.
\tag{5.4}
\]
这是因为每个 Gaussian 权都严格为正，一个单位圆复数的正权平均等于一
要求每个相位都等于一。

在完整独立 Haar 形状下，几乎处处只有平凡字符满足 (5.4)。具体地，先在
格空间选可测基截面，以整数向量标记每条双格向量。若某个
\(\eta_j\ne0\)，固定其余形状、所有整数标记及 \(\Lambda_0^*\) 的一个
向量后，(5.4) 要求该独立 Haar 双格含有一个预先指定的非零向量；
这个事件 Haar 零测。指定向量为零时与非零整数标记矛盾。
对可数个标记取并仍为零测。若全部 \(\eta_j=0\)，则非平凡字符要求
某个固定非零整数 \(k\) 属于 \(\Lambda_0^*\)，同样为 Haar 零测。

stationary 测度的 Fourier 系数满足 \(\widehat\nu=\chi\widehat\nu\)。
所有非平凡字符都有 \(\chi\ne1\)，故其系数为零，条件测度只能是完整环面
Haar 乘积。结合 (4.2)，全部仿射平移、首末相位及 \(\varrho\) 共同独立。
由 \(\sigma_1=\sigma_0+\varrho\pmod1\) 恢复三个独立源相位，定理 1 得证。

三个格原点始终只影响平移或单位模 Fourier 因子，所有误差和不变性论证
对它们一致。任取原点序列，全部弱极限都被上述论证唯一确定，因此收敛
是对原点一致的。

## 6. 完整有限分离曲线

令 \(\mathcal F(X)=F^{-1}(F(X))\cap\Delta\) 为完整物理纤维。对几乎处处
正规源，它是一个含源自身的有限集合，最多六点。定义
\[
a_X=L^2J(X),\quad a_Y=L^2J(Y),\quad
h_Y=\frac{L\tau}{2}\,[B_2(Y)-B_2(X)],
\]
\[
w_a(d)=(1-|d|)F_2\left(\frac a{1-|d|}\right),\qquad
\ell_h(d)=(1-|d-h|)_+.
\]
仍以 \(E_2(s)\) 表示余体积 \(s\) 的仿射 Haar 格避开单位方格的概率，
规定零窗口的因子为一，空乘积为一。

**定理 3（全目录的端点有限分离极限）。** 若 (T) 对完整物理逆支组合
几乎处处成立，则在 (0.1) 下
\[
\boxed{\sup_{\alpha\in\mathbb T^3}
|V_c^{\mathrm{full}}(\alpha)-\Psi_\tau(L)|\to0,}
\tag{6.1}
\]
其中
\[
\boxed{
\Psi_\tau(L)=
2\int_\Delta\int_{-1}^1
w_{a_X}(d)
\prod_{Y\in\mathcal F(X)\setminus\{X\}}
E_2\left(\frac{a_Y}{\ell_{h_Y}(d)}\right)\,dd\,dX.
}
\tag{6.2}
\]

**证明。** 固定完整正规纤维图。条件于三个源相位，源支与每条远支的
碰撞窗口都是 C88 的准确有限展开所给的矩形。源支删去零点；各远支窗口
首坐标长度为 \(\ell_{h_Y}(d)\)，末坐标长度为一。
定理 1 使各远支仿射格独立，且独立于源格及相位，因此避空概率相乘。
对首末源相位积分的源支因子恰为 \(w_{a_X}(d)\)，同 C89 §5。

原点或格点恰位于半开窗口边界的事件为 Haar 零测。原有限标记的
\(O(D^3/c)\) 误差因此允许从连续测试转到唯一指示函数。既有紧图定位保证
全部有效对手都位于某一完整准确逆图的 \(O(D)\) 邻域，所选完整图内没有
遗漏竞争者。

再排除源边界、同步线、临界源及边界/临界目标的逆像。这些继承的例外
集合二维测度为零。剩余源域可由完整正规逆图的紧子域穷尽。唯一指标在
零与一之间，未覆盖源面积的贡献一致至多为其原目录比例，故局部极限
拼接并穷尽给 (6.1)–(6.2)。证毕。

C90 的全局双斜率证明及 15 对准确有理证书解除 (T)，因此在其给定的原谱
与物理域上，(6.1) 是本轮完整全库存结论。概率积分只包含原物理域中的
真实逆支；用于横截性解析延拓的额外实根不进入 (6.2)。

## 7. 参数连续性、远分离匹配与移动参数

**命题 4。** \(\Psi_\tau(L)\) 在
\((L,\tau)\in(0,\infty)\times[0,\infty)\) 上联合连续。并且对任意固定
\(0<L_-\le L_+<\infty\)，
\[
\sup_{L\in[L_-,L_+]}|\Psi_\tau(L)-\Phi_0(L)|\to0
\qquad(\tau\to\infty).
\tag{7.1}
\]

**证明。** C89 已证明 \(E_2\) 在正半轴连续。固定底格并对基本环面上的
平移积分，逐格点展开即得方格内格点数均值为 \(1/s\)。所以
\[
0\le1-E_2(s)\le\min(1,s^{-1}),
\tag{7.2}
\]
因为方格中格点数的均值为 \(1/s\)，命中概率不超过均值。
故 \(E_2(s)\to1\) 当 \(s\to\infty\)，零窗口端也连续。
\(F_2\) 的正参数连续性由同一零边界质量与支配收敛得到。
对固定正规 \(X\)，(6.2) 的被积函数因而对 \(L,\tau\) 连续，且在
\(-1<d<1\) 上被 \(1-|d|\) 控制。全源有界面积允许支配收敛，得联合连续。

令
\[
\delta(X)=
\min_{Y\in\mathcal F(X)\setminus\{X\}}
|B_2(Y)-B_2(X)|,
\]
单支纤维取 \(+\infty\)。继承的三谱几乎处处单原像结论使
\(\delta(X)>0\) 几乎处处。若
\(\delta(X)>4/(L_-\tau)\)，则对全部 \(L\ge L_-\)，每条远支均有
\(|h_Y|>2\)，所以其窗口对全部 \(d\in(-1,1)\) 为空，乘积等于一。
因此
\[
0\le\Phi_0(L)-\Psi_\tau(L)
\le2\,\operatorname{area}
\{X\in\Delta:\delta(X)\le4/(L_-\tau)\}.
\tag{7.3}
\]
右边随 \(\tau\to\infty\) 趋零且不依赖 \(L\)，得 (7.1)。证毕。

固定正紧 \(L\) 区间和有限紧 \(\tau\) 区间时，允许 \(L_c,\tau_c=A/D\)
不收敛：任何子列都可再取 \(L_c\to L,\tau_c\to\tau\)，应用定理 3 与
命题 4，得到
\[
\sup_\alpha|V_c^{\mathrm{full}}(\alpha)-\Psi_{\tau_c}(L_c)|\to0.
\tag{7.4}
\]
这是序列意义的移动参数结论，没有声称统一有效收敛率。

将所有 \(h_Y\) 同时变号、再作 \(d\mapsto-d\)，不改变 (6.2)，因为
\(w_a\) 是偶函数。因此末端对应模型在反转首末标记后具有同一
\(\Psi_\tau\)，其中 \(\tau=(B-A)/D\)。这与 C88 的末端标记反射一致。

## 8. 与 C89 真实缺口的结合

既然完整极限已存在，C89 的真实损失夹逼现在可直接写在确定曲线上：
\[
\boxed{c_L\min(1,\tau^{-1})\le
\Phi_0(L)-\Psi_\tau(L)
\le C\min(1,(L\tau)^{-\eta}).}
\tag{8.1}
\]
\(\tau=0\) 时左侧取 \(c_L\)，右侧取 \(C\)。
这里 \(\eta>0\) 仍是既有半代数误差界给出的某个指数，尚未宣称最优值。
每个有限 \(\tau\) 的缺口严格为正，而 \(\tau\to\infty\) 时缺口趋零。
这些是库存极限曲线的性质；(8.1) 没有给出 \(c,\tau\) 同时趋于无穷时的
有效有限库存误差率。

## 9. 证明状态及来源边界

主证明为本轮写出的数学论证，新增外部输入限于已实际读取的 Ratner 1990
joining 分类。C89 的有限谱误差、微平移、Gaussian 重指标化、窗口概率与
紧图定位按其冻结版本复用。完整全域应用还使用 C90 单独给出的全局双斜率
证明和 15 对准确有理核验，不能以本篇的条件性核心替代该输入。

本篇不要求所有分支都在同一个二维斜率坐标中独立变化；这在六支时本就
不可能。它利用每对横截产生的 Haar 边缘，加上共同的动力不变性与代数
joining 结构，严格确定完整联合测度。
