# R5 — two-sided uniform resonance chambers and conserved split order losses

Date: 2026-11-12 Asia/Shanghai. **Status:** researcher-side exact rational finite theorem; formal Source Result and independent mathematical review pending. Subject: the frozen *external P/Q–BRC Blackwell auxiliary observer*, not a native X6 model.

## Frozen scientific inputs and lineage

- Global scientific pin `a01383f825ef9d43b4b754254303298c64041568`, EM scientific pin `86149263e38c22292c9def1e0f69092efa1be77e`.
- Original 28-dimensional strictly positive rational state `X`, 15 labeled basic residual moves `M_1,...,M_15`, observer `A`, and exact maximal ray endpoint `epsilon_max=9/115400000`: immutable [PR #2102, commit 435e77a](https://github.com/awdawmip/enterprise-math/commit/435e77af0d180eac32bd1f9c4c464bc4010b7551).
- Original one-coordinate integer subset-sum spectrum `E0` of exactly 1,144 interior thresholds: PR #2108, commit `343ef84562909be87f520049893320d204fa9c4b`.
- Exact single positive perturbation witness: [PR #2111, commit f545f38](https://github.com/awdawmip/enterprise-math/commit/f545f3882b16c1b9d5bab60b5c6eb832b2debe36).
- All new statements below hold for that **same** observer, 15 labeled moves and original frozen scientific inputs. There is no task-ownership, P000 or native-dynamics change.

## Theorem: a **uniform interval** on both sides of the original resonance

Write `X_(i,j)` for target `i=0,...,6`, source `j=1,2,3,5`, and set

```text
x = X_(0,3) = X_(1,3) = 155682221/25142124560000000
rho = x/100000 = 155682221/2514212456000000000000
epsilon_max = 9/115400000.
```

Define the signed six-arc residual `H` on source 3 with entries `(-23,+28,-5)` on targets `(1,2,6)`, the opposite entries at source 1, and zero elsewhere. Then `AH=0` exactly. For every rational `eta` satisfying `-rho <= eta <= rho`, let `X(eta)=X+eta*H`. Every one of the 28 initial masses is positive; `A X(eta)=AX`; and `epsilon_max` remains the **exact maximal nonnegative endpoint** for `X(eta)+epsilon*D`, `D=sum_a M_a`.

For each nonempty subset `S` of the 15 *labeled* moves define the first-zero time

```text
tau_S(eta) = min_{k : M_S[k]<0} -(X[k]+eta*H[k])/M_S[k],
M_S = sum_{a in S} M_a.
```

The finite set of first-zero times within `(0,epsilon_max]` is `E(eta)`. Let

```text
w = (336,184,18,169,64,84,299,126,52,16,-420,-483,-144,-221,-80)
E0 = { -36*x/h : h=sum_{a in S}w_a <= -3, S subset of {1,...,15} }.
```

There are exactly **1,144** distinct elements of `E0`, all in `(0,epsilon_max)`. Then:

```text
E(0) = E0 union {epsilon_max}                         (1145 distinct values)

E(eta) = E0 union {epsilon_max}
               union {(x-23*eta)/15,
                      (x-23*eta)/12,
                      (x-23*eta)/3}                    (1148 distinct values)
          whenever 0 < |eta| <= rho.
```

Thus **both** perturbation signs split the same three originally coincident resource thresholds. Every sufficiently small nonzero signed perturbation in this explicit interval creates exactly three new first-zero values; it is not merely a result for a single positive witness.

The original coincidence locations are the 607th, 715th and 1039th members (1-based) of the sorted `E0`, corresponding respectively to `q=15,12,3`. At `eta>0`, each moving threshold precedes its old fixed `x/q`; at `eta<0`, it follows it. All six distances to the nearest adjacent fixed phase exceed `rho` in the `eta` coordinate. The smallest intersection distance is `x/12443`, so the explicit `rho=x/100000` stays strictly within every required nearest-neighbor gap.

## Proof: an exact all-prefix affine-chamber certificate

All move coefficients have denominator dividing 36. For every one of the `2^15-1=32,767` nonempty labeled subsets, form the integer vector `P_S=36 M_S`. Every subset has a negative coordinate, and each candidate first-zero function is **affine in eta**:

```text
T_(S,k)(eta) = 36*(X[k]+eta*H[k])/(-P_S[k]),  P_S[k]<0.
tau_S(eta) = min_k T_(S,k)(eta).
```

At `eta=0`, enumerate all coordinates attaining the minimum. For `eta>0`, select from these tied minima the coordinate with *smallest* affine slope; for `eta<0`, select the one with *largest* slope. For each subset and each sign, the attached exact checker verifies the chosen affine function is no greater than **every** competing coordinate candidate at `eta=sign*rho`. The same comparison holds at 0 by construction. The difference of two candidate functions is affine, hence the selected minimizer is valid on the **entire closed half interval**. It also checks that no prefix first-zero time crosses `epsilon_max` in the interior.

At both endpoints `eta=+rho,-rho`, exhaustive exact rational comparison of the resulting 32,767 prefix minima gives precisely `E0`, the maximal endpoint, and the three displayed moving values, with no missing `E0` values. The chosen minimizer always has coordinate `(target=0,source=3)`, `(target=1,source=3)`, or `(target=0,source=2)`. In the first case the zero time is fixed and belongs to `E0`; in the second it has one of three forms `(x-23 eta)/q`; the third contributes the original fixed ray endpoint. All six strict gap comparisons are checked exactly. Therefore this equality of complete first-zero spectra is valid for **every rational eta in the stated half intervals**, not just at the sampled endpoints.

Strict positivity of `X(eta)` at both extreme values, exact `AH=0`, and the unchanged endpoint bottleneck `(target=0,source=2)` prove the observer, initial positivity and maximal-ray assertions by affine interpolation. This proof is an exhaustive finite-domain certificate combined with a two-endpoint affine argument, not interpolation from numerical samples.

## Three split pairs: exact conservation of lost legal orders

At a fixed epsilon, a complete labeled order is legal iff all 15 prefix states have nonnegative mass. Integer Boolean-lattice DP computes the count with `ways(empty)=1` and `ways(S)=indicator(prefix S legal) * sum_{a in S}ways(S\{a})`. For each pair of moving and original fixed thresholds, the following *drops in the legal complete-order count* hold uniformly on the stated open half interval (the exact checker evaluates each sign at `eta=sign*rho`; the all-prefix affine-chamber certificate and strict phase separation establish constancy within each sign):

| Resource q | Signed eta | Moving threshold drop | Fixed threshold drop | Combined loss |
|---|---|---:|---:|---:|
| 15 | positive | 379,780,599,984 | 979,249,200 | 380,759,849,184 |
| 15 | negative | 379,627,579,392 | 1,132,269,792 | 380,759,849,184 |
| 12 | positive | 138,525,464,060 | 702,831,804 | 139,228,295,864 |
| 12 | negative | 138,461,493,728 | 766,802,136 | 139,228,295,864 |
| 3 | positive | 12,916,391,928 | 47,238,668 | 12,963,630,596 |
| 3 | negative | 12,891,471,896 | 72,158,700 | 12,963,630,596 |

Each **combined pair loss is independent of the perturbation sign** and agrees with the corresponding original unsplit drop at `eta=0`. Thus perturbation redistributes the lost schedules across two adjacent events while preserving the combined loss. The individual values reflect the actual labeled-resource constraints, not only the numerical threshold set.

## Exact executable evidence

- `VERIFY.py.gz.b64`: gzip/base64 lossless source of a Python-stdlib `Fraction` verifier. Decode with `base64 -d VERIFY.py.gz.b64 | gzip -d > VERIFY.py`; run alongside the original frozen `research_notes/brc_r5_sharp_nonlocal_fifteen_ray_20261111/VERIFY_R5_SHARP_RAY.py`.
- Decoded verifier SHA-256: `64b71c0f8d76114f038253c8b5897099d6668300cf7997142469fad1064c1ad8`.
- `EXACT_OUTPUT.txt`: captured successful execution of the mathematically equivalent program with the precise frozen `X` and `M_a` inputs in a local fixture; the published script imports the frozen parent program and has not separately been executed after its remote-byte publication. All `Fraction` and integer checks are exact.
- The checker includes all 32,767 masks, 28 coordinates, signed half-interval comparisons, endpoint retention, all six gap inequalities, and exact legal-order DP.

The result is a **local complete phase-chamber theorem** for a parameter interval in the external auxiliary model. Formal Source Result binding and independent proof review remain pending.

## Continuation question

Compute the **maximal** positive and negative rational-affine chamber boundaries for this frozen `X+eta H`, including all changes of winning prefix coordinates, extra-value collisions and genuine order-count jumps. Reuse the finite affine-ratio representation to build a general algorithm for complete-spectrum generation across one- or multi-parameter hidden-fiber perturbations; keep threshold generation distinct from first-zero activation and schedule-count loss. The unrelated current canonical task selected by the dispatch router requires its own typed continuation and authenticated CLAIM.
