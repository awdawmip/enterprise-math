<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-MULTIPLICATIVE-BRIDGE-PRIOR-ART-TAXONOMY",
  "title": "乘法桥先验去重：经典分解中的单侧塌缩、零因子与通道分裂",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "Before treating BRC or any new multiplicative bridge as novel, classify how established factorization methods already create a nontrivial factor by making a factor-blind process behave differently in hidden CRT or algebraic channels. The open problem is a mechanism-level taxonomy, not another list of algorithms.",
  "next_action": "Build a source-backed mechanism table for classical bridge families: ambient algebraic carrier, hidden factor-dependent invariant, public factor-blind action, one-sided collapse/collision event, extraction map, success regime and asymptotic/heuristic cost. Then derive a novelty guard for any future BRC bridge claim.",
  "dependencies": [],
  "source_refs": ["driver_reviews/CBRC_F3R2_SURVIVOR_MEMBERSHIP_PREDICATE_DRIVER_REVIEW_20260823.md@main"],
  "evidence_status": "DIRECT_USER_DIRECTION / PRIOR_ART_DEDUP_REQUIRED / BRIDGE_LANGUAGE_OPEN",
  "hard_block": null,
  "tags": ["prior-art", "factorization", "Pollard-p-1", "Williams-p-plus-1", "ECM", "CRT", "zero-divisor", "order", "bridge", "novelty"],
  "claim_lease_minutes": 240,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-MULTIPLICATIVE-BRIDGE-PRIOR-ART-TAXONOMY",
  "parent_objective_id": "OBJ-MULTIPLICATIVE-BRIDGE-GEOMETRY",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "MBG-P0",
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

# 乘法桥先验去重：经典分解中的单侧塌缩、零因子与通道分裂

Status: `READY / P1 / HIGH-LEVERAGE / PRIOR-ART-BOUNDARY`

## Mother question

许多分解方法都可以被重述为：对未知 \(N=pq\) 施加同一个 factor-blind 动力学，使其在隐藏的 \(p\)-channel 与 \(q\)-channel 中出现不同的 order、smoothness、collision、singularity 或 collapse，随后通过 extraction map 得到非平凡因子。在这种语言下，BRC “桥”究竟可能新增什么？

## Frozen inputs and scope

1. 重点不是算法教程，而是机制分解：ambient algebraic carrier、hidden factor-dependent invariant、public factor-blind action、one-sided collapse/collision/singularity、endpoint extraction、成功条件与成本。
2. 至少覆盖 Pollard \(p-1\)、Williams \(p+1\)、ECM；并调查与本桥语言最相关的 order/cyclotomic、collision/gcd、ring zero-divisor 路线。
3. 若出现 \(\gcd(x-y,N)\)，必须区分减法作为 residue equality/collision 的代数检测器与减法作为普通数轴距离。本任务只允许前者作为 bridge mechanism。
4. 使用权威论文、专著或一手算法来源；社区解释只能作为导航。
5. 不得根据“BRC 名称不同”推定新颖性。
6. 不重新审核当前 BRC/CBRC 的数学正确性，只做映射与去重边界。

## Hard target and required outputs

**P0 Mechanism taxonomy.** 构建至少六维机制表：
\[
(\text{carrier},\text{hidden invariant},\text{public action},\text{collapse},\text{extraction},\text{cost regime}).
\]

**P1 CRT-channel formulation.** 对至少三类经典方法给出“同一 public action 在不同 prime channels 中行为不同”的精确重述，并标注等价、启发式或附加假设。

**P2 Bridge-equivalence criterion.** 若 carrier、collapse invariant 与 extraction map 在可计算同构下等价，则新候选不得声称新 bridge family。

**P3 Novelty gaps.** 列出经典方法没有覆盖、BRC 可能覆盖的最小空白，例如 balanced two-channel conservation、operator-survivor existence without endpoint、rank-two coupling not reducible to known group-order smoothness、genuinely different endpoint recovery law；每项必须给出被反证为旧思想的检查。

**P4 Literature ledger.** 记录来源、使用范围和不能导出的结论，避免把启发式复杂度误写成定理。

Required outputs:

- `research_returns/MULTIPLICATIVE_BRIDGE_PRIOR_ART_TAXONOMY_RETURN_20260829.md`
- `research_artifacts/MULTIPLICATIVE_BRIDGE_PRIOR_ART_TAXONOMY/mechanism_ledger.json`
- 一个可复用的 `BRC_NOVELTY_GUARD`。

## Research value to preserve

如果“桥”只是统一语言，它仍有理论价值；但统一语言和新算法必须分开。这个任务给后续 BRC exploration 设置硬 prior-art 边界，使真正的新结果必须来自新的 carrier/collapse/extraction 组合，而不是术语替换。

## Success, kill, and return criteria

**SUCCESS**：形成 source-backed mechanism taxonomy，并能对任意 BRC 候选给出“已知等价 / 部分重合 / 真空白”判据。

**PARTIAL**：主要经典家族完成分类，但某些 BRC 对象缺少足够语义；列出缺失定义。

**NEGATIVE_BOUNDARY**：若所有当前可表述 BRC bridge 机制都落入成熟 prior art，直接冻结，不为追求创新改词。

**KILL**：只列算法名不比较机制；用二手摘要支撑 novelty；把 \(\gcd(x-y,N)\) 的减法误解成加法几何；把统一重述自动算作新数学。

Return 必须给出后续 BRC 任务可合法声称的新颖性上限。
