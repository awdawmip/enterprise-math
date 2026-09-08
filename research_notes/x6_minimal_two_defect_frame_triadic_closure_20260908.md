# X6 minimal-2 correspondence, 120-degree defect frame, and triadic closure

Status: `RESEARCH_NOTE / DURABLE FRONTIER / NONCANONICAL / NOT_FOUNDATION / NOT_WORKING_TRUTH`
Date: `2026-09-08`
Scope: `Enterprise Math / P000 X6 / natural-number geometry / Nollm multiplicative-memory bridge`
Parent: `research_notes/x6_count_metric_split_rotating_index_closure_20260908.md`
EM source snapshot before write: `awdawmip/enterprise-math@7438a37daeb18545727a413cc0a0f74222f9cb19`
Global control snapshot observed before write: `awdawmip/chatgpt-global-knowledge@8ed9e71ccdb877e8358154acabe69f8e33466e87`

## 0. Purpose and strength

This continuation attacks the smallest unresolved unit from the parent note:

- among the 63 index-2 branches of `Z^6`, determine which branches are selected by minimum native quadratic anisotropy;
- derive an exact defect-composition coordinate rather than using only the scalar `Delta_6`;
- classify the shortest exact rotation schedule from arithmetic index `2` to isotropic closure;
- test whether the observed arity-three / `120 degree` resonance is an exact derived relation or only numerology.

The result is substantially stronger than the parent heuristic. Under the current P000 X6 integer-coordinate/quadratic-readout model:

1. the least-anisotropic determinant-2 maps are classified exactly;
2. their branches are precisely the 15 Hamming-weight-2 index-2 branches;
3. their centered logarithmic strain directions form an `S6`-symmetric tight frame in the centered six-axis space;
4. three disjoint minimal branches form an equal-norm zero-sum triad with pairwise angle exactly `120 degrees`;
5. in even dimension `d=2r`, the analogous closure has `r=d/2` branches and pairwise cosine `-1/(r-1)`, so the angle is `120 degrees` iff `d=6`;
6. there is no `S6`-equivariant deterministic next-branch selector without extra state;
7. the branch-schedule matching complex has nontrivial global loop space even though every legal two-step partial matching has a unique third local closure.

These are derived observer/transport theorems under P000. They do **not** identify centered log strain with primitive physical force, and do not alter P000 `TRIADIC_CLOSURE_E`.

## 1. Foundation and BRC carrier

Use the admitted P000 X6 carrier

`X6_NATIVE_SPATIAL = AFFINE_TORSOR(Z^6)`

with native component quadratic readout

`L_E(z)^2 = sum_i z_i^2`.

For an integer full-rank transport

`A in M_6(Z)`, `G(A)=A^T A`,

its Coverage/index is

`n=|det A|`.

The exact transport state must retain at least

`(n, branch, A, G, ordered schedule provenance)`

when future composition is allowed.

Scalar anisotropy, singular values, centered strain, orbit type and final Coverage are observers of this richer carrier.

BRC resolution: `COMPOSE_APPLIED` using `T0_BRC`, `T6_OPERATION_SAFE_QUOTIENT`, `T7_FINITE_SYMMETRY_EQUIVARIANCE`, `T8_RELATION_OBSERVABLE_SPECTRUM`, and the holonomy/gluing viewpoint of `T9` where global schedule loops are discussed.

## 2. The sixth-root scale is determinant-forced, not an isotropy ansatz

Let the singular values of a full-rank `A in M_6(Z)` be

`sigma_1,...,sigma_6 >0`.

Then exactly

`product_i sigma_i = |det A| = n`.

Therefore their geometric mean is

`GM(A)=(product_i sigma_i)^(1/6)=n^(1/6)`.

So

`rho_6(n)=n^(1/6)`

is the exact **volume-equivalent linear-scale observer of every index-n transport**, not merely of an ideal isotropic map.

Anisotropy is the repair information describing how the six individual `sigma_i` differ around this forced mean.

