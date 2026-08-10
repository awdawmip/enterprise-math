# Partial-Operation Semantic Repair：FQ-006 Consumption Bridge

状态：`RESEARCH BRIDGE / NONCANONICAL / NO NEW PARTIAL-QUOTIENT OWNERSHIP`

本文把 task-relative semantic-precision preorder 与 total-operation repair compiler 接到已经 canonical 的 FQ-006/P023 partial-operation quotient。它**不**重新主张 generic partial-transition theorem 的所有权。

## 1. Canonical source theorem 已经属于 FQ-006

对有限 state set X 与 deterministic partial operation

`u:D_u -> X`，

canonical FQ-006 要求同一 quotient class 内的 source states 同时满足：

1. DOMAIN membership / definedness 一致；
2. operation enabled 时，targets 落入同一 quotient class。

因此对一族 named partial operations，canonical refinement signature 正是：

`current block + 每个 operation 的 (definedness,target-block)`。

稳定 partition 已经被证明是 initial observation 内**最粗**、且能让整族 partial operations 保持 domain 并安全 descend 的 refinement。

本文只把这个结论重新解释成一种 **semantic capability repair**。

## 2. Partial operation capability demand

设当前 task-relative precision state 的 observational equivalence 为 E_0，future theory 还要求一族 deterministic partial unary operations U 在 collapse 以后仍然可执行。

相对于当前 equivalence E，对每个 operation 定义 state x 的 signature：

若 x 不在 operation domain：

`UNDEFINED`；

若 operation enabled：

`(DEFINED,[u(x)]_E)`。

当前等价的两个 states 只有在全部 required partial-operation signatures 都相同时，才能继续保持等价。

反复按这个 signature split 到 fixed point，精确就是 FQ-006 legality-sensitive partition refinement。

## 3. DOMAIN 与 target precision 可以相互激活

Definedness 不是“额外贴一个 bit”以后就总能结束。

Sharp four-state example：

initial partition

`{0,1}|{2,3}`，

partial operation

`0->2`, `1->3`, `2->0`，而 3 undefined。

第一轮只先看到下游 block 中的 DOMAIN difference：

`{0,1}|{2}|{3}`。

只有在 2/3 被拆开以后，0 与 1 的 targets 才变得可区分，于是第二轮继续得到：

`{0}|{1}|{2}|{3}`。

因此 DOMAIN refinement 可以触发后续 target refinement。真正的 semantic repair 是 fixed point，不是 one-shot definedness annotation。

## 4. Total-operation specialization

若全部 required operations 都是 total，`UNDEFINED` 分支消失，partial signature 退化成 current target-block vector。

此时 DOMAIN-aware compiler 精确退化为 semantic-operation branch 的 total-operation coarsest refinement。

所以当前 architecture 是嵌套的：

`total operation repair`

是

`FQ-006 partial operation repair`

在 full-domain 情形下的 specialization。

## 5. Observable-UNDEFINED totalization 是 verification equivalence

FQ-006 还允许一种 verification representation：增加一个 distinguished absorbing `UNDEFINED` state，再把 partial maps totalize。

只要这个 extra state 在 observation 上保持独立，在扩展 state set 上运行 ordinary total-operation refinement，并把最终 partition 限制回 X，就得到与 direct partial-operation refinement 完全相同的 coarsest partition。

这个 equivalence 很适合复用 total congruence machinery 做验证。

但它**不**意味着 UNDEFINED 是一个 physical successor state。

## 6. Semantic-preorder interpretation

在 task-relative semantic precision preorder 中，声明一个 required partial operation，实际上同时要求两种 capability：

- DOMAIN law 必须 descend；
- enabled target map 必须 descend。

若当前 representation 允许在同一个 finite X 上任意 refine state partition，FQ-006 已经提供了实现这个 capability join 的 canonical coarsest state lift。

它就是 total-operation semantic repair 的 partial-operation 对应物。

## 7. Ownership boundary

Generic theorem——legality-sensitive refinement、finite stabilization、coarsest compatible partition、observable-UNDEFINED totalization——已经属于 FQ-006/P023 canonical mathematics。

当前 branch 只拥有：

- explicit semantic-preorder consumption bridge；
- DOMAIN→target cascade pressure test；
- 与 total specialization、observable-UNDEFINED verification route 的 executable equivalence。

不能把本 branch 当作 canonical partial-operation quotient 的 replacement owner。

## 8. 下一条真正的新边界：multivalued relation support

Deterministic partial operation 的 successor support 大小只能是 0 或 1。

自然的下一层是 A4 relation-valued action：一个 source 可以拥有任意有限 target set。在 support semantics 下，对应的 current signature 应该是**target partition blocks 的集合**；空集合自然保留 undefinedness。

这个 generalization 应回到 A4/P023 relation-support owner，并且必须明确止步于 support：path multiplicity、witness provenance、branch-death history 仍然需要更细的 A4 witness state。