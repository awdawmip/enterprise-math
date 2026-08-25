# Triaxial Directional Defect — Independent Tool Verification

Researcher-ID: `EM-TDDEF-79114C`

Task: `RS-TRIAXIAL-DIRECTIONAL-DEFECT-INDEPENDENT-TOOL-VERIFICATION`

Hard target: `TRIAXIAL_DIRECTIONAL_DEFECT_CALCULUS_T1_SUBTOOL_INDEPENDENTLY_RECONSTRUCTED_AND_CROSS_DOMAIN_VERIFIED_OR_NARROWED_OR_REJECTED`

Final verdict: **`NEEDS_NARROWER_TOOL_INTERFACE`**

## 0. Independence / control-plane compliance

The required execution stamp was created, committed and remotely confirmed on the owner branch before any mathematical source reading:

- stamp commit: `0f6e3d558411c282af1ffd1cdeae7f045c5722c7`;
- parent: taskbook source `3acc2fd24b074a6de02c47f60730c1fc13ab42bb`;
- stamp phase: `STARTED_BEFORE_WITHHELD_DERIVATIONS`;
- stamp `verification_verdict`: `null`.

Before the Phase-A freeze, the only project mathematical sources read were the taskbook and the two whitelisted definitions. No originating triaxial-tomography / ghost-kernel / chirality-augmentation / tool-validation journal, conversation, source proof, source checker, Driver handoff, toolbox inventory or downstream integration was read.

The Phase-A independent return was frozen at owner-branch commit:

`9ff6b64bee6431be0a44bf876254875c47a6e588`.

Only after that freeze was the current toolbox / method inventory opened for Phase-B deduplication.

## 1. Independent mathematical reconstruction

### 1.1 Native frame and implementation carrier

The native model is kept as canonical nonnegative min-zero triples. For executable endpoint algebra only, a triple `(A,B,C)` is represented in the integer carrier by

`(A-C,B-C)`.

For cyclic rotation `rho(A,B,C)=(C,A,B)`, a declared frame has carrier directions

- `s1=(A-C,B-C)`,
- `s2=(C-B,A-B)`,
- `s3=(B-A,C-A)`.

Hence `s1+s2+s3=0` in the endpoint carrier. This closure is used only for endpoint translation algebra; it is not promoted to a native diagonal-quotient identity.

The frame width is

`w(S)=max(A,B,C)-min(A,B,C)`.

For canonical min-zero seeds, `w(S)=max(A,B,C)`.

A frame is primitive exactly when the carrier direction is primitive, equivalently

`gcd(|A-C|,|B-C|)=1`.

### 1.2 Defect operators

For endpoint translation `tau_i=tau_{s_i}` define

`Delta_i=tau_i-I`,

`H_ij=Delta_i Delta_j`,

`G=Delta_1 Delta_2 Delta_3`.

The translations commute. Therefore:

- cyclic rotation of the frame preserves `G`;
- simultaneous frame reversal sends `G` to `-G`;
- `Delta_1 H_23 = Delta_2 H_31 = Delta_3 H_12 = G`.

Thus `G` is an oriented frame defect, not an orientation-free scalar.

## 2. Eight trace states versus the six-point endpoint ghost

The formal trace expansion is

`G = tau_1 tau_2 tau_3 - tau_1 tau_2 - tau_1 tau_3 - tau_2 tau_3 + tau_1 + tau_2 + tau_3 - I`.

That is an eight-state signed trace cube. The `000` and `111` histories remain distinct trace states.

Only after passing to endpoint carrier algebra does `tau_1 tau_2 tau_3=I` and, e.g., `tau_1 tau_2=tau_3^{-1}`. The endpoint stencil then becomes

`G = tau_1 + tau_2 + tau_3 - tau_1^{-1} - tau_2^{-1} - tau_3^{-1}`.

So the implementation preserves the mandatory distinction:

`EIGHT_STATE_TRACE_CUBE != SIX_POINT_ENDPOINT_STENCIL`.

