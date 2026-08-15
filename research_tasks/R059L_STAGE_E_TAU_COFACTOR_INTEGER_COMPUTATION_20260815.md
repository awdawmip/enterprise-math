# RS-R059L — STAGE E TAU COFACTOR / INTEGER DETERMINANT COMPUTATION

Task-ID: `RS-R059L-STAGE-E-TAU-COFACTOR-INTEGER-COMPUTATION`
Generation: `R059L`
Status: `DRIVER_APPROVED_TASKBOOK`
Identity-lane: `R059L`
Date: `2026-08-15`
Driver: `EM-DVR-R0457K / CONTROL_PLANE`

## 0. Frozen parent

Stage D is frozen at owner head:

`6c6d8b8a8d184f73ebf8e262bf09e1d61660c871`

Stage 0 / A / B / C / D frozen artifacts are immutable.

Stage D already proved, natively and without external theorem premises, for positive realizable finite `T`:

`MU(T;s,t)=TAU_r(T) * d_r! * product_{x in ACTIVE(T), x!=r}(d_x-1)! / product_{x,y}T(x,y)!`

where `r=t` for `s!=t`, and `r=s` for positive closed `s=t`.

Stage E must not alter that theorem. It studies only the exact computation of `TAU_r(T)`.

---

# 1. Scientific question

Stage D defines `TAU_r(T)` by a multiplicity-weighted sum over rooted last-exit parent maps. That definition is exact but may require combinatorial enumeration.

Stage E asks:

> Can `TAU_r(T)` be computed exactly as a cofactor/determinant of a finite integer matrix built only from transition multiplicities, and can that identity be proved self-contained from finite determinant algebra rather than imported as the matrix-tree theorem?

This is an N2 exact-computation problem. It does not promote matrices, determinants, trees, or graph terminology into N0 ontology.

---

# 2. Loop-cancelled transition matrix

For a positive realizable finite table `T`, let `A=ACTIVE(T)` and root `r` be the frozen Stage-D root.

Define an integer matrix `K(T)` indexed by `A`:

for `x != y`:

`K[x,y] = -T(x,y)`

and

`K[x,x] = sum_{y in A, y!=x} T(x,y)`.

Equivalently, if full outgoing count includes self-loops, the self-loop contribution is cancelled from the diagonal arborescence matrix.

This is mandatory because Stage D proved that a self-loop cannot be a non-root last-exit arborescence token.

Let `K^(r)` be the matrix obtained by deleting row `r` and column `r`.

Convention:

`det(empty 0x0 matrix)=1`.

That convention must cover a single active root with only self-loop transitions.

---

# 3. Primary theorem target

Prove or correct:

`TAU_r(T) = det(K^(r))`.

The theorem target uses the same multiplicity-weighted `TAU_r(T)` frozen in Stage D:

`TAU_r(T)=sum_p product_{x!=r} T(x,p(x))`

over parent maps whose iterates reach `r`.

Parallel transition multiplicities must therefore appear as integer weights in the determinant identity.

If the row/column convention, sign, root deletion, or diagonal definition above is wrong, give an exact counterexample and freeze the corrected formula. Do not tune conventions merely to match a regression table.

---

# 4. Native-first proof requirement

The proof must be self-contained inside finite integer/combinatorial algebra.

Forbidden as proof premise:

- matrix-tree theorem;
- Kirchhoff theorem;
- BEST theorem;
- external graph-counting results.

A preferred route is a determinant-expansion / cancellation certificate:

1. expand the reduced determinant exactly;
2. expand each diagonal factor into a sum of outgoing multiplicities;
3. identify every monomial with a finite parent-choice / functional-relation datum;
4. construct an explicit sign-reversing or otherwise exact cancellation for data containing a non-root directed cycle;
5. prove the uncancelled data are exactly the rooted parent maps whose iterates reach `r`;
6. prove each surviving datum has coefficient `+1` and weight `product T(x,p(x))`.

Another self-contained finite proof is allowed, but it must expose why cyclic non-root parent structures cancel and rooted structures survive.

External matrix-tree terminology may be added only after the native proof is frozen, as `EXTERNAL_PRIOR_ART_CORRESPONDENCE`.

---

# 5. Exact MU cofactor formula

After `TAU_r(T)=det(K^(r))` is proved, substitute it into frozen Stage D and freeze the direct formula:

For positive realizable finite `T`:

`MU(T;s,t)=det(K^(r)) * d_r! * product_{x in A, x!=r}(d_x-1)! / product_{x,y}T(x,y)!`.

Keep Stage-C zero branch unchanged:

- if `T=0` and `s=t`, `MU=1`;
- if `T=0` and `s!=t`, `MU=0`.

