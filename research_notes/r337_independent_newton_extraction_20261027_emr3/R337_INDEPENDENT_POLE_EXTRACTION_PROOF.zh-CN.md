# R337｜原始 BRC K/J 递推的 Newton 抽取式与次数界：独立的有限极点证明

**科学级别：AUTHOR_SIDE / EXACT_INTEGER_FRACTION_VERIFIED / UNREVIEWED / NOT_ADMITTED。** 本文从原始十二项带符号 BRC 辅助组合递推重建 R330 使用的关键抽取式与 `deg H_r≤r`，不将 R330 的该引理当作假设。证明使用多项式分子、有限差分与形式幂级数，不采用物理类比或有限样本外推。

## 0. 固定输入与边界

账户规范读取快照：`awdawmip/chatgpt-global-knowledge main@93755c1673bf4ba017acc56f5a7608a8cc730409`；本次 Enterprise Math 源读取快照：`main@5fc8518a2af15c7656a2ad410f5bf04943f88a6b`。先前最高研究证明来源：R336 Git commit `83f8376658be664109d566744c635314970e6a86`；R330 旧作者证明 Git commit `7c73f56263c3f0515aa28e55ced2d4c703b8e086`。

P000 与 ACTIVE 世界观按原件保持，心跳世界的六维原生离散 Cell 空间加独立时间维度未改变。下文 `q,r,s,k,u` 是辅助组合模型的整数下标；`x,t,y,z` 为形式生成函数变量，均非进取原生空间轴、时间或物理相位。本研究只作用于已定义的正权有序六边 BRC **辅助组合计数模型**，保留递推产生的域外有符号尾项，且未建立至原生 X6 Cell 动力学的桥。

定义 `C(n,k)` 为普通二项式系数，`0≤k≤n` 时按通常取值，其余为零。对 `s≥0`，

\[
B_0(t)=1+t,\qquad B_s(t)=J_s(t)+\sum_{i=1}^{\min(12,s)}K_i(t)B_{s-i}(t),
\]

其中

\[
K_i(t)=-\sum_{j=1}^4 d_{ij}t^{i-1}(1+t)^{i+1-j},
\quad(d_{i1},d_{i2},d_{i3},d_{i4})=(-C(4,i)+C(2,i-1),\ C(5,i-1)-C(5,i-2),\ C(7,i-2),\ -C(9,i-3)),
\]

\[
J_s(t)=-C(3,s-1)t^s(1+t)^s-C(6,s-1)t^s(1+t)^{s-1}+C(8,s-2)t^s(1+t)^{s-2}.
\]

没有实际非零系数的越界项视为零；特别 `K_i=0` 对 `i>12`，`J_s=0` 对 `s>10`。令 `b_{s,q}=[t^q]B_s(t)`，以及

\[
D_{q,k}=\sum_{v=0}^k(-1)^{k-v}\binom{k}{v}2^{q-v}b_{q+v,q},\quad 0\le k\le q.
\]

## 1. 新的有限多项式分子递推（不依赖 R330）

定义有限有理母函数

\[
U(x,t)=\sum_{s\ge0}B_s(t)x^s=\frac{A(x,t)}{1-K(x,t)},\quad
K=\sum_{i=1}^{12}K_i(t)x^i,\quad A=1+t+\sum_{s=1}^{10}J_s(t)x^s.
\tag{1}
\]

把 `K(x,t)=2x+Σ_{h≥1}L_h(x)t^h` 与 `A(x,t)=Σ_{h≥0}A_h(x)t^h` 分开，则从上述有限输入**直接**得到：

\[
\deg_x L_h\le h+1\ (h\ge1),\qquad \deg_x A_h\le h,\qquad K(x,0)=2x,\quad A_0(x)=1.
\tag{2}
\]

理由：`K_i` 的每个非零项含因子 `t^{i-1}`，所以对 `t^h` 的贡献必有 `i≤h+1`；`J_s` 的每个非零项含 `t^s`，所以 `A_h` 只含 `x^s` 且 `s≤h`。两结论都保留原始符号，未截除域外项。

取 `U_q(x)=[t^q]U(x,t)`，定义 `P_q(x)=(1-2x)^{q+1}U_q(x)`。从 `(1-K)U=A` 逐阶抽取，得到全 `q≥1` 的有限整数多项式递推：

\[
\boxed{P_0(x)=1,\qquad
P_q(x)=(1-2x)^qA_q(x)+\sum_{h=1}^{q}L_h(x)(1-2x)^{h-1}P_{q-h}(x).}
\tag{3}
\]

