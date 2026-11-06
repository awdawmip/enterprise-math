# D25 — first linear-only outer-source second-digit fiber at p=5113

Date: 2026-11-06. Author-side portable arithmetic for `TASK_RESEARCH`, not an authorized native Result/checkpoint or independent review.
Logical Research lane label: `chatgpt-research-hourly-enterprise-math-20260923` (configured, not platform-attested).
Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`; original scientific pin `c47e13e4aba0e006366f989d6334d443f6333ae3` retained.

## Proposition and proof

Take the explicit auxiliary labelled source family
[
U_j(mathbf z)=(-2)^{-j}prod_{i=1}^{3}inom{s_i+z_i}{j},quad
s=(2m,3m,4m),quad p=6m+1,quad
F_p(mathbf z)=sum_{j=0}^{p-1}(6j+1)U_j(mathbf z).
]
This is the **auxiliary source observer**, not the native H0/B0 experimental readout.
For every prime (p>3), the polynomial coefficients are (p)-integral through (j=p-1). Fix any integer representatives (v) of ((-1/3,-1/2,-2/3)mod p) and (d=(1,0,1)). If the first-order directional derivative is zero modulo (p), then
[
D_p(lambda):=rac{F_p(p(v+lambda d))-F_p(pv)}{p^2}mod p
=k_plambda+c_plambda^2.
]
This exact quadratic law for (lambdainmathbb F_p) follows from Taylor expansion modulo (p^3); it reuses the existing Hessian-jet result, rather than introducing a new universal theorem. A different choice of lifts changes neither two displayed coefficients modulo (p).

**New exact prime-specific result.** The integer (p=5113) is prime, (pequiv1pmod{24}), and
[
oxed{D_{5113}(lambda)=3118lambdapmod{5113},quad c_{5113}=0,quad k_{5113}=3118
e0.}
]
Hence the restriction of the second-digit observer to the complete 5113-element outer-source line is a **bijection** to (mathbb F_{5113}), and the base observation has precisely one preimage on this line. This is a third directional fiber shape, alongside the earlier two-root quadratic and pure-quadratic examples. Its existence shows that the curvature (c_p) need not be a unit for every prime (pequiv1pmod6).

**Full exact finite-sum certificate.** The independently evaluated original 5113-term integer sums, all modulo (p^3=133667977897), are:
[
F_p(pv)=77356458584;quad
F_p(p(v+d))=25201634429;quad
F_p(p(v-d))=129511282739.
]
Both differences are divisible by (p^2=26142769), with respective quotients (3118,1995mod p). Since a quadratic polynomial in (lambda) governs every input, these three complete sums establish the directional derivative condition as well as
[
k=(3118-1995)/2=3118,qquad c=(3118+1995)/2=0pmod{5113}.
]
Independent full-sum calculations at (lambda=2,5,17,53) give second-digit quotients (1123,251,1876,1638), respectively, matching (3118lambdamod5113). The source-labelled (j=1) port changes by
[
[U_1(p(v+d))-U_1(pv)]/p=-1/4=1278pmod{5113}.
]
This labels the direction even as the aggregate retains only its linear readout.

The Fermat quotient is (q_{5113}(2)=665); the observed (k=3118) also agrees with the **still-conjectural universal relation** (k_p=-3q_p(2)). Here the equality is a certified prime-specific calculation.

## Second unit — expanded exact finite scan

Reusing the existing `d25_outer_fiber_strata_20261106.py` algorithm (undivided binomial Taylor recurrence) and extending it in compiled C++ to all primes (7le ple100000), (pequiv1mod6), yields **4784/4784 exact checks** of (T_1+T_3=0) and (k_p+3q_p(2)=0) over this *finite* domain. Among these 4784 primes, 2398 satisfy the parent target congruence (pequiv13,19mod24).

Within this complete tested domain:
- (c_p=0) exactly at (p=5113);
- (q_p(2)=0) exactly at (p=1093,3511);
- (T_1=T_3=0) exactly at (p=7,211).

The C++ scan first reproduced all 330 earlier Python cases up to 5000, including the known (p=1093,3511) coefficients. A preliminary optimized implementation incorrectly doubled the **already second-differentiated** diagonal Hessian coefficients; this was corrected **before** the 4784-prime claimed run. A preliminary >65536 run suffered 64-bit multiplication overflow; switching the modular product to `__uint128_t` and rerunning the entire range produced the stated zero-failure result. The prior failed runs are not included in PASS coverage. Independently, the Python full-sum certificate above computes no Hessian and confirms the new exceptional prime.

Executable evidence: `d25_p5113_direct_certificate_20261106.py` (committed with this note), and the locally executed scan source `/mnt/data/d25_wieferich_outer_scan_20261106.cpp`. The scan's exact counts are finite computations; neither the outer-derivative identity nor the Fermat-quotient formula is claimed proven for all primes.

## Reuse and frontier

BRC carrier: labelled three-source jet over (mathbb Z_p/p^3); observer: the weighted scalar and labelled (U_1) port; operation: outer directional perturbation (lambda(1,0,1)). Reuse resolution: `REUSE_APPLIED` for the earlier exact Taylor/Hessian interface; `EXTEND_EXISTING_TOOL` for the prime range scan, not a new BRC theory. Information preserved: source direction and port derivative; the aggregate fiber type depends on ((k_p,c_p)).

The result is **AUTHOR-PROVED PRIME-SPECIFIC ALGEBRA / EXACT EXECUTED FINITE CERTIFICATE / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_CHECKPOINT**. The exceptional prime is (1mod24), whereas the frozen mother target remains (Delta_p-R_p=0mod p) for primes (pequiv13,19mod24). Continue by investigating the explicit rational/Hessian sum for (c_p=0) and looking for its factorization, while retaining the separate open WZ identity (T_1+T_3=A_m-B_m=0), Fermat-quotient identity, original (p=373) H0/B0 and Frobenius obligations. Avoid re-running existing verified finite cases merely to restate them.

Control remains separate: original read requests `em-h20-20261106-1324-d25-task-r13` and `em-h20-20261106-1324-d25-cont-r13` observed `WAITING_RESOURCE/EVENT_COLLECTION_IO` on 2026-11-06; native session/claim/run not verified in this run. Support: Enterprise Math issue #1558. No native service identity/CLAIM/OPEN or checkpoint created by this author-side artifact.
