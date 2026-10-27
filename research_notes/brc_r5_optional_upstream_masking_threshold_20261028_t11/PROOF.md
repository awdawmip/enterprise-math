# R5: 可选上游停止掩蔽异预测核——四维真实可达集的精确 1/3 阈值

日期：2026-10-28。作者级可移植数学结果：AUTHOR_PROVED / EXACT_FINITE_CHECKED / UNREVIEWED / NOT_ADMITTED；不是 SOURCE 签发的 CLAIM、Result 或独立 Driver 审查。

冻结输入：GLOBAL_KNOWLEDGE_V1 main@9f1b9fec0f4ac5208bfb3449042926bb5923b63d；Enterprise Math main@c0b398eaaeb65eafa9ce31963722d344d37a19e3。读取规范两入口、P000、HEARTBEAT_WORLD_NATIVE_X6_TIME、ACTIVE 世界观、联合关系观察保真约束、项目 AGENTS.md 与自主及 portable research 协议。接续 research_notes/brc_r5_terminal_step_kernel_converse_20261028_t11 中强制到达模型的结论，不把其必要性擅自推广到允许早停的模型。

## 问题与精确模型

这是外部双测度有限观察统计实验，不是原生 X6 时空、BRC-Shor、旋转、相位或物理残差运算。BRC 的正分支保留来源、质量相乘与相加是这里复用的研究方法；证明的压缩只针对明确给定的观察量，不移除后续可能有影响的来源信息。

时间 1 仅有一个似然比 R=1 的根，可宣告 P/Q 停止或继续。继续后，时间 2 的来源 A、B 在 P 与 Q 下均各占 1/2，因此 R_A=R_B=1，来源可被 full 区分而 LR 不可区分。时间 2 可立即宣告或观察至时间 3；时间 3 必须宣告 P/Q。终端似然比 Y=(1/2,1,3/2)。对 0<b≤a<1/2，Q 条件预测核

K_A=(a,1−2a,a),  K_B=(b,1−2b,b).

六叶 Q 质量为各组 1/2 乘以条件核；P 叶质量为 Y 乘对应 Q 叶质量，均严格正且分别归一。full 行为策略使用完整历史；LR 行为策略仅使用 (t,R) 且没有跨时刻共享随机种子。两者允许全部 [0,1] 实数局部随机化。比较四维 O=(e_P,e_Q,T_P,T_Q)=(P[宣告Q],Q[宣告P],E_P τ,E_Q τ)。

### 定理（sharp phase gate）

对于此完整参数族，下列条件等价：

(1) b≥a/3；
(2) 对一切 λ∈R⁴（**全部有符号方向**），full/LR 的最小线性支持值完全相等；
(3) conv(O_full)=conv(O_LR)；
(4) **真实行为可达集合相等** O_full=O_LR。

若 b<a/3，则存在 λ=(1,1,0,c)、c>0，使 V_LR−V_full>0。因此从强制到达模型得出的“异核必有四维严格分离”的逆命题在允许提前停止时为假；但这里也没有产生“凸包相等而真实集合不等”的母问题反例。

### 第一部分：所有 signed 目标的 Bellman 闭式

任给 λ=(α,β,γ,δ)∈R⁴，定义 f(y)=min(αy,β)，c=γ+δ。因 f 是两个仿射函数的最小值，对任意正负 α、β 都是凹函数。定义

D=2f(1)−f(1/2)−f(3/2)≥0，
g_A=aD，g_B=bD，ḡ=(g_A+g_B)/2。

g_i=f(1)−E_{K_i}f(Y) 是已到 t2 后再观察的 Bayes 分类收益。时间 1、2 的似然比均为 1，所以每次继续的双测度时间价格统一为 c，即使 γ、δ 有负值也成立。

full 在 t2 可以分别在 A/B 上选择继续或停止，获得加权节省
A(c)=((g_A−c)_++(g_B−c)_+)/2；
LR 只能在共同的 (t2,R=1) 签名作一个动作，混合核固定为 K̄=(K_A+K_B)/2，节省
B(c)=(ḡ−c)_+，
其中 x_+=max(x,0)。

根在 t1 可立即停止（代价 f(1)+c），也可支付第二步成本 c 再获取 t2 的最优机会（full 代价 f(1)+2c−A；LR 代价 f(1)+2c−B）。**精确等式**为：

V_full=f(1)+c+min(0,c−A(c)),
V_LR  =f(1)+c+min(0,c−B(c)),
Δ_global=V_LR−V_full=(A(c)−c)_+−(B(c)−c)_+.

由 Jensen 的凸性 A≥B≥0，因此另有完全精确的上游掩蔽恒等式：
Δ_global=min{ A−B, (A−c)_+ }。

若 c≤g_B，两条历史都在 t2 继续，A=B=ḡ−c；若 c≥g_A，两者都停止，A=B=0，局部差距为零。仅在 g_B<c<g_A 时局部 Jensen 差距正，此时 A=(g_A−c)/2；它能够越过 t1 提前停止的必要充分条件是 A>c，即 c<g_A/3。因此

Δ_global>0  当且仅当  g_B<c<g_A/3。

若 D=0，增益皆零且不能分离；若 D>0，上式存在 c 当且仅当 b<a/3。对于 b<a/3，取 α=β=1 则 D=1/2，并在 b/2<c<a/6 任取有理数，即严格分离。等号 b=a/3 因为只有非严格端点，属于精确保真侧。这证明 (1)、(2)、(3) 等价。证明覆盖全部实数策略和全部 signed 四维目标，不是参数网格外推。

### 第二部分：为何这里 LR **真实集合** 就是凸集

