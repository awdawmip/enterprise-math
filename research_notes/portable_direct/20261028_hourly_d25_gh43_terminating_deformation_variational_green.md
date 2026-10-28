# D25/LIFT GH-43: exact terminating reverse-Gauss deformation and forced first variation

2026-10-28, TASK_RESEARCH author-side proof and exact finite-field check. AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING. Parent ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION OPEN; Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; immutable publication TP2-B6F4FC938FF94941C1B7. Frozen scientific Source pin c47e13e4aba0e006366f989d6334d443f6333ae3 unchanged. GH-40 and new GH-41/GH-42 are precise author-side inputs. No official CLAIM, run, checkpoint, formal proof or independent review is asserted.

## GH-43: theorem and algebraic proof

Let p=4d+3>=7 be prime, a_r and beta_r the rational Gauss and reverse-Gauss coefficients in GH-41/GH-42. Set D=u d/du. Define the *actual*, rationally reversed forward polynomial

\[
\Gamma_d(u)=\frac{u^d B_d(u^{-1})}{a_d}
=\sum_{r=0}^{d}\frac{a_{d-r}}{a_d}u^r.
\]

**Exact terminating parameter deformation.** The backward coefficient ratio gives

\[
\frac{a_{d-r-1}}{a_{d-r}}=
\frac{(r+1-p/4)(r+3/4-p/4)}{(r+13/8-p/4)^2}.
\]

Therefore, as a polynomial over Q,

\[
\boxed{\Gamma_d(u)={}_3F_2\left(\begin{matrix}
1,\ 1-p/4,\ 3/4-p/4\\
13/8-p/4,\ 13/8-p/4
\end{matrix};u\right).}\tag{43.1}
\]

There is no infinite-series convergence assumption: 3/4-p/4=-d is an exact negative integer, so the series terminates at r=d. Its denominator Pochhammer factors do not vanish before the termination.

Define the parameter-shifted third-order operator

\[
\mathcal L_p=D(D+5/8-p/4)^2
-u(D+1)(D+1-p/4)(D+3/4-p/4).
\]

Coefficient matching through degree d and cancellation of the degree-d+1 coefficient by d+3/4-p/4=0 prove **exactly**

\[
\boxed{\mathcal L_p\Gamma_d=0\quad\text{over }\mathbf Q[u].}\tag{43.2}
\]

**Forced harmonic first variation.** Let H_r be GH-42's source-preserving first p-adic reverse-jet and put \(U_d(u)=\sum_{r=0}^d\beta_rH_ru^r\in\mathbf F_p[u]\). GH-42 gives

\[
\Gamma_d\equiv V_d+pU_d\pmod{p^2}.
\]

Expand the operator as \(\mathcal L_p\equiv\mathcal L_0+p\mathcal L_1\pmod{p^2}\), with

\[
\mathcal L_0=D(D+5/8)^2-u(D+1)^2(D+3/4),\qquad
\mathcal L_1=-\frac12 D(D+5/8)+\frac14u(D+1)(2D+7/4).
\]

The *unshifted* finite polynomial V_d has GH-41's exact boundary
\(\mathcal L_0 V_d=-p(d+1)^2\beta_du^{d+1}/4\). Substitute the two expansions into the exact identity (43.2), divide the coefficientwise equality by p and reduce modulo p. This yields the **nonhomogeneous tangent equation**

\[
\boxed{\mathcal L_0U_d+\mathcal L_1V_d
=\frac{(d+1)^2\beta_d}{4}u^{d+1}
\quad\text{in }\mathbf F_p[u].}\tag{43.3}
\]

The right-hand coefficient is nonzero: d+1 and beta_d are p-units. For 1<=n<=d, the leading coefficient for U_n in [u^n] L_0 U is \(n(n+5/8)^2\), also a p-unit since 8n+5=p would force p=5 mod 8. With U_0=0, the first-variation polynomial of degree <=d is *uniquely determined* by this inhomogeneous recurrence, and its degree-d+1 equality is an exact separate consistency check. The apparent rank-three homogeneous equation for V modulo p cannot be lifted by deleting the nonzero source at order p.

**Typed observer link.** GH-42's ordered-pair weighted first-jet moment J satisfies

\[
\boxed{J(u)=(8D+11)[2V_d(u)U_d(u)]_{<d}.}\tag{43.4}
\]

Indeed, its coefficient at degree r<d before weighting is
\(2\sum_{i+j=r}\beta_i\beta_jH_i
=\sum_{i+j=r}\beta_i\beta_j(H_i+H_j)\).
Truncation at degree <d occurs *before* evaluation at u=1/9. Thus a one-variable variational differential computation can recover the separately required J observer; it does not determine the special value W(1/9) or prove the original T_d(9)=0.

## Executed exact tests and scope

Companion checker: research_notes/portable_direct/20261028_hourly_d25_gh43_gauss_variational_check.py. Author-side execution used exact modular inverses to check (43.2) over Z/p^2 and (43.3) coefficientwise over F_p for **all 154** primes 7<=p<2000, p=3 mod4. Both passed. Examples of the nonzero degree-d+1 tangent coefficient: p=19 gives 16, p=43 gives 6, p=67 gives 55. Executed program's exact Git blob SHA-1: f7f939a97aa0c9de3bc65b4de8a385de83594589. Finite computation is not a universal proof or mathematical admission; the stated general theorem follows from explicit rational hypergeometric recurrences.

BRC COMPOSE_APPLIED: preserve reverse-index source labels, exact signed rational/mod-p^2 weights, harmonic tangent, truncation rank and future derivative/weighted observer. Dropping U while retaining only V erases a measurable first-order source, as (43.3) witnesses. This auxiliary arithmetic model is not a P000 X6 native embedding or independent eta/kappa evidence.

**Next exact scientific action:** use parameter-deformed Gamma_d at u=1/9 to seek an *independent* finite-field, CM/Frobenius or nonlocal WZ special-value certificate, or relate its tangent to the separately retained GH-20/GH-21 p-adic source moments. Do not recombine the same high-tail convolution and call T=T a proof. Parent GH-3, original W/S, six Hasse ports, [X]U mod p^2, R23/R36, native p=373, and independent Driver assessment remain open.
