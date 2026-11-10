# D25 / W216 — 两位素数进位的完整首阶证书与有符号行压缩

Date: 2026-11-10 (Asia/Hong_Kong).
Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`.
Frozen science `c47e13e4aba0e006366f989d6334d443f6333ae3`; historical Source checkpoint `b58330b74576153cdadde5d80a3d92df3a819a0e`.
Logical research lane `chatgpt-research-onhour-enterprise-math-20260923`, **not** maintenance conversation `chatgpt-hourly-enterprise-math-20260921`.
**Classification: AUTHOR_SIDE / ALGEBRAIC_PROOF / EXACT_TESTS / UNREVIEWED / NOT_ADMITTED / NATIVE_H0_B0_NOT_RUN.**

## Objective and research interface

The frozen mother objective is the *original signed* `Delta_p-R_p=0 (mod p)` for every prime `p≡13,19 (mod24)`; the previously proved source-port alignment gives `Delta_p-R_p=(W_p-p)/p² (mod p)`. Earlier author work proved the terminal prime-power carry and observed a finite-only Dwork candidate `W_(p²)-chi_p*p*W_p=c_p*p^6 (mod p^7)`. This unit **actually expands** the two-digit coefficient blocks `k=ap+b`, retaining factorial carries and original signed weights.

BRC `COMPOSE_APPLIED`: carrier consists of each ordered pair `(a,b)`, the original index `k`, factorial valuation, p-free unit, carries `c2,c3`, weighted original summand and row provenance. The future operations covered by the exact compression are weighted row summation and projection mod `p²`, not the open `p^7` Frobenius defect. The digit pair is an external number-theoretic chart, not a native X6 Cell or a P000 change.

## Theorem A — full two-digit factorial first jet

For each prime `p>3` and all `0<=a,b<p`, let
`
a_k=(2k)!(3k)!/((k!)^5 *216^k),  k=ap+b,
2b=c2*p+beta2,   3b=c3*p+beta3,   0<=beta2,beta3<p,
alpha2=2a+c2, alpha3=3a+c3,
D=(p-1)!, H_j=sum_(t=1)^j 1/t (mod p²) for j<p.
`
For any integer factorial, `V_p(n!)=n!/p^{v_p(n!)}` is its p-free factorial unit. Define `nu=v_p(a_(ap+b))` and `U_(a,b)=a_(ap+b)/p^nu`. Then, **for every pair including carry boundaries,**
`
nu=c2+c3+v_p(alpha2!)+v_p(alpha3!).

U_(a,b) ≡ 216^(-(ap+b)) * D^(c2+c3)
          * V_p(alpha2!) V_p(alpha3!) beta2! beta3! / ((a! b!)^5)
          * [1+p*(alpha2 H_beta2+alpha3 H_beta3-5a H_b)] (mod p²).
`
All displayed denominators are p-units, and p-divisible parts are stripped before modular reduction.

**Proof.** Decompose the factorial `n!=(Ap+B)!`, with `0<=B<p`, into multiples of p, full nonmultiples blocks, and a final partial block. Then exactly
`
V_p((Ap+B)!) = V_p(A!) * PROD_(j=0)^(A-1) PROD_(t=1)^(p-1)(jp+t)
                     * PROD_(t=1)^B(Ap+t).
`
For p>3, `H_(p-1)=0 (mod p)` by pairing t with p-t. Each full block is `D (mod p²)`; the partial block is `B![1+p A H_B] (mod p²)`. Hence
`V_p((Ap+B)!) ≡ V_p(A!)D^A B![1+p A H_B] (mod p²)`.
Apply this to `2k,3k,k` (five denominator copies). Their D exponent is `alpha2+alpha3-5a=c2+c3`, their partial-block first jet is the stated bracket, and Legendre factorial valuation yields the exact integer `nu`. QED.

## Theorem B — signed row compression (all p=6m+1>3)

Write `q=q_p(216)=(216^(p-1)-1)/p (mod p)` and
`J_b=2H_(2b)+3H_(3b)-5H_b (mod p)`, for `0<=b<=2m` (all indices <p). Specializing Theorem A gives:

`
a_(ap+b) ≡ a_a*a_b*[1+p*a*(J_b-q)] (mod p²), 0<=a,b<=2m;             (B0)

a_(ap+b) ≡ p*(3a+1)*a_a*(a_b/p) (mod p²),
                              0<=a<=2m, 2m+1<=b<=3m;                (B1)

a_(ap+b)/p ≡ (a_a/p)*a_b (mod p),
                              2m+1<=a<=3m, 0<=b<=2m.               (B2)
