# D25/LIFT — original 3F2 restored from terminating Clausen by a directional parameter jet

Date 2026-10-25; TASK_RESEARCH portable author derivation. Mother Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7. Frozen science Source pin c47e13e4aba0e006366f989d6334d443f6333ae3 unchanged. AUTHOR-DERIVED / AUTHOR-CHECKED / UNREVIEWED / NOT_ADMITTED / NO_NATIVE_CHECKPOINT.

## Exact theorem (all p=6m+1 >=7 prime)

Let theta=z d/dz. The **original** D25 cutoff 3F2 polynomial and weighted observer are
\[
A_p(z)=\sum_{n=0}^{p-1}\frac{(1/2)_n(1/3)_n(2/3)_n}{(n!)^3}z^n,\qquad
W_p=[(1+6\theta)A_p]_{z=1/2}.
\]
Consume the earlier proved deformed terminating Clausen polynomial
\[
T_p(z)={}_3F_2(-2m,-4m,-3m;1-p/2,1-p;z)
\]
of degree 2m. Define the full finite parameter family
\[
\mathcal T(\mathbf a;\mathbf d;z)=\sum_{n=0}^{p-1}
\frac{(a_1)_n(a_2)_n(a_3)_n}{(d_1)_n(d_2)_n\,n!}z^n
\]
with base \(\mathbf a^*=(-2m,-4m,-3m),\mathbf d^*=(1-p/2,1-p)\). Its p-local **directional derivative** is
\[
\mathfrak D=\frac13\partial_{a_1}+\frac23\partial_{a_2}
+\frac12\partial_{a_3}+\frac12\partial_{d_1}+\partial_{d_2},
\quad D_p=\left.\mathfrak D\mathcal T\right|_{\mathbf a^*,\mathbf d^*}.
\]
All denominator factors are p-units through n<p.

**A (full original source, including high ranks):**
\[
\boxed{A_p(z)\equiv T_p(z)+pD_p(z)\pmod{p^2}}
\]
coefficientwise. No high original ranks are discarded.

**B (source-tail structure):** T_p has degree 2m. D_p has degree exactly 3m; for 2m<n<=3m,
\[
\boxed{
[z^n]D_p=
\frac{(2m)!(n-2m-1)!\,(-4m)_n(-3m)_n}
{3(1-p/2)_n(1-p)_n\,n!},
}
\]
a p-unit. For n>3m, [z^n]D_p=0. Hence the true original 3F2 coefficients in 2m<n<=3m have valuation exactly one, recovered as \(p[z^n]D_p\pmod{p^2}\); above 3m they have valuation >=2. This exposes the rank branch falsely suppressed by a terminating-only reduction.

**C (original weighted Clausen/Jacobi bridge):** Let
\[
U_p={}_2F_1(-m,-2m;1;z),\quad
\mathcal H_p(z)=\sum_{n=0}^m[z^n]U_p\,H_nz^n.
\]
The separately proved Clausen resonance identity is \(T_p\equiv U_p^2+pU_p\mathcal H_p\pmod{p^2}\). Thus
\[
\boxed{W_p\equiv [(1+6\theta)U_p^2]_{1/2}
+p[(1+6\theta)(U_p\mathcal H_p+D_p)]_{1/2}\pmod{p^2}.}
\]

For target inert primes p=13,19 (mod24), consume the previously independently accepted first-digit input p|U_p(1/2). Define \(u_p=U_p(1/2)/p\), \(a_p=(\theta U_p)(1/2)\), \(h_p=\mathcal H_p(1/2)\), \(d_p=[(1+6\theta)D_p]_{1/2}\). Then
\[
\boxed{W_p/p\equiv12u_pa_p+6a_ph_p+d_p\pmod p.}
\]
Consequently the already accepted W_p≡p mod p² is equivalent to \(12u_pa_p+6a_ph_p+d_p=1\pmod p\). This is a source-preserving **reduction**, not a new all-prime proof of this first digit, and not completion of the next-digit D25/LIFT.

## Proof

The target parameters are exactly
\((1/3,2/3,1/2;1,1)
=(\mathbf a^*+p(1/3,2/3,1/2);\mathbf d^*+p(1/2,1))\).
For n<p, all lower Pochhammer denominators are p-units at both the base and target. The first-order Taylor expansion in this direction in Z_(p) proves A with legitimate differentiation of reciprocal denominators (including their signs).

For n>2m, (-2m)_n has exactly one simple zero at j=2m, and its derivative equals (2m)!(n-2m-1)!. Thus only the (1/3)∂_(a1) component survives in D. For n>3m the second distinct top factor (-3m)_n has a zero too; one directional derivative cannot remove both, so D vanishes. For 2m<n<=3m all displayed factors after removing the first zero are p-units, proving B including exact valuation. The original numerator crosses its second p-zero only after n=3m.

The declared signed observer 1+6theta acts coefficientwise before evaluation at z=1/2, so A and the earlier resonant T=U²+pU H immediately give C. At the inert point p|U, the square observer contributes 12U theta U modulo p² and the product U H contributes 6p(theta U)H modulo p²; dividing by p proves the displayed three-port first-digit formula. No pth-power point substitution was made before theta. QED.

## Evidence, BRC, and continued objective

The adjacent independent standard-library modular checker computes (i) the actual source 3F2 coefficients to rank p-1, (ii) a dual-number directional derivative of the p-deformed Clausen coefficient recurrence, and (iii) separate terminating Jacobi U/H coefficients. It verifies the bridge at **every original rank modulo p²**, both support/valuation claims, and original and weighted source identities. PASS for all 35 p=1(mod6), 7<=p<=373, plus1327,19963 (37 cases). Target arithmetic: p=13: W_p=13, OT=156, OD mod13=2; p=19: (19,57,17); p=373: (373,132415,? computed from checker). These are author checks, not independent review or native CM experiments. The general statement follows from the p-local Taylor derivation.

BRC COMPOSE_APPLIED: the source rank, zero-factor positions, signs, valuations, parameter direction, reflected/weighted observer and algebraic distinction between source and readout are preserved. The first derivative repairs the terminating polynomial's precise first missing p-adic digit; it is not a substitute for the original CM H0/B0, [X]U modp², Frobenius normalization, kappa, or a native execution claim.

Next smallest unit: lift the exact parameter translation to p³, retaining the second directional jet and the two-top-zero ranks 3m<n<=4m. Compare the next signed original W_p digit and reflected cutoff with a non-tautological all-target-prime telescoper. D25/LIFT/JT2 remains OPEN; Source authority not restored (exact continuation CONTROL_QUOTA), Issue #1558 pending; frozen science pin and contributor history preserved. No scheduler or notification changes.
