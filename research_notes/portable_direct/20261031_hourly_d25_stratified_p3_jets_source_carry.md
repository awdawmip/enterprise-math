# D25/LIFT — source-preserving third-order stratified 216 jet and low/middle carry

Date: 2026-10-31 Asia/Hong_Kong. TASK_RESEARCH lane chatgpt-research-hourly-enterprise-math-20260923; never maintenance. Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7. Frozen science pin c47e13e4aba0e006366f989d6334d443f6333ae3. P000 ACTIVE_LOCKED. AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING. External p-adic arithmetic only.

## Previously completed source consumed (no duplicated credit)

The distinct onhour author showed in commit a9f155affe563940ca8254bec644cdf8aea2f460 that the frozen first-digit 216/E.2 bridge, formerly listed as a separate open obligation by this hourly lane, is ALREADY discharged by the previously sourced UR/Clausen A_p=p (mod p²), the high coefficient valuation bounds, and the published alternating E.2 B_p=p (mod p³). Thus S/p+H+U=1 (mod p) below is a consequence within that frozen target scope, not a remaining unsolved lemma. The original second digit remains the genuine open condition.

## Exact coefficient theorem: three valuation strata

Let p=6l+1>5 prime; m=2l, h=3l, q=4l. In Z_(p), let

    a_n=(1/2)_n(1/3)_n(2/3)_n / (2^n(n!)^3)
       = binom(2n,n)^2 binom(3n,n)/216^n,
    w_n=6n+1, A_p=sum_(n=0)^(p-1) w_n a_n.

For 0<=n<=N<p write d_N(n)=sum_(j=N-n+1)^N 1/j,
e_N(n)=sum_(j=N-n+1)^N 1/j², H_s=sum_(j=1)^s 1/j.
All displayed rational denominators are p-units.

LOW (0<=n<=m):

    t_n=(-1)^n 2^(-n) binom(h,n)binom(m,n)binom(q,n),
    k_n=d_h(n)/2+d_m(n)/3+2d_q(n)/3,
    e_n=e_h(n)/4+e_m(n)/9+4e_q(n)/9,

    a_n=t_n[1-p k_n +p²(k_n²-e_n)/2] (mod p³).     (L)

MIDDLE (m<n<=h), s=n-m-1:

    u_n=m!s!binom(h,n)binom(q,n)/(3n!2^n),
    f_n=d_h(n)/2+2d_q(n)/3+(H_m-H_s)/3,

    a_n=p u_n(1-p f_n) (mod p³).                   (M)

HIGH (h<n<=q), s=n-m-1, r=n-h-1:

    v_n=(-1)^(h+m+n) h!m!s!r!binom(q,n)/(6(n!)²2^n),
    a_n=p² v_n (mod p³).                          (H)

For q<n<p, a_n=0 mod p³. Equations (L),(M),(H) hold coefficientwise for EVERY prime p=6l+1>5, regardless of CM or the target conjecture.

**Proof.** Use the exact parameter identities 1/2=-h+p/2, 1/3=-m+p/3 and 2/3=-q+2p/3. Before a parameter crosses zero, its Pochhammer product is the corresponding signed integer factorial times unit factors 1-p*alpha/j. The low product has logarithm -p k_n-p² e_n/2 mod p³, so exponentiation proves (L). In the middle band, (-m+p/3)_n has a unique factor p/3. Factoring it leaves m negative factors and s positive factors, giving 1-p(H_m-H_s)/3, while the other two factors remain uncrossed. The sign is positive because m=2l is even, giving (M). In the high band, both (-h+p/2)_n and (-m+p/3)_n cross, giving (p/2)(p/3) and the exact displayed factorial/sign unit; (-q+2p/3)_n has not crossed. For n>q all three have crossed, so the valuation is >=3. This is an exact finite factorial proof.

## New source-labelled second-digit bridge

Define

    S=sum_low w_n t_n,
    H=-sum_low w_n t_n k_n,
    L=sum_low w_n t_n(k_n²-e_n)/2,
    U=sum_middle w_n u_n,
    J=sum_middle w_n u_n f_n,
    I=sum_high w_n v_n.

