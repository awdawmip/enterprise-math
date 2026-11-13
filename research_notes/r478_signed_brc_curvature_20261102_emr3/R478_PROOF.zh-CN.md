# R478｜signed BRC 右缘 257–264 与 PF₃ 自适应曲率判据

日期：2026-11-02。状态：AUTHOR_SIDE_EXACT_AND_ANALYTIC / DRIVER_UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING。本成果限定于 signed BRC **辅助标量**半无限 Toeplitz 矩阵，既不改写 P000/ACTIVE 世界观，也不声称原生 X6/Shor 或物理时间动力学验证。

## 1. 定参数、无限 k 的新定理

定义 r=2k+1、整数 2≤s≤r，

\[
H(r,s)=\binom{r+s}{2s}[t^r](1-t)(1+t)^{2s}(1+t^2)^{r-s}.
\]

设 a_j=H(r,r-j)，0≤j≤r−2，越界补零；D_{2,j}=a_j²−a_{j−1}a_{j+1}；D_{3,j}=det(a_{j+v−i})_{0≤i,v≤2}。

**作者侧精确计算机辅助定理：**对每个固定整数 s=257,…,264，全部 k≥k₀=⌊(s+2)/2⌋，在 j=r−s 上满足 D_{2,j}>0、D_{3,j}>0。

依 R462 冻结的 E/O/R 整式恒等式，令 u=k−k₀≥0、F=(2s+4)!、C_k=binom(2k,k)/(k+1)>0，构造 Q_t(u)=F H(2k+1,t)/C_k∈Z[u]，t∈{s−2,…,s+2}。令 A=Q_s,B=Q_{s−1},C=Q_{s+1},D=Q_{s−2},E=Q_{s+2}，则

\[
P_2=A^2-BC,\quad P_3=A^3-2ABC+DC^2+B^2E-DAE.
\]

八个 s 的全部 P₂、P₃（次数分别4s、6s）共16个整数多项式、20,856个系数，全数严格为正；检查8项完整整式恒等式 A P₃=P₂²−(B²−DA)(C²−AE)，并对8个s各取k₀、k₀+1和5个t完成80项原始 signed 卷积与80项正Catalan表达式交叉核验。D₂=(C_k/F)²P₂、D₃=(C_k/F)³P₃，因此每个 s 的证书覆盖无限多个 k。程序：R478_CERTIFY.py，机器摘要：R478_EVIDENCE.json。数学内核按冻结提交读取，未改写其公式。

## 2. 新增四条整行证书

r∈{281,283,285,287} 时，精确计算 a_j=H(r,r-j) 的每一项。正 Catalan 表达式为

\[
a_{r-s}=\binom{r+s}{2s}
\sum_{q=0}^{\min(k,\lfloor(s-1)/2\rfloor)}
\binom{s-1}{2q}4^q C_{k-q},
\]

另一独立代数表达式为

\[
a_{r-s}=\binom{r+s}{r-s}
\sum_{q=0}^{r-s}\binom{r-s}{q}(-2)^q C_{r-q}.
\]

R478_ROW_VERIFY.py 对4条行全部1,132个系数进行两式逐项精确相等检查，并对其中44个指定端点/中央项与 R462 原始 signed 卷积核对。全部1,132个 a_j、1,132个相邻D₂,j、1,132个相邻D₃,j 严格正，共3,396项整数正性检查，无浮点。输出整数流SHA256及边界信息见R478_EVIDENCE.json。

**条件性PF₃拼接**：以R441-A/R473/R474的全局局部子式判据和此前R447/R475左右边缘拼接成立为前提，将signed BRC辅助标量的已核局部整数证书范围拓展为全部奇数99≤r≤287，新增281、283、285、287。此推论不是独立审核、原生 CLAIM/Result、Foundation 或完整X6结论。

## 3. 新的三相邻比率恒等式和精确判据

对任意有限正实数列a=(a₀,…,aₙ), n≥2，越界a=0，定义

