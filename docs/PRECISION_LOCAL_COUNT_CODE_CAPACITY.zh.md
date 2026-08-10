# Exact Branching Precision 的 Local Coefficient-Code Capacity

状态：`RESEARCH BRIDGE / NONCANONICAL`

Exact natural-count branching 并不要求 coefficient semiring 本身就是 natural numbers。

对 one-step outdegree 有界的 relation family，只要 declared coefficient interface 能**injectively 编码 finite local count alphabet**，就已经足够。

这给出一个完整必要且充分 theorem，并把 coefficient capability join 的 reflection power 精确量化成 local code capacity。

## 1. Semiring 的 natural count code

设 K 为 commutative semiring。Raw successor count n 通过 canonical natural map 进入 K：

`eta_K(n)=n*1_K`。

若 maximum raw outdegree 为 Delta，一轮 weighted branching refinement 实际只可能读取：

`0,1,...,Delta`。

因此 exact local count reflection 真正依赖的只是：

`eta_K | {0,...,Delta}`。

## 2. Universal exactness theorem

对所有 maximum outdegree 不超过 Delta 的 finite relation systems：

`K-branching refinement = exact N-branching refinement`

在每一轮都成立

当且仅当

`eta_K` 在 `{0,...,Delta}` 上 injective。

### Sufficiency

任意 current partition 上，每个 source-to-target-block coefficient 都位于 finite alphabet `0..Delta`。

Injectivity 意味着：K-weight vectors 相同，当且仅当 natural-count vectors 相同。

所以任意 partition 上，一轮 K-refinement 与一轮 N-refinement 完全一致。归纳以后，完整 refinement sequences 与 fixed points 都一致。

### Necessity

若有不同 `r,s<=Delta` 满足：

`eta_K(r)=eta_K(s)`，

构造两个 same-observation sources x,y，分别拥有 r 与 s 个不同 successors，并让这些 successors 当前全部处于一个 behavioural target class。

Exact N 看到不同 coefficients，会拆开 x/y。

K 看到相同 code，会合并 x/y。

因此任何 local code collision 都自动给出一个 bounded worst-case relation counterexample。

## 3. Reflection capacity

定义 K 的 universal local count capacity 为：

`eta_K` 在 `0..Delta` 上仍 injective 的最大 Delta。

这不是 semiring 的 global information capacity，而是一个 task-specific branching reflection threshold。

对于固定 world，即使 actual maximum outdegree 超过 generic capacity，只要 critical collisions 从未进入 future-relevant configuration，仍可能 realized exact。

## 4. Boolean support capacity

对 Boolean OR/AND：

`eta_B(0)=0`，

而所有 `n>=1` 都满足：

`eta_B(n)=1`。

所以：

`capacity(B)=1`。

Boolean support 对每个 source/action 最多一个 successor 的 deterministic / partial branching 是 universally exact；一旦 outdegree 可以到2，就 generic 地丢 multiplicity。

这正好恢复 branching-support route 的 deterministic-collapse boundary。

## 5. Modular count capacity

对 `K=Z/MZ`：

`eta_K(n)=n mod M`。

`0,...,M-1` 互不相同，而 M 第一次与0 collision。

因此：

`capacity(Z/MZ)=M-1`。

此前 finite modular cutoff theorem `M>Delta`，精确等价于：

`Delta <= capacity(Z/MZ)`。

## 6. Boolean × modular synergy

取：

`K=B x Z/MZ`。

Natural code 为：

`n -> ([n>0], n mod M)`。

这时 count M 不再与0 collision：

- 0 -> `(0,0)`；
- M -> `(1,0)`。

第一组新 collision 变成：

`1` versus `M+1`，

二者都映到 `(1,1)`。

所以：

`capacity(B x Z/MZ)=M`。

Boolean support 精确把 pure modular precision 的 universal count range 再向上扩一层。

这是 genuine capability synergy：joint interface 能反射一个比任一单独 channel 更大的 local exact world。

