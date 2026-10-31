# R426｜signed BRC 辅助行的全参数非实根定理

日期：2026-10-31。级别：AUTHOR_SIDE_EXACT / DRIVER_UNREVIEWED / NOT_ADMITTED。沿用 R425 的带符号辅助组合对象，不将标量读出等同于原生 X6 状态。P000 和 ACTIVE 世界观保持不变。

## 精确命题

对整数 r≥2，0≤s≤r 定义

\[
\delta_{r,s}=[t^r](1-t)(1+t)^{2s}(1+t^2)^{r-s},\qquad
H_{r,s}=\binom{r+s}{2s}\delta_{r,s},\qquad
P_r(x)=\sum_{s=2}^r H_{r,s}x^{s-2}.
\]

**R426-A（完全解析、无限参数）：每个 r≥4 的 P_r 均为严格正系数多项式，却不能具有全部实根。** 相反 P_2=2、P_3=5+5x，故在 r≥2 中，行多项式实根性恰当且仅当 r∈{2,3}。通过有限非负系数序列的 Aissen–Schoenberg–Whitney 定理，全部 r≥4 的行系数段均不是 PF∞。此结论不依赖 R425 的全域 Turán 断言是否被独立接纳。

**R426-B（最小 PF₃ 反例）：** r=4 时 (H_{4,2},H_{4,3},H_{4,4})=(30,28,14)，其 2×2 中心判别为 28²−30·14=364>0，但如下 Toeplitz 3×3 子式严格为负：

\[
\det\begin{pmatrix}28&14&0\\30&28&14\\0&30&28\end{pmatrix}=-1568.
\]

因此严格的局部二阶 Turán 性质不足以推出三阶 Toeplitz 总非负。R426-B 没有将 r=4 的 PF₃ 反例推广为其他 r 的 PF₃ 结论。

## 原始 signed 卷积与 Catalan 核的独立推导

保留 (1−t) 的有符号支路。由于 (1+t)^2=(1+t²)+2t，对全部 r≥s≥2 有：

\[
\delta_{r,s}=\delta_{r,s-1}+2\delta_{r-1,s-1}.
\tag{1}
\]

对于 s=1，直接用 (1−t)(1+t)²=1+t−t²−t³ 得 δ_{2k,1}=0，以及
δ_{2k+1,1}=\binom{2k}{k}-\binom{2k}{k-1}=Cat_k。
因此（对 r≥s≥1）：

\[
\boxed{\delta_{r,s}=[z^r]\,z(1+2z)^{s-1}C(z^2)},\quad
C(u)=\sum_{j≥0}\operatorname{Cat}_j u^j.
\tag{2}
\]

s≥2 且 r≥s 时，式(2)系数严格为正：若 r−1 偶数，取 j=0 与 Cat_{(r−1)/2}；若 r−1 奇数，取 j=1 与 Cat_{(r−2)/2}。故 H_{r,s}>0、deg P_r=r−2。

## Newton 不等式和全部偶数行

如果 P_r 的全部零点为实数，正系数使这些根均为负，Newton 不等式要求 a_j/\binom{n}{j} 对数凹，其中 n=r−2、a_j=H_{r,j+2}。尤其 j=1 要求：

\[
(r-3)H_{r,3}^2\ge 2(r-2)H_{r,2}H_{r,4}.
\tag{3}
\]

对于 r=2k、k≥2，式(2)逐项给出：

\[
(\delta_{2k,2},\delta_{2k,3},\delta_{2k,4})
=Cat_{k-1}\left(2,4,6+\frac{4k}{2k-3}\right).
\]

精确二项式比值约分：

\[
\frac{H_{2k,3}^2}{H_{2k,2}H_{2k,4}}
=\frac{112(k-1)(2k+3)}{15(k+2)(8k-9)}.
\tag{4}
\]

但式(3)要求此比值至少达到 4(k−1)/(2k−3)。将正分母通分，阈值严格大于式(4)等价于

\[
4(k-1)(8k^2+105k-18)>0\quad(k≥2).
\]

所以全部偶数 r≥4 违反实根性的必要条件。

## 全部奇数行与唯一漏点

对于 r=2k+1，k≥2，令 u=(k+1)/(2(2k−1))；式(2)给出

\[
(\delta_{2k+1,2},\delta_{2k+1,3},\delta_{2k+1,4})
=Cat_k(1,1+4u,1+12u).
\]

从而

\[
\frac{H_{2k+1,3}^2}{H_{2k+1,2}H_{2k+1,4}}
=\frac{28(k+2)(4k+1)^2}{15(k-1)(2k+5)(8k+5)}.
\tag{5}
\]

式(3)要求其至少为 (2k−1)/(k−1)。二者反向比较清除正分母，精确得到多项式

\[
F(k)=15(2k-1)(2k+5)(8k+5)-28(k+2)(4k+1)^2
=32k^3+140k^2-476k-431.
\]

F(3)=265>0，F(k+1)−F(k)=96k²+376k−304>0 对 k≥3 成立。所以全部奇数 r≥7 违反必要条件。

余下 r=5 的正系数完整为 (70,168,126,42)。虽然 j=1 必要不等式没有失败（左减右为 +3528），但 n=3、j=2 时 Newton 不等式要求

\[
2\cdot126^2\ge 6\cdot168\cdot42,
\]

左减右恰为 −10584<0。这完成全部 r≥4 的解析证明。r=2,3 的列式直接从原始系数计算，给出充要分类。

## 来源、校验、学术范围与下一问题

精确复核 R426_VERIFY.py 用 Python 标准库整数/Fraction：4≤r≤256 全部重算原始 signed 系数的 s=2,3,4，核对偶/奇 Catalan 公式、两个比值和 Newton 违例；4≤r≤48 对全部 2≤s≤r 核对原始卷积与式(2)并检查严格正性；另核对 r=4 的 PF₃ 子式与 r=5 的 j=2。运行结果为 R426_EXACT_PASS 256 1125 759 253 253 1125 r4_pf3 -1568，详细结构化输出见 R426_EVIDENCE.json。无限参数结论由上面的整式不等式证明，而非有限枚举推断。

外部背景参考：Brändén 与 Leite，Totally nonnegative matrices, chain enumeration and zeros of polynomials，Advances in Mathematics 487 (2026)，§4，DOI https://doi.org/10.1016/j.aim.2025.110760（PF∞/实根性关系）；标准 Newton 必要不等式也见 https://arxiv.org/abs/2408.09152 。这些文献不构成对本稿新 signed BRC 运算的独立审阅。

固定读取的来源快照：GLOBAL_KNOWLEDGE_V1 main@4b0f5f945fbaee76de9800c6cabf24eb1812fb3d；Enterprise Math main@220645478485d6379c23fcc51b4ea25b8a319981；上游 R425 作者侧 Draft PR #1708@ca57161eb36c96ece7028145907342155ca9bd8b。原生 owner 查询在本轮返回 CONTROL_QUOTA、DIRECTED_RESEARCH profile 的 authority_granted=false；不伪称正式 CLAIM、Result、独立 Driver Review 或接纳。

下一最小问题：在 r≥5 的正数段上，逐个检查**全部** 3×3 Toeplitz 子式（不是只检查主子式）。寻找最小严格负例或证明统一 PF₃；R426 的 Newton 反例仅推翻实根/PF∞，不推翻 r≥5 的 PF₃ 候选。原始十二签名支路与原生 X6 的观察者、未来操作保真映射仍需单独研究。