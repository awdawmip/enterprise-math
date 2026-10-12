# Fixed-C coefficient boundary dictionary and a genuine odd-source comparison

Status: ONE FOCUSED DIRECTED LOCAL AUXILIARY UNIT / NEW CONNECTED
COEFFICIENT, FROBENIUS-TAIL AND BILINEAR SOURCE LEMMAS PROVED / ORIGINAL
SCALAR COMPARISON OPEN. Prepared 2026-10-12 UTC.

Root owns Source custody, Driver review and mathematical direction. This
paper is local research, with no invented native Researcher, Task, Claim,
Run, accepted Result, or Source acceptance. Native identities of the local
author/helper are UNKNOWN. No prime, scalar fit, repeated campaign,
provider query, native write or Source mutation occurs. The arithmetic
models remain external finite classical observers, with native X6 and
separately typed time unchanged. All parent objectives remain OPEN.

The explicit old reciprocal C kernel and the old finite Gauss tau integral
were already proved. They are consumed here, not claimed anew. The new
step connects that fixed C to the exact Gauss coefficients used by the
prefix residual, computes the precise cubic x^p integration tail, and
compares the *actual prescribed odd forcing* to the same CM boundary.
The comparison keeps C(1/2) as a factor; it never divides by C or defines
it from a discrepancy. A second equivalent dictionary preserves the
double-prefix information in tau itself.

## 1. Frozen constructors and notation

Retain the existing conditional premises. Let p=6m+1 be prime in the
classes 13 or 19 modulo 24, N=3m=(p-1)/2, and work in F_p. Thus m>=2.
The literal Heun normalization remains

    h_0=h_N=g=binom(3m,m) != 0, sum h_n=1.

Throughout this paper g means that unit. The old p-adic reverse-Gauss
memo also uses the letter g for f_p(1/2), a different divisible scalar;
that older notation is not used here.

The original Gauss polynomial and fixed reverse carrier are

    V(w)=sum_(i=0)^m v_i w^i,
    v_i=(1/6)_i(1/3)_i/(i!)^2,
    D_G=w(1-w)partial_w^2+(1-3w/2)partial_w-1/18,
    D_G V=0,
    D_G*=w(1-w)partial_w^2+(1-5w/2)partial_w-5/9.

The independent C constructor is exactly the frozen descending recurrence

    c_N=0,
    r_j=-(-1)^(j+1)binom(N,j+1)/9,
    c_j=[(j+1)^2c_(j+1)-r_j]/[(j+2/3)(j+5/6)],
    C(w)=sum_(j=0)^(N-1)c_j w^j.                          (1)

Every divided factor is a unit for j<=N-1; its first zeros are j=4m
and 5m, outside the range. This solves all rows of
D_G*C=-[(1-w)^N-1]/(9w). It is independent of OLD-R, the residual,
and any value of tau.

The already proved shared kernel has d_j=(2/3)_j(5/6)_j/(j!)^2 and

    C(w)=sum_(r=1)^N (-1)^r binom(N,r)2^(2-r)D_r
                       sum_(j=0)^(r-1)d_j w^j,
    D_r=2^(r-1)(r-1)!^2/[18(5/6)_r(2/3)_r].

That reciprocal kernel is p-integral through r=N. Its use here does not
extend or change OLD-R, whose literal triangular constructor ends at
r<=i<=m.

The already fixed Gauss concomitant is

    K_G(w)=w(1-w)(CV'-VC')+(w/2)VC,
    K_G(0)=0, deg K_G<=4m<p,
    K_G(1/2)=C(1/2)V'(1/2)/4=-tau.                       (2)

In particular V(1/2)=0 is the retained CM0 premise. The original finite
integral and binomial double sum for tau are consumed as frozen inputs.
This paper does not choose a new normalization for either side of (2).

Three constructor files were full-read and verified against the SHA256
values recorded by their old independent reviews: the independent reverse
certificate, the finite adjoint Gauss paper, and the shared kernel paper.
The connection and preceding two local units were also full-read. Intake
verification preserves 67 deduplicated frozen paths. No old checker was
read or executed.

## 2. Connected Gauss coordinate and constant reverse forcing

Use the already proved terminating connection, including its literal g:

    V(w)=g A(1-w),
    A(z)=sum_(i=0)^m a_i z^i,
    a_i=(1/6)_i(1/3)_i/[(1/2)_i i!],
    A(0)=1, A(1)=1/g, A(1/2)=0.                         (3)

Reflect the fixed carrier, not its value: Cbar(z)=C(1-z). Direct chain
rule gives

    D_A=z(1-z)partial_z^2+(1/2-3z/2)partial_z-1/18,
    D_A A=0,
    D_A*=z(1-z)partial_z^2+(3/2-5z/2)partial_z-5/9,
    D_A*Cbar=(1-z^N)/[9(1-z)]=G_N(z)/9,
    G_N(z)=sum_(j=0)^(N-1)z^j.                           (4)

