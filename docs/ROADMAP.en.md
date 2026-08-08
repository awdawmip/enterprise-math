# Research Roadmap

## Phase 0 — Definitions before interpretation

Goal: make the arithmetic unambiguous before attaching physical meaning.

Tasks:

- define integer quotient, integer root, power collapse, scale refinement, and scale projection;
- specify domains and codomains for every primitive operation;
- define signed states, units, dimensions, and vector states without importing hidden real coordinates;
- list every classical identity that is being retained, weakened, or rejected.

Gate: every example must be computable using the declared discrete primitives only.

## Phase 1 — Algebraic structure

Prove or disprove:

- monotonicity, idempotence, fixed-point structure, and composition laws of collapse maps;
- compatibility between scale refinement and collapse;
- distributive and associative laws for candidate operations;
- conditions under which root and multiplication commute;
- classification of operations as exact inverses, one-sided inverses, adjoints, projections, or non-invertible maps.

Deliverable: a theorem/counterexample catalog.

## Phase 2 — Automated counterexample search

Build an integer-only reference implementation that exhaustively checks small finite domains.

The first test harness should search for:

- broken imported identities;
- non-associative compositions;
- scale inconsistencies;
- hidden dependence on floating point;
- overflow assumptions;
- unexpected cycles or fixed points in collapse dynamics.

The implementation is a theorem-discovery and falsification aid, not an authority over proofs.

## Phase 3 — Scale theory

Develop scale as a first-class discrete object.

Questions:

- What transformations between scales are admissible?
- Which operations require scale changes?
- Can scale refinement be partially ordered?
- Is there a maximum physically meaningful refinement?
- How do units and dimensions interact with scale?
- Can extremely large and extremely small magnitudes be represented without changing the primitive arithmetic?

## Phase 4 — Geometry without a real continuum

Rebuild geometry rather than importing Euclidean distance unchanged.

Study:

- integer-valued distance candidates;
- lattice and graph metrics;
- discrete rotations and symmetries;
- Pythagorean structure under integer roots;
- circles, areas, volumes, and curvature at finite resolution;
- whether familiar geometric invariants survive scale changes.

A major gate is to avoid defining a discrete geometry and then evaluating it using hidden real-valued distances.

## Phase 5 — Forward collapse dynamics

Study systems

\[
X_{t+1}=T_t(X_t)
\]

where the maps may be many-to-one and need not have inverses.

Tasks:

- classify collapse basins and fixed points;
- study compositions of different collapse operators;
- identify conditions for nontrivial long-term dynamics;
- formalize the monotonic growth of merged-history equivalence classes;
- determine which semigroup structures arise naturally.

## Phase 6 — Discrete irreversibility and entropy candidates

Keep the primitive quantities integer-valued whenever possible.

Primary candidates:

\[
M_t(x)=|[x]_t|
\]

and integer information levels such as

\[
L_B(m)=\min\{\ell:m\le B^\ell\}.
\]

Questions:

- Which quantities are guaranteed to be monotone under arbitrary forward composition?
- Which depend on the selected state partition?
- How do these quantities relate to established preimage entropy and folding entropy?
- Under what additional physical assumptions could they connect to thermodynamic entropy?

Do not identify them with thermodynamic entropy by terminology alone.

## Phase 7 — Time and causality

Investigate the hypothesis that the arrow of time is associated with the direction in which distinguishable histories merge under non-invertible natural laws.

Required distinctions:

- mathematical non-invertibility;
- physical irreversibility;
- causal direction;
- thermodynamic time;
- observational coarse-graining.

The project specifically tests whether physical irreversibility can be ontological rather than merely emergent from coarse-graining.

## Phase 8 — Formalization

Formalize the stable core in a proof assistant after definitions stop changing rapidly.

Preferred early targets:

- integer root definitions;
- collapse-map properties;
- scale-compatibility lemmas;
- history-merging monotonicity;
- finite-state entropy candidates.

Lean is a natural candidate because existing order-theory and integer libraries provide useful comparison structures without forcing the project's interpretation.

## Phase 9 — Physical confrontation

Only after the mathematical core is stable, compare it systematically against physics.

Test domains may include:

- finite-resolution measurement;
- discrete space-time proposals;
- quantum measurement and state reduction;
- irreversible thermodynamics;
- conservation laws;
- Lorentz symmetry and rotational symmetry;
- known high-precision experiments.

A physical mismatch is evidence against the physical interpretation, not a reason to redefine the mathematics silently.

## Repository decision rule

For every major claim, record:

1. exact definition;
2. proof or counterexample status;
3. computational evidence;
4. closest prior art;
5. stronger physical interpretation, if any;
6. what observation or theorem could refute it.
