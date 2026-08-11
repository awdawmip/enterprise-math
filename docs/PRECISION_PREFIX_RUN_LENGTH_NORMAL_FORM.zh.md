# Infinite Prefix-Observable Word Semantics 的 Run-Length Normal Form

状态：`RESEARCH BRIDGE / NONCANONICAL`

Researcher-ID：`R-8F3K`

Full prefix-observable OR semantics 在 unbounded word length 下是 infinite；但 infinite semantic cardinality 并不意味着每个 operation 必须拥有 arbitrarily long 的**结构描述**。

Cumulative OR trace 最多只会变化 k 次，因此存在一个最多 k 个 phases 的 exact run-length normal form，并且具有 closed composition law。

## 1. Phase normal form

对 nonempty word 记录：

`((g_1,r_1),...,(g_s,r_s))`。

其中：

- `g_1,...,g_s` 是 generators 的 first-appearance order，彼此 distinct；
- `r_i>=1` 是引入 `g_i` 后 cumulative mask 连续保持该 level 的 prefix positions 数；
- `sum r_i=H`；
- `s<=k`。

例如：

`a a b a c c`

normal form 为：

`((a,2),(b,2),(c,2))`。

b 之后出现的 stutter a 不改变 cumulative mask，因此被吸收到 b phase 的 duration 中。

## 2. Exact decoding

从 mask0 开始。对每个 phase `(g_i,r_i)`：

1. OR 入 generator bit `g_i`；
2. 把 resulting mask 输出 `r_i` 次。

这样精确重建完整 H-step prefix trace。

所以 phase form 对 full prefix-state observation 完全 sufficient。

## 3. Canonical representative word

可以选择 canonical literal representative：

`g_1^r1 g_2^r2 ... g_s^rs`。

它与 original word 拥有完全相同的 prefix trace，并且重新 normalization 后得到同一个 phase form。

所以 semantic-invisible 的任意 stutter choice 被 exact 删除。

## 4. Closed exact composition

设 left form 已经见过一组 generators。按 first-appearance order 扫描 right phases：

- 若 right generator g 已经在 left 中出现，它整段 run 不会创造新 cumulative mask，只把 duration 加到当前 final phase；
- 若 g 是新的，则 append `(g,r)` 并标记为 seen。

得到的 form 与 literal word concatenation 后重新 normalization 完全相同。

Branch 对 bounded word pairs 做 exhaustive cross-check。

Empty form 是 identity，因此这些 phase forms 构成 prefix semantics 的 exact formulaic operation monoid。

## 5. One-generator specialization

k=1 时，每个 nonempty word 都是：

`((a,H))`。

Composition 只需做 duration addition：

`H_total=H_left+H_right`。

所以即使只有一个 nonidentity terminal transformation，prefix-word semantics 仍然 infinite，但 operation state 只需一个 unbounded integer duration。

这是“infinite semantics 仍可 finite-dimensional parameterize”的最小 sharp witness。

## 6. Exact class count

固定 exact word length H 与 phase count s。

Ordered distinct generator identities 有：

`P(k,s)=k!/(k-s)!`

种。

Positive duration composition：

`r_1+...+r_s=H`

有：

`C(H-1,s-1)`

种。

因此：

`N_s(k,H)=P(k,s) C(H-1,s-1)`。

对 `s=1..min(k,H)` 求和，精确恢复 parent prefix-trace count。

Executable layer 对 literal-word normalization 按 phase count逐层验证该公式。

## 7. Fixed k 下 semantic growth 是 polynomial

H>=k 时：

`N_prefix(k,H)=sum_(s=1)^k P(k,s) C(H-1,s-1)`。

它是 H 的 degree `k-1` polynomial。

最高次项来自 s=k：

`k! C(H-1,k-1)`，

leading coefficient：

`k!/(k-1)! = k`。

因此 fixed k 下：

`N_prefix(k,H)=Theta(H^(k-1))`，

leading asymptotic 为 `k H^(k-1)`。

Branch 机械验证：H>=k 后 `(k-1)` 阶 forward difference 恒等于 `k!`。

## 8. 三种 growth regime

Fixed k、H 增长时：

### Literal syntax

`N_literal=k^H`。

