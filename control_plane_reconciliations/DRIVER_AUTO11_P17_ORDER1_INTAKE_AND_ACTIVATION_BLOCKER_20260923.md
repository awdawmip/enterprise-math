# RESEARCH_DRIVER intake draft — p17 order-one support / current activation blocker

Status: `NONCANONICAL_DRIVER_INTAKE_DRAFT / NOT_A_REVIEW / NOT_A_FOLLOWUP_PACKET / NOT_ACCEPTANCE`
Date: 2026-09-23

## Control identity and exact blocker

This record preserves work completed by the ordinary ChatGPT Driver host without pretending that a failed activation granted Driver authority.

- logical conversation: `driver-auto11-20260923-045818-7c1a`
- successful session request: `driver-auto11-session-20260923-0501-7c1a`
- Source-issued session: `MCP-403a83d728194d43aa83443c7eafbfc7`
- Source-issued Driver identity: `EM-DVR-1CBE02`
- session Source commit: `af0561c5d24f7ec95f49beaff676c9ed35e9579f`
- activation request: `driver-auto11-activate-20260923-0504-7c1a`
- activation terminal state: `FAILED`
- native error: `UPSTREAM_CODE_REVIEW_REQUIRED: control_plane/research_driver_followup_transaction.py, research_driver_followup.py, research_driver_followup_guard.py`
- therefore: no ACTIVE DA was obtained in this run; no privileged continuation/review/follow-up mutation was attempted.

The failure coincided with a real Source change, not a missing checkout/CLI/MCP capability. Main advanced through `d7433ae0e52cf57fbb698acc94ba3bdcac4ec658` (`control: bind follow-up publication to the current authorized driver session`) and then `3db5f407d5a091cb8b36d92fae256725ed4fe749` (`fix: bind follow-up publishers to real immutable review-store paths`). The first commit changes exactly the three files named by the native activation error plus a new targeted test. This draft does not approve those code changes; the next Driver must consume the canonical upstream code-review outcome instead of bypassing the gate.

## Research return consumed

Immutable research evidence commit: `994eec103544ac7476112f992e190ab3c2aade74`.

Relevant durable artifacts:

- `research_artifacts/T6_P17_ORDER1_SUPPORT_20260923/PROOF.md`
- `research_artifacts/T6_P17_ORDER1_SUPPORT_20260923/ROOT_REVIEW.json`
- `research_artifacts/T6_P17_ORDER1_SUPPORT_20260923/ROOT_ORDER1_REVIEW.json`
- `research_artifacts/T6_P17_ORDER1_SUPPORT_20260923/portable_input.json`
- `research_artifacts/T6_P17_ORDER1_SUPPORT_20260923/remaining_certificates.json`
- `research_artifacts/T6_P17_ORDER1_SUPPORT_20260923/order2_problem.json`

Researcher provenance is retained as `EM-DIRECT-3AD825 / TASK_RESEARCH`. Root's computational consumption is explicitly non-author and source-exposed, but is itself marked `not formal Driver acceptance` and is not rewritten here.

The support package states and records exact exclusion certificates for all sixteen relaxed p17 order-one residue classes. `ROOT_ORDER1_REVIEW.json` reports `PASS_ALL_16_ORDER1_RESIDUES`, 16 classes, 154 proof nodes and 170 pruning edges, with scope limited to the p17 order-one relaxed affine family. The package expressly does not claim order-two or global T6 completion.

## Independent bounded audit in this Driver run

This run did not rerun the 154-node certificate family and therefore does not convert the support package into a formal Driver verdict. It did independently check the first order-two frozen input arithmetic from the published compact rule:

- pattern `q2-1`: one positive atom `(q,r)=(2,1)`
- denominator `17*(17*2+1)=595`
- fixed exponent mass `594`
- positive q0 budget `2331-594=1737`
- negative q0 budget `2331`
- radius squared `1737^2+2331^2=8450730`
- exact mixed targets `-35^{-k} mod 17^k`, `k=1..6`, are
  `[16, 67, 2991, 22966, 105654, 11280740]`

These values exactly match `order2_problem.json`. This check verifies the next portable problem's first input, not its solution.

## Independent Driver judgment draft

`DRAFT_JUDGMENT`: the order-one support is a genuine information gain and is strong enough to make repeating order-one research low value. The durable package contains a complete finite-certificate claim plus a separately authored computational consumption record, while carefully limiting its scope. However, without this run's ACTIVE source-backed Driver authority and without a formal canonical review, this record does **not** accept the parent frozen Result `RR-C428294CF760BD8D99AA`, does not close the global T6 target, and does not grant Working Truth/Foundation status.

The exact parent Result remains `NEGATIVE_BOUNDARY` with hard-target disposition `PARTIAL_PROGRESS_GLOBAL_T6_OPEN_P19_AND_P17_Q0_EXCLUDED`; its own unresolved residue explicitly includes p17 vertical orders 1..16 and lower maximal primes. The new direct support narrows the p17 order-one residue but does not mutate the frozen Result bytes.

## Informative next problem already canonically published

Do not publish a duplicate successor. The Researcher already published immutable V2 task:

- task: `RS-T6-P17-ORDER2-PORTABLE-CERTIFICATE-20260923`
- publication: `TP2-33BFE7DD84657DAB803C`
- lineage: `CONTINUATION`
- parent task: `RS-T6-SHAPE-MOMENT-GLOBAL-LOWER-BOUND`
- first unresolved unit: `q2-1`

The mathematically correct next question is therefore to classify `q2-1` first under the exact six congruences and separate budgets above, proving exclusion with a complete two-candidate tree (or stronger exact lemma), or retaining an exact feasible local kernel. A local kernel must still be completed through the remaining BRC observers; a local emptiness certificate must not be promoted to global T6 completion. The existing published task already preserves the full 272-pattern hard target and kill conditions, so a Driver should route to that publication rather than create another task merely to show progress.

## Do not repeat / unverified

Do not repeat the sixteen order-one classes merely because this Driver activation failed. Do not create a new formal review from this draft. Do not hand-build follow-up packets or closure. Do not claim the upstream follow-up code is reviewed from the existence of commits alone.

Still unverified in this Driver run:

- canonical upstream code-review clearance for the three follow-up files;
- this run's ACTIVE DA (not obtained);
- formal independent Driver review of the new order-one support or of the parent frozen Result;
- any order-two pattern solution; `q2-1` remains `INPUT_ONLY_NOT_SOLVED` in the durable problem data.

## Recovery action

After the canonical upstream code-review gate is actually cleared, a future Driver must use its own real session/DA (or consume a still-valid own session if the current contracts permit), refresh current main and current Result/review sets, then continue the smallest unfinished unit. If no formal review exists for the relevant frozen object, review may proceed under the normal binding/independence gates. If review already exists, consume it and continue synthesis/follow-up; never add a duplicate review to push the queue.

This draft is a durable evidence/routing checkpoint only.
