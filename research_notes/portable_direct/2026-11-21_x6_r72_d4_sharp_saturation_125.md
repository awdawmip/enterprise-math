# X6 R72 — 四阶非均匀 BRC 观察的最小统一饱和门槛 P4=125

Date: 2026-11-21 (Asia/Shanghai)
Status: CONDITIONAL_EXACT_FINITE_CERTIFICATE / AUTHOR_RECHECKED / NOT_INDEPENDENTLY_REVIEWED
Scientific input: `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json`. Preserve P000 native six-axis/one-time setting, whole-triad `TRIADIC_CLOSURE_E`, joint-relation provenance, and non-identity of positive BRC moments with native Cell/Link/Port dynamics.
Immediate predecessor: `research_notes/portable_direct/2026-11-21_x6_r71_d4_weighted_ray_saturation_234.md`.

## Exact question and observer

This theorem concerns **only** the conditional normalized positive-count BRC star observer with four positive moments, not physical/native trajectory admissibility. For each named source Port, the independently reset second source produces a degree `d∈{0,1,2,3,4}`. The count vector is `c_d`, `sum c_d=p`. The observer is

`Y_t=m_t+b+e_t,  m_t=sum_{d=0}^4 c_d d^t,` for `t=1,...,4`;

`b` is one unknown common additive offset, `|e_t|≤η w_t`, and each `w_t>0`. The recovery target is the histogram `(c2,c3,c4)` only; no path, sign, joint history, provenance or future operation is asserted to descend through this histogram.

For a difference `a=(a2,a3,a4)∈Z^3`, let

`q(a)=max(sum_d max(a_d,0), sum_d max(-a_d,0))`.
Then `a` is realizable with `p` source Ports exactly when `q(a)≤p`. Set
`z=(z1,z2,z3,z4)=(0,2a2+6a3+12a4,6a2+24a3+60a4,14a2+78a3+252a4)`.
Define the six gaps `G(a)=(|z2-z1|,|z3-z1|,|z4-z1|,|z3-z2|,|z4-z2|,|z4-z3|)`.
For any positive weights, R68's pair threshold is
`η_pair(a;w)=1/2 max_{i<j} |zj-zi|/(wi+wj)`.
The optimal histogram-identification threshold is `η*_{p,4}(w)=min_{a≠0,q(a)≤p} η_pair(a;w)`.

## Main theorem: sharp all-weight saturation threshold

For every positive real weight vector `w∈(0,∞)^4` and every integer `p≥125`,

`η*_{p,4}(w)=η*_{125,4}(w)`.

The integer **125 is the smallest universally sufficient threshold**, i.e. there exist positive weights for which the thresholds at `p=124` and `p=125` differ.

More strongly, a fixed set `A` of **28 unoriented integer vectors** suffices for *all* Port counts `p≥4` and all positive weights:
`η*_{p,4}(w)=min_{a∈A,q(a)≤p} η_pair(a;w)`.
Here orientation `±a` is immaterial to `q,G,η_pair`.

The 28 triples, in ascending `q` (each encoded as `q:(a2,a3,a4)`), are:

```text
1:(1,0,0)        2:(0,2,-1)       3:(1,-3,1)      3:(2,-3,1)
3:(3,-1,0)       4:(1,3,-1)       4:(3,-4,1)      4:(4,-1,0)
5:(3,2,-1)       5:(4,-4,1)       5:(5,-1,0)      6:(5,-4,1)
6:(6,-1,0)       7:(3,-7,2)       7:(6,-4,1)      7:(7,-1,0)
9:(7,2,-1)      10:(9,-5,1)      11:(10,-5,1)    16:(15,-6,1)
22:(21,-7,1)    27:(24,-14,3)    39:(36,-16,3)   43:(39,-20,4)
47:(42,-24,5)   49:(45,-21,4)    71:(66,-28,5)  125:(114,-56,11)
```

## Proof

**Step 1: unrestricted integer differences reduce to q≤234.** The earlier R71 cone theorem (whose complete ray/triple certificate was independently recomputed here) forms the 9×3 map `T=[I3; all six signed moment-gap rows]`. The primitive ray enumeration gives 28 lines, 56 orientations, 212 mutually conformal unoriented ray triples (as oriented choices), maximal single-ray `q=125`, and maximal conformal triple `sum q=235`. By the R71 conformal cone decomposition, every integer `a≠0` admits `h≠0` with `q(h)≤min(q(a),234)` and all `G_i(h)≤G_i(a)`. This is a reduction of the exact *declared* observer, not of the underlying X6 source state.

