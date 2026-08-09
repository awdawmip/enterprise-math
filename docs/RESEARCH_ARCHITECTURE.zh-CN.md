# Enterprise Math / 进取数论研究架构

状态：`PROPOSED / MIGRATION IN PROGRESS`  
生效快照：`2026-08-09`  
源主干快照：`9fe0eb4b9a5a635a029ca5c0d0b5211280aa0c2c`

## 1. 目的与权限边界

Enterprise Math 已经超出按编号问题线性排列即可完整描述的阶段。`Pxxx` 与 `Exxx` 编号仍然是重要的研究身份和来源锚点，但多个分支已经从不同领域独立发现了相同或相近的数学结构。

本文件增加第二条组织轴：**可复用数学结构的归属轴**。它不重新编号已解决问题，不悄悄扩大 `RESOLVED` 的范围，不把研究 WIP 自动提升为 `FOUNDATIONS`，也不改变 `PROBLEM_STATUS` 作为权威问题状态账的地位。

总规则是：

> 保留成果最初被发现的位置；但最一般的已证明陈述只维护一次，放到真正拥有其最弱假设、又能被多个方向复用的数学位置。

当一个问题分支中的母定理被向上提炼后，原问题仍保留领域特化的推论、例子、反例、研究动机与发现来源。

另一个同等重要的规则是：

> 术语相似不是数学对象相同的证据。只有在明确证明等价、特化或严格推广关系以后，两条路线才能合并。

## 2. 两条相互正交的组织轴

### 轴 A —— 可复用数学归属

下面是“定理应该归到哪里”的工作结构，不是新的公理编号。

#### A0. 原始离散状态代数

主要来源：`P001–P009`。

包括整数根与坍缩、有符号状态区别、总尺度因子、typed scale transition、精确 quotient/remainder 语义、序伴随、复合、交换与固定点结构。

这一层向后续研究提供操作和类型纪律。各问题已经解决到什么范围，仍由 `PROBLEM_STATUS` 控制。

#### A1. 单值动力学、kernel 与稳定化

主要来源：`P010`、`P011`、规范 `P019`、`P020`，并与 `P018` 相连。

这里处理单值确定映射及其 fibers：严格历史合并、collision spectrum、随时间增长的 kernel、最终 coalescence 和有限稳定化。

**规范的 `P019` 只表示 collapse-word stabilization。** 历史研究分支里曾经用 `P019` 命名的几何或关系文件，不会因为旧文件名还存在就继续拥有规范 `P019` 身份。

#### A2. 精度、观察与 future-compatible quotient

主要来源：`P018` 和 `P023`；算术实例来自 `P002/P007`，应用来自 `P017/P021/E001`。

这里包括有限 observation、refinement fibers、精确 defect/response transport、面向证明目标的 ambiguity、dynamic closure / congruence、predictive refinement、minimal repair，以及“只有当未来需要的操作和观察都能下降到商状态时，才能真正丢弃细节”的规则。

`P018` 继续作为有限精度演算项目。`P023` 是最一般 future-compatible quotient 定理族的候选归属。在 `P023` 正式集成以前，这只是归属规划，不会反向改写已经在 P018 中成立的定理编号。

#### A3. Partition relation-state algebra —— 候选可复用核心

主要来源：原 minimum-precision-geometry 长分支的后期成果；现在从 `research/core/relation-quotient` 继续，并与 `P018/P022/P023` 相连。

这一条路线的核心对象是**结构化整数 relation field**，不是任意二元关系。对正整数 block capacities `m_i` 与整数 block totals `c_i`，当前路线使用

`Z_ij = m_j c_i - m_i c_j`。

给定 capacities、grand total 与合法的 `Z`，可以恢复当前各 block totals。partition coarsening 同时聚合 capacities/totals，并按 `Z' = A Z A^T` 聚合关系场；相应整数 partition kernel 同时描述 state fiber 与 coarse-invisible additive motion。

当前 A3 候选包括：

