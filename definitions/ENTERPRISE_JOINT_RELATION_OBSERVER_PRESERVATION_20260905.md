# 进取数论最高研究约束：联合关系观察方向不可因分解而默认删除

Status: `ACTIVE / DIRECT-USER PROJECT-HIGHEST RESEARCH CONSTRAINT / ALL-RESEARCH FOUNDATION`
Date: `2026-09-05`
Authority: direct current-user instruction.
Machine contract: `definitions/ENTERPRISE_JOINT_RELATION_OBSERVER_PRESERVATION_20260905.json`
Priority: `PROJECT_HIGHEST_RESEARCH_CONSTRAINT_BELOW_P000_ONTOLOGY`

## 1. 用户原始约束

> 不要只是把合数当成素数的重复产物；应该把它们保留为联合关系的观察方向。分解信息虽然已经存在，允许线性调用的交互方向却可能缺失。

> 合数是路，素数是坑；路都没有了，光盯着坑有啥用。不允许轻易判定冗余。

这两条约束合并为进取数论的全研究最高信息保存原则：**先保留关系背景，再研究异常；先证明冗余，再允许删除。**

它不仅适用于黎曼猜想，也适用于算术、BRC、路径、关系、分支、余数、相关、谱、压缩与商空间等所有会发生“先分解、再删除联合对象或背景对象”的研究。

它是直接用户定义的**研究方法与信息保存约束**，不是需要在项目内部先证明才可使用的数学定理，也不改变 P000 的 6D 世界观根公理。

## 2. “合数是路，素数是坑”的严格研究含义

在进取数论的研究解释中：

- **合数层是路**：它承担大部分整数总体中的连接背景、联合关系、过渡、进位、CRT 耦合、多因子相互作用、路径连续性以及供异常比较的基线；
- **素数层是坑**：它作为相对于完整整数关系背景而出现的特殊、稀疏、缺陷式或例外式观察对象；
- **坑必须相对于路才能被完整描述**：如果先把路删掉，只剩下坑的位置，那么坑之间的间隔、过渡机制、局部环境、关系结构以及“为什么这里是坑”的比较基线都可能同时消失。

因此，研究素数不能默认等价于删除合数后只研究 prime-only 子集。prime-only 视图只能是完整整数总体上的一个次级投影。

Freeze:

`COMPOSITE_LAYER = RELATIONAL_ROAD_BACKGROUND_AND_JOINT_INTERACTION_CARRIER`.

`PRIME_LAYER = DISTINGUISHED_HOLE_OR_DEFECT_OBSERVER_RELATIVE_TO_RETAINED_BACKGROUND`.

`REMOVE_RELATIONAL_ROAD_BACKGROUND -> PRIME_DEFECT_CONTEXT_MAY_BE_DESTROYED`.

`PRIME_ONLY_VIEW_WITHOUT_BACKGROUND_RELATION_FIELD = CONTEXT_LOSS_RISK`.

这里“路/坑”是进取数论内部的强制研究解释与信息保存规则；它不声称是经典教材里对整数的标准术语。

## 3. 核心含义：可分解不等于冗余

一个联合对象能够由其组成部分重建，只说明**原始信息可恢复**；这并不自动说明该联合对象对应的观察量，能够由允许的组成部分观察量通过当前允许的线性组合、加法分离、正质量聚合或其他受限操作来生成。

因此：

\[
\boxed{
\text{factor reconstructibility}
\neq
\text{observer-span completeness}
}
\]

以及

\[
\boxed{
\text{joint object determined by constituents}
\neq
\text{joint observation redundant}
}.
\]

更强地冻结：

`RECONSTRUCTIBLE != REDUNDANT`.

所谓“分解信息已经存在”，不能作为删除联合关系观察方向或合数背景的充分理由。

## 4. 冗余判定责任反转：默认不是冗余，而是尚未证明冗余

以后所有会丢信息的投影、商、压缩、只保留素数、只保留原子因子等操作，都采用以下默认状态：

