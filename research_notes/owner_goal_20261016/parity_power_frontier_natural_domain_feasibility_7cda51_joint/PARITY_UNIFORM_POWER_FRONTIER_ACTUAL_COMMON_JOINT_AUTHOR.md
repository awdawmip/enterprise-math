# A uniform power-frontier family for actual raw COMMON coefficients

AUTHOR PROPOSAL / UNREVIEWED / PREPARED FOR ONE WHOLE FREEZE. Actual joint authors:
EM-PUBLIC-7CDA51, EM-DVR-BFF6DC, EM-DIRECT-88303D. One proposed
parameter-family theorem with its actual auxiliary proofs, not separate
papers for the natural domain, weighted pair, each exponent or readout.
All author checks are collaboration, not independent review votes.
No future nonauthor has received this working or supplied repair.

All derivation is symbolic hand mathematics. Zero programmed scientific
matrix/coefficient evaluations, integration, samples, solvers, scientific
imports/AST/compile/tests or Native calls. Text/JSON/hash/copy operations
are administrative only. All original warm identities, NONBLIND,
failures, permanentSTOP/HOLD and continuous formal-budget UNKNOWN remain.
The original13042/877/e134 and the separately frozen complete-upper
proposal at e08c4defc55fc85e9044066f87e004fce2ed8751 are not modified.
The pending-review complete-upper proposal is NOT a premise here.

## 1. Exact object, genuinely uniform parameter and proposed band

Retain the SAME original positive Student carrier of polynomials in v
of degree<=m-2, dimensionm-1, with weight(1+4v^2)^(-m), monic P_k,
h_k=||P_k||^2, actual positive Hermitian adjoint and Dv=d/dv.
Let n be the largest even integer<=m-2, t=m-n in{2,3}, ell=n-1,q=2ell,
W=m^2,d=W-3,Dold=W-1,D=d-q,J=j-q and y=D/J. D is the scalar shifted
degree, not Dv or Dold. Define

 Hn=n!sqrt(h0/hn), Cxi=Hn/(2pi)^n,
 An(a)=Cxi*a^ell for real a>0, Chat=Hn/(2^n*pi)=pi^ell*Cxi,
 K=m^(2W)/2, hq=(j)_q,fall/(d)_q,fall.                 (N1)

The symbol rho below is the growth exponent; the raw polynomial variable
is still a, and its original Euler prefactor is still alpha.
Fix a RATIONAL exponent

 1/100<=rho<2/11, epsilon=2-11rho>0,
 m integer>=2^ceil(10000/epsilon), mu=m^rho.            (T1)

**Proposed theorem.** For every integer in the complete inclusive band

                  q+ceil(D/mu)<=j<=q+floor(D/2),       (T2)

the SAME original raw homogeneous degree-d COMMON coefficient obeys

 [S^(d-j)a^j]H_d^raw
 >=K binom(d,j) Cxi^2 hq 2^-41m^6(pi*y)^-8>0.          (T3)

An explicitly rational weaker margin is

       K binom(d,j) Hn^2 hq 2^(-6n-57)m^6(J/D)^8>0.   (T4)

Here Hn^2=n!^2/product_(k=1)^n beta_k is a finite positive rational
product, beta_k=k(2m-k)/[16((m-k)^2-1/4)]>0. No giant expression is
programmatically evaluated. Threshold and ceil/floor are exact,
unexpanded symbolic data, not asymptotic or sampled certification.
No j above q+floor(D/2) or below q+ceil(D/mu) is automatically included.
The pending complete-upper theorem is not used to enlarge this band.

The same proof also supplies, as auxiliary parts of THIS chain only,

 ||U1(pi/z)||HS<=2^17An(pi/|z|),
 U1(xi)=xi Dv^2[(2pi)^2I-xi^2Dv^2]^(-1),
 m>=2^1000, 1<=|z|<=sqrt(m-1)/4, |Imz|<=1,             (N2)-(N3)

 Ucal(z)=z^ell U1(pi/z)/Chat,                           (N4)

 b(xi)>=2^-19 z^-8 An(xi)^2>=2^-24 z^-8 An(xi)^2,
 m>=2^1000, xi=pi/z, pi<=z<=sqrt(m)/8.                 (R8*)

These are newly checked domain/weighted estimates, not a transfer of
old narrow-domain votes. They alone imply no coefficient sign.
Every actual input, parity, odd top, rank-one compression and genuine
adjoint remains; an auxiliary ambient norm is used solely as an upper
inequality. No triangular rank-two kernel is called a rank-two matrix.

## 2. Literal COMMON and exact accepted inputs

The original identities, before any new parameter estimate, are

 H_d^raw(S,a)=K(S+a)^d Psi(a/(S+a)),
 [S^(d-j)a^j]H_d^raw=K binom(d,j)L_(d,j)Psi,
 L_(d,j)(xi^k)=(j)_k,fall/(d)_k,fall,

 Psi=C-g(B+2)+alpha[Dold(Dold-1)B-(2Dold-1)E_xi B+E_xi^2B],
 B=b+W-1,b=tr(R^2),R=Z+Zsharp,
 C=2tau tr(Ae[Z,R])-4tau tr(Ae R),
 alpha=(W+1)^2/(8W),tau=(m^4-1)/(24m),g=m*tau,
 E_xi=xi partial_xi, ||Ae||op<=4,||Ae||HS<=4sqrt(m-1).

In particular B+2=b+W+1. The original top/lower prefactors are unequal,
Ktop=m^2K, with the ratio already paid in alpha. The literal coefficient
readout, fixed-r0 differentiation and all C linear terms are retained.
The actual frame and baseline are

 Zxi=Z0-2sum_even k=2..n zeta(k)xi^(k-1)Dv^k/(2pi)^k,
 Z0=vDv-(m-1/2)I, ||Z0||op<=2m,||Z0||HS<=2m sqrt(m-1).

