# RS-R059L — STAGE D EXACT FIBER COUNT / FACTORIAL-ARBORESCENCE FACTORIZATION

Task-ID: `RS-R059L-STAGE-D-EXACT-FIBER-COUNT-FACTORIZATION`
Generation: `R059L`
Status: `DRIVER_APPROVED_TASKBOOK`
Identity-policy: `AUTO_RESOLVE_OR_ALLOCATE`
Identity-lane: `R059L`
Date: `2026-08-15`
Driver: `EM-DVR-R0457K / CONTROL_PLANE`

## 0. Frozen parent

Stage C is frozen at owner head:

`236678081b425d97eeb0326e46041a34a5333ed4`

Stage 0 / A / B / C frozen artifacts are immutable.

This Stage D starts from the exact Stage-C objects only:

- finite transition multiplicity table `T(x,y)`;
- realizability fiber `F(T;s,t)`;
- collapse multiplicity `MU(T;s,t)=|F(T;s,t)|`;
- raw native path equality = full ordered history equality;
- Stage-C realizability theorem;
- Stage-C reversal and relabeling bijections.

No geometry is introduced.

---

# 1. Scientific question

Stage C proved that `MU(T;s,t)` is a finite nonnegative integer, but did not give a non-enumerative exact formula.

Stage D asks:

> For realizable finite `T`, can the exact number of distinct raw ordered histories in `F(T;s,t)` be computed directly from integer transition multiplicities and a finite relational tree-like count, without enumerating the whole fiber?

This is an information-collapse counting problem, not geometry.

---

# 2. Mandatory native-first derivation

Do **not** cite an external graph-counting theorem as the proof.

First derive the counting law self-contained in R059L semantics.

External BEST / Euler-trail literature may be compared only **after** the native formula and normalization are frozen. Any such comparison is prior-art correspondence, not a premise or ontology grant.

---

# 3. Token-labeled lift

For finite `T`, create a proof-only labeled-token lift:

For every ordered packet pair `(x,y)` with multiplicity `T(x,y)=m`, replace the multiplicity by distinguishable proof tokens

`e_{x,y,1},...,e_{x,y,m}`.

These labels are proof bookkeeping only. They are not new native transition distinctions.

Let `LABELED_FIBER(T;s,t)` be token-labeled histories projecting to raw histories in `F(T;s,t)`.

Mandatory theorem target:

`|LABELED_FIBER(T;s,t)| = MU(T;s,t) * product_{x,y} T(x,y)!`

Prove this by showing that every raw history has exactly `product T(x,y)!` independent token assignments.

Self-loops, if admitted by the declared adjacency carrier, must be handled explicitly.

---

# 4. Rooted last-exit relational structure

Define a purely relational rooted last-exit structure for a realizable positive table.

Preferred convention:

- for open `s != t`, root at `t`;
- for closed `s=t` and `N_T>0`, root at `s`;
- each active non-root packet chooses exactly one outgoing **labeled transition token** as its designated last exit;
- the chosen last-exit tokens must form a directed relational arborescence toward the root: following chosen exits from every non-root active packet reaches the root and no directed cycle occurs among chosen exits.

Do not use metric/tree-length/geometric embedding language.

Let `TAU_r(T)` be the number of such token-level rooted last-exit structures.

Parallel transition multiplicity must contribute multiplicity to `TAU`; self-loops cannot serve as a last-exit arborescence arc unless a proof shows otherwise.

---

# 5. Candidate exact formulas — PROVE OR CORRECT, DO NOT ASSUME

Let:

`d_x = OUT_T(x) = sum_y T(x,y)`

and let products range only over the active finite packet set where required so no `(-1)!` expression is formed.

## 5.1 Open case `s != t`

Candidate:

`MU(T;s,t) = TAU_t(T) * [ product_x (d_x - 1 + 1[x=t])! ] / [ product_{x,y} T(x,y)! ]`

Equivalently, the root factor is `d_t!`, while every other active packet contributes `(d_x-1)!`.

## 5.2 Closed positive case `s=t`, `N_T>0`

Candidate:

`MU(T;s,s) = TAU_s(T) * d_s! * [ product_{x != s} (d_x-1)! ] / [ product_{x,y} T(x,y)! ]`

## 5.3 Zero-transition case

Retain Stage C exactly:

`T=0` is realizable iff `s=t`, and then `MU=1`.

The candidate formulas above are **targets**, not premises. If normalization/root convention is wrong, return an exact counterexample and freeze the corrected theorem.

---

# 6. Required self-contained proof architecture

A preferred proof route is a last-exit / local-order bijection.

For token-labeled histories:

1. extract the designated last outgoing token from each non-root packet;
2. prove those last exits necessarily form the rooted relational arborescence;
3. record the remaining local outgoing-token order at every packet;
4. prove this encoding is injective;
5. prove every admissible arborescence + local-order datum reconstructs exactly one token-labeled full history;
6. prove no premature dead-end or unused-token component can occur, using only the Stage-C realizability conditions and finite relational arguments;
7. count the local orders;
8. divide by `product T(x,y)!` using the labeled-to-raw theorem.

Do not silently import the BEST theorem to replace steps 1-8.

---

# 7. Mandatory exact regressions

At minimum verify symbolically / by exhaustive finite enumeration:

1. zero-transition identity;
2. one-transition open path;
3. immediate reversal `A-B-A`;
4. preferred Stage-C table
   - `A->B=B->A=A->C=C->A=1`, `s=t=A`, expected `MU=2`;
5. parallel-transition case
   - `T(A,B)=2`, `T(B,A)=1`, `s=A,t=B`, expected raw `MU=1`;
6. single-packet self-loop multiplicity `T(A,A)=m` for several small `m`, if reflexive adjacency is admitted: raw history should remain unique for fixed `m`;
7. a case with `MU>2`;
8. relabeling covariance;
9. reversal invariance consistency with Stage C.

Run bounded exhaustive enumeration on all finite realizable tables in a declared small registry and compare formula vs direct fiber cardinality. Finite exhaustive validation supports the proof; it does not replace the proof.

---

# 8. Integrality / divisibility

The final raw formula contains factorial denominators.

Prove that the resulting expression is always a nonnegative integer on realizable inputs, preferably as a direct consequence of the explicit labeled-history quotient/bijection rather than an independent divisibility trick.

Do not interpret the factorial denominator as probability.

---

# 9. Optional determinant lane — only after combinatorial theorem freeze

Only after the exact native combinatorial formula is proved may Stage D investigate whether `TAU_r(T)` admits a determinant/cofactor computation from a finite integer matrix.

If pursued:

- type determinant/Laplacian as an N2 computational readout;
- do not call it native geometry;
- prove the finite integer identity or clearly mark external theorem dependence;
- keep this optional lane subordinate to the last-exit combinatorial proof.

Do not allow determinant machinery to become a hidden premise of the fiber-count theorem.

---

# 10. External prior-art comparison

After the R059L formula is independently frozen, compare it with the classical BEST theorem / directed Euler-trail counting literature.

Record:

- whether the formulas correspond exactly after translating conventions;
- root convention;
- open vs closed normalization;
- treatment of parallel transitions;
- treatment of self-loops;
- difference between token-labeled trails and R059L raw packet histories.

Label this `EXTERNAL_PRIOR_ART_CORRESPONDENCE`, not native derivation.

---

# 11. Frozen semantic firewall

Strictly forbidden:

- LINE
- STRAIGHTNESS
- DISTANCE
- LENGTH
- SHORTEST PATH
- GEODESIC
- METRIC / `Q(a,b)`
- ANGLE / CURVATURE
- EDGE / BOUNDARY / AREA / VOLUME geometry
- physical flow / current / divergence interpretation
- path cancellation or quotienting raw histories
- probability / entropy interpretation of `MU`
- changing native path equality
- R057/R058S fitted geometry
- using external BEST theorem as the proof premise

`MU` remains an N2 fiber-cardinality diagnostic, not a packet weight or path weight.

C6 remains frozen at:

`C6_PASSAGE_COMPOSITION_NOT_YET_WELL_TYPED`

unless a separate Driver task changes its typing.

---

# 12. Required artifacts

Freeze at least:

1. `R059L_LABELED_TRANSITION_TOKEN_LIFT.json`
2. `R059L_RAW_LABELED_FIBER_FACTOR.json`
3. `R059L_LAST_EXIT_ARBORESCENCE_PROTOCOL.json`
4. `R059L_LABELED_FIBER_COUNT_FORMULA.json`
5. `R059L_RAW_MU_EXACT_FORMULA.json`
6. `R059L_OPEN_CLOSED_NORMALIZATION_LEDGER.json`
7. `R059L_FACTORIAL_INTEGRALITY_CERTIFICATE.json`
8. `R059L_STAGE_D_EXACT_COUNT_REGRESSION_RESULTS.json`
9. `R059L_STAGE_D_THEOREM_LEDGER.json`
10. `R059L_EXTERNAL_BEST_CORRESPONDENCE.json` if prior-art comparison is performed
11. deterministic Stage-D checker output
12. `R059L_STAGE_D_EXACT_FIBER_COUNT_CHECKPOINT.json`

The checker must hard-reject geometry leakage, probability/entropy interpretation, raw-history quotienting, external-theorem-as-premise, incorrect parallel-edge normalization, and formulas that fail the Stage-C `MU=2` witness.

Then stop for Driver review.
