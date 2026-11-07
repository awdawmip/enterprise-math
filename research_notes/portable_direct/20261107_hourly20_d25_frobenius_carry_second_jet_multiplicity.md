# D25: exact Frobenius-carry multiplicity, universal third-jet coefficient 5 (2026-11-07)

**Status:** AUTHOR-SIDE ALGEBRA PROVED; 815-prime exact checks; UNREVIEWED / NOT_ADMITTED. This is not a native Researcher CLAIM/Result/review.

**Research lane:** \`chatgpt-research-hourly-enterprise-math-20260923\` (not maintenance). Parent \`RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT\`, publication \`TP2-B6F4FC938FF94941C1B7\`, immutable science pin \`c47e13e4aba0e006366f989d6334d443f6333ae3\`. Consumes the preceding hourly20 Frobenius factorization at \`dd3af761bcce0a6dd420b7e3fdde7a982fe547b1\`; distinct onhour work at \`d115e8c962930b2726c0f5463565dee08109ebac\` concerns a separate *p-adic* quadratic jet and is not duplicated.

## Theorem A: exact binomial carrier

Let \(p=8k+5\) be prime, \(k\ge0\), and work in \(\mathbb F_p[z]\). Put \(r=5k+3\), \(s=7k+4\), and \(t=4k+3=(p+1)/2\). Define

\[
G(z)=\sum_{j=0}^{r}\binom rj\binom sj z^j,\qquad
H(z)=\sum_{j=0}^{k}\binom{3k+1}{j}\binom kj z^j .
\]

Then **exactly as polynomials over the finite field**,

\[
\boxed{G(z)=(1-z)^tH(z).}
\]

Proof: Euler's Gauss hypergeometric transformation yields \({}_2F_1(-r,-s;1;z)=(1-z)^{1+r+s}{}_2F_1(1+r,1+s;1;z)\) as characteristic-zero formal series. Reduce coefficients of degree \(<p\). Since \(1+r\equiv-(3k+1)\), \(1+s\equiv-k\), and \(1+r+s=p+t\), the right side is congruent modulo \(z^p\) to \((1-z)^tH(z)\). Both polynomial sides have degree \(r=5k+3<p\); hence equality is exact in \(\mathbb F_p[z]\).

## Theorem B: squarefree carrier polynomial

Vandermonde's identity gives \(H(0)=1\) and

\[
H(1)=\sum_{j=0}^{k}\binom{3k+1}{j}\binom kj
=\binom{4k+1}{k}\not\equiv0\pmod p.
\]

The terminating Gauss equation is

\[
z(1-z)H''+(1+4kz)H'-k(3k+1)H=0.
\tag{1}
\]

If \(\alpha\) were a multiple root of \(H\) in the algebraic closure, it would not be \(0\) or \(1\), and \(H(\alpha)=H'(\alpha)=0\). Repeatedly differentiating (1) at \(\alpha\) forces \(H^{(j)}(\alpha)=0\) for every \(0\le j\le k\), since \(\alpha(1-\alpha)\ne0\). As \(k<p\), all \(j!\) are invertible, forcing \(H\equiv0\), contrary to \(H(0)=1\). Therefore **all \(k\) roots are distinct** (if \(k=0\), no roots).

## Theorem C: complete Frobenius carry multiplicity

Write \(Q(z)=(1-z)H(z)^2\). From Theorem A and \(2t=p+1\),

\[
G(z)^2=(1-z^p)Q(z).
\]

Since \(\deg Q=2k+1<p\), the part of \(G^2\) supported in degree \(\ge p\) is exactly

\[
\boxed{C(z)=-z^p(1-z)H(z)^2.}\tag{2}
\]

Its roots over the algebraic closure, counted with multiplicities, are: \(0\) with order \(p\); \(1\) with order \(1\); and the \(k\) distinct roots of \(H\), each with order **exactly two**. The sum \(p+1+2k\) equals \(\deg C\).

At any root \(\alpha\) of \(H\),

\[
C(\alpha)=C'(\alpha)=0,\quad
C''(\alpha)=-2\alpha(1-\alpha)H'(\alpha)^2\ne0.
\]

Let \(\theta=z\,d/dz\) and \(\mathcal W=1+8\theta\), the polynomial differential observer associated with the 2304 weight \(8j+1\). Then

\[
\mathcal W C(\alpha)=0,\qquad
\theta\mathcal W C(\alpha)=-16\alpha^3(1-\alpha)H'(\alpha)^2\ne0.
\tag{3}
\]

This is **not** an identification of aggregated mod-\(p\) carry with the separately indexed native 2304 \(p\)-adic tail. It is a full certificate for the declared aggregate and future differentiation operation.

## Theorem D: universal third-jet coefficient 5 at the exact 1/9 root

Assume additionally \(H(1/9)=0\) in \(\mathbb F_p\); this assumption is **not yet proved for every \(p\equiv13\bmod24\)**. Since \(8k+5=p\),

\[
4k\equiv-\frac52,\qquad k(3k+1)\equiv\frac{35}{64}\pmod p.
\]

Equation (1) evaluated at \(z_0=1/9\), with \(H(z_0)=0\), gives the prime-independent ratio

\[
\boxed{16H''(z_0)+117H'(z_0)=0.}\tag{4}
\]

Direct differentiation of \(Q=(1-z)H^2\) yields

\[
Q''(z_0)=\frac{16}{9}H'(z_0)^2,\qquad
Q'''(z_0)=6\left(\frac89H'(z_0)H''(z_0)-H'(z_0)^2\right)
=-45H'(z_0)^2.
\]

The derivative of \(z^p\) is zero in characteristic \(p\). Hence (2) gives the **exact universal coefficients**

\[
\boxed{C''(1/9)=-\frac{16}{81}H'(1/9)^2,\qquad
C'''(1/9)=5H'(1/9)^2\pmod p.}\tag{5}
\]

Here \(H'(1/9)\ne0\) by Theorem B. The first observer \((1+8\theta)C\) is zero, but its next differentiated observer is nonzero. The repeated appearance of the numeral \(5\) in another, previously established cross-source residue is an explicit **comparison candidate only**, not an identification between independent invariants.

## Exact independent arithmetic scope

The attached standard-library Python file computes the binomial sum \(H\) and its first two derivatives directly via modular recurrences, then checks the ODE, aggregate second jet, universal relation (4), third jet (5), and weighted differential observer. It tests all 815 primes \(p<30000,\ p\equiv5\bmod8\).

- 407/407 primes \(p\equiv13\bmod24\): \(H(1/9)=0\), with nonzero second and third jet.
- 408/408 primes \(p\equiv5\bmod24\): \(H(1/9)\ne0\).
- These finite residue-class observations are **not** universal zero/nonzero theorems.

| p | H(1/9) | H'(1/9) | C''(1/9) | C'''(1/9) | theta(1+8theta) C(1/9) |
|---:|---:|---:|---:|---:|---:|
| 13 | 0 | 4 | 10 | 2 | 5 |
| 29 | 7 | 0 | 18 | n/a | n/a |
| 37 | 0 | 11 | 30 | 13 | 29 |
| 61 | 0 | 27 | 39 | 46 | 40 |
| 109 | 0 | 14 | 3 | 108 | 77 |
| 181 | 0 | 124 | 42 | 136 | 98 |
| 373 | 0 | 369 | 333 | 80 | 323 |

## BRC scope, next exact action, control boundary

The preserved carrier is the source-indexed polynomial square and its projected degree-\(\ge p\) aggregate. Evaluation and first weighted differentiation collapse information that the next jet detects. This theorem certifies the **aggregate** quotient for the stated future differential operations, not equivalence of individual source ports.

The next open scientific unit is the general \(H_p(1/9)=0\) congruence for \(p\equiv13\bmod24\) (or the first verified counterexample). Work from the proved \(O(k)\) binomial formula in Theorem A, seek a field-character/CM or exact finite-telescoping certificate, and then test a two-legged 216/2304 weighted finite-sum transfer against (3)–(5). Keep the mother target \(\Delta_p-R_p=0\bmod p\) for \(p\equiv13,19\bmod24\) **OPEN**.

Native status in this lane: \`BACKEND_IDENTITY_OR_VERSION_MISMATCH\`, \`operation_sent=false\`, Site \`CONFIGURED_NOT_LIVE_VERIFIED\`; original requests \`em-h20-20261106-1324-d25-task-r13\` and \`em-h20-20261106-1324-d25-cont-r13\` cannot be reconciled; session/claim/run and staging stay \`UNKNOWN_PRESERVE\`. Activity registration \`REGISTER_PENDING\`; support issue \`awdawmip/enterprise-math#1558\`. A GitHub author note does not create a native Source checkpoint.
