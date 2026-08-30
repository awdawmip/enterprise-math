<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-P000-THREE-AXIS-A2-HEXAGONAL-CUBIC-THETA-BRIDGE",
  "title": "P000 三轴切片 A2 / 六角格到 Borwein–Ramanujan 三次 Theta 的条件桥",
  "kind": "RESEARCH",
  "owner": "research/p000-three-axis-a2-hexagonal-cubic-theta-bridge",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "MEDIUM",
  "frontier": "Determine whether any declared three-axis P000 research slice legitimately descends to an A2-type difference/common-mode quotient, and only if that gate is proved, whether its exact shell enumeration naturally realizes hexagonal-lattice cubic theta structures relevant to Borwein and Ramanujan signature-3 theory.",
  "next_action": "Select one already-declared three-axis slice, prove or refute a common-mode/difference-only descent without using carrier rank to reduce P000, then if the descent survives construct exact A2 coordinates and compare the first shell generating functions with independently sourced cubic-theta identities.",
  "dependencies": [
    "enterprise_toolbox_registry.json@main"
  ],
  "source_refs": [],
  "evidence_status": "DRIVER_EXTERNAL_THEORY_SCOUTING_COMPLETE / A2_HEXAGONAL_ANALYTIC_BRIDGE_CONDITIONAL / COMMON_MODE_DESCENT_NOT_GRANTED",
  "last_progress_ref": null,
  "last_progress_at": null,
  "hard_block": null,
  "tags": ["P000","three-axis-slice","A2","hexagonal-lattice","theta-series","Borwein","Ramanujan","signature-3","cubic-theta","conditional-bridge"],
  "claim_lease_minutes": 240,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-P000-THREE-AXIS-A2-HEXAGONAL-CUBIC-THETA-BRIDGE",
  "parent_objective_id": "OBJ-P000-THREE-AXIS-ANALYTIC-NUMBER-THEORY-BRIDGE",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "P000A2T1",
  "origin_kind": "DRIVER_ROADMAP",
  "task_lineage": "NEW_DIRECTION",
  "parent_task_id": null,
  "successor_gate": null,
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:10ec4f937324069d7af8d77a52c244389ac4cccd957e3685c14c6fe8b8fd367c",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# P000 三轴切片 A2 / 六角格到 Borwein–Ramanujan 三次 Theta 的条件桥

Status: `READY / P2 / MEDIUM / P000-BOUND / QUOTIENT-GATE-FIRST`

## Mother question

当前 P000 明确规定：原生 Enterprise 空间是 6D，既有三轴构造只能是 6D 中的 research slice。对一个**已经声明、可独立读取的三轴 slice**，是否能严格证明其相关几何/算术只依赖坐标差，因而允许一个合法的 common-mode quotient；若且仅若这个 gate 成立，该 rank-2 quotient 是否真正形成 `A2`/六角格型离散结构，并进一步让 shell generating functions 自然接上 Borwein cubic theta 与 Ramanujan signature-3 对应理论？

本任务首先审查“能不能降到差分格”，而不是先寻找漂亮的 theta identity。

## Frozen inputs and scope

1. P000 不可被本任务挑战或降维：`6D space + separately typed time` 保持原义。
2. 三轴对象必须先从项目当前已声明的 research slice 中选择；不得为了匹配 `A2` 临时创造一个只有经典意义、没有 Enterprise typing 的三元组。
3. common-mode equivalence `(x,y,z) ~ (x+t,y+t,z+t)` **不是预设公理**。必须证明目标 observables/relations 对该变换不变，或从既有合法 quotient/decoder 中取得同等强度的结论。
4. “三个坐标满足一个线性关系”不能被用来推断 P000 原生空间只有二维或三维。
5. 若 quotient gate 失败，本任务应以 exact negative boundary 终止；不得继续做 A2/theta 拟合。
6. quotient gate 成功后，可选差分坐标 `u=x-y`, `v=y-z`, `w=z-x` with `u+v+w=0`，但 basis、orientation、norm 必须从声明 slice 的 rotation/incidence semantics 推导或明确标为 representation choice。
7. 解析数论部分允许独立查阅 Borwein cubic theta、hexagonal-lattice theta、Ramanujan signature-3、cubic AGM/triplication 的外部文献；所有引用身份与公式必须独立核验。
8. 现有 `T1_SCALE_ENUMERATION_VALUATION` 可用于 shell/count/generating-function compression；T7 可用于有限 symmetry checks。新工具只有在现有接口无法表达所需 exact operation 时才考虑。
9. 不因公式出现经典 `pi`、modular parameter 或 complex variable 就把这些对象提升为 P000 native primitives；它们属于 derived analytic representation。

## Hard target and required outputs

Hard target:

