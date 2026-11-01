# PREFIX-406：六项带噪观测的稳健半正定松弛秩缺口

日期：2026-11-01。研究类别：外部辅助静态复三振幅五 Port 逆问题。作者侧精确证明与实际检查；UNREVIEWED / NOT_ADMITTED / NATIVE_REGISTER_PENDING。

来源：GLOBAL_KNOWLEDGE_V1 main@b687941eae4c219b60f62a03369de1449bd1ad23；Enterprise Math main@4d349d63a10612d9e196f49791bd5946c6dd9bba；继承 PREFIX-405（research_notes/2026-11-01_prefix405_all_noisy_exact_refutation_and_robust_nonconvexity.md）。遵循现行 P000、ACTIVE 世界观和 PORTABLE_RESEARCH_PROTOCOL；不将本模型混同于原生 X6、三维切片或 typed BRC 计算。

## 模型

原始五 Port 矩阵
\[
A=\begin{pmatrix}
4&4&0\\
0&-4&4\\
-5+3i&0&-3+i\\
-2-2i&4+4i&2+2i\\
-2&0&5+2i
\end{pmatrix},
\qquad \det A_{1:3}=-32+32i.
\]
令 \(W=A_{1:3}Y=(1,u,v)^T\)，规范化 \(I_1=1\)，去掉公共复相位。六个观测依次为
\[
I_2=|u|^2,\quad C_u=|1+u|^2,\quad I_3=|v|^2,\quad C_v=|1+v|^2,
\]
\[
I_4=|a+bu+cv|^2,\qquad I_5=|d+du+ev|^2,
\]
其中 \(a=5/2+9i/2,\ b=3/2+7i/2,\ c=4i,\ d=11/4+15i/8,\ e=5/4+9i/4\)。

所有六个读数区间均有非零宽度，设 \(\epsilon=1/10000\)：
\[
J_2=[1-\epsilon,1+\epsilon],\ J_u=[2-\epsilon,2+\epsilon],\
J_3=[0,\epsilon],\ J_v=[1-\epsilon,1+\epsilon],\
J_4=[40,42],\ J_5=[22,23].
\]
相干单一来源对应 Hermitian \(H=WW^*\succeq0,H_{11}=1,\operatorname{rank}H=1\)。对各观测行 \(r_j\)，\(F_j(H)=r_jHr_j^*\) 为实线性。半正定松弛只去掉 rank-one 要求。

## 定理：任意松弛可行点与 rank-one 来源之间存在定量谱间隙

对以上六个正宽度有理闭区间：

1. 不存在任何真实复来源 \(u,v\) 满足全部六项测量。
2. \(H_0=\operatorname{diag}(1,1,0)\) 是满足全部六个区间的 rank-two PSD 矩阵，其真实线性化读数为 \((1,2,0,1,41,709/32)\)。
3. 对**每一**个满足全部六项区间的 \(H\succeq0,H_{11}=1\)，降序实特征值满足
\[
\boxed{\lambda_2(H)>\frac{5623}{10000}=0.5623.}
\]
因此 \(H\) 到任意秩至多一矩阵的算子范数距离严格大于 \(5623/10000\)，Frobenius 距离亦如此。

### A. 松弛可行

两组规范化真实复来源 \(W_+=(1,i,0)^T\)、\(W_-=(1,-i,0)^T\)，观测分别为
\[
F(W_+)=(1,2,0,1,37,709/32),\quad
F(W_-)=(1,2,0,1,45,709/32).
\]
它们的秩一 Hermitian 提升平均恰为
\[
H_0=(W_+W_+^*+W_-W_-^*)/2=\operatorname{diag}(1,1,0).
\]
观测线性，故中点读数为 \((1,2,0,1,41,709/32)\)，全部落入六带。矩阵自身为 PSD 秩二。

### B. 严格排除 rank-one：完整连续盒的解析证书

前四项区间对于真实 \(u,v\) 强制
\[
|\Re u|\le\epsilon,\quad
999/1000<|\Im u|<1001/1000,\quad
|\Re v|\le\epsilon,\quad |\Im v|\le1/100.
\]
令 \(\sigma=\operatorname{sign}\Im u\in\{\pm1\}\)。相对基准 \((u,v)=(\sigma i,0)\)，第四 Port 复振幅的一范数偏差至多
\[
D\le5\cdot11/10000+4\cdot101/10000=459/10000.
\]
\(\sigma=+1\) 时基准振幅为 \(-1+6i\)，平方模37、复一范数7；\(\sigma=-1\) 时为 \(6+3i\)，平方模45、一范数9。对 \(M=7\) 或9有 \(|\Delta I_4|\le2MD+D^2\)，于是
\[
|I_4-37|\le64470681/10^8\quad(\sigma=+1),
\qquad |I_4-45|\le82830681/10^8\quad(\sigma=-1).
\]
这两个完整值域与 \(J_4=[40,42]\) 都严格不交，最小排除裕量为
\[
\boxed{217169319/10^8>0.}
\]
这证明全部 rank-one 来源不可能；不是抽样失败。

