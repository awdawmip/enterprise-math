# Highest actual even derivative: signed Ae boundary calibration

Status: LOCAL_AUTHOR_PROOF / UNREVIEWED / RESULT_ONLY_COMPOSE.
New proof author: BFF, original EM-DVR-BFF6DC Driver. No new Source,
scientific program, Native execution, RA, helper, identity or budget.
The full signed complex-lens C estimate and fullPsi remain HOLD.

## 1. Exact finite target and the two actual old interfaces

Every integer m>=7 is allowed. Put N=m-2, n=m-1 and
K=2floor((m-2)/2). The actual carrier is all complex polynomials of
degree<=N in the ORIGINAL positive Student pairing

    <f,g> = integral conjugate(f(v)) g(v) (1+4v^2)^(-m) dv.

J=-iD_v and Ae is the actual orthogonal compression of
q(v)=8/(1+4v^2)^2-4/(1+4v^2). All adjoints below are actual positive
pairing adjoints; J^K has real coefficients since K is even.
There is no shifted Student model.

The full literal Z and scalar C are

    Z(lambda)=X+sum_(even k=2..K) B_k lambda^(k-1) J^k/k!,
    X=vD_v-(m-1/2)I,
    C(lambda)=2tau tr Ae[Z,Z#]-4tau tr Ae(Z+Z#),
    tau=(m^4-1)/(24m).

Coefficient# is the analytic coefficient adjoint, leaving lambda fixed.
Define E_K=||J^K||_HS^2>0 and
D_K=tr Ae[J^K,(J^K)^dagger]. This finite target is genuinely signed,
not a bound obtained by taking absolute values of the two terms.

The actual accepted coordinate input is A's original19834:
Source13f33f67bc0838034b6caecb99aa941b1ca64027,
research_notes/owner_goal_20261017/student_positive_gram_cayley_bridge_7cda51/ACTUAL_STUDENT_CAYLEY_FRAME_POSITIVE_GRAM_AND_FULL_C_TRACE_BRIDGE_WORKING_AND_CONTEXT.md,
SHA2568be13374dc117c3cb97f9898cc0b666989543e0ee5cc38474645d0444d76b749,
Gitblob8f66bf405a1dcd7c0447eb1f60e1c1cac8623ca8.
BFF actually whole-read all nine sections/F1-F21/context, personally
bound the complete immutable author body and exact1ADD/soleparent,
and completed the NONBLIND18083 technical whole and ownpeerSource
aae06e96a0c296c473d099ed21d592d9fc55e507. A separately reports complete
ordinary2/37917; her API is not BFF's observation.

The original Ae/q/fullC/normalization input is accepted17239:
Source878066668ccca45e66b8791833eaa0ce85ba26d3,
research_notes/owner_goal_20261016/parity_actual_Ae_pole_cut_prefix_feasibility_7cda51/ACTUAL_STUDENT_AE_PARITY_CUT_POLE_FACTORS_AND_FULL_TRACE_PREFIX_FEASIBILITY.md,
SHA2561c42dee3c1ebba1cdbac1b1e5ae7a5f21082043930343645b0dbdd73dd275241,
Gitblob55f675dcf64b9edd5d969f2de5f7daef97f113b9.
BFF's old complete authorwhole/ownauthorSource and genuine17134 review/
ownpeerSource78643ff20f70e4f235f5dc55982e05a6a846412f are honestly reused.
No fresh old-body API or independent vote is claimed here.
No A later polarized generating-kernel formula is an input.

Claim: for all the stated m,

    (27/14) E_K <= D_K < 4E_K.                         (1)

For the actual Gram-pencil boundary Delta from19834,

    -60 E_K/m^2 < tr Delta[J^K,(J^K)^dagger] < 0.      (2)

The numerical factor60 is a simple uniform envelope, not a sharp claim.
More precise formulas for both parities are supplied below. These
results calibrate the highest block only; they do not sum the whole Z.

## 2. Actual Gram coordinates and two Riesz vectors

Use b_j=(1+2iv)^j(1-2iv)^(N-j), j=0..N. The original positive Gram
and the Ae form/operator are exactly

    G=(pi/8) B,  B=2I+A,  P=B^-1,
    H=(pi/16) T,  Ae_matrix=(1/2) PT,
    T=BAB+R.

A is the path adjacency of size n. R has diagonal4 at the two
endpoints and symmetric edge1 between each endpoint and its neighbour.
Thus R consists of two disjoint blocks [[4,1],[1,0]], since n>=6.
Let Delta_matrix=(1/2)PR and Bulk_matrix=(1/2)AB. They are selfadjoint
in the actual G pairing and Ae=Bulk+Delta. Delta is indefinite rank4;
it is not a PSD repair.

Let S=diag((-1)^j), t=j+1 (so 1<=t<=m-1), and
D=2I-A=SBS. The two elementary Dirichlet solutions are

    w0_t=t(m-t)/2,       Dw0=1,
    w1_t=t(m-t)(2t-m)/6, Dw1=d,  d_t=2t-m.           (3)

Both vanish at t=0,m. The cubic second difference verifies the second
formula directly; it is not a continuous-differentiation approximation.
Consequently P times the alternating constant vector is Sw0 and P
times the alternating d vector is Sw1.

The coefficient functional of v^N on b_j is
(2i)^N(-1)^(N-j). That of v^(N-1) is
(2i)^(N-1)(-1)^(N-j)(2j-N). Its Riesz vector in the G pairing is
therefore a scalar multiple of Sw0 or Sw1, respectively.
The first annihilates all lower-degree polynomials. The second
annihilates degrees<=N-2; by the original even measure its parity is
N-1 and hence is orthogonal to the other, parity-N top vector.
Thus their normalized vectors are exactly the actual orthonormal
degree-N and degree-(N-1) inputs, denoted e_N and e_(N-1).
No auxiliary degree-m carrier is introduced.

The elementary finite sums needed for their norms are

    S0=sum w0_t=m(m^2-1)/12,
    S1=sum d_t w1_t=m(m^2-1)(m^2-4)/180.              (4)

These follow by expanding the polynomials in t and summing t through
t^4; equivalently both sides have the same polynomial finite difference
and vanish at the first endpoints. In particular they are positive.

## 3. Input Ae values: actual bulk-boundary cancellation

After alternating sign conjugation, T becomes
D(-A)D+SRS. Therefore

    <e_N,Ae e_N>=(w0^T(STS)w0)/(2S0).

The bulk numerator is -1^T A1=-2(m-2).
At either endpoint w0=(m-1)/2 and its neighbour is m-2.
The total boundary numerator is
2[4((m-1)/2)^2-2((m-1)/2)(m-2)]=2(m-1).
Their SUM is2, not a quantity of order m. Hence, writing eta for input
expectations and a superscript b for the actual boundary part,

    eta_N=12/[m(m^2-1)],
    eta_N^bulk=-12(m-2)/[m(m^2-1)],
    eta_N^b=12/[m(m+1)].                              (5)

This is an explicit cancellation from separate O(m^-2) contributions
to O(m^-3) in the ORIGINAL positive norm.

For w1, the bulk numerator is -d^TAd. The exact adjacent sum is

    d^TAd=2m(m-2)(m-4)/3.

Its endpoint value is -(m-1)(m-2)/6 and the next value is
-(m-2)(m-4)/3. The total boundary numerator is
2(m-1)(m-2)^2/3. Subtracting the bulk gives
2(m^2-4)/3. With the factor1/(2S1), this proves

    eta_(N-1)=60/[m(m^2-1)],
    eta_(N-1)^bulk=-m(m-2)(m-4)/(3S1),
    eta_(N-1)^b=60(m-2)/[m(m+1)(m+2)].               (6)

Again the order m^-3 value is the signed sum of order m^-2 terms.
Equations(5)-(6) retain both endpoint blocks and all boundary signs.

## 4. Output values and a genuinely small signed boundary contraction

The only outputs of the highest even derivative are constants when
N is even, or constants and v when N is odd. Write e0=1/||1|| and
e1=v/||v|| in the actual original pairing. Direct beta integrals, or
their elementary contiguous integration-by-parts ratios, give

    ||v||^2/||1||^2=1/[4(2m-3)],
    mu0=<e0,Ae e0>=4-6/(m+1),
    mu1=<e1,Ae e1>=2(2m-3)(m-2)/[m(m+1)].           (7)

For example integral rho_(m+1)/integral rho_m=(m-1/2)/m;
with v^2 inserted the ratio is (m-3/2)/m. Applying it twice to
q=8rho_(m+2)/rho_m-4rho_(m+1)/rho_m proves both displayed values.
This is a computation of actual expectations, not an auxiliary model.

Put Fm=binom(2m-3,m-2). The b-coordinates of1 are
u_j=2^(-N)binom(N,j), giving
u^TBu=2*4^(-N)Fm and u^TRu=4m*4^(-N).
Those of v, up to an irrelevant common imaginary phase, are
h_j=2^(-N-1)[binom(N-1,j)-binom(N-1,j-1)].
Then h^TRh=N*4^(-N), and its Gram norm is u^TBu/[4(2m-3)].
All binomials out of range are zero. Consequently

    mu0^b=m/Fm,
    mu1^b=(m-2)(2m-3)/Fm.                            (8)

Both endpoints, including the reflected signs of h, have been included.

For every m>=7 the strict finite inequality

    Fm > m(m+1)(m-2)(2m-3)/12                        (9)

holds. At m=7 it is462>770/3. Its left-hand ratio at the next m is
4-2/m>=26/7. The right-hand ratio is
((m+2)/m)*((m-1)/(m-2))*((2m-1)/(2m-3)),
at most (9/7)(6/5)(13/11)=702/385<26/7.
Thus induction proves(9), without asymptotic or numeric enumeration.

It follows that mu1^b<eta_N^b. Also mu0^b<mu1^b and
eta_N^b<=eta_(N-1)^b (the last ratio is5(m-2)/(m+2)>1).
Therefore the signed boundary differences relevant below satisfy

    -12/m^2 < mu0^b-eta_N^b < 0,
    -60/m^2 < mu0^b-eta_(N-1)^b < 0,
    -12/m^2 < mu1^b-eta_N^b < 0.                    (10)

This is a true endpoint-weighted signed estimate, not merely a
rank-four operator norm or termwise unweighted HS bound.

## 5. Both highest even blocks and the complete C leading coefficient

If m is even, N is even and K=N. The actual operator J^N has a single
nonzero input/output channel e_N to e0. Thus

    D_K/E_K=mu0-eta_N.                               (11)

Its boundary analogue is exactly mu0^b-eta_N^b.

If m is odd, N is odd and K=N-1. The two channels are e_(N-1) to e0
and e_N to e1, with squared strengths a>0 and b>0:

    a=(K!)^2 ||1||^2 ||leading_(N-1)||_*^2,
    b=(K!)^2 N^2 ||v||^2 ||leading_N||_*^2.

The stars on the two scalar functional norms mean Riesz dual norms,
not a changed coefficient# convention. The preceding Riesz formulas
give the exact ratio

    b/a=15(m-2)/[(2m-3)(m+2)].                       (12)

Indeed ||leading_N||_*^2/||leading_(N-1)||_*^2
=4S0/S1=60/(m^2-4), which with(7) proves(12).
The inputs and outputs are mutually orthogonal in the ORIGINAL
pairing. Therefore

    E_K=a+b,
    D_K=a(mu0-eta_(N-1))+b(mu1-eta_N).               (13)

The boundary contraction is obtained by replacing each expectation
with its superscript-b value. Equation(10) proves(2) in both parities.
In particular it is strictly NEGATIVE, not unsigned and not absent.

For m>=7, mu0>=13/4, mu1>=55/28,
eta_N<=1/28 and eta_(N-1)<=5/28. The second lower bound follows
directly from (2m-3)/m>=11/7 and (m-2)/(m+1)>=5/8.
Thus every difference in(11)-(13) is at least27/14, while each is
strictly below4 because mu0,mu1<4 and both input values are positive.
This proves(1), with no claim of a sharp uniform constant.
The bulk contraction is consequently positive and is the total
minus the strictly negative boundary term.

Finally K>=4. The highest power of lambda in the complete scalar C
has degree2K-2. Only the highest Bernoulli term paired with itself
can contribute there. X, every lower derivative and the COMPLETE
linear term have lower degree. Their absence in this one coefficient
is a degree statement; they have not been discarded from C.
The classical nonzero even Bernoulli coefficient gives

    [lambda^(2K-2)] C
       =2tau (B_K/K!)^2 D_K > 0.                    (14)

The same coefficient of its boundary part is strictly negative and
has absolute value less than (60/m^2) times
2tau(B_K/K!)^2 E_K, or at most280/(9m^2) times the total coefficient.
This statement is about actual full C, not about an arbitrary nilpotent
test operator or a scalar trace multiplied by a matrix.

In the original physical reversal M=cV, with c=Chat w^(-ell),
the ENTIRE scalar still has its distinct quadratic factor c^2 and
linear factor c. Equation(14) does not delete or merge either one,
and does not discard baseline/Z0/zeta crosses in any full caller.
There is no off-real Hermitian/analytic# substitution.

## 6. Exact stopping point, contribution history and unproved continuation

This is a new BFF finite signed calibration built from the original
accepted coordinate/pencil and actual Ae/C definitions. A owns the
basis/positiveGram/fullC bridge; BFF's previous technical checking is
not coauthorship of19834. A's future all-degree polarized trace
mechanism is a different occupied obligation and no unpublished
formula or repair from it was used here. Root supplies0mathvote.
All relevant old private/warm histories remain NONZERO; no reviewer
qualification or coldblind claim is made for this new author proof.

The success criterion for this bounded round is met: the highest
actual even block has a signed endpoint estimate of order m^-2,
and its top input expectations exhibit an explicit m^-2 to m^-3
bulk-boundary cancellation. It is not a renaming of the old
exp(2|Im w|) absolute-HS envelope.

The continuation is still quantitative HOLD: no estimate for the
OTHER mixed derivative orders, their Bernoulli summation on the
actual complex lens, the full signed raw quadratic-plus-linear C,
baseline/Z0/zeta crosses, or fullPsi is supplied. A bound on one
highest coefficient cannot be substituted into a bound on a
polynomial at complex lambda. These identities neither prove nor
rule out the needed lens/reference inequality; no no-go is claimed.
No inference about actual Ae eigenvalues/norm, a bounded-rank PSD
repair, physical time/Native dynamics, coefficient margins, another
carrier or a new general Tool/paper is made.

This LOCAL artifact has no author Source or independent final review
at creation. Its actual complete self-read and bytepin follow the
write; they do not themselves create independent acceptance.
All old STOP/HOLD/UNKNOWN/authority/budget/error histories and parent
Goal OPEN are retained unchanged.

