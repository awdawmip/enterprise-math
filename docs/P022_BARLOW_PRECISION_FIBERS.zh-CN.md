# P022 —— Barlow 精度 fiber 与最优 checkpoint 调度

状态：`ACTIVE RESEARCH NOTE / EXACT FINITE QUOTIENT SPECTRUM / NOVELTY_UNVERIFIED`  
归属：`program/p022-geometry-v2`  
跨路线关系：P011 fiber/collision spectrum 与 P023/P024 task-relative quotient safety 的 P022 精确特化

## 1. stacking-prefix quotient 有完全可计算的 microscopic fiber structure

长度为 `N` 的 close-packed stacking prefix 是 microscopic word

\[
\sigma=(\sigma_1,\ldots,\sigma_N)
\in\{-1,+1\}^N.
\]

前面的 Barlow theorem 已经证明：若 future language 只关心 root-to-layer-`N` 的完整 coordinate-sensitive distance language，则整个 word 可精确替换为一个整数

\[
\delta_N=\sum_{j=1}^{N}\sigma_j.
\]

因此合法 quotient 是

\[
q_N:\{-1,+1\}^N\to\{-N,-N+2,\ldots,N\},
\qquad
q_N(\sigma)=\delta_N.
\]

这里进一步追问：

> **每一个 observable state 里，究竟合法 collapse 了多少 microscopic histories？**

答案是完全闭式的 binomial structure。

## 2. P022-PF01 —— final imbalance 的 fiber spectrum

若

\[
\delta=2k-N,
\]

则一个 word 具有 imbalance `delta`，当且仅当它含 `k` 个 plus signs 与 `N-k` 个 minus signs。

所以

\[
\boxed{
|q_N^{-1}(\delta)|=\binom Nk.}
\]

完整 quotient-fiber spectrum 为

\[
\boxed{
\left(
-N:\binom N0,
-N+2:\binom N1,
\ldots,
N:\binom NN
\right).}
\]

fibers 高度不均匀：constant-drift 极端态只有一个 microscopic word，而接近 zero drift 的 fiber 最大。

所以同一个 exact future language 在 balanced drift 附近会合法 collapse 更多 microscopic history。

## 3. P022-PF02 —— 精确 pair-collision count

统计 final imbalance 相同的 ordered microscopic word pairs：

\[
\sum_{k=0}^{N}\binom Nk^2.
\]

由 Vandermonde identity：

\[
\boxed{
\sum_{k=0}^{N}\binom Nk^2
=\binom{2N}{N}.}
\]

其中 `2^N` 对是同一个 microscopic word 与自己配对。

因此 final-imbalance quotient 实际识别掉的 **distinct unordered word pairs** 数是

\[
\boxed{
C_N
=\frac{\binom{2N}{N}-2^N}{2}.}
\]

这就是该 quotient map 的 order-two collision statistic。

更一般的 P011-style order-`r` collision count 为

\[
\boxed{
J_r(N)
=\sum_{k=0}^{N}
\binom{\binom Nk}{r}.}
\]

这里不另造 generic irreversibility theory；它只是已有 finite fiber/collision framework 的 Barlow closed specialization。

## 4. selected-layer future language

现在假设 future language 只读取 selected layers

\[
0<k_1<\cdots<k_m\le N
\]

处的 prefix imbalances。

定义 constrained segment lengths

\[
\ell_1=k_1,
\qquad
\ell_j=k_j-k_{j-1}\quad(j>1),
\]

若最后 selected layer 不是 `N`，还有完全不可见的 final tail

\[
u=N-k_m.
\]

observation 为

\[
O_J(\sigma)
=(\delta_{k_1},\ldots,\delta_{k_m}).
\]

由于互不重叠的 stacking segments 是独立有限 words，每一个 fiber 都可以逐 segment factorize。

## 5. P022-PF03 —— selected checkpoint language 的 image size

长度 `ell` 的一个 segment 恰好有

