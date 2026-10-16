# A power-scale raw COMMON coefficient band from actual full-carrier translations

AUTHOR WHOLE WORKING / UNREVIEWED. One complete proposed theorem, not
separate papers for its component lemmas. Authors: EM-PUBLIC-7CDA51,
EM-DVR-BFF6DC and EM-DIRECT-88303D, with actual contributions in the context.
All earlier author/review exposure remains NONBLIND. Author crosschecks
are not independent review. No future nonauthor has received this working.

All derivations are symbolic hand proofs. Zero programmed scientific
matrix/coefficient evaluations, samples, solvers, imports/tests, consumers
or Native operations were used. No Task or budget reset is implied; old
STOP/HOLD and formal budgets UNKNOWN remain. Original real-state and
partial-work HOLD manuscripts are unchanged.

## 1. The proposed exact coefficient statement and accepted inputs

Let m>=2^1000 be an integer. Retain the ORIGINAL COMMON polynomial and
original positive Student carrier of polynomials in v of degree<=m-2,
dimension m-1 and weight(1+4v^2)^(-m). Let P_k be monic orthogonal,
h_k=||P_k||^2, Dv=d/dv, n the largest even integer<=m-2, t=m-n in{2,3},
ell=n-1 and q=2ell. Set

 W=m^2, d=W-3, Dold=W-1, K=m^(2W)/2,
 H_n=n!sqrt(h0/h_n), Cxi=H_n/(2pi)^n,
 A_n(a)=Cxi*a^ell for a>0,
 Dbin=d-q, Jbin=j-q, y=Dbin/Jbin.

**Theorem proposed.** For every integer j in the entire range

 q+ceil(Dbin/m^(1/100))<=j<=q+floor(Dbin/2),            (R1)

the SAME original degree-d raw homogeneous COMMON layer satisfies

 [S^(d-j)a^j]H_d^raw
 >=K binom(d,j) Cxi^2 h_q 2^-41 m^6 (pi*y)^(-12)>0,
 h_q=(j)_q,fall/(d)_q,fall.                           (R2)

A weaker explicitly rational lower expression is

 K binom(d,j) H_n^2 h_q
                 2^(-6n-65) m^6 (Jbin/Dbin)^12.     (R3)

The exact old norm ratios express H_n^2=n!^2 h0/h_n as a finite positive
rational product. No program expands these enormous symbolic quantities.
This is a power-scale coefficient band, not all-j, the whole C1 polynomial,
physical P1 positivity, the original trace inequality or the mother Goal.
Old smaller-m/stronger-margin papers keep their separate domains.

The original coefficient interface, including ALL corrections, is

 H_d^raw=K(S+a)^d Psi(a/(S+a)),
 Psi=C-g(B+2)+alpha[Dold(Dold-1)B-(2Dold-1)E_xi B+E_xi^2 B],
 B=b+W-1, b=tr(R^2), R=Z+Z#,
 C=2tau tr(A_e[Z,R])-4tau tr(A_e R),
 E_xi=xi partial_xi, alpha=(W+1)^2/(8W),
 tau=(m^4-1)/(24m), g=m*tau=(W^2-1)/24.                (1)

Precisely, L_(d,j)(xi^k)=(j)_k,fall/(d)_k,fall for0<=k<=d,
and [S^(d-j)a^j]H_d^raw=K binom(d,j)L_(d,j)Psi. All degrees of
Psi used below are<=q<=d, apart from its degree-zero correction.

Here A_e is the SAME old fixed compressed multiplier, ||A_e||op<=4 and
||A_e||HS<=4sqrt(m-1). The original fixed-r0 differentiation took place
before variable substitution. The unequal COMMON prefactors are retained
in alpha; B+2 contains W+1. The actual frame is

 Z_xi=Z0-2 sum_even k=2..n zeta(k)xi^(k-1)Dv^k/(2pi)^k,
 Z0=vDv-(m-1/2)I.

A dagger denotes the original positive Hermitian adjoint. The analytic
coefficientwise operation F#(u)=F(conjugate(u))^dagger takes the adjoint
of every coefficient and leaves the analytic variable unchanged. On the real axis R is the actual self-adjoint
state. The original rational COMMON expression has real coefficients.
Define finite reversed polynomials

 V(u)=u^ell Z_(1/u)/Cxi, U=V+V#,
 Q(u)=tr(U(u)^2)=u^q b(1/u)/Cxi^2,
 L(u)=u^ell/Cxi, P(u)=u^q Psi(1/u)/Cxi^2.              (2)

The load-bearing exact old input is the fully consumed23366-byte bulk
primary at Sourcecfd876cb9bda189b8978f23d7855a9e66a862a44, path
research_notes/owner_goal_20261016/parity_joint_bulk_raw_layer_7cda51_bff6dc/
PARITY_COMMON_LOWER_LAYER_UNIFORM_BULK_RAW_COEFFICIENT_BAND_JOINT_AUTHOR.md,
SHA25658af3cc47f58d63419c7cd23e5853e1add19810ada0548336e7afa0518a212b9,
blobc8f9f6dde9e4e6939d181afdf7f6092a09d12a1c. We reuse its actual frame,
monic moments/norms, derivative-only B13, COMMON formula and A_e/Z0 norm
facts, not its fixed-xi coefficient conclusion outside its domain.

