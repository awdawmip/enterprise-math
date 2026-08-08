# 前人工作附录 —— P012 几何与 P016 物理反证

状态：`CANONICAL PRIOR-ART APPENDIX`  
范围：P012 内生离散几何与 P016 量化反证协议

本附录扩展主前人工作映射，而不是替代它。下列来源均属于成熟前人工作或实验基准，进取数论不把其中任何一项宣称为自己的发明。

## 1. P012 —— 内生离散几何

Mathlib 的图度量模块以最短 walk 长度定义 `SimpleGraph.edist`，对不连通顶点使用扩展值，并提供自然数值 graph distance 及核心度量规律。 [SRC-MATHLIB-SIMPLEGRAPH-METRIC]

进取数论**采用**这一成熟 graph-distance 结构。P012 的项目特有选择是基础解释，而不是历史优先权：允许把 primitive adjacency / one-step reachability 直接作为显式几何数据，再从中推出整数最短步距离，而不是先假定一个隐藏欧氏长度再做取整。

因此，P012 不对 shortest-path metric、graph automorphism、格点 `L1` 距离、加权图度量或 graph ball 主张创新。该项目级组合记录为 `EM-COMP-012`。

## 2. P016 —— 物理反证协议

P016 不把“有限分辨率可能是基本的”这一宽泛命题写成已经被实验确认或否定。任何具体实现都必须先把自己的参数映射成一个不可回避的可观测后果；已有实验只能约束确实预测对应观测量的具体实现。

### 2.1 优选方向 / Lorentz 各向异性

光学钟比较为那些必然产生方向依赖或 Lorentz 相关频移的模型提供高精度基准。 [SRC-SANNER-2019-LORENTZ-CLOCK]

这是**对比/约束基准**，并不意味着所有离散模型都会违反 Lorentz 对称性。既有离散时空路线本身已经说明，“离散”与“是否保持 Lorentz 对称”是两个逻辑上不同的设计问题。 [SRC-SNYDER-1947] [SRC-CAUSALSET-1987]

### 2.2 修改后的传播规律

GRB 090510 的观测为那些必然预测光子速度随能量变化或修改色散关系的具体实现提供基准。 [SRC-FERMI-2009-GRB090510]

该结果约束的是被测试的传播规律；如果某个有限分辨率实现精确保留相应传播对称性，它并不因此受到同一形式的约束。

### 2.3 相干性损失

大质量分子的 matter-wave interference 展示了在较高分子质量下可实验观测的量子叠加。 [SRC-FEIN-2019-25KDA] 成熟的 collapse-model 分析还说明了如何把 matter-wave 数据转化为特定客观坍缩动力学的参数排除区。 [SRC-TOROS-BASSI-2018-INTERFEROMETRY]

进取数论不能直接继承这些排除结果。未来任何物理实现都必须先推导自己的定量 coherence factor 或 fringe-visibility 损失。

### 2.4 自发辐射与加热

CSL 自发辐射分析为那些必然产生额外 photon-emission channel 的坍缩模型提供了成熟排除方法。 [SRC-PISCICCHIA-2017-CSL-RADIATION]

bulk-heating 计算同样约束那些必然注入能量的坍缩模型。 [SRC-ADLER-VINANTE-2018-HEATING] Diósi–Penrose 的 heating bounds 则为引力相关坍缩模型与超低温 heat-leak 测量提供了相邻基准。 [SRC-VINANTE-ULBRICHT-2021-DP-HEATING]

因此，P016 要求具体 Enterprise Math 物理模型先推出自己的辐射/加热规律，之后才能与这些实验比较。

### 2.5 精确守恒荷

Borexino 的电荷守恒搜索为那些必然允许被测试的电荷不守恒电子衰变通道的模型提供基准。 [SRC-BOREXINO-2015-CHARGE]

“基本多对一演化”本身并不逻辑推出电荷不守恒。具体实现可以把守恒作为精确约束，也可以预测守恒缺陷并接受相应实验检验。

## 3. 项目级组合

`EM-COMP-013` 所记录的是协议层面的组合：

1. 明确物理状态与前向转移律；
2. 明确 observation map；
3. 明确精确/涌现的对称性和守恒主张；
4. 预先声明参数允许区；
5. 推导至少一个不可回避的定量观测后果；
6. 在解释实验之前明确写出 `falsified_if` 条件。

若一个 null result 只排除了部分参数空间，正确结论是参数排除，而不是否定整个进取数论框架。反过来，如果一个模型总能在看到数据后把所有观测后果调走，它还没有成为真正可证伪的物理理论。

## 4. 创新边界

graph metric、Lorentz tests、gamma-ray propagation tests、matter-wave interferometry、客观坍缩模型的排除方法、自发辐射/加热测试以及电荷守恒搜索，均属于成熟前人工作。

进取数论的历史创新性继续标记为 `NOVELTY_UNVERIFIED`。P012/P016 在这里主张的只是项目级综合：一侧是内生有限状态几何，另一侧是未来具体物理实现必须遵守的定量 kill-test contract。
