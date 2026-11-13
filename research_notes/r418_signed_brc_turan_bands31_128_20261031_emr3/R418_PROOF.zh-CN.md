# R418｜31≤s≤128 的98条带符号 BRC 辅助组合 Turán 正性定理

日期：2026-10-31。作者侧计算机辅助精确整数证明；原生研究权限、Driver 审阅和数学接纳未取得。对象仅为辅助组合观察量，未证明 X6 动力学或物理残差。

## 定义与主定理

对整数 r≥s+1，设

\[
\delta_{r,s}=[t^r](1-t)(1+t)^{2s}(1+t^2)^{r-s},\quad
H_{r,s}=\binom{r+s}{2s}\delta_{r,s},\quad
D_{r,s}=H_{r,s}^2-H_{r,s-1}H_{r,s+1}.
\]

**定理 R418：对所有整数 31≤s≤128 与所有整数 r≥s+1，有 D_{r,s}>0。** 即98条各覆盖无穷多个余阶的严格正性命题。

## 自包含推导：Catalan 核与带权恒等式

令 Cat_n=binom(2n,n)/(n+1)，C(w)=Σ_{n≥0} Cat_n w^n。直接从原始带符号提取式得 δ_{r,1}=Cat_{(r-1)/2}（奇 r）或0（偶 r）。由 (1+t)^2=(1+t²)+2t 得 δ_{r,q+1}=δ_{r,q}+2δ_{r-1,q}。对 r≥q≥1 归纳可得

\[
\delta_{r,q}=[z^r]z(1+2z)^{q-1}C(z^2)
=\sum_{\substack{0\le j<q\\r-q+j\ge0\ \mathrm{even}}}
\binom{q-1}{j}2^{q-1-j}\operatorname{Cat}_{(r-q+j)/2}.
\]

固定 s≥2 和余阶奇偶 ε∈{0,1}，令 r0 为满足 r0≥s+1、r0 mod2=ε 的最小整数，并设 r=r0+2x=2m+ε，x≥0，b=m−1+ε=b0+x，K=Cat_b。对 q=s−1,s,s+1 及核中合法 j，置 d=(q−j−2+ε)/2≥0、dmax=floor((s−1+ε)/2)。严格恒等式：

\[
\frac{\mathrm{Cat}_{b-d}}{\mathrm{Cat}_b}
=\prod_{a=0}^{d-1}\frac{b-a+1}{2(2(b-a)-1)}.
\]

设 T=Π_{a<dmax}2(2(b0+x−a)−1)，以及

\[
N_q=\sum_j \binom{q-1}{j}2^{q-1-j}
\left(\prod_{a<d}(b0+x-a+1)\right)
\left(\prod_{d\le a<dmax}2(2(b0+x-a)-1)\right).
\]

这些是 Z[x] 多项式，且 δ_{r,q}/K=N_q/T。因 b0≥dmax，x≥0 时每个乘积因子正。

令 Ln=2s(2s−1)(r+s+1)(r−s)，Ld=(2s+2)(2s+1)(r+s)(r−s+1)。精确的二项式相邻权重比为 λ=Ln/Ld。因此

\[
\frac{D_{r,s}}{[\binom{r+s}{2s}K]^2}
=\frac{A_\epsilon(x)}{B_\epsilon(x)},\qquad
A_\epsilon=Ld\,N_s^2-Ln\,N_{s-1}N_{s+1},\
B_\epsilon=Ld\,T^2.
\]

这里 B(x)>0。T、N_q 的次数均≤dmax，故 A、B 的次数≤2dmax+2。这给出**任意固定 s≥2 的有限正系数证书准则**：若两族 A 的升幂系数都非负且常数项严格正，则对全部 r≥s+1 有 D>0。偶族 dmax=floor((s−1)/2)，奇族 dmax=floor(s/2)，故每条 s 的两族合计恰须检查 2s+4 个分子系数槽位（分母同）。不将该有限判据误称为所有 s 的正性结论。

## 实际执行证据与范围

r418_interval_certificate.py 用标准库在整数多项式环精确构造 s=31..128 的196组 A/B，对升幂全部系数逐一判号：**15,974个 A 系数和15,974个 B 系数全部严格正**；同时从原始带符号式完成196个边界点交叉核验。

回执：R418_INTERVAL_EXACT_PASS 31 128 bands 98 parity_cases 196 A_pos 15974 B_pos 15974 boundary_checks 196

独立 r418_independent_validation.py 不导入生成器，分别使用直接卷积差与 Catalan 核，完成1028组原始整数 Turán 等式与3084组 Catalan 核等式；其中 s=31、64、128 两族全部 deg+1 个点，共458个完整次数界检查。回执：

R418_INDEPENDENT_PASS pairs 196 Turan 1028 Catalan 3084 full_degree_points 458

**这些有限交叉核验是辅助证据，证明无界 r 依靠前述全参数恒等式及完整正系数证书。** 全部判号为整数精确运算，未运行物理 BRC、π/三角演化或浮点判号。

本次生成的 R418_INTERVAL_EVIDENCE.json 含196组完整升幂系数（5,730,996字节），SHA256：
6cc10c505ea1f18bc106b3e58c108b0d1eea9a049c6e9f8b99ff9ace1eb049fe

生成的 R418_INTERVAL_MANIFEST.json SHA256：
995906309915338408717dc26399d98c3051a8deefd7370b41019bc5164120f4

此仓库目录存放完全可重复生成上述两份 JSON 的源码及独立检查程序；原始 JSON 同时保存在本轮交付证据包中。远程持久化源码/摘要与本地完整机器 JSON 是不同存储范围，不把摘要冒称已上传完整原始数组。

## 来源、权限、下一问题

依赖：R416 Catalan 核、R417 固定 s=30；本证明已重给核的独立推导。GLOBAL_KNOWLEDGE_V1 固定 main@7b33f8066e9993e7c941959a9d738ed405248eb8；项目 current main@e3148a75734182faea1e2822c84bd782b43005bb，R417 初始 PR head@89319169398a752883c847c51f3d7b7fe3b8be88。P000 与 ACTIVE 世界观不修改。

本轮定向上下文 authority_granted=false，当前 Task owner 查询 CONTROL_QUOTA；正式 CLAIM、Result、Review/接纳均未确认。状态：AUTHOR_SIDE_EXACT / UNREVIEWED / NOT_ADMITTED。

下一问题：s=129 的两族系数检验，以及是否可对所有 s 的 A 系数建立统一解析非负性定理或构造精确负系数/真实 D 反例。若先前作者侧右边界 r−s≤128 的报告也成立，则两侧合并后未覆盖区为 s≥129 且 r−s≥129，第一个参数对 (r,s)=(258,129)；仍待右边界独立审查。原生 X6 支路保真与物理对应、外部先前文献查重均未完成。
