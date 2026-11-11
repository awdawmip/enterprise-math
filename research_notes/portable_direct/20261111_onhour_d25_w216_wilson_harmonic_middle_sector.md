# D25/LIFT — Original W216 middle band as Wilson quotient + harmonic jet

Date: 2026-11-11 (Asia/Hong_Kong). Status: AUTHOR_SIDE / EXACT_IDENTITY / SELECTED_31_PRIME_INTEGER_CHECKS / UNREVIEWED / NOT_ADMITTED / NATIVE_H0B0_NOT_RUN.
Mother Objective: ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION.
Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT.
Task publication: TP2-B6F4FC938FF94941C1B7.
Frozen scientific input pin: awdawmip/enterprise-math@c47e13e4aba0e006366f989d6334d443f6333ae3 (unchanged).
Logical Research lane: chatgpt-research-onhour-enterprise-math-20260923.
Author-side companion checker: research_notes/portable_direct/d25_w216_wilson_harmonic_middle_sector_20261111.py.

## Exact local theorem (all primes p=6m+1 >=7)

Use the *original frozen* W216 coefficients and signed weights

    a_k = (2k)!(3k)! / (216^k (k!)^5),   w_k=6k+1,
    W_p = sum_{k=0}^{p-1} w_k a_k.

Set n=3m=(p-1)/2, M=p^3, Q_p=((p-1)!+1)/p mod p (Wilson quotient). For every 2m<k<=3m put r_k=3k-p (so 0<r_k<p), and define p-integral quantities

    C_k = (2k)! r_k! / (216^k (k!)^5),
    H_r = sum_{j=1}^r 1/j.

Then, with all divisions by p-units in Z_(p),

    a_k / p = (p-1)! C_k prod_{j=1}^{r_k}(1+p/j)              (EXACT),

and consequently

    a_k / p = -C_k {1+p(H_{r_k}-Q_p)}                  (mod p^2).    (1)

The native coefficient is valuation-one in this band; formula (1) computes both retained p-adic digits without using a p-denominator inverse.

Let

    S0 = sum_{k=0}^{2m} w_k a_k             (mod p^3),
    C0 = sum_{k=2m+1}^{3m} w_k C_k          (mod p^2),
    A  = sum_{k=2m+1}^{3m} w_k C_k H_{r_k}  (mod p),
    J  = sum_{k=2m+1}^{3m} w_k C_k          (mod p).

The original W216 half sum L_p=sum_{k=0}^{3m}w_ka_k satisfies the *exact all-prime congruence*

    L_p = S0 - p*C0 - p^2*(A - Q_p*J)       (mod p^3).    (2)

This is the new result. The middle-index source is now an explicit Wilson quotient plus finite harmonic jet; its observer keeps the original index and valuation, rather than replacing the original W216 by the separate scalar g/h or E3 curve.

Combine (2) with the previously established *exact reflected tail* (reused here, not claimed as new):

    W_p = L_p + p^2*chi_6*D_m/9             (mod p^3),
    chi_6=(6/p),

    D_m=(4+6*x*d/dx) H_m(x) |_{x=1/2},
    H_m(x)=sum_{j=0}^{m-1}
        (1)_j (5/6)_j (7/6)_j / (3/2)_j^3 * x^j.

It follows that the original W216 observer is exactly

    W_p = S0 - p*C0
          + p^2*(-A + Q_p*J + chi_6*D_m/9) (mod p^3).   (3)

In both frozen classes p=13,19 mod24, the accepted first-digit result ensures W_p=p mod p^2. The open second-digit cancellation becomes the concrete condition that (3) equals p modulo p^3. Formula (3) is an exact arithmetic route to that condition, not an all-prime proof of the condition itself.

## Proof

For 2m<k<=3m, 2k<p and p<=3k<2p. Writing 3k=p+r gives the exact factorial factorization

    (3k)! = p*(p-1)!*r!*prod_{j=1}^r(1+p/j).

Here 216, k!, r!, (2k)! are p-units. Hence the first displayed identity. Wilson's theorem makes Q_p integral, (p-1)!=-1+pQ_p, and prod(1+p/j)=1+pH_r modulo p^2. Multiplication proves (1). Summing p times (1) over the middle band gives (2); substituting the exact previously-proved mirror/dual-tail theorem gives (3). No infinite-series or empirical step enters these identities.

## Executed exact certificate and information-loss control

The accompanying checker constructs original coefficients by the independent binomial-factorial ratio recurrence modulo p^3, and evaluates (1) by a factorial / Wilson quotient / harmonic route modulo p^2. It checks each middle-band a_k/p, the whole half-sum L_p and W_p reconstructed with the already verified dual-tail derivative against the original p-term sum.

Selected **31** distinct primes p=6m+1, 7<=p<=733, all passed. This is a selected finite set, not an exhaustive interval. Exact source recurrence is used for W216, not the g/h scalar proxy. The BRC-style branch carrier is the ordered original k, with valuation tiers v=0 (k<=2m), v=1 (2m<k<=3m), and the already-retained mirrored higher tiers.

For p=373:

    p^2=139129, p^3=51895117, Q_p=224,
    S0=28094360,
    C0=137237 (mod139129),
    J=346, A=20, A-Q_p*J=100 (mod373),
    L_p=14887176 (mod51895117),
    D_62=217, chi_6=-1, chi_6*D_62/9=266 (mod373),
    W_373=373 (mod51895117).

Explicitly,

    28094360 - 373*137237 - 139129*100
      = -37007941 = 14887176 (mod51895117),

    14887176+139129*266=51895490 = 373 (mod51895117).

A falsifying negative control for premature quotienting is available: if Q_p is deleted from (1), the p=373 formula yields

    W_wrong = 373 + 80*139129 (mod51895117),

not 373. The correction coefficient J=346 is nonzero, so retaining only harmonic H_r and dropping the factorial-block Wilson quotient loses an actual second-digit contribution in this representation.

## Provenance, relative value and continuation

The 2026-11-11 H40 three-sector source bridge reconstructs **g_p/h_p** using the two roots j=m,2m of its different (1/6,1/3) coefficient product. This result is instead about the **original W216 triple-hypergeometric coefficient** and its middle band. The two artifacts retain distinct input objects and evidence status. The prior 2026-11-11 reflected-half/Legendre-dual-tail theorem is consumed, not reproved.

The newly isolated middle band offers a precise harmonic/Wilson cancellation target; the lower band S0 still needs p^3 precision, and this theorem alone is not a strict full-target reduction or proof of JT2. A meaningful next mathematical unit is to derive an independent algebraic relation for S0-p*C0 and the finite field combination (-A+Q_p J+chi_6 D_m/9), or locate a genuine original-class counterexample.

The highest-priority *native* experiment remains same-original-class H0/B0 divided-power [X]U mod139129 at p=373, with actual rank, semilinear Frobenius direction, eta, odd Green/Hesse signed kappa, original Delta_p-R_p and independently reproducible raw outputs (existing issue #1559; no confirmed native executor). No surrogate coefficient proof is represented as that experiment.

Source status for this author-side checkpoint: earlier exact continuation request onhour11-20261111-1608-exact-cont was confirmed SUCCEEDED, while next exact read onhour11-20261111-1701-cont was QUEUED at the time this note was drafted. Own Sites recovery returned SITE_CONTROL_OWN_ISSUED_SESSION_REQUIRED, so no new formal CLAIM/open/native checkpoint is asserted. Historical Researcher/session identity is provenance only.
