# Stage131 — Chain Jump Presentation 与 Storage / Inference-Depth Frontier

状态：`RESEARCH BRIDGE / NONCANONICAL`

unary-chain counterexample 已经说明：rooted circuits 是 one-round minimal-premise table，不是 globally minimal rule basis；相对于 adjacent / Hasse edges，transitive unary implications 在 closure law 上确实是 semantic redundant。

下一步真正的问题不再是 semantic，而是 operational：

> 如果允许有意缓存 derivable implications，它们究竟能购买多少 inference-depth reduction？

对 chain，这可以精确写成 finite presentation problem。

## 1. Chain law

固定：

`x_0 => x_1 => ... => x_n`。

exact closure law 是：

`x_i => x_j` 对所有 `i<j` 成立。

必须区分三个对象：

- semantic closure law；
- stored implication presentation；
- 该 presentation 下 synchronous forward-chaining depth。

不同 presentation 可以实现同一个 closure law，却有不同 storage/depth cost。

## 2. Translation-invariant jump presentation

选 jump lengths：

`L subseteq {1,...,n}`，

并要求 `1 in L`，保证全部 adjacent targets 可达。

对每个 `ell in L`，存所有合法位置上的 rule：

`x_i => x_(i+ell)`，

其中 `0<=i<=n-ell`。

这不会改变 law：每个 stored jump 都已经是 adjacent chain 的 transitive consequence，而 length1 rules 又保证原 closure 完整保留。

## 3. Exact storage law

jump length ell 恰有：

`n-ell+1`

个 source positions。

因此：

`S_n(L)=sum_(ell in L)(n-ell+1)`。

这个 positional cost 非均匀性非常重要：long jump 比 short jump 更便宜，因为可出现的位置更少。

## 4. Exact inference-depth law

从 x_0 出发，到 x_t 的 derivation path 精确对应：

`t=ell_1+...+ell_r`, `ell_i in L`。

所以 x_t 最早出现的 synchronous round，就是用 L 表示 t 所需的最少 jump 数。

记：

`lambda_L(t)=minimum coin count representing t from L`。

则：

`round(x_t)=lambda_L(t)`，

full closure depth：

`D_n(L)=max_(1<=t<=n) lambda_L(t)`。

executable layer 另外做 synchronous implication closure simulation，并与 dynamic-programming coin count 逐 state 对照。

## 5. Adjacent / Hasse endpoint

当：

`L={1}`，

有：

`S_n=n`，

`D_n=n`。

这是 chain 上 transitive-reduction 型的最小 obvious basis，也是当前最慢 endpoint。

## 6. Full transitive / rooted-circuit endpoint

当：

`L={1,2,...,n}`，

所有 transitive implications 全部存下。

于是：

`S_n=n(n+1)/2 = binom(n+1,2)`，

`D_n=1`。

这就是 one-round complete unary circuit table。

相对于 adjacent basis，它 semantic redundant，却 operationally depth-optimal。

## 7. Binary jump construction

取：

`L={1,2,4,8,...}`

直到 n。

距离 t 精确需要 `popcount(t)` 个 jumps，因此：

`D_binary(n)=floor(log2(n+1))`。

rule count：

`J(n)=sum_(d=1)^n bit_length(d)`。

若 `m=floor(log2 n)`，closed form：

`J(n)=(m+1)(n+1)+1-2^(m+1)`。

所以 binary jumps 给出一个 exact：

`O(n log n) storage / O(log n) inference-depth`

中间 construction。

## 8. Binary 并不 generically Pareto-optimal

由于 jump lengths 的 positional cost 不同，binary basis 可以被支配。

最小 sharp example：n=3。

### Binary `{1,2}`

storage：

`3+2=5`，

depth2。

### `{1,3}`

storage：

`3+1=4`，

depth2。

long jump 只在一个 source position 出现，所以反而更便宜。

因此 binary jumps 是一个 useful closed-form circuit presentation，而不是 Stage131 的 universal optimum。

## 9. General Stage131 optimization problem

在 translation-invariant jump class 内，exact design problem 是同时优化：

`S_n(L)=sum_(ell in L)(n-ell+1)`

与

`D_n(L)=max_t lambda_L(t)`，

其中 L 必须包含1。

这正是一个带非均匀 denomination cost 的 weighted additive-basis / coin-system optimization problem。

cost 来自每种 jump length 会生成多少 positional implication rules。

## 10. Exact small-chain Pareto fronts

