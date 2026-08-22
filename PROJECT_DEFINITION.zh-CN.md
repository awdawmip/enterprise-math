# 进取数论项目定义

Status: `ACTIVE / PROJECT-LEVEL DEFINITION / V3`
Date: `2026-08-21`
Driver: `CONTROL_PLANE`

## 一句话定义

> **进取数论以有限分辨率、精度内生、整数优先和离散可计算为底层研究立场，重新奠基现代数学中已经证明有用的代数、几何、三角、分析与物理工具，并明确它们何时精确恢复、有限精度恢复、渐近恢复或发生系统修正。**

项目总原则：

`REFOUND, NOT REJECT`

即：**重建，而不是废弃。**

## 0. 权威链

本文件定义项目使命、层次和最高路由规则；易变化的具体几何/坐标数学不再复制在多个顶层文件中。

当前原生平面基础的权威来源为：

`definitions/ENTERPRISE_THREE_POSITIVE_AXIS_OVERLAPPING_CIRCLE_CELL_PLANE_20260820.md`

其后当前线、任意点位移、无向段和 BRC × multipath 的冻结定义依次见：

- `definitions/ENTERPRISE_NATIVE_LINE_TRACE_FORMULA_20260821.md`
- `definitions/ENTERPRISE_ARBITRARY_POINT_DIRECTED_LINE_GAUGE_20260821.md`
- `definitions/ENTERPRISE_UNORIENTED_BIDIRECTIONAL_SEGMENT_SPECTRUM_20260821.md`
- `definitions/ENTERPRISE_BRC_MULTIPATH_ENRICHMENT_BRIDGE_20260821.md`

若本文件历史版本、2026-08-16/17 的旧坐标文件或旧任务书与上述当前基础冲突，以较新的明确 supersession/foundational correction 为准。旧文件保留为历史/provenance，不得与当前 foundation 并列争夺权威。

## 1. 当前进取平面的最高结构

当前原生平面冻结：

- `O_E = 0`；
- 原点是三个圆胞元边界的三重交点，不是 cell center，也不是 cell；
- `ENTERPRISE_CELL = CIRCLE_CELL`，cell 由离散圆心标识；
- 最近圆心间距 `D_CENTER=1`；
- 圆胞元半径 `R_CELL=1/sqrt(3)`；
- 相邻圆胞元有正面积重叠，全部圆胞元无缝覆盖平面；
- 原生轴恰为三条**正射线** `E_1,E_2,E_3`；
- 不要求、也不得自动补回原生负轴；
- 三条正轴把一周分成三个 `120°` 原生直角扇区；
- `ENTERPRISE_RIGHT_ANGLE = 120_DEGREES`；
- 三轴两两 `ENTERPRISE_ORTHOGONAL`，这里的“垂直”是进取垂直，不是载体图上的欧式 90°。

因此，旧的：

`3 条无向轴 -> 6 个原生有向方向 -> 60° 正负交错`

不再是当前原生平面定义。

`ENTERPRISE_PLANE_DIMENSION = 3` 继续作为项目自己的维数语义；它不等同于经典线性代数秩、欧式维数或拓扑维数。当前平面中的三个原生维分量由三条正轴/三个正轴族承担，而不是由每轴自动补出的正负双向定义。

## 2. 当前坐标与长度

原生地址使用：

`A_E={(a,b,c) in N_0^3 : min(a,b,c)=0}`

它是三个二轴正扇区 chart 的粘合：

- `S_12={(a,b,0)}`；
- `S_23={(0,b,c)}`；
- `S_31={(a,0,c)}`。

这不是公共对角平移商。

在每个原生 `120°` 直角扇区内：

`L_E^2=a^2+b^2`

因此对 canonical origin-sector triple：

`L_E(a,b,c)^2=a^2+b^2+c^2`。

`(3,4,0)` 的原生长度为 `5`。

旧载体关系 `e_1+e_2+e_3=0`、`u+v+w=0` 及二自由度 A2/C6 表示只能作为 `I0_IMPLEMENTATION_CARRIER / CLASSICAL_COMPATIBILITY` 使用，不能作为原生向量恒等式、负轴来源或 native metric。

## 3. 当前线与点到点结构

当前线身份：

`ENTERPRISE_LINE_IDENTITY = NATIVE_COMPONENT_TRACE`。

同一 trace 可以有多个离散单 cell 路径代表；例如 `(3,4)` trace 有 `35` 个 shuffle/path representatives，而 native length 为 `5`。

任意点之间使用当前冻结的**有向原生线 gauge**。它平移不变、正定并满足三角次可加，但一般不满足反向长度对称，因此：

`NATIVE_INTEGER_VERTEX_DISTANCE_IS_METRIC = false`。

