<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-R017-PTH-POWER-UNRESOLVED-CARRIER-CLASSIFICATION",
  "title": "R017 P-th-Power Unresolved Carrier Classification",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P0",
  "leverage": "FOUNDATIONAL_CRITICAL",
  "frontier": "Classify the correct unresolved carrier for p-th-power collapse after R015/R016 established result-support branch-deferral invariance. Determine exactly when the two-neighbour bracket {L_p(n),U_p(n)} is sound, sufficient and minimal; separate endpoint-alternative semantics from cell-label semantics and from repeated re-collapse semantics; characterize the future-language boundary rather than assuming universal validity.",
  "next_action": "Prove or kill two-neighbour carrier adequacy under explicit semantics; derive strongest iff criteria relative to future languages; build bounded exhaustive and mutation tests; return a scoped recommendation for R009/P023 without editing their canonical semantics.",
  "dependencies": [
    {"target": "RS-R015-RESULT-SUPPORT-BRANCH-DEFERRAL-INVARIANCE", "action": "CONSUME_ACCEPTED_RESULT_SUPPORT_GATE", "satisfied": true},
    {"target": "RS-R016-R015-BRANCH-DEFERRAL-LEAN-FORMALIZATION", "action": "CONSUME_LEAN_CHECKED_GENERIC_CORE", "satisfied": true},
    {"target": "R009 frozen p-th-power collapse program", "action": "AUDIT_IMPACT_ONLY", "satisfied": true},
    {"target": "P023 future-compatible quotient semantics", "action": "AUDIT_IMPACT_ONLY", "satisfied": true}
  ],
  "source_refs": [
    "research_tasks/R015_RESULT_SUPPORT_BRANCH_DEFERRAL_INVARIANCE_20260811.md",
    "research_tasks/R016_R015_BRANCH_DEFERRAL_LEAN_FORMALIZATION_20260811.md",
    "docs/P023_COMPOSITION_SAFE_COLLAPSE.en.md",
    "R009 frozen owner evidence / R011 validation slice",
    "R015 accepted evidence head 2e2ac73195dad99522d94b7de091b24ee511d5c6",
    "R016 Lean-checked evidence head eac1cdb8eeb6e217121d64e5087d9c1b2b6b74ef"
  ],
  "evidence_status": "FOUNDATION_SEMANTICS_GATE_2",
  "last_progress_ref": "R015/R016 dual foundation gate accepted",
  "last_progress_at": "2026-08-11T12:56:00+08:00",
  "hard_block": null,
  "tags": ["R017", "R009", "P023", "collapse", "p-th-power", "unresolved-state", "carrier", "branching", "precision-cell", "future-language", "minimality"],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "DRIVER_APPROVED",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "identity_lane": "R017"
}
-->

# R017 — P-th-Power Unresolved Carrier Classification

Status: `READY / P0 / FOUNDATIONAL_CRITICAL / FOUNDATION SEMANTICS GATE 2 / NOT CANONICAL`

## 1. Mother question

R015/R016 have already settled one layer:

> once the current state is legitimately represented as result-support and future evolution is relational, eager branching, intermediate union/coalescence, lazy branching and directly composed future give the same final reachable support.

R017 studies the logically prior remaining question:

> **what is the correct current unresolved state before that relational theorem is applied?**

For `p >= 2`, let

\[
S_p=\{k^p:k\in\mathbb N\}.
\]

For `n in N`, define the nearest representable anchors on each side

\[
L_p(n)=\max\{s\in S_p:s\le n\},\qquad
U_p(n)=\min\{s\in S_p:n\le s\}.
\]

The candidate unresolved carrier is

\[
B_p(n)=\{L_p(n),U_p(n)\},
\]

with the exact-point convention `B_p(n)={n}` when `n in S_p`.

Do **not** assume this candidate is universally correct. Classify exactly what it means, when it is enough, and when it is not.

---

