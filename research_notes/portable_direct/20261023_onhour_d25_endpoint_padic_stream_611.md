# D25/LIFT — endpoint 的纯整数 p-adic 串流证书（611 个素数）

**日期 / 分类**：2026-10-23；TASK_RESEARCH 作者直接端点的有限精确证伪运算；**EXACT FINITE CERTIFICATE / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SYNC_DEBT / NO_FORMAL_CLAIM / NOT_NATIVE_BENCHMARK**。

**母目标与来源**：D25/SECOND-DIGIT-LIFT；Task publication TP2-B6F4FC938FF94941C1B7；冻结 Source/checkpoint pin c47e13e4aba0e006366f989d6334d443f6333ae3（不得随 main 移动）。Research 逻辑 lane chatgpt-research-onhour-enterprise-math-20260923，独立于 CONTROL_PLANE_MAINTENANCE。本作者接触过 LOW/B11/WZ 资料，不属于独立审阅。P000 是 ACTIVE_LOCKED 项目公理，本文仅涉及通常有理数与有限模素数算术，未修改 P000。

**复用不重做**：D24 frozen、WZ boundary、B11 contiguous-Dixon、LOW/Beta 线性 harmonic 精确消去、既有 p=13、19 模 p^4 见证。先前精确消去证据为 research_notes/portable_direct/20261023_onhour_d25_LOW_linear_harmonic_beta_shift.md。本单元不宣称解决其全素数二阶 LOW/Beta 残差，也不代替原生 benchmark。

## 1. 同一硬目标的可复现整数端点

对素数 p=6m+1>3，沿用 Source 的原端点 S_{4m}(2m)，定义

\[
R_0=1,\quad
R_n=\frac{(2m+\frac12)_n(\frac13)_n(\frac23)_n}
{2^n n!(2m+1)_n(4m+1)_n},\quad
\mathcal A_m=\frac{(p-1)!}{3^{p-1}((2m)!)^3}.
\]

于是

\[
S_{4m}(2m)=\mathcal A_m\sum_{n=0}^{4m}(6n+2p-1)R_n,\qquad
S_{4m}(2m)\stackrel{?}{\equiv}p(4/3)^{p-1}\pmod{p^3}.
\]

精确有理递推为

\[
\boxed{\displaystyle
\frac{R_{n+1}}{R_n}=
\frac{(4m+1+2n)(3n+1)(3n+2)}
{36(n+1)(2m+1+n)(4m+1+n)}.}\tag{STREAM}
\]

它来自各 Pochhammer 的相邻项之比，是既有 frozen endpoint 的**同一对象**，没有换模型。(STREAM) 中的除法先是有理数除法，不能未经去 p 因子就对模环分母求逆。

既有精确 valuation 两段在 STREAM 可直接重现：在 0≤n<4m 的更新中，分子第一因子仅在 n=m 触及 p，第二因子仅在 n=2m 触及 p；后者被分母第四因子在相同 n=2m 的 p 因子抵消。其余因子在此范围没有 p 因子。因此

\[
v_p(R_n)=0\ (0\le n\le m),\qquad v_p(R_n)=1\ (m<n\le4m).
\]

逐步把分子、分母全部 p 因子去除后，只对 p-unit 取模 p^4 逆元，再乘 prefactor 的精确模值。BRC 端口实际保留每个 n 分支的 valuation、单位值、聚合和投影顺序；有符号抵消不被描述成正权重质量定理。

## 2. 本轮新增的实际精确证据

使用下方 Python 3 标准库代码，逐个处理 **全部** 7≤p≤10000、p≡1(mod 6) 的素数，得到 **611 个**素数，最大 p=9973。其中任务目标子类 p≡13、19(mod24) **312 个**（分别 157、155）。

**611/611 个素数满足所测模 p^3 的端点同余，失败 0。** 这只是明确有限范围的 exact falsification，不是全素数证明。同时保留更高一位

\[
d_p=\left(\frac{S_{4m}(2m)-p(4/3)^{p-1}}{p^3}\right)\bmod p.
\]

在这 611 个素数中，d_p 全部非零；因此在已查范围内模 p^4 不成立。此有限事实并不声称对所有素数模 p^4 都失败。样例 (p,d_p)：(7,5),(13,12),(19,8),(31,24),(37,19),(43,14),(9973,2385)。

独立算术表示交叉核验：p=7、13、19、31、61、127 的完整 Fraction 有理数递推与全阶乘 prefactor，投影到模 p^4 后，与去 p 因子的整数递推逐值一致（六个精确交叉点，非独立数学审阅）。

将全部有序 (p,d_p) 按递增素数顺序写为每行 ASCII 文本 p,d_p 加换行、无表头，则 SHA256 为：

