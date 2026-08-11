# Design-Selection Complexity 与 Execution-Algebra Complexity

状态：`RESEARCH BRIDGE / NONCANONICAL`

Researcher-ID：`R-8F3K`

一个 future-operation family 可以非常容易执行，同时仍然很难做**最小设计**。这是两种不同的 computational questions。

现有 Set-Cover / monotone-capability compiler 给出一个 sharp same-family witness：它的 action matrices 两两 commute、idempotent，并具有 bitmask-OR word normal form；但 minimum precision-preserving generator selection 仍然精确等价 Minimum Set Cover，而 generic preserving-family geometry 甚至可以实现任意 finite monotone set system。

## 1. 同一个 compiled action family

对 Set Cover universe elements j 与 candidate sets `S_a`，parent compiler 使用 state coordinates `e_j,f_j`。

Action a：

- 若 `j in S_a`，则 `e_j -> f_j`；
- 否则 `e_j -> e_j`；
- 所有 `f_j -> f_j`。

这些 actions 是 0/1、pairwise commuting、idempotent。

Parent theorem 已证明：

`selected actions preserve full STATE_KERNEL precision`

当且仅当

`selected actions preserve full INTEGER_MODULE precision`

当且仅当

`selected candidate sets cover the universe`。

所以 minimum preserving action selection 精确就是 Minimum Set Cover。

## 2. Exact word execution 只是 union

把 action a 的 candidate set 表示成 universe bitmask `m(a)`。

对任意 literal word w 定义：

`U(w)=w 中出现的 action masks 的 OR`。

那么 compiled matrix 的 exact word effect 只取决于 U(w)：universe coordinate j 是否从 `e_j` 激活到 `f_j`，只看 w 中是否至少有一个 action cover j。

因此：

`U(uv)=U(u) OR U(v)`。

Action order 与 repetition 全部从 exact effect 中消失。

所以同一批“minimum generator design 等价 Set Cover”的 matrices，其 execution algebra 同时又是 formulaic commuting-idempotent semilattice。

## 3. Word normalization 只有 logarithmic parallel depth

长度 H 的 action word 对应 H 个 set masks。

Balanced OR reduction 给出：

`normalization depth=ceil(log2 H)`。

若 universe 有 m 个 elements、按 bit-level work 计，normalization 大约需要：

`m*(H-1)`

个 bit ORs。

Formulaic executor 完全不需要做 matrix multiplication。

所以相对于 compiled instance size，future execution 很简单。

## 4. 给定 subset 的 feasibility verification 也很容易

给定一个 selected action subset A，只要 OR 对应 masks 并检查是否得到 full-universe mask，就能判断 full precision 是否 preserved。

所以该 family 中：

- 执行一个 declared word：easy OR normalization；
- 验证一个 proposed preserving subset：easy union / full-mask test；
- 找 minimum preserving subset：Set Cover optimization。

Verification / evaluation 与 optimization 因而严格分层。

## 5. Same-family NP-hardness boundary

Set Cover reduction 是 polynomial-size。

所以 minimum-design problem 在如下极简 execution family 中仍然 NP-hard：

- commuting；
- idempotent；
- formulaic；
- semilattice-valued；
- word normalization 可用 parallel OR。

因此 generic capability-design difficulty 不能归因于：

- difficult word dynamics；
- noncommutativity；
- long future closure；
- complicated operation evaluation。

组合难度位于**到底要保留哪些 generators**，而不是保留下来的 generators 怎样 compose。

## 6. Strong monotone universality 也保留 easy executor

Parent universality theorem 从任意 nonempty upward-closed preserving family P 出发。

设其 inclusion-maximal false subsets 为：

`F_1,...,F_t`。

给每个 `F_i` 一个 Set-Cover witness coordinate，并令 action a cover witness i 当且仅当：

`a notin F_i`。

Compiled action family 仍然是完全相同的 Set-Cover matrix form。

所以 action a 有一个 t-bit effect mask：

`m(a)_i=1 iff a notin F_i`，

任意 literal word 的 execution 再次只是 bitwise OR。

但 preserving subsets 精确等于 P。

因此任意 finite monotone design geometry 都可以和一个 formulaic OR execution algebra 同时存在。

