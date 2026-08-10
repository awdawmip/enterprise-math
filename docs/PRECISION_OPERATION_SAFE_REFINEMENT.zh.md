# Coarsest Operation-Safe Semantic Refinement

状态：`RESEARCH BRIDGE / NONCANONICAL`

Semantic precision join 有时可以通过增加 state distinctions 来实现，而不必改变 representation type。对有限 states 与有限个 total unary future operations，存在唯一的**最粗** observational refinement，使全部 required operations 都能安全 descend。

## 1. Problem

设 X 是有限 fine-state set。

设 `E_0` 是当前 observational equivalence / partition。

设 U 是 declared future language 必须在 quotient 上执行的一族有限 total unary operations。

Operation u 对 equivalence E 安全，当且仅当：

`x E y -> u(x) E u(y)`。

我们要找最大的 equivalence

`E_* subseteq E_0`

使每个 `u in U` 都 preserve `E_*`。

这就是实现 declared operation capability 所需要的最小额外 state precision。

## 2. Refinement operator

定义

`Phi_U(E)`

`= E intersect intersection_(u in U) (u x u)^(-1)(E)`。

partition 语言下，就是：在每个当前 block 内，按所有 required operations 所到达的当前 target-block vector 继续 split states。

从 `E_0` 开始迭代：

`E_(k+1)=Phi_U(E_k)`。

每一步只会保持或细化 partition。

## 3. Finite termination

若某一步严格变化，至少有一个 partition block 被 split，因此 block count 至少增加1。

在 |X| 个有限 states 上，严格步骤最多：

`|X| - number_of_blocks(E_0)`。

所以迭代会在有限步内到达 fixed point。

这个 fixed point 对当前 total-unary operation family 是 exact stop certificate。

## 4. Fixed point operation-safe

在 fixed point：

`E_*=Phi_U(E_*)`。

所以对每个 `u in U`：

`E_* subseteq (u x u)^(-1)(E_*)`，

也就是

`x E_* y -> u(x) E_* u(y)`。

因此所有 required operations 都唯一 descend 到 `E_*` quotient。

## 5. Coarsest / maximal property

设 F 是任何满足

`F subseteq E_0`

且被全部 U operations preserve 的 equivalence。

则可归纳得到：

`F subseteq E_k`

对所有 k 成立。

因为若 `F subseteq E_k`，operation preservation 给出

`F subseteq (u x u)^(-1)(E_k)`

对每个 u 成立，于是

`F subseteq Phi_U(E_k)=E_(k+1)`。

所以最后：

`F subseteq E_*`。

因此 `E_*` 是原 observational equivalence 内最大的 operation-safe equivalence，也就是实现全部 required operations 的**最粗 state refinement**。

这个 repair 唯一。

## 6. 一次 split 未必够

Operation safety 可能只有在下游 block 自己被拆开后，才暴露新的 distinction。

Sharp four-state cascade：

initial：

`{0,1}|{2,3}`。

定义一个 operation：

`0->2`, `1->3`, `2->0`, `3->3`。

第一次 iteration 只 split 下游 block：

`{0,1}|{2}|{3}`。

此时0与1的 targets 才落进不同 blocks，所以第二次 iteration 再 split 第一块：

`{0}|{1}|{2}|{3}`。

因此 semantic repair 一般需要闭包到 congruence fixed point，不能只加一次 local response signature。

## 7. 与 semantic precision join 的关系

假设 task join 同时要求：

- 至少保留 `E_0` 已有 state distinctions；
- operation capabilities U。

若 representation class 允许对同一个 finite X 做任意 partition refinement，那么这个 join 一定可实现：把 `E_0` 换成 `E_*`。

而且 theorem 给出 canonical minimal lift。

这正是 scalar-modulus nonrealizable join 的正面对照。

## 8. 当前 join 不可实现时有两种不同结局

Semantic-preorder 路线现在可以区分：

### A. Join 可以靠 state splitting 实现

Required operations 都是同一个 fine state X 上的 ordinary functions。

此时 coarsest operation-safe refinement `E_*` 给出 canonical state lift。

### B. Join 在当前 representation class 内根本不可实现

例如：同时要求 mod `p^2` numeric detail 与 generic integral-domain branch reflection，并把 states 限制为 scalar quotients `Z/MZ`。

没有任何 modulus 能满足。

在这类 representation family 内继续 split residue classes 也无法恢复缺失的 algebraic law。

必须改变 representation type，例如显式保 witness / branch data。

所以“提高 precision”可能意味着：

- 在原 representation 中 refine state partition 到 required congruence；或
- 离开当前 representation family，增加新的 semantic channel。

## 9. 与 safe-operation monoid 的关系

给定一个 quotient，它的 safe operation family 是 preserve 该 equivalence 的 transformations。

这里反过来：先声明 required operations U，再 refine quotient，直到 U 被包含进 safe-operation family。

因此 safe-operation analysis 与 semantic refinement 是两个互补 design questions：

`given quotient -> which operations survive?`

vs

`given required operations -> what is the coarsest quotient that supports them?`

这给 A2 safe-operation algebra 与 task-relative semantic precision preorder 之间提供了直接 constructive bridge。

## 10. DOMAIN / partial-operation boundary

Theorem 假设 total unary operations 作用于同一个固定 fine-state set。

对 partial / guarded operations，definedness 自身就是 future-visible state。必须先保留 DOMAIN channel，或消费 partial-operation quotient machinery。若某 operation 在一个 equivalence class 的部分 states 上 undefined，仅按 target blocks split 并不够。

所以本文只是 total-operation core，不替代 FQ-006 / P024 guarded semantics。

## 11. Prior-art boundary

Congruence refinement、deterministic automaton partition refinement 与 invariant equivalences 都是标准既有数学 / 计算机科学。Enterprise Math 在这里得到的 semantic precision 解释是：

> **如果某项 future operation requirement 可以只靠增加 state detail 修复，那么存在唯一 coarsest operation-safe state refinement；否则必须改变 representation type 本身。**