`P000_THREE_AXIS_SLICE_A2_HEXAGONAL_CUBIC_THETA_BRIDGE_CONSTRUCTED_OR_QUOTIENT_GATE_REFUTED`.

任务严格分 Gate 0 与 Gate 1；Gate 0 未通过不得进入 Gate 1 的实质匹配。

### Gate 0. Legitimate rank-2 descent

对一个明确命名的三轴 slice：

- 列出 preserved observables/relations；
- 证明或反驳 simultaneous translation invariance；
- 若通过，构造 quotient map 与 exact reconstruction/fiber description；
- 证明 quotient 没有错误擦除任务所需的 rotation/incidence/time-trace 信息；
- 区分 slice quotient 与 P000 native dimension；
- 给最小反例，说明什么额外 observable 会破坏 common-mode descent。

允许的 terminal negative：`COMMON_MODE_QUOTIENT_NOT_DERIVED_FOR_DECLARED_SLICE`。

### Gate 1A. A2 / hexagonal exact realization

只有 Gate 0 PASS 后：

- 选取 exact rank-2 lattice basis；
- 推导 neighbor/rotation action；
- 计算 induced quadratic or shell form；
- 判断它是否与标准 `A2` root lattice / hexagonal lattice 整同构、仅相似、或不等价；
- 给 determinant/discriminant/index 与 orientation dependence；
- 明确哪些 symmetries 来自 Enterprise slice，哪些只是表示坐标的 automorphisms。

不得以“图看起来像六边形”作为证明。

### Gate 1B. Shell enumeration

对得到的 lattice/slice object：

- exact 枚举前若干 shells；
- 建立 generating series；
- 用 T1 或等价 exact calculation 压缩 coefficient sequence；
- 识别 representation numbers 的 arithmetic structure；
- 对 rotation phase / residue classes 做必要分层；
- 给一个不依赖浮点的 checker。

### Gate 1C. Borwein cubic theta comparison

独立核验 cubic theta functions `a(q), b(q), c(q)` 的定义与标准关系，然后：

- 明确哪个 Enterprise shell series 对应或不对应哪一个 classical theta series；
- 若只差 normalization、character、coset shift 或 rescaling，精确写出；
- 检查 cubic identities 在 Enterprise-derived series 上是 theorem、specialization 还是 false analogy；
- 研究 triplication/cubic AGM 是否有 exact discrete interpretation；
- 至少构造一个能区分“真正 theta equivalence”与“前若干 coefficient 偶合”的反例/判别式。

### Gate 1D. Ramanujan signature-3 interface

只有在 cubic theta equivalence 达到 exact strength 后，才追踪 signature-3 parameterization / modular equations 对当前 derived slice 是否产生新 recurrence、新 shell identity、新 rotation/scale relation，或完全没有额外 Enterprise 信息。不得从 classical identity 的存在反推 P000 公理。

### Required artifact

返回必须含 Gate 0 exact proof/no-go；Gate 0 通过时的 lattice isomorphism certificate；shell table + exact generating data；classical-source audit；coefficient checker；normalization dictionary；所有仅为 analogy 的部分单独列出。

## Research value to preserve

三轴切片长期具有六角/三方向结构，但 P000 已把它重新类型化为 6D 空间中的 slice。正确的研究问题不再是“世界是不是 A2”，而是：

`legitimate 3-axis quotient -> exact A2-like lattice? -> shell arithmetic -> cubic theta?`

如果这条链真正闭合，它会把进取几何的一条**合法切片**接入 Ramanujan–Borwein 的解析数论 machinery，产生可验证的 shell identities、scale relations 和生成函数。若第一 gate 失败，也能明确终止过去容易发生的“减去共同量所以当然是二维六角格”的偷换。

## Success, kill, and return criteria

成功分类：

- `EXACT_A2_CUBIC_THETA_BRIDGE`：Gate 0、A2 realization 与至少一个 cubic-theta equivalence 均精确成立；
- `A2_SLICE_WITHOUT_CUBIC_THETA_GAIN`：合法 A2 slice 成立，但解析数论层没有新信息；
- `NON_A2_RANK2_SLICE`：quotient 合法但 lattice/form 不是 A2；
- `COMMON_MODE_QUOTIENT_NOT_DERIVED`：Gate 0 精确失败。

Kill / stop：需要把 P000 原生 6D 降成 2D/3D；common-mode equivalence 只是视觉或方便选择而非 theorem；只比较前几个系数就宣布 theta identity；用近似 modular numerics 代替 exact coefficient/algebraic identity；把 classical theta/modular parameter 当作 native Enterprise coordinate；为现有 T1/T7 能做的工作复制工具。

Return 必须同时报告正结果和失败的 mapping attempts，尤其要保留 normalization、coset、orientation 和 scale 上的负结果，防止后续重新尝试同一假桥。
