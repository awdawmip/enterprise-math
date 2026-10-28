# BRC N=4：跨父到达、正继续流与后继重标记的精确可修复性

日期：2026-10-28。作者侧 portable 精确研究；UNREVIEWED / NOT_ADMITTED。规范读快照：GLOBAL_KNOWLEDGE_V1 main@889df61d44b53e06ecaaf9dc50071114b45c6e03；科学输入：enterprise-math main@f58010890628c5b18f7344961a09f16f1ff00b19。接续上一轮 research_notes/brc_n4_cross_parent_arrival_exact_obstruction_20261028_r1/PROOF.md（immutable commit 194319dde91018e04f609a3f81cd3dbfb22cdad6）。P000 原件 blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc 与规范投影一致；ACTIVE 世界观保持不变。

## 模型与来源

外部有限双概率律 N=4 序贯树。Q 法支路 q 与 P/Q 似然比 r：t1 A=(1/2,1/2), B=(1/2,3/2)；t2 AU=(1/6,1), AV=(1/3,1/4), BU=(1/4,1), BV=(1/4,2)。t3 每个父节点的两个孩子 Q 质量 q/2、似然比 r(1±e)，AU e=1/10、BU e=4/5、AV/BV e=0；t4 沿先前冻结原树生成，细节见 VERIFY.py。每个父节点的 Q 与 P 子质量分别守恒。完整观察为双律各八个 (T=1..4,D=P/Q) 终止概率。S2 要求 t2 同 LR 历史共享即时 (STOP_P,STOP_Q,C)，S23 另外要求 t3 同 LR 历史共享，t4 也按 LR 共享；每个随机动作即时独立。真正 TV 距离取每律终止联合分布 L1/2 的最大值，再对合法压缩行为取下确界。

使用 BRC 的正有理分支质量、历史来源、似然比纤维、因果占用和两律联合读出，复用分类为 REUSE_APPLIED。该外部树还没有与 P000 原生 X6、三维切片和独立时间建立保真桥接。

## 定理 1：四参数正继续策略族的占用缺陷

取实数 0≤δ<1、0≤θ≤1、0≤c0,c1≤1。合法 S23 端点 E0 令 t1 A/B 继续率 (1,1−δ)，t2 AU/BU 同享 (0,1−c0,c0)；E1 令 t1 继续率 (1−δ,1)，t2 AU/BU 同享 (0,1−c1,c1)。二者的 t2 AV/BV 均 STOP_Q，t3 AU 的两孩子均 STOP_P、BU 的两孩子均 STOP_Q，t4 全部 STOP_Q。

令 a=1−θδ，b=1−(1−θ)δ；xA=(1−θ)c0+θ(1−δ)c1，xB=(1−θ)(1−δ)c0+θc1。完整历史策略 F 的 t1 A/B 继续率为 (a,b)，t2 AU/BU 继续率 cA=xA/a、cB=xB/b，其他行为沿端点固定。分母严格正。其双律全部十六终止坐标恰为 (1−θ)L(E0)+θL(E1)，因为相应逐历史条件占用的凸组合构成此 F。

同 LR 历史 AU/BU 的行动 C 交叉乘缺陷为
$$D_C=x_A b-x_B a=\theta(1-\theta)\delta(2-\delta)(c_0-c_1).$$
当 0<δ<1、0<θ<1、c0≠c1 时非零，说明这个逐历史占用组合不满足 S2/S23 的共享行为约束；它不是占用松弛可执行性的证据。

## 定理 2：锁定未来时的精确 minimax（限制子类）

