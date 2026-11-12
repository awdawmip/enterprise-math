# 虚无起点与最小跳数深度 — 历史/辅助路线

Status: `RETAINED_AS_AUXILIARY_DEPTH_NOT_NATIVE_GEOMETRY`
Original date: `2026-08-17`
Reconciled: `2026-08-21`

本文件保留 `VOID_E`、existence-start 与 minimum-jump depth 作为可声明的辅助过程/计数语义，但它不定义当前 native origin、radius、segment identity 或 line length。

2026-08-20 中间阶段曾将 `O_E=0` 解释为三重 circle-cell boundary intersection。现行 P000 V5 原生坐标零则为选定的实际 Cell 锚点；该三重交点保留为 carrier incidence，不是 native origin。

现行 native 步与路径从 signed-X6 的单位轴正反方向及实际 Cell 出发；原生平方范数用六轴 signed 分量平方和，历史 directed line gauge 只用于适当的相对观察者。`VOID_E` 到目标的最小跳数是独立的过程/计数语义。

因此：

`VOID_START = OPTIONAL N1/PROCESS SEMANTICS`；

`MIN_JUMP_DEPTH = COMBINATORIAL/PROCESS COUNT`；

`MIN_JUMP_DEPTH != NATIVE_LINE_LENGTH` in general。

若某任务需要 `VOID_E -> O_E` 的 existence transition，必须把它显式声明为额外过程语义，不得把它重新解释为当前 native coordinate ontology。

当前几何路由：

- `definitions/00_CURRENT_NATIVE_FOUNDATION.md` 与 `definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md`（native）；
- `definitions/ENTERPRISE_THREE_POSITIVE_AXIS_OVERLAPPING_CIRCLE_CELL_PLANE_20260820.md`（历史三正轴、载体）；
- `definitions/ENTERPRISE_NATIVE_LINE_TRACE_FORMULA_20260821.md`（路径组合）；
- `definitions/ENTERPRISE_ARBITRARY_POINT_DIRECTED_LINE_GAUGE_20260821.md`（相对观察）。

原始文本保留在 Git 历史中。
