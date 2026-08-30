<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-P000-PHILOSOPHY-FIRST-HIDDEN-COUPLING-TORSOR-HOLONOMY",
  "title": "哲学先行 Q21：Hidden Coupling 选择丛的 transport 与 holonomy",
  "kind": "RESEARCH",
  "owner": "research/p000-phil-q21-hidden-coupling-torsor-holonomy",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "Q18 proves that the full Q15 hidden-carrier bridge is a fixed-point-free 24-state relative-frame orbit and that a distinct six-state choice orbit is the minimum full-carrier nonsplit cost in the frozen finite witness. Determine whether actual primitive-preserving changes between admissible local models induce nontrivial transport on these choice orbits, or whether action-groupoid language adds no invariant beyond the static Q18 stabilizer data.",
  "next_action": "Define objects and arrows solely from Q18's actual bridge-free primitive automorphisms and explicitly legal local model changes; construct the 24-state and six-state action groupoids, search the smallest closed change loop, and compute gauge-invariant transport before comparing any loop residue with Q12.",
  "dependencies": [
    "RR-5137B2C5D070E4CEA95E"
  ],
  "source_refs": [
    "research_returns/P000_PHILOSOPHY_FIRST_HIDDEN_CARRIER_BRIDGE_CANONICALITY_RETURN_20260831.md"
  ],
  "evidence_status": "Q18_CONTROLLING_RESULT_SELECTED_AFTER_PARALLEL_SYNTHESIS_FOR_SAME_REVIEW_FOLLOWUP",
  "last_progress_ref": null,
  "last_progress_at": null,
  "hard_block": null,
  "tags": [
    "P000",
    "philosophy-first",
    "hidden-coupling",
    "torsor",
    "action-groupoid",
    "transport",
    "holonomy"
  ],
  "claim_lease_minutes": 240,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-P000-PHILOSOPHY-FIRST-HIDDEN-COUPLING-TORSOR-HOLONOMY",
  "parent_objective_id": "OBJ-P000-ENTERPRISE-6D-ROTATION-TOMOGRAPHY",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "origin_kind": "DRIVER_ROADMAP",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-P000-PHILOSOPHY-FIRST-HIDDEN-CARRIER-BRIDGE-CANONICALITY",
  "successor_gate": {
    "new_information_gap": "Q18 establishes genuine noncanonical choice orbits and stabilizer data, but it does not determine whether legal changes of local primitive presentations produce path-dependent transport or any new gauge-invariant loop datum.",
    "why_parent_result_does_not_close_it": "Q18 is static: it classifies choice orbits, splitness and information cost at one finite witness. It does not construct a path category of model changes or compute holonomy.",
    "discriminating_outcomes": [
      "NONTRIVIAL_COUPLING_CHOICE_HOLONOMY_FOUND",
      "TORSOR_TRANSPORT_REDUCES_TO_STATIC_Q18_DATA",
      "RESIDUE_AND_COUPLING_HOLONOMY_INDEPENDENT_OR_CONDITIONALLY_COUPLED"
    ],
    "kill_condition": "If every closed legal change loop acts trivially modulo the already-known Q18 stabilizer/kernel data, or if the proposed arrows require arbitrary non-primitive identifications, kill the transport upgrade and retain Q18's static finite classification.",
    "alternative_route_or_free_exploration_considered": "Stopping at the static torsor, immediately importing bundle/sheaf/stack terminology, and identifying the choice orbit with Q12 relation residue were considered. The first may miss genuine path information; the latter two assume precisely the structure this task must test.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "Q18 supplies the lower-level failure witness required by the abstraction gate: no natural fixed choice exists. Q21 asks the next falsifiable question—whether morphisms and loops create new invariant content—while retaining an explicit kill path if they do not."
  },
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:10ec4f937324069d7af8d77a52c244389ac4cccd957e3685c14c6fe8b8fd367c",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# 哲学先行 Q21：Hidden Coupling 选择丛的 transport 与 holonomy

Status: `READY / P1 / TORSOR-TRANSPORT-TEST`

## Mother question

Q18 已经证明“没有自然 bridge”并不是语言游戏：full bridge 有 24 个等价选择，另一个 full-carrier nonsplit 构造有 6 个选择状态。

但**没有自然固定点并不自动意味着存在有意义的 holonomy**。下一步必须问：真实的 primitive-preserving 模型变化沿路径传播这些选择时，绕一圈是否留下新的、不可消去的状态？如果没有，就不应继续升级抽象语言。

## Frozen inputs and scope

只消费 Q18 的 controlling finite result：bridge-free hidden automorphism action、carrier action、24-state full-bridge orbit、6-state `BlockOrientationBridge` orbit及其 stabilizers。

对象与 morphism 必须来自实际 primitive-preserving automorphisms、明确合法的局部 presentation/model changes 或它们的组合。不得预先声明 bundle、sheaf、stack、connection 或 holonomy；这些词只能在有限 transport 已经被构造后作为经典解释。

## Hard target and required outputs

Hard target: `P000_HIDDEN_COUPLING_TORSOR_TRANSPORT_OR_NO_NEW_INVARIANT_CLASSIFIED`

1. 明确定义 24-state 与 6-state choice space 上由实际 primitive morphisms 诱导的 action groupoid；若不能自然定义，直接返回 no-go。
2. 构造最小非平凡闭合 change loop，计算 choice transport，并对 basepoint/frame gauge 取商。
3. 判断 loop transport 是否产生超出 Q18 静态 orbit/stabilizer/kernel 的新 invariant；给出非平凡例或精确约化定理。
4. 若得到非平凡 holonomy，再与 Q12 residue/holonomy 做双向反模型测试：same coupling-holonomy/different residue 与反方向；只有反模型失败后才允许建立耦合定理。
5. 比较 24-state 与 6-state 模型的 transport 是否本质不同，避免把 choice cardinality 当成动力学。
6. 通过最低充分抽象门槛：若 groupoid 只重述静态群作用且无新 loop 信息，必须 kill continuation。
7. 输出确定性 checker 与有限证书；不得把 Q18 certificate group names 提升为 bare P000 ontology。

## Research value to preserve

这一步检验“非典范选择”是否真的产生几何，而不只是一个静态对称性事实。

若出现新的 gauge-invariant loop state，hidden coupling 线第一次拥有内部 transport 几何；若没有，负结果同样重要，因为它阻止我们从 torsor 直接滑向高阶几何词汇。

## Success, kill, and return criteria

有效终态：

- `NONTRIVIAL_COUPLING_CHOICE_HOLONOMY_FOUND`;
- `TORSOR_TRANSPORT_REDUCES_TO_STATIC_Q18_DATA`;
- `RESIDUE_AND_COUPLING_HOLONOMY_INDEPENDENT_OR_CONDITIONALLY_COUPLED`.

没有新的 loop invariant 就应冻结在 Q18/Q21 的最低层级，不得以“可能存在更高结构”为理由继续升级。
