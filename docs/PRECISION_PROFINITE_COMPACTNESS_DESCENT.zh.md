# All-Moduli Compactness 与 Exact Descent

状态：`RESEARCH BRIDGE / NONCANONICAL`

Profinite ghost boundary 还能进一步压缩量词结构。对于一个固定的有限整数 polynomial equation system，**每一个有限 modulus 都局部可解，本身就已经保证存在一个 compatible profinite solution**。真正剩下的 failure 完全集中在 profinite completion 到 exact integer world 的 descent。

## 1. 固定 polynomial system

设

`P_1(x_1,...,x_n)=0`, ..., `P_r(x_1,...,x_n)=0`

是有限个整数系数 polynomial equations。

对每个正 modulus M，定义 clopen cylinder

`C_M={x_hat in Z_hat^n : P_j(x_hat)==0 mod M for every j}`。

等价地，`C_M` 就是 mod-M solution set 在 `Z_hat^n` 中的完整 inverse image。

## 2. 有限交由 lcm 精确控制

对正整数 M,N：

`C_M intersect C_N = C_lcm(M,N)`。

更一般地，对任意有限 family：

`intersection_i C_(M_i) = C_lcm(M_i)`。

原因是：一个整数 / profinite integer 同时在每个 `M_i` 下为0，当且仅当它在它们的 lcm 下为0。

因此，如果 equation system 对**每一个**正整数 modulus 都有 solution，那么任意有限组 cylinders `C_M` 的交都非空。

## 3. Compactness 自动产生一个 compatible profinite state

`Z_hat^n` 是 compact。所有 `C_M` 都是非空 clopen，并具有 finite-intersection property，因此

`intersection_(M>=1) C_M != empty`。

而

`intersection_M C_M`

恰好就是 completed equations 在 `Z_hat^n` 中的 solution set。

所以：

`for every M, there exists a solution mod M`

当且仅当

`there exists one profinite solution x_hat`。

反向当然成立：把一个 profinite solution 降到任意 M 即可。

因此，对一个固定有限 polynomial system，一旦所有 moduli 都局部可解，“这些局部 witnesses 是否兼容”就不再是额外 obstruction；compactness 自动提供兼容的 inverse-limit state。

## 4. 真正的 gap 在 profinite-to-integer descent

精确逻辑链应写成：

`all finite moduli locally solvable`

`<=>`

`profinite completion has a solution`

`=>?`

`integer world has a solution`。

只有第二个 implication 可能失败。

Intersective polynomial

`(x^2-13)(x^2-17)(x^2-221)`

正好给出 strict failure：每个 modulus 都可解，所以一定存在 profinite solution；但没有任何 integer root。

## 5. Linear affine systems 的第二个 implication 成立

对

`A x=b`，

profinite solvability 会推出每个 M 下 modular solvability。integer affine local-global theorem 再推出 exact integer solvability。

所以 affine lattice equations 中整条链都变成 equivalence：

`all moduli solvable`

`<=> profinite solution`

`<=> integer solution`。

额外的第二个 equality，正是 route-specific profinite exactness / descent theorem。

## 6. Quantifier discipline

这能区分三个不能混写的 statement。

### 每个 modulus 各自有 witness

`for every M, there exists some x_M mod M`。

这些 witness 表面上可能完全无关，但对一个固定 polynomial system，它们已经足以推出 compatible inverse-limit state。

### 存在一个 profinite state

`there exists x_hat satisfying every finite precision simultaneously`。

由 compactness，它与上一条等价。

### 存在一个 exact integer state

`there exists x in Z^n satisfying the exact law`。

这更强，必须依赖 descent。

因此对固定有限 polynomial equation systems，项目真正的 semantic boundary 应放在**completion 与 exact realization 之间**，而不是放在“分别选择 finite witnesses”与 completion 之间。

## 7. Compactness step 什么时候不能直接套用

这里使用的是一个固定有限 equation system，并且每个 mod-M semantics 都是同一 law 的 reduction。以下情况不能自动套用：

- declared law 自己随 precision 变化；
- 不同 modulus 使用了不同 observation / action semantics，而不是同一 predicate 的 reduction；
- intermediate DOMAIN/RELATION legality 在不同 precision 下被删除或改变；
- state spaces 没有形成 compatible inverse system。

这些情形中，连第一个箭头本身都需要另一个 compatibility theorem。

## 8. Precision 解释

对同一个固定有限整数 polynomial law 的稳定 modular reductions：

> **只要每个 finite precision world 都局部非空，全部 finite precisions 已经保证存在一个 coherent completion-world state。**

它们真正无法自动保证的，是这个 completion state 是否属于 exact integer world。

Compactness、inverse limits 与 polynomial congruences 都是标准既有数学。Enterprise Math 在这里的价值是量词 routing，以及把 descent boundary 的位置精确放对。