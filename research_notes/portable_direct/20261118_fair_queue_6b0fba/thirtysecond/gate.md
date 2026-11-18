# X6 三槽门控的部分回执、最小冲突与可识别函数

任务 `RS-X6-NATIVE-GATE-EVIDENCE-FIBER` 所列原生来源给出的可绑定门位回执数为零。在固定 Cell、等量、三槽有向 Link、六轴的符号协变先验中，**729 个候选全部保留**。对以后可能取得的具名回执，下面给出可行性、最小冲突、精确计数、可识别读数及最少背景标签的条件定理。两个自拟账本分别留下 3 和 5 个候选，用于检验定理。[冻结任务书及取证界限](https://github.com/awdawmip/enterprise-math/blob/f63e62fdffc813d94ff31e9d40146e52cb767ca8/research_tasks/RS-X6-NATIVE-GATE-EVIDENCE-FIBER.md)

## 一、729 从何而来

固定三个具名槽与有向后继，把符号字按旋转群 $C_3$ 识别。四个代表依次取 $+++,---,-++,+--$。六轴的 $S_6$ 重标号消去具体单射轴名。整体翻号及翻转 Link 方向均未取商。每个符号类可排除，或闭合后指定哪些根允许换轴。两个齐次符号类的三个根在各自稳定子下同轨，两个混合类的三个根各成一轨。因此各类独立根数为 $r_i=1,1,3,3$，联合数为 $(1+2)^2(1+2^3)^2=729$。冻结代码用 $-1$ 表示排除，用 $0$ 表示闭合、零根许可，用正整数的三位掩码表示许可。两个齐次类的正掩码只能取 $7$。[R762CA 协变分类](https://github.com/awdawmip/enterprise-math/blob/7530269499c7f799e65cb20b50a0f5c698b4b1c7/research_notes/portable_direct/R762CA_COVARIANT_SIGN_GATE_CLASSIFICATION.md)

冻结观察由上述候选正向生成。单位权回返签名给 90 类，逐符号类闭合与两步支撑总数给 225 类，另计同号端点给 324 类，分开根符号给 441 类，分开根及其有向后继的符号并保留逐类闭合给 729 类。具名正长度来源只配全局零步汇总时给 640 类。这些数目量化理想完备表的区分力。脚本对全部候选独立重建六种签名，并对照过冻结代码逐类产生的两步计数。[观察原文](https://github.com/awdawmip/enterprise-math/blob/7b6ea72b90918af5363b319ef16e25122a123ad9/research_notes/portable_direct/20261116_heartbeat_triad_refinement/POLICY_OBSERVATIONS.md) · [可重放的原代码](https://github.com/awdawmip/enterprise-math/blob/7b6ea72b90918af5363b319ef16e25122a123ad9/research_notes/portable_direct/20261116_heartbeat_triad_refinement/check_policy_observers.py) · [R762CB 回返谱](https://github.com/awdawmip/enterprise-math/blob/e0724e29612a5c5252f425d876e65ad2ef36f06a/research_notes/portable_direct/R762CB_SIGN_GATE_RETURN_SPECTRA_THEOREM.md) · [R762CC 观察条件](https://github.com/awdawmip/enterprise-math/blob/b54aefb88abaa327131e3db85220ce39630b14d8/research_notes/portable_direct/R762CC_OBSERVER_SAFETY_AND_QUERY_COMPLEXITY.md)

| 冻结材料与原字段 | 此项实际支持的观察 | 对应原生门位 |
|---|---|---|
| P000 的 `primitive_force_balance.canonical_equal_quantum_triad.closure_required` 及其机器谓词 | 原始稳定性的要求同时包括恰三个非零力和满足闭合谓词。没有逐符号类该谓词的真值记录。 | 未知 |
| V17 §1 的槽位继承假设、§3 的两个具名轴环、§10 的未决问题 | 在所设规则下 $123,124,125,123$ 与 $123,124,134,123$ 的框运输不同。原文没有给出这些转移的物理触发条件，或同一 Cell、量、有向符号三槽及原生来源的许可回执。 | 未知 |
| 旋转题书的 Hard boundaries 及三元闭合母题 | 静态轴重标号与原生动态转移分开；母题仍求闭合与事件来源。 | 未知 |
| R762CA/CB/CC 及冻结观察程序 | 给定闭合和许可掩码才能生成的路径、深度零可用性、查询答复 | 条件先验 |

[冻结 P000](https://github.com/awdawmip/enterprise-math/blob/fa76228ee339e27b64f595f4ad645e515974d919/p000_reality_foundation.json) · [V17 原文](https://github.com/awdawmip/enterprise-math/blob/ab4699ad2a80b0e040c5a5f287cd34a537d75e6f/research_notes/X6_ACTIVE_TRIAD_HOLONOMY_CONTROL_V17_20260906.md) · [旋转题书](https://github.com/awdawmip/enterprise-math/blob/fa76228ee339e27b64f595f4ad645e515974d919/research_tasks/RS_X6_NATIVE_ROTATION_DYNAMICS_20260906.md) · [三元闭合母题](https://github.com/awdawmip/enterprise-math/blob/fa76228ee339e27b64f595f4ad645e515974d919/research_tasks/RS_X6_TRIADIC_CLOSURE_DYNAMICS_20260906.md) · [冻结具类型算术约定](https://github.com/awdawmip/enterprise-math/blob/fa76228ee339e27b64f595f4ad645e515974d919/research_constraints/heartbeat_brc_only.json)

例如 $(0,0,2,0)$ 与 $(0,0,4,0)$ 同时兼容现有原生记录，在旧的按根符号计数中也一致。两者分别许可 $-++$ 中少数符号后的第一、第二个多数槽。有区分力的一条记录是两候选共用的固定 Cell 和量下，给出有向符号字、具名退出槽、前后轴、Link 及必需历史，证实第一多数槽确已换轴或获明确许可。该记录的证据语义为正，足以排除后一候选；若另有同资格的明确拒绝也可反向区分。

## 二、回执对应的理想与冲突

取偏序 $P$，由四个互不相交的星组成，每个闭合原子 $c_i$ 位于该类的根原子集 $G_i$ 之下，$|G_i|=r_i$。候选恰是 $P$ 的向下闭集，以下称理想，记作 $I$。明示零步起始闭合证明 $c_i\in I$；根事件的实际发生证明对应许可及闭合；仅获书面许可尚无发生历史；明确拒绝一根只令该根为假；没有记录不改变候选。实际转译要先核同一资格与上下文。只有来源保证某一候选集合至少包含一个真实见证时，才可以建立一条析取正记录。

设每条正回执给非空集合 $E_t\subseteq P$，要求 $I\cap E_t\ne\varnothing$。每条明示否定给 $N_j\subseteq P$，要求 $I\cap N_j=\varnothing$。不同析取回执可各选见证；有共同未知字段的情形见第四节。令 $D=\bigcup_j\uparrow N_j$，$M=P\setminus D$。

**定理一（可行、强制与最小冲突）。** 账本可行恰在每个 $E_t\cap M$ 非空，此时 $M$ 是唯一最大可行理想。强制为假者恰为 $D$。任一原子 $x$ 强制为真，恰在某一行满足 $E_t\cap M\subseteq\uparrow x$。全部极小可行理想由每行选一个 $e_t\in E_t\cap M$、取 $\downarrow\{e_t:t\}$ 后删除严格包含另一候选结果者得到。

事实上 $M$ 自身避开所有否证，且包含每行的全部剩余见证。再施加 $x$ 的否定会从 $M$ 删去 $\uparrow x$，于是给出强制真判据。任一可行理想都含逐行选出的见证及其向下闭包，反过来这些闭包本身可行。空的正记录族取空闭包。

一份按包含关系极小的冲突，恰含一条正回执 $E_t$ 和一组否证，其上闭包对 $E_t$ 构成不可删项的覆盖。若某个否证没有仅被自己覆盖的成员，删除该否证仍矛盾。因此冲突行数至多 $1+|E_t|$。在同一混合类的未知根情形，上界为 4；一条确有资格跨全八根轨道的正回执，上界为 9。两界均由一条全域可选的正回执加各根逐一明拒达到。删去四行例的正行后保留 162 项，删去任一负行保留 81 项。九行例相应为 16 与 8 项。粗粒度拒绝闭合可一次覆盖整个符号类，须按原否证为单位核查极小性。覆盖结论不要求否证各自逐根。

**定理二（精确计数）。** 对上闭禁集 $U$ 定义

$$
H(U)=\prod_{i:c_i\notin U}\bigl(1+2^{r_i-|G_i\cap U|}\bigr).
$$

被禁闭合的符号类仅可排除，贡献因子 1。其余各类或排除、或闭合并在未被禁的根中任选子集。记正行数为 $m$。在负记录允许的理想中，对每条正记录“其所有候选均未出现”的事件作容斥，便得

$$
|\mathcal F|=\sum_{S\subseteq\{1,\ldots,m\}}(-1)^{|S|}
 H\!\left(D\cup\bigcup_{t\in S}\uparrow E_t\right).
$$

四星先验固定时，直接筛 729 项的代价与行数成线性；容斥需要 $2^m$ 次乘积，适合正行少的账本，亦提供独立算术校验。

## 三、什么读数可以唯一确定

**定理三（端点与相邻边）。** 在非空纤维 $\mathcal F$ 上，若 $f$ 对包含关系单调不减且取值于有序集，则它可识别当且仅当所有极小可行理想与 $M$ 的读数相同。任一可行理想都介于某个极小解和 $M$ 之间，由单调性即得。对任意函数 $f$，可识别当且仅当所有可行的单原子添加边上 $f$ 恒等。因为任一可行理想都可不断加入 $M$ 中尚未纳入的一个极小原子，直至 $M$，且沿途正回执继续成立。空纤维报告矛盾。

**条件实例一。** 取 $+++$ 闭合而停住，排除 $---$、$+--$；在 $-++$ 明拒少数根，并有正回执确认两个多数根 $x,y$ 中至少一个获准。候选四元组恰为 $(0,-1,2,-1),(0,-1,4,-1),(0,-1,6,-1)$。读数 $x\lor y$ 恒为真，两单根各取过真假，多数根许可数可取 1 或 2。即使有一次可信事件，只保留其多数号也未确定具体有向槽。

**条件实例二。** 排除两个齐次类，两个混合类明示闭合。令 $z$ 为 $+--$ 的少数根。除 $x,y,z$ 外各根均明确拒绝；另有两条各可选见证的正回执，所允许的候选分别为 $\{x,y\}$ 与 $\{y,z\}$。五种可行赋值 $(x,y,z)$ 为 $010,011,101,110,111$。两个极小解的真根集为 $\{y\},\{x,z\}$，最大解含三根。三个单根均不确定，但 $y\lor(x\land z)$ 恒真。另取 $g=y\land(x\mathbin{\mathrm{xor}}z)$，两个极小解和最大解均给零，内部的 $011,110$ 给一，共有四条可行边使 $g$ 改变。这提供了任意函数无法仅凭端点判定的反例。跨符号类的第二行是自拟部分回执，需来源保证其析取为真，才有实际资格采用。

## 四、背景依赖与共享根

若两条原始记录本就共享一个未知根 $j\in\{x,y\}$，而同资格的两行分别断言 $g_j=1$、$g_j=0$，须对同一个 $j$ 检验两行。正确联结的纤维为空。先各自消去 $j$ 再求交会接受 $x,y$ 恰一真，虚增 $4\cdot3\cdot3\cdot9=324$ 个候选。第二行的“某个根被拒绝”也不符合第二节逐项明拒的输入语义。同一 Cell、原事件、时间或必要历史若在行间共用，同理应先保留共同见证，再投影。

**背景标签数。** 将已知来源背景记为 $b$，资格及内部共用字段均已核实后，各有非空可行集 $F_b\subseteq J(P)$。允许为各背景选择辅助标签，同一标签必须共享一套政策。所需最少标签数等于以下两个组合量。

* 覆盖所有背景最少需几套政策，其中政策 $I$ 覆盖 $\{b:I\in F_b\}$。
* 以背景为顶点、极小空交子族为超边的超图弱色数，着色要求没有单色超边。

任何标签组均须有共同政策，选取一个便给覆盖；给定覆盖，每个背景任取覆盖自己的政策即可着色。一个有限颜色类总交为空，恰在它含有一个极小空交子族。这证明两种表达等价。给定特定可观测背景字段时，应检验其实际各标签组是否分别有非空交；自由选标签算出的数目只给所需区分能力，不会由此发现新的物理字段。

例如三种已记录背景分别只有 $x\lor y$、明拒 $x$、明拒 $y$，三对交集分别有 $162,162,243$ 个候选，总交却空。允许合并后两个背景，即只需两个标签。若只记录两两不可兼容的背景图，这个三元冲突将完全丢失。

## 五、复算

在本目录运行以下命令，Python 3.10 或以上即可。第二种方式附加读取原观察程序，先核验完整 Git blob，再逐类核对两步观察；两次产生相同的 JSON。

```sh
python3 gate_check.py > /tmp/x6-gate-replay.json
cmp /tmp/x6-gate-replay.json gate_checked.json
python3 gate_check.py --prior-checker /path/to/check_policy_observers.py > /tmp/x6-gate-prior-replay.json
cmp /tmp/x6-gate-prior-replay.json gate_checked.json
```

脚本同时枚举四元组和 12 原子全部子集，并核对二者给出同一组 729 理想。冻结程序的 Git blob 为 `2e35713c52145d5d9cce05753ff94cb49fc7215e`。两实例以直接筛选对照容斥、强制位及极小解，再直接检查每项读数与全部可行边；额外核验三个根坐标上的 232 种小账本。来源审读和合成账本分别对应 JSON 的 `native_`、`conditional_` 字段，前者的零行数来自第一节的字段审读。[独立脚本](gate_check.py) · [复算结果](gate_checked.json)
