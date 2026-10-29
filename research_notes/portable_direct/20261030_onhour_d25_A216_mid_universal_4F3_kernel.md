# D25 / SECOND-DIGIT-LIFT — universal 4F3 kernel for the ORIGINAL A216 valuation-two port

Date: 2026-10-30 (Asia/Hong_Kong).
Classification: AUTHOR-SIDE / EXACT DERIVED LEMMA / EXECUTED FINITE REGRESSION / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SOURCE_CHECKPOINT_PENDING.
Logical research lane: chatgpt-research-onhour-enterprise-math-20260923 (not maintenance).
Parent: ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION.
Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT.
Publication: TP2-B6F4FC938FF94941C1B7.
Frozen scientific Source pin: c47e13e4aba0e006366f989d6334d443f6333ae3 (unchanged).

## 1. New algebraic lemma: an m-independent term kernel

Let p=6m+1 >=7 be PRIME, and define the original A216 coefficients and signed weights

a_n = binom(2n,n)^2 binom(3n,n) / 216^n,    w_n=(6n+1)a_n.

The original valuation-two contribution is
A_mid = sum_{n=3m+1}^{4m} w_n in Z_(p).
Thus Q_p=A_mid/p^2 (mod p) is well-defined.

The previously author-proved *termwise* reflected formula, without dropping the original weight, is

Q_p = sum_{r=2m}^{3m-1} (6r+5) 216^r (r!)^5
          / ((2r+1)! (3r+2-p)!)             (mod p).

Set

C_m = 3 * 216^(2m) * ((2m)!)^5 / (4m+1)!  in F_p,

h_s = (2s+1)*2^s * ( (2/3)_s )^3
             / ( (7/6)_s (4/3)_s s! ),     0<=s<=m-1,

H_m = sum_{s=0}^{m-1} h_s  in F_p,
where (x)_s is the ascending factorial and all denominators are interpreted in F_p.

**PROVED (conditional on the already documented A216 reflected-term lemma):**

    Q_p = C_m * H_m  (mod p).               (UK-1)

Equivalently H_m is a truncated, universal very explicitly defined hypergeometric kernel

    H_m = sum_{s=0}^{m-1}
          [(3/2)_s (2/3)_s^3 / ((1/2)_s (7/6)_s (4/3)_s)] * 2^s/s!,
i.e. the first m terms of _4F_3(3/2,2/3,2/3,2/3;1/2,7/6,4/3;2).
The ratio of successive *kernel* terms is independent of the prime and of m:

    h_(s+1)/h_s =
    4(2s+3)(3s+2)^3 / [3(2s+1)(6s+7)(3s+4)(s+1)].

This rational formula is valid for 0<=s<m-1; no denominator factor vanishes mod p in this range.
At the *next* formal extension, s=m-1, the denominator factor
6s+7=6m+1=p vanishes: the truncation has an exact p-resonance boundary.
Do NOT extend the recurrence through this pole or silently cancel a valuation source.

## 2. Proof

Write r=2m+s. The original reflected summand is

g_s=(12m+6s+5)216^(2m+s) ((2m+s)!)^5 /
        ((4m+2s+1)! (3s+1)!).

The s=0 term is congruent to C_m, because 12m+5=2p+3.
Every factorial index in these expressions is below p (for 0<=s<m),
so the denominator is a p-unit. For 0<=s<m-1, its exact ratio is

g_(s+1)/g_s =
  [(12m+6s+11)/(12m+6s+5)] *
  [216(2m+s+1)^5 /
   ((4m+2s+2)(4m+2s+3)(3s+2)(3s+3)(3s+4))].

Reduce 6m+1=p:
  2m+1 = 2/3;
  4m+2 = 4/3 = 2*(2/3);
  4m+3 = 7/3 = 2*(7/6);
  3s+2=3*(s+2/3), 3s+3=3*(s+1), 3s+4=3*(s+4/3);
  (12m+6s+11)/(12m+6s+5)=(2s+3)/(2s+1).
Using 216/(2*2*3*3*3)=2, the reduced ratio is exactly

  2*(2s+3)/(2s+1) * (s+2/3)^3 /
            ((s+7/6)(s+4/3)(s+1)),

