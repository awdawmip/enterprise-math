# R004 精度起源——补充 31：typed coupling-liveness gates

状态：`PROVED_WIP + EXECUTABLE_REFERENCE + JOINT-COUPLING DEMOTION SPECIALIZATION`  
父文档：`R004_PRECISION_GENESIS_QUANTUM_MACRO_CLOSURE_SUPPLEMENT_30.zh-CN.md`  
Owner branch：`research/r004-precision-genesis-closure-20260810`

补充 30 已把 joint weighted coupling 固定为 marginal erasure 之前的 canonical strong certificate。本补充研究：remaining coupled query 在什么条件下仍能从 marginals exact 回答，从而允许退休 joint coupling。

答案严格依赖 semantic type。MAY、COUNT 与 LABEL-SET 具有不同的 exact gates。

## 1. MAY cylinder-forcing gate

设 retained marginal supports 为非空 finite sets `S_i`，令

`Y=product_i S_i`。

coupled MAY predicate 为 `P subseteq Y`。joint relation 擦除后，唯一已知事实是未知 coupling J 的 coordinate projections 恰好为 `S_i`。

### Forced false

`MAY(P)` 对所有 compatible J 都为 false，当且仅当

`P cap Y=empty`。

### Forced true

`MAY(P)` 对所有 compatible J 都为 true，当且仅当 complement

`Y\P`

至少在某一个 coordinate 上不再满投影到 S_i。

等价地，存在 coordinate i 与 value `v in S_i`，使完整 cylinder

`{y in Y:y_i=v}`

被 P 全部包含。

证明：存在 avoiding-P coupling 当且仅当 complement 中存在一个具有全部 required projections 的 relation；这又当且仅当 complement 的每个 coordinate projection 都 full，此时 complement 自己就是一个 witness relation。若某个 marginal value 从 complement 消失，任何 compatible relation 为了实现该 value 都必须 hit P。

除此之外 predicate 都 coupling-sensitive。

## 2. COUNT coupled-query gate

现在令 N(y) 为 joint nonnegative integer count tensor，并保留全部 one-dimensional count marginals

`m_i(v)=sum_{y:y_i=v}N(y)`。

对 integer coefficient tensor c，考虑

`Q_c(N)=sum_y c(y)N(y)`。

Q_c 对**所有** joint count tensors 都由一维 marginals 唯一决定，当且仅当

`c(y_1,...,y_m)=alpha+sum_i f_i(y_i)`

其中 f_i 为 integer one-coordinate potentials。

### Sufficiency

若该表示存在，

`Q_c=alpha*N_total+sum_i sum_v f_i(v)m_i(v)`。

### Necessity

Cartesian-product function 属于这种 additive form，当且仅当全部 mixed 2x2 rectangle differences 都为 zero。若某个

`c(a,b)+c(a',b')-c(a,b')-c(a',b)`

非零（其余 coordinates 固定），则标准 signed 2x2 cycle `(+1,+1,-1,-1)` 具有 zero one-dimensional marginals。给四格加 unit baseline 后得到两张 nonnegative integer joint tables：marginals 相同，但 Q_c 不同。

所以任何 non-additive COUNT query 都证明 joint count coupling 仍然 live。

## 3. Boolean predicate COUNT 比 MAY 更严格

若 c 是 predicate P 的 Boolean indicator，则 additive separability 强迫 P 至多依赖一个 nontrivial coordinate（含 empty/full trivial cases）。

若两个 coordinate potentials 都 nonconstant，选取各自两个 values 会得到四个 Boolean values：

`z,z+a,z+b,z+a+b`，

其中 integer `a,b` 都非零；不可能四个都落在 `{0,1}`。

因此

`COUNT(P) from one-way marginals`

当且仅当 P 本质上就是 marginal/single-coordinate query。

这严格强于 MAY：P 可以包含一个完整 cylinder，因此 MAY 被 marginals forced true，但其 exact count 仍然 coupling-sensitive。

## 4. COUNT gate 再次是 Structural Target Compiler

把 N 展平为 joint cells Y 上的向量。one-way marginalization 是固定 integer incidence matrix：

`A_marg N`。

一族 coupled linear count queries 是 target matrix：

`B N`。

则 exact condition 直接是

