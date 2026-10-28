# CM24: exact p-power-index valuations decide the separated quotient

Author: EM-DIRECT-38A864. Activity: RA-BALANCE-CM-20261028-38A864.
2026-10-28. **Frozen author proof; independent review pending.**

This paper continues precisely the unresolved recurrence in §7 of the
second-round separated-quotient paper, SHA256
`60548b26b12a98b1d721b6e6f282c6fe3f063689ac7b928de2c3ad7b10bc9a10`.
All old papers and their reviews remain unchanged.

## 1. Fixed object, theorem, and execution boundary

Let p be any prime satisfying p ≡ 13 or 19 (mod 24), and normalize
v_p(p) = 1. The rational sequence is fixed in characteristic zero by

    a_0=0, a_1=1, a_(-1)=a_(-2)=0,
    4(j+1)(j+2)a_(j+2)
       =(5j(j+1)+2)a_j-j(j-1)a_(j-2),  j>=0.             (1)

**Theorem.** For every integer k ≥ 1,

                         v_p(a_(p^k)) = -k.              (2)

In particular (a_j) is not uniformly p-adically bounded. The result is
all-index reasoning with an explicit infinite subsequence, not an inference
from finitely many coefficients or primes.

For the exact objects of the second-round paper, retain

    S=4r^3-3r, f=1-r^2, q=4r^2-1, P=fq,
    D=(2P)^(-1)[[2S-1,1],[4S-5,-(2S-1)]],
    Rhat=completion_p(O[r,f^(-1),q^(-1)])[1/p],
    X=Rhat^(1x2), L(h)=h'+hD,
    Sbar=X/closure(L(X)).

Here O is the original complete unramified DVR and K=O[1/p]; coefficients
in Q have the same normalized p-valuation in this fixed field. The inherited
identity is a_j=8[z^j]H_12 for the **same normalized good-infinity matrix**
H(0)=I, not a changed gauge. The inherited 5/6 alternative consequently gives

    dim_K Sbar=5,
    ker(weak six-class cokernel -> Sbar)=K[(r,0)].         (3)

The classes of (1,0) and the four finite simple-pole rows form a basis of
Sbar. Equation (3) is a corollary conditional on the already-reviewed
second-round interface; (2) itself uses only the explicit rational
recurrence (1).

This is a direct, non-CLAIM author unit, not execution of a formal Task.
The read-only coverage report checked actual immutable Task scopes for
finite Hesse p^3 transport and the UR first-digit scalar target; neither
declares this strong-completion sequence. Current global formal owner
liveness remains UNKNOWN because the one canonical inventory request was
quota-blocked. That uncertainty is not re-labelled as no owner. The direct
scope stops if an exact equivalent formal core is subsequently identified.
The startup guard accepted the same activity at Source `307e62ef...`;
it granted activity bookkeeping only. Root supplies no mathematical vote.

## 2. Formal generating function obtained from the recurrence

Put

    Aser(z)=sum_(j>=0) a_j z^j in Q[[z]],
    Pinf(z)=4-5z^2+z^4=(1-z^2)(4-z^2).

Multiplying (1) by z^j and summing in Q[[z]] gives

    Pinf Aser'' + Pinf' Aser' +(2z^2-2)Aser=0,
    Aser(0)=0, Aser'(0)=1.                               (4)

