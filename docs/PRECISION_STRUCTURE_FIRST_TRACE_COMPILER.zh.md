# 从 Small Local Precision 编译 Exact Infinite Trace 的 Structure-First 路线

状态：`RESEARCH BRIDGE / NONCANONICAL`

有限 relation system 至少有两条 exact 路线可以得到 natural path-count trace semantics。

一条路线直接观察越来越大的 accumulated counts；另一条路线保留足够的 branching structure，使**很小的 local counts 先被 exact 反射**，随后在恢复出的 weighted machine 内部推导任意大的 future counts。

第二条路线给出一个重要 precision principle：

> 如果 state 保留了生成这些数值的 compositional structure，那么很大的 derived values 并不一定要求同样大的 observational coefficient range。

## 1. Exact count-stable branching quotient

设 E 为 stable natural-count branching equivalence。

对每个 action a、source E-class D 与 target E-class C 定义：

`B_a[C,D] = #{ y in C : x R_a y }`，

其中 `x in D` 为任意 representative。

Count-stability 保证这个数字与 representative 无关。

因此每个 raw relation action 都能 descend 成 quotient classes 上的 integer weighted transition matrix B_a。

这个 quotient 不只是 observation label；它是一个 exact executable weighted machine。

## 2. Exact path-count 会穿过 weighted quotient

从 raw source state x 及其 quotient class D 出发。

一步 action 后，B_a 精确给出 x 的 raw successors 分别落入每个 quotient class 的数量。

假设某个 quotient count vector 已经精确表示当前所有 raw paths 在各 classes 中的数量。乘下一步 weighted matrix 时，会把：

`当前到达 old class 的 path 数`

乘以

`该 class 任意 representative 到 new class 的 raw successor 数`，

然后对 old classes 求和。

由于 successor counts representative-independent，归纳得到：对任意 literal word w，

`raw paths 按 quotient / observation class 的 counts`

精确等于

`weighted quotient matrix execution`。

Owner branch 还有一个独立 oracle，会在 tiny relation families 上逐 literal word 对比 raw dynamic-programming trace 与 quotient matrix execution。

## 3. Small modular branching precision 可以恢复 exact weighted machine

令：

`Delta=max raw outdegree`。

Finite count-branching cutoff theorem 已证明任意：

`M>Delta`

都会得到与 natural counts 完全相同的 branching refinement sequence 与 final partition。

在 final partition 上，每个 local target-block weight 都是：

`0..Delta`

中的一个整数。

它的 mod-M residue 因而在这个 interval 中只有唯一 lift。

所以只要 `M>Delta`，mod-M branching representation 就能确定：

- exact natural count-stable state partition；
- 每个 exact integer quotient transition weight；
- 因而整个 exact weighted quotient machine。

识别这些 local laws 不需要更大的 arithmetic observation。

## 4. 之后可以内部生成 exact infinite traces

Exact integer quotient matrices B_a 一旦恢复，future path counts 就可以通过 ordinary exact integer matrix multiplication 生成。

这些 derived integers 可能远大于 M。

这不与 observational cutoff 矛盾，因为 M 只负责识别**local one-step coefficients**，而这些 coefficients 全部有先验 bound Delta。

更大的数值是已经恢复出的 exact machine 的 deterministic consequences，不是新的 hidden measurements。

因此：

`small local coefficient precision + compositional structure`

可以生成：

`unbounded derived exact count values`。

## 5. Trace-equivalence closure 可以在 quotient dimension 上运行

记：

`b=#(exact count-branching classes)`。

Weighted quotient 只有 b 个 states。由于 branching quotient refine original observation，current observation 在每个 branching class 上 constant。

在 b-dimensional weighted matrices 上运行 rational terminal-trace row-space closure。

若 observation 有 `c_0` 个 independent classes，则 quotient trace closure 最迟在：

`b-c_0`

层停止，而 raw-state theorem bound 是：

`n-c_0`。

所以 exact branching minimization 可以同时降低：

- arithmetic observation range；
- linear trace-analysis dimension / horizon。

