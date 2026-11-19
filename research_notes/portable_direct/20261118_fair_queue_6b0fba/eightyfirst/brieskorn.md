# Seifert 整同调球的有限矩阵探测阈值与分歧提升

同一个有限群清单能否识别一族整同调三维球？设 $n>1$、$(n,6)=1$。对纤维重数为 $(2,3,n)$ 的 Seifert 整同调球 $M_n$，有限域 $\mathbf F_q$ 上真正产生的不可约迹数是
$$
 B_n(q)=\frac{\gcd(n,q-1)+\gcd(n,q+1)-2}{2}+\mathbf1_{\operatorname{char}\mathbf F_q\mid n}.
 \tag{1}
$$
若 $n=r$ 为素数，最小见证域大小为 $r$，唯 $r-1$ 是二的幂时降为 $r-1$。特别地，任何事先规定的有限群清单都漏掉无限多个 $M_r$。下述同态计数还适用于含幂零元的有限交换局部环。在分歧素数 $r$ 上，即使剩余域、绝对分歧指数和模环大小全相同，提升数仍可相差一个正数量级。

## 1. 真实剖分与表示问题

取 $\epsilon\in\{1,-1\}$ 使 $n\equiv\epsilon\pmod6$，置 $b=(\epsilon-n)/6$。给球面基底配三组 Seifert 数据 $(2,1),(3,-1),(n,b)$，无额外扭转。依定向选择，这给 Brieskorn 整同调球 $\Sigma(2,3,n)$ 或其反定向。给基底三孔球选边界环，各实心环面填充分别杀去相应的本原斜率，得到
$$
 G_n=\langle X,Y,Z,h\mid h\text{ 中心},\ X^2=h^{-1},\ Y^3=h,\ Z^n=h^{-b},\ XYZ=1\rangle .
 \tag{2}
