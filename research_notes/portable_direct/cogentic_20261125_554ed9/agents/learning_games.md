# Cogentic 五篇学习、博弈与离散工具论文：提取与局部核验

固定输入：`google-research/google-research@4a7bc8ab0bc7/cogentic_research_papers`。2026-11-25 提取。五篇 PDF 均通过 GitHub connector 以 base64 取回，已保存原 PDF 与 `pdftotext -layout` 文本；关键易错公式另看原页图像。本文是外部文献吸收笔记，主定理保持为原文结论；下面单独标明实际完成的局部重算，不将目录中的声明当作已取得的 Lean 检查结果。

## 结论与阅读优先级

| 优先 | 论文 | 最适合吸收的内容 | 接口与实际条件 |
|---|---|---|---|
| 高 | Fictitious Play | 下降二项式基、整数求和、无除法矩阵预像、稀疏余核残差 | 整数多项式演化、有限步更新证书；可直接做小模块 |
| 高 | VC Sample Compression | 按观测分区、熵增下界、最大彩票的对偶分离、MWU 重构 | 有限候选类/有界 VC 类的实验与证据选择；完整未来语义仍需独立定义 |
| 高 | Bimatrix Nash | 几何尺度指数滤波与耗散支付；kite 区域的精确混合修复 | 多尺度误差核、残差能量；全算法的显式常数非常大 |
| 中 | Subadditive Prophet | 非均匀边际约束下的指数平方、代价仅加常数 | 需要次可加性、独立抽样及对所有边际向量成立的归纳命题 |
| 中 | Convex CE | 条件期望伴随算子、两步残差、后序树分区恒等式 | 联合关系保存、分层状态摘要；查询下界仅限明确黑箱模型 |

所有外部对象以“算法/证明工具”接入，若应用于心跳世界的 X6 状态，需声明状态到外部对象的编码、允许观测和更新，不自动改变本原定义。

## 1. Fictitious Play：值得直接搬入工具箱的整数代数

源：<https://github.com/google-research/google-research/blob/4a7bc8ab0bc7/cogentic_research_papers/fictitious_play_convergence/Fictitious_Play_Convergence.pdf>。32 页。

### 1.1 原文主结论及其准确作用域

Theorem 1，p3：对每个整数 \(d\ge1\)，构造显式有理反对称矩阵 \(A_d\in[-1,1]^{n_d\times n_d}\)，其中

\[
n_d=2d^2+7d-5,\qquad N_d=2n_d=4d^2+14d-10.
\]

从零累计计数出发、固定字典序打破并列的“同时更新 fictitious play”，第 2 步以后最佳响应唯一，且存在显式 \(\kappa_d>0,T_0(d)\)，使每个 \(T\ge T_0(d)\) 满足

\[
\operatorname{Gap}_{A_d}(\bar x_T,\bar y_T)\ge\kappa_d T^{-1/(d+1)}.
\]

这是同时更新 fictitious play 在一族显式输入上的慢收敛下界；量词是“每个 \(d\) 存在一个输入族”，而非所有输入都以此速度收敛。\(\kappa_d\) 和 \(T_0(d)\) 依赖 \(d\)，用于有限步数的实际性能比较时需与指数一起保留。文中技术是单份内层游戏加 \(4\ell+5\) 个辅助策略完成运行后复位，避免每层复制三份。它可用于研究迭代停滞的压力样例。全递归构造的所有相位不等式本次没有做完整独立复证；可直接抽取下面已核对的代数模块。

### 1.2 反对称迭代的单轨道化与精确间隙

Definitions 1–2，Lemmas 1–2，p4–5。若 \(M^T=-M\)，两玩家同时更新、同样打破并列且从零计数出发，则 \(X_t=Y_t\)。置 \(U_t=MX_t\)，有

\[
i_{t+1}\in\arg\max_i(U_t)_i,\qquad U_{t+1}=U_t+Me_{i_{t+1}},\qquad
\operatorname{Gap}_M(\bar x_T,\bar y_T)=\frac{2}{T}\max_i(U_T)_i.
\]

因 \(M_{ii}=0\)，当前获选坐标在更新中保持原值，故 \(\max_i(U_t)_i\) 单调不减。证明只需代入反对称性，已手工核对。可用来把双边迭代化为一个保留整数累计量的状态机；其中“累计量单调”与“归一化间隙下降”是不同量。

