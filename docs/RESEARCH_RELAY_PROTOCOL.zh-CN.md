# Enterprise Math / 进取数论 Research Relay 协议

状态：`ACTIVE ARCHITECTURE PROPOSAL`  
实时总线：GitHub Issue #82 — `Research Relay: cross-branch theorem and finding bus`

## 1. 目的

进取数论现在存在多条长期研究分支。不同路线可能独立发现同一个母定理、严格推广、有价值的特化或反例。反复整分支 merge 不能作为同步机制，因为它会把旧 ledger、历史实验和不相关变更一起带入，并模糊真正的数学归属。

Research Relay 是一个**独立于具体分支历史的实时跨路线数学反馈层**。

它不替代 Git history、定理账本、PR review 或规范 `main`。

## 2. 强制研究循环

每条实质研究分支应执行：

1. **先读再扩展。** 开始新的通用定理路线前，先读取影响当前分支的最新 relay entries。
2. **先分类再新增。** 引入新抽象前，先用以下关系检查已有 relay / lineage：
   - `SAME_MOTHER`；
   - `STRICT_GENERALIZATION`；
   - `SPECIALIZATION`；
   - `GENERATOR`；
   - `COMPOSABLE_INDEPENDENT`；
   - `CONFLICT / NEGATIVE_BOUNDARY`；
   - `NAME_COLLISION_ONLY`。
3. **重要结果必须回流。** 当一个结果改变了其他路线依赖的假设、否定其他路线、给出可复用母定理、发现关键反例，或建立其他活跃分支可以使用的桥梁时，必须及时 relay。
4. **下游按语义吸收。** 下游通过 dependency、corollary 或 semantic replay 使用母定理，不再独立维护第二份同一母结构。
5. **稳定后再提升。** 只有稳定结论才从实时 relay 进入 `CONCEPT_LINEAGE`、架构文档、定理/反例账本、prior-art records 或规范 `main`。

## 3. Relay entry 必须包含

每条重要 relay 至少包括：

- source branch 与精确 commit；
- 可用时附 PR / issue；
- 数学陈述本身；
- 状态：proved / executable-checked / conjectural / counterexample；
- 当前最弱已知假设；
- 影响的 branches / modules；
- 与已有成果的关系分类；
- 下游明确应该采取的动作。

**负结果与正结果同等优先。** 一个反例如果阻止我们错误合并两套理论，本身就是架构推进。

## 4. 需要立即反馈的情形

出现以下情况时应及时 relay：

- 一个定理删除了另一分支正在使用的假设；
- 证明两个不同命名对象实际上是同一母结构；
- 一个 strict generalization 已经覆盖另一活跃路线；
- 反例否定拟议中的桥梁、解释或闭包；
- 新 observable 要求比下游当前保存状态更细的 precision / witness identity；
- application-specific 结果被证明与应用无关；
- 一般母定理产生新的、具有非平凡后果的领域特化。

没有跨路线影响的普通局部 lemma 不需要占用 relay。

## 5. 数学归属规则

Relay 传递的是结论，不自动改变 ownership。

一个可复用结果只保留一个当前一般数学归属。应用分支继续保留：

- discovery provenance；
- domain assumptions；
- application-specific corollaries；
- counterexamples 与 executable pressure tests。

一般 theorem home 保留母定理及其最弱已知假设。

## 6. 与长期研究分支的关系

Relay 位于单个 branch history 之外，所以即便一个研究分支已经和 `main` 分叉很多提交，研究员仍可以读取当前跨项目研究状态。

不要仅仅为了获得其他分支的信息，就反复 merge `main` 或其他 research branch。只有真正需要移动代码/定理资产时才做 semantic replay。

## 7. 第一条正式 Relay 定理

本协议下第一条实质结论是 A3→A4 bridge：

- A3 weighted relation state 在先 quotient `Z_ij=0` classes 后，会生成一类受限制的 A4 admissible-support family；
- support 条件为 `|Z_ij| <= r m_i m_j`；
- A3 weighted closure 推出 `R_r ; R_s ⊆ R_(r+s)`；
- universal fine support 可以下沉为 coarse support；
- coarse support 无法恢复 universal fine support，因为 signed A3 relations 在 partition quotient 中可以抵消。

该结果分类为 `GENERATOR`，并对逆恢复命题记录 `CONFLICT / NEGATIVE_BOUNDARY`。

## 8. 研究员恢复分支时的启动检查

研究员重新进入已有 branch 时，应先确定：

1. 当前 branch head；
2. 最新 canonical `main` head；
3. 与当前路线相关的最新 Research Relay entries；
4. 当前分支所属 architecture node（A0–A5 / P / E）；
5. 准备新增的 theorem 是否已经被其他分支 relay。

这个 startup check 只用于获取信息，不具有破坏性。禁止把 wholesale merge unrelated branch history 当作启动同步手段。
