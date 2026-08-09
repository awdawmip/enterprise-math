# A3 ↔ A4 ↔ A2/P023 Bridge — Supplement 08

状态：`ACTIVE RESEARCH NOTE`  
范围：递归 antichain composition、online legal compression，以及它相对于 witness-count language 的边界

## 1. 问题

Stage 06 通过枚举 represented chains 再 Pareto-prune cost vectors 得到精确 `k`-stage frontier。直接枚举在概念上正确，但随 depth 快速增长。

关键问题是：已经压缩过的 frontier state 能否直接继续向未来扩展，而不恢复之前删除的 paths？

可以。

## 2. B28 — antichain convolution theorem

令

\[
F^{(p)}_{xy}\subset\mathbb N^p
\]

为从 `x` 到 `y` 的精确 `p`-stage frontier，

\[
F^{(q)}_{yz}\subset\mathbb N^q
\]

为从 `y` 到 `z` 的精确 `q`-stage frontier。

对 `u in N^p` 与 `v in N^q`，记 concatenation 为

\[
u\Vert v\in\mathbb N^{p+q}.
\]

定义 frontier convolution

\[
\boxed{
(F^{(p)}\star F^{(q)})_{xz}
=
\operatorname{ParetoMin}
\bigcup_y
\{u\Vert v:u\in F^{(p)}_{xy},\ v\in F^{(q)}_{yz}\}.
}
\]

则

\[
\boxed{
F^{(p+q)}_{xz}
=(F^{(p)}\star F^{(q)})_{xz}.
}
\]

### 证明

任意 represented `(p+q)`-stage chain 在第 `p` stage 后都有唯一 split state `y`。其 prefix/suffix cost vectors 分别属于 `F^(p)_xy` 与 `F^(q)_yz` 所对应的完整 cost sets。

每个 prefix cost 都被某个 Pareto-minimal prefix `u` coordinatewise 支配；每个 suffix cost 同样被某个 Pareto-minimal suffix `v` 支配。因此整个 chain cost 被 `u||v` 支配。

反过来，每个 frontier point `u`、`v` 自己就由真实 represented prefix/suffix chain 实现，在 `y` 处拼接后 `u||v` 也被真实实现。

所以取 Pareto minima 后精确得到 `(p+q)`-stage frontier。

## 3. B29 — canonical frontier composition 的 associativity

frontier convolution 在 canonical antichain 层面满足结合律：

\[
\boxed{
(F^{(p)}\star F^{(q)})\star F^{(r)}
=
F^{(p)}\star(F^{(q)}\star F^{(r)}).
}
\]

因为两边都等于 total depth `p+q+r` 的唯一精确 frontier `F^(p+q+r)`。

因此 finite-depth support evolution 得到一个 antichain-valued associative composition law。

这并不把 arbitrary A4 relations 重新解释成 A3 relation states；它只是 A3-generated metric-support subclass 内部的计算规律。

## 4. B30 — dominated-prefix erasure 对 existence/budget semantics future-safe

设同一 depth 的两个 prefix cost vectors 满足

\[
u\preceq v.
\]

对任何可能 future suffix cost `w`，都有

\[
\boxed{u\Vert w\preceq v\Vert w.}
\]

所以任何能够接受 `v` 的 continuation 的 future budget，也一定能接受对应的 `u` continuation。

因此 dominated prefix 对任何后续 existential staged-budget query 都**永远不会重新变成必要状态**。

这给出一个 online P023-compatible compression rule：

> 每完成一段 stage，就删除所有 dominated path-cost vectors，只保留 Pareto antichain；继续做 future antichain convolution 时，对所有后续 existence/budget queries 仍然精确。

这个 language 下不需要恢复 hidden path identity。

## 5. Dynamic recurrence

定义 one-stage matrix：

\[
F^{(1)}_{xy}=\{(\rho(x,y))\}.
\]

则

\[
\boxed{
F^{(k+1)}=F^{(k)}\star F^{(1)}.
}
\]

所以 arbitrary finite-depth frontiers 可以通过反复 frontier convolution，并在每一步立刻 Pareto-prune 来生成。

reference implementation 保持 finite + exact，目前不主张已经是 optimized multiobjective shortest-path engine。

## 6. B31 — 负边界：Pareto compression 丢失 witness multiplicity

frontier 保留的是**每个 budget 下是否存在 witness**，而不是有多少 represented intermediate witnesses 满足该 budget。

取相同 capacities `10`。

### System A

Totals：

\[
(0,9,20)
\]

对应 normalized positions `0,0.9,2`。

对 endpoints `0,2`，intermediate costs 为

\[
(0,2),\quad(1,2),\quad(2,0),
\]

因此 Pareto frontier 是

\[
F=\{(0,2),(2,0)\}.
\]

budget `(2,2)` 下共有三个 represented witnesses。

### System B

Totals：

\[
(0,9,11,20)
\]

新增 normalized position `1.1`。

额外 cost 为

\[
(2,1),
\]

它被 `(2,0)` 支配，所以 Pareto frontier 完全不变：

\[
F=\{(0,2),(2,0)\}.
\]

但 `(2,2)` budget 下已经有四个 represented witnesses。

所以两个 systems 可以拥有完全相同的 staged existence frontier，却有不同 witness multiplicities：

\[
\boxed{
F\text{ 对 witness-count / multiplicity languages 不 future-safe。}
}
\]

如果 future language 包含 A4 witness spectra、overlap counts 或任何依赖 common-target 数量/身份的量，就必须增加状态。

## 7. 压缩层级进一步明确

合法状态取决于精确 observable language：

### Existence-only staged budgets

Pareto antichain 足够，dominated paths 可以在线安全删除。

### Labeled witness identity

必须保留足以回答 identity-sensitive operations 的 witness 信息。

### Witness multiplicity / spectra

必须保留 count-enriched state；plain Pareto frontier 由 B31 明确不足。

这与 A4 之前对 relation truth、witness count `W_k`、group/event spectra 的区分一致。

## 8. 与 E001 的关系

E001 工程往往首先关心 collision/common target 是否存在，后续 diagnostics 又可能统计 candidate witnesses 或 materialized target memberships。

B30/B31 给出精确边界：

- existence-only broad phase 可以安全 Pareto-prune dominated budget paths；
- 测量 witness multiplicity 的 diagnostic 不能把这份 pruned state 当成 count-complete state。

## 9. 与 P023 和 A3 piecewise refinement 的关系

B30 是正向 future-safety theorem，因为 future language 已经明确固定，而且 dominance 对每一个允许 continuation 都保持。

这与 arbitrary partition refinement 不同。A3 piecewise 结果说明，无控制地增加 detail 可能先暴露 branch effects 却不暴露 selector，反而破坏 exactness。

所以项目级原则不是“多 prune”或“多 refine”，而是：

\[
\boxed{
\text{先确定 future algebra，再证明 state transform 是它的 congruence。}
}
\]

## 10. Prior-art discipline

Pareto dynamic programming、multiobjective path algebra、antichain pruning、dominance-preserving continuation 都有成熟前人工作。当前项目特有的研究目标，是把它们作为 A3→A4→P023 support-language 链中的合法有限状态压缩机制，并明确给出 witness-multiplicity 边界。

## 11. Executable reference

reference layer 新增：

- 按 stage depth 的 antichain frontier matrices；
- exact frontier convolution；
- recursive frontier powers；
- associativity regression checks；
- B31 same-frontier / different-witness-count regression。