`
Indeed `216^(-a(p-1))=1-pa q (mod p²)`, proving the Fermat-quotient term in B0. In B1, the sole factorial carry `3b>=p` shifts `3a` to `3a+1`, hence factor `3a+1`; at a=2m this factor is p and the entire term correctly vanishes mod p². In B2, a has exactly one original p-valuation. All b>3m in low rows and all a>=3m+1 in every row have valuation >=2; the remaining high-row grade-one contributions are exactly B2. These statements are immediate from Theorem A's exact valuation formula.

Keep the *original signed weight*. Define
`
Z_a = sum_(b=0)^(p-1) (6(ap+b)+1)*a_(ap+b),
L0 = sum_(b=0)^(2m) (6b+1)*a_b (mod p²),
L1 = sum_(b=0)^(2m) [6+(6b+1)(J_b-q)]*a_b (mod p),
L2 = sum_(b=2m+1)^(3m) (6b+1)*(a_b/p) (mod p),
F0 = sum_(a=0)^(2m) a_a (mod p²),
F1 = sum_(a=0)^(2m) a*a_a (mod p).
`
B0 and B1, with `6ap` in the weight retained, give the **all-low-row identity**
`
Z_a ≡ a_a*[L0+p*a*L1+p*(3a+1)*L2] (mod p²), 0<=a<=2m.            (R0)
`
B2 gives `Z_a≡(a_a/p)*p*L0 (mod p²)` for `2m+1<=a<=3m`. The previously *accepted first-digit* input `W_p=p (mod p²)` implies `L0=W_p (mod p)=0`; thus every row `a>=2m+1` vanishes mod p² (grade-one upper rows cancel after summation, not necessarily coefficientwise). Summing R0 yields the **full, exact p² weighted block factor**
`
  W_(p²) ≡ F0*L0 + p*F1*L1 + p*(F0+3F1)*L2 (mod p²).               (F)
`
The right-hand side requires O(p) modular ring operations after O(p) first-digit coefficient generation, versus O(p²) direct two-digit summation. Auxiliary aggregates use O(1) registers of O(log p) bits; actual bit complexity depends on modular multiplication. Signed original indices, branch carries, and the cutoff source are retained by the proof. QED.

**Conditional CM corollary:** Whenever `F0≡F1≡0 (mod p)` in addition to the frozen first-digit input, formula F proves `W_(p²)≡0 (mod p²)`. This double-zero condition was exactly verified for target p=13,19,37,43,61,67,109,373, but **the all-prime proof in both target residue classes is still open**. This finite observation is not a newly admitted CM result.

## Reproduction

Companion `d25_w216_two_digit_firstjet_row_compression_20261110.py` separately constructs:
(1) the original coefficient recurrence `a_(k+1)/a_k=(3k+1)(3k+2)(2k+1)/(36(k+1)^3)` as a valuation/unit pair, and
(2) the independent exact factorial-block prediction of Theorem A.

All pairs passed for p=5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,73,109,373; **139129 pairs at p373**. Original signed row identity and F passed at p=7,13,19,31,37,43,61,67,73,109,373. Selected exact output:

| p | L0 mod p² | L1 mod p | L2 mod p | F0 mod p | F1 mod p | W_(p²) mod p² |
|--:|--:|--:|--:|--:|--:|--:|
|13|104|1|6|0|0|0|
|19|247|4|7|0|0|0|
|373|129431|298|27|0|0|0|

Higher-digit control (finite-only) re-evaluated via the raw recurrence mod p^7:

|p|W_p mod p^7|W_(p²) mod p^7|(W_(p²)-pW_p)/p^6 mod p|c_p|
|--:|--:|--:|--:|--:|
|13|33321912|37386518|9|9|
|19|510680005|434881538|12|12|

The proved law F is mod p²; it supplies a genuine first block for studying the still-open mod p^7 Dwork defect and does not by itself prove p^6 divisibility.

## Frontiers and authorized continuation

Smallest unfinished scientific unit: derive the `F0=F1=0 (mod p)` double-root certificate for both p≡13,19 mod24 from an exact finite CM/Clausen polynomial relation, preserving the signed cutoff; or return a minimal counterexample. Then calculate the next block digit toward `W_(p²)-pW_p`. In parallel the original scalar all-prime `W_p≡p (mod p³)` and `Delta-R` remain open.

Highest **separate** native evidence debt: issue #1559 remains OPEN/PENDING_OWNER; run original fixed H0/B0 divided-power `[X]U mod139129` at p373, native module rank, semilinear direction/eta, signed odd Green/Hesse, kappa, original Delta-R and independent reproduction. Native benchmark is **NOT_RUN**.

This turn read former Source request `onhour11-20261110-1157-source-cont` as SUCCEEDED, and new read-only continuation request `onhour11-20261110-1304-existing-continuation` as SUCCEEDED after receipt readback (control source `5057c6ba5d1ba61379719bf84a70c20f38931c4e`). Own recovery_status returned `SITE_CONTROL_OWN_ISSUED_SESSION_REQUIRED`; no own winning CLAIM/run, formal Source checkpoint, Result, review, role-bound reassignment, or maintenance-lane mutation occurred. GitHub file is author-side evidence only.
