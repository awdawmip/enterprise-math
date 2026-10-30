# R402 — 原始带符号 BRC 十二支路的全余阶 Catalan 定理与奇偶退化定理

日期：2026-10-30。作者侧推导，独立审阅未完成；不是正式 Result/Review/接纳，不是原生 X6 物理定理，也不是所有余阶 PF₂ 相图。本条目包含完整证明的核心恒等式、边界、精确可重做条件；逐项原始证书存放于本轮完整交付 ZIP。

## 精确模型

保持原始 R346/R401 的十二个带符号 K_i(t) 支路及 J_s(t)，仅以 K_3[t²]=−8(1+θ) 代替原系数，其他符号不变。规定 B_0(t)=1+t，B_s=J_s+Σ_{i=1}^{min(s,12)}K_i B_{s−i}。记 b_{s,q}=[t^q]B_s，
D_{q,k}=Σ_{w=0}^k (−1)^{k−w}binom(k,w)2^{q−w}b_{q+w,q}，
L_r(k)=5^{r−k}D_{r+k,k}，
Q_r(v)=L_r(v+1)L_r(v+2)−L_{r−1}(v+2)L_{r+1}(v+1)，
c_j^{(r)}=Δ_v^j Q_r(0) (0≤j≤2r)，
T_j^{(r)}=(c_j^{(r)})²−c_{j−1}^{(r)}c_{j+1}^{(r)} (1≤j<2r)。
θ∈ℝ，研究参数范围 θ>−1，r 为正整数。定义 a=30−16θ，θ*=15/8，Cat_r=binom(2r,r)/(r+1)。

**定理 A（全余阶）** 对每个 r≥1，k↦L_r(k) 为次数≤r 的多项式，其 Newton 最高项系数是 a^r，且
\[
\boxed{c_{2r}^{(r)}(\theta)=\mathrm{Cat}_r(30-16\theta)^{2r}.}
\]

**定理 B（全余阶）** 在 θ* 处：
\[
\operatorname{ord}_{a=0} c_{r+s}^{(r)}=2s\quad(2\le s\le r),
\]
\[
\operatorname{ord}_{a=0}c_{r+1}^{(r)}
=\begin{cases}2&r\text{为奇数}\\3&r\text{为偶数},\end{cases}
\quad r\ge1,
\]
以及
\[
a^{4s}\mid T_{r+s}^{(r)} \quad (1\le s\le r-1).
\]
最后一项仅是多项式的整除/消零阶数下界，未宣称所有 T 都恰为 4s 阶。

## 证明 I：形式外根和统一系数提取

