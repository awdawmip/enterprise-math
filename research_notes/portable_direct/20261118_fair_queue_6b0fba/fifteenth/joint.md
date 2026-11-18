# 同一 Eisenstein 行、高度与标记素数的联合矩

令 $\mathcal O=\mathbb Z[\omega]$，$q_A=N A$，$p$ 表示避开固定集合 $\mathcal S\supseteq\{p:p\mid6\}$ 的素理想。采用锁定稿的六次符号，$\chi_A(u)=\prod_{p^a\parallel A}\chi_p(u)^a$，对非单位始终取零，包括指数为六的倍数时。每个非零**元素**行 $u$ 使用一份表示 $\psi_u(A)=\nu(A)\chi_A(u)^\sigma$，$\sigma=\pm1$，$\nu$ 的全部定义模零点保留。下文的额外共同掩码只依赖列，在一个行和中固定，并进系数。$D,N$ 是两个范数尺度。把共同高度写为 $t$，用 $q_A^{-it}$ 代替 $(q_A/D)^{-it}$ 等只改变整因子的单位标量。基本因子为

$$
 M_u(t)=D^{-1/2}\sum_a \mu(a)\psi_u(a)W_M(q_a/D)q_a^{-it},
 \qquad
 S_u(t)=N^{-1/2}\sum_b\psi_u(b)W_S(q_b/N)q_b^{-it}.
$$

