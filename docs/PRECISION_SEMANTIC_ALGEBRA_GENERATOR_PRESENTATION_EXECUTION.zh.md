# Semantic Algebra、Generator Presentation 与 Execution Representation

状态：`FOUNDATION-FACING RESEARCH BRIDGE / NONCANONICAL`

Researcher-ID：`R-8F3K`

Representation-Pareto synthesis 已经把 semantic precision 与 runtime implementation resources 分开。最新 capability-selection 结果还要求再抽出一层：**由哪些 selectable primitive generators 构成的 presentation**，并不能由 generated semantic algebra 单独决定。

本文不新增 Foundation Question，只进一步细化 future-law design 的 object model。

## 1. 三种不同 future-law objects

对 declared task，必须区分：

### A. Generated semantic algebra

Closure 后真实存在的 exact operations / effects，以及它们的 composition law。

它回答：

`future law 最终能够做什么？`

### B. Generator / capability presentation

可供选择的 named primitive actions / channels，以及它们各自的 cost、provenance 与 semantic ownership。

它回答：

`哪些 atomic capabilities 被允许用来构造这份 law？`

### C. Execution representation

Generator set 选定后，真正 runtime 采用什么 operational encoding：generator tables、caches、monoid tables、formulaic normal forms、CRT channels、circuits 等。

它回答：

`已经选定的 exact law 怎样被执行？`

三种对象可以独立变化。

## 2. 相同 semantic algebra 可以有不同 minimum design

Set-Cover action family 给出 sharp witness。

固定 universe size m。比较两个 catalogues，两边都有 m+1 个 named actions，也都生成完整 Boolean semilattice `2^[m]`，composition 都是 OR。

- Catalogue A：全部 singleton actions + 一个 duplicate singleton。Minimum full-precision subset size=m。
- Catalogue B：全部 singleton actions + 一个 full-universe action。Minimum size=1。

所以两边：

- generated semantic effects 完全相同；
- abstract OR composition law 完全相同；
- named action count 相同；

但 minimum precision-preserving generator design 不同。

因此 semantic algebra 不能决定自己的 design-presentation cost。

## 3. Easy execution 不推出 easy capability design

Parent Set-Cover compiled matrices 的任意 action word 都只需 OR set masks。Actions commute、idempotent，word normalization 可用 logarithmic parallel depth。

但 minimum preserving action selection 仍然是 Minimum Set Cover。

更强地，monotone-universality compiler 可以实现任意 finite upward-closed preserving geometry，而 compiled executor 仍然只是 OR semilattice。

所以 execution-algebra 的简单性并不能 generic 地推出 matroid / basis / optimization structure 简单。

## 4. Given-subset verification、optimization、execution 是三种问题

一个 fixed selected subset 的 feasibility 往往很容易检查，即使 optimum 很难找。

在 Set-Cover family 中：

- 执行 word：OR masks；
- 验证 proposed preserving subset：OR masks 后检查 full target coverage；
- 求 minimum preserving subset：Set Cover。

三者属于不同 computational questions。

“law complexity” 不应把它们合并。

## 5. Presentation 本身属于 resource contract

Generator 不是 generated algebra 中一个可以随意忘掉名字的元素。它是一个 atomic selectable resource，可能具有独立的：

- acquisition / storage cost；
- provenance；
- legality / DOMAIN；
- physical / semantic ownership；
- future language availability。

所以即使 generated algebra 不变，替换 generator presentation 也可能实质性改变 design problem。

## 6. Execution representation 位于 generator selection 下游

Generator / capability family 选定以后，同一个 exact future law 仍然有很多 runtime representations：

- sparse generators；
- literal word caches；
- semantic effect automata；
- Cayley tables；
- formulaic normal forms；
- coefficient factorizations / CRT channels。

这些属于 chosen law 的 representation Pareto。

优化这些 runtime representations，并不能 generic 地回答上游本来应该选哪些 generators。

## 7. Revised architecture

Future-law design 可以按如下 pipeline 分层：

`declared semantic target`

`-> choose / synthesize generator presentation`

`-> close to generated semantic algebra`

`-> choose exact runtime representation/compiler`

`-> execute declared futures`。

不同 questions 属于不同 arrows。

## 8. Inverse design 与 forward execution

最新结果提示一个尤其重要的 distinction：

- **forward execution**：给定 primitive generator word / subset，求它的 semantic effect；
- **inverse design / synthesis**：给定 target semantic requirement / effect，寻找 minimum-cost primitive expression 来实现它。

Forward computation 可以 formulaically trivial，而 inverse synthesis 仍然 combinatorially hard。

这是下一条 research bridge，不应继续统称成一个 generic “operation complexity”。

## 9. Foundation routing rule

以后分析 future law 时，分开问：

1. 所需 exact semantic algebra 是什么？
2. 哪些 primitive generator / capability presentations 被允许？
3. Selected presentation 必须实现什么 semantic target？
4. 验证 / 合成满足要求的 generator subset 有多难？
5. Selection 完成后，怎样选择 exact runtime representation 才最省目标 resource vector？

不能因为第1或第5项简单，就推断第2–4项也简单。

## 10. Evidence routes

当前 research evidence 包括：

- action-alphabet Set Cover 与 monotone universality；
- 同一 compiled action families 的 formulaic OR execution；
- same generated monoid 下 minimum preserving basis size 1 vs m；
- constrained modular-sensor Set Cover；
- semantic word-normalizer 与 formulaic-algebra Pareto generations。

全部仍是 Draft / noncanonical evidence。

## Prior-art / status

Generating sets、presentations、semilattices、Set Cover 与 compiler/runtime distinction 都是标准既有数学 / CS。Enterprise Math 的价值是 precision-first architecture：严格区分 semantic algebra、primitive capability presentation 与 execution representation。

No new FQ。无 canonical-main 或 `EXECUTABLE_CHECKED` claim。`CI_NOT_REQUIRED_FOR_RESEARCH`。Hard block：`NONE`。
