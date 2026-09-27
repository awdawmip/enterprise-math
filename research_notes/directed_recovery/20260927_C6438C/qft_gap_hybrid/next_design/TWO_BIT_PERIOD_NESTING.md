# Two signed bits: period nesting, a closed aligned route, and the mixed-moment gap

Status: SYMBOLIC_AUTHOR_RESULT / SHARED_CONTEXT / NOT_EXECUTED / NOT_ADMITTED.
No scientific computation, host numerical test, new literature query or remote
write belongs to this note. The following finite-sum proofs are self-contained;
they are not literature-first novelty claims.

## 1. Exact scalar contract and sources

Let integers satisfy g>=2 and 0<=ell<k<g. Put

    L=2^g, V=2^ell, p=2V, U=2^k, P=2U, H=L/P, mu=U/p.

In particular p divides U; mu is a positive integer even when the two selected
bits are adjacent. For 0<=x<L define

    w(x)=(-1)^(bit_ell(x)+bit_k(x)),
    A_two(d)=sum_(0<=x<L-d) w(x)w(x+d),       0<=d<L,
    K_two(g,ell,k,R,r)=sum_(0<=x,y<L; y-x=r mod R) w(x)w(y),

where R>=1 and 0<=r<R. Physical stride is one. R is supplied counting data;
acquiring an actual modular order and a target address is a separate paid
obligation. Nothing here changes an external matrix weight, reorders native
words, projects a residual coordinate, or supplies a full Gram simulator.
When used under the existing scalar-gap contraction contract the raw scaling
is still 4^(-g), not the scaling of any compressed interval introduced below.

The single-bit point and progression identities are those of
`../sep27-qft-gap-direct/DIFFERENCE_AUTOCORRELATION.md`, SHA-256
`c0c3765fce7d07f383f1ebfcb514dd8483485944bfeb202d024dd21e69205cbf`.
Its separately executed observer is
`direct_gap/direct_signed_gap.py`, SHA-256
`3ab2515c1b9df35d01c9605f21d8f8fe56bd044effe489063192c0a5c56a8521`.
The frozen scalar moment implementation is
`../sep27-qft-adaptive/nonzero_structure/typed_floor_moments.py`, SHA-256
`633502c9b484e60e5dc5fcf6edd0420f12d52c33c43e88851b9e1e6465ea94a2`.
These pins locate the existing arithmetic capability; this note does not claim
that a new two-bit adapter has been implemented or executed.

## 2. Proof of the proposed nesting identity

Write v(x)=(-1)^bit_ell(x), and for fixed d put

    c_d(x)=v(x)v(x+d),     B_d(n)=sum_(0<=x<n) c_d(x), n>=0.

The function c_d is p-periodic. In fact it is already V-periodic because both
factors change sign under x->x+V. Thus it is U-periodic. Decompose
d=qP+s with 0<=s<P. The high-bit sign product depends on s and has period P;
the complete two-bit product has period P as well.

For 0<=s<=U, the high-bit product on the successive half-open intervals

    [0,U-s), [U-s,U), [U,P-s), [P-s,P)

has signs +,-,+,-. U-periodicity of c_d therefore gives its weighted full-period
sum and prefix of length P-s as

    F=4 B_d(U-s)-2 B_d(U),
    T=3 B_d(U-s)-B_d(U).                                  (1)

For U<=s<P, set e=s-U. The successive intervals

    [0,U-e), [U-e,U), [U,P-e), [P-e,P)

have signs -,+,-,+. Therefore

    F=2 B_d(U)-4 B_d(U-e),
    T=-B_d(U-e).                                           (2)

Here the tail length is P-s=U-e, so it includes only the first negative
interval. The overlap length L-d is exactly

    (H-q-1)P+(P-s).

Since d<L, H-q-1>=0, and hence the requested formula is correct:

    A_two(d)=(H-q-1) F+T.                                 (3)

