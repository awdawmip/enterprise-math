# D25/LIFT — BC 镜像二阶 jet 与 divided-digit 成对保真

日期：2026-10-23。分类：TASK_RESEARCH portable mathematics；AUTHOR_DERIVED / EXACT_RATIONAL_SELF_CHECK / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SYNC_DEBT。不是 native CLAIM/checkpoint/Result，不是独立审阅，不是 native benchmark。

来源：既有 Research lane 的逻辑标识 chatgpt-research-onhour-enterprise-math-20260923（仅追溯来源，不作为服务授权）。母目标 RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT，Task TP2-B6F4FC938FF94941C1B7。原冻结任务 Source pin c47e13e4aba0e006366f989d6334d443f6333ae3 **不变**；本轮非正式成果不能改变它。研究使用 GLOBAL_KNOWLEDGE_V1 main@6a791715af63fdb1a7f291c976f3c1baf97cac6f 和 P000 ACTIVE_LOCKED 作为适用项目上下文，不把外部有理恒等式包装为原生 X6/物理证明。此前 WZ/B11、D24 frozen、LOW/Beta 线性层与纯 A 块消去、611 素数端点枚举均作为现成证据消费，不重做。

## 1. 母问题与本轮定理（全部目标素数）

设 m>=1、p=6m+1 是素数，0<=n<=m，并记
\[
\begin{aligned}
A_n&=H_m-H_{m-n},& A_{2,n}&=H_m^{(2)}-H_{m-n}^{(2)},\\
U_n&=H_{2m}-H_{2m-n},& U_{2,n}&=H_{2m}^{(2)}-H_{2m-n}^{(2)},\\
C_n&=H_{4m}-H_{4m-n},& C_{2,n}&=H_{4m}^{(2)}-H_{4m-n}^{(2)},\\
V_n&=H_{2m+n}-H_{2m},& V_{2,n}&=H_{2m+n}^{(2)}-H_{2m}^{(2)}.
\end{aligned}
\]
各调和项、2、3 的分母均为 p-单位。已有 LOW 负整数参数展开：
\[
L_n=-\frac12A_n+\frac23U_n+\frac13C_n,\quad
M_n=\frac12L_n^2-\frac18A_{2,n}+\frac49U_{2,n}+\frac5{18}C_{2,n}.
\]
**新结果一（镜像局部二阶 jet）：** 定义
\[
\Lambda_n=2U_n-V_n,\qquad L_n^\sharp=-\frac12A_n+\frac13\Lambda_n,
\]
\[
\boxed{ M_n^\sharp=
\frac18(A_n^2-A_{2,n})+
\frac1{18}\Lambda_n(\Lambda_n-3A_n)+
\frac49 U_{2,n}-\frac1{18}V_{2,n}. }\tag{MIRROR-M}
\]
则对 **每个** 0<=n<=m：
\[
\boxed{1+pL_n+p^2M_n
\equiv1+pL_n^\sharp+p^2M_n^\sharp\pmod{p^3}.}\tag{MIRROR-JET}
\]
关键是 V_{2,n} 的净系数 **-1/18**；不能在旧 M_n 中直接以 C_n=-V_n、C_{2,n}=V_{2,n} 代换后忽略 L_n 的 p-阶镜像修正，否则会得到错误的 +5/18。

## 2. 全 n 的完整证明（非计算外推）

逐项将 4m-j=p-(2m+1+j) 反射（j=0,...,n-1），定义镜像正侧序列 q_j=2m+1+j。所有 q_j<p，故 p-进几何级数合法：
\[
C_n=\sum_{j=0}^{n-1}\frac1{p-q_j}
\equiv -V_n-pV_{2,n}\pmod{p^2},\qquad
C_{2,n}\equiv V_{2,n}\pmod p.\tag{MIRROR-REFLECT}
\]
因此 L_n\equiv L_n^\sharp-\frac p3 V_{2,n}\pmod{p^2}，而以 C_n=-V_n、C_{2,n}=V_{2,n} 在旧 M_n 中做模 p 运算，得到
\[
M_n\equiv
\frac18(A_n^2-A_{2,n})
+\frac1{18}\Lambda_n(\Lambda_n-3A_n)
+\frac49U_{2,n}+\frac5{18}V_{2,n}
\equiv M_n^\sharp+\frac13V_{2,n}\pmod p.
\]
将两式分别乘 p 和 p² 后，相反号的 p²V_{2,n}/3 **精确抵消到模 p³**，即 MIRROR-JET。证明适用于所有 p=6m+1 素数；不依赖检测素数集合、独立审阅或未知猜想。

## 3. 真正关联 LOW/Beta divided digit 的成对转移

