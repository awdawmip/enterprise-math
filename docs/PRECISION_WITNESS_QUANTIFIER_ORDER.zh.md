# Witness Quantifier Order Across Precision

状态：`RESEARCH BRIDGE / NONCANONICAL`

Finite-precision existence statement 与 exact witnessed-state statement 的逻辑形状并不相同。它们之间的 gap 可以拆成三次彼此独立的 quantifier / descent step。

## 1. 起始 local statement

对 labelled world law，finite precision 通常只给出：

`for every precision M`

`there exists a local label lambda_M`

`there exists a local state x_M`

使 local branch law 成立。

符号上：

`forall M exists lambda_M exists x_M : P_(lambda_M)(x_M) mod M`。

这还没有给出一个跨 precision 固定的 label，也没有给出一个跨 precision 固定的 state。

Exact target statement 则是：

`exists lambda_* exists x in Z^n : P_(lambda_*)(x)=0`。

两者既有 quantifier order 差异，也有 state space 差异。

## 2. 第一次交换：precision 与 witness label

首先希望把

`forall M exists lambda_M`

变成

`exists lambda_* forall M`。

这个 implication 一般不成立。

它在 finite-branch theorem 的 witness-coherence 条件下成立：

- precision 支持有限 joint refinement；
- admissible witness supports 随 refinement 缩小；
- witness space compact（finite labels 是最简单情形）；
- local quotient branch-reflecting，因此每个 local solution 确实贡献真实 witness support。

此时 witness supports 有 finite-intersection property，所以存在一个 `lambda_*` 在所有 precision 下存活。

这是真正的 quantifier swap，靠 compactness / coherence 保证，而不是语法操作。

## 3. 第一次交换的失败：witness escape

对无限 labels `k=1,2,...`，若

`S_M={k:M divides k}`，

则有

`forall M exists k_M`，

却没有

`exists k forall M`。

任何固定 label 最终都会被阻断，而 local 选择的 label 可以随着 precision 增长不断变大。

所以 noncompact witness space 会让

`forall precision exists witness`

严格弱于

`exists witness forall precision`。

## 4. Directedness 也是第一次交换的一部分

即使 witness space 有限，如果 declared precision family 无法形成 joint refinement，也不能自动得到 coherence。

只观察分离的 prime moduli 时，p 上的 local label 与 q 上的 local label 未必会在 lcm `pq` 上被同时检验。缺失 joint precision 可以隐藏 incompatibility。

因此需要的是 precision 上的 finite-intersection structure，而不只是“有很多 individually fine observations”。

对 modular systems，全部 moduli 或一条 nested power ladder 都能提供这种 directedness。

## 5. 第二次交换：local branch states 到一个 completion state

一旦固定一个 label `lambda_*`，statement 变成

`forall M exists x_M : P_(lambda_*)(x_M) mod M`。

对固定有限整数 polynomial system，profinite state space 的 compactness 给出

`exists x_hat in Z_hat^n : P_(lambda_*)(x_hat)=0`。

所以在 stable branch law 下，分别选择的 local states 可以正规化为一个 compatible completion state。

如果 branch law 或 state semantics 自己随 precision 改变，则这一步不能自动套用。

## 6. 第三步：completion 到 exact state

最后需要的是

`exists x_hat in Z_hat^n`

`=>?`

`exists x in Z^n`。

这不是同一个 compact space 内的 quantifier rearrangement，而是从 completion world 回到 exact integer state space 的**world change**。

它需要 route-specific descent theorem，例如 profinite exactness：

`closure(S_Z)=S_hat`。

Affine integer equations 满足它。

Intersective ghost polynomial 不满足。

## 7. 完整 normalization chain

在相应 guards 下，exact witnessed existence 可以按以下链条得到：

`forall M exists lambda_M exists x_M`

`--[branch reflection + directed witness compactness]-->`

`exists lambda_* forall M exists x_M^(lambda_*)`

`--[state compactness for fixed branch]-->`

`exists lambda_* exists x_hat in Z_hat^n`

`--[branch profinite exactness/descent]-->`

`exists lambda_* exists x in Z^n`。

每个箭头由不同数学保证，也有不同 failure mode。

## 8. 三种 sharp failure

### Failure A — local branch reflection

mod15 product ghost locally solvable，但 mod15 没有任何 labelled branch。

所以即使 unlabelled numeric law 为 true，最开始的 `exists lambda_M` 就已经失败。

### Failure B — witness compactness / coherence

Infinite-label escape 在每个 modulus 都有 labelled branch，却没有一个 label 能通过全部 moduli。

第一次 quantifier exchange 失败。

### Failure C — exact state descent

Intersective polynomial 有一个满足全部 finite precisions 的 profinite state，却没有 integer state。

最后 descent 失败。

这三种 error 完全不同，需要不同 repair。

## 9. Fixed witness 与 varying witness precision

一个特别重要的特例是比较：

`exists one integer x such that for all M, P(x)==0 mod M`

与

`for all M, exists x_M such that P(x_M)==0 mod M`。

第一条会直接推出 `P(x)=0` exact，因为一个整数若被所有 M 整除，只能为0。

第二条一般只能得到一个 profinite witness。

所以 witness 在 precision quantifier 的**前面还是后面绑定**，本身就是 semantics 的一部分。

## 10. Foundation consequence

Future / precision system 不应只用 local truth value 表示 existential statement。如果 exact theory 以后还需要 witness，就必须保留足够结构来证明相关 quantifier exchanges。

真正要问的不只是：

`每个 finite world 是否 locally satisfiable？`

而是：

`哪些 witness variables 已经 global 绑定，哪些可以随 precision 改变，以及什么 theorem 允许这些 quantifiers 交换？`

Compactness、finite-intersection arguments 与 profinite descent 都是标准既有数学。Enterprise Math 在这里的价值是对 witness-binding order 的明确 precision interpretation。