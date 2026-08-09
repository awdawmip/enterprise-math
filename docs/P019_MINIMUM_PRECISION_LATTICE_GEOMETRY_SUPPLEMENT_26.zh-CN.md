# P019 补充 26 —— Observation-Aware Future Language 与最小 Exact Relation Precision

状态：`RESEARCH WIP / EXACT LINEAR OBSERVATION + DYNAMICS SOLVER`

## 1. 为什么只看 dynamics 还不够

Supplement 25 解决了 integer affine dynamics 下的最小 exact partition。

但 future language 不只有“状态如何演化”，还包括“未来到底要问什么”。

即使所有 dynamics 都不读取某个 hidden relation，只要未来 observation 会直接查询该 relation，当前 quotient 仍然太粗。

所以 minimum exact relation state 必须同时由：

\[
\boxed{
\text{future operations}
+
\text{future observations}
}
\]

决定。

## 2. exact linear observation

考虑：

\[
\lambda(c)=w^Tc+b,
\qquad
w\in\mathbb Z^k,\ b\in\mathbb Z.
\]

partition matrix：

\[
A:k\to\ell.
\]

若存在 coarse coefficients：

\[
\bar w\in\mathbb Z^\ell
\]

使：

\[
\boxed{
w^T=\bar w^TA,}
\]

则：

\[
\lambda(c)
=\bar w^T(Ac)+b.
\]

所以 observation 可完全从 coarse state 读取。

常数 `b` 不产生额外 distinguishability。

## 3. P019-X96 —— linear observation descent 的 block-constant criterion

由于 partition matrix 的每个 fine column 是其 coarse block 的 basis vector，`w^T=bar w^T A` 当且仅当：

\[
\boxed{
w_i=w_j
\quad\text{对所有同 coarse block 的 }i,j.}
\]

也就是说：

> exact linear score 能在 coarse partition 上读取，当且仅当 coefficient vector 在每个 coarse block 内是常数。

coarse coefficient 就是该 block 的共同 coefficient。

## 4. P019-X97 —— observation family 的最粗 refinement

给定有限 observation family：

\[
W=\{w^{(1)},\ldots,w^{(r)}\}.
\]

对每个 fine coordinate `i`，定义 observation signature：

\[
\boxed{
\sigma_O(i)
=(w_i^{(1)},\ldots,w_i^{(r)}).
}
\]

在每个 current coarse block 内，只按该 signature 分组。

所得 partition：

\[
\Pi_O
\]

是保留所有 exact linear observations 的最粗 refinement。

证明直接：任何 exact partition 都不能把 coefficient signature 不同的 coordinates 留在同一 block；而 signature 相同的 coordinates 对所有 declared scores 完全可互换。

## 5. internal relation query 会自动要求 refinement

unit capacities 下：

\[
Z_{ij}=c_i-c_j.
\]

若 future query 要精确观察：

\[
Z_{01},
\]

其 coefficient vector：

\[
(1,-1,0,\ldots,0).
\]

若 `0,1` 当前在同一个 coarse block，它们 coefficients 不同，所以 X96 自动强迫 split。

因此：

> **查询一个已经 internalized 的 relation，本身就是 refinement demand。**

不需要额外人工标注“请提高精度”。

## 6. coarse relation query 不要求无意义细化

若当前 coarse groups 为 `A,B`，要观察 coarse total difference：

\[
C_A-C_B,
\]

fine coefficient在 `A` 内统一为 `+1`，在 `B` 内统一为 `-1`。

所以它已经 quotient-readable，不要求再拆 A/B 内部。

同理，capacity-weighted coarse relation：

\[
Z_{AB}=M_BC_A-M_AC_B
\]

对应 fine coefficients在每个 current coarse group 内仍为常数。

所以 solver 不会因为“询问 relation”就机械回到 singleton precision；只暴露实际被问题区分的 relation degrees。

## 7. P019-X98 —— operation + observation 的 minimum exact partition

先从 initial partition `Pi_0` 出发。

### 第一步：observation refinement

按所有 `w` coefficient signatures 细化，得到：

\[
\Pi_O.
\]

### 第二步：dynamics refinement

