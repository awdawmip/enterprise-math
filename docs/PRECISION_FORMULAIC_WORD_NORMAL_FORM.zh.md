# Formulaic Word Algebra 与 Tabulated Semantic Monoid

状态：`RESEARCH BRIDGE / NONCANONICAL`

Researcher-ID：`R-8F3K`

Finite transformation-monoid theorem 可以把 literal words 压成 semantic effects，但 generic implementation 仍然要存 `m x m` Cayley table 与 `m x n` effect-action table。

这些 table 并不是 fundamental lower bound。一个很大的 exact monoid 仍然可能拥有极短的 **formulaic presentation**，multiplication 与 state action 都可以直接计算。

Commuting-idempotent bitmask family 给出一个 sharp executable witness。

## 1. Commuting idempotent generators

取 k 个 generators 与 k-bit mask states：

`X={0,...,2^k-1}`。

Generator i 的作用是：

`x -> x OR 2^i`。

每个 generator 都 idempotent，且所有 generators 两两 commute。

## 2. Exact literal-word normal form

对 word w 定义：

`nu(w)=w 中出现过的 generator one-hot bits 的 OR`。

则 induced transformation 精确为：

`x -> x OR nu(w)`。

因此：

`nu(uv)=nu(u) OR nu(v)`。

Normal form 与 action order 无关，重复 generator 会自动消失。

## 3. Exact semantic monoid size

任意 mask 都可以由恰好包含该 subset generators 的 word 实现。

因此 generated transformation monoid 精确有：

`m=2^k`

个 elements。

State set 同样有：

`n=2^k`。

所以这不是“小 monoid”例子。Semantic effect family 本身已经对 generator count 指数增长。

## 4. Generic table cost 是 4^k

Generic finite-monoid implementation 会存：

- Cayley multiplication table：`m^2=4^k` effect-ID entries；
- effect action table on fine states：`m*n=4^k` state-ID entries。

所以两张 generic semantic tables 都比单个 effect 的 k-bit parameterization 指数更大。

## 5. Formulaic representation 同时消掉两张表

把 state 与 effect 都表示成 k-bit mask。

于是：

- normal-form multiplication 就是 bitwise OR；
- effect application to state 也是同一个 bitwise OR；
- generator metadata 只需把 k 个 action names 映到 k 个 bit positions。

不再需要 Cayley table，也不再需要 effect-action table。

因此这个 exact `2^k`-element monoid 只需要一种 k-bit data type 加一条 closed operation law。

## 6. Effect representation 达到 information lower bound

Semantic effects 一共恰有 `2^k` 个，因此任何 fixed-length injective binary effect ID 至少需要 k bits。

Mask normal form 恰好使用 k bits。

所以 per-effect representation 在 information sense 已经 optimal，而且仍然直接 compositional。

巨大的 gap 不在 effect identity，而在 multiplication/action law 是 tabulated 还是 formulaic。

## 7. Horizon-dependent reachable effect count

在 word horizon H 内，一个 nonidentity effect 可达，当且仅当其 support subset size 不超过 H。

所以：

`N_nonid(k,H)=sum_(j=1)^min(k,H) C(k,j)`。

包括 identity：

`N(k,H)=1+N_nonid(k,H)`。

当 `H>=k` 后，全部 `2^k` semantic effects 已经出现，effect count 永久 saturation；但 literal word count 仍会继续按 `sum k^i` 增长。

## 8. Parallel formulaic normalization

长度 H 的 word 对应 H 个 one-hot masks。用 balanced OR tree reduce。

Normalization depth：

`ceil(log2 H)`。

再把 resulting mask OR 到 state，增加1 round。

Total depth：

`ceil(log2 H)+1`。

这与 generic full-Cayley parallel normalizer 的 depth 完全相同，却不需要 `4^k` Cayley storage。

## 9. Bit-level work law

Balanced reduction 使用 H-1 个 word-level OR gates。

若一条 k-bit OR 视为 k 个 independent bit operations，则：

`normalization bit work = k*(H-1)`。

State application 再需要 k 个 bit ORs，所以：

`total bit work = k*H`。

因此 formulaic representation 把 table memory 换成 runtime circuit work：

- algebra storage：O(k) schema / metadata + k-bit values；
- total work：O(kH)；
- parallel depth：O(log H)。

## 10. Sharp k=5, H=20 resource comparison

取 k=5。

此时：

`n=m=32`。

Generic semantic tables：

- Cayley cells：1024；
- effect-action cells：1024。

H=20 的 literal word index 有：

`sum_(i=1)^20 5^i`

个 entries，远大于 `10^10`。

Formulaic route：

- normal form width：5 bits；
- generator metadata：5 个 positions；
- parallel normalization depth：5；
- normalization+application total depth：6；
- total bit work：100 个 primitive bit ORs。

同一个 exact law 的不同 representations 可以在不改变 semantic precision 的情况下出现数量级巨大的 storage 差异。

## 11. Formulaic complexity 与 monoid cardinality 独立

该 family 证明：

`large exact operation set`

并不推出

`large operation-law table`。

Monoid cardinality 衡量有多少 semantic operations；formula / presentation complexity 衡量这些 operations 的 composition 与 action 有多难表示。

这是不同的 precision resources。

## 12. Table complexity 与 presentation complexity

当前 representation ladder 又多一条轴：

### Tabulated algebra

显式存 arbitrary operation products。成本随 semantic element 数增长。

### Formulaic algebra

只存 parameters 加 closed composition formula。成本可以随 parameter dimension 增长，而不是随 monoid cardinality 增长。

因此正确的 resource question 不只是：

`exact operations 有多少个？`

还包括：

`这些 operations 最小的 exact compositional presentation 是什么？`

## 13. 与 P024 的关系

P024 的 guarded translation profile `(T,H)` 已经展示同一 architecture phenomenon，而且其 parameterized monoid 可以是 infinite：closed max-plus-style product 直接表示 exact guarded word semantics，无需枚举 literal words 或所有 operation elements。

Bitmask family 则提供 finite、完全 executable 的 sharp witness，其中 table-vs-formula storage gap 可以精确按指数计算。

## 14. Stage131 consequence

Stage131 的 resource axis 现在至少有三层：

1. literal consequence caching —— precompute words/rules vs runtime composition；
2. semantic quotienting —— 合并 exact operation 相同的 literal words；
3. algebra presentation —— tabulate semantic multiplication vs compact formula/circuit。

每一层都可以在保持同一个 exact future law 的情况下改变 storage 与 execution depth。

因此单纯“rule count”不是 relation-law precision 的充分 complexity measure。

## 15. Scope boundary

本 owner 利用特殊的 commuting-idempotent semilattice law，不声称所有 finite monoid 都有同样紧凑的 formulaic presentation。

寻找最小 exact algebraic / circuit presentation，或证明其 lower bound，是另一类 complexity problem。若没有更紧凑结构，generic Cayley table 仍然是 universal fallback。

## Owner-local assets

- `src/enterprise_math/formulaic_idempotent_word_normal_form.py`；
- `src/enterprise_math/formulaic_normal_form_work_depth.py`；
- 对应 tests；
- 本双语 theorem note。

## Prior-art / status

Semilattice、commuting idempotent、bitmask normal form 与 circuit work/depth 都是标准既有 algebra / CS。P023/A2 保留 future-signature / precision ownership。本文只拥有 formulaic-vs-tabulated future-law representation specialization。

无 repository strict CI、无 `EXECUTABLE_CHECKED`、无 canonical claim。`CI_NOT_REQUIRED_FOR_RESEARCH`。Hard block：`NONE`。
