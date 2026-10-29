# D25 / SECOND-DIGIT-LIFT — finite p² Legendre parameter-jet transport at unchanged argument

**2026-10-29 · AUTHOR-SIDE / EXACT COEFFICIENTWISE DERIVATION / EXECUTED INTEGER CHECK / UNREVIEWED / NOT_ADMITTED / NATIVE_H0_B0_NOT_EXECUTED.**

Mother: ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION. Exact Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7. Frozen scientific Source pin c47e13e4aba0e006366f989d6334d443f6333ae3 (unchanged). Research ordinary-control conversation chatgpt-research-onhour-enterprise-math-20260923, not CONTROL_PLANE_MAINTENANCE. Antecedent Jacobi/Hensel author-side commit 243cdc6ce8e061ec371426bfb650fff0eae8d629.

## Theorem A (every prime p>3)

Let h_q be the smallest nonnegative integer n such that p divides 8n+q (q=1,3), and put r=min(h_1,h_3), b=max(h_1,h_3). Let lambda=1 for p=1,3 mod8 and lambda=5 for p=5,7 mod8; let q=1 for p=1,5 mod8, and q=3 for p=3,7 mod8. Then

r=(lambda*p-q)/8,  r<b<p,  and  b+r+1/2 is divisible by p in Z_(p).

For a p-integral polynomial coefficient define

\[
c_n(a)=\frac{(a)_n(1/2-a)_n}{(n!)^2},\quad
F_r(z)=\sum_{n=0}^{r}c_n(-r)z^n,\quad
G_{r,b}(z)=\sum_{n=0}^{b}c_n'(-r)z^n.
\]

For the ORIGINAL companion
\[
K_b(z)=\sum_{n=0}^{b}\frac{(1/8)_n(3/8)_n}{(n!)^2}z^n
\]
there is a **coefficientwise finite-polynomial congruence**
\[
\boxed{K_b(z)\equiv F_r(z)+\frac{\lambda p}{8}G_{r,b}(z)\pmod{p^2}.}
\]
The Euler/observer jet is retained:
\[
\boxed{\theta K_b(z)\equiv \theta F_r(z)+\frac{\lambda p}{8}\theta G_{r,b}(z)\pmod{p^2},\quad \theta=z\partial_z.}
\]

The *terminating* Gauss quadratic identity provides the exact finite identity
\[
\boxed{F_r(4t(1-t))=P_{2r}(1-2t),}
\]
where P_n is the ordinary classical Legendre polynomial. Hence at the **unchanged source argument** z=1/9, where (1-2t)^2=8/9,
\[
\boxed{K_b(1/9)\equiv P_{2r}(\sqrt{8/9})+\frac{\lambda p}{8}G_{r,b}(1/9)\pmod{p^2}.}
\]
The even Legendre polynomial evaluation is defined algebraically by x²=8/9: no choice of a p-adic square-root or moving CM parameter is needed. The second term is the source-preserving parameter derivative, not the Hasse Hensel-shift term.

**Proof.** The unordered original parameters are a=-r+delta and 1/2-a=r+1/2-delta, with delta=lambda*p/8, because a=q/8. For n<=b<p, the finite numerator product c_n(a) is p-integral: n! and 2 are p-units. Taylor expansion at the EXACT terminating index a=-r gives
\[
c_n(-r+\delta)\equiv c_n(-r)+\delta c_n'(-r)\pmod{p^2},
\]
as the omitted second-order difference has a factor delta². For n>r the first base factor (-r)_n vanishes exactly. For n>b, both original numerator rising factorials have acquired p factors, while c_n'(-r) contains the partner numerator p factor; thus beyond b the original coefficient and delta*c_n'(-r) vanish modulo p². Coefficientwise differentiation by theta preserves the congruence. The classical quadratic identity follows either by the terminating Gauss transformation or by matching the hypergeometric ODE and the value at z=0.

For explicit finite computation put f_n=c_n(-r), g_n=c_n'(-r). For n<=r,
\[
g_n=f_n\sum_{j=0}^{n-1}\left(\frac{1}{j-r}-\frac{1}{j+r+1/2}\right).
\]
For r<n<=b, differentiating the sole zero factor gives
\[
g_n=(-1)^r\,\frac{r!(n-r-1)!(r+1/2)_n}{(n!)^2}.
\]

## Theorem B — inhomogeneous Picard–Fuchs boundary closure

Let
\[
L_r=z(1-z)\partial_z^2+(1-3z/2)\partial_z+r(r+1/2).
\]
The finite source derivative satisfies **as a polynomial modulo p**
\[
\boxed{L_rG_{r,b}(z)\equiv (2r+1/2)F_r(z)\pmod p.}
\]

