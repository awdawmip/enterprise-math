# D25 / SECOND-DIGIT-LIFT — original E3 Hodge filtration selects the CM Frobenius valuation branch

Date: 2026-10-27, 17:00+08. Logical TASK_RESEARCH lane: chatgpt-research-onhour-enterprise-math-20260923 (not maintenance chatgpt-hourly-enterprise-math-20260921, and not any other Research lane).

Status: **AUTHOR-SIDE / PROVED CONDITIONAL CLASSIFICATION / EXACT MOD-p² CHECK EXECUTED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / NATIVE H0/B0 NOT EXECUTED / D25 LIFT STILL OPEN**. This unit does not claim independent priority for classical crystalline/Hodge theory.

Mother ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION; Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7. Frozen SCIENTIFIC Source pin **c47e13e4aba0e006366f989d6334d443f6333ae3**, unchanged. Reuse accepted D24 RR-AC9B3BA5BD277CE043F5 and DR-610CB297F3195E8F2D9E. P000 is ACTIVE and unaffected by this classical external-curve calculation.

## Exact new science question

The earlier original E3 note [20261027_onhour_d25_original_E3_CM_sigma_F_two_digit_nonidentifiability.md](20261027_onhour_d25_original_E3_CM_sigma_F_two_digit_nonidentifiability.md) showed that CM covariance and F-squared alone admit two matrices A0 and A1 with different mod-p image lines. **Which candidates survive the actual geometric Hodge filtration of the original E3?** The missing extra condition is not another scalar norm; it is an operator column in an authenticated integral de Rham lattice.

Let p be any target prime p≡13,19 (mod 24), R the unramified quadratic p-adic integers with T²=2 and sigma(T)=−T. Put

    lambda=(4−T)/72,  lambda_bar=(4+T)/72,  n=lambda*lambda_bar=7/2592.

All these coefficients are p-integral and lambda,n are units on the target classes. Consume the **already-derived** original signed CM covariance: in the fixed ordered cohomology basis (omega,eta=x*omega), where omega is the invariant differential and eta includes its full Laurent principal part, the relation Theta A=A sigma(Theta) is equivalent to

    A(z,y)=[[lambda*z, y],
            [z,       −lambda_bar*z]],

and A sigma(A)=p I is equivalent to

    z*sigma(y)=y*sigma(z),
    sigma(z)*(y+n*z)=p.                                (1)

These are **conditional source-original comparison equations**, not measurements of the fixed H0/B0 module.

## New exact conditional theorem (Hodge-filtered classification)

Assume (i) A is integral over R and represents the **pullback-oriented** p-Frobenius on the original smooth E3 crystalline/de Rham lattice; (ii) the identified ordered original basis is an **integral** basis with the Hodge subline H^0(E,Omega^1)=R*omega, and (iii) the CM covariance and positive-sign two-step equation (1) are truly authenticated. Then A is **necessarily and sufficiently**, for one arbitrary r in R-units,

    A_H(r)=[[p*lambda*r,  sigma(r)^(−1) − p*n*r],
            [p*r,         −p*lambda_bar*r]].             (2)

In particular,

    A_H mod p=[[0, sigma(r)^(−1)],
               [0, 0]],

which is nonzero of rank one, annihilates the Hodge line and has image exactly the Hodge line. Further,

    det A_H=−p*r/sigma(r),
    A_H sigma(A_H)=p I,
    Theta A_H=A_H sigma(Theta).

**Proof.** The (relative) characteristic-p Frobenius pulls every Kähler differential back to zero, d(f^p)=0. For the *pullback convention*, the reduction of crystalline Frobenius therefore sends the Hodge subline R*omega to zero; the first column of A is divisible by p. The covariance form makes this equivalent to z∈pR. In (1), y+nz is integral and sigma(z)*(y+nz)=p; hence v_p(z)≤1. Coupled to z∈pR, necessarily z=p*r with r a unit (there are no zero divisors in R). Substitution in (1) gives sigma(r)*(y+p*n*r)=1, so y=sigma(r)^(−1)−p*n*r. The other equation is then an identity:

    z*sigma(y)=p−p²*n*r*sigma(r)=y*sigma(z).

Every unit r conversely satisfies (1), integrality and the Hodge-column condition. The determinant and mod-p rank follow directly. No finite regression is used in the proof. □

