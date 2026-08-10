# R004 精度起源——补充 23：typed defect certificate composition

状态：`PROVED_WIP + EXECUTABLE_REFERENCE + P023/A4_COMPOSITION_BRIDGE`  
父文档：`R004_PRECISION_GENESIS_QUANTUM_MACRO_CLOSURE_SUPPLEMENT_22.zh-CN.md`  
Owner branch：`research/r004-precision-genesis-closure-20260810`

补充 20–22 已得到几类 exact defect representation：linear target 的 p-adic module、A3 exterior/guard specialization，以及 arbitrary nonlinear MAY semantics 的 A4 support correspondence。本补充研究：连续 representation changes 中，这些 certificate 如何在不重新打开 fine state 的情况下组合。

答案必须 typed。不存在一个 universal scalar defect addition law。每类 certificate 有自己的 strong composition law，并且只能沿 sound erasure path 降到更弱 semantics。A4 MAY correspondence 是 total conservative fallback。

## 1. Universal MAY support composition

设

`X --q1--> Q1 --r--> Q2`，

`t:X->T` 为任意 target。若第一阶段只保留 exact support relation

`R1=R_(q1,t) subseteq Q1 x T`，

令 `r^op subseteq Q2 x Q1` 为 r 的 reverse graph，则

`R_(r o q1,t)=r^op;R1`。

证明直接来自定义：右边 `(b,y)` 成立，当且仅当存在 `a in Q1`，满足 `r(a)=b`，且存在 fine x 使 `q1(x)=a,t(x)=y`；这恰好就是 composite collapse 的 b-fiber 中出现 y。

所以 MAY support certificate 在后续 source coarsening 中总能 exact transport，不需要重新打开 X。

若 future target evolution 还有 relation `S subseteq T x U`，则 exact coarse MAY support 是

`R_(q1,t);S`。

因此 source coarsening 与 future MAY evolution 都由 ordinary relation composition 处理。

## 2. Strong certificate families 与 erasure

### Functional certificate

descended function `f:Q->T` 在下一步仍 functional 时按 function composition 组合；其 MAY erasure 是 graph(f)。

继续 source coarsening 后 function 可能不再下降。一旦 new fibers 不再 singleton，就安全降级成 support relation。

### Homogeneous group/module defect

translation-homogeneous target 携带 variation subgroup/module，以及解释 fiber action 的 maps。nested homogeneous collapses 使用 group/module extension law。其 MAY erasure 是对应 coset-support relation。

### Weighted/COUNT relation certificate

在声明 semiring 上的 relation matrix 按 semiring matrix multiplication 组合。若存在已验证的 Boolean support semiring homomorphism，则 erasure 与 composition commute。

对 natural-number witness counts，`n -> (n != 0)` 就是该 factor，因此

`support(A B)=support(A) support(B)`，

右侧是 Boolean relational composition。

### MAY support certificate

ordinary relation composition 永远定义。因此 stronger closure gate 失败时，它是 total fallback。

## 3. Nested linear target defect 的 short exact sequence

在 `R=Z/p^K` 上，令 finer linear observation 的 row module 为

`V=Row(A1)`，

进一步 coarsening 的 row module 为

`U=Row(A2) subseteq V`，

target row module 为

`W=Row(B)`。

coarser world 与 finer world 的 Structural Target defects 分别为

`D2=(U+W)/U`，

`D1=(V+W)/V`。

自然映射

`D2 -> D1`, `x+U |-> x+V`

为 surjection。其 kernel 为

`((U+W) cap V)/U`。

因为 `U subseteq V`，由 modular law：

`(U+W) cap V = U+(W cap V)`。

所以

`ker ~= (W cap V)/(W cap U)`。

定义 incremental defect

`I_(2/1)=(W cap V)/(W cap U)`。

于是得到 exact sequence

`0 -> I_(2/1) -> D2 -> D1 -> 0`。

这就是 nested linear target loss 的 exact composition law。

## 4. Exponent mass 沿 chain 可加

对 short exact sequence 取 p-power cardinality：

`|D2|=|I_(2/1)| |D1|`。

所以 integer exponent mass 满足

`mu(D2)=mu(I_(2/1))+mu(D1)`。

沿任意 nested linear-collapse chain，incremental masses telescope；只要 endpoints 与 target 固定，总 scalar repair mass 与选哪条中间链无关。

