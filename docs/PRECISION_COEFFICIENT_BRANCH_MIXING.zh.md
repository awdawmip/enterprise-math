# Coefficient Collapse 可以混合 Relation Branches

状态：`RESEARCH BRIDGE / NONCANONICAL`

Nonlinear profinite ghost 还有第二种解释，而且可以直接接到 A4 witness identity：一个在 exact world 中用乘法编码的有限 disjunction，在 coefficient collapse 后可能不再是 faithful 的 labelled-branch representation。

## 1. Exact integer branch semantics

在整数中：

`F(x)=(x^2-13)(x^2-17)(x^2-221)`。

因为 Z 是 integral domain，

`F(x)=0`

当且仅当至少有一个 labelled branch exact 成立：

`x^2=13`，或者 `x^2=17`，或者 `x^2=221`。

所以在 exact coefficient world 中，product-zero 确实是这个有限 branch relation 的 faithful encoding。

## 2. Composite modular precision 改变 coefficient logic

当 n 为 composite 时，`Z/nZ` 有 zero divisors。product-zero 不再推出某个 factor 自己为0。

Sharp reference：

`n=15`, `x=1`。

三个 factors 是

`-12`, `-16`, `-220`。

mod3 时第一个 factor 为0；

mod5 时第三个 factor 为0。

所以整个 product 在 mod15 下为0，但三个 factor 没有任何一个在 mod15 下为0。

因此 mod15 看到一个 unlabelled product-solution，但它没有任何 global mod15 branch label。

finite quotient 已经把不同 prime-component witnesses 混成了一个 state。

## 3. Prime field 只能修复单个 modulus 内部的 defect

当 p 为 prime 时，`Z/pZ` 是 field，所以 product-zero mod p 仍然保证至少一个 labelled factor 在 mod p 下为0。

因此只使用 prime moduli，可以避免**单个 coefficient ring 内部**的 zero-divisor branch mixing。

但它并不能解决 global witness identity 问题。

## 4. Branch label 仍可在不同 primes 之间切换

Ghost construction 在每个 p-adic component 上独立选择一个 square factor。

例如：

- p=13 时选择 branch `x^2=17`；
- p=17 时选择 branch `x^2=13`；
- 其他 primes 根据 quadratic character，可能选择13、17或221。

每个 prime field 内都有合法 local branch，但 label 不需要在不同 primes 之间保持一致。

所以 profinite tuple 可以满足 unlabelled product equation，同时不存在任何一个 labelled branch 在全局成立。

## 5. 没有任何 branch 能通过全部 finite precisions

每个 exact label 都有一个有限 blocker：

- `x^2=13` 在 mod5 无根；
- `x^2=17` 在 mod3 无根；
- `x^2=221` 在 mod3 无根。

因此，没有任何单一 labelled branch 能在每个 modulus 下局部可解。

但是 unlabelled union / product 却对每个 modulus 都可解。

所以，在做 precision inverse limit **之前**擦掉 branch identity，会改变 existence answer。

## 6. 代数来源：completion 引入 zero divisors / idempotent selectors

Profinite completion 分解为

`Z_hat ~= product_p Z_p`。

domains 的 direct product 不再是 domain。它含有大量非平凡 idempotents 与 zero divisors，可以选择不同 prime components。

因此

`f_1(x_hat)...f_k(x_hat)=0`

可以在每个 prime component 上由不同 factor 分别为0来实现，即使没有任何一个 `f_i(x_hat)` 在 global profinite ring 中为0。

completion 自身提供了一套隐藏的 branch-selector algebra。

这就是 ghost 背后的 coefficient-level mechanism。

## 7. A4/P023 interpretation

这与之前 support compiler 的负边界高度平行：

- A4 raw relation 保留 branch / witness identity；
- support projection 可能只保留 possible outcomes 的集合；
- coefficient product-zero 可能只保留“局部上某个 factor 为0”的 unlabelled statement。

如果未来 semantics 会重新读取 branch label，那么这两类 projection 都太粗。

区别只在于：这里的 witness erasure 发生在 arithmetic precision components 之间，而不是 time path 上。

因此可以进一步区分：

`state precision`

vs

`coefficient precision`

vs

`witness / branch-label precision`。

一个 quotient 即使对 raw numeric output 是 exact 的，也可能对依赖 coefficient ring 是 integral domain 的 logical interpretation 不安全。

## 8. Semantic-safe quotient rule

如果 exact world law 依赖如下 implication：

`f g=0 -> f=0 or g=0`，

那么这个 implication 本身就是 world semantics 的一部分，而不只是 algebraic notation。

Coefficient quotient 只有在保留所需 no-zero-divisor / branch-label property 时才安全；或者必须把 branch label 作为额外 state / witness data 单独保留。

仅仅把 polynomial syntax 做 modular reduction 并不够。

这和 safe-operation descent 是同一种 routing：必须检查 operation / logical law 本身是否真的能穿过当前 precision collapse。

## 9. Prime powers 仍然需要警惕

即使只沿一个 prime，`Z/p^e Z` 在 `e>1` 时也有 zero divisors。

因此，限制在单一 p-adic direction 并不会自动保存 integral-domain branch semantics。

Prime modulus 是 field；prime-power modulus 提供更多 p-adic numeric precision，但同时允许 zero-divisor products。

所以“更高 p-adic numeric precision”与“multiplicative branch logic 更 faithful”是两个不同坐标。

## 10. Prior-art boundary

Integral domains、zero divisors、CRT、profinite idempotents 与 factorized polynomial equations 都是标准既有数学。Enterprise Math 在这里得到的 precision-routing 结论是：

> **coefficient collapse 可以擦除或混合 witness identity；algebraic syntax 即使穿过 quotient，exact logical branch semantics 也未必能一起穿过去。**