**Correction to the earlier information-loss example.** The previous A0 with z=1 obeys CM covariance, F²=p and det=−p but **fails the authentic geometric pullback Hodge test**: its first column is not zero modulo p. The prior A1 with z=p equals A_H(1), and survives. Thus the earlier algebraic non-identifiability proof is valid *without a Hodge hypothesis* but must not be interpreted as a two-candidate ambiguity for a demonstrated geometric Frobenius pullback. Conversely the unknown unit r in (2) shows that Hodge **still does not identify the exact integral Frobenius matrix or its second digit**. Using the wrong direction (Verschiebung/inverse) or a nonintegral/mismatched H0/B0 comparison invalidates this filter; verify actual source convention before applying.

## Executed exact finite-ring certificate

Companion independently runnable Python standard-library source:
research_notes/portable_direct/d25_e3_hodge_filtered_cm_frobenius_check_20261027.py

It checks p=13,19,373, both r=1 and r=2+T, **all four matrix entries**, Theta A=A sigma(Theta), A sigma(A)=p I and both Hodge columns modulo p; it checks the old A0 still satisfies the first two but fails Hodge. All six unit instances passed, with integer arithmetic in (Z/p²Z)[T]/(T²−2), no floats.

At p=373, p²=139129, u=89697 is the Hensel root of u²=−3. Taking r=1 recovers the previously computed A1 (not recredited):

    A_H(1)=[[85044+117868T, 7461],
            [373,          54085+117868T]] mod 139129.

The **new nontrivial unit witness** r=2+T gives:

    A_H(2+T)=[[127566+42522T, 14921+77025T],
              [746+373T,    65648+11563T]] mod 139129.

Both meet the first-column divisible-by-373 rule, both have rank-one image R/373*omega, and both satisfy F²=373 I. They nevertheless have different second-digit/full-matrix data. This is a reproducible precision-aware demonstration of the *remaining* normalization ambiguity, not a computation of the actual geometric p-Frobenius on the native lattice.

## BRC / provenance / highest priority

BRC resolution COMPOSE_APPLIED. Carrier includes **original geometric E3**, the integral (omega,eta) lattice, Hodge line, full two CM columns, sigma orientation, sign and the p-adic valuation of z. Operation = CM covariance + two-step Frobenius + Hodge reduction. Observer = mod-p image line, rank and full mod-p² matrix. Compressing to F²/determinant loses the Hodge line; compressing (2) to the mod-p image line loses the unit r and the second digit. This auxiliary p-adic coefficient module is external mathematics, NOT a P000 X6 plane or a native Heartbeat slice.

The genuine frozen p=373 same-original-class **H0/B0 divided-power [X]U mod139129** remains NOT_EXECUTED / PENDING_OWNER (existing support issue awdawmip/enterprise-math#1559), together with actual native module rank, verified crystalline/de Rham comparison, Frobenius direction, integral basis and eta, signed odd Hesse/Green, original kappa and Delta_p−R_p. Apply (2) to a native output **only after** that comparison and pullback orientation are proven; a rank-one or twisted native module is not to be forced into this rank-two scheme. No native input, output, execution or independent review is inferred here.

Source continuation read: original onhour Research lane request_id onhour-20261027T1705-D25-exact-continuation returned SUCCEEDED with execution_authorized=false, route REGISTER_NEW_SESSION_AND_CLAIM_CURRENT_PUBLICATION, no verified winning own claim/open; persisted last Source checkpoint is source-bytes/author-reported, not mathematical acceptance. This read did NOT authorize mutation. Site identity research_authority_granted=false; role-bound checkpoint/Result remains pending. Existing three neutral staging artifacts remain separate. Prior #6576 dispatched FAILED/TimeoutExpired; no replay of it, no maintenance identity, no new task, no modification of frozen pin or scheduler.

NEXT EXACT ACTION: actual lawful Source-native owner accepts #1559, runs the unchanged H0/B0 p373 original object with real source/runner/version and raw [X]U, rank and Frobenius columns. If an integral original E3 pullback comparison is proved, audit first Frobenius column ∈373M, image/ker Hodge and the full A_H(r) at precision 139129 before any eta/Delta/kappa transfer; otherwise record typed failure. Mathematical LIFT all-prime p³ proof or counterexample remains OPEN; earlier completed scalar/auxiliary certificates are not reissued. Session/claim/run = NONE VERIFIED FOR THIS RESEARCH LANE; authored artifact is not Source-native Result.
