# 虚无起点与最小跳数深度 — 历史/辅助路线

Status: `RETAINED_AS_AUXILIARY_DEPTH_NOT_NATIVE_GEOMETRY`
Original date: `2026-08-17`
Reconciled: `2026-08-21`

本文件保留 `VOID_E`、existence-start 与 minimum-jump depth 作为可声明的辅助过程/计数语义，但它不定义当前 native origin、radius、segment identity 或 line length。

当前原生 origin 为：

`O_E=0`，三重 circle-cell boundary intersection。

当前 native line/length 由三正轴 sector foundation、component trace 和 directed native line gauge 给出，而不是由 void-to-target geodesic depth 给出。

因此：

`VOID_START = OPTIONAL N1/PROCESS SEMANTICS`；

`MIN_JUMP_DEPTH = COMBINATORIAL/PROCESS COUNT`；

`MIN_JUMP_DEPTH != NATIVE_LINE_LENGTH` in general。

若某任务需要 `VOID_E -> O_E` 的 existence transition，必须把它显式声明为额外过程语义，不得把它重新解释为当前 native coordinate ontology。

当前几何路由：

- `definitions/ENTERPRISE_THREE_POSITIVE_AXIS_OVERLAPPING_CIRCLE_CELL_PLANE_20260820.md`；
- `definitions/ENTERPRISE_NATIVE_LINE_TRACE_FORMULA_20260821.md`；
- `definitions/ENTERPRISE_ARBITRARY_POINT_DIRECTED_LINE_GAUGE_20260821.md`。

原始文本保留在 Git 历史中。
