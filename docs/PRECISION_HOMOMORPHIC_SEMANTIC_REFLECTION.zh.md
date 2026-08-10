# Homomorphic Syntax Preservation 不等于 Semantic Reflection

状态：`RESEARCH BRIDGE / NONCANONICAL`

Coefficient collapse 通过 quotient homomorphism 时具有天然方向性：algebraic terms 会与 quotient evaluation 自动交换，因此 exact equations 会自动向前 descend；但 quotient 不会自动把 exact truth、witness uniqueness、branch identity 或其他 logical properties 反射回 source world。

## 1. Polynomial syntax 自动 descend

设

`phi:R -> S`

为 ring homomorphism。对任意 polynomial term t 与 tuple x：

`phi(t_R(x)) = t_S(phi(x))`。

所以 quotient coefficients / states 会精确保留 polynomial evaluation。

对 `R=Z`, `S=Z/MZ`，任意 exact equation

`t(x)=0 over Z`

都会推出

`t(x)==0 mod M`。

这种 forward soundness 不需要额外 theorem，只需要 homomorphism 本身。

## 2. Quotient truth 表示 kernel membership，不是 exact truth

在 `R/I` 中，

`t(x)=0`

在 source ring 中只意味着

`t(x) in I`。

因此 quotient truth 是 exact zero 的一个 **I-thickening**。

对任意 finite integer modulus M，甚至 identity equation 都立即给出 reflection failure：

`x=M` 在 Z 中非零，但在 mod M 下为0。

所以任何固定 finite quotient 都不可能在所有无界 integers 上 reflection exact zero。

## 3. 独立 bound 可以恢复 reflection

若另有独立信息保证 source value z 满足

`|z|<=B`，

那么任何

`M>B`

都满足

`z==0 mod M iff z=0`。

这就是 local-global 路线中 bounded-world principle 的最小形式：

`forward quotient soundness + independent height bound -> exact reflection on the admissible set`。

这里的 bound 来自 world structure，不是 quotient 自己产生的。

## 4. Equational syntax 与 logical interpretation 是不同层

Quotient 可以保留 written polynomial term，却破坏 exact world 用来解释该 term 的 logical implication。

例如在 integral domain 中：

`ab=0 -> a=0 OR b=0`。

product term 与 equality-to-zero 在所有 quotient rings 中都能 syntactically descend，但 disjunctive branch interpretation 不一定。

对 `R/I`，这个 implication 对所有 coefficient values 成立，当且仅当 I 为 prime。

所以同一个 homomorphic quotient 可以同时：

- 对 polynomial evaluation 完全 sound；
- 对 source domain 赋予该 polynomial 的 branch logic 完全不 reflection。

## 5. Integer modular specialization

对

`Z -> Z/MZ`，

generic product/disjunction reflection 恰好只在 prime modulus 上成立。

- M prime：quotient 是 field / domain；
- M composite，包括 `p^e`, `e>1`：zero divisors 会制造 product-zero false branches；
- M=1：trivial zero-ring collapse，不作为 faithful logical world。

因此更深的 p-adic numeric precision 可以与更弱的 generic branch-law faithfulness 同时出现。

## 6. Forward preservation 与 backward reflection 必须分名

一个安全 precision architecture 至少应区分：

### Forward preservation

exact source state 若满足 law，其 collapsed image 也满足 quotient law。

Polynomial / equational syntax 在 homomorphism 下自动拥有这一性质。

### Backward reflection

collapsed state 若满足 quotient law，是否真的来自一个满足 intended exact semantics 的 source state？

这需要额外结构。

典型 reflection questions 包括：

- 从 modular zero 反推 exact zero；
- 从 modular reachability 反推 exact IMAGE reachability；
- 从 product zero 反推 branch identity；
- uniqueness / nonzeroness / cancellation；
- 从 profinite existence 反推 exact witness / state realization。

每一项都需要自己的 theorem 或 bound。

## 7. 与 local-global precision 的关系

Affine local-global theorem 是一条跨无界 quotient precision family 的 global reflection theorem：

`Ax==b mod every M`

能够 reflection

`Ax=b over Z`。

有限 family 在没有额外结构时失败；bounded target family 可以恢复 reflection。

Nonlinear profinite ghost 又说明：对一般 equation class，即使**所有** finite quotient truths 都成立，也未必能 reflection exact existence。

所以“homomorphism 保留了 formula”与“整个 inverse system 能 reflection exact semantics”是两件完全不同的事。

## 8. 与 witness descent 的关系

对 labelled relation，quotient 可能保住 unlabelled equation，却失去 witness reflection。

因此 semantics-safe strategy 应是：

1. 先找出 future language 真正依赖哪些 exact logical / witness properties；
2. 判断哪些 properties 会被 quotient 自动 forward-preserve；
3. 再单独证明哪些 reflection properties 足够重构 exact semantics。

这就是 coefficient 版的 safe-operation descent。

## 9. Precision 是 capability-relative

Raw quotient refinement 不是 semantic capability 的 total order。

从 mod p 提升到 mod `p^2` 会增加 residue information，却失去 generic product-branch reflection 所需的 field / domain property。

所以“finer coefficient precision”只有相对于 declared observation / operation / logical language 才有意义。

Structured precision profile 不应只记录能区分多少 residues，还应记录哪些 semantic laws 在 collapse 后仍有效、哪些 exact properties 仍可被 reflection。

## 10. Prior-art boundary

Ring homomorphisms、quotient ideals、polynomial term evaluation、prime ideals 与 zero divisors 都是标准既有代数。Enterprise Math 在这里得到的 routing distinction 是：

> **homomorphism 会自动 forward-preserve algebraic syntax；exact semantic reflection 则是另一条独立的 precision theorem。**