All divisions by 1-z in (4) are polynomial division. Flat-measure
adjunction gives the displayed D_A*, so this is an actual adjoint
dictionary for the existing a_i coefficient recurrence.

Writing Cbar(z)=sum_(j=0)^(N-1)cbar_j z^j yields the explicit constant-
forcing coefficient rows

    (j+1)(j+3/2)cbar_(j+1)
                 -(j+2/3)(j+5/6)cbar_j=1/9,
    cbar_N=0.                                           (5)

The same unit diagonal factors as (1) permit descending uniqueness;
thus solving (5) yields precisely C(1-z), with no extra seed. At the
actual top j=N-1=-3/2, the forward coefficient is zero, the diagonal
is 5/9, and cbar_(N-1)=-1/5. Nothing divides by the forward zero.

A useful explicit coefficient inverse of (5) is

    e_j=(2/3)_j(5/6)_j/[(3/2)_j j!],
    cbar_j=-e_j sum_(r=j+1)^N
                   (r-1)!(3/2)_(r-1)/[9(2/3)_r(5/6)_r]. (6)

Equivalently its summand is
2^(2-r)D_r(3/2)_(r-1)/(r-1)!. This is the unchanged reciprocal D
kernel with a new, directly derived weight. The denominators in e_j
are units through j=N-1; the first zero of (3/2)_j is at j=N. The
inner sum stops before that would become an inverse. Substitution in
the reverse row proves (6), including the actual last term r=N when
j=N-1. The separate convention cbar_N=0 does not introduce an undefined
e_N.

## 3. Bilinear CM boundary as a finite coefficient convolution

Define the actual connected concomitant

    J(z)=z(1-z)(Cbar A'-A Cbar')+(z-1)A Cbar/2.

The reflected original polynomial gives the exact global relation

    K_G(1-z)=-g J(z).                                    (7)

In particular J(1)=0 and J(0)=-C(1)/2. The all-coefficient Green identity
and (4) give

    J'=-A(z)G_N(z)/9,
    deg J<=4m<p,
    J(1/2)=C(1/2)A'(1/2)/4=tau/g.                       (8)

The sign in the CM derivative is explicit: V'(1/2)=-g A'(1/2).
No inverse of either derivative or of C is used.

Let J(z)=sum_(s=0)^(4m)kappa_s z^s. Coefficientwise integration in the
degree<p Gauss coordinate is legal and fixes all coefficients:

    BOX: kappa_s=-[sum_(i=max(0,s-N))^min(m,s-1) a_i]/(9s),
                              1<=s<=4m,
         kappa_0=-sum_(s=1)^(4m)kappa_s.                  (9)

All denominators are <=4m<p. The second equation is the *fixed original*
endpoint J(1)=0, not a value read from a target. It also agrees with
J(0)=-C(1)/2. At the top kappa_(4m)=a_m/6 is nonzero, since the coefficient
reduction 4m=-2/3 gives -a_m/(36m)=a_m/6.

The literal C boundary can therefore be expressed either as the bilinear
coefficient product from (6),

    tau/g=(1/2)sum_(i=1)^m sum_(j=0)^(N-1)
                                 i a_i cbar_j 2^(-(i+j)),

or as the finite Gauss convolution from (9),

    BOX: tau/g=(1/9)sum_(i=0)^m a_i
                      sum_(r=i+1)^(i+N)(1-2^(-r))/r.     (10)

Equation (10) follows by evaluating the same J at 1/2 and reindexing
s=i+j+1 in (9). Its range ends at m+N=4m<p, so no resonant denominator
has appeared or been canceled. This is a directly derived dictionary
for the pre-existing tau in the coefficient system of equation (24).

## 4. The exact cubic Frobenius integration tail

Return to the fixed cubic rho(x)=x(4x-3)^2. It obeys
1-rho(x)=(1-x)(1-4x)^2, and the original Heun polynomial is
y(x)=g A(rho(x)). Define the literal pullback of the fixed concomitant

    B(x)=J(rho(x))=-K_G((1-x)(1-4x)^2)/g.

It has degree 12m=2p-2. The canonical Gauss degree bound has been crossed:
over F_p its derivative cannot recover the x^p coefficient. Its actual
fixed endpoints are

    B(0)=kappa_0, B(1)=B(1/4)=0, B(1/2)=tau/g.            (11)

Write B(x)=sum_(q=0)^(2p-2)b_q x^q. The exact coefficient binomial
expansion from (9) is

    b_q=sum_(s<=q<=3s) kappa_s binom(2s,q-s)
                                  4^(q-s)(-3)^(3s-q).

