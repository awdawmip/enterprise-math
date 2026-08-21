# 最短路径族：历史 downstream realization

Status: `RETAINED / DOWNSTREAM_REALIZATION_ONLY / SUPERSEDED_AS_NATIVE_SEGMENT_IDENTITY`
Original date: `2026-08-17`
Reconciled: `2026-08-21`

本文件只保留一个弱而稳定的作用：**当一个目标对象/目标 cell 已由当前 native semantics 独立确定后，可以研究到该对象的全部最短路径作为组合 realization family。**

它不再定义 native segment identity、native line membership 或 native length。

当前线段/线身份请读：

- `definitions/ENTERPRISE_NATIVE_LINE_TRACE_FORMULA_20260821.md`；
- `definitions/ENTERPRISE_ARBITRARY_POINT_DIRECTED_LINE_GAUGE_20260821.md`；
- `definitions/ENTERPRISE_UNORIENTED_BIDIRECTIONAL_SEGMENT_SPECTRUM_20260821.md`。

冻结边界：

`MIN_JUMP_COUNT != NATIVE_LINE_LENGTH` in general。

`SAME_ENDPOINT_PATH != SAME_NATIVE_LINE_PATH` in general。

因此最短路径是 downstream combinatorial realization，不是当前原生线段 ontology。原始文本保留在 Git 历史中。
