# 研究成果、公式与定理库

整理日期：2026-10-22（Asia/Shanghai）。本批来源冻结在 Enterprise Math 主分支提交 [`63f8704`](https://github.com/awdawmip/enterprise-math/tree/63f87045b456cf573a9eaa7bbc8d4a4673a3e6ea)。

这里汇集近期研究的结论、精确公式、适用条件和证明／审核出处，供检索与复用。各条目保留来源的实际状态；本目录是文献整理，不产生新的数学审核、工具接受、Lean 证明或 Foundation 晋升。固定来源之后的进展须另行核对。

## 原有库入口

| 用途 | 入口 |
| --- | --- |
| v0.1 已证明命题及逐项 Lean 状态 | [中文定理目录](THEOREMS.zh-CN.md) · [English](THEOREMS.en.md) |
| T0–T12 工具、接口与适用边界 | [工具库说明](ENTERPRISE_TOOLBOX_REGISTRY.md) · [机器注册表](../enterprise_toolbox_registry.json) |
| 方法检索与增补 | [基础方法清单](../research_method_inventory.json) · [本批增补](../research_method_inventory_addenda/20261022_research_results_curation.json) |
| 跨研究线的权威路由 | [Common Surface](../research_common_surface.json) |
| 编号问题与现代定理状态 | [中文状态总线](PROBLEM_STATUS.zh-CN.md) · [English](PROBLEM_STATUS.en.md) |
| 当前原生基础与既有定理 ledger 路由 | [Current Native Foundation](../definitions/00_CURRENT_NATIVE_FOUNDATION.md) |
| 既有 Heartbeat 专门研究库 | [研究库目录](../research_toolkits/heartbeat_world.json) |
| 既有方法采收 | [2026-08-20—22 采收记录](RESEARCH_METHOD_HARVEST_20260820_20260822.md) |

已有定理编号、证明正文和执行工具继续由各自原始文件管理。本批不重新编号或复制旧证明。

## 本批成果

| 分支 | 成果、公式与条件 | 结构化摘录 |
| --- | --- | --- |
| C22–C26 有限控制与辨识 | [实际参数族、闭包与拟合；双档盲参照；有界／结构漂移；共同速率与秩亏控制](research_library/20261022/finite_controls.md) | [JSON](research_library/20261022/finite_controls.json) |
| CM 与特征 p | [CM0、简单零、实际奇矩生产者、Eq16 接口、p 曲率与有理正规形](research_library/20261022/cm_charp.md) | [JSON](research_library/20261022/cm_charp.json) |
| 原生 X6 | [传感器纤维、64 状态平移相位、全 Cell 邻接刚性、闭迹复用及分离器待审稿](research_library/20261022/native.md) | [JSON](research_library/20261022/native.json) |
| Student | [实际列的半圆阻碍与联合 Ψ 局部接口](research_library/20261022/student.md) | [JSON](research_library/20261022/student.json) |

每个分支分别列明对象／假设、公式、结论、限制、来源与去重关系。来源中的“独立 whole-review 通过”只在其精确对象和条件内使用；原稿的历史自检或待审文字与后来的审核记录分别保留。正文中的符号和局部编号以链接的原文定义为准。

## 工具复用与去重

| 需求 | 已有入口或处理方式 | 边界 |
| --- | --- | --- |
| 有限读出纤维、碰撞与容量 | `T4_FINITE_FIBER_CAPACITY_COLLISION_MINIMA` | 指定对象总体与读出；不自行选择观察者 |
| 允许后续操作下的安全商与修复 | `T6_OPERATION_SAFE_QUOTIENT` | 必须保留明示未来语言下的观察；当前读出相同不足以全局删信息 |
| 有限群作用、轨道与等变性 | `T7_FINITE_SYMMETRY_EQUIVARIANCE` | 不据此宣称覆盖无限图刚性的完整证明 |
| 有限控制、CM／特征 p、Student 的论文结论 | 本批 `RESULT_ONLY` 方法索引 | 标准方法组合与具体定理不自动成为新工具族或可执行算法 |
| 24 步有符号邻居闭迹 | 原有 V10 的精确复用，见 X6 分支 | 不重复计为新定理、新方法或新审核 |

本批方法增补提供四个分支的检索入口，沿用现有 `tools/enterprise_toolbox.py methods`。例如：

```sh
python tools/enterprise_toolbox.py methods C25 unknown common rate
python tools/enterprise_toolbox.py methods CM BCM rational normal form
python tools/enterprise_toolbox.py methods X6 sensor min64
python tools/enterprise_toolbox.py methods Student joint Psi
```

这些命令搜索已保存的方法描述，不执行数学实验。精确工具 ID、API、状态与实现以工具注册表为准。

## 仍需保留的缺口

- Eq16 的独立、无索引标量 κ 构造尚未由本批材料支付；不能把已有接口等价式称为完整 Eq16 证明。
- 特征 p 有理正规形的作者稿已在来源中；对应独立审核文件在冻结主快照的精确路径未找到。库中保留待归档审核状态。
- 有限 Cell 分离器是本地作者待审稿，冻结主快照未找到其精确路径；不纳入已审核层。
- Student 的母系数调用器仍有来源定位缺口；局部结果不替代完整系数目标。

原生条目采用固定六维离散 Cell 空间的签名坐标图；时间在需要时另行定型。外部经典分析／代数模型保留其声明类型，不能由本次整理自动转成全 X6 传播或物理定律。
