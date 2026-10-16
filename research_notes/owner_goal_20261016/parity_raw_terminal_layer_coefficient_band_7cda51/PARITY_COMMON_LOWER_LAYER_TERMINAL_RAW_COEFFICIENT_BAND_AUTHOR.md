# A terminal raw-coefficient band in the COMMON Parity lower layer

Status: FROZEN_AUTHOR_PAPER_CANDIDATE_UNREVIEWED.

Author: EM-PUBLIC-7CDA51. This is new paper work after the completed growing initial band, not an inference from that paper's independent review. The previous NONBLIND authorship, review and CONTROL history is retained. No scientific program or generated coefficient artifact is used.

## 1. The specified polynomial and the distinct new regime

Use the SAME original COMMON normalization

P(c)=(x+Wc+beta)G_W(x)T(c)/c, P1=[c]P(c),
W=m^2, beta=(W+1)/2, x=W(S+a),
G_W(x)=product_(k=1)^W(x+k).

Put D=W-1, d=W-3 and K=m^(2W)/2. The actual degree-d homogeneous component of P1 is denoted H_d^raw. This manuscript proposes the following different range of coefficients:

For integers m>=10000 and ceil(99999d/100000)<=j<=d,

[S^(d-j)a^j] H_d^raw >= K binom(d,j)m^9/32 >0.             (1)

The width is a fixed positive fraction of d, hence grows quadratically with m. It is a terminal band near the pure-a end, not an improvement of a constant in the old initial range j<=floor(m/6). The large lower bound on m is intentional and is not claimed optimal. No intervening coefficient, full layer, other homogeneous layer, physical P1 sign, trace inequality or all-M objective is settled. Small-m checks, computation and numerical coverage are not substituted for the quantified proof.

The exact COMMON layer and its fixed-r0 frame are consumed from the frozen 13131B original c1 paper, 16649B top-face paper and 21245B single-lower-coefficient paper. The positive contour estimates proved in the separate 13077B growing initial-band paper are consumed in their exact scope. No old peer vote decides this new claim. Exact Source paths and consumption belong in the accompanying context.

## 2. The old exact readout, with both prefactors retained

Let V=Q[u]_(degree<=m-2), n=m-1, J=d/du and

M(f,g)=[u^(m-1)]f(u)g(u)(1+u)^(-m).

The star initially denotes this nondegenerate bilinear M-adjoint. Put c0=m-1/2 and

Z_lambda=uJ-c0 I+gamma_lambda(J),
gamma_lambda(J)=(1/lambda)[exp(lambda J)f(lambda J)^(-1)-I],
f(z)=(exp z-1)/z,
R_lambda=Z_lambda+Z_lambda*.

The inverse is a terminating polynomial on V because J^(m-1)=0. The value at lambda=0 is removable, gamma_0=J/2. All matrices below are finite polynomials in lambda, not infinite operator substitutions.

Use the compressed multiplier A=B_(1/u^2), the reflection I f(u)=f(-1-u), and A_e=(A+IAI)/2. Set

tau=(m^4-1)/(24m), g=m tau,
B(lambda)=tr(R_lambda^2)+W-1,
C(lambda)=2tau tr(A_e[Z_lambda,R_lambda])-4tau tr(A_e R_lambda).

The old reflection trace identity permits A_e in this formula; it is not a matrix equality between the old metric correction and tau A. The exact raw lower-layer readout is

