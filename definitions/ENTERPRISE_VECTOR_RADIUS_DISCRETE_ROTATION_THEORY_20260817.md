# 进取向量半径与离散旋转 — 当前保留边界

Status: `PARTIALLY_SUPERSEDED / RETAINED_DOWNSTREAM_PRINCIPLES`
Original date: `2026-08-17`
Reconciled: `2026-08-21`
Historical intermediate foundation: `definitions/ENTERPRISE_THREE_POSITIVE_AXIS_OVERLAPPING_CIRCLE_CELL_PLANE_20260820.md`
Current native foundation: `p000_reality_foundation.json` V5; `definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md`
Current reader correction: `2026-11-13`

## 为什么本文件不再是整体 canonical theory

原 2026-08-17 synthesis 混合了两类内容：

1. 后来仍然有价值的“代数长度 / 离散 cell 状态 / 组合路径实现”分层原则；
2. 已被 2026-08-20 foundational correction 推翻的 signed-origin-one、no-zero、origin-circle、旧 chamber/sign 结构与相关具体几何。

因此本文件不再整体作为当前 geometry authority。

## 明确 supersede 的部分

不得继续使用原文件中的：

- `O_E=[+1]=[-1]`；
- native coordinate zero 不存在；
- `CIRCLE_E(1)={O_E}`；
- origin circle 的 all-unit radius/diameter/perimeter/area ontology；
- 依赖旧 signed-axis/chamber ontology 的原生坐标结论；
- 依赖当时三正轴 sector atlas 作为完整原生空间的 cross-chamber 解释。

2026-08-20 中间阶段使用三正向射线与 min-zero 表示；现行 P000 V5 使用 **signed 六轴 X6 Cell 仿射扭子**、选定 Cell 锚点与六轴正反单位步。`A_E` 只能作为相对/载体观察截面，`O_E` 三重边界交点只能作为载体关联；角度 `120_DEGREES` 仍按 P000 项目定义保留。

## 当前继续保留的下游原则

以下原则与旧 origin/sign ontology 可分离，继续作为研究指导保留：

### 1. 先组合对象，再读取长度

不要把 path/jump count 自动当作 geometric length。

`COMPOSE_STRUCTURAL_COMPONENTS_FIRST -> MEASURE_REBUILT_LENGTH_SECOND`。

现行原生长度须按声明的 X6 signed 分量平方和及相应原生结构确定；2026-08-20/21 的 line/trace 可在明确的正向 chart、路径或观察者作用域内保留。

### 2. 离散旋转状态是单 cell 状态

`ROTATING_SEGMENT_NATIVE_STATE = ONE_CIRCLE_CELL_PER_TRAJECTORY_STEP`。

边界/交点是 transition/incidence event，不是同时占据多个 cells 的 instantaneous state。

### 3. 歧义保留为多条单值 trajectory

若局部事件存在多个同等合法的下一 cell：

`ALL_LEGITIMATE_PATHS_RETAINED = BRANCHING_OF_SINGLE_CELL_TRAJECTORIES`。

不要把“多个合法 trajectory”误写成“一个时刻同时处于多个 cells”。

### 4. geodesic/min-jump 是后置实现，不是长度来源

`MIN_JUMP_COUNT != NATIVE_LINE_LENGTH` in general。

历史 R061 给出了正向分量 trace 与 multipath fiber；其 directed min-zero gauge 属于相对观察者，不是现行 signed-X6 原生度量。因此 reverse/minimum-jump constructions 只能作为声明后的 realization/readout 使用，不能倒过来定义当前原生长度。

## 暂不保留为当前结论的部分

旧文件关于 hidden-interior radius、`D(1,1)` interval、first hidden radius、旧 algebraic shell 与旧 chamber map 的具体结论，如果其证明依赖 signed-origin/chamber carrier，当前状态统一为：

`HISTORICAL_RESULT / REQUIRES_CURRENT_FOUNDATION_REDERIVATION`。

它们没有被声明为“数学上必错”，但不能在未重推前继续标成 current canonical foundation/theory。

## 当前路由

当前原生 X6 与长度：

`p000_reality_foundation.json` V5；`definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md`（原生 Cell/坐标）；`definitions/ENTERPRISE_X6_CENTERED_THREE_AXIS_SLICE_REBASE_20260905.md`（受限三轴）

历史正向扇区/载体：

`definitions/ENTERPRISE_THREE_POSITIVE_AXIS_OVERLAPPING_CIRCLE_CELL_PLANE_20260820.md`

历史 chart-local line/multipath：

`definitions/ENTERPRISE_NATIVE_LINE_TRACE_FORMULA_20260821.md`

相对观察者 directed gauge：

`definitions/ENTERPRISE_ARBITRARY_POINT_DIRECTED_LINE_GAUGE_20260821.md`

无向结构：

`definitions/ENTERPRISE_UNORIENTED_BIDIRECTIONAL_SEGMENT_SPECTRUM_20260821.md`

BRC × multipath：

`definitions/ENTERPRISE_BRC_MULTIPATH_ENRICHMENT_BRIDGE_20260821.md`

原始 2026-08-17 完整 synthesis 保留在 Git 历史中。