- tree-independent weighted relation state `(m,C,Z)`；
- 任意 partition quotient 及其复合；
- partition kernel `K_A`、relation rank 与 relation-scale quantum；
- exact present-state refinement data 与 Refinement Forest；
- 由声明好的线性 operations 与 observations 推导出的 minimum exact partition / relation precision；
- 定义在结构化 relation state 上、但不依赖具体几何的 observation channels。

A3 **目前不是 Foundation，也暂不分配新的 `P` 编号**。必须先从历史 P019/P022 命名中提炼出来，并完成 prior-art 审计。

#### A4. Admissible support / correspondence algebra —— 候选可复用核心

主要来源：E001 relational-collapse 路线；现在从 `research/core/admissible-support-relations` 继续，并与 `P011/P012/P018` 相连。

这一条路线的核心对象是**有限二元关系 / correspondence** `R ⊆ X×Z`，通常允许多值：同一 source 可以对应多个允许的 target states。它与 A3 的 skew integer field `Z_ij` 不是同一个对象。

当前 A4 候选包括：

- functional collapse 与 multivalued relational support 的区别；
- radius-indexed admissible relation families `R_r`；
- monotonicity 与 relational subadditivity `R_r ; R_s ⊆ R_(r+s)`；
- split-completeness 作为更强的 equality 情形，而不是普遍公理；
- common-target composition `R_r ; converse(R_s)`；
- target-incidence representations；
- witness spectrum `W_k` 与 group/event spectrum `G_k`；
- 当 relation 是 total function graph 时，精确退化 `W_k=G_k=J_k`；
- higher-order common-target structure 与 admissibility constraints。

A4 同样保持 **RESEARCH WIP**，不是 Foundation，也不是新编号问题。

#### A3/A4 桥梁 —— 明确保持开放

“relation”一词目前在 A3 与 A4 中发生了术语重载。这里**不预设二者等价**。

A3 是由 capacities 与 totals 导出的结构化数值状态表示；A4 是 source 与 allowed targets 之间的集合值 incidence/correspondence。

真正的桥梁定理至少需要回答：

- 在什么条件下，一个 A4 support family 能由某个 A3 state 加上声明好的 geometry/operations 完整生成？
- 在什么条件下，A4 observation 能 factor through 某个 A3 partition quotient？
- 为了恢复或判定一个 A4 common-target query，A3 的哪些 internal relations 是不可删除的？

这些命题没有证明以前，A3 与 A4 是相邻的 sibling cores，而不是一个已经统一的“relation theory”。

#### A5. 内禀离散几何

主要来源：`P012` 与 `P022`，必要时消费 A0/A2/A3/A4 的通用结果。

这里包括 primitive adjacency、整数 shortest-path metric、lattice/root-lattice geometry、有限 balls/shells、distance carry、radial/quadratic observation，以及几何专属 contraction 结果。

几何可以生成 A4 admissible support relations，也可以通过 A3 structured relation state 被观察；但一般的 relation-state algebra 与一般 support/correspondence algebra 都不应继续被锁在某个几何编号的分支里。

### 轴 B —— 研究问题与应用项目

即使复用了轴 A 的通用数学，问题/应用项目仍然保持一等地位。

- `P017`：Legendre / 连续平方之间的压力测试及其 square-basin 算术结构；
- `P018`：有限精度证明演算及其精度专属应用；
- `P021`：有限精度 causal horizon / focusing 及面向物理的方向研究；
- `P022`：minimum-precision lattice geometry 与 distance/carry；
- `E001`：可执行 collision/common-collapse 压力测试；
- `P016`：物理实现的 falsification contract。

一个应用项目完全可以首先发现通用定理。发生这种情况时，把一般陈述提升到轴 A；应用项目保留其原始特例与 provenance。

## 3. 已经识别出的跨路线成果合并

### 3.1 P017 → P018：quotient response 与 basin transport

