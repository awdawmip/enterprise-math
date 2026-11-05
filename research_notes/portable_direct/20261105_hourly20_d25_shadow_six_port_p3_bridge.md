# D25 — signed 216 integer-shadow to six-port p-adic jet/shell certificate

Date: 2026-11-05 (+08). Role: TASK_RESEARCH, author-side portable research. Logical research lane: `chatgpt-research-hourly-enterprise-math-20260923`.
Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; immutable publication `TP2-B6F4FC938FF94941C1B7`; frozen scientific source pin `c47e13e4aba0e006366f989d6334d443f6333ae3`.
Status: **AUTHOR-PROVED exact finite-ring identity / FINITE-EXACT-CHECKED (94 primes) / UNREVIEWED / NOT_ADMITTED**. This is an explicit integer-shadow *interface* and valuation-port composition; do not recredit the pre-existing general three-stratum decomposition or prior 216/2304 scans.

## Precise statement

For any prime `p=6n+1>=7`, put `M=p^3` and consider the original 216 series
[
W_p=sum_{k=0}^{p-1}(6k+1)t_k,qquad
t_k=rac{(1/2)_k(1/3)_k(2/3)_k}{2^k(k!)^3}.
]
All following fractions are in `Z_(p)` and taken at their stated precision. Set
[
f_k=(-1)^k 2^{-k}inom{2n}{k}inom{3n}{k}inom{4n}{k}quad(0le kle2n),
]
[
H_{m,k}=sum_{j=0}^{k-1}(j-m)^{-1},quad
J_{m,k}=sum_{j=0}^{k-1}(j-m)^{-2}quad(0le kle m),
]
[
L_k=	frac12 H_{3n,k}+	frac13 H_{2n,k}+	frac23 H_{4n,k},qquad
Q_k=	frac14 J_{3n,k}+	frac19 J_{2n,k}+	frac49 J_{4n,k}.
]
For `2n<k<=3n`, define
[
q_k=rac{inom{3n}{k}inom{4n}{k}(2n)!(k-2n-1)!}{3cdot2^k k!},
]
[
B_k=	frac13left(-sum_{j=1}^{2n}j^{-1}+sum_{j=1}^{k-2n-1}j^{-1}ight)+	frac12 H_{3n,k}+	frac23 H_{4n,k}.
]
For `3n<k<=4n`, define
[
e_k=rac{(-1)^{3n+k}(2n)!(3n)!(k-2n-1)!(k-3n-1)!inom{4n}{k}}{6cdot2^k(k!)^2}.
]
Define six **provenance-preserving signed BRC ports**:
[
S=sum_{k=0}^{2n}(6k+1)f_k,quad
A=sum_{k=0}^{2n}(6k+1)f_kL_k,quad
B=sum_{k=2n+1}^{3n}(6k+1)q_k,
]
[
C=sum_{k=0}^{2n}(6k+1)f_k(L_k^2-Q_k)/2,quad
D=sum_{k=2n+1}^{3n}(6k+1)q_k B_k,quad
E=sum_{k=3n+1}^{4n}(6k+1)e_k.
]
Note `S=2^(-2n)C_n` **exactly**, for the prior integer-shadow `C_n=sum (6k+1)(-1)^k 2^(2n-k) binom(2n,k)binom(3n,k)binom(4n,k)`.

**Theorem (exact p-adic six-port observation law):**
[
oxed{W_pequiv S+p(A+B)+p^2(C+D+E)pmod{p^3}.}
]
The precise carrier is
`(S mod p^3, A mod p^2, B mod p^2, C mod p, D mod p, E mod p)`,
with the displayed signed linear readout. Reduction of all ports to `mod p`, or retaining the integer shadow alone, loses the second-digit correction.

**Equivalent two-stage LIFT scalar certificate:** Set `Z=S+p(A+B)-p`. Then `W_p=p mod p^3` if and only if
[
Zequiv0pmod{p^2},qquad Z/p^2+C+D+Eequiv0pmod p.
]
The second quotient is defined when the first condition holds. This is a strict explicit finite-ring reduction of the signed-216 scalar target; no general all-prime vanishing is assumed.

## Proof

Write the three parameters exactly as `(-3n+p/2,-2n+p/3,-4n+2p/3)`.
For `k<=2n`, none of the three underlying negative-integer Pochhammer products has a zero; expanding the finite products through second order yields
[
t_kequiv f_kleft(1+pL_k+rac{p^2}{2}(L_k^2-Q_k)ight)pmod{p^3}.
]
For `2n<k<=3n`, the `-2n` product has exactly one zero and the other two none, whence
[
t_kequiv p q_k(1+pB_k)pmod{p^3}.
]
For `3n<k<=4n`, both `-2n` and `-3n` products have one zero, giving `t_k≡p^2e_k (mod p^3)`. For `4n<k<p` all three products contain a zero so the term is `0 mod p^3`. Because `4n<p` and `k<p`, all displayed denominator factors are p-adic units. Multiplying each stratum by `6k+1` and summing proves the theorem. The two-stage certificate follows from elementary modular divisibility.

## Exact executable checks / signed readouts

A distinct direct original-series recurrence
`t_(k+1)=t_k(2k+1)(3k+1)(3k+2)/(36(k+1)^3)`,
computed modulo `p^3` and independently compared with the six-port formula, gives **94/94 PASS** for all primes `7<=p<=1200, p=1 mod6`.

| p | S (mod p^3) | A (mod p^2) | B (mod p^2) | (C,D,E) (mod p) | Z/p^2 (mod p) | C+D+E (mod p) | W (mod p^3) |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 13 | 442 | 130 | 45 | (5,8,10) | 3 | 10 | 13 |
| 19 | 5491 | 351 | 292 | (1,17,9) | 11 | 8 | 19 |
| 373 | 15521276 | 3122 | 44787 | (82,158,266) | 240 | 133 | 373 |

For these cases `Z=0 mod p^2` and the second-stage sums are zero mod p, with visible nonzero internal coordinates. The finite checks complement (rather than substitute for) a uniform proof of `W_p=p mod p^3`.

## Provenance, reuse, next problem

BRC resolution: **COMPOSE_APPLIED** — existing integer-shadow `C_n`, existing three-stratum signed-Pochhammer source decomposition and frozen scalar `W_p` interface are combined into a six-port `Z_(p)` observer. Population = ordered k terms 0..p-1, branch = unique valuation stratum plus derivative jet, future operation = signed weighted sum modulo p^3; retain exact k, p, n and source parameter tuple. This is an *ordinary arithmetic* certificate, not original-class native H0/B0 or semilinear Frobenius evidence.

Existing native Source frontier, recorded completed_units, contributor IDs, do_not_repeat, and native experiment obligations stay untouched; exact Source task read request `em-h20-20261105-1748-task-current` succeeded on Source `8228566b152812c1f9e5af58ecfa4ae6e545a326`, but its `execution_authorized=false`. The preceding failed continuation read was `em-h20-20261105-1620-current-continuation` with `CANONICAL_REJECTED: unknown current immutable task publication`; retain its error and the existing controller support issue #1558. This material is author-side portable research, not a new native checkpoint.

**Next exact science:** derive a finite telescoper or parameter-derivative identity enforcing `Z/p^2+C+D+E=0 mod p` uniformly for `p≡13,19 mod24`, testing a candidate on p=13,19,373 with all six provenance ports before claiming LIFT. The integer-shadow all-n divisibility conjecture remains an independent route. Preserve original p373 native `[X]U mod139129` obligation (support issue #1559).

No original Source task publication, session, claim, run or scheduler was modified by this author-side derivation.
