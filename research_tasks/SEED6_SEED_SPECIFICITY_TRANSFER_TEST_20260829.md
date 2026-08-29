<!-- ENTERPRISE_MATH_TASK_V1
{
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "parent_objective_id": "OBJ-SEED6-MULTIPLICATIVE-GROWTH-GEOMETRY",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "NEW_DIRECTION",
  "parent_task_id": null,
  "successor_gate": null,
  "claim_lease_minutes": 240,
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:10ec4f937324069d7af8d77a52c244389ac4cccd957e3685c14c6fe8b8fd367c",
    "review_state": "PASS",
    "temporary_overrides": []
  },
  "task_id": "RS-SEED6-SEED-SPECIFICITY-TRANSFER-TEST",
  "title": "6 是特殊种子还是首个通例：双载体乘法生长的迁移检验",
  "priority": "P2",
  "leverage": "MEDIUM",
  "frontier": "Seed 6 is the first nontrivial product of two distinct primes and generates the observed triangle/rectangle/pairing patterns. Test only after defining the seed-6 invariants whether those structures depend essentially on 2 and 3 or are generic for a coprime two-carrier seed ab.",
  "next_action": "Take the structural signatures proposed by the seed-6 tasks as test objects, compare them first against seeds 10,14,15,21,22, then against general coprime a,b and non-coprime controls, and classify each signature as 6-specific, prime-pair generic, coprime-pair generic, or tautological.",
  "dependencies": [],
  "source_refs": [],
  "evidence_status": "DIRECT_USER_DIRECTION / SEED6_REFERENCE_FIRST / TRANSFER_CONTROL / NO_FACTORIZATION_OBJECTIVE",
  "tags": ["seed6", "seed-specificity", "generalization", "coprime-seed", "transfer-test", "control"],
  "registry_key": "RS-SEED6-SEED-SPECIFICITY-TRANSFER-TEST",
  "identity_lane": "S6X"
}
-->

# 6 是特殊种子还是首个通例：双载体乘法生长的迁移检验

## Mother question

Seed-6 之所以自然，是因为 \(6=2\cdot3\) 是最小的两个不同素数之积。但局部三角 \(\{6,2r,3r\}\) 和四原子三配对恒等式看起来又可能只是一般 \(ab,ar,br\) 或四原子 perfect matching 的实例。

本任务不提前一般化，而是在 Seed-6 结构被明确定义后检验：6 真正特殊在哪里？哪些规律只是一般双载体种子的首个例子？

## Frozen inputs and scope

1. 6 始终是 reference seed，不允许一开始就把它抹成抽象 \(ab\)。
2. 第一控制组：\(10=2\cdot5,14=2\cdot7,15=3\cdot5,21=3\cdot7,22=2\cdot11\)。
3. 第二控制组为互素 \(a,b>1\)；第三控制组允许 \(\gcd(a,b)>1\)。
4. 只迁移已经在 Seed-6 中精确定义的结构签名，不允许为了得到“一般定理”临时改变定义。
5. 禁止因子恢复、分解性能与加法距离。
6. 标准四原子 matching 恒等式若完全解释某规律，应归类为 generic/tautological，而不是 Seed-6 特性。

## Hard target and required outputs

Hard target: `SEED6_SPECIAL_VS_GENERIC_STRUCTURE_CLASSIFIED`

A. 建立 transfer table，对每个来自 Seed-6 的候选结构标记 `SEED6_SPECIFIC / PRIME_PAIR_GENERIC / COPRIME_PAIR_GENERIC / ARBITRARY_PAIR_GENERIC / TAUTOLOGICAL / FAILS_UNDER_TRANSFER`。

B. 对一般 seed \(s=ab\) 定义对应列 \(C_r^{a,b}=(ar,br)\) 和 pairing states，并明确哪些公式无需 \(\gcd(a,b)=1\)。

C. 比较 prime seed 与 composite coprime seed，例如 6 对 \(35=5\cdot7\)、10、15，看 carrier-incidence/aut symmetry 是否发生变化。

D. 比较 non-coprime seed，如 \(12=3\cdot4\) 或 \(18=3\cdot6\)，确定共享 carrier 会破坏哪些结构。

E. 特别检查 2 和 3 的最小性、唯一偶素数、相邻素数等性质是否真的进入桥胞结构；若没有进入，明确说明 6 只是在数值顺序上最先出现。

F. 给出至少 100 个 seed 的 exact census，并为每个候选 invariant 寻找最小反例。

G. 最终回答：未来研究应继续以 6 为 canonical seed、以 6 为教学坐标但数学上一般化，还是保留多个 seed type。

## Research value to preserve

这条控制任务防止两种相反错误：一是把完全一般的 matching 恒等式误认为 6 的新规律；二是过早抽象化，丢掉 6 因最小性、素性或 carrier asymmetry 可能产生的真实特殊结构。

## Success, kill, and return criteria

Success：每个 Seed-6 核心 invariant 都得到迁移分类；至少找到一个明确的 6-specific 机制，或证明当前观察全部属于更一般 seed 类型；给出最小反例和 exact transfer map。

Kill：未先定义 Seed-6 invariant 就直接写一般 \(ab\) 理论；因为公式可替换字母就声称完全一般；因为 6 最小就声称它几何特殊；转向分解问题。

Return：task-terminal；可返回 `SEED6_CANONICAL_SPECIAL / SEED6_FIRST_GENERIC_EXAMPLE / MIXED_SPECIFICITY / TRANSFER_MODEL_DEPENDENT`。