用原始十二支路的有限生成函数
\[
\mathcal B(z,t)=\frac{1+t+\sum_{s\ge1}J_s(t)z^s}{1-\sum_{i=1}^{12}K_i(t)z^i}=\frac{N(z,t)}{1-K(z,t)}.
\]
J_s 在 s>10 为零。置 u=zt，R(z,u)=\mathcal B(z,u/z)=\mathcal N/\mathcal D。直接对原始 K/J 的有限二项式系数按 (u,z) 收集，\mathcal K=K(z,u/z) 的 z 次数仅在 [−8,1]，\mathcal N 的 z 次数在 [−8,0]，且
\[
\mathcal K=2z+(3-z)u+[4-8(1+\theta)z]u^2
 +(4z^{-1}-8-11z)u^3+(4z^{-1}-29+6z)u^4+O(u^5),
\]
\[
\mathcal N=1+(z^{-1}-2)u+O(u^2).
\]
令 P(z,u)=z^8\mathcal D(z,u)，M(z,u)=z^8\mathcal N(z,u)。这是 z 多项式，deg_z P=9、deg_z M≤8，P(z,0)=z^8(1−2z)，M(z,0)=z^8。形式隐函数定理在 z=1/2 的简单根处唯一给出 ζ(u)，满足 ζ(0)=1/2、P(ζ,u)=0。将 P=(z−ζ)H，H(z,0)=−2z^8、deg_z H=8，则
\[
R(z,u)=\frac{A(u)}{1-z/\zeta(u)}+\frac{S(z,u)}{H(z,u)},\quad \deg_z S<8,
\]
其中
\[
A(u)=-\frac{\mathcal N(\zeta(u),u)}{\zeta(u)\partial_z\mathcal D(\zeta(u),u)},\qquad A(0)=1.
\]
因 H(z,0)=−2z^8 且 deg_z H≤8，第二项在 u-adic 展开中只含**严格负的 z Laurent 次幂**；第一项只含非负次幂。乘以次数≤k 的 (1−2z)^k，负次幂部分仍不贡献 z^k，因此准确地有
\[
[z^k](1-2z)^k R(z,u)=A(u)(\zeta(u)^{-1}-2)^k. \tag{1}
\]
从 D 定义换元 i=k−w，可不作近似而得
\[
D_{r+k,k}=2^r[z^{r+2k}t^{r+k}](1-2z)^k\mathcal B(z,t)
=2^r[u^{r+k}z^k](1-2z)^kR(z,u).
\]
记 G(u)=(ζ(u)^{-1}−2)/u，\mathsf A(x)=A(10x)，\mathsf E(x)=G(10x)/5，则对**所有 r,k**：
\[
\boxed{L_r(k)=[x^r]\mathsf A(x)\mathsf E(x)^k.}\tag{2}
\]
严格的低阶展开为 ζ^{-1}=2+5u+(15−8θ)u²+(54−24θ)u³+(226−104θ)u⁴+O(u⁵)、A(u)=1+3u+O(u²)，因此
\[
\boxed{\mathsf A(x)=1+30x+O(x²),\
\mathsf E(x)=1+a x+(180+30a)x²+(6200+1300a)x³+O(x⁴).}\tag{3}
\]
E(0)=1，故 E(x)^k=Σ_j binom(k,j)(E(x)−1)^j；取 [x^r] 后仅有 j≤r，最高 Newton 系数为 a^r。Q_r(v) 中 v^{2r} 系数为
a^{2r}((r!)^{-2}−((r−1)!(r+1)!)^{-1})=Cat_r a^{2r}/(2r)!。
对该次数≤2r 多项式作 Δ^{2r}，正好乘 (2r)!，得定理 A；r 和 θ 均没有有限取样限制。

## 证明 II：精确退化阶数及偶余阶特殊分岔

设 F(x,y)=E(x)E(y)−1。由 (2) 与 Δ 的代数定义，
\[
\begin{aligned}
c_j^{(r)}={}&[x^r y^r]A(x)A(y)E(x)E(y)^2 F(x,y)^j\\
&-[x^{r-1}y^{r+1}]A(x)A(y)E(x)^2E(y) F(x,y)^j.\tag{4}
\end{aligned}
\]
此处 A,E 分别指 \mathsf A,\mathsf E。在 a=0 时 E(x)=1+180x²+6200x³+O(x⁴)。F 唯一空间一次项为 a(x+y)，其他项空间次数≥2。令 j=r+s，目标单项式的总空间次数为 2r，因此 j 个 F 中至少 2s 个必须取 a(x+y)；故 a^{2s}|c_{r+s}，且精确最低候选项是
\[
[a^{2s}]c_{r+s}^{(r)}
=\binom{r+s}{2s}180^{r-s}\,\delta_{r,s},\tag{5}
\]
\[
\delta_{r,s}=[t^r](1-t)(1+t)^{2s}(1+t^2)^{r-s}.
\]
此式对 s=r 的 Catalan 情形也成立。

若 s=1，由 binom 系数恒等式：
\[
\delta_{2m+1,1}=\mathrm{Cat}_m>0,\qquad \delta_{2m,1}=0.
\]
若 s≥2，令 m=r−s≥0。对称多项式 (1+t)²(1+t²)^m 的偶数次系数为 binom(m+1,j)，奇数次系数为 2binom(m,j)，它们对称单峰，且中心相邻两项具有严格差。再连续与 (1+t)² 卷积共 s−1 次，保持对称单峰和该严格中心差，从而 δ_{r,s}>0。由此奇数 r 的全部 s，以及偶数 r 的 s≥2，正好具有 2s 阶零点。

