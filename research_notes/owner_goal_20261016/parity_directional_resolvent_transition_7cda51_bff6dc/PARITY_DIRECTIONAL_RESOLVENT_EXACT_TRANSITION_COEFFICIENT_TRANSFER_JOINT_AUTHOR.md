# Directional resolvents and exact coefficient transfer on a Parity transition scale

Status: FROZEN_JOINT_AUTHOR_PAPER_CANDIDATE_UNREVIEWED.

Authors: EM-DVR-BFF6DC and EM-PUBLIC-7CDA51. This is one proposed method unit:
a bounded, effective coefficient-functional estimate and its application to
the unchanged COMMON lower layer. It is not a new generic Tool, an outside
review, a complete middle-range theorem or a continuation of stopped science.
All prior NONBLIND authorship/review/CONTROL exposure remains. The future
outside reviewer4A56 has received no working or supplied any construction.
All computations here are symbolic hand mathematics; no programmed scientific
matrix/coefficient evaluation, import, test, sample or numerical integration
was performed.

## 1. Statement and the precise increment over the old inputs

Put d=m^2-3, xi=j/d and define the original finite functional

 L_(d,j)(lambda^k)=(j)_k,fall/(d)_k,fall, 0<=k<=d.

For integers m>=100 and 4m<=j<=6m, let Gamma be the closed, piecewise smooth
curve

 lambda(theta)=xi exp(i theta)/(1+|sin theta|),
                         -pi<=theta<=pi.                (1)

Let p_m be a polynomial of degree<=d. If throughout the closed
1/(200m) neighborhood of Gamma it obeys |p_m|<=H m^r, where H>0 and r
are independent of m and j, then

 |L_(d,j)p_m-p_m(xi)|<=2^250 H m^(r-1/2).                (2)

The same neighborhood includes the disk at xi needed below. Analyticity is
automatic for these polynomials; the stated shrinking-neighborhood norm
bound is a substantive hypothesis, not a statement for arbitrary squares.

The actual original Parity frame meets this hypothesis by a directional
numerical-range bound that extends beyond the old power-series operator-norm
majorant. Consequently, for every integer m>=2^1000 and 4m<=j<=6m,

 [S^(d-j)a^j]H_d^raw >= K binom(d,j)m^9/64>0,
 K=m^(2m^2)/2,                                          (3)

in the SAME original COMMON normalization. The range is bounded in j/m.
It does not meet the fixed-xi bulk band, does not cover j/m tending to
infinity, and does not settle all coefficients, P1, physical positivity,
the original trace inequality or the mother Goal. Its increment is the new
restricted transfer capability (2), not a claim of global novelty for
Cauchy integrals or an old endpoint constant renamed as a discovery.

## 2. Exact original object, cutoffs and readout

Use P1=[c]P(c), P(c)=(x+Wc+beta)G_W(x)T(c)/c,
x=W(S+a), W=m^2, beta=(W+1)/2 and G_W(x)=product_(h=1)^W(x+h).
The original T(c) is unchanged; no gcd division or new matrix input is made.
The exact old lower-layer readout is

 H_d^raw=K(S+a)^d Psi(a/(S+a)),
 Psi=C-g(B+2)+alpha[D(D-1)B-(2D-1)EB+E^2B],
 D=W-1, E=lambda partial_lambda,
 alpha=(W+1)^2/(8W), tau=(m^4-1)/(24m), g=m tau,
 B=b+W-1, b=tr(R^2), R=Z+Z^sharp,
 C=2tau tr(A_e[Z,R])-4tau tr(A_eR).                     (4)

The old top layer has prefactor m^2K and the lower layer K; alpha retains
that factor m^2. The scalar correction is B+2=b+W+1. Both Euler derivatives
and both terms of C are retained. The imported fixed-r0 differentiation was
taken before substituting lambda.

The actual space V has dimension m-1 and polynomial degrees<=m-2. Its old
positive auxiliary contour norm is the Student form

 integral_R |f(-1/2+iv)|^2(1+4v^2)^(-m) dv.

It is a positive normalization of the bilinear M-adjoint form after
reflection iota f(u)=f(-1-u), where
M(f,g)=[u^(m-1)]f(u)g(u)(1+u)^(-m). Let J=d/du=-i D_v,
Z0=(u+1/2)J-(m-1/2)I=vD_v-(m-1/2)I. Then

 Z_lambda=Z0-2sum_(k even,2<=k<=n)
              zeta(k)lambda^(k-1) D_v^k/(2pi)^k,       (5)

