# Witness-Semantic Descent Across Precision

状态：`FOUNDATION-FACING RESEARCH BRIDGE / NONCANONICAL`

本文不增加第六种 failure location，而是细化：当 exact world law 携带 witness、branch label、provenance class 或其他隐藏 existential certificate 时，应如何解释 RELATION、DOMAIN 与 precision-completion 的输出。

核心规则是：

> **从 finite-precision existence descent 到 exact world 之前，应先 descent witness semantics，再在固定 witness 内 descent state。**

## 1. Numeric existence 与 witnessed existence 是不同 observation

设 exact world law 有 labelled branches：

`P(x) = OR_(lambda in Lambda) P_lambda(x)`。

unlabelled statement

`P(x) is possible`

弱于

`存在一个特定 lambda 使 P_lambda(x) 成立`。

一个 quotient 可能保留前者，却擦除、混合或改变后者。

当前研究里已经出现多种机制：

- A4 support 忘掉 branch / path identity；
- 带 zero divisors 的 coefficient quotient 可以混合 factors；
- 不同 prime components 可以选择不同 branch labels；
- infinite witness alphabet 可以随着 precision 增长让 label 不断逃向更大值。

因此 witness identity 不会自动跟随 numeric precision 一起保留。

## 2. Local branch reflection 是 semantic quotient condition

在 precision M 下定义

`S_M={lambda : branch lambda 在 M 下 locally realizable}`。

若 unlabelled quotient law 的 local solvability 能推出

`S_M!=empty`，

就称它 branch-reflecting。

这是 quotient 的 semantic property，不只是公式做了 syntactic reduction。

对 domain 中用乘法编码的 disjunction，generic product-zero branch reflection 穿过 quotient `R/I` 的充要条件是 I 为 prime。对整数来说，prime modulus 在 generic product/disjunction 逻辑上 local-safe，而 composite 与非平凡 prime-power quotient generic 不安全。

mod15 ghost 是 sharp failure：product equation 有 solution，但三个 labelled factors 全部没有 mod15 solution。

## 3. Local safety 不等于 cross-precision coherence

即使每一个单独 precision 都有合法 local label，不同 precision components 仍可能选择不同 labels。

要从 witness supports 得到一个 global label，precision system 必须支持**joint refinement**。对 modular precision，就是有限组 observations 能被放到一个共同 multiple / lcm precision 上比较；更抽象地，declared precision family 必须 finitely directed。

全部正整数 moduli 和一条 `R^e` ladder 都是 directed。

“所有 prime moduli 各测一次”并不 lcm-directed。于是 prime-local safety 本身不能推出一个 cross-prime witness label。

## 4. Witness compactness 是独立资源

设 W 为 witness space，`S_M subseteq W` 是 precision M 下的 admissible witness support。

若：

- W compact；
- 每个 `S_M` nonempty 且 closed；
- precision finitely directed；
- supports 随 refinement 缩小；

那么这些 supports 具有 finite-intersection property，从而

`intersection_M S_M != empty`。

于是有一个 witness 在所有 precision 下都存活。

finite witness alphabet 是最简单特例。

Infinite discrete witness alphabet 则不一定。取 branches

`P_k: 0=k`, `k=1,2,...`。

其 local support 是

`S_M={k:M divides k}`。

每个 precision 都有 witnesses，supports 也正确缩小，但总交为空。witness 不断逃向 infinity，因为 witness space 不 compact。

## 5. 固定 witness 内的 state descent 是第二道 guard

一个 coherent witness label 能在所有 precision 下存活，仍然不保证存在 exact state。

固定 `lambda_*` 后，它自己的 local state family 还必须通过 profinite exactness / descent guard：

`closure(exact states satisfying lambda_*)`

`= completed states satisfying lambda_*`。

Affine integer branches 通过 lattice local-global theorem 满足它。

一般 nonlinear Diophantine branch 则不一定。

所以 witness coherence 与 state realization 是两道独立 descent stages。

## 6. Two-stage routing

从 finite-precision existence 到 exact witnessed existence 的安全路线是：

### Stage A — semantic witness descent

检查：

1. local branch reflection；
2. directed joint precision；
3. compact / finite witness space，或其他 witness-coherence theorem。

输出：

`一个固定 witness 在所有 precision 下存活`。

### Stage B — state descent under that witness

检查：

1. 固定 witness 下 compatible local states；
2. 该 branch law 的 profinite exactness 或其他 exact descent theorem。

输出：

`一个携带该 witness 的 exact state`。

两道 stage 互不替代。

## 7. 为什么这不是第六个 failure layer

现有五层 architecture 保持不变。

- RELATION 标记 multivalued successor / witness structure；
- DOMAIN 标记 legality / definedness；
- coefficient precision 影响某个 algebraic encoding 是否仍 faithful 表示 RELATION；
- profinite exactness 控制 completion 到 exact state 的 descent。

Witness descent 是穿过这些 layers 的**routing discipline**，不是新的 ontological category。

## 8. Quotient law 必须保 semantics，不只保 syntax

Coefficient quotient 可能完整保留 written polynomial expression，却让 exact world 用来解释该表达式的 implication 失效。

例如：

`fg=0 -> f=0 or g=0`

在 domain 中成立，在有 zero divisors 的 quotient 中可能失败。

所以 world law 的 semantic contract 包括解释 syntax 时用到的 algebraic properties。

安全 quotient 必须至少做到以下之一：

- generic 地保留所需 logical implication；
- 在当前 route 实际 reachable subset 上证明它；
- 或者直接保留 witness label，不再试图从 collapsed coefficients 重构。

## 9. Precision axes 不一定全局单调

Numeric precision 更高，并不保证 logical witness precision 更高。

沿 `mod p -> mod p^2`，p-adic numeric information 增加，但 coefficient ring 从 field 变成带 zero divisors 的 ring。generic product-branch faithfulness 反而下降。

这直接说明 precision 应表示为 structured capability profile，而不是单一 scalar “resolution level”。

## 10. Foundation routing checklist

在声称

`finite-precision existence -> exact witnessed existence`

之前，应依次问：

1. exact law 需要什么 witness / branch object？
2. 每个 quotient 是否 local 地反映该 witness semantics？
3. declared precisions 是否足够 directed，可以比较不同 local witness choices？
4. witness space 是否 finite / compact，或有其他 coherence control？
5. witness 固定后，其 state law 是否满足 exact descent？

只有所有必要 guards 成立，才应该把 completion-world existence 解释为 exact witnessed state。

Prime ideals、compactness、directed inverse systems 与 profinite descent 都是标准既有数学。Enterprise Math 在这里的价值是 semantic routing：**先 descent witness，再 descent state。**