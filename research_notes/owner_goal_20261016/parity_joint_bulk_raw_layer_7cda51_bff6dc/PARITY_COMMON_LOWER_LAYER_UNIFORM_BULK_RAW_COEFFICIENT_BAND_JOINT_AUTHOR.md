# A uniform bulk band of raw coefficients in the COMMON Parity lower layer

Status: FROZEN_JOINT_AUTHOR_PAPER_CANDIDATE_UNREVIEWED.

Authors: EM-PUBLIC-7CDA51 and EM-DVR-BFF6DC. This is one new whole unit.
The two authors supplied new and complementary constructions; neither is
its independent reviewer. All prior Parity/CM24/P11/CONTROL authorship and
review exposure is retained as NONBLIND. F736 supplied no new construction
or repair of this unit. The future outside reviewer4A56 has not received
working, supplied repair or made a verdict. Old endpoint/single-coefficient
votes do not review the present proof. No programmed/scientific matrix or coefficient evaluation, sampling or
numerical integration was used. Symbolic hand algebra, including the
determinants, finite sums and inequalities displayed below, was performed.

**Theorem proposed for independent whole review.** For every integer m>=2^100000, put d=m^2-3 and
K=m^(2m^2)/2. In the SAME original COMMON normalization, the actual degree-d
raw homogeneous component H_d^raw of the original c1 polynomial satisfies

 [S^(d-j)a^j]H_d^raw >= K binom(d,j) 2^(-512) m^12 >0

for every integer ceil(d/4)<=j<=floor(3d/4). This is a fixed positive-width
bulk fraction, distinct from the old initial O(m) band and the old narrow
terminal Theta(m^2) band. The huge explicit m threshold is not optimized.
The rest of the middle range, the entire layer for each m>=7, other layers,
physical P1 positivity and the original trace inequality remain OPEN.

Every load-bearing estimate is included in this single manuscript. Labels A
and B preserve contribution provenance, not separate papers or claims. All
upstream expressions and literal Source custody belong in the context; their
unchanged exact mathematical statements are recalled at the points used.

## A1. Exact target and imported mathematical interface

Keep the SAME actual COMMON polynomial and original carrier from the three
frozen upstream papers. In their notation P1=[c]P(c),
P(c)=(x+Wc+beta)G_W(x)T(c)/c, x=W(S+a), beta=(W+1)/2,
G_W(x)=product_(h=1)^W(x+h); T(c) is the unchanged original trace expression.
Set W=m^2, D=W-1, d=W-3 and K=m^(2W)/2. For its actual degree-d raw layer,

 H_d^raw=K(S+a)^d Psi(a/(S+a)),
 Psi=C-g(B+2)+alpha[D(D-1)B-(2D-1)E B+E^2 B],
 E=lambda partial_lambda, alpha=(W+1)^2/(8W),
 tau=(m^4-1)/(24m), g=m tau,
 B=b+W-1, b=tr(R^2), R=Z+Z^dagger,
 C=2tau tr(A_e[Z,R])-4tau tr(A_e R).                    (A1)

Here the old fixed-r0 differentiation took place before substituting lambda;
the top prefactor m^2 K versus the lower prefactor K is already in alpha.
The retained constant in B+2 is W+1. No normalization/gcd change is made.
Explicitly V=Q[u]_(degree<=m-2), J=d/du,
M(f,g)=[u^(m-1)]f(u)g(u)(1+u)^(-m), iota f(u)=f(-1-u),
Z_lambda=uJ-(m-1/2)I+gamma_lambda(J),
gamma_lambda(J)=(exp(lambda J)f(lambda J)^(-1)-I)/lambda,
f(z)=(exp(z)-1)/z, with the removable gamma_0=J/2.
Here I denotes the identity and iota denotes reflection. Let A be the
original M-compressed multiplier B_(1/u^2) and A_e=(A+iota A iota)/2. The nilpotent
cutoff J^(m-1)=0 makes every frame entry a finite polynomial in lambda.
On u=-1/2+iv use the old positive Student norm w_m=(1+4v^2)^(-m),
on the actual space of degrees <=m-2. Daggers are its positive Hermitian
adjoints. They agree with the old bilinear M-adjoint for the coefficients
of Z, since those commute with the reflection. Do not replace the adjoint
of uJ by an M-adjoint without this restriction.