where n is the largest even integer<=m-2. The exact Fourier identity for
even Bernoulli coefficients and J^(2a)=(-1)^aD_v^(2a) give the minus sign.
This is the original finite gamma frame, not a new spectral observer.

The old bilinear adjoint agrees with the positive Hermitian adjoint on
the coefficients of Z because Z0 and the even derivatives commute with
iota. Z^sharp is obtained by taking those adjoints coefficient by coefficient.
For complex lambda it is (Z_(conjugate lambda))^dagger, not Z_lambda^dagger.
Thus R and all expressions in (4) are holomorphic matrix polynomials. Their
degrees are <=q=2n-2<=2m-6<d. The old bound ||A_e||<=4 concerns the genuine
even compressed multiplier A_e=(A+iota A iota)/2, A=B_(1/u^2); no rank-one
correction is discarded and the original finite-rho metric is not asserted
positive. Also ||Z0||<=2m, by the previously proved Student estimate.

For a polynomial p of the required degree,

 [S^(d-j)a^j]((S+a)^dp(a/(S+a)))
                      =binom(d,j)L_(d,j)p.             (6)

Neither (6) nor the positivity of the contour norm makes L positive on
arbitrary squares. In fact L((lambda-xi)^2)=-xi(1-xi)/(d-1)<0.

## 3. Directional control on the full circle space and the actual subspace

Let N=m-1 and first consider the full space of polynomial degrees<=N. Its
polynomials

 f_s(v)=(v-i/2)^s(v+i/2)^(N-s), 0<=s<=N,

are mutually orthogonal with one common positive norm. Indeed their
cross-products times w_m reduce under y=(v-i/2)/(v+i/2) to constant circle
measure times the monomial y^(s-t):
|f_s|^2w_m=4^(-N)/(1+4v^2). The real line parametrizes the circle once.
This uses the already known contour/circle identification.

Each f_s has leading coefficient1. The actual V is therefore exactly the
hyperplane sum_s a_s=0 in this orthogonal coordinate space. Differentiation
leaves V invariant. We use the full space only for upper inequalities,
not as an equality replacing the actual carrier.

Direct differentiation gives

 D_v f_s=-is f_(s-1)+i(2s-N)f_s+i(N-s)f_(s+1).         (7)

The row and column absolute sums are <=2m, hence ||D_v||<=2m. For the
Hermitian matrix Re(exp(i theta)D_v), the diagonal is (N-2s)sin theta and
the adjacent (s-1,s) entry is

 (2s-m)sin(theta)/2 - i m cos(theta)/2.

Its magnitude is <=m/2. Hermitian row sums now give the directional bound

 ||Re(exp(i theta)D_v)||<=m(1+|sin theta|).             (8)

Compression to invariant V preserves this numerical-range inequality. The
actual adjoint is its compressed adjoint, and the same inequality for D_v^dagger
follows by theta->-theta. In particular (8), not merely ||D_v||<=2m, gives

 ||Re(lambda D_v)||<=m(|lambda|+|Im lambda|).           (9)

The latter angular control is the additional capability used below. No
normality, diagonalization, coefficient positivity or scalar-spectrum
substitution is inferred.

## 4. Exact Bernoulli resolvents and a uniform thick complex domain

Nilpotence and the zeta sum in (5) give the exact identity

 Z_lambda=Z0-2lambda sum_(h>=1)
             D_v^2[(2pi h)^2I-lambda^2D_v^2]^(-1).     (10)

Every inverse in (10) is a finite polynomial. Summing h termwise recovers
the original finite coefficients. The scalar Bernoulli factors have real
poles after J=-iD_v; the actual finite matrix polynomial has no lambda
pole. The loss of a sufficient numerical-range domain would not be an
actual singularity or a negative-coefficient conclusion.

For (1), m xi<6.1. On its closed 1/(100m) neighborhood,
m(|lambda|+|Im lambda|)<6.12. The same holds for the actual adjoint.
Use the standard rational bounds 3.14<pi<22/7, so 2pi>6.28 and pi^2<10.
By (9), the real part of I plus or minus lambda D_v/(2pi h) is bounded
below by [1-6.12/(2pi h)]I. The elementary accretive inverse inequality
therefore gives norm<64 for each inverse. That inequality follows directly
from Re<v,Av>>=delta||v||^2 and Cauchy-Schwarz, implying ||Av||>=delta||v||.
Finite dimensionality gives invertibility. It does not require a normal A.

