<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-GEO6-KISSING-CONTACT-CAPACITY-BRIDGE",
  "title": "六维 Kissing 接触容量与 P000 Cell 接触桥",
  "kind": "RESEARCH",
  "owner": "research/geo6-kissing-contact-capacity-bridge",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "Classify whether an explicitly defined native six-dimensional Cell contact model admits a finite rotation-compatible contact-capacity invariant that can faithfully receive, compare with, or sharply separate the classical R^6 kissing configurations underlying the 72-to-77 open gap.",
  "next_action": "Freeze one native Cell contact predicate and rotation-orbit readout without importing an Euclidean metric by name; encode the classical 72-point E6 kissing configuration as external comparison data; then test exact contact-graph preservation, lower/upper certificates, and transfer obstructions.",
  "dependencies": [],
  "source_refs": [
    "GLOBAL_KNOWLEDGE_V1:projects/enterprise-math/EXTERNAL_GEOMETRY_OPEN_PROBLEM_INTAKE_20260830.md@5778529",
    "GLOBAL_KNOWLEDGE_V1:projects/enterprise-math/P000_REALITY_FOUNDATION.json@main",
    "GLOBAL_KNOWLEDGE_V1:projects/enterprise-math/00_CURRENT_FOUNDATION.md@main"
  ],
  "evidence_status": "EXTERNAL_R6_KISSING_NUMBER_OPEN_72_TO_77 / E6_72_EXTERNAL_WITNESS / P000_NATIVE_CONTACT_SEMANTICS_NOT_YET_MAPPED",
  "last_progress_ref": "GLOBAL_KNOWLEDGE_V1:projects/enterprise-math/EXTERNAL_GEOMETRY_OPEN_PROBLEM_INTAKE_20260830.md",
  "last_progress_at": "2026-08-30T02:38:51+00:00",
  "hard_block": null,
  "tags": [
    "geometry",
    "P000",
    "native-6D",
    "kissing-number",
    "contact-capacity",
    "E6",
    "rotation",
    "contact-graph",
    "external-bridge"
  ],
  "claim_lease_minutes": 240,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-GEO6-KISSING-CONTACT-CAPACITY-BRIDGE",
  "parent_objective_id": "OBJ-EXTERNAL-GEOMETRY-STRUCTURAL-TRANSFER-20260830",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "G6KISS",
  "origin_kind": "DIRECT_USER_DIRECTION",
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

# 六维 Kissing 接触容量与 P000 Cell 接触桥

## Mother question

在 P000 的原生六维离散 Cell 空间中，先独立定义一个不偷渡欧氏内积的 native contact predicate、局部可容纳邻居集合与 rotation-compatible 方向/轨道读出。然后问：这样的接触模型能否接收、比较或严格区分经典 `R^6` kissing-number 问题中的有限配置，特别是 72 点 `E6` 外部见证与当前 `72 <= tau_6 <= 77` 的开放区间？

目标不是证明 native kissing number 等于经典数值，而是得到一个可复核的 native 接触容量对象，并精确判断经典有限接触码能否成为它的回归模型。

## Frozen inputs and scope

- P000 的 `6D space + 1D time`、Cell 本体、旋转优先与三轴仅为研究切片保持不变。
- 经典 `R^6`、球面、欧氏角度、`E6` 根系与 72 点 kissing configuration 只作为外部比较对象；`E6 != P000 carrier`，也不得替换当前 FCC carrier。
- 若使用距离、角度、Gram matrix 或单位球，必须明确标注为 external-model quantity，并另给 native readout/mapping。
- 第一阶段只研究有限局部接触容量、接触图、轨道、刚性和可验证上下界，不扩张为完整 native packing theorem。
- 允许 exact integer/rational/algebraic certificates 与有限穷举；有限穷举不能冒充一般定理。

## Hard target and required outputs

Hard target: `P000_NATIVE_6D_CONTACT_CAPACITY_ATLAS_CONSTRUCTED_OR_EUCLIDEAN_TRANSFER_OBSTRUCTED`.

至少完成：

1. 给出一个明确的 native Cell contact predicate 与局部 admissibility 条件；
2. 给出 rotation action 下的 contact-orbit / stabilizer / adjacency 数据结构；
3. 独立重建 72 点 `E6` 外部配置的 exact finite contact certificate，避免只引用数值；
4. 定义 external-to-native mapping interface，并证明至少一种：faithful contact embedding、受限同态、或 exact obstruction；
5. 在声明的 native finite model class 上给出非平凡 lower/upper contact-capacity bound，或证明当前 primitives 不足以定义 canonical capacity；
6. 提供 deterministic checker/certificate，至少覆盖 72 点外部回归、native contact consistency、rotation invariance 与一个 adversarial countermodel；
7. 输出 `research_returns/GEO6_KISSING_CONTACT_CAPACITY_BRIDGE_RETURN_20260830.md`。

## Research value to preserve

六维 kissing number 把“连续几何直觉”压缩成一个很小的有限接触缺口。它天然适合进取数论的 Cell、关系、旋转和 exact certificate 语言。如果 transfer 成功，会得到新的六维局部几何压力测试；如果 transfer 被 obstruction，也会精确告诉我们 native contact/metric 还缺什么，而不是用外部欧氏模型替代 P000。

## Success, kill, and return criteria

Success：得到可复核的 native contact-capacity 定义，并在至少一个非平凡模型类上建立 exact bound/realization，且外部 72 点配置的角色被严格分类。

Kill / no-go 也可作为有效终态：证明在当前声明 primitives 下 contact capacity 非 canonical，或任何把 72 点配置搬入 native 结构的映射必然依赖额外 metric/readout datum。

立即判失败而非新结果的情形：
- 直接宣称 `tau_native = 72`、`77` 或 `E6` 为 native carrier；
- 把欧氏内积/角度原样当作未定义的 P000 primitive；
- 只展示数值相似或图形相似；
- 通过选定 embedding 后的 tautology 产生所谓上界；
- 用有限 census 代替全模型证明。

返回必须明确标注 `EXTERNAL_THEOREM / NATIVE_DEFINITION / TRANSFER_THEOREM / OBSTRUCTION / COMPUTATIONAL_REGRESSION` 五类证据的边界。
