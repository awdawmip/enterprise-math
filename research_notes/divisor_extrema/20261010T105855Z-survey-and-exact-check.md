# 范围内约数极值与不同质因子极值：文献核对及精确复算

Progress-Event-ID: `divisor-extrema-20261010T105855Z`
At: `2026-10-10T10:58:55Z`
Scope: `enterprise-math / external classical integer arithmetic`
Status: `UNREVIEWED_RESEARCH_NOTE; NO_MATHEMATICAL_ADMISSION`
Global-read: `559e010c0ed821e1f91306f618a27c0771841a81`
EM-source-read: `c13384fa7c378c4a2ddbd27ce0fd17681e73119d`
Research-Activity-ID: `NONE_ALLOCATED; REGISTRATION_PENDING`
Source: 当前用户问题、下列原始文献、本轮整数枚举及独立全量筛法。

## 问题与边界

当前用户问：“研究一个问题，看看有没有类似的研究。一定范围内，因数最多的数有什么规律，不同因子因数最多的数又有什么规律。”

将范围解释为 1<=n<=N；“不同因子”先按不同质因子种类解释，同时研究固定种类数的约数极值。这不是用户确认后的唯一释义。tau(n)为正约数数（含1和自身）；omega(n)为不同质因子数；Omega(n)计重复次数。若用户指任意[A,B]，需单独处理，最小冠军的替换论证可能跌出下界。

本问题是外部经典整数算术，不作心跳世界物理或几何归因，不更改P000。

## 已知结论与本轮重证

n=product(p_i^a_i) 时，tau(n)=product(a_i+1)，omega(n)=k，Omega(n)=sum(a_i)。

D(N)=max_{n<=N}tau(n)。所有并列最优数中的最小者H(N)属于严格高合成数序列。其质数从2开始连续，指数非增。证明：补入遗漏的小质数可在不变tau时减小n；对p<q但a<b的指数交换，把n乘以(p/q)^(b-a)<1，仍不变tau。两步均与最小性矛盾。这些必要条件不适用于所有并列冠军，也并不充分：96符合形状，但60已达到相同的12个约数。

令P_k为前k个质数之积。W(N)=max_{n<=N}omega(n)=max{k:P_k<=N}，最小代表为P_k。任何含k种质数的整数至少为P_k，P_k达到界。其他并列者不必含完全相同的质数，例如42在N=100时也是omega冠军。

固定k：D_k(N)=max_{n<=N,omega(n)=k}tau(n)，最小代表仍满足上述指数形状；D(N)=max_k D_k(N)。这个固定种类数的优化问题已有经典研究，不宣称首创。

增加p的指数a到a+1使tau乘(a+2)/(a+1)，数值乘p；新质数使tau翻倍。局部效率不能代替离散预算下的完整搜索。
连续松弛：令L=log(N P_k)，则D_k(N)<= (L/k)^k / product(log p_i)，来自对(a_i+1)log p_i用AM-GM。近似均衡(a_i+1)log p_i=L/k需要处理a_i>=1和整数取整；不是精确选优公式。

## 精确计算范围与完备性

任意整数的质数/指数排序可映至不更大的规范整数，保持tau和omega。因此枚举首段质数的所有非增正整数指数足以捕获每个范围及每个k的最小冠军。DFS只用整数乘除判界，没有浮点剪枝。

本轮枚举N<=10^18全部32749个规范候选，得到156个严格纪录（含1）。另用“每个d给所有倍数的计数加1”的独立筛法，遍历1至1000000全部整数，并独立筛omega；38个纪录和所有固定k极值完全一致。

可独立重写的DFS核心：
```python
def visit(i, last_a, n, tau, exps):
    rows.append((n, tau, exps))
    p = primes[i]
    m = n
    for a in range(1, last_a + 1):
        if m > LIMIT // p:
            break
        m *= p
        visit(i + 1, a, m, tau * (a + 1), exps + (a,))
# LIMIT=10**18，足够长的首段质数；起点(0,59,1,1,())。
# 实现中另检查质数数组终点。按n升序扫描，仅tau严格超过旧纪录时保留。
```

| N | 最小约数冠军H | D | omega(H) | W | 最小W冠军 |
|---:|---:|---:|---:|---:|---:|
|10|6|4|2|2|6|
|100|60|12|3|3|30|
|1000|840|32|4|4|210|
|10000|7560|64|4|5|2310|
|100000|83160|128|5|6|30030|
|1000000|720720|240|6|7|510510|
|1000000000|735134400|1344|7|9|223092870|
|1000000000000|963761198400|6720|9|11|200560490130|
|1000000000000000000|897612484786617600|103680|12|15|614889782588491410|

固定N=1000000：

