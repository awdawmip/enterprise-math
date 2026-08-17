# 进取坐标系原点一与零不存在原则

Status: `SUPERSEDED_BY_SIGNED_ORIGIN_ONE`
Date: `2026-08-17`
Driver: `EM-DVR-9GP3M7 / CONTROL_PLANE`

本文件已被更精确的 signed-origin 定义 supersede：

`definitions/ENTERPRISE_SIGNED_ORIGIN_ONE_COORDINATE_20260817.md`

保留的结论：

- `0` 不属于进取原生坐标系。

被撤销/修正的结论：

- 原点不是单符号 `1`，而是 `+1 ≡ -1 ≡ O_E` 的双向粘合态；
- `-2,-3,...` 是合法原生负方向坐标，不应全部改写成独立方向标签加正整数；
- 从原点沿负方向一个 primitive step 到 `-2`，不是到 `-1`；
- 三轴原点可写成 `(±1,±1,±1)`，所有符号选择代表同一个原点状态；
- 外部 step count `n-1` 不重新定义原生坐标幅值 `n`。

因此本文件此前据 `n-1` 重推平方/平方根的路由也已失效。当前平方/平方根见：

`definitions/ENTERPRISE_SQUARE_AND_ROOT_SIGNED_ORIGIN_ONE_20260817.md`。