### C. 对所有 PSD 可行矩阵的谱间隙

任取满足六带的 PSD 矩阵 \(H\)，记 \(r=H_{22},s=H_{33},H_{12}=x+it\)。由 \(I_2,I_3,C_u\) 可得
\[
|r-1|\le\epsilon,\quad0\le s\le\epsilon,\quad |x|\le\epsilon.
\]
PSD 主子式给出
\[
|H_{13}|\le\sqrt{s}\le1/100,\quad
|H_{23}|\le\sqrt{rs}<1001/100000.
\]
精确系数是
\[
a\bar b=39/2-2i,\quad a\bar c=18-10i,\quad b\bar c=14-6i
\]
且 \(|a\bar c|^2=424<21^2,\ |b\bar c|^2=232<16^2\)。直接展开有
\[
I_4=53/2+(29/2)r+16s+
2\Re\big((39/2-2i)H_{12}+(18-10i)H_{13}+(14-6i)H_{23}\big).
\]
因此
\[
|I_4-(41+4t)|
< (29/2+16+39)\epsilon+42/100+32\cdot1001/100000
=74727/100000<3/4.
\]
由 \(40\le I_4\le42\)，得 \(|t|<7/16\)，并且
\[
|H_{12}|\le|t|+|x|<7/16+\epsilon.
\]
令 \(B\) 为 \(H\) 左上角 \(2\times2\) Hermitian 主子矩阵，则
\[
\lambda_{\min}(B)\ge\min(1,r)-|H_{12}|
>1-\epsilon-7/16-\epsilon=9/16-2\epsilon=5623/10000.
\]
Hermitian 特征值交错给出 \(\lambda_2(H)\ge\lambda_{\min}(B)\)。对任意秩至多一的 \(R\)，\(\ker R\) 与 \(H\) 前两个特征子空间有非零交，所以 \(\|H-R\|_{\rm op}\ge\lambda_2(H)\)。证毕。

## 验证、科学边界与下一步

实际执行的符号检查器在 SymPy 1.14.0、Python 3.13.5 下从原始矩阵重新推导第4、5行，并证实所有精确系数、两组读数、PSD 中点、两项严格有理数界；返回 PASS_PREFIX406_ROBUST_PSD_RANK_GAP。独立 Python Fraction 复数有理对检查返回 PASS_PREFIX406_INDEPENDENT_FRACTION_PSD_RANK_GAP。证明全称性来自上述解析论证，程序负责准确算术核验。

与已知 PhaseLift 思想对照：Candès–Strohmer–Voroninski, PhaseLift: Exact and Stable Signal Recovery from Magnitude Measurements via Convex Programming, Communications on Pure and Applied Mathematics 66 (2013), DOI 10.1002/cpa.21432，https://arxiv.org/abs/1109.4499 。PSD 提升和松弛本身并非新发明；该文有特定随机采样成功前提，本确定性 Port 布置不构成对其恢复定理的反驳。该明确 Port 系统的六正宽度带噪松弛假阳性和统一第二特征值有理下界，是本轮新得到的项目内精确结果。未经全面文献查重，不作世界首创宣称。

BRC 只借用其来源/支路与后续观察保真原则：\(H_0\) 是两条真实相干来源的混合，却不对应单一复来源；无 typed BRC 运算、原生 X6 嵌入或动态不变量证明。

下一问题 PREFIX-407：开发可回放的谱间隙/主子式排除证书生成器，研究保留 \(I_3=0\) 的退化观察族中的有限 algebraic YES/NO 判定，并确定噪声临界半径。PREFIX-405 的普适全噪声边界-only YES 算法仍未实现。

保存分类：ordinary research artifact / AUTHOR_SIDE_EXACT_VERIFIED / UNREVIEWED / NOT_ADMITTED / NATIVE_REGISTER_PENDING。原生服务 research_authority_granted=false；Owner 列表实际调用 CONTROL_QUOTA，未取得或借用正式 CLAIM/Result/Review。