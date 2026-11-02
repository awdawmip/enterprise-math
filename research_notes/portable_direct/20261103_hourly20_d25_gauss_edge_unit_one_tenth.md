# D25 — Universal Gauss far-edge unit = 1/10 and a prime-uniform Clausen carrier

2026-11-03 +08:00. AUTHOR-DERIVED / HAND-PROVED / FINITE-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING. Portable original-source algebra, not a native H0/B0 execution or Source checkpoint.

Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; frozen scientific pin c47e13e4aba0e006366f989d6334d443f6333ae3. The prior load-bearing proof is 20261103_r11_d25_clausen_defect_low_high_prefix.md (Git blob f751b08403629e0f35c43789566c426f4b22843c). Distinct mother Delta_p-R_p=0 (mod p) for p mod24 in {13,19} remains OPEN.

## U1 — exact all-prime theorem

Let p=6r+1>=7 be prime; c_k=(1/6)_k(1/3)_k/(k!)^2 in Z_(p), 0<=k<=p-1. Then v_p(c_(p-1))=2 and

    c_(p-1)/p^2 = 1/10 (mod p);
    c_(p-1) = p^2/10 (mod p^3).

Proof: In (1/6)_(p-1) the unique p-divisible factor is j=r, exactly p/6; in (1/3)_(p-1) the unique such factor is j=2r, exactly p/3. The other factors and (p-1)! are units. The residue permutation j -> j+a for j=0,...,p-1 shows that omitting the zero factor and endpoint j=p-1 leaves every nonzero F_p residue except a-1. Wilson's theorem gives

    product_{0<=j<=p-2,j!=r}(j+1/6)
       = (-1)/(-5/6) = 6/5 (mod p),
    product_{0<=j<=p-2,j!=2r}(j+1/3)
       = (-1)/(-2/3) = 3/2 (mod p).

As ((p-1)!)^2=1 (mod p), the p^2-divided product equals (1/6)(1/3)(6/5)(3/2)=1/10. All divisions are of p-units after exact removal of two p factors. QED.

## U2 — source-preserving two-prefix Clausen corollary

By the inherited exact backward Gauss coefficient recurrence,

    c_(n-1)/c_n = n^2 / ((n-5/6)(n-2/3)),

for every 0<=s<r, the new U1 implies

    c_(p-1-s)/p^2 = A_s/10 (mod p),
    A_s = (s!)^2 / ((11/6)_s (5/3)_s).

Define L_k=binom(r,k)binom(2r,k), Lambda_k=sum_{s<k}2^s A_s, Gamma_k=sum_{s<k}s2^s A_s. Substitution in the **previously proved H4** (not re-proved here) yields

    E_p = -(1/5) sum_{k=1}^r L_k 2^{-k}
          [(6k-5)Lambda_k-6Gamma_k] (mod p).

Thus this exact source observer needs only two prefix moments, with no separately evaluated boundary unit U_p. Index/order, p-adic valuation, signed (6k+1) Euler weights, original 216 F and Gauss G, and the point z=1/2 remain explicit; this is scoped algebraic/BRC reuse, not a full native X6 transfer.

## Actually executed exact integer checker

A standard-library Python program computes the **original** finite Gauss G and 216 F recurrences independently modulo p^3, evaluates the complete finite Clausen defect at z=1/2 using theta=z d/dz, and separately evaluates the prime-uniform two-prefix formula. All 611 primes 7<=p<=10000 with p mod6=1 passed both U1 and E_direct=E_closed; exact results and program are stored beside this report. Samples: p=7 U=5 E=4; p=19 U=2 E=7; p=373 U=112, Lambda_r=77, Gamma_r=347, E=177; p=1171 U=1054, E=0. These are author-side finite checks; all-domain U1/U2 come from the proofs.

## Exact continuation

Apply the parameter-free E_p carrier in the inherited second-order Hensel / original 216 identity; find a terminating Gauss/CM or WZ certificate, or a counterexample, coupling epsilon, derivative units and the proven far-upper two-prefix defect. The all-target-primes 12 j h = 1 (mod p) equality and the frozen mother statement remain open. Keep predecessor contributions and frozen source pin; avoid redoing H1-H4.

Control readback on 2026-11-03: gateway 0.6.11 UPSTREAM_CODE_REVIEW_REQUIRED, research_authority_granted=false, executor_binding_configured=false, active_jobs=5/5. Existing #6637 recovery read-only SUCCEEDED and #6638 continuation definitive FAILED were re-read, not replayed. Service session/claim/run not changed; two neutral archived staging records remain historical, not progress. Support #1558 controls native repair; #1559 is separate p373 H0/B0. This author-side GitHub publication grants no formal CLAIM, OPEN, checkpoint, Result, review or admission.


## U3 — Exact parameter-free Hensel / signed source-carry reduction

For a target-class prime p mod 24 in {13,19}, retain the *inherited CM0 hypothesis*, H3c second-Hensel theorem and all original Gauss/216 source labels. Let delta and epsilon in {0,...,p-1} be the first two Hensel digits of the Gauss root near z=1/2; let d=G'(1/2) mod p^2 be its canonical integer representative; and W=[(1+6theta)F](1/2) be the original full 216 signed scalar.

Set S_p=sum_{k=1}^r L_k 2^{-k}[(6k-5)Lambda_k-6Gamma_k] in F_p. The already proved H3c states

    W/p = -6 delta d^2 + p(4 delta^2 d^2 - 6 epsilon d^2 + E_p) (mod p^2).

By U2, E_p=-S_p/5. Define B=-6 delta d^2 (integer), K=4 delta^2 d^2-6 epsilon d^2-S_p/5 (mod p). This gives the exact equivalence, under H3c's hypotheses,

    W/p=1 (mod p^2)
       if and only if
    [B=1 (mod p) and ((B-1)/p)+K=0 (mod p)].

The integer quotient is formed only in the displayed B=1 (mod p) branch. This is an exact two-stage target reduction with a parameter-free, origin-preserving Clausen correction, **not** a proof of the all-prime target vanishing or the distinct frozen Delta-R mother.

At p=373, inherited H3 data delta=274, epsilon=321, d=78545 (mod 373^2), together with new S_373=234, yield B=1 (mod 373), (B-1)/373=348 (mod 373) and K=25 (mod 373), so 348+25=0 (mod 373). The exact condition reproduces W/373=1 (mod 373^2). The general finite CM/WZ cancellation remains the next proof target.
