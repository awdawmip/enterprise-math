<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id":"RS-ADDMUL-GAUSS-ADDITIVE-MULTIPLICATIVE-SPECTRUM","title":"加乘桥 A6：有限域 Gauss / Jacobi 加乘频谱","kind":"RESEARCH","owner":"research/addmul-gauss-additive-multiplicative-spectrum","base_state":"READY","priority":"P2","leverage":"MEDIUM",
  "frontier":"Classify finite-field additive and multiplicative characters as two Fourier-type coordinate systems coupled by Gauss/Jacobi sums, and determine exactly whether this is an algebraic bridge, a spectral correlation probe, or both on restricted subspaces.",
  "next_action":"Start with F_p: write both character systems and orthogonality exactly, compute the additive Fourier transform of multiplicative characters, classify zero/unit exceptions and inversion, then generalize only where the finite-field structure requires it.",
  "dependencies":[],"source_refs":["classical: additive characters, multiplicative characters, Gauss sums and Jacobi sums over finite fields"],
  "evidence_status":"DRIVER_ROADMAP_FROM_ADD_MUL_EXTERNAL_THEORY_SCOUT / FIRST_WAVE_UNEXECUTED","last_progress_ref":null,"last_progress_at":null,"hard_block":null,"tags":["addmul","finite-field","Gauss-sum","Jacobi-sum","Fourier","spectrum","characters"],"claim_lease_minutes":240,
  "created_by_role":"RESEARCH_DRIVER","task_authority":"PUBLISHED_REGISTERED","publication_contract":"RESEARCH_TASK_PUBLICATION_V1","publication_template":"RESEARCH_TASK_PUBLICATION_TEMPLATE_V1","registry_key":"RS-ADDMUL-GAUSS-ADDITIVE-MULTIPLICATIVE-SPECTRUM","parent_objective_id":"OBJ-ADDMUL-BRIDGE-STRUCTURE","parent_objective_generation_id":"OG-9D6617146723B8E72C6F","identity_policy":"AUTO_RESOLVE_OR_ALLOCATE","final_response_identity_policy":"INHERIT_GLOBAL","identity_lane":"AMSPEC","origin_kind":"DRIVER_ROADMAP","task_lineage":"NEW_DIRECTION","parent_task_id":null,"successor_gate":null,
  "policy_review":{"policy_set":"research_taskbook_policy.json","policy_digest":"sha256:10ec4f937324069d7af8d77a52c244389ac4cccd957e3685c14c6fe8b8fd367c","review_state":"PASS","temporary_overrides":[]}
}
-->

# 加乘桥 A6：有限域 Gauss / Jacobi 加乘频谱

Status: `READY / P2 / FINITE-FIELD`

## Mother question

有限域同时有 additive character `psi` 与 multiplicative character `chi`；Gauss sum \(G(\chi,\psi)=\sum_{x\ne0}\chi(x)\psi(x)\) 耦合两套角色。它究竟是可逆坐标桥、operation-intertwining bridge，还是仅为 correlation probe？

## Frozen inputs and scope

先做 `F_p`，确有新增结构才扩到 `F_q`。零元素与单位群分类型处理。允许角色正交、Gauss/Jacobi 基本公式作经典输入，但标准公式不计新结果。不得从小素数外推一般素数分布。

## Hard target and required outputs

Hard target: `FINITE_FIELD_ADDITIVE_MULTIPLICATIVE_SPECTRAL_BRIDGE_CLASSIFIED`

1. 精确定义 additive Fourier basis 与 multiplicative character basis、维数和零值处理。
2. 计算 multiplicative character 的 additive Fourier transform，分类 Gauss coefficients、rank 与 inversion。
3. 反向展开 additive character，处理 trivial character/constant/zero exceptions。
4. 用 Jacobi sums 或等价结构研究两类 convolution 的交叉结构常数。
5. 明确区分 `correlation probe`、`invertible typed transform`、`algebra isomorphism` 三个强度。
6. exact tables/checker 覆盖 `p<=31`；扩到 `F_q` 时只保留必要 trace/norm 增量。

## Research value to preserve

即使只有 probe 强度，也可量化 additive 与 multiplicative structure 的重叠；若存在 typed invertible transform，则为有限模空间提供可复核桥梁坐标。

## Success, kill, and return criteria

有效终态：`INVERTIBLE_TYPED_SPECTRAL_TRANSFORM_CLASSIFIED` / `GAUSS_BRIDGE_IS_CORRELATION_NOT_OPERATION_ISOMORPHISM` / `STANDARD_ONLY_NO_DISTINCT_RESIDUE`。不得忽略零元素，不得把 orthogonality 偷换成运算同构。
