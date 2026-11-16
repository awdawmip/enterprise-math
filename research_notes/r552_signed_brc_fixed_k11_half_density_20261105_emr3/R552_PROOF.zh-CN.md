# R552｜冻结 signed BRC：固定 k=11 的全部阶数正负号各占自然密度 1/2

日期：2026-11-05（Asia/Shanghai）。作者侧精确代数证明和可执行有理数/有限域证书。
本轮真实研究身份：Researcher-ID `EM-DIRECT-51D8CE`，Research-Activity-ID `RA-5F3A05195AD2B7CCBE766FA4`（Source 登记已回读）。正式 TASK CLAIM/Result/Driver 审阅另行认定。

## 1. 来源、问题与范围

- 冻结科学输入：R462 `18783e01e3646c72b7aab3b16d3f565e83e6446f`。
- 依赖已经写入的 R541 阶数生成函数；其后 R543—R551 取得 k=5,...,10 的精确根隔离和非分圆证书。
- 本次延伸到此前未覆盖的 **k=11**。这是 signed BRC 辅助标量行列式问题，不宣称原生 X6 动力学或物理残差结论。P000、ACTIVE 世界观与冻结输入维持原样。

令 (k=11, r=2k+1=23, C_j=\frac{1}{j+1}\binom{2j}{j})。定义
[
H_k(t)=\binom{r+t}{2t}[x^r](1-x)(1+x)^{2t}(1+x^2)^{r-t}
quad(2\le t\le r),
]
其余 (t) 取零。设
[
D_0(k)=1,qquad D_m(k)=\det\big(H_k(3+i-j)\big)_{0\le i,j<m}.
]

