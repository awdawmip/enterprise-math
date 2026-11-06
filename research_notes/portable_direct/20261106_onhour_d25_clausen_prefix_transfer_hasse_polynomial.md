# D25 — one-pass signed Clausen boundary transfer and the finite-field coefficient observer

2026-11-06. TASK_RESEARCH author-side continuation after the exact Clausen triangular identity in `20261106_onhour_d25_clausen_signed_triangle_boundary.md` (commit `ca7b5ce2b8044eb3b12e0ca69226e396fef3bfa9`). **AUTHOR-PROVED finite modular identities / EXACT FINITE CHECKED / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_H0_B0**.

Canonical Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`, publication `TP2-B6F4FC938FF94941C1B7`. Frozen scientific Source `c47e13e4aba0e006366f989d6334d443f6333ae3`; stable Research lane `chatgpt-research-onhour-enterprise-math-20260923`, maintenance lane not used. Parent objective Delta_p=R_p (modp), p=13/19 (mod24), remains OPEN. Native same-original-class H0/B0 p373 remains NOT_RUN (#1559).

## I. Exact finite-field coefficient reduction for the first Gauss factor

Take p=6m+1 prime and
[
d_n=\frac{(1/6)_n(1/3)_n}{2^n(n!)^2},\quad
S_p=\sum_{n=0}^{p-1}d_n,\quad T_p=\sum_{n=0}^{p-1}n d_n.
]
Since `1/6≡-m` and `1/3≡-2m` (modp), and the factors `(1/6)_n` first hit p for n=m+1,
[
\boxed{
d_n\equiv \binom mn\binom{2m}n 2^{-n}\pmod p\quad(0\le n\le m),\qquad
d_n\equiv0\quad(m<n<p).}
]
Define `F_m(z)=sum_{n=0}^{m}binom(m,n)binom(2m,n)z^n` in `F_p[z]`; then
[
\boxed{ S_p\equiv F_m(1/2)
=[x^m](1+x)^{2m}(x+1/2)^m\pmod p},
\qquad T_p\equiv\theta F_m(1/2)\pmod p,
]
where `theta=z*d/dz`. The coefficient extraction follows by expanding both factors and choosing degree m. The *terminating* polynomial also satisfies the formal second-order exact relation
[
\boxed{\theta^2F_m=z(\theta-m)(\theta-2m)F_m}\quad\text{in }\mathbb F_p[z]
]
because adjacent coefficients obey `(n+1)^2 C_{n+1}=(n-m)(n-2m)C_n` with end term zero at n=m. This turns the **observed**, not yet proved, p|S_p first-digit condition for target p=13/19 mod24 into one sharply defined finite-field polynomial evaluation `F_m(1/2)=0`. The polynomial's independent derivative observer `F_m+12 theta F_m` must be retained: zero of product is not proof of zero of a selected factor.

## II. Finite complementary reflection as a single-pass prefix recurrence

Recall the proved signed triangular boundary
[
J_p=\sum_{1\le r\le i\le m}
(1+6(i-r))d_i e_r\pmod p,
\qquad
e_r=\frac{36^{r-1}[(r-1)!]^2}{\prod_{s=1}^r(1-6s)(1-3s)}
\quad(1\le r\le m).
]
Here denominator factors are nonzero modulo p in this exact range. Taking ratios gives the exact mod-p recurrence
[
\boxed{e_1=1/10,\qquad
e_{r+1}=e_r\frac{36r^2}{(6r+5)(3r+2)}
\quad(1\le r<m).}
]
Let `E_i=sum_{r=1}^i e_r`, `R_i=sum_{r=1}^i r e_r`. Reordering the **finite, labelled** sum without collapsing the low/high source yields:
[
\boxed{
J_p=\sum_{i=1}^m d_i\bigl[(1+6i)E_i-6R_i\bigr]\pmod p.
}
]
The original d_i follow `d_0=1` and `d_{i+1}=d_i(6i+1)(3i+1)/[36(i+1)^2]`. Thus e_i,E_i,R_i,d_i,J_i are updated in **one forward pass**, using O(m) finite-field ring updates and constant current-state storage; each inverse computed separately by modular powering costs O(logp) modular operations, or inverses can be batch-computed with one inverse and O(m) extra ring updates. This is an *algorithmic evaluation reduction for the known exact boundary*, not an asymptotic improvement for arbitrary sorting or proof of the supercongruence.

Retaining `E_i,R_i` is a faithful BRC joint-observer sufficient state for the **declared final J_p modulo p readout and sequential accumulation**; it keeps ordered low/high incidence and signed weights. It is not a certificate for modp⁴, individual branch reconstruction, or native Frobenius.

## III. Exact execution and scope

A separate Python-stdlib prefix evaluator (locally actually executed) matched the preceding quadratic double sum `J_p` and original `S_p (modp)` on **all 80 primes p=6m+1 with 7<=p<=997**, with zero assertion failures. Using the one-pass method, an additional **267 frozen-class primes** with 997<p<=10007 were checked: each had `S_p=0 modp`; largest tested p=9973 and its `J_p=2527 mod9973`. This remains bounded evidence, **NOT** a uniform theorem that S_p always vanishes.

At the two adversarial boundary inputs: `J_19=6 mod19` and `J_373=98 mod373`, so the true overflow `2p²J_p` is NONZERO. The earlier uncorrected full-square substitution demonstrably fails at p=19. The new one-pass evaluator preserves, rather than erases, this failure witness.

## IV. Next smallest research action and provenance

Investigate `F_m(1/2)` for all p=13,19 (mod24) using a genuine finite-field hypergeometric/Jacobi or certified modular method; an algebraic proof of its zero would permit division by p and expose the two-digit equation
[
\boxed{(S_p/p)(S_p+12T_p)\equiv1+2pJ_p\pmod{p^2}}
]
as the next open objective. The single-pass signed boundary is already available, including nonzero p=19/373 corrections. Do not repeat Guo–Zudilin 2304 tail, the completed 216 two-jets, or replace native p373 experiment with this polynomial.

Original benchmark support: https://github.com/awdawmip/enterprise-math/issues/1559, PENDING_OWNER / NOT_EXECUTED. Author-side materials can be reviewed but are not formal Source Result, independent Driver review, or project admission. No session, winning CLAIM, open or run asserted.