归纳证明 `P_q∈ℤ[x]` 且

\[
\boxed{\deg_xP_q\le 2q\quad\text{对所有整数 }q\ge0.}
\tag{4}
\]

具体地，(3) 第一项次数至多 `q+q=2q`；任意求和项次数至多 `(h+1)+(h-1)+2(q-h)=2q`。这也给出独立可执行的有限分子算法。

## 2. Newton 差分抽取式的全指标代数证明

令

\[
p_{q,j}=[y^j]P_q((1-y)/2),\qquad 0\le j\le2q.
\]

根据 (4)，`p_{q,j}=0` 对 `j>2q`；且

\[
U_q(x)=\sum_{j=0}^{2q}p_{q,j}(1-2x)^{j-q-1}.
\tag{5}
\]

在 `s=q+v≥q` 抽取 `x^s` 时，`j≥q+1` 对应最高次数 `j-q-1≤q-1` 的普通多项式，因而没有贡献。余下 `0≤j≤q` 使用负整数幂的**严格形式级数恒等式**：

\[
\boxed{b_{q+v,q}=2^{q+v}\sum_{j=0}^{q}p_{q,j}\binom{2q+v-j}{q-j}.}
\tag{6}
\]

将 (6) 代入 `D_{q,k}`，再使用

\[
\Delta_v^k\binom{a+v}{d}\big|_{v=0}=\binom a{d-k},
\]

取 `r=q-k`，得到对**所有整数** `q≥r≥0`：

\[
\boxed{D_{q,q-r}=4^q\sum_{j=0}^{r}p_{q,j}\binom{2q-j}{r-j}.}
\tag{7}
\]

该证明完全由 (1)–(6) 和有限差分恒等式构成，无须先采用 R328–R330 的抽取引理。

## 3. 极点展开、次数界及完整 R330 公式

作形式代换 `x=(1-y)/2, t=yz`，在形式环 `ℚ[[y,z]]` 中考虑

\[
\mathcal P(y,z)=yU((1-y)/2,yz)
=\frac{N(y,z)}{E(y,z)}=\sum_{j\ge0}G_j(z)y^j,
\quad N=A((1-y)/2,yz),\quad E=(1-K((1-y)/2,yz))/y.
\tag{8}
\]

由 (1) 的低阶原始核项 `K_1(t)=2+3t`、`[t]K_2(t)=-1`、`[t^2]K(x,t)=4x^2-8x^3` 可直接得到

\[
E_0(z)=1-\frac54z,\qquad E_1(z)=z,\qquad N_0(z)=1.
\tag{9}
\]

对 `ℓ≥1`，`deg_z E_ℓ≤ℓ+1`（`y^ℓ` 项来自 `t^h=(yz)^h` 与非负的 `(1-y)^i` 幂，满足 `h≤ℓ+1`）；同理 `deg_zN_j≤j`。写

\[
G_j(z)=\frac{g_j(z)}{(1-5z/4)^{j+1}}.
\]

`g_0=1`，形式比较得到对 `j≥1`：

\[
\boxed{g_j=N_jE_0^j-\sum_{\ell=1}^jE_\ell g_{j-\ell}E_0^{\ell-1}.}
\tag{10}
\]

由上述次数界归纳：

\[
\boxed{\deg_z g_j\le2j\quad\text{对全部整数 }j\ge0.}
\tag{11}
\]

另一方面，先以 `t` 展开 `U`、后在 `z` 中系数抽取，有恒等式

\[
[z^q]\mathcal P(y,z)=y^{q+1}U_q((1-y)/2)=P_q((1-y)/2).
\]

`N/E` 的常数项为 1，故在 `ℚ[[y,z]]` 中交换取系数合法，得到 `p_{q,j}=[z^q]G_j(z)`。因此当 `q≥r≥j`，用 `g_j(z)=Σ_{m=0}^{2j}g_{j,m}z^m` 展开：

\[
p_{q,j}=\sum_{m=0}^{2j}g_{j,m}(5/4)^{q-m}\binom{q-m+j}{j}.
\tag{12}
\]

重要的边界细节：`q-m+j≥q-j≥0`。即使 `q<m`，此时上端落在 `0,…,j−1`，普通二项式系数为零，恰好符合不允许负次项的形式级数约定。(12) 因而对**全部** `q≥r≥j` 成立，且关于 `q` 是至多 `j` 次的多项式乘以 `(5/4)^q`。

由 (7)、(12)，令 `q=r+u, a=4/5`：

