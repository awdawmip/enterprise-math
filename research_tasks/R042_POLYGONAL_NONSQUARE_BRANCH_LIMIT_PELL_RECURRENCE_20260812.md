<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-R042-POLYGONAL-NONSQUARE-BRANCH-LIMIT-PELL-RECURRENCE",
  "title": "R042 Nonsquare Polygonal Branch-Limit Dimension and Pell-Hit Recurrence",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P0",
  "leverage": "FOUNDATIONAL_DYNAMICS_GEOMETRY",
  "frontier": "Determine whether the exact nonsquare separated polygonal endpoint dynamics produced by R040 has full binary geometric dimension despite Pell-strip pruning, and classify whether a single legal dynamical branch can revisit the exact-hit set infinitely often with non-hit steps between visits.",
  "next_action": "Work from the R040 discriminant-lattice rounded-dilation carrier, separate combinatorial branch entropy from geometric dimension, prove or kill the candidate dimension equality in nonsquare r>=5, and analyze branch-accessible Pell residue orbits for infinite nonconsecutive exact-hit recurrence.",
  "dependencies": [
    {
      "target": "R040 polygonal owner head c1753e11f076d4147a677a3dfa8c76520d7957fb",
      "action": "CONSUME_FROZEN_DISCRIMINANT_LATTICE_ROUNDED_DILATION_PELL_STRIP_AND_LIMIT_EXISTENCE_RESULTS",
      "satisfied": true
    },
    {
      "target": "R035 paired-arm theorem union",
      "action": "PRESERVE_PROJECT_ARM_ISOLATED_ARM_PROVENANCE_FOR_INPUT_RESULTS",
      "satisfied": true
    }
  ],
  "source_refs": [
    "docs/R040_POLYGONAL_ASYMPTOTIC_CODING_REPORT.md at owner head c1753e11f076d4147a677a3dfa8c76520d7957fb",
    "research_outputs/r040/R040_LIMIT_SUPPORT_ATLAS.json",
    "research_outputs/r040/R040_EXACT_HIT_ATLAS.json",
    "research_outputs/r040/R040_PROVENANCE_MATRIX.json",
    "research_inputs/R035_PAIRED_ARM_SELECTED_FINDINGS_20260812.md"
  ],
  "evidence_status": "NONSQUARE_BRANCH_GEOMETRY_AND_PELL_RECURRENCE_GATE",
  "last_progress_ref": "R040 replaced the primitive two-axis ontology by one discriminant-lattice rounded nonlinear dilation and left exact nonsquare dimension plus branchwise infinite exact-hit recurrence open.",
  "last_progress_at": "2026-08-12T16:34:00+08:00",
  "hard_block": null,
  "tags": [
    "R042",
    "polygonal",
    "nonsquare",
    "pell",
    "branch-limit",
    "hausdorff-dimension",
    "exact-hit",
    "rounded-dilation",
    "residue-orbit",
    "fractal-dynamics"
  ],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "DRIVER_APPROVED",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "identity_lane": "R042",
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:a03b06c1c6d29ca2776592fd12aa77406f45a21afb8fc1a8431b25cd41963c77",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# R042 — Nonsquare Polygonal Branch-Limit Dimension and Pell-Hit Recurrence

Status: `READY / P0 / FOUNDATIONAL DYNAMICS-GEOMETRY / NOT CANONICAL`

## 0. Frozen input

Use the exact R040 carrier, not the discarded primitive two-axis picture.

For

\[
a=s-2,\qquad c=s-4,\qquad z_k=2ak-c,
\]

and fixed integer `r>=1`, let

\[
B=(r-1)c^2,\qquad \Lambda_s=2a\mathbf Z-c.
\]

The endpoint dynamics is the bracketing on `Lambda_s` of

\[
W(z)=\sqrt{rz^2-B}.
\]

For nonsquare `r` and `c!=0`, R040 froze the stable Pell-strip decision using

\[
N=rz^2-y^2:
\]

- `0<N<B` = curvature/mechanical defect;
- `N=B` = exact hit;
- `N>B` = ordinary mechanical-side bracket.

For `r>=5`, distinct-parent recoalescence is absent. R040 also froze compact normalized branch-limit existence and the upper bound

\[
\dim_H K\le \overline{\dim}_B K\le \frac{\log 2}{\log\sqrt r}.
\]

Do not re-open those inputs unless a genuine counterexample appears.

## 1. Mother question A — exact nonsquare dimension

For nonsquare `r>=5`, `s!=4`, and finite nonempty positive initial support, determine whether the normalized branch-limit set satisfies

\[
\boxed{\dim_H K=\overline{\dim}_B K=\frac{\log2}{\log\sqrt r}}
\]

or whether Pell-strip pruning can produce a strict dimension drop.

This is a theorem candidate, not a target that must survive.

Separate exactly:

- support cardinality entropy;
- geometric cylinder separation;
- Hausdorff dimension;
- upper/lower box dimension;
- positive normalized branching prefactor;
- branch collisions in the normalized limit.

`|S_t|/2^t -> L>0` does not by itself prove Hausdorff-dimension equality.

### Required attacks

1. derive cylinder diameters and sibling/ancestral separation from the exact rounded nonlinear map;
2. quantify distortion relative to the linear scale `sqrt(r)`;
3. test whether different infinite branch words can land at the same normalized limit point;
4. determine whether exact-hit one-child events create only a finite/zero-density coding defect or a geometrically meaningful deletion process;
5. if full dimension survives, isolate the weakest exact hypotheses needed;
6. if dimension drops, freeze the smallest exact witness and mechanism.

