# Long-Horizon Prefix Semantic Information：Class Count 增长但 Entropy 有限

状态：`RESEARCH BRIDGE / NONCANONICAL`

Researcher-ID：`R-8F3K`

Fixed generator count k 下，exact length H 的 full-timing semantic classes 会随 H 多项式增长；但在 **uniform random literal-word workload** 下，probability mass 会集中到早期完成 coupon collection 的 histories。

因此 full timing semantic 的 Shannon entropy 反而趋于一个有限常数。

这给 worst-case semantic state count 与 workload-weighted semantic information 一个 sharp separation。

## 1. Random-word model

Literal actions iid uniform 于 k 个 generator labels。

Exact length H：

`H_literal=H log2 k`。

令 H→∞，k 固定。

## 2. Terminal-set entropy 趋于0

某一个 generator 到 H 仍未出现的概率：

`((k-1)/k)^H`。

Union bound：

`P(any generator missing)<=k((k-1)/k)^H`。

该概率指数衰减到0。

所以 terminal semantic state 以概率趋于 deterministic full set：

`H_terminal -> 0`。

也就是说 terminal algebra 即使数学上有 `2^k` 个 possible states，long-run workload entropy 仍可趋于0。

## 3. Discovery order 趋于 uniform permutation

条件在全部 k 个 generators 最终都出现，symmetry 使 first-appearance order 在 `k!` 个 permutations 上 uniform。

Incomplete discovery probability 趋零，因此：

`H_discovery -> log2(k!)`。

Long word 几乎必然看见所有 generators，但它们第一次出现的随机顺序仍保留 finite semantic information。

## 4. Coupon-collector waiting times

当已经发现 i 个 distinct generators，`1<=i<k`：

- 下一 action 已 seen 的概率：`q_i=i/k`；
- 下一 action 是 new generator 的概率：`p_i=(k-i)/k`。

因此 discovery phase i 的 duration R_i 趋于 positive geometric：

`P(R_i=r)=q_i^(r-1)p_i`, `r>=1`。

Coupon-collector stages 的 waiting times 独立；next new generator identity 在 unseen labels 中 uniform，并与 wait 独立。

## 5. Positive geometric phase 的 entropy

Success probability p，`q=1-p`：

`H(Geom(p))=-log2 p-(q/p)log2 q`。

这是 prefix state 在下一次 discovery 前会 stutter 多久的 finite uncertainty。

## 6. Full timing entropy 有 finite limit

Fixed horizon H 下，一旦所有 k generators 都已出现，final phase duration 由 H 与前面 `k-1` 个 waits 唯一确定。

H 增长后 incomplete coupon collection 可忽略，因此：

`H_timing -> C_k`，

其中：

`C_k = log2(k!) + sum_(i=1)^(k-1) H(Geom((k-i)/k))`。

等价展开：

`C_k = log2(k!)`

`+ sum_(i=1)^(k-1)[`

`  -log2((k-i)/k)`

`  -(i/(k-i))log2(i/k)`

`]`。

对每个 fixed k 都是有限常数。

## 7. Sharp k=2 limit

k=2：

- discovery limit：`log2(2!)=1` bit；
- 唯一 pre-completion wait 的 success probability=1/2；
- `H(Geom(1/2))=2` bits。

所以：

`H_timing -> 3 bits`。

Executable layer 验证 H=20 时 terminal entropy 已接近0、discovery 接近1、timing 接近3。

## 8. 但 k=2 timing class count 仍不断增长

k=2,H>=2：

`N_timing(2,H)=2H`。

因此：

`log2 N_timing ~ log2 H + 1`

继续发散。

与此同时 workload entropy 却收敛到3 bits。

所以 worst-case index size 与 Shannon average information 可以朝完全不同方向变化。

## 9. 为什么新增 timing classes 几乎没有 probability mass

很晚才发现 missing generator，意味着在此之前发生了异常长的 already-seen stutter run。

Possible late-discovery timings 数量随 H 增加，但它们总 probability 几何衰减。

因此 class-count growth 测量 reachable **possibility space**，entropy 则按实际 workload 对它加权。

两者都是合法 resources，但不是同一个问题。

## 10. Literal provenance 最终支配 information

Literal entropy：

`H_literal=H log2 k`

线性增长。

Timing entropy趋于 constant `C_k`。

因此：

`H_literal-H_timing = H log2 k-C_k+o(1)`。

这正是 parent decomposition 的 stutter-action provenance information。

H 很大以后，几乎所有新增 literal bits 都在记录**prefix state 已经不变时，到底选择了哪个 already-seen action label**，而不是新的 state timing。

## 11. Discovery 与 duration information 分别 saturation

Parent decomposition 给出：

`H_timing-H_discovery = duration information`。

所以 long-horizon limit 中：

- discovery-order information 趋 `log2(k!)`；
- duration information 趋 finite geometric-entropy sum；
- stutter provenance 吸收剩余 linear literal entropy。

因此可以按 observation layer 精确分配 asymptotic semantic information。

## 12. k=1 boundary

一个 generator 时，每个 fixed H 只有一个 literal word，因此全部 entropies 都为0，asymptotic constant 也是0。

但跨**不同 horizons**，prefix semantic operations 仍因 duration 不同而彼此 distinct。Fixed-H workload entropy 与 cross-horizon semantic cardinality 必须分开。

## 13. Stage131 coding consequence

若一个 table 必须 index horizon 内所有 possible timing classes，storage 仍可能 polynomial 增长。

但对 exact-H random workload 做 entropy coding，expected semantic bits 在 long horizon 下可以只有 O_k(1)。

两者不能互相替代：

- table cardinality 是 worst-case reachability / storage resource；
- Shannon entropy 是 distribution-relative average coding resource。

必须声明优化的是哪一个。

## 14. Broader precision lesson

“增加 future horizon”可以同时：

- 增加 mathematically possible semantic histories；
- 降低 coarse terminal state 的 uncertainty；
- 保留有限 discovery/timing uncertainty；
- 生成线性增长的 literal provenance information。

所以 horizon 不是 semantic information 的 scalar proxy。

它的作用取决于 observation layer 与 workload measure。

## Owner-local assets

- `src/enterprise_math/prefix_information_asymptotic.py`；
- `tests/test_prefix_information_asymptotic.py`；
- 本双语 theorem note。

## Prior-art / status

Coupon collector waiting time、geometric entropy 与 occupancy convergence 都是标准既有 probability / information theory。P023/A2 保留 future-signature / precision ownership。本文只拥有 fixed-k prefix-semantic information asymptotic specialization。

无 repository strict CI、无 `EXECUTABLE_CHECKED`、无 canonical claim。`CI_NOT_REQUIRED_FOR_RESEARCH`。Hard block：`NONE`。
