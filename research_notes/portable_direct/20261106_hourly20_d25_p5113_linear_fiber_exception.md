# D25: p=5113 gives a linear-only second-digit source fiber

Date: 2026-11-06. TASK_RESEARCH author-side portable evidence; **UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_CHECKPOINT**.
Configured Research logical lane: `chatgpt-research-hourly-enterprise-math-20260923` (no platform identity attestation).
Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`; frozen scientific pin `c47e13e4aba0e006366f989d6334d443f6333ae3` unchanged.

## Exact proposition

Fix prime p = 6m+1 > 3, s=(2m,3m,4m). For j=0,...,p-1, define the labelled auxiliary source and weighted observer

```text
U_j(z1,z2,z3) = (-1/2)^j * binom(s1+z1,j) * binom(s2+z2,j) * binom(s3+z3,j)
F_p(z) = sum_{j=0}^{p-1} (6j+1) U_j(z).
v = (-1/3,-1/2,-2/3) modulo p; d=(1,0,1).
D_p(lambda) = [F_p(p*(v+lambda*d)) - F_p(p*v)] / p^2  modulo p.
```

All j! are units modulo p^3. The previously proved source-jet Taylor theorem shows: whenever the directional first derivative along d vanishes modulo p, the quotient is an exact quadratic polynomial on the entire finite field:

```text
D_p(lambda) = k_p*lambda + c_p*lambda^2 (mod p), for every lambda in F_p.
```

**New prime-specific theorem:** p=5113 is prime, p mod 24 = 1, and the complete directional second-digit map is

```text
D_5113(lambda) = 3118*lambda (mod 5113).
k_5113=3118 != 0; c_5113=0.
```

Consequently, this map is a **bijection on all 5113 source directions** lambda; the unchanged aggregate has exactly one preimage on this line. This is a linear-only curvature-zero stratum, distinct from the earlier two-root and pure-quadratic directional families.

## Proof by exact finite sum and general degree bound

Use integer representatives of v and keep each shift `v+lambda*d` as an integer shift **without reduction modulo p inside the p^3 evaluation**. With p^2=26142769 and p^3=133667977897, an independent full original 5113-term sum gives:

```text
lambda     F_5113(p*(v+lambda*d)) mod p^3    [F(lambda)-F(0)]/p^2 mod p
 0         77356458584                       0
 1         25201634429                       3118
-1         129511282739                      1995
 2         106714788171                      1123
 5         83918293603                       251
17         126400293228                      1876
53         120178314206                      1638
```

From lambda=1 and lambda=-1, both differences are multiples of p^2. The first-order derivative along d therefore vanishes modulo p. Taylor expansion in a p-multiple then gives the exact degree-two formula for every lambda, not merely the tested list. The two coefficients are determined by the two evaluations:

```text
k = (D(1)-D(-1))/2 = (3118-1995)/2 = 3118 (mod 5113)
c = (D(1)+D(-1))/2 = (3118+1995)/2 = 0 (mod 5113).
```

(The division by 2 is modular.) Independent evaluations at the additional four shifts match `3118*lambda mod 5113`. The labelled first port changes by `[U_1(p*(v+d))-U_1(p*v)]/p = -1/4 = 1278 mod 5113`; the provenance remains explicitly observable.

The Fermat quotient `q_5113(2)=(2^5112-1)/5113 mod 5113` equals 665, so this concrete case satisfies `k=-3*q_5113(2)=3118 mod 5113`. The corresponding all-prime formula remains a conjecture.

The independent standard-library reproduction is `d25_p5113_direct_certificate_20261106.py`, next to this note.

## Second research increment: expanded exact prime scan

A compiled C++ extension of the prior undivided-binomial recurrence `d25_outer_fiber_strata_20261106.py` evaluated p-adic first derivatives modulo p^2, Hessians modulo p and Fermat quotients for every prime `7 <= p <= 100000, p mod 6 = 1`.

There are **4784 such primes**, including **2398 parent-target primes** with p mod 24 in {13,19}. Exact computed findings for this finite domain:

* All 4784 give `T1+T3=0 mod p` and `k_p+3*q_p(2)=0 mod p`.
* `c_p=0` occurs exactly once, at **p=5113**.
* `q_p(2)=0` occurs exactly at p=1093 and p=3511.
* `T1=T3=0` occurs exactly at p=7 and p=211.

A validation defect was found and corrected *before* the reported run: the initial C++ rewrite doubled the Hessian diagonal despite the recurrence already producing second derivatives. A subsequent preliminary run beyond p=65536 exposed 64-bit modular multiplication overflow; the final run uses `unsigned __int128` products. The corrected implementation first reproduced all 330 prior Python cases through p=5000, then completed the 4784-prime range with **0 failed checks**. The independent direct p=5113 sum above requires neither the scanner's Hessian nor its Fermat-quotient formula.

Locally executed scan source: `/mnt/data/d25_wieferich_outer_scan_20261106.cpp`; exact direct-sum source is also published in this repository. The finite scan is evidence of the stated finite population, not an all-prime proof.

## BRC, result class and next step

BRC representation: labelled three-source p-adic jets; observer: weighted scalar plus labelled port U_1; operation: the outer-source d-line perturbation; information fiber: governed by (k_p,c_p). Reuse: earlier Taylor/Hessian source law `REUSE_APPLIED`; arithmetic scan `EXTEND_EXISTING_TOOL` within that family. No new general-purpose toolbox claim.

This new prime lies in p mod 24 = 1, serving as an informative adjacent class; the frozen mother target stays `Delta_p-R_p=0 mod p` for p mod 24 in {13,19}.

Next mathematical action: derive a symbolic finite-sum expression for `c_p`, and test which part permits the curvature-zero case at 5113 while keeping the WZ identity `T1+T3=A_m-B_m=0`, Fermat quotient and original p=373 H0/B0, Frobenius, eta/kappa as open obligations.

Control state observed 2026-11-06: the original requests `em-h20-20261106-1324-d25-task-r13` and `em-h20-20261106-1324-d25-cont-r13` remain `WAITING_RESOURCE/EVENT_COLLECTION_IO`; current native successor session/claim/run was not verified or modified here. Existing support issue: #1558. This author-side note is not a native Source checkpoint.

## Independent labelled-jet arithmetic certificate (same prime, different calculation)

A separate undivided-binomial recurrence, reducing first derivatives modulo p^2 and the complete labelled Hessian modulo p, gives for p=5113:

```text
T = (2858, 4710, 2255)                   mod 5113
A = (15116886, 25262930, 17243291)     mod 5113^2
H = [ [2979,  908,  255],
      [ 908,   78, 2557],
      [ 255, 2557, 1624] ]               mod 5113
v = (1704,2556,3408)                    mod 5113
```

In particular the two outer gradients sum to `2858+2255=5113`, while the curvature numerator is **literally**
`H11+2*H13+H33 = 2979+2*255+1624 = 5113`, so `c=0 mod p`. The lifted outer gradient contributes `(A1+A3)/p=1216 mod p` and the mixed term contributes `v^T H d=1902 mod p`; together `k=1216+1902=3118 mod p`.

The full-sum certificate does not use these Hessian values, giving an independent path to the same all-lambda conclusion. This exact curvature cancellation is the smallest new symbolic subproblem: express the combination `H11+2*H13+H33` as a provenance-preserving finite sum and study its prime divisibility.
