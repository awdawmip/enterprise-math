# 两正支点 raw X6 稳定性：独立纸面审查

状态：`PASS_BOUNDED_PAPER_PROOF / CANDIDATE_REVIEW_ONLY`。
日期：2026-09-08（Asia/Shanghai）。这是内部 owner 辅助证据，不是正式 V2 review、Result、claim、Working Truth 或 Foundation 晋升。

审查者收到 root 给出的猜想和候选路线，随后独立重建以下推导；**未读取 Hilbert 正在写的稿件**。因此这是对已暴露候选的独立证明核验，不宣称盲目发现或全球新颖性。本次没有运行数学程序、LP、求解器、随机试验或枚举，没有修改 source。

**结论：在所给 raw 合同内，sharp 常数确为 1/4。** 即

\[
\boxed{4\|f\|_1\le D(f),\qquad p(f)\le2.}
\]

二维矩形的对角两正、另两角两负单位质量给出等号。上界允许任意有限负支撑、任意有理正负总质量及任意实际整数坐标跨度，不要求输入两侧等总质量。

## 1. 来源覆盖与固定合同

先核对既有 19 项 owner 候选目录，其 SHA256 仍为
`9b9b1851602200bbb207681dbac444a7e745b2915d6f8851bc999fd3a028f115`。
使用此前已读且本次重新核验字节的 raw 稳定性及单正支点来源；没有通过搜索打开新作者稿。

- `candidate.x6.raw_joint_observer_recovery` 与 T0 BRC：`COMPOSE_APPLIED`，复用同一外部 anchor、带标签 signed X6 chart、完整 raw 边缘及正人口/辅助 signed 差的类型边界。
- `candidate.x6.one_positive_raw_stability_certificate`：`COMPOSE_APPLIED`，复用 Jordan 后的正支点合同和 p<=1 的已审 3/20 界。本审查把相同的“正投影地址外只有负质量”账本用于两个正点；新增的是这里明写的计数与观察函数证明，不是把旧常数无条件迁移。
- 既有正支点保护 raw 压缩引理是可用的有限 carrier 归约；本证明直接逐点处理整个 Z^6，不调用它求解 carrier，也不把有限 carrier 等同于已解权重问题。
- channel quotient 的六通道平均算子/可逆观察分类不作为本证明前提；其 carrier 和算子合同不同。这里没有借用其结论或执行 legacy Fraction consumer。

建议把这份纸面结果按既有 raw 稳定性分析的限定扩展保存，当前属于 `RESULT_ONLY` 的辅助候选证据；没有新增 global family、工具 ID 或可执行 payload，也没有修改目录状态。

固定六轴标签 `C={0,1,2,3,4,5}`。坐标属于同一个外部 anchor 与 labelled signed frame 下的 Z^6。先按相同 Cell 聚合原正人口 mu、nu，再对差 f 做 Jordan 分解并删零。本文的

\[
f=f_+-f_-,\quad S=\operatorname{supp}(f_+),\quad
P=\sum f_+,\quad N=\sum f_-,\quad M=\|f\|_1=P+N
\]

都是聚合抵消后的对象；特别地 `supp(f_-)` 与 S 不交。M_I 是保留实际轴集合 I 的完整 raw 质量表，缺失地址按零，且

\[
D=\sum_{I\subseteq C,\ |I|=3}\|M_If\|_1
\]

包含全部二十张表，不取平均或最大单表误差。若用整数分子和共同单位 `DIV(1,s)`，整个证明可在分子账本完成后保留同一未求值单位；没有数值除法、约分或根读出。

## 2. 一个通用质量账本：避开正投影的负质量

对每张表令 `T_I=pi_I(S)`，并定义

\[
a_I=\sum_{z:\pi_I(z)\notin T_I}f_-(z),\qquad A=\sum_I a_I.
\]

T_I 外只有负质量，所以其 L1 恰为 a_I。T_I 内的 signed 总质量为 `P-N+a_I`，其 L1 至少是该总和。因此

\[
\|M_If\|_1\ge P-N+2a_I. \tag{1}
\]

这里没有把多个正投影地址的 L1 错写为单个绝对值等式；只用了对任意有限实数列都成立的 `sum |h| >= sum h`。无论正投影是否碰撞或原本已在 T_I 内相消，(1) 都成立。

若每个负点至少在 k 张表避开全部正投影，则交换有限求和得 `A>=kN`，从而

\[
D\ge20P+(2k-20)N. \tag{2}
\]

每张表也有 `L1>=N-P`，故

\[
D\ge20(N-P). \tag{3}
\]

对 `0<k<=20`，将 (2) 乘 20、(3) 乘 `20-k` 后相加，两侧系数均非负，得到