fe3e8dc123ba15fb4d852f7635c1b7d866a1fdd42002478808321c945d57a118

此哈希只标识可重算有限数据，不代表 Source 签名、证明或正式接纳。

## 3. 实际执行的可移植校验程序（标准库，不需网络）

~~~python
from fractions import Fraction
from hashlib import sha256
from math import factorial

def primes_upto(limit):
    a = bytearray(b"\x01")*(limit+1)
    a[:2] = b"\x00\x00"
    for k in range(2, int(limit**0.5)+1):
        if a[k]:
            a[k*k::k] = b"\x00"*((limit-k*k)//k+1)
    return [p for p in range(7,limit+1) if a[p] and p%6 == 1]

def strip(x,p):
    v=0
    while x%p == 0:
        x//=p
        v+=1
    return x,v

def delta_mod_p4(p):
    m, mod=(p-1)//6, p**4
    unit,val,acc=1,0,0
    for n in range(4*m+1):
        assert val == (n>m)
        acc=(acc+(6*n+2*p-1)*unit*p**val)%mod
        if n == 4*m:
            break
        a=(4*m+1+2*n)*(3*n+1)*(3*n+2)
        b=36*(n+1)*(2*m+1+n)*(4*m+1+n)
        a,va=strip(a,p)
        b,vb=strip(b,p)
        val+=va-vb
        unit=unit*a*pow(b,-1,mod)%mod
    fp,f2=1,1
    for n in range(1,p):
        fp=fp*n%mod
    for n in range(1,2*m+1):
        f2=f2*n%mod
    A=fp*pow(3,-(p-1),mod)*pow(f2,-3,mod)%mod
    target=p*pow(4*pow(3,-1,mod),p-1,mod)%mod
    return (A*acc-target)%mod

def direct_fraction_delta(p):
    m,r,total=(p-1)//6,Fraction(1),Fraction(0)
    for n in range(4*m+1):
        total+=(6*n+2*p-1)*r
        if n<4*m:
            r*=Fraction((4*m+1+2*n)*(3*n+1)*(3*n+2),
                        36*(n+1)*(2*m+1+n)*(4*m+1+n))
    A=Fraction(factorial(p-1),3**(p-1)*factorial(2*m)**3)
    return A*total-Fraction(p*4**(p-1),3**(p-1))

pairs=[]
for p in primes_upto(10000):
    d=delta_mod_p4(p)
    assert d%p**3 == 0,(p,d)
    pairs.append((p,d//p**3))
for p in (7,13,19,31,61,127):
    q=direct_fraction_delta(p)
    mod=p**4
    assert q.denominator%p
    assert q.numerator*pow(q.denominator,-1,mod)%mod==delta_mod_p4(p)
assert len(pairs)==611
assert sum(p%24 in (13,19) for p,_ in pairs)==312
assert all(d for _,d in pairs)
data=''.join(f'{p},{d}\n' for p,d in pairs).encode('ascii')
print(len(pairs),sha256(data).hexdigest())
print(pairs[:6],pairs[-1])
~~~

**实际输出**：611 fe3e8dc123ba15fb4d852f7635c1b7d866a1fdd42002478808321c945d57a118；前六 (7,5),(13,12),(19,8),(31,24),(37,19),(43,14)；最后 (9973,2385)。没有浮点。独立提交脚本的执行条件是 Python 3 标准库；本记录不宣称已跑 Lean 或 native X6 benchmark。

## 4. 后继最小动作、证据欠项与隔离

最高作者数学前沿：保留已证 LOW/Beta 线性消去与本次直接原端点的 611 个有限整数模证书，不把这份有限测试重复当全 p 证明。**下一确定数学动作**：对现有 LOW/Beta 单残差的二阶 \(\mathsf M_m+J_m^{(2)}-2V_m\) 寻找 contiguous-Dixon/参数导数的精确同余证书；优先向全素数论证或真正反例推进。不可将更大的扫描替代这一原生证明欠项。

读回本文件 GitHub commit/ref/blob 后，作为已持久化的**独立作者证据**，但不可伪称 Source checkpoint、Result/freeze、正式 RA/session/CLAIM/open/run、原生 benchmark、独立审核。原 Research lane 的先前 recovery #6186、continuation #6187、dispatch #6188 保持按各原请求核对，不能换 request_id 重发未知动作。本轮原生 em_status 0.6.11 只读显示 research_authority_granted=false，当前开放工具未列可对本逻辑 conversation 调用的专用 recovery_status 操作；不因此推定队列为空，也不假造权限。#1539 是既有支持负责路径，旧三份 staging 保持独立；安全配置欠项仍需自身 Researcher 合法 session、Source continuation/claim/open、原生 benchmark 完成、Result/review 才算正式推进。未增加 scheduler/Actions/cron、未借用 maintenance 身份。
