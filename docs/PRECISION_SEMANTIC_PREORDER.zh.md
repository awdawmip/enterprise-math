# Task-Relative Semantic Precision 是 Preorder，而不是一个 Scalar

状态：`RESEARCH BRIDGE / NONCANONICAL`

当前多条路线都出现同一个负边界：一个 representation 可以区分更多 raw states，却同时支持更少的 future operations 或 logical laws。因此，仅靠 observational refinement 不能完整定义 declared task 下的“更高 precision”。

## 1. 两个独立坐标

对相对于 future theory T 的 representation P，至少分开：

### Observational equivalence

`E(P)` 记录哪些 fine states 仍不可区分。

若

`E(P2) subseteq E(P1)`，

则 P2 在 observational sense 上比 P1 更细。

对 partitions 来说，就是 P2 的每个 block 都包含在某个 P1 block 内。

### Semantic capability

`C_T(P)` 是 declared task 中真正能穿过 P 的 capabilities，例如：

- safe operations；
- branch / witness reflection；
- 在 declared bound 下的 exact IMAGE reflection；
- DOMAIN legality channels；
- future language 依赖的 coefficient laws。

这里的 capability vocabulary 是 task-relative 的，不是 universal truth table。

## 2. Semantic refinement preorder

定义

`P2 >=_T P1`

当且仅当同时满足：

1. `E(P2) subseteq E(P1)`；
2. `C_T(P1) subseteq C_T(P2)`。

也就是说，semantic refinement 既要让 state distinctions 至少同样细，又不能丢掉已经 declared 必要的 semantic capabilities。

这是一个 **state detail × semantic capability** 的 product-style preorder。

## 3. 更细 state partition 可以失去 safe operation

取 state set `{0,1,2,3}`。

Coarse partition：

`{0,1,2}|{3}`。

Finer partition：

`{0,1}|{2}|{3}`。

定义 unary operation t：

`t(0)=0`, `t(1)=2`, `t(2)=0`, `t(3)=3`。

在 coarse quotient 上，第一个 coarse block 整体仍映回同一个 coarse block，所以 t 可以安全 descend。

在 finer quotient 上，0 与1仍 equivalent，但它们的 images 0 与2 已不 equivalent，所以 t 不安全。

因此 raw partition refinement 可以删除 safe-operation capability。

反向也可能发生：细化到 discrete partition 后，原本 coarse quotient 上不安全的 operation 可能因为不再有 equivalence constraints 而变得 safe。

所以 safe-operation spectrum 对 raw partition refinement 在两个方向都不单调。

## 4. Coefficient refinement 出现同样 tradeoff

对一个 prime p，有 quotient map：

`Z/p^2 Z -> Z/p Z`。

因此 mod `p^2` 在 numeric residue sense 上比 mod p 更细。

但是：

- mod p 是 field / domain，generic product-zero branch logic 可以 reflection；
- mod `p^2` 有 zero divisors，该 logical capability 消失。

如果 declared task 同时读取 numeric residues 与 labelled product branches，那么这两个 representations 互不 semantic dominate：

- mod `p^2` numeric detail 更高；
- mod p 拥有 mod `p^2` 缺失的 logical capability。

所以它们在 semantic preorder 中不可比。

## 5. Raw “higher precision” 必须 task-relative

若 task 只观察 residue 数值，从不重新读取 product-branch semantics，那么 mod `p^2` 确实是相关意义上 mod p 的 refinement。

若 task 需要 branch reflection，raw numeric order 就不再决定 semantic precision。

所以 precision order 必须依赖 future language，正如 P023 所要求的那样。

同一对 representations 在一个 task 下可以有顺序，在另一个 task 下可以不可比。

## 6. Abstract join 未必能在原 representation class 中实现

两个 requirement 的 abstract semantic join 可能同时要求：

- mod `p^2` numeric detail；
- generic integral-domain product-branch reflection。

如果把 representation class 限制为普通 scalar integer quotients `Z/MZ`，则要 numeric-refine mod `p^2` 必须有

`p^2 | M`。

此时 M 必为 composite，`Z/MZ` 不可能是 domain。

所以**不存在任何 scalar modulus 能实现这个 abstract semantic join**。

这比“两个 representation 不可比”更强：desired least common refinement 根本不在原 representation family 内。

## 7. Semantic precision 可以迫使 representation lift

要同时实现两项 capability，就必须 lift / factorize state，例如同时保留：

- mod `p^2` numeric residue；以及
- explicit branch / witness label 或 relation channel。

正确动作不是“继续选更大的 modulus”，而是“改变 state 携带什么”。

这是一个一般 precision-lift pattern：

`required semantic join not realizable in current representation class`

`=> enrich/lift representation instead of extrapolating one scalar precision axis`。

## 8. 与 safe-operation algebra 的关系

一个 quotient 的 safe-operation monoid 来源于哪些 operations preserve 它的 equivalence classes。

更细 partition 并不保证保住 coarse partition 上的 safe-operation family。因此 quotient detail 与 operation language 在 safe-operation 路线中本来就是两个不同坐标。

Coefficient branch reflection 只是在另一张 surface 上重现同一 architecture。

共同结论是：

> **precision 必须包含未来哪些 operations / laws 仍可 executable，而不只是当前 observational partition 有多细。**

## 9. Capability sets 是 declaration，不是 universal property list

Semantic capability set 只应包含当前 declared task / future theory 真正相关的 distinctions。

对一个 task，“field product-branch reflection”可能完全无关，不应阻止 numeric refinement。

对另一个 task，它可能是核心 requirement。

这样可以避免把 semantic preorder 变成对 representation 一切数学性质的不可操作 total comparison。

## 10. Precision joins 与 world design

Semantic requirement profile 可以看成一个 demand vector：

- 必须保留的 state distinctions；
- 必须 descend 的 operations；
- 必须有效的 witness / reflection laws；
- 必须提供的 coefficient / depth resources。

多个 tasks 合并时取 requirements 的 join。若没有现有 representation 能实现这个 join，正确的 world-design 动作就是增加缺失 state / witness channel，或改变 representation type。

所以“precision increase”可以是一种结构性 state-space refinement，而不是单纯增大 denominator / modulus / cutoff。

## 11. Prior-art boundary

Partition refinement、congruence-preserving operations、product preorders 与 quotient-ring properties 都是标准既有数学。Enterprise Math 在这里的价值是 task-relative semantic ordering，以及跨 state/coefficient precision 的 nonrealizable-join boundary。