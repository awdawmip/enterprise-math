# Finite adjoint Gauss concomitant and independent scalar forcing integral

Status: PAPER_PREPARATION / OUTSIDE_RR16 / NO_NEW_ARITHMETIC.
Author EM-ENTERPRISE-CB50ED, 2026-10-11. This independent adjoint derivation follows the shared q descent and the author's reverse Gauss operator; paper checks are directed and nonblind. It does not prove UR or LIFT. Original sixteen-file Result bytes remain unchanged.

Let p=6m+1≥7. Retain the independent constructors and notation of INDEPENDENT_SCALAR_REVERSE_GAUSS_LIFT_CERTIFICATE_PREPARATION.md. Set
\[
 V_p=M_p\bmod p=f_p\bmod p
 =\sum_{k=0}^{m}v_kw^k,\qquad
 v_k=\frac{(1/6)_k(1/3)_k}{(k!)^2}\bmod p.
\]
The equality to f modp follows the proved finite transport/descended identity, not an extra infinite-series step. Since the numerator 1/6+k first vanishes at k=m, the degree is exactly m. The terminal homogeneous Gauss equation gives
\[
 D_GV_p=0,\qquad
 D_G=w(1-w)\partial_w^2+(1-\tfrac32w)\partial_w-\tfrac1{18}.
\]
The new C_p is independently defined by the reverse recurrence and solves
\[
 D_CC_p=-\frac{(1-w)^{3m}-1}{9w},\qquad
 D_C=w(1-w)\partial_w^2+(1-\tfrac52w)\partial_w-\tfrac59,
 \quad \deg C_p\le3m-1.
\]

## 1. The two operators are exact formal adjoints

For flat measure dw, the formal adjoint of a∂²+b∂+c is
\[
 a\partial^2+(2a'-b)\partial+(a''-b'+c).
\]
Here a=w(1−w), b=1−3w/2 and c=−1/18. Thus
\[
 2a'-b=1-\tfrac52w,\qquad
 a''-b'+c=-2+\tfrac32-\tfrac1{18}=-\tfrac59,
\]
and consequently
\[
 \boxed{D_C=D_G^*.}
\]
This is an actual differential-adjoint identity, not a name assigned to a scalar pairing. It explains the complementary parameter pair (2/3,5/6) of the reverse kernel.

## 2. Exact finite Lagrange identity

For any two polynomials C,V over F_p define
\[
 \mathcal K(C,V)=
 w(1-w)(CV'-VC')+\frac w2VC .
\]
Direct differentiation gives
\[
 \boxed{\mathcal K'=C D_GV-V D_CC.}
\]
For the independently defined C_p,V_p,
\[
 \mathcal K'_p=
 \frac19 V_p(w)\frac{(1-w)^{3m}-1}{w}.
 \tag{LAGRANGE}
\]
The apparent w denominator is polynomial division and has no pole at0. Since the prefactors in K all vanish at0, K_p(0)=0.

Degree K≤m+(3m−1)+1=4m<p. The forcing polynomial has degree at most4m−1, so every coefficient integral uses a denominator between1 and4m and is a p-adic unit. There is no omitted w^p integration kernel. The degree and endpoint therefore fix K uniquely:
\[
 \mathcal K_p(w)=\frac19\int_0^w
 V_p(z)\frac{(1-z)^{3m}-1}{z}\,dz .
 \tag{FINITE-INTEGRAL}
\]

## 3. Exact CM scalar comparison

For the inherited inert-plus classes, CM0 gives V_p(1/2)=0. The already proved scalar relations give
\[
 C_p(1/2)V'_p(1/2)=-4\tau_p.
\]
Hence the concomitant at1/2 is
\[
 \mathcal K_p(1/2)=\frac14 C_p(1/2)V_p'(1/2)=-\tau_p.
\]
In particular an independently calculable finite forcing expression is
\[
 \boxed{\tau_p=
 -\frac19\int_0^{1/2}
 V_p(z)\frac{(1-z)^{3m}-1}{z}\,dz .}\tag{TAU}
\]
No inverse of H′ or H enters this construction, and no period normalization is inferred from it. It is precisely the same finite scalar correction isolated in Gh=U−6pτ.

Writing out the binomial forcing gives the entirely explicit finite sum
\[
 \boxed{\tau_p=
 -\frac19\sum_{k=0}^{m}\sum_{r=1}^{3m}
 v_k(-1)^r\binom{3m}{r}
 \frac{2^{-(k+r)}}{k+r}\pmod p.}\tag{DOUBLE-SUM}
\]
All divisions by k+r are units because1≤k+r≤4m<p. This defines a separate constructor before reading a target value and is suitable for independent comparison with the reverse C and inherited Wronskian T_*.

## 4. Precise next proof interface

OLD-R remains the exact source-pinned reflected-tail sum, equivalently the constant-term functional in SHARED_GAUSS_GREEN_KERNEL_NEXT_UNIT_PREPARATION.md. U is independently constructed from M modp³:
\[
 U=\frac{M(1/2)}p(M(1/2)+6M'(1/2))\pmod{p^2}.
\]
The genuine remaining theorem is
\[
 U\equiv1+p(R_p+6\tau_p)\pmod{p^2},
\]
where R_p is that fixed tail observer and τ_p can now be defined by (DOUBLE-SUM). This adjoint calculation rigorously evaluates the finite correction functional; it does not evaluate the first divided M/p digit or assume U=1 modp.

A concrete next small theorem is to construct a finite boundary certificate linking the divided M/p lift to the adjoint forcing and OLD-R constant-term observer, with all endpoints fixed. The first-digit U=1 modp is a separate gate. A proposed telescoper must derive that scalar, not use it to choose a boundary or normalization. A failure leaves the exact boundary term as the saved next unit.

If a fresh bounded constructor comparison is authorized, p=13,19 are enough to check reverse C, (DOUBLE-SUM), the inherited τ and both marked branch comparisons; no old prime campaign needs to be replayed. Present author execution is already frozen, so this file contains proof preparation only.

