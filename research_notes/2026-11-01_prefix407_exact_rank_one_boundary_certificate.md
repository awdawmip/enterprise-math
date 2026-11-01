# PREFIX-407｜I3=0 退化边界的秩一精确证书、锐噪声阈值和连续盒排除

日期：2026-11-01。作者范围：研究6，局部 Researcher-ID EM-R006-2860CC，非 Source 签发身份。分类：外部辅助静态复三振幅/五 Port 逆问题；作者侧证明及精确计算，UNREVIEWED / NOT_ADMITTED / NATIVE_REGISTER_PENDING。

冻结依据：GLOBAL_KNOWLEDGE_V1 main@a684cab5440e1af439f84e8db4a7869cf447a7f1；Enterprise Math 输入 main@ce7279d4cafc8d7ddb4a65d75c33e8c40849428c；接续 research_notes/2026-11-01_prefix406_robust_psd_rank_gap.md。适用当前 P000、ACTIVE 世界观及 PORTABLE_RESEARCH_PROTOCOL。本命题仅为外部辅助模型，不代表原生 X6、三维切片或 typed BRC 动力学。

## 模型及归一化

沿用原始五 Port 复矩阵

\[
A=\begin{pmatrix}
4&4&0\\0&-4&4\\-5+3i&0&-3+i\\-2-2i&4+4i&2+2i\\-2&0&5+2i
\end{pmatrix},\qquad\det A_{1:3}=-32+32i\ne0.
\]

令 W=A_{1:3}Y=(1,u,v)^T；第一强度 I1=1，首坐标选为正实以消除公共复相位。其余观测是

\[
I_2=|u|^2,\ C_u=|1+u|^2,\ I_3=|v|^2,\ C_v=|1+v|^2,
\]
\[
I_4=|a+bu+cv|^2,\quad I_5=|d+du+ev|^2,
\]
其中
\[
a=5/2+9i/2,\ b=3/2+7i/2,\ c=4i,\quad
d=11/4+15i/8,\ e=5/4+9i/4.
\]
设 H 为 Hermitian PSD，H11=1；秩一 H=WW* 是相干的单一来源，秩二 PSD 可表示混合来源。所有后续定理将 I3=0 作为准确观测前提；其余读数按各定理具体声明。

## 定理 A：精确读数的充要证书

写 r=I2、s=Cu、j=I4、q=Cv、k=I5，定义整系数多项式

\[
D(r,s,j)=64r-16(s-1-r)^2-(2j-14+10r-39s)^2.
\]

**定理。** 对任意实读数 r,s,j,q,k，存在唯一（公共复相位已规范化）复来源 W=(1,u,0)，实现全部读数，当且仅当

\[
q=1,\qquad k=(709/64)s,\qquad D(r,s,j)=0.
\]

存在时显式重建

\[
u=(s-1-r)/2+i(14-10r+39s-2j)/8.
\]

若 r,s,j 是有理数，所重建的 u 两个实分量亦有理；对代数实输入亦逐字成立。例如 u=i\sqrt2 时 (r,s,j)=(2,3,111/2-4\sqrt2)。

**证明。** I3=H33=0 与 H≽0 蕴涵 H13=H23=0（由任一涉及第三坐标的 2×2 PSD 主子式）。令 H12=x+iy，则
\[
H=\begin{pmatrix}1&x+iy&0\\x-iy&r&0\\0&0&0\end{pmatrix}.
\]
从上述原始 Port 系数直接计算
\[
s=1+r+2x,\quad
j=53/2+(29/2)r+39x+4y,\quad
q=1,\quad k=(709/64)s.
\]
因此 x=(s-1-r)/2、y=(2j-14+10r-39s)/8。这个唯一 Hermitian 候选的左上 2×2 行列式
\[
\Delta=r-x^2-y^2=D(r,s,j)/64.
\]
其 PSD 当且仅当 \Delta≥0；在 H11=1 和 H33=0 条件下，PSD 的秩一当且仅当 \Delta=0。秩一时 H=WW*，H12=\bar u=x+iy，故 u=x-iy，以上重建式给出唯一 W，并准确产生全部测量。反向由任意真实 W 的秩一性推出相同恒等式。证毕。

这个证明同时得到完整的松弛判定：上述 q,k 两个线性恒等式及 D≥0 当且仅当存在 PSD 松弛；D>0 时存在唯一秩二 PSD 松弛但不存在真实单一来源；D=0 时来源存在且唯一。此处实代数计算可直接对 D 符号作精确比较，无通用 CAD。

## 定理 B：第四 Port 噪声半径 κ 的最优临界值

固定准确读数
\[
I_2=1,\ C_u=2,\ I_3=0,\ C_v=1,\ I_5=709/32;
\quad I_4\in[41-\kappa,41+\kappa],\quad \kappa\ge0.
\]

