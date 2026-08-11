# 相同 Execution Monoid，不同 Minimum Capability Design

状态：`RESEARCH BRIDGE / NONCANONICAL`

Researcher-ID：`R-8F3K`

Design / execution separation 还可以比 NP-hardness 更 sharp：即使给定**完整 generated semantic operation monoid**、named generator 数量以及 exact composition law，也仍然不能推出 minimum precision-preserving generator count。

## 1. 两个 execution semantics 完全相同的 catalogues

固定 universe size `m>=2`。

两套 catalogue 都包含 m 个 singleton actions `{0},...,{m-1}`，再加一个 extra named action，因此两边 action count 都恰好是 `m+1`。

### Catalogue A — duplicate singleton

Extra action 再复制一次 `{0}`。

### Catalogue B — full action

Extra action 是 full universe `{0,...,m-1}`。

由于两套 catalogue 都已经含有所有 singletons，任意 union 都能生成**全部** universe subsets。

所以两边 generated semantic effect monoid 完全相同：

`2^[m]`

配 bitwise OR，effect 数为 `2^m`。

它们拥有相同 monoid carrier、相同 OR multiplication law、相同 identity、相同 named-generator count。

## 2. Minimum preserving basis size 却差到最大

Semantic target 是 full-universe coverage，也就是 parent Set-Cover action compiler 中的 full precision preservation。

在 Catalogue A 中，duplicate action 不贡献任何新方向。每个 universe element 都必须靠自己的 singleton cover，所以 minimum preserving subset size 是：

`m`。

在 Catalogue B 中，full-universe action 单独一个就能 preserve target precision，所以 minimum size 是：

`1`。

因此 minimum-basis gap 为：

`m-1`。

Executable report 对一族递增的 bounded universe sizes 逐一验证该 gap。

## 3. Monoid 本身忘掉了什么

Generated operation monoid 记录的是：

**最终有哪些 exact effects 可以被生成，以及这些 effects 怎样 compose。**

Minimum design 还需要知道 presented generator catalogue：哪些 named primitive actions 被当作可独立选择的 atomic resources。

两套 catalogue 可以生成完全相同的 effect closure，却把 primitive generators 放在 closure 中完全不同的位置。

因此 basis design 是：

`(semantic target, generator presentation, cost model)`

的性质，不是 abstract generated monoid 单独的性质。

## 4. Same action count 也不够

该 witness 两边 named action count 都固定为 `m+1`。

所以即使在 abstract monoid 外再附加 generator-count metadata，仍然无法恢复 minimum basis size。

必须知道真实 generator placement / presentation。

## 5. Stage131 consequence

同一个 semantic operation algebra 可以在 runtime representation optimization 开始**之前**就拥有不同的 upstream design cost。

因此至少三种对象必须保持区分：

1. **generated semantic algebra** —— 全部 exact effects 及其 composition；
2. **generator presentation / catalogue** —— 可供选择的 atomic capabilities；
3. **execution representation** —— selection 之后用 table、cache、formula、circuit 怎样运行。

把三者统称成一个“law complexity”会丢失关键 resource information。

## 6. 与 classical generating-set problem 的边界

本文不声称关于 monoid minimum generating set 的新 generic theorem。

这里的 preserving target 是从 Set-Cover precision compiler 继承来的 project-specific semantic requirement，而不仅仅是“生成整个 monoid”。

因此结论更窄、但对当前问题更直接：

> **即使 exact execution monoid 完全相同，也不能据此决定满足 declared precision target 的 minimum generator subset。**

## Owner-local assets

- `src/enterprise_math/same_monoid_design_gap.py`；
- `tests/test_same_monoid_design_gap.py`；
- 本双语 note。

## Prior-art / status

Semilattice generation 与 Set Cover 都是标准既有数学 / CS。本文只拥有 Enterprise Math 的 same-monoid design-separation pressure test。

无 repository strict CI、无 `EXECUTABLE_CHECKED`、无 canonical claim。`CI_NOT_REQUIRED_FOR_RESEARCH`。Hard block：`NONE`。
