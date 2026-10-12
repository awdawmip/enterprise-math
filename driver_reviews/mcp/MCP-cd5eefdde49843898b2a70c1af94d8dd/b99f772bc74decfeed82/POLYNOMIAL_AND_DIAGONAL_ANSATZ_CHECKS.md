# Polynomial and diagonal ansatz checks

This note concerns only the fixed formal kernel

\[
K(i,r)=B_iD_r,\qquad
\frac{B_{i+1}}{B_i}=a(i)=\frac{(i+\tfrac16)(i+\tfrac13)}{2(i+1)^2},
\qquad
\frac{D_{r+1}}{D_r}=b(r)=\frac{2r^2}{(r+\tfrac56)(r+\tfrac23)},
\]

and the weight \(W(i,r)=1+6(i-r)\). Differences are forward differences.
Only the two explicitly identified narrower certificate classes below are
checked. Arbitrary independent rational two-variable fluxes remain
unexcluded. All conclusions are rational-function identities over characteristic zero;
no summation boundaries, specializations, or congruences are used.

## 1. No certificate in the polynomial adjoint class, at any degree

Suppose the certificate has the prescribed shape

\[
Q=i^2q(i,r),\qquad
S=(r-\tfrac16)(r-\tfrac13)s(i,r),
\qquad q,s\in\mathbb Q[i,r].
\]

After division by \(K\), its divergence equation is

\[
L_iq+L_rs=W,
\]

where

\[
L_iq=\tfrac12(i+\tfrac16)(i+\tfrac13)q(i+1,r)-i^2q(i,r),
\]

\[
L_rs=2r^2s(i,r+1)-(r-\tfrac16)(r-\tfrac13)s(i,r).
\]

The operators commute, because their coefficients and shifts act in
separate variables. If \(h\) is a nonzero homogeneous polynomial, their
highest total-degree parts are

\[
\operatorname{top}(L_ih)=-\tfrac12i^2h,
\qquad \operatorname{top}(L_rh)=r^2h.
\]

**Proposition.** No such polynomial \(q,s\) satisfy the certificate equation.

**Proof.** Assume a solution exists and let
\(d=\max(\deg q,\deg s)\). A nonzero polynomial has nonnegative total degree.
Since \(W\) has degree one, the degree \(d+2\) parts on the left must cancel.
If only one of \(q,s\) has degree \(d\), cancellation is impossible. Otherwise
write their degree-\(d\) homogeneous parts as \(q_d,s_d\). They obey

\[
-\tfrac12i^2q_d+r^2s_d=0.
\]

Since \(i^2\) and \(r^2\) are coprime, there is a homogeneous polynomial
\(h\) of degree \(d-2\) with

\[
q_d=r^2h,\qquad s_d=\tfrac12i^2h.
\]

In particular, \(d\ge2\). Replace the pair by

\[
q'=q-L_rh,\qquad s'=s+L_ih.
\]

Commutation gives \(L_iq'+L_rs'=L_iq+L_rs\), while the degree-\(d\)
parts of both polynomials have been removed. Thus the maximum degree
strictly decreases. Iterating reaches a pair with maximum degree zero or
one, for which the same cancellation would require a nonzero polynomial
of degree \(d-2<0\), an impossibility. The zero pair has zero divergence
and cannot produce \(W\). This contradiction proves the proposition.

Equivalently, polynomial reduction by \(L_i,L_r\) leaves the vector-space
normal-form basis \(\{1,i,r,ir\}\). Here the quotient is by
\(\operatorname{im}L_i+\operatorname{im}L_r\), not an ideal quotient.
The weight \(1+6i-6r\) is already a nonzero normal form. This interpretation
is not needed for the proof above.

## 2. No rational flux in the simultaneous diagonal direction

Consider the narrower proposal

\[
Q(i+1,r+1)K(i+1,r+1)-Q(i,r)K(i,r)=W(i,r)K(i,r),
\qquad Q\in\mathbb Q(i,r).
\]

It is a valid subclass of two-direction divergences: if \(F=QK\), then
\[
\Delta_{(1,1)}F=\Delta_iF+\Delta_r(T_iF),
\]
where \(T_iF(i,r)=F(i+1,r)\).

Set \(n=i-r\) and regard \(n\) as an indeterminate. Work over
\(F_0=\mathbb Q(n)\), with \(r\) the shift variable. The kernel ratio is

\[
\frac{K(i+1,r+1)}{K(i,r)}=\frac{N(r)}{M(r)},
\]

\[
N=r^2(r+n+\tfrac16)(r+n+\tfrac13),\qquad
M=(r+n+1)^2(r+\tfrac56)(r+\tfrac23).
\]

Put

\[
C(r)=M(r-1)=(r+n)^2(r-\tfrac16)(r-\tfrac13),
\qquad Q(r)=C(r)f(r).
\]

This is an invertible change among rational functions. The flux equation
becomes

\[
N(r)f(r+1)-C(r)f(r)=1+6n.\tag{*}
\]

**Lemma.** A rational \(f\in F_0(r)\) satisfying (*) has no finite poles and
therefore is polynomial in \(r\).

**Proof.** Pass to an algebraic closure of \(F_0\) and group the finitely
many poles of \(f\) into their integer-shift orbits. If an orbit contains
poles, write its occupied positions as \(\alpha+k\), with integer \(k\),
and choose the smallest and largest occupied positions \(k_-\le k_+\).
At \(r=\alpha+k_- -1\), only \(f(r+1)\) can have a pole; the polynomial
right side therefore forces \(N\) to have a root there. At
\(r=\alpha+k_+\), only \(f(r)\) can have a pole; it forces \(C\) to have a
root there. Thus \(N\) and \(C\) must have roots differing by an integer
\(k_+-k_-+1\).

Their respective roots are

\[
\{0,-n-\tfrac16,-n-\tfrac13\},\qquad
\{-n,\tfrac16,\tfrac13\}.
\]

No pair differs by an integer in \(F_0\): differences within the
constant-root sets or within the \(-n\)-root sets are nonintegral
fractions, and cross-set differences depend nontrivially on the
indeterminate \(n\). Hence no pole orbit exists.

**Proposition.** The simultaneous diagonal flux equation has no rational
solution \(Q\in\mathbb Q(i,r)\).

**Proof.** By the lemma, \(f\) in (*) must be polynomial. The zero
polynomial cannot produce the nonzero element \(1+6n\in F_0\). If
\(f=c r^k+O(r^{k-1})\), with \(c\ne0\) and \(k\ge0\), then

\[
N=r^4+(2n+\tfrac12)r^3+O(r^2),\qquad
C=r^4+(2n-\tfrac12)r^3+O(r^2),
\]

so

\[
Nf(r+1)-Cf(r)=c(k+1)r^{k+3}+O(r^{k+2}).
\]

The coefficient \(c(k+1)\) is nonzero in characteristic zero. The left
side has degree at least three, while the right side has degree zero in
\(r\). This contradiction proves the proposition.

## Scope

The first proposition excludes only the class with polynomial \(q,s\)
in the stated adjoint factorization. The second excludes only a single
rational simultaneous-diagonal flux. Neither proposition establishes
nonexistence of arbitrary independent rational \(Q,S\in\mathbb Q(i,r)\)
in a general two-direction divergence. In particular, arbitrary
sum- or difference-denominator certificate pairs are not excluded by
these proofs. No broader nonexistence claim is made.

The accompanying exact symbolic checker verifies the kernel-to-adjoint
identities, commutation, diagonal change of variables, and the leading
coefficient calculation. The all-degree and all-rational assertions
come from the proofs, not from finite-degree experimentation.
