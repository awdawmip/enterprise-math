# 进取点态原点与位移零元

Status: `ACTIVE / CANONICAL_FOUNDATIONAL_SEMANTIC`
Date: `2026-08-17`
Driver: `EM-DVR-9GP3M7 / CONTROL_PLANE`

## 1. 冻结决定

从本定义起，进取数轴/进取坐标系正式区分两层语义：

1. **点态层（POINT-STATE SPACE）**：原生存在性基点从 `1` 开始；
2. **位移层（DISPLACEMENT SPACE）**：相对基点的零位移仍为 `0`。

正式冻结：

`ENTERPRISE_POINT_STATE_ORIGIN = 1`

`ENTERPRISE_DISPLACEMENT_ZERO = 0`

二者通过

`rho = 1 + r`

联系，其中：

- `rho in {1,2,3,...}` 是原生点态层级 / point-state level；
- `r in {0,1,2,...}` 是从中心基点出发的 primitive displacement / step radius。

因此中心态同时满足：

`rho=1`

和

`r=0`。

这不是 `0=1`，而是两个不同语义层的基准值。

## 2. 进取数轴的原生点态语义

在任一有向原生轴方向 `d` 上，点态可写为：

`(d,rho)`, `rho>=1`。

所有方向的 `rho=1` 识别为同一个中心存在态：

`(d,1) ~ (d',1) = O`。

向某方向离开中心一个 primitive step 后：

`rho=2`, `r=1`；

再走一步：

`rho=3`, `r=2`；

一般地：

`rho=r+1`。

因此“进取数轴以 1 为原点”的正式含义是：

> `1` 是第一个原生存在点态 / 中心 point-state label。

它不是说普通代数的加法零元被删除或替换。

## 3. 位移坐标继续零中心

所有此前和后续的局部/相对坐标运算仍在位移空间中使用 `0`。

例如：

- `(r,0)` 表示第二位移分量为零；
- `(0,r)` 表示第一位移分量为零；
- `R(a,b)=(-b,a+b)` 继续是位移坐标上的整数 D6 旋转；
- 平移差、步长差、残差、局部向量都继续以 `0` 为零元。

禁止把上述位移坐标中的 `0` 机械替换成 `1`。

## 4. 普通代数兼容性保持

本修正不改变普通代数：

- 加法零元仍为 `0`；
- 乘法单位元仍为 `1`；
- `ENTERPRISE_SQUARE(n)=n*n` 不变；
- 所有整数递推和代数恒等式按原定义保持。

因此本修正是 **POINT SPACE / DISPLACEMENT SPACE semantic separation**，不是新算术，也不是全局坐标平移。

## 5. 对 R059D 已冻结定理的重定型

R059D AG–AN 以及当前 AO 中使用的半径变量 `r`，统一重定型为：

`PRIMITIVE_DISPLACEMENT_RADIUS / STEP_RADIUS`。

也即：

`r=0` 表示中心 point-state `rho=1`；

`r=1` 表示第一层 point-state `rho=2`；

一般：

`rho=r+1`。

因此以下既有结果不需重算：

- `D(r)=2r+1`；
- `V(0)=1`；
- `J_N(r)=floor(alpha*r+1/3)`；
- `C_E(r)=T_r=6*(r+J_N(r))`；
- `kappa_E=lim T_r/(2r)`；
- `kappa_E^2=12`；
- AK fixed-length turn orbit；
- AL canonical resolver rigidity；
- AM/AN BRC fiber / pushforward-measure theorems。

它们中的 `r` 不是 point-state label，而是 displacement/step radius。

若改用原生点态层级 `rho`，应统一代换：

`r=rho-1`。

例如：

`D(rho)=2rho-1`。

## 6. 中心存在态与“零长度”的区分

中心 point-state `rho=1` 是一个真实存在态；这与 displacement radius `r=0` 完全兼容。

因此：

- `V(0)=1` 表示零位移半径下仍有一个中心存在态；
- `D(0)=1` 表示中心轴截面只有该一个点态；
- 真正非退化的 fixed-length turn orbit 从 `r>=1` 开始。

故：

`POINT-STATE EXISTENCE ORIGIN = 1`

`ZERO DISPLACEMENT = 0`

必须长期分开书写。

## 7. 正负/方向语义

进取坐标系已冻结为三条无向原生轴、六个有向方向。

因此原生点态无需把正负号编码成传统单轴上的 `...,-2,-1,0,1,2,...`。

更原生的表示是：

`DIRECTION + POSITIVE POINT-STATE LEVEL rho>=1`。

其中方向承担正负/朝向信息，`rho=1` 是六方向共享中心态。

位移计算层仍可继续使用有符号整数坐标 `(a,b,...)`；二者不得混同。

## 8. 对当前 AO 的约束

Stage AO 继续执行，不重开、不重算既有定理。

AO 中：

- 所有 `r` 均解释为 displacement/step radius；
- 若需要讨论“第几层原生点态”，必须显式写 `rho=r+1`；
- source/target refinement 使用 `r->infinity` 时，其含义是 displacement refinement；
- 不得因 point-state origin=1 而修改已冻结的 target displacement coordinates。

## 9. 最高路由规则

以后所有 Enterprise Math 工作默认遵守：

`ENTERPRISE_POINT_STATE_ORIGIN = 1`

`ENTERPRISE_DISPLACEMENT_ZERO = 0`

`rho = r + 1`

若文档仅写“原点”，必须说明是：

- `POINT-STATE ORIGIN`，还是
- `DISPLACEMENT ZERO`。

未区分者视为语义不完整。

本定义 supersedes 任何把“进取数轴的第一个存在点态”和“位移零元”默认视为同一对象的旧表述，但不改动既有代数零元、位移坐标公式与已证明 R059D 定理。