## 7. Minimal preserving families 可以是任意 antichain

因为任意 finite monotone P 都可实现，所以 inclusion-minimal preserving subsets 可以形成任意 antichain。

它们可以：

- sizes 不同；
- 数量指数多，达到 Sperner bound；
- 不存在 unique least subset；
- 不满足 generic matroid / submodular / basis assumptions。

这些复杂 design geometry 都不会迫使 execution algebra 变复杂；compiled executor 仍只是对 maximal-false witness mask 做 OR。

## 8. Complexity axes 是正交的

至少有三种不同 computational resources：

### Execution complexity

给定一个 word，求 exact semantic operation / effect。

本 family：OR masks，parallel depth logarithmic。

### Feasibility / evaluation complexity

给定 proposed capability subset，判断是否 preserve target precision。

本 family：union / full-mask check。

### Design / optimization complexity

找 minimum-cost preserving subset、枚举所有 minimal preserving subsets、描述 basis geometry。

本 family：Set Cover / arbitrary monotone set-system complexity。

一条轴不能从另一条轴推断。

## 9. “Easy algebra” 不推出 “easy basis”

一个很诱人的 generic heuristic 是：

> operations 若 commute、idempotent，并有简单 normal form，那么 minimum precision-preserving generator basis 应该也容易求、或至少有 canonical structure。

Same-family reduction 直接反驳这一点。

Algebraic composition law 约束的是 selected generators **执行时怎样 interaction**；minimum-basis structure 问的是哪些 subset 能满足一个 global semantic requirement。这是不同层。

## 10. 与 Stage131 representation Pareto 的关系

即使 action alphabet 已经选定，还可以继续优化它的 word law 怎样表示：generators、caches、monoid tables、formulaic normal forms。

但在此之前还有一个更上游问题：到底应该选哪些 generators 存在。

因此完整 design problem 至少分三层：

1. capability selection / semantic basis design；
2. exact execution-law representation；
3. runtime execution of selected representation。

优化第2层不能 generic 地解决第1层。

## 11. 与 constrained modular sensors 的关系

Constrained modular-sensor Set Cover generation 在 coefficient channels 上给出同一 architecture：

- sensors 已选定后，计算 joint residue code 很容易；
- 从 constrained catalogue 选 minimum sensor subset 仍可 Set Cover-hard。

Action 与 coefficient 两条线共同支持一个 generic routing rule：

> **不要从固定 selected representation 的 execution complexity 推断 design-selection complexity。**

## 12. Arbitrary monotone family 的 input-size caveat

Strong universality compiler 可能需要每个 maximal false subset 一个 witness coordinate。该 witness universe 本身可能随 action count 指数增长。

所以 universality statement 说明的是“design geometry 可实现到什么程度”，不声称任意 succinct monotone predicate 都有 polynomial-size OR compilation。

Polynomial NP-hardness statement 来自普通 explicit Set Cover specialization。

## 13. Executable evidence

本 branch 新增 OR-mask executor，并验证：

- literal matrix word effect = formulaic union-mask effect；
- balanced normalization depth；
- 同一 matrices 上 STATE_KERNEL / INTEGER_MODULE preserving subset 精确等于 Set Cover；
- 3-action 的全部 nonempty upward-closed preserving families（19种）都保留 exact predicate，同时 bounded literal words 仍然全部由 OR 执行。

## Owner-local assets

- `src/enterprise_math/set_cover_formulaic_execution.py`；
- `src/enterprise_math/monotone_design_formulaic_execution.py`；
- 对应 tests；
- 本双语 theorem note。

Parent #375 generation 继续拥有 generic action-capability Set Cover 与 monotone-universality theorem。

## Prior-art / status

Set Cover、monotone Boolean function、semilattice 与 parallel OR reduction 都是标准既有数学 / CS。本文只拥有 Enterprise Math 的 cross-layer 结论：minimum semantic design complexity 与 exact execution-algebra complexity 是独立资源。

无 repository strict CI、无 `EXECUTABLE_CHECKED`、无 canonical claim。`CI_NOT_REQUIRED_FOR_RESEARCH`。Hard block：`NONE`。