**定理 R552-A。** 对固定 (k=11)，有
[
\lim_{N\to\infty}\frac{\#\{0\le m<N:D_m(11)>0\}}{N}
=\lim_{N\to\infty}\frac{\#\{0\le m<N:D_m(11)<0\}}{N}=\frac12.
]
零值阶数的自然密度因此为零。结合已保存的 R551 结论，作者侧结果覆盖 k=5,...,11 七个固定参数族。

## 2. 原始定义与线性递推

用有限的二项式恒等式直接化简得到
[
H_k(t)=\binom{r+t}{2t}\sum_{q=0}^{\min(\lfloor(t-1)/2\rfloor,k)}
\binom{t-1}{2q}4^q C_{k-q}.
]
验证源码独立比较这个表达式与原始 ([x^r]) 系数公式，检查 (2\le t\le23) 的全部22项。

定义 (p_t=H_k(t)/C_k)、(d=2k-1=21)、
(a_j=(-1)^{j-1}p_{j+2}/p_2)，则由 R541 的行列式递推
[
F(z)=\sum_{m\ge0}\frac{D_m(k)}{C_k^m p_2^m}z^m
=\frac{1}{1-\sum_{j=1}^{d}a_jz^j}.
]
因此令 (s_m=D_m(k)/(C_k^mp_2^m))，有 (s_0=1) 及
(s_m=\sum_{j=1}^{\min(m,d)}a_js_{m-j})。
核验 (C_{11}=58786)、(p_2=12650>0)。

对应首一特征多项式
[
Q(y)=y^{21}-\sum_{j=1}^{21}a_j y^{21-j}.
]
源码从冻结的整数/有理定义重新构造全部系数，避免人工抄写误差。

## 3. 精确 Rouché 证书：唯一主导非实共轭根对

使用 `R552_VERIFY.py` 中的 `CENTERS`：21 个复有理数圆心（9位小数作为**精确有理数**，并非浮点判定），半径 (arepsilon=1/1000)。对每个圆心 (c)，精确计算 (Q(c+w)=\sum_{j=0}^{21}b_jw^j)，并检查
[
\operatorname{lower}(|b_1|)\varepsilon>
\operatorname{upper}(|b_0|)+
\sum_{j=2}^{21}\operatorname{upper}(|b_j|)\varepsilon^j.
]
上下界使用整数平方根的有理夹逼，向外舍入；对 21 个圆盘全部成立，最大左/右比严格小于 (1/30)。
再用有理下界检查 210 对圆盘间距离均严格大于 (2\varepsilon)。

由 Rouché 定理，每个圆盘恰含一个根，21 个圆盘覆盖21次多项式的全部根，因此全部简单。前两个圆盘相互共轭且非实，并满足
[
|\lambda_+|=|\lambda_-|>11,qquad
\max_{j\ge3}|\lambda_j|<6.
]
其他 19 个根全落入较小模长的圆盘（包含一个正实根）。因此唯一最大模根集合就是这一对非实共轭根。

## 4. 完全有限的非分圆根比值证书

模数 (p=65537)。检查 (3^{65536}\equiv1)、(3^{32768}\equiv-1\pmod p)；
由 65536=2^16，这表明单位群存在65536阶元素，从而 (p) 为素数。
(Q\in\mathbb Z_{(p)}[y]) 首一且全部系数的分母模 (p) 可逆，常数项模 (p) 非零。

令
[
E(u)=\operatorname{Res}_y(Q(y),u^{21}Q(y/u))
=\prod_{i,j}(\lambda_i-u\lambda_j),qquad
R(u)=E(u)/(u-1)^{21}.
]
在 (mathbb F_p) 内对 (u=0,1,\ldots,441) 求结果式，通过 Newton 有限差分插值恢复完整次数441的 (E)。有理/有限域多项式长除法验证 ((u-1)^{21}\mid E)，所得 (R) 次数 (D=420)，且 (R(1)\ne0\pmod p)。另在插值节点外 (u=442,444) 直接用 SymPy 有限域结果式独立核验插值。

若有两个不同特征根之比为单位根，其最小分圆多项式 (Phi_q(u)) 在 (mathbb Q[u]) 中整除 (R)。由
(arphi(q)\le420) 和 (arphi(q)\ge\sqrt{q/2})，得到完整候选界 (2\le q\le352800)。
使用精确整数欧拉函数筛检查这些候选，恰有815个 (q) 满足 (arphi(q)\le420)，最大候选 (q=1680)。
对815个分圆多项式 (Phi_q\bmod p) 逐一求
[
\gcd_{\mathbb F_p[u]}(R\bmod p,\Phi_q\bmod p)=1.
]
由于 (Phi_q) 首一、(R\in\mathbb Z_{(p)}[u])，若 (Phi_q) 在特征零整除 (R)，首一多项式长除法会将整除关系保留至模 (p)，与上述815次 gcd 矛盾。因此任意两个不同根之比都不是单位根。特别地，(lambda_+/\overline{\lambda_+}) 不是单位根。

## 5. 自然密度 1/2 的推导

由唯一主导共轭根对和全部简单根的有理生成函数部分分式分解，存在 (ho>11)、(sigma<6)、(A\ne0)、(\theta\in(0,\pi))，使
[
s_m=2|A|\rho^m\cos(m\theta+\arg A)+O(\sigma^m).
]
主导残数不为零，因为 (F=1/(1-\sum a_jz^j)) 在对应简单零点处必有简单极点。
(lambda_+/\overline{\lambda_+}=e^{2i\theta}) 不是单位根意味着 (\theta/(2\pi)) 无理。Weyl 圆旋转等分布定理给出余弦正负区间的频率各为1/2。对任意 (\delta>0)，指数次主导项最终远小于 (\delta\rho^m)，故实际符号相异只可能位于 (|\cos|\le\delta) 的相位带；该带自然密度随 (delta\downarrow0) 趋于零。(C_kp_2>0)，所以 (D_m(k)) 的两种符号自然密度各等于1/2。

## 6. 实验及边界

实测程序输出：
- `R552_RAW_H_PASS`：22项冻结系数双实现恒等式；
- `R552_EXACT_ROUCHE_PASS`：21个根盘、210对互不相交、最大 Rouché 比 <1/30、主导模 >11、其余 <6；
- `R552_EXACT_MODULAR_CYCLOTOMIC_PASS`：(p=65537)、(deg R=420)、完整 (q\le352800) 中815个候选 gcd、2个独立有限域结果式点值；
- `R552_EXACT_RECURRENCE_PASS`：(0\le m\le1024) 精确递推，正515、负510、零0、相邻换号300次；
- `R552_FIXED_K11_HALF_DENSITY_EXACT_CERT_PASS`：以上证书组合通过。

计算均以精确整数/有理数作最后逻辑判断；有理圆心是外部数值探索之后固定的待检输入，数值寻根结果没有被当成定理。
无限阶结论来自以上两个有限的精确证书与代数/等分布证明。此为作者侧证明；正式独立 Driver 数学审阅和 native CLAIM/Result 仍待实际授权。

下一问题：在 k=12 验证相同主导复根及非分圆条件，并研究可覆盖所有 (k\ge5) 的参数统一模长分离界；保留 (s=3,m=63) 全参数符号分类。