executable layer 对 `n<=20` 枚举全部 jump sets。

Representative storage/depth frontiers：

### n=3

`(3,3), (4,2), (6,1)`。

### n=4

`(4,4), (5,3), (6,2), (10,1)`。

### n=6

`(6,6), (7,5), (8,4), (9,3), (12,2), (21,1)`。

### n=8

`(8,8), (9,7), (10,6), (11,5), (12,4), (15,3), (19,2), (36,1)`。

同一个 storage/depth pair 可能有多个不同 jump sets，所以 frontier 本身是 presentation family，不一定有唯一 canonical basis。

## 11. Two-length family 已经形成强中间 regime

取：

`L={1,q}`, `2<=q<=n`。

storage：

`S=2n-q+1`。

写：

`n=Aq+R`, `0<=R<q`，

则 full closure depth 精确为：

`D=A+max(q-2,R)`。

原因是最短表示会尽量使用 q-jump，再用 unit jumps 补余数。

选 q 在 square-root scale 附近，就可以得到 O(n)-storage / O(sqrt(n))-depth 的 regime，已经远离两个端点。

## 12. Geometric / radix jump family

对 base `b>=2`，取：

`L={1,b,b^2,...}`

直到 n。

storage：

`len(L)(n+1)-sum(L)`，

约为 `O(n log_b n)`。

Derivation depth 是 n 以内最大 base-b digit sum。

若 `n=b^m`，exact depth：

`m(b-1)`。

binary 是 b=2 specialization。更大的 b 通常用更少 jump scales，换取更大的 inference depth。

## 13. n=1024 resource landscape

同一个 chain closure law 的多个 exact presentations：

### Adjacent

- storage1024；
- depth1024。

### Best two-jump presentation

在 `{1,q}` family 中，按“先最小 depth，再最小 storage”的选择是 `q=38`：

- storage2011；
- depth62。

### Base3 geometric

- storage6082；
- depth12。

### Binary

- storage9228；
- depth10。

### Full transitive table

- storage524800；
- depth1。

这些都是 exact resource points，但不主张每一个都在 unrestricted global frontier 上。

## 14. Rooted-circuit interpretation

chain 对“redundancy”给出一个有用修正。

transitive implication 可以同时满足：

- **semantic redundant**：删掉后 closure law 不变；
- **operational useful**：存下来可以缩短 inference rounds。

rooted circuits 天然会保留许多这类 execution shortcuts，因为它按 one-round minimal premises 组织，而不是按 global rule-basis minimality 组织。

因此 global minimality 的 negative boundary 不是需要消灭的缺陷，而是暴露了 storage/execution resource axis。

## 15. Semantic basis 与 execution presentation

adjacent basis 回答：

> 这个 chain relation 最小 obvious generator / basis 是什么？

jump presentation 回答：

> 为了满足 depth/storage budget，哪些 derivable implications 值得缓存？

这是两个不同 optimization problems。

前者做 semantic compression；后者做 presentation engineering。

## 16. 与 A2/P023 presentation 路线的关系

同一架构已经出现在 exact action macros：

- generator transitions 最小化 primitive stored law；
- precomputed macros 用 storage 换 execution depth；
- binary-power circuit 能击穿 flat macro table frontier。

Stage131 chain jumps 就是 implication-rule 版本的 presentation theory。

## 17. 下一数学前沿

finite chain problem 现在可以继续引入：

- additive bases / restricted coin systems；
- ordered DAG shortcut / spanner design；
- circuit / DAG sharing；
- source-dependent nonuniform jump sets；
- 非“每 rule cost=1”的 weighted storage；
- nonuniform query distribution 下的 expected depth；
- 超越 unary chain 的 multi-premise Horn / closure systems。

binary construction 是 bridge，不是 endpoint。

## Owner-local assets

- `src/enterprise_math/stage131_chain_jump_presentation.py`；
- `tests/test_stage131_chain_jump_presentation.py`；
- `docs/STAGE131_CHAIN_JUMP_PRESENTATION_PARETO.{en,zh}.md`。

## Prior art / status

Transitive reduction/closure、shortcutting、graph spanner、coin system 与 additive basis 都是标准既有数学/CS。Enterprise Math 的 Stage131 解释是：

> **closure-law basis 与 execution-efficient rule presentation 是不同对象；semantic redundant 的 transitive rules 可以成为可控的 storage/inference-depth resource。**

不声明 repository strict CI、`EXECUTABLE_CHECKED` 或 canonical。Hard block: `NONE`。