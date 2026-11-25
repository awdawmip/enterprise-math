# Cogentic 十篇论文：面向进取数论的定理、公式与证明工具提取

## 阅读结论

这批材料最值得吸收的，是一组能明确说明输入、保持量、残差与支付的局部数学工具：旧观测保持扰动、有限域独立性证书、复合模数消元、低阶矩盲区、按分离能力选择新观测、无除法离散积分、联合符号正性以及多尺度能量分解。它们能够接入进取数论现有研究对象，形成具体可复算的增量。

原始输入固定为 [google-research/google-research@4a7bc8ab0bc770e71a259b7966c500496b99010a](https://github.com/google-research/google-research/tree/4a7bc8ab0bc770e71a259b7966c500496b99010a/cogentic_research_papers)，该提交日期为 2026-11-25。目录中十篇 PDF 合计 389 页。本次已取得全部原文，核对每份 PDF 与该提交的 Git blob，保存 SHA256、页数与原始路径；逐篇抽取主定理、关键局部命题及相关证明，另对若干易错公式查看原页。

**证据状态：** 本报告中的“大算法主定理”保留为论文主张；列明的短代数推导有本次手工核对，有限例有实际运行的精确计算。十篇论文的全部承重证明没有完成逐行独立复证。该固定目录提供 README 与 PDF；提交说明六篇新增论文的 Lean 4 形式化将在 companion 发布，本次没有取得并运行对应形式化源。因此不能把发布声明当成已完成的项目数学接纳。

本报告是研究笔记与可复用工具提取，不作新颖性主张，也不更改项目 Foundation / Working Truth。Researcher-ID：`EM-DIRECT-554ED9 / TASK_RESEARCH`；Research-Activity-ID：`RA-226AABA6B251DC420A415238`。

## 一、与我们当前研究对象的连接依据

本次使用项目原有的 X6 状态、类型明确的整数寄存器、允许观测及未来操作语义。有限域、实数矩阵、概率分布与多项式均作为显式定义的辅助对象；需要写清从原状态到辅助对象的编码。

三条实际连接依据是：

1. [Riesel observers](https://github.com/awdawmip/enterprise-math/blob/b1b39590cc72fa0a98ef10fb56cd8db9dca3a563/research_notes/portable_direct/riesel_observers_20261122/README.md)：整数寄存器的算术族为 \(F_n(a)=a^22^n-1\)，固定 X6 anchor，更新为 \(x\mapsto2x+1\)。已有有限通道的共同轨迹不等于所有后续覆盖代价。下文的旧通道保持公式、联合符号与模阶工具直接面向这个接口。
2. [RH global sampling](https://github.com/awdawmip/enterprise-math/blob/b1b39590cc72fa0a98ef10fb56cd8db9dca3a563/research_notes/portable_direct/rh_global_sampling_20261123_b5750a/REPORT.md)：
   \[
   q(y)=\sum_{2\le n\le y}D_n(y/n-1)-y\log y+(1+\gamma)y,
   \qquad -\Delta^2q_n=(\kappa_n-D_n)/n,
   \]
   \[
   S(q)=\sum_{n=A}^B\frac{(q_n)_+^2}{n^2},\qquad
   \|v\|_w^2=\sum_{n=A}^B\frac{v_n^2}{n^2}.
   \]
   真实 \(D_n\) 固定；候选核、包络与证书参数可以设计。原有有理 Green 包络与 \(g_n=nH_n,\ \Delta^2g_n=1/n\) 提供对照基准。下文多尺度恒等式与换核支付都在这个明确对象上讨论。
3. [当前 Foundation 提取](https://github.com/awdawmip/enterprise-math/blob/b1b39590cc72fa0a98ef10fb56cd8db9dca3a563/definitions/EM_FOUNDATION_STARTUP.json) 中的联合关系与残差保真要求：摘要是否足够，应按已声明的观测和未来操作判断；边际相同、低阶矩相同、某个有限窗口相同，各自只是特定的等价关系。下文给出一个可直接使用的三阶分离例。

## 二、十篇论文各自应保留什么

下表“主结论”均按原文陈述记录；完整前提、页码、限制和局部推导见后附三份专题笔记。

| 论文与原文 | 主结论的准确读法 | 对我们的优先提取 |
|---|---|---|
| [F-LV：Integer Factorization](https://github.com/google-research/google-research/blob/4a7bc8ab0bc770e71a259b7966c500496b99010a/cogentic_research_papers/integer_factorization/paper.pdf)，54页 | Thm 1.1：Las Vegas 完整分解，期望位复杂度 \(L_N[1/3,105]\)，空间 \(L_N[1/3,40]\) | 祖先消失扰动、条件纤维加权望远镜、平滑权重、平方类残差、隐藏根 CRT 概率 |
| [F-DET：Deterministic Factoring](https://github.com/google-research/google-research/blob/4a7bc8ab0bc770e71a259b7966c500496b99010a/cogentic_research_papers/deterministic_factoring_l34/paper.pdf)，59页 | Thm 1.1–1.3：确定性分解 \(O(\exp(3(\log N)^{3/4}))\)；QNR 使用 PDF 精确指数式 | 子群指数饱和、相容 Walsh 正性、有理数精确恢复 |
| [DLP：Discrete Logarithms](https://github.com/google-research/google-research/blob/4a7bc8ab0bc770e71a259b7966c500496b99010a/cogentic_research_papers/discrete_logarithm/paper.pdf)，36页 | Thm 1.2：固定特征下 \(\exp(((2+o(1))/\log\log\log n)(\log n)^2)\) 的零错误期望界 | Moore 行列式、仿射根结构、分布无关满秩采样、无需预分解的模数消元 |
| [LOGRANK：Square-Root Barrier](https://github.com/google-research/google-research/blob/4a7bc8ab0bc770e71a259b7966c500496b99010a/cogentic_research_papers/logrank_conjecture/paper.pdf)，37页 | Thm 1.1：实秩为 \(r\ge2\) 的布尔 \(0/1\) 矩阵，确定性通信复杂度 \(O(r^{1/2-\epsilon})\)，\(\epsilon=5\cdot10^{-6}\) | 布尔平方约束导出的三次张量恒等式、KL 二阶稳定性、系数截断界 |
| [EDGE：Edge Reconstruction](https://github.com/google-research/google-research/blob/4a7bc8ab0bc770e71a259b7966c500496b99010a/cogentic_research_papers/edge_reconstruction/paper.pdf)，47页 | Thm 1.1：\(n\ge4,m\ge1000n\) 的简单图由完整无标号删边多重集重构 | 平移不变齐次多项式消灭低阶矩、系数对偶、三阶联合分离 |
| [FP：Fictitious Play](https://github.com/google-research/google-research/blob/4a7bc8ab0bc770e71a259b7966c500496b99010a/cogentic_research_papers/fictitious_play_convergence/Fictitious_Play_Convergence.pdf)，32页 | Thm 1：特定同时更新与并列规则下的慢收敛输入族，\(\mathrm{Gap}\ge\kappa_d T^{-1/(d+1)}\) | 下降二项式基、整数移位与求和、无除法预像、稀疏余核 |
| [VC：Sample Compression](https://github.com/google-research/google-research/blob/4a7bc8ab0bc770e71a259b7966c500496b99010a/cogentic_research_papers/vc_sample_compression/Near_Quadratic_Sample_Compression.pdf)，30页 | Thm 1.1：VC 维 \(d\) 的样本压缩大小 \(O(d^2\log^2d)\)，附 \(O(d\log^2d)\) 比特；不自动给高效计算 | 熵增下界、观测分离能力、代表类、重构所需侧信息 |
| [NASH：Bimatrix Nash](https://github.com/google-research/google-research/blob/4a7bc8ab0bc770e71a259b7966c500496b99010a/cogentic_research_papers/bimatrix_nash_equilibrium/paper.pdf)，41页 | 输入位长的多项式时间，精确达到 \(1/5\) 近似阈值；不是误差为零的 Nash 均衡 | 多尺度指数滤波、耗散支付、kite 区域的混合修复 |
| [PROP：Subadditive Prophet](https://github.com/google-research/google-research/blob/4a7bc8ab0bc770e71a259b7966c500496b99010a/cogentic_research_papers/subadditive_prophet_inequalities/Subadditive_Prophet_Inequalities.pdf)，36页 | 独立次可加估值下，静态匿名价格的 \(O(\log\log\log m)\) 近似及相应下界 | 非均匀边际向量下“指数平方、代价加常数”的归纳推进 |
| [CE：Convex Games](https://github.com/google-research/google-research/blob/4a7bc8ab0bc770e71a259b7966c500496b99010a/cogentic_research_papers/ce_convex_games/CE_in_Convex_Games.pdf)，17页 | Thm 2：指定一阶黑箱模型、\(\epsilon=1/d\) 下，CE 查询下界 \(\exp(\Omega(d^{1/16}))\) | 条件期望伴随算子、两步误差分解、树分区恒等式 |

两个特别容易误读的地方：F-DET 的 README 将 \(\exp(O(\sqrt{\log p}\log\log p))\) 简写为 \(L_p[1/2,O(1)]\)，按定义应有 \(\sqrt{\log\log p}\) 而非 \(\log\log p\)，报告采用 PDF 的精确式。NASH 的显式参数含 \(K=3\cdot2^{56}\) 及 \(T=40\cdot2^{54}\cdot64^{K-1}+1\)；LOGRANK 的证明参数有 \(C=2^{38}\) 及 \(R_0=\lceil\exp(4\cdot10^6)\rceil\)。这些渐近结论不能直接读作当前小规模实现的效率保证。

## 三、最值得立即复用的六组工具

### 3.1 保留旧观测，再扩展新约束

F-LV Lemmas 4.4、4.6（pp.35–40）使用祖先消失因子

\[
P_{\rm anc}(X,Y)=\prod_{t<r}(b_tX-a_tY),\qquad \Delta f=P_{\rm anc}H.
\]

因此对所有旧点 \((a_t,b_t)\)，都有 \(\Delta f(a_t,b_t)=0\)。这个代数事实可以直接迁移为“在旧观测算子的核中选新自由度”。

对我们的 Riesel 对象，取旧通道总模数 \(M=\prod_i p_i^{h_i}\)，令 \(a'=a+tM\)，则

\[
\boxed{F_n(a')-F_n(a)=2^n(2atM+t^2M^2)\equiv0\pmod M\quad(\forall n\ge0).}
\]

若新增素数 \(q\nmid M\) 与指定指数类的合法根 \(r\) 已确定，则

\[
t\equiv(r-a)M^{-1}\pmod q
\]

同时保留旧通道并接入新根。例：\(a=7,M=195,q=17,r=4\)，取 \(t=6,a'=1177\)。旧模195读数对所有 \(n\) 保持；因为 \(4^22^4\equiv1\pmod{17}\) 且 \(\operatorname{ord}_{17}(2)=8\)，新增17通道对应 \(n\equiv4\pmod8\)。本次另对旧模195通道在 \(0\le n\le15\) 进行了整数回验。

精确 \(p\)-进赋值还需保留足够高的模数和非零商；只有模 \(p\) 标签不能决定赋值。\(q\mid M\) 时需广义 CRT 相容条件。对 RH，允许调整的是核或证书参数 \(c\)，并令 \(A\delta c=0\) 保留旧证据；不能任意改变真实 \(D_n\)。

### 3.2 低阶矩完全相同，未来三阶观测仍可完全相反

EDGE Theorem 4.2(1)（pp.24–25）的局部核心：若齐次次数 \(N\) 的

\[
P(y)=\sum_{|u|=N}c_u y^u,\qquad P(y+z\mathbf1)=P(y),
\]

则对所有 \(\deg R<N\)，有

\[
\boxed{\sum_{|u|=N}c_uR(u)=0.}
\]

证明：\(P\) 的任意低于 \(N\) 阶导数仍平移不变且是正次数齐次多项式，因此其在 \(\mathbf1\) 的值等于在0的值，均为0；下降阶乘单项式构成低阶多项式的基。

取三变量 Vandermonde 多项式即可得到两个分布：

\[
\mu_+=\operatorname{Unif}\{(2,1,0),(1,0,2),(0,2,1)\},
\]
\[
\mu_-=\operatorname{Unif}\{(2,0,1),(1,2,0),(0,1,2)\}.
\]

两者全部次数不超过2的矩相同：\(\mathbb E u_i=1\)、\(\mathbb E u_i^2=5/3\)、\(\mathbb E u_iu_j=2/3\)（\(i\ne j\)）。但

\[
\Omega(u)=(u_1-u_2)(u_1-u_3)(u_2-u_3)
\]

在 \(\mu_+\) 的全部支撑上为 \(+2\)，在 \(\mu_-\) 上为 \(-2\)。本次对十个次数不超过2的单项式及 \(\Omega\) 都做了精确核验。

这可编码为选定 X6 状态族 \(c_*+u_1E_1+u_2E_2+u_3E_3\)，另外三轴在该族固定。若未来操作语言包含 \(\Omega\)，只保存均值、方差及两两相关就无法保真。这个结论针对明确观测语言，不声称所有任务都必须保留所有高阶矩。

### 3.3 有限域独立性与复合模数消元

DLP Lemma 3.1（pp.10–11）给出 Moore 行列式：对 \(K\supseteq\mathbb F_q\)，

\[
\boxed{\det(z_i^{q^{j-1}})_{i,j=1}^r
=\prod_{j=1}^r\prod_{c\in\mathbb F_q^{j-1}}
\left(z_j-\sum_{i<j}c_iz_i\right).}
\]

非零恰好表示 \(z_i\) 对 \(\mathbb F_q\) 线性独立。比如 \(\mathbb F_4=\mathbb F_2[\alpha]/(\alpha^2+\alpha+1)\) 中，\(1,\alpha\) 的行列式为1。把全部数据仅放在基域 \(\mathbb F_p\) 内，相对该基域秩至多1；研究应用必须给出有效的扩张域编码。

DLP Lemma 6.3(2)（p.31）则解决另一种常见障碍：复合模数下不应只寻找可逆矩阵元素作为枢轴。若 \((u,v)\ne(0,0)\) 且 \(d=\gcd(u,v)=su+tv>0\)，整系数变换

\[
\begin{pmatrix}s&t\\-v/d&u/d\end{pmatrix}
\]

行列式为1，可把列的两项合并为 \((d,0)^T\)。在模 \(M\ge2\) 下、每个素数 \(p\mid M\) 上满列秩的关系矩阵，可用这样的 Bézout 合并完成消元而无需预先分解 \(M\)；对于一般右端必须检查相容性。

例：模6方程

\[
\begin{pmatrix}2&3\\3&2\end{pmatrix}y=\binom54
\]

所有矩阵元素都不可逆，但整行变换 \(U=\begin{pmatrix}-1&1\\-3&2\end{pmatrix}\) 给出

\[
UE\equiv\begin{pmatrix}1&5\\0&1\end{pmatrix},\quad Ua\equiv\binom55,
\quad y\equiv\binom45\pmod6.
\]

这适合真正具有线性关系的 CRT 证书、同余关系及有限模算子，不要求把非线性覆盖约束先假装成线性系统。

### 3.4 按尚未分开的状态对，衡量新增观测

VC Lemma 4.4（pp.17–18）把已有观测 \(W\) 的等价类记为 \(\tau\)，其概率质量为 \(w_\tau\)。新增 \(W'\) 后，分区熵增满足

\[
\boxed{\Delta H\ge\sum_\tau w_\tau
\Pr_{c_1,c_2\sim\nu_\tau}
[c_1|_{W'}\ne c_2|_{W'}].}
\]

其中两次条件抽样独立。每个旧类中，新签名概率为 \(q_j\) 时，分开概率为 \(1-\sum_jq_j^2\)，而 Shannon 熵至少为该数，因此得到公式。

对 Riesel 或有限 X6 候选状态，这提供了具体观测选择准则：评估一个新通道能拆开多少仍混在一起的候选状态对。必须先声明候选集合及权重；概率质量为零的状态不会被这个平均目标保护。若目标是最坏情形或未来操作保真，应另加对应约束。

论文的 VC 维1反例还说明：某些族的任意 \(k\) 个观测只能隔离 \((k+1)/m\) 的质量。不能把“每加一次观测都产生常数收益”当成普遍事实。

### 3.5 整数移位、离散积分和稀疏残差

FP Lemmas 7–10、13–16（pp.18–22）使用下降二项式基

\[
b_r^{(\ell)}(k)=\binom{k+\ell-r}{\ell-r},\qquad r=0,\dots,\ell.
\]

令 \(J\) 为超对角为1的幂零矩阵，则

\[
b(k-1)=(I-J)b(k),\qquad
b(k+1)=(I-J)^{-1}b(k)=\sum_{j=0}^{\ell}J^jb(k).
\]

求和也可由升一级的基在两个端点之差表示。于是多项式时间依赖的精确移位、块间累计与离散积分可以始终用整数矩阵运算。

更特殊但很有价值的算子是

\[
\mathcal T_\ell(P)=P^T-(I-J)^TP.
\]

论文给出的无除法递推 \(P=\mathcal S_\ell(Z,\phi)\) 使残差 \(\mathcal T_\ell(P)-Z\) 仅支撑于

\[
\{(2r,0):0\le r\le\lfloor\ell/2\rfloor\}.
\]

因此可以同时保存“已解部分、少数真正障碍、核参数 \(\phi\)”。本次对 \(\ell=2,\dots,6\) 的全部矩阵基验证了构造、残差位置和核坐标恢复；秩分别为7、14、22、33、45。这是对该具体算子的证据，迁移到我们的新更新算子时须重证其结构。

### 3.6 联合符号正性与模阶饱和

F-DET Lemma 5.1（pp.20–22）的可分离代数核心是有限群 Fourier 正性。若

\[
f(\ell)=\sum_ua_u(-1)^{\ell\cdot u},\quad
g(\ell)=\sum_ub_u(-1)^{\ell\cdot u},\quad a_u,b_u\ge0,
\]

则乘积的 Fourier 系数为非负卷积，因而

\[
\sum_{\ell\in\mathbb F_2^K}f(\ell)g(\ell)
=2^K(a*b)(0)\ge0.
\]

论文将这用于相容的数域理想特征。对我们的符号 CRT 字典，首先要证明符号来自同一个兼容的群表示。随意拼接边际符号没有正性：\((1,-1,-1,-1)\) 的总和为 \(-2\)，并且违反线性特征的乘法相容性。

F-DET Lemma 11.1（p.55）的另一个短核心：\(S\) 是 \(m\) 个不超过 \(B\) 的不同素数，\(B^k\le p-1\)，则不同多重集乘积仍是不同模 \(p\) 元素，所以

\[
|\langle S\bmod p\rangle|\ge\binom{m+k-1}{k}.
\]

若所有 \(s\in S\) 满足 \(s^M=1\)，且子群指数 \(I\le K\)，则

\[
\boxed{p-1\mid M\operatorname{lcm}(1,\dots,K).}
\]

它能为模阶覆盖补全提供具体预算；前提包括 \(\mathbb F_p^\times\) 循环群、足够的生成元信息及有效的指数上界。

## 四、由多尺度滤波提炼的加权有限窗口恒等式

NASH Lemma 3.1（pp.15–16）研究几何尺度滤波器 \(z_k(\xi)=1/(1+i\xi/\alpha_k)\)，其平均 \(\bar z=x+iy\) 满足

\[
D=x(1-x)-y^2=\frac1K\sum_k|z_k-\bar z|^2\ge0.
\]

这提示可以把尺度间差异和非对称误差放进明确耗散项。为了适配本项目有限整数窗口和 \(1/n^2\) 权重，本次另外推导如下恒等式。**下式是本次整理的离散带权版本，不是对原文定理编号的转述，也不作新颖性主张。**

### 命题：常参数指数滤波的加权能量分解

设 \(A\le B\)、\(K\ge1\)，输入 \(h_n\in\mathbb R\)，每个 \(0\le\rho_k<1\) 不随 \(n\) 变，定义

\[
y_{k,n}=\rho_ky_{k,n-1}+(1-\rho_k)h_n,
\qquad \bar y_n=\frac1K\sum_ky_{k,n},
\qquad c_k=\frac{\rho_k}{2(1-\rho_k)}.
\]

对任意非负权重 \(w_n\)，精确成立

\[
\begin{aligned}
\sum_{n=A}^{B}w_n(h_n\bar y_n-\bar y_n^2)
={}&\frac1K\sum_k\sum_{n=A}^{B}w_n(y_{k,n}-\bar y_n)^2\\
&+\frac1K\sum_kc_k\Bigg[
w_By_{k,B}^2-w_Ay_{k,A-1}^2\\
&\qquad+\sum_{n=A}^{B-1}(w_n-w_{n+1})y_{k,n}^2
+\sum_{n=A}^{B}w_n(y_{k,n}-y_{k,n-1})^2\Bigg].
\end{aligned}
\]

**证明。** 单通道递推给

\[
h_n=y_{k,n}+\frac{\rho_k}{1-\rho_k}(y_{k,n}-y_{k,n-1}).
\]

使用 \(2y\Delta y=\Delta(y^2)+(\Delta y)^2\)，乘 \(w_n\) 并求和；离散分部求和给出

\[
\sum_{n=A}^Bw_n(y_n^2-y_{n-1}^2)
=w_By_B^2-w_Ay_{A-1}^2
+\sum_{n=A}^{B-1}(w_n-w_{n+1})y_n^2.
\]

最后平均各通道，并使用 \(K^{-1}\sum_ky_{k,n}^2-\bar y_n^2=K^{-1}\sum_k(y_{k,n}-\bar y_n)^2\)。证毕。

若 \(w_n\) 非增且所有初值 \(y_{k,A-1}=0\)，右端全部非负，因此

\[
\langle h,\bar y\rangle_w\ge\|\bar y\|_w^2,
\qquad \|\bar y\|_w\le\|h\|_w.
\]

第二式由 Cauchy–Schwarz 得到（\(\|\bar y\|_w=0\) 时直接成立）。取 \(A\ge1,w_n=1/n^2\)，与项目现有加权范数一致。输入可以选真实 \(q_n\)，也可以另选明确定义的算术差额 \(\kappa_n-D_n\)；若选择曲率 \((\kappa_n-D_n)/n=-\Delta^2q_n\)，其范数对象已改变。对任何选定输入，正部映射的1-Lipschitz性质给出

\[
\big|\|(h)_+\|_w-\|(\bar y)_+\|_w\big|
\le\|h-\bar y\|_w.
\]

当 \(h=q\) 时，记 \(r=\|q-\bar y\|_w\)、\(v=\|(\bar y)_+\|_w\)，便得到原正部能量的明确支付区间

\[
\boxed{\max\{0,v-r\}^{\,2}\le S(q)\le(v+r)^2.}
\]

选择曲率作为输入时，上述正部不等式控制的是曲率；回到 \(S(q)\) 还需要逆二阶差分的锚点或边界数据及相应误差传播界，不能只用曲率与其滤波输出之间的残差代替 \(q\) 的残差。

**实际增量：** 可以把尺度不一致、时间增量、权重下降、窗口端点分别记账。不能删除非零初值的负边界项，也不能凭该恒等式得到真实算术亏缺的统一上界。

实际核验使用有理数精确运算：输入 \((3,-1,2,-2,1/3)\)、\(\rho=(0,1/2,3/4)\)、零初值，以及 \(n=4,\dots,8\) 的 \(w_n=1/n^2\)，等式两侧都为

\[
\frac{1246359631423}{6658877030400}.
\]

另有零输入、非零初值的例子，左侧为 \(-16401/16384\)，所有分项仍精确相等，直接展示边界项不可省略。

## 五、布尔约束与低秩近似：保留三阶耦合和残差

LOGRANK Lemma 3.4(3)（pp.15–16）利用 \(S^2=1\) 推导三阶矩关系。下面是本次从该机制整理出的常行列均值特例：设有限乘积概率空间上 \(S(x,y)\in\{-1,1\}\)，各行与各列均值都等于 \(m\)，中心化奇异展开为

\[
S(x,y)=m+\sum_i\sigma_i a_i(x)b_i(y),\quad \sigma_i>0,
\]

其中 \(a_i,b_i\) 中心化正交归一。令 \(T_{kij}=\mathbb E[b_kb_ib_j]\)。由 \(S^2=1\)，乘 \(b_k\) 并在 \(y\) 上平均得

\[
\boxed{-2m\sigma_k a_k(x)=\sum_{i,j}\sigma_i\sigma_jT_{kij}a_i(x)a_j(x).}
\]

所以当 \(m\ne0\) 时，一阶特征受到二阶乘积与三阶耦合张量的精确约束。只保留奇异值通常不足以重建这层约束；\(m=0\) 时上式不能除以 \(m\)。本次对 \(S=J_4-2I_4\)、Hadamard 特征核对了全部12个相关等式。

另有本次整理的近似一致性检查。令 \(A\) 为近似矩阵，\(R=S-A\)，则逐点

\[
A^2-1=-2SR+R^2,
\]

从而在有限概率测度下

\[
\boxed{\|A^2-1\|_{L^1}\le2\|R\|_{L^2}+\|R\|_{L^2}^2.}
\]

如果一个方案声称误差 \(\|S-A\|_2\le\varepsilon\)，却有布尔平方缺陷大于 \(2\varepsilon+\varepsilon^2\)，该误差声称就不可能成立。反过来，平方缺陷小不保证接近指定的 \(S\)：完全不同的符号矩阵也可有零平方缺陷。

## 六、值得保留为下一层证明路线的内容

以下内容的完整条件与公式在专题笔记中保留，适合按实际问题调用：

| 工具 | 数学收益 | 接入前真正需要补的条件 |
|---|---|---|
| F-LV 加权接受后的反向望远镜 | 在合适条件纤维上，局部失败累计为 \(\varepsilon\sum_{r=0}^h(3B)^r\)，稀疏密度在条件期望中消去 | 对所有可达纤维的统一估计；不能只用无条件成功率 |
| F-LV 离散 Laplace 平移稳定性 | 保留约束的小扰动带来显式 \((d+1)\alpha\Delta\) 与尾质量支付 | 正确条件切片、位移在格中、截断边界质量 |
| F-LV Gevrey/Mellin 尾界 | 显式分开窗口边界误差与频率截断误差 | 与现有 Green 包络比较总误差；真实算术输入固定 |
| F-LV 平滑权重 | 自由整数因子吸收局部公因子，密度因子精确抵销 | 可容许参数、坏导子等解析条件；不能直接把平滑整数替成素数 |
| DLP 分布无关满秩采样 | \(1-2K2^{-\ell}\) 的覆盖下界不要求已知抽样分布 | 独立同分布和真实合法的移位关系；不能伪造基向量关系 |
| EDGE 系数对偶 | 用单项系数测试低阶统计无法分离的组合 | 齐次与对角平移不变；总次数、重数带条件 |
| PROP 指数平方推进 | \(H(B,C)\to H(B^2,C+3)\) | 次可加性、独立抽样及对所有非均匀边际向量成立的归纳命题 |
| CE 条件期望算子 | \(A=PP^*\) 是正自伴收缩，近似均衡推出 \(\|X-Af(X)\|_2\le4\sqrt\varepsilon\) | 联合分布与条件期望保留；边际分布不能决定 \(P\) |

其中隐藏平方根 CRT 分裂概率 \(1-2^{1-\omega(N)}\)、带分母上界的有理数恢复、3-adic 提升后的整数回验，以及递归成本预算 \(c>a/(1-\theta^\alpha)\)，都适合作为独立算术工具留存，详见附录 A。

## 七、本次已经核验的内容与继续研究入口

| 证据文件 | 实际核验内容 |
|---|---|
| `agents/factorization_checks.py` / `.json` | 640个有序平滑表示、155个整数的精确权重；四个合数全部单位平方纤维；子群饱和例；Walsh 卷积及不相容反例 |
| `agents/algebra_checks.py` / `.json` | 模6 Bézout 消元、满秩概率的有限动态规划、三次张量等式、Vandermonde 低阶矩与三阶分离 |
| `agents/check_learning_kernels.py` / `.json` | 二项式移位与求和、无除法构造、稀疏残差位置与核维数 |
| `verify_bridge_identities.py` / `.json` | 三组有限窗口能量分解（含负边界与非恒定权重）、Riesel 旧通道保持、近似布尔平方缺陷 |
| `source_manifest.json` | 十篇 PDF 的固定来源、Git blob、SHA256、页数与字节数 |

这些检查均已实际运行；重复命令和依赖见 README。它们为所列局部结论提供有限证据，不能替代无限范围证明或未核读的解析链条。上文新恒等式有完整代数证明，因此不限于测试输入。

最自然的三个继续入口：

1. **Riesel 的候选新通道选择。** 在当前合法候选集合上，给每个新模数计算状态对分离质量，同时保持已验证模 \(p^h\) 与联合符号，比较覆盖改善与真实代价。
2. **RH 有限窗口的尺度诊断。** 固定真实 \(D_n\) 和既有 \(q\)，用有理 \(\rho_k\) 实现上面的加权恒等式；对比原 Green 包络，报告残差与边界支付是否改善。未解决的统一算术亏缺仍按原状态保留。
3. **摘要保真的压力例与补观测。** 先使用 Vandermonde 分布对和 Moore 秩证书，为当前允许观测建立最小反例；只有在声明的未来操作语言下才讨论是否已充分。

上述是从本次提取自然得到的研究路线，没有自动发布新任务、领取共享 CLAIM 或宣称原有开放问题已解决。

---

## 附录说明

以下保留三份完整专题提取：A 为两篇整数分解；B 为有限域、低秩与重构；C 为学习、博弈及离散工具。它们包含比概要更完整的命题编号、公式、适用条件、局部证明和有限验证结果。页码按原 PDF 印刷页码记录。



---

## 附录 A：两篇整数分解论文

### 读取边界与来源

固定源：google-research/google-research@4a7bc8ab0bc7，固定版本提交日期 2026-11-25。

- [A：Unconditional Integer Factorization in Time L_N[1/3,O(1)]](https://github.com/google-research/google-research/blob/4a7bc8ab0bc770e71a259b7966c500496b99010a/cogentic_research_papers/integer_factorization/paper.pdf)，54 页。PDF SHA256：9ac07593ca90c0f315af0b0214320823a43e7c905e6700948261ebb09a4d537d。
- [B：Unconditional Deterministic Subexponential Integer Factoring and Quadratic Nonresidue Construction](https://github.com/google-research/google-research/blob/4a7bc8ab0bc770e71a259b7966c500496b99010a/cogentic_research_papers/deterministic_factoring_l34/paper.pdf)，59 页。PDF SHA256：0ccf115516dab3cbeee15167f2dea62fcb29d03a19224cb4a9ae69a5ce402993。
- 两个 README 明示论文 CC-BY-4.0，Copyright 2026 Google LLC；本文对数学内容重新组织并保留出处。
- 两篇全文已取回，阅读了总论、关键定义、下列命题及其相关证明；没有完成全篇全部承重估计的逐行独立审查。
- 固定目录各含 README 和 PDF；README 声称 Lean 4 证明已完成、将在 companion 发布。该固定输入未提供 Lean 源及可执行校验结果。
- 所有外部算术内容作为进取数论的整数寄存器、有限域、系数空间或观测辅助工具吸收；不改 P000 / X6 本原定义。

### 1. 主结论应该怎样记录

A 的 Theorem 1.1（p.2）声称：单一统一经典概率多带 Turing 机对所有 N≥2 零错误输出完整素因数分解；期望位复杂度 L_N[1/3,105]，最坏随机带上的确定性工作空间 L_N[1/3,40]。其中

\[
L_N(\alpha,c)=\exp\{c(\log N)^\alpha(\log\log N)^{1-\alpha}\},
\quad
T\le L_N[\alpha,c]\iff
\limsup_{N\to\infty}
\frac{\log\max(1,T(N))}
{(\log N)^\alpha(\log\log N)^{1-\alpha}}\le c.
\]

这是论文主张；本次独立确认的是若干局部代数机制和有限验证，不将整套渐近复杂度自动标为本项目已接受定理。

B 的 Theorems 1.1–1.3（p.4）分别声称：

1. 每个合数 N≥4 可确定性找非平凡因子，代价 \(O(\exp(3(\log N)^{3/4}))=L_N[3/4,o(1)]\)。
2. 给定非完全幂合数 N 及偶数 \(\widetilde M\)，满足每个 p|N 都有 p−1|\(\widetilde M\)，可在
   \[
   C_1\exp\{C_{\rm split}\sqrt{\log N}\log\log(N+16)\}
   (\log\widetilde M)(\log N)^2
   \]
   位操作内确定性分裂；对奇素数 p，可在
   \[
   C_2\exp\{C_{\rm split}\sqrt{\log p}\log\log(p+16)\}
   \]
   内构造二次非剩余。
3. 给定奇非完全幂合数 N≥9，在上述分解量级内直接找因子，或构造共同 p−1 倍数，且
   \[
   \log\widetilde M\le \exp((\log N)^{0.65}).
   \]

#### 已发现的一处摘要记号偏差

B 的 README 将 QNR 的 \(\exp(O(\sqrt{\log p}\log\log p))\) 写成 \(L_p[1/2,O(1)]\)。按它自己定义的 L 记号，后一量级应为 \(\exp(O(\sqrt{\log p}\sqrt{\log\log p}))\)，两者相差一个 \(\sqrt{\log\log p}\) 因子。PDF Theorem 1.2 没有这个错误简称。提取时采用 PDF 的精确式。此发现涉及摘要记号，没有提供否定主证明的反例。

### 2. 最值得优先拿来的局部工具

#### 2.1 祖先消失扰动：增加自由度，同时严格保留已完成约束

A §4、Lemma 4.4 与 4.6（pp.35–40）将沿途已求值点 \((a_t,b_t)\) 编入

\[
P_{\rm anc}(X,Y)=\prod_{t<r}(b_tX-a_tY).
\]

任何 \(\Delta f=P_{\rm anc}H\) 在所有祖先点取零。因此在新的随机化或搜索中保留每个祖先的完整求值，而非只保留最终标量的某个近似。

可单独手证的加强接口：若还要保持基点 \(f(g_0,g_1)\) 与模 3 多项式，则用

\[
\Delta f(X,Y)=3(g_1X-g_0Y)P_{\rm anc}(X,Y)H(X,Y),
\quad \deg H=d-r-1.
\]

它保持同次次数、每个旧求值、基点值和模 3 系数。系数大小、后续可达性及条件采样分布需要另外计算。

**接入 Riesel 的直接整数版本。** 对 \(F_n(a)=a^22^n-1\)，已有通道模数 \(M=\prod_i p_i^{h_i}\)，取 \(a'=a+tM\)，则

\[
F_n(a')-F_n(a)=2^n(2atM+t^2M^2).
\]

因此所有 \(n\ge0\) 和全部旧通道的模 \(p_i^{h_i}\) 读数同时保持。若新增素数 \(q\nmid M\) 已有合法根 \(r\) 满足 \(r^22^{n_*}\equiv1\pmod q\)，则

\[
t\equiv(r-a)M^{-1}\pmod q
\]

精确接入该新约束。这是既有 CRT 扩展的“旧观测保持证书”，适合写进每次新增通道的证据。

- 要保持精确赋值 \(v_{p_i}(F_n(a))=v\)，至少需要保留模 \(p_i^{v+1}\) 的非零商信息；只有 mod p 标签不够。
- \(q\mid M\) 时应按广义 CRT 的相容条件处理，不能用逆元公式。
- 改 a 是更换初始整数寄存器；它不更改固定 X6 anchor 或既有 \(x\mapsto2x+1\) 更新规则。
- 每个根选择仍需保留联合分支，不把同一边际覆盖当成同一个完整状态。

**接入 RH 三角矩。** 在候选包络或系数参数 c 上，把已验证观测写为矩阵 Ac。新扰动只选 \(\delta c\in\ker A\)，从而保持旧观测。新增观测行不在旧行空间时才有新的可调方向。这里 c 是我们构造的包络/证书参数，真实算术序列 \(D_n\) 仍是固定输入，不能随意改动。

#### 2.2 加权接受后的反向望远镜：把稀疏密度从逐层损失中消掉

A Lemma 4.6（pp.39–40）的要点是按候选权重 \(w_t(a)\) 接受，而不是先逐层乘上粗糙的稀疏性倒数。

设每层实际权重和 \(Z_t\ge\mu_t/2\)，于是候选选择核满足

\[
K_t(a\mid{\cal H}_t)\le \frac{2w_t(a)}{\mu_t}.
\]

如果在相同祖先求值条件下

\[
\sum_a {\mathbb E}[w_t(a)\mid{\cal H}_t]\le \frac32\mu_t,
\]

并且每个可达后继求值纤维上局部失败概率都至多 \(\varepsilon\)，每节点候选子节点数≤B，那么条件期望的塔式法则逐层给出

\[
{\mathbb P}(\text{某层失败})\le
\varepsilon\sum_{r=0}^{h}(3B)^r
\]

加上另行列出的超时及尾部概率。这里的稀疏密度 \(\mu_t\) 在 \((2/\mu_t){\mathbb E}w_t\) 中被消掉。

A 的具体参数是 B≤\(\log_2N\)、h≤\(0.65\log\log N\)、局部失败至多 \(2e^{-25(\log\log N)^2}\)，最终约束到 \(e^{-23(\log\log N)^2}\) 量级。

**可用场景：** 多层 CRT 候选扩展、随机骨架选择、条件关系搜索。**真正需要补的量：** 对全部可达祖先求值纤维有效的局部失败界。无条件采样成功率、固定窗口测试或只看单层边际，不能替代这个条件估计。对 RH 统一素数亏缺而言，这提供组织条件误差的方式，不提供缺失的素数亏缺上界。

#### 2.3 离散 Laplace 权重的平移稳定性

A Lemma 4.2(4)（p.29，证明 pp.31–32）取截断权重

\[
G(c)=e^{-\alpha\|c\|_1}
\]

限制到整数仿射切片 \(U=(c_*+L)\cap[-W,W]^{d+1}\)。若切片分布落在 \(\|c\|_\infty>5W/8\) 的概率≤\(\varepsilon_{\rm tail}\)，扰动 \(\delta\in L\cap[-\Delta,\Delta]^{d+1}\)、\(\Delta\le W/8\)，且

\[
\varepsilon_{\rm lip}=(d+1)\alpha\Delta\le 1/2,
\]

那么对每个 \(0\le\Phi\le1\)，

\[
e^{-\varepsilon_{\rm lip}}\mathbb E\Phi(c)-\varepsilon_{\rm tail}
\le
\mathbb E\Phi(c+\delta)
\le
e^{\varepsilon_{\rm lip}}\mathbb E\Phi(c)+\varepsilon_{\rm tail}.
\]

局部证明仅用 \(|\|c+\delta\|_1-\|c\|_1|\le\|\delta\|_1\) 及边界尾质量，具有独立可复用性。它适合需要“保留旧约束，再作小扰动”的采样；概率分布必须在所声明的切片上，不能用未条件化的尾概率。

#### 2.4 对称区间混合：把离散线性型估计降为区间平均

A Proposition 2.4（p.9；Appendix A，pp.51–52）：

\[
S_n(w)=\sum_{i=0}^{n} w_i a^i(-b)^{n-i},
\quad w_i\sim{\rm Unif}([-W_0,W_0]\cap\mathbb Z),
\]

其中 \(n\ge1\)、a,b 非零且互素、\(C=\max(|a|,|b|)\)、\(W_0\ge4nC\)。设 \(\widetilde q_n\) 是将各 \(w_i\) 换为连续均匀变量后的密度，\(R_n=W_0\sum_i|a|^i|b|^{n-i}\)，\(\Delta\widetilde q_n(R)=\widetilde q_n(R)-\widetilde q_n(R+1)\ge0\)。对每个 \(f:\mathbb Z\to[0,1]\)，

\[
\left|\mathbb E f(S_n)-
\sum_{R=0}^{R_n}\Delta\widetilde q_n(R)\sum_{z=-R}^R f(z)\right|
\le \frac{9n(n+1)C}{W_0}.
\]

质量和距1同样至多这个误差，且小半径部分总质量≤\(R_0/(W_0C^n)\)。这样，复杂系数随机变量的观测可由对称区间平均控制。

对本项目的价值是明确的“输入分布替换支付”；不能自动拿到比既有有理 Green 包络更小的误差，需把新增 \(9n(n+1)C/W_0\) 与原有支付比较。

#### 2.5 Gevrey 截断给显式 Mellin 尾界

A Lemma 3.1（pp.15–16）给出短区间指标的上下光滑包络。若 \(0<\delta\le1/2\)、\(0<\eta\le1/8\)、\(\sigma=\eta\delta/2\)，则

\[
\psi_-\le1_{[1,1+\delta]}\le\psi_+,
\quad
\int_{\mathbb R}|\widehat\psi_\pm(it)|\,dt
\le120+4\log(1/\eta),
\]

且 \(T\ge2000/\sigma\) 时

\[
\int_{|t|>T}|\widehat\psi_\pm(it)|\,dt
\le
\frac{10^6\delta}{\sigma}(1+\sqrt{\sigma T})
e^{-\sqrt{\sigma T}/10}.
\]

它把窗口边界误差和频域截断误差分开显式支付。若对真实三角矩换核，应另计

\[
\left|\sum_n\frac{\phi(n)-\psi(n)}n(\kappa_n-D_n)\right|
\le
\sum_n\frac{|\phi(n)-\psi(n)|}n|\kappa_n-D_n|.
\]

所以优先试验已固定输入的核误差预算是否真的改善，再决定扩大窗口。


#### 2.6 混合平滑权重：一个自由整数因子吸收公因子

A Definition 3.4 / Lemma 3.5（pp.18–19）定义 r=4u、\({\cal P}(y)=\{p:y/2<p\le y\}\)，令

\[
\widetilde w_{y,u}(n)=\frac1{r!}
\#\{(m,p_1,\ldots,p_{r-1}):
y/2<m\le y,\ p_j\in{\cal P}(y),\
mp_1\cdots p_{r-1}=n\}.
\]

正权重只支持 y-平滑整数，且 \(0\le\widetilde w\le1\)。把 \(n=M_{\rm sm}\prod_{q\in{\cal P}(y)}q^{e_q}\)、\(E=\sum e_q\) 分解后，精确公式是

\[
\widetilde w(n)=
\begin{cases}
1_{E=r}/\prod_qe_q!,&M_{\rm sm}=1,\\[2mm]
1_{y/2<M_{\rm sm}\le y}\,1_{E=r-1}/(r\prod_qe_q!),&M_{\rm sm}>1.
\end{cases}
\]

这里“已知完整分解后可多项式时间计算权重”是明示输入条件，不能用来循环声称已经解决分解。

若在等差数列 \(z+mt\) 中 \(g=\gcd(z,m)\le y^{3/10}\)，由于所有选取素数都大于y/2，公因子g必须进入自由整数因子。写 \(m'=m/g\)，局部密度产生精确消去

\[
\frac1g\cdot\frac{\varphi(m')}{m'}\cdot\frac1{\varphi(m')}=\frac1m.
\]

原文进一步在“可容许参数、长度区间、无坏导子因子”等条件下，证明权重等差平均与通用密度 \(\nu\) 的相对误差≤\(e^{-27(\log\log N)^2}\)。这些解析条件需要整体携带。

**对本项目的用途：** 构造可精确计算的正权重探针，使某些局部算术因子由设计抵销。它探测的是特别构造的平滑整数集合；真实素数亏缺问题仍需独立连接式。值得拿来的是“重新设计观测权重以消去局部偏差”的方法，以及上面的精确有限恒等式。

### 3. 与 CRT、模阶和“联合残差”最相关的结构

#### 3.1 子群指数饱和

B Lemma 11.1（p.55）有一个很干净的独立算术核心。

给定素数 p、互异素数集合 S⊂[1,B]，m=|S|，且 \(B^k\le p-1\)。S 的 k 元多重集乘积都是小于 p 的不同正整数，因此在模 p 下仍互异：

\[
|\langle S\bmod p\rangle|
\ge {m+k-1\choose k}.
\]

若 M 对每个 s∈S 都满足 \(s^M\equiv1\pmod p\)，利用 \(\mathbb F_p^\times\) 的循环性得到 \(|G|\mid M\)。若指数 \(I=(p-1)/|G|\le K\)，则

\[
p-1\mid M\operatorname{lcm}(1,\ldots,K).
\]

原文把它同时应用于 N 的全部未知素因子，要求

\[
|S|\ge B/(6\log B),\quad
K_{\rm idx}\ge B\exp\!\left(\frac{\log N}{\log B}\log(6\log N)\right),
\quad P^-(N)>K_{\rm idx},
\]

并给出 \(\log\operatorname{lcm}(1,\dots,K_{\rm idx})=(1+o(1))K_{\rm idx}\)。

**对本项目：** 可用于模阶覆盖的确定性补全、缺失模阶预算和验证器。原文“能低成本找到大量 M”的部分仍依赖其前面的大型解析证明。不能从一个小集合无条件推出它已覆盖整个单位群。循环群前提必需；不可照搬成任意 X6 关系群的阶结论。

有限例：p=31，S={2,5}，M=15，B=5，k=2。多重集给 |G|≥3，实际 |G|=15、指数2；粗上界 K=10，因此 \(15\operatorname{lcm}(1,\ldots,10)=37800\) 是30的倍数，M本身不是。

#### 3.2 Walsh 正性需要联合相容，才能消掉负尾

B Lemma 5.1（pp.20–22）构造 \(2^K-1\) 个二次域及两两双二次合成域上的相容理想特征。其承重假设包含：小整数、小范数主理想及单位上的特征均为+1，以及合成域上特征延拓相容。

设 \(b_\ell(n)\) 是域 \(\ell\) 中范数 n 的理想特征之和。原文证明存在 \(0\le b_0(n)\le\tau(n)\)，使得在 \(\gcd(n,P_Kq)=1\) 上

\[
b_0(n)+\sum_{\ell\in\mathbb F_2^K\setminus\{0\}}b_\ell(n)
\ge 2^K1_{P^+(n)\le Y}.
\]

于是

\[
\max_{\ell\ne0} S_\ell^{\rm cop}(X)
\ge
\Psi_{P_Kq}(X,Y)-\frac{X(\log X+1)}{2^K-1}.
\]

可独立吸收的有限代数事实是：若每个局部因子在群 \(\mathbb F_2^K\) 上有非负 Fourier 系数，局部因子的乘积对应非负系数的卷积，整体和为 \(2^K\) 倍的零频系数，因而非负。

这与保留联合分支、相位及符号 CRT 信息高度契合。仅有各边际符号没有保证：K=2 时随意取 \(b=(1,-1,-1,-1)\)，总和为−2；其中非零三点的符号乘积为−1，违反线性特征的相容关系。真正的收益来自已证明的联合兼容代数。

后续研究可测试 Riesel 的符号 CRT 字典能否给出某个已定义 \(\mathbb F_2^K\) 观测族及非负 Fourier 分解；其存在性需要用当前通道关系证明，不能直接把本论文的理想特征当成我们的字典。

#### 3.3 素理想偶赋值之后仍有平方类残差

A Proposition 2.5（pp.9–10）对奇数次数 d 的不可约整数多项式给单生成序 \(A=\mathbb Z[\theta]\)、判别式 \(\widetilde\Delta\)，令

\[
V_A=\{x\in K^\times:l_{\mathfrak p,A}(x)\equiv0\pmod2
\text{ for all maximal }\mathfrak p\}.
\]

则

\[
\dim_{\mathbb F_2}(V_A/(K^\times)^2)
\le2d\log_2(|\widetilde\Delta|+4)+d.
\]

原文使用局部 Jordan–Hölder 长度处理非极大序，在无判别式坏素数处它退化为普通素理想赋值。价值是：清掉局部奇偶读数后，剩余单位、类群及坏素数信息进入一个有限维残差空间，而非被默认为零。这种“明确剩余空间，再添加分离观测”的做法可迁移到我们现有读数完备性研究；数域维数上界只对该数域对象成立。

#### 3.4 隐藏平方根分支保证精确的 CRT 成功率

A Lemma 5.3（p.44）：N为奇数且 \(k=\omega(N)\ge2\)。独立均匀取单位 \(z_i\)，只把 \(w_i=z_i^2\bmod N\) 提供给关系构造程序。程序基于 w 和独立随机性选非空 T，并给出 \(Y^2=\prod_{i\in T}w_i\bmod N\)。最后才打开 \(Z=\prod_{i\in T}z_i\bmod N\)。则在完整可见记录条件下，

\[
\Pr(1<\gcd(Z-Y,N)<N)=1-2^{1-k}.
\]

证明是 CRT：平方根核有 \(2^k\) 个独立符号，只有全+与全−两个失败。若算法提前看到 z 并故意令Y=Z，概率变成0；“只依赖平方的记录”是实质前提。该结果不是模型盲审制度，而是精确的算术信息流条件。

### 4. 适合精度、递归与验证器的附加提取

#### 4.1 从近似数恢复精确有理数

B Lemma 7.2(3)（pp.30–31）使用 Legendre 连分数准则：

\[
|x-p/q|<1/(2q^2),\ \gcd(p,q)=1
\Longrightarrow p/q \text{ 是 }x\text{ 的连分数收敛分数}.
\]

若已知分母≤Q，误差区间半径<\(1/(2Q^2)\)，同一区间最多容纳一个候选有理数。原文 TryPair 再核验输出满足 \(\ell^{E_\ell}\equiv1\bmod N\)。适合“低精度探索→区间决定能否恢复→整数回验”的路线；精度不够时继续缩小区间即可，无需预设浮点结果就是精确关系。

#### 4.2 3-adic 快速精度提升后整数回验

A Lemma 5.2（pp.43–44）在模3不可约、奇次数d的数域序中，利用 \(3^d\equiv3\bmod4\) 对平方 \(\alpha_0\) 取初始根

\[
\beta_0=\alpha_0^{(3^d+1)/4}\in\mathbb F_{3^d}.
\]

随后 Newton–Hensel 逐次倍增3进精度，同时更新逆导数。原文给定系数界 \(2^{B_{\rm bit}}\)，精度达到 \(3^{2^K}>2^{B_{\rm bit}+2}\) 后用平衡代表恢复整数多项式，最后直接检验 \(\widehat\beta^2=\widetilde\Gamma\)。把局部算术恢复转成全局精确结论所需的关键量是系数界，不是单纯“迭代收敛”。

#### 4.3 递归缩小输入的常数预算公式

A 总论p.5、最终复杂度证明pp.47–49，递归输入≤\(\frac12\sqrt N\)。一般地，若一次外层的递归调用预算为 \(L_N[\alpha,a]\)，每个子输入≤\(N^\theta\)，拟证 \(T(N)\le L_N[\alpha,c]\)，则指数预算应满足

\[
a+c\theta^\alpha<c
\quad\Longleftrightarrow\quad
c>\frac{a}{1-\theta^\alpha}.
\]

还需列入非递归成本及外层重启成功概率。A 使用 \(\alpha=1/3,\theta=1/2,a=21.15,c=104\)，有 \(21.15+104\cdot2^{-1/3}<104\)，最后报告105。它是适合复算的资源预算式，可用于我们需要递归下降的精确搜索与证书生成。

### 5. 有限核对记录

脚本：factorization_checks.py。已实际运行，覆盖：

- y=20、4个因子槽的混合平滑权重：640个有序表示、155个不同整数，逐项核对归一化精确公式。它只验证组合恒等式，参数不在原文渐近解析范围。
- N=15、45、105、225 的所有单位及全部平方纤维；每个纤维的隐藏根拆分比例分别为1/2、1/2、3/4、1/2。
- p=31、S={2,5} 的子群饱和例。
- \(\mathbb F_2^3\) 上非负 Fourier 系数乘法/卷积恒等式；并列出 \(\mathbb F_2^2\) 非兼容符号的负和反例。

这些是抽出的局部工具的有限证据，不是运行了两篇完整分解算法。

### 6. 建议吸收顺序

1. 立刻纳入可手证工具层：祖先约束保持、CRT旧通道保持公式、有限群 Walsh 非负卷积、隐藏平方根 CRT 概率、子群指数饱和核心、带分母界的有理恢复。
2. 用固定输入作对照实验：对称区间混合与 Gevrey 截断能否减少已有核的总误差支付；按“新误差+旧支付”比较，保留失败样例。
3. 作为新的证明路线：条件纤维上的加权望远镜、相容符号族的 Walsh 正性提升。先定义该家族和条件估计，再谈统一结论。
4. 两篇主算法按原文定理及其完整依赖树保存，等待逐段数学复核或实际 Lean 源回读；目前可用局部成果已经足够形成具体研究增量。





---

## 附录 B：有限域、低秩与重构

固定来源：`google-research/google-research@4a7bc8ab0bc7/cogentic_research_papers`。本笔记覆盖 `discrete_logarithm`、`logrank_conjecture`、`edge_reconstruction`。正文PDF已由授权GitHub连接器读取，并保存为本地同名PDF及`pdftotext -layout`文本。页码为PDF印刷页码。下述“局部核验”指列明的短证明与精确示例；三篇主定理的全部承重证明尚未完成独立审核。

### 一、离散对数：优先吸收有限域线性结构和复合模数线性代数

源：[Discrete Logarithms in Finite Fields of Fixed Characteristic in Sub-Quasi-Polynomial Time](https://github.com/google-research/google-research/blob/4a7bc8ab0bc770e71a259b7966c500496b99010a/cogentic_research_papers/discrete_logarithm/paper.pdf)。

#### 1. 原文主张与真正可提取的结构

Theorem 1.2，pp.2–3：对显式给出的有限域`F_{p^n}`及非零`g,h`，声称有无条件零错误Las Vegas算法，返回`g^x=h`，或证书`g^E=1,h^E≠1`。固定`p`时，最坏实例期望位复杂度为

\[
\exp\!\left(\frac{2+o(1)}{\log\log\log n}(\log n)^2\right).
\]

更一般沿`log p/log log n→0`的序列，界为`exp(o((log n)^2))`。这是原文主张；适用对象为小特征有限域DLP。作者用`pn`表示`p·n`时，不能误读成域大小`p^n`；清楚的指数式最不易混淆。

核心机制（pp.3–6）：以稀疏线性化多项式代替一般高次多项式，将根集的置换对称群限制在仿射线性群。`q0`为素数幂，`q=q0^t`，模板

\[
L_Z(T)=\sum_{j=0}^{m-1}c_j(Z)T^{q_0^{t+j}}
       +\sum_{j=0}^{m}b_j(Z)T^{q_0^j}+d_0(Z).
\]

设系数域含`F_{q0}`。若线性项非零、最高指数为`q0^N`，代数闭包中的根集是`N`维`F_{q0}`仿射空间，所以Galois作用落入`AGL_N(F_{q0})`，其阶

\[
|\operatorname{AGL}_N(\mathbb F_{q_0})|
=q_0^N\prod_{j=0}^{N-1}(q_0^N-q_0^j)
<q_0^{N(N+1)}.
\]

这是选择结构化模板来降低分裂代价的具体方法。根数`D=q0^N`时，后者的对数是`O((log D)^2/log q0)`，比任意`D`个根的`D!`对称群预算小得多。要把它用于我们已有对象，应先找到真实的有限域线性作用；一般整数或CRT记录不会自动满足这种结构。

#### 2. Moore行列式：有限域线性独立的精确证书

Lemma 3.1，pp.10–11。若`K⊇F_q`，则

\[
\det(z_i^{q^{j-1}})_{i,j=1}^{r}
=\prod_{j=1}^{r}\prod_{c\in\mathbb F_q^{j-1}}
\left(z_j-\sum_{i<j}c_i z_i\right).
\]

因此行列式非零恰等价于`z1,…,zr`对`F_q`线性独立。所有Frobenius指数共同平移`a≥0`后，行列式只是原式的`q^a`次幂，独立性不变。仿射版使用行`(1,z_i,z_i^q,…,z_i^{q^{r-2}})`。

已逐步核读其归纳证明：将行列式视为最后变量多项式，其根恰包含此前元素的全部`F_q`线性组合，次数和首项系数相等，得乘积分解。

小例：在`F4=F2[α]/(α²+α+1)`中，`z1=1,z2=α`，行列式`α²−α=1`；`z1=z2=1`则为0。必须使用扩张域：若所有`z_i`都仅在同一个`F_p`中，相对`F_p`的秩至多1，不能把一串整数模p数据直接包装成高秩Moore证书。

#### 3. 一条可单独复用的群生成判据

Lemma 3.2，pp.11–12。`dim_F V=N≥2`。令

\[
T_{\varphi,u}(v)=v+\varphi(v)u,\qquad u\in\ker\varphi.
\]

若`G≤GL(V)`不可约，包含某个非零`φ0`对应的全部`T_{φ0,u}`，并且`det(G)=F×`，则`G=GL(V)`。

已逐步核读：取所有“其整族剪切均在G内”的泛函集合`S`；标量封闭、共轭封闭及`T_{φ1,w}`给出的`φ2↦φ2+φ1`保证`S`是非零不变子空间。不可约性给`S=V*`，故包含所有初等矩阵、包含`SL(V)`；再用行列式满射补齐`GL(V)`。对研究“局部更新到底生成多大作用群”有直接价值，但必须核对整族剪切条件，不能用“含一个剪切”代替。

#### 4. 稀疏仿射多项式铅笔的满群判据

Lemma 3.3，pp.12–14，短证明已核读。`q0≥3`为素数幂，系数域`k`包含`F_{q0}`，`N≥2`，且`{0,N−1,N}⊆I⊆{0,…,N}`。对`r=0,1`及`k`内系数，写

\[
L_r(T)=\sum_{i\in I}a_{r,i}T^{q_0^i}+\delta_r,
\quad A_r(T)=\sum_{i\in I}a_{r,i}T^{q_0^i-1},\quad L_Z=L_0+ZL_1.
\]

在两行列式

\[
a_{0,N}a_{1,0}-a_{1,N}a_{0,0}\ne0,
\qquad a_{0,N}a_{1,N-1}-a_{1,N}a_{0,N-1}\ne0,
\]

及`gcd(A0,A1)=gcd(L0,L1)=1`条件下，原文证明几何Galois群为`AGL_N(F_{q0})`。证明的可复用步骤是：局部无穷处分歧迫使一整族超平面剪切；不可约性加上上项判据给满线性群；中央非平凡标量消掉一阶余循环，保证完整平移群。

具体可检验模板：在`F3`上

\[
L_Z(T)=T^9+Z(T^3+T)+1.
\]

此时`N=2`，两行列式均为1；`A0=T8,A1=T2+1`互素；若`T3+T=0`，则`T9+1`不可能同时为零，故第二互素条件也成立。判据给几何群阶`9·8·6=432`。这是条款完整的示例，不能把它外推为所有稀疏多项式的结论。

#### 5. 分裂概率的显式成本

Lemma 5.1，pp.25–26。在其“good pencil”、椭圆曲线、几何群与常数域条件均成立时，令

\[
G=\operatorname{AGL}_N(\mathbb F_{q_0})\times S_{N_R}.
\]

允许的分裂参数个数满足

\[
N_{\rm split}\ge\frac{|k|}{|G|}
-2(N+N_R+1)\sqrt{|k|}-(2N_R+n+10).
\]

只要`|k|≥max{64(N+NR+1)²|G|²,4(2NR+n+10)|G|}`，便得成功概率至少`1/(2|G|)`。可吸收的是“明确列出主项、几何误差和异常集成本”的方法；本次未完成good pencil所有几何假设的独立审核，因此不能单独拿最终概率用于任意模板。

#### 6. 任意采样分布下的增广满秩引理

Lemma 6.3(1)，pp.30–31。`F`为有限域，维数`K≥1,ℓ≥2`，`b_j`为标准基。所有`u_t`、`v_{j,s}`相互独立、同服从任意分布`D`。共取`Kℓ`个`u_t`和`Kℓ`个`b_j+v_{j,s}`，则

\[
\Pr\!\left[\operatorname{span}\bigl(\{u_t\}\cup\{b_j+v_{j,s}\}\bigr)=F^K\right]
\ge1-2K\,2^{-\ell}.
\]

已逐步核读证明。第一批的跨度`W`若承载的分布质量不足1/2，则`K`个长度`ℓ`块中必有一个未增秩块，其发生概率≤`2^{-ℓ}`；否则对每个`j`有一个`v_{j,s}∈W`的失败概率≤`2^{-ℓ}`，从而回收所有标准基。真正有用之处：不要求降阶器输出均匀，但依赖“同分布、相互独立、允许加标准基”三个条件。

精确有限例已算：`F2²,ℓ=4,D=(1,2,3,4)/10`，以子空间动态规划得到失败概率`17560714981/10^15≈1.7560714981e-5`，小于通用上界`1/4`。该计算仅核验这一个分布实例；通用保证来自上述证明。

#### 7. 不先分解模数的Bézout消元

Lemma 6.3(2)，p.31。设`M≥2,R≥K≥1`，对`E∈(Z/MZ)^{R×K}`，如果对每个`p|M`都满列秩，则行模生成`(Z/MZ)^K`；用`xgcd`合并列元素、检测枢轴与`M`互素，可在原文界`O(RK²(log M)²)`位操作内完成关系消元。原文的输出保证针对已满足输入等式的循环群关系。若将此方法用于一般模线性方程`Ey=a`，应核对右端相容（消元后检查剩余零行的右端亦为零）；满列秩保证相容解唯一，不保证每个`a`都有解。无需预先获得`M`的素因子。

关键消元操作：`d=su+tv=gcd(u,v)`时，左乘

\[
\begin{pmatrix}s&t\\-v/d&u/d\end{pmatrix},\qquad\det=1,
\]

把列`(u,v)^T`变成`(d,0)^T`。不能直接套“找一个单位元素枢轴”的域上高斯消元。

精确例：模6矩阵`E=[[2,3],[3,2]]`所有元素均非单位，但`det E≡1`。对`Ey=(5,4)^T`，行变换`[[-1,1],[-3,2]]`给`[[1,5],[0,1]]`和右端`(5,5)`，得`y=(4,5)`。这是适合我们CRT/联合残差计算的直接工具，已用整数精确回算。

### 二、Log-Rank：提取高阶闭包和受控倾斜，不急于搬用主复杂度界

源：[Breaking the Square-Root Barrier for the Log-Rank Conjecture](https://github.com/google-research/google-research/blob/4a7bc8ab0bc770e71a259b7966c500496b99010a/cogentic_research_papers/logrank_conjecture/paper.pdf)。

#### 8. 主定理的精确规模

Theorem 1.1，p.2：`ε=5×10^{-6},C=2^{38},C'=750C`；布尔矩阵实秩`r≥1`有单色矩形密度至少`2^{-Cr^{1/2-ε}}`，`r≥2`时确定性通信复杂度≤`C'r^{1/2-ε}`。高秩论证的门槛为`R0=ceil(exp(4×10^6))`。本次已视觉核对页2，避免将`2^{38}`误读成238。

该主界有渐近数学价值，但其常数及阈值不能支持我们当前小秩状态表的现成压缩收益；实际更值得吸收的是下述恒等式和可局部证明的不等式。

#### 9. 布尔闭包强迫三阶矩约束

Lemma 3.4(3)，pp.15–16，式(3.3)。原文使用一般的带非恒定首奇异向量的分解。下述是我们从`S²=1`自行推出、条件更直观的特例：

设有限积测度`μX×μY`下，`S(x,y)∈{−1,1}`，所有行均值和列均值都等于`m`，且

\[
S(x,y)=m+\sum_{i=1}^{d}\sigma_i a_i(x)b_i(y),
\]

其中`σ_i>0`，`a_i,b_i`为实函数，分别中心化且正交归一。令

\[
T_{kij}=\mathbb E_Y[b_kb_ib_j].
\]

对每个`x,k`，平方并对`b_k`投影，严格得到

\[
-2m\sigma_k a_k(x)
=\sum_{i,j}\sigma_i\sigma_jT_{kij}a_i(x)a_j(x).
\tag{B1}
\]

因此当`m≠0`时，一阶特征由三阶矩张量控制的二次式恢复。`m=0`时这条恢复关系退化。只保留均值、协方差、奇异值可能遗漏此类高阶闭包信息。

若`S²=1+η`，同一步计算给出右端与左端之差`E_Y[η(x,Y)b_k(Y)]`，其绝对值≤`||η(x,·)||_{L²(μY)}`。这是声明了实际残差来源的近似版本，而非把非布尔观测强套成布尔。

精确算例：`S=J4−2I4`，均匀测度下`m=σ_i=1/2`。取四行

`a=(1,1,1),(1,−1,−1),(−1,1,−1),(−1,−1,1)`，并取`b=−a`。`T_{kij}=−1`恰在三个下标互异时，其余为0。B1的12个`(x,k)`等式用有理数全部回算通过。该例适合作为保留联合三阶结构的最小测试夹具；与X6的连接应明确这是状态观察特征，而非把3个特征升级为完整空间。

#### 10. KL稳定性到谱界：可检查的必要条件

Lemma 2.3，pp.10–11。在有限满支持积概率测度`μX×μY`下，设`κ>0`，实核`A`双中心化，并对所有积概率扰动满足

\[
\mathbb E_{\nu_X\times\nu_Y}A
\le\kappa\,[D_{\rm KL}(\nu_X\|\mu_X)+D_{\rm KL}(\nu_Y\|\mu_Y)],
\]

则`||A||_{op,μ}≤κ`。短证明已核读：取`νX=(1+tf)μX,νY=(1+tg)μY`，中心化消去低阶项；KL二阶展开给`E[fAg]≤κ(||f||²+||g||²)/2`。这可用于检测某个声称“对所有重加权稳定”的观察矩阵是否自洽。它是上述KL条件的推论，单有小谱范数不自动给出完整KL稳定性。

#### 11. 有界噪声多项式的一阶系数界

抽自Lemma 4.1及其证明，pp.17–18。若

\[
P(u)=\sum_{j=0}^Nc_ju^j,\quad |P(u)|\le M\ (0\le u\le1),
\quad\sum_j|c_j|\le L,\quad L\ge M>0,
\]

则

\[
|c_1|\le2(e+1)M\left\lceil\log(eL/M)\right\rceil^2.
\]

已核读短证明：在`[0,e^{-1}]`截断至`K=ceil(log(eL/M))`，尾项≤`M/e`，再用区间端点Markov/Chebyshev导数界。与维数无关，代价由系数总变差控制。原文将其用于Efron–Stein一级耦合项；我们可用于已确证的生成函数或多尺度噪声插值，尤其提醒必须支付`L`而不能只看区间函数值。

### 三、边重构：最适合提取的是平移不变多项式与联合信息证书

源：[Unconditional Edge Reconstruction of Simple Graphs of Linear Density](https://github.com/google-research/google-research/blob/4a7bc8ab0bc770e71a259b7966c500496b99010a/cogentic_research_papers/edge_reconstruction/paper.pdf)。

#### 12. 主定理及与我们对象的距离

Theorem 1.1，p.2：声称每个有限无向简单图，`n≥4,m≥1000n`，由全部无标号删一边卡片的多重集唯一确定至同构。这里的输入是完整edge deck，保留重复度；不是少量局部观察、度数摘要或独立边际。简单图可满足条件的最小顶点数是2001。

本文核心长链涉及跨尺度Kruskal树、组件熵、自动同构群、删边多项式与三类组件的总熵支付；本次未完成该完整长链的逐步核验。下面的独立代数部分已读实质证明。

#### 13. 平移不变齐次多项式＝低阶矩湮灭

Theorem 4.2(1)，pp.24–25。`P(y)=Σ_{|u|=N}c_u y^u`为复系数、`N≥1`次齐次多项式，且

\[
P(y_1+z,\ldots,y_M+z)=P(y_1,\ldots,y_M)\quad(\forall z).
\]

则对任意总次数`<N`的多项式`R`，

\[
\sum_{|u|=N}c_uR(u)=0.
\tag{P1}
\]

已逐步核读：对`|r|<N`，`∂^rP`仍平移不变且有正次数，于是`∂^rP(1)=∂^rP(0)=0`；下降阶乘单项式构成低次多项式空间的基，得P1。

进一步，对目标指数`v=(d_i),Σd_i=N`，任取首一`d_i`次一元多项式`q_i`，

\[
c_v=\sum_uc_u\prod_{d_i>0}\frac{q_i(u_i)}{d_i!}.
\tag{P2}
\]

这是从“低阶观测消不掉的差异”构造显式对偶证书的方法。原证明以`∏ binom(u_i,d_i)=1_{u=v}`和相同最高次项比较，短且可复核。

#### 14. 系数相对总变差的抑制

同一定理4.2(2)，p.24：若`max_i d_i≤t`，原文给

\[
|c_v|\le(t+1)^{-N/(200t)}\,||P||_1,
\qquad ||P||_1=\sum_u|c_u|.
\]

当`t=1`时有更强且证明很短的

\[
|c_v|\le(\sqrt3/2)^N||P||_1.
\]

本次完整核读了`t=1`特例：在P2取`q_i(x)=x−1/2`和公共权`r=√3`，对所有整数`k≥0`，`|k−1/2|(√3)^{1−k}≤√3/2`；利用`Σ_i(u_i−d_i)≤0`完成乘积界。一般`t`的界依赖Lemma4.1的Charlier/Bessel振荡积分估计，尚未独立逐行复核全部常数，宜保留为“原文给出的候选工具”。

#### 15. 同一重数分拆的频段局部化

Lemma 4.3，pp.25–26。若P为非零齐次、共同平移不变多项式，且其全部指数向量具有同一个重数分拆，则按目标`v`及整数阈值`0≤t0<t1`划分低、中、高重数坐标；先按低坐标及统一底量`t0`做归一化偏微分，再提取高坐标的最高次单项式，得到中频段多项式。中频段非空时，该多项式仍齐次、仍共同平移不变、目标系数保持、系数`ℓ1`范数不增。

已核读证明的关键排序步骤：保留项的低坐标被总次数强制等于目标低坐标；高坐标是严格最大的剩余次数，提取其顶次系数会使额外高坐标导数项为零，所以中频平移不变性继承。该命题依赖“同一重数分拆”，一般混合支持多项式不能直接使用。

#### 16. 我们可以直接用的精确联合残差例

从`P=(y1−y2)(y1−y3)(y2−y3)`提取正负项，定义两个均匀分布：

\[
\mu_+=\operatorname{Unif}\{(2,1,0),(1,0,2),(0,2,1)\},
\]
\[
\mu_-=\operatorname{Unif}\{(2,0,1),(1,2,0),(0,1,2)\}.
\]

根据P1，它们对全部总次数≤2的多项式观察完全一致：每坐标均值1、平方均值5/3、异坐标乘积均值2/3。可是三次观察

\[
\Omega(u)=(u_1-u_2)(u_1-u_3)(u_2-u_3)
\]

在两组上分别恒等于2和−2。该例已精确穷举10个低次单项式，并回算三次差异。

这是我们自行整理的可复算桥接例，不声称新颖性。可在心跳世界原生坐标中显式嵌入为`(u1,u2,u3,0,0,0)`，把研究对象清楚限定为X6内所选有限状态族。若目前观察语言只含二阶矩，两组可观察等价；允许三次观察或能生成三次观察的后续操作后，等价被打破。它清楚说明“现时低阶矩相同”与“对未来操作充分”的区别，为残差保真、联合状态和压缩门槛提供直接证据。

### 建议采用的实际层次

1. **直接整理为外部工具卡**：Moore判据；剪切生成；复合模数Bézout消元；任意分布的基增广满秩；平移不变多项式低次矩湮灭/对偶；squarefree衰减；布尔三阶张量闭包；有界噪声多项式一阶系数界。
2. **作为明确前提下的候选工具**：稀疏铅笔满仿射群判据（本次已读完整短证明，但尚无项目独立审核）；一般重数Charlier衰减；椭圆曲线分裂概率。
3. **保留为论文级主张供后续审核**：DLP亚拟多项式复杂度、logrank指数改进、线性密度边重构。它们的出处和关键假设已定位；本次提取不等同项目正式接纳。

计算证据：`algebra_checks.py`与`algebra_checks.json`，完全使用整数/有理数，覆盖二阶矩一致/三阶分离、布尔立方恒等式12项、模6消元、一个任意分布满秩概率实例。所用PDF正文不存在已读取的可运行源程序；本地短脚本为本次对选定小例的复算。




---

## 附录 C：学习、博弈与离散工具

固定输入：`google-research/google-research@4a7bc8ab0bc7/cogentic_research_papers`。2026-11-25 提取。五篇 PDF 均通过 GitHub connector 以 base64 取回，已保存原 PDF 与 `pdftotext -layout` 文本；关键易错公式另看原页图像。本文是外部文献吸收笔记，主定理保持为原文结论；下面单独标明实际完成的局部重算，不将目录中的声明当作已取得的 Lean 检查结果。

### 结论与阅读优先级

| 优先 | 论文 | 最适合吸收的内容 | 接口与实际条件 |
|---|---|---|---|
| 高 | Fictitious Play | 下降二项式基、整数求和、无除法矩阵预像、稀疏余核残差 | 整数多项式演化、有限步更新证书；可直接做小模块 |
| 高 | VC Sample Compression | 按观测分区、熵增下界、最大彩票的对偶分离、MWU 重构 | 有限候选类/有界 VC 类的实验与证据选择；完整未来语义仍需独立定义 |
| 高 | Bimatrix Nash | 几何尺度指数滤波与耗散支付；kite 区域的精确混合修复 | 多尺度误差核、残差能量；全算法的显式常数非常大 |
| 中 | Subadditive Prophet | 非均匀边际约束下的指数平方、代价仅加常数 | 需要次可加性、独立抽样及对所有边际向量成立的归纳命题 |
| 中 | Convex CE | 条件期望伴随算子、两步残差、后序树分区恒等式 | 联合关系保存、分层状态摘要；查询下界仅限明确黑箱模型 |

所有外部对象以“算法/证明工具”接入，若应用于心跳世界的 X6 状态，需声明状态到外部对象的编码、允许观测和更新，不自动改变本原定义。

### 1. Fictitious Play：值得直接搬入工具箱的整数代数

源：<https://github.com/google-research/google-research/blob/4a7bc8ab0bc770e71a259b7966c500496b99010a/cogentic_research_papers/fictitious_play_convergence/Fictitious_Play_Convergence.pdf>。32 页。

#### 1.1 原文主结论及其准确作用域

Theorem 1，p3：对每个整数 \(d\ge1\)，构造显式有理反对称矩阵 \(A_d\in[-1,1]^{n_d\times n_d}\)，其中

\[
n_d=2d^2+7d-5,\qquad N_d=2n_d=4d^2+14d-10.
\]

从零累计计数出发、固定字典序打破并列的“同时更新 fictitious play”，第 2 步以后最佳响应唯一，且存在显式 \(\kappa_d>0,T_0(d)\)，使每个 \(T\ge T_0(d)\) 满足

\[
\operatorname{Gap}_{A_d}(\bar x_T,\bar y_T)\ge\kappa_d T^{-1/(d+1)}.
\]

这是同时更新 fictitious play 在一族显式输入上的慢收敛下界；量词是“每个 \(d\) 存在一个输入族”，而非所有输入都以此速度收敛。\(\kappa_d\) 和 \(T_0(d)\) 依赖 \(d\)，用于有限步数的实际性能比较时需与指数一起保留。文中技术是单份内层游戏加 \(4\ell+5\) 个辅助策略完成运行后复位，避免每层复制三份。它可用于研究迭代停滞的压力样例。全递归构造的所有相位不等式本次没有做完整独立复证；可直接抽取下面已核对的代数模块。

#### 1.2 反对称迭代的单轨道化与精确间隙

Definitions 1–2，Lemmas 1–2，p4–5。若 \(M^T=-M\)，两玩家同时更新、同样打破并列且从零计数出发，则 \(X_t=Y_t\)。置 \(U_t=MX_t\)，有

\[
i_{t+1}\in\arg\max_i(U_t)_i,\qquad U_{t+1}=U_t+Me_{i_{t+1}},\qquad
\operatorname{Gap}_M(\bar x_T,\bar y_T)=\frac{2}{T}\max_i(U_T)_i.
\]

因 \(M_{ii}=0\)，当前获选坐标在更新中保持原值，故 \(\max_i(U_t)_i\) 单调不减。证明只需代入反对称性，已手工核对。可用来把双边迭代化为一个保留整数累计量的状态机；其中“累计量单调”与“归一化间隙下降”是不同量。

#### 1.3 下降二项式基：移位与求和全用整数矩阵

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

#### 1.4 无除法预像与稀疏余核

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

### 2. VC 压缩：把观测点选成可重构的证据集

源：<https://github.com/google-research/google-research/blob/4a7bc8ab0bc770e71a259b7966c500496b99010a/cogentic_research_papers/vc_sample_compression/Near_Quadratic_Sample_Compression.pdf>。30 页。

#### 2.1 原文主定理及复杂度含义

Theorem 1.1，p3–4：任意二值概念类 \(\mathcal C\subseteq\{0,1\}^X\)，VC 维数为 \(d\ge1\)，存在有标签样本压缩方案，保存

\[
k=O(d^2\log^2 d)\text{ 个样本},\qquad b=O(d\log^2d)\text{ 个附加比特}.
\]

实际上只有 \(O(d\log d)\) 个需要标签，其余可作无标签观测点。重构是有限代表概念的加权多数票。**定理界定的是表示大小，不保证找出压缩集或执行重构具有多项式时间。** 保证对象是被压缩的可实现样本全部标签；若要用于全体未来行为等价，必须把那个未来语言纳入概念类并证明要求。

#### 2.2 按观测集分区及点态低误差重构

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

#### 2.3 分区熵增由“被新观测区分的同胞对”下界

Lemma 4.4，p17–18，是最短、迁移最直接的小引理。旧分区各单元质量 \(w_\tau\)，条件分布 \(\nu_\tau\)，加入新观测得到细分 \(W'\)。则

\[
H_{W'}(\nu)-H_W(\nu)\ge
\sum_\tau w_\tau\Pr_{c_1,c_2\sim\nu_\tau}\bigl[c_1|_{W'}\ne c_2|_{W'}\bigr].
\]

重算理由：若一个旧单元分为条件质量 \(q_j\)，熵增为 \(w_\tau\sum_jq_j\log_2(1/q_j)\)，而 \(\log_2(1/q)\ge1-q\)，故至少为 \(w_\tau(1-\sum_jq_j^2)\)，右侧正是两次独立抽样落在不同新单元的概率。

可用于选择下一条最有区分力的观察/测试：最大化加权同胞对分离概率，给“这次实验到底增加了多少信息”一个有数学含义的目标。该式只测所选分布和候选集合的信息增量，不把无质量候选自动删去。

#### 2.4 最大彩票与小分离集

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

#### 2.5 必须保存的反例

Appendix B，p29–30：\(\mathcal C=\{0,\mathbf1_{x_1},\ldots,\mathbf1_{x_m}\}\)，VC 维数仅 1，目标为全零，均匀分布在 \(m\) 个单点指标上，每点误差 \(1/m\)。任何 \(k<m\) 个观测点满足

\[
\mu(\operatorname{Pool}(W))\le\frac{k+1}{m},\qquad
H_W(\mu)\le\frac{k(\log_2m+2)}m.
\]

所以固定大小的观测集可以同时几乎拿不到代表质量、也几乎没有熵增。此例已按分区直接核对。对证据压缩很有用：低点误差、低 VC 维数和“分布很分散”本身不足以推出任意贪心选择都有常数进展。

### 3. Bimatrix Nash：耗散支付与小型精确修复

源：<https://github.com/google-research/google-research/blob/4a7bc8ab0bc770e71a259b7966c500496b99010a/cogentic_research_papers/bimatrix_nash_equilibrium/paper.pdf>。41 页。此子目录 README 标明 CC-BY-4.0；本笔记仅提取和重述数学结果。

#### 3.1 原文主结论与实际尺度

Theorem 1.1，p2–3：对有理 \([0,1]\) 双矩阵博弈，给出确定性 \(\operatorname{poly}(L)\) 时间的有理 \(1/5\)-近似纳什均衡算法，其中 \(L\) 是输入位长。这里“exact”指误差阈值恰为 \(1/5\)，不是输出零误差纳什均衡。

Remark 1.3 的显式参数（已看 PDF 原页确认）：

\[
K=3\cdot2^{56},\qquad T=40\cdot2^{54}\cdot64^{K-1}+1.
\]

故本轮更适合提取局部核与证书，不把整套算法列为可立即替代现有求解器的工程实现。README 称 Lean 形式化将另行发布；固定目录只有 PDF/README，没有本轮可运行的 Lean 项目。全局 Volterra 到三变量不等式归约以及附录有理证书表，本次未做全链独立复证。

#### 3.2 Kite 区域的零 LP 修复

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

#### 3.3 几何多尺度指数核与耗散

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

### 4. Subadditive Prophet：让指数平方而代价只增加常数

源：<https://github.com/google-research/google-research/blob/4a7bc8ab0bc770e71a259b7966c500496b99010a/cogentic_research_papers/subadditive_prophet_inequalities/Subadditive_Prophet_Inequalities.pdf>。36 页。

#### 4.1 主结论与最有迁移价值的部分

Theorems 1.2–1.3，p3–4：买家估值按有限支撑的乘积分布独立抽取，每个估值规范化、单调、次可加。在任意给定的固定到达顺序和打破并列规则下，存在静态匿名逐项价格取得 \(O(\log\log\log m)\) 的期望福利近似比。同时，在足够大 \(m\) 上构造两买家实例，使静态匿名价格的近似比至少为 \(\Omega(\log^{(3)}m/\log^{(4)}m)\)；该下界即使允许有利的并列选择、以及独立于实际估值抽取的随机价格仍成立。这里约束的是这类静态逐项价格机制；对我们最有用的是上界证明里完整、短小的非均匀边际归纳引理。

#### 4.2 精确的指数平方引理

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

### 5. Convex CE：联合关系、两步残差和紧凑树摘要

源：<https://github.com/google-research/google-research/blob/4a7bc8ab0bc770e71a259b7966c500496b99010a/cogentic_research_papers/ce_convex_games/CE_in_Convex_Games.pdf>。17 页。

#### 5.1 原文下界的作用域

Theorem 2，p15–16：对每个足够大的总维数 \(d=d_1+d_2\)，在标准一阶黑箱 oracle 模型中构造一族两玩家游戏：策略集是欧氏单位球，成本值在 \([0,1]\)，成本关于各自策略 \(1/2\) 强凸，Lipschitz 常数 \(L<\sqrt d\)。任何在每个该族输入上以至少 \(2/3\) 概率输出 \(\epsilon=1/d\) 的全 normal-form correlated equilibrium 的随机算法，需要 \(\exp(\Omega(d^{1/16}))\) 次 oracle 查询；原文的下界允许任意内部计算时间和任意有限输出支撑大小。这里的均衡条件允许全策略修改映射，和 coarse CE、固定低维偏移类不同。成本对各玩家自身变量是二次，第二玩家目标含非线性 \(f_V(x)\)，不应误读成任意两方联合变量的一个固定全局二次式。

本次没有把此下界视为我们自有结构算法的限制；它可提供“黑箱暴露了什么信息、允许何种偏移”这个比较标准。更实用的是以下独立可核对模块。

#### 5.2 条件期望伴随与两步残差

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

#### 5.3 后序树的点态正部恒等式

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

### 本次材料与验证清单

- 原始 PDF/文本：`cogentic_review/sources/` 的五个对应名称。
- 图像核对：Nash p3、p15 与 FP p21 已在图像中核对；其他选择页已渲染于 `sources/rendered/`。
- 复算脚本：`cogentic_review/agents/check_learning_kernels.py`。
- 真实输出：`cogentic_review/agents/check_learning_kernels.json`，PASS，精确整数/有理数矩阵检验。
- 独立手算核对：FP 反对称单轨道与 binomial 移位/求和；VC 熵增和 LP 乘子界及 MWU 误差；Nash kite 修复与符号方差恒等式；subadditive 指数平方三步的条件边际/独立性；CE 条件均值平方误差和树标量望远镜式。
- 本次没有运行原文所声称的 Lean 项目，也没有给五篇完整主定理作正式项目审查/晋升。目录中的主定理与上述已核对的小工具分开保存。

建议根报告优先呈现“无除法余核残差、观测分区熵增、耗散支付”三组，可把指数平方和条件期望两步残差作为相邻工具；这样既覆盖五篇，又把阅读价值落在可立即复用的数学对象上。
