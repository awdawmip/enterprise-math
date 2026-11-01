# D25: finite Legendre port for the beta Gauss factor and its exact first p-adic defect

2026-10-31. AUTHOR-SIDE MATHEMATICAL DERIVATION / EXACT FINITE TEST / UNREVIEWED / NOT_ADMITTED. The frozen scientific Source pin c47e13e4aba0e006366f989d6334d443f6333ae3 remains unchanged. Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7. Prior author-side character conjecture: commit c68fd26c8e605f2434a38f17f786a3bc2b26b6f7.

## Setup and theorem

For a prime p>3 with p=5 or 7 mod 8 define

\[
F_p(z)=\sum_{k=0}^{p-1}\frac{(1/8)_k(3/8)_k}{(k!)^2}z^k,\quad z_0=1/9,\quad
G_p=F_p(z_0),\quad H_p=[(1+16z\partial_z)F_p(z)]_{z=z_0}.
\]

Set n=(p-1)/4 if p=5 mod8, n=(p-3)/4 if p=7 mod8; n is odd. Set e=(p+1)/2 and

\[
Q_p(z)=\frac{P_n(\sqrt{1-z})}{\sqrt{1-z}},\qquad S_p(z)=(1-z)^e Q_p(z).
\]

Q is a rational polynomial: P_n is odd and its coefficients have denominators that are p-units. No square-root branch is needed in the final expression.

**THEOREM 1 (universal modulo-p polynomial).**

\[
\boxed{F_p(z)\equiv S_p(z)\pmod p\quad\text{in }\mathbb F_p[z],}
\]

and both reduced polynomials have degree (5p-1)/8 if p=5 mod8, or (5p-3)/8 if p=7 mod8, strictly less than p.

**Proof.** The hypergeometric coefficients satisfy
\[
(k+1)^2c_{k+1}=(k+1/8)(k+3/8)c_k.
\]
The first numerator divisible by p occurs when 8k+1=5p in the 5 mod8 case, or 8k+3=5p in the 7 mod8 case. Thus the reduction of F_p has exactly the given degree and constant coefficient 1. Its differential operator is
\[
L=z(1-z)\partial_z^2+(1-3z/2)\partial_z-3/64.
\]
Writing x=sqrt(1-z) formally, the Legendre equation yields
\[
z(1-z)(P_n(x))''+(1-3z/2)(P_n(x))'
=-n(n+1)P_n(x)/4.
\]
Here n(n+1)/4=-3/64 mod p in both classes. Hence P_n(x) solves L=0 modulo p. Moreover S=(1-z)^{p/2}P_n(x) as a formal power series, and the formal derivative of (1-z)^{p/2} vanishes modulo p. Therefore S also solves L=0 modulo p and S(0)=1. The coefficient recurrence uniquely determines every coefficient before degree p because (k+1)^2 is a p-unit for k+1<p. S is a polynomial of degree e+(n-1)/2<p, so equality through degree p-1 proves polynomial equality. Its leading coefficient is nonzero because the Legendre leading coefficient 2^{-n} binom(2n,n) is a p-unit. QED.

## Two-observer consequence and precise p² carry

Let s=8/9. Exact reduction gives
\[
G_p\equiv s^e Q_p(z_0),\qquad
H_p\equiv (16/9)s^e Q'_p(z_0)\pmod p.
\]

**THEOREM 2 (unit partner).** G_p and H_p cannot both vanish modulo p. Indeed if they vanished, the nonzero polynomial S_p would have a double zero at z_0. It solves L S_p=0, whose leading coefficient z_0(1-z_0) is a p-unit. Its Taylor coefficient recurrence at z_0 forces all coefficients through degree less than p to be zero, contradicting S_p(0)=1. Thus a proof that the character-selected G or H vanishes modulo p² would automatically prove that the other is a p-unit; only selected vanishing remains to be shown.