\[
\ell+1
\]

种可能 net imbalance。

segment increments 与 checkpoint trajectory 一一对应。因此

\[
\boxed{
|O_J(\{-1,+1\}^N)|
=\prod_{j=1}^{m}(\ell_j+1).}
\]

unobserved tail 不产生任何 observation coordinate。

几个极端：

- 一个 layer 都不查：image size `1`；
- 只查最终层：image size `N+1`；
- 每个 prefix layer 都查：image size `2^N`，observation 变成 injective。

## 6. P022-PF04 —— 一个 observed trajectory 的 exact fiber size

假设 checkpoint imbalances 为

\[
d_1,\ldots,d_m,
\qquad d_0=0.
\]

第 `j` 段 net increment 是

\[
h_j=d_j-d_{j-1}.
\]

该 segment microscopic words 数为

\[
\binom{\ell_j}{(\ell_j+h_j)/2}
\]

（parity/range 不合法时为 0）。

final unobserved tail 完全自由，因此

\[
\boxed{
|O_J^{-1}(d_1,\ldots,d_m)|
=2^u
\prod_{j=1}^{m}
\binom{\ell_j}{(\ell_j+h_j)/2}.}
\]

这给出了每一个 represented precision state 的 exact microscopic ambiguity。

## 7. P022-PF05 —— global equal-observation pair count

不固定某一个 trajectory，而是对全部 trajectories 求 squared fiber size。

一个长度 `ell` 的 segment 由 Vandermonde 得

\[
\sum_h
\binom{\ell}{(\ell+h)/2}^2
=\binom{2\ell}{\ell}.
\]

segments 独立 factorize，而 unobserved tail 对两个 words 都自由，贡献 `4^u`。

所以

\[
\boxed{
P_J
:=\#\{(\sigma,\tau):O_J(\sigma)=O_J(\tau)\}
=4^u\prod_{j=1}^{m}\binom{2\ell_j}{\ell_j}.}
\]

扣除 `2^N` 个 identical pairs，再除以 2：

\[
\boxed{
C_J
=\frac{
4^u\prod_j\binom{2\ell_j}{\ell_j}-2^N
}{2}.}
\]

这就是 declared checkpoint language 精确 collapse 的 distinct microscopic word-pairs 数。

它在两个极端之间连续插值。

### 只查询 final layer

\[
C_J
=\frac{\binom{2N}{N}-2^N}{2}.
\]

### 每一层都查询

所有 segments 都长 1，因此

\[
P_J=2^N,
\qquad
\boxed{C_J=0.}
\]

不再 collapse 任何 microscopic history。

## 8. observation 数量相同，checkpoint placement 仍然重要

固定 `N` 与 checkpoint 数 `m`。

即使 observation count 完全相同，不同 placements 产生不同 segment lengths，因此产生不同 collision ambiguity。

核心数列是 central binomial

\[
f(n)=\binom{2n}{n}.
\]

它的 consecutive ratio 为

\[
\boxed{
\frac{f(n)}{f(n-1)}
=4-\frac2n,}
\]

并随 `n` 严格增大。

这一个整数 monotonicity identity 已经足以完整解出 scheduling problem。

## 9. P022-PF06 —— final layer 必须可见时，balanced checkpoints 精确最小化 ambiguity

假设允许 `m>=1` 个 checkpoints，并规定 layer `N` 必须被查询。

于是全部 constrained segment lengths 为正，并满足

\[
\ell_1+\cdots+\ell_m=N.
\]

若有两段

\[
a\ge b+2,
\]

把较长段拿 1 步给较短段，比较前后 product：

\[
\frac{f(a)f(b)}{f(a-1)f(b+1)}
=
\frac{4-2/a}{4-2/(b+1)}
>1.
\]

所以 balancing 会严格降低 equal-observation pair count。

不断执行 exchange 得到：

\[
\boxed{
\text{当且仅当所有 segment lengths 相差不超过 1 时，collision ambiguity 最小。}}
\]

