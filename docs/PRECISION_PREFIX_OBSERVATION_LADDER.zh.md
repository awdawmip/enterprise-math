# Prefix Observation Ladder：Terminal Set、Discovery Order 与 Full Timing

状态：`RESEARCH BRIDGE / NONCANONICAL`

Researcher-ID：`R-8F3K`

“Prefix-visible” 不是一个 binary semantic switch。即使只在 commuting-idempotent OR language 内，也至少存在三层 exact future-observation semantics：

1. 最终出现过哪些 generators；
2. 新 generators 第一次出现的顺序；
3. 每个 cumulative prefix state 的完整 timing / duration。

三层之间存在 exact quotient homomorphisms，而且 finite / infinite behavior 不同。

## 1. Level T — terminal-set semantics

只保留 final mask：

`{至少出现过一次的 generators}`。

Composition 是 set union / bitwise OR。

包括 identity 在内，semantic monoid 精确有：

`2^k`

个 elements。

Exact nonempty word length H 下 reachable terminal effects 数量：

`sum_(s=1)^min(k,H) C(k,s)`。

H>=k 后 saturation 到 `2^k-1` 个 nonidentity effects。

## 2. Level D — discovery-order semantics

保留 distinct generators 的 first-appearance order：

`delta(w)=(g_1,...,g_s)`。

Already-discovered generator 的 repeated uses 被删除，但 first introduction order 保留。

Composition：

- 完整保留 left discovery list；
- 扫描 right list，只 append left 里尚未出现的 generators。

这是标准 first-occurrence / free-left-regular-band 型 product。

Executable compiler 在 bounded complete families 上验证：

`x*x=x`

与

`x*y*x=x*y`。

## 3. Level D finite，但远细于 terminal set

包括 identity，discovery-order monoid size：

`1 + sum_(s=1)^k P(k,s)`，

其中：

`P(k,s)=k!/(k-s)!`。

Exact length H 下 count：

`sum_(s=1)^min(k,H) P(k,s)`。

H>=k 后 saturation 到 finite monoid size minus identity。

k=5 时完整 discovery monoid 有326个 elements（含 identity），而 terminal masks 只有32个。

## 4. Strict terminal/discovery witness

Words：

`ab`

与

`ba`

terminal set 都是 `{a,b}`。

但 discovery orders 是：

`(a,b)`

与

`(b,a)`。

所以观察**哪个新 capability 先出现**，会严格 refine terminal-set semantics，即使仍然忽略 stutter timing。

## 5. Level P — full prefix timing

Parent run-length form 保存：

`((g_1,r_1),...,(g_s,r_s))`。

投影到 discovery semantics 时只删除 run lengths：

`((g_i,r_i)) -> (g_i)`。

Branch 验证该 projection 是 monoid homomorphism。

与 Level D 不同，Level P 在 unbounded horizon 下仍然 infinite，因为 durations `r_i` 是 unbounded integers。

## 6. Strict discovery/timing witness

Words：

`aab`

与

`abb`

拥有：

- same terminal set `{a,b}`；
- same discovery order `(a,b)`；
- different timing forms：
  `((a,2),(b,1))` vs `((a,1),(b,2))`。

因此第二个 discovery **何时**发生，是“哪个 discovery 先发生”之外的一条独立 semantic coordinate。

## 7. Exact quotient ladder

存在 exact surjective semantic maps：

`full timing -> discovery order -> terminal set`。

并且都与 word composition commute：

- timing composition 投影成 discovery composition；
- discovery composition 投影成 terminal OR。

所以这不仅是 counting hierarchy，而是 exact operation algebras 的 quotient hierarchy。

Kernels 向下变粗，因此 timing > discovery > terminal 的 semantic precision 逐层降低。

## 8. Event-mask observation 与 discovery order 等价

也可以不直接观察 generator identities，而只观察 cumulative mask **发生变化时的 distinct event sequence**。

每次 event 恰好增加一个新 bit，因此 newly added bit 唯一恢复 introduced generator。

所以：

`discovery order <-> change-event mask sequence`

是 exact bijection。

因此 Level D 正是“报告 state-change events，但不报告 stutter duration”这一 observation language 的 minimal exact state。

## 9. Exact class-count ladder

Exact nonempty word length H：

### Terminal

`N_T=sum C(k,s)`。

### Discovery order

`N_D=sum P(k,s)`。

### Full timing

`N_P=sum P(k,s) C(H-1,s-1)`。

所有 sums 都取 `s=1..min(k,H)`。

总有：

`N_T <= N_D <= N_P <= k^H`。

对应 observation resource 一旦可见，不等式就可以严格。

## 10. Sharp k=5,H=5 ladder

k=5,H=5：

- literal words：3125；
- full timing traces：1045；
- discovery orders：325；
- terminal effects：31。

不同 observation interfaces 删除不同 literal redundancy：

- terminal quotient 删除 order 与 timing；
- discovery quotient 恢复 first-introduction order，但继续删除 stutter timing；
- full timing 恢复 durations，但仍不记录 stutter 时到底用了哪个 already-seen generator。

## 11. 即使 full prefix timing 仍是 literal syntax 的 quotient

若两个 literal words 只在 stutter 时使用哪个 already-seen generator 上不同，它们可以拥有完全相同的 cumulative-mask trace。

例如 a、b 都已经 visible 后，再执行 a 或 b，都不会改变 prefix state。

所以 Level P 对 full prefix-state observation 完全 exact，但仍比 literal action provenance 粗。

如果 future language 还观察 action labels、per-action costs、provenance、witness events，就必须继续 enrich semantic state。

## 12. Semantic dimension 与 resource representation 分开

三层 semantic levels 不能和 implementation choices 混淆。

某一层一旦声明后，仍可有多种 resource-equivalent representations：

- terminal masks 可用 bitsets / tables / circuits；
- discovery orders 可用 generator lists / event masks；
- full timing 可用 raw H-step traces / compact run-length forms。

Semantic ladder 在前，representation Pareto 在后。

## 13. Stage131 consequence

Future-language precision 可以依赖多个 temporal observation coordinates：

- final reachable state / effect；
- 新 distinction 出现的 order；
- changes 之间的 exact timing / duration；
- literal action / witness provenance。

不存在一个安全的 generic “prefix precision” scalar 把它们全部概括。

每一种 observation contract 都诱导自己的 semantic quotient 与 operation algebra。

## Owner-local assets

- `src/enterprise_math/prefix_observation_semantic_ladder.py`；
- `tests/test_prefix_observation_semantic_ladder.py`；
- 本双语 theorem note。

## Prior-art / status

Left regular band、first-occurrence word reduction、event trace 与 quotient homomorphism 都是标准既有 algebra / CS。P023/A2 保留 future-signature / precision ownership。本文只拥有 terminal / discovery / timing observation-ladder specialization。

无 repository strict CI、无 `EXECUTABLE_CHECKED`、无 canonical claim。`CI_NOT_REQUIRED_FOR_RESEARCH`。Hard block：`NONE`。
