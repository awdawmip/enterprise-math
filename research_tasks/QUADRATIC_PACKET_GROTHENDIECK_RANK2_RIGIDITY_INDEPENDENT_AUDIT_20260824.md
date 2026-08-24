<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-QUADRATIC-PACKET-GROTHENDIECK-RANK2-RIGIDITY-INDEPENDENT-AUDIT",
  "title": "Quadratic Packet Grothendieck Rank-Two Rigidity — Independent Audit",
  "kind": "INDEPENDENT_AUDIT",
  "owner": "research/quadratic-packet-rank2-rigidity-independent-audit",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "ONE_PRIME_RANK_TWO_RIGIDITY_INDEPENDENTLY_PROVED_OR_COUNTEREXAMPLED_WITH_PREMISE_MINIMALITY_AUDITED",
  "next_action": "Using only the frozen blind-forward audit packet, independently prove, refute, or minimally narrow QP-R2; freeze the raw verdict before opening the withheld source proof; then perform source comparison, premise-independence pressure, and exact claim-strength classification.",
  "dependencies": [
    "research_inputs/QUADRATIC_PACKET_GROTHENDIECK_RANK2_RIGIDITY_AUDIT_PACKET_20260824.md@blob:f2f64fb25419c592031ca01f467a66ac9fc61676",
    "research_inputs/QUADRATIC_PACKET_GROTHENDIECK_RANK2_RIGIDITY_WITHHELD_SOURCE_PROOF_20260824.md@blob:2c6b53433353995ed54f70758aa66f156e4ea6c0"
  ],
  "source_refs": [
    "research_inputs/QUADRATIC_PACKET_GROTHENDIECK_RANK2_RIGIDITY_AUDIT_PACKET_20260824.md#blob=f2f64fb25419c592031ca01f467a66ac9fc61676",
    "research_inputs/QUADRATIC_PACKET_GROTHENDIECK_RANK2_RIGIDITY_WITHHELD_SOURCE_PROOF_20260824.md#blob=2c6b53433353995ed54f70758aa66f156e4ea6c0"
  ],
  "evidence_status": "INDEPENDENT_AUDIT_COMMISSIONED_SOURCE_PROOF_WITHHELD_UNTIL_RAW_FREEZE",
  "last_progress_ref": "research_inputs/QUADRATIC_PACKET_GROTHENDIECK_RANK2_RIGIDITY_AUDIT_PACKET_20260824.md@blob:f2f64fb25419c592031ca01f467a66ac9fc61676",
  "last_progress_at": "2026-08-24T13:42:00+08:00",
  "hard_block": null,
  "tags": [
    "quadratic-packet",
    "Grothendieck",
    "Cartier",
    "dual-number",
    "rank-two-rigidity",
    "independent-audit",
    "counterexample-first",
    "premise-minimality",
    "source-withheld"
  ],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "DRIVER_APPROVED",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "QPR2A",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "QUADRATIC-PACKET-GROTHENDIECK-ARITHMETIC-FRONTIER",
  "successor_gate": {
    "new_information_gap": "The one-prime rank-two rigidity claim was generated and pressure-tested inside the same free-research context that selected its proof strategy. Its exact statement strength, hidden-assumption risk, and premise minimality have not yet been independently validated in a context that has not seen the source proof.",
    "why_parent_result_does_not_close_it": "Same-context derivation, self-critique, examples, and Foundation-cost classification are discovery evidence rather than independent validation. In particular, possible hidden uses of e mod ell being nonzero, phase-neutral index, cyclic quotient reduction, or a stronger notion of one-clock associateness must be checked without importing the source argument.",
    "discriminating_outcomes": [
      "QP-R2 is independently proved at exactly the stated hypotheses and the source proof survives comparison",
      "an explicit rank greater than two counterexample satisfies every stated hypothesis and refutes QP-R2",
      "QP-R2 is false as written but becomes true after one or more exact additional hypotheses are isolated",
      "QP-R2 is true but one or more stated premises are redundant and a strictly stronger minimal theorem is established"
    ],
    "kill_condition": "If an explicit counterexample satisfies every stated premise, the positive claim is killed immediately and the task returns the smallest exact failure certificate. If a proof requires an unstated premise that cannot be derived from the packet assumptions, do not silently import it; narrow the theorem and return the missing condition.",
    "alternative_route_or_free_exploration_considered": "Further same-context expansion by the originating free researcher was rejected because it would reuse the already exposed proof anchors. Immediate Foundation intake was also rejected because the premises are not canonical Foundation consequences. Independent proof/counterexample audit is the information-gaining route that can distinguish theorem validity from attractive interpretation.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "The parent route has reached a semantic frontier where additional same-context work no longer supplies independent evidence. A separate source-withheld audit task creates a falsifiable validation boundary and can close, refute, or narrow the theorem before any later semantic intake decision."
  },
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:9c1f03a5086432f83d1a3821893be5589124293bc5be5b14d4b7e196220271c7",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# Quadratic Packet Grothendieck Rank-Two Rigidity — Independent Audit

Status: `READY / DRIVER_APPROVED / BLIND-FORWARD INDEPENDENT AUDIT`

Task-ID:

