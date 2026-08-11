# Prefix-Observable Word Semantics 与 Terminal Operation Effects

状态：`RESEARCH BRIDGE / NONCANONICAL`

Researcher-ID：`R-8F3K`

Commuting-idempotent OR normal form 对 word 的 **terminal transformation** 完全 exact，但它不会自动对一个会观察每一步 action prefix 后 state 的 richer future language exact。

这一点给 semantic word quotient 一个 sharp boundary：finite terminal effect algebra 并不推出 finite prefix-observable operation-word semantics。

## 1. Terminal effect semantics

k 个 singleton OR generators 下，word w 的 terminal normal form 是：

`nu(w)=w 中出现过的全部 generator bits 的 OR`。

只需要知道哪些 generators 曾经出现。Order 与 repetition 都被删除。

Generated terminal transformation monoid 包括 identity 在内精确有：

`2^k`

个 effects。

## 2. Prefix-observable normal form

对 word：

`w=a_1...a_H`，

定义 cumulative masks：

`U_t = mask(a_1) OR ... OR mask(a_t)`。

Exact prefix-observable normal form 是：

`tau(w)=(U_1,...,U_H)`。

对任意 initial state x，完整 prefix-state trace 是：

`(x OR U_1,...,x OR U_H)`。

所以 tau 对所有 initial states 都 sufficient。

而且在 full prefix-state observation 下它 extensionally minimal：取 x=0 就能直接恢复 tau 本身。

## 3. Same terminal effect 可以有不同 prefix semantics

对 generators a,b：

`ab` trace：

`(a, a OR b)`，

而 `ba` trace：

`(b, a OR b)`。

Terminal effect 完全相同，但 prefix-observable operations 不同。

所以 terminal transformations commute，并不意味着当 intermediate state 可见时 action order 也 semantic irrelevant。

## 4. Prefix normal forms 仍然能 exact compose

设 `tau(u)` 最后得到 mask F，且：

`tau(v)=(V_1,...,V_r)`。

则：

`tau(uv)=tau(u) ++ (F OR V_1,...,F OR V_r)`。

所以 prefix-observable semantics 仍然有 closed exact composition law；只是它需要一个更丰富、variable-length 的 operation state。

Executable compiler 对 exhaustive small words 验证该 formula 与 literal concatenation 完全一致。

## 5. Finite terminal monoid，但 prefix-word semantics infinite

只取一个 idempotent generator a。

所有 nonempty words：

`a, a^2, a^3, ...`

都有同一个 terminal transformation。

但 prefix traces 长度不同：

`(1)`，

`(1,1)`，

`(1,1,1)`，……

因此 unbounded word length 下 prefix-observable operation algebra 是 infinite，即使：

- fine state set finite；
- terminal transformation monoid finite；
- generator 本身 idempotent。

这证明：

`finite state/effect monoid`

不推出

`finite operation-word semantics`

只要 timing / prefix output 被 declared visible。

## 6. 长度 H 的 exact prefix trace count

假设 length-H word 中一共首次引入 s 个 distinct generators。

它们 ordered identities 有：

`P(k,s)=k!/(k-s)!`

种。

第一个 action 必须在 position1 引入第一个 generator。其余 `s-1` 个 first-appearance times 从 positions2..H 中选择：

`C(H-1,s-1)`。

其他 positions 都是使用 already-seen generators 的 stutters，不改变 prefix mask。

因此 H>=1 时 distinct prefix traces 精确为：

`N_prefix(k,H)=sum_(s=1)^min(k,H) P(k,s) C(H-1,s-1)`。

## 7. Terminal effect count 小得多

Exact word length H 下，terminal masks 只是 size<=H 的 nonempty subsets：

`N_terminal(k,H)=sum_(s=1)^min(k,H) C(k,s)`。

总有：

`N_terminal <= N_prefix <= k^H`。

左边可以非常 strict，因为 prefix semantics 保留 generator discovery order 与 timing。

## 8. Sharp k=5,H=5 counts

k=5,H=5：

- literal words：`5^5=3125`；
- terminal semantic effects：31；
- prefix-observable traces：1045。

只看 terminal effect 为 full five-bit mask 的 words，在 H=5 时也已经有：

`5! = 120`

种不同 prefix traces，对应120种 generator introduction orders。

所以 terminal quotient 删除的大量 behavior，只要 prefix 暴露就立刻重新 semantic-visible。

## 9. Full-support traces with stuttering

H>=k 时，最终到达 full mask 的 prefix traces 数量为：

`k! * C(H-1,k-1)`。

`k!` 选择 first-introduction order；binomial factor 选择其余 introductions 发生在 H 个 positions 中的时点。

因此即使 final terminal effect 已经 saturation，prefix timing 仍会随着 horizon 继续生成新的 word semantics。

## 10. 与 guarded / partial semantics 的关系

Earlier P024 / FQ-006 结果因为 action legality 会在 intermediate states 失败，所以必须保留 prefix information。

本文在另一方向更 sharp：即使 actions **total、everywhere-defined、idempotent**，只要 future language 显式读取 intermediate states，就已经会需要 prefix-sensitive operation semantics。

所以 prefix complexity 不只由 DOMAIN / guards 引起；纯 observation language 也足以生成。

## 11. Semantic quotient 必须声明 observation interface

类似：

`word normal form = final OR mask`

这样的 statement，只对 terminal-transformation semantics 成立。

若 declared future language 包括：

- prefix states；
- prefix observations；
- 新 distinction 出现的 timing；
- intermediate costs / rewards；
- prefix legality 或 witness events；

那么即使 terminal operation quotient 对 final state transformation 完全 exact，也仍可能 semantic 太粗。

## 12. Representation-resource 与 semantic change 不同

这**不是**同一 semantic-equivalence fiber 内的另一个 representation Pareto。

Terminal-only 与 prefix-observable languages 保留的信息本身不同；从一个切到另一个是 declared future theory 的 semantic change。

只有 prefix semantic object 先确定后，才能继续比较 caches、scans、tables、formulaic representations 的 resource cost。

## 13. Stage131 consequence

Stage131 现在有一个硬顺序：

1. 先声明 operation semantics 是 terminal、prefix-observable、guarded、witness-sensitive 等哪一种；
2. 求正确的 semantic word quotient / normal form；
3. 然后再优化该 quotient 的 storage / work / depth representations。

把错误的 terminal quotient precompute 得更快，不能修复 prefix information 已经丢失的 semantic problem。

## Owner-local assets

- `src/enterprise_math/prefix_observable_or_word_semantics.py`；
- `tests/test_prefix_observable_or_word_semantics.py`；
- 本双语 theorem note。

## Prior-art / status

Prefix traces、semilattice actions、trace semantics 与 cumulative scans 都是标准既有数学 / CS。P023/A2 保留 future-signature / precision ownership。本文只拥有 Stage131 line 中 terminal-effect vs prefix-observable semantic boundary。

无 repository strict CI、无 `EXECUTABLE_CHECKED`、无 canonical claim。`CI_NOT_REQUIRED_FOR_RESEARCH`。Hard block：`NONE`。
