# 剩余度三的首层种子：坏率的两项精确极限与第三矩分界

令 $K=\mathbf Q(\zeta_7)$，$p\equiv2,4\pmod 7$ 为素数，$P\mid p$，$r\ge0$。保持原六个幂基的系数平方和 $Q$。在 $P^r/P^{r+1}$ 中等权抽一个非零对偶射影种子，其首层核是 $\mathbf F_p^3$ 的二维平面。若有 $0\ne x\in P^r$ 的类落在核内，且 $Q(x)<\kappa^2p^{r+1/3}$，称该层失守，概率记 $d_{p,r,1}$。分母始终是筛前的 $p^2+p+1$ 个种子。

**定理。** 对每个固定 $0<\kappa^6\le8/49$，当 $p\to\infty$ 时，对 $P$ 和 $r$ 一致有
$$
d_{p,r,1}=C_1\kappa^6-C_2\kappa^{12}+o_\kappa(1).
\tag{1}
$$
两个系数均与门槛无关。第一系数是一个一维积分；第二系数由带明确截尾界的正项级数给出。原门槛 $\kappa=1/\sqrt{42}$ 下，极限位于 **$[0.00002705977252,0.00002706007552]$**。按虚二次子域归并短方向后，单个种子的方向数有整个离散极限律。其均值与方差同趋 $C_1\kappa^6$，极限尾概率正比于 $t^{-3}$，第三矩趋于无穷。