保留原材料的 b_n=(-1)^n binom(m,n)/2^n, w_n=6n-1；\mathcal R_n(F) 是先前证明的高段 Beta adjoint，不改写其含义。原标量：
\[
X_{0,m}=2^{-m}+\sum_{n=0}^mb_nw_n\left(L_n+\tfrac12\mathcal R_n(1)\right), 
\quad
Z_m=\sum_{n=0}^mb_n\left[2L_n-\tfrac12\mathcal R_n(1)+w_n(M_n+\tfrac12\mathcal R_n(J))\right].
\]
用 L_n^\sharp、M_n^\sharp 同步替换，得到 X_{0,m}^\sharp,Z_m^\sharp。定义仍需保留的精确有理矩
\[
T_m=\sum_{n=0}^{m}b_nw_nV_{2,n}.
\]
因为没有对 \mathcal R_n 进行任何近似，上节逐项公式立即导出
\[
\boxed{X_{0,m}-X_{0,m}^\sharp\equiv-\tfrac p3T_m\pmod{p^2},\qquad
Z_m-Z_m^\sharp\equiv\tfrac13T_m\pmod p.}\tag{PAIR}
\]
于是两个 digit 合并后才有
\[
\boxed{\frac{X_{0,m}-X_{0,m}^\sharp}{p}+Z_m-Z_m^\sharp\equiv0\pmod p.}\tag{PAIR-CANCEL}
\]
这一除法是在 \mathbb Z_{(p)} 中对实际 p-可除差进行，**不能**先在模 p 中将 X_0 差抹掉。

令 \mathcal A_m=(p-1)!/[3^{p-1}(2m)!^3]，\chi_p=((4/3)^{p-1}-1)/p。已接纳 first digit 仅用于保证 (\mathcal A_mX_{0,m}-1)/p 的 p-integrality；PAIR 表明 (\mathcal A_mX_{0,m}^\sharp-1)/p 同样可定义，并严格有
\[
\boxed{
\frac{\mathcal A_mX_{0,m}-1}{p}+\mathcal A_mZ_m-\chi_p
\equiv
\frac{\mathcal A_mX_{0,m}^\sharp-1}{p}+\mathcal A_mZ_m^\sharp-\chi_p
\pmod p.}\tag{LOW-MIRROR}
\]
它是 **整个剩余 LOW deficit 的保真等价换元**，不是把缺项设为零，更不是 LIFT/EP 全素数完成。此前纯 A 块 PARITY 公式继续可用于 MIRROR-M 的第一项；待证部分直接集中在 \Lambda_n(\Lambda_n-3A_n), U_{2,n}, V_{2,n} 与 \mathcal R(J) 的配对上。

## 4. 第二个新精确端口：reflected harmonic 头部直接接 L-sharp

沿用原高段 J_r 的分解 J_r=J_r^{\rm harm}+3/[2(3r-1)]，其中
\[
J_r^{\rm harm}=\frac12(H_{r-1}-H_m)+\frac23(H_{2m}-H_{d_r})+\frac13(H_{4m}-H_{3m-r}),
\quad d_r=m-r\ (1\le r\le m).
\]
作与高段 r<=m 对应的无损重标记 r=m-n（0<=n<m），则 3m-r=2m+n；与镜像 V_n 具有**同一个右侧 harmonic 端口**。逐项合并得到对所有 m,n 的**精确有理数恒等式**：
\[
\boxed{
J_{m-n}^{\rm harm}
=L_n^\sharp-\frac1{2(m-n)}
+\frac23(H_{2m-n}-H_n)
+\frac13(H_{4m}-H_{2m}),
\qquad0\le n<m.}\tag{J-HEAD-BRIDGE}
\]
这不是假设两段的 weights 可直接相消；真正高段的 h_r、\varepsilon_r、Beta adjoint 与 r>m 的后继尾必须继续保留。它只确认 r<=m 头部与本轮 mirror low jet 共享 V_n 端口，从而给出下一轮有限矩相消的精确索引对齐。

## 5. 精确自检与有效范围

使用 Python 3 Fraction + 整数逆元（没有浮点），对 **20 个** p=6m+1<200 的素数、每个 0<=n<=m，核验 MIRROR-REFLECT、L/M 分别模 p²/p、MIRROR-JET 模 p³；并对每个 0<=n<m 核验 J-HEAD-BRIDGE 的有理严格相等。20 个素数均通过，未检出失败：
p=7,13,19,31,37,43,61,67,73,79,97,103,109,127,139,151,157,163,181,193。

特别地，T_m/3 mod p 对两个冻结目标类：
p=13,m=2 为 12，p=19,m=3 为 18。两者均不为零，说明分开投影 L 和 M 会确实丢失第二位，必须使用 PAIR-CANCEL。更广泛的 witness：
p=7:6, 13:12, 19:18, 31:2, 37:34, 43:25, 61:11, 67:66, 73:28, 79:15。

最小可重演校验（同时核验独立的原始 gamma/rising-factorial 低段比率）：
~~~python
from fractions import Fraction as Q
from math import comb

def H(n,s=1):
    return sum((Q(1,j**s) for j in range(1,n+1)),Q(0))
def red(x,q):
    return x.numerator*pow(x.denominator,-1,q)%q
def rise(x,n):
    a=Q(1)
    for j in range(n): a*=x+j
    return a
