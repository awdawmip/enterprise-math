# 实际单射轴下的 raw X6 稳定性与三正取等流

Owner source candidate, 2026-09-08. 状态：`SOURCE_ONLY / PAPER_RESULT_CANDIDATE`。本文把已完成的有界独立纸面复核整理为可引用证明；没有新执行数学程序、LP、枚举、消费者或算术审计。没有 API、新工具族、正式 Task/Result/review、Working Truth 或主线准入。全文结论限于下述 raw 分析合同。

## 1. 对象与结论

在同一外部 anchor、同一带标签的实际整数六坐标 X6 图中，先合并同一空间 Cell，再作 Jordan 抵消，写有限有理分析差为

\[
f=\sum_{q\in S}w_q\delta_q-n,\qquad w_q>0,\quad n\ge0,\quad n(S)=0.
\]

这里负号是两个正人口的分析账本，不是负 BRC 原生分支。设

\[
P=\sum_{q\in S}w_q,\qquad N=n(\mathbb Z^6),\qquad
M=P+N=\|f\|_1,\qquad
D=\sum_{\substack{I\subset[6]\\|I|=3}}\|M_I f\|_1.
\]

\(M_I\) 是保留实际坐标标签的 raw 边缘；\(D\) 是全部二十张完整表的范数之和。若使用进取坐标的联合读出，必须同时保留 `can3` 与该 slice 的实际 common offset；`can3` 单独不能替代这些表。

**定理 1。** 假设存在一条实际坐标轴 \(a\)，使 \(q\mapsto q_a\) 在正支点集 \(S\) 上单射。记 \(N_{\rm empty}\) 为落在不含正点的 \(a\)-纤维中的负质量。任意有限 \(p=|S|\ge1\) 都满足

\[
\boxed{D\ge 10P-2N+10|P-N|+12N_{\rm empty}\ge4M.}
\tag{1}
\]

更精确地，右端分别为

\[
\begin{cases}
4M+16(P-N)+12N_{\rm empty},&P\ge N,\\
4M+4(N-P)+12N_{\rm empty},&N\ge P.
\end{cases}
\tag{2}
\]

因此非零差有 \(D>0\) 及 \(M/D\le1/4\)。三个正点已经能达到该常数，见第 4 节。该 sharp 声称针对满足本定理假设的总体类，不声称每个固定支撑模板、固定权向量或每个 \(p\) 都取等。若 \(p=0\)，则 \(f=-n\)，每张表的范数都是 \(N\)，故 \(D=20M\)；零差不取 \(0/0\)。单射轴是现有六条轴之一，不能换成新造的混合线性观测轴。

## 2. 纤维证明及全部松弛量

把二十张表拆成含 \(a\) 的十张之和 \(V\)，以及不含 \(a\) 的十张之和 \(U\)。在含 \(a\) 的表中，纤维标签仍保留，故不同纤维不能互相抵消。令 \(f_s\) 为轴值 \(s\) 的五坐标纤维，则

\[
V=\sum_s V_s,\qquad
V_s=\sum_{\substack{J\subset[6]\setminus\{a\}\\|J|=2}}\|M_J f_s\|_1.
\]

有正点的纤维恰含一个正点 \(r_s\)，正质量为 \(P_s\)，负质量为 \(N_s\)。对每个二轴集 \(J\)，定义

\[
A_{s,J}=\sum_{z:\ z_J\ne(r_s)_J}n_s(z).
\]

正投影地址处的 signed 质量为 \(P_s-N_s+A_{s,J}\)；其他地址只有负质量。因此有逐表精确式

\[
\|M_Jf_s\|_1=|P_s-N_s+A_{s,J}|+A_{s,J}.
\tag{3}
\]

Jordan 不交性保证每个负点 \(z\) 与 \(r_s\) 在剩余五轴上至少有一轴不同。设其不同轴数为 \(h\)。其投影避开正地址的二轴集个数为

\[
k(h)=10-\binom{5-h}{2}\ge4,
\tag{4}
\]

其中上标不足 2 时二项系数取零，且 \(k(h)=4\) 当且仅当 \(h=1\)。于是 \(\sum_JA_{s,J}=\sum_z k(h(z))n_s(z)\ge4N_s\)。利用 \(|x|=x+2\max(-x,0)\)，由 (3) 得到精确的非负松弛分解

