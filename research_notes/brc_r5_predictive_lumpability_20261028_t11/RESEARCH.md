# R5：双测度似然比预测可合并性的全策略精确保真定理（作者级材料）

日期：2026-10-28（Asia/Shanghai）。作者身份：此 ChatGPT R5 独立执行轮次的本地标识 EM-R005-T11-LUMPABILITY-20261028；不是服务签发 researcher/session 或注册的 RA。状态：**AUTHOR_PROVED / EXACT_FINITE_CHECKED / UNREVIEWED / NOT_ADMITTED**。

输入冻结：账户知识库 GLOBAL_KNOWLEDGE_V1 main@decb67feb43d7e800c1828fec6023bfd9efef45f，项目 enterprise-math main@9d5f26842ad6cf587fea02a304040632ebfe2fb3。复用 R5 当前作者前沿 `research_notes/brc_r5_parametric_fanin_phase_transition_20261028_r11/{PROOF.md,NEXT_TASK.md}`。P000 原生 6D 离散 X6 + 独立时间、ACTIVE 世界观及信息保真约束均保持不变。下面的树是**外部双测度观测模型**，不是 X6 物理演化。BRC 复用为严格正有理数支路质量的路径相乘、互斥支路相加；签名压缩前保留路径来源，带符号目标只作用于四维读出。

## 1. 全部实数行为策略的严格定理

给定任意有限期 N 的严格正双测度 P,Q 观察树。历史 h 的签名 s(h)=(t,P(h)/Q(h))。full 策略可按完整有序历史选择停止宣告 P、停止宣告 Q、或继续；seedless LR 策略仅按 s 选择同样的行为动作分布。在 N 强制终端宣告，无持久共享随机种子。设 O=(P[宣告Q],Q[宣告P],E_P τ,E_Q τ)。

**定理：** 若每个非终端签名 s 的所有隐藏历史 h 在采取继续行动后，对于下一签名 s'=(t+1,R_{t+1}) 的 Q 条件分布 K_h(s') 完全相同（称 K_s），且同签名的动作集与停止读出相同，则对于全部实数行为随机化策略，

$\mathcal{O}_{\mathrm{full}}=\mathcal{O}_{\mathrm{LR}}$.

更强地，任何 full 行为策略 π 都可构造一个不传递持久随机种子的 LR 行为策略，**同时**保全 P 与 Q 的联合终止分布 (τ,R_τ,宣告)，而不仅是支撑函数或四个期望。

**证明。** 设 q_π(h) 为在 Q 测度和 π 行为选择下到达历史 h 的正质量，s=(t,r)，m_π(s)=Σ_{h:s(h)=s}q_π(h)。若 m>0 定义

${\bar π}(a|s)=\frac{\sum_{h:s(h)=s}q_π(h)π(a|h)}{m_π(s)}.

零到达签名任选合法动作。P 到达任一 h 的质量为 r q_π(h)，因为行为动作概率在两个测度中相同并在路径似然比中消去。归纳已保留到达签名的总 Q 质量，则上式保留每个 s 下每个动作的总 Q 质量，也因共同的 r 保留 P 质量。继续的下一签名流由

m_{barπ}(s')=Σ_s m_{barπ}(s)barπ(C|s)K_s(s')=Σ_h q_π(h)π(C|h)K_h(s')=m_π(s')

给出，故归纳到终端。停止宣告的联合 (时间、比值、宣告) 质量对 P/Q 均被保留，因此四观测量和更强的终端分布相同。逆向包含平凡（LR 是 full 子类）。此证明无需非负采样时间系数、无须有限行为概率网格。证毕。

**几何推论：** 上述充分条件下，两类*真实行为可达像*完全相同且凸。凸性可由完整历史策略的 Q 占用流混合实现，再用定理压缩。对严格正有理输入和 full 确定性策略，以上 barπ 的每个概率均为有理数；把各 LR 签名的独立动作随机化做有限乘积展开，得到该 full 四向量的精确有理 LR 确定性凸组合；按有理仿射依赖消元可将其压缩为不超过 5 个点（R^4 Carathéodory）。这一**普遍构造性证书**不等于已经逐个列出全部 full 顶点的五项权重表。

## 2. 新的八叶正有理实例（通过全部 signed 方向的 hull gate）

