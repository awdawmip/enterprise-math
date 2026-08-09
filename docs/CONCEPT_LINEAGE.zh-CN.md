# Enterprise Math / 进取数论概念谱系矩阵

状态：`PROPOSED / ACTIVE AUDIT`  
快照日期：`2026-08-09`  
目的：判断不同分支里名称不同或相似的研究路线，究竟是同一个数学结构、严格推广、领域特化、可组合但独立，还是彼此冲突。

本文件属于架构/审计地图，不重新编号规范定理，也不把 WIP 成果提升为 `FOUNDATIONS`。

## 1. 关系标签

在合并两条路线以前，先使用下面标签分类：

- `SAME_MOTHER`：经过明确的记号、坐标或 horizon 编码变换后，两边实际上是同一个数学母定理。只维护一个可复用 mother statement，同时保留各来源的 corollary 与 provenance。
- `STRICT_GENERALIZATION`：目标路线移除了假设、扩大了 operation language，或覆盖严格更多对象，并且原结果作为真正的 theorem-level specialization 被包含。
- `SPECIALIZATION`：一般定理在特定算术、几何、物理或工程领域的实例。只要领域内容仍有价值，就保留。
- `GENERATOR`：一种结构为另一种结构生成例子或输入，但两者不是同一个理论。
- `COMPOSABLE_INDEPENDENT`：数学对象彼此不同，可以由声明好的 map/theorem 连接，但不能因词汇相同就合并。
- `CONFLICT / NEGATIVE_BOUNDARY`：一条路线证明某个看似自然的更强同一性或单调性是假的。反例必须作为架构边界长期保留。
- `NAME_COLLISION_ONLY`：只有历史命名重叠，没有数学归属关系。

两个分支出现同一个单词，本身不是合并证据。

## 2. Precision / quotient / future-compatibility 谱系

| 来源结果 | 目标/一般归属 | 关系 | 审计结论 |
|---|---|---|---|
| P018 T151–T152/T159：observation kernel 动态封闭 iff fine endomap 能下降为自治 coarse dynamics | P023 T01：fiber constancy iff chosen future observable factor through quotient | `SPECIALIZATION` | P018 是 `q=O`、future observable 为 `O∘F` 时的 precision/semiconjugacy 特化。一般 factorization gate 归 P023；P018 保留 precision-time 语义、semiconjugacy、defect 与 observational interpretation。 |
| P018 T160–T168：有限 unary predictive refinement / future-observation signatures | P023 T03–T07：有限 deterministic future-compatible quotient refinement | `SAME_MOTHER` | 两边在有限 unary 情形的 recursion 与 theorem package 相同：monotone refinement、`N-c0` 上界、depth/horizon semantics、stable compatible quotient 与 coarsest compatible refinement。以后不能再作为两个一般 unary 理论各自增长。 |
| P018 T160–T168 / P023 T03–T07 | P023 T10–T14 finite operation-family closure | `STRICT_GENERALIZATION` | P023 把一个 endomap 推广为有限 named operation family，把一条 future trajectory 推广为所有 operation words。P018 C17 已明确把这一 multi-operation 情形留下为开放问题。 |
| P023 T02 coarsest one-step repair `(q,h)` | P018 predictive closure | `COMPOSABLE_INDEPENDENT` | T02 解决的是单个 future observable 的一步 repair；predictive closure 解决的是所有未来的自治 closure。前者可以成为后者的构件，但二者不是同一定理。 |
| P023 T15–T16：`Q_r` 在 `D_d` 下的 boundary-bit repair | P007/P018 quotient/remainder/carry geometry | `SPECIALIZATION + NEW MINIMALITY QUESTION` | 算术坐标来自既有 quotient/remainder geometry；P023 的新增点在于证明当前 future task 可能只需要一个 canonical bit，而不是完整 remainder。精确算术定理留在 P023，同时明确引用其 P007/P018 坐标来源。 |
| P021：cardinality transport 丢失 witness identity | P023 quotient-safety rule | `MOTIVATING SPECIALIZATION` | P021 给出应用级反例，证明 counts 可能不足以支持未来 composition；P023 抽象 legal-collapse criterion。P021 保留 direction/causal 对象，一般 factorization 归 A2/P023。 |
| A3 operation/observation-aware minimum exact relation precision | P018/P023 future-compatible quotient | `SPECIALIZATION / BRIDGE CANDIDATE` | A3 在 structured linear partition/relation-state 模型里计算 task-derived exact precision。未来应证明它是 A2 的实例，而不是宣布成第二套一般 future-compatibility 理论。桥梁假设仍需正式陈述。 |

### 合并决定

一般有限 unary theorem 以后只维护一份 mother statement。迁移期间保留 P018/P023 两套历史 theorem numbers 作为 provenance，但新的**一般推广**进入 P023/A2。P018 引用母定理，只增加 precision-specific consequences：kernel/time bifiltration、defect/response、carry/extension data、merger geometry 与算术实例。

