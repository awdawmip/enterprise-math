# GEO6 Rotation–Kakeya Directional Coverage — Research Return

- Task: `RS-GEO6-ROTATION-KAKEYA-DIRECTIONAL-COVERAGE`
- Publication: `TP2-46A7AB0834EC4AA32869`
- Researcher: `EM-G6KAK-7B31E4`
- Claim: `chatgpt-g6kak-20260830-1115-7b31e4`
- Execution: `ER-B4793716DA78AF24BC67`
- Owner branch: `research/geo6-rotation-kakeya-directional-coverage-em-g6kak-7b31e4`
- P000 status: assumed and unchanged.
- Terminal research classification proposed for Driver review: `NEGATIVE_BOUNDARY`.

## 1. Hard-target disposition

The first rotation-native finite-scale coverage model has been exactly classified at the strongest presently justified **six-axis FCC-carrier readout** strength:

`CARRIER_S4_SIX_AXIS_COVERAGE_EXACTLY_CLASSIFIED / K_6(r)=6r-5 / FIXED_ORBIT_KAKEYA_DEGENERACY_PROVED / MIXED_OR_REFINING_NATIVE_DIRECTIONS_REQUIRED_FOR_NONDEGENERATE_CONTINUATION`.

This is not a theorem that the full native P000 direction space has only six directions. It is the exact result for the currently accepted six axis-type slots under the FCC carrier `S4` readout. The accepted global guard remains:

`CARRIER_S4 != FULL_NATIVE_P000_ROTATION_GROUP`.

The result therefore closes the naive first bridge and isolates the missing semantic ingredient rather than importing Euclidean direction space.

## 2. Evidence typing

### EXTERNAL_THEOREM / STATUS ONLY

The classical Kakeya set conjecture in `R^3` was proved by Hong Wang and Joshua Zahl in 2025; their paper is `arXiv:2502.17655`. Institute for Advanced Study reporting in 2025 explicitly notes that higher-dimensional Kakeya remains open. A 2026 streamlined proof/survey literature now exists as well.

None of those Euclidean results is used as a proof input below. Hausdorff dimension, Lebesgue measure, Euclidean angle and Euclidean tubes are not native primitives in this return.

### NATIVE_DEFINITION — DECLARED DOWNSTREAM BENCHMARK ONLY

The benchmark uses P000's six Cell-state slots together with the accepted FCC axis-type bridge

`AB, AC, AD, BC, BD, CD <-> E1,...,E6`

and the carrier action

`R_sigma(L_ij)=L_sigma(i)sigma(j)`.

The finite model is an explicit downstream Cell-relation model, not a claim that bare P000 is canonically `Z^6`.

### TRANSFER_THEOREM

Carrier `S4` permutes the six declared path relations transitively and preserves the exact support-cost problem. Existing `T7_FINITE_SYMMETRY_EQUIVARIANCE` is reused to certify the finite group action, the six-element orbit and the size-4 stabilizer of one axis type.

### OBSTRUCTION

For the six independent axis relations, the direction/shared-Cell overlap incidence graph is always a forest. Therefore total overlap defect is at most five and the exact optimum is `6r-5`. The fixed six-direction orbit has only linear support growth and cannot by itself express a nondegenerate higher-dimensional Kakeya compression problem.

A three-direction dependent countermodel `{e1,e2,e1+e2}` forms a genuine overlap cycle and beats the independent-axis formula. Thus the missing phenomenon is not “more optimization”; it is **direction circuits / mixed directions with separately justified native semantics**.

### COMPUTATIONAL_REGRESSION

`research_checks/GEO6_ROTATION_KAKEYA_DIRECTIONAL_COVERAGE_CHECK_20260830.py` verifies the carrier `S4` orbit/stabilizer, exact centered constructions at multiple refinement levels, a non-concurrent equality construction, the refinement identities and the dependent-direction adversarial countermodel.

## 3. Declared finite Cell model

Let the six direction labels be

`D={AB,AC,AD,BC,BD,CD}`.

For this benchmark define a Cell readout carrier

`C = Z^6`

with six undirected typed adjacency relations. Writing `e_d` for the basis vector assigned to direction label `d`, relation `H_d` joins `x` to `x+e_d` and `x-e_d`.

This is a combinatorial six-coordinate Cell relation. No inner product, norm or Euclidean length is used.

For a finite window `W_R=[-R,R]^6 intersect Z^6`, a length-`r` direction path is any finite set

`P_d(a,r)={a+t e_d : 0<=t<r}`

contained in the window. Reversing the path does not change its support, so the direction label is unoriented, matching the present unsigned carrier line-family status.

A full direction-coverage packet is a six-tuple

`P=(P_d)_{d in D}`

with one path from every carrier direction class. Its cost is

`cost(P)=| union_d P_d |`.

For a window large enough to contain the centered construction, define

