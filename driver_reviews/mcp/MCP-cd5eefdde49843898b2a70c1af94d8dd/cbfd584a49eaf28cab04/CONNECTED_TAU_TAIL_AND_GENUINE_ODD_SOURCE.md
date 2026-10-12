# Independent connected tau dictionary, both tails, and a genuine odd source

Status: ONE BOUNDED LOCAL ALGEBRA UNIT / CONNECTED FINITE LEMMAS AND ONE
BILINEAR SOURCE COMPARISON PROVED / SCALAR COMPARISON OPEN. Prepared
2026-10-12 UTC. Only this independent-check directory is written. No
prime is instantiated, no scalar is fitted, and no previous checker is
read or executed. There is no Source or native mutation. The old
reciprocal C kernel and old binomial tau double-sum are consumed as
proved inputs, not reproved or replaced.

Here g is always the literal unit binom(3m,m)=h_0=h_N=V(1), with sum h=1.
It is distinct from the earlier p-adic memo's symbol g=f_p(1/2), which
is divisible by p. All formulas below retain the unit g of the latest
frozen units. OLD-R and the original tau remain independent constructors.

## 1. Connected reverse carrier and its finite normalization

Retain p=6m+1 in the frozen marked classes, N=3m, and the independently
defined reverse carrier C(w), deg C<=N-1. Set

    A(z)=sum_(i=0)^m a_i z^i,
    a_i=(1/6)_i(1/3)_i/[(1/2)_i i!],
    Cbar(z)=C(1-z),
    D_A=z(1-z)partial_z^2+(1/2-3z/2)partial_z-1/18.

Under w=1-z, the original D_G transforms exactly into D_A. Thus the
literal V(1)=g and uniqueness of the forward unit-divisor coefficient
recurrence give V(w)=gA(1-w). The fixed degree-m V is used here, not an
infinite series assigned a CM value. In particular

    A(0)=1, A(1)=1/g, A(1/2)=0.

The last equality is the retained CM0 statement and g is a unit.
Flat adjunction gives

    D_A*=z(1-z)partial_z^2+(3/2-5z/2)partial_z-5/9,
    D_A*Cbar=(1-z^N)/[9(1-z)].                             (1)

The right quotient is the literal polynomial (1/9)sum_(j=0)^(N-1)z^j.
Writing Cbar=sum_(j=0)^(N-1)cbar_j z^j, its actual coefficient recurrence
is

    (j+1)(j+3/2)cbar_(j+1)
       -(j+2/3)(j+5/6)cbar_j=1/9, 0<=j<N,
    cbar_N=0.                                            (2)

The denominator factors in reverse propagation vanish first at j=4m,
5m, outside the complete window 0,...,N-1. At its last row the forward
coefficient itself is zero. No division by that coefficient occurs.
Thus (2) determines the same independently defined carrier by a legal
reverse recurrence; no boundary is fitted from tau or the target.

## 2. Concomitant, degree, and the connected tau double sum

Define

    J(z)=z(1-z)(Cbar A'-A Cbar')+(z-1)ACbar/2.

The all-coefficient Green identity and the original concomitant give

    J'=Cbar D_A A-A D_A*Cbar
       =-(A/9)sum_(j=0)^(N-1)z^j,
    J(z)=-K_G(C,V)(1-z)/g,
    J(1)=0, J(1/2)=tau/g.                                (3)

The sign follows directly from V'_w=-gA'_z and C'_w=-Cbar'_z; no
orientation is inferred merely from an integral name. At CM0 the
boundary is also

    C_*A'(1/2)=4tau/g, C_*=Cbar(1/2).                     (4)

No inverse of C_* is taken.

Since deg J<=m+(N-1)+1=4m<p, all antiderivative denominators lie in
1,...,4m. Its normalization J(1)=0 therefore fixes the polynomial
without a Frobenius ambiguity. Integrating (3) from 1/2 to 1 gives

    BOX: tau/g=(1/9)sum_(i=0)^m a_i ell_i,
         ell_i=sum_(r=i+1)^(i+N)(1-2^(-r))/r.             (5)

This is the new connected dictionary for the original tau. Every actual
r lies in 1,...,4m<p. It is not a replacement definition from the scalar
comparison.

The coefficient dictionary is equally explicit. If J=sum_(s=0)^(4m)
kappa_s z^s, then

    kappa_s=-(1/(9s))sum_(i=max(0,s-N))^(min(m,s-1))a_i,
                    1<=s<=4m,
    kappa_0=-sum_(s=1)^(4m)kappa_s.                       (6)

Both endpoints follow from the actual convolution in (3) and J(1)=0.

## 3. The actual harmonic-complement tail and the same prefix weight

Let H_n(c)=sum_(r=1)^n c^r/r and O_n(c)=sum_(r=1)^n c^r/(2r-1), as
in the frozen papers. For 0<=i<=m, every upper harmonic index N+i is
less than p. The marked branch 2^(-N)=-1 and N=-1/2 in coefficient
reductions give the exact upper-tail identities

    H_(N+i)(1)=H_N(1)+2O_i(1),
    H_(N+i)(1/2)=H_N(1/2)-2O_i(1/2).                     (7)

Consequently, with the independently prescribed constant

    ell_0=H_N(1)-H_N(1/2),
    gamma_i=2O_i(1)-H_i(1)+2O_i(1/2)+H_i(1/2),

the actual connected tail is ell_i=ell_0+gamma_i, and

    gamma_i-gamma_(i-1)
         =[1+(4i-1)2^(-i)]/[i(2i-1)], 1<=i<=m.           (8)