在共同的固定参数箱内，两个函数的行、表示、掩码和高度相同。外稿给出的见证高度为 $\gamma-\xi$，可随行变化；物理素数槽的另一高度可独立固定。将素数槽写成 $Q_{i,u}=P_i^{-1/2}\sum_{p\in\mathcal P_i}b_i(p)\psi_u(p)$，其中 $q_p\asymp P_i$，各 $\mathcal P_i$ 在施加掩码前两两不交，$b_i$ 含其有界权及固定高度相位。以下显式公式也对固定正整数 $a,b$ 的 $B_u=M_u^aS_u^b$ 成立，基本例取 $a=b=1$。每个表达式内保留 Möbius 的符号。[任务书](https://github.com/awdawmip/enterprise-math/blob/564949b13c4e7c07c21c075a517e8f3b1bee98c3/research_tasks/RS-OAI7-003-C-20261007-6F2A81.md) · [锁定稿的定义](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex#L700-L729) · [同高见证](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex#L4500-L4543)

## 定理一　两边同槽的精确贡献

两侧展开联合能量 $|B_u\prod_i Q_{i,u}|^2$。以 $J\subseteq I$ 指定两侧恰好在哪些槽选了同一个素理想。令
$$
 D_i(u)=P_i^{-1}\sum_{p\in\mathcal P_i}|b_i(p)|^2|\nu(p)|^2 1_{p\nmid u}
$$
（额外的固定零掩码并入 $b_i$）。则该块逐行精确等于
$$
 \mathcal C_J(u)=|B_u|^2\prod_{i\in J}D_i(u)
                    \prod_{i\notin J}(|Q_{i,u}|^2-D_i(u)). \tag{1}
$$
因为每个槽的同素数项是 $D_i(u)$，异素数项是其余双和，各槽独立展开即可。这里的“独立”只指有限乘法的指标可分；各因子仍共用同一行。逆因子的平方自由列可以含任意已选素数，普通列可含其任意幂，式 (1) 对这两种交叠都成立。$J=I$ 给出非负的全重合贡献，其他块可为负。

还有逐行误差估计。把 $D_i(u)$ 去掉 $1_{p\nmid u}$ 所得常数记为 $d_i$，则 $0\le D_i(u)\le d_i\ll1$。当 $P_i$ 充分大、$0<q_u\ll U$ 时，
$$
 0\le d_i-D_i(u)\ll\frac{\log(2U)}{P_i\log P_i}.
$$
这是因为范数 $\asymp P_i$ 且整除 $(u)$ 的不同素理想个数至多为 $\log q_u/\log(cP_i)$。故全重合块可写为 $|B_u|^2(\prod_i d_i+O(\log(2U)\sum_i(P_i\log P_i)^{-1}))$，有界槽可直接保留准确 $D_i(u)$。此式在根据原稿筛选过的非零行及行依赖见证高度上也逐点成立。

## 定理二　真实导子、重复零点与平滑行能量

固定一份行无关的有限合并列系数 $c_A$，即在原乘积里按理想乘积 $A$ 合并全部分解，包含平滑权、共同高度与固定射线特征。在某素理想比较两列 $A,B$，设
$$
 \mathfrak f=\prod_{v_p(A)-v_p(B)\not\equiv0\ (6)}p,\qquad
 C=\prod_{\substack{p\mid AB\\v_p(A)-v_p(B)\equiv0\ (6)}}p .
$$
二者互素。$\chi_A(u)^\sigma\overline{\chi_B(u)^\sigma}$ 等于模 $\mathfrak f$ 的原始特征乘 $1_{(u,C)=1}$，$\mathfrak f=1$ 时原始部分为 1。在每个出现的好素理想，六次特征的阶恰为 6。因此在模 $\operatorname{rad}(AB)$ 的完整剩余类上，准确平均为
$$
 K(A,B)=1_{\mathfrak f=1}\prod_{p\mid C}(1-q_p^{-1}). \tag{2}
$$
同素数标记在两列增加相同指数，消去自身的相位。残余列若仍有指数差，例如 $A=p^2,B=p$，其导子仍含 $p$。当两列指数差为 6 的倍数，出现过的 $p$ 则留下零掩码。不同理想也可以全高度共振。例如 $7=\pi\bar\pi$ 分裂，$A=\pi^6,B=\bar\pi^6$ 等范数且 $K(A,B)=36/49$。

取非负径向 $\Phi\in C_c^\infty(\mathbb C)$ 支持在固定环带，$c_\Phi=(2/\sqrt3)\int_{\mathbb C}\Phi\,dx\,dy$。任意 $J_0>0$ 和 $U\ge1$ 均有无条件公式
$$
 \sum_{u\in\mathcal O\setminus\{0\}}\Phi(u/\sqrt U)
 \chi_A(u)^\sigma\overline{\chi_B(u)^\sigma}
 =c_\Phi U K(A,B)
 +O_{\Phi,J_0}\!\left(\tau(C)\sqrt{q_{\mathfrak f}}
       (1+U/q_{\mathfrak f C})^{-J_0}\right). \tag{3}
$$

把零掩码展开为 $\sum_{d\mid C}\mu(d)1_{d\mid u}$，置 $u=dv$，尺度变成 $Y=U/q_d$。对模 $\mathfrak f$ 的每个剩余类作二维格 Poisson。$\mathcal O$ 余体积为 $\sqrt3/2$。原始非主局部特征的非零频 Gauss 和模长至多 $\sqrt {q_p}$，零频为零；中国剩余定理给出合计上界 $\sqrt {q_{\mathfrak f}}$。当 $Y\le q_{\mathfrak f}$，快速衰减的非零频格和为 $O(q_{\mathfrak f}/Y)$，与前因子 $Y/\sqrt{q_{\mathfrak f}}$ 相乘即得误差。$Y>q_{\mathfrak f}$ 时，除零以外的最短频率有固定下界，在同一归一化格上以足够多阶衰减得任意次幂节省。$\mathfrak f=1$ 时零频给 $c_\Phi Y$，其余项同理。对 $d\mid C$ 求和即得 (3)。用几何级数或有限 Poisson 独立推 (2) 仅需特征正交。[有限域 Gauss 和定理 2.2](https://kconrad.math.uconn.edu/blurbs/gradnumthy/Gauss-Jacobi-sums.pdf) · [锁定稿的格与零延拓约定](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex#L566-L644)

将式 (3) 逐项乘 $c_A\overline{c_B}$ 并对 $A,B$ 求和，左侧恰为 $\sum_u\Phi(u/\sqrt U)|\sum_A c_A\chi_A(u)^\sigma|^2$，因此主项仍保留不同理想间的共同相位。

**混合上界。** 设 $Y=D^aN^b$，$X=Y\prod_iP_i$，各尺度至少为 1，因子数和环带固定，则
$$
 \left|\sum_{u\ne0}\Phi(u/\sqrt U)\mathcal C_J(u)\right|
 \ll_{\epsilon,\Phi} X^\epsilon
 \left[U+\left(Y\prod_{i\notin J}P_i\right)^2\right]. \tag{4}
$$
其全能量版本为 $\sum_u\Phi|B_u\prod_i Q_{i,u}|^2\ll (U+X^2)X^\epsilon$。证明先合并列，$q_A\asymp X$，$|c_A|\ll_\epsilon X^{-1/2+\epsilon}$（固定长度的有序理想因子分解给出除数界）。对 (3) 的共振主项写 $A=h d^6,B=h e^6$，$h$ 唯一且各素数指数小于 6。范数不超过 $x$ 的理想数 $O(x)$ 由 Eisenstein 格计数给出。由于 $\sum_{q_h\ll X}(X/q_h)^{1/3}\ll X$，共振对至多 $O(X)$，主项绝对贡献 $\ll U X^\epsilon$。误差里 $q_\mathfrak f\ll X^2$、$\tau(C)\ll X^\epsilon$，乘上 $\left(\sum_A|c_A|\right)^2\ll X^{1+\epsilon}$ 即得全能量界，重选 $\epsilon$ 吸收所有除数损失。在 (1) 展开异素数因子后，每项为若干 $D_i(u)$ 乘非负的剩余能量。用 $D_i(u)\ll1$ 与相应较短乘积的界，得到 (4)。若只对固定子集的非零行求和，正能量各项仍由同一全行和控制。式 (3) 的主项则针对全平滑行集。

高度可逐行选择。将探测高度写在 $q_a/D,q_b/N$ 的对数坐标上，每个 $t$ 导数只插入有界的对数因子，尺度相位整体在模长内消去。在每个单位高度区间对原乘积用一维 Sobolev 不等式，再求和，给 $|t_u|\le T$ 的全能量界及 (4) 至多额外 $O(1+T)$ 的代价。这个论证允许已固定的物理槽高度与探测高度不同。二次长度代价中，全重合块的所有标记尺度均已消去。在 $X^2\le U$ 的短列范围，完整联合能量也得到 $U X^\epsilon$。外稿长见证的 $DN\gtrsim U$，单凭 (3)–(4) 仍缺少对大量非共振列的进一步抵消。

## 原稿的边际条件和例外行

原稿的标记逆矩对 $0<q_u\ll Z^m$ 声称 $\sum|M Q|^2\ll Z^{m+\epsilon}$，条件为 $r+2z\le m-c_1,\ 2r+8z\le3m-c_2$，两个余量均固定为正。普通矩是 $\sum|S_1S_2 Q|^2$，$z>0$ 要求各槽小于指定网格、$n_1+n_2+6\kappa z\le m+q$，其中 $q$ 支付显示的移动支撑。$\kappa<1$ 尚有 $\beta_*\le(1+\kappa)/2$ 这一假设。此时须剔除原始诱导特征属于固定有限群 $\Theta$ 的行，$z=0$ 时剔除主诱导特征。非零元素 $u=1$、平凡固定扭曲即显示非零行也能例外。原稿在应用时共轭整个普通乘积，所有槽和测试一并共轭，保留零点。本文的 (1)–(4) 使用有限特征正交与格计数，无需上述待审解析引理。[标记逆矩](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex#L9218-L9276) · [普通四次矩](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex#L12496-L12594)

外稿物理行是六次幂自由的。把固定集合内部分及单位分离后，$(u)_{\rm good}=\mathfrak w\mathfrak k$，其中 $\mathfrak k$ 平方自由，与平方满的 $\mathfrak w$ 互素。每个平方满理想唯一写为 $\mathfrak a^2\mathfrak b^3$，$\mathfrak b$ 平方自由，允许 $\mathfrak a,\mathfrak b$ 相交。范数 $V$ 的平方满段有 $O(V^{1/2})$ 个理想，因 $\sum_{\mathfrak b}q_{\mathfrak b}^{-3/2}<\infty$。每次应用平方自由行筛前须固定 $\mathfrak w$，保留 $\chi_A(\mathfrak w)$ 的相位及零点。式 (3) 的 $\mathfrak f$ 是列对在**行变量**上的好素数导子；外稿所固定的射线数据、移动显示支撑和原始 Hecke 导子的分析依赖仍各归其位。[原稿的平方满行分层](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex#L5241-L5290) · [原稿内逆列与槽的平方重合](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex#L11605-L11673)

对同一行、高度与非负测度，若 $A_1=|M Q_1|^2$、$A_2=|S^2Q_2|^2$，Hölder 给 $\int A_1^\theta A_2^{1-\theta}\le(\int A_1)^\theta(\int A_2)^{1-\theta}$，$0<\theta<1$。在两个门槛均达到的行上，可以分别用各自矩作 Markov，再取两个计数上界的较小者。锁定稿在此处使用的是这种分别计数。若要直接界 $\int A_1A_2$，需互为共轭指数的更高边际矩，或掌握相关项、点态界之一。固定零支撑、有限射线扭曲及所取 $\Theta$ 不能在比较中无代价改变。[原稿的高度与门槛计数](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex#L15135-L15247)

## 可逐项检查的真实特征例子

取惰性素理想 $p=(5)$，$q_p=25$，$\mathcal S$ 仅取 6 上素理想，平凡固定扭曲。$\mathbb F_{25}^\times$ 上六次符号为 $u\mapsto u^4$，每个六次单位根恰有四个原像。记 $x=\chi_p(u)25^{-it}$。逆列取 $1,p$，普通列取 $1,p,\ldots,p^5$，再取单素数槽 $p$。省去固定整体尺度后，三个因子是 $1-x,\ 1+x+\cdots+x^5,\ x$。这些幂是其各自范数上唯一的理想，单次有限算例可用光滑范数测试选出。此处测试的宽度固定在该算例，不提供渐近短二倍区间的下界。

在单位行，联合模方是 $|1-25^{-6it}|^2$。取 $t=0$ 和 $t=\pi/(6\log25)$，两个边际模方平均始终分别为 2 和 6，联合平均却分别为 0 和 4。包括非单位类后，标记在该类为零，联合平均分别为 0 和 $96/25$。

用 $\mathbb Z[\zeta_{12}]$ 验算上述高度，并在两个范数 7 及一个范数 25 的好素理想上遍历全部 1,225 个剩余类。24 列构成的 576 项 Gram 表有 50 项共振，全部与 (2) 一致。另取范数 $7,7,25,13$ 的四个素理想组成两个互斥槽，含平方满和六次幂普通列；在全部 $0<q_u\le81$ 的 300 个元素行上，160 条未合并分解得到 108 个理想列，符号抵消后余 80 个。按无槽同素数、仅第一槽、仅第二槽、两槽均同素数四种情况累计，(1) 的准确贡献为 $2370,636,-8232,28248$，其和 $23022$ 等于完整乘积的模方总和。以 Python 3 运行 joint_check.py 即可重建 JSON，程序只用标准库。数值核对只涉及有限恒等式。长列、行依赖高度与非例外限制共同作用下的统一幂次节省仍待独立证明，$\Re s>7/8$ 的零点陈述仍是所引预印本的待审结论。[复算程序](joint_check.py) · [精确输出](joint_checked.json)
