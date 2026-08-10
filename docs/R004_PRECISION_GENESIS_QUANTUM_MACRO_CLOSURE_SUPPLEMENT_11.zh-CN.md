# R004 精度宇宙生成 —— Supplement 11：fraction-free linear-lift compiler 与 A3 exterior bridge

状态：`PROVED_WIP + EXECUTABLE_CHECKED + A3_BRIDGE + PRIOR_ART_SPECIALIZATION`  
父文档：`R004_PRECISION_GENESIS_QUANTUM_MACRO_CLOSURE_SUPPLEMENT_10.zh-CN.md`  
Owner branch：`research/r004-precision-genesis-closure-20260810`

Supplement 10 使用 additive-congruence gate，把一部分 future kernels 转成 quotient modules。该 gate 故意很严格。本补充证明：原 finite modular carrier 上 congruence gate 失败，**并不等于**已经必须进入完全一般的 relation / witness state。

一个 noncongruent finite partition 仍可能在把 carrier lift 到 `Z^d` 后，恰好是普通 integer / rational linear quotient 的 restriction。R004 现在用 fraction-free determinants 检测这类情况。

## 1. Integer lift 中的 finite future partition

令

`X subset Z^d`

为 finite declared carrier，`E` 为声明 future language 诱导的 future-safe partition。

收集所有已经位于同一 future class 内的 state differences：

`D_E={x-y : x E y}`。

令

`V_E=span_Q(D_E)`。

任何在每个 `E`-class 上 constant 的 linear coordinate，都必须 annihilate `V_E`。

因此 compiler 首先应该问的并不是 `E` 是否为原 finite modular carrier 的 congruence，而是 `E` 是否等于 rational subspace `V_E` 的 coset relation 在 `X` 上的 restriction。

## 2. R004-COMP-T08 —— linear-lift span criterion

Partition `E` 精确等于 modulo `V_E` 的 coset relation restriction，当且仅当任何两个不同 `E`-classes 的 states 都满足：

`x not E y -> x-y notin V_E`。

正向显然。反向则因为所有 same-class differences 按定义都在 `V_E` 中，而上述条件排除了每个 inter-class difference，所以在 finite carrier `X` 上：

`x E y iff x-y in V_E`。

这只是 finite linear-algebra criterion，不是新的 abstract quotient theorem。

分支只用 exact integer rank 做 membership test：`v in V_E` 当且仅当把 `v` 加到 difference basis 后，matrix rank over `Q` 不增加。

## 3. 任意 codimension 的 fraction-free determinant token

设 `V_E` 的 rank 为 `k<d`，选任意 `k` 条 independent integer intra-class differences 作为 matrix `B` 的 rows。

对每个含 `k+1` 个 columns 的 subset `J`，定义：

`Phi_B(x)_J = det([B_J ; x_J])`。

所有 coordinates 都是 integers。Executable layer 使用 Bareiss-style fraction-free elimination 算 determinants。

因为 determinant 对最后一行线性：

`Phi_B(x)-Phi_B(y)=Phi_B(x-y)`。

所有 `(k+1)x(k+1)` minors 同时为零，当且仅当 append `x-y` 不增加 `B` 的 row rank。因此：

`Phi_B(x)=Phi_B(y)`

当且仅当

`x-y in span_Q(B)=V_E`。

与 R004-COMP-T08 合并：

`E = ker(Phi_B)|_X`。

因此任何通过 linear-lift span gate 的 finite future partition 都会得到一个完全 integer 的 determinant relation token，不需要 rational nullspace coordinates。

具体 determinant tuple 会随 `V_E` 的 integer basis 选择改变，但其 equality kernel 在 `X` 上不变。R004 把 kernel / future partition 当 semantic object，而 determinant tuple 只是一个 exact coordinate representation。

Exterior powers、alternating maps、minors、determinants 都是成熟 linear algebra；Mathlib 也已有 canonical exterior-algebra / exterior-power / determinant APIs。R004 不把这些构造本身主张为新数学。

## 4. Codimension one：自动 scalar relation recovery

若

`rank(V_E)=d-1`，

annihilator 是 one-dimensional。Primitive integer normal

`c_E in Z^d`

在 sign 之外唯一。

取 `d-1` 条 independent intra-class differences，它们的 `(d-1) x d` matrix 的 signed cofactors 给出 integer normal；再除掉 coordinates 的 gcd，并固定 sign convention。

那么 partition 恰好是

`x -> c_E . x`

的 fibers，当且仅当每个 inter-class difference 与 `c_E` 的 dot product 非零。

这是 determinant compiler 的 codimension-one specialization：这里只有一个 `d x d` minor，在固定 normalization 下就是 scalar linear coordinate。

## 5. Coupled-AND counterexample 比一般 witness state 更简单

Supplement 08 使用 two-bit state `(Z/2)^2`、XOR dynamics 与 coupled observable：

`O(x_1,x_2)=x_1 x_2`。

Diagonal action language

`{(0,0),(1,1)}`

的 safe partition 是

