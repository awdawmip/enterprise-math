# Full-truncation forcing and Frobenius-kernel algebra audit

Status: BOUNDED_PURE_PAPER_PREPARATION / ALGEBRA_AUDIT_PASS / PARENT_LIFT_OPEN.

Prepared locally on 2026-10-11 under the parent's bounded authorization.
The P000, Heartbeat World, and residual-faithful companion contracts were
read first. This is external finite arithmetic, with no native spatial
or propagation assertion. No Task, claim, identity, immutable Result,
Source publication, remote write, numerical prime campaign, or LIFT
completion is created. The supplied first-digit finite certificate is
the input premise. This is shared-work algebra assistance, not a blind
independent review of the parent's eventual second-digit argument.

## 1. Exact operator normalization and signs

Let p=6m+1 be prime, p>=7, with the parent's target classes 13 or 19 mod 24.
Use rational variable z and

    A=(3z-1)/(z-1)^3,  B=(3z-1)^2/(z+1)^3,
    L=(z+1)/(2(1-z)),  K=-z(z-3)(3z-1)/(3(z+1)^2).

Let b_n=(1/3)_n(2/3)_n/(n!)^2 and F(x)=sum_(n=0)^(p-1)b_n x^n.
Put H=F mod p, of degree 2m, and

    D_H=x(1-x)partial_x^2+(1-2x)partial_x-2/9,
    kappa=(p-2/3)(p-1/3)b_(p-1),
    Q_B=-2/[z(z+1)^2],
    O=K partial_z^2+K'partial_z+K Q_B.

The coefficient recurrence n^2 b_n=(n-2/3)(n-1/3)b_(n-1) gives exactly

    D_H F=-kappa x^(p-1).

Direct rational differentiation verifies

    A'=-6z/(z-1)^4,
    B'=-3(z-3)(3z-1)/(z+1)^4,
    K=B(1-B)/B',  A(1-A)/A'=2L^2K,
    O(F(B))=B'(D_HF)(B),
    O(LF(A))=A'/(2L) (D_HF)(A).

For f=F(B), g=LF(A), R=K(fg'-gf'), the product rule gives

    R'=f O(g)-g O(f)
      =-kappa [F(B) A'/(2L) A^(p-1)-LF(A) B' B^(p-1)].       (1)

All supplied signs and the factor A'/(2L) are correct.

The two numerator products for b_(p-1) each contain one p factor:
p/3 in (1/3)_(p-1), and 2p/3 in (2/3)_(p-1). Removing them, the
remaining residue products are 3/2 and 3 respectively, by Wilson's
product of nonzero residues. Since ((p-1)!)^2=1 mod p,

    b_(p-1)/p^2=1 mod p,  kappa/p^2=2/9 mod p.              (2)

## 2. Divided forcing and rational simplifications

Write J(t)=t(t-3)(3t-1)/(t^2-1)^2. The supplied first-digit certificate
R=-(p/3)J(z^p) mod p^2 makes

    C=(R+(p/3)J(z^p))/p^2 mod p

coefficientwise defined. Differentiate before reducing and use (1),(2):

    C'=-(2/9)[H(B) A'/(2L) A^(p-1)-LH(A) B' B^(p-1)]
        +(1/3)z^(p-1)J'(z^p).                              (3)

There is no missing factor p: the p in differentiating z^p cancels
the p^2 denominator against the preceding factor p/3.

Useful exact expressions are

    A'/(2L)=6z/[(z-1)^3(z+1)],
    LB'=3(z-3)(3z-1)/[2(z-1)(z+1)^3],
    J'(t)=-(t^2-6t+1)(3t^2-2t+3)/[(t-1)^3(t+1)^3].

Consequently the forcing Q=C' can also be written in characteristic p as

    Q=-(4/3)z(3z-1)^(p-1)H(B)/[(z-1)^(3p)(z+1)]
      +(1/3)(z-3)(3z-1)^(2p-1)H(A)/[(z-1)(z+1)^(3p)]
      +(1/3)z^(p-1)J'(z^p).                                (4)