`REDUNDANCY_STATUS_DEFAULT = UNPROVEN_RETAIN`.

即：一个方向没有被证明必要，并不等于它冗余；一个方向在某个有限数值拟合中系数小、为零或能被近似替代，也不等于它全局冗余。

明确禁止：

`EASY_REDUNDANCY_ASSUMPTION = FORBIDDEN`.

`NO_EXACT_REDUNDANCY_CERTIFICATE -> NO_ERASURE`.

任何冗余结论都必须明确回答：

1. 要删的是哪个对象/方向，原总体是什么；
2. 相对于哪个 observer/readout 判定冗余；
3. 后续允许哪些运算、组合、变换和尺度推进；
4. 结论覆盖的是有限 horizon 还是无限 horizon；
5. 是否存在精确 factorization、span membership、fiber constancy、descent 或等价安全证书；
6. signed、phase、multiplicity、carry、CRT、path、provenance、interaction 是否全部得到保存。

任何一项没有闭合，就保持：

`REDUNDANCY = UNPROVEN`，并继续保留该方向。

## 5. 禁止把局部冗余偷换成全局冗余

以下推理一律无效：

`LOCAL_OBSERVER_REDUNDANCY -> GLOBAL_REDUNDANCY`.

`FINITE_HORIZON_REDUNDANCY -> UNBOUNDED_HORIZON_REDUNDANCY`.

`CURRENT_READOUT_REDUNDANCY -> FUTURE_OPERATION_REDUNDANCY`.

`FINITE_NUMERICAL_FIT -> EXACT_REDUNDANCY`.

`SMALL_OR_ZERO_FITTED_COEFFICIENT -> STRUCTURAL_REDUNDANCY`.

正确的机器约束是：

`LOCAL_OBSERVER_REDUNDANCY != GLOBAL_REDUNDANCY`.

`FINITE_HORIZON_REDUNDANCY != UNBOUNDED_HORIZON_REDUNDANCY`.

`CURRENT_READOUT_REDUNDANCY != FUTURE_OPERATION_REDUNDANCY`.

一个冗余证书只在它明确证明的 observer、operation family 和 horizon 内有效，不得静默升级。

## 6. 最高约束的执行顺序

凡研究对象存在组成部分与联合对象两层结构时，默认执行：

1. 保留完整对象总体；
2. 保留作为“路”的背景总体；
3. 保留联合对象作为候选观察方向；
4. 再标注素数、稀疏事件、缺陷或其他特殊 strata；
5. 区分“可由分量重建原对象”与“可由分量观察量生成联合观察量”；
6. 在删除联合方向前，必须给出针对**当前观察者和未来允许操作**的精确因子化、线性张成、纤维常值或等价下降证书；
7. 如果证书不存在，则保留联合方向，或者增加显式 interaction/repair coordinate；
8. 若结果依赖符号、相位、抵消、进位、CRT 耦合、混合差、路径或 provenance，不得用正质量聚合代替。

Freeze:

`RAW_DECOMPOSITION_INFORMATION_COMPLETE != DECLARED_OBSERVER_SPAN_COMPLETE`.

`JOINT_OBJECT_DETERMINED_BY_CONSTITUENTS != JOINT_OBSERVATION_REDUNDANT`.

`RECONSTRUCTIBLE_FROM_FACTORS != LINEARLY_CALLABLE_FROM_FACTOR_OBSERVERS`.

`CONSTITUENT_DATA_PRESENT != INTERACTION_DIRECTION_PRESENT`.

`JOINT_RELATION_DIRECTION -> PRESERVE_BY_DEFAULT`.

`DROP_JOINT_RELATION_DIRECTION -> REQUIRE_EXACT_OBSERVER_FACTORIZATION_OR_SPAN_CERTIFICATE`.

`DROP_JOINT_RELATION_DIRECTION -> REQUIRE_FUTURE_OPERATION_SAFETY_FOR_DECLARED_HORIZON`.

