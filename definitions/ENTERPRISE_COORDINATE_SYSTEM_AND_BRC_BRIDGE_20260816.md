# 进取坐标系与 BRC 坍缩桥梁

Status: `ACTIVE / CANONICAL_TERMINOLOGY_AND_ROUTE`
Date: `2026-08-16`
Updated: `2026-08-17 ORIGIN-ONE / NO-ZERO SUPERSESSION`
Driver: `EM-DVR-9GP3M7 / CONTROL_PLANE`

## 1. 正式名称：进取坐标系

进取数论平面上的三轴原生坐标结构正式命名为：

**进取坐标系**（`ENTERPRISE_COORDINATE_SYSTEM`）。

进取坐标系的平面结构为：

- `3` 个进取维；
- `3` 条原生无向数轴；
- `6` 个有向方向；
- 三条轴两两满足 `ENTERPRISE_ORTHOGONAL`（进取垂直）；
- 任取一个方向为正后，相邻 `60°` 方向正负交错，除整体反号外全局唯一。

`0°/60°/120°` 只是在经典二维兼容图示中标注三条进取轴方向的校准方式；它们不改变进取坐标系自身的三维轴定义。

## 2. 原点一 / 零不存在

当前最高 foundational definition：

`definitions/ENTERPRISE_COORDINATE_ORIGIN_ONE_NO_ZERO_20260817.md`

正式冻结：

`ENTERPRISE_COORDINATE_ORIGIN = 1`

`ENTERPRISE_ZERO_COORDINATE_EXISTS = false`。

因此：

- 原生数轴点态只取 `1,2,3,...`；
- `1` 是所有有向轴共享的唯一原点；
- `0` 不属于进取坐标系，不作为坐标点、坐标分量、轴端点或所谓“原生位移零元”；
- 正负/朝向由方向标签承担，而不是由负坐标或零中心有符号轴承担；
- 从 `1` 到 `n` 的 primitive interval 数可在外部证明语言中写为 `n-1`，但该差值不是原生坐标。

任何 `(r,0)`、`(0,r)`、`(0,0,0)` 或有符号整数零中心格表示，从本定义起只能是：

`LEGACY_SIGNED_AUXILIARY_CHART / EXTERNAL_COMPUTATION_CHART`

不能继续称为 Enterprise native coordinates，除非后来证明无零方向编码下的等价重编码。

## 3. 图示术语

需要在传统二维纸面或屏幕上表达进取坐标系时，统一使用：

- **经典二维兼容图示**；
- `CLASSICAL_2D_COMPATIBILITY_VIEW`。

图示只是表示接口，不定义进取坐标系本体。

## 4. 垂直坐标系

传统以经典垂直/直角/正交关系建立的坐标表示称为：

**垂直坐标系**（`ORTHOGONAL_COORDINATE_SYSTEM`）。

经典欧式/笛卡尔工具保留在兼容层，不作为进取坐标系的原生定义。

## 5. BRC 的定位

BRC 正式定位为：

> **垂直坐标系与进取坐标系之间的可计算桥梁。**

记：

`BRC_COLLAPSE_BRIDGE(ORTHOGONAL_COORDINATE_SYSTEM, ENTERPRISE_COORDINATE_SYSTEM)`。

BRC 不是在进取坐标系内部重新生成坐标系，也不是把经典平方根机械取整。

后续 BRC 必须分别声明：

- source coordinate semantics；
- target native coordinate semantics；
- collapse relation；
- collision / fiber；
- inverse or compatibility readout status；
- precision layer。

## 6. 桥梁不预设可逆

允许：

- 多个垂直坐标状态坍缩到同一个进取状态；
- 一个进取状态在经典兼容层有多个表示；
- 只在声明域内存在精确逆映射；
- 在有限精度下形成等价类或区间对应。

## 7. 与 R059D 历史路线的关系

R059D W–AO 中围绕 frontier/circle/BRC 的结果保留为重要历史与组合/兼容证据。

但由于其中大量 target 计算使用 `(r,0)`、`(a,b)` 有符号零中心 chart，本次用户基础 supersession 后正式冻结：

`R059D_ZERO_CENTERED_CHART_NATIVE_STATUS = SUSPENDED`

`R059D_COMBINATORIAL_RESULTS = PRESERVED_PENDING_ORIGIN_ONE_REENCODING_AUDIT`。

因此不能仅凭旧零中心 chart 继续称其为最终 native coordinate realization；需要后续无零、方向显式的重编码/重证。

## 8. 进取平方与平方根

当前 canonical definition：

`definitions/ENTERPRISE_SQUARE_AND_ROOT_ORIGIN_ONE_20260817.md`

原点从 `0` 改为 `1` 后，从原点 `1` 到点态 `n` 的 primitive interval 数为外部 magnitude `n-1`。

因此完整进取平方的 raw geometric area 为：

`ENTERPRISE_SQUARE_RAW_AREA(n)=(n-1)^2`。

将 raw magnitude 编码回原生标量状态 `1,2,3,...` 后：

`ENTERPRISE_SQUARE(n)=1+(n-1)^2`。

其 exact inverse：

`ENTERPRISE_ROOT(1+(n-1)^2)=n`。

平方态序列：

`1,2,5,10,17,26,...`。

旧 `ENTERPRISE_SQUARE(n)=n*n` 作为原生坐标态平方定义已被 supersede；普通 `m^2` 继续可作为外部 primitive-step magnitude 的普通代数平方。

## 9. 最高路由规则

以后研究中：

1. 平面三轴原生结构统一称 **进取坐标系**；
2. 原点统一为 `1`；
3. `0` 不属于进取坐标系；
4. 二维展示统一称 **经典二维兼容图示**；
5. BRC 默认研究 **垂直坐标系 ↔ 进取坐标系**；
6. 任何依赖零中心 target coordinates 的历史路线必须先完成 origin-one/no-zero reencoding audit 才能恢复 native status；
7. 进取平方/开方使用 origin-one rebuilt definitions，而不是旧零原点公式。
