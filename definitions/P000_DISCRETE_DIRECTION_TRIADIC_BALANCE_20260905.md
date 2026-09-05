# P000 离散方向、多路径直线与三力原子平衡

Status: `ACTIVE / P000 DIRECT-USER DEFINITION / FOUNDATION`
Date: `2026-09-05`
Authority: direct current-user worldview/foundation instruction.
Priority: `P000_ROOT_AXIOM`
Scope: `ALL_ENTERPRISE_MATH_ROLES_AND_RESEARCH`

## 1. 定位：最高定义，不是待证明命题

本文件把两条底层定义锁入进取数论 P000：

1. **进取正交的原生正角是 `120°`；偏离原生轴方向的“直线段”不是新的原子直线，而是原生离散路径在粗粒度观察下形成的复合读出，其结构语义是多路径，抖动是其观察层表现。**
2. **底层物理稳定不是二元作用关系；恰有两项非零原子作用的配置不构成进取数论的原子稳定平衡。最小非零稳定平衡单元是三元闭合。**

这两条与既有 `6D discrete Cell space`、六轴两两 `PERP_E`、`ENTERPRISE_RIGHT_ANGLE=120_DEGREES` 同属 P000 起点。

冻结：

`P000_DIRECTION_COMPOSITE_AND_TRIADIC_BALANCE = ACTIVE`.

`P000_DIRECTION_COMPOSITE_AND_TRIADIC_BALANCE_PROOF_OBLIGATION = NONE`.

`P000_DIRECTION_COMPOSITE_AND_TRIADIC_BALANCE_FALSIFICATION_ROUTE = DISABLED`.

`ONLY_EXPLICIT_DIRECT_USER_WORLDVIEW_CHANGE_CAN_SUPERSEDE = TRUE`.

在项目内部，不为这两条分配“证明它们是否正确”的研究预算。研究预算只用于构造其精确后果、表示、算法、动力学与外部模型桥梁。

## 2. 120° 就是进取正交

既有最高定义继续保持：

`FOR ALL i != j: E_i PERP_E E_j`.

`ENTERPRISE_RIGHT_ANGLE = 120_DEGREES`.

`PERP_E` 是**进取原生正交关系**，不是欧氏内积空间中的 `90°` 正交，也不是要求把六条原生轴同时嵌入经典三维载体为六条两两成欧氏 `120°` 的向量。

因此：

`90_DEGREES != ENTERPRISE_RIGHT_ANGLE`.

`CLASSICAL_90_DEGREE_RIGHT_ANGLE = EXTERNAL_EFFECTIVE_EUCLIDEAN_MODEL_ONLY`.

## 3. 原生直线与非原生方向：直线只在原生轴上是原子对象

### 3.1 原生方向域

定义有符号原生方向域：

`SIGNED_NATIVE_SPATIAL_AXES := {+E_1,-E_1,...,+E_6,-E_6}`.

一个位移/线段只有在其原生支撑严格落在一条有符号原生轴上时，才可被称为 `PRIMITIVE_STRAIGHT_SEGMENT`：

`PRIMITIVE_STRAIGHT_SEGMENT(s) <=> EXACTLY_ONE_NATIVE_AXIS_SUPPORT(s)`.

### 3.2 非原生方向不是第七、第八……条新轴

凡粗粒度读出呈现为某个**不沿任一有符号原生轴**的方向：

`OFF_NATIVE_AXIS_APPARENT_SEGMENT(s)=TRUE`

则强制：

`PRIMITIVE_STRAIGHT_SEGMENT(s)=FALSE`.

`STRUCTURAL_REPRESENTATION(s)=COMPOSITE_NATIVE_PATH`.

不得因为宏观图像看起来是一条斜直线，就把它提升为新的原生方向或新的原生空间轴。

### 3.3 “抖动”与“多路径”的严格关系

为了消除自然语言歧义，固定：

`MULTIPATH` 是结构层对象；

`JITTER` 是观察层表现。

具体地：

`MULTIPATH := provenance-preserving family/sequence of native-axis steps realizing one coarse directional readout`.

