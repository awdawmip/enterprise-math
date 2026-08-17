# 历史定义：进取点态原点与位移零元

Status: `SUPERSEDED / DO_NOT_USE_AS_CANONICAL`
Date: `2026-08-17`
Driver: `EM-DVR-9GP3M7 / CONTROL_PLANE`

本文件曾冻结：

`ENTERPRISE_POINT_STATE_ORIGIN = 1`

`ENTERPRISE_DISPLACEMENT_ZERO = 0`

以及 point-space / zero-centered displacement-space 双层语义。

该定义已被用户明确 supersede。

当前 canonical foundational definition：

`definitions/ENTERPRISE_COORDINATE_ORIGIN_ONE_NO_ZERO_20260817.md`

最新冻结：

`ENTERPRISE_COORDINATE_ORIGIN = 1`

`ENTERPRISE_ZERO_COORDINATE_EXISTS = false`

即：`0` 不属于进取坐标系，也不再存在“原生位移空间中的零坐标”。

所有旧 `(r,0)`、`(0,r)`、`(0,0,0)`、有符号零中心格等表述，从当前定义起只能作为 `LEGACY_SIGNED_AUXILIARY_CHART / EXTERNAL_COMPUTATION_CHART` 使用，不能继续称为进取原生坐标。

本文件仅保留作为历史 superseded 记录；不得继续作为后续任务的 frozen input。