## 2. Semantic distinctions that must not be conflated

Treat the following as different mathematical objects until equivalence is proved.

### A. Endpoint-alternative semantics

`{L_p(n),U_p(n)}` means two actual alternative anchor states. A later selector may resolve to the lower or upper anchor, after which future relations act on anchor states.

### B. Bracket/cell-label semantics

`(L_p(n),U_p(n))`, the unordered two-anchor set, or an equivalent cell identifier is merely a **label for one precision cell**. It does not by itself assert that the physical/mathematical state is literally either endpoint.

### C. Fine-fibre semantics

The unresolved state denotes the whole fine fibre represented by the cell, e.g. for adjacent powers

\[
C_{p,k}=\{n:k^p<n<(k+1)^p\}
\]

with exact powers handled separately.

### D. Re-collapse semantics

After each future operation the state is projected/coalesced back to the current precision carrier, so newly admitted fine representatives of a coarse cell are part of the semantics.

### E. Fine-conservative semantics

Collapse occurs, but later coarse execution is required to preserve exactly the reachable result-support of the original fine state/fine support, without adding results merely because an intermediate coarse cell was re-expanded.

R017 must state every theorem with its semantic regime. A theorem in one regime is not evidence for another.

---

## 3. Mandatory theorem targets

### R017-T01 — bracket structure

Prove for `p >= 2`:

1. `L_p(n) <= n <= U_p(n)`;
2. `L_p(n)=U_p(n)` iff `n` is a perfect `p`-th power;
3. if `k^p < n < (k+1)^p`, then
   \[
   L_p(n)=k^p,\qquad U_p(n)=(k+1)^p;
   \]
4. the bracket carrier partitions `N` into singleton exact powers plus open interior gaps.

Give an exact kernel/fibre description.

### R017-T02 — joint-observation minimality

Let

\[
Q_p(n)=(L_p(n),U_p(n)).
\]

Prove

\[
\ker Q_p=\ker L_p\cap\ker U_p.
\]

Then prove the universal factorization statement:

> among observations from which **both** `L_p` and `U_p` can later be recovered, `Q_p` is the coarsest/minimal observation up to relabelling.

This establishes or kills the strongest valid version of:

> “do not choose lower or upper now; retain exactly enough information to choose either later.”

Also determine whether the unordered set label `B_p(n)`, the ordered pair `Q_p(n)`, and a gap-index/exact-point tag have exactly the same fibres. If yes, classify the difference as representation only.

### R017-T03 — deferred selector theorem

Formalize the regime in which the only unresolved choice is a later selector

\[
\sigma\in\{\text{lower},\text{upper}\},
\]

followed by arbitrary result-only relational future on the selected anchor state.

Using the already accepted R015/R016 result-support law, prove whether:

- resolving lower/upper immediately;
- keeping `Q_p(n)` unresolved until a later selector;
- branching over both selector outcomes and coalescing final result-support

are exactly equivalent.

State clearly what this theorem does **not** cover.

### R017-T04 — future-language adequacy criterion

For a declared future language `U`, define a task/future signature sufficiently strong to compare all final reachable result-supports under finite words from `U`.

Derive the strongest correct criterion of the form

\[
\boxed{
Q_p(x)=Q_p(y)\Longrightarrow
\Sigma_U(x)=\Sigma_U(y)
}
\]

for `Q_p` to be sufficient under **fine-conservative** semantics.

Express the criterion equivalently as a kernel inclusion whenever correct:

\[
\ker Q_p\subseteq\ker\Sigma_U.
\]

Then characterize minimality/coarseness: when is equality of kernels the exact minimal carrier for `U`?

Root generic quotient/task-signature mathematics as prior art rather than novelty.

### R017-T05 — quotient-relational lifting versus exact fine future

Given a fine relation `R` and quotient/carrier `q`, define the induced coarse relation by existence of fine representatives.

Prove the exact one-step result-support statement.

Then attack composition:

\[
\overline{S\circ R}
\stackrel{?}{=}
\bar S\circ\bar R.
\]

Find the strongest correct necessary/sufficient condition for equality of final support under arbitrary finite composition, or give a hierarchy of exact sufficient/necessary conditions if one clean iff is not available.

Mandatory negative boundary:

Construct a minimal example where an intermediate coarse state merges fine representatives that cannot be joined by one fine trajectory, and the coarse composed relation produces a **new final result**. This is a result-support failure even though path identity itself is not an output.

Explain precisely why this does not contradict R015/R016: those theorems start after a valid coarse relational semantics has already been fixed.

### R017-T06 — one-collapse versus repeated re-collapse

Introduce a closure/saturation operator for a carrier/quotient,

\[
c_q(A)=q^{-1}(q(A)).
\]

For a future transformer `F_*` on fine supports, compare:

- fine-conservative evolution;
- one initial collapse followed by fine evolution;
- repeated `c_q` after each step.

Derive a usable algebraic exactness condition, attacking identities such as

\[
c_qF_*c_q=c_qF_*
\]

and their finite-word analogues.

Determine which condition means:

> inserting an intermediate coalescence does not change later **coarse result-support**.

Do not rename standard abstract-interpretation/completeness results as project novelty; root them.

### R017-T07 — arithmetic kill tests for the two-neighbour carrier

The task must not stay abstract.

Start with square collapse (`p=2`) and explicitly test the bracket cell between `4` and `9`.

At minimum analyze:

\[
Q_2(5),\quad Q_2(8),\quad Q_2(5+1),\quad Q_2(8+1).
\]

Determine whether translation by `+1`:

1. descends as a deterministic operation through `Q_2`;
2. is exact as a set-valued coarse relation for one step;
3. remains exact after intermediate re-collapse over multiple steps;
4. preserves the fine-conservative result-support of an exact starting state.

Generalize as far as possible:

- for `p >= 2`, classify positive translations `n -> n+t` that are functional-safe for `Q_p`;
- separately classify or bound those that are support-exact under the declared repeated-collapse semantics;
- if the global safe translation monoid is trivial, prove it rather than infer it from examples.

Also test at least one non-translation operation family relevant to the R009 scale/power program.

### R017-T08 — candidate-carrier comparison

Compare at least:

1. lower-only `L_p`;
2. upper-only `U_p`;
3. nearest-anchor collapse with explicit tie rule;
4. two-sided bracket `Q_p=(L_p,U_p)`;
5. cell/fibre identifier;
6. bracket plus within-cell residual/offset;
7. exact `n`.

For each candidate record:

- fibres/kernel;
- whether lower and upper resolution are recoverable;
- future-language exactness;
- whether branching is functional or relational;
- information retained;
- smallest counterexample to claimed sufficiency.

Do not choose a winner by aesthetic preference.

### R017-T09 — exact minimal repair when `Q_p` fails

When two-neighbour bracketing is insufficient for a future language `U`, determine the minimal additional coordinate required.

Attack whether the repair is:

- a residue/offset inside the gap;
- a bounded distance-to-boundary coordinate;
- a future-signature class;
- or no simpler closed form than task-relative refinement.

Relate this explicitly to the earlier “collapse generates its legal future operations” viewpoint.

### R017-T10 — consequence for the word “collapse”

Return a precise taxonomy distinguishing at least:

- `LOWER_COLLAPSE`;
- `UPPER_COLLAPSE`;
- `UNRESOLVED_BRACKET`;
- `CELL_STATE`;
- `RESULT_SUPPORT_BRANCH_STATE`;
- `FUTURE_REFINEMENT_REQUIRED`.

The output must say whether `5 -> {4,9}` is:

- a theoremically justified exact unresolved state;
- exact only for deferred lower/upper selection;
- an uncertainty cell label;
- a sound over-approximation;
- or false under some future-language semantics.