|k|最小代表|D_k|按2,3,5,...排列的指数|
|---:|---:|---:|---|
|1|524288|20|19|
|2|995328|78|12,5|
|3|777600|144|7,5,2|
|4|907200|210|6,4,2,1|
|5|831600|240|4,3,2,1,1|
|6|720720|240|4,2,1,1,1,1|
|7|510510|128|1,1,1,1,1,1,1|

N=100的全部tau冠军：60,72,84,90,96。
N=1000000的全部tau冠军：720720,831600,942480,982800,997920。
P7=510510，P8=9699690；2P7=1021020>1000000，故该范围任何7种质数的整数都无平方因子，tau=128。两类冠军在此范围无交集。

首个“纪录上升而种类下降”：
27720=2^3*3^2*5*7*11，tau=96，omega=5；
下一纪录45360=2^4*3^4*5*7，tau=100，omega=4。
不从单个固定N的表推出D_k对所有N都单峰。

## 与2026预印本的有限独立复核

Mantovanelli的arXiv:2608.17045v1研究相邻高合成数的指数盒、只朝终点移动的单位指数步、以及数值不超过下一冠军的路径中，最小tau/tau(H)的最大值（capacity）。本轮复核155个相邻纪录对（两端<=10^18），共1324个指数盒状态；精确有理数DP全部capacity>=1/2，12个等号情形恰好为omega下降情形。静态tau(gcd)/tau(H)>=1/2反而有4个反例，首个48886437600 -> 64250746560，静态4/9，动态14/27。

DP：将两端指数补零到同长，状态r每次向终点推进一个指数单位；排除整数值>H_next的状态。V(start)=tau(H)，V(r)=min(tau(n_r),max_{前驱s}V(s))，capacity=V(end)/tau(H)。无前驱状态不达。所有算术为整数或Fraction。

对盒内z及互补z'=H*H_next/z，逐坐标(a+1)(b+1)<=(x+1)(a+b-x+1)，从而tau(z)tau(z')>=tau(H)tau(H_next)。连续纪录间不能有盒内整数，否则z,z'同在间隙，两者tau<=tau(H)，矛盾。

这只是该预印本定义的有限复算，未超过其自报的10^70检查范围，不是新发现，也不是其无限范围猜想的证明。

## BRC实际复用与信息保留

已读EM固定源 definitions/ENTERPRISE_BRC_WEIGHTED_LOG_FOUNDATION_20260902.md，使用WBRC-T01-CWM-SEMIRING的串联合成计数法，状态为REUSE_APPLIED而非执行原生模块。每个p^a的a+1个单位权支路是(a+1,a+1,1)，按质数作笛卡尔积得到(tau,tau,1)。保留带质数标签的指数以支持后续乘法，不把tau或omega标量当作完整状态。

信息丢失见证：12和18的(tau,omega,Omega)同为(6,2,3)，但乘2后，24有8个约数、36有9个。所需补充的是prime-valuation标签，不是凭空引入物理残差。

## 原始文献与读取范围

1. S. Ramanujan, Highly composite numbers, 1915. 原始论文转录PDF；第2–3节已有固定质数/固定质因子种类优化，第6–8节纪录形状。
   https://ramanujan.sirinudi.org/Volumes/published/ram15.pdf
2. G. Robin, Méthodes d’optimisation pour un problème de théorie des nombres, RAIRO Informatique théorique 17(3), 1983, 239–247. 已读原文：整数规划、动态规划、拉格朗日优化。
   https://www.numdam.org/item/ITA_1983__17_3_239_0.pdf
3. J. L. Nicolas and G. Robin, Majorations explicites pour le nombre de diviseurs de N, Canadian Mathematical Bulletin 26(4), 1983, 485–492. 已核原文公式：Wigert最大阶及显式界。DOI 10.4153/CMB-1983-078-5。
4. M. Mantovanelli, Prime-Exponent Transition Geometry and Divisor Barriers Between Consecutive Highly Composite Numbers, arXiv:2608.17045v1, 2026-08-17. 已读原文和公式；预印本身份，不宣称同行评议。
   https://arxiv.org/pdf/2608.17045

## 登记与下一步

em_session_start(request_id=divisor-extrema-20261010T105114Z-session-start)实际返回STATIC_READONLY_SCOPE_DENIED；operation_sent=false；static_machine_readonly只允许em:access/source:read/control:read。没有分配身份或activity，没有CLAIM、正式任务发布或独立准入。本笔记仅保存研究来源，不声称修复登记。

具体可续接单元：分析D_k(N)联合前沿上的种类减少与指数重排，先与上述既有研究逐项比较，再选真正尚未被覆盖的有限命题。不重复已完成的<=10^18枚举及<=10^6全量筛法。
