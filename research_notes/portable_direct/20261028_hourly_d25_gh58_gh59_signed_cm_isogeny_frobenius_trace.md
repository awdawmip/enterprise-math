# D25/LIFT GH-58–GH-59 — Signed CM two-isogeny and Frobenius traces (2026-10-28)

**Scope:** Author-derived / exact finite checks / unreviewed / not admitted / portable-only / register-pending. This is not a native Source CLAIM, OPEN, checkpoint, Result, independent review or admission. Research logical conversation: chatgpt-research-hourly-enterprise-math-20260923 (not the maintenance lane). Parent objective ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION remains OPEN. Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7. Frozen scientific Source pin c47e13e4aba0e006366f989d6334d443f6333ae3 **unchanged**.

## Exact prior inputs and typed scope

For a prime p=8m+3>=11, set n=2m=(p-3)/4 and D_m=binom(3m+1,m). Previous author research GH-32 established the CM(-24) elliptic family

\[
E_T:Y^2=f_T(X):=X^3-\frac32(3T+5)X-(9T+7),\quad
H_p(T)=[X^{p-1}]f_T(X)^{(p-1)/2},
\]

the polynomial identity \(P_n(T)=(-6/p)H_p(T)\) in F_p[T], and F-port vanishing precisely for p=19 mod24. GH-55 established \(D_mF_m(9)=9^mP_n(t)\) and \(D_mG_m(9)=9^m(tP_n'(t)-P_n(t))\), where \(t=2\sqrt2/3\), \(F_m(z)=\sum_{r=0}^m(-m)_r^2 z^r/((2m+2)_r r!)\), and \(G_m=(16z\partial_z+5)F_m\). The class-11 G-port assertion is still OPEN. GH-32 and GH-55 remain author results; their independent review/admission is not implied.

## GH-58: exact signed 2-isogeny (PROVED)

Assume characteristic not 2 or 3, T != ±1, and choose u with u²=-2. Set C_T=(9/2)(1-T). Translating x=X+2, y=Y gives

\[
E_T:\qquad y^2=x(x^2-6x+C_T). \tag{58.1}
\]

The discriminant is \(16C_T^2(36-4C_T)=5832(1-T)^2(1+T)\), nonzero. Thus (0,0) is a rational 2-torsion point for every such T.

The standard Vélu 2-isogeny with kernel {O,(0,0)} is

\[
q_T(x,y)=\big(x-6+C_T/x,\quad y(1-C_T/x^2)\big)
\]

onto \(E'_T:y'^2=x'(x'^2+12x'+4C_{-T})\). The exact rescaling \(x'=-2x_-\), \(y'=-2uy_-\) identifies E'_T with E_{-T}. Consequently

\[
\boxed{\psi_T(x,y)=\left(-\frac{x-6+C_T/x}{2},
-\frac{y(1-C_T/x^2)}{2u}\right):
E_T\longrightarrow E_{-T}.} \tag{58.2}
\]

The formulas extend across the kernel and O as degree-two separable isogenies. With \(\omega_T=dx/(2y)\), \(q_T^*\omega'_T=\omega_T\) and \(\psi_T^*\omega_{-T}=u\omega_T\). Composition has x-coordinate

\[
x(\psi_{-T}\psi_T(P))=
\frac{(x^2-C_T)^2}{4x(x^2-6x+C_T)}=x([2]P).
\]

Its differential multiplier is \(u^2=-2\), not +2; hence the sign cannot be discarded:

\[
\boxed{\psi_{-T}\circ\psi_T=[-2].} \tag{58.3}
\]

For p=8m+3 choose s²=2 in F_(p²), t=2s/3, and u in F_p with u²=-2 (possible since p=3 mod8). We have t^p=-t, so ψ_t is a degree-two isogeny to the Frobenius-conjugate E_t^(p). With relative Frobenius F_p:E_t→E_{-t} define the endomorphism

\[
\Phi_t=\psi_{-t}\circ F_p,\quad \deg\Phi_t=2p.
\]

Use the Frobenius naturality identity \(F_p\psi_{-t}=\psi_tF_p\) (with the appropriate twisted source/target) and (58.3):

\[
\boxed{\Phi_t^2=[-2]\circ F_{p^2,E_t}.} \tag{58.4}
\]

The q-Frobenius is an actual isogeny; it is not the identity morphism even when q-rational coordinates are fixed. If \(A_{p²}=p²+1-\#E_t(F_{p²})=\operatorname{Tr}(F_{p²})\) and \(a_\Phi=\operatorname{Tr}(\Phi_t)\), the elliptic characteristic polynomial gives \(\operatorname{Tr}(\Phi_t^2)=a_\Phi^2-4p=-2A_{p²}\), whence

\[
\boxed{A_{p²}=2p-a_\Phi^2/2.} \tag{58.5}
\]

## GH-59: exact class-wise traces and Legendre F magnitude (PROVED conditional on inherited CM inputs)

First prove the Hasse-to-trace bridge without guessing an extension-field character. Let r=(p−1)/2, f=f_t in F_(p²)[X] and \(f^r=\sum_{i=0}^{3r}b_iX^i\), \(h=b_{p-1}=H_p(t)\). Since \(f^{(p²-1)/2}=f^r(f^r)^p\), the coefficient of X^{p²−1} has **only** the pair i=j=p−1 within 0≤i,j≤3r. The total degree \(3(p²−1)/2\) is less than 2(p²−1), so the complete-field power sum selects exactly this coefficient. Euler's criterion yields

\[
\boxed{A_{p²}\equiv h h^p\pmod p.} \tag{59.1}
\]

The GH-32 polynomial identity and parity n even give \(H_p(t)^p=H_p(-t)=H_p(t)=(-6/p)P_n(t)\). Therefore

\[
\boxed{A_{p²}\equiv P_n(t)^2
\equiv9^{-2m}D_m^2F_m(9)^2\pmod p.} \tag{59.2}
\]

**Inert class p=19 mod24.** By GH-32, P_n(t)=0. Thus p divides A_(p²), and from (58.5), p divides a_\Phi. The standard elliptic endomorphism inequality \(|a_\Phi|\le 2\sqrt{2p}<p\) for p>8 forces \(a_\Phi=0\). Hence for every such prime,

\[
\boxed{A_{p²}=2p,\qquad \#E_t(F_{p²})=(p-1)^2.} \tag{59.19}
\]

**Ordinary class p=11 mod24.** GH-32 shows the curve has CM by the maximal order O_{-24}=Z[√−6] and good ordinary reduction. The CM order injects into the geometric endomorphism ring of the reduction; the latter is an order in Q(√−6), thus equals the maximal O_{-24}. Express the actual degree-2p endomorphism as \(\Phi_t=a+b\sqrt{-6}\), so the norm equation is \(a^2+6b^2=2p\). Since a is even, write a=2x, b=y (signs irrelevant for these conclusions). Then

\[
\boxed{p=2x^2+3y^2,\qquad A_{p²}=2(3y^2-2x^2),} \tag{59.11a}
\]
\[
\boxed{P_{(p-3)/4}(2\sqrt2/3)^2\equiv-8x^2\pmod p,\qquad
(D_mF_m(9))^2\equiv-8x^2\,9^{2m}\pmod p.} \tag{59.11b}
\]

Here \(a_\Phi=2a=4x\) up to a sign; (58.5) gives A_(p²)=2p−8x²=2(3y²−2x²). Substituting in (59.2) gives the squared special-value formula. This is a precise all-prime magnitude formula, **not** the unsquared sign, not the still-open G-derivative special value, and not the original GH-3 T_d(9)=0 theorem.

## Independent exact checks and BRC observer

The companion standard-library program performs finite-field operations in F_p[s]/(s²−2), enumerates the exact norm-character point counts, computes H_p and Legendre F separately, and checks all 11 primes 11≤p<200 with p=3 mod8. It also checks 24 actual extension-valued curve points per prime, 264 points total, for (58.2)–(58.4) including the sign of [-2]. The 11 traces, by p, are
\(11:-10,\ 19:38,\ 43:86,\ 59:-10,\ 67:134,\ 83:134,\ 107:86,\ 131:-250,\ 139:278,\ 163:326,\ 179:230\).
All checked. These finite checks support the proofs; they do not constitute infinite enumeration.

BRC COMPOSE_APPLIED: preserve original rank, F versus G signed source, extension and root-choice, 2-torsion kernel, 2-isogeny, Frobenius order, signed trace and CM norm variables. The exact Hasse/point-count observer factors only for the stated F scalar. The original G square-fiber residual (GH-29/31), W/S, six native Hasse ports, joint-composite information and native X6 space are **not** erased or identified with the trace. No P000/worldview change.

**NEXT:** look for horizontal Gauss–Manin/Katz correspondence acting on the *derivative* \(tP'_n(t)-P_n(t)\), not just the trace. An exact weighted-character or Frobenius derivative certificate is needed for p=11 mod24. Separately the original T_d(9)=0 arithmetic proof, GH-20/21 next digit, R23/R36 Green, [X]U mod p², η/κ, native p=373 and independent Driver review remain OPEN.

**Control boundary (this run):** Native gateway 0.6.11, research_authority_granted=false, executor_binding_configured=false, source_sync.control.state=CODE_REVIEW_REQUIRED. No native own winning CLAIM, authorized OPEN, Source checkpoint, result, session mutation or review attempted. Old session/staging/request/Source frontier remains intact; control recovery owner issue awdawmip/enterprise-math#1558. This source is portable author evidence, NOT canonical native checkpoint. Existing schedule/phase/notifications are unchanged.

**Provenance:** GH-32 and GH-55 source notes in this same directory; Z.-H. Sun, *Congruences concerning Legendre polynomials II*, arXiv:1012.3898. The signed isogeny/Frobenius deductions here are author-derived and are not attributed to Sun.
