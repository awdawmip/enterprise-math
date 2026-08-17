# 进取坐标系与 BRC 坍缩桥梁

Status: `ACTIVE / CANONICAL_TERMINOLOGY_AND_ROUTE`
Date: `2026-08-16`
Updated: `2026-08-17 SIGNED-ORIGIN-ONE / NO-ZERO CORRECTION`
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

## 2. 带符号原点一 / 零不存在

当前最高 foundational definition：

`definitions/ENTERPRISE_SIGNED_ORIGIN_ONE_COORDINATE_20260817.md`

正式冻结：

`+1 ≡ -1 ≡ O_E`

`ENTERPRISE_ZERO_COORDINATE_EXISTS = false`。

因此：

- 原点不是单符号 `1`，而是 `+1/-1` 两个方向代表粘合成的同一个状态；
- 原生一维轴写成 `...,-4,-3,-2,±1,+2,+3,+4,...`；
- 沿正方向离开原点一个 primitive step 到 `+2`；
- 沿负方向离开原点一个 primitive step 到 `-2`；
- `0` 不作为原生坐标点、坐标分量或轴端点；
- `-2,-3,...` 是合法的原生负方向坐标；
- 三轴原点可写成 `(±1,±1,±1)`，所有符号组合代表同一个几何原点状态。

必须区分：

`ENTERPRISE_COORDINATE_MAGNITUDE(±n)=n`

与

`EXTERNAL_ADJACENCY_STEP_COUNT(O_E,±n)=n-1`。

后者是外部图距离，不能用来把原生尺度整体减一。

## 3. 旧零中心 chart 的正确位置

旧 `(a,b,...) in Z^k` 零中心有符号坐标不再直接作为原生坐标出现，但存在自然外部重编码：

`ENC_SIGNED(0)=O_E=[+1]=[-1]`

`ENC_SIGNED(k)=sign(k)*(|k|+1)` for `k!=0`。

因此旧零中心 chart 可以继续作为 `AUXILIARY / EXTERNAL COMPUTATION CHART`。若要恢复某历史结果的 native typing，必须证明相关结构在 `ENC_SIGNED` 共轭下保持，而不能把辅助 chart 的 `0` 直接认作原生坐标。

## 4. 图示术语

需要在传统二维纸面或屏幕上表达进取坐标系时，统一使用：

- **经典二维兼容图示**；
- `CLASSICAL_2D_COMPATIBILITY_VIEW`。

图示只是表示接口，不定义进取坐标系本体。

## 5. 垂直坐标系

传统以经典垂直/直角/正交关系建立的坐标表示称为：

**垂直坐标系**（`ORTHOGONAL_COORDINATE_SYSTEM`）。

经典欧式/笛卡尔工具保留在兼容层，不作为进取坐标系的原生定义。

## 6. BRC 的定位

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

## 7. 桥梁不预设可逆

允许：

- 多个垂直坐标状态坍缩到同一个进取状态；
- 一个进取状态在经典兼容层有多个表示；
- 只在声明域内存在精确逆映射；
- 在有限精度下形成等价类或区间对应。

## 8. 与 R059D 历史路线的关系

R059D W–AO 中围绕 frontier/circle/BRC 的组合和极限结果继续保留。

此前因为用户先冻结“原点 1、0 不存在”而将其零中心 chart native status 暂停。现在 signed-origin 结构给出了显式 `ENC_SIGNED` 重编码，因此下一步若需要恢复 R059D native status，应做**共轭重编码审计**，而不是从头假定旧 `0` 是原生点。

当前冻结：

`R059D_COMBINATORIAL_RESULTS = PRESERVED`

`R059D_NATIVE_STATUS = PENDING_SIGNED_ORIGIN_CONJUGACY_AUDIT`。

## 9. 进取平方与平方根

当前 canonical definition：

`definitions/ENTERPRISE_SQUARE_AND_ROOT_SIGNED_ORIGIN_ONE_20260817.md`

用户给出的基础四边形

`Q=((±1,±1,±1),(2,1,1),(1,-2,1),(1,1,2))`

满足：

`PERIMETER_E(Q)=4`

`AREA_E(Q)=4`。

因此此前 `1+(n-1)^2` 重推被 exact counterexample 推倒。

正式恢复：

`ENTERPRISE_SQUARE(n)=n^2`, `n>=1`

`ENTERPRISE_ROOT(n^2)=n`, `n>=1`。

平方态序列为：

`1,4,9,16,25,...`，不含 `0` 项。

## 10. 最高路由规则

以后研究中：

1. 平面三轴原生结构统一称 **进取坐标系**；
2. 原点统一为 `+1 ≡ -1` 的 signed glued origin；
3. `0` 不属于进取原生坐标系；
4. `-n (n>=2)` 是合法负方向原生坐标；
5. 二维展示统一称 **经典二维兼容图示**；
6. BRC 默认研究 **垂直坐标系 ↔ 进取坐标系**；
7. 旧零中心 chart 仅作为辅助计算 chart，恢复 native status 需做 `ENC_SIGNED` 共轭审计；
8. 进取平方/开方保持 `n^2 <-> n`，不得再因邻接步数 `n-1` 擅自平移公式。