The accepted REAL state input is the genuine whole theorem at author
Source98b1f4b3075da2afab249b85375e73f883ae710e and truepeer
Source88c190aba4414288c908a43ece9abec138ae742d. All three current authors
personally consumed those five immutable Sources, with exact differences.
It gives for real2<=y<=m^.01 the precise normalized consequence

                         Q(y)>=2^-24(pi*y)^(-12)>0.  (3)

Indeed its amplitude is A_n(1/y)=Cxi*y^-ell, which cancels EXACTLY in(2).
That accepted input alone gives no coefficient sign. All NEW full-carrier,
complex, global and functional steps needed for(R2) are proved below.

## 2. A local full-carrier single-pole bound, not a scalar substitute

Put U1(xi)=xi Dv^2[(2pi)^2I-xi^2 Dv^2]^(-1); the inverse is finite by
the original nilpotent cutoff. Denote the parameter domain by

 m>=2^1000, 1<=|z|<=4m^.01, |Im z|<=1.               (S2)

We prove on this domain

 ||U1(pi/z)||HS<=2^17 A_n(pi/|z|).                   (S3)

In the following proof Wamb is an AMBIENT space, not the scalar W=m^2;
Camb is its common basis norm, not the C in(1); Tcal is a translation
integral, not the scalar Q in(2). The notation Chat_n is explicitly
separate from Cxi. No actual carrier is replaced by an ambient equality.

### S2. A legitimate ambient HS upper bound, not a carrier replacement

Write Vspace for the original degree<=m-2 carrier, as distinct from the
reversed matrix polynomial V(u). Put N=m-1 and let Wamb be degree<=N
with the SAME Student inner product.
For0<=r<=N set

 f_r(v)=(v-i/2)^r(v+i/2)^(N-r).

The old exact circle substitution y=(v-i/2)/(v+i/2) makes these mutually
orthogonal with COMMON squared norm

                         Camb=(pi/2)4^(-N).             (S4)

Indeed |f_r|^2w_m=4^(-N)/(1+4v^2), and cross terms integrate nonconstant
circle characters against the uniform Cauchy angular measure.

For complex s define the finite translation T_s=e^(sDv):
(T_s f)(v)=f(v+s). It preserves Vspace and Wamb. Therefore

             ||T_s|Vspace||_HS<=||T_s|Wamb||_HS.             (S5)

This is only an inequality, obtained by extending an orthonormal basis of
Vspace by its one-dimensional orthogonal complement. No actual vector or
rank-one correction has been deleted or identified with the ambient one.
We do not claim an equality or use an ambient adjoint as the actual dagger.

Write s=x0+iy0, y=|y0|, u=|s|, so x0^2+y^2=u^2.
Here x0 is a local real-part coordinate, not the polynomial variable xi. The two factors satisfy

 |v+s-i/2|^2, |v+s+i/2|^2
                   <=(v+x0)^2+(y+1/2)^2.

Consequently the complete ambient HS sum obeys

 ||T_s|Wamb||_HS^2
 <=(2m/pi) integral_R
   [1+4(v+x0)^2+4y^2+4y]^N/(1+4v^2)^(N+1) dv.        (S6)

All m input basis vectors were summed; this is not m^2 individual entry
counting. The integral is a paper identity/inequality, not an evaluation.

Put 2v=tan(theta). Cancellation of the powers of cos(theta) transforms
the integral into one full angular period. With

 a=1+2(u^2+y), b=2sqrt((u^2+y)^2+x0^2), S=a+b,
 rho(s)=sqrt(S),

(S6) is

 ||T_s|Wamb||_HS^2 <=m/(2pi)
                  integral_(-pi)^pi (a+b cos theta)^N dtheta.  (S7)

A rotation of the angular coordinate is allowed over the complete period.
Here a^2-b^2=(1+2y)^2>0, so the integrand is nonnegative.

For real s equality holds in(S6), and(S7) equals m P_N(1+2s^2), if one
uses the classical Legendre name. That name is optional and is not a new
primary import or a proof premise. We only use the explicit integral.

### S3. Angular Gaussian control with the needed m^1/4 prefactor

If u>=1, write v0=u^2+y>=1. Then b>=2v0, a=1+2v0 and

 delta=b/(a+b)>=2v0/(1+4v0)>=2/5>=1/4.

For |theta|<=pi, 1-cos(theta)>=2theta^2/pi^2. Since a>b,

 (a+b cos theta)^N
 =S^N[1-delta(1-cos theta)]^N
 <=S^N exp[-N theta^2/(2pi^2)].

The elementary Gaussian integral gives

 (1/(2pi))integral_(-pi)^pi exp[-N theta^2/(2pi^2)]dtheta
 <=sqrt(pi/2)/sqrt(N)<2/sqrt(N).

Using N>=m/2 in(S7), we get the actual uniform translation bound

          ||T_s|Wamb||_HS<=2m^(1/4)rho(s)^N, u>=1.       (S8)

For every u>=0 the coarser full-period maximum gives

                   ||T_s|Wamb||_HS<=sqrt(m)rho(s)^N.     (S9)

For u>0 the explicit quadratic also gives

 S=1+2(u^2+y)+2sqrt((u^2+y)^2+x0^2)
 <=4u^2+4y+2.

