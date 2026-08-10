# R004 精度起源——补充 20：p-adic 指定结构 target cut

状态：`PROVED_WIP + EXECUTABLE_REFERENCE + STRUCTURE-PRESERVATION SPECIALIZATION + PRIOR_ART_BOUNDED`  
父文档：`R004_PRECISION_GENESIS_QUANTUM_MACRO_CLOSURE_SUPPLEMENT_19.zh-CN.md`  
Owner branch：`research/r004-precision-genesis-closure-20260810`

补充 16–19 解决的是：保留哪些 generators 才能恢复完整 exact carrier，以及何时 obstruction cuts 可以直接由算术/模结构闭式生成。本补充改变目标：future language 不必恢复 exact state，只要求一个指定的**线性 target quotient** 仍可从 coarse world 中唯一恢复。

此时 primitive 不再只是 residue-field rank。对 `Z/p^K`，正确对象是一个 missing row-submodule quotient；补充 19 的普通 matroid 仅在 `K=1` 或 exact-state specialization 中恢复。

## 1. Setup

令

`R=Z/p^K Z`, `X=R^d`。

current observation 为

`O_A(x)=A x`，

必须保留的 target structure 为

`T_B(x)=B x`。

primitive future instructions 仍取 coordinate reset `Z_i`。若保留 reset set `S`，隐藏坐标为 `H=E\S`，则 exact future-safe carrier candidate 为

`q_S(x)=(A x, x|_S)`。

两状态具有相同 `q_S` 当且仅当其差只支撑在 `H` 上，并且属于 `ker A_H`。

因此 `B x` 能通过 `q_S` 下降，当且仅当

`ker A_H subseteq ker B_H`。

这就是 exact target-preservation criterion。

## 2. Row-submodule 对偶判据

在有限 module `R^H` 上使用标准 dot pairing。对任意矩阵 `M`，`Row(M)` 必然 annihilate `ker M`。对整数 lift 做 Smith diagonalization 可证明 `Row(M)` 与 `Ann(ker M)` cardinality 相同，因此

`Row(M)=Ann(ker M)`。

于是

`ker A_H subseteq ker B_H`

等价于

`Row(B_H) subseteq Row(A_H)`。

所以“保住 target quotient”不是普通 rank 条件，而是精确的 **row-submodule inclusion**。

## 3. Missing-target module

定义

`D_H=(Row(A_H)+Row(B_H))/Row(A_H)`。

则

`target safe on H <=> D_H=0`。

`D_H` 是一个有限 abelian p-group，因此它本身就是 typed missing-structure object，而不只是一个 yes/no failure flag。

定义整数 structural repair mass

`Delta(H)=log_p |D_H|`。

计算时不需要 real logarithm；`|D_H|` 必为 p-power，只需反复做 exact division by p。

若 `H subseteq J`，coordinate restriction `R^J -> R^H` 会把 `Row(A_J)` 满射到 `Row(A_H)`，也把 stacked row module 满射到较小 stacked row module，因此诱导

`D_J ->> D_H`。

故

`Delta(H)<=Delta(J)`。

隐藏更多坐标，coarse world 缺失的 target structure 不会减少。

## 4. Smith exponent-mass compiler

对 `R` 上任意矩阵 `M`，取 canonical integer lift，并做整数 Smith normal form，记 diagonal entries 为 `d_i`。定义

`v_i=min(nu_p(d_i),K)`，并约定 `d_i=0` 时 `v_i=K`。

则

`mu_K(M)=log_p |Row_R(M)|=sum_i(K-v_i)`。

所以 target defect 可直接写成

`Delta(H)=mu_K([A_H;B_H])-mu_K(A_H)`。

这给出一个基于 Smith invariants 的 scalable exact backend。仓库中的 reference implementation 刻意使用有限 row-module enumeration，使 oracle 语义透明且与 Smith backend 独立；未来可以替换 backend 而不改 theorem interface。

## 5. Field specialization：relative circuits

当 `K=1`，令

`C=[A;B]`。

则 `H` target-breaking 当且仅当

`rank C_H > rank A_H`。

一个 inclusion-minimal target-breaking set `H` 恰好满足：

- `H` 是 column matroid `M(A)` 的 circuit；
- `H` 在 column matroid `M(C)` 中 independent。

证明思路：minimality 表示每个 proper subset 上 A-rank 与 C-rank 相同。若 H unsafe，则 A 中存在一条被新增 B 坐标解除的 dependence。取其中最小 A-circuit；若它严格小于 H 就得到更小 unsafe set，矛盾，因此 circuit 必须就是 H；其 proper subsets 在 A 中 independent，从而在 C 中也 independent，而 B 正好解除 H 的唯一 A-circuit dependence。

