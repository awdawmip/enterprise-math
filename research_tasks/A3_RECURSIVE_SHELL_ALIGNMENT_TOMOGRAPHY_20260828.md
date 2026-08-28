<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-A3-RECURSIVE-SHELL-ALIGNMENT-TOMOGRAPHY",
  "title": "A3 递归外壳对齐、内部层析与径向 Holonomy",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "No exact construction yet makes outer-shell alignment choice-independent, composes it across nested A3 shells, or classifies the scale defect between align-then-restrict and restrict-then-align.",
  "next_action": "Freeze an exact finite shell filtration, the legal shell/layer move groups, the boundary target and the residual stabilizer; then prove that the aligned-interior observation is either choice-independent, a well-typed stabilizer orbit, or an explicitly set-valued relation before attempting outward recursion.",
  "dependencies": [
    "RELATIONAL_AXIS_CONVENTION.md@main",
    "research_tasks/NOLLM_EISENSTEIN_ROTATION_ATLAS_INTEGRATION_20260828.md@main",
    "enterprise_toolbox_registry.json@main",
    "research_method_inventory.json@main",
    "tool_invocation_policy.json@main",
    "native_semantics_admissibility.json@main"
  ],
  "source_refs": [
    "src/enterprise_math/finite_symmetry.py@main",
    "src/enterprise_math/predictive_quotient.py@main",
    "src/enterprise_math/operation_quotient.py@main",
    "src/enterprise_math/relation_observable_signature.py@main",
    "src/enterprise_math/precision_holonomy.py@main",
    "src/enterprise_math/precision_signed_holonomy.py@main"
  ],
  "evidence_status": "DIRECT_USER_MODEL / EXACT_A3_RELATIONAL_CARRIER_AVAILABLE / 24_FRAME_LIFT_CANDIDATE_AVAILABLE / RECURSIVE_SHELL_OPERATOR_UNPROVED",
  "last_progress_ref": "FINDING-EM-A3-RUBIK-FRAME-TWIST-20260828",
  "last_progress_at": "2026-08-28T05:04:00+00:00",
  "hard_block": null,
  "tags": [
    "A3",
    "recursive-shell",
    "Rubik-style",
    "boundary-alignment",
    "interior-observation",
    "radial-holonomy",
    "scale-coherence",
    "stabilizer-orbit",
    "finite-prototype",
    "NollM-integration"
  ],
  "claim_lease_minutes": 240,
  "created_by_role": "RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-A3-RECURSIVE-SHELL-ALIGNMENT-TOMOGRAPHY",
  "parent_objective_id": "OBJ-A3-RECURSIVE-SHELL-ALIGNMENT-AND-BULK-OBSERVATION",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "A3SHELL",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "NEW_DIRECTION",
  "parent_task_id": null,
  "successor_gate": null,
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:b78f85af4629ddb714870c44535ad0393418dbc3bebe06da142a90c0c6b9075e",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# A3 递归外壳对齐、内部层析与径向 Holonomy

Status: `PUBLISHED_REGISTERED / NEW_DIRECTION / RECURSIVE SCALE-GAUGE PROBLEM`

## Mother question

Suppose a finite three-dimensional relational world is revealed through nested shells. At each order, one first aligns the current outer shell by legal Rubik-style rotations, then observes the interior, then enlarges the world by one shell and repeats. Can this process be made exact and choice-independent, and does the sequence of aligned interior observations define new scale invariants, reconstruction tools, or obstructions?

The intended recursion is

\[
\text{align }S_n
\;\longrightarrow\;
\text{observe }B_{n-1}
\;\longrightarrow\;
\text{reveal/attach }S_{n+1}
\;\longrightarrow\;
\text{align }S_{n+1}
\;\longrightarrow\;
\text{compare inward}.
\]

## Frozen inputs and scope

### 1. Relational carrier and shell candidate

Use the existing three-dimensional displacement carrier

