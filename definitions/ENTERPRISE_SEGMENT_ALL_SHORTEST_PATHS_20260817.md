# 最短路径族：历史 downstream realization

Status: `RETAINED / DOWNSTREAM_REALIZATION_ONLY / SUPERSEDED_AS_NATIVE_SEGMENT_IDENTITY`
Original date: `2026-08-17`
Reconciled: `2026-08-21`

本文件只保留一个弱而稳定的作用：**当一个目标对象/目标 cell 已由当前 native semantics 独立确定后，可以研究到该对象的全部最短路径作为组合 realization family。**

它不再定义 native segment identity、native line membership 或 native length。

现行原生线段/长度基础（2026-11-13）为 `p000_reality_foundation.json` V5、`definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md` 及 `definitions/ENTERPRISE_X6_CENTERED_THREE_AXIS_SLICE_REBASE_20260905.md`。原生直线的 primitive 方向限于六轴正反单位步；其余组合位移可由有序 native 路径实现。

以下旧定义仍可按**声明的历史 chart/观察者作用域**消费：

- `definitions/ENTERPRISE_NATIVE_LINE_TRACE_FORMULA_20260821.md` — 选定正向扇区的 component trace 与 multipath fiber；
- `definitions/ENTERPRISE_ARBITRARY_POINT_DIRECTED_LINE_GAUGE_20260821.md` — 相对/min-zero directed gauge，不是当前原生度量；
- `definitions/ENTERPRISE_UNORIENTED_BIDIRECTIONAL_SEGMENT_SPECTRUM_20260821.md` — 相对观察者的双向 spectrum。

冻结边界：

`MIN_JUMP_COUNT != NATIVE_LINE_LENGTH` in general。

`SAME_ENDPOINT_PATH != SAME_NATIVE_LINE_PATH` in general。

因此最短路径是 downstream combinatorial realization，不是当前原生线段 ontology。原始文本保留在 Git 历史中。
