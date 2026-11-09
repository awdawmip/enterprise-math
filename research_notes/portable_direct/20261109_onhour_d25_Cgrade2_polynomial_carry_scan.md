# D25 / AF4 — original 2304 grade-2 finite-field polynomial and carry

Date: 2026-11-09. Mother Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; immutable publication TP2-B6F4FC938FF94941C1B7; frozen science c47e13e4aba0e006366f989d6334d443f6333ae3.

Status: **AUTHOR-SIDE EXACT ALGEBRAIC REDUCTION + FINITE EXPERIMENT; UNREVIEWED / NOT_ADMITTED / NOT_NATIVE**. Ordinary Research lane chatgpt-research-onhour-enterprise-math-20260923, separate from maintenance chatgpt-hourly-enterprise-math-20260921.

## Scientific connection

Use the original full sums

$$
W_p=\sum_{n=0}^{p-1}(6n+1)A_n,\qquad
V_p=\sum_{n=0}^{p-1}(8n+1)C_n,
$$

$$
A_n=\frac{\binom{2n}{n}^{2}\binom{3n}{n}}{216^n},
\qquad
C_n=\frac{\binom{4n}{2n}\binom{2n}{n}^{2}}{2304^n}.
$$

The unproved AF4 candidate is
$E_p=W_p-2V_p+p\left(\frac{-3}{p}\right)\equiv0\pmod{p^4}$.
Prior grade-layer work defined
$\ell=(W_0+W_1-2(V_0+V_1)+p\chi)/p^2\bmod p^2$,
$b=(W_2-2V_2)/p^2\bmod p^2$ and
$t=(W_3-2V_3)/p^3\bmod p$.
Only sample primes had been checked for the special cancellation
$V_2/p^2\equiv0\pmod p$.

## Proven reduction for every prime p>3

For $0\le n<p$, $v_p(C_n)=\lfloor4n/p\rfloor$. Define

$$
n_0=\frac{p+1}{2},\qquad n_1=\left\lfloor\frac{3p-1}{4}\right\rfloor,
\qquad N=n_1-n_0=\left\lfloor\frac{p-3}{4}\right\rfloor.
$$

The grade-2 contribution is
$V_{2,p}=\sum_{n=n_0}^{n_1}(8n+1)C_n$.
The first normalized coefficient is the nonzero unit
$K_p=C_{n_0}/p^2\bmod p$.

The original rational coefficient recurrence is

$$
\frac{C_{n+1}}{C_n}=
\frac{(4n+1)(4n+3)(2n+1)}{288(n+1)^3}.
$$

For $n=n_0+j$, $0\le j<N$, its mod-p unit reduction is

$$
\frac{C_{n_0+j+1}/p^2}{C_{n_0+j}/p^2}
\equiv\frac{(j+3/4)(j+5/4)(j+1)}
{9(j+3/2)^3}\pmod p.
$$

Also $8(n_0+j)+1\equiv8j+5\pmod p$. For $p=4m+1$, $N=m-1$ and
$(3/4,5/4)\equiv(N+2,-N)\pmod p$; for $p=4m+3$,
$N=m$ and $(3/4,5/4)\equiv(-N,N+2)\pmod p$.
All denominators are units throughout this index range.
Therefore **the following is proved for every prime p>3**:

$$
\boxed{\frac{V_{2,p}}{p^2}\equiv K_p\,P_N(1)\pmod p,}
$$

$$
\boxed{
P_N(x)=\sum_{j=0}^{N}(8j+5)
\frac{(-N)_j(N+2)_j(1)_j}{(3/2)_j^3}
\left(\frac{x}{9}\right)^j\in\mathbb F_p[x].
}
$$

This retains the original coefficient, original signed weight, index interval, and $p$-adic grade. It is a finite-field change of representation, not a native H0/B0 operator computation.

**Uniform open statement:** $P_N(1)=0$ for all primes $p>3$, equivalently $V_{2,p}\equiv0\pmod{p^3}$. The reduction is proved; this zero statement is not yet proved in general.

## Complete finite domain actually checked

A local exact-integer run sieved all **1,227 primes with $5\le p\le10,000$**, maximum p=9973. The code independently evaluates the original modular recurrence and the normalized polynomial.

* $P_N(1)=0$ and $V_{2,p}/p^2=K_pP_N(1)=0$: 1,227 of 1,227.
* $P'_N(1)\ne0$: 1,226 of 1,226 primes $p>5$. For $p=5$, $N=0$ and $P_0(x)=5\equiv0$.
* With the original AF4 lower/second coefficient-grade split, canonical digits satisfy $\ell_0+b_0=p$ (thus the actual base-p carry is $c=1$): 1,227 of 1,227.
* At p=13, 19 and 373, a second implementation using original integer binomial coefficients independently reproduces both $K_p$ and $V_{2,p}/p^2$.

| p | N | Kp | P_N(1) | P'_N(1) | V2/p² | W2/p² | ell0 | carry |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 13 | 2 | 4 | 0 | 3 | 0 | 10 | 3 | 1 |
| 19 | 4 | 9 | 0 | 2 | 0 | 9 | 10 | 1 |
| 73 | 17 | 71 | 0 | 58 | 0 | 31 | 42 | 1 |
| 373 | 92 | 114 | 0 | 152 | 0 | 266 | 107 | 1 |
| 9973 | 2492 | 9696 | 0 | 7249 | 0 | 9655 | 318 | 1 |

The exact record encoding (ordered increasing prime, fields p,N,ell0,b0,Pprime1,Kp; commas within records and semicolons between records) has SHA256:
09de1b21406c355d9cd14cff5994d36dce0a7b563783652fccc225f2ca9eefa6.
Use d25_C_grade2_polynomial_20261109.py to regenerate and verify; no floating point.

## Recovery and next action

The next load-bearing mathematics is to prove or refute the uniform identity
$P_N(1)=0$ under the exact prime relation $p=4N+3$ or $4N+5$, by finite-field hypergeometric/holonomic, finite WZ, or a source-preserving modular transformation. The derivative observation gives a second discriminating test. If uniformly proved, this removes the **2304** coefficient-grade-2 contribution from the third-digit AF4 interface, leaving the original **216** grade-2 carrier; the fourth-digit carry and boundary equation still remain.

The original native $p=373$ H0/B0 divided-power $[X]U\bmod139129$, rank, semilinear Frobenius direction, normalization eta, signed kappa, original Delta-R and independent reproduction remain **NOT_RUN / PENDING_OWNER**, tracked by existing issue #1559. This research does not replace that benchmark.

Fresh canonical continuation request onhour11-20261109-1400-current-task-continuation returned SUCCEEDED observed 2026-11-09 06:06:02 UTC, task route REGISTER_NEW_SESSION_AND_CLAIM_CURRENT_PUBLICATION, NO_LIVE_CLAIM, execution_authorized=false; source changed during the read and would require a fresh write check. Own recovery_status returned SITE_CONTROL_OWN_ISSUED_SESSION_REQUIRED. No new native session, claimant, run, formal checkpoint, Result or acceptance was asserted or produced. Previous author-side AF4 scans and original D24 UR work remain completed at their actual prior scope.