第 17 轮对这一剩余类给出了见证并集上界。第 86、119 轮处理 $p\equiv-1\pmod7$ 的实三次子域与剩余度二。这里利用另一个子域重建实际第一层的点和线，给出同一固定正门槛下两个新素数类的条件化代价。第二层 $j=2$ 与首层共用种子，联合概率另行处理。四个冻结种子沿用原记录。[登记题书与停止条款](https://github.com/awdawmip/enterprise-math/blob/7b32ae2ad9d1c13a13ff4668d1d218adda99390d/research_tasks/X6CM_LOCAL_BAD_SEED_DECAY_GEN2_20260917.md) · [原 T4 的种子与 Krylov 约束](https://github.com/awdawmip/enterprise-math/blob/7abd6f9523e1f6edc4c714b93c9e81dde588633e/research_notes/x6_tunable_geometry_and_second_moment_barrier_20260911.md) · [后继二阶问题](https://github.com/awdawmip/enterprise-math/blob/bd8eed4e44c89aa11286d92e1d38445714b9a994/research_artifacts/mcp/X6CM-LOCAL-BAD-SEED-DECAY-20260917/MCP-456b8f22a648400585024ffbcc1c2c94/ef8f24c2ea7a3d805af4/_checkpoint.json) · [前期碰撞结果](../hundrednineteenth/collision.md)

## 1. 哪些见证落在同一个种子里

取 $D=\mathbf Q(\sqrt{-7})$，$\omega=\zeta+\zeta^2+\zeta^4=(-1+i\sqrt7)/2$，$\mathcal O_D=\mathbf Z[\omega]$。Minkowski 界 $2\sqrt7/\pi<2$ 给类数一，单位只有 $\pm1$。$\mathcal O_K=\mathcal O_D[\zeta]$ 在 $D$ 上有整基 $1,\zeta,\zeta^2$。$p$ 在 $D$ 分裂，每处在 $K/D$ 三次惰性，故 $P=g\mathcal O_K$，$|g|^2=p$。取复嵌入指数 $1,2,4$，三处对 $D$ 的限制相同。写 $x=g^rz$，$c=(g/\sqrt p)^r$，原窗口还原为 $Q(cz)<R^2$，$R=\kappa p^{1/6}$。以下体积一律用原六系数格的余体积一作归一。$c$ 是同一个复相位，实雅可比为一。

令 $z_j$ 是 $z$ 的三个复坐标。原幂基的七点 Parseval 公式在实延拓中给出
$$
Q(z)=\frac27\left(\sum_j|z_j|^2+2\left[\sum_j\Re(\zeta^jz_j)\right]^2\right).
\tag{2}
$$
短点不可能被 $p$ 上任何度三素理想整除，因为 $|N_K z|\le(7/6)^3 Q(cz)^3\ll_\kappa p<p^3$ 对充分大 $p$ 成立。若需真实六坐标整数本原，可以除去有理整数公因子：素数 $p$ 不会整除 $x$ 的全部坐标，因为 $z$ 在 $p$ 上两处均非零、$g$ 仅占其中一处；其他素数可在保持 $P^r$ 及核线的条件下除去。因此命中事件保持不变。下文用 $Z$ 计命中的不同 $D$-方向，逐个原整数见证的重数是另一种统计。

选各条短方向上的一个短整点。两点若约化成同一射影点，各 $2\times2$ 子式被 $(g)$ 整除；用 $D$ 三基写列，子式绝对域范数为 $O(R^4)<p$，故全零，两者本就在同一条 $D$-线上。三点若约化共面，其 $D$-行列式也被 $(g)$ 整除。三次幂基嵌入矩阵的 Vandermonde 绝对值为 $\sqrt7$（三单位根的两两距离是 $2\sin(j\pi/7),j=1,2,3$）。由 Hadamard 及 (2)，
$$|N_D(\det[z_1,z_2,z_3])|\le(49/8)\prod_{i=1}^3 Q(cz_i)<p.$$
因此三点必已在 $D$ 上共面。反向蕴含由原整子式直接约化得到。开球使 $\kappa^6=8/49$ 亦有严格不等式。

记 $L$ 为全部不同短 $D$-方向数，$n_{xy}$ 为一对不同方向 $x,y$ 张成的 $D$-平面中的短方向总数。每个射影点属于 $p+1$ 条有限射影线，每对不同点恰定一条线。模共面与 $D$ 共面既已等价，便有三个**有限**恒等式
$$
 EZ=\frac{(p+1)L}{p^2+p+1},\quad E[Z(Z-1)]=\frac{L(L-1)}{p^2+p+1},\quad
 (p^2+p+1)d_{p,r,1}=(p+1)L-\sum_{x\ne y}\frac1{n_{xy}}.                 \tag{3}
$$
末式按有序方向对计，一条含 $n\ge2$ 点的线恰扣去 $n(n-1)/n=n-1$ 次。

## 2. 第一系数只需三个乘子

每个 $D$-方向有两个 $\mathcal O_D$-本原代表，线上整点是其所有整环倍数。设
$$\Omega=\{z:\min_{0\ne u\in\mathcal O_D}Q(uz)<1\},\qquad
C_1=\frac{\operatorname{vol}(\Omega)}{2\zeta_D(3)}.$$
$\Omega$ 是有限个椭球的并。理想 Möbius 反演给 $L=C_1 R^6+O(R^5+1)$：一个范数 $B$ 的理想按复标量把 $\mathcal O_D^3$ 缩放 $\sqrt B$ 及旋转，格点边界误差 $O(1+R^5/B^{5/2})$；有非零点须 $B\ll R^2$。平面格计数给 $\#\{I:NI\le t\}=O(t)$，误差可和，且相位在紧集中，常数一致。

为计算 $\Omega$，写 $w=\sum_{j=1,2,4}\zeta^jz_j/\sqrt3$。在标准复球面 $S^5$，$x=|w|^2/\|z\|^2$ 的密度是 $2(1-x)$，$\theta=\arg w$ 均匀独立。比较 $Q(uz)$ 归结为最小化 $N(u)+6x\Re(ue^{i\theta})^2$。范数至少 7 的整元不能胜过 1。枚举 $N(a+b\omega)=a^2-ab+2b^2<7$，除 $1,\eta,\bar\eta$（$\eta=(1+i\sqrt7)/2$）外只有其符号、整数 $2$ 和范数四的 $(-3\pm i\sqrt7)/2$ 至符号。整数 2 可删。对后两者，投影平方差的最大特征值为 $(-3+\sqrt{9+7})/2=1/2$，乘 $6x$ 后不能超过范数差 3。

令 $u_0=(3\sqrt7+\sqrt{178})/23$。用第一象限的 $C=\cos^2\theta$、$B=(\cos\theta-\sqrt7\sin\theta)^2/4$ 比较 $1+6Cx$ 和 $2+6Bx$，后者只在 $x>1/[6(C-B)]$ 时较小。径向体积按最小值的负三次幂取平均。利用
$$\int_{x_0}^1\frac{2(1-x)}{(A+Ex)^3}\,dx=\frac{(1-x_0)^2}{(A+Ex_0)^2(A+E)},$$
再令 $t=\tan\theta$，得到
$$
 C_1=\frac{\pi^3}{12\zeta_D(3)}
 \left[1+\frac{2\sqrt7}{\pi}\int_0^{u_0}
 \frac{(5+6\sqrt7t-23t^2)^3\,dt}
 {9(7+2\sqrt7t-7t^2)^2(7-6\sqrt7t+25t^2)(7+t^2)}\right].          \tag{4}
$$
基准球原六维体积 $V=\pi^3/6$，只取乘子 1 的角平均为 $1/\sqrt7$。$\zeta_D(3)=\zeta(3)32\pi^3/(343\sqrt7)$，可用三次 Bernoulli 多项式傅里叶展开及 $\sum_{a=1}^6\chi_{-7}(a)B_3(a/7)=48/343$ 得出。

## 3. 第二系数的正项级数

固定每个非零理想 $\mathfrak b=(\beta)$ 的生成元及其模剩余代表。设 $X,Y\in\mathcal O_D^3$ 是各自本原、相互独立的列。在 $D$-平面与 $\mathcal O_D^3$ 的交格中，$X$ 可扩成基向量；商出 $X$ 后的自由秩一模中，$Y$ 决定指数理想 $\mathfrak b$。因此唯一存在 $a\bmod\mathfrak b$，令 $W=(Y-aX)/\beta$ 且 $(X,W)$ 是交格的基。$Y$ 本原当且仅当 $(a,\beta)=1$。反向取这样的 $a,\beta$ 及饱和标架即给一组有序本原列。

对复线性独立的 $x,y\in\Omega$，令 $n_{a,\beta}(x,y)$ 计 $\mathcal O_Dx+\mathcal O_D(y-ax)/\beta$ 中具有 $0<Q<1$ 代表的不同 $D$-方向数。它至少为二。对 $\mathfrak b=(1)$ 内和只取 $a=0$。公式为
$$ C_2=\frac1{4\zeta_D(2)\zeta_D(3)}
 \sum_{\mathfrak b\ne0}\frac1{(N\mathfrak b)^3}
 \sum_{a\in(\mathcal O_D/\mathfrak b)^\times}
 \int_{\Omega^2}\frac{dx\,dy}{n_{a,\beta}(x,y)}.                       \tag{5}$$

为证明 (5)，先固定指数理想和剩余类。一个 $3\times2$ 整标架饱和，恰当它在每个素理想处均满秩；在范数 $q$ 的素位，其比例为 $(1-q^{-3})(1-q^{-2})$。中国剩余定理先处理有限素位。大素尾可用几何筛：若某个大有理素数上方的素理想整除全部二阶子式，则该有理素数整除 $N_D(\Delta_{12}),N_D(\Delta_{23})$。两者是十二个整数变量的互素多项式；在复数上将原变量和共轭变量线性分开，其因子分别是不同的通用二阶行列式。Poonen 引理 5.1 说明大素尾在统一外包盒中密度趋零，无需 $abc$ 假设。故标架在每个有界 Jordan 区域的密度是 $1/(\zeta_D(2)\zeta_D(3))$。[Poonen，Lemma 5.1](https://arxiv.org/abs/math/0203292)

在复独立点的紧邻域，最小奇异值有正下界，可入球的两个整系数有界。因此 $1/n$ 仅在二次型等号的零测并集和依赖集才可能不连续，作有界 Riemann 积分合法。由 $Y=aX+\beta W$ 换元，实 Jacobian 为 $(N\mathfrak b)^3$；两列各有两个符号代表，故整体除四。将实变量同时乘层相位 $c$ 后，积分与 $c$ 无关。任取相位序列的收敛子列，缩去小奇异值区域后只剩有限二次型的边界，给这些边界加厚再令厚度趋零，即得同一极限。这给对层和素位的一致性。

将被积权 $1/n$ 临时换成 1，有限理想截断的总量随截断增大趋于 $C_1^2$，因为 $\sum\varphi_D(\mathfrak b)/(N\mathfrak b)^3=\zeta_D(2)/\zeta_D(3)$。这正是独立有序方向对的实际总量 $L(L-1)/R^{12}$ 的极限。故无质量遗失，$0<1/n\le1/2$ 允许通过理想和取极限，再由 (3) 得 (1)。对 $T\ge1$，范数 $\le T$ 的理想数小于 $4T$，直接数椭圆 $(a-b/2)^2+7b^2/4\le T$ 再除二即可。因此 (5) 中 $N\mathfrak b>T$ 的尾至多
$$\frac{\operatorname{vol}(\Omega)^2}{\zeta_D(2)\zeta_D(3)T}.$$
这是极限系数的有效截尾，(1) 的素数余项这里只给 $o(1)$。

## 4. 计数律的第三矩临界点

在 (5) 把 $1/n$ 换成 $\mathbf1_{n=k}$，再除 $C_1^2$，记结果 $w_k$，$k\ge2$。上述权 1 的论证和 $n$ 几乎处处有限给 $\sum w_k=1$。它是均匀**有序不同方向对**所见的平面重数律，与种子等权的观察不同。令 $\lambda=C_1\kappa^6$，后者的极限为
$$
 P_k=\frac{\lambda^2 w_k}{k(k-1)}\ (k\ge2),\qquad
 P_1=\lambda-\lambda^2\sum_{k\ge2}\frac{w_k}{k-1},\qquad
 P_0=1-\lambda+\lambda^2\sum_{k\ge2}\frac{w_k}{k}.
$$
前式从各有限平面抽取有序对即得，其余两式用 (3)，尾部以有序对质量控制。逐点收敛且极限总质量一，故在离散总变差中收敛。均值与方差均趋 $\lambda$。

### 极限分布的三次方尾

以下先取素数极限，再令整数阈值 $t\to\infty$。记 $A=\sqrt7/2$ 为 $\mathcal O_D$ 的复平面共体积。令 $x,y$ 独立均匀取自 $\Omega$；几乎处处 $V=\mathbf Cx+\mathbf Cy$ 为复二维平面。取同一 Hermitian 度量计算
$$
 G=\|x\|^2\operatorname{dist}(y,\mathbf Cx)^2,qquad
 \gamma(x,y)=\frac{\operatorname{vol}_4(\Omega\cap V)}{2A^2\zeta_D(2)G}.
$$
前述两种等权抽样的尾部分别为
$$
 \sum_{k\ge t}w_k\sim\frac{K}{t},\qquad
 \Pr(Z_\infty\ge t)\sim\frac{\lambda^2K}{3t^3},\qquad
 K=\frac{\zeta_D(3)\operatorname{Res}_{s=1}\zeta_D(s)}{\zeta_D(2)^2}
       \mathbb E_{x,y}\gamma(x,y).
$$
常数有限且严格为正。故极限占用的实矩对 $0\le h<3$ 有限，对 $h\ge3$ 发散。真实有限素数的三阶阶乘矩也趋向无穷，由逐点极限先求有限和再放开截止即可。有限素数只在固定阈值取极限；随 $p$ 增长的阈值以及 $2<h<3$ 时有限块矩的收敛仍待估计。

固定上述 $x,y$、$B=N\mathfrak b=|\beta|^2$ 与单位余类 $a$，记 $\Lambda=\mathcal O_D x+\mathcal O_D(y-ax)/\beta$。每条短方向恰有一对符号相反的本原代表落在 $\Omega\cap V$ 中，故 $n=n_{a,\beta}$ 是这个本原计数的一半。$\Lambda$ 的实共体积为 $A^2G/B$。取其最短非零向量 $v_1$，它本原，因而可扩成整环基 $v_1,v_2$。沿 $v_1$ 约化第二向量的系数。平面格 $\mathcal O_D$ 的覆盖半径至多 $\rho=2/\sqrt7<1$：其基本平行四边形可切为两只顶点全在格中的三角形，与顶点 $0,1,(1+i\sqrt7)/2$ 的三角形全等，外接圆半径为 $2/\sqrt7$。于是
$$
 \|v_2^\perp\|\ge\sqrt{1-\rho^2}\,\|v_2\|,\qquad
 \|v_1\|^2\|v_2\|^2\asymp G/B.
$$
这里用了 $\|v_1\|\le\|v_2\|$；又 $x,y$ 至少一者的第二个基系数是非零整元，故 $\|v_2^\perp\|\le\max(\|x\|,\|y\|)$。因 $\Omega$ 有界，两根基向量长度全有共同上界。任意短点 $h v_1+j v_2$ 的 $j$ 处于半径 $C/\|v_2\|$ 的盘，给定 $j$ 后 $h$ 处于半径 $C/\|v_1\|$ 的平移盘。计数给 $n\ll B/G$。在 $\Omega^2$ 上 $1/G$ 可积，因为 $x$ 有六实维，而 $y$ 到 $\mathbf Cx$ 的横向有四实维。

对固定 $x,y$、$\epsilon>0$，若 $\|v_2\|>\epsilon$，则 $\|v_1\|\ll_{x,y,\epsilon}B^{-1/2}$。最短向量写为 $u x+v(y-ax)/\beta$，由两列复独立，$|v|$ 与 $|\beta u-av|$ 都有只依 $x,y,\epsilon$ 的界；当 $B$ 足够大时 $v\ne0$。对每对这样的 $v,d=\beta u-av$，线性同余 $av\equiv-d\pmod\beta$ 至多有 $N(v)$ 个解。因此每个理想仅有 $O_{x,y,\epsilon}(1)$ 个坏余类。单位类数 $\varphi_D(\mathfrak b)\to\infty$（例如欧拉乘积直接给 $\varphi_D(\mathfrak b)\gg_D\sqrt B$），故均匀取单位 $a$ 时网格最长基向量依概率趋零。

凡两根基向量长度都趋零的标架，$n/B\to\gamma(x,y)$。具体地，$\Omega\cap V$ 为有界 Jordan 区域，固定小素理想的同余条件可逐格 Riemann 求和。对基系数 $h,j$ 均非零的点，它们分别落在中心为零、半径 $U\asymp1/\|v_1\|,V'\asymp1/\|v_2\|$ 的外包盘内（第一坐标用约化的平行系数有界及 $\|v_1\|\le\|v_2\|$）。因整环是主理想整环，一个半径 $U$ 的中心盘内某理想的非零倍数至多 $O(U^2/N\mathfrak d)$。两基系数同时被范数 $>T$ 的素理想整除的比例因而至多 $C_{x,y}\sum_{N\mathfrak d>T}(N\mathfrak d)^{-2}$，趋零。系数为零的两轴只占 $O_{x,y}(U^{-2}+V'^{-2})$。放开全部局部条件即得本原密度 $1/\zeta_D(2)$。配合前段，$n/B\to\gamma(x,y)$ 对单位 $a$ 依概率成立，沿所有 $B\to\infty$ 的理想皆然。

理想计数 $\#\{N\mathfrak d\le X\}\sim (\operatorname{Res}_{s=1}\zeta_D(s))X$ 在此亦可由整环盘计数除以二得到。将 $\varphi_D=\mu_D*N$ 代入并分部求和给
$$
 \sum_{N\mathfrak b>U}\frac{\varphi_D(\mathfrak b)}{(N\mathfrak b)^3}
 \sim\frac{\operatorname{Res}_{s=1}\zeta_D(s)}{\zeta_D(2)U}.
$$
对固定 $x,y$，由 $n\le CB/G$，算 $n\ge t$ 只需 $B\ge tG/C$。在这些理想上，把除去 $o(1)$ 比例的单位类里的 $n/B$ 用 $\gamma\pm\epsilon$ 夹住，将上式分别在 $t/(\gamma\pm\epsilon)$ 取尾，最后令 $\epsilon\downarrow0$。整个 $t$ 倍尾受 $C'/G$ 支配，故可再对 $x,y$ 积分。(5) 中有序对的归一因子是 $\zeta_D(3)/\zeta_D(2)$，给出第一条等价式。由 $\Pr(Z_\infty=k)=\lambda^2w_k/[k(k-1)]$ 再分部求和，给第二条的因子 $1/3$。

## 5. 系数数值、预算与原坐标实算

复算给出
$$
2.00482935\le C_1\le2.00483275,\qquad
0.434904\le C_2\le1.846585.
$$
第一式将 (4) 积到 1 且取三次分子的正部，分 $262144$ 格逐项以整定点区间外包；$\sqrt7,\pi,\zeta(3)$ 分别用整数平方根、Machin 交错和、正项和加积分余项。第二式是解析围界，未将十二维积分当作已精算小数。具体令
$$ M=\tfrac12\sum_{(u,v)\ne(0,0)}\max(Nu,Nv)^{-3}.$$
在单位指数项上，给定本原系数对 $(u,v)/\pm$，若该方向有短点，则 $ux+vy\in\Omega$。逐一固定 $x$ 或 $y$ 换元，概率至多 $\max(Nu,Nv)^{-3}$。把全部系数对拆成理想公因子及本原对，故 $E_{\Omega^2} n_{0,1}\le M/\zeta_D(3)$；Jensen 给 $C_2\ge C_1^2\zeta_D(3)^2/[\zeta_D(2)M]$。数 $\max(Nu,Nv)\le 10000$ 的整对，余项 $\le96/10000$，因为范数 $\le t$ 的整元至多 $8t$。上界使用 $x,y$ 都在原单位球时的真实附加方向：若其 $Q$-夹角满足 $|\cos\theta|\ge1/2$，则 $x+y,x-y$ 至少一个入球，除零测边界外 $n\ge3$。六实维角概率 $a_0=2/3-3\sqrt3/(4\pi)$，从而 $C_2\le C_1^2/2-a_0[V/(2\zeta_D(3))]^2/6$。

两素数类的自然密度为 $1/3$。令 $d=C_1\kappa^6-C_2\kappa^{12}$、$\alpha=\pi^3\kappa^6/(12\zeta(6))$，取父门槛。在决定平均对数指数的素数底块 $r=0$，两层共同的坏率下极限至少 $d$，上极限最多 $d+\alpha$（第二层仍用原第一矩并集界）。因此第 86 轮全整数条件化均值的对数指数下界再加 $d/[3(1-d)]$，该增量在 $[0.00000902016825,0.00000902026927]$ 内；上界中剩余度三一项可从 $2\alpha/[3(1-2\alpha)]$ 换为 $(d+\alpha)/[3(1-d-\alpha)]$。所用乘法上界、素数恰一次截取和严格窗口余量与原文相同。这里得出的是固定好种子条件费；没有把它转成实际几何失败事件的下界。[全整数预算与四锁](../seventeenth/conditioning.md) · [剩余度二的既有修正](../eightysixth/lines.md)

有限核从 $\mathbf Z[\zeta]$ 的六整数坐标枚举 $x=g^rv$，直接比较 $42^3 Q(x)^3<p^{3r+1}$，另检查原 $\gcd(x_0,\ldots,x_5)=1$ 的向量命中同一组方向。由 (2)，必有 $Q(v)\le7 Q(cv)<7p^{1/3}/42$，故枚举盒完备。再分别在 $D^3$ 与模 $(g)$ 的 $\mathbf F_p^3$ 中对点和两点决定的平面去重，检查逐类计数、两个阶乘矩和有序对重数表。

| $p$ | $r$ | 短整数对，模正负 | 短 $D$ 方向数 | 坏种子 | 最多不同方向 |
|---:|---:|---:|---:|---:|---:|
| 74099 | 0 | 6 | 6 | 444585 | 2 |
| 592727 | 0 | 36 | 36 | 21337831 | 7 |
| 2000387 | 0 | 116 | 91 | 182032948 | 11 |
| 811351 | 0 | 36 | 36 | 29208295 | 7 |
| 811351 | 1 | 39 | 36 | 29208298 | 7 |
| 811351 | 2 | 34 | 28 | 22717629 | 6 |
| 811351 | 7 | 46 | 37 | 30019635 | 7 |

$811351=N(901+450\omega)$，在两个共轭素位分别计算，表内各重数直方图相同。第 0、1 层恰有相同的方向总数，实际坏种子数仍相差三，互异点数本身不足以恢复坏率。$p=2,11$ 的首层另直接穷举全部种子对照。其余原冻结锁定和其它剩余度保持原计数范围。运行 `python seeds_check.py` 重建相邻 JSON。[标准库复算](seeds_check.py) · [整数与区间证书](seeds_checked.json)