At the only nonconstant derivative-kernel index q=p this gives

    BOX: b_p=sum_(s=2m+1)^(4m) kappa_s binom(2s,p-s)
                                  4^(p-s)(-3)^(3s-p).    (12)

For that entire range, s>=m+1, so the full prefix information in kappa is

    kappa_s=-[1/g-1_(s>N) S_(s-N-1)]/(9s),
    S_k=sum_(i=0)^k a_i.                                 (13)

This is an explicit coefficient tail, not an unspecified Frobenius
constant. In this particular coefficient it simplifies further. For
N+1<=s<=4m the binomial numerator (2s)! contains one p factor, while
both denominator factorial indices p-s and 3s-p are strictly below p;
also 2s<2p. Therefore binom(2s,p-s)=0 in F_p. Those high-s *terms*
vanish, without deleting the original prefixes from (9),(10). Thus

    BOX: b_p=-(1/(9g))sum_(s=2m+1)^(3m)
                      binom(2s,p-s)4^(p-s)(-3)^(3s-p)/s. (14)

Every s in (14) is a unit and every factorial is below p. This explicit
finite sum is retained; no claim that its value is zero or nonzero is
made here.

The derivative source is fixed by (8):

    B'(x)=-A(rho(x))G_N(rho(x))rho'(x)/9.

Its x^(p-1) coefficient is zero, since it is the derivative of the
literal B. Let P_B be the coefficientwise primitive of that source with
zero constant and zero x^p coefficient, in degree <=2p-2. Explicitly it
integrates every coefficient except the absent resonant one; all remaining
denominators q are units. The kernel in that degree range consists exactly
of a constant and an x^p term. Hence the complete dictionary is

    B(x)=kappa_0+P_B(x)+b_p x^p,
    BOX: tau/g=kappa_0+P_B(1/2)+b_p/2.                    (15)

The factor 1/2 is the actual base-field Frobenius (1/2)^p=1/2. The
same polynomial in the self-adjoint t coordinate, x=t^2, has the term
b_p t^(2p). Equations (12)-(15) supply the missing normalization that
cannot be recovered by differentiating the old composed concomitant
and deleting multiples of p. They do not introduce a new C or tau.

## 5. A second dictionary retaining the double-prefix source

For 0<=i<=m define the actual finite harmonic tail

    ell_i=sum_(r=i+1)^(i+N)(1-2^(-r))/r,
    ell_0=H_N(1)-H_N(1/2).

All indices are between 1 and 4m<p. Only the two new endpoints change
when i advances, so

    ell_i-ell_(i-1)
      =(1-2^(-(N+i)))/(N+i)-(1-2^(-i))/i.

Using the residue N=-1/2 and the retained marked branch 2^(-N)=-1 gives
the small exact increment

    d_tau(i)=[1+(4i-1)2^(-i)]/[i(2i-1)], 1<=i<=m.         (16)

There is no extension of a harmonic prefix past p. In particular

    ell_i=ell_0+gamma_i,
    gamma_i=2O_i(1)-H_i(1)+2O_i(1/2)+H_i(1/2).

The lower-case gamma_i is a new independently derived harmonic kernel,
distinct from the old repaired observer Gamma(a). Apply (10) and exact
finite summation by parts, using sum a_i=1/g:

    M_tau=sum_(k=0)^(m-1) S_k d_tau(k+1),
    BOX: 9tau=ell_m-g M_tau.                             (17)

Every S prefix and both i=0,m endpoints are retained. This converts the
literal tau boundary into the *same fixed double-prefix weight* that
occurs in the preceding Gauss comparison, rather than replacing S by a
rational multiple of a or repeating the ruled-out two-carrier ansatz.

For an explicit last tail put L_full(c)=sum_(r=1)^(p-1)c^r/r. The finite
complement r=p-s, together with the pairwise identity H_(p-1)(1)=0, gives

    H_(4m)(1)=H_(2m)(1),
    H_(4m)(1/2)=L_full(1/2)+(1/2)H_(2m)(2).

The second identity retains the Frobenius coefficient (1/2)^p=1/2.
Consequently

    BOX: ell_m=H_(2m)(1)-H_m(1)-L_full(1/2)
                          -(1/2)H_(2m)(2)+H_m(1/2).       (18)

No r=p denominator occurs. The previously fixed identity
L_full(1/2)=q_2 may be consumed to simplify this expression, but it is
not needed here. The cubic derivative-kernel tail b_p in (15) and the
finite-log complement tail in (18) are distinct corrections, both
explicitly retained.

## 6. Genuine comparison of the prescribed odd forcing with C/tau

The preceding unit's actual odd affine-weight sum and forcing are

    L_O=sum_(k=0)^(m-1)a_k(k+1/6)V_k,
    F_O=sum_(k=0)^(m-1)a_(k+1)s_O(k)/[54(2k+3)],
    L_O=154/81-2a_m16^m/27+F_O.                           (19)