Proof: differentiating the exact finite hypergeometric coefficient recurrence gives
\[
(n+1)^2g_{n+1}=(n-r)(n+r+1/2)g_n+(2r+1/2)f_n.
\]
For n<b this is precisely the L_r coefficient equation. At n=b the truncated boundary is -(b-r)(b+r+1/2)g_b; the partner numerator hit makes it zero modulo p. Above b both ports vanish modulo p. This checks the boundary rather than commuting differentiation and premature truncation. As (n+1)² are p-units below degree p, the initial condition g_0=0 uniquely specifies the degree-<p polynomial source jet in F_p[z].

An exact residue-class distinction follows:
\[
\boxed{2r+1/2\equiv
\begin{cases}
+1/4 \pmod p& (p\equiv1,5\bmod8),\\
-1/4 \pmod p& (p\equiv3,7\bmod8).
\end{cases}}
\]
Therefore the two finite Root2 observation classes 13 and 23 mod24 have **opposite forcing signs**, even though both have lambda=5. This is a theorem about the signed source jet; it is not a claim that either infinite Root2 congruence has been proved.

## Executed exact evidence

Actual checker: research_notes/portable_direct/d25_fixed_arg_legendre_parameter_jet_guard_20261029.py, same-day commit 11d628968b26cf3549dd9cd19c32324c52fa4fdf; exact code blob bc58b76f0710e145430ba8325388a696557b3c9b. It executes all **194 primes 5<=p<1200**, checking original coefficient transport mod p² up to n=p-1, Euler jet mod p², and full Picard–Fuchs coefficient boundaries mod p. Independent binomial evaluation of the even Legendre polynomial cross-checks p=13,17,19,23,37,61,373. It uses no floating-point arithmetic and is not native H0/B0.

| p | (r,b) | F_r(1/9) mod p² | (lambda*p/8)G mod p² | original K mod p² | theta K mod p² |
| ---:|:---:|---:|---:|---:|---:|
| 13 | (8,11) | 117 | 52 | 0 | 167 |
| 17 | (2,6) | 17 | 238 | 255 | 93 |
| 19 | (2,7) | 342 | 190 | 171 | 178 |
| 23 | (14,20) | 161 | 368 | 0 | 445 |
| 37 | (23,32) | 1073 | 296 | 0 | 442 |
| 61 | (38,53) | 2867 | 854 | 0 | 770 |
| 373 | (233,326) | 92131=247p | 46998=126p | 0 | 102580 |

At p=373 the distinct p-adic sources exactly cancel: 247p+126p=p². At p=23: 7p+16p=p². These are finite certificates, not all-prime Root2 proofs.

## Scope, method and next obligation

**BRC COMPOSE_APPLIED**: carrier (p, numerator-hit type q, lambda, r, b, finite original coefficients, terminating coefficients f_n, parameter derivatives g_n, theta jets, delta, valuation and ordered operations). Do not collapse signed p-order ports before differentiation, CM base-change or higher precision. The external Legendre coordinate t is not a P000-native two-dimensional plane. P000 and ACTIVE worldview stay unchanged.

**New resolved mathematical unit**: a genuine fixed-argument finite p² quadratic transport with an explicit parameter-source correction and fully closed inhomogeneous differential boundary. **Unresolved**: for all p≡13 mod24 (and separately 23 mod24) prove
\[
P_{2r}(\sqrt{8/9})/p+(\lambda/8)G_{r,b}(1/9)\equiv0\pmod p,
\]
using the earlier independently established first-digit divisibility; connect this direct source jet with the external Hasse 13-class rank-line and the 216/2304 third-digit bridge without replacing original cutoffs. The finite checks do not discharge this.

**Native first-priority evidence unchanged**: Enterprise Math Issue #1559, OPEN/PENDING_OWNER at 2026-10-29 read time, fixed 373 same-original-class H0/B0 divided-power [X]U mod139129, module rank, semilinear Frobenius/eta, signed Green/Hesse, kappa, Delta_p-R_p. This work does not execute or close that native benchmark.

**Authorization/recovery**: gateway 0.6.11 Site verified static read-only, research_authority_granted=false; no Site Researcher write relay or actual session/CLAIM/run/target_request_id confirmed; the callable recovery_status endpoint was not exposed by available tools. No inferred empty queue, no fresh dispatch, claim, checkpoint, formal Result, freeze or review. Original Research/maintenance identity separation and frozen scientific Source pin persist. Formal Source entry requires genuine authorized writer and exact continuation/receipt reconciliation. Existing scheduled task configuration was not altered.
