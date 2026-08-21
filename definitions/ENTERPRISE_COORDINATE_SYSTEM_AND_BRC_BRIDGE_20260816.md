# 进取坐标系与 BRC 坍缩桥梁 — 历史路由

Status: `SUPERSEDED / HISTORICAL_PROVENANCE`
Original date: `2026-08-16`
Superseded: `2026-08-20`
Driver reconciliation: `2026-08-21`

## 当前状态

本文件曾经同时承载：

1. “进取坐标系”正式命名；
2. 三条无向轴 / 六个有向方向 / 60° 正负交错；
3. signed-origin-one / no-zero 坐标；
4. BRC 作为垂直坐标系与进取坐标系之间桥梁的定位。

其中第 2、3 项已经被新的 foundational correction 推翻，不再是当前原生基础。

当前必须改读：

`definitions/ENTERPRISE_THREE_POSITIVE_AXIS_OVERLAPPING_CIRCLE_CELL_PLANE_20260820.md`

以及当前 downstream definitions：

- `definitions/ENTERPRISE_NATIVE_LINE_TRACE_FORMULA_20260821.md`
- `definitions/ENTERPRISE_ARBITRARY_POINT_DIRECTED_LINE_GAUGE_20260821.md`
- `definitions/ENTERPRISE_UNORIENTED_BIDIRECTIONAL_SEGMENT_SPECTRUM_20260821.md`
- `definitions/ENTERPRISE_BRC_MULTIPATH_ENRICHMENT_BRIDGE_20260821.md`

## 已 supersede 的内容

不得再从本历史文件恢复以下 native claims：

- `ORIGIN = ±1`；
- `0` 不存在于原生坐标；
- 三条原生无向轴自动产生六个原生有向方向；
- 相邻 `60°` 方向正负交错；
- 原生负轴是基础结构；
- origin circle / diameter-one circle ontology；
- 用旧 signed chart 作为当前 native coordinate system。

当前 foundation 冻结：

`O_E = 0`；

`ENTERPRISE_NATIVE_AXES = THREE_POSITIVE_RAYS`；

`NO_NATIVE_NEGATIVE_AXES_REQUIRED`；

`ENTERPRISE_RIGHT_ANGLE = 120_DEGREES`；

`A_E={(a,b,c) in N_0^3 : min(a,b,c)=0}` 为三个正二轴扇区 chart 的粘合。

## 保留的术语/路线

以下历史贡献继续保留：

- “进取坐标系 / ENTERPRISE_COORDINATE_SYSTEM”作为项目术语；
- “经典二维兼容图示”作为表示层术语；
- `ORTHOGONAL_COORDINATE_SYSTEM` 作为经典/垂直坐标语义名称；
- BRC 可作为垂直/经典坐标语义与进取坐标语义之间的 typed collapse/readout bridge；
- BRC bridge 不预设双射，必须声明 source/target semantics、collapse relation、fiber/collision、inverse/readout status 与 precision layer。

这些保留内容必须在当前三正轴 foundation 上重新类型化使用。

## Provenance

原始 2026-08-16/17 文本保留在 Git 历史中。本文件现在只承担历史索引和 supersession 路由，避免其旧 `ACTIVE / CANONICAL` 标记继续与当前 foundation 争夺权威。
