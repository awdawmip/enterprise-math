# R525 — signed BRC 辅助标量四十八阶 Toeplitz 子式：全正整数参数符号分类

日期：2026-11-04。冻结科学输入 R462@18783e01e3646c72b7aab3b16d3f565e83e6446f；前沿 R524@df9bdb0b9f2fb564716ad2a523da9f8ab451b630。状态：AUTHOR_SIDE_EXACT_COMPUTER_CERTIFICATE / DRIVER_UNREVIEWED / NOT_ADMITTED。

## 条件定理：m=48 的全正整数参数符号

设整数 \(k\ge1\)、\(r=2k+1\)、\(C_k=\binom{2k}{k}/(k+1)>0\)，并定义

\[
H_k(t)=\binom{r+t}{2t}[x^r](1-x)(1+x)^{2t}(1+x^2)^{r-t}\quad(2\le t\le r),
\]

在其余整数 \(t\) 上取零。令 \(D_m(k)=\det(H_k(3+i-j))_{0\le i,j<m}\)，\(D_0=1\)。采用冻结 R452/R462 固定 \(t\) 的多项式引理：\(p_t(k)=H_k(t)/C_k\) 在 \(k\ge1\) 上等于次数至多 \(2t\) 的有理多项式。

则
\[
\boxed{D_{48}(k)>0 \ (1\le k\le5\ \text{或}\ k\ge14),\qquad D_{48}(k)<0\ (6\le k\le13).}
\]
这给出 \(r=3,5,\ldots,11\) 的严格正性、\(r=13,15,\ldots,27\) 的严格负性，以及**全部奇数 \(r\ge29\)** 的严格正性。整数 \(k\ge1\) 没有零点。

结合 R524 的 \(D_{47}\) 全参数结论，可推出两个相邻阶数异号区间：
\[
D_{47}(k)>0>D_{48}(k)\quad(k=6,7),
\qquad
D_{47}(k)<0<D_{48}(k)\quad(14\le k\le20).
\]

## 归一化行列式、多项式证书

Toeplitz–Hessenberg 展开给出 \(f_0=1\) 及
\[
f_m=\sum_{a=1}^{m}(-1)^{a-1}p_{a+2}p_2^{a-1}f_{m-a},\qquad f_m=D_m/C_k^m .
\]
冻结多项式引理蕴含 \(\deg f_m\le6m\)，所以 \(\deg f_{48}\le288\)。取正多项式
\[
G(k)=[k(k+1)(2k+1)(2k+3)]^{48}(k+2),\quad \deg G=193.
\]
在 \(k=1,\ldots,96\) 对 \(f_{48}(k)/G(k)\) 求精确约分分母的最小公倍数 \(L>0\)，令
\(\delta_j=\Delta^j[L f_{48}/G](1)\)（\(0\le j<96\)），定义
\[
S(k)=\sum_{j=0}^{95}\delta_j\binom{k-1}{j}.
\]
因此 \(\deg(GS)\le193+95=288\)。在 \(k=1,\ldots,289\) 的 **289 个不同正整数点**，R525_VERIFY.js 用 BigInt 检查
\[
 L D_{48}(k)=C_k^{48}G(k)S(k).
\]
左右除以正的 \(C_k^{48}\) 后均为次数不超过 288 的有理多项式，故构成多项式恒等式；不依赖有限样本对无限范围的直接外推。完整 \(L\)、96 项 \(\delta_j\)、符号值及尾部证书均保存在 R525_EVIDENCE.json。

## 尾部 Newton 系数给出严格符号

证书给出 \(S(1),\ldots,S(5)>0\)，以及 \(S(6),\ldots,S(13)<0\)；以 \(k=14\) 为原点，**全部 96 项**
\(\varepsilon_j=\Delta^j S(14)\) 严格为正。对于任意整数 \(u\ge0\)，
\[
S(14+u)=\sum_{j=0}^{95}\varepsilon_j\binom{u}{j}>0.
\]
其中 \(\varepsilon_0>0\)，其余项非负。由 \(L>0,C_k>0,G(k)>0\) 得到定理的全正整数参数结论。该结果的强度是以冻结固定 \(t\) 多项式引理为前提的**精确计算机辅助条件证明**。

## 精确计算、复现与地位

运行 \`node R525_VERIFY.js > R525_EVIDENCE.json\`，得到 \`R525_EXACT_JS_PASS\`，包含 289 项整点恒等式、20 个原始 48×48 Bareiss 整数行列式交叉检查、960 项原始 signed BRC 卷积与 ballot–Catalan 系数交叉核验，以及 96 项严格正的尾部差分。

运行 \`python R525_INDEPENDENT.py > R525_INDEPENDENT_EVIDENCE.json\`，以 Python/SymPy Berkowitz 独立计算 18 项原始 48×48 整数行列式，覆盖 \(k=5/6\)、\(13/14\) 边界，并完成 864 项 signed BRC 系数交叉核验，得到 \`R525_INDEPENDENT_PASS\`。两条检查链均使用精确整数，Python 验证属于作者侧跨实现交叉检查；独立 Driver 数学审核、原生 CLAIM/Result 均待正式办理。

本证明限定在冻结 R462 的 **signed BRC 辅助 Toeplitz 标量模型**。P000、ACTIVE 世界观及原生六维心跳世界研究输入未修改。该子式结论也不自动给出原生 X6 物理动力学或残差归因命题。

## 下一问题

一是 \(s=3,m=49\)：验证次数上界 294、98 项 Newton 系数和 295 个互异整数点，寻找全正整数符号分类及尾部证明；二是沿 R524 固定 \(k=7,8,20,21\) 的有理阶数生成函数开展主导代数根与极点相位分析，以解释跨阶数的符号变换，而非仅逐阶列证书。