Let n be the largest EVEN integer <=m-2, t=m-n in {2,3}, ell=n-1, q=2ell.
The actual degrees of Z and b are <=ell and <=q. In particular for odd m
the last missing even derivative is not reintroduced. The looser old bound
q<=2m-6 remains true. Put xi=j/d in [1/4,3/4]. For any actual polynomial p,

 [S^(d-j)a^j]((S+a)^d p(a/(S+a)))
       =binom(d,j) L_(d,j)p,
 L_(d,j)(lambda^k)=(j)_k,fall/(d)_k,fall.               (A2)

This is not a positive functional on arbitrary squares.

Write h_l^m=integral (P_l^m)^2 w_m, for the actual monic orthogonal
polynomials, and set

 H_n=n! sqrt(h_0^m/h_n^m),
 A_n=H_n xi^(n-1)/(2pi)^n.                              (A3)

The Pearson estimates proved below establish, for m>=10000 and this xi range,

 N0(Z):=sum_k ||Z_k||_HS xi^k <= e^5001 m^(1/4) A_n,
 Ndef(Z):=sum_k (ell-k)||Z_k||_HS xi^k
                                      <= e^5001 m^(1/4) A_n,
 N0(b)<=4e^10002 sqrt(m) A_n^2,
 Ndef(b):=sum_k(q-k)|b_k|xi^k <= e^10010 sqrt(m) A_n^2,
 A_n>=4 n!/16^n>=m^3.                                  (A4)

The exact mean formula proved below gives actual constant-output entries

 <(Z_xi-Z0)e_n,e_0>/A_n=-2F_t(pi/xi)+epsilon_t,
 <(Z_xi-Z0)e_(n-2),e_0>/A_(n-2)
                       =-2F_(t+2)(pi/xi)+epsilon_(t+2),
 |epsilon_t|,|epsilon_(t+2)|<=e^100/m,                  (A5)

where e_l=P_l^m/sqrt(h_l^m), Z0=v partial_v-(m-1/2)I and

 F_t(z)=sum_(s>=0) (-z^2/4)^s/[s!(t+1/2)_s,rise].

All inputs and the constant output in (A5) are in the SAME original carrier.
No rank-one correction of the old compression has been discarded.

## B1. Monic orthogonal polynomials with all parameters retained

Set v=(u+1/2)/i, Dv=d/dv, J=-i Dv and
w_m(v)=(1+4v^2)^(-m). Let P_l^(m) be the monic polynomial orthogonal for w_m,
and h_l^(m)=integral |P_l^(m)|^2 w_m. All integrals in this component are
paper expressions, not numerical integrations. For 0<=l<=m-1 they exist.
The actual carrier ends at m-2.

The already available self-adjoint Pearson operator is

 - (1+4v^2) Dv^2 +8(m-1)v Dv,

with eigenvalue4l(2m-1-l). Its monic eigenpolynomial has the exact coefficients

 P_l^(m)(v)=sum_(r=0)^floor(l/2)
   (-1)^r (l)_(2r,fall) v^(l-2r)
       /[16^r r! (m-l+1/2)_(r,rise)].                  (B1)

Substitution into that triangular differential equation proves (B1): the
coefficient recurrence denominator is8r(2m-2l+2r-1). Integration by parts
makes distinct eigenpolynomials orthogonal; boundary terms vanish in the
declared range. Consequently ordinary differentiation gives exactly

 Dv^k P_l^(m)=(l)_(k,fall) P_(l-k)^(m-k).                (B2)

The symmetric three-term recurrence and the v^(l-1) coefficient in (B1) give

 h_l^(m)/h_(l-1)^(m)
   = l(2m-l)/[4(4(m-l)^2-1)].                           (B3)

This is an identity on the actual polynomial space, not a sampled spectrum.

Repeated Pearson integration by parts also yields

 (l)_(k,fall)^2 h_(l-k)^(m-k)
   =4^k (l)_(k,fall)(2m-l-1)_(k,fall) h_l^(m).          (B4)

One can prove (B4) inductively from the k=1 energy identity and (B2).
Every shifted parameter m-k is at least2 when it is used below.

