<!-- ENTERPRISE_MATH_TASK_V1
{
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "MEDIUM",
  "dependencies": [
    "X6-FAC-AUDIT-20260909"
  ],
  "source_refs": [
    "research_handoffs/X6_FACTOR_LAYER_20260909/START_HERE.md",
    "research_handoffs/X6_FACTOR_LAYER_20260909/source_manifest.json",
    "research_notes/20260906T122500+0800-x6-layer-frobenius-multiresolution-progress.md"
  ],
  "last_progress_ref": null,
  "last_progress_at": null,
  "hard_block": null,
  "claim_lease_minutes": 120,
  "created_by_role": "RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "parent_objective_id": "OBJ-X6-FACTOR-LAYER-20260906",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "X6-FAC",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "parent_task_id": null,
  "successor_gate": null,
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "review_state": "PASS",
    "temporary_overrides": [],
    "policy_digest": "sha256:1f84e78de591605da6106f3f14ffad3cd7fad66aa5bf67e29beb44906b976c8a"
  },
  "task_id": "X6-FAC-OBSERVER-20260909",
  "title": "Search for a non-Frobenius X6/BRC factor observer below the sqrt(p) work barrier",
  "frontier": "All current scalar-layer, prefix-gcd, multiplicative-order, arbitrary-convolution compression, and generic Frobenius multiresolution routes either reduce to classical baselines or retain at least ~p-scale work for balanced semiprimes.",
  "next_action": "Using the handoff's no-go inventory as hard exclusions, formulate one new provenance-preserving X6/BRC factor observer whose declared total work target is o(sqrt(p)); derive its exact observable and falsifier before running large experiments.",
  "evidence_status": "CURRENT_KNOWN_OBSERVERS_CLASSIFIED_GENERIC_SUB_SQRT_P_OBSERVER_NOT_FOUND",
  "tags": [
    "X6",
    "factorization",
    "BRC",
    "observer",
    "complexity",
    "new-direction"
  ],
  "registry_key": "X6-FAC-OBSERVER-20260909",
  "task_lineage": "NEW_DIRECTION"
}
-->

# X6/BRC 新因子观察器：突破当前工作量墙

## 0. Mother question

在不回到 Fibonacci 标量、阶周期、prefix-gcd、随机线性撞因子或现有 Frobenius support 机制的前提下，是否能从 X6 路径 provenance / 因子纤维 / 缺陷子格中定义一个新的可计算观察器，使平衡半素数的总工作量目标真正低于 `sqrt(p)`？

## 1. Frozen inputs and scope

必须先读 `research_handoffs/X6_FACTOR_LAYER_20260909/START_HERE.md` 及审计返回，特别保留已知 no-go：标量层数退化、prefix-gcd 退化为 LCM/阶乘筛、一般安全压缩保留不了位置关系、固定宽 Frobenius 跨尺度失效、大量换基只重现随机 gcd 基线。

BRC 第一行先声明 population、branch identity、observer、未来操作和压缩租约。允许使用 X6 原生路径多重性、primitive/nonprimitive 子层、valuation、碰撞、有限相关张量或新的几何操作，但不能仅把 Pollard rho、Pollard-Strassen、p-1/p+1、QS/NFS 或 Frobenius 方法换名。

## 2. Hard target and required outputs

输出 `research_notes/X6_FAC_OBSERVER_20260909/RETURN.md`。在任何大规模测试之前，先固定：

1. 新观察器的精确定义和输入输出；
2. 为什么现有 no-go 不直接涵盖它；
3. 计算该观察器的位复杂度/模乘/gcd 成本模型；
4. 一条明确的成功机制和至少一条可执行 falsifier；
5. 与 Pollard rho、Pollard-Strassen/product tree 及相关经典方法的对应关系。

随后只对通过理论门槛的候选做有限实验。若观察器需要 `Omega(p)` 个独立机会、需要恢复完整因子比值、或其核心运算已等价于已知因子算法，则立即分类并停止该候选。

## 3. Research value to preserve

这是当前分解路线唯一值得重新打开“通用突破”的门。任务价值不是保证找到更快算法，而是以严格观察器/未来操作 typing 继续排除伪突破，直到找到真正不同的复杂度机制或得到更强的结构性 no-go。

## 4. Success, kill, and return criteria

成功：得到一个未被现有归约覆盖的精确观察器，并证明或有强可复验证据支持总工作量 `o(sqrt(p))` 的机制；或者得到一个新的普遍 no-go，覆盖当前未分类的 X6/BRC 观察器家族。

若所有候选在精确成本核算后回到 `Omega(sqrt(p))` 或已知算法，则以分类表和最小证明返回，不通过扩大随机试验延长任务。
