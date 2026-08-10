# Future 半模终止边界：有限表示不等于有限闭包

状态：`RESEARCH BRIDGE / NONCANONICAL`

共同的 future recurrence

`L_(h+1)=L_h + sum_a L_h A_a`

以及精确 plateau 证书

`L_(h+1)=L_h => 永久闭包`

可以同时出现在多种 coefficient systems 中。但这**不**表示每个有限 state/action 表示都会在有限 horizon 达到 semimodule plateau。

## 自然数系数的 sharp counterexample

取一个两状态的 0/1 relation，adjacency 为

`A=[[1,1],[0,1]]`

并取 constant natural path-count observation

`C=(1,1)`。

则

`C A^h=(1,h+1)`。

由 horizon `h` 以内 rows 生成的 `N`-semimodule 对每个 h 都严格小于下一层。原因是：所有 generator 的第一坐标都是 1；任何非负整数组合若仍要得到第一坐标 1，其系数和只能是 1，因此只能选中某一个旧 generator，不可能生成新的第二坐标。

所以，一个只有两个 raw states、一个 action 的有限世界，也可以产生无限严格增长的 reconstructive `N`-semimodule chain。

## 三种不同的“有限性”

同一个例子把三个问题严格分开。

### 1. 世界表示有限

整个 future language 由一个有限 `2x2` matrix 和一个 observation row 生成。

### 2. state-equality precision 有限完成

当前 count row `(1,1)` 合并两个 source。horizon 1 的 `(1,2)` 已经把它们区分。两状态 partition 此后不可能再继续细化。

### 3. coefficient reconstruction closure 有限完成

尽管 state identity 已完成，natural semimodule 仍然在每个 horizon 获得一个新的 irreducible generator `(1,h+1)`。

因此：有限表示、完整 state identification、有限正系数 reconstructive basis，是三个不同问题。

## Boolean 与整数 coefficient 对照

应用 coefficient map

`N -> B`, `n |-> [n>0]`。

所有 count rows 都变成 `(1,1)`，所以 Boolean reachable-support precision 永远不区分两个 source。

若改为扩张到整数 group envelope，则 `(1,1)` 与 `(1,2)` 通过减法生成 `(0,1)`，所以 `Z`-row module 在 horizon 1 已经是完整 `Z^2` 并永久闭合。

`Z` envelope 与 literal exact-count rows 具有相同的 state equality kernel，但它允许减法，所以拥有更强的 reconstruction language。负的中间 coefficient 只是分析坐标，不表示物理 path count 可以为负。

同一个有限矩阵还给出有限 recurrence：

`r_(h+2)=2 r_(h+1)-r_h`。

因此，有限 generator/recurrence 表示与“需要有限个 N-semimodule generators”同样不是一回事。

## 架构结论

为 future semantics 选择 coefficient system 后，必须分开问：

1. action / observation presentation 是否有限？
2. state-equality kernel 是否稳定？
3. 所选 coefficient-semimodule 的 reconstructive state 是否稳定？

其中一个问题有有限答案，不能自动推出另外两个也有限。

当前进取数论已出现的 coefficient specializations：

- `Z`：Noetherian module + Smith/HNF 算术闭包；
- finite modular rings：finite-index HNF closure；
- Boolean semiring：finite join-semilattice closure；
- `N`：即使 relation 有限，也不存在通用 finite semimodule plateau theorem。

这里使用的都是标准 semimodule 与 matrix recurrence 事实。项目价值在于阻止把某个 coefficient system 的终止性错误推广到另一个 coefficient system。