`ker A_marg subseteq ker B`，

即补充 20 Structural Target criterion 递归作用于**coupling certificate state**。

单个 query row c 的 additive-potential 条件正好是

`c in Row(A_marg)`。

所以 COUNT coupling liveness 不需要新 mother theory。

## 5. Full joint COUNT coupling dimension

若 target coordinate i 有 n_i 个 values，joint count tensor 有

`Ncells=product_i n_i`

个 coordinates。

one-way marginal incidence matrix rank 为

`r_marg=sum_i n_i-(m-1)`。

证明：其 row relation 等价于 one-coordinate functions g_i 满足

`sum_i g_i(y_i)=0`

对全部 joint tuples 成立。逐 coordinate 改变 y_i 会强迫每个 g_i 都 constant；m 个 constants 只有一条总和为零的约束，所以 row-relation dimension 为 m-1。

此外可选一个 base cell，再选每次只改变一个 coordinate 的 cells，得到 determinant ±1 的 full-rank integer minor。因此所有 nonzero Smith invariants 都为 1。

所以 full joint count tensor 相对于 one-way marginals 的 exact p-adic coupling defect 是 free module

`(Z/p^K)^(d_coup)`，

其中

`d_coup=product_i n_i-sum_i n_i+(m-1)`。

二维 r×c table 退化为 `(r-1)(c-1)`。

## 6. LABEL-SET gate 按 label 分解

finite label sets under union 等价于每个 label 一个 Boolean OR channel 的 product。

对每个 live label lambda，考虑“携带 lambda 的 joint tuples”的 Boolean support 与对应 marginals。lambda 是否进入 coupled predicate 的 union，正好是该 label-specific MAY query。

所以 marginal LABEL-SET certificates 能 exact 回答 coupled label-union query，当且仅当每个 live label 的 MAY cylinder gate 都 decisive。

只要有一个 label 仍 coupling-sensitive，joint label coupling 就必须继续 live。

## 7. Generic monoid fallback

本补充不主张任意 commutative monoid / query language 都有统一 closed form。

若没有 typed factorization theorem，就保留 joint coupling table 作为 certificate state，并使用补充 24 / P023 suffix compiler。compiler 必须 fail closed，不能从 marginal summaries 自动猜 independence。

## 8. Validation

### MAY

枚举 shapes `2x2`, `2x3`, `2x2x2`, `2x2x3` 上全部 nonempty Boolean relations。共 **120** 个 distinct marginal profiles；forced true/false/ambiguous gate 0 violation，其中 35 个 profiles 存在多个 couplings。

### COUNT

枚举 cell entries 属于 `{0,1,2}` 的全部 joint tables：

- `2x2`：81 tables / 65 margin profiles；
- `2x3`：729 tables / 425 margin profiles；
- `2x2x2`：6,561 tables / 1,537 margin profiles。

对所有 Boolean predicate coefficient tensors（分别 16、64、256 queries），"在每个 fixed-marginal fiber 上恒定" 与 additive-potential gate 完全一致。

另对 `2x2`、`2x3` 的全部 `{-1,0,1}` coefficient tensors（81 与 729 queries）做同样检查，仍 0 mismatch。

### Smith/rank formula

对 target coordinates 数 m=2,3,4、每轴 size 属于 `{1,2,3}` 的全部 shapes，共 **117** 个，one-way marginal incidence matrix 的 rank 都为 `sum n_i-(m-1)`，且全部 nonzero integer Smith invariants 都为 1。

## 9. Architecture consequence

“coupled query”本身不是充分的 compiler type。semantic layer 才决定 liveness：

- MAY 有 cylinder forcing；
- exact COUNT 要求 additive marginal factorization；
- LABEL-SET 按 label 分解成 MAY gates；
- generic witness semantics 回退到 joint coupling certificate。

同一个 syntactic predicate 在不同 declared semantics 下可以需要不同 representation precision。

## 10. Next frontier

下一题是 **coupling obstruction cuts for a family of live queries**。COUNT 已经提示可以把 query family 做成 Structural Target defect module；MAY 则更像 coupling-sensitive predicate hypergraph。目标是求“marginals 之外最小还需保留多少 coupling certificate”，而不只是判断 full joint state 是否必要。
