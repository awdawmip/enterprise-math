# 心跳世界 BRC 余数端口工具包

状态：`EXECUTABLE_RESEARCH_CANDIDATE / NOT_FOUNDATION`  
世界：`HEARTBEAT_WORLD = ENTERPRISE_NATIVE_X6 + TIME`

本工具包把近期“心跳世界”研究中可复用的三类能力提取到 T0 BRC 家族，而不新建顶层工具族：

1. `brc_residue_port.py`：在有限余数纤维上保留正权重、仿射作用、重数和时间端口；验证周期子格与源/目标余数纤维。
2. `brc_residue_quotient.py`：对指定未来算子族，比较精确作用/二阶矩算子，证明哪些余数通道可安全合并；宏观边界证书不能自动用于轮内观察。
3. `brc_contact_horizon.py`：两个带标签 X6 位置的有限时限接触观察。剩余时限 h 内只需精确保留 L1 距离不超过 h 的相对位移，其余合为 FAR；增加时限时必须从更完整状态重新编码。

## 核心原则

`CURRENTLY_SIMILAR != FUTURE_EQUIVALENT`

只有在声明的观察量、未来操作族和时间范围内证明下降/纤维常值，才允许合并。余数、相位、资源、接触关系都是附加有类型状态，不增加空间维数。

`FAR != ZERO`；`MACRO_QUOTIENT != MICRO_QUOTIENT`；`MOMENT_EQUIVALENCE != EFFECT_EQUIVALENCE`。

机器定理台账：`research_notes/heartbeat_brc_library_20260920_AD0416/THEOREM_LEDGER.json`。  
方法索引：`research_method_inventory_addenda/20260920_brc_*.json`。  
最小验收：`tests/test_brc_heartbeat_toolkit.py`。

这些工具没有获得独立数学审稿、Foundation 录入或 Nollm 生产语义收益验证。
