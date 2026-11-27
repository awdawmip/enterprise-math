# EC49 任意预算下的首次删除耦合

2026-11-27 · 作者证明与本地精确复算 · 待项目评审

固定一个初始可加的 Port 分区，固定非负整数容量与当前活动标签。只做具名删除，许可删池为任意固定的标签子集。按包含关系极小的耦合删除集，恰好是**整体对偶中的 circuit（极小相关集），且在至少两个分块对偶中变为独立集**。若恰在 \(l\) 个分块对偶中独立，删除后的耦合缺口为 \(l-1\)。因此任意预算 \(h\) 内是否存在分区失效，可以只检查大小至多 \(h\) 的整体对偶 circuit。该命题在 EC49 有限容量匹配观察器上成立。

沿用具名删除对偶秩和两删缺口公式。三删判据已把第三删的首次耦合限制为整体秩二直线上的三元 circuit。本证明把该结构扩展到任意大小，并给出任意正缺口所需的最少标签数。[具名删除对偶秩](https://github.com/awdawmip/enterprise-math/blob/d80b07b7abe8d05915f682869f7a3192856af60f/research_notes/portable_direct/ec49_dual_deletion_observer_20261127/REPORT.md) · [两删缺口公式](https://github.com/awdawmip/enterprise-math/blob/126be54212a3668fee7803159d67aa55244d311c/research_notes/portable_direct/ec49_dual_deletion_observer_20261127/COUPLING.md) · [三删判据](https://github.com/awdawmip/enterprise-math/blob/399708591cc6a6bffe076c8d8e6f8f8135ada3df/research_notes/portable_direct/ec49_triple_coupling_20261127/REPORT.md)

## 记号与单步秩增量

设 Port 集 \(P=C_1\sqcup\cdots\sqcup C_k\)，活动标签集为 \(A\)。对于 \(S\subseteq P\)，记 \(r_S(Y)\) 为标签 \(Y\subseteq A\) 用 \(P\setminus S\) 的容量所能达到的最大匹配秩。记对应对偶秩为

\[
\rho_S(D)=|D|-r_S(A)+r_S(A\setminus D).
\]

删除后的 Port 观察为 \(g_D(S)=c(S)+r_S(A\setminus D)-r_\varnothing(A\setminus D)\)。定义缺口

\[
\Delta(D)=\sum_i g_D(C_i)-g_D(P)
=\sum_i\rho_{C_i}(D)-|D|-(k-1)\rho_\varnothing(D).
\]

第二个等号使用初态可加性。\(g_D\) 是容量匹配拟阵上增加各 Port 专用探针所得的归一化秩，因此次模。对任意查询 \(S\)，缺口 \(\sum_i g_D(S\cap C_i)-g_D(S)\) 沿加入一个 Port 弱增，初值为零，最大值为 \(\Delta(D)\)。于是 \(\Delta(D)=0\) 当且仅当分区在所有查询上可加。

令 \(R\) 是在活动标签之外，还加入每个 Port \(p\) 恰好 \(c(p)\) 个专用探针的容量匹配拟阵的秩。设 \(U_S\) 为 \(S\) 中所有探针。任意 \(Y\subseteq A\) 满足

\[
R(Y\cup U_S)=c(S)+r_S(Y).
\]

直接放入全部探针，再从 \(P\setminus S\) 匹配 \(Y\)，达到右侧。任意匹配在 \(S\) 至多使用 \(c(S)\) 个槽，其余匹配至多有 \(r_S(Y)\) 条，给出上界。给定 \(x\notin E\)，取 \(Y=A\setminus(E\cup\{x\})\)，可得

\[
\rho_S(E\cup\{x\})-\rho_S(E)=1-R(x\mid Y\cup U_S).
\]

秩边际 \(R(x\mid Y\cup U_S)\) 随 \(S\) 扩大弱减。因此每个标签在分块对偶中的单步秩增量，至少与同一前缀下的整体对偶增量一样大。特别地，整体对偶独立的集合在每个分块对偶也独立。

## 极小失败恰为多块独立的整体 circuit

设 \(D\) 是固定删池中按包含关系极小的正缺口集合。删池中的所有子集都合法，故对每个 \(x\in D\)，有 \(\Delta(D\setminus\{x\})=0<\Delta(D)\)。若 \(x\) 相对 \(D\setminus\{x\}\) 的整体对偶秩增量为一，各分块增量也均为一，代入缺口公式得到增量零。因此每个 \(x\) 的整体对偶秩增量为零，整体对偶限制在 \(D\) 上没有 coloop。

若 \(D\) 包含一个真子集 circuit \(B\)，则 \(\rho_\varnothing(B)=|B|-1\)。\(B\) 的每个真子集在各分块对偶中独立，因此每个 \(\rho_{C_i}(B)\) 取 \(|B|-1\) 或 \(|B|\)。设第二种值出现 \(l(B)\) 次，代入缺口公式得 \(\Delta(B)=l(B)-1\)。极小性给出 \(\Delta(B)=0\)，所以 \(l(B)=1\)。

取 \(x\in B\)。在其余分块对偶中 \(B\) 仍是 circuit，故 \(x\) 在 \(B\setminus\{x\}\) 的闭包中，也在 \(D\setminus\{x\}\) 的闭包中。至多一个分块对偶从 \(D\setminus\{x\}\) 加入 \(x\) 时增秩。整体增量为零，故 \(\Delta(D)-\Delta(D\setminus\{x\})\le 1-1=0\)，矛盾。于是 \(D\) 本身为整体 circuit。此时同一公式给出 \(\Delta(D)=l(D)-1>0\)。

反过来，给定整体 circuit \(D\)，若 \(l(D)\ge2\)，则 \(\Delta(D)=l(D)-1>0\)。其所有真子集整体独立，也在每个分块独立，缺口公式给出零。于是 \(D\) 是极小失败。预算查询只需找其中任一大小至多 \(h\) 的见证。给定删除序列的首次失效前缀内含一个上述见证。两个单位容量 Port 和两个均可去任一 Port 的标签，删除其中一个标签后耦合，再删除最后一个标签后恢复可加。故判断给定删除集的当前缺口仍使用 \(\Delta(D)\)。

## 标签数的尖锐界

设极小失败 \(D\) 的大小为 \(h\ge1\)，缺口为 \(d\ge1\)，它在 \(l=d+1\) 个分块对偶中独立。写 \(r=r_\varnothing(A)\) 与 \(r_i=r_{C_i}(A)\)。整体对偶 circuit 使整体匹配秩恰降一。每个令 \(D\) 独立的分块在删除后保持匹配秩 \(r_i\)，所以 \(r_i\le r-1\)。初态可加性给出 \(\sum_i(r-r_i)=r\)，于是 \(r\ge l\)。整体对偶总秩 \(|A|-r\) 至少为 \(h-1\)，因此

\[
|A|\ge h+d.
\]

给定任意 \(k\ge2\)、\(h\ge1\) 和 \(1\le d\le k-1\)，取 \(k\) 个单位容量的单 Port 分块，放入 \(h+d\) 个标签，每个标签均可去前 \(d+1\) 个 Port。删除少于 \(h\) 个标签时，前 \(d+1\) 个 Port 仍能同时满配，初态和这些后继态均可加。删除任意 \(h\) 个后，剩余 \(d\) 个标签仍可在移除任一单 Port 的情况下全部匹配，故 \(r_\varnothing(A\setminus D)=r_{C_i}(A\setminus D)=d\)，缺口为 \(d\)。该族对每个允许的 \((k,h,d)\) 取到等号。

## Hall 割的候选生成式

对 \(W\subseteq P\)，令 \(B_W=\{x\in A:E_x\not\subseteq W\}\)，其中 \(E_x\) 是标签许可掩码。定义初态割余量 \(s_W=c(W)+|B_W|-r\)。Hall 公式给出

\[
r_\varnothing(A\setminus D)=\min_{W\subseteq P}\bigl(c(W)+|B_W|-|D\cap B_W|\bigr).
\]

因此整体对偶 circuit 恰好是候选族 \(D\subseteq B_W\), \(|D|=s_W+1\) 的包含极小元素。每个匹配秩下降的删除集至少达到一个割的阈值，因而含有该割的一个候选。预算为 \(h\) 时，候选生成只需要 \(s_W<h\) 的割。可以对候选逐一查询整体对偶 circuit 条件，再检查分块对偶中是否至少两次独立。该式连接原始 Hall 割与本证明使用的具名 circuit。候选数量与代价取决于低余量割和许可删池的交集。

## 复算与续接

在本目录运行 `python replay.py | diff -u results.json -`。程序用直接 Hall 极小值逐一检查所有 Port 查询，用独立的容量槽位枚举计算整体和分块对偶秩，并逐个核对包含极小失败及 Hall 割生成式。固定输入为两个 Port、容量 0 至 2、至多六个标签的全部许可掩码多重集，以及种子 `4926112710` 的 300 个三至五 Port 实例。另外检查 75 个尖锐族实例，覆盖 \(2\le k\le6\)、\(1\le h\le5\) 和全部允许的 \(d\)。共核对 105,485 个具名删除集，其中 4,840 个为极小失败。各域的整数计数见 `results.json`。

续接时优先在实际冻结的许可删池上量出低余量 Hall 割的候选数，测试它与直接枚举整体对偶 circuit 前缀的代价分界。该实验需要保留标签、许可掩码、固定容量和分块映射。
