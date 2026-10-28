# D25/LIFT GH-80 — Odd-degree Clausen–Legendre bridge for the original Laurent source

Date: 2026-10-29 (Asia/Hong_Kong). **Portable TASK_RESEARCH author proof; UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING.** Mother objective \`ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION\` OPEN. Historical Task \`RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT\`, publication \`TP2-B6F4FC938FF94941C1B7\`. Frozen *scientific* pin \`c47e13e4aba0e006366f989d6334d443f6333ae3\` unchanged. The research lane claims no new native session/CLAIM/open/run/checkpoint.

## Exact scope: the previously unresolved p ≡ 7 (mod 8) branch

Let \(p=8m+7\ge7\) be a prime, \(m\ge0\), \(d=2m+1=(p-3)/4\), and \(k=\mathbb F_p\). Retain GH-16's original-source ordered coefficients
\[
U_d(z)=\sum_{r=0}^{d}h_rz^r,\quad h_0=1,\quad
h_{r+1}/h_r=\frac{(4r+3)^3}{(4r+4)(4r+5)(4r+6)}
\]
and the **distinct** original Laurent double-pole observer \(\mathcal H_d(z)=(8z\partial_z+5)U_d(z)\). All recurrence denominators in this range are \(p\)-units.

Define the new auxiliary degree-\(m\) polynomial
\[
F_m^{\rm odd}(z)=
\sum_{r=0}^{m}\frac{(-m)_r^2}{(2m+3)_r\,r!}\,z^r,
\qquad D_m=\binom{3m+2}{m}\in k^\times.
\]
This is **not** the GH-22 \(F_m\) port for \(p=8m+3\); preserve its odd-branch label.

### GH-80A. Complete polynomial asymmetric factorization

**Theorem.** In the *entire polynomial ring* \(k[z]\),
\[
\boxed{U_d(z)=(1-z)\bigl(F_m^{\rm odd}(z)\bigr)^2},\tag{80.1}
\]
\[
\boxed{
\mathcal H_d(z)
=F_m^{\rm odd}(z)
\left[16z(1-z)(F_m^{\rm odd})'(z)
 +(5-13z)F_m^{\rm odd}(z)\right].}\tag{80.2}
\]
The two factors of \(\mathcal H_d\) have respective degrees \(m\) and \(m+1\), exactly matching GH-78's odd-degree no-go against two degree-\(m\) factors.

**Proof without a characteristic-\(p\) division beyond its domain.** By the coefficient recurrence \(F=F_m^{\rm odd}\) solves
\[
z(1-z)F''+\left(\frac54-\frac{11}4z\right)F'-\frac{49}{64}F=0
\quad\text{in }k[z],
\]
because \(-m=7/8\), \(2m+3=5/4\) modulo \(p=8m+7\). Direct differentiation of \(q=(1-z)F^2\), followed by elimination of \(F''\), gives
\[
\left[\theta(\theta+\tfrac14)(\theta+\tfrac12)
-z(\theta+\tfrac34)^3\right]q=0,\quad\theta=z\partial_z.
\]
One checkable expansion of this third-order operator is
\[
z^3(1-z)\partial_z^3
+\frac{z^2(15-21z)}4\partial_z^2
+\frac{z(30-79z)}{16}\partial_z-\frac{27z}{64}.
\]
Here \(\deg q=2m+1=d\) and \(q(0)=1\). GH-78's exact source recurrence proves that the displayed third-order equation has a *unique* polynomial solution of degree \(\le d\) and constant coefficient \(1\): for \(1\le r\le d\), the leading recurrence divisor \(r(r+1/4)(r+1/2)\) is a \(p\)-unit. Therefore \(q=U_d\), proving (80.1) with no unjustified extension of a truncated formal series. Applying \(8\theta+5\) and collecting terms proves (80.2). The leading coefficient of \(F\) is \(D_m^{-1}\ne0\); the second factor's highest coefficient is \(-(16m+13)D_m^{-1}=D_m^{-1}\) modulo \(p\), so the asserted degrees are exact.

For classical context, this is the characteristic-\(p\) polynomial counterpart of Euler's \({}_2F_1\) transformation followed by Clausen's square identity (NIST DLMF §16.12.2), but the proof above relies only on the displayed **polynomial differential operators and source coefficient recurrence**, so no reduction of a series through undefined denominators is assumed.

### GH-80B. Whole-polynomial odd Legendre transform

Let \(P_d\) be the ordinary Legendre polynomial and \(t^2=(z-1)/z\). Since \(d=2m+1\) is odd,
\[
W_m(z):=z^m\frac{P_{2m+1}(t)}t
\]
is a well-defined polynomial in \(k[z]\) of degree \(m\). By the Legendre differential equation and the rational change of variable (first over characteristic zero, then reduce),
\[
z(1-z)W_m''+
\left[-2m-\frac12-(1-2m)z\right]W_m'-m^2W_m=0.
\]
Its constant coefficient is a \(p\)-unit (the signed leading coefficient of \(P_{2m+1}/t\)); its leading coefficient is \(P_{2m+1}(1)=1\). Since \(-2m-\tfrac12\equiv2m+3\pmod p\), the displayed equation becomes exactly the \(F_m^{\rm odd}\) Gauss equation. Its degree-\(\le m\) polynomial solutions are one-dimensional by the unit coefficient recurrence. As the leading coefficient of \(F_m^{\rm odd}\) is \(D_m^{-1}\), the precise normalized identity is
\[
\boxed{D_mF_m^{\rm odd}(z)=
 z^m\frac{P_{2m+1}(t)}t\quad\text{in }k[z].}\tag{80.3}
\]
Inserting (80.3) into (80.1) and using \(1-z=-zt^2\) yields a **global polynomial identity**
\[
\boxed{U_d(z)=-D_m^{-2}z^dP_d(t)^2.}\tag{80.4}
\]
The right side is polynomial because \(P_d\) is odd. Differentiating this full identity and only then setting \(z=9,\ t^2=8/9\), gives
\[
\boxed{\mathcal H_d(9)=
-D_m^{-2}9^dP_d(t)[tP_d'(t)-P_d(t)].}\tag{80.5}
\]
Here \(t\in\mathbb F_p^\times\) for \(p\equiv7\pmod8\), since \(2\) is a quadratic residue. Equation (80.5) is a new source-faithful bridge, *not yet by itself* a proof of either prime-class branch.

## Evidence and provenance

The standard-library exact checker independently constructs GH-16 \(U_d\), the new \(F_m^{\rm odd}\), and the Legendre polynomial. It verifies both full-polynomial identities (80.1),(80.3) and the factorization (80.2) for **all 78 primes** \(7\le p<2000,\ p\equiv7\bmod8\). The complete special-value connection was checked for **all 308 primes** \(7\le p<10000,\ p\equiv7\bmod8\). This is implementation evidence; the all-prime proof is the preceding recurrence/ODE argument.

Inherited exact author-side sources: GH-16/GH-78 original \(U_d,\mathcal H_d\) and the third-order operator (enterprise-math@30a93372b5fdfa4eb761fd047a1a94e5f0f687ff); GH-79 \(p=23\) normalization falsifier (enterprise-math@e6888532a93ef1f591b950daa08388d0dafa014d). The GH-22 even-branch \(F/G\) ports remain separate.

BRC **COMPOSE_APPLIED**: preserve \(p,d,m\), original ordered \(h_r\), the observer \(8\theta+5\), the new labeled \(F^{\rm odd}\), the parity factor \(1-z\), the Legendre square-root chart and all derivative jets. A scalar zero is not a safe quotient of separate F/H/Laurent sources. This arithmetic chart is external, *not* an X6 native coordinate or a substitute for P000's six-axis/three-dimensional-slice semantics.

**Next exact action:** use GH-74's *actual* CM endomorphism and GH-75's Cartier calculation with \(d\) odd and \(t\in\mathbb F_p\) (a different Frobenius branch) to independently classify the two factors in (80.5). A proof must check the characteristic-seven edge case, Hasse normalization sign and absence of double Legendre roots. Keep GH-3 endpoint/first-order Laurent and all \(p^2\)/native experiment obligations independent.

Status: \`AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING\`. No native Source checkpoint, activity registration or Driver review is claimed.
