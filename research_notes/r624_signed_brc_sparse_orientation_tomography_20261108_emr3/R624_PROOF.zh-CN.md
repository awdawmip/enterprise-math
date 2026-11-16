# R624｜冻结 signed BRC 的双系数方向层析定理

Date: 2026-11-08
Status: AUTHOR-SIDE / EXACT PROOF / UNREVIEWED / NOT_ADMITTED
Scientific pin: R462 immutable commit 18783e01e3646c72b7aab3b16d3f565e83e6446f, theta=0; original signed K Git blob 7fa7a762f758b30c6090468ac43487daa34abad8.
Continuation: R623 b63f9b41b6c190fd3b291f829986cc9aee21885f.

## 1. Declared X6 orientation calibration

For π in the S6 direction configurations, let π(j) be the spatial axis occupied by basic axis j. The signed BRC factor seen at +e_x is K_(2π^-1(x)-1); that at -e_x is K_(2π^-1(x)). A uniform scalar calibration channel (sign ε, degree h) reports the exact integer coefficient [t^h] of that *frozen original signed K factor* on each of the six spatial axes. This is a typed K-kernel observation; it is distinct from a sensor of the multiplied packet amplitude or a native physical field operation.

The original K formula is

K_i(t) = -t^(i-1) sum_(r=1)^4 d_r(i) (1+t)^(i+1-r),

omitting r with i+1-r<0; d_1=-binom(4,i)+binom(2,i-1), d_2=binom(5,i-1)-binom(5,i-2), d_3=binom(7,i-2), d_4=-binom(9,i-3), binomial terms outside range zero.

## 2. Constructive two-probe theorem

Take the same two coefficient queries on every spatial axis:

A=(+,8), B=(-,3).

Their ordered signatures for the basic axes j=1..6 are:

| basic j | [t^8]K_(2j-1) | [t^3]K_(2j) |
|--:|--:|--:|
| 1 | 0 | 4 |
| 2 | 0 | -11 |
| 3 | 5 | 0 |
| 4 | 561 | 0 |
| 5 | 83 | 0 |
| 6 | 0 | 0 |

All six rows are pairwise distinct, obtained exactly from the signed K binomial formula. Given the two measured values for a spatial axis x, look up its unique basic j and assign π^-1(x)=j. Across all six spatial axes this reconstructs π uniquely; consequently all 6!=720 orientations are distinct. Simultaneously permuting spatial axes simply permutes the six signatures, hence the calibration map is S6-equivariant.

Once the orientation is reconstructed, its twelve signed-branch indices and branch-grade increments are known, so *provided all the packet's other needed state is retained*, any finite formal R623 signed-K append sequence can be performed with the exact original factors. The two coefficients encode orientation, not the packet amplitude, provenance, history or time.

## 3. Exact minimality and unique degree-optimal pair

**Theorem.** Among nonadaptive, spatially uniform, single signed-branch coefficient channels (ε,h), with h a nonnegative integer:

(i) One channel, at any degree h, does not identify all six axes.

(ii) Every distinguishing family has highest coefficient degree at least 8.

(iii) Among the 18 candidate channels with degree 0..8, the only unordered distinguishing pair is { (+,8), (-,3) }. Therefore minimum channel count is two and the degree-optimal two-channel set is unique up to ordering.

**Proof (i).** For sign + and h<8, axes j5,j6 both have zero coefficients, since K9 and K11 start at degrees 8 and 10. For sign + and h≥8, j1,j2 both give zero since K1 has degree 1 and K3 degree 5. For sign - and h<9, j5,j6 both have zero coefficients since K10 and K12 start at degrees 9 and 11. For sign - and h≥9, j1,j2 both vanish since K2 and K4 have degrees 3 and 7. So every single query has a collision.

**Proof (ii).** With every h≤7, both signs of j5 and j6 vanish. Distinguishing them requires h≥8.

**Proof (iii).** Among degree≤8 channels, the sole channel separating j5 and j6 is (+,8). At (+,8), j1,j2,j6 all return zero. The second channel must therefore have three pairwise distinct values on these axes. All j6 coefficients through degree 8 vanish; thus values for j1,j2 must be different from zero and one another. For positive sign, K1 is supported only in degrees 0,1 and K3 only in degrees 2..5; no common h yields both nonzero. For negative sign, the support intersection of K2 (degrees 1..3) and K4 (degrees 3..7) is exactly degree 3. There [t^3]K2=4 and [t^3]K4=-11. The displayed table proves sufficiency. QED.

The proof is universal over all π∈S6 for the frozen signed K polynomials and the stated channel language. It does not require a finite-computation extrapolation.

## 4. Sparse-versus-full observation and native interface

R622 reached full 720-state orientation classification with consecutive coefficient jets of degree d=8 on both signs. Here only *two targeted scalar signed coefficients per spatial axis* suffice (12 scalar readings in all). This is a reduction in the **observation count**, not an unmeasured end-to-end computing-speed claim; computing a t^8 coefficient may have its own acquisition cost. R623's modulus/grade quotient remains valid for its distinct observation/action language.

The exact signed BRC source is retained. The six-dimensional native X6 spatial Cell torsor and separately typed time follow P000. In current source definitions/HEARTBEAT_WORLD_NATIVE_X6_TIME.json, fixed_heartbeat_program is null. Therefore the calibrated readout is a testable algebraic bridge proposal, not an assertion that an implemented native field device supplies the two probes.

## 5. Verification

Attached R624_VERIFY.js uses BigInt exact binomial coefficients, independently reconstructs all twelve frozen K factors, checks the six signed signatures, examines all 153 two-channel choices from 18 candidates with degree 0..8, scans all single-coefficient queries through maximum K polynomial degree, and enumerates all 720 permutations. Exactly one candidate pair works, and all 720 codes are distinct. R624_EVIDENCE.json is the execution result.

Marker: R624_EXACT_SPARSE_TWO_PROBE_BRC_ORIENTATION_PASS.
Validation scope: frozen K at theta=0; sparse uniform kernel coefficient calibration; all S6 orientations. Independent Driver mathematical review: pending; native Source identity and active task Owner: unconfirmed.

## 6. Next open problem

Find an actually registered X6 internal-field or time-evolution update F with typed inputs and observations, then test whether its readout can factor through these two signed kernel-coefficient channels, or construct a minimal viable BRC-native joint readout. For each F test future-fiber constancy, provenance and joint relation retention, with a concrete one-operation witness. Do not equate BRC branch grade to heartbeat time.
