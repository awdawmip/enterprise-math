# D25/LIFT — mirror-curvature T_m 的单 Beta-log 证书（第二研究单元）

2026-10-23。TASK_RESEARCH 作者原创推导；EXACT_RATIONAL_IDENTITY / EXPLICIT_MOD_P_PROJECTION / SELF_VERIFIED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SYNC_DEBT。不作 Source CLAIM/checkpoint、正式 Result 或独立审阅。

承接已经回读的独立材料：research_notes/portable_direct/20261023_onhour_d25_BC_mirror_second_digit_transfer.md @ 45f127fee1f2f506fee5b448f90acebcf0fe17d4。固定 Research 来源 lane chatgpt-research-onhour-enterprise-math-20260923；区别于 maintenance。D25 母 Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT / TP2-B6F4FC938FF94941C1B7，原 canonical freeze/source pin c47e13e4aba0e006366f989d6334d443f6333ae3 保持冻结。账户阅读基准 GLOBAL_KNOWLEDGE_V1 main@6a791715af63fdb1a7f291c976f3c1baf97cac6f，P000 ACTIVE_LOCKED。

## 1. 精确科学问题

上一研究单元证明 LOW 的镜像二阶重写不能逐项拆开： 
\[
\frac{X_{0,m}-X_{0,m}^\sharp}{p}\equiv -\frac{T_m}{3},\qquad 
Z_m-Z_m^\sharp\equiv+\frac{T_m}{3}\pmod p
\]
的加法必须发生在 divided digit 之后，其中
\[
b_n=\frac{(-1)^n}{2^n}\binom mn,\quad w_n=6n-1,\quad
V_{2,n}=H_{2m+n}^{(2)}-H_{2m}^{(2)},\quad
T_m=\sum_{n=0}^{m}b_nw_nV_{2,n}.
\]
\(T_m\) 一般并不为零。现在真正将它从 **带权调和二次差的 n-和**压成 **一个独立 Beta-log 端口**，而不是扩大旧素数端点的有限测试。

## 2. 全体 m 正整数的 exact theorem

令 p=6m+1（这小节无需素数性），定义多项式
\[
F_m(t):=\sum_{n=0}^{m}b_nw_n t^n,\quad
P_m(t):=(1-t/2)^{m-1},
\quad R_m(t):=\frac{tP_m(t)-2^{1-m}}{1-t}.
\]
分子 t=1 时为零，因此 \(R_m\) 是次数至多 m-1 的**真正有理系数多项式**，不是奇异有理函数。

**新结果（exact curvature-to-Beta identity）**：
\[
\boxed{
T_m=\int_0^1 t^{2m}(-\log t)
\left[P_m(t)+\frac p2R_m(t)\right]\,dt.}
\tag{CURVATURE-BETA-EXACT}
\]
同时，若
\[
a_{m,j}=\frac{(-1)^j}{2^j}\binom{m-1}{j},\qquad
r_{m,j}=-2^{1-m}+\sum_{k=0}^{j-1}a_{m,k}
\quad(0\le j<m),
\]
空和取零，则有完全有限的显式有理数证书
\[
\boxed{
T_m=I_m+\frac p2E_m,\qquad
I_m:=\sum_{j=0}^{m-1}\frac{a_{m,j}}{(2m+j+1)^2},\quad
E_m:=\sum_{j=0}^{m-1}\frac{r_{m,j}}{(2m+j+1)^2}.
}\tag{CURVATURE-FINITE}
\]
这是一条**所有正整数 m 的恒等式**，没有将模 p 的观察器提前误作精确等式。

特别地，p=6m+1 为素数时，所有 \(2m+j+1\le3m<p\)，从而
\[
\boxed{
T_m\equiv I_m
=\sum_{j=0}^{m-1}
\frac{(-1)^j\binom{m-1}{j}}{2^j(2m+j+1)^2}
\pmod p.}\tag{CURVATURE-MOD-P}
\]
它把 mirror second-digit 的关键非零端口降低为一个 **没有 harmonic differences 或 nested sums 的长度 m 单和**；可直接送入 contiguous/Beta 求导，不需要对 B/C 二阶项作未经证明的相消。

## 3. 推导全过程

由有限二项式定理和算子 \(6t\partial_t-1\)，直接得到
\[
F_m(t)=\left(6t\partial_t-1\right)(1-t/2)^m
=-(1-t/2)^{m-1}\left[1+\left(3m-\frac12\right)t\right].
\]
由 \(p=6m+1\) 代入 \(3m-1/2=p/2-1\)，因此
\[
\boxed{F_m(t)=-P_m(t)[(1-t)+pt/2],\quad F_m(1)=-p\,2^{-m}.}\tag{BINOM-PORT}
\]
另一方面 \(V_{2,n}=\sum_{j=1}^{n}(2m+j)^{-2}\)，有限 Euler 积分 \(\int_0^1t^{k-1}(-\log t)\,dt=k^{-2}\) 证明
\[
V_{2,n}=\int_0^1 t^{2m}(-\log t)\frac{1-t^n}{1-t}\,dt.
\]
将它代回 \(T_m\) 并交换有限求和与积分（在 t=1 的因子可去）：
\[
T_m=\int_0^1 t^{2m}(-\log t)\frac{F_m(1)-F_m(t)}{1-t}\,dt.
\]
利用 BINOM-PORT，整分式**精确多项式化**：
\[
\frac{F_m(1)-F_m(t)}{1-t}
=P_m(t)+\frac p2\frac{tP_m(t)-P_m(1)}{1-t}
=P_m(t)+\frac p2 R_m(t).
\]
这证明 CURVATURE-BETA-EXACT。将 \(P_m(t)=\sum_{j=0}^{m-1}a_{m,j}t^j\) 与
\(R_m(t)=\sum_{j=0}^{m-1}r_{m,j}t^j\) 展开，用
\((1-t)R_m(t)=tP_m(t)-P_m(1)\) 比较系数即有所列 \(r_{m,j}\)；逐项求 Beta-log 积分得到 CURVATURE-FINITE。最后应用所有分母的 p-单位性质得到 CURVATURE-MOD-P。