Factoring the quadratic inverse and using ||D_v||<=2m, sum h^(-2)<2 and
|lambda|<7/m bounds the correction in (10) by

 2|lambda|(2m)^2 64^2 sum_h(2pi h)^(-2)
          <(114688/9)m.

Adding ||Z0||<=2m yields ||Z_lambda||<=2^14m throughout that neighborhood.
The corresponding coefficientwise-adjoint formula gives the same bound
for Z^sharp. Thus

 ||R_lambda||<=2^15m,
 |b(lambda)|<=2^30m^3,
 |C(lambda)|<=2^34m^6.                                (11)

For C, use dimension<=m, ||A_e||<=4, the commutator estimate
||[Z,R]||<=2||Z||||R||, and both trace terms in (4). The bounds are valid
on the larger 1/(100m) neighborhood. Cauchy differentiation on disks of
radius1/(200m), centered anywhere on the smaller 1/(200m) neighborhood,
then gives

 |Eb|<=2^41m^3, |E^2b|<=2^53m^3.                      (12)

For example |b'|<=200m*2^30m^3 and
|b''|<=2(200m)^2*2^30m^3, with |lambda|<7/m. These are coefficientwise
holomorphic derivatives, not a moving Hermitian metric differentiation.

This resolvent domain has a fixed upper bound for j/m below 2pi. Neither
(10)-(12) nor the following transfer establishes any bound when j/m grows
without bound.

## 5. Exact Cauchy extraction and the cubic majorant

For every polynomial of degree<=d the exact identity

 Lp=[z^j](1+z)^d p(z/(1+z))/binom(d,j)

follows monomial by monomial. With z=lambda/(1-lambda), let
P_j=binom(d,j)xi^j(1-xi)^(d-j). Cauchy's formula becomes

 Lp=(1/P_j) integral_Gamma p(lambda)(xi/lambda)^j
       ((1-xi)/(1-lambda))^(d-j)
                     d lambda/[2pi i lambda(1-lambda)]. (13)

The curve is radial, simple, encloses0 once, is piecewise C1 and lies
strictly inside |lambda|<1. Thus the change of variable and the factor
(1-lambda)^(-1) in (13) are legitimate. No factorial weight or eta is
replaced by a Gaussian.

For theta>=0 set s=sin theta, h=cos(theta)/(1+s) and

 F(theta)=h-1+log(1+s).

Then F(0)=0 and F'=(cos theta-1)/(1+sin theta)<=-theta^2/10 on [0,pi].
Indeed 1-cos theta>=2theta^2/pi^2 and 1+sin theta<=2. Consequently

 F(theta)<=-theta^3/30.                               (14)

The exact normalized kernel in (13) has logarithmic modulus

 jlog(xi/|lambda|)+(d-j)[log(1-xi)-log|1-lambda|].

Here |lambda|<=xi. Keep the negative quadratic term:
log(1-xi)<=-xi-xi^2/2, while
-log|1-lambda|<=Re lambda+|lambda|^2/[2(1-|lambda|)].
Their quadratic difference is at most xi^3/[2(1-xi)]. Also

 (d-j)(Re lambda-xi)=j(h-1)+jxi(1-h), 0<=1-h<=2.

As (d-j)xi^3/[2(1-xi)]=jxi^2/2, the logarithmic modulus is at most

 jF(theta)+2jxi+jxi^2/2 <=jF(theta)+(5/2)jxi.

For m>=100 and j<=6m the last term is<100. By conjugate symmetry the
same bound holds at negative theta. Thus

 |normalized kernel|<=e^100 exp(-j|theta|^3/30).        (15)

The measure factor satisfies |d lambda/[lambda(1-lambda)]|<=3dtheta.
Finally j is a mode of Binomial(d,xi): floor((d+1)xi)=j. Variance is
<=j, and Chebyshev gives at least3/4 total mass within2sqrt(j) of the
mean. There are at most4sqrt(j)+1<=5sqrt(j) integers there, each of mass
at most P_j. Therefore

 P_j>=1/(8sqrt(j)).                                   (16)

Only exact finite-binomial facts have been used, not an asymptotic normal
approximation or a sampled mass.

## 6. Uniform transfer for the specified analytic families

The functional preserves constants and first moments exactly:
L1=1, Llambda=xi. Subtract p(xi)+p'(xi)(lambda-xi) in (13).
Under the hypothesis of (2), Cauchy/Taylor estimates give

 |p(lambda)-p(xi)-p'(xi)(lambda-xi)|
                         <=2^40 Hm^r theta^2.          (17)

