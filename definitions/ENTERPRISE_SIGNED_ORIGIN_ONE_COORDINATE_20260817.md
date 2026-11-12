# 进取坐标系：带符号原点一 / 零不存在 — 历史定义

Status: `SUPERSEDED / HISTORICAL_PROVENANCE`
Original date: `2026-08-17`
Historical intermediate successor: `definitions/ENTERPRISE_THREE_POSITIVE_AXIS_OVERLAPPING_CIRCLE_CELL_PLANE_20260820.md`
Current P000/X6 native reference: `definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md`

## 历史内容

本文件曾冻结：

`O_E=[+1]=[-1]`

以及“原生坐标 0 不存在、负坐标为原生方向状态”的 signed-origin-one ontology。

该 ontology 已被 2026-08-20 foundational correction 明确 supersede。

## 历史中间阶段与现行 X6 基础

2026-08-20 中间阶段曾使用：

`O_E = 0`。

原点是三个 circle cells 的三重边界交点，不是 cell center，也不是 cell。

原生轴为三条正射线：

`ENTERPRISE_NATIVE_AXES = THREE_POSITIVE_RAYS`。

地址采用：

`A_E={(a,b,c) in N_0^3 : min(a,b,c)=0}`。

上述三正轴正射线和三圆交点原点均属已退役的 2026-08-20 中间原生解释。现行 P000 V5 使用六轴 signed Cell 锚点和 `AFFINE_TORSOR(Z^6)`，原生负向单位步合法；不得将本文件特有的 `±1` origin/no-zero 等价关系，或中间版本的三正轴 min-zero 身份，带入当前 theorem premises。

## 可保留用途

本文件仍可作为：

- 历史研究路线 provenance；
- 对旧 signed-coordinate experiments 的解释；
- 研究“为什么该 ontology 被替换”的负结果材料；
- 对旧脚本/任务书的兼容追踪。

若旧结果依赖本文件的 signed-origin ontology，它默认是 `HISTORICAL / REQUIRES_RETYPING_OR_REDERIVATION`，除非已有独立证明将对应结论正确嵌入现行 signed-X6、载体或观察者层。

原始完整文本保留在 Git 历史中。