## B2. Exact actual means, not a guessed corner asymptotic

Let m-n=t be fixed and n even. For s>=0 with k=n-2s>=0, the normalized
Student moments obtained by one integration-by-parts recurrence are

 E_m(v^(2r))=(2r)!/[16^r r! (m-r-1/2)_(r,rise)].

Inserting these into (B1), or applying finite Chu-Vandermonde to the resulting
terminating sum, gives the exact identity

 E_m P_(2s)^(t+2s)
  = (-1)^s (2s)!/[16^s s!(t+1/2)_(s,rise)]
      * (n-2s)_(s,rise)/(m-s-1/2)_(s,rise).             (B5)

For clarity the terminating Vandermonde ratio is
(1+t+s-m)_(s,rise)/(3/2-m)_(s,rise); reversing the two products gives the
last ratio in (B5). This verifies the parameters and signs without a
general asymptotic assumption. Explicitly substitution of the moment formula
into (B1), with h=s-r, reduces the mean to

 (2s)!/[16^s s!(m-s-1/2)_s]
 *sum_(r=0)^s (-1)^r binom(s,r)(m-s-1/2)_r/(t+1/2)_r.

The finite identity sum(-1)^r binom(s,r)(a)_r/(b)_r=(b-a)_s/(b)_s
follows by induction from Pascal's identity: the next sum is the preceding
sum at (a,b) minus (a/b) times that at (a+1,b+1). Here
(b-a)_s=(t+s+1-m)_s=(-1)^s(n-2s)_s, which gives (B5).
All rising denominators used here are nonzero in the declared range.

For k>=2 denote that last ratio by rho_(m,t,s). Then0<=rho<=1. For every
fixed s it tends to1 as m tends to infinity. For s<=n/4, m sufficiently
large and t in {2,3,4,5}, comparing the individual product factors gives

 1-rho <= C (s^2+t s)/m,                                (B6)

with one absolute constant C. All denominators there are at least m-s-1/2.
This bound will be used only with fixed t in that four-element set.

## B3. The actual Bernoulli sign and the two possible corner parities

Let n be the largest even integer <=m-2 and put t=m-n, so t=2 or3.
Set l=n-1 and

 H_n=n! sqrt(h_0^(m)/h_n^(m)),
 A_n(xi)=H_n xi^(n-1)/(2pi)^n.

The variable xi is always in [1/4,3/4]. This A_n is an auxiliary scale, not
the old compressed multiplier A_e.

The finite actual frame, not a new arbitrary polynomial, satisfies

 Z_lambda=Z0+sum_(k even,2<=k<=n) G_(k-1) lambda^(k-1),
 Z0=v Dv-(m-1/2)I,
 G_(k-1)=-2 zeta(k)/(2pi)^k Dv^k.                       (B7)

Indeed gamma_lambda(J)-J/2 has coefficient B_k J^k/k!,
B_(2r)/(2r)!=2(-1)^(r+1)zeta(2r)/(2pi)^(2r), while
J^(2r)=(-1)^r Dv^(2r). Their product has the minus sign in (B7).
This sign cancellation must not be replaced by an alternating Bernoulli
coefficient while forgetting J=-i Dv.

The Bernoulli-zeta equality is classical reuse. It also follows directly
by integrating the Bernoulli polynomial against exp(-2pi i h x), repeatedly
using B_k'=kB_(k-1) and B_k(1)=B_k(0) for k!=1. Its absolutely convergent
Fourier series at x=0 for even k>=2 gives the displayed equality. It is not
a scientific coefficient-generation step or a claim of a new Tool.

For the normalized actual input e_n=P_n^(m)/sqrt(h_n^(m)) and output
e_0=1/sqrt(h_0^(m)), equations (B2),(B5),(B7) give

 <(Z_xi-Z0)e_n,e_0>/A_n(xi)
  =-2 sum_(s=0)^(n/2-1)
     (-1)^s zeta(n-2s) rho_(m,t,s)
       [pi^2/(4xi^2)]^s/[s!(t+1/2)_(s,rise)].           (B8)

The same equality with n replaced by n-2 has t replaced by t+2.
These are actual matrix entries, not hypothetical test states or a newly
selected readout. Both input polynomials belong to the original carrier.