Here are explicit bounds for both parts of the curve. If |theta|<=1/10000,
then |lambda-xi|<=14|theta|/m. Dividing by the available disk radius
1/(200m) gives at most .28, and summing the Taylor tail from degree2
gives the bound in (17). Outside that arc use |p(lambda)|,|p(xi)|<=Hm^r,
|p'(xi)|<=200Hm^(r+1), |lambda-xi|<=14/m and theta^2>=10^(-8).
This is also <2^40 Hm^r theta^2. No unbounded similarity norm enters.

The integral of theta^2 exp(-jtheta^3/30) from0 to pi is <=10/j.
Equations (13),(15)-(17) bound the error by

 120*2^40 e^100 Hm^r/sqrt(j)
                     <=2^250 Hm^(r-1/2).

For the last deliberately loose comparison use e<4 and j>=4m. This proves
(2) for the entire stated family, with explicit assumptions and constants.
It does not imply any sign for an arbitrary p_m. The thick-domain norm
assumption and the actual matrix resolvent are the essential new bridge.

## 7. The whole COMMON application with all prefactors and corrections

For real xi the actual R is Hermitian. Its trace is -(m^2-1), so the
positive Hilbert-Schmidt trace inequality in dimension m-1 gives

 b(xi)>= (m^2-1)^2/(m-1)=(m-1)(m+1)^2>m^3.             (18)

This is an evaluation bound only; (2), not generic positivity of L,
transfers it to coefficients. Apply (2) to b, Eb, E^2b, C and B+2,
using (11)-(12) on the required neighborhood. For every m>=2^1000,

 Lb>=m^3/2,
 |L(Eb)|<=2^42m^3, |L(E^2b)|<=2^54m^3,
 |LC|<=2^35m^6, |L(B+2)|<=2^32m^3.                     (19)

For instance the b error is <=2^280m^(5/2), less than m^3/2 at this
threshold; the largest other error exponent is2^303m^(5/2) for E^2b,
again negligible compared with its displayed bound. The scalar W+1 in
B+2 is included in |B+2|<=2^31m^3. Every degree remains <=q<d.

The positive constant W-1 in B adds to the leading term and its Euler
derivatives vanish. With alpha>=m^2/8, D(D-1)>=m^4/2, the leading term
in LPsi is >=m^9/32. Using alpha<=m^2, g<=m^4 and (19), all unfavorable
terms together are <=2^56m^7. For m>=2^1000 this is at most m^9/64.
Thus LPsi>=m^9/64, and (6) proves (3). Neither the linear term of C,
W+1, E^2b nor the factor m^2 in alpha has been dropped.

## 8. Coverage, author contribution and the unclosed gap

The literal COMMON/frame/readout, positive Student contour, reflection
adjoint, ||A_e|| bound, circle identification and Fourier/zeta identity
are reused at their exact frozen scopes. Numerical-range inverse estimates,
Cauchy extraction, Taylor subtraction and Chebyshev are classical methods,
not newly invented generic mathematics or a registered Tool.

The restricted new capability proved here is their exact composition on
the actual carrier and angular domain. The old coarse bound ||D_v||<=2m
only certifies its geometric majorant when m|lambda|<pi. At j/m in [4,6]
that particular certification does not apply at lambda=xi; no lower bound
on the actual ||lambda D_v|| is being asserted. The full angular support
and non-Gaussian contour control supply (2). This is a comparison with the
specified old certification in actually consumed inputs, not a claim that
all old Tools lack the capability or that all literature was searched.

BFF constructed the actual connection/sign intake, directional circle
matrix, resolvent representation/bounds and cubic-contour transfer route.
7CDA supplied the actual transition coefficient-functional target, the
complete exact log-kernel majorant derivation retaining its negative
quadratic term, the full readout/constant/prefactor integration and whole
exposition/self-check. The two authors shared new proof material; neither
may be this unit's independent reviewer. The preliminary checkerboard
cross-trace connection is retained as working history and is not a hidden
premise or a second result being frozen here.

This does not connect bounded j/m to the fixed-xi bulk band, prove a growing
j/m regime, or settle the complete raw layer. Suggested logarithmic-bulk
extensions remain unproved candidates and are excluded. The range and
threshold are deliberately explicit, not practical computation claims.
All old STOP/HOLD, actual identities and unknown formal cumulative budgets
remain; no Task/claim/Native science, Source/RA write or global ending
authority follows from this paper. Both authors completed whole-manuscript symbolic self-checking. This frozen
author candidate awaits genuine outside whole review; self-check is not a peer vote.
