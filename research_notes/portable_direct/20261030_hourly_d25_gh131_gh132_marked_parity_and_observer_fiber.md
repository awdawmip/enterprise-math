# D25/LIFT GH-131–GH-132：Lucas 盲区的标记共轭定理与迹压缩反例

2026-10-30 (Asia/Hong_Kong)；本 Research 逻辑会话：chatgpt-research-hourly-enterprise-math-20260923。作者侧可移植成果：AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING。

Parent Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT；publication TP2-B6F4FC938FF94941C1B7；冻结科学 Source pin c47e13e4aba0e006366f989d6334d443f6333ae3 不变。精确前提：GH-124–GH-130，特别是 GH-129 的全指标系数提取与两通道公式。GH-130 的 19 个素数、1659 指标共轭奇偶规律原为有限诊断，现给出全素数证明。

## GH-131（已推导的一般性命题）

令 p=8m+3≥11 为素数，m≥1，N=(p−1)/2=4m+1，e=(p²−1)/2=N(p+1)，g_B(X)=X²+X+B。在 F_p[B] 定义

\[
F_s(B)=-[X^e]g_B(X)^{Np-s}\quad(1\le s\le N),\qquad J(B)=\tfrac14-B.
\]

**定理：**对全部 1≤s≤N，成立 **F_s(J(B))=(-1)^{s-1}F_s(B)**，这是 F_p[B] 的多项式恒等式；因此对任意特征 p 扩域参数 B 也成立。

在 k=F_{p²}=F_p(√2) 取 T=2√2/3、B₀=(1+T)/8。由 (2/p)=-1，B₀^p=(1−T)/8=J(B₀)。GH-129 已证明实际带标记字符矩 S_{N+s}(B₀)=F_s(B₀)，因此

\[
\boxed{S_{N+s}(B_0)^p=(-1)^{s-1}S_{N+s}(B_0).}
\]

奇数 s 的矩位于 F_p，偶数 s 的矩位于 √2·F_p，允许矩为零。这将 GH-130 的有限猜想提升为整个 p≡3 mod 8 素数族的代数定理；不依赖 GH-83 或 GH-3 的未决特殊值。

### 完整证明

定义 H=[X^N]g_B^N、C=[X^N]g_B^{N−1}、D=[X^{N−1}]g_B^{N−1}、A=[X^N]g_B^{p−1}、E=[X^{3N+1}]g_B^{p−1}。由在 B 求导和对 X 的系数比较，

\[
H'=NC,\qquad D=H-2BC.
\]

因为 Np−1=(p−1)+(N−1)p，且 e=Np+N，在 g_B^{p−1}(g_B^{N−1})^p 中贡献 X^e 的指数对仅有 (N,N) 和 (3N+1,N−1)，所以

\[
F_1=-AC^p-ED^p. \tag{1}
\]

令 P_n(B)=[X^n](1+X+BX²)^{-1}
=\sum_{j=0}^{\lfloor n/2\rfloor}(-1)^{n-j}{n-j\choose j}B^j。
利用特征 p 的 g_B^{p−1}=g_B^p/g_B，在次数 <p 处提取倒数系数，得到

\[
E=P_{N-1},\qquad A=B^NP_N \quad\text{in }F_p[B]. \tag{2}
\]

后式先可在 B 可逆的有理函数环中核验，乘开后为多项式恒等式，包含 B=0。

设形式微分算子

\[
L_H=B(1-4B)\partial_B^2+(1-8B)\partial_B-\tfrac34,
\quad
L_E=B(1-4B)\partial_B^2+(\tfrac32-12B)\partial_B-\tfrac{15}4.
\]

H 的系数 h_j=N!/(j!²(N−2j)!)（0≤j≤2m）满足
4(j+1)²h_{j+1}=(4j+1)(4j+3)h_j；故 L_H H=0。
P_{N−1} 和 B^NP_N 的二项式系数按相邻项比值都满足

\[
2(j+1)(2j+3)a_{j+1}=(4j+3)(4j+5)a_j, \tag{3}
\]

故 L_E E=L_E A=0，零项边界也满足。其精确次数是 deg H=deg E=2m，deg A=N+2m=6m+1<p；E(0)=1，A 的首个非零项为 −B^N。

变换 J 保持 B(1−4B) 不变，令 1−8B 反号，同时对一阶导数引入反号，因此 L_H 和 L_E 都与 J 相容。H 的系数递推在 deg≤2m 范围由常数项唯一确定；其次数为偶数，故 H(J)=H。