The last step uses sqrt(v0^2+x0^2)<=v0+x0^2/(2v0) and x0^2<=u^2<=v0.
At u=0 the same bound is immediate. Along any fixed direction,
rho(u e^(i phi)) is nondecreasing in u, since both a and b are.
Writing sigma=|sin phi|, for u>0,

 rho(u e^(i phi))^N
 <=(2u)^N exp[N sigma/(2u)+N/(4u^2)].                 (S10)

### S4. The exact finite Laplace identity for the single pole

For any complex xi the matrix exponential is a finite polynomial on Vspace.
Termwise elementary integration integral_0^infinity e^-v v^k dv=k!
therefore proves, without an infinite matrix-series convergence issue,

 Tcal(xi):=integral_0^infinity e^-v
       [T_(xi v/(2pi))+T_(-xi v/(2pi))]/2 dv
       =sum_(k even>=0) (xi Dv/(2pi))^k,
                       U1(xi)=(Tcal(xi)-I)/xi.         (S11)

The right sum has the true finite cutoff. It retains all even derivative
terms and all actual inputs, including the odd top input when present.

Let Z=|z|, xi=pi/z, mu=2Z, phi=-arg(z), gamma=|Im z|<=1.
After v=mu u, the shifts in(S11) are +/-u e^(i phi), with
sigma=gamma/Z. The two signs have the same bound in(S7)-(S10).
By the ordinary triangle inequality for the genuine HS norm,

 ||Tcal|Vspace||_HS<=mu integral_0^infinity e^(-mu u)
                          ||T_(u e^(i phi))|Wamb||_HS du. (S12)

The signed/complex polynomial integral has not been replaced by a claim
of functional positivity. This is a valid upper bound on its norm.

### S5. Saddle-scale split with no exp(CZ) loss

Choose T=N/(4mu)=N/(8Z). Under(S2),

 T>=m^.99/64>1, 16Z^2/N<=512m^(-.98)<1.               (S13)

For u>=T, the exponent in(S10) satisfies

 N sigma/(2u)<=4gamma<=4,
 N/(4u^2)<=16Z^2/N<=1.

Thus rho^N<e^5(2u)^N<2^8(2u)^N. Applying(S8) to the tail of(S12),

 I_tail<=2^9 m^.25 mu integral_0^infinity e^(-mu u)(2u)^N du
       =2^9 m^.25 Gamma(m)/Z^(m-1).                  (S14)

In the early interval0<=u<=T, use monotonicity, (S9), and the same estimate
at T. Since mu integral_0^T e^(-mu u)du<=1,

 I_early<=2^8sqrt(m)(2T)^N
         =2^8sqrt(m)(N/(4Z))^N.                     (S15)

Put G=m^.25 Gamma(m)/Z^(m-1). The elementary factorial bound
N!>=(N/3)^N gives

 I_early/G<=2^8 m^.25(3/4)^N<=2^8.

For the last inequality, log_2m<=m/16 for m>=256 (check the value at256
and the positive derivative), and
log(4/3)>=1/4 by log(1+x)>=x/(1+x). Hence

 m^.25(3/4)^N<=2^(m/64-N/4)<=1,

using N>=m/2. These are explicit estimates, not a claimed asymptotic saddle
formula. Combining(S14)-(S15) yields

               ||Tcal|Vspace||_HS<2^10 m^.25 Gamma(m)/Z^(m-1). (S16)

This is the point where the earlier absolute derivative majorant's exp(CZ)
is avoided. It is not an optimization of that exponential constant.

### S6. Exact amplitude comparison from the actual monic norm ratios

Let alpha_k=m-k-1/2, B_k=binom(2m-1,k). The actual old norm identity is

 h_k/h_(k-1)=k(2m-k)/[16alpha_k(alpha_k+1)].

Define a_k=4^k sqrt(h_k)/(k!Gamma(alpha_k)).
Then a_k^2/a_(k-1)^2
=(2m-k)alpha_k/[k(alpha_k+1)], so telescoping gives

 a_k^2=Cnorm alpha_k B_k,
 a_0 b_n=sqrt((m-1/2)(t-1/2)/B_n),

where Cnorm=a_0^2/(m-1/2) is a separate telescoping constant, not
the ambient common norm Camb, and b_n=n!Gamma(t+1/2)/(4^n sqrt(h_n)).
This is the same normalization as the earlier exact Green entry, but
here it has been derived directly from the old norm ratio. It implies

 A_n(pi/Z)
 =2^n Gamma(m-1/2)/[pi Gamma(t+1/2)Z^(n-1)]
        sqrt((m-1/2)(t-1/2)/B_n).                    (S17)

An elementary central-binomial estimate is

 binom(2m,m)<=4^m/sqrt(3m+1).

To prove it, divide by4^m and induct. The squared ratio inequality is
(2m+1)^2(3m+4)<=(2m+2)^2(3m+1); the right minus left is m>=0.
Since B_n<=binom(2m-1,m-1)=binom(2m,m)/2, it follows that

 B_n<=2^(2m-1)/sqrt(3m+1).

Cauchy-Schwarz in the defining positive Gamma integral gives

 Gamma(m)^2<=Gamma(m-1/2)Gamma(m+1/2)
            =(m-1/2)Gamma(m-1/2)^2.

