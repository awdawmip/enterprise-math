<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-NOLLM-EISENSTEIN-ROTATION-ATLAS",
  "title": "NollM–进取数论 Eisenstein 旋转图册与路径矩桥接",
  "kind": "RESEARCH",
  "owner": "research/nollm-eisenstein-rotation-atlas",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "MEDIUM",
  "frontier": "No theorem package yet unifies circle–hex core/halo duality, exact Eisenstein center/intersection refinement, finite rotation-phase classification, and path-jet oriented moments while preserving native semantics.",
  "next_action": "Freeze the exact (1-omega)^-1 Lambda three-coset decomposition and axial mod-3 classifier, then prove the normalized path-jet/oriented-triangle moment identity with explicit native/carrier typing.",
  "dependencies": [],
  "source_refs": [],
  "evidence_status": "DIRECT_USER_INTEGRATION_DIRECTION / NOLLM_BRIDGE / NO_WORKING_TRUTH_GRANT",
  "last_progress_ref": "main@29b915e115c403017b8b1aedddd60fc14edd3e3a",
  "last_progress_at": "2026-08-28T04:20:00+00:00",
  "hard_block": null,
  "tags": ["INTEGRATION", "NOLLM", "EISENSTEIN", "ROTATION", "PATH_JET", "THREE_DIMENSIONAL_PRECURSOR"],
  "claim_lease_minutes": 240,
  "created_by_role": "RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-NOLLM-EISENSTEIN-ROTATION-ATLAS",
  "parent_objective_id": "NOLLM_ENTERPRISE_ROTATION_GEOMETRY_INTEGRATION_20260828",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "R3D",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "INTEGRATION",
  "parent_task_id": "",
  "successor_gate": {},
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:b78f85af4629ddb714870c44535ad0393418dbc3bebe06da142a90c0c6b9075e",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# NollM–进取数论 Eisenstein 旋转图册与路径矩桥接

Status: `PUBLISHED_REGISTERED / INTEGRATION / NOLLM-BRIDGE`

## Mother question

Can NollM's hex-atlas, rotation, phase, and coverage machinery be integrated with the 进取 circle Cell, triple-intersection, path-holonomy, and precision-layer structures to yield exact reusable tools without replacing native Cell semantics by geometric implementation semantics?

## Frozen inputs and scope

1. Use the planar center lattice candidate
   \[
   \Lambda=\mathbb Z[\omega],\qquad \omega^2+\omega+1=0,
   \]
   with nearest-center spacing \(1\) and circle radius \(1/\sqrt3\).

2. Use a pointy-top regular-hexagon carrier of side \(1/\sqrt3\) on the same center lattice, together with exact axial/cube integer addresses.

3. Freeze the exact refinement candidate
   \[
   \alpha=1-\omega,\qquad N(\alpha)=3,\qquad \Lambda^+=\alpha^{-1}\Lambda.
   \]

4. Reuse the existing path-jet family
   \[
   J_n(u,v)=\det(u,v)\,\operatorname{Sym}^n([u\ v])
   \frac{(X+Y)^{n+1}-X^{n+1}}{Y},
   \]
   and the existing endpoint, positive-axis holonomy, path-order, and triple-incidence observables.

5. Preserve the semantic boundary: circle Cell and triple incidence remain native candidates; hexagons, Euclidean moments, similarity maps, and area coverage remain carrier/readout structures unless independently rederived at stronger semantic level.

6. Primary source surfaces:
   - `awdawmip/Nollm`: atlas parameter matrix, exact hex metric, coverage kernel/oracles, rotation sweep, cycle residuals, affine holonomy, and anti-resonance probes;
   - `awdawmip/enterprise-math`: native coordinate conventions, precision change, symmetry quotient, finite-model, holonomy, incidence, and path-jet packages.

7. This task integrates two existing research lines. It does not silently replace either project's native objects, nor does a visual coincidence count as a theorem.

## Hard target and required outputs

### H1. Circle-halo / hex-core theorem package

Prove that the Voronoi core of the unit triangular center lattice is a regular hexagon of side \(1/\sqrt3\), and that its vertices are exactly the triple boundary intersections of the radius-\(1/\sqrt3\) circle family. Define a non-overlapping target-core transfer kernel and prove total-mass conservation.