P017 的精确 cofactor-window 宽度已经被证明就是 P018 quotient response 中的 `whole blocks + boundary carry`。这是同一结构在不同坐标下的表达，不应继续维护为两个理论。

同样，首先在 P017 中发现的 square-basin / floor-division 结果后来发现并不需要 prime 假设：一般定理应归 P018 quotient/root transport；P017 保留 lower-band least-factor 应用。

### 3.2 P018 ↔ P023：predictive closure 与一般 future-compatible quotient

P018 的 dynamic/predictive closure 与 P023 的 future-compatible quotient 在追问同一个母问题：什么时候 coarse observation 能承载精确自治的未来演化？不能时，最小 repair 是什么？

工作归属规则：

- P018 保留 precision interpretation、precision-time filtration、defect/response 坐标以及有限精度应用；
- P023 在正式集成后承担最一般的 operation-language factorization / congruence / minimal-repair 陈述；
- 若两边定理等价或一边严格推广另一边，必须明确写出这种关系，而不是用两套词汇长期复制两个 theorem family。

### 3.3 P021 → P023：先保留 witness identity，再谈 cardinality collapse

P021 direction transport 得到一个重要反例：count matrix 可以保留相邻 cardinalities，却丢掉未来精确复合需要的 witness identity。P021 中被证明安全的 reduction regime，进一步推动出“只有证明被丢弃的 identity 不会影响未来复合以后才可压缩”的一般原则。

一般 quotient-safety 归 A2/P023；P021 保留 direction-orbit、causal-role、focusing 与 witness-join 应用。

### 3.4 P011 → A4 relation spectra：函数只是 relation 的特例

对有限关系 `R ⊆ X×Z`，E001 relational 路线区分 witness multiplicity `W_k` 与 common-target group/event count `G_k`。当 `R` 是 total function `F` 的 graph 时，两者都严格退化为 P011 的 `J_k(F)`。

因此 P011 继续作为规范的单值函数/partition spectrum。A4 可以把它推广到 relations，但必须显式保留这个退化定理，也不能把在 multivalued relation 下会失败的单调性结论机械继承过去。

### 3.5 E001 ↔ P018 ↔ A4

E001 不再另建一套 precision calculus。P018 已经能够提供有限 observation/refinement 逻辑；把 observation 作用于有限 support 后，也能承载 MAY/MUST 类型的 refinement 行为。

分工如下：

- A4：admissible target/support relations 与 common-target 数学；
- P018/A2：observation/refinement 与 future compatibility；
- E001：可执行 collision workload、certificate、schedule、benchmark 和工程 falsification。

### 3.6 原 P019 relation-state 路线 ↔ P022 ↔ P023

原几何长分支发现了 tree-independent weighted relation state `(m,C,Z)`、partition quotient `Q_A`、整数 kernel `K_A` 以及精确 refinement-memory 结果。这些已经明显比 lattice geometry 更一般。

新的分工是：

- A3：抽象 structured relation-state / partition representation 与 kernel algebra；
- P022：root-lattice、metric、ball、radial、distance-carry 与几何专属 contraction；
- A2/P023：决定 A3 被删除的 internal relations 是否可对某个未来语言永久遗忘的安全条件。

分流以后，relation branch 已继续推进 observation-aware minimum exact relation precision；这属于 A3/A2，而不是新增 P022 geometry。

### 3.7 P012 → A4/E001/P022：几何是 admissible supports 的生成器

P012 的 primitive adjacency 可以生成有限 graph balls，进而生成 A4 target-support relations。E001 的方形 supports 只是其中一个具体实例。因此依赖方向应明确写成：

`primitive geometry -> admissible supports -> support observations -> precision/refinement -> application decision`。

这样可以避免把某个应用专属 collision 公式误当成新的 primitive geometry。

### 3.8 A3 ↔ A4：需要桥梁定理，而不是预设统一

A3 与 A4 很可能存在强交互，但当前对象不可互换。

