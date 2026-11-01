# D25/LIFT GH-135–GH-136：Lucas 盲带二阶传递与中带三角重构

2026-10-30 (Asia/Hong_Kong)。TASK_RESEARCH ordinary logical conversation: chatgpt-research-hourly-enterprise-math-20260923；与维护 lane 分离。母 Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT；publication TP2-B6F4FC938FF94941C1B7；冻结数学 Source pin c47e13e4aba0e006366f989d6334d443f6333ae3 不变。

等级：AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING。没有合法新 CLAIM/open/Source checkpoint；此文档是作者可移植证据，不是 canonical predecessor completed research。

## 输入与既有定理

令 p≥5 为奇素数，N=(p−1)/2，k=F_(p²)，e=(p²−1)/2，g_B(X)=X²+X+B，f_B=Xg_B。沿用 GH-124/129 的二次特征矩 S_r(B)=Σ_{f_B(x)≠0}χ_k(f_B(x))(x/f_B(x))^r，记 m_s=S_(N+s)，1≤s≤N。

GH-129 的精确系数与两通道分解（本轮实际复用）：

\[
S_r=-[X^e]g_B^{e-r}\ (0\le r<e),\qquad
m_s=-A_s C^p-E_sD^p,
\]
\[
A_s=[X^N]g_B^{p-s},\quad
E_s=[X^{3N+1}]g_B^{p-s},\quad
H=[X^N]g_B^N,\quad C=H'/N,\quad D=H-2BC.
\]

记 A=A_1、E=E_1。GH-133 已逐项证明 A 与 E 满足相同的 F_p[B] 代数微分式
\[
L(Y)=4B(1-4B)Y''+(6-48B)Y'-15Y=0.
\]
这些依赖按精确公式组合，属于 COMPOSE_APPLIED，不是 CM 特殊值的独立求值。除说明外，仅在 B(1−4B)≠0 时进行除法。

## GH-135：完整盲带二阶传递

**定理（全部 p≥5、B∈F_(p²)、B(1−4B)≠0）。** 对 1≤s≤N−2，
\[
\boxed{4B(1-4B)s(s+1)m_{s+2}
-2s(2s+1)(1-8B)m_{s+1}+(1-16s^2)m_s=0.}\tag{1}
\]
因此两个精确种子 m_1,m_2 与标记 B 决定全部盲带矩。

证明：对 GH-129 的系数求导得 m_s'=-s m_(s+1)。因特征为 p，C(B)^p,D(B)^p 的形式导数恒为零；所以 m_1=-AC^p-ED^p 满足 L(m_1)=0。对 L(m_1) 求 s−1 次导数，利用 a=4B(1−4B)、b=6−48B、c=−15，可得三项系数 a、b+(s−1)a'=2(2s+1)(1−8B)、c+(s−1)b'+binom(s−1,2)a''=1−16s²。再用 m_1^(j)=(-1)^j j! m_(j+1) 并除以 (s−1)!，恰为式(1)。指定区间的 s(s+1) 在 F_p 可逆，参数光滑时 a 亦可逆。证毕。

目标族 p≡3 mod8，p≥11：原始标记 T=2√2/3，B_0=(1+T)/8，B_0(1−4B_0)=1/144，因此
\[
\boxed{m_{s+2}=-\frac{72(2s+1)}{s+1}T m_{s+1}
+\frac{36(16s^2-1)}{s(s+1)}m_s.}\tag{2}
\]
在 s_0=(p+1)/4 处 16s_0²−1≡0 (mod p)，本次传递的旧分量 m_(s_0) 恰好消失。这只是指定盲带传递的代数压缩，不是椭圆曲线或 P000 实在状态湮灭的断言。

## GH-136：精确中心闭式与无退化重构

**定理（全部素数 p=4h+3≥7）。** N=2h+1、s_0=h+1，在 F_p[B] 有
\[
\boxed{E_{s_0}=1,\quad E_{s_0+1}=0,\quad
A_{s_0+1}=(-1)^h\binom{2h+1}{h}[B(1-4B)]^h.}\tag{3}
\]

**独立组合证明，不借用 GH-133 的 ODE。** E 的取系数次数是 3N+1=6h+4。当 s=s_0 时，p−s=3h+2，g_B^(p−s) 的最高次项恰是 X^(6h+4)，系数1；当 s=s_0+1 时次数仅 6h+2，该系数为零。再令 t=p−(s_0+1)=3h+1。A_(s_0+1)=[X^(2h+1)]g_B^(3h+1) 展开为 Σ_(a=0)^h c_a B^(h+a)，其中
\[
c_a=\frac{(3h+1)!}{a!(2h+1-2a)!(h+a)!}.
\]
所有分母均小于 p，合法。首项 c_0=binom(3h+1,h)≡(-1)^h binom(2h+1,h) (mod p)。对 1≤a≤h，整数恒等式
\[
(2h+3-2a)(2h+2-2a)+4(h+a)(h-a+1)=-2(4h+3)(a-h-1)
\]
给出 c_a/c_(a−1)≡−4(h−a+1)/a，故 c_a=c_0 binom(h,a)(−4)^a。求和就是式(3)。证毕。