## 3. P017 压力测试向可复用 precision 数学的提炼

| 来源结果 | 目标/一般归属 | 关系 | 审计结论 |
|---|---|---|---|
| P017 cofactor-window raw width = whole quotient blocks + one boundary carry | P018 quotient response / carry pattern | `SAME_MOTHER` | cofactor residue-hit 公式与 quotient-response carry 是同一 finite boundary phenomenon 的不同坐标表达。一般 response 只维护一份；P017 保留 square-basin cofactor 特化。 |
| P017 在 prime-oriented 动机下首先得到的 square-basin floor-division / quotient-root transport | P018 general quotient/root two-basin theorem | `STRICT_GENERALIZATION` | 后续发现 prime 假设可以删除。一般定理归 P018；P017 保留 lower-band least-factor consequence。 |
| P017 的 cofactor residue hit、quotient-response carry bit、common-center unique hit 等局部名称 | canonical P017 high-band hit machinery | `SAME_MOTHER` | P017 已经完成过一次正确合并。未来除非出现新的不变量证明两者真的不同，否则不得重新把它们当独立路线发展。 |
| P017 generic sieve-density heuristic | canonical P017 deterministic resource/correlation route | `CONFLICT / NEGATIVE_BOUNDARY` | independent-density 直觉会 telescope 或无法给出所需 deterministic control。把它长期保留为 forbidden shortcut，而不是活跃平行证明路线。 |

### P017 架构规则

P017 保持领域压力测试，不作为它暴露出的所有通用结构的仓库。只要证明允许，就移除 prime/square-basin 假设并把 mother theorem 提升；P017 本地只保留真正依赖 square-basin / least-factor / resource constraint 的成果。

## 4. Functional irreversibility 与 relational spectra

| 来源结果 | 目标/一般归属 | 关系 | 审计结论 |
|---|---|---|---|
| P011 total deterministic map 的 collision spectrum `J_k(F)` | A4 witness spectrum `W_k(R)` 与 group/event spectrum `G_k(R)` | `EXACT SPECIALIZATION` | 当 `R` 是 total function `F` 的 graph 时，`W_k=G_k=J_k(F)`。P011 继续作为 functional fibers 的规范理论；A4 处理 multivalued correspondence。 |
| P011 deterministic postcomposition 下的单调性 | A4 deterministic target postcomposition 下的 `G_k` | `STRICT GENERALIZATION WITH BOUNDARY` | `G_k` 保留 group/event 单调性，但 `W_k` 不一定。禁止把 P011 的所有 monotonicity 自动搬到 witness multiplicity。 |
| P011 fiber partition | 一般 A4 support relation | `SPECIALIZATION` | function graph 让 source 按唯一 target 形成 partition；multivalued relation 的 target supports 一般重叠，未必形成 equivalence relation。 |
| pairwise common-target graph | A4 higher-order common-target hyperstructure / `G_k` | `CONFLICT / NEGATIVE_BOUNDARY` | pairwise intersection data 一般无法恢复 triple 及更高阶 common targets。没有证明以前，禁止把 higher-order support structure 换成简单 graph。 |

## 5. 两个不同的“relation”核心

本轮审计最重要的负向合并结论：A3 与 A4 **不是同一个对象**。

| A3 —— partition relation-state algebra | A4 —— admissible support/correspondence algebra |
|---|---|
| structured integer field `Z_ij=m_j c_i-m_i c_j` + capacities/totals | arbitrary-but-admissible finite binary relation `R⊆X×Z` |
| 表示当前 block-total state 的精确结构信息 | 表示每个 source 允许哪些 target states |
| partition quotient  obeys `Z'=AZA^T` | composition 是普通 relation composition |
| kernel `K_A={η:Aη=0}` 描述 invisible additive motion/state fiber | common-target relation 是 `R_r ; converse(R_s)` |
| rank/quantum/refinement forest 量化 structured state precision | `W_k/G_k` 量化 witness 与 common-target multiplicity |

关系：`COMPOSABLE_INDEPENDENT`。

当前共有的 “relation” 只是术语碰撞，不是 equivalence theorem。

### A3/A4 开放桥梁问题

1. 给定 geometry 或 operation family，什么条件下 A4 support relation 可以完全由 A3 structured state 推导？
2. 什么条件下 A4 common-target query 能 factor through A3 partition quotient？
3. 针对给定 A4 query language，A3 哪些 internal relation coordinates 是充分/必要的？
4. 在受限 admissible class 里是否存在自然 functor/forgetful map，还是两种结构在离开具体应用后根本不可比较？

至少有一个精确桥梁定理成立以前，不允许架构上合并。

## 6. Geometry 谱系