## 6. Pullback 恢复 raw infinite trace partition

Quotient rational closure 最终得到 branching quotient classes 之间的 terminal-trace equivalence。

沿

`raw state -> count-branching class`

把这个 partition pull back。

因为所有 raw word counts 都精确 factor through weighted quotient，这个 pullback 就等于 raw infinite exact natural terminal-trace partition。

Executable compiler 会直接把两者与独立 raw rational-trace compiler 对照并 assert equality。

## 7. Twenty-to-two dimension-collapse witness

取二十个 raw states：

- 十个 `a_i`，每个都有一个 successor 指向某个 terminal-type state；
- 十个 `b_j`，全部没有 successor；
- present observation constant。

Raw state count：

`n=20`。

Exact count branching 只有两个 classes：

- 全部 `a_i`；
- 全部 `b_j`。

因此：

`b=2`, `Delta=1`。

### Raw theorem bound

Current observation 只有一个 class，generic raw trace dimension bound 是：

`n-c_0=19`。

### Structure-first quotient

因为 `2>Delta`，mod2 已经 exact。

恢复出的 weighted quotient 只有两个 states，其 trace closure bound 为：

`b-c_0=1`。

并且实际恰好一层停止。

所以 structural quotient 把一个 nominal 20-state trace analysis 压成 two-state weighted machine，同时 local count precision 只需要一 bit。

## 8. 固定 branching-versus-trace witness

对此前 Delta=2 的 world：

- mod3 已 exactize branching structure；
- direct mod3 terminal traces 因为 `4==1 mod3` 而错误；
- structure-first mod3 会先恢复 exact local quotient matrices；
- quotient execution 随后生成 exact integer path totals 4 与1；
- rational quotient analysis 最终恢复 exact infinite trace partition。

所以**同一份 mod3 data 作为 flattened terminal trace 不够，但作为 structured branching machine state 已经足够**。

这是“precision 不能只由 modulus 分类”的最直接 proof。

## 9. Direct-trace route 与 structure-first route

### Direct trace observation

若要直接反射 closure horizon h 以内的全部 terminal counts，safe modulus 是：

`M > Delta^h`。

Representation 几乎不保留 branching structure，而要求 coefficient channel 直接承载 accumulated value。

### Structure-first route

只用：

`M > Delta`

恢复 exact weighted branching quotient，然后在 quotient 内部用 exact arithmetic 计算任意 future counts。

Representation 保留更多 compositional structure，所以 observational arithmetic range 可以更小。

这两条都是 exact 路线，只是 precision resources 的分配方式不同。

## 10. 这不是从 lossy residue 凭空得到 exact arithmetic

从 mod M 唯一 lift 回 exact local count，依赖显式先验 bound：

`0 <= local count <= Delta < M`。

若没有这个 bound，一个 residue 当然不能唯一决定 integer lift。

所以这个 compiler 完全遵守此前已经建立的 reflection architecture：

`quotient value + independent finite bound -> exact local reflection`。

新的部分是：一旦**local law**被 exact 反射，compositional structure 就能把它传播成 unbounded future derived values。

## 11. 与 Markov / state sufficiency 的关系

Weighted branching quotient 是 count-valued relation interface 的 sufficient continuation state。

Terminal trace value 只是这个 state 在某个 word 下输出的一个 answer。

把 machine flatten 成 outputs 会减少 structural state，却可能让这些 outputs 的 numeric range 变大。

这再次精确实现项目原则：

> sufficient state 与 sufficient answer 是不同对象。

## 12. Prior-art boundary

Equitable partition、weighted lumping、quotient automaton、integer matrix path counting 与 observability reduction 都是标准既有数学 / CS。A4 保留 relation / witness ownership；P023/A2 保留 future-signature 与 precision ownership。

这里的项目价值是 exact compiler / resource theorem：

> **modulus `Delta+1` 加上 exact branching structure，就足以恢复 weighted quotient，并由此生成完整 infinite exact natural path-count language；即使同样小的 modulus 作为 flattened terminal count trace 仍然不足。**