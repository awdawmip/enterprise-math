# P022 —— Barlow 观测格与不可比较的精度 shadow

状态：`ACTIVE RESEARCH NOTE / EXACT FINITE SEPARATIONS / NOVELTY UNVERIFIED`  
归属：`program/p022-geometry-v2`  
范围：close-packed contact graph 的 rooted shell observables  
目的：用精确有限反例证明 exact precision 是由 future observables 索引的偏序，而不是单一 scalar ladder

## 1. 同一个 geometry 可以投影出多个不等价 shadows

固定一个 rooted Barlow contact graph 与 radius `n`。

同一个有限 shell 可以承载许多 exact observations：

1. coordinate-labelled endpoint set；
2. coordinate-labelled shortest-path count function；
3. 每个 target layer 分别保留的 multiplicity spectrum；
4. 整个 shell 的 global shortest-path multiplicity spectrum；
5. shell cardinality；
6. 进入整个 shell 的 shortest paths 总数。

其中一些 observables 可以确定性地 postprocess 成另一些；另外一些彼此不可比较。

所以真正出现的是一个有限 information **poset**，而不是一条线性的 precision scale。

## 2. 定义这些 observables

令 rooted shell 为 `X_n`。

### coordinate-labelled path-count function

\[
\boxed{
F_n(v)=g(0,v),
\qquad v\in X_n.}
\]

domain 保留真实 Barlow coordinates / layer labels。

### layer-resolved multiplicity spectrum

对每个 target layer `k`，定义