Multiple answers may coexist under different semantics, but the scopes must be explicit.

---

## 4. Executable evidence

Build independent reference engines for:

1. exact fine-state/fine-support evolution;
2. bracket/cell quotient evolution;
3. endpoint-alternative branching;
4. repeated re-collapse/coalescence.

Mandatory bounded tests:

- `p = 2,3,4,5`;
- enough consecutive gaps to include small and nontrivial widths;
- translations over a nontrivial range of `t`;
- horizons at least `0..6`;
- exact-point and interior-cell starts;
- automatic comparison of direct fine composition versus stepwise coarse composition.

Add mutation tests that deliberately violate current-state sufficiency or exact-composition conditions and verify the oracle detects new/missing final results.

Where feasible, automatically minimize counterexamples by state count / `p` / gap / translation / horizon.

Do not use floating-point roots for theorem-critical classification.

---

## 5. Required decision matrix

Return one table with rows:

- selection-only future;
- arbitrary relation after endpoint resolution;
- deterministic fine operation before resolution;
- relational coarse operation;
- repeated re-collapse;
- fine-conservative execution;
- translation language;
- chosen R009-relevant operation family.

Columns:

- two-neighbour carrier sound?;
- exact?;
- minimal?;
- counterexample?;
- required extra hypothesis/coordinate?;
- project impact.

---

## 6. Prior-art/rooting attack

Explicitly root and separate any use of:

- lower/upper adjoints or Galois connections;
- interval/bracketing abstraction;
- closure/saturation operators;
- abstract interpretation completeness;
- quotient congruence / bisimulation / simulation;
- nondeterministic powerset semantics;
- Myhill–Nerode/task-signature style minimal quotients;
- rough/interval approximation if materially relevant.

The target is not to claim these generic tools as new. The project-specific residue, if any, is the exact integration of p-th-power precision cells, deferred branch semantics and future-language legality.

---

## 7. Project impact

Audit consequences for:

- R009 lower collapse and its scale/naturality laws;
- P023 functional-safe terminology;
- P018 precision projection;
- R015/R016 result-support branch deferral;
- R013 current-state/witness boundaries;
- R014 semantic-fibre-before-resource comparison.

Do not edit canonical R009/P023 in this task.

The task should end with one of the following scoped recommendations:

### A — strong two-neighbour result

`TWO_NEIGHBOUR_CARRIER_PROVED_IN_DECLARED_SCOPE / SUFFICIENT_AND_MINIMAL / TOOL_CHECKED / FOUNDATION_REWRITE_CANDIDATE / NOT_CANONICAL`

### B — selection-only result

`TWO_NEIGHBOUR_MINIMAL_FOR_DEFERRED_SELECTION_ONLY / GENERAL_FUTURE_INCOMPLETE / MINIMAL_REPAIR_CLASSIFIED / TOOL_CHECKED / NOT_CANONICAL`

### C — cell-semantics result

`BRACKET_IS_CELL_LABEL_NOT_ENDPOINT_ALTERNATIVE / RECOLLAPSE_SEMANTICS_CLASSIFIED / TOOL_CHECKED / NOT_CANONICAL`

### D — killed

`TWO_NEIGHBOUR_CARRIER_KILLED_IN_REQUIRED_SEMANTICS / FOUNDATION_REWRITE_ABORT`

A mixed result is expected if rigor requires it; report the strongest true scoped theorem rather than forcing one headline.

---

## 8. Deliverables

Return one compact package containing:

1. main mathematical report;
2. theorem/lemma list with weakest assumptions;
3. executable reference implementation;
4. focused tests and exhaustive summary;
5. minimized positive/negative examples;
6. carrier comparison matrix;
7. prior-art/rooting matrix;
8. R009/P023 impact recommendation;
9. final scoped verdict.

A separate Lean task is **not** part of R017. If R017 freezes a stable theorem package, Driver decides whether to open an independent R018 formalization gate.
