# 研究成果、公式、定理与工具库

整理范围：**2026 年 10 月 1 日至本次冻结快照**（Asia/Shanghai）；研究来源冻结于 [`56f5938`](https://github.com/awdawmip/enterprise-math/tree/56f5938da3f707c1d9db1b39afde124eac4634e3)。必要的较早论文、已离开当前主树的历史报告及未合并研究分支，按各自固定提交追溯。

本目录按对象和适用条件整理已有研究，提供结论、公式、证明位置、作者、原审核、复用关系与未支付缺口。原有探索保持暂停。本次整理不新增证明、数学审核、工具接受、Lean 证明或 Foundation 晋升，也未执行科学计算。

## 本月总目录

以下 **435 个文献整理单元**可合并多个同对象结果；其中也包含条件接口、旧结论复用、未审稿与负面边界，不能作为新定理数量或已接受结果数量。不同分卷的交叉引用按原始来源去重，首批 23 条目保留在下表后的旧入口。

| 分卷 | 整理单元 | 适用内容与边界 | 结构化来源 |
| --- | ---: | --- | --- |
| [P11、Selmer 与完全数方法边界](research_library/202610_month/p11.md) | 40 | 固定局部像、Cassels 配对、二进与四下降；保留 NO_INVOKE 和未支付的算术执行 | [JSON](research_library/202610_month/p11.json) · [覆盖清单](research_library/202610_month/p11_coverage.json) |
| [Student、Parity 与局部解析接口](research_library/202610_month/student_parity.md) | 46 | 惯性、极点、局部 Ψ、first variation；保留母系数调用器来源缺口 | [JSON](research_library/202610_month/student_parity.json) · [覆盖清单](research_library/202610_month/student_parity_coverage.json) |
| [原生 X6 观察者、纤维与读出](research_library/202610_month/native_brc.md) | 14 | 整数占据、质量阈值、未来语言、有限字母与距离；保留未审稿和附件缺口 | [JSON](research_library/202610_month/native_brc.json) · [覆盖清单](research_library/202610_month/native_brc_coverage.json) |
| [CM 代数、特征 p 与 Hodge 有限支撑](research_library/202610_month/cm_algebra.md) | 48 | weak/rational/integral carrier、正规形、PD 与 Frobenius；Hodge 仅限实际任务范围 | [JSON](research_library/202610_month/cm_algebra.json) · [覆盖清单](research_library/202610_month/cm_algebra_coverage.json) |
| [CM 解析、源像与有限归一化](research_library/202610_month/cm_analytic.md) | 61 | Green、Heun、h_div、canonical delta 与有限正规化；κ 和目标 join 的债分别保留 | [JSON](research_library/202610_month/cm_analytic.json) · [覆盖清单](research_library/202610_month/cm_analytic_coverage.json) |
| [数论、有限控制、CRT 与 Hart](research_library/202610_month/number_theory.md) | 57 | 约数、辨识、QR/素数幂表、批处理成本与删失时间；明确纸面结果和旧计算等级 | [JSON](research_library/202610_month/number_theory.json) · [覆盖清单](research_library/202610_month/number_theory_coverage.json) |
| [T6 有限分支与有条件电路接口](research_library/202610_month/t6_formal.md) | 8 | 各 q 层的精确有限输入及已有 Task 审核；不外推全局闭合 | [JSON](research_library/202610_month/t6_formal.json) · [覆盖清单](research_library/202610_month/t6_formal_coverage.json) |
| [形式结果、公共接口与 J1](research_library/202610_month/misc_formal.md) | 23 | 实际 RR/DR/HIRR 绑定、标记编译器与有限接口；保留仅到任务的验收范围 | [JSON](research_library/202610_month/misc_formal.json) · [覆盖清单](research_library/202610_month/misc_formal_coverage.json) |
| [BRC、残余反馈与历史实验文献](research_library/202610_month/brc_residual.md) | 69 | 被动时钟、U21、GBRC/CBRC 与历史模型报告；未合并 PR 和历史计算单列 | [JSON](research_library/202610_month/brc_residual.json) · [覆盖清单](research_library/202610_month/brc_residual_coverage.json) |
| [CELL 闭包与路径证书](research_library/202610_month/cell_euler.md) | 30 | U1–U25 的精确预算、恢复与修复；原生实验文献及路径反例按来源定型 | [JSON](research_library/202610_month/cell_euler.json) · [覆盖清单](research_library/202610_month/cell_euler_coverage.json) |
| [Euler 记录、测量与反馈](research_library/202610_month/euler_measurement.md) | 25 | 不扰动、可逆性、选择性、自治反馈与门切换；区分外部模型和原生读出 | [JSON](research_library/202610_month/euler_measurement.json) · [覆盖清单](research_library/202610_month/euler_measurement_coverage.json) |
| [数论来源追溯补卷](research_library/202610_month/supplement_number_theory.md) | 14 | CRT 修正条件、移位二次式、格与有限模数分支；同旧结论时仅作复用 | [JSON](research_library/202610_month/supplement_number_theory.json) · [覆盖清单](research_library/202610_month/supplement_number_theory_coverage.json) |

覆盖基准是月初前最后提交与冻结树之间的逐子树清单，研究笔记、结果／审核、研究附件、任务和基础定义等共有 **2,474 个当前新增或修改文件**。该数是文件数，不是研究数量；治理记录、附件清单和重复文稿分别归账。历史及分支来源另列，不加入这个分母。逐文件去向及历史补查见[本月覆盖说明](research_library/202610_month/COVERAGE.md)。

## 原有库与首批摘录

| 用途 | 入口 |
| --- | --- |
| 已证明命题与逐项 Lean 状态 | [中文定理目录](THEOREMS.zh-CN.md) · [English](THEOREMS.en.md) |
| T0–T12 工具及接口 | [工具库说明](ENTERPRISE_TOOLBOX_REGISTRY.md) · [机器注册表](../enterprise_toolbox_registry.json) |
| 方法检索 | [基础清单](../research_method_inventory.json) · [本月索引增补](../research_method_inventory_addenda/202610_month_research_library.json) |
| 权威路由与问题状态 | [Common Surface](../research_common_surface.json) · [问题状态](PROBLEM_STATUS.zh-CN.md) |
| 当前原生基础与原有 ledger | [Current Native Foundation](../definitions/00_CURRENT_NATIVE_FOUNDATION.md) · [Heartbeat 工具包](../research_toolkits/heartbeat_world.json) |
| 首批有限控制 10 条 | [C22–C26](research_library/20261022/finite_controls.md) |
| 首批 CM／特征 p 6 条 | [CM／char-p](research_library/20261022/cm_charp.md) |
| 首批原生 X6 5 条 | [X6](research_library/20261022/native.md) |
| 首批 Student 2 条 | [Student](research_library/20261022/student.md) |

已有定理编号、证明正文、审核和执行工具继续由原文件管理。本月分卷链接到旧结果，不重新把首批 23 条计为新增研究。

## 状态如何使用

`EXTRACTED` 仅表示已有正文被摘录；`REUSE` 表示已有结论的复用；`DUPLICATE` 表示重复副本；`CONTROL_ONLY` 是治理或来源路由；`SOURCE_GAP` 须结合具体原因阅读，可能是原稿、附件、独立审核或数学接口的缺口。各卷保留自己的精确状态字段。

原非作者论文审核、正式 Task／Result 验收及 Foundation 状态分别记录。创建时的 `UNREVIEWED` 与后续审核按时间分开；一个有限任务的 `ACCEPTED` 不代表母问题闭合。静态 `NO_INVOKE` 报告不是算术计算完成；历史计算和未合并 PR 也不能冒充当前主树的结论。[文献交叉核对](research_library/202610_month/QA.md)只检查整理是否忠于来源。

## 工具与方法复用

| 需求 | 复用入口 | 必须保留的条件 |
| --- | --- | --- |
| 有限读出纤维、碰撞和容量 | `T4_FINITE_FIBER_CAPACITY_COLLISION_MINIMA` | 指定对象总体与读出；占据数、权重与概率不能混用 |
| 后续操作下的安全商 | `T6_OPERATION_SAFE_QUOTIENT` | 明示未来语言与全部所需观察；当前读出相同不足以删信息 |
| 有限群作用、轨道和等变性 | `T7_FINITE_SYMMETRY_EQUIVARIANCE` | 非空性与完整有限 carrier 条件；不能充当无限 carrier 的自动约化 |
| CM 连接／余核、Selmer／配对、CRT／秩与成本、局部解析接口 | 各分卷的假设、公式、证明和 method-harvest 段落 | 论文中的可复用接口保留 `RESULT_ONLY` 或原状态，不自动成为新工具族或可执行算法 |
| 旧闭迹、filament、PCF 与首批已摘结果 | 各卷明确的 `REUSE` 和来源链接 | 不重复计数、不重新审核、不重跑旧计算 |

本月增补沿用现有方法检索器，API 为空，只返回来源与使用边界。例如：

```sh
python tools/enterprise_toolbox.py methods P11 Selmer dyadic
python tools/enterprise_toolbox.py methods CRT Hart primepower
python tools/enterprise_toolbox.py methods CM canonical delta hdiv
python tools/enterprise_toolbox.py methods CELL closure port budget
```

## 需要保留的缺口

- CM 的 canonical δ 构造、任意平移 δ 与 Eq16 的 κ 是不同接口；已有有限归一化审核不支付目标 join、h_div 数值或独立 κ 构造。特征 p 有理正规形的独立审核归档仍按实际来源状态保留。
- Student 局部 Ψ 和 first-variation 不补齐母系数调用器的精确原式、变量和轮廓。
- P11 的算术执行债与纸面 Selmer／配对结果分开；m7 对某个正性方法的阻碍不构成 HCM0 反例。
- X6 的部分附件、局部分离器审核、较早公式定位及未审核推广仍保留缺口；BRC 中撤回引理、未闭父问题和未执行桥接不因整理而升级。

原生条目采用固定六维离散 Cell 空间的签名坐标图，时间在需要时另行定型。外部经典分析／代数模型保持其声明类型；本目录不据此生成全 X6 传播结论或物理定律。
