# X6 endpoint quotient type audit：`Z^2 x Z/2` 不得晋升为 full Cell 定理

Status: `CORRECTION / SUPERSEDES PR1257 CORE X6-CELL CLAIM / PRESERVE_AS_TYPED_COUNTERMODEL`
Date: `2026-09-05`

## 1. 发现的类型错误

先前 `G6^cell ~= Z^2 x Z/2` 构造同时用了两类当前都合法、但属于**不同 observer** 的 quotient：

1. **line / component-trace observer**：同一 physical positive axis 在两个相邻 chart 中按 axis label + radial component 去重；
2. **Cell endpoint observer**：在一个固定三轴 slice 内，`X_i X_j` 与 reverse-third carrier adjacency 可以落到同一个 terminal Cell，因此三步 local triangle 可以是 Cell-return loop。

错误发生在把 (1) 的 shared-axis identity 直接搬成 (2) 的 shared **Cell-transition generator**。

当前 R061 Stage1R checker 实际冻结的更强事实是：同一 global axis line identity 有两个相邻-sector chart presentations，而且它们的 physical Cell trajectories 始终不同；通过 radial 0..18：

- 57 global axis line identities；
- 114 chart presentations；
- physical trajectory duplicate count = 0。

因此：

`SAME_NATIVE_AXIS_LINE_IDENTITY != SAME_CHART_LOCAL_CELL_TRAJECTORY`。

更不能在没有 full-native lift theorem 时推出：

`SAME_AXIS_LABEL -> SAME_FULL_CELL_ENDPOINT_GENERATOR`。

这正是 previous `G6^cell` presentation 的隐含额外 quotient。

## 2. 为什么漂亮的代数仍不能当 X6 证明

一旦把每条 K4 edge 的两个 incidence/chart presentations 强制为一个 endpoint generator，就会得到四个 local star relations 组成的 K4 incidence matrix，并出现 Smith `(1,1,1,2)`、`Z^2 x Z/2`、companion `t`、intrinsic S4 等整套漂亮结构。

这些计算本身是正确的；错误在**输入类型**。

正确状态：

`Z^2 x Z/2 = EXACT ALGEBRA OF THE SHARED-AXIS-ENDPOINT-IDENTIFIED MODEL`，

不是

`PROVED FULL NATIVE CELL ENDPOINT ALGEBRA`。

因此 PR #1257 中的：

- return parity；
- one-slice-address + bit；
- quotient rigidity；
- companion C2；
- BRC factorization；

全部保留为该**额外 shared-axis endpoint quotient model** 的精确定理/工具，但不得晋升为 `X6_native`。

## 3. 当前真正可用的最细局部对象

一个 global axis label `e=uv` 有两个 incidence presentations：

`(u,e)` 与 `(v,e)`。

因此 Cell-level local transition provenance 至少需要 12 个 K4 incidence flags，而不是直接压成 6 个 axis endpoint generators。

这与 FCC first shell 的 12 个 directed/contact incidence flags 兼容，但仍不能把 carrier ray 当 native Cell transition identity；它只是强烈提示正确 interface 的**类型**应保留 `(slice,axis)` incidence。

四个 slice 各自仍有一个经过验证的 local triangular Cell/path structure；全局问题是这些 local Cell states/trajectories如何作为同一个 full 6D Cell 的不同 slice observations/lifts 兼容，而不是先把 shared axis 的两个 chart endpoints相等。

## 4. 旧 context candidate 也不能反向晋升

先前 `X_ctx` 保留 `(slice,axis)` 并定义了一个特定 normalization update；这避免 shared-axis endpoint overquotient，但其具体跨-slice state update 仍是新增机制，不是当前 Foundation 强制。

所以：

- shared-axis identified `Z^2 x Z/2` model = **too coarse without lift theorem**；
- old context-normalized model = **too specific without cross-slice update theorem**。

真正的 current frontier 在两者之间：

`FULL X6 CELL STATE -> FOUR SLICE CELL OBSERVATIONS + INCIDENCE/TRANSITION COMPATIBILITY`。

## 5. 下一正确构造

应构造 typed observation diagram，而非直接 endpoint quotient：

1. 四个 local slice Cell spaces `C_A,C_B,C_C,C_D`；
2. 六个 shared-axis line/trace overlap objects `L_AB,...,L_CD`；
3. 每个 incidence `(v,e)` 的 local Cell/path-to-line readout；
4. full state candidate as a compatible lift/fibre product plus any genuinely unobserved native fibre；
5. only after proving a cross-chart Cell lift relation may two incidence transitions be identified at full-state level。

BRC discipline：Path-formal occurrence、chart incidence、terminal Cell、line identity与 Boolean support 必须继续分层。

## 6. Correction freeze

`PR1257_X6_CELL_PROMOTION = WITHDRAWN_BY_TYPE_AUDIT`。

`PR1257_ALGEBRA = PRESERVED_AS_SHARED_AXIS_ENDPOINT_IDENTIFIED_MODEL`。

`FULL_NATIVE_X6 = NOT_YET_CLOSED`。

`NEXT_FRONTIER = COMPATIBLE_FOUR_SLICE_CELL_OBSERVATION/LIFT DIAGRAM WITH 12 INCIDENCE FLAGS`。
