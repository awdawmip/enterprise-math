# R004 精度起源——补充 30：joint witness coupling 与 lossless marginalization gate

状态：`PROVED_WIP + EXECUTABLE_REFERENCE + A4/WEIGHTED-RELATION SPECIALIZATION`  
父文档：`R004_PRECISION_GENESIS_QUANTUM_MACRO_CLOSURE_SUPPLEMENT_29.zh-CN.md`  
Owner branch：`research/r004-precision-genesis-closure-20260810`

补充 28–29 已在线性 module 世界中分解 simultaneous target requirements。本补充回到任意有限 witness semantics，先固定在任何 algebraic compression 之前真正 canonical 的对象：同一批 fine witnesses 上所有 target coordinates 的 joint weighted coupling。

Relational projection、multivalued dependency 与 lossless join 属于成熟数据库关系理论。R004 当前只研究这些对象如何进入 typed Representation Compiler 与 A4 escalation ladder。

## 1. Joint weighted coupling

设 `q:X->Q` 为有限 source collapse。多个 target maps

`t_i:X->T_i`, `i=1,...,m`

共享同一个 fine witness x。witness weight 取值于声明的交换幺半群 M。

对 coarse state a 与 joint target tuple `y=(y_1,...,y_m)`，定义

`J_a(y)=op_{x:q(x)=a, t_i(x)=y_i for all i} w(x)`。

这就是一个 typed weighted relation

`J:Q x (product_i T_i)->M`。

重要 special cases：

- Boolean OR：joint MAY support；
- natural-number addition：joint witness-count tensor；
- finite-label union：joint witness-label coupling。

补充 13 的 generic weighted-relation machinery 可以直接作用于 product target carrier，不需要新建 mother relation theory。

## 2. Marginals 是 pushforward

对 joint target carrier 上任意 finite map `f:Y->Z`，定义

`(f_*J)_a(z)=op_{y:f(y)=z}J_a(y)`。

由 associativity / commutativity 得到 exact functoriality：

`(g o f)_*J=g_*(f_*J)`。

每个 target marginal 只是 coordinate projection

`pi_i: product T_j -> T_i`

下的 pushforward。

coupled target predicate 或 target-side quotient 同样只是另一种 pushforward。

所以 joint witness state 可以沿后续 deterministic target maps exact transport，不必重新打开 fine witnesses。

## 3. Marginals 一般不能恢复 coupling

Erasure

`J -> (pi_1*J,...,pi_m*J)`

一般是 many-to-one。

最小 Boolean/count example 用两个 binary targets。

Diagonal coupling：

`{(0,0),(1,1)}`

与 anti-diagonal coupling：

`{(0,1),(1,0)}`

在两个 coordinates 上都有完全相同的 marginal MAY support `{0,1}`。

若每个 witness count 都为 1，则 count tensors

`[[1,0],[0,1]]`

与

`[[0,1],[1,0]]`

也具有完全相同的 row/column count marginals `(1,1)`。

但 coupled predicate `y_1=y_2` 在第一张表上的 count 为 2，第二张表为 0。

所以

`marginal semantics !=> joint witness semantics`。

只要 remaining future 中仍有 coupled query，joint coupling distinction 就仍然 live。

## 4. Boolean uniqueness theorem

设 J 是 `product_i T_i` 中非空有限 relation，`S_i=pi_i(J)` 为各 marginal supports。

这些 marginal supports 在所有具有同样 projections 的 relations 中唯一决定 J，当且仅当**至多一个 S_i 是 non-singleton**。

证明：

- 若至多一个 marginal non-singleton，所有 singleton coordinates 被固定，而唯一变化 coordinate 的每个值都必须出现，所以 J 被强制为完整 rectangular product。
- 若至少两个 marginals 各有至少两个 values，则完整 rectangular product 与“删掉一个 tuple”的 relation 仍具有相同 coordinate projections：被删 tuple 的每个 coordinate value 都能通过改变另一个 non-singleton coordinate 在剩余 tuple 中继续出现。

