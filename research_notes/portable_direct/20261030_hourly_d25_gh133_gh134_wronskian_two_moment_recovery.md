# D25/LIFT GH-133–GH-134：通用 Wronskian 非退化与两项字符矩恢复

2026-10-30（Asia/Hong_Kong）；研究逻辑会话 chatgpt-research-hourly-enterprise-math-20260923。作者侧数学成果：AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING。母任务 RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT，publication TP2-B6F4FC938FF94941C1B7；冻结科学 Source pin **c47e13e4aba0e006366f989d6334d443f6333ae3** 未变。延续 GH-124（S1）、GH-129（双通道）、GH-130（3347 行列式=72）、GH-131（有限域微分/反射）而非重复其中已完成结论。

## GH-133：适用于全部奇素数的系数 Wronskian 定理

设 p≥5 为奇素数，N=(p−1)/2，g_B(X)=X²+X+B，且在 F_p[B] 中定义

\[
A=[X^N]g_B^{p-1},\quad E=[X^{3N+1}]g_B^{p-1},
\quad A_2=[X^N]g_B^{p-2},\quad E_2=[X^{3N+1}]g_B^{p-2}.
\]

形式求导即得 A_2=−A'、E_2=−E'，因此矩阵行列式 Δ=AE_2−A_2E=A'E−AE'。

**定理**（F_p[B] 多项式恒等式）：

\[
\boxed{\Delta(B)=-N[B(1-4B)]^{N-1}.}\tag{1}
\]

从而对任何特征 p 的扩域，矩阵 [[A,E],[A_2,E_2]] 当且仅当 B≠0,1/4 可逆。对于曲线 y²=x³+x²+Bx，其三次式判别式是 B²(1−4B)，故**恰好在椭圆曲线非奇异的参数域**上，这个两通道矩阵处处非退化。

**代数证明。** 定义 P_n(B)=[X^n](1+X+BX²)^{-1}=Σ_{0≤j≤n/2}(−1)^{n−j}binom(n−j,j)B^j。由特征 p 恒等式 g_B^{p−1}=g_B^p/g_B 比较系数，得到 E=P_{N−1}、A=B^N P_N。将上述二项式系数逐项代入，可验证 A 与 E 均满足 F_p[B] 中的同一微分方程

\[
4B(1-4B)Y''+(6-48B)Y'-15Y=0.\tag{2}
\]

检验时 Y=Σ y_jB^j 的系数递推准确为 2(j+1)(2j+3)y_{j+1}=(4j+3)(4j+5)y_j，连同截断处的零因子边界由 P_n 的显式系数或递推 P_n=−P_{n−1}−BP_{n−2} 逐项核实。无需解析或连续性假设。

令 W=A'E−AE'。直接对 W 求导，利用 (2) 消去 A''、E''，在 F_p(B) 中有

\[
W'=-\frac{6-48B}{4B(1-4B)}W.
\]

而 Q=[B(1−4B)]^{N−1} 因 N−1≡−3/2 (mod p)，满足相同的一阶方程。故 (W/Q)'=0。因 deg W≤p−3，deg Q=p−3，在 F_p(B) 中这个约分后分子分母次数均 <p 的有理函数若导数为零，只能是常数（导数核 F_p(B^p)）。又 A=(−1)^N B^N+O(B^{N+1})、E(0)=(−1)^{N−1}，故 W=−NB^{N−1}+O(B^N)，常数是 −N，证得 (1)。这里的 Wronskian 思路是经典 Abel 型方法在有限特征多项式环境中的直接代数验证，并不主张历史首次性。

对目标素数 p≡3 (mod 8), p≥11，固定原标记 T=2√2/3∈F_{p²}、B0=(1+T)/8。计算 B0(1−4B0)=(1−T²)/16=1/144。由 144=12² 和 Euler 判据 (144^{-1})^N=1，故

\[
\boxed{\Delta(B_0)=-144N\equiv72\pmod p\neq0.}\tag{3}
\]

**GH-130 的3347数值72因而推广为所有目标素数的统一常数。**

## GH-134：两个盲带矩恢复一阶标记信息

令 k=F_{p²}，f_B=Xg_B，χ_k 为零处取0的二次特征。延用 GH-129 定义 S_r(B)=Σ_{x∈k,f_B(x)≠0}χ_k(f_B(x))(x/f_B(x))^r。令 H=[X^N]g_B^N，C=H'/N=[X^N]g_B^{N−1}，D=H−2BC=[X^{N−1}]g_B^{N−1}。GH-129 两通道恒等式给出

\[
\binom{m_1}{m_2}=-\begin{pmatrix}A&E\\A_2&E_2\end{pmatrix}\binom{C^p}{D^p},
\qquad m_1=S_{N+1},\ m_2=S_{N+2}.
\]