for m in range(1,33):
    p=6*m+1
    if any(p%d==0 for d in range(2,int(p**.5)+1)):continue
    T=Q(0)
    for n in range(m+1):
        A=H(m)-H(m-n); A2=H(m,2)-H(m-n,2)
        U=H(2*m)-H(2*m-n); U2=H(2*m,2)-H(2*m-n,2)
        C=H(4*m)-H(4*m-n); C2=H(4*m,2)-H(4*m-n,2)
        V=H(2*m+n)-H(2*m); V2=H(2*m+n,2)-H(2*m,2)
        L=-A/2+Q(2,3)*U+C/3
        M=L*L/2-A2/8+Q(4,9)*U2+Q(5,18)*C2
        Ls=-A/2+(2*U-V)/3
        Ms=(A*A-A2)/8+(2*U-V)*(2*U-V-3*A)/18+Q(4,9)*U2-V2/18
        assert red(C+V+p*V2,p*p)==0
        assert red(p*(L-Ls)+p*p*(M-Ms),p**3)==0
        T+=Q((-1)**n*comb(m,n),2**n)*(6*n-1)*V2
        if n<m:
            r=m-n
            Jh=(H(r-1)-H(m))/2+Q(2,3)*(H(2*m)-H(m-r))+(H(4*m)-H(3*m-r))/3
            bridge=Ls-Q(1,2*(m-n))+Q(2,3)*(H(2*m-n)-H(n))+(H(4*m)-H(2*m))/3
            assert Jh==bridge
        if p<=103:
            native=(rise(-m+Q(p,2),n)/rise(-m,n)
                *rise(-2*m+Q(p,3),n)/rise(-2*m+p,n)
                *rise(-4*m+Q(2*p,3),n)/rise(-4*m+p,n))
            assert red(native-(1+p*Ls+p*p*Ms),p**3)==0
    assert red(T/3,p)==sum((Q((-1)**n*comb(m,n),2**n)*(6*n-1)*(H(2*m+n,2)-H(2*m,2))/3 for n in range(m+1)),Q(0)).numerator*pow(sum((Q((-1)**n*comb(m,n),2**n)*(6*n-1)*(H(2*m+n,2)-H(2*m,2))/3 for n in range(m+1)),Q(0)).denominator,-1,p)%p
print("20 primes, all low n, mirror + J head + selected original-ratio crosscheck: PASS")
~~~

注意：最后一个重复构造 T/3 的断言只作 Fraction arithmetic 的内部一致性检查，非第三方独立审阅。普遍性来自第 2、3、4 节的代数证明，不来自 20 素数覆盖。

## 6. BRC 信息、未完成证据与下一精确动作

**REUSE_APPLIED + COMPOSE_APPLIED**：carrier 是已有 n=0..m 的 signed rational binomial branch b_n，附带 p-adic valuation、low/high 原来源及镜像 q_j=2m+1+j；observer 为 w_n、p³ 二阶 jet 和先除 p 的 LOW scalar。MIRROR-REFLECT 是有明确精度的有损替换，但 PAIR-CANCEL 证明在该 observer 下总体保真；不把有符号抵消当非负 BRC mass，也不作未证的 X6 本体转移。

尚未完成：把 J-HEAD-BRIDGE 插入真实的 reflected Beta h_r kernel 并与 \Lambda_n 二阶及两个曲率 U2,V2 的**完整加权积分/有限和**配对，连同 r>m 尾、divided first digit，最后证明或反驳 LOW-MIRROR 模 p。此文件**不**证明 EP/LIFT，不代表 original native benchmark 执行，也没有审阅或 Source checkpoint。不能将辅助项局部消去冒称主实验完成。

**下一精确动作**：严格沿用已证 BA/INT 的权重，把 reflected harmonic 的 r<=m 部分经 J-HEAD-BRIDGE 搬到 low mirror ports，并保留 r>m 原始 e_r；检验由 T_m/3 导致的第二位配对能否同 Beta adjoint 抵消。优先得到完整 joint residual 的可验证单标量，若剩余非零只报告条件差/实际反例。已有 611 素数 endpoint 枚举、纯 A 块、WZ/B11 proof 不重做。原 frozen source pin、native benchmark、独立审阅及 Source 本身保持不变。

**实际控制恢复**：原 Research lane 的 bridge #6186（recovery_status SUCCEEDED，但 ACTIVE 仅本地投影、source_authority_verified=false、无 CLAIM/run）、#6187（exact continuation PREREQUISITE_NOT_SUCCEEDED）、#6188（dispatch 最终 FAILED/TimeoutExpired）已回读，不重复副作用；#1539 仍负责旧 session-start/Source 先决条件。当前 Sites 0.6.11 客户端只读，research_authority_granted=false，本文件仅是已授权 GitHub 中立科研材料。未获得 native Researcher 权限时保留 REGISTER_PENDING/SYNC_DEBT，不借维护 lane，也不因接口错误永久停止可移植数学。
