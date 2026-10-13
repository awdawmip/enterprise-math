# Complete cubic strict central source image and a preset right inverse

Status: NEW BOUNDED PURE-PAPER UNIT. The full source image, kernel and rank
are determined without any new execution, prime check or census. The fixed
CM24 target and all mathematical parents remain OPEN. Root remains Driver;
no Native Task, Claim, Run, branch, accepted Result or decisive review exists
for this auxiliary return.

Researcher EM-DIRECT-18F24A continues the same actual delegated direct-research
session and already Source-verified activity RA-CM24PSG-20261013-BOUND01.
Its locally assigned session key is unchanged, not a server-issued MCP or
platform-attested chat ID. Startup activity verification succeeded against
the current immutable activity record main@2f77c5bc09084c8b1dad6cf7b2503d5ab62dc3ff.
The original Root/Hart owners and Root's six contributor IDs remain intact.
All auxiliary context and review are directed NONBLIND, without mathematical
acceptance or independence promoted merely from different visible markers.

## 1. Exact finite objects and the question now answered

Let p=6m+1 be a prime in the declared classes 13 or 19 modulo 24, m>=2,
N=3m and d=2m. All exponents and indices are actual finite integers. In F_p
put q(x)=x(x-3)^2/4 and define the linear strict central source observer

    M:F_p[z]_(degree<N) -> F_p^(N-1),
    (MF)_n=-[x^(N+n)]q'(x)F(q(x)), 1<=n<N.

The source omits only the separately retained boundary rows 0 and N; this
is a typed restriction, not a declaration that either boundary is zero.
In particular the existing class-19 +t0 epsilonN=-epsilonN/3 is unchanged.

The previous bounded Source result proved the independent annihilators

    Gamma_s(y)=sum_{k=0}^{2s}binom(2s,k)(-3)^(2s-k)y_(N-s-k),
    Gamma_s(MF)=0, s=1,...,m-1.

It proved necessity and only one finite image rank, not completeness. This
unit proves, for every p in the declared family,

    THEOREM:
      rank M=d=2m,
      ker M=F_p[z]_(degree<m),
      image M=intersection_{s=1}^{m-1} ker Gamma_s.                  (1)

There is no prime run behind this assertion. The existing Gamma theorem,
finite flat-gauge identity and Gauss rows are used as exact dependencies;
no old Green identity, first-row mismatch or checker is reproved or executed.
The rank proof below does not need chi3 or the half-geometric 2^N=-1; it uses
the actual p=2N+1 and ordinary finite field Frobenius.

## 2. One fixed minor and its exact normalization