### 1.3 下降二项式基：移位与求和全用整数矩阵

Definition 4，Lemmas 7–10，p7–8、18–19。令

\[
b_r^{(\ell)}(k)=\binom{k+\ell-r}{\ell-r},\quad r=0,\ldots,\ell,\qquad
b^{(\ell)}(k)=(b_0^{(\ell)}(k),\ldots,b_\ell^{(\ell)}(k))^T.
\]

这里二项式按下降阶乘多项式定义，可在所有整数 \(k\) 上使用。令 \(J\) 为超对角为 1 的幂零矩阵，则

\[
C_- = I-J,\quad C_+=(I-J)^{-1}=I+J+\cdots+J^\ell,
\]
\[
b^{(\ell)}(k-1)=C_-b^{(\ell)}(k),\qquad b^{(\ell)}(k+1)=C_+b^{(\ell)}(k).
\]

例如 \(\ell=2\) 时 \(b(k)=((k+1)(k+2)/2,k+1,1)^T\)，向前一步就是分别取后缀和。

设

\[
S_{\rm sum}^{(\ell)}=(I_{\ell+1}-J_{\ell+1}\mid -e_\ell).
\]

则对整数 \(K\ge k_0\ge0\)，

\[
\sum_{j=k_0}^{K-1}b^{(\ell)}(j)=S_{\rm sum}^{(\ell)}\bigl(b^{(\ell+1)}(K)-b^{(\ell+1)}(k_0)\bigr).
\]

离散积分升一级但不用反复引入分母，适合精确累计资源、阶数预算、块间更新、整数证书。若一个对象不具有多项式迭代结构，先证明这层表示对应关系再用。

### 1.4 无除法预像与稀疏余核

Definition 7、Lemmas 13–16，p20–22。令

\[
\mathcal T_\ell(P)=P^T-(I-J)^TP=P^T-P+J^TP.
\]

文中沿反对角线递推构造 \(P=\mathcal S_\ell(Z,\phi)\)，仅用加减。对任意 \(Z\)，残差

\[
R=\mathcal T_\ell(P)-Z
\]

只能出现在

\[
\{(2r,0):0\le r\le\lfloor\ell/2\rfloor\}.
\]

具体为 \(R_{00}=-Z_{00}\)，以及

\[
R_{2r,0}=P_{2r-1,0}-(Z_{2r,0}+Z_{0,2r}).
\]

若 \(Z,\phi\) 整数，则 \(P\) 整数，并有保守范数界

\[
\|P\|_{\max}\le(4\ell+4)^{2\ell+1}(\|\phi\|_\infty+\|Z\|_{\max}).
\]

给定 \(\phi_A=(A_{kk}\mathbf1_{k\ge\lceil\ell/2\rceil})_{k=0}^{\ell}\)，有精确左逆恢复

\[
\mathcal S_\ell(\mathcal T_\ell(A),\phi_A)=A.
\]

**对我们最有用的结构**：解一个大矩阵方程时，把可解部分显式消去，将实际障碍保存成少量余核坐标；用核参数 \(\phi\) 保存重构所需自由度。这正适合“结构残差要保留、零残差情形也允许”的接口。它本身只针对这个 Pascal 移位转置算子，其他关系算子需另导出对应余核。

**本次精确计算**：`check_learning_kernels.py` 对 \(\ell=2,3,4,5,6\) 的所有矩阵单位基检查零核参数时的残差支撑、全基左逆恢复，并检查一个明确 \(r_2\) 向量下的单位主元公式；全部通过。矩阵方程的秩/核维为 \((7,2),(14,2),(22,3),(33,3),(45,4)\)。同时在 \(\ell=0..8\)、\(k=0..19\) 及列明求和区间做了整数移位/求和校验。完整参数范围的证明仍来自文中反对角归纳，不由这些有限计算代替。

## 2. VC 压缩：把观测点选成可重构的证据集

源：<https://github.com/google-research/google-research/blob/4a7bc8ab0bc7/cogentic_research_papers/vc_sample_compression/Near_Quadratic_Sample_Compression.pdf>。30 页。

### 2.1 原文主定理及复杂度含义

Theorem 1.1，p3–4：任意二值概念类 \(\mathcal C\subseteq\{0,1\}^X\)，VC 维数为 \(d\ge1\)，存在有标签样本压缩方案，保存