Define the **beta-specific** exact defect
\[
\mathcal D_{\beta,p}(z)=\frac{F_p(z)-S_p(z)}p\in\mathbb Z_{(p)}[z].
\]
This is distinct from the **frozen signed boundary** R_p of the original 216 model. Theorem 1 justifies the coefficientwise divisibility, and ordinary differentiation yields the following exact rational polynomial identities:
\[
\boxed{G_p=s^eQ_p(z_0)+p\mathcal D_{\beta,p}(z_0),}
\]
\[
\boxed{H_p=s^e[-pQ_p(z_0)+(16/9)Q'_p(z_0)]
+p[(1+16z\partial_z)\mathcal D_{\beta,p}]_{z_0}.}
\]
The term -pQ is the exact integer exponent carry 1-2e=-p and matters modulo p².

If Q_p(z_0)=0 mod p, then G_p=0 mod p² **if and only if**
\[
s^e\,Q_p(z_0)/p+\mathcal D_{\beta,p}(z_0)=0\pmod p.
\]
If Q'_p(z_0)=0 mod p, then H_p=0 mod p² **if and only if**
\[
s^e[-Q_p(z_0)+(16/9)Q'_p(z_0)/p]
+[(1+16z\partial_z)\mathcal D_{\beta,p}]_{z_0}=0\pmod p.
\]
Division by p is only taken after the stated divisibility. These are exact **conditional** criteria, not a universal proof of the character-selected zero.

## Exact finite test; signed/valuation observers

The accompanying standard-library Python certificate independently constructs the characteristic-p polynomial, computes original Pochhammer coefficients modulo p², checks selected factor vanishing at ten primes, and cross-checks selected coefficients by direct numerator products at p=5,7,13,23,29. All reported checks pass, but selected p² vanishing for every prime remains an unproved conjecture.

| p | selected | Q mod p | Q' mod p | Legendre/carry port mod p | defect port mod p |
|---:|:---:|---:|---:|---:|---:|
| 5 | H | 1 | 0 | 2 | 3 |
| 7 | H | 1 | 0 | 3 | 4 |
| 13 | G | 0 | 4 | 3 | 10 |
| 23 | G | 0 | 12 | 2 | 21 |
| 29 | H | 7 | 0 | 7 | 22 |
| 31 | H | 29 | 0 | 20 | 11 |
| 37 | G | 0 | 11 | 29 | 8 |
| 47 | G | 0 | 44 | 36 | 11 |
| 71 | G | 0 | 16 | 33 | 38 |
| 373 | G | 0 | 369 | 95 | 278 |

Each pair of last two columns sums to zero modulo p. In particular at p=5 the derivative carry alone contributes 2 and the beta defect contributes 3. A quotient retaining only characteristic-p Legendre output erases a relevant p² source. This is **BRC REUSE_APPLIED** with typed finite coefficients, signed port, p-adic valuation and derivative operator, not a positive-mass cancellation theorem, native X6 theorem, or original-class Frobenius computation.

## Next exact research unit and control frontier

First prove characteristic selection of Q(z_0)=0 or Q'(z_0)=0 modulo p via a finite-field CM/Legendre evaluation. Then prove the relevant p² defect-port cancellation for all p in the specified classes, using the equations above. The unproved original 216 p³ target and the stronger A_p-2B_p+p χ_{-3}(p)=0 mod p⁴ bridge are separate. The original-class p373 native H0/B0 divided-power [X]U, semilinear Frobenius, module rank, eta, signed odd Green/Hesse, κ and independent replication under issue #1559 remain NOT_EXECUTED/PENDING_OWNER.

This is an author-side portable mathematical source artifact; not a formal Source checkpoint, accepted Result, review or registered Research-Activity. Research lane logical ID is chatgpt-research-onhour-enterprise-math-20260923 (separate from maintenance lane). Own historical recovery request research-onhour-20261031-0202-recovery-r15 at awdawmip/kimi-query-bridge#6632 showed no active CLAIM/run; dispatch request research-onhour-20261031-0205-dispatch-r15 at #6633 failed UPSTREAM_CODE_REVIEW_REQUIRED. The currently read Site Gateway 0.6.11 is read-only and grants no Researcher Source execution. Preserve these original requests without retransmission. Registration REGISTER_PENDING, mathematical review UNREVIEWED, admission NOT_ADMITTED. Preserve Source pin c47e13e4aba0e006366f989d6334d443f6333ae3, P000, ACTIVE worldview, and the existing research schedule and notifications.
