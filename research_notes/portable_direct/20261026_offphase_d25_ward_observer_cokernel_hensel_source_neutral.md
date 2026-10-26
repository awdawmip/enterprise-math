# D25/LIFT: Ward observer cokernel, universal pole residue, p=733 Hensel lift

2026-10-26. **SOURCE-NEUTRAL PORTABLE AUTHOR MATHEMATICS**; AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / NATIVE_SYNC_DEBT. This is not native task progress, CLA﻿IM, Source checkpoint, original-class CM/DP Frobenius, Driver review, or LIFT/JT2 proof.

Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; **frozen science source c47e13e4aba0e006366f989d6334d443f6333ae3 unchanged**. The parent target remains Delta_p = R_p (mod p) for primes p =13,19 (mod24). The accepted first-digit UR/JT0 proof is not reopened.

## Precisely consumed existing work, without new credit

The existing main-backed note 20261026_hourly_d25_ward_seam_resonance_binomial_r11.md proved the authentic corrected-Clausen Hasse Ward source law, left-Dirichlet adjoint, the special geometric weight 2^n, the p733 scalar seam resonance, and its omega_0 =187337 modulo 733². The separate offphase negative-Ward second-jet and the six-channel signed J/E, positive infinity and ordered high-high calculations are previous evidence, not contributions claimed here. The present output changes the *observer*, determines its entire p-local cokernel and proves an original observer-sensitivity counterexample.

## Theorem 1: all integral scalar weight observers and a single seam obstruction

Let p=6m+1 be a prime >=7, M=2m-1=(p-4)/3, L=-M, N=M, and A=Z_(p). For independent labelled variables Y_L,...,Y_N with Y_(N+1)=0, keep the inherited Ward law exactly:

    S_n = (p-2n)Y_n - (p-2n-1)Y_(n+1),   L<=n<=N.

For *any* weights w_n in A, W_w(Y)=sum_{n=L}^N w_n Y_n. For 1<=t<=M define the p-integral rational coefficients

    a_t(p) = [1/(p+2t)] * product_{j=1}^{t-1} [(p+2j+1)/(p+2j)]
    X_p(w) = w_0+(p+1)*sum_{t=1}^M a_t(p) w_(-t).

The unique rational solution to W_w(Y)=sum omega_n S_n is p-integral for every n **if and only if**

    chi_p(w) = w_0+sum_{t=1}^M [binom(2t,t)/4^t]w_(-t) = 0 modulo p.    (1)

In fact, the transpose Ward operator has Smith invariants (1,...,1,p) over A and cokernel A/pA; chi_p is the unique obstruction normalized to coefficient 1 at w_0.

**Proof.** The Ward matrix is upper bidiagonal. Its diagonal p-2n consists of p-units except exactly one pivot n=0, whose value is p; 2M<p. The (dimension-1)-minor deleting row/column n=0 is a p-unit, while the determinant has valuation exactly one. Thus Smith factors are 1,...,1,p. From coefficient comparison, with omega_(L-1)=0,

    (p-2n)omega_n-(p-2n+1)omega_(n-1)=w_n.

Every n<0 pivot is a p-unit; unfolding gives omega_(-1)=sum_t a_t(p)w_(-t). The singular seam n=0 requires p omega_0=X_p(w). Every n>0 pivot is again a p-unit. Finally a_t(0)=binom(2t,t)/4^t, with only p-unit denominators because 2M<p. Hence X_p(w) mod p =chi_p(w); (1) is necessary and sufficient. This is a proof over the p-local rational ring, not finite-scan induction.

## Theorem 2: exact positive-rank pole profile and a lossless split

If chi_p(w) !=0, the negative adjoint coefficients remain p-integral, but **every** positive-side rational coefficient omega_n for 0<=n<=M has valuation -1. Its normalized residue is

    p omega_n = chi_p(w) * binom(2n,n)/4^n modulo p.                (2)

At n=0 the residue is chi_p(w). For n>=1 multiply the recurrence by p: the inhomogeneity p*w_n vanishes mod p, and the positive transition becomes (2n-1)/(2n), producing the central-binomial product. All factors are p-units.

An exact and integral repair retains the seam *separately*: solve negative coefficients eta_n from the unit pivots with eta_(L-1)=0, put eta_0=0 and solve all positive coefficients eta_n via unit pivots. Then for **every** Y,

    W_w(Y) = sum_{n=L}^N eta_n S_n + X_p(w)Y_0.                  (3)

Thus one extra labelled seam observer is necessary and sufficient for this precise source/observer interface; it is **not** an automatic compression of true J/E, the positive infinity source or ordered high-high data.

## Theorem 3: p=733 first-moment nonresonance, and unique local Hensel repair

