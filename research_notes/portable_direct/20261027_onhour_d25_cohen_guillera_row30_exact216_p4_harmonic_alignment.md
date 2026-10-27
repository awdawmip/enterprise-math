# D25/LIFT — exact original-216 prior-art match and a proved L(-3,3-p) / inverse-square observer bridge

**Date:** 2026-10-27. **Lane:** chatgpt-research-onhour-enterprise-math-20260923, not the maintenance lane. **Parent:** ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION. **Task:** RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; **frozen scientific Source pin:** c47e13e4aba0e006366f989d6334d443f6333ae3 (unchanged).

**Result class:** AUTHOR-SIDE / EXACT PRIOR-ART OBJECT IDENTIFICATION PROVED / HARMONIC-CHARACTER CONVERSION PROVED / TEN FINITE p^4 CHECKS EXECUTED / EXTERNAL SUPERCONGRUENCE NOT PROVED / UNREVIEWED / NOT_ADMITTED / NO NATIVE H0-B0 RUN / REGISTER_PENDING. Not a Source-native CLAIM, checkpoint, Result or independent review.

## 1. New exact positive literature identification (not the previous E.2 termwise transfer)

**Primary external source:** Henri Cohen and Jesús Guillera, *Rational Hypergeometric Ramanujan Identities for 1/pi^c: Survey and Generalizations* (2021), arXiv:2101.12592v1, https://arxiv.org/html/2101.12592v1 . Section 1 Definition 1.1; Section 3 basic list **row 30**; Section 6 Taylor coefficient table **row 30**; Section 8 general supercongruence and its one-higher-digit refinement. The paper is primarily a survey. Its generic p-adic rule is worded "we should have" and the abstract calls the generalizations a survey **without proof**; do not promote that recipe into an all-prime theorem.

Section 3 row 30 specifies exactly
- level N=3, H_N=R_n(2)R_n(3);
- CM parameter tau=sqrt(-6)/3, rational a=2;
- P(n)=6n+1, k=3^3=27;
- convergent complex identity sum_{n>=0} P(n)H_N(n)/2^n = sqrt(27)/pi = 3 sqrt(3)/pi.

From Definition 1.1, R_n(2)=(1/2)_n/n!, R_n(3)=(1/3)_n(2/3)_n/(n!)^2. The **termwise exact identity in Q**, with no index change, is

(6n+1)R_n(2)R_n(3)/2^n
 = (6n+1) (1/2)_n(1/3)_n(2/3)_n/[2^n (n!)^3]
 = (6n+1) binom(2n,n)^2 binom(3n,n)/216^n.

Thus row 30's finite p-1 sum is **exactly the frozen W_p itself**, retaining original index, 216 denominator, weight, cutoff, and mod p^3/p^4 meaning. This is fundamentally unlike the previously examined Van Hamme E.2 \`(1/3)_n^3(-1)^n\` series: no speculative termwise transfer is necessary.

Section 8's generic p^3 *proposal* with c=1, k=27 and P(0)=1 specializes precisely to
    W_p ?= p * (-108/p) = p * (-3/p) mod p^3         (HYPOTHESIS, not a proved theorem here).
For the frozen classes p≡13,19 (mod24), (-3/p)=+1. The inert CM character (-6/p)=-1 in those same classes is a **different labeled observation** and must not be silently substituted for (-3/p). The level-3 CM parameter tau=sqrt(-6)/3 is compatible with the prior D=-24 context, but its complex CM presentation does not prove the p-adic congruence.

## 2. New proved exact bridge: the source's p^4 correction to one inverse-square harmonic readout

Section 6 row 30 lists C_3=-15/4 and the fundamental discriminant D=-3. Section 8 *proposes* the sharper formula
    W_p ?= p*(-3/p) - (15/4) p^3 L(chi_-3,3-p)  mod p^4.   (CONJECTURAL p^4 statement)
Here chi_-3 is the primitive quadratic Dirichlet character modulo 3 and L is the **generalized Bernoulli special value**, not an arbitrary coefficient. It is not the already accepted LIFT theorem.

We **prove**, independent of that conjecture, that for every prime p>3, writing n=p-2 and t the unique integer 1<=t<p with 3t≡1 (mod p),
    L(chi_-3,3-p) ≡ -(2/9) sum_{j=1}^{t-1} j^(-2)  (mod p).
All inverses are in F_p; no denominator divisible by p is introduced. Indeed
    L(chi_-3,1-n) = - B_(n,chi_-3)/n
                  = - 3^(n-1)[B_n(1/3)-B_n(2/3)]/n
                  = - 2*3^(n-1) B_n(1/3)/n
because n=p-2 is odd, B_n(2/3)=-B_n(1/3). Bernoulli coefficients of order <=p-2 are p-integral. Modulo p, 1/3=t; B_n(0)=0; the difference identity B_n(x+1)-B_n(x)=n x^(n-1) gives
    B_n(t) = n sum_{j=1}^{t-1} j^(p-3)
           = n sum_{j=1}^{t-1} j^(-2) mod p.
