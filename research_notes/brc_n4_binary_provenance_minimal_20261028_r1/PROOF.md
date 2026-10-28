# BRC N4：一个来源比特已足以强制正的全局 TV 压缩损失

日期：2026-10-28。分类：作者侧解析证明 / 精确有理复验 / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING。对象：外部有限严格正双概率律停止树，未与 P000 X6 Cell 动力学建立保真对应。

## 模型、观察器与最优值

沿用已经公开的 N4 源树，精确代码见固定前沿 820e7c4afd18efbe031eaa226feb88ac8292e288 的 research_notes/brc_n4_provenance_refined_tv_exact_20261028_r1/VERIFY.py。Q 律在 t1 的 A,B 质量各为 1/2，P/Q 比分别为 1/2,3/2；t2 的 AU,AV,BU,BV 的 Q 质量为 1/6,1/3,1/4,1/4，P/Q 比为 1,1/4,1,2。第三、四层沿该源码中的逐父严格正有理守恒树。t<4 的每历史允许 (STOP_P,STOP_Q,CONTINUE) 任意非负、和为 1 的独立即时随机行为；t4 必停止。压缩类 S2 要求 AU/BU 共享全部 t2 行为；S23 额外要求 t3/t4 同似然比历史共享全部即时行为；S3 仅约束 t3/t4。

目标策略 F(a,b,cA,cB) 在 t1 A/B 以 a/b 继续，其余 STOP_Q；t2 AU/BU 分别以 cA/cB 继续，其余 STOP_Q，AV/BV STOP_Q；t3 AU 两个子历史 STOP_P，其他历史 STOP_Q，t4 STOP_Q。假设 0<a,b<=1 及 0<=cB<cA<=1。新二值来源标签 ZA 记录是否到达第三层的 AU 前缀：当且仅当 t>=3 且历史前缀为 AU 时 ZA=1，其余为 0；继续到 t4 后仍保留 ZA=1。观察为 O=(T,Decision,ZA)。损失 dJ(F) 为对全部合法 G∈SJ 取下确界的 max{TV_P(O(F),O(G)),TV_Q(O(F),O(G))}。

## 全实数参数定理

记 alpha=a/6，beta=b/4，r=b/a，Delta=beta(cA-cB)>0，
KQ=max{(5+3r)/4, 1+3r/2}，KP=(1+r)/2。
那么对全部声明的实数参数都有

0 < Delta/(KQ+KP) <= d2(F) <= d23(F) <= [alpha beta/(alpha+beta)](cA-cB)，并且 d3(F)=0。

这是全策略上下界定理，并没有宣称 d2、d23 的精确最优值。

## 全策略下界证明