`K_6(r)=min cost(P)`.

Because the optimization is over a finite window and a finite set of path placements, this is an exact finite optimization problem.

## 4. Rotation covariance

The accepted carrier algebra has `O_FCC ~= S4` at carrier-atlas strength and acts on the six K4-edge labels. Let `sigma in S4`. On Cell coordinate readouts let it permute coordinates by the induced edge permutation:

`(R_sigma x)_d = x_{sigma^{-1} d}`.

Then

`R_sigma(P_d(a,r)) = P_{sigma d}(R_sigma a,r)`.

Hence every carrier rotation sends an admissible six-direction packet to another admissible packet and preserves support cardinality.

The six labels form one orbit. Since `|S4|=24` and the orbit has size six, each direction stabilizer has size four. The deterministic checker verifies this through the accepted finite-symmetry tool rather than by introducing a new group package.

Again: this is carrier equivariance. It does not assert a universal native `S4` action on all P000 states.

## 5. Core theorem — overlap-cycle obstruction

### Theorem 5.1 — direction/shared-Cell incidence is acyclic

For any packet made from distinct basis-direction paths, construct a bipartite graph `B(P)`:

- left vertices are the six direction paths;
- right vertices are Cells covered by at least two paths;
- join direction `d` to shared Cell `x` iff `x in P_d`.

Then `B(P)` is a forest.

### Proof

Assume a simple cycle exists:

`d1 - x1 - d2 - x2 - ... - dk - xk - d1`.

For each `j`, the two distinct shared Cells adjacent to path `P_{d_j}` lie on the same typed axis path. Therefore

`x_j - x_{j-1} = lambda_j e_{d_j}`

for a nonzero integer `lambda_j` (indices cyclic).

Summing around the cycle gives

`0 = sum_j (x_j-x_{j-1}) = sum_j lambda_j e_{d_j}`.

The participating `e_{d_j}` are distinct members of the six coordinate basis vectors and are integer-linearly independent. Therefore every `lambda_j=0`, contradicting distinctness of the successive shared Cells. Thus no cycle exists. QED.

This is the structural reason the first model is easy: distinct-axis overlap cannot circulate.

## 6. Exact support optimum

For every shared Cell `x`, let `m_x` be the number of direction paths containing it. Since each of the six paths contains exactly `r` Cells,

`6r = |union_d P_d| + sum_x (m_x-1)`.

The second term is the overlap defect.

In the incidence forest, let `X` be the number of shared-Cell vertices and let `c` be the number of connected components after all six direction vertices are included. The forest has

`E = 6 + X - c`

incidence edges. But also

`E=sum_x m_x`.

Therefore

`sum_x(m_x-1)=E-X=6-c<=5`.

Hence every full packet satisfies

`cost(P)>=6r-5`.

### Upper construction

Choose all six paths to contain one common Cell `o` and otherwise move along their own six distinct axis relations. Their only common Cell is `o`, so

`cost = 1 + 6(r-1)=6r-5`.

Thus:

## Theorem 6.1 — exact six-axis directional coverage law

For every integer `r>=2` and every finite window large enough to contain the centered certificate,

`K_6(r)=6r-5`.

No numerical optimizer is needed to establish optimality; the checker only verifies the finite certificates and regressions.

### Equality is not the same as full concurrency

The proof gives a sharper characterization of the overlap accounting: equality occurs whenever the overlap-incidence forest is connected, so overlap defect reaches five. Full six-way concurrency is one symmetric minimizer but not the only one.

At `r=2`, an explicit chain of six direction paths can use five distinct pairwise intersection Cells and still attain support seven. The checker freezes this adversarial equality example. Thus a future theorem must not silently equate “optimal” with “all directions meet at one Cell.”

## 7. Exact finite levels and refinement

The first consecutive refinement levels are:

| path length `r` | exact minimum `K_6(r)` |
|---:|---:|
| 2 | 7 |
| 3 | 13 |
| 4 | 19 |

The scale law is exact:

`K_6(r+1)-K_6(r)=6`.

A convenient renormalization identity is

`K_6(2r-1)=2K_6(r)-1`.

So the fixed six-axis direction family has linear support growth with exact slope six.

This is a genuine nontrivial lower/upper classification, but it is also the key obstruction to treating this fixed orbit as a deep six-dimensional Kakeya analogue: the number of direction classes does not grow with resolution and the overlap graph cannot sustain a circuit.

## 8. Adversarial dependent-direction countermodel

The linear independence hypothesis is not cosmetic.

Inside the first two coordinates take three direction vectors

`v1=e1`, `v2=e2`, `v3=e1+e2`.

At `r=2`, choose the three supports

- `{0,e1}`;
- `{e1,e1+e2}`;
- `{0,e1+e2}`.

Their union has only three Cells. The direction/shared-Cell incidence graph is a six-cycle. The cycle closes because

