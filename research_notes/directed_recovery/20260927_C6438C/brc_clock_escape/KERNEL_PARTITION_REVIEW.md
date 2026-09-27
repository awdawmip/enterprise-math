# Split kernel partition：共享上下文符号审查

结论：**PASS / SHARED_CONTEXT / PURE_SYMBOLIC_REVIEW / NOT_EXECUTED / NOT_ADMITTED**。逐段全文核对后，未发现阻断几何理想分解、完整素数幂估值或条件标签概率公式的数学问题。该结果给出有用的返回观察量细化；它没有提供到达核的有效时钟或无因子信息的成功率。

审查对象：`KERNEL_PARTITION_LAW.md`，SHA-256 `f608e47eecf0d0cfb53eb3680f9dd8836cbad673e7c5d8e84885eeb6950fea55`。同时全文读取具体接口稿 `CLOCK_ESCAPE_AND_TORSION_MARK.md`，SHA-256 `ac743ae40288095cc1633de2e91aa2453d61b921e362e941db2b1eab27207542`，核对其第 5–6 节。没有修改两份稿件，没有科学模块 import、数值试验、外部 provider query 或远端写入；本审查不宣称重新验证原生执行或外部论文。

## 1. 全局分裂假设足够强，而且不能省略

这里使用的是有证书的 scheme-theoretic kernel：它在 `R=Z/nZ` 上就是给定 sections 的不交并，而不只是每个代数闭包上的几何点数相同。有限 étale 加上实际的完整分裂 sections 排除了重根、缺失标签和局部相撞。各 section 的理想、identity fiber 的理想均按稿中闭子概形的含义使用。

在任何局部仿射图，有限个不交闭 section 的理想两两 comaximal，其交等于积；这个等式粘合为理想层等式。identity ideal 沿 phi 拉回就是 kernel 的理想，这是 scheme-theoretic fiber 的定义。再沿 Q 拉回，积和理想和都与基变换相容，所以确有

`J = product_i I_i`，`I_i+I_j=R`。

此论证没有错误地声称任意交与拉回可交换；先在 comaximal 情形把交化为积，才作拉回。它也不需要知道 n 的因子来定义观察量；后面的素数幂分解仅用于证明。

若只拥有未分裂核、几何点集合、非单位缩放的坐标，或带厚化的非 étale 核，当前假设不成立，不能继续使用这份分区证书。原稿明确把分裂和实际坐标 admission 列为义务。

## 2. 整数乘积与 prime-power 深度

对 `R_r=Z/r^a Z`，任一理想由某个 `r^b` 生成，其中 `0<=b<=a`；b=0 是单位理想，b=a 是零理想。两理想 comaximal 意味着至少一个 b 为零。因此，对固定 r，至多一个 I_i 有正估值。乘积的估值是该唯一的 b，而不是若干 b 的和再截断。

于是不同正整数代表 g_i 不共享素因子，且其普通整数乘积已经整除 n：

`gcd(g_i,g_j)=1`，`g(J)=product_i g_i`。

这验证了稿中最重要的深度边界。它不是把一般环理想乘积错误地当作未截断整数乘积；无截断恰由 comaximal 条件保证。

若 phi(Q)=O 在整个 R 上成立，J 为零理想，所以每个 `r^a` 分量恰有一个 I_i 为零，其他 I_j 为单位。等价地，连通局部谱 `Spec(R_r)` 上的 Q 落在唯一一个完整 kernel section，而不是只在模 r 的点上接近它。此时各非平凡 g_i 是互素的完整 prime-power 块，乘积为 n。

因此“全部分量同一全局标签，或读出 proper factor”是准确的二择结论。它不表示同一标签概率小，也不表示达到核就必然分解。只有模 r 返回而尚未模 `r^a` 返回时，g_i 可为部分深度；一般乘积定理仍有效，但不能宣称已经得到完整 prime-power 分块。

## 3. 条件概率、联合标签与不可省略的准备成本

在 n=pq、p/q 不同且为素数，并已条件于 phi(Q)=O 时，标签不同当且仅当至少一个 g_i 是 proper factor。故任意联合标签分布 pi 都满足