Endpoint coalescence is not trace-identity coalescence.

## 3. Exact finite tomography kernel and uniqueness

Let

`B_R = {(x,y) in Z^2 : max(|x|,|y|,|x-y|) <= R}`.

For a primitive direction `s`, vanishing sums on every `s`-parallel line are equivalent, for finitely supported fields over a field `K`, to divisibility by the Laurent factor `X^s-1`.

For a finite family `F` of pairwise distinct unoriented primitive frame orbits, let

`P_F = product_{S in F} G_S`,

`W = sum_{S in F} w(S)`.

The primitive directional factors are pairwise nonassociate primes in `K[Z^2]`. Therefore simultaneous X-ray cancellation is exactly divisibility by their product. Newton-polytope support widths add under multiplication by a nonzero Laurent polynomial. Each frame triple-defect has support width `w(S)` in each of the three hex-box facet directions. Consequently:

`ker X_F(B_R) = P_F K^{B_{R-W}}`.

The convention is that `B_n` is empty for `n<0`.

Hence

`dim_K ker X_F(B_R) = |B_{R-W}|`,

with

`|B_n| = 3n^2+3n+1` for `n>=0`.

Therefore finite-box uniqueness holds exactly when

`W > R`.

At `W=R`, exactly one ghost-amplitude degree remains.

The committed checker verifies the equality by independent X-ray and defect-image rank calculations in characteristic zero and characteristics `2,3,5,7`, including mixed-frame cases.

## 4. Primitive frame width / Euler-phi census

For exact width `w>1`, cyclicly oriented primitive frame representatives can be written

`(w,k,0)` and `(k,w,0)`

with `1<=k<w` and `gcd(k,w)=1`.

Thus:

- oriented/chiral frame count at width `w`: `2 phi(w)`;
- unoriented tomography-frame count at width `w`: `phi(w)`.

The same formulas hold at `w=1` after the direct base-case check.

The deterministic checker verifies the census through `w=32`.

## 5. Exposed-vertex minimal augmentation

The Newton support of `P_F` has exposed vertices whose coefficients are units `+/-1`. Choose a generic integral linear functional exposing one such vertex `v`.

For every ghost-amplitude coordinate `x`, sample the reconstructed field at `x+v`. Order amplitude coordinates by decreasing value of the exposing functional. The resulting sampling matrix is triangular with diagonal entries `+/-1`.

Consequences:

1. the measurement family is injective over every commutative coefficient ring with identity;
2. over a field, one scalar sample per ghost-amplitude degree is minimal by dimension;
3. the reconstruction certificate is stronger than a floating-rank argument because the determinant is a unit.

The checker validates one-frame and mixed-frame exposed augmentations in characteristic zero and `2,3,5,7`.

## 6. Chirality, adjoint, Gram and Laplacian factorization

With translation adjoint `tau_s^*=tau_{-s}`,

`Delta_s^* = tau_{-s}-I`.

Define the directional Laplacian factor

`L_s = Delta_s^* Delta_s = 2I-tau_s-tau_{-s}`.

Since the translations commute,

`G^*G = L_{s1} L_{s2} L_{s3}`.

This identity is exact over the integer Laurent group ring.

However, two mathematically different augmentations must not share one unqualified `CHIRALITY_AUGMENT` name:

### 6.1 Full adjoint-field augmentation

`f -> G^* f` with the full finite-support output retained is injective on the ghost image over every field: multiplication by the nonzero Laurent polynomial `G^*G` is injective in the Laurent domain.

### 6.2 Compressed square-Gram augmentation

If the adjoint output is compressed back to the amplitude-domain square Gram matrix, characteristic-uniform invertibility fails.

For the primitive base frame, independently computed examples are:

| box radius | amplitude dimension | rank over Q | rank mod 2 | rank mod 3 | rank mod 5 | rank mod 7 |
|---:|---:|---:|---:|---:|---:|---:|
| 1 | 1 | 1 | 0 | 0 | 1 | 1 |
| 2 | 7 | 7 | 6 | 4 | 4 | 7 |
| 3 | 19 | 19 | 12 | 15 | 19 | 16 |

