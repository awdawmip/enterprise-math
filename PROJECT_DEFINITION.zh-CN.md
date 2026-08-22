# 进取数论项目定义

Status: `ACTIVE / PROJECT-LEVEL DEFINITION / V4`
Date: `2026-08-22`
Driver: `CONTROL_PLANE`

## 一句话定义

> **进取数论以有限分辨率、精度内生、整数优先和离散可计算为底层研究立场，重新奠基现代数学中有用的代数、几何、三角、分析与物理工具，并明确它们何时精确恢复、有限精度恢复、渐近恢复或发生系统修正。**

项目原则：

`REFOUND, NOT REJECT`。

## 0. 当前权威

本文件定义项目使命、层次和当前路由。

当前原生数学的稳定入口：

`definitions/00_CURRENT_NATIVE_FOUNDATION.md`。

当前 FREE 公理发现的原始基础入口：

`definitions/00_FREE_AXIOM_DISCOVERY_SUBSTRATE.md`。

精确数学声明以任务实际使用的 exact canonical definition 为准。

## 1. 当前进取平面

当前原生平面：

- `O_E=0`；
- 原点是三个 circle cells 的三重边界交点；
- `ENTERPRISE_CELL=CIRCLE_CELL`；
- 最近圆心间距 `D_CENTER=1`；
- `R_CELL=1/sqrt(3)`；
- 原生轴为三条正射线 `E_1,E_2,E_3`；
- `ENTERPRISE_RIGHT_ANGLE=120_DEGREES`；
- 三轴两两 `ENTERPRISE_ORTHOGONAL`；
- `ENTERPRISE_PLANE_DIMENSION=3` 是项目自己的原生维数语义。

## 2. 当前坐标与长度

原生地址：

`A_E={(a,b,c) in N_0^3 : min(a,b,c)=0}`。

三个正二轴 chart：

- `S_12={(a,b,0)}`；
- `S_23={(0,b,c)}`；
- `S_31={(a,0,c)}`。

在原生 `120°` 扇区内：

`L_E^2=a^2+b^2`。

对 canonical triple：

`L_E(a,b,c)^2=a^2+b^2+c^2`。

载体关系只在明确标记的 implementation/classical layer 使用，不自动成为 native identity 或 native metric。

## 3. 当前线与点到点结构

`ENTERPRISE_LINE_IDENTITY=NATIVE_COMPONENT_TRACE`。

同一 trace 可以有多个离散单-cell 路径代表；路径字母数不等于原生线长度。

任意点之间使用当前的**有向原生线 gauge**。

无向端点对的 canonical 数据是双向 trace pair 与 bidirectional length spectrum；当前 premises 不唯一选定一个 canonical symmetric scalar metric。

## 4. BRC

`BRC=Branch-Recoalescence Collapse`。

当前 BRC 基层：

`CANONICAL_BRC_BASE_LAYER=BOOLEAN_RESULT_SUPPORT_SEMANTICS`。

当前 enrichment：

`PATH_FORMAL_BRC -> N_BRC -> BOOLEAN_BRC`。

经典/工程 readout 可以作为 typed compatibility layer，但不得把目标侧定义反向写成 native premise。

## 5. 定义不继承

`Definition is not inherited.`

成熟概念可以保留；禁止的是因为某个经典定义有效，就未经证明把它直接当成 native premise，再把其恢复当成新推导。

经典/工程成功是强证据与 calibration target，不是自动 ontology。

## 6. 项目层次

- `P0`：数、精度、整数、离散状态、关系、collapse/quotient；
- `P1`：packet/cell、adjacency、transition、path、branch/recoalescence、进取坐标/代数；
- `P2`：重建 length、distance、angle、norm、pairing、projection、area/volume、curve；
- `P3`：重建 trig、pi 语义、坐标变换、分析工具；
- `P4`：经典/连续/工程 recovery/deviation 分类；
- `P5`：数学语义冻结后的物理与工程校准。

必须区分：

`PACKET_COUNT != TRANSITION_COUNT != GEOMETRIC_LENGTH`。

## 7. 恢复分类

- `EXACT_RECOVERY`
- `FINITE_PRECISION_RECOVERY`
- `ASYMPTOTIC_RECOVERY`
- `DOMAIN_RESTRICTED_RECOVERY`
- `SYSTEMATIC_DEVIATION`
- `NONRECOVERY`

偏差必须可推导、可复现、可检验。

## 8. 当前项目栈

`NUMBER -> PRECISION -> DISCRETE STATE -> RELATION/PATH/BRC -> THREE-POSITIVE-AXIS ENTERPRISE COORDINATES -> REBUILT GEOMETRY -> TRIG/ANALYSIS -> CLASSICAL COMPATIBILITY/CORRECTION -> PHYSICS -> ENGINEERING`。

> **不是把旧数学推倒，而是让它拥有一个更好的地基。**

## 9. 当前世界观

账户级受保护 `我眼中的世界.md` 与本项目当前空间基础一致，并提供当前有限精度与后分配研究公理。

## 10. 历史访问

本文件不重复项目旧代际、旧路线或 supersession 叙事。需要历史/provenance 时，从 Git history、journal 或明确历史文件检索。
