# R004 精度起源——补充 18：由 dissociated weight supports 得到 Arithmetic Cut Compiler

状态：`PROVED_WIP + EXECUTABLE_CHECKED + PRIOR_ART_SPECIALIZATION + STRUCTURAL_CUT_CLOSED_FORM`  
父文档：`R004_PRECISION_GENESIS_QUANTUM_MACRO_CLOSURE_SUPPLEMENT_17.zh-CN.md`  
Owner branch：`research/r004-precision-genesis-closure-20260810`

补充 16–17 已经把 obstruction 问题从 Bell-number 状态 partitions 移到 generator-side cut clutter，但 generic extraction 仍然可能需要最多 `2^|G|` 次 retained-generator compiler 调用。本补充给出第一类 arithmetic family：carrier-cut clutter 可以直接由 typed generator coordinates 的整数关系推出。

additive combinatorics 中 dissociated / subset-sum-distinct set 是成熟先行概念。R004 当前真正新增的是：在下面 weighted-observation / bit-flip compiler 中，future-language carrier cuts 恰好等于 dissociativity 失败的 support-minimal supports。

## 1. Binary weighted-observation world

设

`X={0,1}^d`。

取非零整数 weights

`a=(a_1,...,a_d)`，

当前 observable 为

`L_a(x)=sum_i a_i x_i`。

令 `P0=ker L_a`。

对每个 coordinate `i`，声明一个 total future generator `F_i`，只翻转该 bit：

`(F_i x)_i = 1-x_i`，

其余 coordinates 不变。

记 `G={F_1,...,F_d}`。

## 2. R004-COMP-T32——retained flips 的 exact quotient

对 retained coordinate set `S subseteq {1,...,d}`，定义

`q_S(x)=(L_a(x), x|_S)`。

则 `q_S` 正好是 retained flip language 的唯一最粗 future-safe quotient。

充分性：若两个 states 的 weighted observation 相同，且 retained bits 逐位相同，则任何 retained-flip word 都会从相同 bit value 出发翻转同一组 coordinates，所以所有 future weighted observations 都继续相同。

必要性：对 retained `i`，

`L_a(F_i x)-L_a(x)=a_i(1-2x_i)`。

由于 `a_i != 0`，current/future observation pair 精确确定 `x_i`。因此任何 safe quotient 都必须保留每个 retained bit 以及 `L_a(x)`。

所以

`Compile_S(P0)=ker q_S`。

这是 closed-form compiler output，不是 generic partition-refinement 结果的重命名。

## 3. R004-COMP-T33——deletion failure 等价于 subset-sum collision

令 deleted/hidden coordinate set 为 `H=G\S`。

因为 `x|_S` 已知，`q_S` 是否 injective 精确归约为 hidden subset-sum map 是否 injective：

`z in {0,1}^H -> sum_(i in H) a_i z_i`。

因此删除 `H` 会破坏 full discrete carrier，当且仅当存在两个不同 hidden binary vectors `u != v`，满足

`sum_(i in H) a_i u_i = sum_(i in H) a_i v_i`。

相减得到非零 signed relation：

`sum_(i in H) epsilon_i a_i = 0`，

其中每个

`epsilon_i in {-1,0,1}`。

反过来，任意这样的 signed relation 都可把 positive/negative supports 分成两个不同 hidden subsets，得到同和碰撞。

所以：

`H carrier-breaking <=> {a_i : i in H} 不是 subset-sum-distinct / dissociated`。

## 4. R004-COMP-T34——arithmetic carrier-cut theorem

该 future language 的 minimal carrier cuts 精确为：

`C_car = { support-minimal nonzero epsilon in {-1,0,1}^d : sum_i epsilon_i a_i = 0 }`，

每条 cut edge 就是 support：

`{i : epsilon_i != 0}`。

等价地：

`minimal carrier cuts = inclusion-minimal non-dissociated weight supports`。

因此 structural obstruction clutter 可直接从 weights 的 arithmetic dependencies 生成。只要这些 minimal signed dependencies 已知，就不需要逐个 retained subset 调 compiler。

这是补充 17 frontier 的第一条 exact realization：

`typed algebraic invariant -> exact cut clutter`。

## 5. Equal-weight closed form

若所有 weights 相等且非零：

`a_i=c`，

则任意 two-coordinate set `{i,j}` 都有 relation

`a_i-a_j=0`，

而 singleton 不可能 dependent。

因此

`C_car = [d] 的全部 2-subsets`。

