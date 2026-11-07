# D25: Gauss monodromy obstruction and exact quadratic p-adic first jets (2026-11-07)

**Status:** AUTHOR_SIDE_PROVED / EXACT_FINITE_CHECKED / UNREVIEWED / NOT_ADMITTED. This is not a Source Result, a native p=373 benchmark, or independent mathematical review.

Research logical lane: \`chatgpt-research-onhour-enterprise-math-20260923\`, never the separate CONTROL_PLANE_MAINTENANCE lane.
Mother Task \`RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT\`, publication \`TP2-B6F4FC938FF94941C1B7\`, immutable frozen scientific pin \`c47e13e4aba0e006366f989d6334d443f6333ae3\`.
Consumed previous author-side frontier: \`20261107_onhour_d25_heun_period_gate_signed_jet.md\` at commit \`4020b5d8be7d1bfb8f9673d65f2331407609c476\`; its fixed-band obstruction, exact p=19 scalar non-transfer, analytic period candidate, and earlier p4 signed-tail formulas are not repeated.

## Theorem A (proved): no one-legged rational pullback of the full Gauss equations

Define
\[
F_A(z)={}_2F_1(1/6,1/3;1;z),\qquad F_B(w)={}_2F_1(1/8,3/8;1;w).
\]
Their squares at \(z=1/2\) and \(w=1/9\) yield the unweighted 216 and 2304 hypergeometric periods by Clausen's identity.

**Exact scope.** No nonconstant rational map \(\phi\) and nonzero algebraic *scalar gauge* \(\lambda\) carry the entire rank-two Gauss differential equation of \(F_A\) into that of \(F_B\), or vice versa, via a single pullback \(z=\phi(w)\), \(Y\mapsto\lambda Y\). The theorem does **not** prohibit a special-value period equality, a two-legged Heun/modular correspondence, a nonlocal integral transform or the finite-sum p4 conjecture.

**Proof.** The Gauss equation
\[
z(1-z)y''+[c-(a+b+1)z]y'-ab\,y=0
\]
has local exponent differences \((1-c,c-a-b,b-a)\) at \(0,1,\infty\). For \(F_A\) they are \((0,1/2,1/6)\); for \(F_B\), \((0,1/2,1/4)\). Thus finite local **projective** monodromy orders of the rank-two equations are \(2,6\) for A and \(2,4\) for B. The zero exponent difference singularity at zero is logarithmic, giving infinite-order projective monodromy.

At any preimage of a singularity under a rational map with ramification index \(e\), pulled-back projective local monodromy is conjugate to the original monodromy raised to the \(e\)-th power. Therefore its finite order divides the original finite local order. A point over an ordinary point has projectively trivial local monodromy. A scalar algebraic gauge has no effect on projective monodromy. Pulling back A cannot create order 4, which B requires; pulling back B cannot create order 6, which A requires. Hence neither direct full-equation pullback exists. QED.

**Positive replacement route (conditional).** For a common two-legged *orbifold-unramified covering*, if one exists, the triangle-orbifold Euler characteristics are
\(\chi_A=1/6+1/2-1=-1/3\) and \(\chi_B=1/4+1/2-1=-1/4\). If the two cover degrees are \(d_A,d_B\), multiplicativity gives \(d_A\chi_A=d_B\chi_B\), hence \(4d_A=3d_B\) and \((d_A,d_B)=(3h,4h)\). These are necessary degrees in this particular covering class, **not** an existence or minimality assertion. A point of residual order 2 over the A order-6 vertex needs ramification \(e\equiv3\pmod6\); over the B order-4 vertex, \(e\equiv2\pmod4\). This supplies concrete branching and degree filters for a two-legged Heun correspondence.

## Theorem B (proved with exact finite arithmetic): necessary first quadratic jet

Let
\[
a_k=\binom{2k}{k}^2\binom{3k}{k}216^{-k},\qquad
b_k=\binom{2k}{k}^2\binom{4k}{2k}2304^{-k},
\]
and define, with reductions modulo \(p^3\),
\[
A_p=\sum_{k=0}^{p-1}a_k,\quad B_p=\sum_{k=0}^{p-1}b_k,\quad
D_{B,p}=\sum_{k=0}^{p-1}k\,b_k.
\]
Here \(D_{B,p}\) is the logarithmic derivative of the B generating series at the fixed argument \(1/9\).

For \(p=19\) and \(373\), \((2/p)=-1\), and let \(E_p=\mathbb F_p[s]/(s^2-2)\). The analytic candidate's scalar is \(\rho=3s/4\). In both examples \(A_p,B_p\) are divisible by \(p^2\), while \(D_{B,p}/p\) is a nonzero residue. Therefore the relation
\[
 A_p\equiv \rho B_p+p\,\mu_p D_{B,p}\pmod{p^3}
\]
has a **unique necessary** \(\mu_p\in E_p\), namely
\[
\mu_p=
 \frac{(A_p/p^2)-(3s/4)(B_p/p^2)}{D_{B,p}/p}\pmod p.
\]
Integer computation gives:

| p | \(A_p\bmod p^3\) | \(B_p\bmod p^3\) | \(D_{B,p}\bmod p^3\) | \((A_p/p^2,B_p/p^2,D_{B,p}/p)\bmod p\) | \(\mu_p\) |
|---:|---:|---:|---:|---|---|
|19|2888|2527|3116|(8,7,12)|\(7+15s\)|
|373|9878159|28243187|35390986|(71,203,140)|\(195+274s\)|

These values are exact residues, checked by two independent algorithms in \`d25_two_leg_monodromy_jet_check_20261107.py\`. In particular the \(s\) component is nonzero: **a base-field coefficient in \(\mathbb F_p\) multiplying \(pD_{B,p}\) cannot repair the naive period scalar at either prime**. An extension-field coefficient is possible and the above first-digit value is necessary. This is not a globally derived Gauss/Heun jet, Frobenius result, or universal p-adic theorem.

The same checker independently computes the original weighted 216/2304 streams modulo \(p^4\) at 11,19,373 and verifies the previously proposed **conjectural** signed congruence for this finite set only; it also reconstructs the exact \(p=11\) failure at the fifth digit:
\[
2V_{11}-W_{11}+11\equiv6\cdot 11^4\not\equiv0\pmod{11^5}.
\]

## Relation to the frozen objective and next action

The mother target remains \(\Delta_p\equiv R_p\pmod p\) for \(p\equiv13,19\pmod{24}\), with the previously established bridge to \(W_p\equiv p\pmod{p^3}\). The independent author-side candidate
\[
2V_p-W_p-p\left(\frac{-3}{p}\right)\equiv0\pmod{p^4}
\]
is still **unproved** universally. The newly established monodromy obstruction narrows one approach; the two exact quadratic jets provide discriminating signed targets for the replacement. The next action is to build a two-legged Heun/modular correspondence, examine its differential/Frobenius action, and test whether its finite-index cutoff correction reduces to \(7+15s\) at 19 and \(195+274s\) at 373 while respecting the p=11 fifth-digit witness.

The BRC observer retains original source stream A/B, index \(k\), cutoff, coefficient-ring extension, denominator units, valuation, derivative/Frobenius and Wilson corrections separately until any justified quotient. No identity with the native six-axis Heartbeat World or promotion of P000 is asserted.

## Source and native experiment boundary

Original unclosed request: \`onhour11-20261106-1400-exact-research-lane-continuation\`, outcome UNKNOWN_NOT_RESENT. Fresh Site check 2026-11-07 04:59 UTC: CONFIGURED_NOT_LIVE_VERIFIED, research_authority_granted=false; the receipt and status return BACKEND_IDENTITY_OR_VERSION_MISMATCH with operation_sent=false. Service session, CLAIM and run have **not** been verified; research activity REGISTER_PENDING / SYNC_DEBT. Next real control action requires a dedicated Site-bound backend client with a reviewed compatible version and secure credential, then re-reading this original request's receipt and exact Source continuation before any role-bound mutation.

Original fixed p373 native H0/B0 divided-power, Frobenius, Hesse-kappa and independent reproduction remains separate: issue #1559 OPEN, NOT_EXECUTED. No portable finite-field substitute is offered as that experiment.

References: DLMF §15.10 for hypergeometric differential equations; Bostan et al., *Ising n-fold integrals as diagonals of rational functions and integrality of series expansions*, J. Phys. A 46 (2013) 185202, as inspiration only; immutable prior Enterprise Math artifacts as above.