因此，只要真正存在多 coordinate coupling，自身的 MAY marginals 一般不足以重建 joint relation。

## 5. Rectangularity 是 reconstruction certificate，不是 inference rule

定义 rectangular hull

`Rect(J)=product_i pi_i(J)`，

以及 Boolean coupling obstruction

`C(J)=Rect(J)\J`。

则

`C(J)=empty <=> J=Rect(J)`。

如果在擦除之前已有 explicit lossless-factorization witness 证明 `C(J)=empty`，joint MAY support 可由 marginals 重建。

但 J 一旦被擦除，nontrivial marginals 本身并不能证明 rectangularity：相同 marginals 同时兼容 full rectangular relation 与 nonrectangular couplings。

所以 independence/lossless join 必须作为额外 reconstruction certificate；绝不能从 marginals 自动 upward lift。

这正是补充 23 no-upward-lift rule 的另一个实例。

## 6. COUNT 与 richer witness semantics

witness-count marginals 一般不能决定 joint contingency tensor。2x2 diagonal / anti-diagonal 已经是最小 counterexample。

对 LABEL / witness identity，marginal label sets 同样会丢掉“哪些 labels 在同一个 joint target tuple 上共同发生”的 coupling。

因此 exact fallback 必须始终保留 declared semantic strength 下的 joint typed weighted relation。Boolean rectangularity certificate 只能证明 MAY-level reconstruction，不会凭空恢复 COUNT、LABEL 或 witness transport。

## 7. Coupling state 自己也是 certificate carrier

J 一旦形成，后续 marginal query、coupled predicate 与 target transform 都只是 J 上的 deterministic observations / pushforwards。

所以补充 24 可以再次递归使用：把 finite joint-coupling table 本身当 certificate state，用**remaining coupled future language** 去编译它。

至此同一 future-safe quotient principle 已经递归作用三次：

1. compile world state；
2. compile retained certificate state；
3. compile joint-coupling state。

最后一个 coupled query 结束后，如果剩余 suffix 只使用 marginals，J 才可以安全降级成 marginal certificates。

## 8. Validation

Independent finite checks 包括：

- product shapes `2x2`, `2x3`, `2x2x2`, `2x2x3` 上全部 nonempty Boolean relations：共 **120** 个 distinct marginal-support profiles；Boolean uniqueness criterion 0 violation，其中 35 个 profiles 存在多个 couplings；
- 所有 entries 属于 `0,1,2` 的 nonzero 2x2 natural-count tables：64 个 distinct row/column margin profiles，其中 15 个允许多个 joint tensors；diagonal/anti-diagonal 是最小 ambiguity；
- **1,296** 个 count-table/component-map cases：joint pushforward 与后续 marginalization/composition 完全 commute。

这些是 finite exact WIP checks，不是 fresh full-repository CI 或 canonical-main claims。

## 9. Prior-art 与 ownership boundary

Relational projection、multivalued dependency、lossless join 与 contingency-table marginal ambiguity 都属于先行数学/计算机科学。Fagin 1977 的 multivalued-dependency 工作是 relation projections 无损重建的直接经典 prior。

Generic support/correspondence semantics 仍归 A4；generic weighted-relation aggregation 仍归 typed relation compiler / P023-A4 interface。R004 当前只增加 **joint witness coupling 必须先于 marginal erasure** 的 fail-closed placement，以及相应 reconstruction/liveness rule。

## 10. Next frontier

下一题不再是“marginals 会不会丢 coupling”，这已经关闭。真正值得研究的是 **coupling cuts**：给定 remaining coupled predicates，joint witness distinctions 中哪些是阻止 demotion 到 cheaper marginal/factored certificates 的 minimal obstructions？应继续把 obstruction-cut method 作用在 coupling-certificate state 上，而不是另造一个 correlation metric。