If j<m then deg(q'q^j)=3j+2<=N-1, so its entire strict central column is
zero. Hence rank M<=N-m=d. Select, once and independently of any target,
the d rows n=1,...,d and d high source coefficients f_j for m<=j<N.
We prove this fixed minor invertible.

For F(z)=sum_{j=0}^{N-1} f_j z^j let

    H(z)=sum_{j=0}^{N-1} f_j z^(j+1)/(j+1).

Every divisor j+1 in [1,N] is a unit. Thus H'(q)q'=q'F(q), and

    (MF)_n=-(N+n+1)[x^(N+n+1)]H(q).                                (2)

Reverse only the high primitive coefficients: r=0,...,d-1 indexes
h_(N-r)=f_(N-r-1)/(N-r). The actual Frobenius identity is

    q^N=x^N(x^p-3)/(x-3),
    q^(N-r)=4^r x^(N-r)(x^p-3)/(x-3)^(2r+1).                       (3)

Indeed 4^N=2^(p-1)=1 and (x-3)^p=x^p-3. Expanding at x=0 is legal because
x-3 has a unit constant term. The x^p part in (3) begins at degree
N-r+p>N+d+1, and therefore contributes to none of the selected rows.
The exact coefficient, with no infinite truncation substitution, is

    [x^(N+n+1)]q^(N-r)
       =3^(-n-1)(4/27)^r binom(3r+n+1,2r),
         1<=n<=d, 0<=r<d.                                       (4)

The same formula holds throughout the strict window, but the stated minor
is sufficient. Integer binomial coefficients are reduced modulo p; their
top entry may exceed p. This is not division by its factorial across p.

Put u_n=-3^(n+1)y_n/(N+n+1) and c_r=(4/27)^r h_(N-r). The row divisors
N+n+1<=N+d+1=5m+1<p and every column factor are units. The selected source
minor is consequently equivalent by fixed nonzero diagonal factors to

    P_(i,r)=binom(3r+i+2,2r), 0<=i,r<d.                            (5)

## 3. All-prime invertibility by two prescribed node sets

Replace row i by its i-th forward difference at i=0, using the preceding
rows. This fixed lower triangular row transformation has diagonal 1.
Repeated finite Pascal identities transform (5) to

    A_(i,r)=binom(3r+2,2r-i).

Set C_r=binom(3r+2,2r), D(r)=(r+3)_(d-1), and the following degree d-1
polynomials, with empty products equal to 1:

    Q_i(X)=(2X)_falling(i) (X+3+i)_rising(d-1-i).

The exact falling/rising factorial identity gives

    A_(i,r)=C_r Q_i(r)/D(r).                                     (6)

For i>2r its zero binomial agrees with the zero falling factorial, so there
is no omitted exceptional entry. All C_r are units: 3r+2<=3d-1=p-2, hence
the three factorials defining C_r are below p. All D(r) are units because
their factors range from r+3 through r+d+1<=2d<p.

Now evaluate Q_i at the PRESET half nodes t_k=k/2, 0<=k<d. They are distinct
in F_p. For i>k the falling factorial contains a zero, so Q_i(t_k)=0. Its
diagonal entry is

    Q_k(t_k)=k! (3k/2+3)_(d-1-k).                                 (7)

This is a unit. For k<=d-2, every numerator of a rising factor is of the
form 3k+6+2a, 0<=a<=d-2-k, and lies between 6 and 3d=p-1. For k=d-1 the
rising product is empty. The factorial k! and denominator 2 are units.
Thus the half-node evaluation matrix is triangular with nonzero diagonal;
Q_0,...,Q_(d-1) form a basis of polynomials of degree<d.

Evaluation of this basis at the distinct integer nodes r=0,...,d-1 is also
invertible: both node Vandermonde matrices have nonzero differences. By (6)
and the reversible differences, P is invertible. This proves the fixed minor
has rank d for every declared p, using only positive finite factorial/rising
windows strictly below p. No empirical extrapolation from the previous prime
is involved.

Combining rank>=d with rank<=d proves rank=d. The known low m-dimensional
block in ker M is therefore the full kernel. The independent m-1 Gamma
functionals have common kernel dimension (N-1)-(m-1)=d. The known image
inclusion and equal dimensions prove all of (1).

## 4. Preset triangular source projection and complete residual coordinates

The first d source coordinates are free coordinates on image M. For any
given strict central source y, keep these first d entries and reconstruct
the remaining entries from s=m-1 down to s=1:

    yhat_n=y_n, 1<=n<=d,
    yhat_(N-s)=-9^(-s) sum_{k=1}^{2s}
                 binom(2s,k)(-3)^(2s-k)yhat_(N-s-k).               (8)

The pivot 9^s is a unit; the lower indices have either already been supplied
or already reconstructed. All support lies within the strict interior.
This is a fixed triangular map P_I, depending only on p,m, not on tau,
F_CM, a desired endpoint or any outcome. It has image exactly image M and
is the identity there.

Define e=y-yhat. It has zero first d entries and retains every remaining
source residual. Thus

    y=P_I y+e,
    image M direct_sum E=F_p^(N-1),
    E={e: e_1=...=e_d=0}, dim E=m-1.                              (9)

The m-1 raw tail entries e_(d+1),...,e_(N-1) are a canonical complement
coordinate system. Equivalently the Gamma_s(y) are complete obstruction
coordinates: Gamma restricted to E is triangular in increasing tail order,
with the same nonzero pivots 9^s. Vanishing of all Gamma is now sufficient
as well as necessary. A source with a nonzero coordinate is NOT repaired
by returning only P_I y; its exact residual e must remain in an additional
source channel. Nothing in (8)-(9) deletes the separately typed endpoint
or original full half-prefix tail.

## 5. A fixed right inverse, using only triangular algebra

The right inverse has domain image M, not arbitrary sources with their
obstructions erased. Its output is the unique F with f_j=0 for j<m and
MF=y. The same fixed formula can be applied to arbitrary y but then only
MF=P_I y, together with the retained residual from (9).

For the first d rows compute the normalization u_n in §2 and the preset
forward differences

    v_i=Delta^i u_1
       =sum_{a=0}^i (-1)^(i-a)binom(i,a)u_(a+1), 0<=i<d.

Let ell_r(X)=product_{a=0,a!=r}^{d-1}(X-a)/(r-a) be the fixed integer-node
Lagrange polynomials. Expand them in the basis Q_i:

    ell_r=sum_{i=0}^{d-1} alpha_(r,i)Q_i.

All coefficients alpha are fixed cold data, obtained by the predetermined
triangular half-node interpolation

    alpha_(r,k)=[ell_r(t_k)-sum_{i<k}alpha_(r,i)Q_i(t_k)]/Q_k(t_k),
                 k=0,...,d-1.                                  (10)

Every divided diagonal was proved a unit in (7), and r-a is a unit.
No division by a variable forcing value, desired seed, e_N, internal h
coefficient or derivative of the original carrier is involved.

From (6), v_i=sum_r w_r Q_i(r), where w_r=c_r C_r/D(r). Apply the associated
linear functional to ell_r to recover the weights and high source coefficients:

    w_r=sum_i alpha_(r,i)v_i,
    c_r=D(r)w_r/C_r,
    f_(N-r-1)=(N-r)(27/4)^r c_r, 0<=r<d,
    f_j=0, 0<=j<m.                                              (11)

The Lagrange property proves these formulas solve exactly the fixed minor.
Completeness (1) then proves MF=y for every compatible strict source, rather
than only for the first d entries. Formulas (8),(10),(11) are specified before
input values, not a fit selecting an endpoint or forcing from F_CM.

If a separate Gauss polynomial carrier is required, the existing unit-diagonal
descending D* rows can map F to B with B_N=0. This is a prescribed linear
source response. It still does not identify its endpoint with the fixed CM24
target or remove an incompatible source residual.

## 6. Paid complexity and implementation limits

No implementation or timing run was made for this unit. The following are
honest worst-case costs for direct exact arithmetic, not measured runtimes
or free preparation assumptions. Let b=ceil(log2 p), M(b) be paid modular
multiplication cost and I(b)>0 paid modular inversion cost.

* A direct cold setup computes Q_i(t_k), ell_r(t_k) by products and alpha by
  (10) in O(d^3) field operations. All required inverses can be cached with
  O(d) paid inversions (diagonals, Lagrange denominators, C_r, row scalars and
  fixed constants), and it retains O(d^2) field elements. The bit bound is
  O(d^3 M(b)+d I(b)), with O(d^2 b) stored bits. Add/subtract and serialization
  costs are positive and remain in the chosen exact arithmetic model.
* After that already paid setup, one source projection/residual reconstruction
  (8) and one right-inverse evaluation (11) each cost O(d^2) field operations;
  source normalization is O(d) with the cached inverses. Their bit bound is
  O(d^2 M(b)); output and residual storage are O(N b), in addition to the
  stored cold tables. A subsequent Gauss descending response adds O(N) field
  operations with paid unit inverses or their previously paid cache.

These are bounds, not claims of exact operation counts or Native cost parity.
A cold, uncached or independently charged source must pay the setup. Finite
field operations are not unit bit instructions or API blocks. No fixed
cross-source cache is granted without its own declared cost/scope.

In particular an off-diagonal Q_i(t_k) may be zero. Computing its table by
naively dividing successive Q values would be unjustified; the stated direct
product construction performs no such zero-denominator ratio. Only the
proved nonzero diagonals in (10) are used for triangular divisions.

## 7. New corollary for the previously unresolved central endpoint observer

Use the already frozen finite Gauss adjoint D*, its unit descending diagonal
on degree<N, and the old flat-gauge identity for

    T(B)=Pi_(0..N)[x^(-N)(x-3)B(q)/24].

Its strict source is M(D*B). If T(B)=0, then M(D*B)=0, hence D*B has degree<m
by (1). D* and its descending inverse preserve this lower block, so B has
degree<m. The converse was already the elementary support inclusion. Thus

    ker T=F_p[z]_(degree<m).                                     (12)

This is now a full kernel statement, stronger than the prior unit's deliberately
limited inclusion. It uses no new Green solve or inverses of h coefficients.
Consequently the observer pair

    (T(B), L_m(B)), L_m(B)=sum_{j=0}^{m-1}B_j,

is sufficient for the scoped future evaluation B(1): equal observer pairs
have difference in degree<m with coefficient sum zero, hence equal endpoints.
One extra scalar is necessary on the displayed nontrivial lower-block fibers
of the ambient degree<N family when the available observer is only T. This
necessity does not apply to the singleton already specified by a fixed source.
This does NOT recover the full m-dimensional lower block, different endpoints
or derivative jets. Their extra observers remain necessary as dictated by
the expanded future language.

The fixed B is still the uniquely prescribed source G_N(2z)/9, and its
previous independent lower-block transport remains valid. No scalar is set
from the target. Its 2m<r<=N half-prefix tail is retained by L_m, its upper
block remains intact, and its class-19 normalization retains +t0 epsilonN.

## 8. Scope, provenance and the still-open mathematical target

The ordinary finite-field/source-image question requested in this unit is
answered completely. No mathematical mother is marked done. In particular
the prior exact p=13 counterexample to the harmonic source being in this
finite polynomial image remains merely its original saved evidence; it was
neither rerun nor used as the all-prime proof. Completeness identifies the
precise missing m-1 source channels and gives a valid inverse on the legal
image; it does not make those channels vanish for the actual harmonic source.

All original C, tau, fixed F_CM, beta^1/beta^q/half-beta definitions, literal
g, unscaled rho leading16, finite logs, odd flux, class-dependent boundary
and full half-prefix tail are preserved. The actual next target gap is still
a separately prescribed mechanism for those residual channels and its full
endpoint connection. It may not be resolved by renaming Green(v), choosing
a target-derived seed or treating source image projection as full equality.

Mandatory P000, heartbeat native X6, joint-observer preservation and residual
fidelity remain binding and were already read in this same execution. This
is external finite classical auxiliary algebra with a declared coefficient
readout, not a new native plane or an automatic physical/X6/Working Truth/
Foundation promotion. The residual decomposition explicitly retains every
signed source channel and the endpoint scope; no larger observer-safe quotient
or native propagation claim follows. Static algebra has no compulsory native
time parameter; custody and execution timestamps remain separately typed.

Existing exact coefficient/recurrence/finite-difference and interpolation
coverage is composed; no new general-purpose execution tool, provider or
configuration is introduced. No script, prime check, old test, source-fit or
census was run. The proof is saved for directed nonauthor review and immutable
Source custody. Activity bookkeeping grants no formal Task or review authority.