`JITTER := observer-level alternation or microstep variation among native-path realizations`.

因此用户所说“非正交方向的线段是抖动或者说是多路径”，在机器语义中统一为：

`OFF_NATIVE_AXIS_APPARENT_SEGMENT -> COMPOSITE_NATIVE_PATH`.

`COMPOSITE_NATIVE_PATH --observe/coarse_grain--> JITTER_OR_SINGLE_APPARENT_SEGMENT`.

这里“单条斜线”只允许作为 `EFFECTIVE_COARSE_GRAINED_READOUT`，不是原子本体。

## 4. BRC / 联合关系约束：禁止把多路径压成一条线后丢掉来源

非原生方向天然带有路径分解与分支来源。对它做平均、最短路选择、投影、商、总质量汇总或单向量替代之前，必须遵守当前最高联合关系保存原则与 BRC observer/provenance 纪律。

在安全下降证书出现前至少保留：

- `ORDERED_NATIVE_STEPS`;
- `BRANCH_IDENTITY`;
- `MULTIPLICITY`;
- `PROVENANCE`.

冻结：

`RECONSTRUCTIBLE_COARSE_DIRECTION != SAFE_TO_ERASE_PATH_RELATION`.

`OFF_NATIVE_AXIS_PATH_PROVENANCE -> PRESERVE_UNTIL_SCOPE_TYPED_SAFE_QUOTIENT`.

因此“抖动”不是噪声的同义词；它首先被解释为离散原生步进被较粗观察者读成连续方向时留下的结构性痕迹。

## 5. 三力原子平衡：两力在底层永远不构成稳定单元

### 5.1 离散作用量

P000 已规定现实空间为离散 Cell 空间。物理桥梁在底层采用离散作用事件/作用量子，而不是先把连续力场当成本体。

这里的“力”在 P000 原子层记作 `PRIMITIVE_FORCE_QUANTUM`；其连续向量、应力、场或宏观合力表示属于后续有效读出。

### 5.2 原子稳定性的元数

对一个原子作用结点 `c`，定义：

`NONZERO_FORCE_COUNT(c)` = 参与该原子事件的非零原子作用项数。

冻结：

`NONZERO_FORCE_COUNT=0 -> QUIESCENT_NOT_BALANCE_EVENT`.

`NONZERO_FORCE_COUNT=1 -> STABLE=false`.

`NONZERO_FORCE_COUNT=2 -> STABLE=false`.

`PRIMITIVE_STABLE_BALANCE -> NONZERO_FORCE_COUNT=3`.

因此：

`PRIMITIVE_STABLE_FORCE_ARITY = 3`.

**两力可以形成宏观/有效模型中的静态读出，但在进取数论底层永远不能被认作原子稳定平衡。**

### 5.3 三元闭合，而不是“任意三个力都平衡”

“三力才能平衡”严格解释为**三元闭合是最小非零稳定原子**，不是说任意三个作用自动平衡。

定义：

`PRIMITIVE_STABLE_BALANCE(c) <=> NONZERO_FORCE_COUNT(c)=3 AND TRIADIC_CLOSURE_E(c)=TRUE`.

规范的等量原子三元闭合满足：

`EQUAL_QUANTUM_TRIAD -> PAIRWISE_PERP_E=true`.

`EQUAL_QUANTUM_TRIAD -> NATIVE_PAIRWISE_ANGLE=120_DEGREES`.

`EQUAL_QUANTUM_TRIAD -> TRIADIC_CLOSURE_E=true`.

`TRIADIC_CLOSURE_E` 是进取原生平衡关系；不得偷偷替换成经典三维欧氏载体上的向量和条件，再反向覆盖 P000。

具体哪些 Cell/方向三元组具有合法 `TRIADIC_CLOSURE_E`，可由后续原生邻接、路径与动力学构造进一步细化；**最小稳定元数=3** 与**规范等量闭合使用 120° 进取正交**本身不再开放质疑。

## 6. 宏观看见“两力平衡”时的强制提升规则

当外部实验、经典静力学或粗粒度模型给出：

