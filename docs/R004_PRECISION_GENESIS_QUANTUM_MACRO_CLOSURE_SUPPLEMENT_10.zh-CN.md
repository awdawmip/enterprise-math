# R004 精度宇宙生成 —— Supplement 10：自动 congruence-to-relation module extraction

状态：`PROVED_WIP + EXECUTABLE_CHECKED + PRIOR_ART_SPECIALIZATION + FOUNDATION_FEEDBACK_CANDIDATE`  
父文档：`R004_PRECISION_GENESIS_QUANTUM_MACRO_CLOSURE_SUPPLEMENT_09.zh-CN.md`  
Owner branch：`research/r004-precision-genesis-closure-20260810`

Supplement 09 已证明：若给定 linear relation matrix，可以得到 sufficient future state。本补充进一步拿掉“必须先猜 matrix”这个条件，在一个重要 regime 中直接从 future-safe kernel 本身自动恢复 relation-module shape。

从声明的 future signature 得到 kernel 后，compiler 首先检查它是否是 additive translation congruence。若通过，则 opaque partition 规范地变成 finite quotient module，随后可以仅用 exact integer torsion counts 恢复其 prime-exponent shape。

## 1. Translation-congruence gate

固定

`X=(Z/p^K Z)^d`

并令

`E=ker(Sigma)`

为声明 future signature 得到的 future-safe equivalence relation。

检查是否对任意 `x,y,z in X` 都有：

`x E y -> (x+z) E (y+z)`。

若 translation invariance 成立，令

`H=[0]_E`。

则 `H` 是 additive subgroup，并且

`x E y iff x-y in H`。

所以每个 `E`-class 都是 `H` 的 coset，safe state 就是 quotient group/module：

`Q=X/H`。

这就是 group congruence 与 normal subgroup 的标准对应；在 abelian case 下所有 subgroup 都 normal。R004 不把这部分成熟代数当作新数学。

Executable gate 采用 fail-closed 方式：若 zero block 不是 subgroup，或 partition 不精确等于该 zero block 的 coset partition，relation-module compiler 就拒绝赋予 quotient exponent profile。

## 2. Exact quotient torsion counts

假设 congruence gate 已通过。

对 `j=0,...,K` 定义：

`T_j = #{q in Q : p^j q = 0}`。

因为 `Q` 是 finite abelian p-group，每个 `T_j` 都是 `p` 的 exact power。

不使用 real logarithm，而是通过 repeated exact division 定义整数 `alpha_j`：

`T_j=p^(alpha_j)`。

也就是说 `alpha_j` 本来就是 finite state count 中的 prime exponent。

若

`Q ~= direct_sum_i Z/p^(e_i) Z`，

则

`alpha_j=sum_i min(j,e_i)`。

于是第一有限差分：

`beta_j=alpha_j-alpha_(j-1)`

满足

`beta_j=#{i:e_i>=j}`。

因此 exponent 恰为 `j` 的 invariant axes 数为

`beta_j-beta_(j+1)`。

由此可仅从 finite torsion-count sequence 恢复完整 invariant exponent multiset `(e_i)`。

有限阿贝尔群结构定理、Smith normal form / invariant factor decomposition 都属于成熟先行代数，而不是 R004 的新发明。

## 3. R004-COMP-T07 —— quotient exponent profile compiler

对 `(Z/p^K)^d` 上通过 translation-congruence gate 的 future kernel，定义 compiled **quotient exponent profile** 为由上述 torsion finite differences 恢复的降序 tuple：

`E_Q=(e_1,...,e_r)`。

该 profile 在通常 invariant-factor 排序意义下是 canonical 的。

它比 quotient cardinality 单独包含更多结构。例如：

`Z/p^3 x Z/p`

与

`Z/p^2 x Z/p^2`

都有 `p^4` 个 elements，但 profiles `(3,1)` 和 `(2,2)` 可以区分二者 future-relevant module shape。

## 4. Representation exponent mass 与 codimension

定义

`M_Q=sum_i e_i`。

于是

`|Q|=p^(M_Q)`。

这仍不是 real logarithmic definition；profile 本身就是 exact quotient size 的整数 prime-exponent decomposition。

ambient state 的 exponent mass 为

`M_X=K d`。