This strengthens the parent note:

`SIXTH_ROOT_SCALE = DERIVED_FROM_X6_DIMENSION + INDEX/DETERMINANT`,

conditional only on using lattice index/Coverage as the multiplicative arithmetic carrier.

In general dimension d,

`GM_d(A)=|det A|^(1/d)`.

The ordinary number line is the special `d=1` case where count/index and linear scale coincide.

## 3. General determinant-2 anisotropy minimum in dimension d

For `A in M_d(Z)` let

`G=A^T A`

and define

`Delta_d(A)=d tr(G^2)-tr(G)^2`.

Writing `d_i=g_ii`,

`Delta_d(A)`

`= sum_(i<j)(d_i-d_j)^2 + 2d sum_(i<j) g_ij^2`.

Assume `|det A|=2`, so

`det G=4`.

For every `d>=3`,

`boxed: Delta_d(A) >= 2(d-2)`.

Proof:

- if any integer off-diagonal `g_ij` is nonzero, its contribution alone is at least `2d > 2(d-2)`;
- hence any competitor below the claimed bound would have diagonal G;
- positive integer diagonal entries with product 4 are, up to permutation, either `(4,1,...,1)` or `(2,2,1,...,1)`;
- their defects are respectively `9(d-1)` and `2(d-2)`.

Thus the second pattern is optimal.

For P000 `d=6`, this gives the parent result

`Delta_6,min(2)=8`.

## 4. Equality classification: the natural minimum-defect 2-branches are exactly weight 2

Suppose `d=6`, `|det A|=2`, and

`Delta_6(A)=8`.

The proof above shows necessarily

`G=A^T A`

is diagonal with multiset

`(2,2,1,1,1,1)`.

Therefore four columns of A are integer vectors of norm 1 and hence signed standard basis vectors. After signed row/column permutations they occupy four coordinate axes.

The remaining two columns:

- lie entirely in the complementary two-coordinate plane;
- each have squared norm 2;
- are orthogonal.

Hence, again up to signed row/column permutations, their 2x2 block is one of the standard determinant-2 conformal blocks, e.g.

`H2=[[1,1],[1,-1]]`

or the orientation-preserving variant

`C2=[[1,-1],[1,1]]`.

Both satisfy

`B^T B=2 I_2`, `|det B|=2`.

The image sublattice in that axis pair is exactly the parity relation

`x_i == x_j (mod 2)`,

whose defining nonzero functional in `F_2^6` is

`e_i+e_j`.

Thus:

`boxed: MINIMUM-DEFECT INDEX-2 BRANCH <=> HAMMING WEIGHT 2`.

There are exactly

`binom(6,2)=15`

such branches.

This reduces the full 63-branch projective family to a distinguished 15-branch orbit **only after declaring the minimum-anisotropy observer**. It does not erase the other 48 index-2 branches globally.

The 15 branches may be identified with the 15 edges of the complete graph `K6` on the native axis labels.

## 5. Canonical centered log-strain direction of a minimal 2-event

For a minimum-defect branch `e={i,j}`, the singular values are

`sqrt(2), sqrt(2), 1,1,1,1`.

Let `chi_e in {0,1}^6` be the indicator of its two supported axes.

The log singular-value vector is

`ell_e=(ln 2)/2 * chi_e`.

Its mean coordinate is forced by determinant 2:

`bar(ell)=(ln 2)/6`.

Define the centered log-strain defect

`s_e = ell_e - bar(ell) * 1`

`    = (ln 2)/6 * d_e`,

where the exact integer defect direction is

`d_e = 3 chi_e - 1`.

Thus `d_e` has value 2 on the two loaded axes and -1 on the other four.

It lies in the centered hyperplane

`A5_R={x in R^6 : sum_i x_i=0}`.

This is a richer oriented anisotropy observer than scalar `Delta_6`, though full matrix A is still required for arbitrary noncommuting composition.

## 6. Exact defect inner products and the 120-degree law

