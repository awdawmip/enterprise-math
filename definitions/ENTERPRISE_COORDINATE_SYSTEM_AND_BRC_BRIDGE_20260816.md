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

现行原生入口（2026-09-05 X6 统一之后，以现行 P000 为准）：

- `definitions/00_CURRENT_NATIVE_FOUNDATION.md`
- `definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md`
- `definitions/ENTERPRISE_X6_CENTERED_THREE_AXIS_SLICE_REBASE_20260905.md`

以下为 2026-08-20 中间阶段的历史后继文档，仅作载体、观察者和术语沿革：

`definitions/ENTERPRISE_THREE_POSITIVE_AXIS_OVERLAPPING_CIRCLE_CELL_PLANE_20260820.md`

另可按各自现行类型使用已修订的 downstream definitions：

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

**下列仅为 2026-08-20 中间阶段曾采用、但已被 2026-09-05 有符号 X6 Cell 基础取代的历史声明；不代表现行 P000：**

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

这些保留内容必须在现行六轴有符号 X6 Cell 基础下分别类型化为载体、观察者或 BRC 路径关系；不能将正轴或 min-zero 地址恢复成完整原生 Cell 身份。

## Provenance

原始 2026-08-16/17 文本保留在 Git 历史中。本文件现在只承担历史索引和 supersession 路由，避免其旧 `ACTIVE / CANONICAL` 标记继续与当前 foundation 争夺权威。