The uniform limit of the sum is

 F_t(pi/xi)=sum_(s>=0)
  [-pi^2/(4xi^2)]^s/[s!(t+1/2)_(s,rise)].               (B9)

Here1<=zeta(k)<=2. Uniform convergence follows by domination with
2 a^s/(s!)^2, a<=4pi^2<64, and fixed-s rho->1. It can be made quantitative:
for s<=n/4 use (B6) and zeta(n-2s)-1<=2^(1-n/2); for s>n/4 use the first
moment of that summable majorant to bound the tail by C/m. Thus the error
in (B8) versus -2F_t is O(e^100/m), uniformly on the declared xi interval
and t in {2,3,4,5}; a larger fixed numerical constant can be chosen if desired.

The two necessary lower channels do not have a common zero. From the
power series one obtains

 F_t'=-x F_(t+1)/[2(t+1/2)],
 F_(t+1)-F_t=x^2 F_(t+2)/[4(t+1/2)(t+3/2)],
 x F_t''+2t F_t'+x F_t=0.

If F_t and F_(t+2) vanished at x>0, then F_t' would vanish too. Uniqueness
for this ordinary differential equation would contradict F_t(0)=1.
Therefore F_t^2+F_(t+2)^2 has a positive minimum on
x in [4pi/3,4pi], for t=2,3. This elementary series/ODE argument is enough;
no uninspected general Bessel theorem is needed.

The exact norm ratio from (B3) gives

 A_(n-2)(xi)/A_n(xi)
 = (2pi/xi)^2 sqrt(b_n b_(n-1))/[n(n-1)],
 b_j=h_j^(m)/h_(j-1)^(m),

which tends uniformly to
pi^2/[xi^2 sqrt((4t^2-1)(4(t+1)^2-1))].
It is consequently bounded above and below by positive constants for all
sufficiently large m. Together with (B8)-(B9), the two actual entries give
||Z_xi||_HS >= c A_n(xi), once the Z0 contribution is negligible.
The next section supplies the needed growth and upper-tail bounds.
Section A3 below fixes explicit constants and the threshold; no bare
compactness lower bound is used in the final quantified conclusion.

## B4. Uniform Hilbert-Schmidt tails from the actual cutoff

Since w_m<=w_(m-k), (B2)-(B4) imply the uniform exact upper estimate

 ||Dv^k||_HS,m^2
 <=4^k sum_(a=k)^(m-2)
       (a)_(k,fall)(2m-a-1)_(k,fall).                  (B10)

This controls all actual input degrees and therefore does not drop the
codimension-one/rank-one correction of the earlier kernel. It is not the
norm of an enlarged carrier used as an equality.

For comparison the baseline is exactly

 H_n^2
 =4^n n!(m+t-1)!/(2t-1)! *h_0^(m)/h_0^(t).             (B11)

Put k=n-r and c0=2t-1, with t=2 or3. The ratio of the sum in (B10) to its
factorial part in (B11) is

 4^(-r)c0! sum_(i=0)^(r+t-2)
  R_n(r-i)/[i!(c0+2r-i)!],
 R_n(h)=(n-h)!(n+c0+h)!/[n!(n+c0)!].                   (B12)

For h>=0, write its c0=0 part as a product of h ratios. At fixed h that
part decreases with n, so its maximum at n=h is binom(2h,h)<=4^h.
The additional c0 factors are each <=2. Thus R_n(h)<=2^c0 4^h.
The only negative h needed is h=-1 (when t=3), and then
R_n(-1)=(n+1)/(n+c0)<=1. It follows that (B12) is at most

 c0! 2^(2c0) 4^r/(c0+2r)!.

Also h_0^(t)<2 and h_0^(m)>=1/(4sqrt(m)): for the latter, integrate only
|v|<=1/(2sqrt(m)) and use (1+1/m)^m<4.
Combining these facts gives, for c0=3 or5,

 ||Dv^(n-r)||_HS,m^2/H_n^2
 <=2^20 sqrt(m) 4^r/(2r+c0)!.                          (B13)

The crude constant covers8 c0!2^(2c0). Every factorial is nonnegative in
the actual range; no derivative powers past the cutoff are retained.

