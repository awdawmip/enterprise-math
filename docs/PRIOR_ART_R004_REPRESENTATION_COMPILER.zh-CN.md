# R004 future-language representation compiler —— prior art 边界

状态：`RESEARCH PRIOR-ART MAP / NOVELTY_UNVERIFIED`

本说明把 R004 compiler package 与成熟的 quotient、p-adic、product、finite-abelian、normal-form 数学分开。即使得到 closed-form finite compiler specialization，也不能据此把底层代数宣称为项目发明。

## 1. Generic future-safe quotient 属于上游

Generic statement

`declared future signature -> coarsest safe equality = kernel of that signature`

属于现有 P023/FQ-004 future-compatible quotient layer，R004 不重新取得该 mother theorem 的所有权。

P024 也已经把同一原则专门化到 integer translation languages 与 reachable boundary orbits。因此 R004 compiler 工作属于 consumer / specialization：它问的是，哪些特定 arithmetic future kernels 可以直接得到 structured normal form，而不是最后只剩一次 opaque partition-refinement 结果。

## 2. P-adic valuation 与 prefix geometry 是成熟数学

p-adic valuation laws 是成熟数学 [SRC-EOM-PADIC-VALUATION]；valuation 对乘法可加，对加法满足 non-Archimedean minimum inequality。

R004 单轴 compiler 使用的有限事实是：`v_p(x-c)` 衡量 `x` 与 center `c` 从最低位开始连续共享多少个 base-`p` digits。把有限 center set 按共享低位 prefix 组织成 trie，也属于成熟 prefix / p-adic congruence-ball 结构；R004 不主张这些概念本身为新发明。

项目级新增只在声明的 capped-valuation translation language 上给出 exact normal form：

`center token OR deepest occupied exit-parent token`，

class count 为

`|centers| + # deficit trie nodes`。

该精确 package 的历史 novelty 仍未验证。

## 3. Product kernels 与 CRT 是成熟数学

Chinese remainder decomposition、Cartesian product kernels、componentwise factorization 都是标准数学。

因此 full product observable 在 componentwise dynamics 下通过 marginal future kernels 因子化，不作为新的 abstract product theorem 宣称。

R004 使用它得到的是架构上的 negative boundary：

> 只要 required future outputs 仍逐 component，correlated joint action labels 本身并不需要 joint repair state。

只有出现真正 cross-axis observable / dynamics / witness coupling，joint repair 才成为必要候选。

## 4. Linear relation state 与 rank 属于成熟代数

整数 matrix `A` 定义

`R_A(x)=A x mod p^K`

只是 ordinary modular linear algebra。`A mod p` full row rank 时存在 unit minor，从而 relation map 对 relation module surjective。Matrix rank、invertible minor 与线性 factorization 都属于 prior algebra。

R004 的新增只在 application/compiler 边界：

`ambient future -> proved relation factorization -> induced relation action language -> minimal relation repair`。

full translations 下得到 exact future-safe state count `p^(Kr)`，ambient exact state count 为 `p^(Kd)`，并定义整数 exponent codimension `K(d-r)`。底层代数属于先行工作；representation-compiler interpretation 仍是 project-local、`NOVELTY_UNVERIFIED`。

## 5. Group congruence 与 finite abelian decomposition 属于 mature math

Group congruence 对应 normal subgroup；在 abelian group 中每个 subgroup 都 normal。因此 `(Z/p^K Z)^d` 上 translation-invariant equivalence relation 可以由 zero class 给出 quotient。这属于成熟 group / universal algebra。

Mathlib 官方文档已经记录 finite abelian groups 分解为 prime-power cyclic `ZMod` direct sums [SRC-MATHLIB-FINITE-ABELIAN]，也提供 PID 上 submodule 的 Smith-normal-form bases [SRC-MATHLIB-SMITH-NORMAL-FORM]，以及利用 Smith coefficients 对 finite free-module quotient 做 cyclic quotient decomposition [SRC-MATHLIB-FREE-MODULE-QUOTIENT]。

所以 R004 不主张 finite abelian classification、Smith normal form、invariant factors 或 cyclic quotient decomposition 是新数学。

## 6. 用 torsion counts 恢复 exponent profile 只是 invariant 用法

对 finite abelian p-group

`Q ~= direct_sum_i Z/p^(e_i) Z`，

被 `p^j` annihilate 的 elements 数为

`T_j=p^(sum_i min(j,e_i))`。

因此对 `T_j` 的 exact `p`-power exponents 做 finite differences，就能恢复有多少 cyclic factors 的 depth 至少为 `j`，最终恢复 invariant exponent multiset。

这直接来自 standard cyclic decomposition，不是新的 classification theorem。

R004 只把这些 counts 当 **compiler extraction method**：generic future kernel 一旦通过 additive-congruence gate，就可以不预先声明 relation matrix、也不使用 real logarithm，直接恢复 structured quotient exponent profile。

## 7. Fail-closed compiler ladder 才是项目级 architecture

当前 R004 package 为：

1. one p-power axis + arbitrary translations -> p-adic trie compiler；
2. product/full-vector future -> product of marginal compilers，即使 joint actions correlated；
3. proved linear coupled future -> relation-rank compiler；
4. generic future kernel 是 additive congruence -> quotient module -> invariant exponent profile；
5. noncongruent coupled kernel -> 不强行套 exponent/module coordinates，保留 richer relation/witness state。

前四层都使用成熟数学。R004 当前真正研究的是：**typed fail-closed compilation architecture**、若干 exact closed-form specializations、finite operation/state-complexity laws，以及何时必须升级到 A3/A4-style state 的明确边界。

目前没有任何 compiler result 是 `CANONICAL_MAIN`。整套架构的历史 novelty 继续标记 `NOVELTY_UNVERIFIED`。
