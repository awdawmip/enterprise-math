<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-ADDMUL-DELTA-FROBENIUS-DEFECT-TOWER",
  "title": "加乘桥 A2：整数 δ_p / Frobenius 加法缺陷塔",
  "kind": "RESEARCH",
  "owner": "research/addmul-delta-frobenius-defect-tower",
  "base_state": "READY",
  "priority": "P0",
  "leverage": "HIGH",
  "frontier": "Classify the exact integer family delta_p(n)=(n-n^p)/p and its additive defect D_p(x,y), with p=2 recovering -xy and odd primes producing higher mixed terms; determine cocycle, reconstruction, valuation and information-loss structure.",
  "next_action": "Prove integrality and the general mixed-coefficient formula, derive the associativity/cocycle identity, classify p=2 versus odd-prime reconstruction and singular loci, then connect the defect tower to existing valuation/holonomy machinery.",
  "dependencies": [],
  "source_refs": ["classical: p-derivation / delta-ring Frobenius-lift identities","research_method_inventory.json@main","src/enterprise_math/precision_holonomy.py@main","src/enterprise_math/precision.py@main"],
  "evidence_status": "DRIVER_ROADMAP_FROM_ADD_MUL_EXTERNAL_THEORY_SCOUT / FIRST_WAVE_UNEXECUTED",
  "last_progress_ref": null,
  "last_progress_at": null,
  "hard_block": null,
  "tags": ["addmul","delta-ring","Frobenius","p-derivation","defect","cocycle","valuation"],
  "claim_lease_minutes": 240,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-ADDMUL-DELTA-FROBENIUS-DEFECT-TOWER",
  "parent_objective_id": "OBJ-ADDMUL-BRIDGE-STRUCTURE",
  "parent_objective_generation_id": "OG-9D6617146723B8E72C6F",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "AMDELTA",
  "origin_kind": "DRIVER_ROADMAP",
  "task_lineage": "NEW_DIRECTION",
  "parent_task_id": null,
  "successor_gate": null,
  "policy_review": {"policy_set":"research_taskbook_policy.json","policy_digest":"sha256:10ec4f937324069d7af8d77a52c244389ac4cccd957e3685c14c6fe8b8fd367c","review_state":"PASS","temporary_overrides":[]}
}
-->

# 加乘桥 A2：整数 δ_p / Frobenius 加法缺陷塔

Status: `READY / P0 / PRIME-INDEXED`

## Mother question

对素数 `p`，
\[
\delta_p(n)=\frac{n-n^p}{p},\qquad
D_p(x,y)=\delta_p(x+y)-\delta_p(x)-\delta_p(y)
=-\sum_{i=1}^{p-1}\frac{\binom pi}{p}x^iy^{p-i}.
\]
特别地 \(D_2=-xy\)。这一 prime-indexed defect family 是否产生真正可复用的加乘耦合塔？

## Frozen inputs and scope

`x,y,z in Z`；允许 Fermat 同余和标准 p-derivation/Frobenius-lift 恒等式。必须分开 `p=2` 与奇素数，不得假设奇 `p` 可无损恢复乘法。defect transport/valuation/holonomy 优先复用现有工具；外部 δ-ring 理论不自动成为项目底层结构。

## Hard target and required outputs

Hard target: `INTEGER_DELTA_P_FROBENIUS_ADDITIVE_MULTIPLICATIVE_DEFECT_TOWER_CLASSIFIED`

1. 证明 integrality 与一般整数系数公式。
2. 完全冻结 `p=2` 的全整数域乘法恢复式。
3. 显式展开 `p=3,5,7` 并证明一般奇素数的混合项结构。
4. 证明并分类 \(D_p(x,y)+D_p(x+y,z)=D_p(y,z)+D_p(x,y+z)\) 的 coherence 强度。
5. 分类奇 `p` 从 `(x+y,D_p)` 恢复 `xy` 的可行域、奇异域、附加信息与整数除法障碍。
6. 研究 valuation/support footprint，给出与现有 defect/holonomy 工具的复用结论及 exact checker。

## Research value to preserve

把单一 `p=2` 现象扩展成素数尺度 defect tower；即使奇素数只给有损 bridge，奇异集和 valuation footprint 也可成为后续不变量。

## Success, kill, and return criteria

有效终态：`PRIME_INDEXED_DEFECT_TOWER_CLASSIFIED` / `P2_EXACT_ODD_P_INFORMATION_LOSS_CLASSIFIED` / `STANDARD_COBBOUNDARY_ONLY_NO_NEW_RESIDUE`。不得把标准 p-derivation 公式当新定理，不得隐藏 `x+y=0` 等奇异点，不得把有理逆误写成整数同构。