\[
\boxed{(40-k)D\ge20k(P+N).} \tag{4}
\]

这一步直接消除 P、N，不需要对 N/P 求最值，也不需要假定 P=N。N=0 时同样适用。

## 3. 两正点相差一轴或至少三轴

现在 p(f)=2，写 `S={u,v}`，u、v 是两个不同 Cell。令

\[
J=\{i:u_i\ne v_i\},\qquad d=|J|\in\{1,\ldots,6\}.
\]

对任意负点 z，定义

\[
Q=\{i:z_i=u_i\},\quad R=\{i:z_i=v_i\},\quad
q=|Q|,\ r=|R|,\ c=|Q\cap R|.
\]

由于 z 不是 u 或 v，`q,r<=5`。表 I 投影到某个正地址当且仅当 `I subseteq Q` 或 `I subseteq R`，所以这样的表数恰为

\[
G(z)=\binom q3+\binom r3-\binom c3. \tag{5}
\]

当上标小于 3 时二项式记为零。这是表的集合并计数，没有把两正投影重合的表重复计算。

**d=1。** 在五条共同轴上 Q、R 完全相同，在唯一差轴上 z 至多匹配 u、v 的一个值。因此 Q、R 嵌套，包括相等的情形。由 `max(q,r)<=5`，

\[
G(z)=\binom{\max(q,r)}3\le10.
\]

每个负点至少避开 k=10 张表。(4) 给出 `20M<=3D`，所以该情形满足比 1/4 更小的统一上界 3/20。

**d>=3。** Q 与 R 的交集只能来自 u、v 相等的共同轴，故 `c<=6-d<=3`。并且

\[
q+r-c=|Q\cup R|\le6. \tag{6}
\]

若 q、r 均不超过 4，则 (5) 给出 `G(z)<=4+4=8`。否则交换名称后可设 q=5，由 (6) 得 `r<=c+1`，所以

\[
\begin{aligned}
G(z)&\le10+\binom{c+1}3-\binom c3\\
&=10+\binom c2\le13.
\end{aligned}
\]

故所有负点至少避开 k=7 张表。(4) 给出

\[
140M\le33D.
\]

由于 `4*33=132<140`，系数 33/140 严格小于 1/4。这包括负坐标、第三种坐标值以及任意大跨度；计数只使用相等关系，没有把坐标偷换成二值。

## 4. 唯一剩余情形 d=2：显式观察函数

设 `J={a,b}`，其余四条共同轴记为 W；对 `j in W` 记 `w_j=u_j=v_j`。四张同时包含 a、b 的表组成

\[
\mathcal H=\{\{a,b,j\}:j\in W\}.
\]

另外十六张表组成 L。为每张 raw 表定义分析用的有界函数

\[
b_I(t)=
\begin{cases}
1,&I\in\mathcal H,\ t\in T_I,\\
-1,&I\in\mathcal H,\ t\notin T_I,\\
0,&I\in\mathcal L,\ t\in T_I,\\
-1,&I\in\mathcal L,\ t\notin T_I.
\end{cases}
\]

令 `F(x)=sum_I b_I(pi_I(x))`。每个 b_I 的绝对值至多 1，而且

\[
F(u)=F(v)=4. \tag{7}
\]

下面对整个 Z^6 中任意 `x notin {u,v}` 证明 `F(x)<=-4`。

**情形 A：** `(x_a,x_b)` 不等于 `(u_a,u_b)` 或 `(v_a,v_b)` 这两个正对角 tuple。四张 H 表都不能落在正投影地址上，故四项全为 -1。其余项至多零，因此 `F(x)<=-4`。

**情形 B：** 这个 tuple 等于其中一个正对角。由于 x 不是对应的正点，至少一条共同轴改变。令

\[
h=|\{j\in W:x_j\ne w_j\}|\ge1.
\]

四张 H 表中的每个未改变共同轴给 +1，每个改变轴给 -1，所以其总贡献准确为 `4-2h`。

任选一条改变的共同轴 j。包含 j 的三轴集合共有 `binom(5,2)=10` 个，其中只有 `{a,b,j}` 属于 H；另外 **九个全部属于 L**。每个这样的表都观察到 `x_j!=w_j`，而两个正点在 j 上均为 w_j，所以这九项全为 -1。其余 L 项至多零。这里已排除了那一个 H 表，没有跨组重复计数，故

\[
F(x)\le4-2h-9\le-7<-4. \tag{8}
\]

任意坐标值都落入 A 或 B；B 中多个共同轴改变只会加强界，不会削弱这九项的有效性。因此

