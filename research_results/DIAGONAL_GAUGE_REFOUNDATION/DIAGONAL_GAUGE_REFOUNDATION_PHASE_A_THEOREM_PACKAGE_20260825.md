# Diagonal Gauge Refoundation — Phase A theorem package

Status: `RAW REFOUNDATION CANDIDATE / EXACT ALGEBRA + REGRESSION / NOT CANONICAL`
Date: `2026-08-25`
Researcher-ID: `EM-DGR-8C2D41`
Owner branch: `research/diagonal-gauge-refoundation`
Base main: `9d1aceb5d98c4e029a68734ef89f7b80e6c1bf8c`

Primary disposition:

`EXACT_DERIVED_DIAGONAL_DISPLACEMENT_GAUGE_ESTABLISHED__CURRENT_R061_RECOVERED__N0_PROMOTION_NOT_CLAIMED__GLOBAL_THREE_GENERATOR_PATH_LOOP_OPEN`

## 0. Scope and semantic separation

This package does **not** restore the superseded carrier-Euclidean native metric and does **not** identify noncanonical triples as additional native point addresses.

It distinguishes three layers:

1. **current native/canonical point address**: `A_E={(a,b,c) in N_0^3 : min(a,b,c)=0}`;
2. **lifted displacement labels**: `L=Z^3`;
3. **derived diagonal displacement gauge**: quotient only at the lifted-displacement layer.

The intended correction is therefore not

`ALL NATIVE POINT COORDINATES ARE PRIMITIVELY QUOTIENTED`,

but rather

`LIFTED DISPLACEMENT LABELS HAVE A DIAGONAL GAUGE KERNEL WHOSE UNIQUE MIN-ZERO SECTION IS THE CURRENT ADDRESS ATLAS`.

This keeps:

- three positive native axis labels;
- no primitive native negative axes;
- current three-sector atlas;
- current sector Pythagorean law;
- current native line trace identity;
- current directed arbitrary-point gauge;
- current bidirectional segment spectrum.

It does not restore `a^2+b^2+c^2-ab-bc-ca` as the native Enterprise metric.

---

## 1. Lifted displacement carrier and gauge kernel

Let

`L = Z^3`

and write

`1_diag=(1,1,1)`.

Define the homomorphism

`chi : Z^3 -> Z^2`

by

`chi(a,b,c)=(a-c,b-c)`.

### Theorem DG-A1 — exact kernel

`ker(chi)=Z*(1,1,1)`.

Hence

`G_D := Z^3 / Z*(1,1,1) ~= Z^2`.

**Proof.** `chi(a,b,c)=(0,0)` iff `a=c` and `b=c`, i.e. `(a,b,c)=k(1,1,1)`. Surjectivity is witnessed by `(r,s,0)`. QED.

This theorem can be derived from the current two-coordinate displacement carrier itself; it does not require promoting the old carrier Euclidean vector relation to a native vector identity.

Freeze candidate:

`DIAGONAL_GAUGE_IS_KERNEL_OF_CURRENT_TWO_COORDINATE_DISPLACEMENT_CHART = true`.

---

## 2. Unique minimum-zero canonical section

Define for any `z=(a,b,c) in Z^3`

`can(z)=z-min(a,b,c)*(1,1,1)`.

Then `can(z)` is nonnegative and has minimum component zero.

### Theorem DG-A2 — gauge invariance and uniqueness

For all `z,z' in Z^3`:

1. `can(z+k*1_diag)=can(z)` for every `k in Z`;
2. `can(z)=can(z')` iff `z-z' in Z*1_diag`;
3. every class in `G_D` has exactly one representative in `A_E`.

Therefore `A_E` is a unique canonical section of `G_D`.

Important typing:

`NONCANONICAL LIFT != SECOND NATIVE POINT ADDRESS`.

The current `min=0` atlas remains the concrete native/canonical address language; the quotient acts on lifted displacement labels.

Freeze candidate:

`MIN_ZERO_ADDRESS_IS_UNIQUE_DIAGONAL_GAUGE_SECTION = true`.

---

## 3. Current Stage-2 decoder is exactly the section map

For `(r,s) in Z^2`, current R061 Stage 2 freezes

`m=min(r,s,0)`

and

`D_E(r,s)=(r-m,s-m,-m)`.

### Theorem DG-A3 — decoder factorization

`D_E(r,s)=can(r,s,0)`.

Moreover

`chi(D_E(r,s))=(r,s)`

and for every `z in Z^3`

`D_E(chi(z))=can(z)`.

Thus the current arbitrary-point displacement decoder is exactly the canonical section

`Z^2 ~= G_D -> A_E`.

Freeze candidate:

`R061_STAGE2_DECODER = DIAGONAL_GAUGE_CANONICAL_SECTION_IN_Z2_CHART`.

