# 两个非共线整数波矢的八个收缩量，哪些必须保留？

在波矢及两个模态能量已知时，原任务的全域恰有 **6 个按包含关系极小的观测菜单**，每个含 5 项。若两个模态能量均严格为正，则有 **19 个**，其中 18 个含 5 项，另一个含 6 项。两个自收缩可以在后一域同时删除。以下分类同时重建每个带符号频率的原始系数、压力接口和 Leray 投影。

一次简单的原始接口对照说明为何要分别检查这三个量。取 $k=e_1,l=e_2,B=e_3/2$，分别取 $A=e_3/2$ 与 $A=e_2/2$。支撑与两份能量相同。在 $k+l$ 处，依次得到 $(R/i,\sigma/i,P R/i)=((1,1,0)/4,1/4,0)$ 与 $(-e_3/4,0,-e_3/4)$。这是冻结来源的见证，本稿以此校准符号。母任务 R23 的原生 $32^3$ 运行仍待测量。[原任务](https://github.com/awdawmip/enterprise-math/blob/e17e50381a1ba51a2d1c8ad96e9440d08eb8ddc5/research_tasks/CFD_POLARIZATION_PORTABLE_CERTIFICATE_20260923.md) · [冻结输入](https://github.com/awdawmip/enterprise-math/blob/e17e50381a1ba51a2d1c8ad96e9440d08eb8ddc5/research_artifacts/CFD_POLARIZATION_SUPPORT_20260923/portable_problem.json) · [原始卷积函数](https://github.com/awdawmip/enterprise-math/blob/e17e50381a1ba51a2d1c8ad96e9440d08eb8ddc5/research_artifacts/CFD_POLARIZATION_SUPPORT_20260923/check_polarization.py)

## 1. 域和分类

$k,l\in\mathbb Z^3$ 非共线，$A,B\in\mathbb Q(i)^3$，$k\cdot A=l\cdot B=0$。点积是双线性积。记 $E_A=A\cdot\bar A,E_B=B\cdot\bar B$。负频率取共轭，正负交叉频率、自频率和零模全部保留，无混叠。表内单字母 $K,L$ 代表 $J_k=A\cdot A,J_l=B\cdot B$。其余为
$$
 S=A\cdot B,\quad T=A\cdot\bar B,\quad
 (\alpha,\beta)=(A\cdot l,B\cdot k),\quad
 (X,Y,Z,W)=(\alpha B,\beta A,\alpha\bar B,\bar\beta A).
$$

**极小菜单定理。** 表的前两行为含零能量的全域分类。表的全部六行为 $E_AE_B>0$ 的分类。每个名称串表示必须同时保留的字段。任意菜单充分当且仅当包含所在域的一项极小菜单。

|代表|同轨全部菜单|
|---|---|
|$KLSXW$|$KLSXW,\ KLSYZ,\ KLTXW,\ KLTYZ$|
|$KLTXY$|$KLTXY,\ KLSZW$|
|$KSTXW$|$KSTXW,\ KSTYZ,\ LSTXW,\ LSTYZ$|
|$KSXYZ$|$KSXYZ,\ KTXZW,\ LSXYW,\ LTYZW$|
|$KTXYZ$|$KTXYZ,\ KSXZW,\ LSYZW,\ LTXYW$|
|$STXYZW$|$STXYZW$|

还有两个半域。若仅保证 $A\ne0$ 而容许 $B=0$，从 19 个菜单中只保留含 $K$ 的 12 个，全部大小为 5。仅保证 $B\ne0$ 时对换 $K,L$。

交换两组波矢及振幅、或将 $B$ 共轭，分别诱导字段名置换 $(K\,L)(X\,Y)(Z\,W)$ 和 $(S\,T)(X\,Z)(Y\,W)$。具体数值可能同时共轭。例如交换振幅后 $Z'=\bar W$。两者都是全字段上的可逆换标，所以一旦某个代表恢复全部八个值，即可推广到整轨。

## 2. 统一恢复和退化分层

设 $U=k\cdot k,V=l\cdot l,s=k\cdot l,D=UV-s^2>0,n=k\times l$。取双基
$$
 u=(Ul-sk)/D,\qquad v=(Vk-sl)/D,\qquad
 A=\alpha u+a n,\quad B=\beta v+b n .
$$
则 $u\cdot u=U/D,\ v\cdot v=V/D,\ u\cdot v=-s/D,\ n\cdot n=D$。先处理 $E_AE_B>0$。此时 $X=0\iff\alpha=0$，$Y=0\iff W=0\iff\beta=0$，每个代表都能辨别分层。

**两自收缩同删。** 由最后一行其余六项，有下列精确分式：
$$
 K=\begin{cases}
 E_A(Y\cdot W)/(Y\cdot\bar Y),&Y\ne0,\\
 (ST+(U/D)X\cdot Z)/E_B,&Y=0,
 \end{cases}\qquad
 L=\begin{cases}
 E_B(X\cdot\bar Z)/(X\cdot\bar X),&X\ne0,\\
 (S\bar T+(V/D)Y\cdot\bar W)/E_A,&X=0.
 \end{cases}
$$
例如 $Y=0$ 时 $B=bn$，于是 $ST=D a^2 E_B$，且 $X\cdot Z=\alpha^2 E_B$。另一边同理。如此保留了复相位。

**$\alpha\beta\ne0$。** 前五行代表都给出 $X$ 及 $Y$ 或 $W$。记 $q=k\cdot X=\alpha\beta$。只有 $W$ 时令 $Y=q W/(l\cdot W)$。设 $A_0=Y/q=A/\alpha,\ B_0=X=\alpha B,\ h=E_A/(A_0\cdot\bar A_0)=|\alpha|^2,\ t=\alpha/\bar\alpha$。有
$$
 K=t h(A_0\cdot A_0),\quad L=(B_0\cdot B_0)/(t h),\quad
 S=A_0\cdot B_0,\quad T=t(A_0\cdot\bar B_0),\quad
 Z=t\bar X,\quad W=t(\bar q/q)Y .
$$
若给了 $Z$ 或 $W$，以 $k\cdot Z$ 或 $l\cdot W$ 除以 $\bar q$ 即得 $t$。余下的代表 $KLTXY$ 用 $K,L,T$ 中任一非零量和对应公式解 $t$。这三者不能同零：若 $K=L=0$，在两个实极化平面内写 $A=c(e+i\epsilon n_0),B=d(f+i\eta n_0)$，其中 $n_0=n/|n|$，$e,f$ 是相应平面内与 $n$ 正交的实单位向量，$\epsilon,\eta=\pm1$。于是 $T=c\bar d(e\cdot f+\epsilon\eta)\ne0$，因为非共线给出 $|e\cdot f|<1$。这里使用实归一向量仅为证明非零；恢复公式本身闭合于 $\mathbb Q(i)$。

**$\alpha=0$，容许 $\beta=0$。** 前五行代表均有 $K$。写 $A=a n,\ t_a=K/E_A=a/\bar a$。用 $T=t_a\bar S,\ W=t_a\bar Y$ 从每对给出的一端恢复另一端。再取 $y=n\cdot Y/D=a\beta,\ c=S/D=ab$，得到
$$
 L=\frac{(V/D)y^2+D c^2}{K/D},\qquad X=Z=0 .
$$
这也覆盖双公共法向情形，此时 $Y=W=0$。

**$\beta=0,\alpha\ne0$。** 此时 $B=b n,\ x=n\cdot X/D=\alpha b\ne0$。若给了 $L$，取 $t_b=L/E_B=b/\bar b$；若给了 $Z$，取 $t_b=x/(n\cdot Z/D)$。剩下的代表 $KSTXW$ 同时有 $S,T$。当 $T\ne0$ 取 $S/T$；当 $T=0$ 必有 $a=0$，此时取 $t_b=(x/\bar x)/(K/E_A)$。于是 $Z=X/t_b,\ S=t_bT,\ L=t_bE_B,\ Y=W=0$，任给 $S,T$ 之一即足够。

**零振幅。** 当 $B=0$ 只有 $K$ 可给出非零自频率，$A=0$ 时对称。两者俱零时全部为零。在所有层，恢复的八值按原接口给出
$$
 R_{2k}/i=kK,\quad R_{2l}/i=lL,\quad
 R_{k+l}/i=(k+l)S-X-Y,\quad R_{k-l}/i=(k-l)T+Z-W .
$$
$R_{-m}=\bar R_m$，零模由相反有序对抵消。由 $\sigma_m=m\cdot R_m/|m|^2,\ P_mR_m=R_m-m\sigma_m$ 唯一给出其余两项。

## 3. 同记录异输出的下界

固定 $k=e_1,l=e_2$。下列四元组依次是 $(\alpha,a,\beta,b)$，即 $A=(0,\alpha,a), B=(\beta,0,b)$。两列的能量逐模相同；第三列恰列出八字段中**不同**的项目。第四列的每个差异集均有一个不同带符号原始输出的实例。所有输入仅用 $0,\pm1,\pm i$。

|第一组|第二组|本行差异|合计差异集|
|---|---|---|---|
|$(0,1,0,1)$|$(0,i,0,i)$|$KLS$|$KLS,KLT$|
|$(1,0,0,1)$|$(i,0,0,i)$|$KLX$|$KLX,KLY,KLZ,KLW$|
|$(1,i,0,1)$|$(i,-1,0,i)$|$LSX$|$LSX,LTZ,KSY,KTW$|
|$(1,i,0,1)$|$(i,1,0,i)$|$LTX$|$LTX,LSZ,KTY,KSW$|
|$(1,0,1,i)$|$(i,0,i,-1)$|$KXY$|$KXY,KZW,LXY,LZW$|
|$(0,1,0,1)$|$(0,1,0,-1)$|$ST$|$ST$|
|$(1,i,1,i)$|$(i,-1,i,-1)$|$SXY$|$SXY$|
|$(1,i,1,i)$|$(i,-1,-i,1)$|$TZW$|$TZW$|
|$(1,0,0,1)$|$(1,0,0,-1)$|$XZ$|$XZ,YW$|

第四列通过交换两对坐标或共轭后两坐标取得。$TZW$ 独立列出，因为只对 $SXY$ 见证两边的 $B$ 取共轭能改变输出是否相等。复算对每个见证直接重算原始卷积。举例，$ST$ 行的正交叉输出依次是 $i(k+l),-i(k+l)$；其余六个字段全同，投影都为零。$XZ$ 行的正交叉输出分别是 $-i e_3,+i e_3$，连投影亦不同。

为重建全标签原始输出，每个充分菜单必须命中所列 23 个差异集。按 $|M|$ 从 0 到 8 枚举 $M\subset\{K,L,S,T,X,Y,Z,W\}$，保留满足“对表中每个集合 $D'$ 都有 $M\cap D'\ne\varnothing$”且不含已有解的 $M$，正好得到第 1 节 19 项。共有 52 个子集能命中全部差异集，第 2 节证明它们悉数充分；无需假设这个小高斯整数网格代表全部输入。一个容易人工核对的全域下界是再加入单点差异集 $\{K\},\{L\}$：$B=0,A=e_3$ 与 $B=0,A=i e_3$ 只改变 $K$，$R_{2k}$ 从 $ik$ 变为 $-ik$。交换得到 $\{L\}$。所以只保留含两个自收缩的六个极小菜单；半域则只加相应的单点约束。

## 4. 两种输出约定的代价

**仅求带符号的 Leray 投影。** $S,T,K,L$ 在各自频率产生纯梯度。故 $X,Y,Z,W$ 已经足够。第 3 节 $KLX$ 一组的四个实例各只改动一个向量字段并改变投影，因此这个向量菜单按包含关系极小。这里未分类含标量字段的其他投影菜单。

**原始输出按同一个空间平移等价。** 精确定义为 $R'_m=e^{im\cdot z}R_m$ 对所有 $m$ 同时成立，其中 $z\in\mathbb R^3/(2\pi\mathbb Z)^3$。对非共线 $k,l$，任意两个单位相位都可同时实现为 $e^{ik\cdot z},e^{il\cdot z}$，因为两个实线性方程可解。振幅的两条复射影线与两能量足以确定这一输出等价类，同一平移也给出相应的 $\sigma, P R$。

当 $E_AE_B>0$，最短观测恰为 $\{S,X,Y\}$ 与 $\{T,Z,W\}$。先证第一组充分。在 $\alpha\beta\ne0$ 时，两条复线由 $Y,X$ 直接读出。$\alpha=0,\beta\ne0$ 时第一条是 $[n]$，而 $b/\beta=S/(n\cdot Y)$ 决定第二条线 $[v+(b/\beta)n]$。$\beta=0,\alpha\ne0$ 时 $a/\alpha=S/(n\cdot X)$。两者都零时两线同为 $[n]$。第二组由第一组应用于 $(A,\bar B)$ 后再将第二条线共轭得到。

下界比计算不同的带符号系数更强。在 $k+l$ 处，下列各对 $R/i$ 甚至不在同一条复线上，空间平移无法消除其差别；它们的全部字段差异分别为三组互不相交的 $\{X,Z\},\{Y,W\},\{S,T\}$。

|不同字段|第一组四元组|第二组四元组|两列正交叉 $R/i$|
|---|---|---|---|
|$X,Z$|$(1,1,0,1)$|$(-1,1,0,1)$|$(1,1,-1),(1,1,1)$|
|$Y,W$|$(0,1,1,1)$|$(0,1,-1,1)$|$(1,1,-1),(1,1,1)$|
|$S,T$|$(0,1,1,1)$|$(0,1,1,-1)$|$(1,1,-1),(-1,-1,-1)$|

故三项候选必须从这三对各取一个。六个混用的三项也能排除：取 $(0,1,1,1)$ 与 $(0,i,i,-i)$。其 $S,W$ 相等，$X=Z=0$，但正交叉 $R/i$ 分别为 $(1,1,-1),(1,1,1)$。对两列交换或共轭 $B$，逐一代入，可排除 $SXW,SZW,TXY,TYZ,SYZ,TXW$。剩下的正是上述两个充分三项。

若容许单模，额外两组单点差异仍不可少，包括按平移取商时：$B=0$，把 $A=(0,1,1)$ 改为 $A'=(0,1,i)$，两能量相等而 $K$ 由 2 变为 0，原始输出从非零变成零。交换给出 $L$。故全域平移商最少 5 项，$K,L,S,X,Y$ 可达。这里仅对单一空间平移取商，未将旋转、反射、分频任意相位或另种压力约定纳入等价。

## 5. 复算与界面

同目录 [contractions_check.py](contractions_check.py) 的 $\mathbb Q(i)$ 观察器仅从被选择的字段及基底数据重建；实现按原输入来源约定建立完整符号频谱。输出记录 [contractions_checked.json](contractions_checked.json) 为**每个**差异集列出两份四元组、一个可区别的带符号频率及两份精确 $R/i$。代码中的 A、B 字段对应文中的 $K,L$。数值编码为一对有理数字符串，依次为实部、虚部。

三组波矢包括非正交、不等长的方向。共 252 组输入对卷积 16 个有序项和恢复公式作逐项对账，含 1308 次代表观察器恢复及 282 次完整字段换标恢复检查。原来源的 dot 和 raw_vortex 两个 AST 在可选命令中逐项比较相同，随后直接使用来源中的原函数。原函数的记录键含 over_4，这是原始分子示例的字段名；此处给它传入实际振幅，返回向量按 $R/i$ 解读。脚本只作外部精确有理代数核验。原生数值路线、BRC 商和性能仍依循母任务。此文完成固定相位、全保留、原始输出这一个八项菜单的数学分类。部分频率保留或有混叠时不适用。

单独运行和与原文件对账可分别执行：

~~~sh
python contractions_check.py | cmp - contractions_checked.json
python contractions_check.py --source "$ENTERPRISE_MATH/research_artifacts/CFD_POLARIZATION_SUPPORT_20260923/check_polarization.py" | cmp - contractions_checked.json
~~~