\[
F(x)\le-4\quad\text{对所有 }x\notin S. \tag{9}
\]

对每张表，由 `|b_I|<=1`，有 `L1(M_I f)>=sum_t b_I(t) M_I f(t)`。交换有限求和，并使用 (7)、(9) 与 Jordan 正负支撑不交，得到

\[
\begin{aligned}
D
&\ge\sum_I\sum_t b_I(t)M_If(t)
=\sum_x F(x)f(x)\\
&=4P+\sum_{x\notin S}F(x)(-f_-(x))
\ge4P+4N=4M.
\end{aligned} \tag{10}
\]

负号乘法方向在最后一步反转，故 `F<=-4` 正好给出正的 `4N` 下界。两个正点的权重不必相等；F 在二者都是同一个数 4。负支点数和负权重也没有额外限制。

## 5. p<=1、零差与 sharp 见证

p=1 时，既有已审 raw 单正支点界给出 `20M<=3D`，因此满足 (10)。也可把第 2 节账本用于单个正地址：负点最多匹配五轴，所以 k=10，得到同一个界。

p=0 时 f 整体非正，每张 raw 表均非正且 L1=M，因此 `D=20M`。f=0 时 M=D=0，保留不等式而不报告 0/0。

为证明 1/4 不能缩小，固定任意两条实际轴 a、b，取两个不同整数值 `alpha_0!=alpha_1`、`beta_0!=beta_1`，另四轴固定为同一个 w。在这四个原生 Cell 上放置如下 signed 分析质量：

| a 轴 / b 轴 | beta_0 | beta_1 |
| --- | --- | --- |
| alpha_0 | +1 | -1 |
| alpha_1 | -1 | +1 |

正、负两侧分别由两条单位正质量分支组成，Jordan 后恰有两个正点，M=4。四张同时观察 a、b 的表均保留四个不同地址，每张 L1=4；另外十六张表至多观察一条差轴，同地址的正负单位质量逐项相消，因此每张为零。故

\[
M=4,\qquad D=4\cdot4=16,\qquad D=4M.
\]

这是合法 raw X6 矩形见证，不需要单位坐标跨度、不增加维数，也不需要运行验证程序。见证本身正负总质量相等，所以额外要求等总质量也不能把本题的统一常数降到 1/4 以下。本文未分类全部取等对象。

## 6. 世界观、观察与状态边界

- 该定理属于聚合后的空间质量分析。原 mu、nu 是正人口；f、b_I 的符号用于数学分析，不是负 BRC primitive 或实际事件权重。
- 必须保留 raw 地址，或其无损联合 `(can3, common offset)` 编码。can3-alone、分离的 can3/depth 直方图、任意线性观察、最大单表范数或二十表平均值不自动继承本常数。
- 计数没有恢复 branch history、路径顺序、路径数、common-depth 或微观 WeightHistogram，也没有声明观察函数是原生 isometry 或动力操作。
- 对 p=2 的证明是全体有限输入的纸面推导，不是从有限样例归纳；本次没有程序或运行时算术合规证书，也没有把原工具的有限执行审查扩大为传递合规。
- p>=3 的 sharp 常数没有由此解决；没有修改一般 p<=7 的现有结果、工具状态、任务权威或 Foundation。

## 7. 精确来源与审查结论

| 已读来源 | 本次核验 SHA256 |
| --- | --- |
| `research_method_inventory_addenda/20260907_owner_native_frontier_candidates.json`，19 项 | `9b9b1851602200bbb207681dbac444a7e745b2915d6f8851bc999fd3a028f115` |
| `research_notes/OWNER_ONE_POSITIVE_STABILITY_20260907.md` | `b49eac9291c7b6a6ec458a133700ee17a4573972e58787a976871512746dd4e7` |
| `research_notes/OWNER_X6_STABILITY_20260907.md` | `2915e70210dce5bc136c915e45e96a7c8a1f6dd414fae1590a4687f41bff3127` |
| `research_notes/OWNER_POSITIVE_SUPPORT_RAW_COMPRESSION_REVIEW_20260908.md` | `2cb061262e713859fd419871d0be9e4d5041698a01a46a55bd5ef5fc3f7e38b4` |

最终判定：**PASS**。d>=3 的并集计数、d=2 的额外九表、任意质量差与坐标值，以及 sharp 矩形见证均有完整直接论证。未发现反例或需要补充的实质假设；Jordan 后负支撑不含正点、完整 raw 二十表及共同 chart 是不可省略的已有合同。此回执只支持这一限定纸面结论，不执行任何正式状态晋升。

Global-Knowledge-Sync: main@990d7c1 / GLOBAL_KNOWLEDGE_V1
