# R565｜冻结 signed BRC 辅助标量模型：固定 k=24 的半数符号密度和有限零项

2026-11-06（北京时间）。作者侧精确计算机辅助证明；独立数学 Driver 审阅待完成。

**冻结科学输入：** R462 @ 18783e01e3646c72b7aab3b16d3f565e83e6446f（research_notes/r462_signed_brc_right_edge_171_174_20261101_emr3/R462_PROOF.zh-CN.md）；接续 R564 @ 3d67eed1cd2993fc461086cab515e366ad22ee4f。P000、ACTIVE 世界观与原生 X6 类型定义不变。

## 一、命题

令 k=24，r=2k+1=49，Catalan 数 C_j=binom(2j,j)/(j+1)。对整数 2≤t≤49 定义

\[
H(t)=\binom{r+t}{2t}\sum_{q=0}^{\min(k,\lfloor(t-1)/2\rfloor)}\binom{t-1}{2q}4^qC_{k-q};
\]

其他整数 t 取 H(t)=0。与 R462 冻结 signed BRC 带符号系数严格相等的原始公式是

\[
H(t)=\binom{r+t}{2t}\sum_{q=0}^{r-t}\binom{r-t}{q}\left(\binom{2t}{r-2q}-\binom{2t}{r-2q-1}\right)
\]

（越界二项式取零）。令 D_0=1，D_m=det(H(3+i-j))_{0≤i,j<m}。

**定理（固定 k=24）：**

\[
\lim_{N\to\infty}N^{-1}\#\{0\le m<N:D_m>0\}
=\lim_{N\to\infty}N^{-1}\#\{0\le m<N:D_m<0\}=\frac12,
\qquad\#\{m\ge0:D_m=0\}<\infty.
\]

## 二、有理线性递推和特征根隔离

h=H(2)=322347046416267600>0。令 s_m=D_m/h^m，s_0=1。Toeplitz–Hessenberg 展开得到

\[
s_m=\sum_{j=1}^{\min(m,47)}a_js_{m-j},\quad
a_j=(-1)^{j-1}H(j+2)/h.
\]

生成函数 \(\sum_{m\ge0}s_mz^m=[1-\sum_{j=1}^{47}a_jz^j]^{-1}\)。令
\(Q(y)=y^{47}-\sum_{j=1}^{47}a_jy^{47-j}\)，整数多项式
\(P(y)=80586761604066900\,Q(y)\)。

用 65 位数值 nroots **提议** 47 个有理复圆心 c_i；所有接受判断使用整数或 Fraction 精确运算。固定 ε=10^{-22}，展开 \(P(c_i+w)=\sum_{j=0}^{47}b_{ij}w^j\)。逐盘严格验证

\[
\max(|\Re b_{i1}|,|\Im b_{i1}|)\varepsilon>
|\Re b_{i0}|+|\Im b_{i0}|+\sum_{j=2}^{47}(|\Re b_{ij}|+|\Im b_{ij}|)\varepsilon^j.
\]

左侧≤|b_{i1}|ε，右侧≥|b_{i0}|+Σ_{j≥2}|b_{ij}|ε^j，故 Rouché 定理保证每盘唯一简单根。47盘的1081对严格不相交，且对其他45盘逐一做保留 ε 误差的精确平方模间隔比较，证明唯一最大模的一对非实共轭根 λ、λ̄。主导模长数值约53.46645568632029，非主导最大模长数值约18.793129138252787；所有严格判断使用有理数。最大 Rouché 右/左比约9.064335635754067×10^{-21}。

## 三、无理相位的完整有限证书

取 λ 的虚部为正、θ=arg λ∈(0,π/2)。从根圆盘严格界定 Re λ/Im λ，利用 arctan 交错级数有理上下界及 Machin 恒等式 π=16 arctan(1/5)-4 arctan(1/239)，求得有理相位包络 θ/π∈(lo,hi)，宽度约1.659218167956085×10^{-24}。

假如 θ/π=p/q 为既约有理数，则 λ/λ̄=e^{2πip/q} 是 q 阶本原单位根。作为有理47次特征多项式两个不同根之比，其代数次数≤47·46=2162，因此 φ(q)≤2162。使用整数欧拉函数界 φ(q)≥√(q/2)，得

\[
q\le2(2162)^2=9348488=:M.
\]

有理区间 (lo,hi) 宽度严格小于 1/M²，因此其中至多存在一个分母≤M的既约有理数。若存在，它必是中点在该分母范围内的最近有理逼近（区间内点距中点严格小于区间外点）。Python Fraction.limit_denominator(M) 使用精确连分数求得最近候选

\[
127149/417490.
\]

严格分数比较证实该候选不在 (lo,hi) 内。故 θ/π 无理。此处排除覆盖全部 q≤M，无须枚举欧拉函数值。

## 四、半数符号密度和零项有限性

特征根全部简单、生成函数分子为1，因此主导留数 A≠0，且存在 ρ<|λ| 使

\[
s_m=A\lambda^m+\bar A\bar\lambda^m+O(\rho^m)
=2|A||\lambda|^m\cos(m\theta+\arg A)+O(\rho^m).
\]

由 θ/π 无理及 Weyl 等分布定理，主导余弦正、负的频率各为1/2；指数小误差只可能在越来越小的余弦零点邻域影响符号，故 s_m 的正、负符号自然密度各1/2。若 s_m 无限多项为零，则特征0线性递推的 Skolem–Mahler–Lech 定理推出某条无限算术级数全零；沿该级数主导相位依然等分布，有任意大项余弦绝对值>1/2，与指数小误差和全零矛盾。故零项集合有限。因 h>0，D_m 与 s_m 同号。

## 五、执行证据和再验证

执行环境 Python 3.13.5 / SymPy 1.14.0；命令 python -u R565_VERIFY.py；输出见 R565_EVIDENCE.txt。检查48个原始 H 整数恒等式、47个精确根圆盘、1081对圆盘间隔、全部其他根的严格模长分离、连分数无理相位证书、m=0..1024 全整数递推与前12阶独立 Berkowitz 原始行列式。实测正514、负511、零0、相邻换号311。终止标记 R565_K24_HALF_DENSITY_AUTHOR_CERT_PASS。数值求根只用于产生待验证中心。

外部经典定理依据：Skolem–Mahler–Lech 定理（Encyclopedia of Mathematics，https://encyclopediaofmath.org/wiki/Skolem-Mahler-Lech_theorem）；Weyl 无理旋转等分布定理。

**接续：** k=25 的49次特征多项式；更重要的是 k≥5 的统一主导模长分离和无理相位判据；RS-X6-NATIVE-ROTATION-DYNAMICS 按原生 owner/CLAIM 单独处理。