For a unit z write geometric weights w_n=z^n, and X_p(z)=1+(p+1)sum_t a_t(p) z^(-t). The existing 733 calculation establishes chi_733(z=2)=0: a resonant **undifferentiated geometric scalar**. Differentiating the *observer* (not the source), the rank moment w_n=n*2^n has a **new nonzero obstruction**:

    chi_733(n*2^n) = -sum_{t=1}^243 t*binom(2t,t)/8^t
                   = 211 modulo 733.                                  (4)

Therefore this first rank-moment observer has *no* p-integral source-only full-range Ward adjoint. The pole profile (2) is 211*binom(2n,n)/4^n for every 0<=n<=243. This is an exact information-loss witness: retaining the geometric scalar resonance does not preserve the derivative/moment observer.

Since 2*X'_733(2)=211 modulo 733, X'_733(2)=472 mod733 is invertible. The usual integral Hensel lemma yields exactly one root z_* in **the residue class z=2 mod733**. The complete arithmetic certificate through p³ is:

    p=733; p²=537289; p³=393832837; M=243
    X_733(2) mod p² =309326=733*422
    X_733(2) mod p³ =137318021
    X'_733(2) mod p =472
    z_* mod p² =534359 = 2-4*733
    X_733(534359) mod p² =0
    X_733(2-4*733) mod p³ =102622199 =191*733²
    z_* mod p³ =155810880 = 2-4*733+290*733²
    X_733(155810880) mod p³ =0.

The mod-733 polynomial/rational observer actually has **two** unit roots, 2 and 649. The uniqueness is *local to the class 2*; we do not assert globally one p-adic root. p13 comparison: chi_13(2^n)=9 and chi_13(n*2^n)=3 (mod13).

## Reproducible check and exact scope

Use modular integer inverses to construct a_t(p) recursively:
a_1=(p+2)^(-1);
a_t=a_(t-1)*(p+2t-1)/(p+2t), t>=2.
Build X from arbitrary w and check reduction against the binomial coefficient formula; independently solve the labelled Ward negative recursion, construct split (3) and check it on finite arbitrary Y, then check pole profile (2). Hensel calculations use the exact rational derivative
X'_p(z)=-(p+1)sum_t t*a_t(p)*z^(-t-1).

Executed stdlib Python checker (full local source in current conversation artifact d25_ward_observer_cokernel_hensel_checker_20261026.py) passes, for **80** p≡1 mod6 primes 7<=p<=997, **12516** coefficient congruence checks, **960** labelled Ward identities, **48304** explicit pole residue checks. A separate p=7 exhaustive finite operator census checks **all 343** weight vectors; 49 of those 343 are in the image of the transpose Ward map. **48** independent exact rational assertions for p=7,13,19, and **5** Hensel checks at p733 also pass. The JSON is retained as a local author artifact. These checks are **author-only**; universal mathematics follows from the proof, not from an extrapolated scan.

BRC/method reuse: T0_BRC and provenance-preserving signed observer typing (COMPOSE_APPLIED), T1_SCALE_ENUMERATION_VALUATION p-valuation (REUSE_APPLIED), T6_OPERATION_SAFE_QUOTIENT observer-relative preservation (REUSE_APPLIED), plus prior exact Ward/Gauss source interfaces (COMPOSE_APPLIED). Signed Ward amplitudes are **not** positive BRC mass; summation rank n and scalar z are *external auxiliary coordinates*, not native X6 spatial axes. No new foundation family, native physics or P000 transfer is claimed.

## Native authority, full UR original, and smallest next unit

At this actual Sites subject: em_status 0.6.11 reports research_authority_granted=false; Site static_machine_readonly and write_relay_enabled=false. Fresh direct continuation/task requests returned CONTROL_QUOTA; checkpoint listing ACCESS_DENIED. No fresh own CLAIM/OPEN/Source checkpoint or Research-Activity registration is asserted. Existing control support enterprise-math Issue #1558 must reconcile real Source predecessor-claim CAS and legal same-conversation service-session continuation, preserving original archived staging and all contributor history, before the legitimate Research lane can perform its own typed prepare/claim/open and native checkpoint. A neutral GitHub source note does not bypass those gates.

Original four-file UR V2 bundle target SHA256 4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76 (historical size 94687 bytes) is **not recovered**. The two individually traced revised original bridge uploads (#1121/#1224) are distinct and were not source-published; no preexisting UR proof is redone.

**Smallest live scientific next question:** does the true original-class LIFT divided residual have any faithful, fixed Hasse-to-Ward weight observer w without destroying signed J/E, infinity, high-high or Frobenius direction? Prove exact factorization to Delta_p-R_p, or find a counterexample to the proposed factorization. Observer derivative must be preserved if future operations demand it. Original H0/B0, [X]U mod p², eta/kappa and independent review remain open.

For a continuation_seed.state of CURRENT_TASK_INPUTS_WITH_NO_RECORDED_OWNER_PROGRESS, input artifacts are only input; any frontier_notes.completed_units must remain [] until Source validates actual predecessor research. This author note is not such a predecessor checkpoint. Existing automation settings are unchanged.