The coefficient theorem yields the all-prime full-source identity

    A_p = S+p(H+U)+p²(L-J+I) (mod p³).             (T)

For the frozen classes p mod24 in {13,19}, the previously established first digit makes the following division integral:

    C=[S-p+p(H+U)]/p² (mod p).

Consequently

    (A_p-p)/p² = C+L-J+I (mod p).                  (T2)

Let B_p be the DISTINCT alternating E.2 source. Source indexing gives the exact partition A_p-B_p=D0+D1+S2+S3, with S2/p²=I mod p and S3=0 mod p³. Consume the externally proved E.2 congruence B_p=p mod p³. Then

    (D0+D1)/p² = C+L-J (mod p).                    (B2)

Thus the original 216/E.2 low/middle SECOND-DIGIT quotient now has a direct finite 216-only three-port binomial/harmonic representation; the high signed port is the previously known I, not re-proved here. The unsolved exact all-target cancellation is C+L-J+I=0 mod p. Equation (T2) is an equivalence, not a proof of that last zero.

The earlier same-lane terminating Clausen denominator CM two-jet (commit f7f61aa61a5a5ee63061542ff3a5028bf1776c1c) evaluates S/p mod p². Inserting it into C=[S/p-1+H+U]/p mod p is therefore a precise CM-to-middle-to-signed-high interface. H and U MUST be evaluated modulo p²; substituting only their first residues loses the carry.

## Reproducible author-side exact arithmetic

Executed the accompanying Python standard-library program through p<5000. All 330 primes p=1 mod6 pass 772,620 individual coefficient comparisons, the exact (T) reconstruction mod p³, and independently computed alternating E.2. All 166 frozen-class primes pass the legal first-digit division, (T2) and (B2). Separately cross-checked the integer-binomial original coefficients at every n for p=13,19,37,43,67,157,373. No floating point, Lean, native H0/B0 or semilinear Frobenius execution.

At p=373 (l=62, m=124, h=186, q=248), the distinct mod-373 ports are

    (C,L,-J,I)=(240,82,158,266).

The low/middle value is 240+82+158=480=107 mod373, matching the independently computed (D0+D1)/p²=107. The high signed I=266 and 107+266=373=0 mod373. Other witnesses: p13 (3,5,8,10), p19 (11,1,17,9), p37 (5,19,30,20), p43 (7,0,1,35), p67 (19,42,15,58), p157 (33,24,2,98); every indicated four-port sum is 0 modulo its prime. The universal jet theorem follows algebraically; finite zero observations do not prove LIFT.

## Provenance, BRC, authorization and continuation

Typed BRC carrier: (p,l,n,original-216/E.2 source, low/middle/high, p-valuation, exact sign, p-unit factorial, first/second harmonic defect, CM carry, fixed observer, modulus). The p-adic statements are EXTERNAL mathematical lemmas, not promoted to native P000 X6 physics.

Read-only Gateway 0.6.11 status observed 2026-10-31T00:14Z: research_authority_granted=false, executor_binding_configured=false, active_jobs=5/5, source control CODE_REVIEW_REQUIRED / UPSTREAM_CODE_REVIEW_REQUIRED. Historical exact same-conversation recovery https://github.com/awdawmip/kimi-query-bridge/issues/6424 and continuation https://github.com/awdawmip/kimi-query-bridge/issues/6425: execution_authorized=false, no winning claim/run. No new native CLAIM/OPEN/checkpoint/freeze/review is asserted. Research activity REGISTER_PENDING; protected staging and other conversation identities unchanged. Existing actual controller support issue enterprise-math #1558, native fixed p373 scientific experiment #1559.

Next exact mathematical unit: substitute the known CM two-jet into C, then construct a genuine finite WZ/contiguous/CM cancellation for the COMPLETE C+L-J+I in both target classes, retaining H,U mod p² and the original signed I port. Do not re-open the consumed first-digit proof. Native H0/B0 [X]U mod p², rank, Frobenius/eta, odd Green-Hesse and kappa remain independent experimental obligations with an authorized owner.