For two weight-2 branches e,f,

`d_e dot d_f = 9 |e intersect f| - 6`.

Therefore:

- `e=f`: inner product `12`;
- distinct branches sharing one axis: inner product `3`;
- disjoint branches: inner product `-6`.

Every defect vector has

`||d_e||^2=12`.

Hence for disjoint e,f,

`cos angle(d_e,d_f) = -6/12 = -1/2`,

so

`boxed: angle(d_e,d_f)=120 degrees`.

Thus the negative-correlation relation inside the minimum-defect 2-field is exactly the disjoint-edge relation.

This gives an intrinsic rotation rule without referring to axis labels:

`NEXT MINIMAL 2-BRANCH IS TRIAD-COMPATIBLE <=> DEFECT INNER PRODUCT < 0`.

For a fixed e there are exactly six such f.

## 7. Perfect matchings are exactly the zero-sum 120-degree defect triads

Take three weight-2 branches `e,f,g`.

Because

`d_e+d_f+d_g = 3(deg_1-1,...,deg_6-1)`,

where `deg_i` is the number of selected edges incident to axis i,

we have

`d_e+d_f+d_g=0`

iff every axis has degree exactly one.

With three 2-sets on six axes, this is equivalent to

`{e,f,g}` being a perfect matching of K6.

Therefore:

`boxed: ZERO-SUM DEFECT TRIAD <=> PERFECT MATCHING}`.

For such a triad the three vectors are:

- equal norm;
- pairwise 120 degrees;
- exactly zero-sum.

Example:

`d_12=(2,2,-1,-1,-1,-1)`,

`d_34=(-1,-1,2,2,-1,-1)`,

`d_56=(-1,-1,-1,-1,2,2)`,

and

`d_12+d_34+d_56=0`.

This is an exact **observer-level triadic 120-degree closure theorem** under P000 X6.

Strength boundary:

`CENTERED LOG-STRAIN TRIADIC CLOSURE != PRIMITIVE FORCE TRIADIC_CLOSURE_E`.

A physical/dynamical bridge would still be required to identify them.

## 8. The 2 -> 4 -> 8 binary closure ladder

Fix a perfect matching `M={e,f,g}` and apply one minimum-defect determinant-2 map on each pair plane.

Stage 1 — arithmetic index 2:

- singular values: `sqrt(2)` on 2 axes, `1` on 4;
- geometric mean: `2^(1/6)`;
- centered defect: `s_e`.

Stage 2 — arithmetic index 4, using a disjoint second pair:

- singular values: `sqrt(2)` on 4 axes, `1` on 2;
- geometric mean: `4^(1/6)=2^(1/3)`;
- centered defect:

`s_e+s_f=-s_g`.

Thus the anisotropy at 4 is exactly the negative of the missing third 2-event.

Stage 3 — arithmetic index 8:

- singular values: `sqrt(2)` on all six axes;
- geometric mean: `8^(1/6)=sqrt(2)`;
- centered defect:

`s_e+s_f+s_g=0`.

The total Gram matrix is

`2 I_6`.

So:

`2 CREATES A MINIMAL TWO-AXIS DEFECT`,

`4 CARRIES THE ANTI-DEFECT OF THE REMAINING PAIR`,

`8 CLOSES EXACTLY TO ISOTROPY`.

The scalar `Delta_6` reads `8,8,0` over these three stages; the oriented strain state explains why the same scalar defect at stages 1 and 2 has opposite completion meaning.

## 9. Dimension-general theorem: six dimensions force triadic 120-degree closure

Now let the ambient dimension be even:

`d=2r`.

A minimum-defect determinant-2 event again has singular values

`sqrt(2),sqrt(2),1,...,1`

and is supported on one coordinate pair.

Its centered log-strain direction, ignoring the common scalar `(ln2)/2`, is

`u_e = chi_e - (2/d) 1`.

For disjoint e,f:

`u_e dot u_f = -4/d`,

`||u_e||^2 = 2(d-2)/d`.

