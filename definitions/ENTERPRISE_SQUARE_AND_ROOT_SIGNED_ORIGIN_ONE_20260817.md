# 进取平方与平方根：带符号原点一校正版

Status: `ACTIVE / CANONICAL_FOUNDATIONAL_CORRECTION`
Date: `2026-08-17`
Driver: `EM-DVR-9GP3M7 / CONTROL_PLANE`
Depends on: `definitions/ENTERPRISE_SIGNED_ORIGIN_ONE_COORDINATE_20260817.md`
Supersedes: `definitions/ENTERPRISE_SQUARE_AND_ROOT_ORIGIN_ONE_20260817.md`

## 1. 纠错结论

此前 origin-one rebuild 把“从原点 `±1` 到坐标 `±n` 的邻接步数为 `n-1`”错误地等同为“原生坐标幅值必须改成 `n-1`”，进而得到

`ENTERPRISE_SQUARE(n)=1+(n-1)^2`。

该推导错误。

新的 signed-origin 定义冻结：

`+1 ≡ -1 ≡ O_E`

`0` 不存在；

`ENTERPRISE_COORDINATE_MAGNITUDE(±n)=n`；

邻接步数 `n-1` 只是外部图距离，不替代原生坐标幅值。

## 2. 单位四边形精确反例

用户/Driver 给出基础四边形

`Q=((±1,±1,±1),(2,1,1),(1,-2,1),(1,1,2))`。

在原生邻接语义下冻结：

`PERIMETER_E(Q)=4`

`AREA_E(Q)=4`。

因为第一层外邻坐标幅值为 `2`，任何合法平方定义必须满足

`ENTERPRISE_SQUARE(2)=4`。

所以 `1+(2-1)^2=2` 与该原生校准矛盾，前一版本被 exact counterexample supersede。

## 3. 恢复进取平方公式

对原生坐标幅值 `n>=1`，进取平方继续定义为普通自乘的几何平方读数：

`ENTERPRISE_SQUARE(n)=n*n=n^2`。

若原生点带方向符号 `±n`，平方丢弃方向符号并返回正的标量平方态：

`ENTERPRISE_SQUARE(+n)=ENTERPRISE_SQUARE(-n)=n^2`。

特别：

`SQUARE_E(±1)=1`

`SQUARE_E(±2)=4`

`SQUARE_E(±3)=9`

`SQUARE_E(±4)=16`。

因此 exact square-state sequence 重新冻结为

`1,4,9,16,25,...`。

注意：这里没有坐标 `0` 项；序列从原点幅值 `1` 开始。

## 4. 平方根恢复

在正 square-state domain 上：

`ENTERPRISE_ROOT(n^2)=n`, `n>=1`。

首项：

`ROOT_E(1)=1`

`ROOT_E(4)=2`

`ROOT_E(9)=3`

`ROOT_E(16)=4`。

平方映射不保存方向，因此 `ROOT_E(n^2)=n` 返回坐标幅值；若需要方向分支，必须另带方向信息，不能从平方值单独恢复 `+/-`。

## 5. 邻接步数不控制平方公式

从原点到 `±n` 的外部 primitive step count 确实是 `n-1`：

`STEP_COUNT(O_E,±n)=n-1`。

但 square 的输入是原生坐标幅值 `n`，不是外部图距离。

因此：

`STEP_COUNT^2=(n-1)^2`

可以作为外部图距离平方；

而

`ENTERPRISE_SQUARE(n)=n^2`

是原生坐标平方。

二者属于不同类型，不得再互相替代。

## 6. 对旧三角胞元计数的重新解释

旧 triangular-cell 结果仍可按其明确参数继续使用，但必须说明参数到底是：

- 原生坐标幅值 `n`；还是
- 外部 primitive interval count `m`。

若一个具体 cell census 以 `m` 条 primitive intervals 为边长，则其 ordinary cell count 可以出现 `m^2`；这不自动重新定义原生 `SQUARE_E(n)`。

因此本次修正恢复 square/root 公式，但同时保留“坐标幅值与图距离不可混同”的类型纪律。

## 7. 最高冻结

正式冻结：

`ENTERPRISE_ORIGIN = ±1`

`ZERO_IS_NOT_AN_ENTERPRISE_COORDINATE`

`ENTERPRISE_SQUARE(n)=n^2, n>=1`

`ENTERPRISE_ROOT(n^2)=n, n>=1`

`STEP_COUNT(O_E,±n)=n-1` is external and does not redefine square.

若以后新的原生几何给出 exact counterexample，再按用户规则推倒重来；在被 supersede 前，本文件是当前 canonical square/root definition。