The existing R mod p=0 certificate implies a finite rational transport

    H(A)=L^(p-1)H(B).                                      (5)

Indeed, the ratio LH(A)/H(B) belongs to F_p(z^p). Divide it by L^p.
The result is G_A/G_B, where

    G_A=(z-1)^(p-1)H(A),  G_B=(z+1)^(p-1)H(B)

are monic polynomials of degree p-1. A reduced rational function with
numerator and denominator degrees less than p cannot be a nonconstant
member of F_p(z^p). Its value at infinity is 1. This proves (5)
without a new analytic transformation or an asserted CM value.

For X=z^p, (5) combines the first two terms of (3) into

    Q=-H(B)(3X-1)[4z(X+1)^2-(z-3)(3X-1)(X-1)^2]
        /[3(z+1)(3z-1)(X-1)^3(X+1)^2]
      +(X/(3z))J'(X).                                     (6)

The displayed denominators at z=0 and z=1/3 in (6) are removable;
the original expression (4) introduces poles only at z=+/-1.

## 3. Pole classification: the lift of J must be expanded

For the full degree p-1 truncation, g has pole order at most 3p-2
at z=1, while f,K are regular. Thus R has pole order at most 3p-1.
At z=-1, f has pole order at most 3p-3, g has a zero of order at
least 1, and K has pole order 2; the same bound follows. Critical
points 0,3,1/3 add no poles.

It is not valid simply to transfer this bound to C: over characteristic
zero the exact J(z^p) has cyclotomic poles. Their first-order reduction
must be retained after division by p^2.

Put D=z^2-1, N(t)=t(t-3)(3t-1), and

    E=[z^(2p)-1-D^p]/p in Z[z].

The numerator is divisible by p, and E is divisible by D because it
vanishes at both z=1 and z=-1. Expanding the denominator gives

    J(z^p)=N(z^p)/D^(2p)-2p N(z^p)E/D^(3p) mod p^2,
    C=[R+(p/3)N(z^p)/D^(2p)]/p^2
      -(2/3)N(z^p)E/D^(3p) mod p.                          (7)

The first divided term is coefficientwise integral by the first-digit
certificate and has pole order at most 3p-1. The second term has the
same bound since D divides E. Thus C has poles only at +/-1, of order
at most 3p-1. In particular Q=C' has order at most 3p at each pole.
The three terms of (4) independently exhibit the latter bound, using
deg H=(p-1)/3.

For an equivalent local expansion,

    J(t)=-1/(t-1)^2-1/(t-1)-4/(t+1)^2+4/(t+1),
    a_+=(z^p-1-(z-1)^p)/p,  a_-=(z^p+1-(z+1)^p)/p.

Both a_+ and a_- contain their indicated linear factor. The p correction
is a_+[2/(z-1)^(3p)+1/(z-1)^(2p)]
 +a_-[8/(z+1)^(3p)-4/(z+1)^(2p)], giving the same bound.

## 4. Canonical finite primitive and exact residual kernel

R=O(z^-1) and J(z^p)=O(z^-p) at infinity. Monic integral common
denominators preserve properness under coefficientwise division.
Therefore C is proper and Q has no polynomial part.

Write its unique finite partial fractions as

    Q=sum_(a=+/-1) sum_(k=1)^(3p) q_(a,k)/(z-a)^k.

For example q_(a,k) is the coefficient of u^(3p-k) in the formal
polynomial jet u^(3p)Q(a+u) modulo u^(3p). Rational integrability
requires precisely

    q_(a,1)=q_(a,p+1)=q_(a,2p+1)=0  for each a.             (8)

These vanish here because the coefficientwise constructed C is already
a rational primitive. They are useful exact consistency obligations
for any independently produced version of the forcing.

After (8), define the canonical proper primitive

    P=-sum_(a=+/-1) sum_(2<=k<=3p, k!=1 mod p)
          q_(a,k)/(k-1) (z-a)^(-(k-1)).                     (9)