Hence

`cos theta = -2/(d-2)`

`          = -1/(r-1)`.

A perfect matching contains exactly r disjoint pair events, their centered strains sum to zero, and they form a regular `(r-1)`-simplex.

Therefore:

`PAIRWISE CLOSURE ANGLE = arccos[-1/(r-1)]`.

In particular

`theta=120 degrees`

iff

`-1/(r-1)=-1/2`

iff

`r=3`

iff

`d=6`.

Thus within this minimum-index-2 centered-strain framework:

`boxed: SIX DIMENSIONS <=> THREE-BRANCH SIMPLEX CLOSURE <=> 120-DEGREE PAIRWISE ANGLE`.

This is a strong internal-consistency bridge between P000's six-dimensional ontology and its triadic/120-degree structural motif. It is not a proof or replacement of P000.

A second derivation of the same arity comes from determinant counting. Exact scale `sqrt(2)` isotropy in dimension `d=2r` has determinant

`(sqrt(2))^d = 2^r`.

Each minimal event has determinant 2, so exactly r such events are required. For d=6, exactly three determinant-2 events are necessary.

## 10. The full 15-branch minimal-2 field is already isotropic as a relation

The 15 integer defect directions are not an arbitrary orbit. They satisfy

`sum_e d_e = 0`.

Moreover

`sum_e d_e d_e^T = 36 P_center`,

where

`P_center = I_6 - (1/6) 11^T`

is the orthogonal projector onto the centered hyperplane `A5_R`.

Proof: direct counting gives diagonal entries 30 and off-diagonal entries -6; this is exactly `36 P_center`.

Consequences:

- the uniform 15-branch relation has zero mean anisotropy direction;
- its second moment is exactly isotropic on the five-dimensional centered defect space;
- the normalized 15 directions form a finite equal-norm tight frame (equivalently a spherical 2-design at the first/second-moment level).

The branch indicators `chi_e` are the 15 vertices of the hypersimplex `Delta(2,6)`; the defect field is its centered/scaled realization.

Therefore arithmetic 2 has a natural `S6`-symmetric geometric representation **as the whole minimum-defect correspondence**, even though no single minimum-defect branch is S6-invariant.

This is a direct structural reason not to identify 2 with one selected Cell or one selected direction.

## 11. Exact closure graph and the 15 -> 6 -> 1 rule

Put a graph on the 15 minimal branches by joining e and f iff they are disjoint, equivalently iff

`d_e dot d_f < 0`.

This is the Kneser graph

`KG(6,2)`.

Exact finite data:

- vertices: 15;
- degree: 6;
- adjacent pair common neighbors: 1;
- nonadjacent distinct pair common neighbors: 3.

Thus it is strongly regular with parameters

`(15,6,1,3)`.

Every allowed two-step partial matching e,f has exactly one branch g disjoint from both: the complementary pair on the remaining two axes.

Hence the exact closure protocol is

`FIRST BRANCH: 15 choices`,

`SECOND 120-DEGREE / DISJOINT BRANCH: 6 choices`,

`THIRD CLOSING BRANCH: 1 forced choice`.

There are

`15*6=90`

ordered three-step closure histories.

Because order within a perfect matching does not matter for disjoint pair-supported maps, these 90 histories recoalesce to

`90 ordered path histories -> 15 perfect-matching transports -> 1 isotropic Gram state 2I_6`.

This is an exact BRC provenance hierarchy.

## 12. No S6-equivariant deterministic next-branch selector

Let E be the 15-edge minimum-defect branch set.

There is no map

`F:E->E`

such that

1. `F(e)` is disjoint from e for every e;
2. F is equivariant under the full axis-permutation `S6` action.

Proof. Fix e. Its stabilizer contains an `S4` acting on the four complementary axes. That `S4` acts transitively on the six edges disjoint from e. Hence no disjoint edge is fixed by the stabilizer. Equivariance would require `F(e)` to be stabilizer-fixed, contradiction.