**精度信息非常明确**：在 mod p 上可以删除 \(\frac p2E_m\)，但在任何 mod p² 或 higher-digit 工作中必须保留它。本定理不依赖 611 素数端点计算，也未改变原 benchmark 条件。

## 4. 可重演精确计算、非零 witness

使用标准 Python 3 Fraction，一路直接计算 \(T_m\) 的 harmonic sum，另一路计算 \(I_m,E_m\) 的多项式系数表达。m=1,...,19 每个数均严格有理相等。所测 p=6m+1<200 的 20 个素数上进一步检验 \(T_m\equiv I_m\bmod p\)，全部通过；这些有限测试只核查推导，不构成全素数证明。

实例（都是精确有理数，非浮点）：
\[
m=1:\quad T_1=-5/18,\ I_1=1/9,\ E_1=-1/9;
\]
\[
m=2:\quad T_2=-49/3600,\ I_2=47/1800,\ E_2=-11/1800;
\]
\[
m=3:\quad T_3=84145/2032128,\ I_3=1999/254016,\ E_3=3587/1016064.
\]
冻结目标的 \(p=13,m=2\) 上 \(T_m\equiv10\pmod{13}\)（\(T_m/3\equiv12\)），\(p=19,m=3\) 上 \(T_m\equiv16\pmod{19}\)（\(T_m/3\equiv18\)），可见镜像 curvature 不是可忽略误差。

最小复核代码：
~~~python
from fractions import Fraction as Q
from math import comb
def H2(k):
    return sum((Q(1,j*j) for j in range(1,k+1)),Q(0))
def residue(x,p):
    return x.numerator*pow(x.denominator,-1,p)%p
for m in range(1,33):
    p=6*m+1
    a=[Q((-1)**j*comb(m-1,j),2**j) for j in range(m)]
    r=[-Q(1,2**(m-1))+sum(a[:j],Q(0)) for j in range(m)]
    I=sum((a[j]/(2*m+j+1)**2 for j in range(m)),Q(0))
    E=sum((r[j]/(2*m+j+1)**2 for j in range(m)),Q(0))
    T=sum((Q((-1)**n*comb(m,n),2**n)*(6*n-1)*(H2(2*m+n)-H2(2*m))
           for n in range(m+1)),Q(0))
    assert T==I+Q(p,2)*E
    if not any(p%d==0 for d in range(2,int(p**.5)+1)):
        assert residue(T-I,p)==0
print("m=1..32 exact identity; 20 prime residue checks: PASS")
~~~

## 5. BRC/Observer 与接续

BRC 的 carrier 是带来源的 signed binomial 支路 \(b_n\)；\(w_n\) 是固定 observable，\(T_m\) 是 V2 曲率端口；\(F_m\) 将原 n 标签的信息汇聚到多项式，但 CURVATURE-BETA-EXACT 证明了对当前唯一所需的 \(T_m\) 读出无损。高段 \(r,\varepsilon_r,h_r\) 并未因此被删除。REUSE_APPLIED + COMPOSE_APPLIED；不把有符号相消偷换为正质量守恒，也不把数学式推广为原生 X6 空间动力学。

**下一最小数学动作**：把上一笔记的 J-HEAD-BRIDGE 用真实 BA/INT 权重代入 reflected r<=m，构造与本轮 \(I_m\) 在同一区间的 Beta-log 核（变换 t=2x 后 \(I_m=2^{2m+1}\int_0^{1/2} x^{2m}(1-x)^{m-1}[-\log(2x)]dx\)），再以 \(r>m\) 的保留尾检查是否出现完整 joint cancellation。源中的 \(J_m^{(2)},V_m,\mathcal A_m\Theta_m\) 仍需同时检查；CURVATURE-MOD-P 并未证明 LOW-MIRROR=0 或 LIFT/EP。

保留恢复上下文：Research bridge #6186 recovery_status 为未认证的本地 ACTIVE 投影且没有 CLAIM/run，#6187 exact continuation 拒绝先决条件，#6188 dispatch 最终 TimeoutExpired；enterprise-math #1539 追踪同一签名。Sites 0.6.11 目前 research_authority_granted=false，仅能向已有授权 GitHub surface 提交中立数学证据；无正式 Source checkpoint/Result/Driver review/native benchmark。任务保留启用，未修改 scheduler/通知。