\[
\begin{aligned}
V_s-(10P_s-2N_s)
={}&2\sum_z(k(h(z))-4)n_s(z)\\
&+2\sum_J\max(N_s-P_s-A_{s,J},0)\ge0.
\end{aligned}
\tag{5}
\]

无正点的纤维完全非正，每张二轴表的范数都是 \(N_s\)，所以 \(V_s=10N_s\)。合并有正与无正纤维，得到

\[
V\ge10P-2N+12N_{\rm empty}.
\tag{6}
\]

不含 \(a\) 的每张三轴表的 signed 总质量均为 \(P-N\)，故其范数至少 \(|P-N|\)，即

\[
U\ge10|P-N|.
\tag{7}
\]

(6) 与 (7) 证明 (1)，分开 \(P\ge N\) 与 \(N\ge P\) 即得 (2)。特别地，非零取等 \(D=4M\) 必须满足

\[
P=N,\quad N_{\rm empty}=0,\quad U=0,\quad V=8P,
\tag{8}
\]

且每个有正点纤维的 (5) 两项松弛都为零。这里既没有等质量的预设，也没有遗漏无正纤维；两者都是取等的必要后果。

## 3. 三正支撑模板中的 41/16 范围

复用已发布的三正 raw 支撑模板分类：一条轴的 `D-type` 表示三个正点在该轴上的值两两不同；它不是数值缺陷 \(D\)。因此存在实际单射轴等价于 \(n_{\mathrm{D\text{-}type}}\ge1\)。既有 57 个三点不同的无权支撑模板按该计数分组为

| `D-type` 轴数 | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 无权支撑模板数 | 16 | 16 | 11 | 7 | 4 | 2 | 1 |

所以其中 41 类满足定理 1 的假设，其余 16 类不由此假设覆盖。这是对已有分类及其手工计数的引用，本次没有重新枚举。41/16 分类的是无权正支撑；固定权向量仍须随点标签搬运，并遵守模板 stabilizer，不能独立排序或擅自改成等权。这里没有给出 41 类逐一取等结论，也没有解决一般三正问题。星形子类的既有结论不能借此推广到缺少单射轴的一般模板。

## 4. 非退化的三正 sharp 见证

取不同实际轴 \(a,b\)，其余四坐标全部相同且任意。取整数 \(a_0,a_1,a_2\) 两两不同、\(b_0\ne b_1\)，以及正有理权

\[
w_2,w_3>0,\qquad w_1=w_2+w_3.
\]

在这两轴平面内令

\[
\begin{aligned}
\mu={}&w_1\delta_{(a_0,b_0)}+w_2\delta_{(a_1,b_1)}+w_3\delta_{(a_2,b_1)},\\
\nu={}&w_1\delta_{(a_0,b_1)}+w_2\delta_{(a_1,b_0)}+w_3\delta_{(a_2,b_0)}.
\end{aligned}
\tag{9}
\]

六个 Cell 两两不同，故这就是 Jordan 分解，且恰有三个正支点。每个 \(a\)-行质量平衡；由 \(w_1=w_2+w_3\)，两个 \(b\)-列也分别平衡。四张同时含 \(a,b\) 的三轴表保留全部六个不同 Cell，范数各为 \(M\)；其余十六张分别由行平衡、列平衡或总质量平衡而为零。因此

\[
D=4M>0.
\]

见证的正支撑模板是 \(n_C=4,n_{\mathrm{D\text{-}type}}=1,n_{P_{23}}=1\)。\(b_0\ne b_1\) 不可删除：否则正负在原 Cell 抵消成零，不能证明非零 sharp。坐标间隔可以是任意非零整数，不要求相邻或单位步；此分析构造不声称是原生物理事件或路径实现。

## 5. 三正取等的去重流判据

现在固定恰好三个 Jordan 正点以及一条实际单射轴：

\[
q_i=(a_i,r_i),\quad a_i\text{ 两两不同},\quad r_i\in\mathbb Z^5,
\quad w_i>0\quad(i=1,2,3).
\]

令 \(R=\{r_1,r_2,r_3\}\) 为**去重后的坐标集合**，并设

