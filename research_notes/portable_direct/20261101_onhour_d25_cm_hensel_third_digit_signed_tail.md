# D25 p19 third CM Hensel digit: signed Clausen boundary enters linearly

**2026-11-01 Asia/Hong_Kong.** Scope: existing D25 SECOND-DIGIT-LIFT, author-side mathematical proof composition and 29-prime exact checker; **UNREVIEWED / NOT_ADMITTED / NATIVE_NOT_RUN / REGISTER_PENDING**. Research conversation \`chatgpt-research-onhour-enterprise-math-20260923\` remains separate from maintenance. Scientific Source pin \`c47e13e4aba0e006366f989d6334d443f6333ae3\`, P000 and ACTIVE worldview unchanged.

## New second consecutive scientific unit

Extend this run's newly proved **unique Gauss root mod p²** result without replacing the native H0/B0 benchmark. Work for all primes \(p\equiv19\bmod24\). Use the original
\[
F_p(z)=\sum_{k=0}^{p-1}\frac{(1/8)_k(3/8)_k}{(k!)^2}z^k,
\quad z_0=1/9,\quad G=F_p(z_0),\quad H=G+16z_0F_p'(z_0).
\]
Let \(D=F_p'(z_0)\) as a p-local integer modulo p², \(C=F_p''(z_0)\bmod p\); \(D\bmod p\) is a unit. The predecessor author-proved reflection gives the original signed \(\beta\)-Clausen boundary \(T_{\beta,p}=p^2U_{\beta,p}\bmod p^3\) with explicit \(O(p)\) recurrence. Guo–Zudilin's independently published \(B_p\equiv p\bmod p^3\) and \(B_p=GH-T_{\beta,p}\) yield the previously established
\[
\boxed{G/p\equiv H^{-1}(1+pU_{\beta,p})\pmod{p^2}.}\tag{R}
\]

Select integer digits \(d_1,d_2\in\{0,\ldots,p-1\}\) so that
\(F_p(z_0+p d_1+p^2 d_2)\equiv0\bmod p^3\). From the first-unit formula,
\[
d_1=-16(9H^2)^{-1}\bmod p
    =-2(P'_{(p-3)/4}(\sqrt{8/9})^2)^{-1}\bmod p,
\]
and \(d_1\ne0\). Define the *reproducible p-unit residue lifts*
\[
h=H\bmod p^2,\qquad g=h^{-1}(1+pU_{\beta,p})\bmod p^2,\qquad
D_2=D\bmod p^2,\quad D_0=D\bmod p .
\]
Because \(g+d_1D_2\equiv0\bmod p\), the quotient below is well-defined mod p. **New full-class third-digit formula**:
\[
\boxed{
d_2=-D_0^{-1}\left[
       \frac{g+d_1D_2}{p}+\frac{d_1^2}{2}C
       \right]\pmod p.}\tag{3D}
\]
All divisions by \(p\) occur on integral expressions *before* reduction. This is an actual algorithm for the unique third digit of the original Gauss polynomial root; it uses **signed \(U_{\beta,p}\)** and the first two derivative jets, not a new assumed hypergeometric supercongruence.

**Proof.** In the p-local polynomial ring, the second-order Taylor formula is
\[
F_p(z_0+p d_1+p^2d_2)
\equiv G+p d_1D+p^2(d_2D+\tfrac12d_1^2 C)\pmod {p^3}.
\]
Substitute (R) for \(G/p\bmod p^2\), divide by \(p\), and solve the remaining linear congruence because \(D_0\) is invertible. Uniqueness follows from the same simple-root derivative condition already proved at level p².

To **measure the exact signed boundary's contribution**, perform a separate comparison in the right side of (3D), using \(g^{(0)}=h^{-1}\bmod p^2\), with *unchanged* \(h,D_2,C,d_1\). Write \(d_2^{(0)}\) for this counterfactual algebraic readout. The two quotients differ by \(U_{\beta,p}h^{-1}\bmod p\); since \(d_1=-h^{-1}D_0^{-1}\bmod p\), their displacement satisfies
\[
\boxed{d_2-d_2^{(0)}\equiv d_1 U_{\beta,p}\pmod p.}\tag{SIGNED}
\]
This is a **source-sensitivity identity**, not a claim that \(g^{(0)}\) is a second real CM model. It proves algebraically that the genuine signed cutoff can change the third digit even when its contribution vanishes at the second-digit level; one must preserve it in further reductions.

## Independently executed exact certificate

The complete standard-library script \`research_notes/portable_direct/d25_cm_hensel_third_digit_20261101.py\` executed for **all 29 primes \(p\le1500,\ p\equiv19\bmod24\)**. It computes the reflected \(U\), original rising-factorial Gauss first/second derivatives, solves (3D), verifies (SIGNED), and **independently recomputes the original polynomial at the reconstructed root modulo p³**; the neighboring p²-lift is nonzero as predicted. All assertions passed.

| p | signed U | d1 | actual d2 | d2 ignoring U only in algebraic comparator | signed shift d1·U |
|---:|---:|---:|---:|---:|---:|
| 19 | 3 | 8 | 18 | 13 | 5 |
| 43 | 14 | 39 | 29 | 42 | 30 |
| 67 | 46 | 61 | 11 | 19 | 59 |
| 139 | 102 | 15 | 120 | 119 | 1 |
| 211 | 128 | 97 | 61 | 94 | 178 |
| 523 | 452 | 513 | 357 | 170 | 187 |

At 19 the unique root is \(z_*=5888\bmod6859\); the prior root modulo \(19^2\) was \(112\bmod361\) because \(5888\equiv112\bmod361\). The signed \(U=3\) changes the third-digit readout by \(8\cdot3=5\bmod19\). This is a concrete non-removable cutoff sensitivity witness in the BRC labeled \(\beta\)-Gauss source; it is **not** a p373 original-class Frobenius coefficient.

## Continuation, status, next action

First-unit p=19 exact simple-root displacement and this new third-digit formula are available as author-side outputs. They **do not** prove the original mother \(A_p\equiv p\bmod p^3\) for p≡13,19 mod24. The remaining target p13 requires a true proof of the zero-lift alignment \(d_p=0\), exactly equivalent to the prior two-shift Jacobi congruence. The original signed 216-model \(\Delta_p-R_p\) must then be joined without dropping its cutoff.

BRC resolution COMPOSE_APPLIED: carry \((p,G,H,D,C,U_{\beta},d_1,d_2)\) with original coefficient indices, p-adic valuations, **signed cutoff** and operation-specific polynomial-root observer; (SIGNED) quantifies information lost by dropping \(U_\beta\). Existing p19 p³ reflection is consumed, not re-proved. There is no native X6 promotion.

Native benchmark **Issue #1559** remains original-class p=373 H0/B0 divided-power \([X]U\bmod139129\), module rank, actual semilinear Frobenius/eta, odd Green/Hesse and \(\kappa\), original \(\Delta-R\) and independent reproducibility. Its actual execution is pending an authorized same-object evaluator; present scalar root computations cannot substitute. Current read-only Gateway 0.6.11 gave no research authority/executor binding, and own checkpoint/get request scope was denied; no Source CLAIM/run/Result or official review is inferred. Historical request \`research-onhour-20261031-0205-dispatch-r15\` remains unresolved in this client's scope; no duplicate dispatch, no maintenance-session use. Continue at the highest recorded author frontier when Source access becomes legal, preserving independent staging.
