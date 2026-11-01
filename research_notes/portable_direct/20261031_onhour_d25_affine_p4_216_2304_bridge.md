# D25: exact fourth-order affine 216/2304 bridge certificate and sharpness counterexamples

**2026-10-31 19:10 Asia/Hong_Kong · AUTHOR-SIDE / FINITE EXACT CERTIFICATE / OPEN CONJECTURE / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING.**

Mother objective: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`; immutable scientific source pin `c47e13e4aba0e006366f989d6334d443f6333ae3`. Research ordinary-control lane `chatgpt-research-onhour-enterprise-math-20260923`, distinct from maintenance. P000 and ACTIVE worldview retained. These are classical arithmetic scalar readouts **not** verified native X6/H0/B0/Frobenius transfers.

## Original distinct sums and the external theorem

For prime `p>3`, preserve full cutoffs and weights:

`A_p = Σ[k=0..p−1] (6k+1)·C(2k,k)^2·C(3k,k)/216^k`,
`B_p = Σ[k=0..p−1] (8k+1)·C(4k,2k)·C(2k,k)^2/2304^k`,
`χ = χ_{−3}(p)=1` if `p≡1 (mod 3)`, otherwise `−1`.

Guo–Zudilin, *A q-microscope for supercongruences*, Adv. Math. **346** (2019) 329–358, DOI `10.1016/j.aim.2019.02.008`, **prove** `B_p ≡ pχ (mod p³)`. This is not a theorem about A. Frozen D25 objective is `A_p≡p (mod p³)` for every `p≡13,19 (mod24)`, currently OPEN.

## New research finding: fourth-order affine bridge (CONJECTURE, not proved)

A sharper candidate than the old `A−B≡0 mod p³` is:

`A_p − 2B_p + pχ ≡ 0 (mod p⁴)`, proposed for **all primes p>3**.

If proved, this with the published B theorem yields `A_p≡pχ (mod p³)`; χ=1 in the original target classes. **The proposed universal affine bridge itself has NOT been proved.**

On the tested finite domain both A and B have the p³ baseline. Then define exact mod-p observer/valuation ports
`u_A=((A−pχ) mod p⁴)/p³`, `u_B=((B−pχ) mod p⁴)/p³`,
`u_gap=((A−B) mod p⁴)/p³`. The affine relation there is equivalent to `u_A=2u_B` and `u_gap=u_B` modulo p. These different ports may not be conflated.

## Actual exact finite execution

Ran a Python standard-library integer/sieve verifier twice over **all 1,752 primes 5≤p≤15,000**, of which **445** satisfy the original frozen `p mod 24∈{13,19}`. **0** p⁴ affine failures. Independently checked original integer-binomial sums against modular recurrences at p⁴ for `5,7,13,19,31,37,67,373`; p⁵ direct original checks for `13,19,373`; all PASS. No floating point; all inverted denominators for indices k<p are p-units. Unweighted recurrence:

`a[0]=b[0]=1`,
`a[k+1]/a[k]=(2k+1)(3k+1)(3k+2)/(36(k+1)^3)`,
`b[k+1]/b[k]=(4k+1)(2k+1)(4k+3)/(288(k+1)^3)`.

Apply weights `6k+1` and `8k+1` at summation. Exact ordered witness stream `(p,A4,B4,u_A,u_B,u_gap);` SHA256:
`242a7f35012cffa4e3e3bed3ea1a3f66d25d97b28794a2f5c6f365c0d31feaff`.
Executed full-source verifier: `d25_affine_p4_bridge_cert_20261031.py` (local artifact, available from originating ChatGPT research run; **not claimed uploaded as a GitHub program**).

| p | A mod p⁴ | B mod p⁴ | u_A | u_B | u_gap | affine mod p⁴ |
|---:|---:|---:|---:|---:|---:|---:|
| 13 | 19786 | 24180 | 9 | 11 | 11 | 0 |
| 19 | 82327 | 41173 | 12 | 6 | 6 | 0 |
| 373 | 11832087049 | 5916043711 | 228 | 114 | 114 | 0 |

## Two exact counterexamples to over-strengthened claims

1. **A and B do NOT agree mod p⁴**: at target p=13,
`A_13−B_13≡11×13³ ≠0 (mod13⁴)`. Also p=19 gives `6×19³`, p=373 gives `114×373³`. A WZ/CM proof may not discard this genuine comparator source defect.
2. **The affine formula does NOT automatically lift to p⁵**: independent direct-binomial calculations give `(A−2B+pχ)/p⁴ ≡ 9,14,174 (mod p)` for `p=13,19,373`, respectively. These prove the unmodified p⁵ statement false.

All above finite numerical statements are proven only within the explicitly computed prime domain, **not universal all-prime mathematical proofs**.

## Highest frontier, next scientific action, native debt

Previously accepted D24 first-digit UR remains frozen. The D25 second-digit theorem is OPEN. This new author-side candidate + 1,752-prime exact certificate + target counterexamples are additional evidence, **not** a Result or mathematical acceptance.

**Next precise unit:** derive a finite parametric WZ/creative telescoping, CM or q-microscopic identity that proves `A_p−2B_p+pχ≡0 mod p⁴` for all prime inputs or the two frozen target classes; alternatively prove the smaller required p³ bridge directly. Must preserve p−1 whole cutoffs, both original weights, p-adic valuation layers, nonzero A half-tail, and the nonzero p⁴ comparator defects (13/19/373). Avoid repeating the already completed p³ prime sweep and independent Gauss/Green auxiliary results.

Native support `awdawmip/enterprise-math#1559` is **NOT_EXECUTED/PENDING_OWNER**: fixed-373 original H0/B0 divided-power, semilinear Frobenius, native rank, signed Green/Hesse, κ and independent reproduction are not substituted by classical scalar calculation.

**Control receipts:** own-lane historical recovery `awdawmip/kimi-query-bridge#6632` did not establish current CLAIM/run; original dispatch `#6633` request `research-onhour-20261031-0205-dispatch-r15` FAILED `UPSTREAM_CODE_REVIEW_REQUIRED`. Current Gateway v0.6.11 reports `research_authority_granted=false`, `executor_binding_configured=false`. No duplicated mutation, formal Source checkpoint, role-bound register, Result, Driver review or admission has been asserted. Frozen source pin and existing hourly schedule/notification settings unchanged.