For a polynomial F, Fsharp(u)=F(conjugate(u))^dagger takes the adjoint
of every coefficient and leaves the analytic variable unchanged. It is
analytic, not a moving complex dagger. On the real axis it agrees with
the actual adjoint. Define finite reversed polynomials

 V=u^ell Z_(1/u)/Cxi,U=V+Vsharp,Q=tr(U^2),
 L=u^ell/Cxi,P=u^q Psi(1/u)/Cxi^2.

Then Q=u^q b(1/u)/Cxi^2. At complex u this is not a positive Hermitian
square. Degrees are<=ell and<=q, with finite continuation at zero.

Accepted exact inputs are, with their original scopes retained:

* Source cfd876cb9bda189b8978f23d7855a9e66a862a44, the23366-byte
  PARITY_COMMON_LOWER_LAYER_UNIFORM_BULK_RAW_COEFFICIENT_BAND_JOINT_AUTHOR.md,
  SHA58af3cc47f58d63419c7cd23e5853e1add19810ada0548336e7afa0518a212b9,
  blobc8f9f6dde9e4e6939d181afdf7f6092a09d12a1c. Use its literal model,
  COMMON/readout, norm ratios, full-carrier B13 and spectrum/Ae/baseline
  identities, not its coefficient verdict outside its domain.
* Real-state author Source98b1f4b3075da2afab249b85375e73f883ae710e,
  primary14891/SHA545c93a4778e30a70b50cc87db289cc81dce7679487571e9ab0a46a0d260cd88,
  blob23fcd878e31ad985b85c643d928bf2512a9ccf5f, and truepeer
  Source88c190aba4414288c908a43ece9abec138ae742d. Use exact finite means,
  Lommel/Bessel matching, real-phase polynomial and scalar-zeta lemma
  at their actual parameter domains; their finite proofs are restated
  below. The old z^-12 conclusion/domain is not relabeled as the new R8.
* Power-scale author Source877aa46f1a58b1c314595e18217ae54e44bc0a14,
  primary33784/SHAf07b8b69f649a97d18931490c16b91db198d2c450a76bb591e2f6fd8dd9f16f5,
  blobba7db3cdd88dc711c630b7c12f29a628e3def6f6, and genuine whole peer
  Sourcee13462192b274e15d7c5b3e17fa3841db8c16be4. Use its exact full-matrix
  reversed-zeta bound for |u|<=m/(512pi), Euler0..2, and its generic
  phased finite-functional lemma with any1<=J<=D/2 and supplied local/
  global hypotheses. Neither generic lemma restricts y to m^.01; its
  old actual coefficient APPLICATION did, and that application is not
  upgraded by an old vote. The new conditions are proved here.

All current authors' old semantic/immutable Source consumption belongs
to its own observer, not borrowed sibling APIs. No new HTTP/wholechapter
or unread asymptotic theorem is invented. Selected classical imports
remain their original accepted real-state provenance. The unreviewed
3ccHOLD, failed all-subsets certificate, optional CF complex component
and a quantitative Green hypothesis are not hidden premises.
The numbering below keeps N/R/F/I prefixes distinct.

## 3. Complete natural-domain single-pole upper proof

For this section ONLY set N=m-1, and write Vspace for the original
degree<=m-2 carrier. This ambient-degree N is distinct from the local
Lommel degree N=n_s-1 introduced in section4.

### N2. Legitimate actual-to-ambient inequality and angular prefactor

Use the auxiliary degree<=N space Wamb with the SAME Student inner
product. Its m polynomials

 f_r(v)=(v-i/2)^r(v+i/2)^(N-r), 0<=r<=N,

are mutually orthogonal with common squared norm (pi/2)4^-N. Indeed
|f_r|^2 times the weight is4^-N/(1+4v^2), and cross terms are nonconstant
circle characters under y=(v-i/2)/(v+i/2). The integrable extra top
degree is an ambient aid, not an identification with Vspace.

For complex s, finite translation T_s=e^(sDv) preserves Vspace and
Wamb. Extending an orthonormal basis of Vspace proves only

               ||T_s|Vspace||HS<=||T_s|Wamb||HS.       (N5)

No actual vector, rank-one correction, parity block or input is removed;
no ambient adjoint is equated to the actual adjoint.

Write s=x0+iy0, u=|s|, b0=|y0|, so x0^2+b0^2=u^2. The two translated
linear factors have squared moduli at most
(v+x0)^2+(b0+1/2)^2. Summing all m normalized input norms and applying
2v=tan(theta), with full-period angular rotation, gives

 ||T_s|Wamb||HS^2
 <=m/(2pi) integral_-pi^pi (a+b cos(theta))^N dtheta,  (N6)
 a=1+2(u^2+b0), b=2sqrt((u^2+b0)^2+x0^2).

Here a^2-b^2=(1+2b0)^2>0, and the angular integrand is nonnegative.
For u>=1, v0=u^2+b0>=1, so

 b/(a+b)>=2v0/(1+4v0)>=1/4.

Using1-cos(theta)>=2theta^2/pi^2, the angular average is bounded by
rhotrans(s)^(2N) times a Gaussian majorant of integral at most2/sqrt(N),
where rhotrans^2=a+b. Since N>=m/2,

 ||T_s|Wamb||HS<=2m^(1/4)rhotrans(s)^N, u>=1,
 ||T_s|Wamb||HS<=sqrt(m)rhotrans(s)^N, all u>=0.            (N7)

The second inequality is the direct full-period maximum. The first
retains the needed m^(1/4) factor; no m^2 entry count is substituted.

The elementary root inequality gives

 rhotrans(s)^2<=4u^2+4b0+2.
 rhotrans(u e^(i phi))^N
 <=(2u)^N exp[N|sin(phi)|/(2u)+N/(4u^2)], u>0.        (N8)

Along a fixed direction rhotrans(u e^(i phi)) is nondecreasing in u. These
are algebraic inequalities from(N6), independent of the new z domain.

### N3. The finite Laplace proof reaches the natural domain at the same constants

Termwise integration of the finite matrix exponential gives exactly

 Tcal(xi)=integral_0^infinity e^-v
             (T_(xi v/(2pi))+T_(-xi v/(2pi)))/2 dv
         =sum_even k>=0 (xi Dv/(2pi))^k,
                 U1(xi)=(Tcal(xi)-I)/xi.              (N9)

