# P022 —— Barlow 堆垛多项式与任务相对精度

状态：`ACTIVE RESEARCH NOTE / EXACT INTEGER SPECIALIZATION / NOVELTY UNVERIFIED`  
归属：`program/p022-geometry-v2`  
依赖：`P022_GEODESIC_MULTIPLICITY.*`、`P022_GEODESIC_MULTIPLICITY_SUPPLEMENT_01.*`  
跨路线关系：A2/P023/P024“未来语言决定所需状态”的 P022 具体特化

## 1. 动机

FCC 与 HCP 不应继续被当成两个彼此无关的 graph examples。它们其实属于同一个 close-packed stacking family。

每个 close-packed layer 都是 triangular lattice。相邻两层之间有两种可选的 triangular-hole orientation，记界面选择为

\[
\sigma_j\in\{-1,+1\}.
\]

一个有限 prefix

\[
\sigma_0,\sigma_1,\ldots,\sigma_{k-1}
\]

描述从 layer zero 到 layer `k` 所经过的 contact geometry。周期 sign pattern 就给出周期 Barlow stacking。

真正的精度问题不是“有多少层选择”，而是：

> **当未来只询问某一类几何问题时，stacking word 的哪一部分必须继续可见？**

对“根层到一个指定目标层的全部本征距离 + 最短路重数”语言，答案出乎意料地小：一个整数 imbalance 就够，而且在自然意义下也是最小的。

## 2. 界面多项式

使用 triangular Laurent coordinates，定义

\[
A=x+x^{-1}+y+y^{-1}+xy^{-1}+x^{-1}y,
\]

\[
B_-=1+x^{-1}+y^{-1},
\qquad
B_+=1+x+y.
\]

`A` 表示一次层内 triangular move；`B_-`、`B_+` 表示两种 close-packed 界面各自三个可能的水平 offset。

二者满足

\[
\boxed{B_-B_+=A+3.}
\]

这就是上一份 HCP 推导中的 vertical-pair identity，现在提升为整个 close-packing family 的基本关系。

向下穿过某个界面时，edge offset 反向，因此 upward sign `sigma` 在 downward traversal 中变成 effective sign `-sigma`。

## 3. P022-BS01 —— geodesic 不会发生 vertical backtracking

固定根层和目标层 `k`。

一次 vertical backtrack 会跨过一个 interface，之后再反向跨回来。这一对 matched crossings 的水平 displacement polynomial 总是

\[
B_-B_+=A+3.
\]

其 support 只有零位移和六个 triangular primitive displacement。因此两次 backtracking steps 可以替换为：

- 净位移为零时，0 个层内 step；
- 净位移非零时，1 个层内 primitive step。

两种替换都严格短于原来的 2 步。

所以

\[
\boxed{
\text{从 layer 0 到 layer k 的任何最短路都只单调跨越恰好 }|k|
\text{ 个 interfaces。}}
\]

于是 arbitrary close-packed shortest path 被压缩成“一个有限 interface prefix + 必要的层内修正”。

## 4. P022-BS02 —— vertical witness polynomial

记从根层单调走到目标层 `k` 的 effective interface signs 为

\[
\epsilon_1,\ldots,\epsilon_{|k|}\in\{-1,+1\}.
\]

定义

\[
\boxed{
P_k(x,y)=\prod_{j=1}^{|k|}B_{\epsilon_j}(x,y).
}
\]

系数

\[
[x^qy^r]P_k
\]

就是只使用 mandatory vertical segment 时，到达目标层水平坐标 `(q,r)` 的 witness 数。

定义

\[
t_*(q,r;k)=
\min\{t\ge0:[x^qy^r]P_kA^t>0\}.
\]

因为每个 `B_±` 都包含零 monomial，这个有限最小值必定存在，并满足

\[
t_*\le h(q,r),
\]

其中 `h` 是 triangular distance。

于是精确得到

\[
\boxed{d(q,r,k)=|k|+t_*}
\]

以及

\[
\boxed{
g(q,r,k)
=\binom{|k|+t_*}{t_*}
[x^qy^r]P_kA^{t_*}.}
\]

binomial factor 只负责交错 vertical subsequence 与 in-layer subsequence，同时保留各自内部次序。

### 可执行复核

reference implementation 会把该公式与独立 BFS 对照。额外的会话内重建检查了 period length 不超过 4 的全部 30 个 ± 周期 patterns，在 graph radius 4 内共 9,530 个状态，没有发现 `(distance, shortest-path count)` 不一致。

## 5. P022-BS03 —— 可交换 normal form

定义目标 prefix 中 effective 两种 signs 的计数

\[
n_-(k)=\#\{j:\epsilon_j=-1\},
\qquad
n_+(k)=\#\{j:\epsilon_j=+1\},
\]

满足

\[
n_-+n_+=|k|.
\]

再定义整数 prefix imbalance

\[
\boxed{\delta_k=n_+(k)-n_-(k).}
\]