\[
k=O(d^2\log^2 d)\text{ 个样本},\qquad b=O(d\log^2d)\text{ 个附加比特}.
\]

实际上只有 \(O(d\log d)\) 个需要标签，其余可作无标签观测点。重构是有限代表概念的加权多数票。**定理界定的是表示大小，不保证找出压缩集或执行重构具有多项式时间。** 保证对象是被压缩的可实现样本全部标签；若要用于全体未来行为等价，必须把那个未来语言纳入概念类并证明要求。

### 2.2 按观测集分区及点态低误差重构

Definition 2.1，Lemma 2.2，p10–11。对观测点集 \(W\)，按 \(c|_W\) 将候选 \(c\in\mathcal C\) 分区，固定全序并取每类最小代表，形成 \(\operatorname{Pool}(W)\)。Sauer 界给出

\[
|\operatorname{Pool}(W)|\le(|W|+1)^d.
\]

若这个代表池上存在分布 \(q\)，在每个需恢复的点上错误概率不超过 \(1/4\)，则记录少于

\[
k_1=8d\lceil\log_2(k_0+1)\rceil,\quad k_0\ge |W|,
\]

次最坏错误点及其标签，就能通过重放 MWU 得到所有点均正确的多数票。关键估计为

\[
\operatorname{err}_x(\bar p)\le\frac14+\sqrt{\frac{\ln N}{2k_1}}<\frac12,\qquad N=|\operatorname{Pool}(W)|.
\]

已核对这一步的从最坏点损失到每点误差、再到严格多数的推导；需要每轮确实选到最坏点、固定 MWU 与代表顺序，且重放时保留顺序/重复点的侧信息。

### 2.3 分区熵增由“被新观测区分的同胞对”下界