式 (3) 在 0≤j<p−1 的前向递推分母 2(j+1)(2j+3) 唯一零点是 j=N−1，故次数 <p 的多项式解空间至多二维，独立的 E、A 张成。E 的次数 2m 偶且小于 N，A 的次数 6m+1 奇，于是 E(J)=E，A(J)=−A+cE。代入 B=0 得 c=A(1/4)。由

\[
P_N(1/4)=(-1)^N(N+1)2^{-N},
\]

及 2^N=(2/p)=−1、N+1≡1/2 mod p，求得 c=1/2。因此

\[
H(J)=H,\quad E(J)=E,\quad A(J)=\tfrac12E-A. \tag{4}
\]

从 H'=NC、D=H−2BC 得 C(J)=−C、D(J)=D+C/2。代入 (1)：

\[
F_1(J)=-(E/2-A)(-C)^p-E(D+C/2)^p=-AC^p-ED^p=F_1.
\]

对 1≤s<N，形式系数的导数满足

\[
F_s'(B)=(Np-s)F_{s+1}(B)=-sF_{s+1}(B).
\]

s<p 可逆。每提高一次 s 即对 B 求一次导，J 反射使导数多一个负号。由 F₁(J)=F₁ 归纳得 F_s(J)=(-1)^{s−1}F_s。最后在 B₀ 取 p 次 Frobenius 即得字符矩命题。证毕。

注意：形式微分在有限域多项式内运算；未将连续性或原生 X6 几何引入本命题。实际字符矩等于 F_s 的依据是 GH-129，冻结源来源未变。

## GH-132：精确 BRC 观察者纤维不保真反例

保留 GH-130 精确值，在 F_{3347}(√2) 中 S_{1674}=3179、S_{1675}=2701√2≠0。本次额外精确计算 S_{1676}=806∈F_{3347}。令 v=2701√2。则

\[
Tr(0)=Tr(v)=0,\quad Norm(0)=0,\quad
\boxed{Norm(v)=-2\cdot2701^2\equiv2118\ne0\pmod{3347}.}
\]

因此在状态集合 {0,v} 上，不存在 φ:F_{3347}→F_{3347} 使 Norm=φ∘Tr。明确限定的载体是 (标记 B₀、指标 s、有限域有符号字符矩、Frobenius 共轭)，候选压缩观察者是 Trace，未来操作是 Norm；此观察者纤维证书要求保留反迹分量。并不声称所有观察都需要原始完整状态，也不是 P000 原生六维空间定理。GH-131 定理精确说明奇偶方向，GH-132 则给出后续操作下确切的压缩失败。

## 实际验证与不可变前沿

本轮 Python 标准库脚本 d25_gh131_marked_conjugation_parity_check.py 在 F_p 多项式上逐项核验两微分算子的递推式、H/E/A 反射恒等式，并调用已发布的 GH-129 系数实现 d25_gh129_blind_band_check.py（已核 blob da49700410d0bce2e872667c008b0cc8804965ac）。精确执行覆盖 p=11,19,43,59,83,107 的全部 1≤s≤N 及 p=3347 的 s=1,2,3,4,5,10,N，总计 165 个带标记矩实例；3347 的 H/E/A 多项式分别为 837/837/2510 个系数。运行输出：

PASS_GH131_ALL_PRIMES_PROOF_CONSISTENCY_EXACT_INVARIANCE polynomial_prime_instances=7 marked_moment_instances=165

特别核验 S_{1674}=(3179,0)、S_{1675}=(0,2701)、S_{1676}=(806,0)、Norm(S_{1675})=(2118,0)。全部为有限域整数精确运算，无浮点。一般性结论由以上代数证明承担，165 组是执行层验证；没有进行原生 p=373 实验。

**证据与接续：** GH-124–GH-130 的已完成证明、3347 前两项字符矩及旧扫描不重算。下一精确科学问题仍是从保留标记的 CM/Jacobi/Gauss 或 p-进周期独立求值 S₁(B₀)，从而尝试预测 R_{3347}(9)=0；原 GH-3 全素数同余、GH-83 独立证明与 p=373 原生实验保留各自义务。正式接续须核实固定 Research 会话自己的 recovery、原请求、Source winning claim/predecessor CAS，合法 CLAIM、authorized OPEN 后才能原生 checkpoint。Gateway 0.6.11 的本轮读取曾报告 research_authority_granted=false、executor_binding_configured=false、active_jobs=5/5、CODE_REVIEW_REQUIRED；原受保护 session/staging、源冻结 pin、维护支持 issue #1558 均保持。此文是作者侧科研证据存储，不授 task claim、Result、review 或 Source admission。