由于从唯一 t1 根继续进入 t2 后，A/B 的固定 1/2 混合比例不依赖 LR 策略，t2 的 LR 预测核始终是 K̄，尽管个别隐藏历史核不同。定义 Q 下分别在 t1/t2/t3 停止的质量 z0,z1,z2≥0，z0+z1+z2=1。对局部宣告 Q 的 Q 占用质量定义 v0,v1,v_y，满足线性约束：

0≤v0≤z0；0≤v1≤z1；0≤v_y≤z2 K̄(y)。

它们的观察线性读出为

e_P=v0+v1+Σ_y y v_y，
e_Q=(z0−v0)+(z1−v1)+Σ_y(z2 K̄(y)−v_y)，
T_P=T_Q=z0+2z1+3z2。

任何无持久种子的 LR 策略都产生这些占用量；反向任何满足线性约束的占用量也可由 t1 继续率 x=z1+z2、t2 继续率 z2/(z1+z2) 及本地宣告概率 v/其到达质量重建，分母为 0 时随意选择。故 **LR 真实集合就是一个闭凸多面体的线性像，本身闭凸**。LR⊆full，且两者紧凸包已在第一部分证明相等，则 O_full⊆conv(O_full)=conv(O_LR)=O_LR。反向包含显然。因此 (1)→(4)；(4)→(2) 显然。定理证毕。

### 第三部分：严格正六叶精确证书

取 a=1/4,b=1/8，b/a=1/2>1/3；两隐藏预测核不同：
K_A=(1/4,1/2,1/4)，K_B=(1/8,3/4,1/8)。
六叶 Q=(1/8,1/4,1/8;1/16,3/8,1/16)；
六叶 P=(1/16,1/4,3/16;1/32,3/8,3/32)。
P/Q 均严格正、和各为 1，全部似然比约束精确成立。于是四维 O_full=O_LR。

独立有限精确复核：102 个有效完整历史确定性策略描述（根停 2 个、根继续后 10² 个）去重得 77 个三维不同点 (e_P,e_Q,T_P=T_Q)；LR 2+2+8=12 个不同确定性点。以所有不共线 LR 点三元组求 exact Fraction 交叉积，枚举出全部 7 个三维凸包支持面。写 x=e_P,y=e_Q,t=T_P=T_Q：

-64x−64y−3t≤−67;
-2x−3y≤−2;
-2x−y≤−1;
t≤3;
2x+y≤2;
2x+3y≤3;
64x+64y−3t≤61.

全部 77 个完整历史不同确定性点逐项满足这些 7 个精确面；有限完美记忆树的行为策略占用流可分解成其确定性点的凸组合，LR 真实集合已证明凸，从而也是独立有限证书。VERIFY.py 运行 Fraction 检查并输出 ALL EXACT CHECKS PASSED；另有 343 组 signed 系数网格仅作旁证，不作为全实数证明。

具体构造说明保真范围：full 在 t1 必继续，A 在 t2 继续且 t3 仅 Y=1/2 宣告 Q，B 在 t2 停止宣告 P，得到 O=(1/16,7/8,5/2,5/2)；LR 在 t1 以 3/4 继续（否则停止宣告 P），t2 若到达则必继续，t3 在 Y=1/2 以 8/9 宣告 Q（否则宣告 P），也得到完全相同 O。然而 full 有 Pr_Q(τ=2)=1/2、Pr_Q(τ=3)=1/2，LR 对应 Pr_Q(τ=1)=1/4、Pr_Q(τ=3)=3/4。实际上如强制 LR 轨迹时间分布等于这个 full，LR 必须 t1 全继续且 t2 继续率 1/2，其分类误差总改善最多 3/64，但 full 改善 1/16=4/64，故不能同时保真四维及完整时间分布。

阈值反侧的另一严格正实例：a=3/8,b=1/32，取 λ=(1,1,0,1/32)，则 g_A=3/16,g_B=1/64，A=5/64,B=9/128，精确有 V_LR−V_full=1/128>0。

### 验证边界、来源与下一个问题

理论成立于上述明确的 t1 单根、t2 双异核同签名、t3 必终止的模型族，不适用于任意多上游来源比例可变的 N=3/N=4 树，不涉及原生六维 Cell 或未来时空物理。已由 Python Fraction 实际核验六叶输入/质量守恒、完整顶点、七个有理面、全部顶点覆盖、精确策略映射与反侧差距；没有 Lean 形式化、独立审查或 SOURCE Result。状态保持 AUTHOR_PROVED / EXACT_FINITE_CHECKED / UNREVIEWED / NOT_ADMITTED；活跃 owner 的原生查询返回 CONTROL_QUOTA，无法证明有正式 CLAIM。资料不是 Research-Activity 正式注册；REGISTER_PENDING。

文献背景（非特定 1/3 定理的来源、也不主张论文优先权）：Laroche & Tachet Des Combes (2023), On the Occupancy Measure of Non-Markovian Policies in Continuous MDPs, ICML / PMLR 202, https://proceedings.mlr.press/v202/laroche23a.html；Khan, Yu & Zhang (2025), A simple proof of Blackwell's theorem on the comparison of experiments for a general state space, Economics Letters 247:112146, https://doi.org/10.1016/j.econlet.2024.112146。上述一般理论与本模型假设/观察范围不同，不能替代这里的推导。

**下一单元**：用至少两个独立可控的 t1 LR 签名在 t2 汇聚来破坏当前“固定混合核占用流凸化”的充分结构，先以确切有理质量和完整 real-policy algebra 判定 LR 真实集合是否非凸，再检验所有四维 signed 支撑方向是否仍与 full 相等，最后才寻求非凸真实集合见证。母问题仍开放；见 NEXT_TASK.md。