For r=2s and the actual Bernoulli coefficients in (B7), (B13) gives

 ||G_(n-2s-1)||_HS xi^(n-2s-1)/A_n(xi)
 <=2^12 m^(1/4) [4(2pi/xi)^2]^s/sqrt((4s+c0)!).         (B14)

Since2pi/xi<32 and sqrt((4s+c0)!)>=(s!)^2, the sum of (B14), also
weighted by1+2s, is bounded by e^5000 m^(1/4). This deliberately huge
constant is independent of m and xi; it is not a numerical sampled bound.

It remains legitimate to absorb the constant frame. Monicity minimizes
norm, so h_n^(m)/h_0^(m)<=E_m(v^(2n))<=4^(-n) for t=2 or3 and n>=4
by the moment formula above. Hence

 A_n(xi)>=4 n!/16^n.

For m>=10000 and n>=m-3 this is larger than m^3. Indeed
n!>=(n/2)^(n/2), and n>=8192 gives sqrt(n/2)/16>=4. Thus
4 n!/16^n>=4^(n+1)>(n+3)^3>=m^3. The exponential/polynomial
comparison follows at n=3 and then by induction, not by sampling. The old ||Z0||<=2m therefore shows that its constant
coefficient and its degree-deficit weight are negligible compared with
m^(1/4)A_n. In particular, after harmlessly enlarging the fixed constant,

 sum_k ||Z_k||_HS xi^k <=e^5001 m^(1/4) A_n,
 sum_k (l-k)||Z_k||_HS xi^k <=e^5001 m^(1/4) A_n.        (B15)

All degrees satisfy k<=l=n-1. This is a coefficient-tail bound for the
actual frame, not a bound inferred from its value or its highest degree.

## B5. The actual coefficient concentration interface

Write R_k=Z_k+Z_k^dagger and b(lambda)=tr(R_lambda^2).
The positive Hilbert-Schmidt Cauchy-Schwarz inequality gives the ordinary
absolute convolution estimate for these actual matrix coefficients.
Thus (B15) yields

 sum_k |b_k|xi^k <=4e^10002 sqrt(m) A_n^2,
 sum_k (2l-k)|b_k|xi^k <=8e^10002 sqrt(m) A_n^2.

With the actual q=2l in this manuscript, the displayed estimates imply

 sum_k (q-k)|b_k|xi^k <=e^10010 sqrt(m) A_n(xi)^2.       (B16)

The same two-channel argument in Section B3, the Z0 growth just proved,
and ||R||_HS^2=2tr(Z^2)+2||Z||_HS^2 give b(xi)>=c A_n^2
uniformly for sufficiently large m. Consequently (B16) supplies the
actual noncancellation/concentration ratio O(sqrt(m))=o(m), not a
generic positivity statement for the coefficient functional.


## A2. Quantitative meaning of the uniform mean error

For completeness the constants in (A5) can be fixed without compactness-only
reasoning. In the B exact sum the coefficient multiplying the s-th summand is
zeta(n-2s)rho, with

 rho=product_(i=0)^(s-1) (n-2s+i)/(m-s-1/2+i).

For s<=n/4, t in {2,3,4,5} and m>=100,

 0<=1-rho<=2s(s+t)/m,
 |zeta(n-2s)-1|<=2^(1-n/2).

The latter is used only when n-2s>=n/2>=3. For every remaining actual
even index >=2 use merely 1<=zeta<=2. Write a=z^2/4<=64 and
v_s=a^s/(s!)^2. Then sum v_s<=e^(2sqrt(a))<=e^16,
sum s v_s<=64e^16 and sum s^2 v_s<=64e^16; the last identity bound follows
by shifting s^2/(s!)^2. The omitted/high-s tail is at most
(4/n)sum s v_s. Also m 2^(1-n/2)<=1 for m>=100 and n>=m-5.
Combining the low-s rho error, the low-s zeta error and the full high-s tail,
including the outside factor2, is less than e^100/m. This proves the exact
uniform numerical convention in (A5), rather than an unnamed O constant.

## A3. Two channels cannot cancel: an explicit lower bound