对于 B∈k\{0,1/4}，使用 (1) 的非零 Δ，定义

\[
U=\frac{Em_2-E_2m_1}{\Delta},\quad
V=\frac{A_2m_1-Am_2}{\Delta}.
\]

Cramer 法则得 U=C^p、V=D^p。由于 k 上两次 Frobenius 是恒等，C=U^p、D=V^p，H=V^p+2BU^p，H'=NU^p。消费 GH-124 已验证的 S1=2H'H^p（2N=−1 in F_p），得到

\[
\boxed{S_1(B)=-U^p(V+2B^pU).}\tag{4}
\]

同理，曲线光滑时仅在模 p 意义下有

\[
\boxed{a_{p^2}(E_B)\equiv(V^p+2BU^p)(V+2B^pU)\pmod p.}\tag{5}
\]

式 (4) 是精确 **two-moment reconstruction**，**不是**从 CM/Jacobi 独立求值 S1，也不确定整数 Frobenius 迹的符号。依赖 GH-124 和 GH-129 的数学强度不因重组提高；GH-83、反射尾项 R_3347(9)=0 和 GH-3 仍分别未解决。

## 3347的精确整数证书

在 k=F_3347[r]/(r²−2) 中，用 (a,b) 表示 a+br。原始 B0=(2092,279)，N=1673。直接系数和有限域计算得到：

| 精确量 | (a,b) |
| --- | --- |
| A, E | (3052,295), (2167,0) |
| A2, E2 | (33,2542), (0,127) |
| Δ | **(72,0)** |
| m1=S1674, m2=S1675 | (3179,0), (0,2701) |
| recovered U=C^p, V=D^p | (0,2702), (568,998) |
| recovered C, D | (0,645), (568,2349) |
| recovered H, H' | (783,0), (0,1351) |
| **recovered S1** | **(0,362)** |
| **recovered a_(p²) mod p** | **(588,0)** |

两种独立的精确系数算法分别采用 P_n/导数递推与多项系数：

\[
[X^j]g_B^t=\sum_{a=\max(0,j-t)}^{\min(t,\lfloor j/2\rfloor)}
\frac{t!}{a!(j-2a)!(t-j+a)!}B^{t-j+a}.
\]

程序实际执行：对 44 个素数 3≤p≤199 逐系数核验 (1) 及 (2)；对其中 11 个 p≡3 mod8 的原始标记核验 (3) 和双矩恢复；对3347双算法核验所有系数/恢复式。stdout:
- PASS_GH133_UNIVERSAL_WRONSKIAN_POLYNOMIAL primes 44 max_p 199
- PASS_GH134_ALL_TARGET_MARKS_DETERMINANT_72 small_primes 11
- P3347_EXACT (3347, (3179, 0), (0, 2701), (0, 362), (588, 0))
- PASS_GH134_P3347_TWO_MOMENT_RECOVERY_AND_INDEPENDENT_MULTINOMIAL

44个有限检查不是一般性证明；(1)–(5) 的通用性来自前述代数论证与明确依赖。未重跑 GH-125 的1120万元素全域枚举，未运行原生 p=373 实验。参考：MathWorld, Abel's Differential Equation Identity, https://mathworld.wolfram.com/AbelsDifferentialEquationIdentity.html；这里的正特征步骤已逐项自证。不存在独立审稿者或 Lean 准入。

**BRC作用域。** 保留素数、原始标记、域的 Frobenius 共轭、带符号字符矩及定义中的零点支持。所证只是给定 B、指定两个矩、未来操作仅 H/H'/S1/a_q modp 的精确双通道因子恢复；不能删除标记、推广到所有未来操作、替代原生 P000 X6 时空结构，或将其说成 CM 特殊值独立来源。

**持久前沿与下一动作。** D25/LIFT/JT2 OPEN。已有 GH-124～GH-132 证明及3347原始枚举不重做。下一最小科学问题：从保留二阶挠点标记的独立 CM/Jacobi/Gauss/p进周期来源直接求值 m1,m2 或 S1，以式 (4) 作可信的跨路径交叉检验。原 GH-3、GH-83 独立证明与原生 p=373 实验保持分离。认证 Gateway 0.6.11 最新只读显示 research_authority_granted=false、executor_binding_configured=false、native active_jobs=5/5、Source CODE_REVIEW_REQUIRED；本轮没有合法新 CLAIM、authorized OPEN、native Source checkpoint、Result、review。历史 session/claim/staging 不动；控制支持仍是 Enterprise Math #1558，恢复需 source exact continuation/old request reconcile、继任 CAS、合法 CLAiM 和 OPEN。此作者侧 Git 文件不是 native checkpoint，也不授 Research-Activity 登记。
