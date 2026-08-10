# Two-Stage Witness Descent Across Precision

状态：`RESEARCH BRIDGE / NONCANONICAL`

Coefficient branch mixing 与 profinite ghost 把两个不同的 descent 问题彻底分开了：

1. **一个 local / unlabelled state 是否能在不同 precision 中保持同一个 coherent witness label？**
2. **一旦固定一个 witness label，它的 compatible finite states 是否能 descent 成一个 exact state？**

这两步需要不同的 hypotheses。

## 1. Labelled branch family

设 exact world law 是 labelled branches 的并：

`P(x) = OR_(lambda in Lambda) P_lambda(x)`。

对一个 declared precision M，定义 branch-support set：

`S_M = {lambda in Lambda : branch P_lambda 在 precision M 下有 local solution}`。

若 N 比 M 更细，并且每个 N-solution 都能 reduction 成 M-solution，则

`S_N subseteq S_M`。

因此提高 precision 只能删除 witness labels，不能凭空产生一个在更粗 reduction 中本来不可能的 label。

## 2. Local branch reflection 是第一道 guard

若 unlabelled quotient law 在 precision M 下的 local solvability 能推出

`S_M != empty`，

就称它在该 precision 下 **branch-reflecting**。

最强形式是：quotient solution set 就等于 labelled branch solution sets 的 literal union。

这条 guard 可以在任何 inverse limit 之前就失败。

Ghost product polynomial 在 mod15 下有 product solution，但三个 labelled square branches 全部 mod15 无解。因此 branch reflection 已经在一个有限 joint precision 上失败。

## 3. Directed precision 是第二项结构资源

把 experiment family 按 refinement 排序，并要求它 **finitely directed**：

> 任意有限组 declared precisions，都存在另一个 declared precision 同时细化它们全部。

对普通 modular precision，这意味着 family 中包含、或 semantics 能评价一个共同 multiple / lcm refinement。

例子：

- 全部正整数 moduli：由 lcm directed；
- 一条 `R,R^2,...` ladder：取更大的 exponent 即可共同 refinement；
- “所有 prime moduli 各测一次”：**不**对 lcm directed，因为两个不同 primes 的 joint refinement 是 composite modulus，已经离开 family。

因此，prime-local branch safety 本身并不能推出 cross-prime witness coherence。

## 4. Finite witness theorem

假设：

1. Lambda 有限；
2. precision family finitely directed；
3. branch supports 随 refinement 单调缩小；
4. unlabelled law 在每个 declared joint precision 都 branch-reflecting；
5. unlabelled law 在每个 declared precision 都 locally solvable。

那么

`intersection_M S_M != empty`。

所以存在一个固定 label `lambda_*`，在每一个 precision 下都 locally solvable。

### Blocker proof

反设没有任何 label 能通过所有 precisions。对每个 lambda 选一个 blocker precision `M_lambda`，使

`lambda notin S_(M_lambda)`。

因为 Lambda 有限，而且 precision directed，可以取一个共同 refinement L，同时细化所有 `M_lambda`。

由 support monotonicity：

`S_L subseteq intersection_lambda S_(M_lambda)`，

于是所有 labels 都被排除，`S_L=empty`。

但 local solvability + branch reflection 又要求 `S_L!=empty`，矛盾。

对普通 modulus，L 就是所有 blocker moduli 的 lcm。

## 5. Ghost 在 mod15 已暴露第一道 guard 失败

三个 branches：

`x^2=13`, `x^2=17`, `x^2=221`。

可以选 blocker：

`13 -> mod5`，

`17 -> mod3`，

`221 -> mod3`。

它们的 lcm 是15。

在 mod15 下，每个 labelled branch 都被 blocker 排除，但 unlabelled product polynomial 仍有 root `x=1`。

所以 failure 并不是某种必须等到 inverse limit 才出现的神秘 incompatibility。product encoding 在有限 joint precision15 上就已经不再反映 exact branch relation。

这是一个可执行的 blocker-lcm diagnosis。

## 6. 真正的一般原则是 witness compactness

Lambda 有限是充分条件，但并不是概念上最根本的条件。

设 W 为 compact witness space，并且每个 precision 都给出

`S_M subseteq W`

这样的 nonempty closed admissible-witness set。若 precision family finitely directed，且 supports 随 refinement 缩小，那么 `S_M` 具有 finite-intersection property。Compactness 推出

`intersection_M S_M != empty`。

因此，更一般的 witness-coherence resource 是：

`compact witness space + directed precision + closed shrinking witness supports`。

有限 label alphabet 只是 discrete finite special case。

## 7. 无限 noncompact labels 可以不断逃向 infinity

取 witness labels `k=1,2,3,...`，并定义 exact branch laws：

`P_k : 0=k`。

每个 exact branch 都不可能成立。

但 modulo M，branch k 当且仅当

`M|k`

时 locally solvable。

因此

`S_M={k:M|k}`

对每个 M 都非空，并且满足 refinement monotonicity；然而

`intersection_M S_M=empty`。

任何有限 precision prefix 都有一个共同大 label——该 prefix 的 lcm；但任何固定 label 最终都会被更细 modulus 阻断。

witness 不断逃向 infinity，因为 discrete witness space N 不 compact。

所以 infinite witness alphabet 即使满足 local branch reflection 与 directed precision，也并不自动安全。

## 8. 固定 label 的 profinite descent 是另一道独立 guard

第一阶段 theorem 只得到一个 label `lambda_*`，它在每个 precision 下都 locally solvable。

这还没有产生一个 exact state 去满足 branch `P_(lambda_*)`。

要完成这一步，仍需要 route-specific descent theorem：

`branch locally solvable at every precision`

`=> branch has a profinite solution`

`=> exact branch solution`。

对于固定有限 polynomial branch，compactness 可以给出第一箭头；第二箭头就是该 branch 自身的 **profinite exactness**。

Affine integer branches 满足它；一般 nonlinear Diophantine branch 则不一定。

## 9. 完整的 two-stage witness descent theorem

所以，一个 finite labelled union 要安全 descent，至少可以采用如下两阶段 architecture：

### Stage A — witness coherence

- local branch reflection；
- finitely directed precision family；
- finite / compact witness space，且 witness supports closed、随 precision 缩小。

这一步得到一个固定 witness label，在所有 precision 下都存活。

### Stage B — state descent inside that witness

- 固定 branch 下 compatible local solutions；
- profinite exactness 或其他 route-specific exact descent theorem。

这一步得到真正的 exact state，并携带那个 witness。

两阶段修复的是不同 precision loss，不能合并成一个条件。

## 10. A4/P023 routing consequence

这把此前若干边界放进了同一张图：

- support 可以忘掉 path / witness identity；
- coefficient quotient 可以忘掉 factor / branch identity；
- finite precision 可以产生 completion state，但未必 exact descent；
- witness label coherence 与 state realization 是两个独立问题。

如果 future language 会重新读取 witness，那么必须同时保留足以通过**两道 guard**的结构。

Finite-set compactness、directed inverse systems、lcm refinement 与 profinite descent 都是标准既有数学。Enterprise Math 在这里的价值是 two-stage precision routing，以及明确把 witness compactness 本身识别为一种资源。