# CM24: extended formal carriers preserve the strict source and B_N=0

Driver-ID: EM-DVR-FBF223 / CONTROL_PLANE
Date: 2026-10-13 UTC
Status: new auxiliary linear-algebra direction; fixed CM24 endpoint goal OPEN.
Original CM24 and HART owners are unchanged. This is a Root direction note,
with directed NONBLIND paper review by a local UNKNOWN helper, not a new
Task, Claim, Run, owner or branch.

## Fixed inputs and exact domain

Work over F_p with p=6m+1 prime, m>=2, N=3m and q=x(x-3)^2/4. Keep the
original C, tau, F_CM, beta components, literal g, rho leading16, complete
2m<r<=N tail, and class-19 +t0 epsilon_N term. The source map is

    (MF)_n=-[x^(N+n)]q'(x)F(q(x)), 1<=n<N.

We enlarge the FORMAL polynomial degree bound from degree<N to degree<=p-2.
There is no identification modulo z^p-z, source projection, or change to the
original fixed degree<N construction. One original boundary condition,
B_N=0, can be retained in the enlarged construction.

Dependencies are the full Source proofs at:
- 2afa093dfd43de5d86b63b3b940b40034ea3b0e3: cubic source annihilators;
- d0274b66f3b4622519cd2dda659ce13415baff51: old-image completeness and fixed right inverse;
- 4176498bac854ace8fbfd8d1bb397294921524d3: actual half-source obstruction.

The local directed reviews separately pin their complete input files. No
mathematical script, old p13 sample, prime census, Green solve or experimental
producer/checker was run for this direction.

## Coefficient obstruction extends to arbitrary formal degree

For 1<=s<=m-1 define

    Gamma_s(y)=sum_(k=0)^(2s) binom(2s,k)(-3)^(2s-k)y_(N-s-k).

For every finite formal F=sum_j f_j z^j, the first directed review proves

    Gamma_s(MF)=-9*4^(s-1) f_(p-s-1).

It proves the formula directly from the coefficient window and a binomial
identity dividing only by a nonzero ell<p. Terms of degree>=p-1 are outside
every strict-source coefficient window. No functional-polynomial reduction
is used.

For m>=3, Lambda=Gamma_2-4Gamma_1 therefore gives

    Lambda(MF)=36(f_(p-2)-f_(p-3)).

The already proved actual half source v=-beta^h-t has
Lambda(v)=19816/3465!=0. Consequently any formal source lift MF=v requires
degree F>=p-3. This strengthens the old degree<N exclusion to degree<=p-4;
it does not assert sufficiency at degree p-3. Lambda is not applied at m=2.

## Preset completion of the strict-source image

The old image I=M(P_degree<N) equals the joint kernel of all Gamma_s and
has rank 2m. Fix H_s=z^(p-s-1). Their Gamma matrix is diagonal:

    Gamma_t(MH_s)=-9*4^(t-1) delta_(t,s).

For any independently specified strict source y choose

    c_s=-Gamma_s(y)/(9*4^(s-1)),
    y_0=y-sum_s c_s MH_s,
    F=R_old(y_0)+sum_s c_s H_s.

Then MF=y and degree F<=p-2. R_old is the already preset old-image right
inverse. The fixed basis and linear response use the prescribed source;
they are not selected to fit a desired endpoint.

## Gauss resonances: one compatibility and its source-preserving repair

For the unchanged operator D*=z(1-z)d^2+(3/2-5z/2)d-5/9 write

    F_j=A_j B_(j+1)-D_j B_j,
    A_j=(j+1)(j+3/2), D_j=(j+2/3)(j+5/6).

In 0<=j<=p-2, D_j vanishes exactly at 4m and 5m; A_j vanishes at
N-1=3m-1. Set B_(p-1)=0. Descending above 5m determines B_(5m+1).
The genuine top compatibility is F_(5m)=A_(5m)B_(5m+1). After that
B_(5m) is free. Rows 5m-1 down to 4m+1 transfer it with a nonzero
coefficient to B_(4m+1), so it can satisfy the row at 4m. Thus the
two resonant rows are not independent forcing obstructions.

The fixed polynomial

    K=z^(5m)-R_old(M z^(5m))

has MK=0, K_(5m)=1 and no coefficient above 5m: every Gamma_s(Mz^(5m))
vanishes, and R_old returns degree<N. For any F choose

    lambda=A_(5m) B_(5m+1)-F_(5m), F'=F+lambda K.

The upper block is unchanged, MF'=MF, and the top compatibility holds.
Choose the remaining free B_(5m) to satisfy the row at 4m.

## The original B_N=0 can also be retained

B_(4m) is still free. For every row j=N,...,4m-1, both A_j and D_j are
units: the A zero N-1 lies below this interval and the D zeros 4m,5m
lie above it. Descending these rows makes

    B_N = alpha B_(4m)+eta,
    alpha=product_(j=N)^(4m-1) A_j/D_j != 0.

Choose B_(4m)=-eta/alpha. This sets B_N=0. The next row j=N-1 has
A_(N-1)=0 and D_(N-1)!=0, so it determines the lower coefficient and
does not impose a new condition on B_N. The remaining lower rows descend
using D_j units. All equations remain satisfied and the source is unchanged.

Therefore

    M composed with D* : {B: degree B<=p-2, B_N=0} -> F_p^(N-1)

is surjective. This statement is restricted to the enlarged formal carrier
space. It does not assert an original degree<N carrier for the actual source.

## Paid construction and remaining mathematical work

A conservative implementation may store the full truncated source matrix
and the fixed old-image inverse. Constructing columns via the fixed cubic
recurrence costs O(p^2) field operations; dense old-image factorization is
O(p^3) field operations with O(p) inversions and O(p^2) field-element
storage. Applying the resulting fixed source response costs O(p^2) field
operations, followed by O(p) descending rows, including paid divisions and
the two scalar choices. Input, output, retained joint state, setup and
field/bit arithmetic all remain charged. These are upper bounds for the
explicit auxiliary construction, not a total bit-cost or performance gain.

The next mathematical action is to derive the enlarged carrier's complete
flat-gauge boundary and seed ledger and compare its resulting endpoint with
the independently fixed C/tau/F_CM. Source surjectivity and B_N=0 do not
prove that endpoint equality. The full half-prefix tail, lower-block
transport and class-19 top correction remain explicit dependencies. No
mother-goal completion, Native acceptance or physical/Foundation promotion
follows from this note.

