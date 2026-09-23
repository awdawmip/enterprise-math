# 进取数论项目定义

<!-- EM_FINAL_CELL_ADDRESS_CONTRACT_V1 -->
## 晶包坐标接口约束（2026-09-13）

所有最终晶包地址遵循 [`coordinate_address_contract.json`](coordinate_address_contract.json)：六字段非负；未启用字段只在可恢复完整身份时置0；显示原点与轴线不参与晶包运算；跨区不强制加1。内部原始坐标、位移、反向操作与零位移分别保留，不能直接当作最终地址输出。已验证三分区实现仅覆盖固定两原生方向切片，不适用于任意完整六轴状态。旧文中的坐标零点为内部锚点，不是显示原点放置要求。
<!-- END_EM_FINAL_CELL_ADDRESS_CONTRACT_V1 -->

Status: `ACTIVE / PROJECT-LEVEL DEFINITION / V4`
Date: `2026-09-23`
Position update authority: `DIRECT_CURRENT_USER_INSTRUCTION`

## 一句话定义

> **进取数论以有限分辨率、整数优先和残差保真的离散关系为基础，保留对声明的后续操作与观察仍有效的区别，重新奠基有用的数学工具，并区分精确、有限精度、渐近、限域恢复或系统修正。**

项目原则：`REFOUND, NOT REJECT`。

## 残差保真的研究定位

主定位是**以有限分辨率为基础、保留结构残差的离散关系体系**；动力学研究简称**残差保真的离散关系动力学**。当前坐标或读数不默认等于完整状态。对声明的未来仍有影响的支路、路径、联合关系、内部场、回路、来源或记忆，应以相应类型保留；这些是可能的载体，不是必须齐备的万能状态元组，也不增加空间维数。

无损压缩须保持声明的观察及所有允许的后续组合；近似压缩须在相关时说明分辨率、时间窗口、资源范围及误差传播界。允许真实多对一演化，也允许经证明的零残差。当前不可见不足以授权删除；同时，不要求永久保留全部历史。目标是最小充分状态，不预设所有模型都有有限、局部的最小闭合表示。

结构或关系残差、表示或近似误差、实现或推导错误、未分类差异应分别处理；未知不等于零或物理规律。相消须核对适当代数中的完整联合状态，不能只看标量系数异号；正质量不是有符号幅值。残差不必小、不必是实数、不必非零，也不自动等于能量、温度或力。

离散基底标签本身不保证所有幅值参数离散。连续数学仍可作为具类型的有效描述或形式工具，不能以任意实数“余量”自动充当原生结构。研究残差的生成、传播、复合、修复、保持及资源代价，不以残差普遍清零为成功标准。

机器契约：[`definitions/RESIDUAL_FAITHFUL_DISCRETE_RELATIONAL_SYSTEM.json`](definitions/RESIDUAL_FAITHFUL_DISCRETE_RELATIONAL_SYSTEM.json)。本定位不改变 P000、最终地址接口、既有 BRC 代数类型、任务归属、定理或审查状态及运行时行为，也不将某个具体场模型升格为世界公理。

## 0. 当前权威

本文件定义项目使命、层次和当前路由。

当前原生数学的稳定入口：

`definitions/00_CURRENT_NATIVE_FOUNDATION.md`。

当前 FREE 公理发现的原始基础入口：

`definitions/00_FREE_AXIOM_DISCOVERY_SUBSTRATE.md`。

精确数学声明以任务实际使用的 exact canonical definition 为准。

## 1. 当前空间与显示参照

原生六轴晶包结构以 `p000_reality_foundation.json` 和
`definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md` 为准。
六条原生轴及既有正向、反向操作保持不变。
P000 继续规定进取原生直角关系为 120°；该关系与最终地址是否使用负数无关。
原始有符号坐标属于内部数学表示；
其零坐标标记一个选定晶包锚点，不规定物理全局中心或显示原点。
显示原点可以位于空隙，显示轴线不必经过晶包中心；二者不是晶包、路径节点或运算起点。

## 2. 当前坐标与长度