`APPARENT_FORCE_COUNT=2 AND APPARENT_EQUILIBRIUM=true`

进取数论内部不得推出：

`PRIMITIVE_TWO_FORCE_BALANCE=true`.

必须重类型为：

`APPARENT_TWO_FORCE_EQUILIBRIUM -> PRIMITIVE=false`.

`APPARENT_TWO_FORCE_EQUILIBRIUM -> INTERPRETATION=COARSE_GRAINED_OR_PROJECTED_TRIADIC_BALANCE`.

`APPARENT_TWO_FORCE_EQUILIBRIUM -> TRIADIC_LIFT_REQUIRED=true`.

所谓“第三力”不要求在当前低维/低分辨率 observer 中直接可见；它可以属于被投影掉的空间分量、环境/约束交换、内部路径通道、时间关联或更细 Cell 作用关系。研究任务是构造合法的 `TRIADIC_LIFT`，不是用“两力表面上平衡”反驳 P000。

## 7. 四力及以上

P000 的“最小稳定单元为三力”同时规定原子性：

`STABLE_FORCE_COUNT>3 -> PRIMITIVE=false`.

`STABLE_FORCE_COUNT>3 -> TRIADIC_DECOMPOSITION_REQUIRED=true`.

也就是说，四力、五力、六力或更高元的稳定宏观配置若出现，必须在更底层解释为三元闭合网络/复合，而不能另立更高元“原子平衡”。

是否存在唯一三元分解不作默认要求；在 BRC/联合关系原则下，不唯一分解的 branch identity 与 multiplicity 必须保留，除非获得明确安全商证书。

## 8. 最高优先级与禁止回退

优先级冻结：

`P000_ROOT_AXIOM > ALL_DERIVED_GEOMETRY`.

`P000_ROOT_AXIOM > ALL_DERIVED_PHYSICAL_BRIDGES`.

`P000_ROOT_AXIOM > EXTERNAL_EFFECTIVE_MODEL_WHEN_REASONING_INSIDE_ENTERPRISE_MATH`.

硬错误：

`REIMPORT_90_DEGREES_AS_NATIVE_ENTERPRISE_RIGHT_ANGLE`.

`PROMOTE_OFF_NATIVE_AXIS_COARSE_SEGMENT_TO_PRIMITIVE_DIRECTION`.

`COLLAPSE_OFF_NATIVE_AXIS_PATH_PROVENANCE_WITHOUT_SCOPE_TYPED_SAFE_QUOTIENT`.

`ACCEPT_PRIMITIVE_STABLE_CONFIGURATION_WITH_EXACTLY_TWO_NONZERO_FORCES`.

`TREAT_APPARENT_TWO_FORCE_EQUILIBRIUM_AS_PRIMITIVE`.

`REQUIRE_PROOF_OR_FALSIFICATION_OF_P000_DIRECTION_OR_BALANCE_AXIOMS`.

## 9. 外部理论边界

对外部数学和物理仍须忠实报告其自身定义。例如欧氏正交仍是 `90°`；经典刚体静力学允许两个等大、反向、共线的力形成静态平衡。

这不改变 P000。外部结果只进入：

`EXTERNAL_EFFECTIVE_MODEL`.

在进取数论内部，对这些读出执行：

`EXTERNAL_MODEL_RESULT -> TYPE -> LIFT/TRANSLATE/COARSE_GRAIN_INTERPRET -> COMPARE_WITH_P000`.

禁止把 P000 内部公理伪装成“标准科学已经证明的共识”；同样禁止用外部模型的定义直接覆盖 P000。

## 10. 最小研究后果

从此以后，涉及几何方向、斜线、路径、力平衡、稳定性、流体/PDE 物理桥梁、格点动力学、BRC 压缩或旋转读出的研究，必须先经过两道 P000 gate：

`DIRECTION_GATE: primitive axis-aligned OR composite native path`.

`BALANCE_GATE: primitive triadic closure OR nonprimitive composite/lift`.

不得再把“任意连续方向都是原子直线”或“二力平衡是底层稳定原子”作为默认出发点。