H_d^raw=K(S+a)^d Psi(a/(S+a)),
Psi=C-g(B+2)+alpha[D(D-1)B-2(D-1)lambda B'+lambda^2B''],
alpha=(W+1)^2/(8W).                                      (2)

In particular the top layer has prefactor m^2 K, whereas the lower layer has prefactor K. The translation correction in (2) already includes this m^2. The old centered reflection rules out the missing odd homogeneous layer, so only the displayed old top and lower layers enter. This manuscript does not alter the source normalization or differentiate at fixed lambda: the fixed-r0 derivative was taken in the imported exact frame before lambda substitution.

For a polynomial p define the actual coefficient functional

L_(d,j)(lambda^k)=(j)_k/(d)_k.

Then the coefficient in (1), divided by K binom(d,j), is exactly L_(d,j)(Psi). Degrees of Z and R are at most m-3, and degrees of B,C,Psi are at most q=2m-6<d. These are the actual nilpotent cutoffs, not continuation of a low-dimensional trace table.

## 3. The auxiliary Hilbert space and fixed quantitative estimates

On u=-1/2+iv use the positive form proportional to

integral_R f(-1/2+iv) overline(g(-1/2+iv))(1+4v^2)^(-m) dv.

It is the positive scalar normalization of M(f,I overline_coeff(g)). It is an auxiliary finite-dimensional form, not positivity of the original finite-rho metric. Z_lambda commutes with I coefficient by coefficient: Z0=(u+1/2)J-c0 I does, and gamma_lambda(J)-J/2 contains only even powers of J. Consequently its old M-star agrees with its positive Hermitian adjoint for real lambda. A dagger below denotes the latter adjoint, including when applied to an operator, such as uJ, that does not commute with I.

The previously proved integration-by-parts estimate gives

||J||<=2m, ||v partial_v||<=m, ||A_e||<=4.                 (3)

For clarity, its finite self-adjoint polynomial operator is

-(1+4v^2)partial_v^2+8(m-1)v partial_v,

with triangular eigenvalues 4k(2m-1-k), 0<=k<=m-2. Its largest eigenvalue is less than 4m^2. The declared cutoff makes all boundary terms vanish. This is the already established finite weighted estimate, not a newly sampled spectral claim.

Write U=uJ and A0=U-c0 I. Since J=-i partial_v on this contour,

||U||<=2m, ||A0||<=3m.                                  (4)

Let || ||_2 be Hilbert-Schmidt norm for this positive form. For every real lambda, Z has the triangular eigenvalues k-m+1/2, 0<=k<=m-2. Hence tr(Z^2) is a positive real number, independent of lambda, and

||R||_2^2=2tr(Z^2)+2||Z||_2^2>=2||Z||_2^2.

Also tr R=-(m^2-1), so Hilbert-Schmidt Cauchy-Schwarz gives

r(lambda)^2:=||R_lambda||_2^2 >= (m^2-1)^2/n
                              =n(m+1)^2>m^3.            (5)

These statements concern the real evaluation point used later. They do not identify a complex-lambda algebraic star with conjugating lambda.

## 4. A bounded Euler operator for the actual whole frame

The new comparison uses degree, not a small lambda J majorant. For E=lambda partial_lambda, homogeneity of J^k gives

E Z=-[U,Z]-Z+A0,
E Z^dagger=[U^dagger,Z^dagger]-Z^dagger+A0^dagger.          (6)

The second equation means the polynomial obtained by taking daggers of coefficients; for real lambda it is the Hermitian adjoint of Z. It is not a different moving metric. Equation (6) follows termwise from [U,J^k]=-kJ^k and the factor lambda^(k-1) in gamma.

Use the finite Hilbert direct sum of four matrix spaces and one scalar space. Its vector is

x(lambda)=(Z_lambda,Z_lambda^dagger,A0,A0^dagger,s0),
s0=m sqrt(n).

Define the constant linear operator T by

T(Z,Y,A,B,s)=(-[U,Z]-Z+A, [U^dagger,Y]-Y+B, 0,0,0).

Thus E x=T x exactly, including the constant terms. From (4),

||T||<=2||U||+2<=4m+2<=5m.                              (7)

At a real point lambda, equations (4)-(5) imply

||x(lambda)||^2=2||Z||_2^2+2||A0||_2^2+m^2n
 <=r(lambda)^2+19m^2n<=20r(lambda)^2.                    (8)

No scalar bound for an arbitrary nilpotent function is asserted. The added constant coordinates are what make (6) a homogeneous bounded linear equation.

On the tensor product use the projective norm: the infimum of sum ||x_i||||y_i|| over finite representations as sum x_i tensor y_i. In particular ||x tensor x||=||x||^2. The induced operator

S=T tensor 1+1 tensor T

has norm at most 10m. Every coefficient of the actual polynomial y(lambda)=x(lambda) tensor x(lambda) is an eigenvector of S with its nonnegative integer degree as eigenvalue, because E y=S y. Its degree is at most q. This coefficient identity is all the spectral information needed; no assertion that S is self-adjoint or normal is made.

Two bounded bilinear functionals encode the exact readout. Put R_i=Z_i+Y_i and set

b(x1 tensor x2)=tr(R1 R2),
c(x1 tensor x2)=2tau tr(A_e[Z1,R2])
                -(4tau/s0)tr(A_e R1)s2.

For the actual equal arguments, b(y)=tr(R^2) and c(y)=C. Trace Cauchy-Schwarz and (3) give

||b||<=2,
||c||<=16sqrt(2)tau(1+1/m)<=32tau.                      (9)

For the linear term use ||A_e||_2<=4sqrt(n) and s0=m sqrt(n). These are bounds for bilinear functionals on the declared projective norm, not a positivity claim for L on squares.

## 5. An exact finite-product comparison for the coefficient functional

Fix an integer j in (1), and put xi=j/d. For every integer 0<=k<=q,

eta(k):=xi^(-k)(j)_k/(d)_k
       =(d/j)^k product_(l=j+1)^d(1-k/l).                (10)

This follows by cancelling factorials; the same expression would also vanish at j<k<=d. Empty products at j=d equal one. On the actual polynomial coefficient space define

eta(S)=exp(log(d/j)S) product_(l=j+1)^d(1-S/l).

Using the eigenvector identity after (8), equation (10) gives the exact vector relation

L_(d,j)(y)=eta(S)y(xi).                                  (11)

This does not evaluate L at random points, change the polynomial, or identify L with a positive integral. Exponentials and logarithms here are convergent series of a fixed finite linear operator used in a paper norm estimate.

Let t=10m. In our range j>=9m^2/10 and t/j<=1/900. The logarithm series therefore converges absolutely in operator norm. All its factors commute. Its linear part and tail give

||log eta(S)||
 <=t[log(d/j)-sum_(l=j+1)^d 1/l]
   +sum_(h>=2)(t^h/h)sum_(l=j+1)^d l^(-h)
 <=t(d-j)/(jd)+(d-j)t^2/[2j^2(1-t/j)].                  (12)

For the linear bound compare the decreasing function 1/x with its integrals over the adjacent unit intervals: the bracket is nonnegative and at most 1/j-1/d. For the tail use sum l^(-h)<=(d-j)/j^h and 1/h<=1/2. Thus no gamma-function asymptotic or imported quantitative Bernstein theorem is required.

Since d-j<=d/100000<=m^2/100000, j>=9m^2/10 and 1-t/j>=9/10, (12) is at most

1/(9000m)+1/1458<1/1000.                                (13)

For example the first term is less than 1/10000 at m>=10000, and the second is less than 7/10000. The coarser inequalities are chosen to avoid optimization. The hypothesis j>=9m^2/10 follows directly from j>=99999(m^2-3)/100000 and m>=10000.

Put h0=1/1000 and delta=exp(h0)-1. The norm-exponential series gives

||eta(S)||<=exp(h0)<=1000/999<11/10,
||eta(S)-1||<=delta<=1/999,
40delta<1/20.                                          (14)

The inequality exp(h0)<=1/(1-h0) follows termwise from its scalar series. All constants are independent of the target j and of m in the stated range.

## 6. Apply the comparison to the full raw layer

In the following estimates r=r(xi). From (8)-(11) and (14),

|L(b(y))-r^2|<=40delta r^2,
|L(E b(y))|<=40t exp(h0)r^2,
|L(E^2 b(y))|<=40t^2 exp(h0)r^2,
|L(C)|<=640tau exp(h0)r^2<=704tau r^2.                  (15)

For the derivative identities use E y=S y before applying (11). The bound for C controls its entire polynomial, including its commutator and linear terms; it does not reuse the old six traces as though they eliminated all higher coefficients.

The differentiated top operator in (2) is

D(D-1)B-(2D-1)E B+E^2 B.

After dropping the nonnegative constant D(D-1)(W-1), (15) bounds its coefficient-functional value below by

{D(D-1)(1-40delta)
 -40exp(h0)[(2D-1)t+t^2]}r^2.                           (16)

As D(D-1)>=m^4/2, 2D-1<=2m^2 and t=10m,

40exp(h0)[(2D-1)t+t^2]/[D(D-1)]
 <=88(20/m+100/m^2)<1/5                                (17)

for m>=10000. Indeed the two terms are at most 176/1000 and 1/1000 respectively. Together with 40delta<1/20 this makes (16) at least (3/4)D(D-1)r^2.

Also W+1<=r^2 by (5), so

L(B+2)<= (1+40delta)r^2+(W+1)<3r^2.                    (18)

The sign of L(C) is not assumed. Combining (2) and (15)-(18),

L(Psi)>=[(3/4)alpha D(D-1)-(704+3m)tau]r^2
 >=[3m^6/64-(704+3m)m^3/24]r^2
 >=(m^6/32)r^2>m^9/32.                                (19)

For the last comparison use 704<=m, so the subtracted term is at most m^4/6, which is at most m^6/64 in this range. Multiply (19) by the positive K binom(d,j) to obtain (1). The endpoint j=d is included: eta(S) is then the identity, so no singular limiting interpretation is needed.

## 7. Why this is a different finite gap, and what remains open

The old initial-band proof required xi||J|| small and covered j=O(m). Here xi is close to one and that smallness fails. The actual replacement is the finite-product formula (10) on a bounded Euler operator and its tensor square. The small parameter is (d-j)||S||^2/j^2, not xi||J||. It controls the true coefficient functional, including its failure to be positive on squares. Both frame derivatives and the complete C polynomial are retained. This is one growing terminal band, not separately counted coefficients or a constant refinement of the initial band.

The earlier reproducing-kernel/circle-coordinate intake remains an unsuccessful sign route: its exact representations alone gave zero new signs. This proof does not recast those expressions as a new tool. The new mechanism is the comparison (11)-(15) specialized to the actual whole frame with its fixed trace coercivity.

There is still a large unresolved region between the two bands, and all coefficients at m<10000 outside old coverage remain outside this new statement. No complete homogeneous-layer positivity follows, much less full P1 or trace positivity. The threshold 10000 and the fraction 1/100000 are explicit conservative paper constants, not actual sampled cutoffs or numerical certificates. They do not authorize or restart an exhausted computational task.

This is solely author work pending genuine whole-proof review. Future 4A56 has received only previously frozen background inputs and has supplied no new construction or repair; the unfrozen working was not sent to that future peer. A fresh whole-scope independence declaration and genuine review of the frozen three notes are still required. All earlier author/reviewer identities and NONBLIND exposure are retained. Scientific programs, imports, compilation, tests, samples, matrix or coefficient evaluation, generated expansions, new Task/Native mutations, Tool registration and Native votes are zero. Own canonical34 remains unchanged, mother Goal remains OPEN, and every original STOP/HOLD and budget remains unchanged.
