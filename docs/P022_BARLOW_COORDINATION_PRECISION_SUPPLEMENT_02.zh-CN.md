# P022 Barlow 配位精度补充 02 —— 坐标敏感 support 可恢复 signed drift

状态：`ACTIVE RESEARCH NOTE / EXACT FINITE MOMENT RECONSTRUCTION / NOVELTY UNVERIFIED`  
归属：`program/p022-geometry-v2`  
依赖：BC01–BC04 与 Barlow prefix normal form  
目的：区分“实际 shell-layer 集合”与“该集合的 cardinality”所需要的精度

## 1. 对一个容易误读结论的修正

BC02 已证明

\[
S_n(k)=3(2n-|k|)
\qquad(|k|<n),
\]

所以所有 non-extreme shell layers 的**点数**都与 stacking 无关。

但这绝不能被误读成“实际 shell-layer geometry 也与 stacking 无关”。

它作为坐标集合的 shape 仍然保留 signed prefix imbalance，而且仅用一个一阶整数 moment 就能把这个 imbalance 完整恢复。

因此

\[
\boxed{
\text{shell-layer set}
\text{ 与 }
|\text{shell-layer set}|
\text{ 的 minimum precision 不同。}}
\]

## 2. 对称 triple-coordinate 表示

先取 positive imbalance `delta=d>=0`。vertical support 为

\[
V_{c,d}=H_c+\Delta_d^+,
\]

并可写成

\[
V_{c,d}
=
\{(q,r):
-c\le q,r,q+r\le c+d
\}.
\]

定义

\[
x=q+c,
\qquad
y=r+c,
\qquad
z=c+d-q-r.
\]

则

\[
x+y+z=3c+d,
\]

其余 inequalities 也变成 `x,y,z` 上完全对称的 bounds。

所以 admissible triples 在任意 permutation of coordinates 下不变，从而

\[
\sum x=\sum y=\sum z
=\frac{3c+d}{3}|V_{c,d}|.
\]

回到 axial coordinates：

\[
\boxed{
\frac1{|V_{c,d}|}\sum_{(q,r)\in V_{c,d}}q
=
\frac1{|V_{c,d}|}\sum_{(q,r)\in V_{c,d}}r
=rac d3.}
\]

negative imbalance 对应 support reflection，因此 signed 形式是

\[
\boxed{
\sum q=\sum r
=\frac{\delta}{3}|V_{c,|\delta|}|.}
\]

除以 3 的整除性由 lattice symmetry 自动保证。

## 3. P022-BCS01 —— vertical support 精确恢复 signed imbalance

记

\[
K=|V_{c,|\delta|}|,
\]

以及

\[
M_q=\sum_{(q,r)\in V}q.
\]

则

\[
\boxed{
\delta=\frac{3M_q}{K}.}
\]

因此 selected target layer 上完整的 coordinate-sensitive **minimum-vertical existence set** 本身就能恢复 `delta`，包括 sign。

这比前面的 Barlow BS05 更强。BS05 是从完整 distance+shortest-count language 的 coefficient moments 中恢复 `delta`；现在可知 count observable 对这个 minimality statement 并不是必要的：

> **只要保留 selected layer 上完整 coordinate-sensitive native distance/existence language，就已经能恢复 signed prefix imbalance。**

因为 distance function 会识别出“恰好在 `|k|` 步可达”的 endpoints；这一集合就是 `V`，其 first moment 直接恢复 `delta`。

所以 shortest-path multiplicity 确实保留更深几何，但对完整 coordinate-sensitive one-layer distance language 来说，它不会进一步提高最低 stacking state。

## 4. P022-BCS02 —— 所有 expanded supports 保持同一个 centroid

对任意非负整数 `s`，考虑

\[
H_s+\Delta_d^+.
\]

同样的 triple-coordinate symmetry 仍成立，只是 `c` 换成 `s`；其 axial centroid 仍是

\[
(d/3,d/3).
\]

negative imbalance 反射后，centroid 变成

\[
(\delta/3,\delta/3).
\]

因此 graph-shell construction 中用到的所有 nested expansions 都共享同一个、只由 signed drift 决定的 centroid。

## 5. P022-BCS03 —— non-extreme shell layer 的 first moment 仍保留 signed drift