无向端点对的 canonical 数据是双向 trace pair 与 bidirectional length spectrum；可以附加构造多种对称 metric，但当前 premises 不唯一选择其中任何一个作为 canonical native scalar metric。

## 4. BRC 的定位

BRC 保留其正式名称和桥梁定位：

`BRC = Branch-Recoalescence Collapse`。

经典/垂直坐标语义与进取坐标语义之间可以建立可计算 collapse/readout bridge，但不得把经典目标定义复制进 native premise。

当前 R062 进一步冻结：

`PATH_FORMAL_BRC -> N_BRC -> BOOLEAN_BRC`

以及：

`BRC_IS_EXACT_BOOLEAN_SHADOW_OF_COMPONENT_TYPED_NATIVE_MULTIPATH = true`。

Boolean BRC 保存 support，不保存已经丢弃的路径身份、multiplicity 或 provenance；component labels 对区分“同 endpoint”与“同 native line”是必要的。

## 5. 精度数学的项目归属

`Precision Mathematics / 精度数学` 是进取数论的前身，不再作为独立同级研究项目。

从 2026-08-21 起，有限分辨率数轴、precision-defined number、精度内生、离散/整数优先等路线的全部新工作统一属于 Enterprise Math。

历史精度数学文件继续保留来源关系，不抹除其 provenance。

## 6. 《我眼中的世界》已经统一到三正轴

账户级受保护文件 `我眼中的世界.md` 已由用户在 2026-08-21 当前对话中直接修改：旧“六维十二方向 / 每平面六方向 / 60° 正负交错”世界模型不再 ACTIVE。

当前世界观与本项目当前 foundation 一致：

- `WORLDVIEW_SPATIAL_FOUNDATION = THREE_POSITIVE_AXIS_ENTERPRISE_PLANE`；
- `O_E=0`；
- `NO_NATIVE_NEGATIVE_AXES_REQUIRED`；
- `ENTERPRISE_RIGHT_ANGLE=120_DEGREES`；
- `OLD_6D_12_DIRECTION_WORLD_MODEL = SUPERSEDED_BY_USER`；
- `OLD_60_DEGREE_ALTERNATING_SIGN_PLANE = SUPERSEDED_BY_USER`。

因此项目层不再保留第二套“六维/十二方向”世界实现，也不需要三正轴到该旧模型的桥接任务。历史材料只保留 provenance。

## 7. “定义不继承”的正式含义

`Definition is not inherited.` 不等于禁止成熟概念。

允许保留：VECTOR、LENGTH、DISTANCE、ANGLE、NORM、PAIRING/DOT、PROJECTION、SIN/COS/TAN、AREA/VOLUME、PI、Euclidean geometry、continuum models 等概念和正确条件数学。

禁止的是：因为经典定义成功，就未经证明把它当成 native premise，再把同一对象的恢复当成新推导。

经典/工程成功是强证据和 calibration target，但不是 native definition 的自动来源。

## 8. 项目层次

- `P0`：数、精度、整数、离散状态、关系、collapse/quotient；
- `P1`：packet/cell、adjacency、transition、path、branch/recoalescence、进取坐标/代数；
- `P2`：重建 length、distance、angle、norm、pairing、projection、area/volume、curve 等几何工具；
- `P3`：重建 trig、pi 语义、坐标变换、分析工具；
- `P4`：与欧式/连续/工程数学做 recovery/deviation 分类；
- `P5`：数学定义冻结后进入物理和工程校准。

必须继续区分：

`PACKET_COUNT != TRANSITION_COUNT != GEOMETRIC_LENGTH`。

## 9. 恢复分类

成熟工具与经典对象比较时使用：

- `EXACT_RECOVERY`
- `FINITE_PRECISION_RECOVERY`
- `ASYMPTOTIC_RECOVERY`
- `DOMAIN_RESTRICTED_RECOVERY`
- `SYSTEMATIC_DEVIATION`
- `NONRECOVERY`

偏差本身不是“更好”的证据；必须可推导、可复现、可检验。

## 10. 总纲

当前项目栈：

`NUMBER -> PRECISION -> DISCRETE STATE -> RELATION/PATH/BRC -> THREE-POSITIVE-AXIS ENTERPRISE COORDINATES -> REBUILT GEOMETRY -> TRIG/ANALYSIS -> CLASSICAL COMPATIBILITY/CORRECTION -> PHYSICS -> ENGINEERING`

项目口号保持：

> **不是把旧数学推倒，而是让它拥有一个更好的地基。**

具体基础研究纪律继续由 `FOUNDATIONAL_LOGIC.md`、`foundational_logic.json`、`native_semantics_admissibility.json` 和 `GEOMETRIC_TOOL_REFOUNDATION_POLICY.md` 控制。