任取 G∈S2。记 G 的 t1 继续率为 a',b'，t2 AU/BU 共享继续率 c∈[0,1]；允许 G 在 t1/t2 有 STOP_P，AV/BV 自由提前停止或继续，第三、四层全部任意合法随机化。令 u=a'-a，v=b'-b，并记
s=(u+v)/2，t=(u+3v)/4，h=(a cA-a'c)/6，
z=Q_F(T=2)-Q_G(T=2)。

这四个量是实际可观察事件的 F−G 概率差：s=Q_F(T=1)-Q_G(T=1)，t=P_F(T=1)-P_G(T=1)，h=Q_F(ZA=1)-Q_G(ZA=1)。特别地，Q_G(ZA=1)=a'c/6 与后续所有随机化无关，因为每个达到 AU 第三层的样本终究停止并保留标签。

目标 Q_F(T=2)=(a+b)/2-a cA/6-b cB/4。G 在 AU/BU 的共同 continue 为 c，而 AV/BV 的 t2 总停止概率各至多 1，故
Q_G(T=2) <= (a'+b')/2-a'c/6-b'c/4。
结合 v-r u=2(1+r)t-(1+3r)s，直接整理得

z >= Delta-[1+(1+3r)c/4]s-[1+3r/2]h+[(1+r)c/2]t.   (1)

这是全策略因果约束；没有把局部纤维损失误认为全局下界。因为 Q 律事件 T=1、T=2、ZA=1 两两互斥，若 x_+=max(x,0)，完整观察 TV_Q >= s_+ + z_+ + h_+。P 律另有 TV_P >= |t|。把 (1) 移项，利用 c∈[0,1] 与系数非负，得到

Delta <= z+[1+(1+3r)c/4]s+[1+3r/2]h-[(1+r)c/2]t
      <= KQ TV_Q + KP TV_P
      <= (KQ+KP) max{TV_Q,TV_P}。

对全部 G∈S2 成立，且 S23⊂S2，故二者都有严格正下界；此证明适用于整个实数参数域，不依赖有限网格或凸松弛。

## 真实行为策略上界与可恢复性

取 c*=(alpha cA+beta cB)/(alpha+beta)，令 G* 保留 F 的 t1、t3/t4 及 AV/BV 行为，仅把 t2 AU/BU 统一改为共同继续率 c*、其余 STOP_Q。G*∈S23，逐历史三动作非负且归一。由于 alpha(c*-cA)+beta(c*-cB)=0，t2 聚合停止量不变；t3 只有带 AU 来源的 STOP_P 与不带该位的 BU STOP_Q 两项质量等量异号地改变，大小 k=alpha beta(cA-cB)/(alpha+beta)。AU/BU 父历史的 P/Q 比均为 1，故 P、Q 两律完整 (T,Decision,ZA) 分布的 TV 均恰为 k。F 本身属于 S3，故 d3=0。

## 精确见证与二值标签最小性

固定 a=b=3/4，cA=5/12，cB=1/3。则 alpha=1/8，beta=3/16，r=1，Delta=1/64，KQ=5/2，KP=1，c*=11/30，k=1/160，严格得到

1/224 <= d2(F) <= d23(F) <= 1/160，且 d3(F)=0。

现在把 ZA 改为一个常数标签，即恢复旧 (T,Decision) 观察。定义 H：t1 a=b=3/4；t2 AU/BU 共同 c*=11/30；t3 AU 全 STOP_P，BU 两子历史各以 1/11 STOP_P、10/11 STOP_Q，其他历史 STOP_Q；t4 STOP_Q。H∈S23。沿完整 N4 正质量叶树精确计算可得 P 和 Q 两律下 L_F(T,Decision)=L_H(T,Decision)，因此恒值标签时 d2=d23=0。新二值标签对同一 F 产生上述严格正下界。由于非空标签集合至少有一个值，而且 1 不够、2 已够，得出：

在此固定 N4 见证及声明的来源增强观察族中，使全局 S2/S23 压缩有正共同 TV 损失的最小来源标签取值数是 2。

这项最小基数结论不等于二值观察器的精确 minimax 数值已求出，也不是所有外部概率模型的统一结论。

## 可复算证据、方法及边界

本目录 VERIFY.py 通过固定 N4 源码的 Fraction 全展开逐项检查双律质量守恒、合法 S23 竞争策略、旧 (T,Decision) 双律零损失修复，以及新 (T,Decision,ZA) 双律上界精确为 1/160。作者侧扩展 Fraction 程序已实际运行，另验证 1200 个全历史随机行为策略和 324 个多参数有理竞争案例；还以符号代数检查 (1) 的等式残差为零。采样仅验证实现，实数域下界的有效性来自上面的代数证明。

BRC 的实际类型为保留分支来源、双律正质量、到达率与停止时序的有标记路径；ZA 是一个来源事件观测映射。此次没有符号/相位抵消，不归类为 HEARTBEAT 原生算术计算。P000 起点、六维原生空间、三维切片与时间语义不变。原生 Owner/身份服务只读查询返回 BACKEND_IDENTITY_CHECK_UNAVAILABLE 且 operation_sent=false，所以本结果只是作者侧可移植成果：尚未正式 CLAIM、原生 Result、独立 Driver 审阅或数学准入。

下一步：证明 d2、d23 是否等于 1/160（或者提供更优真实策略和匹配的全策略对偶）；再讨论 cB>cA 时的 BU 标签及二值标签分类。