\[
\Lambda_3
=
\left\{
x=(x_1,x_2,x_3,x_4)\in\mathbb Z^4:
\sum_i x_i=0
\right\}.
\]

As the first exact finite carrier, test the frame-invariant radius

\[
r_{A_3}(x)=\max_i |x_i|,
\]

with nested finite regions and shells

\[
B_n=\{x\in\Lambda_3:r_{A_3}(x)\le n\},
\qquad
S_n=B_n\setminus B_{n-1}.
\]

The sign-twisted coordinate-permutation action

\[
R_\sigma=\operatorname{sgn}(\sigma)P_\sigma|_{\Lambda_3}
\]

is a candidate exact 24-frame action and preserves \(r_{A_3}\). This claim must be proved in the task package rather than treated as a visual fact.

A literal cubical \(N\times N\times N\) carrier may be used as a separately typed implementation/control model. It must not silently replace the relational carrier.

### 2. State and move typing

For each \(n\), declare explicitly:

- a finite state space \(X_n\);
- the restriction map \(\rho_{n+1,n}:X_{n+1}\to X_n\);
- the outer-shell readout \(\partial_n:X_n\to Y_n\);
- a legal move group or move-generated groupoid \(G_n\);
- the subgroup or subrelation allowed during shell alignment;
- a canonical boundary target \(\beta_n\in Y_n\);
- the interior observation language \(O_n\).

Distinguish:

- `FRAME_ROTATION`: passive re-framing;
- `SHELL_SUPPORTED_TWIST`: active move fixing a declared deep core;
- `LAYER_COUPLED_TWIST`: active move whose support crosses radial shells;
- `REGLUE_ALIGN`: interface compatibility repair;
- `REVEAL_EXPANSION`: restriction of a pre-existing larger state;
- `ACTIVE_EXTENSION`: attachment of a new shell payload.

### 3. Nontriviality gate

A recursion is not automatically informative. If every legal aligning move fixes the observed interior pointwise, then shell alignment cannot reveal an active bulk response.

Define the penetration depth of a move and prove a shielding statement of the form:

\[
\operatorname{depth}(g)\le d
\quad\Longrightarrow\quad
g\text{ fixes }B_{n-d}
\]

for the chosen carrier and generator semantics.

The task must separate:

1. the decoupled control regime, where outer alignment leaves the deep core unchanged;
2. the coupled regime, where legal alignment can transport frame, phase, incidence, or payload information across shells;
3. the regime where the state is unchanged but the admissible quotient/stabilizer changes with scale.

### 4. Existing-tool composition is mandatory

The first implementation must compose current tools before proposing a new top-level family:

- `T1_SCALE_ENUMERATION_VALUATION` for finite shell extraction and shell counts;
- `T4_FINITE_FIBER_CAPACITY_COLLISION_MINIMA` for first distinguishing scale and observation collisions;
- `T5_PRECISION_REFINEMENT` for nested restriction/recomposition;
- `T6_OPERATION_SAFE_QUOTIENT` for descent of shell normalization and interior observations;
- `T7_FINITE_SYMMETRY_EQUIVARIANCE` for orbit, stabilizer and canonical-choice obstruction;
- `T8_RELATION_OBSERVABLE_SPECTRUM` for set-valued alignment outcomes;
- `T9_HOLONOMY_COCOYCLE_GLUING` for staged-versus-direct scale transport;
- `T2_BLOCK_FINITE_CERTIFICATE` when a bounded local incompatibility certificate exists.

The default expected outcome is `COMPOSE_EXISTING_TOOLS` plus a task-local domain operator. A new shared tool family requires an exact missing input/output capability and a proof that composition is insufficient.

### 5. Semantic boundary

The Rubik-style world is a research model, not a promoted foundation statement.

The shell radius, chosen boundary target, word metric, alignment algorithm, cubical visualization, and finite/infinite completion are typed operational/readout structures unless separately derived at stronger semantic level. Minimal word length is algorithmic complexity, not physical energy.

## Hard target and required outputs

### H1. Exact nested-shell package

