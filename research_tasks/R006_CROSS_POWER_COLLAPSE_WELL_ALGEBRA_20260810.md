<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-R006-CROSS-POWER-COLLAPSE-WELL-ALGEBRA",
  "title": "R006 Cross-Power Collapse-Well Algebra",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "Build the missing well-level interaction theory for different perfect-power collapse partitions: exact well intersection, transport, splitting/merging, transient order defects, partition refinement, and the bridge from local well geometry to the already-canonical operator/lcm stabilization layer.",
  "next_action": "Consume P003/P004/P019 without reproving them; define the power-well partitions B_{p,k}, prove the exact p-to-q intersection-count formula, classify refinement by divisibility, then test whether the power-well family forms a gcd/lcm lattice internally while its ambient common refinement exposes genuinely new hybrid-well structure.",
  "dependencies": [
    {"target": "P003 collapse commutation classification", "action": "CONSUME", "satisfied": true},
    {"target": "P004 collapse-word fixed-point classification", "action": "CONSUME", "satisfied": true},
    {"target": "P019 exact lcm stabilization", "action": "CONSUME", "satisfied": true},
    {"target": "P002 basin/gap coordinates", "action": "CONSUME", "satisfied": true}
  ],
  "source_refs": [
    "research_tasks/R006_CROSS_POWER_COLLAPSE_WELL_ALGEBRA_20260810.md",
    "docs/P002_COLLAPSE_GAP_BOUND.zh-CN.md",
    "docs/P003_COLLAPSE_COMMUTATION.zh-CN.md",
    "docs/P004_COLLAPSE_FIXED_POINTS.zh-CN.md",
    "docs/P019_COLLAPSE_WORD_STABILIZATION.zh-CN.md"
  ],
  "evidence_status": "CANDIDATE_RESEARCH_HANDOFF",
  "last_progress_ref": "research scout taskbook",
  "last_progress_at": "2026-08-10T11:37:00+08:00",
  "hard_block": null,
  "tags": ["R006", "collapse", "power-well", "basin", "partition", "commutation", "lcm", "gcd", "transient", "A0"],
  "claim_lease_minutes": 1440
}
-->

# R006 — 不同 N 次方坍缩井互运算代数

Status: `CANDIDATE RESEARCH HANDOFF / NOT CANONICAL`

## 0. 任务定位

建立 **Cross-Power Collapse-Well Algebra / 不同次幂坍缩井互运算理论**。

现有 Enterprise Math 已经把“坍缩算子互运算”推进得较深：

- P003：分类 `C_p` 与 `C_q` 的交换与吸收；
- P004：有限坍缩词的共同不动点只由指数 lcm 控制；
- P019：固定坍缩词反复作用后精确稳定为 `C_L`，稳定商是 lcm join-semilattice。

本任务**禁止重做这些结果**。

缺失层是：

> **把坍缩井 / basin 本身当作对象，研究不同指数的井怎样相交、切分、吞并、搬运、共同细化，以及这些瞬态井结构怎样在长期稳定化中被压缩成 lcm 语义。**

如果成功，应形成 A0 的新基础工具层，而不是 P003 的一个备注。

---

# 1. 基本对象

对正整数 `p>=1`、`k>=0`，定义 p 次方坍缩井

\[
B_{p,k}=\{n\in\mathbb N:k^p\le n<(k+1)^p\}.
\]

等价地：

\[
B_{p,k}=R_p^{-1}(k).
\]

记整套 p-井分区为

\[
\Pi_p=\{B_{p,k}:k\in\mathbb N\}.
\]

需要严格区分：

- `C_p`：状态上的坍缩算子；
- `R_p`：井编号 / 根坐标；
- `B_{p,k}`：一个具体井；
- `Pi_p`：整个 p-井分区。

不得把这四层混成“坍缩”。

---

# 2. 第一条必须证明的 exact formula：井交连续性

固定 `p,q,k`，研究一个 p-井会与哪些 q-井相交。

由于 `R_q` 单调，候选 q-井编号应形成连续整数区间：

\[
J_{p\to q}(k)
=
\{R_q(k^p),\ldots,R_q((k+1)^p-1)\}.
\]

优先严格证明：

### Candidate R006-T01 — exact well-intersection interval

\[
B_{p,k}\cap B_{q,j}\ne\varnothing
\]

当且仅当

\[
R_q(k^p)\le j\le R_q((k+1)^p-1).
\]

于是一个 p-井与 q-井的相交数量精确为

\[
\boxed{
M_{p\to q}(k)
=
R_q((k+1)^p-1)-R_q(k^p)+1.
}
\]

这必须首先作为普通数学证明，而不是仅由穷举支持。

---

# 3. 三种局部 regime：切分、自对齐、吞并

研究指数大小关系控制的局部井几何。

候选现象：

## 3.1 `p=q`

