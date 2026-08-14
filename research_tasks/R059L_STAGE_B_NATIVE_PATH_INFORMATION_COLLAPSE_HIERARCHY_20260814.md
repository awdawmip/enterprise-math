# RS-R059L — STAGE B NATIVE PATH INFORMATION COLLAPSE HIERARCHY

Task-ID: `RS-R059L-STAGE-B-NATIVE-PATH-INFORMATION-COLLAPSE`
Generation: `R059L`
Status: `DRIVER_APPROVED_TASKBOOK`
Identity-policy: `AUTO_RESOLVE_OR_ALLOCATE`
Identity-lane: `R059L`
Date: `2026-08-14`
Driver: `EM-DVR-R0457K / CONTROL_PLANE`

## 0. Accepted frozen input

Stage A accepted frozen owner head:

`4d196b916c815f665ea725f40ee5fb48ef76b10e`

Stage A established exact native path algebra:

- zero-transition identity paths;
- associative composable concatenation;
- additive `PATH_COUNT`;
- involutive order-reversing `rev`;
- `PATH_COUNT(rev(gamma)) = PATH_COUNT(gamma)`;
- `PATH_COUNT(gamma * rev(gamma)) = 2 PATH_COUNT(gamma)`;
- reversal is NOT a cancellative inverse of raw event history;
- endpoint incidence identity;
- arrival/departure totals;
- visit multiplicity identities;
- conditional C6 bookkeeping only when `IDEAL_C6_CHANNEL_STATE` is declared.

All Stage-0 and Stage-A frozen artifacts are immutable inputs.

---

# 1. Scientific question

Do not introduce geometry.

The next foundational question is:

> When an ordered path history is replaced by progressively coarser integer summaries, exactly what information survives and what information is irreversibly forgotten?

This is an **information-collapse** problem, not a geometric-collapse problem.

The native path remains the full ordered transition history. Every summary below is a downstream exact readout/forgetful map. Equality of readouts does NOT identify native paths and does NOT authorize cancellation or quotienting of event history at N0.

---

# 2. Frozen semantic firewall

Continue to forbid theorem-critical use of:

- line / straightness;
- distance / length;
- shortest path / geodesic;
- displacement magnitude;
- metric / `Q(a,b)`;
- angle / slope / curvature;
- edge / boundary / perimeter / chord;
- area / volume;
- Voronoi or Euclidean geometry;
- physical flux / divergence / current / momentum / charge language;
- R057/R058S fitted geometry;
- path cancellation quotient or reduction of `gamma*rev(gamma)` to identity.

`UNIT_PACKET=1` and one actual adjacency transition `=1 event` remain binding.

---

# 3. Readout hierarchy

For a finite path

`gamma = (x_0, x_1, ..., x_n)`

define the following exact combinatorial readouts.

## 3.1 H0 — full ordered history

`H0(gamma) = gamma`.

This is the native path object, not a collapse.

## 3.2 H1 — directed transition multiplicity

For ordered adjacent packet pairs:

`T_gamma(x,y) = # { j : x_j=x and x_{j+1}=y }`.

Required exact identities:

`sum_{x,y} T_gamma(x,y) = PATH_COUNT(gamma)`.

`DEPART_gamma(x) = sum_y T_gamma(x,y)`.

`ARRIVE_gamma(x) = sum_y T_gamma(y,x)`.

Hence recover the Stage-A endpoint identity as the row-minus-column identity:

`sum_y T_gamma(x,y) - sum_y T_gamma(y,x) = 1[x=x_0]-1[x=x_n]`.

For composable paths:

`T_{gamma*eta} = T_gamma + T_eta`.

For reversal:

`T_{rev(gamma)}(x,y) = T_gamma(y,x)`.

## 3.3 H2 — undirected adjacency-use multiplicity

For unordered adjacent pair `{x,y}`:

`U_gamma({x,y}) = T_gamma(x,y) + T_gamma(y,x)`.

Required:

`sum_{ {x,y} } U_gamma({x,y}) = PATH_COUNT(gamma)`.

`U_{gamma*eta} = U_gamma + U_eta`.

`U_{rev(gamma)} = U_gamma`.

Do not call `{x,y}` an edge with geometric length. It is only an unordered adjacency relation instance.

## 3.4 H3 — packet visit multiplicity

Use the frozen Stage-A `VISIT_gamma(x)` convention.

Required links to arrival/departure and endpoints remain exact.

## 3.5 H4 — support set

`SUPPORT(gamma) = { x : VISIT_gamma(x)>0 }`.

This is a set of visited packets. Do not interpret it as a geometric trace/curve/region.

## 3.6 H5 — total transition count

`N(gamma)=PATH_COUNT(gamma)`.

This is the coarsest required integer event count in this Stage.

---

# 4. Information-loss / non-reconstruction theorems

The hierarchy must not merely list summaries. It must prove exact reconstruction/non-reconstruction relations.

## 4.1 Full history determines all lower readouts

Prove deterministic maps:

`H0 -> H1 -> H2`

and

`H1 + endpoint data -> ARRIVE/DEPART -> visit data`

where valid under the frozen definitions.

Also record maps to support and total count.

Do not assert a reverse map unless proved.

## 4.2 Directed transition counts do NOT determine ordered history in general

Provide an exact finite counterexample on a valid adjacency carrier.

Preferred canonical example if valid under the declared carrier:

`gamma = (A,B,A,C,A)`

`eta   = (A,C,A,B,A)`

with `A~B` and `A~C`.

These are distinct ordered histories with the same start/end and the same directed transition multiplicity table:

`A->B = B->A = A->C = C->A = 1`.

Therefore:

`T_gamma = T_eta`

but

`gamma != eta` as raw histories.

Freeze this as an information-loss theorem, not as permission to identify the paths in N0.

## 4.3 Coarser readouts lose at least as much information

Give exact counterexamples / implication arguments showing that support and total count do not reconstruct full history.

For `U`, establish precisely what directional/order information is lost. Avoid claiming a complete classification unless proved.

## 4.4 Readout-induced equivalence is N2 only

For any readout `R`, one may define for diagnostics:

`gamma ~_R eta iff R(gamma)=R(eta)`.

This is an **N2 information quotient/readout relation** only.

It must not rewrite native path equality, must not cancel events, and must not make `gamma*rev(gamma)` a zero path.

---

# 5. Composition compatibility

Classify each readout by whether it is exactly additive/compositional under path concatenation.

At minimum:

- `T`: exact additive;
- `U`: exact additive;
- `PATH_COUNT`: exact additive;
- support: union-like but join/revisit-sensitive, so state exact law carefully;
- visit multiplicity: derive exact concatenation law including the shared join packet correction.

Do not handwave shared-endpoint double counting.

A high-value exact target is the visit law for composable `gamma: a->b` and `eta: b->c`:

`VISIT_{gamma*eta}(x) = VISIT_gamma(x) + VISIT_eta(x) - 1[x=b]`.

Prove or correct it under the frozen Stage-A visit convention.

---

# 6. Optional C6 local-passage composition defect

Only when `IDEAL_C6_CHANNEL_STATE` is declared, investigate `M_x[a,b]` as a local two-transition readout.

Important: unlike `T`, passage-pair counts need not be naively additive under concatenation, because concatenating a nonzero path ending at packet `b` with a nonzero path starting at `b` creates a new internal passage event at the join.

Freeze an exact formula if well-typed:

`M^{gamma*eta} = M^gamma + M^eta + JOIN_CROSS_TERM`

where the cross-term records the ingress label supplied by the last transition of `gamma` and the egress label supplied by the first transition of `eta` at the shared packet.

Handle zero-transition paths and missing channel records explicitly.

This is purely integer event bookkeeping. Do not call the cross-term a turn, angle, scattering, or curvature.

If the exact formula is not well-defined under current Stage-0 conventions, return `C6_PASSAGE_COMPOSITION_NOT_YET_WELL_TYPED` rather than inventing geometry.

---

# 7. Stage B required artifacts

Freeze at least:

1. `R059L_DIRECTED_TRANSITION_MULTIPLICITY.json`
2. `R059L_UNDIRECTED_ADJACENCY_USE_READOUT.json`
3. `R059L_PATH_INFORMATION_HIERARCHY.json`
4. `R059L_PATH_READOUT_NONIDENTIFIABILITY.json`
5. `R059L_PATH_READOUT_COMPOSITION_LAWS.json`
6. `R059L_VISIT_SUPPORT_COLLAPSE.json`
7. `R059L_C6_PASSAGE_COMPOSITION.json` (conditional / may return NOT_YET_WELL_TYPED)
8. `R059L_STAGE_B_THEOREM_LEDGER.json`
9. `R059L_STAGE_B_REGRESSION_RESULTS.json`
10. deterministic Stage-B checker output
11. `R059L_STAGE_B_PATH_INFORMATION_COLLAPSE_CHECKPOINT.json`

The checkpoint must contain exact SHA256 for all frozen Stage-B artifacts and reproduce the frozen Stage-0/Stage-A parent anchors.

---

# 8. Required regression cases

Include exact cases that separate the hierarchy, including at least:

- zero-transition path;
- one transition;
- immediate reversal;
- repeated adjacency reuse;
- closed loop;
- repeated packet visits;
- the `A-B-A-C-A` vs `A-C-A-B-A` same-`T`, different-history pair;
- composable paths whose shared endpoint has already been visited earlier;
- reversal pairs to test `T^T` and `U` invariance;
- C6 same-channel case if C6 extension is active.

No ranking or geometric preference among paths.

---

# 9. Required theorem dispositions

At minimum freeze explicit dispositions for:

- `PB-T01`: directed transition total equals path count;
- `PB-T02`: directed transition readout additive under concatenation;
- `PB-T03`: reversal transposes directed transition counts;
- `PB-T04`: row-minus-column endpoint incidence identity;
- `PB-T05`: undirected adjacency-use reversal invariance;
- `PB-T06`: full history -> transition multiplicity deterministic;
- `PB-T07`: transition multiplicity -> full history NOT reconstructible in general;
- `PB-T08`: visit concatenation law;
- `PB-T09`: support concatenation law;
- `PB-C6-01`: conditional C6 passage composition law or exact NOT_YET_WELL_TYPED disposition.

Statuses may include:

- `PROVED_EXACT`
- `COUNTEREXAMPLE_PROVED`
- `CONDITIONAL_ON_C6_EXTENSION`
- `NOT_YET_WELL_TYPED`
- `NOT_IDENTIFIED`

Do not overclaim completeness of the entire quotient lattice.

---

# 10. Hard stop

Stop after the Stage-B frozen checkpoint.

Do NOT proceed to:

- direction;
- displacement;
- distance;
- length;
- straightness;
- shortest path;
- geometry;
- physical interpretation;
- stochastic path laws;
- optimization;
- metric learning;
- classical-shape calibration.

The point of Stage B is to establish the first exact native **information-collapse hierarchy** of path histories before any geometry is allowed to emerge.