Prove finiteness and nesting of \(B_n\), identify the shell \(S_n\), prove the declared 24-frame invariance, and compute exact shell cardinalities for the first nontrivial radii.

Return a comparison between the \(A_3\)-invariant shell and any literal cubical carrier used as a control. Record which claims depend on the carrier choice.

### H2. Alignment relation and residual stabilizer

For \(x\in X_n\), define the set of aligning words or morphisms

\[
\mathcal W_n(x)
=
\left\{
w\in G_n:
\partial_n(w\cdot x)=\beta_n
\right\}.
\]

Classify:

- `UNREACHABLE_SHELL` when \(\mathcal W_n(x)=\varnothing\);
- `UNIQUE_ALIGNMENT`;
- `MULTIPLE_ALIGNMENT_SAME_INTERIOR`;
- `MULTIPLE_ALIGNMENT_STABILIZER_EQUIVALENT`;
- `MULTIPLE_ALIGNMENT_GENUINELY_AMBIGUOUS`.

Let

\[
H_n=\operatorname{Stab}_{G_n}(\beta_n).
\]

Define first the always-valid set-valued aligned interior signature

\[
\mathcal I_n(x)
=
\left\{
O_n\!\left(\rho_{n,n-1}(w\cdot x)\right):
w\in\mathcal W_n(x)
\right\}.
\]

Then determine whether it collapses to a singleton, an \(H_n\)-orbit, or requires a coarser operation-safe quotient. No arbitrary solver word may be used as if it were canonical.

### H3. Shell-penetration and shielding theorem

Define a support/penetration profile for every legal generator and word. Prove the strongest correct shell-shielding theorem.

At minimum, decide whether the selected move model satisfies:

\[
\max_{g\in\mathcal M_n}\operatorname{depth}(g)\le d
\quad\Longrightarrow\quad
\mathcal I_n(x)\text{ on }B_{n-d}\text{ is unaffected by active shell alignment}.
\]

If the recursion is trivial under shell-supported moves, identify the smallest coupled move semantics that makes a nontrivial interior response possible without losing exact bijectivity and typing.

### H4. Outward recursion and radial scale defect

Construct the outward recursion using restriction/reveal and active-extension variants separately.

After passing to the strongest valid aligned quotient, test the scale square

\[
\widehat\rho_{n+1,n}\circ C_{n+1}
\stackrel{?}{=}
C_n\circ\rho_{n+1,n},
\]

where \(C_n\) is the shell-alignment normalization relation or quotient map.

If the square does not commute, define a typed radial defect rather than assuming subtraction. Classify at least:

- reachability failure;
- move-action non-descent;
- stabilizer leakage;
- target incoherence;
- alignment-word ambiguity;
- nontrivial group/groupoid-valued radial holonomy.

Prove the transformation law of the defect under changes of local frame and alignment representative.

### H5. Recursive observation spectrum

Define a finite-scale signature such as

\[
\Sigma_N(x)
=
\bigl(
\mathcal I_1,\Delta_1,
\mathcal I_2,\Delta_2,
\dots,
\mathcal I_N
\bigr),
\]

with every component typed.

Derive and test:

- `DEFECT_BIRTH_RADIUS`: first scale at which a hidden mismatch becomes visible;
- `DISTINGUISHING_RADIUS`: first scale separating two states;
- `SHIELDING_DEPTH`: deepest core protected from the chosen move set;
- `STABILIZATION_RADIUS`: first scale after which the aligned observation is unchanged up to the declared quotient;
- `PERIODIC_SCALE_ORBIT`: eventual periodicity under repeated expansion/alignment;
- `BOUNDARY_TO_BULK_COLLISION`: distinct bulk states sharing the same finite shell-aligned signature.

An inverse-limit or infinite-world object may be proposed only after exact finite compatibility maps are proved. It remains conditional on the declared completion semantics.

### H6. Exact finite prototype