若 target 是 exact state，即 `B=I`，stacked column matroid 为 free，因此所有 `M(A)` circuits 都变成 relative cuts，恢复补充 19。

## 6. Relative cuts 一般不构成 matroid

补充 19 的 exact-state Module Cut Compiler 有特别强的性质：

`cuts=circuits(M(A mod p))`，

因此 minimal carrier instructions 是 dual-matroid bases。

一般 target B 不满足这点。

在 `F_2` 上取

`A=(0,1,1,1)`，

`B=(0,0,0,1)`。

minimal target cuts 为

`{1,3}` 与 `{2,3}`。

它们违反 circuit elimination：消去共同元素 `3` 后，`{1,2}` 中不存在新的 cut。等价地，target-safe hidden-set family 违反 matroid augmentation。

因此一般 relative target-cut clutter 是真正的 hypergraph obstruction family，不是另一个 ordinary matroid 的 circuit family。

## 7. mod p 看不见的高阶 p-adic target information

只看 residue-field rank 会漏掉 target structure。

在 `Z/4` 上令

`A=(1,1)`, `B=(0,2)`。

mod 2 后叠加 B 不增加 rank。但

`z=(1,3)`

满足

`A z=0 mod 4`，

而

`B z=2 mod 4`。

所以 B 不能从 A 恢复。

更一般地，在 `Z/p^K` 上取

`A=(1,1)`, `B=(0,p^t)`, `1<=t<K`。

唯一 minimal hidden cut 是两坐标全集，并且

`D_H ~= Z/p^(K-t) Z`，

故

`Delta(H)=K-t`。

这些例子的 B row 在 mod p 后全部为 zero，但 missing target depth 可以遍历 `1,...,K-1`。因此 ordinary mod-p matroid data 不足以编码完整 structural repair precision。

## 8. Defect mass 单调，但不是 polymatroid rank

由 quotient-surjection theorem，`Delta(H)` 对 hidden-set inclusion 单调。

但 exact primitive-column `Z/4` examples 可以让 `Delta` 违反 submodularity，也能让它违反 supermodularity。因此这个 scalar defect mass 一般不是 ordinary matroid / polymatroid rank function。

真正的 typed primitive 是 missing-target p-group `D_H`；`Delta(H)` 只是它的整数 exponent mass。

这还直接接回此前 quotient exponent-profile compiler：`D_H` 的 invariant-factor exponent word 正好就是隐藏 H 后丢失结构的 exact typed repair profile。

## 9. 对 compiler 架构的直接后果

当前 cut atlas 至少分三层：

1. **Exact-state module reset**：mod-p column matroid circuits；minimal instructions 是 dual-matroid bases。
2. **Field target quotient**：`M([A;B])` 与 `M(A)` 之间的 relative circuit clutter；一般不再 matroidal。
3. **p-adic target quotient**：minimal supports where missing row-submodule quotient `D_H` is nonzero；每条 cut 都携带有限 p-group repair object 与 exponent mass。

因此 `preserve exact state` 与 `preserve declared structure` 是两个不同的 compiler problem。后者可能要求保留 residue field 之上才可见的精度。

## 10. Validation

本补充的 independent exact checks 包括：

- 1,024 个 exhaustive `Z/4`、两坐标、一行 A/B retained-set cases：kernel-inclusion target safety 与 row-submodule inclusion 完全一致；
- 4,800 个额外 small p-power multirow cases：target safety 与 `Delta(H)=0` 完全一致；
- 793 个 `F_2/F_3` one-row systems：minimal compiler cuts 与 relative-circuit formula 完全一致；
- 900 个 random small p-power matrices：direct row-module exponent mass 与 Smith-invariant formula 完全一致；
- 显式 primitive-column examples 验证 `Delta` 可分别违反 submodularity 与 supermodularity。

这些是 finite exact WIP checks，不是 fresh full-repository CI 或 canonical-main claim。

## 11. Prior-art boundary 与下一 frontier

Smith normal form、有限 abelian p-groups、matroid circuits/duality、local/valuation ring modules、matroids over rings/valuation rings 都是 prior mathematics。R004 不主张这些理论为新发明。

当前 project-local addition under test 仅是 compiler bridge：

`declared target quotient -> hidden-coordinate row-submodule defect -> structural cut clutter -> p-group repair profile`。

下一步应把 reference row enumeration 替换为 exact Smith/profile extraction，并测试 A3 determinant/exterior target 与 guard-image lattice 是否能成为同一个 `target object + defect module` 接口的实例；不能为了统一而把 nonlinear semantics 强塞进 linear module model。
