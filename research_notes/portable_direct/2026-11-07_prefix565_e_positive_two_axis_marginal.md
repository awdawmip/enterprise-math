# PREFIX-565｜第五、六轴BRC联合边缘计数的精确五状态商与全长度e-非负性

2026-11-07。接续PREFIX-564，冻结科学输入f42f2906d77f24085c123f3ccfe9667d41caa96d。来源：PREFIX-550的冻结四STAR原生权重、PREFIX-561的交换对合、PREFIX-564的整系数u,v变基。状态AUTHOR_PROVED / EXACT_SYMBOLIC_CERTIFIED / INTEGER_CHECKED / UNREVIEWED / NOT_ADMITTED。

## 问题与观察范围

本研究处理固定根（辅助零根及±1、±2、±3、±4共九种）的BRC边缘观察。设x=q5、y=q6，令q1=q2=q3=q4=z=1，保留第五、第六轴次数的完整双变量整数联合直方图。完整七变量非负性是PREFIX-564的较强开放问题。此商只用于所声明的当前及全部未来两轴联合计数；原生96端口图仍保存动作顺序、支路、来源和门控标记，不能从边缘商重建已汇总的四轴及门控分布。

## 定理一：全长度五状态强等价商

原生相位为(star,prev,current)，加分支位形成96端口。按轴编号绝对值划类：C0为|current|≤4且|prev|≤4（32端口）；C1为|current|≤4且|prev|=6（16）；C2为|current|=6（16）；C3为|current|≤4且|prev|=5（16）；C4为|current|=5（16）。

原生BRC边权为w_k=(|s_k(i)|+|s_k(j)|-|s_k(j)-r_k|+|s_k(i)-r_k|)/2。当r5=r6=0时，w5=|s5(i)|、w6=|s6(i)|，故该边缘与上述九根选择无关。对全部六动作枚举，任意同类端口的目标类/两轴权重/整数重数完全相等，转移矩阵为：

M(x,y) =
[ [2,0,2,0,2],
  [4,0,0,0,2],
  [0,6y,0,0,0],
  [4,0,2,0,0],
  [0,0,0,6x,0] ].

令f_i(0)=1、f(d+1)=M f(d)。完整原生边相同类的加权强等价性加深度归纳证明：对所有d≥0、九根和96端口，该端口的精确两轴联合计数等于f_{class(port)}(d)。PREFIX-561对合固定的32端口恰属于C0。

## 定理二：C0全部深度在初等对称变量u=x+y、v=xy下非负

设F_i(t)=Σ_{d≥0} f_i(d)t^d。矩阵方程F=1+tMF给出
F0=1+t(2F0+2F2+2F4);
F1=1+t(4F0+2F4);
F2=1+6ytF1;
F3=1+t(4F0+2F2);
F4=1+6xtF3.

消元或对I-tM作克拉默法则，得到精确形式级数恒等式：

**F0(t)=(1+4t+12ut²+24ut³+144vt⁴)/(1-2t-48ut³-144vt⁴-864vt⁵).**

令P=2t+48ut³+144vt⁴+864vt⁵。因分母常数项为1，(1-P)^(-1)=Σ_{j≥0}P^j在Z[u,v][[t]]中合法；分子及P均有非负整数系数。于是对任意整数d≥0，**f0(d)∈Z≥0[u,v]**。这是保留两轴联合关系的精确全长度e-positive定理。一般对称非负多项式不必在u,v下非负，例如x²+y²=u²-2v；此处证明依靠冻结原生模型的五状态特殊结构。

## 正系数递推与初值

对n≥5：
**f0(n)=2f0(n-1)+48u f0(n-3)+144v f0(n-4)+864v f0(n-5)**。
f0(0)=1；f0(1)=6；f0(2)=12+12u；f0(3)=24+96u；f0(4)=48+480u+288v。递推只使用非负整系数加乘与指数平移，并能通过x+y、xy的二项展开精确读出两轴联合计数。

## 精确证书

自包含程序PREFIX565_positive_marginal_certificate.py保留四STAR原生48相位、96端口、6动作及BRC边权定义，不使用浮点。实际执行返回ALL_CHECKS_PASS：
- 对九根完整检查9×96×6=5184条原生投影边的同类重数与带权关系；
- 以Z[t,x,y]整系数多项式字典，计算两个由全部5!置换展开的行列式，逐系数验证上述克拉默分子和分母及单位常数项；
- 原生96状态与五状态递推在d=0..32逐系数比较3168份双变量多项式，共117248个非零系数位置；C0同时与u,v递推的x,y展开逐系数一致；
- 正系数递推执行到d=128，所有生成的u,v整数系数非负。无穷深度范围由上述精确有理生成函数证明，而非有限测试。

该成果不改变P000、ACTIVE世界观或冻结科学pin。深度是原生动作数，不是心跳物理时长。

## 下一具体问题与控制状态

在q1=...=q4=1而保留门控z的更细观察中，使用PREFIX-557至559的秩一门控核寻找全长度u,v非负表达或最短精确反例；随后逐一恢复前四轴权重，区分可能的耦合来源。对任何负系数候选均在冻结原生七变量计数中复核。BRC reuse=REUSE_APPLIED，新增五状态商仅用于其声明的观察范围。

2026-11-07本轮em_status实际返回BACKEND_IDENTITY_OR_VERSION_MISMATCH / STATUS_DATABASE_UNAVAILABLE / operation_sent=false，当前Owner、原生Researcher-ID未核实，未建立CLAIM、Result或Review。成果仅作为独立作者Source材料保存。适用控制：GLOBAL_KNOWLEDGE_V1，EM docs/RESEARCH_CONTINUATION_PROTOCOL.md#current-normative-context、P000 V5、ACTIVE Heartbeat World、docs/PORTABLE_RESEARCH_PROTOCOL.md与research_priorities/research_method.json。