At s=0, T=F and the expression means H-q complete periods; no empty tail is
mistakenly added. At s=U, both descriptions give F=-2B_d(U), T=-B_d(U).
Zero-length subintervals contribute zero. This verifies all shared boundaries.

There is also a constant-size expression for B_d(n), requiring no scan of
either period. Let z=d mod p, eta=floor(z/V) in {0,1}, a=z-eta V, and
n=hV+t with 0<=t<V. For x reduced modulo V,

    c_d(x)=(-1)^eta [1-2*1_(x>=V-a)].

Consequently

    B_d(n)=(-1)^eta [h(V-2a)+t-2 max(0,t-(V-a))].           (4)

The a=0 boundary has an empty negative interval and obeys the same formula.
All of (1)-(4) are signed integer identities, not probabilities or approximate
rotations. Ordinary host evaluation is not substituted for typed arithmetic.

## 3. A second proof through block stretching

This identity gives a useful route that avoids new mixed moments on an explicit
input family. Let M=L/V=2^(g-ell) and hbit=k-ell>=1. Write x=Vn+u with
0<=u<V. The two selected bits depend only on n, so

    w(Vn+u)=f(n),    f(n)=(-1)^(bit_0(n)+bit_hbit(n)), 0<=n<M.

Let A_one(z) be the existing single-bit autocorrelation of
(-1)^bit_hbit(n) on the interval 0<=n<M, defined for 0<=z<M.
For use in this section only, explicitly extend it by A_one(M)=0.
This is the empty finite sum; it is not a legal nonempty argument to the old
point/progression formula. A_one beyond M is never needed.

For 0<=d<L write d=Vz+t with 0<=t<V. If u<V-t, the second block index is
n+z, and there are V-t choices of u. If u>=V-t, it is n+z+1, with t choices.
The length constraints on n are respectively n<M-z and n<M-z-1. Since the
LSB product f(n)f(n+j) contributes the constant factor (-1)^j,

    A_two(d)=(-1)^z [(V-t) A_one(z)-t A_one(z+1)].          (5)

This proof counts every starting position once. At t=0 the carry branch has
coefficient zero. At z=M-1 its shifted contribution uses exactly the empty
A_one(M)=0. The unshifted contribution remains in its valid domain. There is
no normalization change: (5) is a raw integer autocorrelation.

Equation (5) extends the ell=0 LSB identity: V=1 forces t=0 and reduces to
A_two(d)=(-1)^d A_one(d). It holds for every ell, not only ell=0, but the
progression evaluation below needs an additional divisibility premise.

## 4. A proved closure when V divides R

For a nonnegative head b, the canonical displacement progression is

    d_j=b+jR, 0<=j<n,
    n=0 if b>=L; otherwise n=1+floor((L-1-b)/R).            (6)

Assume V|R. In a nonempty progression write b=Vz0+t, 0<=t<V, and h=R/V.
Then d_j=V(z0+jh)+t, so t is constant and z_j=z0+jh. Moreover

    d_j<L  iff  z_j<M.

If h is even, (-1)^z_j is constant throughout the progression. If h is odd,
split j into its even and odd subsequences. These have heads z0 and z0+h,
step 2h, and counts ceil(n/2) and floor(n/2). Their signs are constant and
opposite. Each count equals the canonical length of its new head/step inside
[0,M); the split omits empty branches. No enumeration of V or P/p is used.

For any surviving constant-sign subsequence with head c and step a, equation
(5) requires two ordinary unsigned single-bit sums:

    sum A_one(c+ja),       c+ja<M,
    sum A_one(c+1+ja),     c+1+ja<M.                       (7)

The second range is the first range with a possible final z=M-1 term removed.
Indeed for the same j, z+1<=M; equality holds only for a last z=M-1 term.
Dropping that term is exactly the explicit zero extension in section 3.
Thus the second sum is the canonical progression of head c+1 and step a in
[0,M), with its own length. It may be empty even when the first is nonempty.
The old routine must receive that truncated length, not a nonempty request
with displacement M. The sign multiplying the shifted sum remains the sign
of z=c+ja, namely (-1)^c, with the minus sign already present in (5).