\[
\boxed{
D_{r+u,u}=5^uH_r(u),\quad
H_r(u)=5^r\sum_{j=0}^r\sum_{m=0}^{2j}g_{j,m}a^m
\binom{r+u-m+j}{j}\binom{2(r+u)-j}{r-j}.
}
\tag{13}
\]

每一求和项关于 `u` 的次数至多 `j+(r-j)=r`，所以

\[
\boxed{H_r\in\mathbb Q[u],\qquad\deg H_r\le r\quad\forall r\ge0.}
\tag{14}
\]

即 R330 被 R331–R336 反复引用的抽取式与次数界，现在具有**来自原始有符号 K/J 的一条独立完整代数证明**。这不宣称 R331–R336 的每一份计算证书都已经获得数学同行审查。

## 4. 附带结论：全 r 最高 Newton 插值差分系数

设 `c_{r,i}=Δ_u^i H_r(0)`。令 `a=4/5`，由 (9)(10) 直接在 `z=a` 评价。`E_0(a)=0` 且 `E_1(a)=a`，故

\[
g_0(a)=1,\qquad g_j(a)=-a\,g_{j-1}(a)=(-a)^j.
\tag{15}
\]

在 (13) 抽取 `u^r` 最高次系数：

\[
[u^r]H_r=5^r\sum_{j=0}^r\frac{2^{r-j}g_j(a)}{j!(r-j)!}
=\frac{5^r}{r!}(2-a)^r=\frac{6^r}{r!}.
\]

由于 `Δ^r` 消去所有低于 `r` 次的多项式，得到独立推论

\[
\boxed{c_{r,r}=\Delta^rH_r(0)=6^r>0\quad\forall r\ge0.}
\tag{16}
\]

这是对 R333 最高层全指标公式的另一条独立推导，而不是新的系数取样外推。它不能仅凭最高差分正性推出所有中间 `c_{r,i}>0`。

## 5. 实际精确验证范围

`R337_verify_pole_extraction.py` 使用独立编写的 Python 整数多项式递推与 `Fraction`，重新生成原始 **全有符号** 12 项 `K/J/B` 以及全新的 `P_q` 递推 (3)，没有导入 R330–R336 的程序、系数表或预设多项式。

命令：`python R337_verify_pole_extraction.py --max-q 24 --output R337_EXACT_EVIDENCE.json`。实际输出 `PASS`：`q=0..24`、`B_s s=0..56`，直接整数系数与有限分子重构 **1,425项**一致，原始 `D_{q,k}` 与 (7) **325项**一致，(16) 的 `r=0..18` **19项**一致；原始三角域内 **1,653项**严格正，域外 **697个负系数**保留。精确有理变换系数计算625项；没有使用浮点数判别正负。

机器摘要中的 325 个 D 值序列 SHA256：`bf583d44e3bc308ec11233b86dca57a907ccb9f398ffa5811bebd2386e4cccdf`。有限交叉验证与上述全指标形式代数证明是两类证据；无界结论建立在 (1)–(16)，不依赖计算上限24。

## 6. 研究等级、来源与下一问题

2026-10-27 本轮作者侧结构性证明**明确消除了 R331–R336 共同依赖的 R330 抽取/次数引理作为“未证明外部假设”的必要性**，但其余逐带正性证书仍按自身内容及独立审查流程评估。没有原生 CLAIM、Source Result 或 Driver 审查的成功回执；科学状态为 `AUTHOR_SIDE / SOURCE_PERSISTENCE_SUBJECT_TO_REMOTE_READBACK / UNREVIEWED / NOT_ADMITTED`。此次 native `em_control_tasks` 返回 `CONTROL_QUOTA`；活跃 Owner 权威核对列为恢复项，不能用仓库写入权限等同于 Owner 授权。

**下一精确问题**：利用 (3) 与 (13) 的两种完全不同的表示独立复核 R331–R336 中任意一段临界正锥系数；进一步证明 `(r,i)` 同时增长时全部 `c_{r,i}` 正性，或者给出精确负系数及其在原始 `D`/规定三角域中的作用。另一条明确定义的支线是由 (10) 推导第五阶 jet 与第六高 `c_{r,r-5}`。

来源：R330 Git commit `7c73f56263c3f0515aa28e55ced2d4c703b8e086`、R336 Git commit `83f8376658be664109d566744c635314970e6a86`；P000 `main@5fc8518a2af15c7656a2ad410f5bf04943f88a6b`，GLOBAL_KNOWLEDGE_V1 `main@93755c1673bf4ba017acc56f5a7608a8cc730409`。
