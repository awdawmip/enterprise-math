# 晶包非负地址约束统一部署记录

日期：2026-09-13。授权：当前用户要求更新项目全部坐标约束及机器语言。
范围：当前晶包最终地址接口、规范入口和机器约束；不是物理前提重建。
基准主干：`366a7517c3baf91ade267c972833fe722902519c`。

## 生效要求

最终地址六字段均为非负整数；未启用字段只有在身份无损时才可置0。
显示原点与显示轴线不参与运算，不增加原点节点或通道。跨区不强制加1，
等值换栏和调整字段按已验证的边界表执行。内部原始坐标、位移、反向操作及
零位移单独保留；六条原生轴不默认拆成十二个地址字段。

统一权威是 `coordinate_address_contract.json`。本轮为26个现有入口／机器／
库导入文件建立一致引用，修正项目定义中旧的三轴原点与有向距离摘要，具体
修改前后散列列于 `coordinate_contract_migration_manifest.json`。
历史定理、研究结果、归档和受保护的账户世界观未改写。

## 机器实现

- `schemas/cell_address.schema.json`：版本、编码、参照系、六字段及合法零位模式。
- `src/enterprise_math/cell_address.py`：公开强类型、严格JSON、切片编码与解码、
  边界更新及解码后的距离；`FinalCellAddress` 不作为整数序列被旧距离API误用。
- `tools/validate_cell_address.py`：标准输入JSON的可执行校验器。
- `EnterpriseMath/CellAddress/ThreeRegionSlice.lean`：前次成功证明逐字节迁入。
- `EnterpriseMath/CellAddress/Contract.lean`：六字段公开类型与4条桥接定理。
- 公开Python包和Lean库入口已加入新接口导入，原接口保留。

只登记 `three_region_slice_v1`，其范围为固定两原生方向切片。完整六轴通用编码
尚未登记；输入不支持就拒绝，不允许清零隐藏分量后伪装为切片。

## 实际验证

已观察 GitHub Actions `34759025088` / job `103728388285` 成功：
26处一致性检查和重复执行无变化；P000的完整 `axioms` 对象与修改前相同；
16项新运行时／JSON规范测试通过；真实包入口与整数根／塌缩冒烟检查通过。

既有7个测试文件的66项测试在原始主干及更新后各运行一次，均为65通过、1失败。
同一失败是 `test_x6_current_publication_integrity_isolation` 中另一个研究任务
`RS-RB-CM24-COMMON-DIFFERENTIAL-RIGIDITY` 的任务封装格式问题。
没有删除或豁免该测试；验证结论明确为无新增回归，而不是旧测试全部通过。

Lean 4.33.0-rc2实际编译迁入的40条原定理及4条公开接口桥接定理，输出
`COORDINATE_PUBLIC_INTERFACE_LEAN_PASSED`。没有占位证明、自定义公理或
编译器信任式证明依赖；允许的标准依赖仍为propext、Classical.choice、Quot.sound。
这不是全仓库Lake构建，也不是Python解释器全输入精化证明。

经验证的生成改动保存在提交 `34f1b7d2e9d72346b6bae6aa45cae2cb6ad3625e`。
后续只读持续检查覆盖约束相关main推送及拉取请求，不再自动修改或推送文件。
规则是否属于当前主干，以实际main包含该提交及后续发布提交为准，不以本记录文字代替。

## 仍须分开处理

全六轴几何编码与跨切片拼接、所有应用调用点及存量地址数据迁移、全仓库完整构建，
以及上述原有任务封装问题，未在本轮冒充已经完成。地址要求已统一，未验证实现不能
因此获得登记或基础定理地位。已有原始空间／路径／BRC数学不因改地址重新作废。