Thus a compressed-Gram API must either carry the coefficient field / characteristic plus an invertibility certificate, or refuse a universal exact-recovery claim.

In addition, characteristic `2` identifies `G` and `-G`, so reversal-sign chirality itself disappears there.

## 7. No finite-support translation-invariant deghosting

A finite-support translation-invariant deghosting convolution would require a finite Laurent polynomial `Q` with

`QG=1`.

The units of `K[Z^2]` are scalar monomials, while the triple defect has a genuine six-term support. Therefore no such finite-support convolutional left inverse exists.

This does not contradict the finite-box exposed-vertex inverse, which is domain-aware and triangular rather than translation-invariant.

## 8. Second independent problem family: Hive / rhombus reuse

The implementation does not create a separate Hive operator. It reuses the exact same functions:

- `RHOMBUS2 = Delta_i Delta_j`;
- `TRIPLE_DEFECT = Delta_k RHOMBUS2`.

On a cubic lattice field regression the three complementary-direction evaluations agree exactly and are nonzero:

`Delta_1 H_23 = Delta_2 H_31 = Delta_3 H_12 = G`.

Therefore the operator algebra has a genuine second-domain reuse beyond X-ray tomography.

Cross-domain verdict: **PASS**.

## 9. Y–Delta as negative boundary discriminator

For star conductances `(a,b,c)`, the equivalent triangle parameters are

`(ab/(a+b+c), bc/(a+b+c), ca/(a+b+c))`.

This response-equivalence transformation is rational and nonadditive in the edge parameters. A direct regression exhibits

`YDelta(p+q) != YDelta(p)+YDelta(q)`.

Therefore Y–Delta is not an instance of the fixed linear translation-defect calculus merely because both settings contain three directions / three arms and local elimination.

Boundary verdict: **`OUTSIDE_INTERFACE / HARD_NEGATIVE_DISCRIMINATOR`**.

## 10. Phase-B toolbox / method deduplication

Phase B began only after the Phase-A freeze.

### 10.1 Existing `difference_response`

`src/enterprise_math/difference_response.py` already packages exact finite responses `F(x+h)-F(x)` for deterministic natural-number operations. This means the generic idea “take a finite difference” is already represented and, in any case, is standard mathematics.

It does **not** implement the present Laurent translation-group operator, the closed three-direction frame, the six-point stencil, finite-X-ray kernel theorem or exposed-vertex reconstruction.

Dedup result: `DIFF1` is not a new T1 family by itself; implementation-level specialization remains justified inside the typed triaxial module.

### 10.2 Existing adjoint-boundary precision

`src/enterprise_math/adjoint_boundary_precision.py` uses order/Galois adjoints that pull threshold cuts backward through monotone actions. That is a different notion from the linear-algebraic / convolution adjoint `tau_s^*=tau_{-s}` used here.

Dedup result: name collision only; no semantic implementation reuse should be claimed.

### 10.3 Existing graph Laplacian / chip-firing T1 family

`T1_GRAPH_LAPLACIAN_CHIP_FIRING` and `src/enterprise_math/discrete_laplacian_chip_firing.py` already provide an exact finite graph-Laplacian/toppling interface. The module explicitly treats the underlying mathematics as classical and limits its semantics to the graph/toppling setting.

The directional factor `L_s=2I-tau_s-tau_{-s}` is mathematically a one-dimensional translation Laplacian, so the bare observation “a Laplacian appears” is not a new tool claim. But the existing graph T1 family does not supply the triaxial Laurent-product factorization, tomography kernel certificate or native-frame typing.

Dedup result: `GRAM_FACTOR` is a theorem/helper inside the narrowed module, not a new standalone T1 family.

### 10.4 Current inventory gap

The current curated registry / method inventory and executable surface contain no exact replacement for the combined capability:

`closed primitive triaxial frame -> exact three-direction defect -> finite hex-box X-ray kernel certificate -> unimodular exposed reconstruction`,

with the same operator reused in a rhombus/Hive calculation.

The reusable gap is therefore real, but narrower than the unrestricted proposed candidate API.

## 11. Required interface narrowing

The independent verification does **not** support promotion of one monolithic unrestricted `TRIAXIAL_DIRECTIONAL_DEFECT` interface. A safe interface must make the following distinctions explicit.

### 11.1 Required typed preconditions

`DECLARE_FRAME` must return a typed closed frame carrying:

- three pairwise distinct directions;
- closure certificate `s1+s2+s3=0` in the implementation carrier;
- orientation;
- primitive/unoriented-ray identifiers;
- exact width.

Tomography routines must reject nonprimitive frames and duplicate unoriented ray orbits unless multiplicity semantics are explicitly requested.

### 11.2 Recommended narrow surface

Core algebra:

- `DECLARE_FRAME`
- `DIFF1`
- `RHOMBUS2`
- `TRIPLE_DEFECT`
- `FRAME_WIDTH`

Finite tomography specialization:

- `XRAY_KERNEL_CERT`
- `MULTIFRAME_UNIQUENESS`
- `EXPOSED_AUGMENT`

Adjoint/chirality specialization, split rather than conflated:

- `CHIRALITY_AUGMENT_FULL`
- `COMPRESSED_GRAM_AUGMENT(characteristic, invertibility_certificate)`
- `GRAM_FACTOR`

Explicit non-capabilities:

- no finite-support translation-invariant deghosting inverse;
- no automatic native trace quotient from endpoint closure;
- no characteristic-uniform compressed-Gram recovery;
- no Y–Delta / arbitrary Schur-complement identification.

## 12. Why the final verdict is not one of the other three

### Not `ACCEPT_T1_TRIAXIAL_DIRECTIONAL_DEFECT_GLOBAL_SUBTOOL`

The mathematics and code pass independent reconstruction, but the candidate interface is too broad as stated. In particular `CHIRALITY_AUGMENT` conflates full adjoint output with compressed Gram recovery, primitive/disjoint ray preconditions are load-bearing, and several elementary pieces are already generic/classical rather than novel T1 value.

### Not `ACCEPT_AS_DOMAIN_OPERATOR_ONLY`

The same exact `RHOMBUS2` / `TRIPLE_DEFECT` implementation works in a second independent Hive/rhombus family. The reusable algebra is therefore not confined to tomography.

### Not `REJECT_TOOL_UPGRADE`

There is an actual capability gap after deduplication: no current shared tool combines native closed-frame typing, exact finite-X-ray kernel structure, frame-width uniqueness and unimodular exposed reconstruction. Independent tests support that capability.

## 13. Final verdict

**`NEEDS_NARROWER_TOOL_INTERFACE`**

The Driver may consider later integration of the narrowed typed interface. This task does not modify `enterprise_toolbox_registry.json`, `research_method_inventory.json`, or any shared toolbox registry.

## 14. Executable evidence

Committed implementation:

- `src/enterprise_math/triaxial_directional_defect.py`

Committed unit regressions:

- `tests/test_triaxial_directional_defect.py`
- independent local suite: `11/11 PASS`.

Committed deterministic checker:

- `research_output/evidence/triaxial_directional_defect_independent_checker.py`

Checker coverage:

- 14 exact tomography rank/kernel cases, including mixed frames;
- characteristic-zero and mod `2,3,5,7` checks;
- Euler-phi census through width `32`;
- exposed-vertex unimodular reconstruction;
- Gram/Laplacian factorization and small-characteristic failures;
- same-implementation Hive/rhombus bridge;
- Y–Delta negative discriminator;
- no finite-support Laurent left inverse.

Phase-A frozen return:

- `research_returns/TRIAXIAL_DIRECTIONAL_DEFECT_INDEPENDENT_TOOL_VERIFICATION_PHASE_A_RETURN_20260825.md`.