This is an exact recovery of the already frozen decoder, not a replacement algorithm.

---

## 4. Transported group law on min-zero addresses

For `x,y in A_E`, define

`x (+)_D y := can(x+y)`.

Define

`(-)_D x := can(-x)`.

### Theorem DG-A4 — abelian displacement group

`(A_E,(+)_D)` is an abelian group isomorphic to `G_D` and `Z^2`.

Identity is `(0,0,0)`.

If `M=max(x_1,x_2,x_3)`, then

`(-)_D x = (M-x_1,M-x_2,M-x_3)`.

Associativity follows from

`can(can(x)+can(y))=can(x+y)`.

Freeze candidate:

`MIN_ZERO_DISPLACEMENTS_WITH_CANONICALIZED_ADDITION_FORM_DERIVED_ABELIAN_GROUP = true`.

### Exact R061 recovery

Current R061 Stage 2 composes canonical displacement triples by adding and subtracting the common minimum. This is exactly `(+)_D`.

Current reversal formula

`(A,B,C) -> (M-A,M-B,M-C)`

is exactly group inversion `(-)_D`.

Therefore the quotient interpretation explains two already-frozen formulas simultaneously.

---

## 5. Three positive generators and no primitive negative axes

Let

`g_1=[(1,0,0)]`, `g_2=[(0,1,0)]`, `g_3=[(0,0,1)]`

in `G_D`.

### Theorem DG-A5 — derived balanced-generator relation

`g_1+g_2+g_3=0` in the **derived displacement group**.

Hence

`-g_1=g_2+g_3`,

and cyclically.

In the min-zero section:

`-g_1=(0,1,1)`,

`-g_2=(1,0,1)`,

`-g_3=(1,1,0)`.

This does **not** introduce primitive negative native axes. It says that the inverse of a derived displacement class has a canonical representation using the other two positive component labels.

Typing freeze candidate:

`DIAGONAL_GAUGE_GROUP_INVERSE != PRIMITIVE_NATIVE_NEGATIVE_AXIS`.

Also:

`DERIVED_DISPLACEMENT_RELATION g1+g2+g3=0 != NATIVE_EUCLIDEAN_VECTOR_IDENTITY`.

---

## 6. Three-sector fan survives exactly

The unique min-zero section decomposes into

- `C_12={(a,b,0):a,b>=0}`;
- `C_23={(0,b,c):b,c>=0}`;
- `C_31={(a,0,c):a,c>=0}`.

These are exactly the current three positive right-sector charts, glued on the positive axes.

Therefore the diagonal gauge group does not replace the sector atlas. It explains why those three charts form one canonical section of a larger lifted displacement calculus.

The algebraic rank of `G_D` is two. This is a statement about the derived displacement gauge group / current two-coordinate carrier and is **not** promoted here to a claim about the project's native dimension semantics.

Freeze boundary:

`RANK(G_D)=2 != AUTOMATIC_NATIVE_DIMENSION_CLAIM`.

---

## 7. Current directed Pythagorean gauge descends to the quotient

For `g in G_D`, let `hat(g)=can(z)` be its unique min-zero representative and define

`q_E(g)=sum_i hat(g)_i^2`,

`ell_E(g)=sqrt(q_E(g))`.

### Theorem DG-A6 — well-defined three-sector directed gauge

`q_E` is well-defined on `G_D` because `hat(g)` is unique.

On each sector it is exactly the frozen Pythagorean law:

- `(a,b,0)` -> `a^2+b^2`;
- `(0,b,c)` -> `b^2+c^2`;
- `(a,0,c)` -> `a^2+c^2`.

It is invariant under component permutations / cyclic sector relabeling.

For nonnegative integers `n`,

`ell_E(n g)=n ell_E(g)`.

It is generally inversion-asymmetric:

`ell_E(-g) != ell_E(g)`.

For canonical `x=(A,B,C)` with `M=max(A,B,C)`:

`q_E(-g)-q_E(g)=M(3M-2(A+B+C))`,

exactly the current R061 reversal formula.

Freeze candidate:

`CURRENT_DIRECTED_NATIVE_GAUGE = POSITIVE_SECTION_GAUGE_ON_DERIVED_DIAGONAL_DISPLACEMENT_GROUP`.

---

## 8. Triangle inequality is preserved

For canonical `x,y in A_E`, write

`x (+)_D y = x+y-m*1_diag`

with `m=min_i(x_i+y_i)>=0`.

Therefore every component of `x (+)_D y` is no larger than the corresponding component of the nonnegative vector `x+y`, so

`||x (+)_D y||_2 <= ||x+y||_2 <= ||x||_2+||y||_2`.

Hence

`ell_E(g+h)<=ell_E(g)+ell_E(h)`.

This recovers the frozen Stage-2 triangle inequality without treating `ell_E` as a symmetric metric.

---