Lemma 4.4，p17–18，是最短、迁移最直接的小引理。旧分区各单元质量 \(w_\tau\)，条件分布 \(\nu_\tau\)，加入新观测得到细分 \(W'\)。则

\[
H_{W'}(\nu)-H_W(\nu)\ge
\sum_\tau w_\tau\Pr_{c_1,c_2\sim\nu_\tau}\bigl[c_1|_{W'}\ne c_2|_{W'}\bigr].
\]

重算理由：若一个旧单元分为条件质量 \(q_j\)，熵增为 \(w_\tau\sum_jq_j\log_2(1/q_j)\)，而 \(\log_2(1/q)\ge1-q\)，故至少为 \(w_\tau(1-\sum_jq_j^2)\)，右侧正是两次独立抽样落在不同新单元的概率。

可用于选择下一条最有区分力的观察/测试：最大化加权同胞对分离概率，给“这次实验到底增加了多少信息”一个有数学含义的目标。该式只测所选分布和候选集合的信息增量，不把无质量候选自动删去。

### 2.4 最大彩票与小分离集

Claim 4.1、Lemma 4.2、Claim 4.6，p14–16、20–22。维持旧单元质量和各点误差上限，形成可行分布多面体 \(K(\theta')\)。在同一单元中比较两个概念谁在固定顺序中更早，得到常和为 1 的双线性零和游戏，存在对称最优分布 \(\mu^*\)，值为 \(1/2\)。若已有严格松弛 \(\delta=\theta'-\theta>0\)，对偶误差乘子总量

\[
\Lambda=\sum_x\lambda_x\le\frac1{2\delta}.
\]

归一化为观测分布 \(p^*(x)=\lambda_x/\Lambda\)，将单元内分位差变为可观测分歧：

\[
d_{p^*}(c_1,c_2)\ge2\delta\bigl(r_\tau(c_2)-r_\tau(c_1)\bigr)
\]

（\(c_1\prec c_2\)、\(\mu^*(c_2)>0\)；两者正质量时可用绝对值）。若 \(\Lambda=0\)，分布已完全落在代表上。

承重逻辑已核对：最优性/互补松弛给“次序优势必须由某些点上的加权误差抵销”；旧分布有 \(\delta\) 松弛给乘子质量上界。因此这不是“看起来分散就容易找到短证据”，而是有目标地重排分布后得到可量化分离。

### 2.5 必须保存的反例

Appendix B，p29–30：\(\mathcal C=\{0,\mathbf1_{x_1},\ldots,\mathbf1_{x_m}\}\)，VC 维数仅 1，目标为全零，均匀分布在 \(m\) 个单点指标上，每点误差 \(1/m\)。任何 \(k<m\) 个观测点满足

\[
\mu(\operatorname{Pool}(W))\le\frac{k+1}{m},\qquad
H_W(\mu)\le\frac{k(\log_2m+2)}m.
\]

所以固定大小的观测集可以同时几乎拿不到代表质量、也几乎没有熵增。此例已按分区直接核对。对证据压缩很有用：低点误差、低 VC 维数和“分布很分散”本身不足以推出任意贪心选择都有常数进展。

## 3. Bimatrix Nash：耗散支付与小型精确修复

源：<https://github.com/google-research/google-research/blob/4a7bc8ab0bc7/cogentic_research_papers/bimatrix_nash_equilibrium/paper.pdf>。41 页。此子目录 README 标明 CC-BY-4.0；本笔记仅提取和重述数学结果。

### 3.1 原文主结论与实际尺度

Theorem 1.1，p2–3：对有理 \([0,1]\) 双矩阵博弈，给出确定性 \(\operatorname{poly}(L)\) 时间的有理 \(1/5\)-近似纳什均衡算法，其中 \(L\) 是输入位长。这里“exact”指误差阈值恰为 \(1/5\)，不是输出零误差纳什均衡。

Remark 1.3 的显式参数（已看 PDF 原页确认）：

\[
K=3\cdot2^{56},\qquad T=40\cdot2^{54}\cdot64^{K-1}+1.
\]

故本轮更适合提取局部核与证书，不把整套算法列为可立即替代现有求解器的工程实现。README 称 Lean 形式化将另行发布；固定目录只有 PDF/README，没有本轮可运行的 Lean 项目。全局 Volterra 到三变量不等式归约以及附录有理证书表，本次未做全链独立复证。

### 3.2 Kite 区域的零 LP 修复

Lemma 2.3(a)，p7–9。设双方悔值为 \(r_1,r_2\)，目标 \(s\in(0,1/2)\)。若

\[
(1-s)r_1+sr_2\le s,\qquad sr_1+(1-s)r_2\le s,
\]

则可仅混合一次最佳响应变为双方悔值均不超过 \(s\)。例如 \(r_1>s\) 时，取行最佳响应 \(e_{i^*}\)，

\[
\theta=1-s/r_1,\qquad x'=(1-\theta)x+\theta e_{i^*},\quad y'=y.
\]

于是 \(r'_1=s\)，而

\[
r'_2\le(1-\theta)r_2+\theta\le s.
\]

已重算不等式与端点分支。这个修复可以在有限多目标/对手约束模块内作为廉价后处理，条件需要直接检查。

### 3.3 几何多尺度指数核与耗散

Lemma 3.1，p15–16。定义 \(\alpha_k=64^{-(k-1)}\)、\(k_k(u)=\alpha_ke^{-\alpha_ku}\)（\(u\ge0\)）、\(k_0=K^{-1}\sum_kk_k\)。傅里叶符号为

\[
z_k(\xi)=\frac1{1+i\xi/\alpha_k},\qquad \bar z=\widehat k_0=x+iy,\qquad D=x(1-x)-y^2.
\]

当 \(K\ge10\)，原文证明

\[
y^2\le\frac5Kx(1-x),\quad D\ge\tfrac12x(1-x),\quad
|\overline{\bar z}-\bar z|^2=4y^2\le\frac{40}K D.
\]

若 \(w_k=\min(k,K+1-k)\)，还有

\[
\sum_kw_k|\overline{z_k}-z_k|^2\le56K D.
\]

本次额外手算的简单恒等式（直接由 \(\Re z_k=|z_k|^2\)）：

\[
D=\frac1K\sum_k|z_k|^2-|\bar z|^2
=\frac1K\sum_k|z_k-\bar z|^2\ge0.
\]

经 Plancherel，前面的频域不等式可以转成 \(\|(\mathcal K-\mathcal K^*)a\|_2^2\) 由 \(\langle a,\mathcal Ka\rangle-\|\mathcal Ka\|_2^2\) 支付的估计，系数 \(40/K\)。对我们已有误差核/局部三角矩方向，值得尝试的连接是用多尺度滤波的耗散预算支付非对称误差。有限区间、离散求和、加权 \(\ell^2\) 版本需要各自计算边界/离散化项；这里明确只提取全线 \(L^2\) 工具。

## 4. Subadditive Prophet：让指数平方而代价只增加常数

源：<https://github.com/google-research/google-research/blob/4a7bc8ab0bc7/cogentic_research_papers/subadditive_prophet_inequalities/Subadditive_Prophet_Inequalities.pdf>。36 页。

### 4.1 主结论与最有迁移价值的部分

Theorems 1.2–1.3，p3–4：买家估值按有限支撑的乘积分布独立抽取，每个估值规范化、单调、次可加。在任意给定的固定到达顺序和打破并列规则下，存在静态匿名逐项价格取得 \(O(\log\log\log m)\) 的期望福利近似比。同时，在足够大 \(m\) 上构造两买家实例，使静态匿名价格的近似比至少为 \(\Omega(\log^{(3)}m/\log^{(4)}m)\)；该下界即使允许有利的并列选择、以及独立于实际估值抽取的随机价格仍成立。这里约束的是这类静态逐项价格机制；对我们最有用的是上界证明里完整、短小的非均匀边际归纳引理。

### 4.2 精确的指数平方引理

令有限地集 \(U\)，\(v:2^U\to\mathbb R_{\ge0}\) 满足 \(v(\varnothing)=0\)、单调和次可加。\(\Delta(a)\) 是逐项边际不超过向量 \(a\in[0,1]^U\) 的子集分布。定义

\[
f(a)=\max_{S\sim\lambda\in\Delta(a)}\mathbb E v(S),\quad
g(a)=\max_{\lambda\in\Delta(a)}\min_{\mu\in\Delta(a)}\mathbb E v(S\setminus T),\quad
G=\max_ag(a),
\]

其中 \(S,T\) 独立，向量幂按分量取。

基本式是 \(f(a)\le f(a^2)+G\)。若对**所有**边际向量 \(b\) 已知

\[
f(b)\le f(b^B)+CG,\qquad B\ge2,
\]

Lemma 2.3，p9–11 给出更强的

\[
f(a)\le f(a^{B^2+2B})+(C+3)G\le f(a^{B^2})+(C+3)G.
\]

关键是抽取一个 minimax 最优随机集合 \(T\)，在 \(T\) 内外用不同边际 \(a_j^{B+1}\) 与 \(a_j\)，一次应用统一归纳假设，同时处理两个阶段。先修薄付 \(G\)，归纳付 \(CG\)，最后用新独立副本解耦丢弃部分付 \(2G\)。已逐步核对独立性、条件边际及次可加的三次支付。

这将代价更新从 \(C\mapsto2C\) 改成 \(C\mapsto C+3\)，而指数仍 \(B\mapsto B^2\)。由此文中得到

\[
G\ge\frac{v(U)}{\alpha(m)},\quad
\alpha(m)=\frac{3\lceil\log_2\lceil\log_2(2\log_2m)\rceil\rceil}{1-1/m}\quad(m\ge5),
\]

小规模 \(1\le m\le4\) 用 \(\alpha(m)=4m\)。该证明显示，允许非均匀分量条件可以突破只在相等边际上成立的较弱界；不是单靠把原递推写成新符号。

**迁移建议**：若我们的误差预算能表示为对子通道集合的单调次可加代价，并能实现相应独立抽取和条件边际类，可复用此加法代价平方递推。先验证这些对象对应；当前数论误差核尚未自动满足这些假设。拍卖下界、复杂高围长图和价格估计构造对当前目标较间接，保留索引即可。

## 5. Convex CE：联合关系、两步残差和紧凑树摘要

源：<https://github.com/google-research/google-research/blob/4a7bc8ab0bc7/cogentic_research_papers/ce_convex_games/CE_in_Convex_Games.pdf>。17 页。

### 5.1 原文下界的作用域

Theorem 2，p15–16：对每个足够大的总维数 \(d=d_1+d_2\)，在标准一阶黑箱 oracle 模型中构造一族两玩家游戏：策略集是欧氏单位球，成本值在 \([0,1]\)，成本关于各自策略 \(1/2\) 强凸，Lipschitz 常数 \(L<\sqrt d\)。任何在每个该族输入上以至少 \(2/3\) 概率输出 \(\epsilon=1/d\) 的全 normal-form correlated equilibrium 的随机算法，需要 \(\exp(\Omega(d^{1/16}))\) 次 oracle 查询；原文的下界允许任意内部计算时间和任意有限输出支撑大小。这里的均衡条件允许全策略修改映射，和 coarse CE、固定低维偏移类不同。成本对各玩家自身变量是二次，第二玩家目标含非线性 \(f_V(x)\)，不应误读成任意两方联合变量的一个固定全局二次式。

本次没有把此下界视为我们自有结构算法的限制；它可提供“黑箱暴露了什么信息、允许何种偏移”这个比较标准。更实用的是以下独立可核对模块。

### 5.2 条件期望伴随与两步残差

Lemma 7，p12–13。考虑成本

\[
c_1(x,y)=\tfrac14\|x-y\|^2,\qquad c_2(x,y)=\tfrac14\|y-f(x)\|^2
\]

其中双方策略位于同一欧氏单位球，\(f\) 映入该球（文中另有填充坐标）。有限支撑联合分布 \(\mu\) 的双方 swap gap 都不超过 \(\epsilon\)。令

\[
Ph(x)=\mathbb E[h(Y)\mid X=x],\qquad
P^*g(y)=\mathbb E[g(X)\mid Y=y],\qquad A=PP^*.
\]

则 \(P\) 是 \(L^2\) 收缩，\(A\) 自伴正半定，且

\[
\|X-Af(X)\|_{L^2}\le4\sqrt\epsilon.
\]

核对：条件平方损失的最优偏移是条件均值，分别得到 \(\|X-PY\|_2\le2\sqrt\epsilon\) 与 \(\|Y-P^*f(X)\|_2\le2\sqrt\epsilon\)，三角不等式加 \(\|P\|\le1\) 即结论。对我们联合关系保留，这提供把“两方局部残差”提升成“联合两步算子残差”的具体公式。只保存两边边际无法重建这个 \(P\)，这一点与残差保真接口吻合。

### 5.3 后序树的点态正部恒等式

Definition 3、Lemmas 1–3，p5–8。文中递归二叉-单叉树有 \(N=3\cdot2^k-2\) 个节点，已完成后序前缀只须保留至多 \(k+1\) 个最大完整子树的根 \(B(s')\)。它们精确满足

\[
\{u:u\le_{\rm post}s'\}=\bigsqcup_{b\in B(s')}\operatorname{Subtree}(b),
\]
\[
|\operatorname{Path}(s,r_k)\cap B(s')|=\mathbf1_{s\le_{\rm post}s'}.
\]

定义每个节点的 prerequisite 集 \(\operatorname{Req}(s)\) 与 blocker 集 \(\operatorname{Block}(s)\)，对连续激活 \(w\in[0,1]^{F_k}\)，

\[
L_s(w)=\left(\min_{b\in\operatorname{Req}(s)}w_b-\max_{b\in\operatorname{Block}(s)}w_b\right)_+,
\qquad\sum_sL_s(w)=1-w_{r_k}.
\]

承重标量恒等式（已手工核对全序分支）是

\[
(Q-\max\{A,F\})_++(\min\{Q,A\}-F)_+=(Q-F)_+.
\]

对我们有两种具体用途：树状正部能量分解时可试用这类精确望远镜关系；给固定后序读取语言做状态摘要时，可只保存完结子树根并证明重建前缀。这不是任意树动态或任意未来观察下的通用状态压缩。

## 本次材料与验证清单

- 原始 PDF/文本：`cogentic_review/sources/` 的五个对应名称。
- 图像核对：Nash p3、p15 与 FP p21 已在图像中核对；其他选择页已渲染于 `sources/rendered/`。
- 复算脚本：`cogentic_review/agents/check_learning_kernels.py`。
- 真实输出：`cogentic_review/agents/check_learning_kernels.json`，PASS，精确整数/有理数矩阵检验。
- 独立手算核对：FP 反对称单轨道与 binomial 移位/求和；VC 熵增和 LP 乘子界及 MWU 误差；Nash kite 修复与符号方差恒等式；subadditive 指数平方三步的条件边际/独立性；CE 条件均值平方误差和树标量望远镜式。
- 本次没有运行原文所声称的 Lean 项目，也没有给五篇完整主定理作正式项目审查/晋升。目录中的主定理与上述已核对的小工具分开保存。

建议根报告优先呈现“无除法余核残差、观测分区熵增、耗散支付”三组，可把指数平方和条件期望两步残差作为相邻工具；这样既覆盖五篇，又把阅读价值落在可立即复用的数学对象上。
