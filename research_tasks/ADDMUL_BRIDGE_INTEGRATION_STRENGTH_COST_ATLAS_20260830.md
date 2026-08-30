<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-ADDMUL-BRIDGE-INTEGRATION-STRENGTH-COST-ATLAS",
  "title": "加乘桥 Integration：统一强度—信息成本—可组合性图谱",
  "kind": "RESEARCH",
  "owner": "research/addmul-bridge-integration-strength-cost-atlas",
  "base_state": "READY",
  "priority": "P0",
  "leverage": "HIGH",
  "frontier": "Integrate the accepted A1–A7 addition/multiplication bridge results into one exact operation-safe comparison atlas: classify bridge strength, law transport, injectivity/fibers, hidden coordinates, partiality, exceptional loci, precision/refinement cost, and composability, then determine whether a minimal common bridge kernel exists or prove irreducible incomparability.",
  "next_action": "Instantiate the A7 BRIDGE_AUDIT_PACKET on A1–A6, freeze a common bridge signature, construct the pairwise composability matrix with exact witnesses/counterexamples, and isolate the minimal state augmentation required for operation-safe addition and multiplication without inventing duplicate precision, quotient, valuation, holonomy, or finite-difference machinery.",
  "dependencies": [
    "driver_reviews/ADDMUL_FIRST_WAVE_A1_A7_DRIVER_REVIEW_20260830.md",
    "research_returns/ADDMUL_BINOMIAL_CROSS_EFFECT_CALCULUS_RETURN_20260830.md",
    "research_returns/ADDMUL_DELTA_FROBENIUS_DEFECT_TOWER_RETURN_20260830.md",
    "research_returns/ADDMUL_FORMAL_GROUP_INTERPOLATION_RETURN_20260830.md",
    "research_returns/ADDMUL_WITT_GHOST_MULTISCALE_BRIDGE_RETURN_20260830.md",
    "research_returns/ADDMUL_VALUATION_TROPICAL_COLLAPSE_GEOMETRY_RETURN_20260830.md",
    "research_returns/ADDMUL_GAUSS_ADDITIVE_MULTIPLICATIVE_SPECTRUM_RETURN_20260830.md",
    "research_returns/ADDMUL_SUM_PRODUCT_OBSTRUCTION_STRESS_TEST_RETURN_20260830.md",
    "research_artifacts/ADDMUL_SUM_PRODUCT_OBSTRUCTION_STRESS_TEST/BRIDGE_AUDIT_PACKET_V1.json"
  ],
  "source_refs": [
    "research_method_inventory.json@main",
    "src/enterprise_math/precision.py@main",
    "src/enterprise_math/precision_holonomy.py@main",
    "src/enterprise_math/operation_quotient.py@main"
  ],
  "evidence_status": "A1_A7_DRIVER_ACCEPTED / CROSS_ROUTE_INTEGRATION_FRONTIER",
  "last_progress_ref": null,
  "last_progress_at": null,
  "hard_block": null,
  "tags": [
    "addmul",
    "integration",
    "bridge-strength",
    "information-cost",
    "operation-safety",
    "composability",
    "defect",
    "precision"
  ],
  "claim_lease_minutes": 240,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-ADDMUL-BRIDGE-INTEGRATION-STRENGTH-COST-ATLAS",
  "parent_objective_id": "OBJ-ADDMUL-BRIDGE-STRUCTURE",
  "parent_objective_generation_id": "OG-9D6617146723B8E72C6F",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "AMINT",
  "origin_kind": "DRIVER_ROADMAP",
  "task_lineage": "INTEGRATION",
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

# 加乘桥 Integration：统一强度—信息成本—可组合性图谱

Status: `READY / P0 / CROSS-ROUTE INTEGRATION`

## Mother question

A1–A7 已分别给出 cross-effect、delta/Frobenius、formal-group、Witt/ghost、valuation/tropical、Gauss/Jacobi 与 sum-product audit 七种不同强度的加乘桥。现在要回答的不是再找一种桥，而是：这些桥在同一 operation-safe 语言下究竟如何比较、能否组合，以及是否存在一个最小共同桥核；若不存在，精确证明其不可比性来源。

