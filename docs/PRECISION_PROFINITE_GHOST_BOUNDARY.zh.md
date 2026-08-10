# Profinite Ghost Boundary：Completion 不等于 Exact Descent

状态：`RESEARCH BRIDGE / NONCANONICAL`

当前 local-global 路线必须明确保留一条负边界：**任意精细的有限 precision 可以收敛到一个真实的 profinite state，却不一定收敛到一个 exact integer state。**

前面的 affine lattice 正面 theorem 之所以没有发生这个失败，是因为它拥有额外结构：整数 lattice image 在 profinite topology 中是 closed。

## 1. 必须分开的两个问题

给定一个 exact integer world 及其所有 finite modular quotients，要区分：

1. **completion question** —— 所有有限 modular worlds 的 inverse limit 中，是否存在一个 compatible state？
2. **descent question** —— 这个 inverse-limit state 是否来自原始 integer world 中的一个真正 state？

对整数：

`Z_hat ~= product_p Z_p`。

自然嵌入

`Z -> Z_hat`

是 injective，但不是 surjective。

因此，finite-precision coherence 可以产生 completion 中完全合法的 point，而它并不是 ordinary integer。

## 2. Sharp polynomial witness

考虑

`F(x)=(x^2-13)(x^2-17)(x^2-221)`。

它没有任何整数根，因为 `13,17,221` 都不是整数平方数。

但是 F 对每一个正整数 modulus 都有根。

### Prime powers

对每个 prime p，都能选出一个在 `Z_p` 中有根的 factor：

- p=2：`17==1 mod8`，所以17是2-adic square；
- p=13：17在 mod13 下有 simple root `2`，可用 Hensel 提升；
- p=17：13在 mod17 下有 simple root `8`，同样可提升；
- 其他奇素数 p：如果13或17有一个是 quadratic residue，就选它；如果两者都是 nonresidue，那么221的 Legendre symbol 是两者乘积，等于 `+1`，所以221是 residue。

因此对每个 p，都存在

`x_p in Z_p`

使

`F(x_p)=0`。

### Profinite state

取

`x_hat=(x_p)_p in product_p Z_p ~= Z_hat`。

这是真正的 profinite solution：

`F(x_hat)=0 in Z_hat`。

但它不来自任何 `x in Z`，因为 F 没有整数零点。

因此：

`profinite solution exists`

并不能推出

`integer solution exists`。

## 3. 每个有限 modulus 仍然都会看到一个合法 state

对任意有限 modulus

`M=product_p p^(e_p)`，

把所选 p-adic roots 分别降到 `p^(e_p)`，再用 CRT 合并，就得到一个 residue `x_M` 满足

`F(x_M)==0 mod M`。

所以不仅任意一个 finite modular experiment 无法排除这个 ghost；即使拥有所有 compatible finite experiments 的 inverse system，只要没有额外 descent theorem，也不能把 profinite ghost 自动认定为 exact realizable state。

## 4. 为什么 affine linear theorem 不会失败

对

`A:Z^n -> Z^m`，

exact reachability of b 是 lattice image

`L=im_Z(A)`

的 membership。

恒等式

`L = intersection_M (L + M Z^m)`

恰好说明 L 在 profinite topology 中是 closed。

所以

`A x == b mod every M`

会强制

`b in L`，

进而确实存在一个 integer solution。

因此，local-global 成功并不是因为“把所有 finite precision 都测试了一遍”就自动成立，而是因为：

`all finite precisions + profinite closedness of the declared solution relation`。

## 5. Foundation routing rule

面对一个新的 world law 或 state predicate，不能自动假设：

`compatible at every finite precision -> exact realizable`。

要做出这一步 inference，必须额外拥有 route-specific theorem，例如：

- profinite closedness / subgroup separability；
- 针对该 equation class 有效的 local-global / Hasse-type principle；
- 独立 finite height / compactness bound，迫使 completion point descent；
- 其他 project-native structure，能够证明 completion points 就是 exact states。

没有这些 theorem，inverse-limit state 只能被解释为属于 **precision completion**，不能自动放进 exact world。

## 6. Bounded world 又是另一种情况

如果 admissible integer state family 已被独立 bounded，那么它就是有限集。此时足够精细的 modular reduction 可以在这个有限集上变成 injective，于是任何 exact predicate 原则上都能由某个足够大的 finite quotient 恢复。

所以 ghost boundary 讨论的是无界 exact descent；它并不是说 finite precision 永远无法在有限 bounded world 上成为 exact。

## 7. Prior-art boundary

Quadratic residues、Hensel lifting、CRT、profinite completion 与 intersective polynomials 都是标准既有数学。这里使用的显式 polynomial witness 只作为压力测试，不主张其本身的新颖性。

Enterprise Math 在这里得到的架构结论是：

> **precision completion 与 exact-world realization 是两个独立层级；local-global descent 是额外 theorem，不是 precision refinement 本身自动带来的结果。**