Put z=pi/xi; the crude interval 1<=z<=16 suffices. Direct comparison with
the sine and cosine power series gives

 F_2=3(sin z-z cos z)/z^3,
 F_4=105[(15-6z^2)sin z+(z^3-15z)cos z]/z^7,
 F_3=15[(3-z^2)sin z-3z cos z]/z^5,
 F_5=945[(105-45z^2+z^4)sin z+(10z^3-105z)cos z]/z^9.

For each t=2,3 view (F_t,F_(t+2)) as a 2 by2 real matrix times
(sin z,cos z). The respective determinants are exactly

 -1575/z^7 and -99225/z^9.                              (A6)

Every matrix entry has magnitude <=2^18 on 1<=z<=16, by bounding inverse
powers of z by1 in the displayed expressions. The determinant magnitude
is >=16^(-9)=2^(-36). Thus its least squared singular value is at least
determinant^2 divided by its squared Frobenius norm, hence >=2^(-110).
Since sin^2+cos^2=1,

 F_t(z)^2+F_(t+2)(z)^2>=2^(-110).                       (A7)

This is an explicit bound for the two actual channels, not an abstract
pointwise Gram argument for all coefficients.

The exact monic norm recurrence is

 beta_l=h_l^m/h_(l-1)^m
       =l(2m-l)/[16((m-l)^2-1/4)].

Consequently, for m>=100,

 w_n:=A_(n-2)/A_n
   =z^2/[4sqrt((t^2-1/4)((t+1)^2-1/4))]
      *sqrt((m+t)(m+t+1)/(n(n-1))),
 1/64<=w_n<=64.                                        (A8)

For the lower bound the square-root factor is >=1 and the denominator
outside it is <64. For the upper bound it is <2, while z<=16 and t>=2;
the same displayed expression is <64. Therefore the squared norm of the
two limiting entries in units A_n is at least
4*2^(-12)*2^(-110)=2^(-120).

The actual pair error from (A5),(A8) is <=65e^100/m. The Z0 pair has norm
<=2sqrt(2)m, since ||Z0||<=2m. In units A_n, (A4) bounds it by3/m^2.
For m>=e^500 each error is <=2^(-62). Hence the pair of actual Z entries
has norm >=2^(-61) A_n. The triangular eigenvalues of Z are real and
independent of xi, so tr(Z^2)>0. Thus, with no sign inference about L,

 b(xi)=||R_xi||_HS^2=2tr(Z_xi^2)+2||Z_xi||_HS^2
                           >=2^(-130) A_n^2.          (A9)

The intentionally weaker constant allows all of the preceding margins.

## A4. The scalar finite product follows the concentrated actual state

For m>=100 and the stated xi let

 eta(s)=(d/j)^s product_(l=j+1)^d(1-s/l), 0<=s<=q.

Since j>=m^2/5 and q<=2m, q/j<=1/10. Cancellation of factorials gives

 L_(d,j)b=sum_k eta(k)b_k xi^k.                         (A10)

The exact derivative is

 (log eta)'(s)=log(d/j)-sum_(l=j+1)^d 1/(l-s).

Comparison of right Riemann sums with the integral of1/x gives
0<=log(d/j)-sum1/l<=1/j. Also sum1/l^2<=(d-j)/j^2. Hence

 |(log eta)'(s)|<=1/j+q(d-j)/[j^2(1-q/j)]<=101/m.

The logarithm-series tail yields

 log eta(q)>=-q^2(d-j)/[2j^2(1-q/j)]>=-100,
 eta(q)>=e^(-100).                                     (A11)

For integer k, 0<eta(k)<=1, directly from the falling-factorial ratio.
For real 1<=s<=q, log eta is concave and vanishes at0 and1, so eta(s)<=1.
The possible real overshoot on (0,1) does not invalidate the following
integer bound: eta(0)=eta(1)=1, so integrate from max(k,1) to q to obtain

 |eta(k)-eta(q)|<=101(q-k)/m, integer0<=k<=q.            (A12)

Applying (A4),(A9),(A12), for all m>=e^50000,

 Lb>=eta(q)b(xi)-(101/m)Ndef(b)
   >=e^(-100)2^(-130)A_n^2
       -101e^10010 A_n^2/sqrt(m)
   >=e^(-231) A_n^2.                                  (A13)