写

\[
N=am+r,
\qquad0\le r<m.
\]

则最优 segment multiset 是

\[
\boxed{
\underbrace{a,\ldots,a}_{m-r},
\underbrace{a+1,\ldots,a+1}_{r}.}
\]

这些 segments 怎样排列，collision count 相同；canonical schedule 可把短段放在前面。

minimum ordered equal-observation pair count 为

\[
\boxed{
P_{\min}
=\binom{2a}{a}^{m-r}
\binom{2a+2}{a+1}^{r}.}
\]

所以 near-uniform checkpoint spacing 不是 heuristic suggestion，而是这一 quotient-collision objective 的 exact optimizer。

## 10. P022-PF07 —— final layer 可见条件下，最不均匀 schedule 最大化 ambiguity

在同一 final-visible constraint 下，strict log-convexity 也直接给出另一端 extremum。

让 `m-1` 段尽可能短，把全部剩余长度堆入一段：

\[
\boxed{
(1,\ldots,1,N-m+1).}
\]

此时

\[
\boxed{
P_{\max}^{\mathrm{final}}
=2^{m-1}
\binom{2(N-m+1)}{N-m+1}.}
\]

所以即使 checkpoint 数完全相同，不同 placements 仍可能合法 collapse 非常不同数量的 histories。

## 11. P022-PF08 —— final layer 不要求可见时，front-loading 最差

现在允许最后 checkpoint 早于 `N`，留下长度 `u` 的 unobserved tail。

该 tail 对 pair ambiguity 的贡献是

\[
4^u.
\]

若把 tail 中一个 hidden step 移入最后一个已观察 segment（当前长度 `ell`），ambiguity factor 改变量为

\[
\frac{f(\ell+1)/f(\ell)}{4}
=
1-\frac{1}{2(\ell+1)}
<1.
\]

所以 observation 往后延伸一定会减少 ambiguity。

固定 checkpoint 数 `m` 时，最大 ambiguity 出现在 checkpoints 全堆在前 `m` 层、保留最长 invisible tail `N-m`：

\[
\boxed{
P_{\max}
=2^m4^{N-m}.}
\]

因此，如果目标是 reconstruct 整个有限 prefix，早期 observations 再密也不能弥补 terminal tail 完全不可见带来的信息丢失。

## 12. 一个 exact finite precision-scheduling model

这个 Barlow quotient 给出了一个完全闭式的 precision placement toy model：

- 每个 queried layer 是 finite observation；
- unqueried interface identities 是 microscopic detail；
- quotient fiber 直接计数仍然合法不可见的 detail；
- collision count 测量 global ambiguity；
- 即使 observation 数不变，checkpoint placement 也会改变 ambiguity。

因此得到严格 design rule：

> **固定 checkpoint budget 且要求最终状态可见时，应把 observations 尽可能均匀地分布在 hidden evolution 上。**

这条结论依赖当前 ±1 prefix-imbalance language 的 log-convex fiber structure。不能未经证明就推广成所有 engineering sampling system 的普遍定理。

## 13. 跨路线含义

### P011

binomial fibers 构成一个 closed functional collision spectrum；generic fiber/collision statistics 的母归属仍是 P011。

### P023/P024

checkpoint set 本身就是 future observation language 的一部分。改变 checkpoint set 会改变 coarsest legal quotient 与 fiber structure。极端的 “every layer” 会让 quotient 变成 injective。

### P022

P022 保留 close-packed stacking specialization 与 exact checkpoint optimization。

## 14. executable assets

新增：

- `src/enterprise_math/p022_barlow_precision_fibers.py`；
- `tests/test_p022_barlow_precision_fibers.py`。

测试会 exhaustively 对照所有短 ±1 words 的 fiber formula、pair-collision formula，并 brute-force small `N` 的全部 checkpoint placements，验证 balanced/minimum 与 front-loaded/maximum scheduling theorem。
