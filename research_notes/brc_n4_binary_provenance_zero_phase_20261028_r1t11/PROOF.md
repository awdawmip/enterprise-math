# BRC N4：AU/BU 单比特来源观察器的零损充要相图

日期：2026-10-28。类型：作者侧解析证明／精确有理计算；UNREVIEWED / NOT_ADMITTED。
对象仅为外部有限、严格正的双概率律停止树；没有证明对应于 P000 原生 X6 Cell 动力学。

## 输入与模型
固定树和后继比率来自 enterprise-math@820e7c4afd18efbe031eaa226feb88ac8292e288 的 research_notes/brc_n4_provenance_refined_tv_exact_20261028_r1/VERIFY.py；前代直接来源为 enterprise-math@c69221729692723d44ff12aacce6fa8940578b0b 的 single_bit_observer_asymmetry PROOF.md。本轮输入主干 main@a0af13c48e2fd320e8e529c5fd6420bba402ad0f，知识快照 GLOBAL_KNOWLEDGE_V1 main@c5547c717135d4d54d93d79fd47daecf9a9fb138。

第1层 A/B 的 (Q质量,P/Q比) 为 (1/2,1/2),(1/2,3/2)；第2层 AU/AV/BU/BV 为 (1/6,1),(1/3,1/4),(1/4,1),(1/4,2)。第3、4层用所引源码的严格正逐父守恒二叉树。t<4 每个完整历史可独立选择三动作 (STOP_P,STOP_Q,CONTINUE) 的任意概率分布，t=4 必停止。S2 强制 AU/BU 在 t2 共享全部即时动作，S23 另强制 t3、t4 的同似然比历史共享动作，S3 只限制 t3/t4。

目标 F(a,b,cA,cB) 的 t1 A/B 继续率为 a/b（其余 STOP_Q）；t2 AU/BU 继续率为 cA/cB，AV/BV STOP_Q；t3 AU 子历史 STOP_P，其他 STOP_Q；t4 STOP_Q。参数域：所有实数 0<a,b<=1, 0<=cA,cB<=1。

来源观察器 O_H=(T,Decision,Z_H)，H 为 AU 或 BU，且 Z_H=1 当且仅当真实前缀经过 H 并在 t>=3 停止；其他为0。d_J^H(F) 是所有真实策略 G∈S_J 中 max(TV_P,TV_Q) 的最小值。

## 主定理（两个方向的完整零点相图）
(1) d2^AU(F)=d23^AU(F)=0 当且仅当 cB>=cA 且 3b(cB-cA)<=7a。
(2) d2^BU(F)=d23^BU(F)=0 当且仅当 cA>=cB 且 2a(cA-cB)<=7b。
任一条件失败时，相应 d2^H、d23^H 严格大于0。全部参数都有 d3^H=0（F 本身∈S3）。不主张正值区域的具体 minimax 分数已求出。

## 必要性：所有未来策略无法绕过的双律方程
假设 G∈S2 精确保持 O_H 的 P、Q 全部终止分布。目标在 t1 的 STOP_P 概率为0，故由严格正质量，G 在两条 t1 历史的 STOP_P 率均为0。设继续率 a',b'。t1 STOP_Q 在 Q、P 下的观察质量相等给出 a'+b'=a+b 与 a'+3b'=a+3b，唯一解 a'=a,b'=b。

目标 t2 STOP_P 总质量也是0；因此 G 在四条可达 t2 历史均不得 STOP_P。S2 迫使 AU、BU 共享继续率 c。目标所有 t4 停止质量都是0，故 G 没有到 t4 的存活概率。H 标签仅在 t3 被读出，并且只有一个非零决策（H=AU 时 STOP_P；H=BU 时 STOP_Q）。该标签对应的 t3 全部质量必须等于目标：当 H=AU 时 c=cA；当 H=BU 时 c=cB。这与任意未标记 t3 的重分配无关。