cut clutter 就是 complete graph `K_d` 的 edges。

其 minimal transversals 恰好是“删去一个 coordinate”的所有 sets：

`B_C = { [d]\{i} : i in [d] }`。

所以每个 minimal Carrier Basis 的大小精确为

`d-1`。

解释：total-count observation `sum_i x_i` 已经给出一条全局 relation；只要暴露任意 `d-1` 个 coordinate bits，最后一个 bit 可由 total 恢复。

此前 two-bit coupled-observation 反例就是 `d=2` specialization：唯一 minimal cut 为 `{F_1,F_2}`，因此任一 local flip 单独都足以完成 carrier，虽然 observable 本身跨轴耦合。

## 6. Powers-of-two closed form

若

`a_i=2^(i-1)`，

所有 binary subset sums 都不同。weight family 是 dissociated，`L_a` 自身在 `{0,1}^d` 上已 injective。

因此

`C_car=empty`，

minimal Carrier Basis 是 empty instruction set。

这不表示 future flip operations 可从“什么都没有”重建；这里只说明它们对 **carrier generation** 已经不必要，因为 current observation 本身已经编码 exact state。补充 17 的 semantic adequacy 仍是独立层。

## 7. Intermediate arithmetic example

对

`a=(1,2,3)`，

唯一 inclusion-minimal subset-sum collision 是

`1+2=3`。

所以

`C_car={{1,2,3}}`。

任何单个 retained flip 都是 minimal Carrier Basis：暴露任意一个 bit 后，剩余两个 hidden weights 的 subset sums 都 unique。

这与 equal weights `(1,1,1)` 完全不同：后者存在全部 three 2-coordinate cuts，因此每个 Carrier Basis 大小为 2。

所以 instruction complexity 由 observation weights 的 arithmetic dependency structure 决定，而不是由 dimension 单独决定。

## 8. Exact validation

独立验证覆盖所有 positive weight vectors：

`a_i in {1,2,3,4,5}`，

且 `1<=d<=4`，总计 **780** 个 weight systems。

每个 system 都验证：

1. full flip language 编译为 discrete partition；
2. compiler-derived minimal deletion cuts 与 inclusion-minimal non-dissociated supports 完全相同。

零 violation。

更强的 all-retained-subset 核对，在同一 family 中对每个 retained `S` 比较 iterative compiler 与 closed form：

`ker(x -> (L_a(x),x|_S))`。

共 **11,110** 个 quotient cases，0 mismatch。

Executable reference：

`src/enterprise_math/precision_arithmetic_cut_compiler.py`

Direct regressions：

`tests/test_precision_arithmetic_cut_compiler.py`。

不主张 fresh full-repository CI 或 canonical-main status。

## 9. Prior-art 边界

subset-sum-distinct / dissociated sets，以及“没有非平凡 `{-1,0,1}` relation”的等价定义，都是成熟 additive-combinatorics notions。source mapping 记录在：

`docs/PRIOR_ART_R004_ARITHMETIC_CUT_COMPILER.*`

和

`sources_r004_arithmetic_cut_compiler.json`。

R004 不把 dissociated-set theory 或 subset-sum uniqueness 宣称为新发明。

项目级 theorem 是 compiler bridge：

`weighted observation + coordinate flips -> retained quotient (L_a,x|_S) -> carrier cuts = minimal non-dissociated supports`。

该 Enterprise Math specialization 的历史 novelty 仍为 `NOVELTY_UNVERIFIED`。

## 10. 架构后果

obstruction compiler 现在有两种模式：

Generic：

`typed compiler oracle -> minimal deletion cuts -> transversal basis`。

Arithmetic closed form：

`typed integer weights -> support-minimal signed relations -> cut clutter -> transversal basis`。

这是第一次证明：`C_joint/C_car` 在某些 typed family 中可以直接由 algebraic invariant 生成，而不需要枚举所有 retained generator subsets。

## 11. 下一 frontier

自然的下一步是寻找其他 typed families 的 algebraic cut closed forms：

- quotient-module generators -> support-minimal module relations / invariant-factor defects；
- A3 determinant/exterior relation state -> minimal rank-loss supports；
- guard-image lattices -> 会降低 reachable guard-image rank 或 orthant support 的 minimal generator deletions；
- prime-axis/exponent languages -> 会摧毁 required arithmetic axes 的 minimal support deletions。

目标不是发明 universal combinatorial algorithm，而是建立 Enterprise Math typed future-language families 的 exact algebraic cut compiler atlas。
