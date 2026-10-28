# N=4 BRC：跨父到达的占用插值障碍与双律观察精确修复

2026-10-28；作者侧可移植研究，UNREVIEWED / NOT_ADMITTED。账户规范冻结：GLOBAL_KNOWLEDGE_V1 main@f6e3098b58d632d29c0979e9a7dc0dfc12c8a9e8；研究源输入：enterprise-math main@a086c975c5b0bbf1ef2a6b84532da40df6004d56。续接 research_notes/brc_n4_full_epsilon_exact_tv_phase_20261028_r1t11/NEXT_TASK.md。本研究没有求出跨父双参数真正共同 TV minimax，也不把原生 P000 的六维离散动力学等同于外部有限树。

## 定理 1：两个端点的共享行为占用，何时可以仿射插值

在带父子来源的正有理 BRC 双律概率树上，选一个同似然比信息集的两个历史 h,k。端点 i=0,1 下，它们的条件到达流分别为 a_i,b_i>=0，端点使用相同的即时行为向量 pi_i=(pi_i,u)（u=P,Q,C），故 x^i_h,u=a_i*pi_i,u、x^i_k,u=b_i*pi_i,u。记 x^theta=(1-theta)x^0+theta*x^1, theta∈[0,1]；对应到达为 a_theta,b_theta。定义同策略交叉乘残差
D_u(theta)=x^theta_h,u*b_theta-x^theta_k,u*a_theta。
精确恒等式：

D_u(theta)=theta(1-theta)(a_0*b_1-a_1*b_0)(pi_0,u-pi_1,u)。

证明：展开双乘积，同端点的平方项互相抵消，交叉项按端点对称配对后即为上式。因此若 0<theta<1 且 a_theta,b_theta>0，给定信息集内的插值流满足真实即时共享行为约束，当且仅当 a_0*b_1=a_1*b_0（两端点到达比相同）或者 pi_0=pi_1（两端点动作完全相同）。对于大于两个历史的信息集，需要逐对检查。其他信息集和未来读出仍各有自己的约束，此结论不声称整个 S2/S23 集合或观察像必然非凸。

## 定理 2：一种明确可执行的占用修复及其精确 L1 代价

当 a_theta+b_theta>0，取 pi_pool,u=(x_h,u+x_k,u)/(a_theta+b_theta)。该向量非负且归一。用同一 pi_pool 作用于两个给定到达流，满足信息集共享行为且保留两个到达。逐行动有
x_h,u-a_theta*pi_pool,u=D_u/(a_theta+b_theta)，
x_k,u-b_theta*pi_pool,u=-D_u/(a_theta+b_theta)。
因而这一个规范修复的**条件占用** L1 改变量恰为
2 sum_u |D_u|/(a_theta+b_theta)。
这不是最优 TV 距离，也不自动为未来分支观察误差提供下界。

## 同一棵严格正 N4 树上的实数二参数反例

沿用此前冻结的双律正概率树 t1 A:(q=1/2,r=1/2), B:(1/2,3/2)；t2 AU:(1/6,1), AV:(1/3,1/4), BU:(1/4,1), BV:(1/4,2)。q 是 Q 律分支质量，r=P/Q 似然比，两律均正且质量守恒。AU、BU 在第二时刻具有相同 r=1，须共享动作。t3/t4 原树保持不变，但下面的端点策略在 t2 停止，因此后续读出质量为零；不可达后期历史统一选择 Q，符合 S23。

取任意实数 0<=delta<1。端点0在 t1 的 A 继续率1，B继续率1-delta；端点1则 A继续率1-delta，B继续率1；t1 其他质量停止并判 Q。t2 AV/BV 始终判 Q；端点0在 AU/BU 共同行动 P，端点1在 AU/BU 共同行动 Q。这两个端点自身均为真实合法 fresh-random S23 策略。

对任意 theta∈[0,1]，上述两策略条件占用的逐历史仿射混合满足
a_theta=1-theta*delta；b_theta=1-(1-theta)*delta；
x_AU,P=1-theta；x_BU,P=(1-theta)(1-delta)；
x_AU,Q=theta(1-delta)；x_BU,Q=theta。
因此
D_P=theta(1-theta)delta(2-delta)，D_Q=-D_P，D_C=0。
对所有 0<theta<1、0<delta<1，D_P>0，故**这一个逐历史插值占用绝不对应合法 AU/BU 共享行为策略**。定理2对应 pi_pool(P)=1-theta、pi_pool(Q)=theta，修复占用 L1 代价精确为 4theta(1-theta)delta。原来证明单参数 F_e 端点策略可插值的“同父、等到达、线性共享式”不能未经核验推广到这种跨父到达断面。

## 重要反向结论：非凸占用仍可以在双律终止观察层实现精确零误差

观察为每律的全部八个 (T=1..4,D=P/Q) 坐标，Q/P 共16个。终止目标是端点0、1的全读出分布按 theta 混合。保持 t1 混合后的继续率 a_theta,b_theta，AV/BV 仍 Q。因为 AU/BU 的 r 均为1，且在 t2 完全终止，可另选**同一即时**合法行为：

pi_weighted(P)=[(1/6)(1-theta)+(1/4)(1-theta)(1-delta)]/[(1/6)a_theta+(1/4)b_theta]；
pi_weighted(Q)=1-pi_weighted(P)，pi_weighted(C)=0。

分母正，两个动作质量非负且归一。AU/BU 两律下相同的 LR=1，故此策略同时精确匹配这两个历史在 Q/P 两律的 (t=2,P/Q) 聚合终止贡献。t1 停止贡献来自前期概率的线性插值，AV/BV 的 t2 Q 质量亦线性保留，t3/t4 均为零。因此对**全部实数** 0<=delta<1、theta∈[0,1]，该真实 S23 策略的**整个16坐标双律终止分布**等于两端点分布的凸组合；观察 TV_Q=TV_P=0。

严格有理见证 delta=theta=1/2：a=b=3/4；原插值 AU/BU 的 P 占用为1/2与1/4，Q占用为1/4与1/2；交叉乘缺陷 D_P=+3/16，D_Q=-3/16。规范 pi_pool=(1/2,1/2,0) 的条件占用 L1 代价为1/2，对完整 (T,D) 分布的 TV_Q=TV_P=1/96。然而合法加权行为 pi_weighted=(7/15,8/15,0) 使 TV_Q=TV_P=0。由此不能把占用交叉乘残差或某个选定修复的损失误报为全局共同 TV 的严格下界。

## 验证、归属、适用范围

VERIFY.py 以 Python 标准库 Fraction 重建两律完整16坐标，按不同 t1/t2 分支质量核验质量守恒，验证定理两条代数公式、两种修复及25个精确有理参数点；输出保存 RESULT.json。连续**实数**定理由上面的显式代数展开与正分母直接证明，而非有限点外推。BRC 实际复用：正有理分支 q、LR、历史标签、父条件占用、共享行为交叉乘、Q/P 全部终止读出。可检验非凸性与观察保真属于不同层次。

这只是外部有限序贯概率树的数学结论；原生 X6 Cell、独立时间、三维切片的选择/嵌入、第三分量和状态保真关系未建立。当前 GitHub 已验证 writer 为 awdawmip，但尚未取得原生研究任务 CLAIM 或独立 Driver 准入。作者侧产物不等于 native Result。下一步见 NEXT_TASK.md。