\[
M_{p\to p}(k)=1.
\]

即严格自对齐。

## 3.2 `p>q`

p-井在数轴上相对增长更快，预期会被越来越多 q-井切开。

研究 exact lower/upper bounds，并证明或反驳：

\[
M_{p\to q}(k)
\]

随 `k` 无界。

连续近似

\[
\frac pq k^{p/q-1}
\]

只能作为发现工具，最终结论必须回到整数根界。

## 3.3 `p<q`

q-井相对更宽，一个 p-井最终应只落入极少数 q-井。

研究：

- 是否最终 `M_{p->q}(k) <= 2`；
- 何时等于 1，何时跨过一个 q-boundary；
- crossing 的 exact integer criterion；
- crossing indices 的稀疏结构。

不要把“导数趋于零”当证明。

---

# 4. 第二条母结构：整除序控制全局分区 refinement

P003 已知：

\[
C_p,C_q\text{ 全局交换}
\iff
p\mid q\text{ 或 }q\mid p.
\]

本任务研究井分区层面的对应定理。

定义“`Pi_p` finer than `Pi_q`”为每个 p-井都包含在某个 q-井中。

优先证明：

### Candidate R006-T02 — divisibility/refinement equivalence

\[
\boxed{
\Pi_p\text{ refines }\Pi_q
\iff
p\mid q.
}
\]

正向可利用 q 次幂边界同时是 p 次幂边界；反向必须给出完整论证，例如利用素数幂边界排除 `p∤q`。

如果成立，则：

> **整除序不仅控制算子吸收，也控制整个坍缩井分区的全局 refinement。**

这将是 P003 与 well geometry 的第一个真正 bridge theorem。

---

# 5. 双序结构：divisibility order × magnitude order

这是本任务的核心结构候选。

现有证据提示：

- **整除序** `p|q` 控制：分区 refinement、算子吸收、交换；
- **大小序** `p<q` 控制：局部井宽、切分/吞并方向、相交数量增长。

二者不相同。

例如 `2<3` 但 `2∤3`、`3∤2`：

- 局部井几何有明确粗细方向；
- 算子却非交换。

研究完整 pair-type classification：

1. `p=q`；
2. `p|q, p<q`；
3. `q|p, q<p`；
4. `p<q` 且互不整除；
5. `q<p` 且互不整除。

对每类给出：

- partition refinement；
- intersection multiplicity；
- transport shape；
- operator commutation；
- transient order sensitivity；
- stable lcm fate。

目标不是做表格，而是寻找能够统一这些性质的双序定理。

---

# 6. Power-well partition lattice

把 `Pi_p` 作为 partition lattice 中的一族特殊对象。

在明确规定 refinement order 后，研究：

### Candidate R006-T03 — internal gcd/lcm lattice

在 **power-well family 内部**，是否有：

- common refinement 对应 `gcd(p,q)`；
- common coarsening 对应 `lcm(p,q)`。

特别注意：必须区分

1. **在 power-well 子族内部求 meet/join**；
2. **在全部 partition 的大格里求真正 common refinement/coarsening**。

不可默认二者一致。

一个重要候选：

> ambient common refinement 的边界集合是 p-power boundaries 与 q-power boundaries 的并，而当 p、q 不可比时，它通常不是任何单一 `Pi_r`。

如果成立，这将产生一种新的：

**hybrid collapse-well partition / 混合坍缩井场**。

必须寻找最小显式反例和完整分类：

> 什么时候两个 power-well partition 的 ambient common refinement 本身仍属于 power-well family？

候选答案可能恰好是指数可比时。

---

# 7. 井传输：一个 p-井经过 `C_q` 后变成什么

定义集合像：

\[
T_{p\to q}(k)=C_q(B_{p,k}).
\]

研究并证明其 exact form。

一个自然候选是：

\[
T_{p\to q}(k)
=
\{j^q:j\in J_{p\to q}(k)\}.
\]

如果成立，进一步定义：

- transport cardinality；
- contiguous q-root-coordinate image；
- state-space gap after collapse；
- full-well vs boundary-partial-well contributions。

研究 transport composition：

\[
B_{p,k}
\xrightarrow{C_q}
T_{p\to q}(k)
\xrightarrow{C_r}
\cdots
\]

集合层的 transport 是否保留比单点算子复合更多的瞬态信息？

---

# 8. 完整井 / 部分井分解

仅知道相交 q-井数量还不够。

对 `B_{p,k}` 与 q-井分解，区分：

- fully contained q-wells；
- left boundary partial well；
- right boundary partial well；
- 两端是否可能落在同一 q-well。

建立 exact observables：

- `F_{p->q}(k)`：完整包含 q-井数；
- `L_{p->q}(k)` / `R_{p->q}(k)`：两端截断长度；
- `M_{p->q}(k)`：总相交井数；
- normalized integer boundary coordinates。