对 H 指数增长。

### Full prefix semantics

`N_prefix=Theta(H^(k-1))`。

对 H 多项式增长。

### Terminal transformation semantics

H>=k 后：

`N_terminal=2^k-1`。

对 H 完全 saturation。

所以 semantic quotient 删除了 exponential syntax redundancy，而 prefix timing 又阻止 terminal effect 那种完全 saturation。

## 9. Simple RLE storage upper bound

一个 total length H、s-phase form，可以用简单 fixed-width fields：

- 每个 generator ID：`ceil(log2 k)` bits；
- 每个 run length：`ceil(log2(H+1))` bits。

所以：

`B_RLE <= s[ceil(log2 k)+ceil(log2(H+1))]`，

且 `s<=k`。

Fixed k 下是 `O(k log H)` bits。

若直接 materialize 全部 prefix masks，需要：

`kH`

bits。

所以 compact operation state 与 fully materialized observable history 的 storage scaling 完全不同。

## 10. Information lower bound

固定 phase count s 时，一共有：

`P(k,s) C(H-1,s-1)`

种 forms。

任何 injective binary code 至少需要：

`ceil(log2[P(k,s) C(H-1,s-1)])`

bits。

可以分别 rank：

- ordered distinct generator tuple；
- H-1 slots 中的 `s-1` 个 positive-composition cut positions。

本文 simple field encoding 不声称 bit-optimal，只是透明 constructive upper bound。

## 11. Sharp k=5,H=100 storage example

Full materialized prefix trace：

`5*100=500` bits。

Worst-case simple five-phase RLE：

- generator ID width3；
- run-length width7；
- total `5*(3+7)=50` bits。

即使使用最简单 representation，也有10倍 storage reduction，而且仍可 exact decode。

H=1,000,000 时 materialized trace 要五百万 bits，而 simple five-phase form 对每个 duration 仍只需 O(log H) bits。

## 12. Composition cost 与 horizon 脱钩

每个 normal form 最多 k phases。Compose 两个 forms 只需扫描最多 k 个 right phases，output 也最多 k phases。

因此 high-level structural composition work 是 O(k)，与两个 literal word lengths 无关。

Run-length integer addition 的 bit cost只随 accumulated horizon logarithmic 增长。

所以很长的 future history 仍可拥有 compact exact compositional summary。

## 13. 若真的要求 full history，decoding cost 仍不可消失

Compressed form 可以不展开 H-step trace就继续 composition。

但若 consumer 真正要求**观察所有 H prefixes**，这些 H 个 outputs 最终仍需 materialize / stream。Prefix-scan generation 单独研究这一 execution cost。

所以：

`compact semantic state`

不推出

`zero-cost full observable history`。

两个 interfaces 必须保持区分。

## 14. 与 P024 的关系

P024 guarded `(T,H)` profile 已经说明 infinite operation language 可以有 finite-parameter exact normal form 与 closed composition。

Prefix-run form 给出第二个独立例子：

- parameter structure 数量最多 k phases；
- unbounded horizon 存在 integer duration fields 中；
- literal syntax 可无限增长，但 exact operation state 仍 finitely parameterized。

这支持更一般的 Stage131 原则：**compact exact law presentation 不要求 operation cardinality finite。**

## 15. Stage131 consequence

Semantic-resource hierarchy 现在必须同时区分：

- literal word length；
- semantic class count；
- exact normal form parameter dimension；
- parameter bit size；
- normal-form composition cost；
- declared outputs 的 materialization cost。

这些量彼此都不能单独决定其他量。

## Owner-local assets

- `src/enterprise_math/prefix_run_length_normal_form.py`；
- `src/enterprise_math/prefix_run_length_resources.py`；
- 对应 tests；
- 本双语 theorem note。

## Prior-art / status

Run-length encoding、positive composition、ordered first-appearance form 与 idempotent semigroup reduction 都是标准既有数学 / CS。P023/A2 保留 future-signature / precision ownership。本文只拥有 prefix-word finite-parameter exact representation specialization。

无 repository strict CI、无 `EXECUTABLE_CHECKED`、无 canonical claim。`CI_NOT_REQUIRED_FOR_RESEARCH`。Hard block：`NONE`。
