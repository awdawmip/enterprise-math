# 有限 Modular Observation Ceiling

状态：`RESEARCH BRIDGE / NONCANONICAL`

一组有限 modular observations 其实只有一个精确的联合算术精度上限。

## 1. LCM 就是联合有限精度

设有限非空模数族为

`M_family={M_1,...,M_k}`，

并令

`D=lcm(M_1,...,M_k)`。

对整数 z,z'：

`z == z' mod 每个 M_i`

当且仅当

`z == z' mod D`。

因此，全部已声明有限 modular observations 的 tuple，在 equality precision 上精确等价于一次 mod-D observation。多个模数可以分别读取不同 prime-power 方向，但它们的共同 refinement 只是 lcm，仍然是一个有限精度。

## 2. 整数模型数据形成 mod-D lift fiber

考虑一个 total integer linear / affine model，其 actions、observations、offsets 与其他代数参数全部是整数数据。把所有数据逐项约到 mod D。

任意两个拥有相同 mod-D 数据的 exact integer lifts，在任何对应的有限 action word 下，其输出都仍然 mod D 同余，因为整数加法和乘法保持 congruence。因此它们在所有 `M_i|D` 的测试下也永久相同。

对已声明的有限 modular experiment family 来说，同一个 mod-D data fiber 内的所有 exact lifts 都 operationally indistinguishable。

## 3. exact property 的可识别性必要条件

设 P 是底层整数模型数据的某个 exact property，例如：

- hidden free rank；
- Smith torsion；
- exact target reachability；
- unimodularity；
- exact action algebra；
- 其他 exact integer invariant。

若想仅凭这组有限 modular experiments 认证 P，一个必要条件是：

> **P 必须在所有与实验一致的 admissible mod-D lift fibers 上保持常值。**

只要存在两个 integer lifts，拥有完全相同的 mod-D 数据却具有不同 P，那么无论执行多少对应的 finite action words，都不可能只靠这组有限模数把它们区分。

这是一条确定性的 identifiability 结论，不是统计能力不足。

## 4. FIBER no-go 是 lift-fiber 的一个实例

对任意有限模数族及其 lcm D，比较

`diag(1,0)`

与

`diag(1,D)`。

它们在每个 `M_i` 下完全相同，但 exact integer structure 不同：

- 第一个有一个 free hidden direction；
- 第二个 rational rank 已满，只剩有限 Smith torsion D。

因此有限 modular tests 不能认证一个持续不可见方向真的是 free，而不是更深的 finite torsion lift。

## 5. IMAGE no-go 是另一个 lift-fiber 实例

取同一个 scalar coefficient

`q=D+1`，

比较 targets

`b_reach=q`，

`b_bad=q+D`。

exact equation `q x=q` 可达，而 `q x=q+D` 不可达。但两个 target 在所有 `M_i` 下相同，因此全部 modular equations 及其 solution sets 都在所有已声明测试中一致。

所以有限 modular tests 同样不能认证 exact integer target reachability。

## 6. 只增加 future depth 不能突破 coefficient ceiling

如果两个 total integer dynamic models 的全部 action / observation / offset 数据已经在 mod D 下同余，那么执行更长的对应 action words 也无法逃出这个 coefficient quotient；所有 future outputs 都会继续保持 mod D 同余。

因此 future depth 与 arithmetic precision 是两个不同资源：

- 更长 word 可以激活当前 coefficient world 里已经存在但尚未暴露的差异；
- 若完整 model data 在 mod D 下已经相同，仅靠增加 future depth 无法恢复被 mod-D quotient 消掉的整数信息。

要打破这种 lift ambiguity，必须提高 coefficient precision、加入 non-modular / exact 信息，或引入一个独立 bound 限制 admissible lifts。

## 7. 扩展有限实验族

新增 modulus N 时，联合 ceiling 只会按

`D -> lcm(D,N)`

变化。

若 `N|D`，它不增加任何新的 equality precision。

若 N 不整除 D，ceiling 在 divisibility lattice 中严格变细。某个原先不可见的 exact lift difference，恰好在新的 lcm 不再 annihilate 该差异时变得可见。

在没有独立有限上界的情况下，任何固定有限 modular family 都不等于 exact integer access。exact equality 对应的是能够通过所有 modular refinements，而不是某一个固定有限 modulus。

## 8. 架构结论

finite-modular ceiling 原则统一了当前多条 precision boundary：

- p-adic free-vs-deep-torsion ambiguity；
- exact IMAGE reachability 与 deeper congruence mimic；
- model-difference content 的 divisor region；
- CRT 下 prime-power refinement 的并行结构；
- modulus precision lattice 的 `meet=gcd / join=lcm`。

实际规则可以压成一句：

> **把有限 modular experiment 解释成 exact integer property 的证据前，先问该 property 是否能通过实验族的 lcm reduction 因子化；若不能，必须先构造或排除其他 integer lifts。**

这里使用的 CRT、congruence、lcm refinement 与整数多项式保持同余，都是标准既有数学。项目价值在于把它们明确组织成有限精度 identifiability 架构。