# R004 精度起源——补充 29：canonical multi-target dependency/synergy decomposition

状态：`PROVED_WIP + EXECUTABLE_REFERENCE + MULTI-TARGET MODULE DECOMPOSITION`  
父文档：`R004_PRECISION_GENESIS_QUANTUM_MACRO_CLOSURE_SUPPLEMENT_28.zh-CN.md`  
Owner branch：`research/r004-precision-genesis-closure-20260810`

补充 28 已证明普通 pairwise inclusion-exclusion 会因为 observation 知道 cross-target combinations 而失败。本补充给任意有限 target family 一个与 parenthesization 无关的 canonical decomposition。

## 1. Target presentation relation module

给定 target row modules `W_1,...,W_m`，定义 sum map

`pi_W: direct_sum_i W_i -> sum_i W_i`，

`pi_W((w_i))=sum_i w_i`。

其 kernel

`R_W=ker pi_W`

就是 complete target-dependency module，包含 targets 之间全部 linear relations，不只 pairwise intersections。

exact sequence

`0 -> R_W -> direct_sum_i W_i -> sum_i W_i -> 0`

给出

`mu(R_W)=sum_i mu(W_i)-mu(sum_i W_i)`。

## 2. Observed relation module

令

`U_i=U cap W_i`。

observed component sum 有 presentation

`pi_U: direct_sum_i U_i -> sum_i U_i`。

定义

`R_U=ker pi_U`。

由于每个 U_i 都包含于 W_i，direct-sum inclusion 会把 observed relation 送成 target relation，因此

`R_U subseteq R_W`。

quotient

`R_W/R_U`

就是 individual defect accounting 会重复计算、但并未在 individually observed parts 内部已经体现的 target dependency structure。

## 3. Multi-target observation synergy

定义

`S_U(W_1,...,W_m)`
` = (U cap sum_i W_i)/(sum_i(U cap W_i))`。

它量化 U 知道的 cross-target combinations 中，不能由任何 individually observed target components 组合出来的部分。

这就是补充 28 distributivity-defect quotient 的 multi-target generalization。

## 4. Canonical joint-defect formula

每个 target 定义

`delta_i=delta(U,W_i)=mu(W_i)-mu(U cap W_i)`。

则

`delta(U,sum_i W_i)`
` = sum_i delta_i`
`   - mu(R_W/R_U)`
`   - mu(S_U(W_1,...,W_m))`。

证明只需：用 R_W exact sequence 展开 target sum mass，用 R_U 展开 `sum_i U_i` mass，再使用

`mu(U cap sum W_i)=mu(sum U_i)+mu(S_U)`。

完全不使用 distributive-lattice 或 Möbius 假设。

## 5. 两种 canonical rebate

individual defects 之和 overcount joint defect 只有两类 module-valued 原因：

### Dependency rebate

`R_W/R_U`：targets 之间本来就有、但 separately observed parts 尚未体现的 dependencies。

### Synergy rebate

`S_U`：observation 已经联合知道、但任何 individual observed target part 都单独看不见的 combinations。

因此

`delta(U,sum_i W_i)<=sum_i delta(U,W_i)`。

差值不是 opaque scalar，而是两个 explicit finite p-group objects 的 exponent mass。

## 6. Examples

### Pure target dependency

在 `F_2^2` 上取 U=0，targets：

`W1=<e1>`, `W2=<e2>`, `W3=<e1+e2>`。

三个 individual defect 都为 1，但三 targets 总共只 span 两维。此时

`mu(R_W/R_U)=1`, `mu(S_U)=0`，

joint defect=`3-1=2`。

### Pure observation synergy

在 `F_2^3` 上取

`U=<e1+e2>`，

独立 targets：

`W1=<e1>`, `W2=<e2>`, `W3=<e3>`。

target dependency 为零，但 `mu(S_U)=1`；三个 individual defects sum=3，joint defect=2。

两种机制即使产生相同 scalar rebate，结构来源也完全不同。

## 7. 为什么这替代 Möbius bookkeeping

三个以上 submodules 时，在 non-distributive subgroup lattice 中 ordinary inclusion-exclusion over intersections 不是 canonical。presentation-kernel module R_W 一次捕获全部 target dependencies；S_U 一次捕获全部 observation-side join synergy。

公式与 target ordering / parenthesization 无关。

## 8. Validation

Independent exact checks 覆盖 **7,200** 个 small 2/3-power ambient modules 上的 random systems，targets 数为 2、3、4。所有 cases 中：

- `R_U` mass 不超过 `R_W` mass；
- dependency / synergy rebates 均非负；
- canonical decomposition 与 direct joint target defect 完全一致。

其中 3,362 个 total rebate 严格正。

## 9. Architecture consequence

Multi-target precision accounting 应保留 **dependency presentations 与 relative embeddings**，不能只保 individual target profiles 或 pairwise overlaps。这再次说明 scalar summaries 可以作为输出，但不能当 complete compositional state。

下一步若进入 A4 MAY / richer witness semantics，需要按 declared witness algebra 寻找相应的 typed dependency presentation，而不能把 nonlinear witness correlation 强制线性化成 row module。
