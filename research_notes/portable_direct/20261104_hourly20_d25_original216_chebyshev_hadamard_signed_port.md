# D25 — original-216 high valuation-two Chebyshev–Hadamard signed observer

2026-11-04 (+08). **AUTHOR-DERIVED / EXACT SCOPED ALGEBRA / FINITE-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING.** Author-side mathematical evidence, **not** native Source checkpoint or Result.

Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`; frozen scientific pin `c47e13e4aba0e006366f989d6334d443f6333ae3`. Research logical lane `chatgpt-research-hourly-enterprise-math-20260923`, not maintenance `chatgpt-hourly-enterprise-math-20260921`.

## Theorem 1: terminating Chebyshev times prime-independent Hadamard mask

For any prime p=6r+1>=7, keep the original coefficient a_k=(2k)!(3k)!/[(k!)^5 216^k]. The original high interval is k_s=3r+1+s=(p+1)/2+s, 0<=s<r. Write H_p=sum_s (6k_s+1)a_(k_s). Each term has v_p(a_(k_s))=2. Its exact initial normalized coefficient has this p-local reduction:

    alpha_p=a_(3r+1)/p^2
           =(3r+2)/[((3r+1)!)^4 * 216^(3r+1)]  (mod p),  alpha_p !=0.

Define the rational degree-(r−1) Chebyshev polynomial and *prime-independent* formal series

    Q_r(z)=U_(r-1)(1−2z)/r
          =sum_(s=0)^(r−1) [(-4)^s/r * binom(r+s,2s+1)] z^s,

    B(z) = _3F_2(1,1,1;3/2,3/2;z)
         =sum_(s>=0) beta_s z^s, beta_s=(s!)^2/(3/2)_s^2.

Let ⊙ denote coefficientwise/Hadamard product and theta=z*d/dz. Since all relevant denominators are p-units, the following is a rigorous identity *modulo p* in Z_(p):

    [H_p/p^2] = alpha_p [(4+6theta)(Q_r ⊙ B)]_(z=1/2)       (CH).

Equivalent finite binomial form:

    [H_p/p^2] =
    (alpha_p/r) sum_(s=0)^(r−1) (4+6s)(−32)^s
       * binom(r+s,2s+1) * (s!)^4/((2s+1)!)^2            (BIN).

Proof: original factorial recurrence gives

    a_(k+1)/a_k = (2k+1)(3k+1)(3k+2)/(36(k+1)^3).

For k=k_s, normalization Y_s=a_(k_s)/p^2 yields

    Y_(s+1)/Y_s =
       [(s+1)(s+5/6)(s+7/6)]/[2(s+3/2)^3]               (mod p).

Since p=6r+1, 5/6=r+1 and 7/6=1−r modulo p. Thus

    Y_s=alpha_p*2^(−s)*(1)_s*(1−r)_s*(1+r)_s/(3/2)_s^3.

The Gauss polynomial _2F_1(1−r,1+r;3/2;z)=Q_r(z) exactly over Q
(by their normalized Chebyshev/hypergeometric differential equation);
multiplying its coefficient by beta_s gives the displayed Y_s kernel.
Also 6k_s+1=3p+4+6s, proving CH. Using
(3/2)_s=(2s+1)!/(4^s s!) and the explicit Q_r coefficient proves BIN.
Finally, (p+1)!/p=−1 (mod p) and (p+3r+2)!/p=−(3r+2)!
(mod p) by Wilson, proving alpha_p. Denominators are p-units
because 0<=s<r and 2s+1<p. QED.

This is a source-preserving *signed observer factorization*, not a
claim that the original coefficients, internal valuation ports or
other observer operations can be discarded.

## Theorem 2: all-target integrality of the signed comparator residue

For target primes p mod24 in {13,19}, put h=3r=(p−1)/2, and retain
the separate quartic coefficients c_k=(4k)!/[(k!)^4 2304^k]. Define

    L_p=sum_(k=0)^h (6k+1)a_k,
    V_half=sum_(k=0)^h (8k+1)c_k.

The frozen Task's accepted first-digit result states
W_p=sum_(k=0)^(p−1)(6k+1)a_k = p (mod p^2) in the target classes.
The proven Guo–Zudilin (2019) **half-cutoff** theorem says
V_half=p*(-3/p)=p (mod p^3) for these classes
(V.J.W. Guo and W. Zudilin, *A q-microscope for supercongruences*,
Adv. Math. 346 (2019), 329–358; https://arxiv.org/abs/1803.01830).
The original 216 valuation split shows
W_p=L_p+H_p (mod p^3) and H_p in p^2 Z_(p).
It follows that L_p−V_half lies in p^2 Z_(p) for **every target prime**,
not only the sample primes. Put M_p=(L_p−V_half)/p^2 (mod p).
Combining these sourced inputs with Theorem 1 gives

    (W_p−p)/p^2 =
       M_p + alpha_p[(4+6theta)(Q_r ⊙ B)]_(z=1/2)        (mod p).   (C)

Consequently **at the declared frozen scalar interface**,
W_p=p (mod p^3) iff the signed Chebyshev compensation
M_p=−alpha_p[(4+6theta)(Q_r ⊙ B)]_(z=1/2) (mod p).
This is an exact equivalent remaining condition, NOT a proof of its
vanishing and not an independently established Delta_p−R_p bridge.
The first-digit theorem is an explicit trusted frozen dependency;
without it the p^2-integrality of M_p is not claimed.

## Actual exact validation

Companion Python stdlib checker independently reconstructed original
216 and quartic 2304 factorial ratios mod p^3, initial factorial
normalization, per-position Chebyshev coefficients, and a separate
finite-binomial assembly. PASS: all 148 primes 7<=p<=2000 with
p=1(mod6), 22,952 original high-band indices. PASS: 77 target-class
primes for the signed L−V_half p^2-integrality, source-accurate
comparator, and equation (C). This finite check is not the proof.

    p     r   alpha   H/p^2   M    M+H/p^2
    13    2     10      10    3       0
    19    3     17       9   10       0
    37    6      4      20   17       0
    373  62    290     266  107       0

## Precise unfinished unit

Find a finite, original-source and endpoint-preserving WZ/Clausen
transport that evaluates M_p as the **negative** of (BIN).
First test the proposed relation itself, not just its summed zero,
at p=13,19,373 where both signed ports are nonzero.
Do not reopen already-closed Guo–Zudilin quartic val2 cancellation
or earlier original high Green/second-jet facts. Native p=373 H0/B0
semilinear Frobenius experiment #1559 is NOT executed by this code.

Native status actually read: Gateway 0.6.11,
research_authority_granted=false,
UPSTREAM_CODE_REVIEW_REQUIRED, executor_binding_configured=false,
active request jobs 5/5. Direct recovery_status not exposed as a
named callable action in this client. No new session/CLAIM/OPEN,
native Source checkpoint, Result, review, or admission asserted.
Old request/staging and maintenance lane preserved. Issue #1558
remains the control remediation path. No schedule setting changed.