## 9. Stage-3 bidirectional spectrum becomes group-theoretic

For a directed displacement class `g=delta(P,Q)`, current Stage 3 freezes

`SPEC_E(P,Q)=multiset{ell_E(P->Q),ell_E(Q->P)}`.

### Theorem DG-A7 — spectrum recovery

Under the diagonal gauge refoundation,

`SPEC_E(P,Q)=multiset{ell_E(g),ell_E(-g)}`.

Thus current orientation-free data is exactly the two-sided gauge spectrum of one derived displacement-group element.

This does not identify the path-groupoid inverse with the independently decoded canonical reverse trace; it only identifies their endpoint displacement classes as group inverses.

Freeze candidate:

`BIDIRECTIONAL_LENGTH_SPECTRUM = {GAUGE(g),GAUGE(-g)}`.

---

## 10. Metric fork theorem: quotient does not force the old metric

Let `Q` be a globally quadratic scalar on lifted `Z^3` that

1. is invariant under all component permutations;
2. descends through common-diagonal shifts;
3. satisfies `Q(1,0,0)=1`.

Permutation invariance forces

`Q=alpha*(a^2+b^2+c^2)+beta*(ab+bc+ca)`.

Diagonal-shift invariance forces

`alpha+beta=0`.

Unit calibration forces `alpha=1`.

### Theorem DG-A8 — unique symmetric quadratic branch

The unique such quadratic is

`Delta=a^2+b^2+c^2-ab-bc-ca`.

But

`Delta(g_1+g_2)=Delta(1,1,0)=1`,

while the current Enterprise sector Pythagorean law requires

`q_E(g_1+g_2)=q_E(1,1,0)=2`.

Therefore:

`DIAGONAL_GAUGE_QUOTIENT DOES NOT FORCE THE HISTORICAL METRIC`.

More strongly:

`CURRENT_120_DEGREE_PYTHAGOREAN_GAUGE CANNOT BE A GLOBAL S3-INVARIANT QUADRATIC FORM ON G_D`.

The 2026-08-20 correction should therefore be understood as changing the **length functional** from the globally quadratic symmetric branch to a three-sector positive-section gauge, not as mathematically requiring deletion of the displacement quotient itself.

Freeze candidate:

`QUOTIENT_STRUCTURE_AND_METRIC_STRUCTURE_ARE_LOGICALLY_SEPARABLE = true`.

---

## 11. Line identity remains strictly richer than endpoint displacement

For a sector trace `T_{a,b}^{(ij)}`, define the endpoint-displacement class

`End_D(T_{a,b}^{(ij)}) = a g_i + b g_j`.

Trace composition maps homomorphically to displacement addition.

### Theorem DG-A9 — endpoint map is not a line classifier

For example,

`End_D(T_{1,1}^{(12)})=g_1+g_2=-g_3`.

The frozen R061 line theory already records a reverse-third carrier shortcut reaching that same endpoint while not belonging to the `T_{1,1}^{(12)}` native component trace.

Hence diagonal gauge endpoint equality does not imply same native line identity or same path witness.

Freeze candidate:

`DIAGONAL_GAUGE_ENDPOINT_QUOTIENT DOES_NOT_COLLAPSE_NATIVE_TRACE_IDENTITY`.

This is essential: the refoundation is an endpoint/displacement algebra, not a quotient of path provenance.

---

## 12. Balanced triad: exact displacement theorem, path theorem still open

From DG-A5,

`[(1,1,1)]=0` in `G_D`.

Equivalently

`can(1,1,1)=(0,0,0)`.

### Exact statement established

`ONE_OF_EACH_THREE_POSITIVE_COMPONENT_LABELS_HAS_ZERO_DERIVED_ENDPOINT_DISPLACEMENT`.

### Statement **not** established by current line theory

Current native line traces are sector-local two-component objects. No canonical global native three-generator line trace

`T_{1,1,1}`

has been frozen.

Therefore this package does **not** assert

`X_1 X_2 X_3 = identity_path`

or that all permutations are one native trace.

### Conditional extension

If a future globally typed three-generator path language is frozen with endpoint map `End_D(X_i)=g_i` and concatenation mapped to group addition, then every word containing equal numbers `m` of `X_1,X_2,X_3` has zero endpoint displacement. The number of such formal words is

`(3m)!/(m!)^3`.

For `m=1..10` the first regression values are

`6, 90, 1680, 34650, 756756, 17153136, 399072960, 9465511770, 227873431500, 5550996791340`.

This is **conditional word enumeration only**. Same endpoint is not identity morphism, and the global three-generator typing remains open.

Freeze boundary:

`BALANCED_TRIAD_ZERO_DISPLACEMENT = EXACT_DERIVED`;

`BALANCED_TRIAD_NATIVE_PATH_LOOP_FIBER = OPEN_TYPING_GATE`.

---

