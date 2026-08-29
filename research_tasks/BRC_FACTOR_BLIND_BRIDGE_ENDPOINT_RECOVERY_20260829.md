<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-BRC-FACTOR-BLIND-BRIDGE-ENDPOINT-RECOVERY",
  "title": "BRC 因子盲桥端点恢复：从桥响应到非平凡因子",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "The factor-blind square-shell bridge route has closed its tested periodic/residue mechanism class, while CBRC exposes exact support-sensitive survivor structure without an endpoint-recovery rule. Explore whether BRC-style balanced operators can generate a public response whose hidden CRT channels separate enough to extract a nontrivial factor, without additive-distance features or factor-label leakage.",
  "next_action": "Freeze a public-input/private-verifier contract for semiprime N, then precommit a small BRC-derived operator family and response/extraction rule before inspecting hidden factors. Test bridge-existence detection, endpoint recall and exact total cost separately, with adversarial balanced/unbalanced semiprimes and prior-art-equivalence checks.",
  "dependencies": [
    "research_result_reviews/RR-C5769D6B237D02BFF025/DR-BC224E4802009728727F.json@main",
    "driver_reviews/CBRC_F3R2_SURVIVOR_MEMBERSHIP_PREDICATE_DRIVER_REVIEW_20260823.md@main"
  ],
  "source_refs": [
    "driver_reviews/FACTOR_BLIND_SQUARE_MULTIPLICATIVE_SHELL_BRIDGE_DRIVER_REVIEW_20260829.md@main",
    "driver_reviews/CBRC_F3R2_SURVIVOR_MEMBERSHIP_PREDICATE_DRIVER_REVIEW_20260823.md@main"
  ],
  "evidence_status": "DIRECT_USER_DIRECTION / INTEGRATION / PERIODIC_SHELL_RESIDUE_ROUTE_CLOSED / NONPERIODIC_BRC_ENDPOINT_ROUTE_OPEN",
  "hard_block": null,
  "tags": ["BRC", "factor-blind", "endpoint-recovery", "semiprime", "CRT", "zero-divisor", "gcd", "balanced-operator", "leakage-control", "factorization"],
  "claim_lease_minutes": 240,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-BRC-FACTOR-BLIND-BRIDGE-ENDPOINT-RECOVERY",
  "parent_objective_id": "OBJ-MULTIPLICATIVE-BRIDGE-GEOMETRY",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "MBG-E0",
  "origin_kind": "DIRECT_USER_DIRECTION",
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

# BRC 因子盲桥端点恢复：从桥响应到非平凡因子

Status: `READY / P1 / HIGH-LEVERAGE / FACTOR-BLIND-ENDPOINT`

## Mother question

给定未知奇半素数 \(N=pq\)，能否完全不知道 \(p,q\) 地选择一族 BRC-derived operators \(B_\lambda\)，计算公开 response \(R_\lambda(N)\)，并产生公开可计算 endpoint witness \(C_\lambda(N)\)，使

\[
1<\gcd(C_\lambda(N),N)<N?
\]

核心不是预测因子离 \(\sqrt N\) 多远，而是主动制造**单侧乘法通道塌缩**。

## Frozen inputs and scope

1. Worker-visible 输入只能来自 \(N\)、公开 seed、预先承诺的 operator family 与 factor-blind arithmetic。
2. \(p,q\)、factor midpoint/gap、prime rank、成功 operator 标签、任何由真因子直接计算的 bucket 只允许 verifier 使用。
3. 禁止使用平方壳/固定有限周期 residue family 作为主要机制；已接受的 periodic no-go 不得靠扩大周期、更多 bucket 或更多 finite multipliers 重跑。
4. 禁止使用 \(|p-q|\)、Fermat offset、\(|N-M|\) 或 factor-edit L1 作为搜索顺序、训练特征或成功解释。
5. subtraction/difference 只可作为 ring equality/collision 的代数构造；若 extraction 是 \(\gcd(x-y,N)\)，必须说明 \(x-y\) 为什么由 BRC response 自然产生，而不是普通数轴距离。
6. 首批 operator family 必须在查看 verifier labels 前冻结。
7. 若候选机制与 Pollard \(p-1\)、Williams \(p+1\)、ECM 或已知 order/cyclotomic/collision bridge 在可计算同构下等价，标为 `PRIOR_ART_EQUIVALENT`，不得声称新算法。
8. 任何分解收益都计入 operator construction、response evaluation、gcd/extraction、失败重试和预处理总成本。

## Hard target and required outputs

严格分开三层：

**E1 BRIDGE_DETECTION.** 不恢复因子，只判断某个 \(\lambda\) 是否可能使 hidden channels 行为不同；报告 recall、false-positive 与 factor-blindness。

**E2 ENDPOINT_RECOVERY.** 给出完全公开 extraction rule，成功时返回
\[
d=\gcd(C_\lambda(N),N),\quad 1<d<N.
\]
若选择 \(\lambda\) 需要 factor labels，则 E2 自动失败。

**E3 SEARCH_REDUCTION.** 在 held-out semiprimes 上预注册 operator budget，比较 operator evaluations、exact arithmetic/gcd count、bit complexity 或可复核 proxy、success probability；不得只报告命中后的条件成本。

**E4 PRIOR_ART_EQUIVALENCE.** 对所有正结果检查是否只是已知 one-sided order/smoothness/collision 算法的重参数化。

**E5 ADVERSARIAL SPLIT.** 至少包含 balanced、moderate imbalance、strong imbalance、near-twin、repeated/square controls，以及 32/48/64-bit 或同等分层。资源不足可缩小样本，但必须保留 sealed verifier 结构。

**E6 THEORY BOUNDARY.** 若无正算法，尝试证明当前 BRC operator class 的交换对称性、周期性或 support invariance 为什么阻止 endpoint recovery。

Required outputs:

- `research_returns/BRC_FACTOR_BLIND_BRIDGE_ENDPOINT_RECOVERY_RETURN_20260829.md`
- `research_artifacts/BRC_FACTOR_BLIND_BRIDGE_ENDPOINT_RECOVERY/` 下 public corpus、private verifier manifest 摘要与 result summary；
- independent exact checker；
- `LEAKAGE_AUDIT`；
- `PRIOR_ART_EQUIVALENCE_AUDIT`。

## Research value to preserve

这是从“桥是几何概念”到“桥能否实际拆出隐藏 carrier”的第一条 factor-blind 接口。正结果可以把 multiplicative bridge geometry 变成算法；严格负结果则能告诉我们 BRC balanced coupling 仍缺哪一种 asymmetry 或 singularization primitive，从而避免重新回到平方壳距离搜索。

## Success, kill, and return criteria

终态只能取：

- `ENDPOINT_BRIDGE_NEW`：E2 成立且 prior-art audit 未发现等价旧机制；
- `ENDPOINT_BRIDGE_PRIOR_ART_EQUIVALENT`：E2 成立但机制等价于已知分解桥；
- `BRIDGE_DETECTION_ONLY`：E1 有效而 E2 失败；
- `NEGATIVE_BOUNDARY`：当前 frozen BRC family 无法可靠形成 factor-blind endpoint；
- `LEAKAGE_INVALID`：任一关键选择依赖 hidden factors，结果作废。

**KILL**：用真因子挑 operator；把高 train accuracy 当 factorization；只计算成功样本后验成本；把 near-twin 天然易分解性当 BRC 收益；通过 additive-distance feature 绕回已关闭路线。

只有 `ENDPOINT_BRIDGE_NEW` 才允许建议后续竞争性 factorization benchmark；其他结果不得自动声称算法突破。
