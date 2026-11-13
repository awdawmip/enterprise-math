# R415｜带符号 BRC 辅助组合模型：s=28 的全余阶 Turán 正性及加权双参数递推

日期：2026-10-30。研究身份：Enterprise Math 研究3 的作者侧可移植推导。状态：AUTHOR_SIDE_EXACT / UNREVIEWED / NOT_ADMITTED。项目 P000、ACTIVE 世界观不变；本证明只对明确定义的辅助组合对象负责，不自动声称原生 X6 动力学或物理定理。

## 1. 对象和依赖

以原始十二支路带符号 BRC 的辅助组合对象定义

\[
\delta_{r,s}=[t^r](1-t)(1+t)^{2s}(1+t^2)^{r-s},\quad
H_{r,s}=\binom{r+s}{2s}\delta_{r,s},\quad
D_{r,s}=H_{r,s}^2-H_{r,s-1}H_{r,s+1}.
\]

这里 r,s 是整数、0≤s≤r；D 取 1≤s<r。已有 R404、R407 的 Catalan 正核恒等式适用于 s≥1：

\[
\delta_{r,s}=\sum_{\substack{0\le j<s\\r-s+j\equiv0\pmod2}}
\binom{s-1}{j}2^{s-1-j}\operatorname{Cat}_{(r-s+j)/2},\quad
\operatorname{Cat}_n=\binom{2n}{n}/(n+1).
\]

这项核恒等式及十二支路到该组合对象的上游传递仍需独立数学审阅。本研究对辅助数学定义的符号证明与原生模型解释分级保留。

## 2. 定理 R415-A（无界余阶）

\[
\boxed{\forall r\in\mathbb Z,\quad r\ge29\Longrightarrow D_{r,28}>0.}
\]

证明。令 r=2m+ε，ε∈{0,1}，C_0=Cat_(m-1)，C_1=Cat_m，并定义 Δ_(s,ε)=δ_(2m+ε,s)/C_ε。应用精确二项式权重比率

\[
\lambda(r,s)
=\frac{\binom{r+s-1}{2s-2}\binom{r+s+1}{2s+2}}{\binom{r+s}{2s}^2}
=\frac{2s(2s-1)(r+s+1)(r-s)}
{(2s+2)(2s+1)(r+s)(r-s+1)}.
\]

则严格有理恒等式为

\[
\frac{D_{r,s}}{\left(\binom{r+s}{2s}C_\epsilon\right)^2}
=\Delta_{s,\epsilon}^2-\lambda(r,s)\Delta_{s-1,\epsilon}\Delta_{s+1,\epsilon}.
\]

对 s=28，分两族做精确变量替换：偶 r=30+2x，m=15+x；奇 r=29+2x，m=14+x；x 为任意非负整数。对每一族，用 Catalan 数比率的逐因子有理表达计算右侧，在 QQ(x) 中化简、取分子分母并展开。实际运行的 r415_verify.py 将完整四个多项式降幂整数系数输出 R415_EVIDENCE.json。结果如下：

偶族的 P_0(x),Q_0(x) 均为27次，每个28个整数系数全部严格正；最小系数依次为 136608617616453096741797888 和 110930952192。奇族的 P_1(x),Q_1(x) 均为28次，每个29个整数系数全部严格正；最小系数依次为 68304308808226548370898944 和 221861904384。总计57个严格正分子系数及57个严格正分母系数，故 P_ε(x),Q_ε(x)>0 对全部 x≥0 成立。二项式权重和 Catalan 数均严格正，得到全部整数 r≥29 的 D_(r,28)>0。证毕。

两个端点的直接整数值：D_(29,28)=384402256302889411714898965764416；D_(30,28)=743413518624108347641997167198085376，均严格正。端点核对仅辅助检查，不代替全无限域符号证书。

## 3. 定理 R415-B（全部合法双参数的精确加权递推）

由 R414 已证明的三角递推 δ_(r,s+1)=δ_(r,s)+2δ_(r-1,s)，对任意整数 r≥1、0≤s<r，都有

\[
\boxed{(2s+2)(2s+1)H_{r,s+1}
=(r+s+1)\left[(r-s)H_{r,s}+2(r+s)H_{r-1,s}\right].}
\]

证明。设 b_(r,s)=binom(r+s,2s)，则

\[
b_{r,s+1}/b_{r,s}
={(r+s+1)(r-s)}/{((2s+2)(2s+1))},
\quad b_{r,s}/b_{r-1,s}={(r+s)}/{(r-s)}.
\]

将两个比率代回 δ 递推，清除分母即得。公式为纯整数的多项式恒等式，适用于边界 s=0，无须对所有 δ 假设正性；事实上 δ_(1,0)=-1。它将 R414 原始系数递推提升至直接控制 Turán 不等式的二项式加权对象，但尚未单独证明全双参数的 D>0。r415_weighted_recurrence.py 额外以精确整数对 1≤r≤160、0≤s<r 的12,880个参数对核验此代数式。

## 4. 执行证据、验证范围

在本地 Python/SymPy 精确算术环境，原始两族符号展开与完整系数证书通过，得到

R415_EXACT_PASS 2 57 57 92 276

修正证据 JSON 的 schema 字段为 S28 后，其 SHA256：
7cf60bf4d463546ea381d5b33437c0a1526006e64dd438cbc354ba8bb78fc6bc

该格式更正不改变已实际生成且交叉核验的114个正系数；证明生成器保留完整的精确有理构造。标准库独立复算返回：
R415_INDEPENDENT_INTEGER_PASS 10 points, 30 Catalan-kernel checks

三角递推扫描返回：
R415_RECURRENCE_PASS direct_coefficients= 1347 s28_cert_crosschecks= 292 uncovered_region_positive_grid= 13366 first_uncovered= (158, 29) s29_unknown_grid= 163

加权递推整数核验返回：
R415_WEIGHTED_RECURRENCE_PASS 12880 exact integer identities r<=160

92次 Turán 十进制整数交叉乘验证与276次 Catalan 核核验来自生成器；独立标准库程序还检查10个更大 r 的点；原始 δ 提取与三角递推比对1347个整数系数；r≤320 的未覆盖区仅有13,366个点得到有限精确正性，不能把它当作无限域证明。所有判号采用精确整数/有理代数而非浮点推测。附件 R415_EVIDENCE.json 含全部四组实际整数系数，可由脚本重建和独立验算。

## 5. 依赖、权限、下一问题

已知作者侧左带至 s=28，右带覆盖 r-s≤128；未获得无条件双参数证明的区域因此变为 s≥29 且 r-s≥129，首个参数对为 (r,s)=(158,29)。下一最小单元是固定 s=29 的全余阶正性证书或严格反例；长期问题是使用 R415-B 证明权重补偿机制而不再逐带扩展。R403/R404 的上游符号转移、与原生 X6 的联系以及独立数学审阅仍待明确完成。

规范来源：GLOBAL_KNOWLEDGE_V1 main@4458ae7b7f0c3f1645083f0d64fd7d5e77f112e8；Enterprise Math main@93aed370045bcd8a1cc8685c3f593f0d4e375577；直接上游 R414@9290f8145defff77a7a389ff7e6635d60d9ae70f。GitHub 连接身份 awdawmip；原生服务0.6.11 research_authority_granted=false，control_tasks 返回 CONTROL_QUOTA，故 Source Owner 无法权威确认且本轮无正式 CLAIM/Result/Driver Review/准入。