寻找 Euclidean-division / carry 表达。

这一层可能与 P002 gap/basin coordinate、P007 quotient/remainder、P018 carry 发生直接连接。

---

# 9. 顺序缺陷场：从“是否交换”升级为“哪里不交换”

P003 已解决全局二值问题：是否处处交换。

本任务禁止重新证明这个 yes/no 分类，而应研究更细的 transient defect geometry。

定义例如：

\[
D_{p,q}(n)=C_p(C_q(n))-C_q(C_p(n)).
\]

或更稳健地保留有序 pair：

\[
\Delta_{p,q}(n)=
(C_pC_q(n),C_qC_p(n)).
\]

研究：

- defect support；
- defect 在 `(p,q)` 井交 cells 上是否常值；
- 最小充分坐标；
- 最大 defect / signed defect；
- defect zero fibers；
- defect 是否具有 scale/carry 周期；
- incomparable exponents 的最小 witness 是否只是冰山一角。

目标：

### Candidate R006-T04 — order-defect cell decomposition

把非交换性定位到具体 cross-well cells，而不是只保留一个 `2^max(p,q)` 见证。

---

# 10. 坍缩词的瞬态井几何 vs P019 稳定 lcm

P019 已证明任意固定词最终只剩：

\[
C_{L(W)}.
\]

本任务研究：

> 在稳定到 lcm 之前，井层到底保存了多少词序信息？

对坍缩词

\[
W=(p_1,p_2,\ldots,p_m)
\]

研究：

- transient well itinerary；
- intermediate partition sequence；
- well-count contraction profile；
- order-sensitive path multiplicity；
- stabilization depth；
- 两个具有相同 lcm 的不同词，其 transient well geometry 如何分类。

定义候选“瞬态复杂度”：

- 最大中间井数；
- total split/merge count；
- cumulative defect；
- shortest stabilization word；
- same-lcm word distinguishability horizon。

目标是判断：

\[
\text{full transient well algebra}
\longrightarrow
\text{stable quotient }(\mathbb N_{>0},\operatorname{lcm})
\]

能否成为一个真正的 quotient / forgetful structure。

---

# 11. 是否存在真正的“井代数”

不要预设答案。

至少测试以下候选运算：

1. well intersection；
2. common refinement；
3. common coarsening；
4. collapse transport；
5. sequential transport；
6. well union only when structurally natural；
7. transient composition classes。

检查：

- closure；
- associativity；
- commutativity；
- idempotence；
- absorption；
- identity/zero-like objects；
- typedness。

如果没有一个统一 algebra，允许得到更诚实的结论：

> 井结构需要 partition lattice + typed transport category / relation system，而不是单一二元代数。

不要为了“代数”这个名字硬造封闭运算。

---

# 12. 多指数 generalization

从 pair `(p,q)` 扩展到 finite exponent family

\[
P=\{p_1,\ldots,p_m\}.
\]

研究：

- ambient common refinement 的 boundary union；
- power-family internal refinement `gcd(P)`；
- common coarsening / stable semantics `lcm(P)`；
- hybrid cells；
- cell count；
- finite interval内的 exact boundary arrangement。

重点寻找：

### Candidate R006-T05 — finite-family boundary theorem

有限指数族的混合井 partition 能否由所有完全 `p_i` 次幂边界的有序并唯一确定，并得到 exact finite cell enumeration？

---

# 13. 与 P005 scale lattice 的关系

P005 的 `d` 是**同一 root order 下的尺度因子**；R006 的 `p,q` 是**不同 perfect-power exponent**。

严禁把两者混淆。

研究二者是否形成 typed product structure：

\[
(p,d)
\]

同时携带：

- exponent/well family；
- scale factor。

只有在已经完成 unscaled `p↔q` 基础之后，才允许进入：

\[
B_{p,d,k}
\quad\text{vs}\quad
B_{q,e,j}.
\]

不要一开始就把 R006 扩成四参数巨型问题。

---

# 14. exact executable atlas

建立纯整数研究工具，建议第一阶段：

- `p,q = 1..10`；
- `k` 先做到足够 exhaustive 的有限范围；
- 禁止浮点作为 correctness oracle。

至少实现：

- `power_well(p,k)` boundary representation；
- `intersecting_well_indices(p,q,k)`；
- `intersection_multiplicity(p,q,k)`；
- `well_intersection_length(p,k,q,j)`；
- `well_transport(p,q,k)`；
- partition-refinement checker；
- ambient hybrid-boundary builder；
- order-defect explorer；
- finite word transient itinerary。

所有公式必须与 direct enumeration 在 bounded domain 交叉验证。

计算用于发现/反例/回归，不替代证明。

---

# 15. 必须主动寻找的反例

### N1 — “大小序就等于 refinement 序”