$$
交换化关系行列式绝对值为 $|6n(1/2-1/3+b/n)|=1$。Regina 的具名例程接受正负未经正规化的纤维参数；程序先构造闭剖分，再从签名重新解码，使用解码后真实的生成元和关系作有限枚举。以下列出一部分输入。[Regina 标准剖分接口](https://regina-normal.github.io/engine-docs/classregina_1_1Example_3_013_01_4.html) · [登记任务书](https://github.com/awdawmip/enterprise-math/blob/e68f6bd03ad532f8c754ba70e8b655933f107d5b/research_tasks/P3R-NONABELIAN-FINITE-OBSERVER.md)

|对象|四面体数|Regina 签名|最小见证域大小|
|---|---:|---|---:|
|$S^3$|1|`bkaagj`|无|
|旧五胞庞加莱球|5|`fvPQcdecedekrsnrs`|4|
|$M_7$|9|`jLAMLLQbcbdeghhiixxjxxjqisj`|7|
|$M_{11}$|9|`jLAMLLQbcbdeghhiixxnxxjqisj`|11|
|$M_{13}$|10|`kLAMzLMkbcbdefhiijjhhwhhhkixnn`|13|
|$M_{17}$|10|`kLAMzLMkbcbdefhiijjxhnhhhkixnn`|16|
|$M_{25}$|12|`mLAMzMLLQbcbdefghjkkllxxjqqqqqwihrw`|4|
|$M_{35}$|13|`nLAMzMzLAkbcbdefghikllmmhhjhxqqqqnmxkk`|4|

例如 $M_7$ 解码后的两条关系为 $ab^{-1}ab^2=1$ 与 $a^{-1}ba^6b=1$。模七取
$$
 a=\begin{pmatrix}0&1\\6&5\end{pmatrix},\qquad b=\begin{pmatrix}1&1\\6&0\end{pmatrix}.
$$
两条关系均成立，生成的 $336$ 个矩阵遍及 $\mathrm{SL}_2(\mathbf F_7)$。这里的 $a,b$ 属于剖分返回的呈示。(2) 用来证明整个族的分类，两组原字分别核验。$n=5$ 的黄金迹二次式及其模 $25$ 障碍已由第22轮得到；复数域上 Brieskorn 球的不可约角色计数也有经典工作。[第22轮](../twentysecond/finite_observer.md) · [Kitano–Yamaguchi 的实与复表示结果](https://arxiv.org/abs/1602.07503)

## 2. 所有有限局部环上的迹分类

令 $R$ 为有限交换局部环，极大理想为 $\mathfrak m$，剩余域为 $k=\mathbf F_q$。令 $m=(n-1)/2$，以整数递推 $V_{-1}=0,V_0=1,V_{j+1}=xV_j-V_{j-1}$ 定义 $P_n=V_m-V_{m-1}$。则
$$
 \#\operatorname{Hom}(G_n,\mathrm{SL}_2(R))
 =1+|\mathfrak m|^3 q(q^2-1)\,\#\{c\in R:P_n(c)=0\}. \tag{3}
$$
每个 $c$ 恰标记一个非平凡 $\mathrm{GL}_2(R)$ 共轭类，约化后绝对不可约。

**中心纤维与小特征。** 若约化在代数闭包上可三角化，约化像可解，完美性迫其平凡。同余核按 $\mathfrak m^j$ 过滤有可解商，所以原像也平凡。以下取非平凡表示。约化的 $X,Y$ 生成全部矩阵代数，而 $h$ 必为标量（先在剩余域用绝对不可约性，再由 Cayley–Hamilton 和 Nakayama 将基 $I,X,Y,XY$ 提至 $R$）。剩余射影像中 $X,Y,XY$ 任一为单位都会使该像变为循环群；完美性排除此情形。因此 $I,X$、$I,Y$ 各自在 $R$ 上线性独立。设 $h=\lambda I$，比较 $X^2=(\operatorname{tr} X)X-I=\lambda^{-1}I$ 得 $\operatorname{tr}X=0$、$\lambda=-1$。比较 $Y^3=((\operatorname{tr}Y)^2-1)Y-(\operatorname{tr}Y)I=-I$ 得 $\operatorname{tr}Y=1$。这个系数比较在剩余特征二、三也成立。例如 $R=(\mathbb Z/4)[w]/(w^2+w+1)$ 含有平方为一的单位 $1+2w$，关系仍强制 $h=-I$。

**双向还原。** 置 $X'=(-1)^{1-b}X$、$C=X'Y$，则 $C^n=-I$。反过来给出行列式为一、迹为 $0,1$ 的 $X',Y$，以及 $C^n=-I$，逆用此符号，置 $Z=(XY)^{-1}$、$h=-I$，即满足 (2) 全部关系。令 $c=\operatorname{tr}C$，Cayley–Hamilton 给出无除法恒等式
$$
 C^{-m}(C^n+I)=(C+I)P_n(c).
$$
剩余 $C$ 非标量，故 $C+I$ 有单位条目，必要性成立；反向直接相乘即可。

**存在及轨道。** 每个迹根 $c$ 都使 $c^2-3$ 为单位。看剩余域代数闭包，写 $\bar c=z+z^{-1}$。恒等式 $z^m(z+1)P_n(z+z^{-1})=z^n+1$ 给 $z^{2n}=1$。若 $\bar c^2=3$，又有 $z^4-z^2+1=0$，故 $z^{12}=1$。由 $(2n,12)=2$，推出 $z^2=1$、$\bar c^2-3=1$，矛盾。取
$$
 X'=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\qquad
 Y=\begin{pmatrix}u&v+c\\v&1-u\end{pmatrix}.
$$
行列式条件为 $u^2-u+v^2+cv+1=0$。奇特征下其齐次二次型的二倍矩阵行列式为 $2(3-\bar c^2)$；特征二下仿射偏导 $F_u=1$，无穷远唯一可能奇点 $[1:1:0]$ 要求 $\bar c=1$，也已排除。有限域上的光滑射影圆锥由 Chevalley–Warning 有点，故有 $q+1$ 点，无穷远至多两个。任一光滑仿射解沿极大理想各层提升。此迹三元组的 Fricke 不可约判别量就是 $c^2-3$；在迹配对下 $I,X',Y,C$ 的 Gram 行列式为 $-(c^2-3)^2$。同迹对的矩阵基乘法表相同，两对共轭，因为局部环上矩阵代数自同构是内自同构（用两对角矩阵单位的秩一自由直和作基）。稳定子为 $R^\times I$，轨道长即 (3) 的前因子。

## 3. 有限域见证的算术阈值

在 $\bar k$ 置 $w=-z$。对 $w\ne1$，根对应 $w^n=1$ 的反演对 $\{w,w^{-1}\}$。其迹属 $k$ 当且仅当 $w^q=w$ 或 $w^q=w^{-1}$；两群的公共 $n$ 阶元素只有 $1$。剩余的 $w=1$ 对应 $c=-2$，而 $P_n(-2)=(-1)^m n$。这就证明 (1)，含特征二及 $n$ 有重素因子的情形。特别地当 $n=r$ 为素数，根数在剩余特征 $r$ 时为 $1$；其余情形中，$q\equiv\pm1\pmod r$ 时为 $m$，否则为零。

故 $r$ 自身始终可用；较小的见证仅可能为 $q=r-1$，此数是偶数，作为素幂它必须是二的幂。实际上令 $S=\left(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\right)$、$Y=\left(\begin{smallmatrix}0&-1\\1&1\end{smallmatrix}\right)$，则 $SY=-\left(\begin{smallmatrix}1&1\\0&1\end{smallmatrix}\right)$。$S,Y$ 于 $\mathbf F_r$ 上满足正规化关系，并生成全 $\mathrm{SL}_2(\mathbf F_r)$。固定 $p\ne r$ 时，最小扩域次数是 $\operatorname{ord}_r(p)/\gcd(2,\operatorname{ord}_r(p))$。相对于所有有理素数，见证素域的自然密度为 $2/(r-1)$；不同 $r$ 的这种事件独立于素数自然密度，来自固定乘积模数上的中国剩余定理和等差数列素数定理。例如同一素域同时见证 $M_7,M_{11}$ 的密度为 $1/15$。

任意有限群 $Q$ 若 $(n,|Q|)=1$，每个 $G_n\to Q$ 都平凡。用像中 $h$ 的中心循环群取商，$Z$ 在商中满足 $Z^n=1$，故平凡；$X,Y$ 互逆且阶分别整除二、三，也平凡。原像因此为交换群，完美性完成证明。取大于有限清单中所有群阶的素数 $r$ 即得同时漏检，同时上面的模 $r$ 矩阵证明 $G_r$ 确实非平凡。

## 4. 分歧素数上模精度的断点

限 $n=r$ 为素数，$m=(r-1)/2$。在混合特征离散赋值环 $\mathcal O$ 中，剩余域大小 $q=r^f$，均匀化元 $\pi$，$e=v_\pi(r)$。令 $N_k$ 为 $P_r(c)$ 在 $\mathcal O/\pi^k$ 的根数。对全部 $k\ge1$，
$$
 N_k=
 \begin{cases}
 q^{k-\lceil k/m\rceil},&k\le e,\\
 m q^{e-e/m},& k>e,\quad m\mid e,\quad
 (-1)^{m+1}\overline{r/\pi^e}\in(k_0^\times)^m,\\
 0,&\text{其余情形},
 \end{cases}\qquad k_0=\mathbf F_q. \tag{4}
$$
在等特征 $r$ 离散赋值环取第一行对全部精度成立；在剩余特征异于 $r$ 时所有迹根单纯，按 Hensel 逐级唯一提升。

证明只需看 $P_r(y-2)$。这是首一的 $r$-Eisenstein 多项式，常数为 $(-1)^m r$，且模 $r$ 等于 $y^m$（由 $(z^r+1)/(z+1)=(z+1)^{r-1}$）。当 $k>e$ 时，先看剩余已得 $v_\pi(y)>0$；若 $mv_\pi(y)\ne e$，首尾项的最低赋值唯一。如果 $mv_\pi(y)=e$，写 $y=\pi^{e/m}v$，除掉 $\pi^e$，得到单位上的剩余方程 $v^m=(-1)^{m+1}\overline{r/\pi^e}$。它共有零或 $m$ 个简单根，每个根提升到精度 $k-e$ 后，还剩 $e-e/m$ 个任意剩余位。固定一对模 $\pi$ 的非平凡原关系矩阵，则其模 $\pi^k$ 的具名提升数为 $N_k q^{3(k-1)}$，由 (3) 的各轨道等纤维性得出。

例取 $r=7$，在 $\pi^3=7$ 与 $\pi^3=14$ 的两座全分歧塔中，前三层迹根数同为 $1,7,49$。第四层分别为 $147$ 与 $0$：在 $\mathbf F_7$ 中 $1$ 是立方，$1/2$ 不是立方。这些数字通过环上逐系数乘法穷举核验。另一项复算从旧五胞剖分的真实生成元出发，在 $(\mathbb Z/4)[w]/(w^2+w+1)$ 和 $(\mathbb Z/9)[w]/(w^2+1)$ 中，固定各自模 $2$、模 $3$ 扩域表示，分别检验 $4096$ 和 $531441$ 对行列式一候选，准确得到 $64$、$729$ 个具名提升。

## 5. 复算、归属与开放范围

使用 Python 与 Regina 7.4.1，运行 `python brieskorn_check.py --out brieskorn_checked.json`。程序逐个重建闭、可定向、连通的有效剖分，验其整一阶同调，直接枚举重解码呈示的同态。为使计数可复验，首矩阵按 $\mathrm{GL}_2(\mathbf F_q)$ 共轭类分组（标量单列，其余由迹唯一确定）；每个首矩阵代表搭配全部第二矩阵，按类长计权。第一条非平凡见证直接核验交换子迹异于二，其像阶由群乘法闭包算出。七个 $n$ 上共计 $61$ 组剖分–有限域配对，另以冻结五胞逐字做三组对照。实测域大小从 $2$ 至 $17$，各剖分所用的具体域、原关系、生成矩阵、扩域多项式及精度分层均在结果文件中。$O(q^4)$ 个矩阵对称代表测试足以核一个有两个生成元且关系长度固定的剖分；该复算不依赖式 (1) 跳过任何测试。有限域公式、局部环计数与 $r$ 处分歧分类是本轮在旧黄金迹之外直接处理的范围。[复算程序](brieskorn_check.py) · [逐项输出](brieskorn_checked.json)

给定剖分、从其基本群导出的呈示和一组真正满足关系的非平凡矩阵，排除三球是无条件的。对本文族，填充关系给出显式见证，无须寻找例外素数。对任意非三球整同调三维球，Zentner 的普遍复不可约表示存在性有几何化依赖；复代数解约化到某个有限域有非有效的代数途径，而普遍多项式位长的见证素数界另有 GRH 条件。本文算出的阈值针对这组具名 Seifert 输入，其他剖分的见证规模仍是独立问题。[Zentner 的存在性及复杂性推论](https://arxiv.org/abs/1605.08530) · [项目纠正后的依赖范围](https://github.com/awdawmip/enterprise-math/blob/3359de19ffb776ebfaa59bc7443b171b23d35f4d/research_notes/POINCARE_BRC_CORRECTED_FRONTIER_HANDOFF_20260909.md)
