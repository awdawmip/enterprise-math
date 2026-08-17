# 进取坐标系原点一与零不存在原则

Status: `ACTIVE / CANONICAL_FOUNDATIONAL_SUPERSESSION`
Date: `2026-08-17`
Driver: `EM-DVR-9GP3M7 / CONTROL_PLANE`

## 1. 用户冻结决定

从本定义起，进取坐标系的原生数轴与原生坐标状态正式冻结为：

`ENTERPRISE_COORDINATE_ORIGIN = 1`

`ENTERPRISE_ZERO_COORDINATE_EXISTS = false`

`0` 不属于进取坐标系，不作为进取数轴点、不作为原生坐标分量、不作为原生轴端点，也不再存在所谓“进取位移空间中的零坐标”。

本定义 supersedes：

`definitions/ENTERPRISE_POINT_ORIGIN_AND_DISPLACEMENT_ZERO_20260817.md`

尤其 supersede 其中：

`ENTERPRISE_DISPLACEMENT_ZERO = 0`

以及“原生位移坐标继续零中心”的表述。

## 2. 原生数轴

每条有向原生轴上的坐标状态取值为：

`1,2,3,...`

方向单独承担朝向/正负语义。

对于任意两个有向方向 `d,d'`，其坐标 `1` 识别为同一个共享原点：

`(d,1) ~ (d',1) = O_E`。

沿方向 `d` 向外一个 primitive step 后坐标为 `2`；再向外一步为 `3`；依次类推。

原点处向同一有向射线的“前一个坐标”不存在；不得写成 `0`。跨过原点应改变方向标签，而不是经过坐标 `0`。

因此原生一维轴不是经典的

`...,-2,-1,0,1,2,...`

而是两个方向射线通过共享的 `1` 粘合：

`..., (d_-,3),(d_-,2), 1, (d_+,2),(d_+,3), ...`

其中 `1` 只出现一次。

## 3. 原生多轴坐标纪律

若采用局部多分量原生坐标表示，则每一个原生坐标分量都必须属于 `{1,2,3,...}`。

原生坐标中禁止出现：

- `0` 分量；
- `-n` 作为“负坐标值”；
- 通过 `0` 表示“未沿某轴移动”的传统笛卡尔式空分量。

方向、轴选择、粘合关系与有限控制状态必须承担这些传统由正负号/零分量承担的语义。

## 4. 外部步数不是原生坐标

为了计数两个原生点之间包含多少 primitive intervals，可在证明/兼容层定义外部步数：

`STEP_COUNT(n)=n-1`。

这里的 `n-1` 属于环境数学/计数语言，不是一个进取坐标值。

因此当 `n=1` 时，可以在外部计数语言中说“primitive interval 数为空 / 数量为 0”，但该 `0` 不进入进取坐标系。

最高类型规则：

`ZERO_MAY_APPEAR_AS_EXTERNAL_CARDINAL_OR_ALGEBRAIC_SYMBOL`

`ZERO_MUST_NOT_APPEAR_AS_ENTERPRISE_COORDINATE_STATE`

## 5. 对旧零中心坐标公式的重新定型

任何含有原生坐标 `0` 的旧公式，从本定义起不得继续称为“进取原生坐标公式”。

包括但不限于：

- `(r,0)`；
- `(0,r)`；
- `(0,0,0)`；
- `R(a,b)=(-b,a+b)` 若其 `a,b` 被解释为原生坐标分量；
- 任何以有符号整数格 `Z^k` 作为进取坐标本体的表述。

这些公式可以保留为：

`LEGACY_SIGNED_AUXILIARY_CHART / EXTERNAL_COMPUTATION_CHART`

但其 native-coordinate typing 被撤销，除非后来给出无零、方向显式的等价重编码定理。

## 6. 对 R059D 的基础影响

R059D AG–AO 已冻结的组合恒等式、整数递推、极限、BRC 比较结果不会因为本次决定自动变成“算术上错误”；但其中使用的零中心/有符号坐标表示不再具有原生坐标资格。

因此冻结：

`R059D_ZERO_CENTERED_CHART_NATIVE_STATUS = SUSPENDED`

`R059D_COMBINATORIAL_RESULTS = PRESERVED_AS_LEGACY_CHART_RESULTS_PENDING_REENCODING_AUDIT`

特别是此前称为 canonical Enterprise native circle 的结果，需要在无零原生坐标语义下重新完成坐标重编码/资格审计后，才能恢复完全 native 的称号。

这不是宣布其定理数值全部错误，而是撤销一个已被用户 supersede 的坐标本体前提。

## 7. 平方与平方根必须重推

旧平方定义使用：

`T_n=((0,0,0),(n,0,0),(0,-n,0))`

因此把“从 0 到 n 有 n 个 primitive intervals”写入了几何面积计数。

在本定义下，从原点 `1` 到点态 `n` 的 primitive interval 数是外部计数 `n-1`。

所以旧的几何推导

`ENTERPRISE_SQUARE(n)=n*n`

不得继续作为原生坐标态平方定义直接继承；必须从 origin-one / no-zero 几何重新推导。

新的 canonical 推导见：

`definitions/ENTERPRISE_SQUARE_AND_ROOT_ORIGIN_ONE_20260817.md`

## 8. 最高路由规则

以后所有 Enterprise Math 工作默认：

1. 原生坐标原点是 `1`；
2. `0` 不属于进取坐标系；
3. 方向承担正负/朝向；
4. 外部证明可以使用普通整数、差值与零计数，但必须标注其非原生坐标类型；
5. 任何依赖零坐标本体的历史结果必须先重编码再获得 native status；
6. 若基础定义与历史任务冲突，以本定义为准。
