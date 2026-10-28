# BRC N=4：BU 单比特来源容量壁的全策略精确 minimax

**作者侧数学证明，2026-10-29。** Frozen GLOBAL_KNOWLEDGE_V1 main@edee29410faf7b200a72c3b7e6bd2d62e4d4025a；EM science main@3a806398761cb2717c6a9139c498a8e40afb83e3。P000 读取原文的 Git blob=770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc；本结论只针对外部有限双律 BRC 树，不包含原生 X6 动力学保真声明。

## Model and exact theorem

Q律 t1 A,B 各质量1/2，P/Q似然比为1/2、3/2。t2 (Q质量,比)：AU=(1/6,1), AV=(1/3,1/4), BU=(1/4,1), BV=(1/4,2)。t3 所有父历史等分Q，AU子代比乘(9/10,11/10)，BU乘(1/5,9/5)，AV/BV比不变。t4保持严格正的双律守恒二分（完整程序在本轮本地可复验包）。目标完整历史策略 F=(a,b,cA,cB)=(1,1/20,1,0)：t1 A,B继续率1,1/20；t2 AU全继续，其他STOP_Q；t3 AU子代STOP_P，其余STOP_Q；t4 STOP_Q。观察器 O=(T,Decision,Z_BU)，Z_BU=1当且仅当BU前缀到达t3。

S2是全部合法全因果即时随机策略，其中t2似然比相同的AU和BU共用完整(STOP_P,STOP_Q,CONTINUE)向量；S23还要求t3、t4相同似然比历史行为相同。对 J=2,23，dJ=inf_{G∈SJ} max(TV_Q(F,G),TV_P(F,G))。

**Theorem.**  对全部实数合法竞争策略，d2=d23=3/320。

## Reduction by genuine policy and observer data processing

共同确定性后处理K把t1/t2的STOP_P/Q合并为Q；t3/t4终止结果合并到t3，其中Z_BU=1则判Q，Z_BU=0则判P。F被K固定。任一G∈S2可构造合法G'，保持t1、t2各历史继续率，早期停止改判Q，t3立即停止并依上述来源位判定，t4全STOP_Q。于是 O_L(G')=K O_L(G)，L=P,Q，因此 TV_L(F,G')≤TV_L(F,G)。这一化约适用于所有原先允许的提前停止、第三四时刻随机判定及继续；没有使用非因果占用松弛。

G'的四个观察原子依序为 (1,Q,0),(2,Q,0),(3,P,0),(3,Q,1)。F的Q分布是(19/40,43/120,1/6,0)，P分布是(57/80,29/240,1/6,0)。记t1 A/B继续率为A,B∈[0,1]，t2 AU/BU共用c∈[0,1]，AV/BV分别继续率u,v∈[0,1]；U=A*u，V=B*v，故0≤U≤A、0≤V≤B。定义

```
s=(A-1+B-1/20)/2;    t=(A-1+3*(B-1/20))/4;
H=B*c/4;
rQ=1/6-A*c/6-U/3-V/4;
rP=1/6-A*c/6-U/12-V/2.
DeltaQ=(s,H-s-rQ,rQ,-H);
DeltaP=(t,H-t-rP,rP,-H).
```

令e=max(TV_Q,TV_P)。每一观察事件差分绝对值≤TV，故 H≤e、|s|,|t|,|rQ|,|rP|≤e，且B=1/20+2t-s≤1/20+3e。关键容量恒等式为
```
2*A*c+7*B+16*rP-4*rQ = 2+7*(B-V) ≥ 2.
```

## Exact all-real three-region TV dual certificate

**0≤c<3/7**：由A≤1、B≤1/20+3e、rP≤e、−rQ≤e，得 2≤2c+7/20+41e，故 e≥(33/20−2c)/41≥111/5740>3/320。

**3/7≤c≤3/4**：设
```
w1=7*(1-c)/20, w2=(7*c-3)/20,
w3=(3*c+1)/10, w4=(7-3*c)/10.
```
它们非负，和为1。Q律的两个观察事件 t2、t1∪t2 的差分分别为 H−s−rQ、H−rQ；P律的两个事件 (t3,P,Z0)、t1∪(t3,P,Z0) 的差分分别为rP、t+rP。各差分≤e。下式是精确有理/符号恒等式：
```
w1*(H-s-rQ)+w2*(H-rQ)+w3*rP+w4*(t+rP)
+ 7/20*(V-B) = (33-39*c)/400.
```
因为V−B≤0，非负权重的四事件和≤e，得到 e≥(33−39c)/400≥3/320。

**3/4≤c≤1**：若B≥1/20，则独立来源标签原子的差分H=Bc/4≥c/80；若B<1/20，A≤1给出s≤(B−1/20)/2<0，考虑不交原子t1与(t3,Q,Z1)，其合并差分为s−H，故
```
e≥H-s≥Bc/4+(1/20-B)/2
 =c/80+(1/20-B)*(1/2-c/4)≥c/80≥3/320.
```
三段穷尽所有实数c∈[0,1]，为完整S2（从而S23）下界。

## Matching genuine S23 policy

取G★: t1 (A,B)继续率(1,1/20)；t2 AU、BU共同继续率c=3/4，AV为u=7/80，BV为v=1，其他t2动作STOP_Q；t3 BU后代STOP_Q，其余STOP_P；t4 STOP_Q。t3 BU后代似然比{1/5,9/5}与其他历史比{9/10,11/10,1/4,2}不重合，t2 AU/BU共用行为，所以G★∈S23。此时s=t=rQ=0，H=rP=3/320，DeltaQ=(0,3/320,0,−3/320)，DeltaP=(0,0,3/320,−3/320)。故TV_Q=TV_P=3/320，匹配下界，证毕。

## Evidence and limits

本轮实际执行 Python标准库Fraction完整16叶重建、双律正质量/守恒、完整观察分布及1000组随机S2全历史竞争策略，结果PASS_EXACT_N4_BU_BINARY_WALL_GLOBAL_MINIMAX；发布目录VERIFY.py为另一次实际执行的5000组精确有理对偶检查PASS_N4_BU_WALL_EXACT_RATIONAL_DUAL_5000，另有SymPy符号证明PASS_SYMBOLIC_N4_BU_DUAL_IDENTITY。随机检验用于实现核查，**全部实数结论来自上文解析证明**。完整执行源程序/原始结果/SHA256证据包由本轮交付保存。原生Owner查询CONTROL_QUOTA，research_authority_granted=false；仅AUTHOR_EXACT_PROOF / UNREVIEWED / NOT_ADMITTED，未取得CLAIM、Result、独立Driver审阅。若转移到P000原生心跳世界须另证六轴、三维切片第三分量、独立时间、历史来源及允许后续操作读出的保真映射。下一问题见NEXT_TASK.md。