Build an independently checkable smallest nontrivial prototype with at least three nested radii. A literal odd-order control may use the sequence \(3\to5\to7\); the \(A_3\) model may use \(B_1\subset B_2\subset B_3\).

The prototype must include:

1. exact state serialization;
2. exact legal move generators and inverses;
3. group/groupoid closure checks;
4. shell target and aligning-word enumeration or certified search;
5. residual stabilizers;
6. all alignment ambiguities;
7. radial defect classification;
8. at least one coherent positive case;
9. at least one adversarial unreachable, ambiguous, or scale-incoherent case;
10. deterministic replayable certificates.

Do not import the parity or orientation invariants of the standard commercial cube unless they are rederived from the chosen generators.

### H7. Recursive solver and BRC representation

Represent shell completion choices, aligning words, and outward extensions as a typed relation or BRC when the process is not functional.

Construct a solver skeleton:

\[
\text{boundary target}
\to
\text{alignment relation}
\to
\text{residual-stabilizer quotient}
\to
\text{interior signature}
\to
\text{outward extension}
\to
\text{radial-defect update}.
\]

Conjugation, commutators, stabilizer chains and pruning tables may be used only after their support and quotient-safety conditions are proved for the selected move set.

### H8. Integration with the planar program

Identify which aligned three-dimensional shells contain typed \(A_2\) slices on which the NollM/Eisenstein refinement and path-holonomy tools can be transported.

Test whether the shell recursion carries:

- center/intersection precision phase;
- frame holonomy;
- positive-axis/path-order invariants;
- path-moment towers;
- incidence defects

from one radius to the next. A successful transport must retain slice orientation, layer and carrier/native typing.

## Research value to preserve

This task converts the user's proposed process into a radial gauge-fixing microscope rather than a visual analogy.

Its central new object is not a solved cube but a sequence of shell-normalized interior observations. That sequence can distinguish four phenomena that ordinary coordinates conflate:

1. a boundary that cannot be aligned;
2. a boundary that aligns in several inequivalent ways;
3. a deep core shielded from all admissible shell moves;
4. a scale defect that appears only after the world is enlarged and re-aligned.

If coherent, the construction supplies finite-to-large-scale coordinate normalization and a candidate inverse system. If incoherent, it supplies exact birth scales, collision witnesses and holonomy obstructions. Either outcome gives reusable diagnostics for three-dimensional 进取 coordinates and NollM-style multiscale atlases.

## Success, kill, and return criteria

### Success

Success requires:

1. an exact nested finite carrier and legal move model;
2. a choice-independent aligned-interior object, or the strongest exact set-valued/quotient replacement;
3. a proved shielding/nontriviality theorem;
4. a typed scale-commutation or radial-holonomy classification;
5. a complete smallest finite prototype with replayable certificates;
6. explicit reuse/composition findings for the current tool families;
7. a semantic ledger separating relational substrate, active operations, readouts and completion assumptions;
8. a bounded next theorem if the full recursion remains open.

### Kill

Kill or downgrade any route that:

1. selects one alignment word arbitrarily and calls the resulting interior canonical;
2. uses shell-supported moves yet claims nontrivial deep-core transport without proof;
3. imports standard Rubik-cube solvability invariants without deriving them from the chosen generators;
4. treats a cubical visualization, radius or shortest word as native ontology;
5. assumes align-then-restrict commutes with restrict-then-align;
6. hides multivalued alignment behind a deterministic implementation;
7. infers an infinite or physical world model from a finite carrier experiment;
8. creates a new shared tool family when current symmetry, quotient, relation and holonomy tools already compose to the required semantics.

### Return

Return a bounded package containing:

- exact definitions, maps and action laws;
- the alignment/stabilizer/ambiguity classification;
- shell penetration and shielding certificates;
- scale-commutation or radial-defect results;
- finite prototype data and deterministic checkers;
- collisions, counterexamples and failed branches;
- tool-reuse verdicts and any confirmed capability gap;
- semantic typing and the unresolved frontier;
- the first exact lemma or finite classification to execute next.