The sum has the true finite cutoff. No convergence interchange for an
infinite matrix series is presumed. Take Z=|z|, gamma=|Im z|<=1,
xi=pi/z, muLap=2Z and phi=-arg z. After v=muLap u, the shifts have direction
phi or its negative and modulus u, with |sin(phi)|=gamma/Z. By the
ordinary actual HS triangle inequality and(N5),

 ||Tcal|Vspace||HS
 <=muLap integral_0^infinity e^(-muLap u)
                         ||T_(u e^(i phi))|Wamb||HS du. (N10)

The new domain (N3) permits the split

                         T=N/(8Z).                   (N11)

At its actual upper endpoint Z<=sqrt(N)/4 one has

 T>=sqrt(N)/2>1,  16Z^2/N<=1.                         (N12)

These are the precise replacement for the old small m^.01 estimates.
For u>=T, (N8) has

 N|sin(phi)|/(2u)<=4gamma<=4,
 N/(4u^2)<=16Z^2/N<=1.

Therefore rhotrans^N<=e^5(2u)^N<2^8(2u)^N. By(N7), the tail of(N10) is

 I_tail<=2^9m^(1/4)muLap integral_0^infinity e^(-muLap u)(2u)^N du
        =2^9m^(1/4)Gamma(m)/Z^(m-1).                  (N13)

The exact finite Gamma integral is used, not a sampled saddle formula.
For0<=u<=T use monotonicity, the coarse bound(N7), and the same bound
at T. Since muLap integral_0^T e^(-muLap u)du<=1,

                 I_early<=2^8sqrt(m)(N/(4Z))^N.       (N14)

With G=m^(1/4)Gamma(m)/Z^(m-1), N!>=(N/3)^N implies

 I_early/G<=2^8m^(1/4)(3/4)^N<=2^8.

For the last inequality, log_2m<=m/16 for m>=256 and
log(4/3)>=1/4 give
m^(1/4)(3/4)^N<=2^(m/64-N/4)<=1, since N>=m/2.
Together,

             ||Tcal|Vspace||HS<2^10G.                 (N15)

No exp(CZ) appears. In particular the endpoint16Z^2/N=1 was kept,
rather than silently assuming Z=o(sqrt(m)).

### N4. Actual norm/Gamma scale, with no dependence on a narrow z range

The old exact norm ratio is

 h_k/h_(k-1)=k(2m-k)/
       [16(m-k-1/2)(m-k+1/2)].

Let alpha_k=m-k-1/2, B_k=binom(2m-1,k), and
a_k=4^k sqrt(h_k)/(k!Gamma(alpha_k)). Direct telescoping gives

 a_k^2/a_(k-1)^2=(2m-k)alpha_k/[k(alpha_k+1)],
 a_k^2=Cnorm alpha_k B_k, Cnorm=a_0^2/(m-1/2).

This is a separate normalization constant, not the common ambient
basis norm. Substitution into (N1) gives the exact scale identity

 An(pi/Z)=
  2^n Gamma(m-1/2)/
      [pi Gamma(t+1/2) Z^(n-1)]
       sqrt((m-1/2)(t-1/2)/B_n).                     (N16)

Nothing in this identity restricts Z. The elementary bound
binom(2m,m)<=4^m/sqrt(3m+1) follows by induction: the squared adjacent
ratio inequality has right-minus-left equal to m. Also
B_n<=binom(2m,m)/2. Positive Gamma-integral Cauchy-Schwarz gives

 Gamma(m)<=sqrt(m-1/2)Gamma(m-1/2).

Using both in(N16), with n=m-t, gives

 An(pi/Z)>=[2^(.5-t)sqrt(t-.5)/(pi Gamma(t+.5))]
             (3m+1)^(.25) Gamma(m)/Z^(n-1)
          >=2^-6m^(1/4)Gamma(m)/Z^(n-1).              (N17)

For t=2,3 the numerator factor exceeds1/4, pi<4 and
Gamma(t+.5)<4. This lower bound is valid for every Z>0; it is not a
narrow-domain asymptotic imported from the old theorem.

### N5. The NEW wide-domain amplitude and true full-HS identity contribution

The old monic-minimizer/moment inequality hn/h0<=4^-n gives
Hn>=2^n n!. Hence

                     An(pi/Z)>=n!/[pi Z^(n-1)].

On(N3), Z<=sqrt(m)/4. Since n is even and n>=m/2,

 An(pi/Z)
 >=n!4^(n-1)/(pi m^((n-1)/2))
 >=sqrt(m)2^(n-2)/pi.                                (N18)

The second step uses n!>=(n/2)^(n/2)>=(sqrt(m)/2)^n.
At m>=2^1000, sqrt(m)/(4pi)>1 and 2^n>=m^3: the latter follows from
n>=m/2 and3log_2m<=3m/16<m/2. Thus

                           An(pi/Z)>=m^3             (N19)

on the full new closed domain. This is a NEW explicit wider-domain
check; the previous An>=m^3 statement for Z<=4m^.01 is not simply
extrapolated. In fact (N18) is much larger than the coarse target.

The identity in(N9) has full actual HS norm sqrt(m-1). It is NOT
bounded by an operator norm without its dimension. From(N9),(N15),

 ||U1(pi/z)||HS
 <=Z/pi [2^10m^(1/4)Gamma(m)/Z^(m-1)+sqrt(m-1)].

Dividing its first term by(N17) gives exactly

                    2^16 Z^(1-t)/pi<=2^16,           (N20)

using Z>=1 and t=2 or3. Its second term divided by(N19) is at most

            Z sqrt(m-1)/(pi m^3)<=1/(4pi m^2)<1.     (N21)

Thus the same constant2^17 proves (N2) on ALL of(N3), with every
actual input and original parity present. No pointwise lower-state
estimate or invalid actual/ambient adjoint identity was used.