Substitute both inequalities into(S17). Since n=m-t,

 A_n(pi/Z)
 >=[2^(.5-t)sqrt(t-.5)/(pi Gamma(t+.5))]
                (3m+1)^.25 Gamma(m)/Z^(n-1)
 >=2^-6 m^.25 Gamma(m)/Z^(n-1).                      (S18)

For t=2,3 the numerator factor2^(.5-t)sqrt(t-.5)>1/4,
while pi<4 and Gamma(t+.5)<4, proving the last explicit constant.

We also need to absorb the I in(S11), so recheck a coarse amplitude bound
on the slightly wider domain(S2), not just the earlier real xi interval.
Monic minimization and the exact old Student moment give h_n/h0<=4^-n.
Therefore

 A_n(pi/Z)>=n!/[pi Z^(n-1)]
          >=n!m^(-(n-1)/100)/4^n
          >=m^.01[m^.49/8]^n>=4^n>=m^3.              (S19)

Here n!>=(n/2)^(n/2), n>=m/2, m>=2^1000. The last comparison uses
4^n>=2^m>=m^3 and the same log_2m<=m/16 inequality. The new complex modulus
domain has thus been checked explicitly; no fixed-domain lower bound was
extended by fiat.

### S7. Full-carrier bound and normalized analytic form

From(S11),(S16) and ||I|Vspace||_HS=sqrt(m-1),

 ||U1(xi)||_HS
 <=Z/pi [2^10 m^.25 Gamma(m)/Z^(m-1)+sqrt(m)].

Dividing by(S18), its first term is at most
2^16 Z^(1-t)/pi<=2^16 because Z>=1 and t=2 or3.
By(S19) the second term divided by A_n is at most

 Z sqrt(m)/(pi A_n)<=4m^(-249/100)<1.

This proves the actual full-carrier claim(S3). Every original parity and
all actual inputs remain in the norm. We never identified a triangular
rank-two Green kernel with a rank-two matrix or dropped the coherent sum
within the single pole.

There is a useful exact normalized polynomial, with
Chat_n=H_n/(2^n pi)=pi^ell*Cxi>0 and ell=n-1:

                 Ucal_m(z)=z^ell U1(pi/z)/Chat_n.       (S20)

Since the largest even derivative is n, this is a finite even matrix
polynomial, not a singular function at0. Also
A_n(pi/|z|)=Chat_n/|z|^ell. Thus(S3) is exactly

                   ||Ucal_m(z)||_HS<=2^17            (S21)

on(S2). In particular every disk |z-z0|<=1/2 with real
pi<=z0<=pi*m^.01 lies in(S2): its modulus is>1 and is<4m^.01,
and its imaginary part is<=1/2. Vector-valued Cauchy on these disks gives

 ||partial_z^r Ucal_m(z0)||_HS<=2^(17+r)r!, r>=0.     (S22)

This is normalized local control, not a falsely bounded derivative of
the unnormalized U1 without its amplitude derivative. The coefficient-functional proof below uses this exact normalization
and domain.


## 3. Full-matrix zeta removal and analytic reversal

The independent scalar mean remainder is not enough here. Define

 W_xi=Z_xi-(Z0-2U1(xi))
   =-2 sum_even k=2..n (zeta(k)-1)xi^(k-1)Dv^k/(2pi)^k.

The accepted old B13 is a FULL-carrier derivative estimate, with all input
degrees through m-2 and the odd-top factorial endpoint retained. For
j=n-k,c0=2t-1 in{3,5}, it gives

 ||Dv^(n-j)||HS^2/H_n^2<=2^20sqrt(m)4^j/(2j+c0)!,
 ||Dv^(n-j)||HS/H_n<=2^10m^.25 2^j/j!.               (Z1)

It is independent of xi. For any nonzero complex xi assume the NATURAL
condition v0=4pi/|xi|<=m/128. Dividing after differentiation by
A_n(|xi|), E_xi^r multiplies the actual kth term by(k-1)^r, so r=0,1,2
simultaneously obey

 ||E_xi^r W_xi||HS/A_n(|xi|)
 <=2^11m^(9/4) sum_even k=2..n
                (zeta(k)-1)v0^(n-k)/(n-k)!.         (Z2)

This differentiates W, not W/A_n. For k>=3, integral comparison yields
zeta(k)-1<=2^(1-k); for all k>=2 separately zeta(k)-1<1. Put j0=n/2>=m/3.
For high k>=n/2, enlarge only the nonnegative majorant to obtain

 High<=2^12m^(9/4)2^(-n/2)e^v0<=2^(-m/4).           (Z3)

Explicitly log_2m<=m/16 for m>=256, n>=m-3 and e^v0<=2^(m/64), so its
base-two logarithm is at most27/2-11m/32<=-m/4. The log bound holds at256
and thereafter by derivative1/16-1/(m log2)>=1/16-2/m>=0.
For low k<n/2, use j=n-k>=j0 and the factorial bound j!>=(j/3)^j.
The first term v0^j0/j0!<=(9/128)^j0<(1/8)^j0<=2^-m and the subsequent
ratio is<=3/128<1/2. Thus

 Low<=2^12m^(9/4)2^-m<=2^(-m/2).                    (Z4)

Here the last logarithmic bound is12-55m/64<=-m/2. We used k=2 only in
this low part with zeta(k)-1<1, not an invalid high-k tail inequality.
Both branches are full-HS majorants, not concentration assumptions.
Consequently B_m:=2^(-m/4)+2^(-m/2)<=2^(1-m/4) bounds(Z2).

