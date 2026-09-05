# 六轴派生基础闭合状态 V2

状态：`DERIVED_LAYER_CLOSED / NOT_NATIVE_X6_PROMOTION`

已闭合：K4/S4 六轴图册、12 incidence flags 的 proper FCC 旋转读出、120° 局部朝向 gauge 类、三/四切片循环粘合与公共深度、带 S4 frame 的六计数合成及 depth 2-cocycle、端点/重数/正权保真的 BRC 摘要、形式长度 Schur 端口合同、S4 不变二次型 metric fork、native lift 的 action/category/quotient 检查合同。

已闭合成 no-go：不能由 12/2 推出 native 六维；不能把 opposite carrier ray 当 native negative axis；不能把六计数自动当 native Cell address；不能把 S4 atlas automorphism 自动升级成完整 native rotation group；不能由局部勾股律唯一选全局二次度量；不能把负三角 sign product 自动解释成物理 holonomy；不能以无端点/无重数摘要替代 provenance-sensitive path。

二次型类的最小剩余数据：`Q_c=<n,(I+cJ)n>`，J 交换三组 K4 对边；谱 `1+c`×3、`1-c`×3，正定 iff `-1<c<1`。现有局部三轴定律不含任何对边同现信息，因此还差且仅差一个跨切片标量 `c`。`c=0` 是新增正交性公理，不是当前结论。

剩余原生输入只有：`X6_native` 状态/地址合法性、native adjacency/path category、native-to-atlas 等变 readout、native rotation action（及是否存在超出 S4 skeleton 的内部自由度）、以及若需要唯一 global metric 时的真实跨切片 datum。

运行：先执行 V1 `check_six_axis.py`, `check_ports.py`, `check_mutations.py`，再执行 `check_closure_addenda.py` 与 `check_independent_reference.py`。后者故意不 import 主实现或 vendor，用于降低相关实现错误。