Finally 3^(n-1)=3^(p-3)≡3^(-2) mod p. QED.

For p≡1 (mod3), t=(2p+1)/3 and sum_{j=1}^{p-1}j^(-2)=0 mod p. Reflection j<->p-j proves
    L(chi_-3,3-p) ≡ (2/9) H_((p-1)/3)^(2) mod p.
For p≡2 (mod3), t=(p+1)/3 yields
    L(chi_-3,3-p) ≡ -(2/9) H_((p-2)/3)^(2) mod p,
where H_N^(2)=sum_{j=1}^N j^(-2) in F_p.

Therefore the **conjectural source refinement** is **rigorously equivalent** to two explicit finite observer conditions:
    p≡1 (mod3): W_p ?= +p - (5/6)p^3 H_((p-1)/3)^(2) mod p^4,
    p≡2 (mod3): W_p ?= -p + (5/6)p^3 H_((p-2)/3)^(2) mod p^4.
In particular the *frozen* D25 p≡13,19 (mod24) fourth digit is predicted by a **single low-range inverse-square harmonic readout**, with no new E3/Frobenius gauge choice. This is a proved simplification of an external conjectural coefficient, **not** an all-prime proof of the conjecture, LIFT, or the native H0/B0 benchmark.

## 3. Executed verification and precision boundary

The companion program \`d25_cohen_guillera_exact216_p4_harmonic_check_20261027.py\` was run in this turn. It cross-checks:
1. first fifteen rational terms of R_n(2)R_n(3)/2^n against the exact original binomial ratio;
2. an independent original integer-binomial sum against the rational hypergeometric modular recurrence to modulus p^4;
3. the displayed Dirichlet L(-3,3-p) modulo p via Bernoulli polynomial recurrence versus the proved reciprocal-square formula;
4. the source's **proposed**, not proven, p^4 correction against actual arithmetic for p=7,11,13,17,19,23,37,43,73,373.

All checks passed. At the frozen p=373, H_124^(2)=174 (mod373), L(chi_-3,-370)=163 (mod373), and the predicted fourth digit -5/6*174=228 (mod373), matching independently computed W_373≡373+228*373^3 mod373^4. At p=13: H_4^(2)=10 and fourth digit 9; at p=19: H_6^(2)=16 and fourth digit 12. These *numerical* fourth digits were already previously known; **new increment is their exact alignment with published same-object prior art and the proved simple harmonic readout**. This is not new broad prime enumeration and ten passing fixtures are not a proof of any supercongruence.

## 4. Information loss / future research / preserved native debt

BRC typing: carrier = labeled original W coefficients and source row 30 (not E.2), two separate characters (-3/p) and (-6/p), finite p^4 arithmetic and rational L-value; observer = p^3 coefficient after exact leading p*chi, and H^(2) over F_p; valid operations = exact term identification, finite reciprocal sums and modular reduction with p-unit denominators. The proved quotient from special L value to H^(2) preserves the requested fourth digit modulo p but **does not determine the real native Frobenius operator or any sixth-axis native spatial state**. Analytic CM/modular formulas are externally typed mathematical observers, not X6-native dynamics. P000 remains locked.

The published recipe offers a direct same-object prior-art path rather than a transfer from Van Hamme E.2. **First next mathematical action only under lawful canonical routing:** determine whether a primary source actually *proves* the row-30 supercongruence at p^3 or p^4; if not, attempt a valid uniform proof via the source's level-3 modular / harmonic method and retain full cutoff and p-adic boundary. Never cite this survey's suggestive equation or the ten checks as a completed proof.

**Higher-priority native responsibility unchanged:** https://github.com/awdawmip/enterprise-math/issues/1559 remains the original fixed p373 H0/B0 divided-power request, real [X]U mod139129, rank, semilinear Frobenius/eta, signed odd Green/Hesse, kappa and Delta-R; no actual native executor/result is supplied here. Do not replace its benchmark with the harmonic prediction. D25/LIFT/JT2 remains OPEN. No other owner's CLAIM/run/Result borrowed; all frozen predecessors, completed UR/CM0/source R and previous author's exact fourth-digit arithmetic are consumed, not repeated or credited. Staging stays separate.

**Control continuation as last verified in this run:** own recovery request #6575 projected ACTIVE session but execution_authorized=false, source_authority_verified=false, no own run/claim; own dispatch request #6576 definitively FAILED/TimeoutExpired, not NO_DISPATCH. Gateway v0.6.11 Site grants source/control read but research_authority_granted=false and native control quota 5/5. No new protected Source mutation, session, claim/open, freeze or Result attempted. This stand-alone GitHub proof and source assessment is AUTHOR-SIDE, **not** a Source \`publish_checkpoint\`. Next exact protected action is lawful Source recovery/continuation after restoring permissions, then canonical claim/dispatch only as routed. Scientific source pin c47e13e4aba0e006366f989d6334d443f6333ae3 and task/scheduler/notification controls remain unchanged.