`RS-QUADRATIC-PACKET-GROTHENDIECK-RANK2-RIGIDITY-INDEPENDENT-AUDIT`

Owner branch:

`research/quadratic-packet-rank2-rigidity-independent-audit`

Hard target:

`ONE_PRIME_RANK_TWO_RIGIDITY_INDEPENDENTLY_PROVED_OR_COUNTEREXAMPLED_WITH_PREMISE_MINIMALITY_AUDITED`

## 0. Audit object

The only theorem under audit is QP-R2 as frozen in:

`research_inputs/QUADRATIC_PACKET_GROTHENDIECK_RANK2_RIGIDITY_AUDIT_PACKET_20260824.md`

Do not strengthen, weaken, or reinterpret its hypotheses before testing the literal statement.

The originating result is currently only a structural/interpretive theorem candidate. This task does not assume that the theorem is true and does not assume that its premises are Enterprise Foundation primitives.

## 1. Blind-forward phase

Before the raw verdict is frozen, the route-specific source whitelist consists only of the frozen audit packet above.

Do **not** read the originating proof, originating route journals, or the withheld comparison source during this phase.

In particular, do not read:

`research_inputs/QUADRATIC_PACKET_GROTHENDIECK_RANK2_RIGIDITY_WITHHELD_SOURCE_PROOF_20260824.md`

until the independent raw verdict has been frozen.

The blind-forward phase ends only when the auditor has written a complete proof, counterexample, or exact narrowing with all actually used premises visible.

## 2. Required independent work

Settle the exact main claim and all audit obligations A–E from the frozen packet.

The work must include:

1. a complete derivation or a complete counterexample at exact statement strength;
2. explicit pressure on `e in ell A`, arbitrary-unit associateness, and nilpotence index greater than two;
3. a positive rank-two model if the theorem is non-vacuous;
4. a premise-minimality table for nilpotence, self-composition closure, and cyclic primitive quotient;
5. a statement of every lemma not proved directly in the return;
6. a clear separation between conditional algebraic rigidity and any later semantic/Foundation interpretation.

Small-model computation is allowed as a counterexample search aid or sanity check, but a finite census is not a proof of the general positive theorem.

## 3. Mandatory raw freeze

Before source comparison, freeze:

`research_returns/QUADRATIC_PACKET_GROTHENDIECK_RANK2_RIGIDITY_INDEPENDENT_AUDIT_RAW_20260824.md`

The raw file must state one of:

- `PROVED_AT_EXACT_STRENGTH`;
- `REFUTED_BY_EXPLICIT_COUNTEREXAMPLE`;
- `NARROWED_WITH_EXACT_MISSING_HYPOTHESIS`.

It must include enough mathematics to reconstruct the verdict without any source-proof access.

After this freeze, preserve the raw argument. Later corrections discovered during source comparison must be recorded as corrections rather than silently rewriting the independent provenance.

## 4. Post-freeze source comparison

After the raw freeze, open the withheld source proof and compare it against the independent argument.

The comparison must identify:

- every essential lemma shared by both arguments;
- any source-only or audit-only hypothesis;
- any hidden use of nonvanishing modulo `ell`;
- whether the phase-neutral index is derived or assumed;
- whether cyclicity is used at exactly the required strength;
- whether arbitrary-unit associateness causes any gap;
- whether commutativity can be weakened without changing the result;
- whether the source-side premise-independence examples are correct.

If the source proof contains a gap that the independent proof avoids, state the gap explicitly. If the independent proof fails after source comparison, preserve the failure record and issue a corrected verdict.

## 5. Outcome matrix

### PASS-A — exact proof

Return PASS-A only if QP-R2 is proved from exactly the frozen hypotheses and the proof survives source comparison.

### PASS-B — valid narrowing

Return PASS-B if the original statement is false or unproved but a minimal corrected theorem is established, together with a counterexample showing why the correction is necessary.

### KILL — refutation

Return KILL if a rank-greater-than-two counterexample satisfies every frozen premise.

### NO-GO — unresolved

Return NO-GO if neither proof nor refutation can be completed. The return must isolate the smallest unresolved lemma and must not upgrade the candidate by plausibility.

## 6. Scope exclusions

Do not reopen the closed QRF-R1 strict-replacement route.

Do not treat survival of QP-R2 as automatic permission to modify Foundation semantics.

Do not restart factoring/Shor complexity exploration in this task.

Do not broaden the assignment into a general survey of Grothendieck, Cartier, deformation, or nilpotent algebra unless a specific theorem step requires it.

## 7. Final return

Freeze the final audit at:

`research_returns/QUADRATIC_PACKET_GROTHENDIECK_RANK2_RIGIDITY_INDEPENDENT_AUDIT_RETURN_20260824.md`

The return must contain:

- raw verdict reference;
- final theorem statement actually verified;
- proof or counterexample synopsis;
- premise-minimality table;
- source-comparison verdict;
- Foundation-scope classification;
- exact recommendation: `REJECT`, `PARK`, `INDEPENDENTLY_VERIFIED_L2`, or `FOUNDATION_INTAKE_WORTHY_BUT_NOT_YET_ADMITTED`.

Stop after freezing the audit return. Any Foundation intake or formalization is a separate control-plane decision.