但这不意味着 defect mass 是 matroid/polymatroid rank。补充 20 已给出离开单条 nested chain 后的 submodularity 与 supermodularity failures。chain additivity 明显弱于 global lattice-rank law。

## 5. Exponent profile 没有 extension data 时不能组合

short exact sequence 决定 cardinality，但 middle module 的 invariant exponent profile 并不由 submodule profile 与 quotient profile 唯一决定。

在同一个 ambient target group

`T=Z/4 x Z/2`

里，令

`H1=< (2,0) > ~= Z/2`。

可以取

`H2a=< (1,0) > ~= Z/4`，

也可以取

`H2b=< (2,0),(0,1) > ~= Z/2 x Z/2`。

两条 chain 都有

`profile(H1)=(1)`，

且

`profile(H2/H1)=(1)`。

但 total profile 分别为

`(2)` 与 `(1,1)`。

因此 exact composable structured certificate 必须保留 actual module/group presentation 与 morphisms，或等价 extension data。rank、total mass、invariant-factor profile 都只是 complexity summary，不是完整 composition state。

## 6. 禁止 automatic upward lift

compiler 使用的每个 sound erasure，若没有 explicit reconstruction certificate，都只能单向使用。

已有三个最小边界：

1. **MAY 不决定 COUNT。** 同一 support edge 的 witness count 可以是 1 或 2，Boolean support 完全相同。
2. **Coset support 不决定 action transport。** 补充 22 的 `Z/6 -> Z/2` 例子里，两个 coarse fibers 都有 full `Z/3` support，但同一个 kernel translation 的 target derivative 在两 fiber 上方向相反。
3. **Profile 不决定 structured defect。** 上述 extension 例子具有相同 stage profiles 却有不同 total module；补充 21 还证明相同 A3 relation exponent profile 可以对应不同 projective directions。

所以 compiler 可以沿 verified forgetful map 自动**降级**，但不能仅因为某个 stronger realization 存在就从弱 certificate 自动推回强 certificate。

## 7. Typed partial composition table

当前 fail-closed 表：

| Certificate kind | Strong composition gate 通过时 | Safe fallback |
|---|---|---|
| function | function composition / constant-on-new-fibers | MAY graph/support |
| p-adic module defect | 带 explicit module maps 的 short exact sequence | coset/MAY support |
| homogeneous group defect | derivative homogeneity 下 subgroup extension | coset/MAY support |
| semiring-weighted relation | semiring matrix composition | 通过 declared Boolean factor 降为 MAY |
| MAY correspondence | relation composition | itself |

strong level 是 partial algebra，但 MAY level 是 total 的。

这就是 **typed defect certificate calculus** 的含义：不是一个 universal defect algebra，而是一组 exact algebras，加上显式 erasure morphisms。

## 8. Validation

Independent exact checks 包括：

- carrier 最多五 states 的 nested set partitions + binary targets 共 12,526 cases：`R_(r o q,t)=r^op;R_(q,t)` 全部 exact；
- entries 为 0/1/2 的全部 2x2 natural-number witness-matrix pairs，共 6,561 cases：count-semiring product 的 Boolean support 与 Boolean relational composition 完全一致；
- 1,171 个 nested cyclic-group quotient / homomorphic-target cases：target supports 都是 exact variation-subgroup cosets，sequential MAY support 与 composite collapse 完全一致；
- 4,000 个 random nested p-power row-module systems：linear defect short-exact-sequence cardinality identity 全部成立；
- 额外 small subgroup-chain checks 验证 exponent-mass telescoping。

这些是 finite exact WIP checks，不是 fresh full-repository CI 或 canonical-main claims。

## 9. Ownership 与下一 frontier

Generic future-safe quotient descent 仍归 P023。Generic relation/correspondence composition 仍归 A4。Semiring-weighted relation composition 与有限 group/module exact sequences 都是 prior mathematics。R004 当前只提供 typed compiler dispatch/composition contract 与 explicit no-upward-lift boundary。

下一步真正值得研究的是 **certificate minimization under composition**：对一个 multi-stage future program，求不重新打开 fine state 即可贯穿整条程序的 weakest certificate type 与最小 retained generator surface。这会把补充 16–19 的 obstruction-cut basis 与本补充的 typed composition laws 真正接起来。
