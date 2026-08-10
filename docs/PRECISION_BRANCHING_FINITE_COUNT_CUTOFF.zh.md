# Exact Count-Branching State 的有限 Arithmetic Cutoff

状态：`RESEARCH BRIDGE / NONCANONICAL`

有限 multivalued relation 可以产生任意长的 future words，但如果目标是直接执行它的 **count-sensitive branching state**，所需的 exact natural-number coefficient precision 其实存在统一有限上界。

真正控制这个 cutoff 的不是 path-count growth，而是 raw one-step successor 的最大数量。

## 1. Maximum raw outdegree

对有限 labelled relation family 定义：

`Delta = max_(action a, source x) |R_a(x)|`。

任意 current quotient partition E、任意 target E-class C，一轮 weighted refinement 使用的 exact natural coefficient 都是：

`n_(a,x,C)=#{y in C : x R_a y}`。

始终有：

`0 <= n_(a,x,C) <= Delta`。

无论已经进行多少轮 refinement，这个范围都不会改变。

## 2. Finite modular reflection theorem

任选 modulus M 满足：

`M > Delta`。

Reduction modulo M 在整个实际 coefficient interval

`{0,1,...,Delta}`

上 injective。

因此，对**任意 current partition**：

两个 sources 的 exact-N target-block weight vectors 相同，当且仅当它们的 mod-M weight vectors 相同。

所以一轮 exact-N refinement 与一轮 mod-M refinement 完全相同。

从同一个 initial observation partition 出发归纳得到：

`E_h^N = E_h^(mod M)`

对所有 refinement depths h 都成立。

最终 stable infinite branching quotients 也完全相同。

## 3. Uniform exact cutoff

因此可以取 canonical guaranteed modulus：

`M_safe=max(2,Delta+1)`。

这个 modulus 会精确重现：

- 每一个中间 count-branching partition；
- exact stabilization round；
- final exact natural-count branching state quotient。

它与以下因素无关：

- future word horizon；
- raw relation 中是否有 cycles；
- accumulated path-count magnitude。

它只依赖 one-step raw branching degree。

## 4. Worst-case sharpness

条件 `M>Delta` 对“所有 outdegree <=Delta 的 relation worlds”这个 uniform theorem 来说是 optimal 的。

固定任意：

`2 <= M <= Delta`。

构造两个 same-observation sources x,y：

- x 没有 successors；
- y 恰好有 M 个不同 successors；
- 这 M 个 successors 当前全部落在同一个 behavioural class。

Exact-N refinement 看到：

`0` versus `M`，

所以拆开 x/y。

mod-M refinement 看到：

`0` versus `0`，

所以合并 x/y。

若 `Delta>M`，再加一个 observation-isolated source，让它拥有恰好 Delta 个 successors，即可把世界的 actual maximum outdegree 提高到 Delta，而不影响原先 x/y 的 collision。

因此任何 `M<=Delta` 都不可能成为该 outdegree budget 下的 universal all-world cutoff。

## 5. 固定 relation 可能需要更小 modulus

`Delta+1` 是 uniform worst-case certificate，并不一定是某个固定 world 的最小 modulus。

具体 relation / observation 可能根本不会出现 critical coefficient collision；或者 current observation 已经提前拆开相关 states。

由于 `Delta+1` 保证有效，一个 finite system 的 least exact branching modulus 可以有限搜索：

`M=2,3,...,max(2,Delta+1)`。

Executable branch 返回第一个使**完整 refinement sequence**与 exact N 完全一致的 modulus，而不是只比较 final partition。

## 6. 为什么这不与 unbounded path counts 矛盾

Count-branching state 保存的是 successor behavioural types 的**局部 multiplicity**。

即使 future depth 很深，一个 source/action 仍然只有原始 one-step successor set，所以每个 coefficient 始终不超过 Delta。

Terminal path-count traces 不同。长度 h 的 word 可以每一步继续 branching，因此总 path 数有粗上界：

`total paths <= Delta^h`。

于是若想直接反射 horizon h 内**全部 exact terminal path counts**，一个简单 universal coefficient bound 是：

`M > max(1,Delta^h)`。

这个 sufficient bound 随 h 增长，而 branching-state cutoff 始终只是 `Delta+1`。

这直接表现了 compositional state 与 accumulated trace value 的 arithmetic resource difference。

## 7. Sharp fixed-world branching-versus-trace gap

取 `Delta=2`，于是 exact branching cutoff 是：

`M_safe=3`。

只有一个 action a，observation constant。

Sources p,q 都有两个 first-step successors。

对 p：

- children 为 u1,u2；
- 每个 child 都有两个 terminal successors。

对 q：

- children 为 v1,v0；
- v1 有一个 terminal successor；
- v0 没有 successor。

因此 exact total path counts 为：

| word | p | q |
|---|---:|---:|
| empty | 1 | 1 |
| a | 2 | 2 |
| a^2 | 4 | 1 |
| a^k, k>=3 | 0 | 0 |

Exact terminal count traces 在 `a^2` 处拆开 p/q。

但 modulo3：

`4 == 1`，

所以这个 acyclic fixture 的全部 modular terminal trace language 永远合并 p/q。

然而 mod3 branching 已经 exact：depth1 会拆开 outdegree 2、1、0 的 child behavioural types；到了 depth2：

- p -> 两个 degree-2 child types；
- q -> 一个 degree-1 + 一个 degree-0 child type。

因此 mod3 count-branching state 与 exact N branching 完全相同，而 mod3 terminal path-count trace 仍然严格太粗。

## 8. Finite-horizon terminal trace theorem

对 maximum outdegree Delta 与 word horizon h，任意 terminal observation count 都位于：

`[0,max(1,Delta^h)]`。

因此任意：

`M > max(1,Delta^h)`

都会反射 horizon h 内所有 exact natural terminal count coefficients，使完整 exact-N 与 mod-M terminal trace partitions 完全相同。

这是 safe universal bound，不主张对固定 relation 最小。

## 9. State 与 value 的 arithmetic precision 不同

同一个 raw finite world 因而存在两种不同的 arithmetic requirement。

### Exact compositional branching state

只需要足以区分 local successor counts：

`M > Delta`。

### Horizon h 内 exact accumulated terminal count values

简单 universal reflection bound 则是：

`M > Delta^h`。

前者 horizon-independent，因为 state 递归保存 structure。

后者把 structure flatten 成持续增长的 accumulated scalar / count vector。

因此，一个 structurally richer state 反而可能需要**更少的 numeric magnitude precision**，而一个 structurally poorer aggregate trace representation 需要更大的 arithmetic range。

## 10. Semantic-precision consequence

这是又一个 non-scalar precision tradeoff：

- branching representation 在 structure 上更丰富；
- 但很小的 coefficient modulus 就能 exact；
- trace representation 在 structure 上更粗；
- 但 exact trace values 可能需要更大的 arithmetic range。

只有先声明 future interface，才可能讨论“structure”与“coefficient bits”之间是否能互换；两者没有一个 global dominance order。

## 11. Prior-art boundary

Finite equitable partition、modular injectivity、branching degree bounds 与 path-count growth 都是标准既有数学 / CS。A4 保留 raw relation / witness ownership；P023/A2 保留 future-signature precision ownership。

这里的项目价值是 exact resource separation：

> **finite count-branching state 拥有 sharp、horizon-independent coefficient cutoff `Delta+1`；即使 exact terminal path-count values 所需 precision 会随 future horizon 增长。**