The last term -2a_m16^m/27 is the separately proved degree-p odd-moment
boundary. It is retained throughout this calculation; no undefined V_m
is introduced.

Define independent legal coefficient moments of A by

    E_c(A)=sum_(i=0)^m a_i c^i/(2i+1), c=1 or 1/2.

Their denominators are <=2m+1<p. Reindex i=k+1 in the *fixed* F_O and
perform the exact rational partial fraction identity

    s_O(i-1)/[54(2i+1)]
      =4/3+4/[81(2i+1)]
         +2^(-i)[(4/3)i+2/9+8/[27(2i+1)]].              (20)

Sum each term using A(1)=1/g, A(1/2)=0 and
sum i a_i2^(-i)=A'(1/2)/2. The i=0 omissions contribute the fixed
constant -154/81. This proves a genuine evaluation of the actual source:

    BOX: F_O=4/(3g)+(2/3)A'(1/2)
                  +(4/81)E_1(A)+(8/27)E_(1/2)(A)-154/81. (21)

No OLD-R or tau value entered this partial-fraction calculation. Combining
(19),(21), define the independently specified odd boundary observer

    B_CM=L_O+2a_m16^m/27-4/(3g)
                         -(4/81)E_1(A)-(8/27)E_(1/2)(A).

It has the proved identity B_CM=(2/3)A'(1/2). Multiply by the actual
fixed C_*=C(1/2)=Cbar(1/2) and use (8). The new bilinear endpoint lemma is

    BOX: C_* B_CM=8tau/(3g),
         6tau=(9g/4)C_* B_CM.                            (22)

This is the requested source-to-boundary comparison: it takes the
prescribed forcing appearing in the old equation (24), keeps its known
Frobenius top correction, and derives its bilinear CM pairing with the
independent reverse carrier. It does not assume C_* is a unit. It remains
valid when C_*=0. The C factor and the double-prefix dictionary (17) are
both retained, rather than discarded to force a rational scalar comparison.

## 7. Exact successor residual and bounded remaining scope

Let B_H,B_O,M_R denote precisely the independently fixed quantities in
the preceding frozen equation (24); in particular M_R retains the
unchanged OLD-R increment with r=1,m endpoints. That open comparison is

    g(B_H+B_O)+2M_R=kappa+T_m+2W_m/g+6tau.

Substitute the proved bilinear boundary (22), without changing the
target or assigning any value from its discrepancy. The exact successor is

    BOX: g[B_H+B_O-(9/4)C_* B_CM]+2M_R
                                 =kappa+T_m+2W_m/g.      (OPEN) (23)

Alternatively, the preserved double-prefix dictionary (17) gives

    BOX: g[B_H+B_O+(2/3)M_tau]+2M_R
                    =kappa+T_m+2W_m/g+(2/3)ell_m.         (OPEN) (24)

These are two proved reformulations of the original fixed scalar
residual, not proofs of its zero. Each symbol has an independent
constructor before the comparison. The remaining substantive lemma is
to relate the actual moment/prefix sources in B_H,B_O and the literal
reciprocal-D source M_R to either the bilinear C_* B_CM or the explicit
tau double-prefix source, with the same endpoints. No value of those
remaining sums is supplied here and no nonzero scalar residual is proved.

All literal g factors, the Heun/Gauss finite defects, the degree-p odd
source correction, the cubic b_p correction, and the independent tau
normalization remain in their appropriate dictionaries. The earlier
universal rational two-carrier obstruction is not re-searched, enlarged,
or promoted into a finite-field no-go. LIFT, weighted p^3, raw period
normalization and full native X6 propagation remain OPEN.

## 8. Checks and custody

The new main script passes 95 exact checks: reflected operators and
adjoint coefficients, Green and original-concomitant signs, constant-
forcing reverse rows and top coefficient, generic coefficient convolutions
and cubic binomial coefficients, exact tail bounds, harmonic increments,
formal double-prefix summation by parts, actual odd-forcing partial
fractions, the bilinear source normalization, and both successor residual
signs. The generic rational polynomial examples use unrelated degrees
(M,N)=(1,2),(2,4),(3,5); no p=6m+1 is instantiated for those checks and
no target scalar is evaluated.

The independent helper consumes the same fixed old constructors, verifies
the connected dictionary, harmonic/Frobenius tails and source comparison,
and saves its own 46 PASS checks and pins in independent-check. The source
comparison was reached independently; formulas were exchanged during the
unit, so this is directed collaborative verification, not blind final
peer review. Neither checker imports or executes an old checker.

Frozen byte pins are checked again after writing. All output is local
research for Root's separate Driver review and Source custody. No native
claim or accepted operational completion is asserted.