The equality An(pi/|z|)=Chat/|z|^ell now turns (N2) into
||Ucal(z)||HS<=2^17. A derivative conclusion may be taken ONLY on a
whole disk inside (N3); no fixed-radius disk at the maximal-modulus
boundary is promised. The later consumer checks strict spare room.

## 4. Exact matched scalar identities and finite real phase energy

The following accepted finite identities are explicitly restated to fix
normalization, common order and scalar-zeta domain. Their rho_r finite
coefficient is distinct from the growth exponent rho. The monic norm
ratios used above hold for the same actual carrier.

### I1. Exact finite means and the classical parameter certificate

For s=2,3,4,5 with n_s=m-s even>=2, define

 F_m,s(z)=sum_(r=0)^(n_s/2-1)
        (-z^2/4)^r rho_r/[r!(s+1/2)_r],
 rho_r=(n_s-2r)_r,rise/(m-r-1/2)_r,rise.              (I4)

Let F_zeta,m,s be this SAME finite sum with the extra original multiplier
zeta(n_s-2r). Every argument is>=2. There is no generic continuation
through a negative-integer hypergeometric denominator. The exact old B8 is

 <(Z_xi-Z0)e_(n_s),e0>/A_(n_s)(xi)
                              =-2F_zeta,m,s(z).      (I5)

Set N=n_s-1,nu=s+1/2,M=nu+N=m-1/2. Define scalar Laurent polynomials
L_(0,nu)=1,L_(1,nu)=2nu/z and

 L_(k+1,nu)=2(nu+k)L_(k,nu)/z-L_(k-1,nu).             (I6)

Their exact finite certificate is

 L_(N,nu)=sum_(r=0)^floor(N/2) (-1)^r binom(N-r,r)
          Gamma(nu+N-r)/Gamma(nu+r) (2/z)^(N-2r).     (I7)

For completeness put C_(N,r)=binom(N-r,r)Gamma(nu+N-r)/Gamma(nu+r),
zero outside the finite support. The coefficient recurrence required by(I6)
is C_(N+1,r)=(nu+N)C_(N,r)+C_(N-1,r-1). Pascal's identity reduces it to
-r binom(N-r,r)+(N-2r+1)binom(N-r,r-1)=0. The initial cases agree,
so finite induction proves(I7). Multiplying it by(z/2)^N Gamma(nu)/Gamma(M),
and using binom(n_s-1-r,r)=(n_s-2r)_r/r! and
Gamma(M-r)/Gamma(M)=1/(m-r-1/2)_r, proves

 F_m,s=(z/2)^N Gamma(nu)/Gamma(M)L_(N,nu).             (I8)

N is odd: floor(N/2)=n_s/2-1 is exactly the original cutoff. The scaled
expression is an even polynomial with constant1; it is removable at0.
These are classical Lommel recurrences composed with the actual parameters,
not a new generic special-function tool or an asymptotic approximation.

The selected classical Bessel recurrence and Wronskian give, for real z>0,

 L_(N,nu)=(pi z/2)[J_M Y_(nu-1)-Y_M J_(nu-1)].        (I9)

At N=0 the Wronskian shifted to nu-1 gives+1; the order recurrence then
gives2nu/z and(I6). Thus both the sign and normalization are fixed by finite
initial conditions. No separate singular Y value is substituted at z=0.

Define real functions on z>0 by

 A_M=-pi(z/2)^M Y_M/Gamma(M),
 B_M= pi(z/2)^M J_M/Gamma(M),
 Phi_s=Gamma(s+1/2)(z/2)^(1/2-s)J_(s-1/2),
 Xi_s= Gamma(s+1/2)(z/2)^(1/2-s)Y_(s-1/2).

Then(I8)-(I9) give the EXACT finite identity

                         F_m,s=A_M Phi_s+B_M Xi_s.   (I10)

Here A_M,B_M are auxiliary scalar functions, distinct from the actual
matrix amplitude A_n and state polynomial b(xi). The two actual channels
s=t,t+2 have N->N-2,nu->nu+2 but the SAME M. Their prefactors in(I8)
are different and both have been retained in deriving(I10).

### I2. Exact real phase energy, proved by finite coefficients

Put l=m-1, M=l+1/2. We will prove

 A_M(z)^2+B_M(z)^2
  =sum_(r=0)^l [c_(l,r)/c_(l,l)] z^(2(l-r))>=1,
 c_(l,r)=(l+r)!/(l-r)! *binom(2r,r)/4^r, z>0.         (I11)

This is a REAL inequality; it is not complex-disk positivity. Here is a
finite proof. The selected J-series, Y-connection and Gamma reflection
give J_(1/2)=sqrt(2/(pi z))sin z,Y_(1/2)=-sqrt(2/(pi z))cos z,
J_(-1/2)=sqrt(2/(pi z))cos z,Y_(-1/2)=sqrt(2/(pi z))sin z.
For H_v=J_v+iY_v, the order recurrence implies

 H_(k+1/2)=sqrt(2/(pi z))(-i)^(k+1)e^(iz) p_k(i/z),
 p_(-1)=p_0=1, p_(k+1)(w)=(2k+1)w p_k(w)+p_(k-1)(w).

Thus p_k is a real polynomial of degree<=k with constant1. On the real
axis its squared modulus is p_l(i/z)p_l(-i/z), an even Laurent polynomial
of degree<=2l with constant1. Consequently

 h(z):=z(J_M^2+Y_M^2)=2/pi sum_(r=0)^l c_r z^(-2r), c0=1.

