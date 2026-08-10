# Profinite Exactness：Completion 与 Solving 何时交换

状态：`RESEARCH BRIDGE / NONCANONICAL`

用 topology 解释 local-global precision 时，需要做一个细致修正：**exact integer solution set 本身 closed，并不足以推出 local-global descent。**

真正需要比较的是两个操作是否交换：

1. 先在 exact integer world 中求解 world law，再对 solution set 做 completion；
2. 先把 world law 延拓到 profinite completion，再在 completion 中求解。

这两个结果可以不同。

## 1. 两种 solution construction

对整数 law / predicate `P(x)=0`，记

`S_Z={x in Z^n : P(x)=0}`

为 exact integer solutions。

它在 profinite completion 中的闭包是

`closure(S_Z) in Z_hat^n`。

另一方面，把同一个整数公式按系数连续延拓到 profinite completion，再定义

`S_hat={x_hat in Z_hat^n : P(x_hat)=0}`。

对 polynomial / continuous integer laws，总有

`closure(S_Z) subseteq S_hat`，

因为 exact solution 在 completion 后仍然是 solution。

真正关键的是这个 inclusion 是否为 equality。

## 2. Profinite exactness

如果对当前 declared equation class / problem 有

`closure(S_Z)=S_hat`，

就称其在该问题上具有 **profinite exactness**。

这意味着：每一个 compatible inverse-limit solution 都来自 exact integer solutions 的 completion；completion 没有额外制造一个只存在于 finite-precision worlds 中的新 solution component。

对于只问“是否存在”的问题，如果 `S_Z` 为空，那么 profinite exactness 会强制 `S_hat` 也为空。

这才是从完整 finite-precision coherence 推出 exact realizability 所需的 descent property。

## 3. Affine integer equations 具有 profinite exactness

对

`A x=b`，

若存在 integer solution，exact solution set 是 `ker_Z(A)` 的 affine coset。它在 completion 中的 closure 就是对应的 profinite-kernel affine coset。

若不存在 integer solution，affine IMAGE local-global theorem 会给出某个有限 modulus，使 modular solvability 已经失败，因此也不存在 profinite solution。

所以

`closure({x in Z^n:A x=b})`

`= {x_hat in Z_hat^n:A x_hat=b}`。

这比“exact solution set 是 closed”更强，也更精确。

## 4. Intersective polynomial 不具有 profinite exactness

对

`F(x)=(x^2-13)(x^2-17)(x^2-221)`，

`S_Z=empty`。

因此

`closure(S_Z)=empty`。

但逐 prime 选择 p-adic roots 可以构造

`S_hat != empty`。

所以

`closure(S_Z) proper_subset S_hat`。

profinite completion 中确实存在 completed equation 的 solution，但它不从任何 exact integer solution descent。

这就是 **profinite ghost state** 的精确代数含义。

## 5. 为什么 modular satisfiability 不总是 exact set 的 neighborhood thickening

对 linear target membership，modular solvability 恰好是

`b in im_Z(A)+M Z^m`，

也就是同一个 exact lattice image 的 congruence thickening。对所有 M 取交，能够恢复 closed lattice。

但对 nonlinear polynomial：

`{x mod M : F(x)==0 mod M}`

并不一定是 exact integer zero set 的 reduction 或 neighborhood thickening。新的 finite-quotient roots 可以在不同 prime 上独立出现，并最终拼成一个没有 exact integer ancestor 的 profinite solution component。

因此在一般情形下，下面这个口号是错误的：

`exact set is closed -> local-global descent`。

真正需要的是更强的 compatibility：

`local/profinite solution functor = completion of exact solutions`，

或者其他能推出同样 descent 结论的 theorem。

## 6. Foundation routing rule

当某条路线试图从任意精细的 finite precision 推出 exact existence 时，应按以下顺序问：

1. exact-state solution object `S_Z` 是什么？
2. finite quotients 诱导出的 completed/local solution object `S_hat` 是什么？
3. 自然 inclusion

   `closure(S_Z) -> S_hat`

   在当前 equation class 中是否为 equality？
4. 如果不是，什么额外 axiom、bound 或 world law 能排除 ghost components？

Linear lattice IMAGE 的答案是肯定的；一般 nonlinear Diophantine predicates 则不是。

## 7. Bounded admissible world

独立 finite state bound 可以因为另一种原因恢复 descent。admissible exact state set 此时是有限的，因此足够精细的 modular reduction 可以在该集合上 injective。

这是一条 bounded-world certificate，不代表原本的 unbounded equation class 本身具有 profinite exactness。

## 8. Prior-art boundary

Profinite completion、p-adic solution sets、integral points、local-global principles 以及 descent failure 都是标准既有数学。Enterprise Math 在这里得到的是 precision-routing 区分：

> **exact solutions 的 completion 与 completed world law 的 solutions 是两个不同 construction；要从 finite precision exact descent，必须证明二者相同，而不只是证明 exact set closed。**