Do not call this a probability, entropy, metric, action, or physical weight.

---

# 6. Exact integer computation protocol

Implement an exact deterministic computation of `det(K^(r))` using integer arithmetic only.

Preferred:

- fraction-free Bareiss elimination, or
- another exact integer/rational algorithm with a fully specified normalization.

Forbidden:

- floating-point determinant as theorem evidence;
- tolerance-based rounding to an integer;
- numerical linear algebra whose exact sign/value depends on floating error.

Record:

- matrix dimension `q=|ACTIVE(T)|-1`;
- arithmetic-operation complexity;
- integer intermediate-value behavior / exactness notes;
- special handling of `q=0`.

Do not overclaim bit-complexity if not proved.

---

# 7. Mandatory regressions

At minimum verify parent-map `TAU`, exact cofactor, and final `MU` agree on:

1. zero-transition identity via separate branch;
2. one-transition open path;
3. immediate reversal `A-B-A`;
4. preferred `MU=2` table;
5. Stage-D parallel normalization case `T(A,B)=2,T(B,A)=1`;
6. single-packet self-loop multiplicities `m=1,2,3` if reflexive adjacency is declared;
7. non-root self-loop case;
8. Stage-D bidirected-triangle `MU=6` case;
9. a case with at least four active packets;
10. relabeling covariance under simultaneous row/column permutation.

Run bounded exhaustive comparison of:

`parent-map TAU == exact cofactor TAU`

on a declared finite registry. Prefer at least all 3-packet tables through the Stage-D bounded range plus an independent bounded 4-packet registry if computationally reasonable.

Enumeration is validation, not proof.

---

# 8. Reversal consistency

Stage C froze:

`MU(T;s,t)=MU(T^T;t,s)`.

After the cofactor formula is proved, verify the determinant-factorial formulas on `T` and `T^T` agree on all regression cases.

Do not assume individual matrix entries or cofactors are equal merely because the final `MU` is equal. If an exact relation between the two rooted cofactors follows from the endpoint-balance law, prove it separately; otherwise report only formula-level consistency.

No spatial-opposition interpretation is allowed.

---

# 9. Semantic firewall

Continue to forbid:

- LINE / STRAIGHTNESS;
- DISTANCE / LENGTH;
- SHORTEST PATH / GEODESIC;
- METRIC / `Q(a,b)`;
- EDGE / BOUNDARY / AREA / VOLUME;
- ANGLE / CURVATURE / VECTOR DISPLACEMENT;
- physical flow / current / divergence interpretation;
- path cancellation / raw-history quotient;
- probability or entropy interpretation of `MU`;
- R057/R058S fitted geometry;
- C6 passage-composition repair.

`C6_PASSAGE_COMPOSITION_NOT_YET_WELL_TYPED` remains frozen.

Determinant/cofactor is an exact downstream computation of an already-derived relational count, not N0 ontology.

---

# 10. Required artifacts

Freeze at least:

1. `R059L_TAU_INTEGER_MATRIX_PROTOCOL.json`
2. `R059L_TAU_COFACTOR_THEOREM.json`
3. `R059L_DETERMINANT_CYCLE_CANCELLATION_CERTIFICATE.json`
4. `R059L_EXACT_INTEGER_DETERMINANT_PROTOCOL.json`
5. `R059L_MU_COFACTOR_EXACT_FORMULA.json`
6. `R059L_COFACTOR_REVERSAL_RELABELING_AUDIT.json`
7. `R059L_STAGE_E_REGRESSION_RESULTS.json`
8. `R059L_STAGE_E_THEOREM_LEDGER.json`
9. `R059L_STAGE_E_CHECKER_OUTPUT.json`
10. `R059L_STAGE_E_TAU_COFACTOR_CHECKPOINT.json`

Checker must hard-reject at least:

- external matrix-tree theorem used as native proof premise;
- diagonal including uncancelled self-loop weight;
- wrong root deletion;
- floating determinant + rounding;
- simple-support rather than multiplicity-weighted matrix;
- determinant promoted to N0 ontology;
- MU as probability/entropy;
- raw-history quotient/cancellation;
- geometry leakage;
- C6 untyped repair.

Return hashes and stop for Driver review.

---

# 11. Completion disposition

If the cofactor theorem and direct exact `MU` formula are proved with exact integer computation and regressions:

return

`R059L_PATH_COLLAPSE_COUNTING_KERNEL_COMPLETE_CANDIDATE`

and stop.

This does not authorize geometry. It only marks that the current packet/path lane has reached an exact native-history -> transition-table -> fiber-cardinality computation kernel.

If the determinant target is false under the frozen Stage-D `TAU`, return an exact counterexample and corrected weakest theorem instead.