所有最终晶包地址统一遵循 `coordinate_address_contract.json`：六个非负整数字段，
明确编码版本及固定参照系。不参与表达的字段只有在完整身份不丢失时才可置0；
未知、隐藏或省略的信息不等于0。地址数字不能未经解码直接当作位移或距离。

已登记实现 `three_region_slice_v1` 仅覆盖固定两原生方向切片，形式为
`(0,b,c,0,0,0)`、`(a,0,c,0,0,0)`、`(a,b,0,0,0,0)`，启用字段为正整数。
这不是完整六轴通用编码。其他输入必须使用另行验证登记的编码；不支持时明确拒绝，
不得偷偷清零其他分量后套用切片。

## 3. 当前线与点到点结构

原生有符号位移、距离、邻接规则保留。距离基于解码后的晶包，不基于地址数字的差。
跨显示分界不增加节点，也不强制加1；当前已证明的边界表同时包含等值换栏和调整字段。
实际边身份、路径先后、BRC 重复度、端口、权重、边界及初态均需保留。
步数与原生分量长度仍须区别。当前原生有符号距离具有反向对称性；历史有向 min-zero
数值仅是信息较少的观察读数，不再作为当前原生点到点距离。

## 4. BRC

`BRC=Branch-Recoalescence Collapse`。

当前 BRC 基层：

`CANONICAL_BRC_BASE_LAYER=BOOLEAN_RESULT_SUPPORT_SEMANTICS`。

当前 enrichment：

`PATH_FORMAL_BRC -> N_BRC -> BOOLEAN_BRC`。

经典/工程 readout 可以作为 typed compatibility layer，但不得把目标侧定义反向写成 native premise。存在布尔投影不等于它对所有未来问题都足够；信息缩减投影还须遵守上述残差保真契约。

## 5. 定义不继承

`Definition is not inherited.`

成熟概念可以保留；禁止的是因为某个经典定义有效，就未经证明把它直接当成 native premise，再把其恢复当成新推导。

经典/工程成功是强证据与 calibration target，不是自动 ontology。

## 6. 项目层次

- `P0`：数、精度、整数、离散状态、关系、残差、collapse/quotient；
- `P1`：packet/cell、adjacency、transition、path、branch/recoalescence、进取坐标/代数；
- `P2`：重建 length、distance、angle、norm、pairing、projection、area/volume、curve；
- `P3`：重建 trig、pi 语义、坐标变换、分析工具；
- `P4`：经典/连续/工程 recovery/deviation 分类；
- `P5`：数学语义冻结后的物理与工程校准。

必须区分：

`PACKET_COUNT != TRANSITION_COUNT != GEOMETRIC_LENGTH`。

## 7. 恢复分类

- `EXACT_RECOVERY`
- `FINITE_PRECISION_RECOVERY`
- `ASYMPTOTIC_RECOVERY`
- `DOMAIN_RESTRICTED_RECOVERY`
- `SYSTEMATIC_DEVIATION`
- `NONRECOVERY`

偏差必须可推导、可复现、可检验。

## 8. 当前项目栈

`NUMBER -> PRECISION -> DISCRETE STATE -> RELATION/PATH/BRC -> RESIDUAL-FAITHFUL STATE AND SCOPED COMPRESSION -> NONNEGATIVE CELL ADDRESSES OVER TYPED NATIVE RELATIONS -> REBUILT GEOMETRY -> TRIG/ANALYSIS -> CLASSICAL COMPATIBILITY/CORRECTION -> PHYSICS -> ENGINEERING`。

> **不是把旧数学推倒，而是让它拥有一个更好的地基。**

## 9. 当前世界观

账户级受保护 `我眼中的世界.md` 及其 JSON 对应提供当前有限分辨率、后分配与残差保真研究定位；空间基础继续由 P000 控制。本次更新经用户明确授权，不把候选模型、有限实验或形式推导升级为已确立的物理规律。

## 10. 历史访问

本文件不重复项目旧代际、旧路线或 supersession 叙事。需要历史/provenance 时，从 Git history、journal 或明确历史文件检索。