锁定 t1、AV/BV 及 t3/t4 行为，只允许 AU/BU 同享任意三元 (p,q,c)。令 wA=a/6、wB=b/4、W=wA+wB、cbar=(wA cA+wB cB)/W。由于 AU、BU 的 LR 都是 1，且各自 t3 孩子的两律质量守恒，候选与 F 在 Q、P 两律的四个可能非零差坐标都相同：
$$\Delta_{2P}=Wp,\quad\Delta_{2Q}=W(cbar-c-p),\quad\Delta_{3P}=w_A(c-c_A),\quad\Delta_{3Q}=w_B(c-c_B).$$
故两律 TV 均为
$$\frac{Wp+W|cbar-c-p|+w_A|c-c_A|+w_B|c-c_B|}{2}.$$
因为 p+|cbar-c-p|≥|cbar-c| 且 p=0 取等，最优可令 p=0。剩余绝对值凸函数在 c=cbar 取全局最小：若 cA≥cB，区间 [cB,cbar] 导数为 −wA，[cbar,cA] 导数为 +wB，其他区间单调外延；反序对称。因而
$$\boxed{d_{\mathrm{locked}}=\frac{w_Aw_B}{W}|c_A-c_B|=\frac{|D_C|}{2(2a+3b)}.}$$
这是冻结其他行为的精确双律 TV minimax，不能当作全部 S2/S23 策略的下界。

## 定理 3：释放 t3 读出后，真实完整 S23 minimax 等于零

在压缩策略中保持 t1 的 a,b，AV/BV STOP_Q，并令 AU/BU 在 t2 共同 STOP_Q 概率 1−cbar、CONTINUE 概率 cbar。若 cA≥cB，令 AU 所有 t3 子历史 STOP_P，BU 两个子历史以同一概率
$$f_B=\frac{w_A(c_A-c_B)}{w_Ac_A+w_Bc_B}$$
STOP_P，其余 STOP_Q。若 cA<cB，令 BU 子历史 STOP_Q，AU 两个子历史以同一概率
$$f_A=\frac{w_B(c_B-c_A)}{w_Ac_A+w_Bc_B}$$
STOP_Q，其余 STOP_P。分母为零（cA=cB=0）时所有 t2 行为 STOP_Q，无需补偿。所列 f 均在 [0,1]。

证明：t2 同享 cbar 保持两律的 t2 STOP_Q 总量；当 cA≥cB，目标 t3 的 P 质量 wA cA 与修复质量 wA cbar+wB cbar fB 相等，t3 Q 质量随总量守恒相等；另一情形对称。BU（或 AU）的每个孩子选相同 f，使两律终止质量均按父节点 LR=1 等比例调节，所以 P 律同样逐坐标相等。t1 与其他历史原样；t4 不可达。t3 四个可达孩子 AU0, AU1, BU0, BU1 的 LR 分别为 9/10,11/10,1/5,9/5，互不相同；其余等 LR 历史不可达并统一动作，故修复是真实 S23 即时随机策略。F 在 t3/t4 自身满足 S3。因此：
$$\boxed{d_2(F)=d_3(F)=d_{23}(F)=0}$$
对上述全部实数参数成立；下界为 TV 非负性。非凸的 BRC 来源占用可有完全可修复的联合观察商。

## 精确见证与证据

δ=θ=1/2，c0=1/2，c1=1/4；两端点在 AU、BU 均有正继续率。F 的 t1 a=b=3/4，t2 cA=5/12、cB=1/3、D_C=3/64。两律父到达 wA=1/8、wB=3/16；锁定未来的最优值 1/160。实际修复令 t2 cbar=11/30，t3 BU0/BU1 均以概率 1/11 STOP_P，而 AU0/AU1 STOP_P。经真实策略的十六坐标计算，两律 TV 全为0。

VERIFY.py 独立重建原 N4 两律树，执行 500 组全有理输入的父子守恒、合法随机动作、占用交叉乘、端点观察混合、锁定未来精确值、S23 同 LR 共享及完整双律十六坐标相等检查，RESULT.json 保留实跑回执。500 组只是证书检查；连续实数定理由上面显式恒等式证明。

## 下一问题

改动下游 LR 信息集或未来读出，使跨父支路的均匀后继重标记不能同时满足 P/Q 质量约束；给出可执行上界与覆盖整个即时随机策略类的 Bellman/精确代数下界，确定非零的真实 S2/S23 TV minimax。保持原始证据和作者未获正式 CLAIM/Driver 准入的边界；正式所有权与任务进度须经 native Source 核实。