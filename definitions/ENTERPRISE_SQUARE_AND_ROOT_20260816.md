# 历史定义：进取半平方、进取平方与进取开方

Status: `SUPERSEDED_BY_ORIGIN_ONE_REBUILD`
Date: `2026-08-16`
Driver: `EM-DVR-9GP3M7 / CONTROL_PLANE`

本文件曾以零原点三角形

`T_n=((0,0,0),(n,0,0),(0,-n,0))`

为基础，冻结：

`ENTERPRISE_SQUARE(n)=n*n`

`ENTERPRISE_ROOT(n^2)=n`。

用户于 `2026-08-17` 明确冻结新的基础坐标语义：

`ENTERPRISE_COORDINATE_ORIGIN = 1`

`ENTERPRISE_ZERO_COORDINATE_EXISTS = false`。

因此本文件中把原生坐标标签 `n` 与从原点出发的 primitive interval 数直接等同的零原点推导失效。

当前 canonical square/root definition：

`definitions/ENTERPRISE_SQUARE_AND_ROOT_ORIGIN_ONE_20260817.md`

最新冻结：

`ENTERPRISE_SQUARE_RAW_AREA(n)=(n-1)^2`

`ENTERPRISE_SQUARE(n)=1+(n-1)^2`

`ENTERPRISE_ROOT(1+(n-1)^2)=n`。

仍保留为历史几何事实的是：若外部 primitive interval 边长 magnitude 为 `m`，则半平方 elementary triangle 总数为 `m^2`，完整镜像平方含 `2m^2` elementary triangular cells，普通 magnitude area 为 `m^2`。

被 supersede 的是把原生坐标标签本身直接当成该 magnitude 的解释。

本文件只保留作历史记录，不得继续作为 canonical frozen input。