For an independent sign check, subtract the two moving tail endpoints
in (5): its increment is
(1+2^(-i))/(i-1/2)-(1-2^(-i))/i, exactly (8).

Set the unchanged prefix S_k=sum_(r=0)^k a_r. Finite summation by parts,
including i=0,m and sum a=1/g, now gives the genuine prefix comparison

    BOX: 9tau=ell_m-g M_tau,
    M_tau=sum_(k=0)^(m-1) S_k
            [1+(4k+3)2^(-k-1)]/[(k+1)(2k+1)],
    ell_m=ell_0+gamma_m.                                  (9)

Thus the original tau source is carried by the very same fixed S_k
weight appearing in the previous exact residual. Its upper endpoint is
the actual ell_m; it is not omitted or chosen from a discrepancy.

For an explicit complement form of that endpoint, define the full
finite logarithm L_full(c)=H_(p-1)(c). Complementing only actual
denominators 1,...,p-1 gives

    H_(p-1-q)(c)=L_full(c)+c^p H_q(1/c).

Here q=2m. Since L_full(1)=0 and (1/2)^p=1/2 in the base field,

    BOX: ell_m=H_(2m)(1)-H_m(1)-L_full(1/2)
                         -H_(2m)(2)/2+H_m(1/2).         (10)

The full finite-log tail and its Frobenius coefficient 1/2 are retained
literally; no Fermat quotient or target value is used to remove them.

## 4. Cubic composition and its distinct x^p tail

Let z(x)=x(4x-3)^2 and B(x)=J(z(x)). Its degree is 12m=2p-2, so the
only possible nonconstant derivative-kernel monomial is x^p. Its actual
coefficient is

    b_p=sum_(s=2m+1)^(4m) kappa_s
           binom(2s,p-s)4^(p-s)(-3)^(3s-p).              (11)

The lower bound follows from 3s>=p, and the upper from deg J=4m. For
that whole range, formula (6) can be written

    kappa_s=-[1/g-1_(s>N)S_(s-N-1)]/(9s).               (12)

This preserves the full raw coefficient/prefix tail before any modular
simplification. There is also a useful exact finite simplification: every
term with N+1<=s<=4m has zero binomial coefficient modulo p. Indeed
p<=2s<2p, while j=p-s lies between 2m+1 and 3m, and its complement
2s-j=3s-p lies between 3m+2 and p-2. Thus the numerator factorial (2s)!
contains exactly one p factor and both denominator factorials contain
none. Therefore

    BOX: b_p=-(1/(9g))sum_(s=2m+1)^N
              binom(2s,p-s)4^(p-s)(-3)^(3s-p)/s.         (13)

The displayed high-s prefix tail vanishes by this proof, not by omission
or fitting. Formula (13) does not assert that the remaining b_p is zero.

The canonical derivative inversion of B is B-b_p x^p, with its literal
constant B(0)=J(0) fixed. At x=1/2, z(x)=1/2 and x^p=1/2, so

    (B-b_p x^p)(1/2)=tau/g-b_p/2.                        (14)

This cubic Frobenius correction is separate from the harmonic tail in
(10) and from the old odd-moment term 16^m. All are retained. Knowing
the derivative alone cannot set b_p to zero.

## 5. One genuine prescribed old forcing has a bilinear CM boundary

The old odd affine-weight identity contains the fixed forcing sum

    F_O=sum_(k=0)^(m-1) a_(k+1)s_O(k)/[54(2k+3)],
    L_O=154/81-2a_m16^m/27+F_O,                          (15)

where s_O is the unchanged two-phase source of the preceding paper.
Put i=k+1, and define the independent odd Gauss moments

    E_c(A)=sum_(i=0)^m a_i c^i/(2i+1).

Every denominator is at most 2m+1<p. Exact partial fractions give

    s_O(i-1)/[54(2i+1)]
       =4/3+4/[81(2i+1)]
             +2^(-i)[4i/3+2/9+8/(27(2i+1))].            (16)

Now use A(1)=1/g, A(1/2)=0, and
sum_i i a_i2^(-i)=A'(1/2)/2. Retaining the omitted i=0 constants yields

    BOX: F_O=4/(3g)+2A'(1/2)/3
                      +4E_1(A)/81+8E_(1/2)(A)/27-154/81. (17)

This is a derived dictionary for a genuine independently fixed source,
not a source selected from the desired scalar difference. Multiply
(17) by the actual C_*, and use the literal concomitant boundary (4).
Combining with (15) proves the new bilinear source comparison

    BOX: C_*[L_O+2a_m16^m/27-4/(3g)
                             -4E_1(A)/81-8E_(1/2)(A)/27]
                                           =8tau/(3g).  (18)

No inverse of C_* is used and no value is assigned to it. The old
16^m Frobenius correction is explicit. The remaining E moments are
independently defined and unevaluated; (18) is not the old scalar target.

## 6. Scope and independent verification

The new checker passed 46 exact checks and independently verifies the connected operator and adjoint
coefficients, Green sign, literal concomitant change, CM coefficient,
finite convolution coefficient dictionary, harmonic tail increment,
abstract finite prefix summation, exact old forcing partial fractions,
all constants in (17), the bilinear boundary in (18), and symbolic range
arithmetic behind the cubic factorial proof. No modular instance or old
checker is used. The proofs above provide the finite endpoint/unit scope.

The old reverse C constructor, reciprocal kernel, OLD-R, kappa, tau and
literal g remain fixed. The new dictionary supplies both actual tails
and one genuine bilinear CM source comparison. Neither the leftover E
moments nor the old A_X,R_X,E_X and OLD-R pairings are evaluated. The
unchanged scalar comparison, LIFT, weighted p^3, period normalization
and full native X6 remain OPEN.