non-extreme shell layer 是

\[
\bigl(H_{c+t}+\Delta_d\bigr)
\setminus
\bigl(H_{c+t-1}+\Delta_d\bigr),
\qquad t=n-|k|>0.
\]

两层 nested supports 的 centroid 都是 `delta/3`，所以 set difference 仍保持这一 centroid。

其 cardinality 为

\[
N=3(2n-|k|).
\]

于是任意 axial first moment 都满足

\[
\boxed{
M_q=M_r
=rac{\delta N}{3}
=\delta(2n-|k|).}
\]

所以

\[
\boxed{
\delta
=rac{M_q}{2n-|k|}.}
\]

因此即使 **cardinality 完全 stacking-independent**，coordinate-sensitive shell layer 本身仍然在一阶 moment 中保留完整 signed imbalance。

这是一个非常尖锐的信息损失例子：

\[
\boxed{
\text{same layer cardinality}
\not\Rightarrow
\text{same layer support shape}.}
\]

## 6. extreme layers

当 `|k|=n` 时，shell layer 就等于 vertical support 本身。BCS01 给出

\[
\delta=3M_q/K.
\]

如果只保留 cardinality `K`，BC03 说明 sign 会丢失，只能恢复

\[
|\delta|.
\]

因此 identified extreme layer 上存在严格层级：

\[
\boxed{
\text{coordinate-sensitive set}
\to \delta
\to |\delta|
\to K.}
\]

第一步在 finite represented drift values 的 relabeling 意义下是 exact equivalence；第二步是主动做 reflection quotient。

## 7. 一个 selected shell layer 的 precision table

固定 shell radius `n` 与 selected layer `k`：

### 完整 coordinate-sensitive membership / distance function

需要 stacking state：

\[
\boxed{\delta_k.}
\]

### 只保留 first axial moment

在 `(n,k)` 与 layer size 属于 query context 时，仍然足以并且精确等价于 `delta_k`。

### 只问 layer cardinality，且 non-extreme `|k|<n`

需要 stacking state：

\[
\boxed{\text{none}.}
\]

答案恒为 `3(2n-|k|)`。

### 只问 layer cardinality，且 extreme `|k|=n`

需要 stacking state：

\[
\boxed{|\delta_k|.}
\]

仅仅把 observation 从 set membership 改成 first moment、再改成 cardinality，就出现了四层不同 exact quotient。

## 8. 与 multiplicity hierarchy 的关系

这个结果澄清了 geodesic multiplicity 到底在做什么。

它**不是**第一个能看见 stacking phase 的 observable：coordinate-sensitive distance support 已经能看到 signed `delta`。

multiplicity 真正不可替代的是更细问题：

- 同一个 endpoint 有多少 shortest witnesses；
- geodesic interval profiles；
- shell multiplicity spectra；
- count-enriched composition。

这些 observables 会继续区分已经共享某些 existence support / cardinality shadows 的状态。

所以 geometry hierarchy 不能简单写成一条全序，而应明确区分：

\[
\text{coordinate support shape}
\quad\text{vs}\quad
\text{support cardinality}
\quad\text{vs}\quad
\text{witness multiplicity}.
\]

它们来自同一个 primitive graph，却可以是不同甚至不可比较的 future observables。

## 9. 对 P023/P024 的反哺

这是一般 future-language rule 的直接 worked example：

- 保留完整 coordinate-sensitive relation，需要一个 signed integer；
- 对 non-extreme layer 应用 `cardinality` observation，可把这个 integer 全部擦掉；
- 对 extreme layer 应用 `cardinality`，只擦掉 sign；
- 再把 top / bottom 汇总成 whole-shell cardinality，又擦掉两侧 allocation，只保留 `delta_n^2+delta_-n^2`。

这些 successive quotients 不是由一个抽象 global precision order 决定，而是由 declared observations 诱导出来的。

一般 mother theorem 仍归 A2/P023/P024；本文只是 P022 的 concrete geometry specialization。

## 10. executable assets

`p022_barlow_coordination.py` 已新增 vertical support 与 shell-layer set 的 exact first-moment formula 和 inverse recovery functions。

测试把这些 moments 与 explicit polynomial-support / contact-shell enumeration 对照，覆盖全部短周期 stackings。
