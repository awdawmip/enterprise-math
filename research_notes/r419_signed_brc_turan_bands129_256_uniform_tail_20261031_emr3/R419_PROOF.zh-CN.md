# R419｜带符号 BRC 辅助模型：128 条新无限 Turán 带与统一二次尾部定理

日期：2026-10-31。状态：作者侧精确整数计算机辅助证明及解析证明；UNREVIEWED / NOT_ADMITTED。本研究只涉及带符号 BRC 的辅助组合读出，不声称原生 X6 动力学或物理残差定理。

## 定义与主结论

对整数 r≥s+1、s≥2 定义

\[
\delta_{r,s}=[t^r](1-t)(1+t)^{2s}(1+t^2)^{r-s},\quad
H_{r,s}=\binom{r+s}{2s}\delta_{r,s},\quad
D_{r,s}=H_{r,s}^2-H_{r,s-1}H_{r,s+1}.
\]

**定理 A（精确计算机辅助证明）：** 所有 129≤s≤256 的整数 s 与所有整数 r≥s+1，均有 D_{r,s}>0。这包含 128 条分别覆盖无限 r 的严格正性定理。

**定理 B（独立解析证明）：** 任意整数 s≥3、r≥s+1，只要

\[
\boxed{r>s+1+\frac{3s(s+1)(2s+1)}{4s+1}},
\]

就有 D_{r,s}>0。特别地，

\[
\boxed{\forall s\in\mathbb Z_{\ge7}\ \forall r\in\mathbb Z_{\ge2s^2}:\quad D_{r,s}>0.}
\]

定理 B 不依赖逐 s 计算机证书；它尚未处理 r 低于显式二次阈值的所有参数。

## 解析证明（定理 B）

令 Cat_n=binom(2n,n)/(n+1)，C(z)=Σ_{n≥0}Cat_n z^n。从原始带符号系数直接计算基例：δ_{2m,1}=0，δ_{2m+1,1}=Cat_m；利用 (1+t)^2=(1+t²)+2t 得到 δ_{r,q+1}=δ_{r,q}+2δ_{r-1,q}。归纳得到，对 r≥q≥1，

\[
\delta_{r,q}=[z^r]z(1+2z)^{q-1}C(z^2)
=\sum_{\substack{0\le j<q\\r-q+j\in2\mathbb Z_{\ge0}}}
\binom{q-1}{j}2^{q-1-j}\mathrm{Cat}_{(r-q+j)/2}.
\]

固定 s≥3，令 ε=r mod 2、b=(r+ε)/2−1。对 q∈{s−1,s,s+1}，合法项的 Catalan 指标等于 b−d，其中

\[
d=(q-j-2+\varepsilon)/2,\quad
0\le d\le d_*:=\lfloor(s-1+\varepsilon)/2\rfloor\le s/2,\quad b\ge d_*.
\]

由 Catalan 邻项比，

\[
\frac{\mathrm{Cat}_{b-d}}{\mathrm{Cat}_b}
=4^{-d}\prod_{a=0}^{d-1}\left(1+\frac3{2(b-a)-1}\right).
\]

每一因子为正，利用 log(1+u)≤u，可得

\[
1\le4^d\frac{\mathrm{Cat}_{b-d}}{\mathrm{Cat}_b}
\le\exp\frac{3d_*}{2(b-d_*+1)-1}
\le U:=\exp\frac{3s}{2(r-s-1)}.
\]

本定理的 r 下界保证 r−s−1>0。由于 q≥2，奇偶项的二项式半和均为 2^{q−2}，所以

\[
M_q=\sum_{j\text{合法}}\binom{q-1}{j}2^{q-1-j}4^{-d}
=2^{q-1-\varepsilon}>0,\qquad
M_q\le\delta_{r,q}/\mathrm{Cat}_b\le UM_q.
\]

令 C_q=binom(r+q,2q)。直接计算二项式比率：

\[
\lambda=\frac{C_{s-1}C_{s+1}}{C_s^2}
=\frac{2s(2s-1)(r+s+1)(r-s)}
{(2s+2)(2s+1)(r+s)(r-s+1)}
<\lambda_\infty:=\frac{2s(2s-1)}{(2s+2)(2s+1)}<1.
\]

由于 M_{s-1}M_{s+1}=M_s²，

\[
\frac{D_{r,s}}{(C_s\mathrm{Cat}_b)^2}
=\left(\frac{\delta_{r,s}}{\mathrm{Cat}_b}\right)^2
-\lambda\frac{\delta_{r,s-1}\delta_{r,s+1}}{\mathrm{Cat}_b^2}
\ge M_s^2(1-\lambda U^2)
>M_s^2\left(1-\lambda_\infty e^{3s/(r-s-1)}\right).
\]

又 1−λ∞=(4s+1)/((s+1)(2s+1))，对 0<λ∞<1 有 log λ∞≤−(1−λ∞)。因此只需

\[
\frac{3s}{r-s-1}<1-\lambda_\infty
=\frac{4s+1}{(s+1)(2s+1)},
\]

等价于主定理 B 的显式阈值，就有 λ∞ U²<1，所以上式严格正，证毕。