这是明显危险的直觉。`p<q` 不等于 `p|q`。找最小明确反例并制度化。

### N2 — “gcd 就是 ambient common refinement”

对不可比指数，ambient boundary union 很可能严格少于 `Pi_gcd` 的全部边界。必须给出最小反例。

### N3 — “well transport 闭合成单一 power well”

集合像通常可能是若干离散 q-power states，而不是一个连续井。不要偷换对象类型。

### N4 — “same lcm means transient same”

P004/P019 已明确只保证固定点/稳定层相同。寻找最小 transient well-geometry 区分。

### N5 — “asymptotic ratio 就是 exact count”

所有连续近似必须有整数边界误差分析。

### N6 — “任意 partition operation 都值得叫新代数”

若结果退化为经典 partition lattice / closure operator / Galois connection，明确归入 prior art，只保留 Enterprise Math specialization。

---

# 16. Prior-art / lineage 必查

至少对照：

- partition lattices；
- closure/interior operators；
- commuting idempotents / projections；
- equivalence-relation refinement；
- semilattices / gcd-lcm lattices；
- interval partitions；
- symbolic dynamics / finite-state transients（如真正相关）；
- Galois connections；
- common refinement/coarsening of partitions。

不要因为“坍缩井”这个名字新，就把经典 partition mathematics 当作新发现。

真正可能的新贡献应来自：

- perfect-power basin family 的 exact specialization；
- divisibility-order × magnitude-order 双序结构；
- exact cross-power intersection/transport formulas；
- transient defect geometry；
- hybrid-well partition 的特殊分类；
- 与 P003/P019 的新 bridge theorem。

---

# 17. 第一阶段优先 theorem targets

按优先顺序：

1. **T01** exact cross-well intersection interval/count；
2. **T02** `Pi_p refines Pi_q iff p|q`；
3. **T03** power-well family 内部 gcd/lcm lattice；
4. **T04** ambient common refinement 何时仍是 power-well partition；
5. **T05** p>q split multiplicity unbounded / p<q eventual boundedness；
6. **T06** exact well transport image；
7. **T07** order-defect cell decomposition；
8. **T08** same-lcm transient distinguishability / quotient-to-P019 bridge。

不要一次铺太多 theorem prose；优先把 T01–T04 做硬。

---

# 18. Foundation backflow 问题

若 T01–T04 成立，必须判断是否出现新的基础母结构：

> **指数整除格是否同时控制 power-well partitions 的内部 refinement lattice，而指数数值大小控制其局部几何增长；二者组成一个此前 A0 未显式建模的 dual-order / two-order layer？**

如果这是可复用母结构，形成 Foundation Feedback Packet。

如果最终只是经典 partition lattice 的直接重述，则保持 A0 application-local，不强行 foundation promotion。

---

# 19. 与现有 owner 的边界

- P003 owns operator commutation/absorption；
- P004 owns fixed-point intersection/lcm；
- P019 owns exact repeated-word stabilization and stable lcm quotient；
- P002 owns ordinary single-power basin/gap coordinate；
- P005 owns same-root-order scale-factor lattice；
- R006 owns candidate **cross-power well interaction layer** only。

如果某个结果退化成已有 mother theorem，必须 `CONSUME`，不能重复占有。

成熟可复用结果通过 Relay / Foundation backflow 路由；taskbook claimant 不自动成为 mother-theorem owner。

---

# 20. 必须交付

至少返回：

1. precise well / partition / transport definitions；
2. T01–T04 的 proof 或 counterexample；
3. exact Python explorer + tests；
4. 至少一个不可比指数的最小 hybrid-refinement 反例；
5. 至少一个 same-lcm 但 transient-well geometry 不同的 witness；
6. `p<q / p=q / p>q` 的严格整数 regime theorem，而不是仅渐近图；
7. divisibility-order × magnitude-order 分类；
8. prior-art map；
9. 与 P002/P003/P004/P005/P019 的 ownership map；
10. 是否值得建立 canonical `collapse_well` shared module 的最小接口建议；
11. Foundation Feedback / Relay 候选。

---

# 21. 停止条件

以下任何一种都算有效完成：

- 得到一套非平凡 cross-power well theorem family；
- 证明所谓“井代数”大部分退化为经典 partition lattice，但留下精确的新 perfect-power specialization；
- 找到关键反例，证明某些预期闭包/格结构不存在；
- 证明双序结构不能统一，并明确其最小分层方式。

不要为了正结果无限扩大 cutoff。

---

## 最终必须回答

> **不同 N 次方坍缩井之间，是否存在一套比算子交换性更丰富、但又能在长期稳定化后自然压缩为 lcm 半格的瞬态互运算结构？**

以及：

> **“整除序控制代数、大小序控制井几何”是否能被提升为严格的 Enterprise Math 双序基础定理？**