| 来源结果 | 目标/一般归属 | 关系 | 审计结论 |
|---|---|---|---|
| P012 primitive adjacency 与 integer graph metric | P022 lattice/root-lattice geometry | `GENERATOR / SPECIALIZATION` | P022 可以选择具体 lattice 并推出 balls/shells、radial observations 与 carry；P012 继续作为 metric-foundation baseline。 |
| P012 finite graph balls / geometry-generated supports | A4 admissible support relations | `GENERATOR` | geometry 可以生成 admissible correspondence family，但这不意味着 A4 属于 primitive geometry。 |
| 历史 P022 分支里的 weighted relation-state machinery | A3 | `STRICT GENERALIZATION OUT OF GEOMETRY` | 公式一旦不再使用 lattice/metric 假设，mother statement 就归 A3；P022 只保留 geometry instantiation。 |
| P022 radial/quadratic/distance observations | A3 observation-aware relation precision | `SPECIALIZATION / CONSUMER` | geometry 提供具体 observation rows/queries；A3 可以求它们所需的 minimum exact partition precision。 |
| E001 square-body/Chebyshev supports | P012/A4 | `APPLICATION` | E001 是一个 geometry-generated admissible-support 可执行系统，不是新的 primitive geometry。 |

## 7. Stabilization / kernel 谱系

| 来源结果 | 目标/一般归属 | 关系 | 审计结论 |
|---|---|---|---|
| P010 strict history merge | P018 pair/kernel filtration | `SPECIALIZATION / REUSE` | P018 把 kernel/pair 暴露为更底层 substrate，并增加 precision-time 语义；P010 保留 deterministic-history merge 的规范问题身份。 |
| P011 collision polynomial/spectrum | P018 time-resolved collision increments | `STRICT TEMPORAL REFINEMENT` | P018 把同一 finite partition evolution 按“何时发生 merge”继续分解；最终 spectrum 仍应引用 P011，而不是另起名字。 |
| P019 collapse-word stabilization | P020 well-founded stabilization | `SPECIALIZATION` | P020 提供一般 monotone reductive well-founded theorem；P019 保留精确 lcm collapse-word consequences 与 semilattice quotient。 |
| 历史 `P019_*` geometry/relation files | canonical P019 | `NAME_COLLISION_ONLY` | 旧文件名不产生 theorem ownership。规范 P019 是 collapse-word stabilization；历史 geometry/relation 按内容迁入 P022/A3。 |

## 8. P021 面向物理的谱系

| 来源结果 | 目标/一般归属 | 关系 | 审计结论 |
|---|---|---|---|
| Direction orbit、causal role、focusing/horizon constructions | P021 | `APPLICATION-SPECIFIC` | 这些保持 P021，不因为使用 witness transport 就提升为一般 quotient theory。 |
| witness relation vs count-matrix insufficiency | A2/P023 | `MOTIVATING SPECIALIZATION` | 负向结果暴露一般 information-sufficiency 问题；P023 负责抽象 quotient gate。 |
| physical horizon/time interpretation | P016 falsification contract | `DOWNSTREAM HYPOTHESIS` | many-to-one / focusing 数学结果本身不建立真实黑洞、时间本体、曲率或 GR 替代理论。 |

## 9. E001 分流后的谱系

| E001 资产 | 长期归属 | 关系 |
|---|---|---|
| collision engine、broad phase、adaptive schedule、exact oracle、benchmark | E001 | `APPLICATION / EXECUTABLE TEST` |
| finite observation/refinement logic | P018/A2 | `REUSE` |
| admissible support relations、common-target composition、split-completeness | A4 | `LIFTED GENERAL MATHEMATICS` |
| `W_k/G_k` relation spectra | A4，并显式保留 P011 degeneration | `LIFTED GENERAL MATHEMATICS` |
| CPU/performance measurements | 仅 E001 | `ENGINEERING EVIDENCE`，绝不是数学定理 |

这样分流可以防止 E001 长出第二套 precision calculus，也防止可复用 relation 数学被埋在 benchmark branch 内。

## 10. 立即执行的去重动作

1. 以后把 P018 T160–T168 与 P023 T03–T07 视为一个 unary mother theorem family。保留双方历史 theorem numbers，但停止平行增加一般 extensions。
2. multi-operation closure 继续由 P023 T10–T14/A2 推进；P018 只增加 precision-specific corollaries。
3. P023 one-step/minimal repair 保持独立子路线，不并入 predictive closure。
4. A3 与 A4 在桥梁定理出现以前严格分开。
5. P022 clean replay 时，先把所有不依赖 lattice 的 weighted relation theorem 提升到 A3，再集成剩余 geometry-specific 内容。
6. E001 clean replay 时依赖 A4，而不是在 engineering modules 复制 A4 理论。
7. P017 延续已经证明有效的策略：coordinate-equivalent routes 只保留一个；general result 向上提炼。

## 11. Provenance 规则

合并路线永远不等于删除发现历史。

每个 lifted theorem 都必须记录：

- 最初暴露该结构的 branch 与 commit；
- 原问题/应用动机；
- 最终可复用 theorem home；
- 仍然保留的 specialized corollary；
- 两者关系究竟是 exact equivalence、strict generalization，还是 application。

仓库应该因为整理而更容易推理，同时不能让真实的发现过程更难恢复。
