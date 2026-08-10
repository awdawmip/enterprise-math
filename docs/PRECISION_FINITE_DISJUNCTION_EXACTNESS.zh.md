# Finite Disjunction 在 Literal Branch Semantics 下保持 Profinite Exactness

状态：`RESEARCH BRIDGE / NONCANONICAL`

有限 branching 本身并不是 exact descent 的 obstruction。只要 local semantics 保持正确，profinite exactness 对有限 labelled union 是闭合的。

## 1. Branchwise exactness

设有限 label 集 `Lambda` 中每个 exact branch 的整数 solution set 为

`S_lambda subseteq Z^n`，

其 completed solution set 为

`S_hat_lambda subseteq Z_hat^n`。

假设每个 branch 自身 profinite-exact：

`closure(S_lambda)=S_hat_lambda`。

Affine integer branches 是最重要的正面例子之一。

## 2. Literal-union local semantics

假设 unlabelled completed world law 精确等于 labelled union：

`S_hat = union_(lambda in Lambda) S_hat_lambda`。

也就是说，没有 coefficient quotient、support projection 或其他 compiler 在所有 labelled branch solution sets 之外额外制造新的 unlabelled solutions。

这比“written syntax 还在”更强，它是 completed semantic level 上真正的 branch-reflection condition。

## 3. 有限 union 与 closure 交换

因为 Lambda 有限：

`closure(union_lambda S_lambda)`

`= union_lambda closure(S_lambda)`。

再代入 branchwise profinite exactness：

`= union_lambda S_hat_lambda`

`= S_hat`。

所以整个 unlabelled finite disjunction 自身也 profinite-exact。

因此：

`finite labelled union`

`+ literal local branch semantics`

`+ branchwise profinite exactness`

推出

`whole union is profinite-exact`。

## 4. 为什么 ghost product 不适用这个 theorem

Intersective ghost 虽然 exact world 中有三个 labelled square branches，但 modular product equation 在 composite modulus 下**并不**等于这些 branch equations 的 literal union。

mod15 时 product 有 root，而三个 labelled branches 全部为空。

所以 completed / unlabelled solution set 严格大于 completed labelled branch sets 的 union。

这个 theorem 的 local semantic hypothesis 在 branchwise descent 之前就已经失败。

## 5. Infinite union 不同

若 branches 无限，closure 未必与 union 交换：

`closure(union_i S_i)`

可能严格大于

`union_i closure(S_i)`。

Infinite-label escape 给出了 witness-level 对应物：每个 finite precision 都能挑一个 branch，但没有任何固定 branch 能 global 存活。

若 witness parameter space 有 compact / proper structure，可以恢复相应 projection theorem；任意 infinite discrete witness alphabet 则不行。

## 6. Routing consequence

Finite disjunction 不应因为形式上可以相乘，就默认被编译成 multiplicative polynomial 再 coefficientwise reduction。如果 exact witness identity 可能被未来读取，semantics-safe representation 应优先保 labelled union；除非已有 theorem 证明替代 encoding 在当前 coefficient precision 下仍 branch-reflecting。

这与项目其他地方的 design rule 完全一致：

> 先保住 semantic relation，再在证明 compression 对 future / witness language 安全之后压缩 representation。

Finite unions 与 topological closure 都是标准既有数学。Enterprise Math 在这里的价值是明确给出 finite RELATION branching 能安全穿过 profinite descent 的精确 hypotheses。