`P(factor | kernel return)=1-sum_i pi(i,i)`。

只有额外证明该条件分布分解为 `pi(i,j)=alpha_i beta_j` 后，才得到 `1-sum_i alpha_i beta_i`。uniform independent 时为 `1-1/s`；s=1 时为零。共享随机种子、同一公时钟或强制全局 section 都可能产生相关性；CRT 只给状态分解，不自动给分布独立。稿中已保留联合公式并指出共享标签的零成功情形。

所有上述概率都是给定已返回核后的概率，包括文中不作独立性假设的联合版本。取得 Q、使其进入核、获得真实标签证书以及每次失败的成本必须先计入；不能把此条件概率直接当作一轮无条件成功率，更不能把筛选后的返回样本当作免费样本。

若协议只在已认证总核返回时才运行标签 observer，其无条件成功项为“该返回事件概率”乘上述条件概率。稿件没有构造这种返回分布，亦未声称同一式子直接覆盖任意复合数或 prime-power 上未经说明的抽样律。

## 4. 与具体 two-torsion 接口的匹配

Montgomery smooth odd 模型上的 T=(0,0) 与 O 构成显式分裂的两点 subgroup，是其 degree-2 quotient 的 kernel；它不是把整个 [2] kernel 都误称为两点核。

具体接口稿保留原固定非二阶点 P=(a,b)，其中 b 及由曲线方程推出的 a 为单位。T 平移在 Kummer 线上是 primitive swap `(X:Z)->(Z:X)`；它没有把 T 当作原 translated-mark 定理中需要 b 为单位的固定 mark。对真实相邻 Q、Q+P 同时平移 T，仍是 Q+T、Q+T+P，因而可以合法复用同一个固定 P 的原定理，得到

`g_O=gcd(n,Z0,X1-a Z1)`，

`g_T=gcd(n,X0,a X1-Z1)`。

primitive pair 使两者不可能共享 residue prime，故本核分区的乘积即 `g_O*g_T`，保留 primitive 深度而没有 Kummer 单坐标的平方歧义。已有 ladder、adjacency、smoothness 和 primitive admission 均不能由末态两个任意 pair 冒充。

具体稿的另一个存在性例子也正确：在完整 `[2]Q=O` 且 Q 处处有限的强前提下，y=0，`x(x²+alpha x+beta)=0`；beta 单位排除两因子同时非单位。因此每个局部分量一因子完全为零，另一因子为单位。这比仅有平方 observer 饱和更强。把不同 CRT 分量置于不同非零二阶 section 证明观察量确有严格增益，但该构造没有成为未知因子的盲选点方法。

## 5. 复杂度与可续接范围

给出 s 个 section 不代表 s 为输入位长的多项式，亦不保证每个 section 的坐标或理想生成元很短。直接执行需支付全部 section 构造与 admission、s 次 primitive ideal 观察、gcd、失败结果及 proper-divisor 的 exact-division 验证。单个生成元、单坐标或平方商函数只有在证书证明其生成同一理想后才能替代完整观察。

平衡标签树若想把 s 次观察变成对数次，还需要可构造、可组合、可验证的 subset-union ideal；仅写一个乘积或集合符号不能给出该工具。稿中明确这一点。几何证明用局部因子分析也没有把这些因子作为执行输入。

下一有界工具可以是已存在 Montgomery 相邻 pair 上新增 g_T 的付费原生接口，保留原 g_O 与全部失败分支，再比较相同准备过程下新增的真实因子事件。更大核的 label compiler 另需闭合坐标/理想成本。未知奇部的到达条件、整体选参成功率及原生 Shor 主目标仍开放；此审查不把符号分区定理当作已执行优化。

本次实际运行全局知识 helper 返回 `BEFORE_WRITE_REFRESHED`，canonical `1f6ebeb12631aa4314e94b2666784954e231c566`，读取三入口；相对本单元先前 `2450bbb` 仅新增一个 journal，政策文件未变。未重新注册或改变活动来源，沿已读有效活动 guard 做同一研究单位的只读数学审查。

Global-Knowledge-Sync: main@1f6ebeb / GLOBAL_KNOWLEDGE_V1。