由于 Laurent multiplication 可交换，literal order 在 `P_k` 中消失：

\[
P_k=B_-^{n_-}B_+^{n_+}.
\]

使用 `B_-B_+=A+3`，设

\[
c_k=\min(n_-,n_+)=\frac{|k|-|\delta_k|}{2},
\]

则

\[
\boxed{
P_k=(A+3)^{c_k}
\begin{cases}
B_+^{\delta_k},&\delta_k>0,\\
1,&\delta_k=0,\\
B_-^{-\delta_k},&\delta_k<0.
\end{cases}}
\]

这就是 **Barlow prefix normal form**。

它把 prefix 拆成两个有限成分：

- `c_k`：多少对相反 orientation 被配成 HCP-like oscillation factor `A+3`；
- `|delta_k|`：还有多少 unmatched stacking drift 保留在同一方向。

固定 target layer 后，`|k|` 已知，因此其中一个量就能决定另一个。

## 6. P022-BS04 —— 对完整 target-layer metric+count language，一个整数已经充分

假设 future language 只针对一个声明好的目标层 `k`，但允许询问该层任意水平 endpoint `(q,r)` 的精确

\[
(d(q,r,k),g(q,r,k)).
\]

目标层编号 `k` 属于 query context。由 `(|k|,delta_k)` 可精确恢复

\[
n_-=(|k|-\delta_k)/2,
\qquad
n_+=(|k|+\delta_k)/2,
\]

进而恢复 `P_k`，再由 BS02 恢复所有 endpoint 的 distance 与 geodesic count。

所以

\[
\boxed{
\delta_k
\text{ 是完整 root-to-layer-k distance+count language 的充分 stacking-prefix state。}}
\]

这个 future language 不需要保留每个 individual interface identity。

这是 task-relative precision 在 close-packed geometry 中的一个完全整数实例。

## 7. P022-BS05 —— imbalance 也确实是必要坐标

仅有“充分”还不能证明 `delta_k` 就是精确 precision coordinate。下面可以从完整 target-layer count language 反向恢复它。

对 Laurent polynomial

\[
P=\sum_{q,r}c_{q,r}x^qy^r
\]

定义总质量与一阶 exponent moments：

\[
M(P)=\sum c_{q,r},
\]

\[
Q(P)=\sum q\,c_{q,r},
\qquad
R(P)=\sum r\,c_{q,r}.
\]

单个 interface 有

\[
M(B_+)=M(B_-)=3,
\]

\[
Q(B_+)=R(B_+)=1,
\qquad
Q(B_-)=R(B_-)=-1.
\]

而 product moment identity

\[
Q(PQ)=Q(P)M(Q)+M(P)Q(Q)
\]

给出：当 `|k|>0`，

\[
\boxed{
M(P_k)=3^{|k|},
\qquad
Q(P_k)=R(P_k)=\delta_k\,3^{|k|-1}.}
\]

因此

\[
\boxed{
\delta_k=Q(P_k)/3^{|k|-1}.}
\]

另一方面，完整 root-to-layer `distance+count` language 本身就能恢复 `P_k`：

- 若 `[x^qy^r]P_k>0`，endpoint `(q,r,k)` 的距离恰好为 `|k|`，此时 `t=0` 的 shortest-path count 就等于该 coefficient；
- coefficient 为零则意味着至少还需要一个层内 step，故距离严格大于 `|k|`。

所以 future language → `P_k` → `delta_k`。

于是，在所有针对该 future language 的 exact finite quotients 中，

\[
\boxed{
\delta_k
\text{ 在有限表示值的双射重标记意义下是最小的。}}
\]

不同 imbalance 不能继续安全合并。

## 8. P022-BS06 —— 多个 selected layers 的精度就是对应 prefix imbalances 向量

若 future language 查询有限 target-layer set

\[
J=\{k_1,\ldots,k_m\},
\]

则 BS04 立即给出充分状态

\[
\boxed{
\Delta_J=(\delta_{k_1},\ldots,\delta_{k_m}).
}
\]

BS05 又说明每个坐标都可从对应 target-layer language 反向恢复。因此 `Delta_J` 同样在有限 relabeling 意义下是最小的。

所以 precision cost 随**实际查询的 layer set**增长，而不是自动随 literal stacking-history length 增长。

### 两个极端

如果只查一个很远的 layer，一个整数就够。

如果把 upward prefix 的每一层 `1,2,...,N` 全部纳入 future language，则

\[
\sigma_j=\delta_{j+1}-\delta_j,
\]

并规定 `delta_0=0`。所以完整 trajectory

\[
(\delta_1,\ldots,\delta_N)
\]

会反向恢复 entire stacking word。

因此

\[
\boxed{
\text{查询所有 intermediate layers}
\Longrightarrow
\text{stacking-order compression 完全消失。}}
\]

这不是矛盾，而正是“精度取决于 future language”的精确体现。