**Step 2: exact bounded dominance certificate.** Consider all nonzero integer triples with `q(a)≤234` modulo overall sign. There are exactly **21,492,159** such unoriented triples. The independent full-cube checker `x6_r72_d4_atlas_verify.cpp` checks every one, without relying on discovery order, and verifies the following quantified finite statement:

`∀ a∈Z³\{0}, q(a)≤234: ∃u∈A: q(u)≤q(a) and G_i(u)≤G_i(a) (i=1,...,6).`

It returns `tested_unoriented=covered=21492159; failures=0; atlas_size=28; max_q=125`. The independent ascending-q enumeration `x6_r72_d4_atlas_discovery.cpp` generates the same 28-element undominated atlas; signed 3D cube and q-shell enumeration are independent enumeration mechanisms. The finite certificate is supplied as executable source and actual output: it is not claimed to be a human-only proof or independent mathematical review.

Combining Steps 1 and 2, for every nonzero difference feasible at `p`, a vector `u∈A` is feasible at the same `p` and has `η_pair(u;w)≤η_pair(a;w)` for **every** positive weight vector. Since the maximum `q` in `A` is 125, saturation holds for `p≥125`.

**Step 3: sharpness at weight profile (1,24,1,1).** In this profile, channels 1, 3, 4 are the precise trio, while channel 2 is noisy. The exact common-zero kernel of their two independent differences `z3=z4=0` is `Z(114,-56,11)`: take the primitive cross product of rows `(6,24,60)` and `(14,78,252)`. Its smallest nonzero Port demand is `q=125`. If `q(a)<125`, at least one of `z3,z4` is a nonzero even integer. Consequently a precise-channel pair gap is ≥2 and `η_pair(a;(1,24,1,1))≥1/2`. This bound is attained already at `q=11` by `a=(10,-5,1)` with `z=(0,2,0,2)`.

For `a=(114,-56,11)` one has `z=(0,24,0,0)`, `q=125`, hence `η_pair=12/25`. Every other nonzero `a` either has a precise-channel gap ≥2, implying `η_pair≥1/2`, or belongs to the integer kernel and is a multiple of this primitive vector, implying `η_pair≥12/25`. Thus the *exact* special-profile staircase is

`η*_{p,4}(1,24,1,1)=1/2 for 11≤p≤124; 12/25 for p≥125.`

In particular 124 is insufficient universally. Together with Step 2 this proves `P4=125`. QED (relative to explicitly executable exhaustive finite certificate).

## Computational evidence

- `x6_r72_d4_atlas_discovery.cpp`: exact q-shell enumeration of 21,492,159 unoriented triples, 28 undominated atlas entries, max q=125.
- `x6_r72_d4_atlas_verify.cpp`: independent signed-cube full check of all 21,492,159 unoriented triples against 28 witnesses, zero failures.
- `x6_r72_d4_ray_recheck.py`: independent exact recomputation of R71 bound: 28 unoriented primitive ray lines, 56 signed rays, 212 conformal triples, max q sum=235, hence q≤234 sufficiency.
- `x6_r72_d4_results.json`: exact inputs, observed counts, special-profile rational witness and hashes/evidence scope.

This is an **exhaustive finite computational certificate plus an exact general reduction and a symbolic lower-bound proof**. Human independent review and checking the executables in another environment remain open. The theorem does **not** assert native X6 time dynamics, triadic admission or signed BRC amplitude cancellation.

## Next questions

Determine the smallest *weight-specific* Port threshold for arbitrary `w`, partition weight-ratio space into exact optimality chambers for the 28 candidates (some may never be optimal), and test native source-admissible triadic Cell/Link/Port event trajectories and future observer safety separately; do not infer them from histogram recovery.

Attribution: independent portable research continuing R61–R71 under existing provenance. Historical researcher `EM-X6-214D9C` and Activity `RA-545183ADD4EF71C3E4698AEE` are source references, not a claim of current private capability, execution ownership or formal PROGRESS.
