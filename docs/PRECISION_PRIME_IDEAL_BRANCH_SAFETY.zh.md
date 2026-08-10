# Branch-Safe Coefficient Quotient 的 Prime-Ideal Criterion

状态：`RESEARCH BRIDGE / NONCANONICAL`

Coefficient branch-mixing 的例子可以进一步压成一个精确的 generic criterion。

## 1. Product-zero branch semantics

设 exact coefficient ring R 是 integral domain，并且某条 world law 用

`f g=0`

编码逻辑含义

`f=0 OR g=0`。

现在把 coefficient collapse 到 quotient：

`R -> R/I`。

若要求这个 product-zero branch implication 对**所有 coefficient values**在 quotient 中仍成立，就必须有

`ab in I -> a in I or b in I`

对全部 `a,b in R` 成立。

而这正是 I 为 prime ideal 的定义。

所以：

`product-zero branch semantics descends through R/I`

当且仅当

`I is prime`

当且仅当

`R/I is an integral domain`。

## 2. Integer modular specialization

对 R=Z 与非平凡 finite quotient

`Z -> Z/MZ`，

ideal `M Z` 为 prime，当且仅当 M 是素数。

所以 generic product/disjunction semantics 在局部 coefficient world 中 branch-safe，当且仅当 modulus 是 prime。

- mod p：product-zero branch logic 安全；
- mod `p^e`, `e>1`：generic 不安全；
- 含多个 prime factors 的 composite M：同样 generic 不安全。

Exact world 对应 `I=(0)`，它也是 prime，因为 Z 是 domain；mod1 的 zero ring 只是 trivial collapse boundary，不作为 faithful logical world。

## 3. Numeric precision 更高，不代表 logical precision 更高

沿同一个 p-adic numeric chain：

`mod p -> mod p^2 -> mod p^3 -> ...`

state / residue information 会按 divisibility 越来越细。

但是只有第一层非平凡 quotient mod p 是 field。所有更深的 `Z/p^e Z` 都有 zero divisors。

因此同一个 precision vector 的不同坐标可以反向变化：

- **numeric p-adic precision** 上升；
- **generic product-branch faithfulness** 在 `e>1` 后从 true 变成 false。

这直接证明：单一 scalar “precision level” 无法概括 quotient 的全部 semantic capability。

## 4. Local branch safety 仍不等于 global branch coherence

Prime modulus 可以消除单个 local field 内部的 zero-divisor branch mixing，但不同 p 上选中的 branch 仍然可能不同。

所以还要分两层：

1. **local algebraic safety** —— coefficient quotient kernel 为 prime，因此每个 local product-zero state 至少有一个 local branch label；
2. **cross-precision witness coherence** —— 不同 precision components 上的 branch labels 是否能 descent 成一个共同 exact/global witness。

Profinite ghost 在每个 prime 上通过第一条，却在第二条失败。

所以 prime-ideal safety 是 faithful local disjunction semantics 的 exact criterion，但不是 global exact witness descent 的充分条件。

## 5. Restricted factor family 可能比 generic quotient 更安全

如果实际 world law 只允许一个受限的 factor-value subset，某个有 zero divisors 的 quotient 仍可能在这部分 reachable image 上偶然安全。

Prime-ideal criterion 是**uniform all-values theorem**。

因此 project routing 还应区分：

- quotient 自身的 generic coefficient-law safety；
- 对当前 route 实际可达 factor-value subset 的 task-relative safety。

这与 generic safe-operation algebra 和更小的 task-relative safe operation family 之间的区分是同一种结构。

## 6. Prior-art boundary

Prime ideals、integral domains、quotient rings 与 zero divisors 都是标准既有代数。Enterprise Math 在这里得到的 precision 解释是：

> **coefficient collapse 可以保留 polynomial syntax，却破坏该 syntax 在 exact world 中承载的 logical branch law；uniform branch-safe descent 的充要条件正是 prime-ideal condition。**