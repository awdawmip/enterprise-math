# HCM0 有符号极端支的全阶导数与误差半径

在已冻结的相邻等长三层点 $m=15,S=0,a=c=1$，完整迹之差是一个十四阶导数的平均。对同一有理核再求导，前 36 个交替导数在整个积分区间恒正，随后四个导数各有一个简单零点，从第 40 个开始恒负（以十四阶导数为第 0 个）。这给出迹为正的逐点证书，也给出把该核加强为完全单调函数的严格反例。两组可测节点还能给出完整迹的最优误差半径。两项推导使用同一原始点。

## 1. 观测量及来源

任务的原域是整数 $m\ge2$、实数 $S\ge0$、$a,c>0$，同步三层满足 $r_0=mS,\ M=ma,\ N=m(a+c)$。原式 (6.2) 用行标 $(i,p,q)$、奇偶符号 $(-1)^{i+p+q}$、正的 beta/二项式权和混合余子式的平方表示完整迹。此次按作者交接固定 $a=c=1$。记 $n=m-1,\ r=m(S+1),\ s=r+m$，早晚两端的归一化割线型为 $A,B$，目标为 $D=\operatorname{tr}(B^{-1}A)-n>0$。早晚共用的符号对角合同保持迹。以下等式只使用完整收缩，原三元标签对应的两类质量仍以原式为准。[原任务书](https://github.com/awdawmip/enterprise-math/blob/ff3a4a4f203e77db68631232ce85d89c595595f9/research_tasks/PERFECT_PRIME_AP_HCM0_EXTREME_BRANCH_PARITY_DOMINATION_20260909.md) · [原始三指标公式 §6](https://github.com/awdawmip/enterprise-math/blob/623a4ee81911cc79d07ed5db1887a06ebe91ffd5/research_artifacts/PERFECT_PRIME_AP_SIGNED_SECANT_HCM0_HAUSDORFF_LIFT/EXTREME_COEFFICIENT_SIGNED_BRANCH_BRC_REDUCTION_20260906.md)

写 $\theta_i=(i+1)/m,\ \xi_k=-r-k$（$0\le i,k<m$），并置

$$
V(X)=\prod_i(X-\theta_i),\quad P_t(X)=(X+t)_m,\quad
R_t=P_t-V,\quad L_t=mt+(m^2+1)/2.
$$

交接单位 B 的核为

$$
\mathcal B_t(X,Y)=\frac{V(X)R_t(Y)-R_t(X)V(Y)}{X-Y}
-\frac{R_t(X)R_t(Y)}{L_t}.
$$

令 $E_mg(X)=g(X+m)$，$T=2(I+E_m)^{-1}$，并取
$Z(X)=[T_XT_Y\mathcal B_s-\mathcal B_r](X,X)$、$f=Z/P_r$。由双边最高项分别相消，$\deg Z\le2m-4$。出处已给出

$$
D=\frac{m^n}{n!}\Delta_{1/m}^n f(1/m)
=\int_{[0,1]^n}\frac{f^{(n)}((1+\sum_j u_j)/m)}{n!}\,du.
\tag{1}
$$

原作者还证明单位 A 的固定坐标逐项比较在 $m=3$ 对每个 $S\ge0$ 失败，并以完整矩阵有理计算得到单位 C 的 $m=15,S=0$ 正迹。单位 A 的负结果针对充分条件。切向面的既有验收 RR-491F / DR-053D 与本题相邻正间隙的全域断言分别立项。下文在单位 C 同一参数上使用单位 B 的标量公式，不增扫维度或参数。[原有残数对偶](https://github.com/awdawmip/enterprise-math/blob/623a4ee81911cc79d07ed5db1887a06ebe91ffd5/research_artifacts/PERFECT_PRIME_AP_SIGNED_SECANT_HCM0_HAUSDORFF_LIFT/RESIDUE_DUAL_STP_SECANT_FRAME_20260904.md) · [作者部分交接与三单位原文](https://github.com/awdawmip/enterprise-math/blob/ff3a4a4f203e77db68631232ce85d89c595595f9/research_artifacts/mcp/RS-PERFECT-PRIME-AP-HCM0-EXTREME-BRANCH-PARITY-DOMINATION/MCP-e3eda4529333438d8ae1ae7e6983e5e5/8c93a8558258cb5e68f5/PARITY_WHOLE_UNIT_PARTIAL_CAPSULE.json) · [最新交接检查点](https://github.com/awdawmip/enterprise-math/blob/b46c77b64f5f42ed98a14f94dda29d4e2dc2cfac/research_artifacts/mcp/RS-PERFECT-PRIME-AP-HCM0-EXTREME-BRANCH-PARITY-DOMINATION/MCP-e3eda4529333438d8ae1ae7e6983e5e5/8c93a8558258cb5e68f5/_checkpoint.json)

## 2. 全部导数的符号

令 $I=[1/m,1]$，对整数 $h\ge0$ 置

$$
F_h(x)=\frac{(-1)^h f^{(n+h)}(x)}{(n+h)!}
=\sum_{k=0}^{m-1}\frac{\gamma_k}{(x+r+k)^{m+h}},
\qquad
\gamma_k=\frac{(-1)^{n+k}Z(-r-k)}{k!(n-k)!}.
\tag{2}
$$

这是部分分式展开，因为 $Z/P_r$ 的多项式部分次数小于 $n$。故 $F'_h=-(m+h)F_{h+1}$。

**有序极点判据。** 在右端 $b$ 取 $b>-r$。若对某 $H\ge0$ 的所有前缀满足
$C_j=\sum_{k=0}^{j}\gamma_k/(b+r+k)^{m+H}<0$，则一切 $h\ge H,\ -r<x\le b$ 都有 $F_h(x)<0$。所有不等号同时反向也成立。事实上令
$v_k=(b+r+k)^{m+H}/(x+r+k)^{m+h}$，由对数导数可得 $v_k\ge v_{k+1}>0$，再用

$$
F_h(x)=C_{m-1}v_{m-1}+\sum_{j=0}^{m-2}C_j(v_j-v_{j+1}).
\tag{3}
$$

**冻结点定理。** 对 $m=r=15,\ s=30$，$F_h$ 在 $I=[1/15,1]$ 的完整分类如下。

| $h$ | 对应 $f$ 的阶数 | $F_h$ 在 $I$ 的符号 |
|---|---|---|
| $0$ 至 $35$ | $14$ 至 $49$ | 全区间严格正 |
| $36,37,38,39$ | $50$ 至 $53$ | 各有一个简单零点，左负右正 |
| $h\ge40$ | 所有 $54$ 阶及以上 | 全区间严格负 |

四个零点依序落在 $(67,68)/1000$、$(363,364)/1000$、$(659,660)/1000$、$(955,956)/1000$。以下三项有限有理检验足以推出整张无限表。

1. 在 $b=1,H=47$，(3) 的十五个前缀全部严格负。
2. 左端点 $F_0,\ldots,F_{47}$ 的符号为前 36 个正、后 12 个负。右端点为前 40 个正、后 8 个负。
3. 直接把四组有理端点代入 (2)，每组左负右正。

由 (3)，尾部 $h\ge47$ 已定。向下递推到 $h=40$ 时，每个 $F_h$ 随 $x$ 递增，右端值为负。于是 $F_{39}$ 严格递增，恰穿零一次。若 $F_{h+1}$ 左负右正且只有一个简单零，则 $F_h$ 在该零点前递增、后递减。对 $h=38,37,36$，两端异号迫使简单零点落在递增段，依次得到四根的严格次序。此时 $F_{35}$ 的最小值取于两个端点之一，故全区间为正。继续向下，每层递减且右端值为正。特别地，积分式 (1) 的被积函数 $F_0$ 严格递减，给出

$$
3\,956\,244\,916\,140 < F_0(1)<D<F_0(1/15)<14\,723\,994\,965\,339.
$$

这说明在此参数，积分使用的逐点正性成立，提高到无限阶交替正性则在 $h=36$ 首次失败。截断前缀从 $H=47$ 启动只是该尾部判据的一种取法，函数本身从 $h=40$ 开始就在全区间负。

## 3. 由两个节点网格得到精确误差半径

用 $U=\{\theta_i\}$、$W=\{\xi_k\}$ 和 $Q=VP_r$。早端有限差分及其残数式给出同一线性泛函

$$
\Lambda(Z)=\sum_{z\in U}\frac{Z(z)}{Q'(z)}
=-\sum_{z\in W}\frac{Z(z)}{Q'(z)}=D .
\tag{4}
$$

对任意次数 $\le2m-4$ 的实多项式，两边相等。更精确地，Lagrange 插值给出
$\sum_{Q(z)=0}Z(z)/Q'(z)=[X^{2m-1}](Z\bmod Q)$，从而等式在次数 $\le2m-2$ 仍成立，单项式 $X^{2m-1}$ 给出首个差值 $1$。

**最优误差定理。** 对次数 $\le2m-4$ 的多项式，能在全部 $2m$ 个节点恢复 $\Lambda$ 的线性系数恰为

$$
c_z(H)=\frac{\mathbf1_{z\in U}+H(z)}{Q'(z)},\qquad \deg H\le2.
$$

若每个读数准许独立绝对误差 $\delta_z>0$，仅使用这一次数信息，在所有容许的真多项式和观测上取最坏情形，最小可保证的绝对误差为

$$
R(\delta)=\min_{\deg H\le2}\sum_z \delta_z |c_z(H)|
=\max_{\substack{\deg p\le2m-4\\ |p(z)|\le\delta_z}}\big|\Lambda(p)\big|.
\tag{5}
$$

证明如下。多项式取值空间的余维恰为三。三个向量 $(z^j/Q'(z))_z$，$0\le j\le2$，由高项插值系数恒为零而湮没这一空间，且线性独立。给取值空间赋范数 $\max_z |p(z)|/\delta_z$；有限维线性规划对偶（等价地，保范延拓）给出 (5)。极端多项式 $p$ 和 $-p$ 可产生同一组零读数，证明任意估计器都服从下界。目标函数是三维空间上分片线性的加权绝对值和。由于节点互异、权重为正，其最小集有界，必可取到一个分片顶点。于是只须枚举任意三个节点，把 $H$ 插值为在这三点等于 $-\mathbf1_U$，总计至多 $\binom{2m}{3}$ 组。该论证对 $m=2$ 亦适用。

**同一冻结点的尖锐精度。** 取固定误差尺度 $e_z=|Z_{\rm ref}(z)|$，其中 $Z_{\rm ref}$ 是本点原核，所有 $e_z>0$；读数误差至多 $2^{-b}e_z$。表中 $\kappa=R(e)/|D|$，$b$ 为使 $2^{-b}\kappa<1$ 的最小非负整数。单网格使用 (4) 的对应系数，本例每个单网格的取值都可任意插值。

| 可用的节点 | $\kappa$（近似） | $b$ |
|---|---:|---:|
| 早端 $U$ | $1.771044359\cdot10^{19}$ | 64 |
| 极点 $W$ | $17\,256.45686$ | 15 |
| 两组全部 | $17\,256.45686$ | 15 |

全网格最优可取 $H=-1$。这是对独立节点读数误差的结论，运算中间值的舍入需另行计入。取 $b=15$ 的最差相对正余量约为 $47.33747\%$，取 $b=14$ 时即使测得完整无偏移中心数据，也容许相反符号的候选多项式。此歧义针对固定尺度和次数信息；额外使用核的具体参数方程可缩小候选集。

下界证书还可跳过二次函数枚举。令候选极端多项式的极点取值为 $u_z=-\operatorname{sgn}(Q'(z))e_z$。早端仅在 $J=\{1/15,8/15,1\}$ 三处取非零值；用 $J$ 的二次 Lagrange 基 $\ell_i$ 定义

$$
u_i=-Q'(i)\sum_{z\in W}\frac{u_z\ell_i(z)}{Q'(z)},\qquad i\in J.
$$

由此三个湮没和 $\sum_z z^j u_z/Q'(z)$ 全为零，故 $u$ 正是某个次数 $\le26$ 多项式的取值。对三个特殊节点逐个有理比较得 $|u_i|<4\cdot10^{-9}e_i$，全部误差约束都满足。其 $\Lambda$ 恰达到极点单网格上界，证明任意混合读法均无法改进。这是实际模型的一次精度测量，两个网格内的残数贡献各为 7 项正、8 项负。

## 4. 复算与边界

运行同目录的 <code>python residues_check.py</code> 可逐字重建 <code>residues_checked.json</code>，只需 Python 3.9 及以上标准库。程序用 $T=\sum_{j=0}^{m-2}(-1/2)^j(E_m-I)^j$ 在节点上直接生成 Bezout 核，不调用冻结的矩阵程序；两个网格独立收缩，结果均与既有完整矩阵证书的精确分数一致（$D\approx7.6447755242922\cdot10^{12}$）。脚本记录两端全部 48 个符号的游程、十五个前缀的符号、四组零点区间、三个极端插值修正以及三种精度的确切分数。公开检查与原始作者单位共享来源及参数。

在全部 $m\ge2,S\ge0$ 的相邻等长族，(2)、(3)、(5) 都可使用。使 $F_0$ 或其平均统一为正的条件仍待证明。一般正间隙的原奇偶质量比较和 HCM0 母目标也仍开放。本笔记提供局部数学结果，正式 Driver 验收另由原流程处理。

[复算程序](residues_check.py) · [有理数证书](residues_checked.json)
