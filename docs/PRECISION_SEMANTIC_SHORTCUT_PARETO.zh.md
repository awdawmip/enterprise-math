# Semantic Shortcut Generators：Quotient-First Storage/Depth Pareto

状态：`RESEARCH BRIDGE / NONCANONICAL`

Researcher-ID：`R-8F3K`

Literal word caching 预计算的是 syntax。如果 future law 已经先 quotient 成一个更简单的 exact semantic algebra，同一 shortcut-depth 思想可以在 **semantic collapse 之后**再执行。

对 commuting-idempotent k-bit OR algebra，这会把 storage law 从 literal words 改写成 semantic subsets，而 execution-depth geometry 保持相同。

## 1. Semantic effect algebra

取 k 个 singleton semantic generators，以 bitwise OR composition。

每个 exact effect 是 k 个 primitive directions 的一个 subset mask。

Word 的 semantic effect 只取决于哪些 generator names 至少出现过一次；literal order 与 repetition 已经被 exact quotient 擦除。

## 2. Bounded-support semantic shortcuts

选 shortcut depth d，`1<=d<=k`。

把所有 support size<=d 的 nonzero semantic effects 都提升为 primitive shortcut generators。

Exact shortcut count：

`G(k,d)=sum_(i=1)^d C(k,i)`。

这正是长度<=d 的全部 nonempty literal words 在 semantic quotient 下的 image size。

## 3. Exact target geodesic

若 target effect T 的 support size 为 s，则每个 shortcut 最多加入 d 个 target bits，所以至少需要：

`ceil(s/d)`

次 applications。

反过来，把 target 的 s 个 bits 分成 size<=d 的 chunks，每个 chunk 用一个 shortcut 即可达到上界。

因此：

`dist_d(0,T)=ceil(s/d)`。

Owner 会返回 explicit optimal chunk decomposition。

## 4. Worst-case execution distance

Full mask support size=k，所以 worst-case semantic geodesic：

`R(k,d)=ceil(k/d)`。

Endpoints：

- d=1：k 个 singleton generators，worst-case distance k；
- d=k：全部 `2^k-1` nonidentity effects 都成为 primitive，worst-case distance1。

所有 intermediate d 都给出 exact shortcut-storage/runtime points。

## 5. Runtime-budget design

若 worst-case geodesic budget 是 r，则当前 bounded-support family 中 minimum shortcut depth：

`d_min=ceil(k/r)`，

当 r>=k 时 d=1。

由于 `G(k,d)` 随 d 严格增加，这个 d 同时最小化该 family 内的 shortcut count。

## 6. Pareto depth locations

Storage 随 d 严格增加，而 runtime 是 `ceil(k/d)` step function。

所以 nondominated depths 精确为：

`{ceil(k/r):r=1,...,k}`

去重后的集合。

这与 literal block-cache 在 horizon H=k 时的 depth locations 完全相同。

Semantic quotient 不改变“哪些 depth 值值得选”；它改变的是这些 Pareto points 在 storage 轴上的高度。

## 7. Literal-cache 与 semantic-shortcut storage

Literal free-word caching through depth d 要存：

`S_lit(k,d)=sum_(i=1)^d k^i`。

Semantic shortcut caching 则存：

`S_sem(k,d)=sum_(i=1)^d C(k,i)`，

其中 d<=k。

存在自然 surjection：

`literal words -> support subset masks`，

因此：

`S_sem(k,d)<=S_lit(k,d)`。

Semantic table 在真正 materialize precomputation 之前，就已经删除了 order / repetition redundancy。

## 8. Sharp storage comparisons

k=20,d=3：

`S_lit=20+400+8000=8420`，

而

`S_sem=20+190+1140=1350`。

两种对应 shortcut model 都能用：

`ceil(20/3)=7`

轮完成 full-mask execution。

k=8,d=4：

`S_lit=4680`，

而

`S_sem=162`，

full semantic mask 都可在2轮达到。

## 9. Full precomputation 的 syntax/semantics gap 最大

当 d=k：

semantic shortcut storage saturation 到：

`2^k-1`

个 nonidentity effects。

而长度<=k 的 literal word storage 是：

`sum_(i=1)^k k^i`，

随 k 增长远大于 semantic effect table。

差距正是 commuting-idempotent word quotient 删除掉的 syntax redundancy。

## 10. Cache-before-quotient 与 quotient-before-cache

只看最终 exact effect **set**，两条路径一致：

1. 先 cache 所有长度<=d literal words，再 quotient equal effects；
2. 先按 semantic equality quotient words，再 cache support size<=d 的 distinct effects。

两边都会得到同一个 `G(k,d)` semantic shortcut set。

但若第一条路径真的先 materialize literal table，再做 dedup，operational storage 会高得多。

所以 transformation order 即使不改变最终 semantic set，也会改变 representation resource cost。

## 11. 与 formulaic OR representation 的关系

前面的 formulaic-normal-form generation 还可以更进一步：根本不 table shortcut effects，而是把任意 effect 直接编码成 k-bit mask，用 OR 公式 compose。

因此 semantic shortcut table 自己也只是一个 intermediate representation：

- singleton generators + formulaic composition；
- bounded semantic shortcut table；
- full semantic effect table。

是否值得存 shortcut，取决于 future execution interface 如何给 formula work 与 table lookup 定价。

## 12. Stage131 hierarchy

Shortcut result 说明 Stage131 storage/depth 轴取决于**在哪一层 semantic object 上做 cache**。

相同 shortcut depth d 可以 precompute：

- literal syntax blocks；
- semantic effect blocks；
- 或完全不建 table，直接用 formulaic normal form。

三者都可实现同一个 exact future law，但 resource points 完全不同。

所以正确问题不只是：

`cache 有多深？`

还必须问：

`cache materialize 之前做了什么 quotient / normal form？`

## 13. Scope boundary

Exact binomial law 依赖 free commuting-idempotent semilattice on k primitive directions。

当前 bounded-support shortcut catalogue 是 canonical family，但不声称它在“所有可能 shortcut sets 中”对给定 diameter globally minimum。若只关心一个 target 或一个 task region，target-specific shortcut design 可以使用远少于 `G(k,d)` 的 effects。

## Owner-local assets

- `src/enterprise_math/semantic_shortcut_generator_pareto.py`；
- `src/enterprise_math/semantic_shortcut_frontier.py`；
- 对应 tests；
- 本双语 theorem note。

## Prior-art / status

Boolean semilattice、binomial subset count、word quotient 与 shortcut / time-memory tradeoff 都是标准既有数学 / CS。P023/A2 保留 future-signature / precision ownership。本文只拥有 quotient-first semantic shortcut Pareto specialization。

无 repository strict CI、无 `EXECUTABLE_CHECKED`、无 canonical claim。`CI_NOT_REQUIRED_FOR_RESEARCH`。Hard block：`NONE`。
