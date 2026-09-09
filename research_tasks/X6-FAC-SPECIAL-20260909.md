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
  "task_id": "X6-FAC-SPECIAL-20260909",
  "title": "X6 multiresolution special semiprime family search",
  "frontier": "Generic balanced semiprime factorization is blocked at the current frontier by an empirical R~p scale wall, while the one-fine-layer multiresolution observer remains potentially useful when factor gaps or algebraic dependencies permit much smaller cyclic width.",
  "next_action": "After consuming the audit handoff, define explicit special semiprime families with factor relations that can force or plausibly yield R=o(p), then derive the required cyclic width and compare equal-cost performance with the classical Frobenius and near-factor baselines.",
  "evidence_status": "GENERIC_ROUTE_CLOSED_AT_CURRENT_FRONTIER_SPECIAL_DEPENDENCY_FAMILIES_OPEN",
  "tags": [
    "X6",
    "factorization",
    "special-family",
    "Frobenius",
    "multiresolution",
    "BRC"
  ],
  "registry_key": "X6-FAC-SPECIAL-20260909",
  "task_lineage": "NEW_DIRECTION"
}
-->

# X6 多尺度观察器：特殊半素数族

## 0. Mother question

是否存在自然且非平凡的半素数族 `N=pq`，其因子间距、同余关系或其他可公开描述的代数依赖，使一次 X6/Frobenius 细层的必要宽度满足 `R=o(p)`，从而让 divisor/cyclotomic 多尺度复用产生相对经典方法的真实 Pareto 优势？

## 1. Frozen inputs and scope

先读取 `research_handoffs/X6_FACTOR_LAYER_20260909/START_HERE.md`，并消费审计任务的可复现边界。当前一般平衡半素数路线视为关闭基线：不能以调大 `R`、增加大量随机线性组合或重复 gcd 尝试重新宣称通用突破。

候选族必须能仅从公开的族定义或 `N` 可获得的先验条件描述，不能在查询时偷用 `p`、`q`。优先考虑具有明确小 gap、固定低次数多项式关系、受限同余类、特殊递推来源或其他使 Frobenius 相对方向受约束的族。必须与 Agrawal–Saxena–Srivastava 2016 类方法、Fermat/近因子法和 Pollard rho 做同成本比较。

## 2. Hard target and required outputs

输出 `research_notes/X6_FAC_SPECIAL_20260909/RETURN.md` 与可运行实验/证明材料。至少研究三个彼此不同的候选族，并对每个族给出：

1. 因子关系的精确定义及可检测/可承诺的输入条件；
2. 对所需层宽 `R` 的证明上界、条件上界或可证伪猜想；
3. 一次细层复用到 divisor 层和 cyclotomic 分量后的总成本；
4. 与最强相关经典基线在等成功率、等算术操作或等墙钟预算下的 Pareto 比较；
5. 该族是否只是 Fermat、小 gap Frobenius、Pollard p-1 / Lucas 阶方法的重命名。

## 3. Research value to preserve

当前一般路线的负结论并不排除有结构输入。若能找到 `R=o(p)` 的自然族，多尺度复用可从“通用分解失败路线”转成明确的特殊族算法；若所有候选族都坍缩到已有方法，也会形成可复用的分类 no-go，阻止重复研究。

## 4. Success, kill, and return criteria

成功至少满足其一：给出一个非平凡族及严格/有力证据表明 `R=o(p)`，并在公平基线上显示多尺度复用的独立优势；或给出一个覆盖广泛候选族的结构性归约，证明它们都落回现有方法。

若三个候选族均需要 `R=Theta(p)`、或优势完全由已知近因子/阶平滑机制解释，则冻结本任务为负结果并返回，不继续扩大经验参数搜索。