## 13. Relation to the parabola / multipath program

The sector-local jitter/parabola work uses only a two-component trace fiber. None of its exact two-generator formulas require a diagonal quotient.

The refoundation therefore leaves that sector-local theory unchanged.

What reopens is the global/background question: whether a properly typed three-generator path layer contains balanced zero-displacement excursions that may dress a two-generator trace without changing its endpoint displacement. That is a separate Stage-B path-typing problem and must not be assumed here.

---

## 14. Proposed correction to the 2026-08-20 freeze

Do **not** simply restore the old sentence

`(a,b,c) ~ (a+k,b+k,c+k)`

as an untyped native-point ontology statement.

Instead, if Driver review accepts this package, replace the overstrong freeze with a typed bundle:

1. `NO_UNTYPED_DIAGONAL_SHIFT_POINT_ONTOLOGY = true`;
2. `LIFTED_DISPLACEMENT_DIAGONAL_GAUGE = DERIVED_G1`;
3. `MIN_ZERO_ADDRESS = UNIQUE_CANONICAL_GAUGE_SECTION`;
4. `DIAGONAL_GAUGE_RELATION != NATIVE_EUCLIDEAN_VECTOR_IDENTITY`;
5. `DIAGONAL_GAUGE_DOES_NOT_SELECT_NATIVE_METRIC`;
6. `CURRENT_SECTOR_PYTHAGOREAN_GAUGE_RETAINED`;
7. `NO_PRIMITIVE_NATIVE_NEGATIVE_AXES_REQUIRED`.

Retain without change:

`CARRIER_DIRECTION_RELATION != NATIVE_VECTOR_RELATION`.

The phrase `NO_NATIVE_DIAGONAL_SHIFT_QUOTIENT` should be classified as overstrong unless it is narrowly redefined to mean only `no primitive untyped native-point quotient`.

---

## 15. Native-semantics ledger

### Claim: diagonal gauge quotient is N0 primitive

Verdict: `NOT CLAIMED / UNRESOLVED`.

Reason: the packet/path N0 substrate does not itself contain the lifted `Z^3` displacement group as a primitive.

### Claim: diagonal gauge quotient is an exact derived displacement calculus compatible with current G1/R061 definitions

Verdict: `CONDITIONAL_DERIVED / EXACT_RECOVERY`.

Certificate:

- constructed from the current two-coordinate displacement chart and min-zero decoder;
- exact kernel/section theorem;
- exact recovery of current Stage-2 composition and reversal;
- exact recovery of current sector gauge and Stage-3 spectrum;
- component-permutation covariance;
- no metric target leakage.

### Claim: old `Delta` returns as native metric

Verdict: `REJECTED`.

The metric fork theorem shows `Delta` is the unique globally quadratic S3-symmetric gauge-invariant branch, but it conflicts with the currently frozen sector Pythagorean value on `(1,1,0)`. It remains a carrier/optional symmetric quadratic readout, not the current native metric.

### Claim: `(1,1,1)` is a native identity path

Verdict: `UNRESOLVED / NOT ESTABLISHED`.

Only zero endpoint displacement is established in Phase A.

---

## 16. Verification

Deterministic exact-integer checker:

`scripts/check_diagonal_gauge_refoundation.py`

Frozen first report:

`research_results/DIAGONAL_GAUGE_REFOUNDATION/DIAGONAL_GAUGE_REFOUNDATION_CHECK_REPORT.json`

Status: `PASS`.

Report SHA-256:

`5a5d2d1f46bf876434b9c95365e85d69af9ce47c10dd069a704d8b21e7e5569a`.

Checked finite regressions include:

- 4,913 lifted canonical-section states;
- 117,649 kernel-equivalence pairs;
- 1,681 Stage-2 decoder chart pairs;
- 47,089 group-law pairs;
- 50,653 associativity triples;
- 47,089 exact directed-gauge triangle certificate pairs;
- 1,302 S3 covariance cases;
- 7,203 `Delta` diagonal-invariance cases;
- frozen unit / 3-4-5 reversal examples;
- displacement-level balanced triad relation.

Finite regression is not used as a substitute for the algebraic proofs above.

---

## 17. Phase-A stop / next executable stage

Phase A establishes the derived displacement gauge and current-R061 recovery.

Next stage:

`DIAGONAL_GAUGE_REFOUNDATION_PHASE_B_GLOBAL_THREE_GENERATOR_PATH_TYPING`.

Hard target:

Determine whether the current packet/cell adjacency and component typing canonically support a global three-generator path language whose endpoint forgetful map is `G_D`, and classify the balanced-triad fiber as one of:

- canonical native closed path family;
- carrier-only closed walk family;
- typed enrichment requiring new N1 structure;
- impossible/inconsistent with current line/BRC typing.

No current canonical foundation file is modified by this Phase-A package.
