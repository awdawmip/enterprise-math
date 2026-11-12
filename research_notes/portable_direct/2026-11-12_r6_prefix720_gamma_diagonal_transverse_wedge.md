# PREFIX-720-R6 — exact local transverse elimination around a frozen Gamma-clock diagonal point

Date: 2026-11-12 (Asia/Shanghai). Parent: PREFIX-675. Immediate antecedent: PREFIX-719. Frozen science: \`awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d\`. Mode: independent auxiliary BRC statistical observer, not a native X6 spatial plane. Evidence: AUTHOR_EXACT_INTEGER_CHECKED / UNREVIEWED / NOT_ADMITTED.

## Question and advance beyond PREFIX-719

PREFIX-719 gave a diagonal stationary-maximizer interval \((43/384,91/768)\) for each \(q\ge2\) and finite pointwise off-diagonal signs \(J(p,z)>0\) at 120 predeclared pairs. These point tests alone did not establish any open two-parameter region where off-diagonal stationary points are excluded.

Here the new test is a *transverse diagonal derivative*, computed with the exact frozen Gamma moment and second-survivor derivatives at \(x_0=11/96=88/768\), strictly inside the PREFIX-719 interval. The test proves both \(J_z(x_0,x_0)>0\) and \(\Theta'(x_0)<0\). Algebraic antisymmetry then upgrades one exact rational test to a genuinely open, but non-effectively sized, neighborhood.

## Definitions and exact two-clock kernel

Let \(D=[0,\tfrac12]^2\). Let \(N_p\) be the original frozen 189-level stopping count, with \(s_n(p)=\Pr(N_p>n)\), \(0\le n\le188\). Conditional on \(N_p=k\), let \(T_p\sim\mathrm{Gamma}(k,1)\), with two independent clocks; put \(Y(p,z)=\max(T_p,T_z)\).

Set \(\mu=E[Y]\), \(M_2=E[Y^2]\), \(W=M_2-\mu^2\), \(f_t=W-t\mu\), \(t=1/q\). The exact Gamma survivor kernel from PREFIX-719 is
\[
 C_{nm}=\frac{\binom{n+m}{n}}{2^{n+m+1}}.
\]
It gives finite rational-polynomial moment expressions
\[
\begin{aligned}
\mu(p,z)&=\sum_n[s_n(p)+s_n(z)]-\sum_{n,m}C_{nm}s_n(p)s_m(z),\\
M_2(p,z)&=2\sum_n(n+1)[s_n(p)+s_n(z)]
-\sum_{n,m}(n+m+1)C_{nm}s_n(p)s_m(z).
\end{aligned}
\]
Use
\[
 A_n(z)=1-\sum_m C_{nm}s_m(z),\qquad
 H_n(z)=2(n+1)-\sum_m(n+m+1)C_{nm}s_m(z).
\]
The previously certified nonnegative survivor derivatives and strictly positive coordinate influence imply \(\mu_p,\mu_z>0\) in the open parameter square. Exact derivatives are
\[
\begin{array}{ll}
\mu_p=\sum_n s'_n(p) A_n(z),&
(M_2)_p=\sum_n s'_n(p)H_n(z),\\
\mu_{pp}=\sum_n s''_n(p) A_n(z),&
(M_2)_{pp}=\sum_n s''_n(p)H_n(z),\\
\mu_{pz}=-\sum_{n,m}C_{nm}s'_n(p)s'_m(z),&
(M_2)_{pz}=-\sum_{n,m}(n+m+1)C_{nm}s'_n(p)s'_m(z).
\end{array}
\]

## New theorem: nonempty open off-diagonal stationary-free wedge

Define
\[
 J(p,z)=\mu_p(M_2)_z-\mu_z(M_2)_p,\quad
 R_p=(M_2)_p/\mu_p,\quad \Theta(x)=R_p(x,x)-2\mu(x,x).
\]

**Theorem (local transverse exclusion and local diagonal uniqueness).** In the frozen model there exists an \(\varepsilon>0\), not yet explicitly bounded, such that:

1. Whenever \(|p-x_0|<\varepsilon\), \(|z-x_0|<\varepsilon\), and \(p<z\), one has \(J(p,z)>0\). For \(p>z\), one has \(J(p,z)<0\). In particular no off-diagonal interior point in this square is a stationary point of \(V_q=q^2 f_{1/q}\), for any real \(q>0\).
2. On the diagonal interval \((x_0-\varepsilon,x_0+\varepsilon)\), the function \(\Theta\) is strictly decreasing. Hence for any \(q>0\) there is **at most one** diagonal stationary point in that interval, and any such point is a strict local maximizer of \(x\mapsto V_q(x,x)\).

**Proof.** The exact moment polynomials are symmetric under clock exchange, so \(J(z,p)=-J(p,z)\). As a rational-coefficient polynomial it has the exact factorization \(J(p,z)=(z-p)K(p,z)\) for a symmetric polynomial \(K\); at a diagonal point \(K(x,x)=\partial_z J(x,x)\). Differentiating \(J\) and using clock symmetry yields
\[
 J_z(x,x)=\mu_p[(M_2)_{pp}-(M_2)_{pz}]
 -(M_2)_p[\mu_{pp}-\mu_{pz}]
\]
with all derivatives evaluated at \((x,x)\). The finite exact certificate below gives \(J_z(x_0,x_0)>0\). By continuity, \(K>0\) throughout a sufficiently small open square about \((x_0,x_0)\), which proves the sign statements. Moreover,
\[
 \nabla f_t=
 \big(\mu_p(R_p-2\mu-t),\,\mu_z(R_z-2\mu-t)\big).
\]
An interior stationary point would require \(R_p=R_z\), hence \(J=\mu_p\mu_z(R_z-R_p)=0\); therefore the off-diagonal portion of that square has no stationary point.

On the diagonal,
\[
 \Theta'(x)=
 \frac{\mu_p[(M_2)_{pp}+(M_2)_{pz}]
 -(M_2)_p[\mu_{pp}+\mu_{pz}]}{\mu_p^2}-4\mu_p.
\]
The same integer certificate gives \(\Theta'(x_0)<0\). Continuity makes \(\Theta'<0\) in some interval about \(x_0\). Since \(d f_t(x,x)/dx=2\mu_p(x,x)(\Theta(x)-t)\), any zero of the derivative in that interval is unique and changes sign from positive to negative; it is a strict local maximum. Take the smaller of the two neighborhoods. \(\square\)

## Fully specified finite exact certificate

The companion checker reconstructs the original 189 rows with the frozen width predicate, proves exactly 9,529 nonzero row coefficients, and evaluates at \(i=88\), \(D_0=768\), \(L=D_0^{188}\), \(Z=2^{377}\). Write the integer numerators \(a_n=LZ\,A_n(x_0)\), \(h_n=LZ\,H_n(x_0)\), \(d_n=L\,s'_n(x_0)\), and \(e_n=L\,s''_n(x_0)\).

Define integers
\[
 P=\sum_n d_n a_n,\quad Q=\sum_n d_n h_n,\quad
 PP=\sum_n e_n a_n,\quad QQ=\sum_n e_n h_n,
\]
and
\[
 C_0=\sum_{n,m}d_nd_m\,\binom{n+m}{n}2^{376-n-m},\qquad
 C_1=\sum_{n,m}(n+m+1)d_nd_m\,\binom{n+m}{n}2^{376-n-m}.
\]
The exact common denominator for first and second moment partials is \(L^2Z\), with \(\mu_p=P/(L^2Z)\), \((M_2)_p=Q/(L^2Z)\), \(\mu_{pp}=PP/(L^2Z)\), \(\mu_{pz}=-C_0/(L^2Z)\), and analogous second-moment expressions.

The checked integer inequalities are
\[
 \boxed{P(QQ+C_1)-Q(PP+C_0)>0}
\]
and
\[
 \boxed{\bigl[P(QQ-C_1)-Q(PP-C_0)\bigr]L^2Z-4P^3<0}.
\]
The first numerator has 2,405 decimal digits. Its SHA-256 over the plain decimal integer string is \`f9eab864317b8b68e16940ed539733265725445e8108de8c7075d4d18adc95d2\`. The second numerator's string SHA-256 is \`c3cb0b08933d50689c97613e80cc6b53820dc8820e1c7f084cb6ec64e6d0e0b1\`. Those digests are reproduction identifiers, **not** substitutes for the executed exact integer sign comparisons.

The local self-contained Python execution of the same 189-row/second-derivative arithmetic confirmed both signs and persisted \`PREFIX720_R6_TRANSVERSE_J_RESULTS.json\` in the local scratch area. A repository checker reuses exactly the existing PREFIX-719 frozen-row implementation and has its own output file \`PREFIX720_R6_RESULTS.json\`. The latter is supplied as a corresponding JSON artifact; no GitHub CI execution or independent proof review is claimed.

## Scope, relation to the parent objective and next discriminating unit

This is a new *local continuum* stationary-elimination statement, not a quantified exclusion area, not a full-square sign proof, and not a proof of the global maximum. It relies on PREFIX-705 survivor monotonicity and the correct PREFIX-710 Gamma maximum, not the invalid stopping-count maximum of PREFIX-709. The previous PREFIX-718 author-level certified exclusion fraction \(139018/147456\) is inherited without additional area.

Next mathematical unit: obtain an **explicit rational \(\varepsilon\)** with interval/Bernstein bounds on \(K(p,z)=J(p,z)/(z-p)\) and on \(-\Theta'(x)\), starting around \(x_0=11/96\), then extend the sign-safe wedge toward the surviving candidate cells. Alternatively find a genuine off-diagonal zero of \(K\) and preserve its exact counterexample. The q-uniform full-square optimizer in PREFIX-675 remains open.

Control: native session issuance for this run returned \`SESSION_ISSUANCE_QUOTA\`; a fresh Source dispatch selected a different task. No claim/owner takeover is made; this independent research artifact is not a formally admitted task Result/Review. Historical research activity identifiers are only provenance, not current execution authentication.
