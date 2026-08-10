# Semantic Precision = State Detail × Future Capability

状态：`FOUNDATION-FACING RESEARCH BRIDGE / NONCANONICAL`

当前研究已经反复表明：“区分更多 state detail”与“保留更多 future semantics”是两组独立 precision coordinates。一个 raw quotient 可以 observationally 更细，却同时失去 declared future language 所需要的 operation 或 logical law。

本文不新增 Foundation Question，而是细化 precision comparison 的 routing。

## 1. Observational refinement 只是一个坐标

对 representation P，令

`E(P)`

表示当前 observation / state quotient 在 fine states 上诱导出的 equivalence relation。

kernel 越小，state detail 越高：

`E(P2) subseteq E(P1)`。

这是普通 partition / quotient 意义上的 refinement。

但它并没有说明哪些 future actions、logical laws 或 witness semantics 仍能穿过这个 representation。

## 2. Future semantic capability 是第二个坐标

对 declared future theory T，令

`C_T(P)`

表示在 representation P 上仍然安全成立的 task-relevant semantic capabilities。

根据 task 不同，可以包括：

- preserve quotient 的 operations；
- DOMAIN / definedness channels；
- branch / witness identity reflection；
- 在 declared hypotheses 下的 exact IMAGE reflection；
- 解释 algebraic encoding 所需的 coefficient laws；
- future operation 可能重新激活的 provenance / history distinctions。

这个 set 是**declared-task relative** 的，不是要罗列 P 的全部数学性质。

## 3. Task-relative semantic precision preorder

定义

`P2 >=_T P1`

当且仅当同时满足：

1. `E(P2) subseteq E(P1)` —— P2 observationally 至少同样细；
2. `C_T(P1) subseteq C_T(P2)` —— P2 不会丢掉 P1 已拥有的 declared capabilities。

所以 semantic refinement 是一个 product-style preorder：

`state detail x safe future capability`。

Raw quotient refinement 只是这个 preorder 的第一个 projection。

## 4. Partition refinement 不保证 operation safety

Unary operation 能穿过 partition，当且仅当 equivalent inputs 的 outputs 仍 equivalent。

更细 partition 可以破坏这个条件：两个 inputs 仍 equivalent，但它们的 outputs 被 finer partition 分开了。

反过来，足够细甚至 discrete 的 partition 会消除 equivalence constraints，使某个 coarse quotient 上 unsafe 的 operation 变 safe。

所以 safe-operation spectrum 对 raw partition refinement 在两个方向都不单调。

这已经在 A2 safe-operation algebra 路线中出现。

## 5. Coefficient refinement 重现同样的 nonmonotonicity

对 prime p：

`Z/p^2 Z -> Z/p Z`

是 numeric refinement map：mod `p^2` 能区分更多 residues。

但是：

- mod p 是 field / domain，generic product-zero branch logic 可以 reflection；
- mod `p^2` 有 zero divisors，这项 logical capability 消失。

如果 branch semantics 属于 T，那么即使 raw numeric refinement 存在，这两个 representations 仍然 semantic incomparable。

如果 branch semantics 对 T 无关，那么 mod `p^2` 又可以恢复为该 task 下的 relevant refinement。

所以 precision order 真正是 future-language relative 的。

## 6. Forward syntax preservation 不能修复已丢失 capability

Quotient homomorphism 仍会完美保留 polynomial evaluation：

`phi(t(x))=t(phi(x))`。

所以 representation 可以保住 written algebraic syntax，却丢掉 exact interpretation 需要的 reflection law。

这说明 capability 必须按 semantics 显式记录，不能因为 collapse 后公式长得一样，就自动认为 logical law 还在。

## 7. Semantic join 未必存在于当前 representation family

假设一个 task 同时要求：

- numeric detail 至少达到 mod `p^2`；
- generic product-branch reflection。

若 representation family 只允许 `Z/MZ`，要 numeric-refine mod `p^2` 必须满足：

`p^2|M`。

此时 M 必为 composite，quotient ring 不可能是 domain。

所以没有任何 scalar modulus 能实现 joined requirement。

Abstract semantic join 作为 demand profile 存在，但**无法由原 scalar precision parameter 表示出来**。

## 8. Nonrealizable join 意味着 state representation 必须 lift

要同时实现两项 requirement，必须改变 representation type，例如同时保留：

- mod `p^2` numeric residue；
- explicit branch / witness channel。

由此得到一般 architecture rule：

> **如果 declared precision requirements 的 join 在当前 representation class 中不可实现，就不应继续增大旧 scalar precision parameter；必须 enrich / lift state representation。**

这与加入 age/source state、witness repair、operation-word precision 等路线是同一种结构：future law 一旦能重新激活某个 distinction，就需要显式携带它。

## 9. Requirement joins 是 arithmetic lcm joins 的推广

此前 modular research 把 arithmetic requirements 表示为：

`(free-separation flag ; p-adic depths)`

并按 coordinatewise join 合并 tasks。

Semantic preorder 把这套思想推广。一个 task requirement profile 可以包含：

- state distinctions；
- safe operations；
- DOMAIN / RELATION witness channels；
- reflection / descent guarantees；
- arithmetic depth resources。

多任务合并就是取这些 requirements 的 join，而不是把 scalar precision costs 相加。

某些 join 仍可由 finite / modular representation 实现；另一些 join 会迫使 representation lift。

## 10. 与 witness-semantic descent 的关系

Witness descent 会要求如下 capabilities：

- local branch reflection；
- directed joint precision；
- compact / proper witness projection；
- fixed witnessed relation 的 profinite exactness。

若一个 representation 虽然 numeric state 更细，却丢掉其中一项 guard，那么对以后会重新读取 witness 的 task 来说，它并不 semantic finer。

所以 witness coherence 应自然进入 `C_T(P)`，而不是另造一条与 precision 平行的概念。

## 11. Foundation routing rule

比较两个 candidate precision states 时，不要只问：

`哪个 partition 更细 / modulus 更大 / scale 更小？`

而要问：

1. 哪些 exact state distinctions 被保留？
2. 哪些 declared future operations 仍可 descend？
3. 哪些 logical / witness / reflection laws 仍有效？
4. 一个 representation 是否能在全部 task-relevant coordinates 上 semantic dominate 另一个？
5. 如果不能，是否需要 richer representation 去实现 joined demand？

这可以避免在 future language 本身具有多个独立 semantic requirements 时，仍把 precision 错误压成一维 scalar。

## 12. Prior-art boundary

Partition refinement、congruence-preserving operations、preorders 与 product orders 都是标准既有数学。Enterprise Math 在这里得到的 routing principle 是：

> **task-relative precision 必须同时按 observational detail 与 future semantic capability 排序；raw refinement 自身并不足够。**