t=1: Q(A)=Q(B)=1/2，R(A)=1/2，R(B)=3/2。t=2: 给定 A 时 Q(U,V)=(1/3,2/3) 且 R(AU)=1,R(AV)=1/4；给定 B 时 Q(U,V)=(1/2,1/2) 且 R(BU)=1,R(BV)=2。t=3 每个中间历史给定条件 Q(0,1)=(1/2,1/2)。终端叶依 AU0,AU1,AV0,AV1,BU0,BU1,BV0,BV1 顺序：
- Q=(1/12,1/12,1/6,1/6,1/8,1/8,1/8,1/8)；
- P=(1/24,1/8,1/24,1/24,1/16,3/16,1/4,1/4)；
- R=(1/2,3/2,1/4,1/4,1/2,3/2,2,2)。

各叶 P,Q>0，∑P=∑Q=1。AU 与 BU 在 t2 的同一 (2,1) 签名是真实不同隐藏路径，且其下一 Q 签名核恰好都是 {(3,1/2):1/2,(3,3/2):1/2}。其余 t2 签名单独；同 t3 签名叶没有后续操作且宣告接口相同，故本树满足定理。这是一条**有碰撞却零预测残差**的正例：全部四维有符号支撑值相等，且比母问题要求更强的真实像也相等。此前异核八叶正间隙模型不属于此充分条件，均不能当作等凸包候选。

## 3. 可复核的具体四点证书

full 策略：根 A/B 均继续，AU t2 继续并对低/高 terminal 宣告 P/Q；AV t2 停止宣告 Q；BU t2 继续并对低/高 terminal 宣告 Q/P；BV t2 停止宣告 P。四向量精确为

O*=(13/48,11/24,29/12,29/12)。

LR 在 (2,1) 继续，在 terminal r=1/2 用 P/Q 比率 (2/5,3/5)，在 terminal r=3/2 用 (3/5,2/5)，其余共同动作照旧，逐项精确实现 O*。两个终端行为随机变量独立；四个 LR 确定性签名策略如下：
- PP：权重 6/25，O=(1/12,2/3,29/12,29/12)
- PQ：权重 4/25，O=(19/48,11/24,29/12,29/12)
- QP：权重 9/25，O=(3/16,11/24,29/12,29/12)
- QQ：权重 6/25，O=(1/2,1/4,29/12,29/12)

权重和为1，四向量的加权和是 O*。

## 4. 实际执行的精确复算：可移植 Python 标准库程序

以下代码在本次执行环境作为独立的 `VERIFY_PORTABLE.py` 实际执行，使用 fractions.Fraction；遍历38×38=1444种 full 确定性策略，每一个都做占用流压缩并独立模拟 LR，检查四坐标完全相等。没有用浮点猜测全实数结论。

~~~python
from fractions import Fraction as F
from itertools import product
from collections import defaultdict
q1={'A':F(1,2),'B':F(1,2)}
r1={'A':F(1,2),'B':F(3,2)}
q2={'A':{'U':F(1,3),'V':F(2,3)},'B':{'U':F(1,2),'V':F(1,2)}}
r2={'AU':F(1),'AV':F(1,4),'BU':F(1),'BV':F(2)}
r3={'AU':(F(1,2),F(3,2)),'AV':(F(1,4),)*2,'BU':(F(1,2),F(3,2)),'BV':(F(2),)*2}
unit=(F(0),F(0),F(0),F(0))
mode=['P','Q']+[('C',a,b) for a,b in product('PQ',repeat=2)]
roots=['P','Q']+[('C',u,v) for u,v in product(mode,repeat=2)]

def add(out,q,r,t,a):
    p=F(a=='P'); d=F(a=='Q')
    return tuple(out[i]+v for i,v in enumerate((q*r*d,q*p,t*q*r*(p+d),t*q*(p+d))))

def exact_full(policy):
    arrival=defaultdict(F); actions=defaultdict(lambda:defaultdict(F));out=unit
    def visit(t,r,q,a):
        nonlocal out
        arrival[(t,r)]+=q;actions[(t,r)][a]+=q;out=add(out,q,r,t,a)
    for root,choice in zip('AB',policy):
        a=choice if isinstance(choice,str) else 'C'
        visit(1,r1[root],q1[root],a)
        if a!='C':continue
        for j,x in enumerate('UV'):
            h=root+x;q=q1[root]*q2[root][x];r=r2[h];sub=choice[j+1]
            a=sub if isinstance(sub,str) else 'C'
            visit(2,r,q,a)
            if a!='C':continue
            for k in (0,1):visit(3,r3[h][k],q/2,sub[k+1])
    return out,{s:{a:mass/arrival[s] for a,mass in dist.items()} for s,dist in actions.items()}

