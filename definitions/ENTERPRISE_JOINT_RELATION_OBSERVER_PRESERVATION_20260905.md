# 进取数论最高研究约束：联合关系观察方向不可因分解而默认删除

Status: `ACTIVE / DIRECT-USER PROJECT-HIGHEST RESEARCH CONSTRAINT / ALL-RESEARCH FOUNDATION`
Date: `2026-09-05`
Authority: direct current-user instruction.
Machine contract: `definitions/ENTERPRISE_JOINT_RELATION_OBSERVER_PRESERVATION_20260905.json`
Priority: `PROJECT_HIGHEST_RESEARCH_CONSTRAINT_BELOW_P000_ONTOLOGY`

## 1. 用户原始约束

> 不要只是把合数当成素数的重复产物；应该把它们保留为联合关系的观察方向。分解信息虽然已经存在，允许线性调用的交互方向却可能缺失。

这条约束在进取数论中提升为全研究基础约束，不仅适用于黎曼猜想，也适用于算术、BRC、路径、关系、分支、余数、相关、谱、压缩与商空间等所有会发生“先分解、再删除联合对象”的研究。

它是**研究方法与信息保存约束**，不是一个需要证明的数学定理，也不改变 P000 的 6D 世界观根公理。

## 2. 核心含义

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

所谓“分解信息已经存在”，不能作为删除联合关系观察方向的充分理由。

## 3. 最高约束

凡研究对象存在组成部分与联合对象两层结构时，默认执行：

1. 保留完整对象总体；
2. 保留联合对象作为候选观察方向；
3. 区分“可由分量重建原对象”与“可由分量观察量生成联合观察量”；
4. 在删除联合方向前，必须给出针对**当前观察者和未来允许操作**的精确因子化、线性张成、纤维常值或等价下降证书；
5. 如果证书不存在，则保留联合方向，或者增加显式 interaction/repair coordinate；
6. 若结果依赖符号、相位、抵消、进位、CRT 耦合、混合差或 provenance，不得用正质量聚合代替。

Freeze:

`RAW_DECOMPOSITION_INFORMATION_COMPLETE != DECLARED_OBSERVER_SPAN_COMPLETE`.

`JOINT_OBJECT_DETERMINED_BY_CONSTITUENTS != JOINT_OBSERVATION_REDUNDANT`.

`RECONSTRUCTIBLE_FROM_FACTORS != LINEARLY_CALLABLE_FROM_FACTOR_OBSERVERS`.

`CONSTITUENT_DATA_PRESENT != INTERACTION_DIRECTION_PRESENT`.

`JOINT_RELATION_DIRECTION -> PRESERVE_BY_DEFAULT`.

`DROP_JOINT_RELATION_DIRECTION -> REQUIRE_EXACT_OBSERVER_FACTORIZATION_OR_SPAN_CERTIFICATE`.

`DROP_JOINT_RELATION_DIRECTION -> REQUIRE_FUTURE_OPERATION_SAFETY_FOR_DECLARED_HORIZON`.

`WHEN_IN_DOUBT -> PRESERVE_JOINT_RELATION_DIRECTION`.

## 4. 算术专门化：合数不是默认可删除的“重复素数”

唯一分解或素因子分解可以决定一个合数的组成，但不能仅凭这一点推出合数索引的观察方向位于素数索引观察方向的允许线性张成中。

因此在算术研究中：

`COMPOSITE_INTEGER = ELIGIBLE_JOINT_RELATION_OBSERVATION_DIRECTION`.

`COMPOSITE_DECOMPOSABLE_INTO_PRIMES != COMPOSITE_OBSERVER_DIRECTION_DISCARDABLE`.

`PRIME_ONLY_VIEW = SECONDARY_PROJECTION_NOT_DEFAULT_DISCOVERY_UNIVERSE`.

删除合数观察方向必须证明具体的 observer-specific reduction，而不能只援引“它已经由素因子决定”。

特别地，若某个合数坐标承载 CRT 联合余数、进位、混合有限差分、多因子相关或其他非加法可分离交互，则应继续保留，直到存在更强的精确等价证书。

## 5. BRC 约束

本规则直接约束 BRC 压缩：

- branch/object population 必须先声明；
- observer、允许的未来操作与时间/尺度 horizon 必须先声明；
- raw reconstructibility 与 observer completeness 必须分开；
- quotient/collapse 前必须证明 fiber constancy、descent 或等价 factorization；
- 若联合方向未下降，则应保留或增加 repair coordinate；
- positive Weighted-BRC 不得替代 signed/phase interaction。

因此，“更小的 carrier”只有在对声明的 observer 与未来操作充分时才是合法的；**因子更基础、对象更原始、分解更唯一，都不能单独构成删除联合方向的理由。**

## 6. 适用范围

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
- 任意“分量数据存在，所以联合对象可删”的压缩尝试。

## 7. 防误读边界

本约束**不**意味着：

- 每个合数坐标都必然线性独立；
- 所有联合对象都必须永久保留；
- 唯一分解失效；
- prime-only 研究永远非法；
- 任何有限数值增益就是 RH 证明。

允许删除，但删除义务发生反转：

\[
\boxed{
\text{不是“证明联合方向有用后才保留”};\quad
\text{而是“证明联合方向对当前 observer 真正冗余后才删除”}.
}
\]

这就是本约束的默认研究姿态。

## 8. 优先级

本约束是进取数论的**最高研究方法/信息保存约束**，其优先级低于系统/安全/平台、用户当前直接指令以及 P000 世界观根公理，高于：

- 方法便利性的降维；
- prime-only 默认过滤；
- factor-only observer 选择；
- 未经证明的正质量重聚合；
- 未经证明的商、投影、压缩和 collapse。

任何下游定理、工具、BRC carrier 或研究路线，如与本约束发生冲突，应先保留联合关系方向并记录尚未完成的 reduction obligation。