`{{00},{01,10},{11}}`。

它在 modular carrier 上 congruence gate 失败，但 integer-lift compiler 自动恢复 primitive normal：

`(1,1)`。

所以 safe classes 恰好是普通 integer total

`x_1+x_2`

的 fibers。

Cross action language

`{(0,1),(1,0)}`

的 safe partition 是

`{{00,11},{01},{10}}`。

它同样 modular congruence 失败，但 integer-lift compiler 自动恢复：

`(1,-1)`。

所以 safe classes 恰好是

`x_1-x_2`

的 fibers。

这修正了此前的临时解释：modular noncongruence 并不足以说明必须使用 general A4 witness state；integer lift 可能暴露一个更小、更直接的 relation coordinate。

## 6. A3 weighted relation field 就是 rank-one determinant compiler

取现有 A3 capacity vector

`m=(m_i)`

与 block-total state

`c=(c_i)`。

A3 定义：

`Z_ij=m_j c_i-m_i c_j`。

对 determinant compiler 使用一个 intra-class / basis direction `m`。对 column pair `(i,j)`：

`D_ij(c)=det([[m_i,m_j],[c_i,c_j]])`

`=m_i c_j-m_j c_i`。

因此：

`Z_ij=-D_ij`。

所以 canonical A3 weighted relation field 精确等于（差一个 sign convention）沿 capacity direction quotient total-state vector 时得到的 **rank-one exterior/determinant token**。

这不是 analogy，而是 exact reduction identity。

现有 A3 primitive field-preserving shift `m/gcd(m)` 正好是该 rank-one kernel 的 primitive integer generator；现有 A3 relation dimension `n-1` 也正好等于 ambient dimension `n` 中忘掉 one-dimensional span 后的 quotient codimension。

## 7. A3 closure 是 exterior integrability identity

A3 要求 antisymmetry 与 weighted closure：

`m_k Z_ij + m_i Z_jk + m_j Z_ki = 0`。

代入 `Z_ij=m_jc_i-m_ic_j` 后，每个 triple defect 恒等消去。

用 exterior language 表达，就是：

`m wedge (m wedge c)=0`。

所以 A3 three-block closure 不是另一个无关 pattern；它正是 decomposable rank-one exterior relation field 强制产生的 redundancy / integrability identity。

分支新增 executable bridge 检查：

- A3 upper-triangular relation coordinates 恰好是 determinant-token coordinates 的负值；
- 所有 weighted closure defects 都为零；
- A3 relation dimension 等于 rank-one quotient codimension；
- primitive capacity shifts 同时保持 A3 field 与 determinant token。

R004 不修改 A3 ownership，也不把 exterior algebra 主张为新数学；这里只建立 cross-owner structural identification。

## 8. Validation

新增 executable assets：

- `precision_integer_linear_lift_compiler.py`；
- `precision_a3_exterior_bridge.py`；
- 对应 tests。

独立验证还把 fraction-free integer rank / determinant routines 与 SymPy exact rank / determinant 在数万随机小整数 matrices 上比较，没有发现 mismatch。

对 **329** 组 primitive linear forms 生成的 finite 2D / 3D / 4D boxes，只要 induced same-class span 真达到 codimension one，compiler 都恢复正确 primitive normal（按固定 sign convention）。

Committed regressions 包括：

- coupled-AND partitions 自动恢复 `(1,1)` 与 `(1,-1)`；
- primitive normal `(1,-2,1)` 的 3D codimension-one example；
- `Z^3` 中任意 codimension line quotient 的 determinant-minor compiler；
- intra-class span 无法区分 inter-class states 时 fail closed；
- A3 exterior identity 与 weighted closure 的直接检查。

本轮不声称 fresh full-repository CI 或 Lean status。

## 9. Revised fail-closed compiler ladder

当前 compiler 在适用时应按以下顺序尝试 structured representations：

1. one axis 上直接 p-adic translation trie；
2. full product observation 下 product of axis compilers；
3. proved modular linear relation factorization；
4. additive-congruence quotient module + invariant exponent profile；
5. **integer-lift rational-linear span gate + determinant relation token**；
6. rank-one positive-capacity specialization 精确退化到 A3 weighted relation field；
7. 只有这些 gates 全部失败后，才需要 genuinely more general A3/A4 relation/witness representation。

这个顺序很重要：它防止 compiler 仅仅因为原 modular coordinates 不是合适 carrier，就过早升级到 richer state type。

## 10. Next frontier

本补充之后，真正 hard case 不再是所有 noncongruent partitions，而是同时失败以下条件的 future-safe partition：

- product factorization；
- additive congruence / module extraction；
- rational-linear lift / coset representation。

对此类 partition，项目才应该问：A3 更丰富的 weighted relation structures、A4 finite witness / correspondence structures，或者二者之间新的 verified bridge，谁提供最弱的 non-opaque state。

该 frontier 应由真实 A3/A4 owners 推进。R004 当前职责是继续提供 compiler gates、reduction identities 与 counterexamples，明确每种简单 representation 在什么地方失效。