进一步在 r=2s² 处，

\[
\frac{4s+1}{(s+1)(2s+1)}-\frac{3s}{2s^2-s-1}
=\frac{s^2-6s-1}{(s-1)(s+1)(2s+1)}>0 \quad(s\ge7).
\]

随着 r 增大误差上界单调下降，遂得所有 s≥7、r≥2s² 的结论。这里的全称证明为解析严格不等式，不依赖后述有限 s 扫描。

## 精确整数系数证明（定理 A）

对固定 s≥2、ε∈{0,1}，取满足 r0≥s+1 且 r0 mod 2=ε 的最小 r0，令 r=r0+2x、x≥0、b=b0+x，dmax=floor((s−1+ε)/2)。按上述 Catalan 比值对三个 q∈{s−1,s,s+1} 通分，定义整数多项式

\[
T(x)=\prod_{a=0}^{dmax-1}2(2(b_0+x-a)-1),
\]

\[
N_q(x)=\sum_{\substack{0\le j<q\\\varepsilon-q+j\ \mathrm{even}}}
\binom{q-1}{j}2^{q-1-j}
\left[\prod_{a<d}(b_0+x-a+1)\right]
\left[\prod_{d\le a<dmax}2(2(b_0+x-a)-1)\right],
\quad d=(q-j-2+\varepsilon)/2.
\]

于是 δ_{r,q}/Cat_b=N_q/T。令

\[
L_n=2s(2s-1)(r+s+1)(r-s),\qquad
L_d=(2s+2)(2s+1)(r+s)(r-s+1),
\]

\[
A_\varepsilon=L_dN_s^2-L_nN_{s-1}N_{s+1},\qquad B_\varepsilon=L_dT^2.
\]

严格恒等式：

\[
\frac{D_{r,s}}{[\binom{r+s}{2s}\mathrm{Cat}_b]^2}
=\frac{A_\varepsilon(x)}{B_\varepsilon(x)}.
\]

B(x)>0；A 与 B 均为整数多项式，次数≤2dmax+2。因此若 A 的全部升幂系数严格正，则全部 x≥0 严格正，这是真正涵盖无限 r 的有限代数证书，而非有限抽样推断。

实际执行 r419_exact_certify.py 的精确整数卷积、前缀/后缀乘法，对 s=129..256 共 256 个 (s,ε) 族逐个计算 A、B 的完整升幂系数，得到

R419_EXACT_PASS 129 256 bands 128 parity_cases 256 A_positive 49792 B_positive 49792 raw_boundary_checks 256

两类各 49,792 个系数全部严格正。每族另从原始 (1−t) 提取式检查 x=0 的 D 有理恒等式。完整原始 JSON：39,387,830 字节，SHA256 bd4829a0bd04a9085c5b4672007f3763cd24fa0ce5d1aee603c719250245172d；全行哈希摘要 SHA256 c2d07f45bd45bdd8a8b699e716c121a35e4c8e5dbae4b54de105b1e2a7a48aeb。

独立程序 r419_independent_validation.py 不导入生成器；独立以原始带符号二项式卷积和 Catalan 核复核 252 项，交叉校验 84 个 D 多项式恒等式点，验证每族系数哈希与全部正系数，程序返回：

R419_INDEPENDENT_PASS parity_cases 256 coefficients_per_sign 49792 raw_delta_and_Catalan_pairs 252 polynomial_identity_pairs 84 analytic_bound_test_s7_to512 506

其中 s=7..512 的有限有理不等式检查只是附加诊断，定理 B 的无限结论由上面的因式分解证明。所有计算仅用整数精确算术，无浮点判号。

## 来源与使用界限

源项：R416 Catalan 核、R418 正系数证书以及本文重新导出的递推/核/权比。上一作者侧 R418 前沿 commit ba992e845f1239c85d35ec9bff256e2726fd0a61。GLOBAL_KNOWLEDGE_V1 固定 main@053f10e0e8ce78f013ddc43ab4d62e3382f7744e；Enterprise Math 规范 main@42fae018032be0be1b496b749472ead751d624a2。

实际 Github 身份 awdawmip；原生定向研究上下文 authority_granted=false，活跃任务查询 CONTROL_QUOTA，故当前有效 Source owner、正式 CLAIM/Result、独立 Driver 审阅和数学接纳均未确认。本文件仅是作者侧可移植研究物料，GitHub commit/PR 不是 Source 数学准入。P000 与 ACTIVE 世界观不变。

GitHub 提供可重建完整证据的执行程序与本证明；完整 39MB 原始 JSON 在本轮研究 ZIP 中。**源码/哈希摘要不等于已将原始完整 JSON 单独上传 GitHub**。

下一问题：试图解析证明所有 s≥3、r≥s+1 的 D 正性或找到准确原始定义反例。重点是 s≥257 且 r<2s²、r−s≥129（此后半条件依赖待独立审查的旧右边界证书），对相邻 q 的相关误差做联合估计，而非将其独立作最差上界；也可从 s=257 开展下一组完整整数系数证书。不得推定原生 X6 支路动力学保真已经证明。