`WHEN_IN_DOUBT -> PRESERVE_COMPOSITE_ROAD_AND_JOINT_RELATION_DIRECTION`.

## 7. 算术专门化：不能把路删了以后只研究坑

唯一分解或素因子分解可以决定一个合数的组成，但不能仅凭这一点推出合数索引的观察方向位于素数索引观察方向的允许线性张成中。

因此在算术研究中：

`COMPOSITE_INTEGER = ELIGIBLE_JOINT_RELATION_OBSERVATION_DIRECTION`.

`COMPOSITE_DECOMPOSABLE_INTO_PRIMES != COMPOSITE_OBSERVER_DIRECTION_DISCARDABLE`.

`PRIME_ONLY_VIEW = SECONDARY_PROJECTION_NOT_DEFAULT_DISCOVERY_UNIVERSE`.

`PRESERVE_FULL_INTEGER_POPULATION -> RETAIN_COMPOSITE_ROAD_BACKGROUND -> RETAIN_JOINT_COMPOSITE_OBSERVERS -> PROVE_SCOPE_TYPED_REDUNDANCY_BEFORE_ERASURE`.

删除合数观察方向必须证明具体的 observer-specific reduction，而不能只援引“它已经由素因子决定”。

特别地，若某个合数坐标承载 CRT 联合余数、进位、混合有限差分、多因子相关、路径连续性、过渡结构或其他非加法可分离交互，则应继续保留，直到存在更强的精确等价证书。

## 8. BRC 约束

本规则直接约束 BRC 压缩：

- branch/object population 必须先声明；
- “路”的背景总体不能在研究“坑”之前被默认抹去；
- observer、允许的未来操作与时间/尺度 horizon 必须先声明；
- raw reconstructibility 与 observer completeness 必须分开；
- redundancy 默认状态是 `UNPROVEN_RETAIN`；
- quotient/collapse 前必须证明 fiber constancy、descent 或等价 factorization；
- 若联合方向未下降，则应保留或增加 repair coordinate；
- positive Weighted-BRC 不得替代 signed/phase interaction。

因此，“更小的 carrier”只有在对声明的 observer 与未来操作**已经证明充分**时才是合法的；**更基础、更原子、可分解、分解唯一、数值上暂时不活跃，都不能单独构成冗余证书。**

## 9. 适用范围

本约束一般化到：

- 合数与素因子；
- 联合模数与单模数；
- CRT 联合余数；
- 路径组合与单段路径；
- 多分支联合事件；
- 高阶反馈 interaction；
- 多因子相关与单因子边缘量；
- joint residue / mixed difference / carry；
- provenance-sensitive observables；
- background/defect、road/hole 型结构；
- 任意“分量数据存在，所以联合对象可删”的压缩尝试。

## 10. 防误读边界

本约束不要求预先证明每个合数坐标都线性独立，也不禁止在获得严格证书后建立 prime-only 投影。

但删除义务发生彻底反转：

\[
\boxed{
\text{不是“证明联合方向有用后才保留”};\quad
\text{而是“在明确范围内证明联合方向真正冗余后才删除”}.
}
\]

而且这个“真正冗余”必须带 scope：局部只能推出局部，有限只能推出有限，当前 observer 只能推出当前 observer。

## 11. 优先级

本约束是进取数论的**最高研究方法/信息保存约束**，其优先级低于系统/安全/平台、用户当前直接指令以及 P000 世界观根公理，高于：

- 方法便利性的降维；
- prime-only 默认过滤；
- factor-only observer 选择；
- 非正式的“看起来重复”；
- 有限拟合得到的“似乎没用”；
- 未经证明的正质量重聚合；
- 未经证明的商、投影、压缩和 collapse。

任何下游定理、工具、BRC carrier 或研究路线，如与本约束发生冲突，应先保留“合数之路”和联合关系方向，并把冗余状态记录为 `UNPROVEN`，直到严格 reduction obligation 闭合。
