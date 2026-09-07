# 单正支点 raw X6 边缘稳定性：证明与暂停检查点

辅助工作包 `/root/exact_solver`，owner 限定单元；未注册新 task、claim 或工具。
状态：`PROOF_CHECKPOINT / NOT_INDEPENDENTLY_AUDITED / NO_EXECUTABLE_VALIDATION_YET`。
用户把控制面修复设为当前优先级后，本单元停在完整纸面推导与计算合同；未创建 checker 或结果 JSON，未运行新 BRC 回验。
本文不修改 P000、Foundation 或一般七正支点常数的已知区间。

## 1. 固定合同与已查覆盖

在同一 anchor、同一带标签 signed frame 的 raw X6 空间 chart 中，Cell 坐标为六个有符号整数。
设 f 为有限有理 signed 空间质量，p(f) 为严格正质量的空间支点数。
所有零项删除；同一 Cell 上的不同分支先按空间质量聚合。
令 M_I 为保留实际轴集合 I 的完整 raw 边缘，缺失地址按零，且

\[
D(f)=\sum_{|I|=3}\|M_I f\|_1.
\]

这里有全部二十张表，不对每张表取平均、不把范数改为最大单表误差。
can3 与其整数共同偏移必须联合保留，才能替换 raw 三元组；分别的 can3/depth 直方图不够。
空间质量结论不恢复路径标签、历史、branch count 或 dominant mass。

已完整阅读 `OWNER_X6_STABILITY_20260907.md`、
`OWNER_STABILITY_CONSTANT_FRONTIER_20260907.md`，并执行工具覆盖查询
`python -X utf8 -B tools/enterprise_toolbox.py --json coverage 'one positive support raw marginal stability'`。
返回 `REUSE_CANDIDATE_FOUND`，相关项为：

- `result.x6.sparse_marginal_stability`：既有 p(f)≤7 的 111/20 上界与 [1,111/20] 区间。
- `candidate.x6.raw_joint_observer_recovery`：完整二十表及正分支接口，可复用输入类型；恢复求解器不是本证明所需。
- `t0.weighted_brc_cwm` 和 histogram：正有理 BRC 的质量读出，不允许直接输入 signed 差。

对 `research_notes`、`research_method_inventory_addenda` 搜索 one-positive / single-positive / 单正 / 3/20，
未找到本定点 sharp 常数的同义结果。这个有界本地覆盖不构成全球新颖性判断。
本单元延伸既有 raw 边缘合同，使用有限组合计数，不建立新工具家族。

## 2. 单正支点的精确单表账本

先设 p(f)=1，则唯一地写成

\[
f=P\delta_q-\nu,\qquad P>0,\quad \nu\geq0,\quad \nu(q)=0,\quad N=\sum_z\nu(z).
\]

负侧可以有任意有限支点数、任意正有理权、任意坐标跨度。
对每张表定义远离 q 投影的负质量

\[
a_I=\sum_{z:z_I\ne q_I}\nu(z),\qquad A=\sum_{|I|=3}a_I.
\]

在地址 q_I 上，边缘质量为 P−N+a_I；所有其他地址都非正，总绝对质量恰为 a_I。
负点之间的投影碰撞只合并同号质量，不改变这一式子。因此严格有

\[
\|M_I f\|_1=|P-N+a_I|+a_I. \tag{1}
\]

若 z≠q 恰在 r 个轴上不同，1≤r≤6，则恰有

\[
m_r=\binom63-\binom{6-r}3
\]

张表区分二者；上标小于 3 时的二项系数按零。数值依次为 10、16、19、20、20、20。
故 m_r≥10，且等号恰在 r=1。交换有限求和得到

\[
A=\sum_z m_{r(z)}\nu(z)\geq10N. \tag{2}
\]

这里“至少十张”依赖 raw 实际轴坐标；对单独 can3 不成立。

## 3. 任意总质量的 sharp 常数 3/20

