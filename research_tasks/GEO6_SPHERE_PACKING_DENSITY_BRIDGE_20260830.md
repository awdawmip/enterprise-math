<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-GEO6-SPHERE-PACKING-DENSITY-BRIDGE",
  "title": "六维球堆积与 P000 非重叠密度桥",
  "kind": "RESEARCH",
  "owner": "research/geo6-sphere-packing-density-bridge",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "Define a native six-dimensional non-overlap and density/occupancy invariant for Cell configurations and determine which parts of the classical R^6 sphere-packing problem, including the known nonsharp linear-programming boundary, survive an explicit semantics-preserving transfer.",
  "next_action": "Freeze one finite-window native occupancy/non-overlap model and its refinement law; separate contact from volume/density; reproduce one classical R^6 packing benchmark as external data; then search for native density bounds or an exact proof that the Euclidean density notion has no canonical transfer.",
  "dependencies": [],
  "source_refs": [
    "GLOBAL_KNOWLEDGE_V1:projects/enterprise-math/EXTERNAL_GEOMETRY_OPEN_PROBLEM_INTAKE_20260830.md@5778529",
    "GLOBAL_KNOWLEDGE_V1:projects/enterprise-math/P000_REALITY_FOUNDATION.json@main",
    "GLOBAL_KNOWLEDGE_V1:projects/enterprise-math/00_CURRENT_FOUNDATION.md@main"
  ],
  "evidence_status": "EXTERNAL_R6_SPHERE_PACKING_OPTIMUM_OPEN / CLASSICAL_LP_BOUND_NONSHARP_IN_D6 / P000_NATIVE_DENSITY_SEMANTICS_UNRESOLVED",
  "last_progress_ref": "GLOBAL_KNOWLEDGE_V1:projects/enterprise-math/EXTERNAL_GEOMETRY_OPEN_PROBLEM_INTAKE_20260830.md",
  "last_progress_at": "2026-08-30T02:38:51+00:00",
  "hard_block": null,
  "tags": [
    "geometry",
    "P000",
    "native-6D",
    "sphere-packing",
    "density",
    "non-overlap",
    "E6",
    "refinement",
    "external-bridge"
  ],
  "claim_lease_minutes": 240,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-GEO6-SPHERE-PACKING-DENSITY-BRIDGE",
  "parent_objective_id": "OBJ-EXTERNAL-GEOMETRY-STRUCTURAL-TRANSFER-20260830",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "G6PACK",
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

# 六维球堆积与 P000 非重叠密度桥

## Mother question

在 P000 原生六维 Cell 空间里，能否定义一个由 native non-overlap、有限窗口/边界规则与 refinement law 共同决定的“堆积占用/密度”对象，并把经典 `R^6` 球堆积只作为外部 benchmark 来比较？

核心不是寻找一个欧氏格点的同构，而是判断哪些 packing 结构——局部排斥、接触、周期性、密度极限、线性规划式约束——在明确 mapping 后仍有 native 意义。

## Frozen inputs and scope

- 不把欧氏球、Lebesgue volume、半径、`E6` lattice 或经典最密猜想作为 P000 primitive。
- native packing object 必须首先由 Cell relation / admissibility / occupancy 规则定义。
- contact capacity 与 global density 分开；本任务不得把上一条 kissing task 的结论当作已知。
- 经典六维 sphere packing、`E6` 等候选与“经典线性规划界在 d=6 不锋利”的事实仅用于外部压力测试。
- 允许有限周期盒、quotient cell complex、exact rational density、subadditive/superadditive bounds 与 refinement experiments；任何极限结论必须有证明。

## Hard target and required outputs

Hard target: `P000_NATIVE_6D_PACKING_DENSITY_OR_NONOVERLAP_INVARIANT_CLASSIFIED`.

必须输出：

1. 一个 native object/non-overlap predicate；
2. 一个有限窗口占用函数与边界误差控制，或证明此类极限不可由当前 primitives canonical 地定义；
3. translation/rotation/refinement 变换下的 invariant/equivariance law；
4. 至少一个外部六维 packing benchmark 的 exact representation，并明确 mapping 所需额外 datum；
5. 至少一个 native lower construction 与一个 independent upper mechanism，或 exact no-go；
6. 分析 classical LP/energy bound 哪些抽象步骤可移植、哪些严格依赖欧氏 Fourier/volume 结构；
7. deterministic checker 覆盖有限窗口、non-overlap、对称性和 adversarial boundary cases；
8. 输出 `research_returns/GEO6_SPHERE_PACKING_DENSITY_BRIDGE_RETURN_20260830.md`。

## Research value to preserve

如果 P000 的六维 Cell 空间存在自然 packing density，它可能成为连接局部接触、全局覆盖、旋转和尺度 refinement 的核心几何量；如果不存在 canonical density，则这个 no-go 同样重要，因为它会阻止以后把经典 sphere packing 的结论未经语义映射就搬入体系。

## Success, kill, and return criteria

Success：在声明的 native model class 上定义并证明一个非平凡 density/occupancy invariant，给出上下界或极值结构，并对 classical benchmark 的 transfer strength 做清晰分级。

有效 kill/no-go：证明任何候选 density 必须依赖未冻结的 measure/metric/window datum，从而当前 P000 primitives 只支持 contact/occupancy 层而不支持 canonical packing density。

失败情形：
- 直接把 Euclidean sphere volume 当 native Cell volume；
- 以 `E6` 候选身份代替 native 最优性证明；
- 把经典 LP bound 当成 native upper bound 而无 transfer theorem；
- 只做有限盒优化后外推无限极限；
- 用选定坐标 presentation 的密度冒充 coordinate-free native invariant。
