# 先行工作——R004 Arithmetic Cut Compiler

状态：`RESEARCH PRIOR-ART MAP / NOVELTY_UNVERIFIED`

补充 18 在一个 weighted binary future-language family 中，把 carrier cuts 识别为 subset-sum distinctness 失败的 support-minimal supports。dissociated set / subset-sum 理论本身属于成熟 additive combinatorics。

## 1. Dissociated / subset-sum-distinct sets 是先行工作

Dutta 把正整数集合定义为 subset-sum-distinct / dissociated，当且仅当所有有限 subsets 的 sums 都不同；并给出等价条件：所有 coefficients 属于 `{-1,0,+1}` 的零和 relation 都必须 trivial [SRC-DUTTA-2026-DISSOCIATED-GREEDY]。

Mendoza-Smith 与 Tanner 在 sparse recovery 中使用同样的 operational condition：若 support 上全部 `2^k` subset sums pairwise different，则称 signal dissociated [SRC-MENDOZA-SMITH-TANNER-2015-DISSOCIATED]。

更早的 additive-combinatorics 工作也研究 dissociated sets 的 sumsets [SRC-SHKREDOV-2007-DISSOCIATED-SUMSETS]。

因此 R004 不把 dissociated set、distinct subset sums 或 `{-1,0,1}` relation characterization 宣称为新数学。

## 2. 当前 project-local bridge

R004 Supplement 18 只主张以下 specialization：

1. exact binary state `x in {0,1}^d`；
2. current observation `L_a(x)=sum_i a_i x_i`，weights 为非零整数；
3. future generators 是 coordinate bit flips；
4. retained flip set `S` 的 exact safe quotient 为 `q_S=(L_a,x|_S)`；
5. deleted coordinate set `H` 破坏 full carrier，当且仅当 `H` 上的 hidden weight subfamily 非 dissociated；
6. minimal carrier cuts 精确等于 observation weights 中 support-minimal nontrivial `{-1,0,1}` relations。

所以即使存在 novelty，也只能位于 future-safe compiler reduction 与 obstruction-cut interpretation，而不是 dissociativity 本身。

历史 novelty 仍为 `NOVELTY_UNVERIFIED`。