The two oriented heads for the modular query remain b=r and b=R-r:

    K_two=Sum_two(head r,step R)+Sum_two(head R-r,step R).   (8)

The second head excludes displacement zero at r=0. At an even half-modulus,
both coincident heads are retained because they represent opposite displacement
orientations. Heads outside [0,L) are zero before any compression.

Therefore the complete query needs at most eight old single-bit progression
sums: two orientations, at most two parity subsequences, and two sums in (7).
Each old progression uses at most two degree-three moment tables, so the
upper bound is **sixteen top-level moment tables**, not eight. Empty branches
and zero coefficients may reduce this count only when their omission is
recorded. Recursive nodes, cache requests, typed digit work and receipts are
additional paid resources. This is a constant number of existing poly-bit
scalar computations in g+log(R+1), after the counting parameters are supplied.

The executed single-bit observer already contains a private `_progression`
method and the underlying moment arithmetic needed for (7). A separately
versioned adapter would have to expose the compressed length/bit/step, typed
parity and coefficient operations, both orientations and the empty truncation
in its certificate. The old public `one_negative` API computes a complete
two-orientation modular sum and must not be mistaken for one progression.
No such two-bit adapter or execution is claimed here.

For V not dividing R, t_j=(b+jR) mod V varies. Splitting into
V/gcd(V,R) constant-remainder subsequences would restore this route, but that
number can be 2^ell for odd R. This is not a uniform polynomial-in-ell method
and is not proposed as a hidden loop. One may use it only with an explicit
small, paid split bound. The ell=0 case has V=1 and needs no extra premise.

## 5. Exact missing moment contract for arbitrary R

The general nesting formula also identifies a finite-dimensional sufficient
interface without falsely claiming that the present scalar evaluator supplies
it. For one progression d=b+jR, define

    q=floor(d/P),       q_plus=floor((d+U)/P), delta=q_plus-q in {0,1},
    Q=floor(d/p),       Q_plus=floor((d+V)/p), eta=Q_plus-Q in {0,1},
    z=d-pQ,
    C(z)=p-4z                    if 0<=z<=V,
         4z-3p                   if V<=z<p,
    T(z)=p-3z                    if 0<=z<=V,
         z-p                     if V<=z<p,
    E(z)=T(z)-C(z).

C is the lower-bit full-p correlation and T its prefix of length p-z.
At z=0, T=C=p; at z=V either branch agrees. Define

    B=(mu-Q+2mu q) C+E,
    f=(4H-1)-4q+delta*(4-8H+8q).

Then (1)-(3) simplify to

    A_two(d)=f B-mu*(2H-2q-1) C.                         (9)

To verify this simplification, when delta=0 the term B is exactly B_d(U-s).
When delta=1, B_d(U-(s-U))=B+mu C, while B_d(U)=mu C in both cases.
Substitution into (1) and (2) leaves the same second term of (9). This also
checks the high-half boundary without assuming either tail is positive.

A compact task-specific missing interface returns these fourteen exact sums
over the declared progression:

    C_(a,e)=sum q^a delta^e C(z),      a=0,1,2; e=0,1,
    D_(a,e)=sum q^a delta^e Q C(z),    a=0,1;   e=0,1,
    E_(a,e)=sum q^a delta^e E(z),      a=0,1;   e=0,1.      (10)

The complete answer for that orientation is the following fixed combination:

    2mu H C00 + mu(8H-4) C10 - 8mu C20
      +(1-4H) D00 + 4 D10
      +mu(4-8H) C01 + 16mu(1-H) C11 + 16mu C21
      +(8H-4) D01 - 8 D11
      +(4H-1) E00 - 4 E10 +(4-8H) E01 + 8 E11.           (11)