Indeed 2^(-130)>e^(-130), the first term exceeds e^(-230), and
sqrt(m)>=e^25000 makes the second <e^(-14985). This is an actual
coefficient-functional lower bound derived from the degree-deficit control.
It is not L(square)>=0 or an unbounded similarity estimate.

## A5. Retaining the full differentiated top and the whole lower correction

For a polynomial p write N0(p)=sum|p_k|xi^k. Since eta(k)<=1 at integer
degrees, |Lp|<=N0(p). From (A4), A_n>=m^3 and q<=2m,

 N0(b)<=e^10004 sqrt(m) A_n^2,
 |L(Eb)|<=qN0(b), |L(E^2b)|<=q^2N0(b),
 N0(B+2)<=e^10006 sqrt(m) A_n^2.                        (A14)

To control C without losing the original compressed multiplier, use
||A_e||<=4 and ||A_e||_HS<=4sqrt(m-1), the old positive-contour estimates.
The first term of C has N0 <=32tau N0(Z)^2; the second has
N0 <=32tau sqrt(m)N0(Z). Since A_n>=m^3, (A4) gives

 N0(C)<=e^10010 tau sqrt(m) A_n^2.                      (A15)

This includes the linear trace term and constant frame. It does not assert
that a nonpositive compressed metric is positive.

Since D(D-1)>=m^4/2 and (2D-1)q+q^2<=5m^3,
(A13)-(A14) and sqrt(m)>=e^25000 give

 L[D(D-1)B-(2D-1)EB+E^2B]
                 >=e^(-231)m^4 A_n^2/4.               (A16)

The positive constant W-1 in B contributes to the first term and its
Euler derivatives vanish; it was not thrown into an unfavorable error.
As alpha>m^2/8, the positive contribution in LPsi is at least
e^(-231)m^6 A_n^2/32. On the other hand, tau<m^3/24 and g<m^4/24 give

 |LC|+g|L(B+2)|<=e^10011 m^(9/2) A_n^2.

For m>=e^50000 this is at most half the preceding positive term. Thus

 LPsi>=e^(-231)m^6 A_n^2/64
       >2^(-512)m^6 A_n^2>0.                          (A17)

The last elementary comparison uses e<4 and64=2^6. One explicit integral
threshold for the whole statement is M=2^100000, since e<4 implies
M>e^50000. No practical/optimal threshold, finite computational coverage,
unexamined smaller m or missing coefficient interval is asserted.

Combined with (A2), the new single-unit author claim is positivity
of the SAME COMMON degree-(m^2-3) raw coefficients for every integer
m>=2^100000 and ceil(d/4)<=j<=floor(3d/4), with lower bound

 K binom(d,j) 2^(-512)m^6 A_n(j/d)^2.

This is an explicit real lower expression: h_n/h_0 is a
finite rational product from beta_l, so A_n^2 contains only that product
and powers of pi. If a strictly rational numerical coefficient is desired,
the older bound A_n>=m^3 gives the weaker rational bound
K binom(d,j)2^(-512)m^12. No claim about every j, every m>=7, other layers,
physical P1, the trace inequality or the mother Goal follows.

## Scope, reuse and the independent-review boundary

The preceding proof is one new joint construction. The earlier kernel
rewrite and pointwise-Gram-to-coefficients route produced zero new signs;
they remain recorded as killed routes. Here their false implication is
replaced by the actual degree-deficit control (B16), the actual two-channel
lower bound (A9), and the exact scalar comparison (A10)-(A13).

The only newly selected external primary is NIST DLMF24.8.1, whose stated
Fourier domain includes x=0 for every even index used. Its complete selected
formula and receipt were read; no claim of reading the whole NIST chapter
is made. The Bernoulli sign is also derived in B3. No numerical constant was
estimated by running a series, a coefficient generator or a scientific test.
The giant explicit threshold is a paper bound, not a practical certificate
of the uncovered finite values or a claim of computational coverage.

No conclusion about all-j, full P1, the trace, a new formal Task, Native
acceptance or mother Goal completion follows. All historical STOP/HOLD
budgets remain unchanged. Both authors completed whole-primary, typed and context self-checking before
this immutable freeze. This is author checking, not a peer verdict. Genuine
outside whole-scope review remains pending.