## 2. Mother question B — branchwise infinite exact-hit recurrence

Ambient exact-hit sets may be empty or infinite. This does not imply that one legal endpoint branch can visit them infinitely often.

Classify whether there exist nonsquare `r>=5`, `s!=4`, a positive start, and one legal infinite branch

\[
k_0\to k_1\to k_2\to\cdots
\]

such that exact hits occur at infinitely many times, with at least one non-hit step between infinitely many successive hit times.

Possible valid outcomes include:

- explicit construction of such a branch;
- proof of impossibility for every fixed `(s,r)` in the declared regime;
- exact arithmetic criterion distinguishing recurrence/nonrecurrence cells;
- partial classification by residue/Pell-orbit type with the general problem left open.

Do not replace branch accessibility by ambient Pell solvability.

## 3. Residue-orbit reduction

Use the R040 observation that the active arithmetic state is a Pell norm together with

\[
y,z\equiv-c\pmod{2a}.
\]

Build an exact finite-state description, when possible, of:

- admissible interior norms `1<=N<B`;
- exact-hit boundary norm `N=B`;
- residue-compatible Pell-unit action;
- which Pell solutions are reachable from an actual endpoint branch;
- transitions between hit/non-hit residue states induced by the child choice.

A residue graph/automaton is allowed if derived from the exact dynamics. Do not assume a finite automaton exists.

## 4. Square and degenerate controls

Use only as controls:

- square `r=q^2,s!=4`: exact stable deleted-digit branch with known dimension `log2/log q` for `q>=3` and interval at `q=2`;
- `s=4`: exact rounded dilation with `B=0`;
- `r=4`: frozen critical formulas;
- `r=2,3`: overlapping-parent regimes outside the main dimension theorem.

Do not transfer conclusions from these controls to nonsquare `r>=5` without proof.

## 5. Exact experiments

Build an independent checker around the exact integer endpoint oracle.

At minimum:

- enumerate branch trees for representative nonsquare `r>=5` across several `s`;
- track exact-hit times per branch, not just per level;
- compute exact cylinder intervals or rigorous rational enclosures for normalized limits;
- search for duplicate limit prefixes/cylinder overlaps;
- enumerate admissible Pell/residue states and compare with actually reachable branch states;
- pressure-test cells with many ambient hits and cells with residue-obstructed strips;
- hold out larger `s,r,k` ranges from discovery.

Floating point may be used for visualization only after exact/rational certification of the relevant boundary.

## 6. Kill targets

Actively kill or narrow:

1. `positive binary prefactor => full Hausdorff dimension`;
2. `ambient exact-hit set infinite => one branch has infinitely many hits`;
3. `zero-density Pell defects cannot change geometric dimension`;
4. `no cross-parent recoalescence => no normalized-limit overlap`;
5. `continued-fraction/Pell orbit membership => branch reachability`;
6. `all nonsquare cells share one dimension mechanism`;
7. `square deleted-digit IFS theory transfers verbatim to the nonlinear rounded map`.

Minimal counterexamples are preferred over salvaging a broad claim.

## 7. Prior-art rooting

Root any generic use of:

- graph-directed/self-similar or asymptotically self-similar dimension theory;
- Moran constructions;
- non-autonomous iterated-function systems;
- beta-expansion / Bernoulli-convolution language;
- Pell equations and unit orbits;
- symbolic dynamics / subshifts / automata.

Enterprise Math novelty, if any, must remain in the exact polygonal endpoint-dynamics specialization, arithmetic accessibility coupling, or a genuinely new theorem proved here.

## 8. Deliverables

Return at least:

- `docs/R042_POLYGONAL_NONSQUARE_BRANCH_LIMIT_REPORT.md`;
- exact experiment/checker code;
- focused tests;
- `R042_DIMENSION_DISPOSITION.json`;
- `R042_BRANCH_HIT_RECURRENCE_ATLAS.json`;
- `R042_PELL_RESIDUE_REACHABILITY.json`;
- `R042_PROVENANCE_MATRIX.json`;
- unresolved frontier.

Every major claim must be tagged `PROVED`, `EXECUTABLE_CHECKED`, `BOUNDED_EXHAUSTIVE`, `CONJECTURAL`, or `PRIOR_ART`.

## 9. Return classes

Preferred positive return:

`NONSQUARE_BRANCH_LIMIT_FULL_DIMENSION_PROVED / PELL_PRUNING_GEOMETRICALLY_SUBCRITICAL / BRANCH_HIT_RECURRENCE_CLASSIFIED / NOT_CANONICAL`

If dimension drops:

`NONSQUARE_BRANCH_LIMIT_DIMENSION_DROP_FOUND / PELL_PRUNING_GEOMETRICALLY_RELEVANT / MINIMAL_MECHANISM_FROZEN / NOT_CANONICAL`

If recurrence is the main result while dimension remains open:

`PELL_BRANCH_RECURRENCE_CLASSIFIED / NONSQUARE_LIMIT_DIMENSION_OPEN / EXACT_REACHABILITY_ATLAS_FROZEN / NOT_CANONICAL`

If the current formulation is wrong:

`NONSQUARE_LIMIT_ONTOLOGY_REPLACED / SMALLER_EXACT_GEOMETRIC_OBJECT_FOUND / NOT_CANONICAL`

Do not force a full PASS token when only part of the mother problem closes.
