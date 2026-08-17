# 进取坐标系：带符号原点一 / 零不存在

Status: `ACTIVE / CANONICAL_FOUNDATIONAL_SUPERSESSION`
Date: `2026-08-17`
Driver: `EM-DVR-9GP3M7 / CONTROL_PLANE`

## 1. 冻结决定

从本定义起，进取数轴不是把经典零原点数轴整体平移一格，也不是只保留正整数射线。

正式冻结：

`ENTERPRISE_COORDINATE_ORIGIN = ±1 (single glued state)`

`+1 ≡ -1 ≡ O_E`

`0` 不属于进取坐标系。

原点同时具有正、负两个方向代表；`+1` 与 `-1` 不是两个不同点，而是同一个原点状态的两个方向代表。

因此沿正方向从原点走一个 primitive step 到 `+2`；沿负方向从原点走一个 primitive step 到 `-2`。不存在原生坐标 `0`，也不存在“先从 +1 到 0 再到 -1”的路径。

## 2. 一条进取原生轴

一条无向原生轴的状态空间定义为

`A_E = {O_E} ∪ {+n,-n : n>=2}`

其中

`O_E=[+1]=[-1]`。

原生邻接为：

- `O_E ~ +2`；
- `O_E ~ -2`；
- `+n ~ +(n+1)`，`n>=2`；
- `-n ~ -(n+1)`，`n>=2`。

因此原生轴可写成

`...,-4,-3,-2,±1,+2,+3,+4,...`

其中 `±1` 只表示一个粘合原点，`0` 永不出现。

## 3. 三轴原点

在进取平面的三条原生轴表示中，原点可写为

`(±1,±1,±1)`。

这里每一个 `±1` 都是该轴原点的方向代表。所有八种符号选择都属于同一个几何原点状态：

`(s1*1,s2*1,s3*1) ~ O_E`, `s_i in {+,-}`。

因此以下都是从原点沿一条原生方向走一个 primitive step 的合法点态示例：

- `(2,1,1)`；
- `(-2,1,1)`；
- `(1,2,1)`；
- `(1,-2,1)`；
- `(1,1,2)`；
- `(1,1,-2)`。

未移动轴上的 `1` 可以按需要选择 `+1/-1` 方向代表；它们在原点分量上等价。

## 4. 0 与负号的正式类型

冻结：

`ZERO_IS_NOT_AN_ENTERPRISE_COORDINATE`。

但负号是合法的原生方向信息：

`-2,-3,...` 是合法原生坐标状态。

所以被撤销的是此前“负号只能放在方向标签、原生坐标值本身只取正整数”的表述。

正确规则是：

- `±1`：同一原点的双符号代表；
- `±n (n>=2)`：不同方向上的不同原生点态；
- `0`：不存在于原生坐标状态空间。

## 5. 坐标幅值与邻接步数必须区分

从原点 `±1` 到 `±n` 的 primitive adjacency step 数为外部计数 `n-1`。

但这不意味着原生坐标幅值应改写为 `n-1`。

冻结两种不同对象：

- `ENTERPRISE_COORDINATE_MAGNITUDE(±n)=n`；
- `EXTERNAL_ADJACENCY_STEP_COUNT(O_E,±n)=n-1`。

坐标幅值是原生状态标签/尺度；邻接步数是外部图距离。不得把二者相减一后混同。

这正是此前错误重推 `ENTERPRISE_SQUARE(n)=1+(n-1)^2` 的根源。

## 6. 与旧零中心辅助图的精确重编码

旧的有符号整数辅助坐标可以继续作为外部计算 chart，但不含原生 `0`。

定义一维编码：

`ENC_SIGNED(0)=O_E=[+1]=[-1]`

`ENC_SIGNED(k)=sign(k)*(|k|+1)` for `k!=0`。

逆编码：

`DEC_SIGNED(O_E)=0`

`DEC_SIGNED(±n)=±(n-1)` for `n>=2`。

因此旧 `Z` 型辅助 chart 与新的无零原生轴在邻接图层面存在自然双射。任何旧公式若要恢复 native status，必须通过该编码共轭证明，而不能直接把旧坐标 `0` 当成原生点。

## 7. 单位四边形校准

用户/Driver 给出新的基础校准四边形：

`Q=((±1,±1,±1),(2,1,1),(1,-2,1),(1,1,2))`。

在原生邻接语义下，它的四条边均为一个 primitive edge，冻结：

`PERIMETER_E(Q)=4`

`AREA_E(Q)=4`。

该校准点直接否定把第一层外邻点 `2` 的平方改写为 `2` 的公式。

## 8. Supersession

本定义 supersedes：

- `definitions/ENTERPRISE_POINT_ORIGIN_AND_DISPLACEMENT_ZERO_20260817.md`；
- `definitions/ENTERPRISE_COORDINATE_ORIGIN_ONE_NO_ZERO_20260817.md` 中“原生坐标只取正整数、负号仅属于方向标签”的部分。

保留：`0` 不属于进取坐标系。

改变：原点不是单符号 `1`，而是 `+1≡-1` 的双向粘合态；负坐标 `-n (n>=2)` 为合法原生坐标。

## 9. 最高路由规则

以后所有 Enterprise Math 原生坐标默认：

`ORIGIN = ±1`

`+1 ≡ -1`

`0 DOES NOT EXIST AS NATIVE COORDINATE`

`ONE NEGATIVE STEP FROM ORIGIN = -2`

`ONE POSITIVE STEP FROM ORIGIN = +2`。

若历史结果使用零中心辅助 chart，必须标记 auxiliary/external，或给出 `ENC_SIGNED` 共轭重编码后再恢复 native typing。