Every denominator k-1 in this formula is a unit. The derivative kernel
of F_p(z) is exactly F_p(z^p), so the remaining ambiguity is exactly

    C-P=h(z^p),
    h(X)=N_0(X)/(X^2-1)^2,  deg N_0<=3.                    (10)

Equivalently it is the span of (z-1)^(-p),(z-1)^(-2p),
(z+1)^(-p),(z+1)^(-2p). There are four kernel coefficients; forcing
alone does not determine them. No constant survives C(infinity)=0.

## 5. Four finite normalizations fix the kernel, including infinity

Let q=q_p(3)=(3^(p-1)-1)/p mod p. The exact zeros R(0)=R(3)=R(1/3)=0
and the first-order expansions of J give

    C(0)=0,  C(3)=C(1/3)=3q/8.                             (11)

Specifically J'(3)=3/8, J'(1/3)=-27/8,
(3^p-3)/p=3q, and ((1/3)^p-1/3)/p=-q/3 mod p.
These are evaluations of the actual rational lift, not a literal
characteristic-zero replacement of z^p by its residue.

The fourth normalization is also explicit. Since

    b_n=(3n)!/[27^n(n!)^3],

split the numerator for n=p-1 into its three p blocks and remove p,2p.
Modulo p^2, with H_r=sum_(i=1)^r 1/i,

    b_(p-1)/p^2
      =2[1+pH_(p-1)+2pH_(p-3)]/[27^(p-1)(p-1)(p-2)]
      =1+p(9/2-3q),
    kappa/p^2=(2/9)(1-3pq).                                (12)

Here H_(p-1)=0 mod p, H_(p-3)=3/2 mod p and q_p(27)=3q mod p.
All divisions in this calculation are by p-adic units.

At infinity the bracket in (1) begins -9^p z^(-p-1)/2,
so R'=kappa 9^p z^(-p-1)/2+O(z^(-p-2)). Properness gives the exact
coefficient [z^-p]R=-kappa 9^p/(2p), with earlier Laurent coefficients
zero. Since J(z^p)=3z^-p+O(z^-2p), (12) gives

    C=O(z^-p),
    [z^-p]C=[1-9^p kappa/(2p^2)]/p=q mod p.                (13)

This retains the next coefficient of kappa and cannot be deduced from
kappa/p^2=2/9 alone.

For a fully fixed finite reconstruction, set

    v0=-P(0),  v3=3q/8-P(3),  va=3q/8-P(1/3),
    eta(X)=v0(X-3)(X-1/3)
           +8v3 X(X-1/3)-(8/9)va X(X-3),
    gamma=[q-[z^-p]P]/3.

Then all four normalizations are incorporated by

    C(z)=P(z)+eta(z^p)/(z^(2p)-1)^2+gamma J(z^p) in F_p(z). (14)

The degree-two eta interpolates the three finite values, and J vanishes
at all three nodes. The leading coefficient of J at infinity is 3,
so gamma supplies exactly (13). A difference satisfying all four
conditions would have numerator proportional to X(X-3)(3X-1) and
zero leading coefficient, hence would be zero. Thus this reconstruction
is unique, finite, and determined by actual arithmetic, without fitting.

Formula (14) leaves the parent's substantive CM evaluation identity
open. No vanishing of C at the CM point, and no second-digit LIFT,
has been inferred from kernel normalization alone.

## 6. Verification and handoff

The adjacent `check_forcing_algebra.py` verifies the exact operator
pullbacks, Wronskian sign, recurrence multipliers, forcing prefactors,
J partial fractions and derivatives, combined forcing, and four-node
kernel interpolation symbolically. Its JSON report records actual
execution. Pole, integrability, finite transport, valuation and infinity
arguments above are paper derivations, not numerical prime tests.

The delegated characteristic-p pole/kernel helper independently checked
the four-dimensional residual kernel and the need for the first-order
J expansion. The parent independently confirmed (12),(13) and supplied
the same finite endpoint values during this shared-work audit.
