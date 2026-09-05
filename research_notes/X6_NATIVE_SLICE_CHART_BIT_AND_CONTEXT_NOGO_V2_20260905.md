# X6 universal completion：一片 min-zero 地址 + 1 bit 完整坐标与 context-state no-go

Status: `DERIVED / EXACT / COMPANION TO X6 UNIVERSAL COMPLETION V2`
Date: `2026-09-05`

## 1. 具体 full-state chart

沿用

`G6^cell ~= Z^2 x Z/2`

与唯一非零 torsion element `t`。

对任意三轴 slice `v`，其 local subgroup `G_v` 精确同构于已建立三轴 Cell address group；用当前三轴 canonical section 把元素写成一个非负 min-zero triple

`A_v = {(a,b,c) in N_0^3 : min(a,b,c)=0}`。

定义 index-2 sheet homomorphism

`lambda_v:G6^cell -> Z/2`

为：incident axes 取 0，slice 外三个 axis labels 取 1。

则

`ker(lambda_v)=G_v`, `lambda_v(t)=1`。

对 full state `g` 定义

`h_v(g)=g + lambda_v(g) t in G_v`。

由 local min-zero section 得 `addr_v(g) in A_v`。

于是映射

`Phi_v(g)=(addr_v(g), lambda_v(g))`

是双射：

`G6^cell <-> A_v x Z/2`。

逆映射是：先把 min-zero triple 解码为 local endpoint `h in G_v`，再加 `bit*t`。

因此任何一个三轴 slice 的完整坐标图都是

`ONE_EXISTING_3AXIS_MINZERO_ADDRESS + ONE_BINARY_SHEET_BIT`。

这里的 `Z/2` bit 是 full Cell 关系 fibre，不是第七空间维，也不是时间维。

## 2. ordinary slice observation 丢掉的恰是这个 bit

普通 slice observation 只返回 `addr_v(g)`，不返回 `lambda_v(g)`。

因此

`addr_v(g+t)=addr_v(g)`。

对四个 slice 同时观察仍有

`(addr_A,addr_B,addr_C,addr_D)(g+t)=(addr_A,addr_B,addr_C,addr_D)(g)`。

共同不可见 fibre 精确为 `{g,g+t}`；不存在更大的 universal ambiguity。

这给出 P000 语句

`SLICE_OBSERVATION != FULL_CELL_STATE`

的一个完全有限、可计算实现。

## 3. chart transition

从 source slice chart `(addr_v,bit_v)`：

1. 解码为 `g in G6^cell`；
2. 对 target slice `w` 计算 `bit_w=lambda_w(g)`；
3. 计算 `h_w=g+bit_w*t in G_w`；
4. 用 w-slice 的 min-zero section 输出 `addr_w`。

因此 chart transition 是 exact integer map，无 carrier Euclidean coordinate、浮点或连续插值。

执行模块：

`experiments/x6_native_universal_completion_v2_20260905/x6_cell.py`。

独立执行已覆盖 `u,v in [-12,12]`、两种 sheet、四个 slice 的 5,000 次完整 roundtrip。

## 4. 旧 context-dependent Cell-state candidate 的精确 no-go

前一阶段候选曾让同一 FCC/shared axis 在两个 incident slice 中拥有不同 Cell-state update，因为 chart-local carrier orientation 不同。

这与当前已冻结类型边界不相容：

- native physical positive axis 按 global axis label 去重；
- 两个 chart-local trajectories/flags 是 realization provenance；
- carrier orientation sign 不是新的 native axis identity。

因此 `(slice,axis)` 可作为 Path-formal/BRC realization label，但不能在没有新 Foundation 定义时自动成为两个不同 native endpoint generators。

旧候选中的四步 word

`B/AB(+), A/AC(-), C/AC(-), B/AB(-)`

若按当前 shared-axis identity 去掉 chart gauge，其 native net axis exponent 恰为

`-2 AC`。

在 universal endpoint group 中

`End(-2 AC) != 0`。

所以该四步路径的“闭合”不是由当前 Cell/path/axis 基础强制出的 return law，而来自把 chart context 额外保留为 Cell state 并采用了特定 normalization update。

Freeze research correction:

`OLD_X_CTX_FOUR_STEP_RETURN = NOT_NATIVE_FORCED`。

`CHART_CONTEXT = PATH/REALIZATION_PROVENANCE_UNLESS_SEPARATELY_PROMOTED_TO_CELL_STATE`。

旧候选仍可作为带额外内部状态的 extension model，但不能再作为最小 `X6_native` 默认候选。

## 5. 12 个有向一步邻接的兼容性

在 `G6^cell` 中六个 positive-axis generators 与各自 path inverse 给出 12 个互不相同的一步 directed endpoint neighbours。

这与 FCC first-shell 的 12 directed carrier rays / 12 incidence flags 在计数上兼容，但不反向推出 P000 六维，也不把 carrier ray sign 定义为 native negative axis。

正确类型仍是：

`native axis / inverse adjacency event -> may have chart-local carrier realizations`，

而不是

`carrier directed ray -> defines native axis identity`。

## 6. 对 Foundation 选择的影响

若后续采用

`NO_UNFORCED_CELL_IDENTIFICATION`

作为 native Cell identity 原则，则可直接冻结

`X6_native := torsor(G6^cell)`。

这时每个 Cell 在任一三轴 chart 中都精确表现为

`(existing min-zero triple, one hidden sheet bit)`。

若不采用该最小性原则，则任何进一步 Cell quotient 必须给出新的 native cross-slice return relation；不能从 chart orientation、FCC Euclidean linear dependence 或 Boolean endpoint support 静默制造。
