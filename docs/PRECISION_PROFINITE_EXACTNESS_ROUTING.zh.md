# Profinite Exactness 作为 Descent Guard

状态：`FOUNDATION-FACING RESEARCH BRIDGE / NONCANONICAL`

Profinite local-global architecture 需要明确加入一条防止过度推广的 guard。对 subgroup membership，modular refinement 确实就是同一个 exact subgroup 的 congruence thickenings，closedness 控制其极限；但对一般 world law，先 completion 再求解可能制造出并非 exact solutions completion 的新 solution。

这不是第六种 failure location，而是一个**routing condition：finite-precision completion 是否允许 descent 回 exact world。**

## 1. 必须区分两个操作

对整数 law `P(x)=0`，定义

`S_Z={x in Z^n:P(x)=0}`。

在 profinite world 中有两种 construction。

### 先求解，再 completion

取

`closure(S_Z) subseteq Z_hat^n`。

这些 point 是 exact-world solutions 的极限。

### 先 completion，再求解

先把 law 延拓到 `Z_hat^n`，再定义

`S_hat={x_hat in Z_hat^n:P(x_hat)=0}`。

这些 point 是 completed world law 自己允许的 solutions。

对 continuous integer laws，有自然 inclusion

`closure(S_Z) subseteq S_hat`，

但 equality 是额外 theorem，不是定义自动给出的。

## 2. Profinite exactness / descent property

真正的正面条件是

`closure(S_Z)=S_hat`。

把它称为当前 declared problem 的 **profinite exactness**。

一旦成立，completion 不会额外制造 ghost solution component。特别地，若 `S_Z` 为空，`S_hat` 也必须为空。

若不成立，则所有 finite precision layers 即使彼此完全 compatible，对应的 inverse-limit state 也可能只存在于 completion 中，而不属于 exact integer world。

## 3. Linear affine equations 满足这条 guard

对

`A x=b`，

integer solvability 就是 lattice IMAGE membership。affine local-global theorem 给出：

- 若没有 integer solution，则一定存在某个有限 modulus 已经无解；
- 若有一个 integer solution，exact solution set 是 integer kernel 的 affine coset，而它的 closure 就是相应 profinite affine-kernel coset。

因此

`closure({integer solutions})={profinite solutions}`。

所以 linear IMAGE/FIBER 路线中的 positive local-global results 可以安全 descent。

## 4. Nonlinear ghost 违反这条 guard

对

`F(x)=(x^2-13)(x^2-17)(x^2-221)`，

没有 integer root，所以

`S_Z=empty`，

并且

`closure(S_Z)=empty`。

但每个 prime 上都存在 compatible p-adic root，因此

`S_hat!=empty`。

于是

`closure(S_Z) proper_subset S_hat`。

这说明为什么“exact set closed”并不足够：这里 exact zero set 是 empty，因此当然 closed。真正失败的是 completed solution functor 比 exact solutions 的 completion 更大。

## 5. 如何正确理解 closed/open architecture

closed/open 结果对它们真正证明的对象仍然完全正确。

### Subgroup / lattice IMAGE membership

local modular sets 就是实际的 thickening：

`H + M Z^n`。

于是 H 的 closedness 精确表示：对所有 finite thickenings 取交可以恢复 H。

### General equation classes

local solution sets 未必是某一个 exact solution set 的 thickenings。新的 quotient solutions 可以在不同 prime 上分别出现，最终拼成一个 profinite ghost。

因此，不能用泛化口号

“exact solution set closed”

去替代 route-specific local-global / descent theorem。

## 6. Exact descent 前的 routing checklist

当某条路线试图从任意精细的 finite precision 推出 exact existence / identity 时，按顺序检查：

1. **Exact object：** `S_Z` 是什么？
2. **Completed object：** 什么 finite-quotient / inverse-limit semantics 定义了 `S_hat`？
3. **Natural map：** `closure(S_Z) -> S_hat` 是否已知 surjective？
4. **Descent theorem：** 什么结构证明 equality？
5. **Ghost boundary：** 若 equality 未证明，哪些 completion-only states 仍然 admissible？

可能的正面机制包括：

- subgroup/lattice structure 与 separability；
- 针对当前 equation class 的有效 local-global principle；
- route-specific Hasse/descent theorem；
- 独立 finite state/height bound，把 admissible world 直接限制成有限集合。

## 7. Bounded world 不需要全局 profinite exactness

如果 admissible exact state family 已经独立有限，则足够精细的 modular reduction 可以在该有限集合上 injective。此时即使 unbounded equation class 存在 profinite ghosts，也仍然可以从一个 finite quotient 做 exact decision。

这是另一种机制：

`finite admissible world -> finite injective precision`，

而不是

`unbounded equation class -> profinite exactness`。

## 8. Precision 解释

所以当前 hierarchy 应被读取为：

`finite quotients`

`-> inverse-limit / completion semantics`

`-> [descent guard]`

`-> exact-world realization`。

第一步可以存在，而第二步不一定成立。

因此最强的安全表述是：

> **任意精细的 finite precision 只有在当前 route 证明 completed law 的 solutions 能从 exact states descent 时，才可以被解释为已经确定 exact world。**

Profinite completion、p-adic solutions、local-global principles 与 descent failure 都是标准既有数学。Enterprise Math 在这里的价值是 routing distinction，以及显式阻止一个错误的 generic inference。