## 9. final prefix state 相同，并不意味着 intermediate future 相同

考虑两个 four-interface words：

\[
(-,-,+,+)
\]

与

\[
(-,+,-,+).
\]

到 layer four 时，两者都有

\[
(n_-,n_+)=(2,2),
\qquad
\delta_4=0.
\]

因此它们完整的 root-to-layer-four distance+count language 完全相同。

但到 layer two：

第一条 word 有

\[
\delta_2=-2,
\]

第二条有

\[
\delta_2=0.
\]

其 layer-two endpoint semantics 不同。

所以

\[
\boxed{
\text{same final prefix imbalance}
\not\Rightarrow
\text{same intermediate-layer future language}.}
\]

这就是 close-packing 版本的 P023/P024 原则：只有在声明好的 operations/observations 下，quotient 才是合法的。

## 10. FCC 与 HCP 是 normal form 的两个极端

### FCC-type constant drift

constant sign pattern 满足

\[
|\delta_k|=|k|,
\qquad c_k=0,
\]

因此

\[
P_k=B_\pm^{|k|}.
\]

reference tests 中它精确重建 `A_3/FCC` contact graph 的 shell 与 multiplicity spectra。

### HCP-type alternating stacking

alternating pattern 的 imbalance 被严格限制：

\[
\delta_{2m}=0,
\qquad |\delta_{2m+1}|=1.
\]

所以

\[
P_{2m}=(A+3)^m,
\]

奇数层只多一个 `B_±` factor，恰好回到 Supplement 01 的 HCP 公式。

### 一般 Barlow prefix

每个有限 prefix 都有统一 normal form：

\[
P_k=(A+3)^{(|k|-|\delta_k|)/2}B_{\operatorname{sgn}\delta_k}^{|\delta_k|}.
\]

因此 `|delta_k|` 是当前 root-to-layer language 下 unmatched stacking drift 的一个直接整数尺度。

## 11. period-boundary universality

设周期 stacking word 的周期长度为 `L`，周期 imbalance 为

\[
D=\sum_{j=0}^{L-1}\sigma_j.
\]

那么在 layer `mL`，

\[
\delta_{mL}=mD.
\]

因此所有拥有同一 `(L,D)` 的周期 stacking，在每一个 period boundary layer 上都有完全相同的 vertical witness polynomial，以及完全相同的 root-to-layer-`mL` distance+count language：

\[
\boxed{
P_{mL}
=(A+3)^{m(L-|D|)/2}
B_{\operatorname{sgn}D}^{m|D|}.}
\]

period 内部 literal order 在这些被查询的层上不可见。

特别地，任何 zero-drift period 在 period boundaries 都满足

\[
P_{mL}=(A+3)^{mL/2},
\]

即使它们 intermediate layers 与完整 rooted shell spectra 不同。

这是一条 exact theorem，但不能误扩张成 all-layer 或 all-shell equivalence。

## 12. 当前 growth 开放问题

bounded computation 显示一个很有结构的现象：

- 当前测试过的 zero-drift periodic stackings，其 shell-total geodesic growth rate 都趋向 HCP 的增长率；
- nonzero-drift periodic stackings 的样本位于 HCP 与 FCC 之间；
- long-run drift 相同但 period 内 order 不同的 patterns，有限 shell 可以不同，但似乎趋向相同 exponential rate。

目前这**还不是定理**。

normal form 让下一步问题变得非常具体：

> 周期 Barlow stacking 的 asymptotic shell-total geodesic growth rate 是否只取决于 rational drift `|D|/L`？若是，能否从 drift 直接导出对应 algebraic growth constant？

真正的证明必须控制 whole-shell language，因为 whole shell 同时读取一个 period 内多个 prefix imbalance，而不只读 period boundary state。

## 13. 归属与架构

“future language 决定合法 quotient”的一般母定理仍属于 A2/P023/P024。

P022 此处拥有的是 concrete specialization：

- close-packed stacking signs；
- `B_±` 与 `A` Laurent polynomials；
- Barlow prefix normal form；
- exact integer imbalance coordinate；
- FCC/HCP 与周期 stacking 推论。

跨路线关系应记为 `SPECIALIZATION / CONSUMER`，不是 `SAME_MOTHER`。

## 14. executable assets

新增：

- `src/enterprise_math/p022_barlow_stacking.py`；
- `src/enterprise_math/p022_barlow_precision.py`；
- `tests/test_p022_barlow_stacking.py`；
- `tests/test_p022_barlow_precision.py`。

可执行层检查：

- unified formula vs FCC/HCP BFS；
- FCC reconstruction vs `A_3` spectra；
- HCP reconstruction vs 独立 HCP module；
- same-count/different-order prefix 在指定最终层上的 equivalence；
- intermediate-layer equivalence 失败；
- first-moment exact recovery of `delta`；
- 短 stacking words 上的有限 exhaustive minimality shadow。