以 `Pi_O` 为 initial partition，运行 Supplement 25 的 matrix signature refinement，直到所有 future dynamics descend，得到：

\[
\Pi_*.
\]

则：

\[
\boxed{
\Pi_*
=
\text{同时保持 declared linear observations 与 affine dynamics 的最粗 exact refinement。}
}
\]

### 证明

任意 exact common refinement `R`：

1. 必须 refine `Pi_O`，否则某个 observation coefficients 在一个 `R` block 内不同；
2. Supplement 25 X95 保证从 `Pi_O` 出发得到的 `Pi_*` 是所有 dynamics-exact refinements 中最粗的；
3. 所以 `R` 必须 refine `Pi_*`。

得证。∎

## 8. branch predicate 的安全解释

若 piecewise future rule 的 branch condition 由某个 exact linear score：

\[
w^Tc+b
\]

经过 threshold/equality/sign 等 deterministic function 决定，那么只要该 score 能 descend，branch choice 就一定能从 coarse state 决定。

因此，把 branch score 加入 declared observations，是一个**充分且透明**的安全策略。

注意：若不同 hidden branch 最终恰有相同 coarse effect，实际最小 quotient 可能更粗；因此“先保存 exact branch score”是 branch-identity-sensitive language 的 exact solver，不应未经证明声称对所有 piecewise maps 都是绝对最粗 output-only quotient。

## 9. P019-X99 —— relation precision rank cost

current initial partition 有：

\[
\ell_0
\]

个 blocks；minimum exact partition 有：

\[
\ell_*
\]

个 blocks。

固定 grand total 时 relation dimension 分别：

\[
\ell_0-1,
\qquad
\ell_*-1.
\]

因此为了这组 future language 必须新增的 relation rank：

\[
\boxed{
\Delta d
=\ell_*-\ell_0.
}
\]

Supplement 19 的 Refinement Forest 说明 exact current refinement 恰可用同样数量：

\[
\boxed{\Delta d}
\]

条 independent internal weighted relations 补回。

所以 `Delta d` 是一个完全内生、纯整数的**minimum exact relation-refinement cost**。

它不代表执行时间/bit cost；它代表必须重新暴露多少 independent relation degrees。

## 10. precision selection 不再依赖经验精度

传统做法可能先选一个“看起来足够细”的 precision，再运行任务。

当前 solver 的顺序相反：

1. 声明 future operation/observation language；
2. 自动求最粗 exact partition；
3. 由 `ell_*-ell_0` 得到最低 relation refinement rank；
4. 只暴露这部分 relation detail。

所以：

\[
\boxed{
\text{required precision}
\text{由 future distinguishability 推出，
而不是先验指定。}
}
\]

这与 P018 的研究目标高度一致。

## 11. 实现与验证

新增：

- `src/enterprise_math/linear_observation_quotient.py`
  - exact linear observable descent；
  - observation-family signature refinement；
  - joint operation+observation minimum partition solver。
- `tests/test_linear_observation_quotient.py`
  - block-constant criterion；
  - observation-only minimum split；
  - hidden internal relation query forces refinement；
  - coarse relation query does not over-refine；
  - operation+observation joint solver；
  - all 4-coordinate candidate partitions brute-force common-coarsest check；
  - affine observation constant invariance。

## 12. 前人工作纪律

observable congruence、behavioral equivalence、minimal realization、partition refinement 等领域有成熟工具。

P019 不把“保留所有未来可观测区别”作为原创思想。

当前具体连接是：

\[
\boxed{
\text{future language}
\to
\text{minimum partition precision}
\to
\text{weighted relation state}
\to
\text{exact refinement rank cost}.
}

## 13. 下一步

1. 将 `Delta d` 与 Supplement 24 relation quantum `g` 合成二维 precision cost：relation rank + relation quantum；
2. 对 selected modular/congruence observations，寻找比 exact-score preservation 更粗的合法 quotient；
3. 处理 predicate-controlled affine dynamics 的 output-equivalence 情形，允许隐藏 branch identity 但保持 coarse result exact；
4. 将 solver 接入 P018 adaptive precision selection；
5. 用实际 P021 witness queries 作为 observations，计算哪些 relation degrees 是未来 causal composition 真正需要的。
