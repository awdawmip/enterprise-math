# X6 historical reconciliation — R063 signed two-axis lift and bounded LP011 caller audit (2026-11-12)

**Status:** AUTHOR_PROVED / EXACT_FINITE_CHECK_EXECUTED / NONBLIND / UNREVIEWED / NOT_ADMITTED. Scientific evidence only; no formal native CLAIM, Result, semantic checkpoint or independent Driver admission is asserted.

**Mother task:** `RS-X6-LEGACY-PLANE-RECONCILIATION`, publication `TP2-B4A441B23DA3159232C2`, objective `PO-X6-SPATIAL-FOUNDATION-CONSISTENCY-20260905`. Existing historical intake `HRI-1A48B2D7F0E242FCC2C57D7E`, review `HIRR-1C60C7CCFAE8636E82F43A76` = `REQUEST_REVISION`. Frozen mathematical input remains `awdawmip/enterprise-math@59538f585d037d09ef687b28715c4bc1a3f9fe03`; historical comparison generation remains `fd2bcff10ca6e147348b6c1236027fc0d2877df3`.

## 1. Specific located current downstream consumer

`definitions/ENTERPRISE_PATH_VALUED_SQUARE_ROOT_OPERATOR_20260821.md` on current main, blob `61f23f2bcf965aa21d093ae3e35c0d6cb70610b7`, retains `ACTIVE / CANONICAL / FROZEN`. Its lines 13–17 describe square-native-norm algebraic discovery, lines 37–68 enumerate **ordered nonnegative two-component roots**, lines 89–113 construct **two positive-generator path words**, and lines 121–168 report the N=2500 example. This is an actual named R063 consumer, not a guessed LP011 original caller.

The frozen X6 slice source `definitions/ENTERPRISE_X6_CENTERED_THREE_AXIS_SLICE_REBASE_20260905.md` at the immutable task pin, blob `b0988c9fa0f2f7c3314784673cf21a2df2340ebe`, defines signed primitive steps and the squared norm on the selected native slice. The pinned executable `experiments/x6_signed_native_spatial_v16_20260905/signed_brc.py`, blob `300a96e3dc24bf6fff73743037a0347a8bc83176`, supplies `shortest_event_count`, `spatial_norm_squared`, and `shortest_path_multiplicity`. This unit **composes those exact existing laws**; it does not replace or rerun the pre-existing R063 checker.

## 2. New exact signed-lift theorem for a fixed ordered pair of native axes

Select distinct native axes `i,j` of the signed X6 Cell torsor and fix a Cell anchor. All four other *relative displacement* components are exactly zero. This is a **two-coordinate restriction within the native X6 / selected three-axis slice**, not an independent native plane and not the complete X6 squared-norm shell.

For every positive integer `r`, let
```
R_r^+ = {(a,b) in Z_{≥0}^2 : a*a+b*b=r*r},
F(a,b) = {(eps*a,delta*b) : eps,delta in {-1,+1}},
w(a,b) = 2^([a>0]+[b>0]).
```
Then `F(a,b)` has exactly `w(a,b)` elements, distinct nonnegative pairs have disjoint sign-lift fibers, and the complete signed two-axis shell is their disjoint union. Therefore

```
#native_signed_endpoints(r) = sum_{(a,b) in R_r^+} w(a,b),

N_BRC_shortest(r)
  = sum_{(a,b) in R_r^+} w(a,b) * binom(a+b,a).
```

Here the second sum counts **unweighted ordered shortest signed primitive words in one fixed ordered axis pair**, with endpoints distinguished. Each signed endpoint `(x,y)` requires exactly `|x|+|y|` signed primitive steps, and its words are the multinomial permutations `binom(|x|+|y|,|x|)`. Changing either nonzero sign changes the native endpoint but not that count. The formula holds for all `r≥1` and includes axis points (`w=2`) and nondegenerate points (`w=4`). It does not make a claim about constrained/weighted paths, R063 Gaussian factor-channel multiplicity, or all six-dimensional directions.

**Proof.** Squaring erases signs. Every nonzero component has two signed choices and a zero component has one, yielding `w`. Absolute values recover a unique ordered nonnegative pair; hence distinct sign fibers are disjoint and exhaustive. Minimality of `|x|+|y|` and the multinomial count follow from the pinned signed-BRC step rules. Summation proves the identities. QED.

## 3. N=2500 exact certificate and direct R063 consumption

R063's unchanged ordered positive root list is
```
(0,50), (14,48), (30,40), (40,30), (48,14), (50,0).
```
Its six positive-sector branches contain
```
2 + 2*binom(62,14) + 2*binom(70,30)
= 110695538274255714208
```
shortest positive words, reproducing R063 lines 155–168.

The signed X6 lift over the **same two fixed axes**, with no additional axes, contains
```
4 axis endpoints + 4*4 nonaxis endpoints = 20 distinct endpoints,
4 + 8*binom(62,14) + 8*binom(70,30)
= 442782153097022856828 shortest signed words.
```
`binom(62,14)=29078984349975`; `binom(70,30)=55347740058143507128`. The original R063 count is therefore retained **exactly at its fixed-positive-sector observer strength**, while the 20-endpoint total is its signed-native two-axis extension. This is a precise retyping/extension, not a blanket error finding against R063's arithmetic.

The companion deterministic checker `research_checks/X6_R063_SIGNED_TWO_AXIS_LIFT_20261112_ONHOUR.py` was run with exact Python integers over `1≤r≤100`, enumerating all signed endpoints in each fixed two-axis shell and matching both formulas. It independently checks the N=2500 integers, reversed-endpoint symmetry and zero-coordinate sign deduplication. This is finite implementation evidence; the all-`r` theorem has the above algebraic proof.