## Frozen inputs and scope

冻结 A1–A7 已接受的定理强度与所有反过度解释边界。A7 的 `BRIDGE_AUDIT_PACKET_V1` 作为共同审计框架；A1–A6 的原始 Result/Return 作为比较对象。必须先检查并复用现有 finite-difference、precision、quotient、valuation 与 defect/holonomy 工具覆盖。允许构造任务局部适配器与 exact finite certificates，但不得把经典理论改名后视为新机制。

## Hard target and required outputs

Hard target: `ADDMUL_BRIDGE_STRENGTH_INFORMATION_COST_COMPOSABILITY_ATLAS_CLASSIFIED`.

1. 为 A1–A6 各生成统一 `BRIDGE_SIGNATURE`：强度层级、domain/codomain、两种源操作的 transport 状态、injectivity/fiber、closure、exceptional locus、hidden coordinates、partiality、error、reconstruction rule。
2. 精确区分 coordinate change、exact homomorphic image、finite typed embedding、lossy invariant 与 spectral/correlation bridge；禁止用“都能把乘法变简单”替代分类。
3. 构造 A1–A6 的 pairwise composability matrix：对每一对给出 `COMPOSES_EXACTLY / COMPOSES_WITH_EXTRA_STATE / REDUNDANT_ON_DECLARED_DOMAIN / INCOMPATIBLE_OR_NOT_NATURAL` 之一，并附定理或最小反例。
4. 计算最小信息成本：至少跟踪 `DOMAIN / COLLISION / HIDDEN_COORDINATE / PARTIALITY / ERROR / PRECISION_REFINEMENT`；说明哪些成本可交换、哪些不可由另一类成本替代。
5. 特别比较 A1/A2 的 defect-reconstruction 与 A5 的 cancellation/refinement：判断是否存在统一的“生成缺陷 + 传输缺陷”有限状态接口，若不存在给出最小 no-go。
6. 特别比较 A3/A4 的 exact transformed-law/image 结构：判断 integrality/image predicates 是否可纳入同一 operation-safe state grammar，而不丢失 divisor locality 或 annihilator/fiber 信息。
7. 用 A6 作为独立谱侧压力测试：判断 zero-atom completion/sparse resonance defect 与前述代数状态是否有自然组合，还是只提供不可互换的线性坐标层。
8. 输出一个 exact atlas/certificate 与 deterministic checker。有限枚举仅作回归，核心分类必须由符号证明、类型证明或 exact counterexample 支撑。
9. 明确下一层只有在出现具体统一接口或具体能力缺口时才允许打开；若最终得到不可比性定理，则以该负结果关闭本 Integration task。

## Research value to preserve

第一波已经证明“加乘桥”不是单一概念。此任务要保存真正可复用的结构：桥梁强度、为了让操作成立必须付出的信息成本、以及不同桥之间是否能安全组合。若不存在统一核，精确的不可比性本身就是重要结果，可阻止后续把不同类型的桥误称为同一种机制。

## Success, kill, and return criteria

有效终态：`MINIMAL_COMMON_BRIDGE_KERNEL_CLASSIFIED` / `FINITE_SET_OF_INCOMPARABLE_BRIDGE_CLASSES_CLASSIFIED` / `OPERATION_SAFE_COMPOSITION_REQUIRES_EXPLICIT_DYNAMIC_STATE_AND_COST_LOWER_BOUND` / `INTEGRATION_NO_GO_WITH_EXACT_COUNTEREXAMPLES`。

Kill：不得把 A1 的 definability 升格为 primitive elimination；不得把 A6 的线性可逆升格为 convolution-algebra 同构；不得忽略 A4 的 integral-image predicate、A5 的 unit/residue 精度或 A2 的 anti-diagonal singularity；不得创建与现有工具功能等价的新通用引擎；不得为追求统一而删除类型、隐藏坐标或异常集合。