## 7. Sharp support + parity example

对 M=2：

| count | support | parity | pair |
|---|---:|---:|---:|
| 0 | 0 | 0 | (0,0) |
| 1 | 1 | 1 | (1,1) |
| 2 | 1 | 0 | (1,0) |
| 3 | 1 | 1 | (1,1) |

Boolean alone 的 capacity=1。

Parity alone 的 capacity=1。

二者 together 的 capacity=2。

Owner regression 会穷举 two-state set 上全部 relation pairs，在 constant / identity observations 下验证：coupled Boolean×parity branching 在 full outdegree2 bound 上与 exact N 完全一致。

到了 outdegree3，count1 与3 立即给出 sharp failure。

## 8. Finite modular families 通过 lcm 组合

对 moduli `M_1,...,M_k`，product natural code 就是 tuple：

`(n mod M_1,...,n mod M_k)`。

两个 natural numbers 拥有相同 tuple，当且仅当它们 modulo

`L=lcm(M_1,...,M_k)`

同余。

因此：

`capacity(product_i Z/M_iZ)=L-1`。

这正是 modular coefficient join theorem 的 local-count 版本。

若再加 Boolean support：

`capacity(B x product_i Z/M_iZ)=L`。

原因相同：support 能拆开0与第一个 positive multiple L，而1与 `L+1` 仍是下一组 sharp collision。

## 9. Coefficient capability join 会增加 reflection power

所以 semantic capability join 不只是把两个 labels 放在一起。

当 channels 被保留成一个**coupled compositional coefficient interface** 时，它们的 joint code 可以区分任一单独 channel 都无法区分的 local exact values。

这与 independent readout join 不同：

- independent readout 只保证两个 completed answers 分别可读；
- coupled product 会在每个 current target class 上保留 joint local code，并支持 recursive execution。

Capacity theorem 属于后者。

## 10. Capacity synergy 与 compositional debt 是两种不同现象

两个 coefficient interfaces 至少可以有两种 interaction。

### Reflection synergy

Joint natural code 比任一单独 code 在 local count alphabet 上更 injective。

例：Boolean + parity。

### Compositional closure debt

即使两个 final interface labels 分别已经 available，它们的 ordinary state join 也可能重新变 transition-unsafe，需要额外 refinement。

两者逻辑不同：

- capacity 讨论**一个 target block 上的 value reflection**；
- debt 讨论**target partition 被跨 capability refine 后的 continuation safety**。

一个 representation family 可能有其中任意一种、两种都有、或两种都没有。

## 11. Worst-case collision compiler

对任意 semiring K 与 degree bound Delta，executable layer 会在 finite local alphabet 上搜索第一组 code collision：

`r<s<=Delta`, `eta_K(r)=eta_K(s)`。

若存在，就自动构造 relation world，使 exact natural counts 在第一轮 precisely 区分 r versus s，而 K 把它们合并。

因此 injectivity criterion 的每次 failure 都能转成一个 concrete bounded A4 witness。

## 12. Relation-specific realized precision

Universal capacity 故意是 conservative 的。

固定 relation system 可能在 generic capacity 低于 actual max outdegree 时仍 exact，原因包括：

- colliding counts 从不出现在 equivalent source states 上；
- colliding target blocks 已被 observation 提前拆开；
- later future structure 让 collision 对 declared quotient 无关。

因此必须继续区分：

`universal code capacity`

与

`one world 的 realized exact precision`。

## 13. Prior-art boundary

Finite coding、CRT、semiring product 与 weighted partition refinement 都是标准既有数学 / CS。A4 保留 relation / witness ownership；P023/A2 保留 future-signature 与 semantic-precision ownership。

这里的项目价值是 exact theorem：

> **coefficient interface 对 outdegree Delta 的 count branching universally exact，当且仅当其 natural-number code 在 finite local count alphabet `0..Delta` 上 injective；coupled capability join 可以严格提高这项 reflection capacity。**