**Operational adapter for actual consumers:** R063's `GRoot_E(r^2)` returns the ordered nonnegative pair set. A downstream signed-native X6 consumer must explicitly apply `F(a,b)` and decorate every nonzero generator with its sign before taking shortest-word BRC; a downstream *positive sector* consumer may retain R063's existing path count unchanged. Boolean support cannot recover sign, counts or ordered path provenance. Review the current R063 type/routing label before promoting the adapter; the original frozen mathematical evidence is preserved byte-for-byte.

## 4. Bounded LP011 original-caller source audit

Read the historical `definitions/` tree at `fd2bcff10ca6e147348b6c1236027fc0d2877df3` and **16 named historical definition files** in the old plane/trace/vector/line/coordinate family. The targeted explicit-rule search used source text for `dominant axis`, `dominant direction`, `argmax`, `主导轴`, `主轴`, explicit `M=max`, and sign/tie selector language. Exactly **two named files** in this bounded set contained an `M=max` formula:

1. `definitions/ENTERPRISE_ARBITRARY_POINT_DIRECTED_LINE_GAUGE_20260821.md`, historical blob `58ccac6d8b88dcfd91a0a6017ca7b29187b4e7b0`, lines 236–250: `M=max(A,B,C)` defines the **min-zero reverse quotient decoder** `(M-A,M-B,M-C)`; it does not select the dominant raw signed native axis.
2. `definitions/ENTERPRISE_DERIVED_DIAGONAL_DISPLACEMENT_QUOTIENT_20260826.md`, historical blob `11f47f9d2d70439fdada6d59242790fdcf46929e`, lines 132–148: the same `M=max` construction is the algebraic **derived-quotient inverse**. It explicitly distinguishes derived inversion from native trace/path inversion.

Other inspected historical files: `ENTERPRISE_NATIVE_LINE_TRACE_FORMULA_20260821.md`, `ENTERPRISE_BRC_MULTIPATH_ENRICHMENT_BRIDGE_20260821.md`, `ENTERPRISE_UNORIENTED_BIDIRECTIONAL_SEGMENT_SPECTRUM_20260821.md`, `ENTERPRISE_PATH_VALUED_SQUARE_ROOT_OPERATOR_20260821.md`, `ENTERPRISE_VECTOR_NORM_ENDPOINT_REVERSE_GEODESIC_SEGMENT_20260817.md`, `ENTERPRISE_SEGMENT_ALL_SHORTEST_PATHS_20260817.md`, `ENTERPRISE_THREE_POSITIVE_AXIS_OVERLAPPING_CIRCLE_CELL_PLANE_20260820.md`, `ENTERPRISE_COORDINATE_SYSTEM_AND_BRC_BRIDGE_20260816.md`, `ENTERPRISE_SQUARE_AND_ROOT_SIGNED_ORIGIN_ONE_20260817.md`, `ENTERPRISE_ORIGIN_IS_DIAMETER_ONE_CIRCLE_20260817.md`, `ENTERPRISE_CHAMBER_LOCAL_ALGEBRAIC_VECTOR_OPERATIONS_20260817.md`, `ENTERPRISE_SIGNED_ORIGIN_ONE_COORDINATE_20260817.md`, `ENTERPRISE_VECTOR_RADIUS_DISCRETE_ROTATION_THEORY_20260817.md`, and `ENTERPRISE_POINT_ORIGIN_AND_DISPLACEMENT_ZERO_20260817.md`. The two explicit inverse hits are not evidence of LP011's claimed original dominant-axis caller. The remaining caller/provenance question is still **UNRESOLVED_PROVENANCE** outside this bounded corpus. No claim of repository-wide negative coverage.

Current consumer readbacks: R061 directed gauge blob `875e3b274e5be03c5872f782872065a0b96d14eb` is retyped to relative observer; R062 BRC bridge `97ab1403ab04b4fa80034625fb1b2e3ed115e59b` is retyped to signed native paths; bidirectional spectrum `358a4997157d7546d88e63ae8d32e95feebf9c08` is observer-diagnostic; derived diagonal quotient `175d2c0f00db8e94a263442dbdc77928c0dc9567` is relative-only. These four current named downstream surfaces already preserve their corrected type boundaries. R063 is the concrete **still-live sector/native interface needing an explicit signed lift**; revise its downstream type/routing through the authorized review rather than rewriting any frozen Result as though accepted.

## 5. Return and immutable frontier

- **Complete this unit:** signed two-axis R063 lift theorem, exact N=2500 certificate, 100-radius implementation check and targeted 16-file LP011 search. Preserve the preceding LP011 chamber/inverse theorem without rederivation.
- **Current unfinished unit:** source-bound full finite legacy consumer/dependency/28-row coverage manifest, with exact remaining original LP011 claim/caller, R063 consumer admission/retyping decision and any additional active erroneous native surfaces.
- **Do not repeat:** the frozen 28-row supplement, native 30/846 shell, 72 positive-sector history, 111 kernel, filled-disk carrier proof, R063 original C3/C4 checker, signed median-bit inverse and all previously verified native proofs.
- **Next precise action:** bind this immutable note/checker to the existing X6 parent at the permitted Source/RA checkpoint route and review the R063 interface; continue named caller-by-caller audit of current surfaces. Preserve prior original `onhour-20261112-0519-x6-postscience-continuation` result `SUCCEEDED` as **read-only continuation**, not a new winning claim. Own Research conversation label is `chatgpt-research-onhour-enterprise-math-20260923`; the maintenance lane is distinct. No service-issued original session key / winning current X6 CLAIM/run was established in this turn, so no native semantic checkpoint or Result was attempted.

Scientific author: current TASK_RESEARCH continuation, NONBLIND; previous author/review/owner identities are preserved, not adopted. No P000, active worldview, accepted RR/DR or task publication was modified.