Here the second index is the indicator exponent, so e=0 includes all terms.
This is the exact finite list sufficient for this derivation; it is not a
claim that fourteen is a minimal linearly independent basis among all possible
algorithms. At present some terms require correlations of two nested floors,
and those terms are the missing capability, not a new propagator.

For a more uniform mathematical API, (10) reduces to a subset of mixed moments

    G_(u,alpha,beta)^(epsilon,zeta)
      =sum_(j=0)^(n-1) j^u
          floor((Rj+b+epsilon U)/P)^alpha
          floor((Rj+b+zeta V)/p)^beta,                   (12)

where epsilon,zeta are 0 or 1, u is 0 or 1, alpha,beta<=3 and
u+alpha+beta<=5. Both moduli are powers of two and p|P; the underlying affine
argument and range are shared. Pure single-floor terms are already covered
where their degree is at most three. The cross terms in (12) are not arguments
accepted by the frozen single-floor degree-three API.

The degree-five bound follows constructively. With Delta_Q^t=Q_plus^t-Q^t,

    C=p-4d+4pQ+8d*(Q_plus-Q)-4p*Delta_Q^2,
    E=d-pQ-4d*(Q_plus-Q)+2p*Delta_Q^2.                  (13)

These have total degree at most two in d and one lower floor at a time.
For Q*C, remove Q*eta and Q^2*eta using

    Q*eta=(Delta_Q^2-Delta_Q^1)/2,
    Q^2*eta=(2Delta_Q^3-3Delta_Q^2+Delta_Q^1)/6.

This yields a sum of lower-floor monomials of total degree at most three,
still linear at most in d. For the high floor use the same two identities
with q and delta; q^a delta for a<=2 becomes a linear combination of
q_plus^t-q^t with t<=a+1. Thus C terms have high degree <=3 plus lower degree
<=2; Q*C terms have high degree <=2 plus lower degree <=3; E terms have
high degree <=2 plus lower degree <=2. Substituting d=b+Rj proves (12) with
degree at most five and u<=1. All divisions introduced this way are exact.
No product of two offsets of the *same* floor is left; products of the coarse
and fine floor remain.

This is an algebraic reduction, **not** an implemented or proved poly-bit
mixed-moment evaluator. Separate marginal moment tables do not directly supply
their products. The old Euclidean recursion proves closure for powers of one
floor on one geometry; it does not state a recursion for (12). Neither a
constant-size moment list nor the divisibility p|P by itself is a termination
or complexity proof. This note also does not prove that such a recursion is
impossible, or that no sharper reduction back to the old API exists.

## 6. Exact next mathematical step and limitations

The smallest immediately constructive path is the V|R adapter of section 4:
all scalar formulas already have a proved single-floor reduction. Before any
execution, its proof/certificate design must cover d=0, s=0/U, z=V,
adjacent ell/k, high bit k=g-1, t=0, compressed z=M-1 with zero shifted tail,
both parity branches, an empty orientation, and coincident half-modulus heads.
R and all scale/divisibility/parity values must be observed through the existing
typed integer route. The overall cost may still be higher than specialized
one-bit endpoints; no timing advantage is predicted without measurement.

For arbitrary R, the precise open task is to give a simultaneous recurrence
for the mixed subfamily (12), or an algebraic elimination of just the needed
fourteen values (10), with a proven descending size measure, bounded coefficient
growth, exact signed normalization, and a polynomial number of retained states.
It must not enumerate P/p, V/gcd(V,R), R residues, or the original overlap
interval while advertising a poly-bit bound. The one-floor Euclidean proof is
a useful template, not completion of that task.

The present note proves general pointwise identities and the V|R progression
closure, and isolates the remaining generic progression interface. It does not
claim a generic two-bit poly-bit evaluator has been built, does not handle an
arbitrary Walsh mask, and does not remove order/address or full matrix query
growth from a QFT/Shor simulation. Full external residual and normalization
contracts remain intact.

Global-Knowledge-Sync: main@f8aa9c8 / GLOBAL_KNOWLEDGE_V1
