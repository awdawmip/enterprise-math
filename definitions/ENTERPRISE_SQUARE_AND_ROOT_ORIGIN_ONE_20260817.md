# 进取平方与平方根：原点一 / 零不存在重推

Status: `SUPERSEDED_BY_SIGNED_ORIGIN_ONE_CORRECTION`
Date: `2026-08-17`
Driver: `EM-DVR-9GP3M7 / CONTROL_PLANE`

本文件的核心公式

`ENTERPRISE_SQUARE(n)=1+(n-1)^2`

已被用户给出的原生单位四边形 exact counterexample 推倒。

反例四边形：

`Q=((±1,±1,±1),(2,1,1),(1,-2,1),(1,1,2))`

其原生周长和面积均为 `4`，所以必须满足

`ENTERPRISE_SQUARE(2)=4`，

而不是本文件给出的 `2`。

错误根源：把“从原点到 `±n` 的 primitive adjacency step 数 `n-1`”误当成“原生坐标幅值应为 `n-1`”。

当前 canonical signed-origin 定义：

`definitions/ENTERPRISE_SIGNED_ORIGIN_ONE_COORDINATE_20260817.md`

当前 canonical square/root 定义：

`definitions/ENTERPRISE_SQUARE_AND_ROOT_SIGNED_ORIGIN_ONE_20260817.md`

正式恢复：

`ENTERPRISE_SQUARE(n)=n^2`, `n>=1`

`ENTERPRISE_ROOT(n^2)=n`, `n>=1`。