Set V_W(u)=u^ell W_(1/u)/Cxi. Every term is a matrix times u^(n-k), so
this is an entire finite matrix polynomial. For u!=0,

 E_u^r V_W=u^ell(ell-E_xi)^r W_xi/Cxi, xi=1/u.        (Z5)

The amplitude cancels exactly because A_n(1/|u|)=Cxi|u|^-ell. Expanding
(ell-E_xi)^r loses at most(ell+1)^r<=m^2. On the entire disk
|u|<=m/(512pi), polynomial continuity includes zero and gives

 ||E_u^r V_W||HS<=m^2 B_m,
 ||E_u^r(V_W+V_W#)||HS<=2m^2 B_m
             <=2^(2-m/8)<=2^(-m/100), r=0,1,2.       (Z6)

The same final bound holds for V_W alone. The coefficientwise # identity
E_xi^r W#(xi)=(E_xi^r W(conjugate(xi)))^dagger is used, not a moving
complex dagger. The final comparison holds for m>=18. In particular the
disk |u|<=4m^.01 is included, since m^.99>=2^990>2048pi.

## 4. The actual local outer disk is now supplied

Fix2<=y<=m^.01. On |u-y|<=1/4, put z=pi*u. Then |Im z|<=pi/4<1,
|z|>=7pi/4>1 and |z|<=pi*m^.01+pi/4<4m^.01. One elementary sufficient
rational bound is pi<52/15<7/2, from integrating
1/(1+x^2)<1-x^2+x^4 on[0,1]; also pi>2. These inequalities explicitly
justify the spare room at the domain endpoint: m^.01>=2^10 gives
pi(m^.01+1/4)<(7/2)(1+1/(4*2^10))m^.01<4m^.01.
The normalization in section2 is EXACTLY

 u^ell U1(1/u)/Cxi=Ucal_m(pi*u).

The S19 amplitude estimate also gives A_n(1/|u|)>=m^3 on this larger
disk. The correct full baseline is ||Z0||HS<=2m sqrt(m-1), hence its
normalized contribution is<1. With(Z6) and the factor-2 in Z, we obtain

 sup_|u-y|<=1/4 ||V(u)||HS<=2^19,
 sup_|u-y|<=1/4 ||U(u)||HS<=2^20.                    (H)

For the second bound the disk is invariant under complex conjugation,
so V# has the same norm bound. This proves(H) on the ACTUAL full carrier;
it is not imported from a two-channel lower bound or CF's fixed-order
complex lemma. All original input degrees and compression effects remain.

## 5. Full original Psi: local point margin and complex bound

From(3),(H) and the actual COMMON formula we prove

 P(y)>=2^-40m^6(pi*y)^(-12),                          (4)
 sup_|u-y|<=1/8 |P(u)|<=2^100m^6.                   (5)

The following derivation retains the exact C linear term, W+1 and both
COMMON prefactors. In this section Cn means Cxi, and all former conditional
outer-disk references refer to the actual proved(H) above.

### L3. Exact Euler reversal, including the constant-only term

The b part in(1) obeys the exact identities

 (u^q/Cn^2)(E_xi b)(1/u)=(q-E_u)Q,
 (u^q/Cn^2)(E_xi^2 b)(1/u)=(q-E_u)^2Q.              (6)

These follow by differentiating b(xi)=Cn^2 xi^q Q(1/xi), with Cn fixed
in xi. Thus neither a derivative of Cn nor a dropped Euler shift is
allowed. The original Euler polynomial factors exactly as
(Dold-E_xi)(Dold-1-E_xi). Writing a=Dold-q, its reversed action is
(a+E_u)(a-1+E_u)Q, equivalently

                   a(a-1)Q+2a*u*Q'+u^2 Q''.         (7)

The factorization and expanded version also agree by direct multiplication:
the intermediate E_u coefficient is2a-1, and E_u^2Q=uQ'+u^2Q''.
7CDA supplied the same factorization during this coauthor derivation;
it is a shared author interface, not an independent verification.

For the full C, reversing its quadratic and linear terms separately gives

 Cstar(u)=u^q C(1/u)/Cn^2
       =2tau tr(A_e[V,U])-4tau L tr(A_e U).          (8)

In particular the linear term still has its single L factor. Substitution
of (6)--(8) in the ENTIRE(1) gives the identity

 P=[alpha*a(a-1)-g]Q
       +alpha[2a*u*Q'+u^2Q'']+Cstar+K0 L^2,         (9)
 K0=alpha Dold(Dold-1)(W-1)-g(W+1)
    =(W-1)(W+1)^2(3W^2-10W+6)/(24W).               (10)

Equation(10) is the complete constant-only correction, including the
exact lower W+1 counterterm. It was NOT omitted as a derivative or
placed in an arbitrary adverse error. For W>=3 it is nonnegative:
3W^2-10W+6=3(W-3)^2+8(W-3)+3>0. On the real center y, L(y)^2>=0,
so this complete contribution HELPS the point margin. On a complex disk
we use its magnitude, not a sign. Also 0<=K0<=m^8, because the original
positive term in(10)'s first line is at most alpha*W^2*(W-1)<=W^4;
alpha<=W for W>=1 and g(W+1)>=0.

### L4. Cauchy bounds and the true baseline scaling on the larger disk

On the outer disk(H), analytic HS Cauchy--Schwarz gives

                         |Q(u)|<=||U(u)||HS^2<=2^40.

For every |u-y|<=1/8 the circle of radius1/8 about u stays inside that
outer disk. The genuine Cauchy derivative bounds therefore give

                         |Q'|<=2^43, |Q''|<=2^47.   (11)

Only the outer disk supplies these derivatives. A real point lower
bound or a fixed-output scalar formula alone would not justify them.

We also need a separate, actual bound on L throughout the outer disk.
There |u|<=y+1/4<=2m^.01. The exact old Student moment/minimizer
comparison, also proved in the real-state primary, gives
h_n/h0<=4^-n and hence Cn>=n!/pi^n>=n!/4^n. Thus for u!=0,

 A_n(1/|u|)=Cn/|u|^ell
    >=2m^.01 n!/(8m^.01)^n
    >=2m^.01 [m^.49/16]^n>=4^n>=m^3.                (12)

Here n!>=(n/2)^(n/2), n>=m-3>=m/2 and m^.49/16>=2^486>4.
The final4^n>=m^3 follows from2n>=m and log_2m<=m/16 for m>=256;
that elementary log bound is true at256 and increasing thereafter.
Consequently |L(u)|<=m^-3 everywhere on the outer disk. This explicitly
rechecks the slightly enlarged complex-radius domain rather than
extending the old real-state xi endpoint by fiat. The local disk does
not meet zero; polynomial continuity would in any event cover u=0.

By the actual A_e bounds and positive-HS matrix inequalities,

 |tr(A_e[V,U])|<=2||A_e||op ||V||HS ||U||HS,
 |tr(A_e U)|<=||A_e||HS ||U||HS.

Since tau<=m^3, (8),(H),(12) give on the full outer disk

 |Cstar|<=16tau ||V||HS||U||HS
                +16tau sqrt(m)|L| ||U||HS
         <=2^43m^3+2^24sqrt(m)<=2^44m^3.             (13)

This retains BOTH the commutator and the linear trace term, with the
original compressed multiplier. No whole-HS bound||Z0||<=2m is used.

### L5. Complete local real point margin

Since q=2(n-1)<=2m-6,
a-1=m^2-2-q>=m^2-2m+4>=m^2/2, and a<=m^2.
Also alpha>=m^2/8 and g<=m^4/24. Thus

                  alpha*a(a-1)-g>=m^6/64,            (14)

where g<=m^6/64 holds for m>=2. Combining(3),(14), the leading term
of(9) is at least

                         2^-30 m^6(pi*y)^(-12).     (15)

At the real center, all derivative/commutator/linear adverse terms in(9)
are bounded using(11),(13) by

 2^44m^4 y+2^47m^2 y^2+2^44m^3<=2^49m^5,           (16)

because y<=m^.01<=m. The ENTIRE constant-only term K0L(y)^2 is
nonnegative by(10), and is retained as such. For this domain,

 m>=2^80(pi*y)^12,

since pi<4,y<=m^.01 and m^.88>=2^880>2^104. Hence(16) is at most
half(15). We obtain the stronger point estimate

                         P(y)>=2^-31m^6(pi*y)^(-12),

and therefore(4). This point conclusion consumes the proved actual(H); it makes no
inference that a real point margin alone supplies a complex bound.

### L6. Full Psi bound on the inner complex disk

For |u-y|<=1/8 one has |u|<=2y<=2m. Using the exact decomposition(9),
not just its leading Q term, the six magnitudes are at most

 alpha*a(a-1)|Q|          <=2^40m^6,
 2alpha*a*|u|*|Q'|        <=2^45m^5,
 alpha*|u|^2*|Q''|        <=2^49m^4,
 g|Q|                     <=2^40m^4,
 |Cstar|                  <=2^44m^3,
 |K0 L^2|                 <=m^2.                    (17)

Their sum is <2^51m^6, which is stronger than(5). The constant W+1,
both derivatives, the C linear trace and the original alpha/g/tau
normalizations have all contributed to this complete complex upper bound.
There is no inference from a positive Hermitian form at a real point to
such a complex disk estimate without(H) and the actual Cauchy argument.


## 6. A global coefficient envelope, paid only on the far tail

For a finite matrix polynomial F=sum F_r u^r write
N_y(F)=sum||F_r||HS y^r; scalar polynomials use absolute coefficients.
The exact reversed kth term of V, with r=n-k, is
-2zeta(n-r)(2pi)^r Dv^(n-r)u^r/H_n. By(Z1), zeta<=2 gives

 ||V_r||HS<=2^12m^.25(4pi)^r/r!.

The baseline coefficient contributes ||Z0||HS/A_n(1/y)<=1. Summing the
actual even deficits and only then enlarging the positive majorant gives

 N_y(V)<=2^13m^.25e^(4pi y),
 N_y(U)<=2^14m^.25e^(4pi y),
 N_y(Q)<=N_y(U)^2<=2^28sqrt(m)e^(8pi y).              (G1)

This includes every carrier input, both parity blocks, the odd top and
u=0. The analytic scalar Q at complex u is not a Hermitian norm. The
last inequality is the genuine HS trace convolution bound.

The coefficient of b of degree k=q-r is multiplied in its Euler block
by(Dold-k)(Dold-k-1), which lies in[0,m^4] for0<=k<=q. This does not
assert that Q_r is positive. As alpha<=m^2/2, the coefficient norm of
that block's b part is at most(m^6/2)N_y(Q). Its constant B part is at
most m^2 because N_y(L)=1/A_n(1/y)<=m^-3. The full Cstar has

 N_y(Cstar)<=16tau N_y(V)N_y(U)
               +16tau sqrt(m)N_y(L)N_y(U)
            <=2^32m^(7/2)e^(8pi y).

Likewise g[N_y(Q)+(W+1)N_y(L)^2]
<=2^28m^(9/2)e^(8pi y)+2. These inequalities keep the original linear
trace term and W+1. Combining them proves the deliberately loose
GLOBAL bound

 sup_|u|<=y |P(u)|<=N_y(P)<=2^100m^7e^(32y).         (G2)

This exponential is permitted on the far tail. It is not substituted for
(H) or the polynomial local bound(5). No positive coefficient-functional
representation is asserted.

## 7. Exact binomial local/global transfer

The next lemma is elementary finite Cauchy transfer. Inside its proof
D=Dbin,J=Jbin, so D is a scalar degree parameter, not the derivative Dv or
Dold. Assume1<=J<=D/2,y=D/J>=2 and0<h<=y.

### T1. Local/global transfer inequality

Let Q be any polynomial with Q(y)>0 real, and let 0<h<=y. Assume only

 sup_|z-y|<=h |Q(z)| <= M Q(y),
 sup_|z|<=y   |Q(z)| <= G Q(y),                         (A3)

where M,G>=1 may depend on all parameters. They are hypotheses, not
properties inferred from a positive Gram value. Then the exact functional
T(z^s)=(D+1)_s/(J+1)_s obeys

 |TQ-Q(y)|/Q(y)
 <=512 M y^2/(J h^2)
   +8 sqrt(J) (G+1+2My/h)
                exp[-J h^2/(4pi^2 y^2)].               (A4)

Consequently a REAL-coefficient Q with the right side<1 has TQ>0. The lemma is conditional for a general polynomial; the actual M,G for
our full P are supplied by(4),(5),(G2) in the next section.
There is no assertion that T is positive on arbitrary squares.

### T2. Exact coefficient contour, retaining its complex phase

The finite monomial identity

 [s^J](1+s)^D Q((1+s)/s)/binom(D,J)=TQ                 (A5)

follows because for Q(z)=z^a the coefficient ratio is
binom(D+a,J+a)/binom(D,J)=(D+1)_a/(J+1)_a. The expression can have a
finite pole at zero but is a Laurent polynomial; its coefficient contour
is still exact on any circle about zero. Put p=J/D, r=p/(1-p), and

 K(theta)=[(1+r exp(i theta))/(1+r)]^D exp(-iJ theta),
 Y(theta)=1+r^(-1)exp(-i theta),
 p_J=binom(D,J)r^J/(1+r)^D.

Cauchy's finite coefficient formula gives

 TQ=(2pi p_J)^(-1) integral_(-pi)^pi K(theta)Q(Y(theta))dtheta. (A6)

In particular the same integral sends 1 to1 and Y to y0=(D+1)/(J+1)
exactly, so y0-y=-(y-1)/(J+1). We never
discard the phase of K or replace this integral by a Gaussian expectation.

The scalar binomial mode has the elementary bound

                         p_J>=1/(8sqrt(J)).            (A7)

For completeness, the finite binomial distribution with parameters D,p
has mean J and variance J(1-p)<=J. Chebyshev puts mass>=3/4 on fewer
than 4sqrt(J)+1<=5sqrt(J) integer sites about J. Its mode is J, as is
seen directly by ratios of adjacent binomial masses for p=J/D and p<1.
Thus p_J>=3/(20sqrt(J))>1/(8sqrt(J)). This is a paper proof about finite
weights, not a sampled or scientifically executed distribution.

For -pi<=theta<=pi, the EXACT kernel satisfies

 |K(theta)|
 =[1-2p(1-p)(1-cos(theta))]^(D/2)
 <=exp[-Dp(1-p)(1-cos(theta))]
 <=exp[-J theta^2/pi^2].                               (A8)

We used p<=1/2 and 1-cos(theta)>=2theta^2/pi^2. This Gaussian-shaped
MAJORANT bounds the true kernel; it is not a substitution for it. Also

 |Y(theta)|<=y, |Y(theta)-y|<=y|theta|,
                     |Y(theta)-y|<=2y.                 (A9)

The global envelope in(A3) is needed only on this exact curve, and an
origin-disk upper bound is one sufficient way to supply it. It need not
be small or polynomial relative to Q(y).

### T3. Taylor subtraction and proof of the error bound

Let theta0=h/(2y), so 0<theta0<=1/2. Cauchy's bound on the LOCAL disk
in(A3) gives |Q'(y)|<=MQ(y)/h. For |theta|<=theta0 the Taylor remainder

 B(theta)=Q(Y(theta))-Q(y)-Q'(y)(Y(theta)-y)

satisfies |B(theta)|<=2MQ(y)y^2 theta^2/h^2, by summing the coefficient
tail from degree2 at |Y-y|<=h/2. On the rest of the contour, (A3),(A9)
give |B(theta)|<=(G+1+2My/h)Q(y).

Using(A7)-(A8), the inner remainder after division by 2pi p_J is at most

 [4sqrt(J)/pi] *[2My^2/h^2]
       *integral_R theta^2 exp(-Jtheta^2/pi^2)dtheta
 <=16pi^2 M y^2/(J h^2) Q(y).                          (A10)

The elementary integral bound integral_R u^2 exp(-u^2)du<=2 suffices;
it follows by integration by parts on [1,infinity) and the direct bound
on [0,1]. The outer remainder is at most

 8sqrt(J)(G+1+2My/h)exp[-J h^2/(4pi^2 y^2)]Q(y).       (A11)

Finally y0-y=-(y-1)/(J+1) and(A6) retain the linear term exactly, whose magnitude is at
most MQ(y)y/(Jh). Since h<=y and pi<4, its contribution together with
(A10) is less than512My^2/(Jh^2)Q(y). This proves(A4), with no unbounded
norm of a partial elementary-factor product and no probability moment
representation of the exact theta_s weights on the unit circle.


## 8. Actual envelopes, explicit tail and original coefficient margin

The ORIGINAL finite coefficient identity gives, term by term,

 L_(d,j)Psi=Cxi^2 h_q T P,
 h_q=(j)_q,fall/(d)_q,fall>0,
 T(u^s)=(Dbin+1)_s,rise/(Jbin+1)_s,rise.             (R4)

Indeed the ratio of the falling factors for degrees q-s and q is the
stated rising ratio. For(R1),1<=Jbin<=Dbin/2,2<=y<=m^.01,
Dbin>=m^2/2 and Jbin>=m^2/(2y). The functional lemma's point y=Dbin/Jbin
and its exact shifted mean are retained; neither is replaced by d/j.

Take h=1/8. The actual bounds(4),(5),(G2), with pi<4, allow

                  M=2^164 y^12,
                  G=2^164 m y^12 e^(32y).           (R5)

The first term in(A4) is at most

 2^180 y^15/m^2<=2^180m^(-185/100)<=2^-1670<1/16.    (R6)

For its tail, h^2/(4pi^2)>2^-12 gives

 Jbin h^2/(4pi^2y^2)>=2^-13m^2/y^3
                            >=2^-13m^(197/100).    (R7)

Crucially the chosen envelopes satisfy the STRONG relation
G=m e^(32y)M>=mM>=yM and G>=1. Thus
G+1+16My<=18G<32G, and the entire tail prefactor is at most

 8sqrt(Jbin)(G+1+16My)<=2^8 mG
                        =2^172m^2y^12e^(32y).

This step would not follow from only G>=M. Its natural logarithm is at
most172+3log m+32m^.01. For m>=2^1000, log m<=log_2m<=m/16;
32m^.01<=m/128 and172<=m/128. Therefore it is less than m/4.
The negative exponent(R7) is at least2m, since m^.97>=2^970>2^14.
The entire far tail in(A4) is consequently at most e^(-7m/4)<=2^-m<1/16.
These are uniform hand inequalities on the full integer domain, not
finite sampling or a Gaussian approximation of the original functional.

It follows that |TP-P(y)|<P(y)/8 and, in particular,

                   TP>=P(y)/2>=2^-41m^6(pi y)^(-12). (R8)

Using(R4) and the original coefficient identity in(1) proves(R2).
Finally Cxi^2=H_n^2/(2pi)^(2n)>=H_n^2/8^(2n) and
(pi y)^(-12)>=(4y)^(-12). This proves the rational weaker bound(R3).
No sign of the physical P1 or any other homogeneous layer was inferred.

## 9. What changed, what remains open, and scientific scope

The new capability is a full-original-carrier complex local bound obtained
through a justified ambient upper inequality, finite translations, an
angular Gaussian MAJORANT and finite Laplace integration. A separate
coarse exp(Cy) global envelope is paid only against the exact binomial
far tail. Local Psi includes all original corrections; coefficient
positivity is never inferred merely from a positive Gram value. The
classical Gamma/finite-Cauchy inequalities are proved at their actual
parameters, not imported as an unread asymptotic theorem. This is a
composed quantitative proof, not automatic registration of a generic Tool.

The old varying-order Green formula, CF's fixed-common-order complex
lemma, and the unreviewed3cc HOLD archive are not hidden premises here.
Their proof/contribution boundaries and all earlier failures are preserved.
The selected classical sources used by the accepted real-state input
remain its own earlier scoped observations; no new NIST HTTP call is
invented for this paper. Every NEW load-bearing proof is in this primary.

This proposed band does not bridge all the way down to bounded j/m,
does not close all-j or small m, and does not cover every upper coefficient
for its own m threshold. All older initial/directional/log/bulk/terminal
statements retain their own thresholds and stronger margins. The rest
of COMMON C1, whole P1/physical positivity, the trace inequality and
mother Goal remain OPEN. No Task, Native scientific call/vote, Foundation,
WorkingTruth, budget reset or Goal closure follows. A new complete
nonauthor whole review is required; Root is control/routing only.

All actual authors must personally completely read the same fixed final
primary, typed result and input/contribution context before a true freeze.
Current status remains AUTHOR WHOLE WORKING / UNREVIEWED, not a PASS.
MotherGoal OPEN; global ending UNKNOWN; MESSAGE only, no FINAL.