Likewise, the three perfect matchings containing a fixed e are permuted transitively by the complementary `S4`; there is no canonical matching containing e without extra state.

Therefore an exact natural schedule must do at least one of:

- preserve the six-way next-branch relation;
- carry additional orientation/history/port state that breaks the stabilizer;
- explicitly reduce the symmetry group.

`UNIQUE NEXT BRANCH + FULL S6 + NO EXTRA STATE` is impossible.

This is a finite symmetry obstruction, not an implementation preference.

## 13. Local triadic closure does not globally trivialize schedule topology

Form the simplicial matching complex `M_6`:

- its 15 vertices are minimal weight-2 branches;
- its 45 edges are unordered disjoint branch pairs;
- its 15 triangles are perfect matchings / exact triadic closures.

Every disjoint pair belongs to exactly one perfect matching triangle, because four used axes leave one unique complementary pair.

Thus the 15 triangle boundaries have disjoint edge supports and are linearly independent.

The 1-skeleton is connected, so over the integers:

`rank boundary_1 = 14`,

`rank boundary_2 = 15`.

Hence

`H_0(M_6;Z) ~= Z`,

`H_1(M_6;Z) ~= Z^16`,

`H_2(M_6;Z) = 0`.

So the local 120-degree triangles do not make the global schedule space simply connected. There remain 16 independent first-homology loop directions.

BRC / holonomy interpretation:

- local perfect-matching closure is exact;
- global branch-history/path dependence is not thereby erased;
- any attempt to quotient the schedule to local closure state alone must prove that the intended future operations are insensitive to these global loops or retain a repair/holonomy coordinate.

No physical meaning is assigned to the number 16 here.

## 14. Count-versus-linear-coordinate inversion

The exact volume-equivalent scale law gives

`rho_6(n)=n^(1/6)`

and inverse

`n=rho^6`.

Therefore a literal isotropic **linear scale 2** represents arithmetic Coverage/count

`2^6=64`,

not arithmetic count 2.

This is a concise explanation of why the ordinary point `x=2` is not the native X6 realization of arithmetic 2.

The first exact shell landing after 1 is arithmetic 8 at radius `sqrt(2)`; the first integer linear scale 2 occurs at arithmetic 64.

More generally exact shell landings occur at cubes `k^3`, and their natural density among positive integers is zero:

`# {k^3<=N}/N ~ N^(-2/3) -> 0`.

The gap between consecutive exact shell-landing counts is

`(k+1)^3-k^3 = 3k^2+3k+1`,

which diverges.

Hence shell-only point snapping has growing arithmetic fibers and cannot be a lossless natural-number carrier.

## 15. Consequence for the meaning of geometric 2

The strongest current typed picture is:

**Arithmetic identity:**

`1+1=2` remains exact.

**Volume-equivalent scale:**

`rho_6(2)=2^(1/6)` is determinant-forced.

**Exact native integer transport:**

one-step index 2 cannot be isotropic.

**Minimum-defect geometric realization:**

2 is naturally a 15-branch `S6` correspondence of pair-supported transports.

**Branch defect geometry:**

the 15 centered defect directions form a tight frame; disjoint/negatively-correlated directions meet at exactly 120 degrees.

**Multiplicative closure:**

three 2-events on one perfect matching close at arithmetic 8 to exact isotropy.

Thus the current evidence favors

`NATURAL INTEGER = EXACT ARITHMETIC COUNT/INDEX + GEOMETRIC FIBER/RELATION`,

not

`NATURAL INTEGER = UNIQUE LINEAR POINT`.

## 16. Immediate Nollm architecture implication

A P000-aware multiplicative memory field should not force a unique Cell for arithmetic 2.

A first exact layered candidate is:

1. arithmetic carrier `n` and prime valuations;
2. index/Coverage branch relation;
3. minimum-defect branch orbit when a geometric selector criterion is invoked;
4. determinant-forced scale `n^(1/6)`;
5. centered strain / full transport repair state;
6. branch schedule on the exact closure graph;
7. local 120-degree completion when compatible;
8. global path/holonomy state retained until an observer-safe quotient is proved;
9. final physical Cell/Q16 projection only downstream.