\[
\boxed{
\Sigma_{n,k}(m)
=\#\{v\in X_n:\text{layer}(v)=k,\ g(0,v)=m\}.}
\]

### global multiplicity spectrum

忘记 target layer：

\[
\boxed{
\Sigma_n(m)
=\sum_k\Sigma_{n,k}(m).}
\]

### shell cardinality

\[
\boxed{
S_n=\sum_m\Sigma_n(m).}
\]

### total geodesic multiplicity

\[
\boxed{
T_n=\sum_m m\,\Sigma_n(m).}
\]

因此 global spectrum 同时确定 `S_n` 与 `T_n`。

## 3. exact forgetful maps

存在规范 maps：

\[
F_n
\longrightarrow
(\Sigma_{n,k})_k
\longrightarrow
\Sigma_n
\longrightarrow
(S_n,T_n).
\]

最后的 pair 又分别投影到

\[
S_n
\quad\text{与}\quad
T_n.
\]

每一个箭头都是 exact finite postprocessing。

关键问题是：coarser observable 能否反向恢复 finer observable？下面所有逆向都被 explicit finite counterexample 否定。

## 4. P022-OL01 —— shell cardinality 不决定 total geodesic count

radius `3` 时，考虑两个 period-three stackings：

\[
(-,-,+)
\]

与

\[
(-,+,-).
\]

二者都有

\[
\boxed{S_3=96.}
\]

但 shortest-path totals 分别是

\[
\boxed{T_3=402}
\]

与

\[
\boxed{T_3=384.}
\]

所以

\[
\boxed{S_n\not\Rightarrow T_n.}
\]

也就是说，对 shell cardinality 足够的 quadratic drift energy `Q_n` 并不足以回答 path multiplicity。

## 5. P022-OL02 —— total geodesic count 也不决定 shell cardinality

radius `2` 时，FCC 与 HCP 都有

\[
\boxed{T_2=84.}
\]

但

\[
S_2^{FCC}=42,
\qquad
S_2^{HCP}=44.
\]

因此

\[
\boxed{T_n\not\Rightarrow S_n.}
\]

所以 `S_n` 与 `T_n` 是真正不可比较的 observables；不能说其中一个只是另一个的“更高精度版本”。

联合 observation `(S_n,T_n)` 才严格强于任意单独一个坐标。

## 6. P022-OL03 —— 即使 `(S_n,T_n)` 联合也不决定 multiplicity spectrum

radius `3` 时取两个 period-five words：

\[
(-,-,-,+,-)
\]

与

\[
(-,-,+,-,+).
\]

二者都满足

\[
\boxed{(S_3,T_3)=(96,390).}
\]

但 global multiplicity spectra 不同。

第一条：

\[
\boxed{
\Sigma_3=\{1:18,\ 3:54,\ 6:6,\ 9:18\}.}
\]

第二条：

\[
\boxed{
\Sigma_3=\{1:14,\ 2:8,\ 3:42,\ 5:4,\ 6:8,\ 9:20\}.}
\]

两个 spectra 的 zeroth moment 都是 `S_3=96`，first multiplicity moment 都是 `T_3=390`，但 distribution 本身不同。

所以

\[
\boxed{(S_n,T_n)\not\Rightarrow\Sigma_n.}
\]

这正对应 count-enriched A4/P021 bridge 中的有限 moment 现象：少数 moments 不会自动决定完整 witness distribution。

## 7. P022-OL04 —— global spectrum 不决定 layer-resolved spectrum

radius `2` 时，period-four words

\[
(-,-,-,+)
\]

与

\[
(-,+,-,+)
\]

拥有相同的**global** multiplicity spectrum：

\[
\boxed{
\Sigma_2=\{1:18,\ 2:18,\ 3:2,\ 4:6\}.}
\]

但这些 multiplicities 在各个 target layers 之间的 allocation 不同。

因此

\[
\boxed{
\Sigma_n\not\Rightarrow(\Sigma_{n,k})_k.}
\]

global histogram 已经忘记每个 witness multiplicity 究竟出现在哪一层。

## 8. P022-OL05 —— layer-resolved spectrum 仍不决定 coordinate-labelled geometry

取两个 constant-drift patterns：

\[
(-)
\]

与

\[
(+).
\]

它们通过 horizontal reflection 互相对应，因此每个 radius 的 layer-resolved multiplicity spectra 相同。

但在固定 axial coordinate chart 中，coordinate-labelled path-count functions 被反射，因而并不相等：

\[
F_n^-\ne F_n^+.
\]

所以

\[
\boxed{
(\Sigma_{n,k})_k\not\Rightarrow F_n.}
\]

这不是 physical inequivalence claim，只是在精确展示 quotient 掉 coordinate labels 后损失了什么信息。

## 9. 得到的 observation poset

已经证明的关系可以写成

\[
\boxed{
F_n
\to
(\Sigma_{n,k})_k
\to
\Sigma_n
\to
(S_n,T_n),
}
\]

且

\[
(S_n,T_n)\to S_n,
\qquad
(S_n,T_n)\to T_n,
\]

但

\[
S_n\not\to T_n,
\qquad
T_n\not\to S_n.
\]

每一个 reverse failure 都有显式 finite Barlow counterexample。

仅这一点就足以否定“shell state 有一个统一 scalar 精度高低”的想法。

## 10. 与 coordinate-sensitive support moment 的关系

coordination-moment supplement 又给出了 observation poset 的另一条 branch。

对一个 selected target layer，coordinate-sensitive shell set 的 first moment 能恢复 signed `delta_k`；但 non-extreme layer cardinality 完全与 stacking 无关。

所以即使只在 **existence-only geometry** 内，也已经必须区分

\[
\text{coordinate-labelled membership}
\]

与

\[
\text{cardinality of that membership set}.
\]

这个差别在 path multiplicity 介入以前就已经存在。

## 11. P023/P024 后果 —— precision 应由 observation factorization 组织

Barlow examples 强烈指向一个更合适的抽象：precision 不是 scalar，而是 observation factorization order。

如果 observation `O_2` 是 `O_1` 的 deterministic function，那么 `O_1` 对这门 future language 至少同样有信息；如果二者互相都不能 factor，则它们不可比较。

这里：

- `Sigma_n` 可 factor 到 `S_n` 和 `T_n`；
- `S_n` 与 `T_n` 不能互相 factor；
- product observation `(S_n,T_n)` 仍不能恢复 `Sigma_n`。

这完全是 A2/P023/P024 已有 quotient/factorization principle 的 finite concrete specialization。

P022 应保留具体 geometry 与 counterexamples；如果以后把 abstract observation-poset theorem 提升为一般数学，归属应在上游，而不是让 P022 重复造母理论。

## 12. executable assets

新增：

- `src/enterprise_math/p022_barlow_observables.py`；
- `tests/test_p022_barlow_observables.py`。

测试编码了上述全部 strict separation examples，并逐项验证所有 forward forgetful maps。