\[
W_r=\sum_{j:r_j=r}w_j.
\]

**定理 2。** 对任意有限有理负人口 \(n\ge0\) 且 \(n(\{q_1,q_2,q_3\})=0\)，有 \(D(f)=4M(f)\) 当且仅当存在非负有理数 \(c_{i,r}\)，使

\[
n=\sum_{i=1}^3\sum_{r\in R}c_{i,r}\delta_{(a_i,r)},
\tag{10}
\]

并且

\[
\begin{aligned}
c_{i,r}&=0\quad\text{除非 }\operatorname{Ham}(r,r_i)=1,\\
\sum_{r\in R}c_{i,r}&=w_i\quad(i=1,2,3),\\
\sum_{i=1}^3c_{i,r}&=W_r\quad(r\in R).
\end{aligned}
\tag{11}
\]

这里 \(\operatorname{Ham}=1\) 指恰有一条实际坐标不同，不是单位距离。\(c_{i,r}\) 是聚合后的 Cell 质量，不是微观分支流。重复的 \(r_j\) 只产生一个列地址，其列需求是聚合权 \(W_r\)。

### 必要性

由 (8) 得 \(P=N\)、无空纤维负质量、\(U=0\)，且 (5) 的各个非负项为零。因此每个负点都处于某条正点 \(a_i\)-纤维，与该行的 \(r_i\) 恰在一轴不同；并且每个二轴集满足

\[
w_i-N_i+A_{i,J}\ge0.
\tag{12}
\]

擦去 \(a\) 后，记五坐标差

\[
g=\sum_iw_i\delta_{r_i}-\pi_*n.
\]

\(U=0\) 表示 \(g\) 的全部十张三轴边缘都为零。其 Jordan 正支点数至多为 3。下面直接证明 \(g=0\)：若 \(g\ne0\)，其总质量为零，故存在负支点 \(z\)，并有一至三个正支点。对每个正支点选一条与 \(z\) 不同的实际坐标，所选轴的并集至多三条；补足为五轴中的三轴集。在 \(z\) 的该投影地址上没有任何正贡献，却有严格负贡献，矛盾。因此 \(g=0\)。

所以 \(\pi_*n\) 恰好支撑于 \(R\)，各地址质量为 \(W_r\)。由此已得到 (10)、列和及 Hamming 限制。固定行 \(i\)，可有的不同目标地址至多是 \(R\setminus\{r_i\}\) 的两个元素；每个只改变一轴。因此这些目标所改变轴的并集至多两条。选择其外的任意两条轴作为 \(J\)，就有 \(A_{i,J}=0\)。由 (12) 得 \(N_i\le w_i\)。所有行负质量之和是 \(N=P=\sum_iw_i\)，故每行都满足 \(N_i=w_i\)，即行和条件。

### 充分性

若 (10)–(11) 成立，列和使 \(\pi_*n=\sum_iw_i\delta_{r_i}\)，所以 \(g=0\)、\(U=0\)。行和使 \(N_i=w_i\)，且每个负点恰改变一轴，故由 (4)

\[
\sum_J A_{i,J}=4w_i.
\]

在 (3) 中代入等质量，有 \(\|M_Jf_i\|_1=2A_{i,J}\)，从而 \(V_i=8w_i\)。因此 \(D=8P=4M\)。这也证明所有满足该有限流条件的负人口确实取等，未调用求解器。

### 退化与适用边界

- 若三个 \(r_i\) 全相同，\(|R|=1\)，没有 Hamming 距离 1 的目标，正行和不能实现；该固定支撑没有非零取等，定理 1 仍成立。
- 若例如 \(r_2=r_3\ne r_1\)，则必须有 \(\operatorname{Ham}(r_1,r_2)=1\)，且行列和强制 \(w_1=w_2+w_3\)。这是 (9) 的情况；相同的 \(r_2,r_3\) 不能被当成两个独立坐标列。
- 任何一行没有合法目标，便不可能满足其正行和。若初始差抵消后不足三正，须按实际 Jordan 正支点数处理。
- 必要性证明明确用了“\(g\) 至多三正”和“每行至多两个去重邻居”。定理 2 不是任意 \(p\) 的取等分类；任意 \(p\) 的结论仅为定理 1 及其必要松弛条件。