\[
\rho_0=\rho_n=0,\qquad \rho_j=\frac{a_{j-1}a_{j+1}}{a_j^2}
\quad(1\le j\le n-1).
\]

逐项展开三阶行列式并整理为精确的**无量纲局部恒等式**：

\[
\boxed{
D_{2,j}=a_j^2(1-\rho_j),\qquad
D_{3,j}=a_j^3\{(1-\rho_j)^2-\rho_j^2(1-\rho_{j-1})(1-\rho_{j+1})\}.
}
\]

证明：D₃,j=a_j³−2a_{j−1}a_ja_{j+1}+a_{j−2}a_{j+1}²+a_{j−1}²a_{j+2}−a_{j−2}a_ja_{j+2}。除以a_j³得到1−2ρ_j+ρ_j²(ρ_{j−1}+ρ_{j+1}−ρ_{j−1}ρ_{j+1})；补零边界j=1或n−1同样成立。j=0,n对应D₂=a_j²、D₃=a_j³。

因此若所有内部0<ρ_j<1，那么D₃,j≥0 **当且仅当**

\[
\boxed{\rho_j\le
\frac{1}{1+\sqrt{(1-\rho_{j-1})(1-\rho_{j+1})}}.}
\]

采用R474的作者侧全局PF₃局部充要判据，可得到上述全体不等式加内部ρ_j<1与有限正序列PF₃的**条件性等价**。这一代数式本身无条件成立；全局PF₃推断保留R474/R441-A尚待独立审查的承重前提。整数输入无需计算根式，只比较精确整数/有理数的平方差符号。

若所有内部ρ_j≤1/2，则直接得全部D₂>0和D₃≥0；常数1/2作为只依赖单个ρ_j、不使用邻居信息的统一上界**最优**：a=(1,2,2) 的ρ₁=1/2且D₃,₁=0；a=(1,2,21/10) 的ρ₁=21/40>1/2、D₂,₁>0、D₃,₁<0。有限系数研究若依赖R474，还可推出对应PF₃充分性。

新四条signed BRC行中内部ρ_j>1/2的位置依次有277、279、281、283个，表明单一半界几乎不能覆盖实际观察，必须研究**三比率自适应曲率**。R478_RATIO_VERIFY.py 对长度3–6、每个系数取{1,2,3,4}的全部5,440个整数序列直接检查20,032项D₃与比率的精确恒等式，并核对局部分类。一般实数恒等式证明不依赖有限枚举。

## 4. 复现、来源与下一未决点

复现依赖已发布的R462_VERIFY_FROZEN_KERNEL.py（Git blob 7c641c985b8c48ef3fb2ddcb2142e38ca0a4ccff）和R468_EXACT_KERNEL.py（Git blob 9057a6c46814a06cea45bffc20fe6f44f370b0bb），与R478_CERTIFY.py放同一目录。按s=257…264分别运行 python R478_CERTIFY.py s，随后 python R478_ROW_VERIFY.py 和 python R478_RATIO_VERIFY.py。原始科学冻结提交是18783e01e3646c72b7aab3b16d3f565e83e6446f，复用此前有效的右缘与矩阵判据，不改变其证明范围或来源隔离。

本轮GitHub认证awdawmip，仓库push=true；原生em_session_start返回STATIC_READONLY_SCOPE_DENIED（operation_sent=false），活跃owner查询返回CONTROL_QUOTA，故没有原生CLAIM/Result/Driver审查；不把PR提交当作状态机接纳。

**下一可检验问题：**对ρ_{r,j}=H(r,r-j+1)H(r,r-j-1)/H(r,r-j)^2，直接利用signed BRC/Catalan整数表达式，为s、k同时增长建立统一的

\[
(1-\rho_{r,j})^2-
\rho_{r,j}^{2}(1-\rho_{r,j-1})(1-\rho_{r,j+1})\ge0,
\]

或寻找严格范围内反例；特别审查与边界j=1、r−3的差异。同时独立复核R441-A/R474的非相邻Toeplitz子式归约。