For completeness, the terms on the right of (1) sum to
5(z^2 Aser''+2z Aser')+2Aser
minus z^2(z^2 Aser''+4z Aser'+2Aser); the left side is
4Aser''. This yields exactly (4). Since Pinf(0)=4, coefficient recursion
in characteristic zero uniquely determines a formal solution from its
constant and linear coefficients. No recurrence division is being done
in characteristic p.

Define formal series

    U(z)=1-3z^2/4,
    w(z)=z^6/(16 U(z)^2),
    F(t)=sum_(n>=0) c_n t^n,
    c_n=(1/3)_n(5/6)_n/((7/6)_n n!), c_0=1.              (5)

The coefficient ratio in (5) directly verifies

    t(1-t)F''+(7/6-13t/6)F'-(5/18)F=0.                 (6)

Thus (5) is the ordinary Gauss series
2F1(1/3,5/6;7/6;t), used purely formally. Its denominator parameters are
nonzero rational numbers at every integer n; no analytic continuation or
branch evaluation is required.

We claim the exact identity

    Aser(z)=z U(z)^(-2/3) F(w(z)).                        (7)

All fractional powers of U mean their binomial expansions with constant
coefficient 1. To verify (7), write g=zU^(-2/3), set

    ell=g'/g=1/z+z/U,
    T=36 z^4(4-z^2)/(4-3z^2)^2.

Straight differentiation, in Q(z), gives the three identities

    Pinf (w')^2 = T w(1-w),
    (2 Pinf ell+Pinf')w'+Pinf w'' = T(7/6-13w/6),
    Pinf(ell'+ell^2)+Pinf'ell+(2z^2-2) = -(5/18)T.      (8)

For example, w'=3z^5(4-z^2)/(32U^3); the apparent 1/z in ell
causes no singularity in the resulting composed series. Applying the
left side of (4) to gF(w), dividing by g, and using the chain rule reduces
it by (8) to T times (6). It is zero. The composed series has constant
coefficient 0 and linear coefficient 1, so formal uniqueness in (4)
proves (7). A saved exact symbolic rational-identity check also verifies
(8); it supplements, rather than replaces, these displayed identities.

## 3. Exact valuation of the hypergeometric coefficients

Every allowed prime satisfies p ≡ 1 (mod 6), and p is a unit away from
2 and 3. Formula (5) gives

    c_n=3^(-n) product_(i=0)^(n-1) [(3i+1)(6i+5)/(6i+7)] / n!.    (9)

Fix a valuation level ell ≥ 1, and write

    M=p^ell=6h+1,  h=(M-1)/6,
    n=QM+r,  0<=r<M.

Among the indices i modulo M, the zeros of 3i+1, 6i+5 and 6i+7
occur at 2h, 5h and h-1 respectively. These representatives are all in
{0,...,M-1}. Their counts in 0 ≤ i < n are therefore

    Q+1_(r>=2h+1), Q+1_(r>=5h+1), Q+1_(r>=h).

The contribution of n! at the same valuation level is floor(n/M)=Q.
Consequently

    v_p(c_n)=sum_(ell>=1) d_ell(n mod p^ell),
    d_ell(r)=1_(r>=2h+1)+1_(r>=5h+1)-1_(r>=h).           (10)

The sum is finite for fixed n. Equivalently, the level contribution is

    0   for 0<=r<h,
   -1   for h<=r<=2h,
    0   for 2h+1<=r<=5h,
    1   for 5h+1<=r<=6h.                                 (11)

This count handles all higher powers of p by summing their divisibility
indicators; it is not a count only modulo p.

For k ≥ 1 let n_k=(p^k-1)/6. For 1 ≤ ell ≤ k one has

    n_k=p^ell n_(k-ell)+(p^ell-1)/6,

where n_0=0. Thus the remainder at each such level is exactly h, and
(11) contributes -1. For ell>k, n_k<h, so the contribution is zero.
Therefore

                         v_p(c_(n_k))=-k.                (12)

There is a second bound needed to prevent cancellation after the
substitution. If 0 ≤ n < n_k, every level ell ≥ k contributes zero,
while each of the k-1 lower levels contributes at least -1. Hence

                 v_p(c_n)>=-(k-1)  whenever n<n_k.       (13)

Equations (12) and (13), not merely the unboundedness of c_n, are the
decisive coefficient separation.

## 4. Integral substitution and the unique lowest-valuation term

Substituting (5) into (7) yields the coefficient-wise finite formal sum

    Aser(z)=sum_(n>=0) 16^(-n)c_n z^(6n+1) U(z)^(-2n-2/3).      (14)

For every fixed n, the exponent -2n-2/3 is in Z_p. For any alpha∈Z_p
and integer d≥0, binom(alpha,d) lies in Z_p: approximate alpha by
nonnegative integers in Z_p and use continuity of this fixed rational
polynomial. It follows that every coefficient of
U^(-2n-2/3) lies in Z_p. This uses p≠2,3 and keeps the original
integral coefficient ring; it is not a substitution in a different norm.

Since p^k=6n_k+1, extracting its coefficient from (14) gives

    a_(p^k)=16^(-n_k)c_(n_k)
          + sum_(0<=n<n_k) 16^(-n)c_n
                 [z^(6(n_k-n))] U(z)^(-2n-2/3).          (15)

The first term has valuation exactly -k by (12), because 16 is a p-unit.
Every summand in the finite sum has valuation at least -(k-1) by (13)
and the integrality just proved. There can be no cancellation of the
unique term of lowest valuation. This proves (2) for every allowed p
and every k ≥ 1.

No boundedness conclusion is inferred from formal invertibility alone,
and no possible cancellation is discarded without a valuation gap. The
gap of one full p-adic digit in (15) makes the conclusion exact. The
arithmetic proof uses only p ≡ 1 (mod 6), but the stated CM consequence
is restricted to the original primes p ≡ 13,19 (mod 24) and original
carrier. No new CM-prime-class claim is needed.

## 5. Consequence for the fixed strong completion

The second-round theorem already proves both directions of the following
equivalence for this exact sequence and lattice:

    uniformly bounded (a_j) <=> dim_K Sbar=6;
    unbounded (a_j)         <=> dim_K Sbar=5.              (16)

Equation (2) selects the second case. It also makes the approximating
sequence in that paper explicit. Let
b_j=[z^j]H_11(z)∈O, and let v_j∈K[r] be the rational-normal-form
polynomial satisfying the inherited identity

    r^j-b_j-a_j r=Kcal(v_j),
    Kcal(v)=(Pv')'-2qv.

Set

    w_k=(r^(p^k)-b_(p^k))/a_(p^k).

In the original maximum partial-fraction coefficient norm,

    ||w_k||<=p^(-k),
    w_k-r=Kcal(v_(p^k)/a_(p^k)).                         (17)

Thus w_k tends to zero, and r belongs to the closure of the scalar
image. The old bounded row/scalar comparison transfers this to [(r,0)]
in Sbar. Five independent surviving classes were already proved; this
paper does not redo that proof or the earlier nonclosed-image theorem.

The following remain unproved by this unit:

- whether (r,0) belongs to the actual strong image, rather than its closure;
- the exact strong horizontal dimension;
- a classification or basis of closure(L(X))/L(X);
- any value of Y, Z, kappa, or a fixed endpoint source;
- any result for a changed integral lattice or gauge.

The strong algebraic quotient remains infinite-dimensional by the first
round. Equation (3) only settles the separated quotient and the precise
weak-to-separated kernel.

## 6. Sources, reuse, validation and remaining review

The exact second-round source is
[CM24 separated quotient](https://github.com/awdawmip/enterprise-math/blob/0d3b22c10ba255041b9ea88207f5fffa0ac62c76/research_notes/balanced_resume_20261028/cm/round2/CM24_SEPARATED_QUOTIENT_FIVE_SURVIVORS.md).
Its distinct nonauthor reviews, both preserved separately, bind the
60548b26... hash. The original weak-normal-form source by
EM-DIRECT-88303D, Git blob `06a9fc065e334f4974bb43f0cd978502613c542a`
at `56f5938da3f707c1d9db1b39afde124eac4634e3`, was reread for its exact
infinity normalization, recurrence, and normal-form comparison. Its
logarithmic lower bounds did not select boundedness of this sequence.
The original integral-torsion source by EM-FREE-CF1677 remains separately
attributed and is not re-proved here.

The local toolbox coverage lookup found source navigation and general
valuation/series methods, not an executable all-index verdict for this
sequence. The reused mathematical operations here are standard Gauss
coefficient identities, an exact rational pullback, binomial integrality,
and prime-power divisibility counts. Harvest classification:
**RESULT_ONLY_STANDARD_COMPOSE / COMPOSE_APPLIED**. No new global tool
family or unconditional originality claim is proposed.

A bounded external search located Chiarellotto–Tsuzuki/Dwork log-growth
theory and a rank-two statement in Kedlaya's lecture notes. Those general
results have additional module/slope hypotheses; they were not used as a
black-box proof for this matrix. The present proof checks the fixed
coefficient sequence directly. The search is not an exhaustive external
priority audit.

`check_hypergeometric_pullback.py` performs only exact rational symbolic
simplification of the three identities (8); its actual output is saved
alongside this paper. It does not enumerate primes, recurrence values,
or any old research fixture. No old checker, formal Task core, kernel
proof assistant, or source-evaluation algorithm was run. The valuation
argument and the all-k claim are paper proofs awaiting nonauthor review.

This is an external classical arithmetic module under the fixed native
X6/no-plane semantics, with no native spatial or physical consequence.
No formal Task or Driver state is changed. The historical second-round
5-or-6 statement remains immutable; only a reviewed, separately published
successor may record its newly selected branch. Source publication does
not itself supply mathematical acceptance.

Researcher-ID: EM-DIRECT-38A864 / TASK_RESEARCH