`e1 + e2 - (e1+e2)=0`.

For three independent directions the forest formula would give

`3*2-(3-1)=4`,

so the dependent direction circuit strictly improves compression to three.

This countermodel establishes the exact failure boundary of Theorem 6.1:

`INDEPENDENT_AXIS_DIRECTION_ORBIT -> OVERLAP_FOREST`,

while

`DIRECTION_CIRCUIT -> OVERLAP_CYCLE_POSSIBLE`.

It does **not** prove that every dependent direction family yields a useful Kakeya model. It proves only that dependence is a necessary opening through which non-tree overlap can enter.

## 9. Why this matters for P000

The task began with the idea that “rotation is primary” should have a measurable support cost. The minimal accepted carrier orbit does provide such a cost, but the answer is rigid:

`K_6(r)=6r-5`.

Therefore the naive first route is now classified and should not be repeatedly optimized. Its limitation is structural, not computational.

A nondegenerate continuation must add at least one of the following, with separate native justification:

1. a scale-dependent family of direction classes `D_r` whose cardinality genuinely grows under refinement;
2. mixed direction relations not equivalent to merely permuting the six basis slots;
3. a state-level/native rotation lift that creates additional admissible path types while respecting P000 and the existing carrier/native separation;
4. a typed gluing rule whose new direction circuits survive the native legality conditions.

The dependent triangle shows what to look for: a first exact direction circuit whose path overlap closes without importing an external Euclidean angle or continuum direction sphere.

This also links naturally to, but does not silently invoke, the existing `T3_TYPED_INCIDENCE_CIRCUIT` boundary: a future mixed-direction task should explicitly establish the direction relation before promoting any circuit calculus. The present result stays task-local.

## 10. External Kakeya comparison boundary

The classical Kakeya problem asks for sets containing a unit line segment in every Euclidean direction and studies continuum size/dimension. The present model has a fixed six-element carrier direction orbit and exact finite support.

Consequently:

- `K_6(r)=6r-5` is **not** a new bound for classical Kakeya;
- it does not imply a Hausdorff-dimension statement;
- the 2025 Wang–Zahl theorem is not used to prove it;
- higher-dimensional classical openness does not imply P000 openness at the same statement;
- the result is a native-model pressure test showing which discrete ingredient is missing before a serious analogy is justified.

## 11. Tool reuse / method harvest

Current toolbox lookup was performed before constructing the checker.

Reused:

- `T7_FINITE_SYMMETRY_EQUIVARIANCE` for finite action/orbit/stabilizer validation.

Consulted boundary:

- `T3_TYPED_INCIDENCE_CIRCUIT`: the present direction-cycle observation is not promoted to a new global tool because the registry explicitly warns that a direction-only signed circuit is not automatically derived.

No new reusable global tool is claimed. `method_harvest=RESULT_ONLY`.

## 12. Deterministic artifacts

- `research_checks/GEO6_ROTATION_KAKEYA_DIRECTIONAL_COVERAGE_CHECK_20260830.py`
- `research_artifacts/GEO6_ROTATION_KAKEYA_DIRECTIONAL_COVERAGE/coverage_certificate_v1.json`

The checker covers:

1. all 24 carrier `S4` permutations on the six direction labels;
2. one six-element direction orbit;
3. stabilizer size four for `AB`;
4. centered exact upper certificates for `r=2,...,8`;
5. overlap defect five and exact support `6r-5`;
6. the non-concurrent `r=2` equality chain;
7. refinement and renormalization identities;
8. the dependent-direction triangle where the overlap forest mechanism correctly fails.

## 13. Unresolved residue

`FULL_P000_NATIVE_DIRECTION_FAMILY_BEYOND_CARRIER_S4_UNRESOLVED`.

The current Foundation does not grant that the full native P000 rotation/direction structure is exactly the six carrier axes, nor does it yet grant a canonical scale-dependent mixed direction family. Therefore this return must not be promoted as a universal bare-P000 Kakeya theorem.

The exact residue is now narrower:

**Find the first native-legal mixed/refining direction orbit that contains a genuine direction circuit, then determine whether its overlap compression survives two refinement levels and remains equivariant under the actually granted rotation action.**

That is the next mathematically informative point. Re-running optimization on the fixed six-axis carrier orbit is not.

## 14. Proposed control-plane recommendation

Driver review this result as a terminal negative boundary for the first fixed-orbit bridge. Preserve:

- exact law `K_6(r)=6r-5`;
- overlap-incidence forest theorem;
- equality-via-connected-overlap, not forced concurrency;
- dependent-direction triangle as the mandatory regression against overgeneralizing the lower bound;
- carrier/native rotation separation.

If a successor is justified, scope it narrowly to **native mixed/refining direction-circuit construction** rather than another finite optimization of the same six basis directions.