Positivity of these coefficients has not been assumed from a square.
The selected Bessel ODE gives u=sqrt(z)J_M,v=sqrt(z)Y_M satisfying
u''+Qu=0,v''+Qv=0,Q=1-l(l+1)/z^2. Differentiation of h=u^2+v^2 gives
h'''+4Qh'+2Q'h=0. Its exact coefficient z^(-2r-1) yields

 c_r=(2r-1)/(2r)[l(l+1)-r(r-1)]c_(r-1)
    =(2r-1)/(2r)(l+r)(l-r+1)c_(r-1).                 (I12)

For1<=r<=l all factors are positive, and finite multiplication gives
c_r=c_(l,r) in(I11). At r=l+1 the factor vanishes, as required by the
already established finite support. The half-integer Gamma recurrence
and Gamma(1/2)^2=pi give

 c_(l,l)=[(2l)!/(2^l l!)]^2=2^(2l)Gamma(l+1/2)^2/pi.

Substituting into the exact A_M,B_M scale proves(I11), whose constant
term is1. For l=0 the identity is the usual sine/cosine energy and the
same empty recurrence applies. This proof uses no large-order asymptotic.


### I3. Uniform scalar-zeta remainder with both actual cutoffs

For any fixed s>=2 and even n_s>=64, we prove

 |F_zeta,m,s-F_m,s|<=2^(-n_s/4), |z|<=n_s/64.         (I16)

On the actual support0<=r<=n_s/2-1,0<rho_r<=1 and(s+1/2)_r>=r!.
Thus the absolute finite coefficients are majorized by
|z|^(2r)/(4^r(r!)^2), whose infinite sum is <=cosh|z|<=e^|z|,
because binom(2r,r)<=4^r. For integers k>=3,
zeta(k)-1<=2^-k+integral_2^infinity u^-k du<=2^(1-k);
for k>=2,0<zeta(k)-1<1 by integral comparison with u^-2.

Let S=floor(n_s/4). The actual low indices r<=S have k=n_s-2r>=n_s/2,
so their contribution to the difference is at most
2^(1-n_s/2)e^|z|<=2^(1-15n_s/32)<=2^(-n_s/3).
Here log2>=1/2 and n_s>=64 suffice. For the remaining finite indices,
majorize by a_r=(|z|/2)^(2r)/(r!)^2. At r>=S+1 its consecutive ratio
is <=1/1024. Also r!>=(r/3)^r, so the first term is at most
(3/32)^(2(S+1))<=2^(-6(S+1)). The geometric tail is less than
2^(1-3n_s/2)<=2^(-n_s/3). Adding gives2^(1-n_s/3)<=2^(-n_s/4).
Only majorants were extended to infinity, never the actual zeta cutoff.


## 5. Complete new weighted two-channel proof and actual state

### R2. The exact amplitude and common real phase

For s=t,t+2, put nu_s=s+1/2 and M=m-1/2. The actual finite sums satisfy

 F_(m,s)=A_M Phi_s+B_M Xi_s,
 A_M=-pi(z/2)^M Y_M(z)/Gamma(M),
 B_M= pi(z/2)^M J_M(z)/Gamma(M).                      (R2)

The two channels have different positive Gamma/power prefactors in
the finite classical bridge; after the exact conversion in(R2), they
share these SAME real A_M,B_M. This conversion is unchanged here.

The normalized nonconstant actual entry pair is

 An^(-1)(<(Zxi-Z0)e_n,e0>,<(Zxi-Z0)e_(n-2),e0>)
       =-2(F_(zeta,m,t),w F_(zeta,m,t+2)),              (R3)

where the actual AMPLITUDE ratio is

 w=z^2/[4sqrt((t^2-1/4)((t+1)^2-1/4))]
       sqrt((m+t)(m+t+1)/[(m-t)(m-t-1)]).             (R4)

In particular the squared norm in(R3) has w^2, never w. For m>=100
the square-root ratio lies in[1,2]. For the upper estimate the numerator
is <=(m+3)(m+4), denominator>=(m-3)(m-4), and

 4(m-3)(m-4)-(m+3)(m+4)=3m^2-35m+36>0.

The first denominator in(R4) is sqrt525 when t=2 and sqrt2205 when
t=3; both are between16 and64. Hence, for every z>0,

                    z^2/64<=w<=z^2.                  (R5)

Keeping the z^2 in the LOWER bound is the point of this component.

Write Phi_s=a_s sin z+b_s cos z. The exact fixed-order entries are

 a2=3/z^3,                 b2=-3/z^2,
 a3=15(3-z^2)/z^5,         b3=-45/z^4,
 a4=105(15-6z^2)/z^7,      b4=105(z^3-15z)/z^7,
 a5=945(105-45z^2+z^4)/z^9,
 b5=945(10z^3-105z)/z^9.                              (R6)

The SAME cylinder-order recurrence and normalization give

                         Xi_s=-a_s cos z+b_s sin z.  (R7)

Thus, for real A,B, the common phase vector

 u=(A sin z-B cos z,A cos z+B sin z)

has squared norm A^2+B^2, and the ACTUAL weighted finite pair is

 (A Phi_t+B Xi_t,w(A Phi_(t+2)+B Xi_(t+2)))^T
              =Ltilde_t u,
 Ltilde_t=diag(1,w)L_t,
 rows(L_t)=(a_t,b_t),(a_(t+2),b_(t+2)).                (R8)

There is no channel-dependent free phase, complex-Hermitian substitution
or requirement that B be small.

### R3. Direct weighted singular-value certificate

Exact multiplication of(R6) gives

              det L2=-1575 z^-7,
              det L3=-99225 z^-9.                    (R9)

For example the z^-9 terms cancel in detL2, leaving
315z^-7-1890z^-7. In detL3 the z^-13 and z^-11 terms cancel,
leaving(-141750+42525)z^-9. These are symbolic identities.

For a real invertible2x2 matrix T,

            s_min(T)^2>=det(T)^2/||T||F^2.            (R10)

Indeed the two squared singular values have product det(T)^2,
and the larger is at most their sum ||T||F^2.

Suppose z>=1. For t=2 the four entries of Ltilde2, after extracting
z^-2, have absolute bounds

                         3,3,2205,1680.

For its second row this follows from w<=z^2 and

 |wa4|<=1575z^-5+630z^-3<=2205z^-2,
 |wb4|<=105z^-2+1575z^-4<=1680z^-2.

Therefore ||Ltilde2||F^2<2^26 z^-4. On the other hand (R5),(R9) give

 |det Ltilde2|=w*1575z^-7>2^4 z^-5.

Applying(R10) yields

                   s_min(Ltilde2)^2>2^-18 z^-6.       (R11)

For t=3, after extracting z^-3, the four absolute bounds are

                       60,45,142695,108675.

Explicitly the weighted second row is bounded by

 |wa5|<=945(105z^-7+45z^-5+z^-3)<=142695z^-3,
 |wb5|<=945(10z^-4+105z^-6)<=108675z^-3.

Thus ||Ltilde3||F^2<2^38 z^-6. Since99225>2^16, (R5),(R9) give

 |det Ltilde3|>2^10 z^-7,

and hence

                   s_min(Ltilde3)^2>2^-18 z^-8.       (R12)

For z>=1, z^-6>=z^-8. The two exact parity cases therefore give the
UNIFORM actual finite-pair inequality

 F_(m,t)^2+w^2 F_(m,t+2)^2
            >=2^-18 z^-8 (A_M^2+B_M^2).              (R13)

The z^2 upper bound on w was paid in each row norm and its z^2 lower
bound was paid in the determinant. We have not first multiplied an
unweighted lower bound by a constant min(1,w^2), nor discarded w^2.

### R4. Exact phase energy and actual zeta cutoffs

For the same M=m-1/2 and L=m-1, the accepted exact real phase identity is

 A_M^2+B_M^2
    =sum_(k=0)^L [c_(L,k)/c_(L,L)]z^(2(L-k)),
 c_(L,k)=(L+k)!/(L-k)! *binom(2k,k)/4^k.               (R14)

Every coefficient is positive and the constant term is1. Its finite
Laurent/third-order-ODE proof is the old accepted phase certificate,
not an unproved asymptotic premise. In particular for real z>0,

                           A_M^2+B_M^2>=1.            (R15)

Thus the Euclidean norm of the pre-zeta pair in(R13) is at least
2^-9 z^-4.

For each ACTUAL even cutoff n_s=m-s, s=t,t+2, the retained scalar-zeta
bound gives

 |F_(zeta,m,s)-F_(m,s)|<=epsilon_s=2^(-n_s/4),
         n_s>=64, |z|<=n_s/64.                       (R16)

This is the earlier full finite cutoff, not a replacement common n.
For m>=2^1000 and 1<=z<=m/128, both n_s>=m-5>=m/2, so(R16) applies.
For completeness, log2 m<=m/128 for m>=2048: at2048 it is11<=16,
and the derivative of the difference is
1/128-1/(m log2)>=1/128-2/m>=0 there. Also11<=m/128 in this range.
Consequently

 n_s/4>=m/8>11+6log2 m>=11+6log2 z,

so the actual errors obey

                         epsilon_s<=2^-11 z^-6.      (R17)

Use epszeta=max(epsilon_t,epsilon_(t+2)). Since w<=z^2 and z>=1, the
weighted pair error is at most

 sqrt(1+w^2)epszeta<=sqrt2 z^2 epszeta
                       <=2^-10 z^-4.                (R18)

Subtracting(R18) from the pre-zeta norm >=2^-9 z^-4 proves

 ||(F_(zeta,m,t),wF_(zeta,m,t+2))||2>=2^-10 z^-4.

Restoring the ORIGINAL -2 factor in(R3) gives the actual normalized
nonconstant-entry margin

 ||An^(-1)(<(Zxi-Z0)e_n,e0>,<(Zxi-Z0)e_(n-2),e0>)||2
                           >=2^-9 z^-4,
 squared norm              >=2^-18 z^-8.              (R19)

This holds on the stated finite-sum domain1<=z<=m/128. The constant
factor2, w^2, both finite cutoffs and shared phase were all retained.
It remains a pair estimate until the actual baseline is restored.

### R5. Recheck the amplitude on the new real square-root domain

We now impose the NEW physical real domain

                    pi<=z<=sqrt(m)/8.                (R20)

It is nonempty at the explicit m threshold, and lies inside z<=m/128,
because sqrt(m)>=16 for m>=256.

The old exact Student moment and monic-minimization identities give

 hn/h0<=E_m(v^(2n))
      =(2n)!/[16^n n!(t-1/2)_n]<=4^-n.                (R21)

For the last inequality use
(t-1/2)_n>=(1/2)_n=(2n)!/(4^n n!). Therefore

 An>=n! xi^(n-1)/pi^n
    =n!/[pi z^(n-1)].                                (R22)

Here n is even and n>=m-3>=m/2, so
n!>=(n/2)^(n/2)>=(sqrt(m)/2)^n. On(R20) this yields

 An>=(z/pi)(sqrt(m)/(2z))^n>=4^n>=m^3.               (R23)

Indeed z/pi>=1 and sqrt(m)/(2z)>=4. For the final comparison,
2n>=m and log2m<=m/16 for m>=256 imply
4^n>=2^m>=2^(3log2m)=m^3.
The log inequality holds at256 and its difference has derivative
1/16-1/(m log2)>=1/16-2/m>=0 there.

Thus(R23) is a genuine NEW-domain calculation. The earlier
xi>=m^-1/100 amplitude bound is not being extended by a label, nor
is a full-carrier upper bound inferred from this pair calculation.

### R6. Restore Z0 and obtain an actual full-state LOWER bound

For the original two matrix entries, the actual old baseline gives

 ||(<Z0 e_n,e0>,<Z0 e_(n-2),e0>)||2<=2sqrt2 m.

This is only the TWO-ENTRY baseline norm. We do not replace the full
baseline HS norm by2m. By(R23) its normalized contribution is <=3/m^2.

The nonconstant pair norm in(R19) is >=2^-9 z^-4. On(R20),

           2^-10 z^-4>=2^-10*8^4/m^2=4/m^2>3/m^2.

So the baseline is less than one half of this actual pair margin.
The original Z pair itself satisfies

 ||(<Zxi e_n,e0>,<Zxi e_(n-2),e0>)||2
                         >=2^-10 z^-4 An.             (R24)

The HS norm of the original full carrier Zxi dominates its two actual
entries. For real xi, the exact positive-adjoint identity is

 b(xi)=tr(Zxi+Zxi^dagger)^2
      =2tr(Zxi^2)+2||Zxi||HS^2.                        (R25)

In a degree-ordered polynomial basis the derivative corrections are
strictly lowering and Zxi has eigenvalues k-(m-1/2),0<=k<=m-2.
Hence tr(Zxi^2)>0, as in the original exact carrier proof. From(R24),(R25),

                   b(xi)>=2^-19 z^-8 An(xi)^2
                         >=2^-24 z^-8 An(xi)^2>0.     (R26)

The weaker2^-24 constant is available if a future unified whole wants
to retain the older state constant. The power8 and the domain(R20)
were actually derived; neither was preset as a premise.

Equivalently, for real y=z/pi and the actual reversal
Q(y)=y^(2ell)b(1/y)/Cxi^2=b(1/y)/An(1/y)^2,

 1<=y<=sqrt(m)/(8pi) =>
 Q(y)>=2^-19(pi y)^-8>=2^-24(pi y)^-8.                 (R27)

This is only a REAL state lower bound. It neither controls Q on a
complex disk nor proves a coefficient functional nonnegative.


## 6. Uniform growing-parameter complete COMMON consumer

### F2. One uniform exponent family and an effective symbolic threshold

Fix a rational exponent

               1/100 <= rho < 2/11, epsilon=2-11rho>0,
               m >= 2^ceil(10000/epsilon), mu=m^rho.       (F1)

This unexpanded threshold implies m>=2^1000, mu>=2^10 and rho<1/5.
The candidate lower/power interval is

              q+ceil(D/mu) <= j <= q+floor(D/2).        (F2)

Thus y lies in[2,mu], and every integer bound is shifted and inclusive.
Most importantly

                  y^11/m^2 <=m^(-epsilon)<=2^-10000.    (F3)

This is a whole exponent family, not a fixed numerical endpoint change.
The actual natural-domain and weighted real-state obligations are proved
in the preceding N and R sections. No coefficient no-go is inferred
from a failure of a sufficient interface outside this proved domain.

For |u-y|<=1/4, y>=2 gives |pi u|>1 and |Im(pi u)|<=pi/4<1.
Since pi<7/2 and mu>=2^10, |pi u|<4mu. Also

 m^(1/2-rho)>=m^(7/22)>=2^318>32,

so 4mu<sqrt(m-1)/4 and pi*mu<sqrt(m)/8.
These strict margins keep the ENTIRE outer disks inside(N3), not merely
their real centers. Similarly |u|<=mu+1/4<2mu<m/(512pi).
The actual normalization Chat=pi^ell Cxi cancels exactly as before.
The natural-domain amplitude >=m^3 is checked on the entire outer
z domain in(N3), so the true full-HS baseline 2m sqrt(m-1) contributes
less than1. The original -2singlepole factor plus the actual fullmatrix
zeta reversal then give

                  ||V||outer<=2^19, ||U||outer<=2^20,
                  |L|outer<=m^-3.                      (F4)

This retains both parities and analytic sharp via conjugation-invariance
of the same disk. It does not replace full HS by an operator/two-entry
norm. At the real center, the proved weaker bound(R26) cancels amplitude and gives

                         Q(y)>=2^-24(pi*y)^-8.         (F5)

### F3. Complete original Psi: the true growing-y adverse term

Keep alpha=(W+1)^2/(8W),tau=(m^4-1)/(24m),g=m tau,
a0=Dold-q. Exact reversal of EVERY original term gives

 P=[alpha a0(a0-1)-g]Q+alpha[2a0 uQ'+u^2Q'']
       +Cstar+K0 L^2,
 Cstar=2tau tr(Ae[V,U])-4tau L tr(Ae U),
 K0=(W-1)(W+1)^2(3W^2-10W+6)/(24W)>0.                (F6)

The single L in the linear trace, full W+1, unequal original COMMON
factors, q shift and second Euler derivative are not dropped.
As in the accepted narrow-domain calculation, (F4) gives actual
|Q|outer<=2^40, |Q'|inner<=2^43, |Q''|inner<=2^47,
|Cstar|outer<=2^44m^3 and
alpha a0(a0-1)-g>=m^6/64. The leading real term is at least
2^-30m^6(pi*y)^-8. Crucially do NOT immediately relax all adverse terms
to m^5. Their actual sum is

 2^44m^4 y+2^47m^2 y^2+2^44m^3 <=2^49m^4 y,          (F7)

because 1<=y<=mu<m and m>=2. Relative to the leading term it is at most

 2^79pi^8 y^9/m^2 <2^95 y^9/m^2
                         <=2^95m^(-epsilon)<1/2.      (F8)

The full K0L(y)^2 helps the real lower bound. Hence

                    P(y)>=2^-40m^6(pi*y)^-8.           (F9)

On the inner1/8 complex disk, |u|<=2y<=2m. The same six absolute
magnitudes are <=2^40m^6,2^45m^5,2^49m^4,2^40m^4,
2^44m^3,m^2 respectively. Therefore

              supinner |P|<=2^100m^6.                 (F10)

No real positivity is substituted for the complex derivative bound.

### F4. GLOBAL envelope and the exact phased transfer at growing y

The B13 coefficient bound, actual zeta<=2 and true baseline amplitude
>=m^3 give exactly as finite coefficient sums

 N_y(V)<=2^13m^.25 exp(4pi y),
 N_y(U)<=2^14m^.25 exp(4pi y), N_y(L)<=m^-3.

There is no y<=m^.01 premise in these coefficient inequalities after
the new amplitude has been actually checked. Full Euler/baseline/Clinear
and g(B+2) estimates yield

                    N_y(P)<=2^100m^7 exp(32y),         (F11)

not merely a carrier envelope. Here is the complete term accounting.
Trace convolution gives N_y(Q)<=2^28sqrt(m)exp(8pi y).
For each original coefficient b_k the upper Euler multiplier is
alpha(Dold-k)(Dold-k-1), with0<=(Dold-k)(Dold-k-1)<=m^4
for0<=k<=q. Thus its reversed b part is at most(m^6/2)N_y(Q).
Its COMPLETE B baseline contributes at most m^8N_y(L)^2<=m^2.
The exact Cstar has coefficient norm at most

 16tau N_y(V)N_y(U)+16tau sqrt(m)N_y(L)N_y(U)
 <=2^31m^(7/2)exp(8pi y)+2^18m^(3/4)exp(4pi y)
 <=2^32m^(7/2)exp(8pi y).

This includes the LINEAR single-L trace. The ENTIRE -g(B+2) correction,
including W+1, is at most
2^28m^(9/2)exp(8pi y)+2. The dominant term is bounded by
2^27m^(13/2)exp(8pi y); all these terms fit inside(F11), since m>=2
and pi<4. No sign of any complex coefficient was asserted.
Thus relative local and global hypotheses hold with

 h=1/8,M=2^164 y^8,G=2^164m y^8 exp(32y).

The accepted finite phased-contour lemma for J<=D/2 gives error

 512My^2/(J h^2)
       +8sqrt(J)(G+1+16My) exp[-J h^2/(4pi^2 y^2)].    (F12)

It is the exact finite Laurent functional, with shifted first moment
(D+1)/(J+1), not a Gaussian expectation or a positive functional on
all squares. Since J=D/y,D>=m^2/2, its first error is at most

                         2^180 y^11/m^2<1/16.         (F13)

The strong relation G=m exp(32y)M and m>=16y gives
G+1+16My<=3G. Also sqrt(J)<=m. Its far prefactor is <=2^8mG.
The far negative exponent A satisfies

 A=J/(256pi^2 y^2)>=m^2/(8192 y^3)
                         =m^2/(2^13 y^3).             (F14)

The logarithm of the positive prefactor is
<=172 log2+2log m+8log y+32y
<=120+10log m+32y.
Explicitly120<=m/8,32m^(1/5)<=m/8 and
10log m<=10m/16=5m/8 for m>=2^1000, so this expression is <=7m/8<m.
These inequalities pay the complete positive prefactor uniformly. Meanwhile
A>=2^-13m^(7/5)>=2m, because m^(2/5)>=2^400>2^14.
Therefore the far error is <=exp(-m)<1/16. This particular far proof
only needs rho<1/5; the near error is the actual bottleneck.
Consequently

                  T(P)>=P(y)/2>=2^-41m^6(pi*y)^-8.     (F15)

Multiplying the TWO positive original factors gives, by the
completed actual natural-domain and weighted real-state proofs above, the new SAMECOMMON band(F2)
with exact margin Kbinom(d,j)Cxi^2hq2^-41m^6(pi*y)^-8.
A finite rational weaker margin is

        Kbinom(d,j)Hn^2 hq2^(-6n-57)m^6(J/D)^8>0,     (F16)

using pi<4 and (2pi)^(2n)<2^(6n). No rescaling or factor is lost.


## 7. Exact original readout, authorship and honest sufficient frontier

For every original monomial degree q-s in Psi, dividing its falling
ratio by hq gives (D+1)_s,rise/(J+1)_s,rise EXACTLY. Therefore

 L_(d,j)Psi=Cxi^2 hq T(P),
 [S^(d-j)a^j]H_d^raw=K binom(d,j) Cxi^2 hq T(P).

Both K binom(d,j)>0 and Cxi^2hq>0 hold throughout(T2). The functional
uses D=d-q,J=j-q,y=D/J, not Dold or d/j. The first and last integers
are inclusive. At J=D/2 when integral the contour may meet u=0, but
P is a finite polynomial; no singularity occurs. This band does not
reach J=D, and no pending upper theorem is needed. Equations(F15)--(F16)
prove precisely(T3)--(T4), with no factor hq,Cxi or original K lost.

The sufficient frontier is epsilon=2-11rho>0 because the p8 actual
point margin and exact near error give y^(8+3)/m^2. The complete
original-Psi adverse term needs only y^9/m^2; the far tail wins against
exp(O(y)) under the wider condition rho<1/5. The NATURAL full-carrier
and weighted real-state proofs are genuine new input strengths, not a
renaming of an old absolute exponential bound. This accounting yields
one uniform family with an explicit threshold, not isolated numerical
constants. It is NOT an optimality theorem, a sign barrier at rho=2/11,
or a negative coefficient conclusion outside the sufficient range.

BFF constructed the natural-domain actual single-pole proof, including
its new amplitude check, and assembled this whole primary. 883 constructed
the direct ACTUAL weighted two-row singular-value proof, scalar-zeta and
wide-domain baseline/state composition. 7CDA constructed the complete
original-Psi growing-parameter consumer, phased-functional error budget,
unexpanded uniform threshold, integer band and both margins. Full
cross-author handchecks are genuine collaboration, not independent votes.
All old credit/NONBLIND remains; no optional unused CF component creates
automatic coauthorship. Root is routing/CONTROL only,not a second math vote.

The OLD accepted input theorem thresholds/stronger margins and all
original Source bytes remain unchanged. We do not claim all(T2) indices
were previously uncovered by every old theorem. This whole makes no
additional assertion for indices outside(T2) or a smaller m; already
accepted older bands retain their own truth. Genuine remaining lower
holes, full-C1/other homogeneous layers, all-j/full-P1/physical positivity,
the original trace inequality and mother Goal remain OPEN. No Tool,
Native/Task/ReviewRecord, Foundation/WorkingTruth or budget authority is
created. The later complete-upper proposal is neither rewritten nor
silently assumed accepted.

This is one prepared AUTHOR PROPOSAL. The external wholehandoff records
exact three bytepins and genuine same-three author consumption before
one freeze and independent review. All new load-bearing proofs are
in this primary; standalone workings and metadata preserve provenance,
not hidden accepted axioms. A genuine nonauthor may still REVISE. No
Source,peer verdict or final activity observation is guessed. No working
or repair is supplied to4A56/F736. All failures/STOP/HOLD and formal
cumulative-budget UNKNOWN remain;0 programmed scientific operations,
Native,newTask or budgetreset.
Mother Goal OPEN/global ending UNKNOWN;MESSAGE only,no FINAL.