设 G 的 AV、BV 继续率为 u,v，新增 Q 继续质量 x=au/3, y=bv/4；由概率约束，0<=x<=a/3, 0<=y<=b/4。t2 STOP_Q 的 Q 质量：
Q_F=a(1/2-cA/6)+b(1/2-cB/4);
Q_G=a(1/2-c/6)+b(1/2-c/4)-x-y。
P 质量：
P_F=a(1/4-cA/6)+b(3/4-cB/4);
P_G=a(1/4-c/6)+b(3/4-c/4)-x/4-2y。
两律同时相等严格等价于
  x+y=m, x/4+2y=m,
  m=a(cA-c)/6+b(cB-c)/4。
唯一解 x=4m/7, y=3m/7。

对 H=AU，c=cA，m=b(cB-cA)/4：x,y 非负当且仅当 cB>=cA；且 x<=a/3 当且仅当 3b(cB-cA)<=7a。另一个容量条件 y<=b/4 在 cB-cA<=1 下自动满足。
对 H=BU，c=cB，m=a(cA-cB)/6：非负条件为 cA>=cB；且 y<=b/4 当且仅当 2a(cA-cB)<=7b。另一个容量条件 x<=a/3 自动满足。
故上述条件是所有合法 S2 历史策略实现零损的必要条件；提前停止、t3/t4 重标记及非因果占用松弛均不能改变这些被实际观察固定的约束。

## 充分性：逐历史真实 S23 修复
令 m、x=4m/7、y=3m/7 采用相应标签的公式。构造 G：t1 与 F 一致；t2 AU 与 BU 统一继续率 c，AV/BV 继续率分别为 3x/a、4y/b，其余 STOP_Q；t4 全 STOP_Q。

H=AU：取 c=cA；t3 AU 全 STOP_P，BU/AV/BV 全 STOP_Q。BU 比目标少继续的双律质量为 (m,m)，从 AV/BV 新增的双律质量分别为 (x,x/4)、(y,2y)，其和正是 (m,m)，都属于未标记 t3 STOP_Q，恰好补足。
H=BU：取 c=cB；t3 BU 全 STOP_Q，AU/AV/BV 全 STOP_P。AU 比目标少继续的质量 (m,m) 正好由未标记的 AV/BV 的双律新增 STOP_P 补足。
t1 未改，t2 STOP_Q 已由线性方程精确匹配，被标记 t3 无差，未标记 t3 经上述双律补足，t4 两者均无质量。故完整联合观察分布逐坐标在 P、Q 下相同。实际源树的 t3 相同似然比组仅需 AV0/AV1 与 BV0/BV1 一致，而本构造对各组一致；t2 AU/BU 共享、t4 全停止，故 G 真正属于 S23。上界=0，TV 非负，得到两种压缩类别的精确零值。

若条件失败，有限策略单纯形加共享动作闭约束构成非空紧集，双律终止观察多项式及 TV 连续，故最小值必达到。既然零损被全策略必要性排除，最优值必严格为正；这没有量化其具体数值。

## 新见证和校验范围
对 a=b=3/4、cA=1/3、cB=5/12，新给出 AU 零损、BU 严格正的反向见证：AU 修复共享继续率1/3，m=1/64，AV/BV 新 Q 质量分别 x=1/112、y=3/448，两分支 t2 继续率均为1/28。前一轮 a=b=3/4、cA=5/12、cB=1/3 则方向相反：BU 零损、AU 严格正，BU 修复 AV/BV 率均1/42。

容量壁不是简单方向符号：AU 参数 (a,b,cA,cB)=(1/20,1,0,1) 虽 cB>cA，仍因 3b(cB-cA)>7a 无法零损；BU 参数 (1,1/20,1,0) 同样因 2a(cA-cB)>7b 无法零损。

VERIFY.py 以 Fraction 精确重建 N4 各层、双律质量与完整联合终止分布，对625个有理参数组合×2标签检验零值端构造的 S23 可行性与逐坐标相等，并在非零端检查强制流方程无法满足容量。所有实数域的充要结论来自上述代数必要性、构造充分性及紧性，而非网格外推。旧见证 AU 正值区间的准确 minimax 仍只知 1/224..1/160；P000 原生 X6、独立时间与三维切片保真桥接未建立。

BRC 复用：REUSE_APPLIED，使用来源保留的 (Q_mass,P_mass) 双律正质量、时间和行为容量锥；不使用负质量抵消，不将外部正概率树宣称为 HEARTBEAT 原生 BRC-only 算术。
