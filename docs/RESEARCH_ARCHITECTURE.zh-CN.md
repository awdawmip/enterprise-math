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

#### A3. Relation / support 与 partition-quotient 核心 —— 候选可复用核心

当前来源包括原 minimum-precision-geometry 长分支、E001 relational-collapse 路线，以及 `P011`、`P012`、`P018`、`P021`、`P023` 的交叉成果。

之所以需要这一候选归属，是因为两条原本属于应用的路线都已经长出了超出原标签的通用数学：

1. 原 `P019_MINIMUM_PRECISION_LATTICE_GEOMETRY` 分支已经发展出 capacity-weighted relation field、partition quotient、整数 kernel lattice、refinement memory、relation scale 以及 witness/value separation；
2. E001 已经发展出 admissible support relation、共同 target 复合、MAY/MUST support precision，以及在单值函数情形精确退化为 P011 collision spectrum 的 relation spectra。

这个候选核心**目前不是新的 Foundation，也暂不分配新的 `P` 编号**。当前任务仅是把共享的母陈述提炼出来，同时保证两个来源分支都不丢历史。

当前建议的内部拆分是：

- relation 表示与 partition quotient：weighted relation state、`Q_A`、`K_A`、relation rank、精确 present-state refinement 数据；
- admissible finite relations/supports：functional 与 multivalued collapse、common-target relation、split-completeness、target incidence；
- relation observations：单值 collision spectrum 作为特例、witness 与 group/event 双谱、几何 observation channels；
- witness/provenance：为了未来精确复合必须保留的信息，与只足以恢复当前 coarse value 的信息之间的区别。

future-operational safety 本身仍归 A2：A3 提供 relation state 与 quotient；A2 判断某个未来操作语言是否允许该 quotient 永久删除 internal detail。

#### A4. 内禀离散几何

主要来源：`P012` 和 `P022`，必要时消费 A0/A2/A3 的通用结果。

这里包括 primitive adjacency、整数 shortest-path metric、lattice/root-lattice geometry、有限 balls/shells、distance carry、radial/quadratic observation，以及几何专属 contraction 结果。

几何可以生成 admissible support relation 与 relation observation，但一般的 finite relation 或 partition quotient 理论不应继续被锁在某个几何编号的分支里。

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

### 3.4 P011 → relation spectra：函数只是 relation 的特例

对有限关系 `R ⊆ X×Z`，E001 relational 路线区分 witness multiplicity `W_k` 与 common-target group/event count `G_k`。当 `R` 是 total function `F` 的 graph 时，两者都严格退化为 P011 的 `J_k(F)`。

因此 P011 继续作为规范的单值函数/partition spectrum。A3 可以把它推广到关系，但必须显式保留这个退化定理，也不能把在 multivalued relation 下会失败的单调性结论机械继承过去。

### 3.5 E001 ↔ P018 ↔ A3

E001 不再另建一套 precision calculus。P018 已经能够提供有限 observation/refinement 逻辑；把 observation 作用于有限 support 后，也能承载 MAY/MUST 类型的 refinement 行为。

分工如下：

- A3：admissible target/support relation 与 common-target 数学；
- P018/A2：observation/refinement 与 future compatibility；
- E001：可执行 collision workload、certificate、schedule、benchmark 和工程 falsification。

### 3.6 原 P019 relation 路线 ↔ P022 ↔ P023

原几何长分支发现了 tree-independent weighted relation state `(m,C,Z)`、partition quotient `Q_A`、整数 kernel `K_A` 以及精确 refinement-memory 结果。这些已经明显比 lattice geometry 更一般。

新的分工是：

- A3：抽象 relation/partition representation 与 kernel algebra；
- P022：root-lattice、metric、ball、radial、distance-carry 与几何专属 contraction；
- A2/P023：决定 A3 被删除的 internal relations 是否可对某个未来语言永久遗忘的安全条件。

### 3.7 P012 → E001/P022：几何是 admissible relation 的生成器

P012 的 primitive adjacency 可以生成有限 graph balls，进而生成 admissible target-support relations。E001 的方形 support 只是其中一个具体实例。因此依赖方向应明确写成：

`primitive geometry -> admissible supports -> relation observations -> precision/refinement -> application decision`。

这样可以避免把某个应用专属 collision 公式误当成新的 primitive geometry。

## 4. 通用定理向上提炼协议

当某个分支看起来发现了可复用结果时：

1. **保留发现分支和精确 commit。** 不因为要改名就 force-rebase。
2. **寻找最弱假设。** 一项一项移除领域前提，并给不能移除的前提保留显式反例。
3. **与现有路线比对。** 查找等价 invariant、坐标变换、特例和已有 prior art。
4. **只选一个 mother statement。** 最一般的已证明陈述只有一个可复用归属；原项目保留 corollary 和 provenance。
5. **双向记录复用。** 来源项目引用提炼后的定理；通用核心也记录是谁、在哪个压力测试中首先暴露该结构。
6. **在最新 main 上 semantic replay。** 高度 diverged 的历史分支不应为了合并而整条硬并入主干。
7. **照常通过仓库 gates。** bilingual、reference/lineage、测试及适用的 Lean gate 均不降低标准。
8. **不要把词汇自动升级为本体。** coordinate、chart、witness、observation、physical interpretation 必须分层，除非有定理证明它们是不变量意义上的同一对象。

## 5. 非破坏性迁移规则

- 现有 branch 是研究历史，不在本轮迁移中当作“垃圾”删除。
- 精确 checkpoint branch 继续作为固定审计锚。
- 新 continuation branch 可以和旧 branch 指向同一个 commit；这是 namespace migration，不是复制数学权威。
- 不能因为有了更好的 branch name 就直接关闭旧 open PR。只有完成 clean replay 或明确的等价审计，确认所有成果被接住以后，才关闭/标记 superseded。
- 任何历史 `P019_*` 几何/关系文件都不能以旧编号直接进入 main。规范 `P019` 已经是 collapse-word stabilization。
- `P021` 的物理解释始终位于数学定理下游，并受 P016 falsification contract 约束。
- A3 relation/support 在 theorem boundary、prior art 和 clean integration 审计完成前保持 `RESEARCH WIP`。

## 6. 迁移后的直接研究前沿

1. 从两条独立来源提炼 A3 relation/support core，避免夹带 geometry 或 collision 应用专属假设。
2. 证明或否定 P018 predictive closure 与 P023 相应 operation-language closure 的精确等价关系；一般定理只保留一套。
3. 把 P011 推广到 relation 时必须同时保留 `W_k` 与 `G_k` 的不同语义及单调性边界。
4. 从混合历史分支把 P022 几何在当前 main 上 clean replay，只在确实能简化几何时引用 A3。
5. 把 P021 按规范编号 clean replay 到当前 main，并保留 witness identity 与 physical/falsification boundary。
6. E001 的工程测量和数学主张继续分开；用提炼后的 relation core 作为依赖，而不是继续在 benchmark branch 内长出第二套理论。
7. P017 继续作为压力测试：一般结果向上提炼，square-basin 专属约束留在本地；一旦证明两条坐标路线等价，就停止重复维护。

## 7. 架构不变量

只有当未来研究员在不丢历史的情况下，都能回答下面四个问题时，迁移才算成功：

1. 这个结果最初在哪里被发现？
2. 它最一般的已证明数学形式是什么？
3. 现在应该在哪个 branch 继续推进这个一般形式？
4. 哪个原问题/应用 branch 仍然消费它？

如果一次仓库整理让这四个答案中的任何一个更难恢复，这次整理就是错误的。