### H2. Exact center/intersection refinement

With
\[
c=\alpha^{-1}=\frac{2+\omega}3,
\]
prove the disjoint coset decomposition
\[
\alpha^{-1}\Lambda
=
\Lambda\sqcup(c+\Lambda)\sqcup(2c+\Lambda).
\]
Derive the exact axial integer matrix, prove the classifier \(q-r\pmod3\), identify the two triangle-orientation classes, and prove two refinement steps reduce to scale \(1/3\) up to a lattice unit.

### H3. Path-jet / oriented-moment bridge

Prove
\[
J_n(u,v)
=
(n+1)(n+2)
\int_{\operatorname{conv}\{0,u,u+v\}}
x^{\odot n}\,dA_{\rm or}.
\]
Define the closed-path tower
\[
\mathcal A_n(\gamma)=\sum_iJ_n(P_{i-1},D_i),
\]
and prove subdivision invariance, reversal, concatenation, translation law, and affine covariance. Identify
\[
\mathcal A_0=\Omega_2
\]
and isolate the \(n=1\) signed-standard component.

### H4. Rotation-phase classification

Classify when the translation-phase orbit between \(\Lambda\) and \(a\Lambda\) is finite in terms of lattice commensurability. For nested Eisenstein refinements, prove the exact phase count and distinguish exact-resonant, commensurable non-nested, and nonresonant regimes.

### H5. Integrated typed invariant

Construct and test a typed combined object of the form
\[
\mathfrak H_{\le N}(\gamma)
=
\bigl(
D_{\rm net},H_+;
\operatorname{Hol}_{\rm chart};
\mathcal A_0,\ldots,\mathcal A_N
\bigr),
\]
with explicit source/target types, layer labels, phase classes, and failure certificates.

### H6. Prime-index exploratory bridge

For Eisenstein prime index \(p\), test whether the finite phase action
\[
\mathbb F_p\rtimes\mathbb F_p^\times
\]
has a structural relation to the path-jet first-bad degree \(p(p-1)\). Treat equal cardinalities as a lead only; return a theorem, a precise obstruction, or an explicitly bounded unresolved residue.

### H7. Tool-reuse matrix

Compose existing precision-change, finite-symmetry, holonomy, incidence, and finite-model tools before defining new general machinery. Create a new broad tool only after recording the exact capability gap that the existing composition cannot cover.

## Research value to preserve

This task supplies an exact bridge between NollM's engineered rotation atlas and the 进取 native/derived hierarchy. It can provide:

- a deterministic center-to-intersection precision transition;
- finite versus nonresonant rotation-phase classification;
- mass-conserving cross-layer transfer;
- higher path observables beyond scalar area;
- a reusable base for a future three-dimensional rotating-coordinate theory.

The value depends on preserving types. The circle remains the native Cell candidate; the hexagon is a unique-address partition core. A triple intersection may become a center only at a tagged finer layer. A geometric moment is not promoted merely because it computes an existing combinatorial invariant.

## Success, kill, and return criteria

### Success

Success requires:

1. exact maps and quotient/type declarations;
2. symbolic proofs or independently checkable derivations for H1-H4;
3. exact small-instance tests and adversarial counterexample searches;
4. at least one theorem-level integration package and one executable experiment bundle;
5. a clear boundary between proved statements, geometric readouts, and exploratory prime-index evidence.

### Kill

Reject or downgrade any branch that:

1. depends on floating nearest-point selection where an exact address is claimed;
2. loses quotient invariance or orientation typing;
3. double-counts mass by using overlapping target circles as a partition;
4. identifies same-layer centers with intersections without layer/type tags;
5. promotes visual similarity, numerical agreement, or equal group cardinality to a theorem;
6. duplicates an existing general tool without a demonstrated coverage gap.

If the proposed finite-phase criterion fails, return the smallest counterexample and replace it with the strongest correct classification.

### Return

Return a bounded result package containing:

- proved statements and proof dependencies;
- exact maps, tests, and counterexamples;
- failed branches and semantic downgrades;
- the unresolved frontier;
- the first exact lemma that should be attempted next.
