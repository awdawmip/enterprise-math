# Enterprise Math Research Relay Protocol

Status: `ACTIVE ARCHITECTURE PROPOSAL`  
Live relay: GitHub Issue #82 — `Research Relay: cross-branch theorem and finding bus`

## 1. Purpose

Enterprise Math now has multiple long-lived research branches that can discover the same mother theorem, strict generalizations, useful specializations, or counterexamples independently. Repeated whole-branch merges are not an acceptable synchronization mechanism because they can overwrite ledgers, drag stale experiments forward, and blur mathematical ownership.

The Research Relay is the branch-independent coordination surface for **timely cross-route mathematical feedback**.

It does not replace Git history, theorem ledgers, PR review, or canonical `main`.

## 2. Mandatory branch loop

Every substantive research branch should follow this loop:

1. **Read before extending.** Before starting a new general theorem line, read recent relay entries affecting the branch.
2. **Classify before duplicating.** Before introducing a new abstraction, compare it with existing relay/lineage entries using:
   - `SAME_MOTHER`;
   - `STRICT_GENERALIZATION`;
   - `SPECIALIZATION`;
   - `GENERATOR`;
   - `COMPOSABLE_INDEPENDENT`;
   - `CONFLICT / NEGATIVE_BOUNDARY`;
   - `NAME_COLLISION_ONLY`.
3. **Relay material results.** A result must be relayed when it changes assumptions, invalidates another route, supplies a reusable mother theorem, exposes a counterexample, or creates a bridge another active branch can consume.
4. **Consume semantically.** Downstream branches reuse a mother theorem by dependency, corollary, or semantic replay. They do not create a second independently maintained copy.
5. **Promote only when stable.** Stable conclusions move from the live relay into `CONCEPT_LINEAGE`, architecture documents, theorem/counterexample ledgers, prior-art records, or canonical `main` according to their status.

## 3. Required relay payload

Every material relay entry should contain:

- source branch and exact commit;
- PR/issue when available;
- mathematical statement;
- status: proved, executable-checked, conjectural, or counterexample;
- weakest known assumptions;
- affected branches/modules;
- relationship class to existing results;
- explicit downstream action.

The relay should report **negative results with the same priority as positive results**. A counterexample that prevents two theories from being merged is architecture progress.

## 4. Feedback urgency

Relay immediately when one of these occurs:

- a theorem removes assumptions used by another branch;
- a branch proves that two named objects are actually the same mother structure;
- a strict generalization subsumes an active theorem line elsewhere;
- a counterexample invalidates a proposed bridge or interpretation;
- a new observable requires finer precision/witness identity than a downstream branch currently stores;
- an application-specific result becomes independent of its application;
- a general theorem acquires a new domain-specific specialization with nontrivial consequences.

Routine local lemmas that have no cross-route consequence need not be relayed.

## 5. Ownership rule

The relay carries conclusions, not ownership transfers.

A reusable result has one current mathematical home. Application branches retain:

- discovery provenance;
- domain assumptions;
- application-specific corollaries;
- counterexamples and executable pressure tests.

The general theorem home retains the mother statement and weakest known assumptions.

## 6. Relationship to long-lived branches

The relay exists outside individual branch histories, so researchers can read the current state even when their working branch is months of commits away from `main`.

Do not repeatedly merge `main` or another research branch merely to receive relay information. Use semantic replay only when actual code/theorem assets need to move.

## 7. Current first relay theorem

The first material result posted under this protocol is the A3→A4 bridge:

- A3 weighted relation state generates a restricted A4 admissible-support family after quotienting `Z_ij=0` classes;
- the support law is `|Z_ij| <= r m_i m_j`;
- A3 weighted closure proves `R_r ; R_s ⊆ R_(r+s)`;
- universal fine support descends to coarse support;
- coarse support does **not** recover universal fine support because signed A3 relations may cancel under partition quotient.

This is classified as `GENERATOR` plus a `CONFLICT / NEGATIVE_BOUNDARY` for the converse recovery claim.

## 8. Agent/researcher startup expectation

A researcher resuming an existing branch should first identify:

1. the current branch head;
2. the latest canonical `main` head;
3. relevant recent Research Relay entries;
4. the branch's owner architecture node (A0–A5 / P / E);
5. whether any intended new theorem has already been relayed elsewhere.

This startup check is informational and non-destructive. It must not be implemented by wholesale merging unrelated branch history.
