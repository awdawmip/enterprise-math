<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-P000-PHILOSOPHY-FIRST-HIDDEN-KERNEL-MODEL-SIGNATURE",
  "title": "哲学先行 Q15：Nonsplit Hidden-Kernel 的最小 Native 模型签名",
  "kind": "RESEARCH",
  "owner": "research/p000-phil-q15-hidden-kernel-model-signature",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "Q10 derives carrier S4 and lift quantifiers from a minimal primitive signature but intentionally leaves the nonsplit GL(2,3)-type hidden-kernel benchmark outside that universe. Find the smallest typed primitive-signature extension that internalizes a semantically real nonsplit kernel without inserting the desired extension by hand.",
  "next_action": "Start from the accepted Q10 primitive signature and add one candidate hidden sort/relation at a time; recompute primitive automorphism groups and carrier readout, seeking an inside model whose derived readout is surjective nonsplit, with deletion certificates for every added field.",
  "dependencies": [
    "RR-3C5E7A91D0B24F6882A1",
    "DR-AF3026BF9546DE05BE36",
    "RR-FD229649452476EB1CFB"
  ],
  "source_refs": [
    "research_returns/P000_PHILOSOPHY_FIRST_NATIVE_MODEL_GROUPOID_UNIVERSALITY_RETURN_20260830.md",
    "research_returns/P000_PHILOSOPHY_FIRST_RESIDUE_HOLONOMY_COUPLING_RETURN_20260830.md",
    "driver_reviews/P000_PHILOSOPHY_FIRST_Q9_Q12_DRIVER_REVIEW_20260830.md"
  ],
  "evidence_status": "DRIVER_ACCEPTED_Q10_MINIMAL_SIGNATURE_WITH_EXPLICIT_NONSPLIT_OUTSIDE_BOUNDARY",
  "last_progress_ref": null,
  "last_progress_at": null,
  "hard_block": null,
  "tags": [
    "P000",
    "philosophy-first",
    "hidden-kernel",
    "nonsplit",
    "primitive-signature",
    "minimality",
    "automorphism"
  ],
  "claim_lease_minutes": 240,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-P000-PHILOSOPHY-FIRST-HIDDEN-KERNEL-MODEL-SIGNATURE",
  "parent_objective_id": "OBJ-P000-ENTERPRISE-6D-ROTATION-TOMOGRAPHY",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "origin_kind": "DRIVER_ROADMAP",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-P000-PHILOSOPHY-FIRST-NATIVE-MODEL-GROUPOID-UNIVERSALITY",
  "successor_gate": {
    "new_information_gap": "Q10's minimal signature classifies lift/no-lift/noncanonical regimes but deliberately excludes a semantically internal nonsplit hidden-kernel model. The algebraic GL(2,3) benchmark therefore remains outside the native model universe.",
    "why_parent_result_does_not_close_it": "Q10 explicitly lists Hidden-sort expansion as unresolved and does not derive a nonsplit extension from primitive automorphisms.",
    "discriminating_outcomes": [
      "MINIMAL_NONSPLIT_HIDDEN_KERNEL_SIGNATURE_FOUND",
      "NONSPLIT_INTERNALIZATION_REQUIRES_NONMINIMAL_OR_CIRCULAR_DATA",
      "DECLARED_Q10_PRIMITIVES_FORBID_NONSPLIT_INTERNALIZATION"
    ],
    "kill_condition": "If every candidate hidden field either fails to produce a derived nonsplit readout or simply encodes the target extension/section in disguise, kill the proposed internalization and return the exact circularity/no-go certificate.",
    "alternative_route_or_free_exploration_considered": "Leaving nonsplit extensions as external comparison algebra is a valid closure option and remains the default if no noncircular primitive signature is found. A general nonabelian-cohomology route is deliberately deferred because Q12 does not force it.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "Q10 is terminal for its minimal signature and should remain so. A separate task makes every additional hidden field pay an explicit semantic/minimality cost and allows the correct answer to be that no extension is justified."
  },
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:10ec4f937324069d7af8d77a52c244389ac4cccd957e3685c14c6fe8b8fd367c",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# 哲学先行 Q15：Nonsplit Hidden-Kernel 的最小 Native 模型签名

Status: `READY / P1 / HIDDEN-KERNEL-SIGNATURE`

## Mother question

Q10 已经把 carrier target 与 `rho_M` 从 primitive signature 推出来，但它有意没有把 `GL(2,3)` 型 nonsplit hidden-kernel benchmark 放进模型宇宙。

现在的问题不是“怎样把 GL(2,3) 塞进去”，而是：**什么最小 native relational data 会自然地产生一个 surjective but nonsplit 的 readout？** 如果答案只能通过把目标 extension 本身写成 primitive 才得到，那么这个方向必须被杀死。

## Frozen inputs and scope

以 Q10 已接受的 typed sorts / relations 为基底，保持 carrier/Cell sort 分离。任何 Hidden sort、orientation、sign fiber、incidence 或 relation-phase 结构都必须逐项声明其 native 语义。

`GL(2,3)`、central `C2` extension 与 Q12 只作为反例/回归 benchmark；不得把矩阵群名称、group law 或目标 quotient map 直接当 primitive 输入，然后宣称“导出了”它。

## Hard target and required outputs

Hard target: `P000_HIDDEN_KERNEL_NONSPLIT_MODEL_SIGNATURE_MINIMALITY_CLASSIFIED`

1. 给出至少一个候选 typed Hidden extension of Q10 signature，所有 `Aut_prim(M)` 与 carrier readout 必须由 primitive-preserving automorphisms 派生。
2. 寻找内部 nonsplit witness：`rho_M` surjective、kernel 非平凡、无 homomorphic section；或者证明当前可接受候选全部失败。
3. 对每个新增 primitive field 做 deletion audit：删除后 nonsplit 性是否消失、语义是否塌缩、或出现伪 section。
4. 同一签名内至少保留 Q10 的 split / no-lift regression，以防为了制造 nonsplit 而改变了问题类别。
5. 检查 Q12 residue/holonomy 是否成为该模型的真实 derived observable，而不是另加标签。
6. 给出 circularity test：任何直接编码目标 group extension、section obstruction 或 desired residue 的字段必须判失败。
7. 输出确定性 checker 与 exact finite certificate；不把 benchmark 提升为 bare P000 truth。

## Research value to preserve

这一步决定“hidden kernel”能不能从进取数论的关系本体内部生长出来。如果成功，Gen13/Q5/Q12 的外部 extension benchmark 将第一次获得 native model semantics；如果失败，我们就得到一条非常有价值的 no-go：现有 P000 语言不足以自然地产生 nonsplit hidden state，不能靠换名字伪装突破。

## Success, kill, and return criteria

有效终态：

- `MINIMAL_NONSPLIT_HIDDEN_KERNEL_SIGNATURE_FOUND`；
- `NONSPLIT_INTERNALIZATION_REQUIRES_NONMINIMAL_OR_CIRCULAR_DATA`；
- `DECLARED_Q10_PRIMITIVES_FORBID_NONSPLIT_INTERNALIZATION`。

任何成功都必须同时给出非循环性与 deletion minimality；否则应按 kill/negative 终态返回。