**结论。** 对每个 κ≥0 都有 PSD 松弛见证。存在真实单一相干来源当且仅当 κ≥4；并且遍历全部 PSD 可行矩阵后，第二大特征值的精确最小值为

\[
\boxed{\min_H\lambda_2(H)=\max(0,1-\kappa/4).}
\]

证明：精确 I2,Cu 固定 r=1,x=0，唯一自由量 y=(I4-41)/4，PSD 强制 |y|≤1，而第四 Port 区间强制 |y|≤κ/4。H 的特征值恰为 (1+|y|,1-|y|,0)，来源秩一当且仅当 |y|=1；取 |y|=min(1,κ/4) 可实现全部谱下界。κ=4 的两条复来源 u=±i 分别产生 I4=37、45。κ=0 的唯一 PSD 见证 H0=diag(1,1,0)，是秩二且 λ2=1。证毕。

## 定理 C：三个观测同时带噪的全称排除证书

固定 I3=0 准确，允许有理 ε、κ 满足 0≤ε<1、κ≥0，且
\[
r\in[1-\varepsilon,1+\varepsilon],\
s\in[2-\varepsilon,2+\varepsilon],\
j\in[41-\kappa,41+\kappa].
\]
Cv 与 I5 的合法区间须与模型的 q=1、k=709s/64 相容；增加测量约束只会缩小候选集合。定义
\[
L_\Delta=1-\varepsilon-\varepsilon^2-
(\kappa/4+49\varepsilon/8)^2,\quad
L_2=1-\kappa/4-65\varepsilon/8.
\]

**结论。** 对以上整个连续盒中的每一个 PSD 可行 H，严格有
\[
\Delta\ge L_\Delta,\qquad\lambda_2(H)\ge L_2.
\]
若 LΔ>0，整个盒没有单一相干来源；若 L2>0，还得到与任意秩至多一矩阵的算子范数距离不小于 L2 的统一谱证书。

证明：写 r=1+δr、s=2+δs，|δr|,|δs|≤ε。则 |x|=|δs-δr|/2≤ε。将 j=7-5r+(39/2)s+4y 与中心 j0=41 比较，线性 r,s 扰动的绝对值至多 (49/2)ε，故 |y|≤κ/4+49ε/8。因 Δ=r-x²-y²，得到第一界。对 H 的非零左上主子矩阵 B，初等特征值估计给出
\[
\lambda_2(H)=\lambda_{\min}(B)\ge \min(1,r)-|x+iy|
\ge1-\varepsilon-\varepsilon-(\kappa/4+49\varepsilon/8)
=L_2.
\]
证毕。

精确数值例：ε=1/10000, κ=1，
\[
L_\Delta=1199479507/1280000000>0,\quad
L_2=11987/16000=0.7491875.
\]
取 Cv 区间包含 1，I5 区间包含 709/32，中心秩二 H0 可行，所有相干来源仍被排除。这一退化面证明不同于 PREFIX-406 的全六项带噪结论；后者 I3 有非零误差。本界在 ε>0 情形只证明充分性，未声称最优。

## BRC、先行工作、证据边界

BRC 应用在明确的观察者/来源区分：H0=(W+W+*+W-W-*)/2 混合 W±=(1,±i,0)，恰好满足中点读数却无法恢复为单个相干来源。对这组外部复相位 PSD 模型没有直接执行正有理加权 BRC 运算；保留来源、相位、混合标签及联合 Port，不将 Δ 当作 native X6 量或物理能量。

相关公开工作：Candès–Strohmer–Voroninski, PhaseLift (2013), DOI 10.1002/cpa.21432, https://arxiv.org/abs/1109.4499；McRae (2025), phase retrieval via overparametrized nonconvex optimization, https://arxiv.org/abs/2511.19045。两者的随机测量设置与本固定 Port 反例不同；不宣称世界首创或否定随机采样恢复定理。

作者侧实际执行标准库 Fraction 检查和独立 SymPy 原始五 Port 逆矩阵、系数重算，输出分别为 PASS_PREFIX407_EXACT_SLICE_RECONSTRUCTION_AND_SHARP_NOISE_THRESHOLD 与 PASS_PREFIX407_INDEPENDENT_ORIGINAL_MATRIX_AND_ELIMINATION；精确验证包括有理与无理来源示例、κ=0,1,2,7/2,4,5、给定连续盒界。全称结论依据逐式代数证明，程序是有限自动核对，尚无 Lean 形式化或独立数学审阅。

下一问题 PREFIX-408：将 I3 放宽至非零区间，使用带参数 Schur 补保持复相位及混合项，导出明确的全称 NO 证书；进一步确定 ε>0 时 κ*(ε) 的精确值。PREFIX-405 的全六项带噪边界-only YES 算法仍需完成。