对 r=2m≥2、s=1，(5) 首项消失。直接用 (3) 在 (4) 提取 a³ 系数，只需分配三次 a(x+y)、一个二次项（及一次 prefactor），或分配二次 a(x+y) 与一个随 a 变化的二次项。后者乘 δ_{r,1}=0 消去；前者涉及
\[
\delta_{2m,2}=2\mathrm{Cat}_{m-1},\qquad
\gamma_{2m}=[t^{2m}](1-t)(1+t)^3(1+t^3)(1+t^2)^{2m-3}
=\mathrm{Cat}_{m-1}\ (m\ge2).
\]
计算得到**非零严格正**的首项：
\[
\boxed{[a^3]c_{2m+1}^{(2m)}
=\binom{2m+1}{3}180^{2m-2}\mathrm{Cat}_{m-1}
\left(60+\frac{6200}{180}(2m-2)\right)>0.}\tag{6}
\]
m=1 时三次项来自 60，γ 项为零，不需要定义负指数。故所有偶数 r 的 c_{r+1} 恰有 3 阶零点。因 a=−16(θ−15/8)，a 阶与 θ 阶相同。最后 T_{r+s}=c_{r+s}²−c_{r+s−1}c_{r+s+1}，两项由上述下界均被 a^{4s} 整除，定理 B 完成。

**范围和审阅要求。** 精确代数命题限于原始带符号 K/J→B→D 的辅助有限序列，不将相消改造成正质量，未作完整原生三维切片嵌入或六维 X6 动力学证明；不是新的物理证据，也不代替 PF₂ 相图认证。R401 已完成 r=29 的全参数分类；本轮 R402 证明的是此前逐余阶观察的跨余阶结构，而非 r=30 的全参数分类。独立审阅应重点核对 Laurent 负幂分解、(4) 的下标、(5) 的 binomial 中心差、(6) 的三类 a³ 来源。

**实际验证及来源。** 作者侧 Python stdlib Fraction 原始十二支路重算：θ∈{−1/2,0,1/2,15/8,187/100}，r=1..8，共 40 项 L_r 最高前向差分及 40 项 c_{2r} Catalan 身份独立检查；另一条 a-jet 精确路径核验 36 个 c 的消零阶数和 28 个 T 的四倍阶下界，另对 r≤10 再运行 jet 检查成功。核和形式外根前四阶均精确核验。程序输出 R402_EXACT_FINITE_CROSSCHECK_PASS，完整本地 EVIDENCE.json SHA256 a2e4a304573b98f3cff141e0ab881f8f4f56bfc1eccfd43de0af255022309a26。有限测试不是全余阶证明，全余阶依赖上述形式代数证明。

**下一项可判定问题。** 定理 B 已证明 T_{r+s} 至少有 4s 阶零点。求其首个非零系数，证明是否始终恰为 4s，或提交最小精确反例。其次继续研究 η_r 的奇偶极限/共同界；没有充分证据不将有限实验推出全余阶 PF₂ 结论。

冻结知识：GLOBAL_KNOWLEDGE_V1 main@a725c591052bc9f146a6f27abc75030181d6da26；Enterprise Math control-main@b8853d39eeb8a38cff2ba77a0fc3d19a452cfeaf；先前 R401 研究 PR HEAD@afeaff5284df2029c319c48bb7c9e062cc199be3。P000/ACTIVE 世界观未修改。Native service version 0.6.11 报 research_authority_granted=false、CONTROL_QUOTA 5/5、CODE_REVIEW_REQUIRED，未得到正式 owner/CLAIM/Result/Driver Review。性质 AUTHOR_SIDE_PROOF / DRIVER_UNREVIEWED / NOT_ADMITTED / ACTIVITY_REGISTER_PENDING。
