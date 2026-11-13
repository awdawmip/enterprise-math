# 向量模定端点 + 反向 geodesic 线段 — 历史路线

Status: `PARTIALLY_SUPERSEDED / HISTORICAL_REALIZATION_ROUTE`
Original date: `2026-08-17`
Reconciled: `2026-08-21`

本文件原先依赖 signed-origin-one 与 initial-circle ontology，并把“代数向量模先选端点、再反向取全部最短路径”作为线段重基。

其中依赖旧 origin/chamber 的 native geometry 在 2026-08-20 三正轴阶段已被修订；该中间阶段又被 P000 V5 的 signed 六轴 Cell 原生空间所取代。

当前分类型路由（2026-11-13）：

1. `p000_reality_foundation.json` V5 与 `definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md` — 原生 signed 六轴 Cell 身份、位移与分量平方范数；
2. `definitions/ENTERPRISE_X6_CENTERED_THREE_AXIS_SLICE_REBASE_20260905.md` — 选定 signed 三轴受限子空间；
3. `definitions/ENTERPRISE_THREE_POSITIVE_AXIS_OVERLAPPING_CIRCLE_CELL_PLANE_20260820.md` — **历史**固定正向扇区/载体，不是原生平面；
4. `definitions/ENTERPRISE_NATIVE_LINE_TRACE_FORMULA_20260821.md` — 历史固定 chart 的正向分量 trace 与 exact multipath fiber；
5. `definitions/ENTERPRISE_ARBITRARY_POINT_DIRECTED_LINE_GAUGE_20260821.md` — 相对/min-zero directed gauge，不是原生 signed 度量；
6. `definitions/ENTERPRISE_UNORIENTED_BIDIRECTIONAL_SEGMENT_SPECTRUM_20260821.md` — 需在其声明的相对/载体双向 trace 与读出范围内解释。

继续保留的弱原则只有：

- graph/geodesic/min-jump family 可以作为一个已经声明对象的 downstream realization fiber；
- `MIN_JUMP_COUNT != NATIVE_LINE_LENGTH` in general；
- 所有合法 realization 可以保留，而不把 path multiplicity 混成一个标量长度。

不得再从本文件推出：

- shortest path family 本身定义 native segment identity；
- shortest jump count 定义 native length；
- 旧 signed-vector norm/chamber 自动给出当前任意点线段。

原始完整文本保留在 Git 历史中。