定义 generalized representation exponent codimension：

`Gamma=Kd-M_Q`。

这扩展了 Supplement 09 full-row-rank matrix 情形的 `Gamma=K(d-r)`。

若每个 quotient axis 都是 full depth `K`，那么 `M_Q=Kr`，两条定义一致。若 quotient axes 有 mixed depths，则 `Gamma` 精确记录 future-safe kernel 删除的 p-digit mass。

## 5. 自动恢复 examples

Executable compiler 在完全不预先告诉答案的情况下恢复：

- exact `Z/8 x Z/8` state -> profile `(3,3)`；
- kill 一条完整 axis 后 -> `(3)`；
- quotient `Z/8 x Z/2` -> `(3,1)`；
- 3-adic quotient `Z/9 x Z/3` -> `(2,1)`；
- Supplement 09 rank-two relation matrix 的 kernel，在 `K=2` 时 -> `(2,2)`。

即使 raw class count 一样，torsion sequences 仍可区分不同 quotient shapes。

## 6. Noncongruence boundary

Supplement 08 的 coupled-AND future-safe partitions 无法通过 translation-congruence gate。

Diagonal action language 的 partition：

`{{00},{01,10},{11}}`。

Cross action language 的 partition：

`{{00,11},{01},{10}}`。

二者都不是自身 zero block 的 coset partition。因此都不能诚实地表示成 additive quotient module。

这给出强 fail-closed rule：

`future kernel not translation-congruent -> do not force quotient-exponent coordinates`。

这样的 kernel 必须保留 richer relation / witness representation，除非另有独立证明的结构可用。

## 7. Supplement 10 之后的 compiler ladder

R004 当前 structured compilation ladder 为：

### Layer A —— axiswise arithmetic

`one p-power axis + arbitrary translations -> p-adic trie compiler`。

### Layer B —— full product observation

`product state + componentwise dynamics + arbitrary correlated actions -> product of marginal compilers`。

### Layer C —— declared relation factorization

`coupled future factors through a proven linear relation matrix -> relation-rank compiler`。

### Layer D —— 从 kernel 自动发现 relation state

`future kernel is additive translation congruence -> quotient module -> invariant exponent profile`。

### Layer E —— genuine noncongruent coupling

若上述 gates 全都不通过，compiler 必须保留 general structured relation / witness state；强行使用 exponent 或 quotient coordinates 会不 sound。

这就是 A3/A4 ownership 真正开始不可绕过的位置。

## 8. Validation

新增 executable module：

`src/enterprise_math/precision_congruence_relation_compiler.py`

以及对应 regression coverage。

独立 checks 只使用 exact subgroup/coset/torsion arithmetic，就恢复了 `(3,3)`、`(3)`、`(3,1)`、`(2,1)` profiles；coupled-AND partitions 则按预期被 congruence gate 拒绝。

Supplement 09 的 relation-rank oracle 也在本轮进一步加强：compiler construction 可以 deduplicate 相同 induced relation actions，但 regression 改为拿 compiled token 与**原始 literal joint-action future signature**对照。修正后独立 sweep 共 **1,313** 个 partition cases，没有发现 mismatch。

本轮不声称 Lean status 或 fresh full-repository CI status。

## 9. Prior-art 与 ownership 边界

以下都属于成熟数学，R004 不主张原创：

- group congruence 作为 normal subgroup cosets；
- finite abelian group 分解为 prime-power cyclic factors；
- PID 上的 Smith normal form / invariant factors；
- finite abelian p-group 的 torsion subgroup counts 作为结构不变量。

R004 的项目级新增是 architecture + executable specialization：把这些成熟 invariants 放到 generic future-safe partition 与 A3/A4 relation/witness state 之间，形成一个中间 compiler stage。

## 10. Revised frontier

目前最强的 compiler open question 已进一步收窄为：

> **当 future-safe kernel 既不是 product kernel，也不是 additive congruence 时，哪一种最弱 structured relation/witness object 能够表示它，而不退回 opaque class label？**

候选 destination 包括 A3 weighted relation state、A4 witness/correspondence state，或二者之间新的 verified bridge。该问题必须由正确 owner / Foundation route 推进；R004 只应继续提供 counterexamples、sufficient special cases 与 compiler pressure tests。