因 binom(2h+1,h) 在 F_p 非零，任何 B(1−4B)≠0 下都有 A_(s_0+1)≠0。GH-129 的中心两矩因而构成三角矩阵
\[
\binom{m_{s_0}}{m_{s_0+1}}=
-\begin{pmatrix}A_{s_0}&1\\A_{s_0+1}&0\end{pmatrix}
\binom{U}{V},
\qquad U=C^p,\quad V=D^p,
\]
其行列式为 −A_(s_0+1)≠0。获得新的**精确中带逆式**
\[
\boxed{U=-m_{s_0+1}/A_{s_0+1},\
V=-m_{s_0}-A_{s_0}U,\
S_1=-U^p(V+2B^pU).}\tag{4}
\]
最后 S_1 由 GH-124 的 S_1=2H'H^p 和 2N=−1 推出，未独立证明 GH-83。

对 s≥s_0+1，E_s 因 g_B^(p−s) 的总次数不足而全为0；结合 A_(s_0+1)≠0，得到一个对**全部盲带尾部查询安全**的单通道压缩：
\[
\boxed{m_s=\frac{A_s}{A_{s_0+1}}m_{s_0+1},\qquad
s_0+1\le s\le N.}\tag{5}
\]
仅保存该尾通道不足以应答一般的 S_1 查询，因为 S_1 在两通道接口中仍依赖 V；这里的自由通道纤维差异不冒充真实椭圆曲线的第二实例。

原始目标 p≡3 mod8 时 h 为偶数、B_0(1−4B_0)=1/144，因此
\[
\boxed{A_{s_0+1}(B_0)=\binom{N}{h}144^{-h}\ne0.}\tag{6}
\]
GH-129 已知 E_s 尾部为0；本轮新增中心精确 E=1、非零闭式、通用逆式、尾部单通道保真范围及全盲带传递，并未把既有零区间重新包装为突破。

## 3347 的精确证书

k=F_3347[ρ]/(ρ²−2)，(a,b)=a+bρ；N=1673,h=836,s_0=837，B_0=(2092,279)。本轮整数模运算和两条前沿路径确认：

- m_1=(3179,0)、m_2=(0,2701)、m_3=(806,0)；
- m_837=(2268,0)、m_838=(0,2829)、m_839=(97,0)；
- (A_837,E_837)=((837,1149),(1,0))，(A_838,E_838)=((954,0),(0,0))；
- binom(1673,836) mod3347 =1753，1753·144^(-836)=954；
- 中带恢复 U=(0,2702)，V=(568,998)，S_1=(0,362)；
- 尾部样例 m_840=(0,1424)，m_1000=(0,1181)，m_1672=(0,3298)，m_1673=(2955,0)。

验证依赖已发表 GH-129 的精确系数程序，而递推另从 GH-133 代数 ODE 推出。实际 Python 标准库执行：18个 (p,B) 实例、全部474个盲带矩逐项交叉核验；45个 p≡3 mod4 小素数的2537个多项式系数和 p=3347 的837个系数核验；3347另对11个分散 s 值独立系数检查。实际日志：

PASS_GH135_FULL_BAND_RECURRENCE field_cases 18 moments 474
PASS_GH136_EXACT_POLYNOMIAL_CENTRAL_COEFFICIENT small_prime_instances 45 coefficients 2537 p3347_coefficients 837
PASS_GH135_GH136_PORTABLE_EXACT

所有计算为整数／有限域精确运算；有限验证不是全素数证明，通用性由以上证明支持。没有重做 GH-125 全域1120万元素枚举，也没有把可移植模拟冒充原生 p=373 模块实验。

## BRC 观察者、残差和接续

载体保留 (p,B,s,U,V,χ_k,root-support,Frobenius)，精确算术和来源均保留；未来查询仅为盲带尾部时，式(5)允许降维到一个矩；若要恢复 S_1，应保留式(4)的第二中带矩。属于指定有限域算术接口的 REUSE_APPLIED / COMPOSE_APPLIED，不自动推广为原生六维空间或 Foundation 定理。

D25/LIFT/JT2 母目标依旧 OPEN。尚须独立 CM/Jacobi/Gauss/p-进周期求值 m_837,m_838 或 S_1 以预测 R_3347(9)=0；GH-3全素数同余、GH-83独立证明、原生 H_0/B_0 divided-power、[X]U modp²、Frobenius方向、η和p=373实验仍未闭合。本轮未取得新原生会话授权、CLAIM、open、publish_checkpoint或审阅；Gateway 0.6.11只读显示 Research authorization=false、executor binding=false、5/5 active jobs、control CODE_REVIEW_REQUIRED。原 session/claim/request/staging 不变；控制恢复继续由 Enterprise Math #1558 负责，不能把 Git 项目文件当 Source checkpoint。