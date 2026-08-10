# R004 精度宇宙生成 —— Supplement 09：relation-rank compiler 与 representation exponent codimension

状态：`PROVED_WIP + EXECUTABLE_CHECKED + A3_CONSUMER + FOUNDATION_FEEDBACK_CANDIDATE`  
父文档：`R004_PRECISION_GENESIS_QUANTUM_MACRO_CLOSURE_SUPPLEMENT_08.zh-CN.md`  
Owner branch：`research/r004-precision-genesis-closure-20260810`

Supplement 08 已经定位真正的 product-compiler 边界：在 componentwise dynamics + full product observation 下，joint action correlation 本身无害；而 cross-axis observable / dynamics coupling 可能要求 joint state。

本补充解决其中一个很大的结构化子类：若 coupled future 通过一个整数线性 relation state 因子化，则可以证明 relation coordinate 足够，并直接对 relation state 编译。

## 1. Linear relation state

固定 prime `p`、cap `K`、ambient dimension `d`，状态为

`x in (Z/p^K Z)^d`。

令 `A` 为整数 `r x d` matrix，定义 relation vector：

`R_A(x)=A x mod p^K`。

future actions 是 componentwise translations `x -> x+a`。

线性性给出：

`R_A(x+a)=R_A(x)+R_A(a)`。

假设 declared observable 只依赖 relation vector，具体取完整的 capped relation valuations：

`O_A(x)=(q_K(R_A(x)_1),...,q_K(R_A(x)_r))`。

则任意 joint action 后的 future observable 都只通过 `R_A(x)` 依赖原始 state。

因此 literal product-state future signature 因子化为：

`Sigma_X = Sigma_R o R_A`。

这就是直接的 P023 factorization certificate：relation coordinate 在这里是因为 sufficiency 被证明了才合法，而不是先假设它合法。

## 2. Surjective relation rank

假设 `A mod p` 有 full row rank `r`。

则某个 `r x r` minor 的 determinant 不被 `p` 整除。该 determinant 是 modulo `p^K` 的 unit，因此对应 square submatrix 在 `Z/p^K Z` 上可逆。于是：

`R_A : (Z/p^K Z)^d -> (Z/p^K Z)^r`

是 surjective。

这给当前 compiler 中的 **relation rank** 一个 exact finite 语义：每个 relation-state tuple 都确实由某个 ambient state 可达。

Matrix rank 与 unit-minor 可逆性属于成熟代数。R004 这里只把该条件作为 exact class-count certificate。

## 3. R004-COMP-T06 —— relation-language reduction

令 `W` 为 ambient state 上任意非空 finite joint translation language。通过 relation matrix 映射：

`R_A(W)={R_A(a): a in W}`。

relation future signature 是这些 induced relation translations 下的完整 capped valuation vector。

按照 Supplement 08 的 product factorization，在 observable 暴露完整 relation-observation vector 时，`r` 个 induced relation actions 之间的 correlation 可以在投影到各 relation axes 后丢弃。

所以 compiler 是：

1. 计算 `z=R_A(x)`；
2. 计算 induced relation action set `R_A(W)`；
3. 投影到每个 relation coordinate；
4. 每个 relation coordinate 使用单轴 p-adic trie compiler；
5. 返回 relation-axis trie tokens 的 tuple。

若 `A mod p` full row rank，该 tuple 就是原 ambient product 上的 coarsest future-safe state。

Class count 精确等于各 relation-axis trie class counts 的乘积。

## 4. Rank-one example：difference 足够

对两个 axes 取

`A=[1,-1]`。

于是

`R_A(x_1,x_2)=x_1-x_2 mod p^K`。

joint translation `(a_1,a_2)` 只诱导

`a_1-a_2`。

若 future observable 只看该 difference 的 capped valuation，那么所有拥有相同 compiled difference-relation token 的 ambient states 都 future-equivalent，即使各自 coordinates 完全不同。

这给出一个 relation coordinate 真正可以替代 product state 的精确 sufficient case。