The current 2D Nollm `sqrt(n)` observer remains a separate rank-2 physical/shape surface and is not overwritten by this X6 law.

## 17. Tool and observer-safety audit

`T0_BRC`: `REUSE_APPLIED`.

- 90 ordered schedules, 15 matching transports and one final Gram state are explicitly distinguished.
- endpoint/Gram/isotropy compression is not used to reconstruct lost path order.

`T6_OPERATION_SAFE_QUOTIENT`: `REUSE_APPLIED`.

- scalar `Delta_d` is used only for minimization;
- centered strain retains defect orientation for the commuting matching closure;
- full A remains required outside the safe commuting/disjoint scope.

`T7_FINITE_SYMMETRY_EQUIVARIANCE`: `REUSE_APPLIED`.

- the 15-branch `S6` orbit is classified;
- the no-equivariant-selector obstruction is exact.

`T8_RELATION_OBSERVABLE_SPECTRUM`: `COMPOSE_APPLIED`.

- arithmetic 2 is treated as a multivalued minimum-defect geometric relation when the minimum-anisotropy observer is declared.

`T9_HOLONOMY_COCOYCLE_GLUING`: `COMPOSE_APPLIED` at the abstract schedule level.

- local triangle closure is distinguished from global `H_1 ~= Z^16` path structure;
- no physical holonomy theorem is claimed yet.

No new top-level tool family is proposed.

## 18. Status ledger

Exact proved derivations under the declared X6/index model:

- `n^(1/6)` is the singular-value geometric mean of every index-n transport;
- general determinant-2 lower bound `Delta_d>=2(d-2)` for `d>=3`;
- equality classification in X6;
- minimum-defect index-2 branches are exactly the 15 weight-2 branches;
- exact centered defect formula `d_e=3chi_e-1`;
- exact two-distance inner-product law;
- disjoint minimal branches meet at 120 degrees in X6 centered strain space;
- zero-sum defect triples are exactly perfect matchings;
- 2->4->8 centered-strain cancellation;
- even-dimension regular-simplex closure law and `120 degrees iff d=6`;
- full 15-branch tight-frame first/second moments;
- exact closure graph `KG(6,2)` with 15->6->1 completion;
- no full-S6 deterministic disjoint-next selector without extra state;
- matching complex integral `H_1` rank 16 and zero `H_2`;
- linear scale 2 corresponds to arithmetic index 64 under the six-volume observer.

Interpretive / open:

- whether minimum anisotropy is the physically/natively selected criterion for arithmetic 2;
- whether centered strain is the correct bridge object to P000 force/dynamics;
- whether the observer-level 120-degree triad lifts to `TRIADIC_CLOSURE_E`;
- what minimal extra orientation/history state selects one branch while preserving the desired symmetry;
- how the 16 global schedule loops should be represented in a Nollm memory field;
- general-prime minimum-defect branch orbits and exact closure periods.

## 19. Smallest next research unit

The next hard unit is now sharply defined:

**General prime-p minimal-defect classification in X6.**

For `|det A|=p` prime:

1. minimize `Delta_6(A)` exactly;
2. identify the `S6` orbit(s) of index-p branches admitting minimizers;
3. derive the centered log-strain directions and their finite frame/correlation structure;
4. determine the shortest branch schedule whose product becomes exact isotropic index `p^3` when such a schedule exists;
5. separate split-prime exact pair-plane closures from primes with an unavoidable residual defect/holonomy;
6. compare the resulting arithmetic classification with the independent 2D Hecke/Eisenstein Nollm defect spectrum without conflating carriers.

That task can test whether the exceptionally clean `2 -> 4 -> 8` triadic closure is the first member of a general arithmetic rotation law or a genuinely special binary phenomenon.