对式 (1) 分别使用 |x|≥x 与 |x|≥−x，得到

\[
D\geq20(P-N)+2A\geq20P,
\qquad D\geq20(N-P).
\]

于是 D≥20 max(P,N−P)>0，且 ||f||₁=P+N。
若 N≤2P，则 P+N≤3P；若 N≥2P，则 P+N≤3(N−P)。因此

\[
\boxed{\|f\|_1\leq\frac3{20}D(f).} \tag{3}
\]

这是对所有负侧有限非负质量的统一保证，负侧不受单支点限制。
N=0 完全允许，此时 D=20P，比值仅为 1/20；不需要除以 N。

原生 sharp 见证：任选合法 q，以及每轴一个实际 signed 单位位移 σ_i e_i，σ_i∈{−1,1}，取

\[
f=3\delta_q-\sum_{i=1}^6\delta_{q+\sigma_i e_i}.
\]

六个负 Cell 彼此不同，P=3、N=6。每个 I 都有 a_I=3，q_I 地址的差为零，
单表范数为 3；故 D=60、||f||₁=9，式 (3) 取等。
双方分别是严格正输入分支族；减号仅属于分析时的差，不是负 BRC primitive。

还可读出准确的取等条件：p(f)=1 时，比值为 3/20 当且仅当
N=2P、每个负点只在一个轴上偏离 q，并且六条轴线各承载负质量 N/6。
证明：达到比值首先强制 N=2P；前述两层下界取等强制 A=10N，故所有负点只有一个不同轴。
式 (1) 的取等要求每个 a_I≥N/2；其总和是 10N，故所有 a_I=N/2。
记六轴负质量为 b_i，则所有三轴和相等；用只交换一个轴的两组三元集合，得到 b_i=b_j。
反向代入式 (1) 即可。单条轴线上可以有多个位置、不同权重；并非要求每个负点等权。

## 4. 等总质量的 sharp 常数 1/10 与重合边界

如果 Σf=0，则上述 Jordan 表示满足 P=N>0，式 (1) 给出 D=2A≥20N。
因此

\[
\boxed{\|f\|_1\leq\frac1{10}D(f)\quad\text{当 }\sum f=0.} \tag{4}
\]

概率见证可以取 μ=δ_q、ν=δ_(q+e_1)：十张表差为零，十张表范数为 2，故 D=20、||μ−ν||₁=2。
也可取 μ=δ_q、ν=(1/6)Σ_i δ_(q+σ_i e_i)：每张表范数为 1，同样取等。
非零等质量差的取等条件恰为所有负点只偏离 q 一个轴；不再要求各轴质量均分。

若输入为 μ=Tδ_q 与任意有限非负 ν，允许 ν(q)>0，必须先在 q 消去共同质量。
当 T−ν(q)>0 时，上式中的 P=T−ν(q)、N=Σ_(z≠q)ν(z)，而不是把原 T 误当 Jordan 正质量。
当 T−ν(q)≤0 时，f 整体非正，此时每张表的 ℓ¹ 范数都等于 ||f||₁，故 D=20||f||₁。
因而式 (3) 对 p(f)≤1 仍成立。f=0 时两边为零，不报告 0/0 比值。
原输入等总质量时，非零差消去后仍 P=N，因此式 (4) 也覆盖 ν(q)>0 的情况。

## 5. 辅助 product 计数引理的完整范围

以下仅为组合证明的辅助记号，不把原生 X6 空间改为可变维数。
对 n≥1、1≤k≤n，任意 product 坐标上的有限有理 f、p(f)≤1，记
D_(n,k)=Σ_(|I|=k)||M_I f||₁，则

\[
\|f\|_1\leq\frac{2n-k}{k\binom nk}D_{n,k},
\qquad
\sum f=0\ \Longrightarrow\ \|f\|_1\leq\frac1{\binom{n-1}{k-1}}D_{n,k}. \tag{5}
\]