def compressed(d):
    out=unit
    def apply(t,r,q):
        nonlocal out
        p=d.get((t,r),{'P':F(1)})
        for a,v in p.items():
            out=tuple(out[i]+v*x for i,x in enumerate((q*r*(a=='Q'),q*(a=='P'),t*q*r*(a!='C'),t*q*(a!='C'))))
        return p.get('C',F(0))
    for root in 'AB':
        c=apply(1,r1[root],q1[root])
        for x in 'UV':
            h=root+x;q=q1[root]*q2[root][x]*c
            c2=apply(2,r2[h],q)
            for k in (0,1):
                q3=q*c2/2
                if q3:apply(3,r3[h][k],q3)
    return out

assert sum(q1[h[0]]*q2[h[0]][h[1]]/2 for h in r3 for _ in (0,1))==1
assert sum(q1[h[0]]*q2[h[0]][h[1]]*r/2 for h,rs in r3.items() for r in rs)==1
assert r3['AU']==r3['BU']
seen=set()
for policy in product(roots,repeat=2):
    expected,bar=exact_full(policy)
    actual=compressed(bar)
    assert expected==actual,(policy,expected,actual)
    seen.add(expected)
assert len(roots)==38
print('POSITIVE_LEAVES 8')
print('P_Q_TOTALS 1 1')
print('FULL_STRATEGIES_TESTED',len(roots)**2)
print('DISTINCT_FULL_VECTORS',len(seen))
print('EVERY_FULL_POLICY_EXACTLY_REPRODUCED True')
print('ALL EXACT CHECKS PASSED')
~~~

原始程序 stdout：

~~~text
POSITIVE_LEAVES 8
P_Q_TOTALS 1 1
FULL_STRATEGIES_TESTED 1444
DISTINCT_FULL_VECTORS 1004
EVERY_FULL_POLICY_EXACTLY_REPRODUCED True
ALL EXACT CHECKS PASSED
~~~

另一个较全面的本地 `VERIFY.py` 实际枚举 seedless LR 864 个确定性描述，得到196个不同向量，并复验上面的四点证书及每个 full 确定性策略的匹配。两份本地脚本均完成执行；证明全实数行为像相等来自本文的占用流归纳，不来自有限测试。此稿未做独立同行审查或 Lean 形式化。

## 5. 已核来源与原创性边界

这是对经典 Markov 可合并性/受控等价思路的**双测度、似然比签名、可自愿提前停止的专门推导及八叶精确构造**，不宣称广义 lumpability 是新概念。元数据及摘要核对：
- Peter Buchholz, *Exact and Ordinary Lumpability in Finite Markov Chains*, Journal of Applied Probability 31(1), 59–75 (1994), DOI 10.2307/3215235.
- Pablo S. Castro, Prakash Panangaden, Doina Precup, *Equivalence Relations in Fully and Partially Observable Markov Decision Processes*, IJCAI 2009, pp.1653–1657, https://ijcai.org/proceedings/2009/276.
未取得/核验论文全文，因此只将其作为前沿背景，不把文献摘要误称为本文的已发表定理。

## 6. 下一最小研究问题与权限实态

继续寻找**下一步预测核不相同**的 t2 似然比碰撞树，且可能因提前停止而所有 signed 方向最优值相同的严格正有理数 N=3 模型。先对全部 λ∈R^4 获得精确凸包相等或有理分离证书，再讨论完整实数行为 LR 像是否真非凸。本轮新充分条件保证零预测残差类别的可达像完全相同，故这类树已可从母问题反例搜索中剔除。

本轮原生控制库存查询返回 `CONTROL_QUOTA`，活跃 owner 不能据此核实，未取得正式 CLAIM、Result、Driver 独立审查。没有重试之前已被拒绝的服务 session_start（历史报告 `STATIC_READONLY_SCOPE_DENIED`）。此 GitHub 作者级研究保全不冒充已注册 Activity、task publication 或数学准入；不变更 P000/worldview，也不调整共享权限。