A3 可以从 structured weighted relations 恢复一个 present block-total state；A4 追问每个 source 允许哪些 target states，以及这些 target sets 如何复合和相交。未来可能证明某个具体 A4 family 是某个 A3 state 的 derived observation，但必须对声明好的 generator/geometry 明确证明。

这个边界用于阻止“因为都叫 relation，所以是同一个理论”的错误统一。

## 4. 通用定理向上提炼协议

当某个分支看起来发现了可复用结果时：

1. **保留发现分支和精确 commit。** 不因为要改名就 force-rebase。
2. **寻找最弱假设。** 一项一项移除领域前提，并给不能移除的前提保留显式反例。
3. **与现有路线比对。** 查找等价 invariant、坐标变换、特例和已有 prior art。
4. **合并以前先分类关系。** 至少使用 `same`、`strict generalization`、`specialization`、`independent`、`conflict` 五类之一。
5. **完成第 4 步后才能选择唯一 mother statement。** 最一般的已证明陈述只有一个可复用归属；原项目保留 corollary 与 provenance。
6. **双向记录复用。** 来源项目引用提炼后的定理；通用核心也记录是谁、在哪个压力测试中首先暴露该结构。
7. **在最新 main 上 semantic replay。** 高度 diverged 的历史分支不应为了合并而整条硬并入主干。
8. **照常通过仓库 gates。** bilingual、reference/lineage、测试及适用的 Lean gate 均不降低标准。
9. **不要把词汇自动升级为本体。** coordinate、chart、witness、observation、relation 与 physical interpretation 必须分层，除非有定理证明它们在不变量意义下相同。

## 5. 非破坏性迁移规则

- 现有 branch 是研究历史，不在本轮迁移中当作“垃圾”删除。
- 精确 checkpoint branch 继续作为固定审计锚。
- 新 continuation branch 可以和旧 branch 指向同一个 commit；这是 namespace migration，不是复制数学权威。
- 不能因为有了更好的 branch name 就直接关闭旧 open PR。只有完成 clean replay 或明确的等价审计，确认所有成果被接住以后，才关闭/标记 superseded。
- 任何历史 `P019_*` 几何/关系文件都不能以旧编号直接进入 main。规范 `P019` 已经是 collapse-word stabilization。
- `P021` 的物理解释始终位于数学定理下游，并受 P016 falsification contract 约束。
- A3/A4 在 theorem boundary、prior art 与 clean integration 审计完成前都保持 `RESEARCH WIP`。

## 6. 迁移后的直接研究前沿

1. 在尝试任何 bridge theorem 以前，分别建立 A3 与 A4 的 theorem-by-theorem lineage matrix。
2. 判断 E001/P022 相关的 A4 admissible-support family 是否能 factor through A3 weighted relation state；不能时精确找出丢失的信息。
3. 证明或否定 P018 predictive closure 与 P023 相应 operation-language closure 的精确等价关系；一般定理只保留一套。
4. 把 P011 推广到 A4 relations 时必须同时保留 `W_k` 与 `G_k` 的不同语义及单调性边界。
5. 从混合历史分支把 P022 geometry 在当前 main 上 clean replay，只在 A3/A4 确实能简化几何时引用它们。
6. 把 P021 按规范编号 clean replay 到当前 main，并保留 witness identity 与 physical/falsification boundary。
7. E001 的工程测量和数学主张继续分开；使用抽出的 reusable cores 作为依赖，而不是继续在 benchmark branch 内复制理论。
8. P017 继续作为压力测试：一般结果向上提炼，square-basin 专属约束留在本地；一旦证明两条坐标路线等价，就停止重复维护。

## 7. 架构不变量

只有当未来研究员在不丢历史的情况下，都能回答下面四个问题时，迁移才算成功：

1. 这个结果最初在哪里被发现？
2. 它最一般的已证明数学形式是什么？
3. 现在应该在哪个 branch 继续推进这个一般形式？
4. 哪个原问题/应用 branch 仍然消费它？

如果一次仓库整理让这四个答案中的任何一个更难恢复，这次整理就是错误的。