which equals h_(s+1)/h_s. The initial value and the ratios give
g_s=C_m h_s in F_p for all s=0,...,m-1; summing proves UK-1.
This is a finite-field exact proof, not an inference from the regression.

## 3. Exact LIFT input and next proof obligation

Use the preceding D25 two-original-port equivalence, including the accepted D24 first digit and the Guo–Zudilin (2019) B2304 dual-cutoff theorem:
  LIFT iff (A_low-p)/p^2 + Q_p = 0 (mod p),
  A_low=sum_{n=0}^{3m}(6n+1)a_n.
Substituting UK-1 gives the SAME original scientific target in a different, WZ-ready form:

  **LIFT iff (A_low-p)/p^2 + C_m H_m = 0 (mod p)**,      (UK-2)

for p congruent to 13 or 19 (mod 24). The first quotient is integral
by the accepted first-digit result. UK-2 has NOT been proved to vanish
for every prime. The mathematical gain is an m-independent, single-ratio
hypergeometric kernel for the entire middle port, with a visible
p-resonance boundary; it is not another claim of native H0/B0 completion.

BRC/source observer: retain (original n, A coefficient, signed 6n+1,
valuation-two membership, reflection r, translated index s, denominator
p-units, modulo-p observer after exact division by p^2). The equality
permits compressing this *port's scalar readout*, not its provenance or
the native H0/B0 operator.

## 4. Executed exact independent regression

Python 3 standard-library code computed 115 primes p<1500 with p=1 mod 6,
including all 60 primes in p=13,19 mod 24; compared:
(a) ORIGINAL weighted terms modulo p^3 by the exact coefficient ratio,
(b) previous factorial reflection term-by-term sum modulo p,
(c) the new universal h_s recurrence and C_m modulo p.
Five primes (7,13,19,31,373) additionally recomputed original
binomial coefficients independently, without the coefficient recurrence.
Output from the actual execution:

    CERT 7 Q 5 C 5 H 1 raw 5
    CERT 13 Q 10 C 9 H 4 raw 10
    CERT 19 Q 9 C 13 H 8 raw 9
    CERT 31 Q 23 C 13 H 28 raw 23
    CERT 373 Q 266 C 203 H 310 raw 266
    PASS_ALL_A216_UNIVERSAL_MID_KERNEL 115 TARGET_13_19_MOD24 60

The executable used for this author check is the accompanying
conversation artifact d25_a216_mid_universal_kernel_guard_20261030.py;
the exact operations are given by the formulas above. The 115-prime
regression confirms implementation but is not a universal proof.
At p=373, prior A_low source gives (A_low-p)/p^2=107 (mod 373), and
C_m H_m=203*310=266 (mod 373); the required sum is 373=0 modulo 373.

## 5. Non-closure / continuation

Native original-class fixed-p373 H0/B0 divided-power [X]U modulo 139129,
module rank, semilinear Frobenius, eta, signed Green/Hesse and kappa
remain NOT_EXECUTED in this lane. Issue #1559 is OPEN with no assignee
at read time (2026-10-30). This portable hypergeometric note cannot
substitute for that original-class experiment. The current Site gateway
reports research_authority_granted=false and write_relay_enabled=false,
and the separate em_status read returned BACKEND_IDENTITY_CHECK_UNAVAILABLE
with operation_sent=false. No recovery_status/Source-backed continuation
or own CLAIM was obtained this turn. Do not infer NO_DISPATCH.

NEXT EXACT MATHEMATICAL ACTION: try a bounded finite WZ/contiguous
relation for the universal _4F_3 partial sum H_m at its resonant
terminus, comparing to the original lower-window divided residue;
prove or falsify the resulting UK-2 equality uniformly. The external
native benchmark has its distinct authorized executor requirement.
Do not redo Guo–Zudilin dual cutoff, D24 first-digit, or the
previous A216 reflected-term proof.

Result classification: AUTHOR_SIDE_PROVED_DERIVATION_ONLY,
NOT_ADMITTED, independent review pending. No user schedule,
notification, Source pin, role or session was modified.
