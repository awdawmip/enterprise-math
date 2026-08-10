# Proper Witness Projection 保持 Profinite Exactness

状态：`RESEARCH BRIDGE / NONCANONICAL`

Finite-branch 与 witness-compactness 结果可以进一步压成一个结构 theorem：只有当**witnessed relation 本身 exact**、**completed unlabelled semantics 仍然是同一个 existential projection**、并且**witness projection closed / proper** 时，existentially forgetting witness 才能安全保持 profinite exactness。

## 1. Exact witnessed relation

设 W 是 compact Hausdorff witness space，并且 arithmetic completion 不改变 W 本身。

令

`R_Z subseteq Z^n x W`

为 exact witnessed-state relation。

exact unlabelled state set 是 projection：

`S_Z = pi(R_Z)`，

其中

`pi: Z^n x W -> Z^n`。

有限 labelled relation 就是最简单例子：W 是 finite discrete set。

## 2. 先 completion witnessed relation，再忘掉 witness

把 integer state 嵌入 profinite state space，并假设 completed witnessed relation 满足

`R_hat = closure(R_Z) subseteq Z_hat^n x W`。

这就是 state+witness relation 的 **joint profinite exactness**。

另外独立要求 completed unlabelled world law 在 semantics 上仍然是

`S_hat = pi(R_hat)`。

这叫 **projection-faithfulness**：completion / coefficient collapse 没有在所有 completed witness branches 之外制造额外 unlabelled states。

Coefficient ghost product 正好在这里失败：completed product-zero set 比 completed finite factor-labelled relation 的 projection 更大。

## 3. Compact witness 让 existential projection 成为 closed map

因为 W compact，而 `Z_hat^n` Hausdorff，projection

`pi: Z_hat^n x W -> Z_hat^n`

是 closed map。

对任意 relation R：

- continuity 给出
  `pi(closure(R)) subseteq closure(pi(R))`；
- pi 的 closedness 给出反向 inclusion，因为 `pi(closure(R))` 本身 closed 且包含 `pi(R)`。

所以

`closure(pi(R)) = pi(closure(R))`。

这正是 existential witness elimination 所需要的 topological commutation law。

## 4. Proper-witness exactness theorem

在以下三项成立时：

1. `R_hat=closure(R_Z)` —— witnessed relation joint profinite-exact；
2. `S_hat=pi(R_hat)` —— completed unlabelled semantics 仍是同一个 witness projection；
3. W compact —— witness projection closed / proper；

得到：

`closure(S_Z)`

`= closure(pi(R_Z))`

`= pi(closure(R_Z))`

`= pi(R_hat)`

`= S_hat`。

因此 existentially quantified unlabelled law 自身 profinite-exact。

## 5. Finite disjunction 是最简单推论

对 finite branch set Lambda，取 W=Lambda 的 discrete topology。

W 自动 compact。

若每个 labelled branch profinite-exact，则 finite witnessed relation profinite-exact；若 completed law 仍保持这些 branches 的 literal union，则 projection-faithfulness 成立。

于是 theorem 直接恢复 finite-disjunction exactness result。

## 6. 三种互相独立的 failure mode

Theorem 精确定位 existential descent 的三种失败。

### A. Witnessed relation 自身不 exact

某个固定 nonlinear branch 可能只有 completion-state solution，没有 exact state solution。于是

`R_hat != closure(R_Z)`。

这是 branch-level profinite ghost / descent failure。

### B. Unlabelled completion 不 witness-faithful

Witnessed relation 自己可以完全 exact，但 coefficient collapse 把 unlabelled syntax 扩大。

Finite factor labels 的 product ghost 是 sharp example：每个 fixed labelled factor 都有 local blocker，但 completed product equation 仍产生 mixed-component roots。

于是

`S_hat != pi(R_hat)`。

### C. Witness projection 不 proper / closed

若 witness space 不 compact，projection 未必与 closure 交换，witness 可以逃向 infinity。

Infinite-label support

`S_M={k:M|k}`

是离散算术压力测试：每个 finite precision 都有 witnesses，却没有一个 fixed witness 能通过全部 precisions。

## 7. 与 quantifier order 的关系

这个 topological theorem 就是 quantifier exchange

`forall precision exists witness`

`=> exists coherent witness in the completion`

的结构版本。

Compact / proper witness projection 防止 existential witness 在 limit 中消失。

而 completed witnessed relation 到 exact integer state 的 state descent，仍然包含在 hypothesis1 中。

所以此前 two-stage routing 在适当条件下可以被压成一个 commutative diagram：

`exact witnessed relation --closure--> completed witnessed relation`

`          | projection                 | projection`

`          v                            v`

`exact unlabelled set --closure--> completed unlabelled set`。

Profinite exact descent 就是要求这个 square 交换，并且 horizontal completion 不引入 ghost components。

## 8. 为什么 semantic projection hypothesis 不能省略

不能先把某个 algebraic encoding 做 modular reduction，然后自动假设它等于 completed witnessed relation 的 projection。

这个 equality 自身需要 theorem。

Finite union 的 product encoding 在 integral domain 中 faithful；但 coefficient collapse 到 zero-divisor ring 后，zero set 可以严格大于 branch projection。

因此：**semantic projection 应优先，algebraic encoding 是 secondary representation，除非已证明它保存 semantics。**

## 9. 更一般的 witness space

Compactness 是一个干净充分条件，不是唯一可能条件。更一般地，只需要 witness projection 在相关 completed relation 上表现为 closed / proper map。

某条 route 可以在没有全局 compact witness universe 的情况下，用更弱的 route-specific theorem 证明这一点。

因此项目应记录真正使用的 weakest property：

`projection of relevant closed witnessed-state sets remains closed`。

## 10. Prior-art boundary

Compact fibers 下的 closed projection、proper maps、topological closure 与 existential projection 都是标准既有 topology。Enterprise Math 在这里的 precision-routing 结论是：

> **existentially forgetting witness 要安全穿过 completion，必须同时保 witnessed-state exactness、semantic projection faithfulness 与 witness-projection properness。**