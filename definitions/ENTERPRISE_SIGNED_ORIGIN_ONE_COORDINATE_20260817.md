# 进取坐标系：带符号原点一 / 零不存在 — 历史定义

Status: `SUPERSEDED / HISTORICAL_PROVENANCE`
Original date: `2026-08-17`
Superseded by: `definitions/ENTERPRISE_THREE_POSITIVE_AXIS_OVERLAPPING_CIRCLE_CELL_PLANE_20260820.md`

## 历史内容

本文件曾冻结：

`O_E=[+1]=[-1]`

以及“原生坐标 0 不存在、负坐标为原生方向状态”的 signed-origin-one ontology。

该 ontology 已被 2026-08-20 foundational correction 明确 supersede。

## 当前基础

当前原生平面使用：

`O_E = 0`。

原点是三个 circle cells 的三重边界交点，不是 cell center，也不是 cell。

原生轴为三条正射线：

`ENTERPRISE_NATIVE_AXES = THREE_POSITIVE_RAYS`。

地址采用：

`A_E={(a,b,c) in N_0^3 : min(a,b,c)=0}`。

因此不得把本文件的 `±1` origin、负原生坐标或 no-zero 规则带入当前 theorem premises。

## 可保留用途

本文件仍可作为：

- 历史研究路线 provenance；
- 对旧 signed-coordinate experiments 的解释；
- 研究“为什么该 ontology 被替换”的负结果材料；
- 对旧脚本/任务书的兼容追踪。

若旧结果依赖本文件的 signed-origin ontology，它默认是 `HISTORICAL / REQUIRES_RETYPING_OR_REDERIVATION`，除非已有较新的独立证明表明结论在当前三正轴 foundation 下仍成立。

原始完整文本保留在 Git 历史中。