## 6. 复用来源、证据代次与未完成事项

四个冻结源均引用 owner 已发布的 `b506f92a117ec4f2e9b9b1a792fddb349a74b24d`。本次实际读取和元数据检索所用本地 `af4e305fb2e8aaf642b4c3c60f2bb44524c74a85` 的树为 `32dc880389d8f49352b72d88d774381b1d71338e`，与该发布树一致；具体文件 pins 见配套 `source_adoption.json`。

| 来源 | 本文使用范围 |
| --- | --- |
| [单正稳定性纸面来源](https://github.com/awdawmip/enterprise-math/blob/b506f92a117ec4f2e9b9b1a792fddb349a74b24d/research_notes/OWNER_ONE_POSITIVE_STABILITY_20260907.md) | 复用单正投影的正负聚合数账；第 2 节完整重建五轴二投影版本。 |
| [双正 raw 稳定性来源](https://github.com/awdawmip/enterprise-math/blob/b506f92a117ec4f2e9b9b1a792fddb349a74b24d/research_notes/OWNER_TWO_POSITIVE_RAW_STABILITY_BOUND_REVIEW_20260908.md) | 同一 raw 范数与 Jordan 合同的已有 \(p\le2\) 结果边界；本文不修改它的消费者守卫。 |
| [三正支撑模板来源](https://github.com/awdawmip/enterprise-math/blob/b506f92a117ec4f2e9b9b1a792fddb349a74b24d/research_notes/OWNER_THREE_POSITIVE_RAW_SUPPORT_TEMPLATE_REVIEW_20260908.md) | 第 3 节的 D-type、41/16 以及权标签/stabilizer 限定。 |
| [raw 零缺陷支撑来源](https://github.com/awdawmip/enterprise-math/blob/b506f92a117ec4f2e9b9b1a792fddb349a74b24d/research_notes/OWNER_X6_STABILITY_20260907.md) | 已有零缺陷稀疏支撑背景；定理 2 已给不依赖额外调用的短证明。 |

本次在上述 owner 树以既有 canonical toolbox 对指定原查询 `raw X6 three positive injective coordinate distinct axis one positive fiber stability` 实际运行一次 coverage，返回 `REUSE_CANDIDATE_FOUND`。完整输出已保存，没有执行匹配到的模块；退出码为 0，stderr 中 58 字节的 `SyntaxWarning: invalid escape sequence` 同时原样保留，没有将它记成零警告或修改范围外源码。语义决策是 **COMPOSE / EXTEND_EXISTING_RESULT**：把既有单正数账沿实际单射轴逐纤维组合，补齐质量差与空纤维项，再给三正去重流分类。raw 压缩、双正消费者、星形与 raw 对偶条目的词法命中只提供原合同下的邻接覆盖，不自动证明本定理、提供通用验证器或增加新 global family；有限 fiber、precision 等宽泛命中也不构成数学依赖。

配套 `OWNER_INJECTIVE_AXIS_RAW_STABILITY_INDEPENDENT_REVIEW_20260908.md` 是原 TEMP 时间点的辅助独审记录。其原始 SHA256 为 `436ce0539a4080efd9e5421b12fd9a0451198f6d072a8db950f8b86e87398a7d`；原文件已是 UTF8、LF、无 BOM、EOF LF，本归档逐字节保持，包括历史 `main@c2b245e` footer。这不是新的审稿执行或当前同步回执。源采纳由 owner 另行决定，本包不写仓库、不登记状态。

未完成边界：一般三正 raw 稳定性及无单射轴的 16 个模板仍未由本文解决；没有 41 类逐一 sharp 分类、任意 \(p\) 取等流分类、执行 API 或原生 runtime 认证。本文不恢复微观 BRC 分支、路径数、common-depth、history、原生距离或物理事件；任意线性观测与 `can3` 单独读出不继承结论。所有质量除式仅是纸面精确有理表述，本次没有执行求值算术。

Driver-ID: EM-DVR-01E1D9 / CONTROL_PLANE
Global-Knowledge-Sync: main@a624e4d / GLOBAL_KNOWLEDGE_V1