证明：令 m=binom(n,k)、λ=binom(n−1,k−1)。每个不同点至少由 λ 张表区分，故 A≥λN，
式 (1) 原样给出 D≥max(mP+(2λ−m)N,m(N−P))。
若 k<n，令 α=k/n、t=N/P；比值至多
(1+t)/(m max(1+(2α−1)t,t−1))。
两段在 t=1/(1−α) 相交，第一段比值严格增加、第二段严格减少；交点值就是式 (5) 首常数。
各段使用的分母均为正。等质量则直接 D=2A≥2λN。
当 k=n，唯一的完整表就是 f，两个常数都等于 1，不使用不存在的有限交点。
f 非正和 f=0 如前单独处理。

这些常数在 Z^n 或每个轴至少有两个值的 product 上 sharp：k<n 时取 n 个单位邻点、每点质量 w>0，
正点质量 P=(n−k)w；每张 k 表 a_I=kw，中心差为零，立刻达到首常数。
等质量可只取一对单轴邻点的等权差。k=n 的非零数组本身取等。
若某些坐标域退化为单点，式 (5) 仍是上界，但不声称在该退化域上最优。
k=0 没有此保证：只有总质量观察，非零等质量差不可见；n=0 不在辅助引理范围。

## 6. 待执行的整数 / DIV 与原生 BRC 回验合同

已完整阅读 `exact_arithmetic_runtime_policy.json` V2、
`src/enterprise_math/exact_arithmetic.py` 和 `tools/check_exact_arithmetic_policy.py`。
新执行器不得直接以 Fraction 约分、求商、余数或浮点值构成 native exact evidence。

最小续接方案是每例使用整数分子权重和一个未求值共同质量单位 DIV(1,s)。
完整 raw 表及距离均保留整数分子；比值、归一化质量和常数用 `division` 构造的不约分 DivisionExpr，
所有取等或大小比较用整数交叉乘或 `compare_divisions`。不需要求商/根；
若后续要求数值读出，则必须由 BRC facade 求值并保存 quotient、remainder、collapsed numerator trace。
这不是把 DIV 换名为偷偷约分的 rational wrapper。

实际原生接口应复用：

- `experiments/x6_signed_native_spatial_v16_20260905/x6_signed.py` 的 Spatial6、step 和联合切片坐标；
- `experiments/x6_signed_native_spatial_v16_20260905/signed_brc.py` 的纯整数 support_size、shortest_event_count；
- `experiments/owner_joint_observer_20260907/observer_certificate.py` 的正 Branch、fiber_histograms 与完整 raw 表；
- 既有 WeightHistogram / CWM，仅以整数分子权重回验正侧和负侧，保留共同质量单位。

旧 histogram/observer 内部使用 Fraction，是明确的 legacy 接口边界。新主账本应独立用整数生成，
旧接口返回的单位分母整数分子只用于兼容性回验，不能宣称这些旧依赖已经完成运行时迁移。
若 owner 判断该消费路径也必须迁移，则先处理该接口边界，不能通过静态 gate 的非传递性掩盖问题。
can3 回验必须联合其 common offset，signed 位移与外部共同 anchor 均需保留。

计划的有界例只包括两个 sharp 见证、平移及 signed 轴版本、N=0、q 处消去、非正差、零差、
投影碰撞和单独 can3 的对角位移反例；不调用 LP、不重跑 600 次旧搜索、不扩大枚举。
这些例子的实际程序证据仍未生成，不把以上计划说成 PASS。

## 7. 暂停状态与原开放问题

当前只交还此证明检查点。独立审计、符合运行时政策的执行器与正 BRC 实际回验均待后续明确接续。
一般 p(f)≤7 的最优统一常数仍仅保留 [1,111/20]；式 (3) 不升级该一般问题。
单正支点精确分层可为后续路线选择提供一个已推导候选，但本单元暂停期间不自动续开其他稀疏度。

Global-Knowledge-Sync: main@4fa7d7d / GLOBAL_KNOWLEDGE_V1