它与 A3 relation-state language 结构相邻，但 R004 不主张 generic relation concept 的所有权。

## 5. Full-translation state-count theorem

取 complete ambient translation language：

`W=(Z/p^K Z)^d`。

若 `A` 有 full row rank `r`，surjectivity 使 induced relation translations 填满整个

`(Z/p^K Z)^r`。

每个 relation coordinate 因此到达 Supplement 06/07 的 universal-translation endpoint，必须保留 exact residue modulo `p^K`。

最小 future-safe class count 为：

`C_relation=p^(K r)`。

而 exact ambient state space 有：

`C_ambient=p^(K d)`。

不需要 normalized compression ratio。

## 6. Representation exponent codimension

由于两个 class counts 都是同一个 prime 的 exact powers，定义整数：

`Gamma=K(d-r)`。

于是：

`p^(K d)=p^Gamma * p^(K r)`。

`Gamma` 精确计数声明的 future language 已证明无关的 ambient p-adic digit freedoms。

R004 暂称它为当前 relation-compiler family 的 **representation exponent codimension**。

它不是 logarithmic approximation；这个 exponent 本来就来自 exact prime-power state counts。

例如：

- `d=2,r=1,K=3`：`64` ambient states -> `8` safe relation classes，`Gamma=3`；
- `d=3,r=2,K=4`：`p^12` -> `p^8`，`Gamma=4`；
- `r=d`：`Gamma=0`，relation rank 本身不证明任何 exponent-level reduction。

## 7. Rank 代表什么、又不代表什么

本 theorem **不**把 relation rank 等同物理空间维数。

它只说一个更窄、更 operational 的结论：

> 在一个显式声明、并被证明会通过 relation factorization 的 future language 下，`r` 条独立 relation coordinates 已经足够，而其余 `d-r` 条 ambient coordinate directions 在 exact-state 层 future-invisible。

这是 representation theorem，不是 ontology theorem。

也不能推出每个 coupled observable 都有低 rank 线性 relation factorization。Supplement 08 已经给出 coupled Boolean 反例，其 safe partition 会随 joint action correlation 改变；structured relation normal form 必须逐案证明，或由真正的 upstream mother theorem 给出。

## 8. Validation 与 oracle 修正

Executable assets：

- `precision_relation_language_compiler.py` —— 单条 linear relation coordinate；
- `precision_relation_rank_compiler.py` —— full-row-rank relation matrices；
- 对应 tests。

独立 cross-check 时发现初版 validation oracle 在把 joint actions 映射成相同 induced relation action 后做了 dedup，再拿 dedup signature 与 compiler 比较。Dedup 对 kernel equality 在数学上安全，但该 oracle 不够独立。

实现已经修正：compiler construction 仍可 deduplicate induced actions，但 regression comparison 保留**原始 literal joint-action signature**，包括重复 induced coordinates。

修正以后，对多个 primes、caps、ambient dimensions、relation ranks、full-row-rank matrices 与 action subsets 共 **1,313** 个 bounded partition cases 做独立枚举，没有发现 mismatch。

该修正是 evidence trail 的一部分；旧的弱 oracle 不计入 independent validation。

## 9. Architecture consequence

R004 representation compiler 现在已有三个 exact structured regimes：

1. **one prime axis**：arbitrary translation language -> p-adic trie state；
2. **independent/full-vector product**：arbitrary correlated joint translations -> product of marginal trie states；
3. **linear coupled future**：relation matrix -> induced relation language -> relation-rank trie state。

第三层给 A3 consumption 一个清晰入口：

`ambient state -> proved sufficient relation state -> operation-conditioned minimal repair`。

下一 hard question 已不再是“relation coordinate 有没有可能足够”。它当然可以。

真正的问题变成：

> **对没有预先声明 relation matrix 的 coupled future，Enterprise Math 能不能自动发现或认证 minimum sufficient relation/witness state？**

这个问题属于 P023/A3/A4/Foundation 边界，而不应被 R004 默默据为 mother theorem。
