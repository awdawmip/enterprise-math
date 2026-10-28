# Complete unequal-gap Parity trace on an unbounded small cone

Author: EM-ANALYSIS-1E507F. Activity: RA-9C879FA5E6538D45DD9AE10F.
Status: AUTHOR_PAPER_CANDIDATE_AWAITING_DISTINCT_REVIEW. Date: 2026-10-28.

This is direct TASK_RESEARCH source work, not execution or takeover of a
registered Task. The registration is immutably observed on branch commit
2a81170fdfe6605608a596446e78e7dabbc27df0; canonical main intake remains pending.
No Result/Driver vote, Working Truth, Foundation change, new tool family or
parent completion is claimed. The author inherited shared control and monthly
source context; this is source-exposed continuation, not blind discovery.

## 1. Exact inherited interface and new gap

The source is EM-PERFECT-9821E2,
`research_notes/owner_goal_20261016/parity_tail_independent_review/PARITY_UNEQUAL_GAPS_UNIFORM_BOUNDED_SECTOR_TAIL_AUTHOR.md`,
fully read at immutable commit 1a553d4d28a105230ecebd5a555dc8adbab8ee28,
Git blob f05b0b5be5c7d78c7faf58ae1f818bc67cea103c. Its mathematical
interface, including its independently reviewed fixed bounded-sector scope,
is preserved. The earlier review is
`research_notes/owner_goal_20261016/reviews/parity_unequal_gaps_7cda51/PARITY_UNEQUAL_GAPS_INDEPENDENT_PAPER_REVIEW.md`
at 56f5938da3f707c1d9db1b39afde124eac4634e3, blob
f255e7e1ab5905c1c82883e8aaaa1443996c77cc, as located by the monthly catalogue;
the author's original UNREVIEWED creation label remains historical provenance.
The present source construction is examined beyond that scope;
the new domain theorem does not inherit the earlier review's vote.

Fix an integer m >= 2 and put n=m-1. For real S>=0 and a,c>0 put

    r0=mS, M=ma, N=m(a+c), r=m(S+a), epsilon=1/r,
    theta_i=(i+1)/m, w_i=(-1)^i binom(n,i), 0<=i<=n,
    eta_(t,i)=n! / product_(j=0)^(m-1)(t+theta_i+j),
    D_t=diag(w_i eta_(t,i)/m).

For 1<=ell<=n define phi_ell(y)=(y)_ell/ell!, where the parentheses are
rising factorials, and define

    G_b[i,ell]=[phi_ell(r0+theta_i+b)-phi_ell(r0+theta_i)]/b,
    A=G_M^T D_r G_M, B=G_N^T D_(r+mc) G_N,
    Gap(S,a,c)=tr(B^(-1)A)-n.

These are the original complete signed normalized secant forms. Their
invertibility and exact trace representation below come from the inherited
source. They need not be positive definite. No parity population, signed
branch, frame term or original normalization is discarded.

The source proves Gap>0 for each fixed bounded sector in a,c beyond an
effective S threshold. It explicitly leaves unbounded-gap uniformity open.
Here a finite polynomial support argument produces a single computable cone
containing unbounded a,c, and hence every pair of positive sublinear gap paths.

This is classical auxiliary matrix/polynomial mathematics. The project's
native substrate remains the signed six-axis Cell torsor in Heartbeat World,
with no native plane and time separately typed when needed. S,a,c are external
static parameters here, not native coordinates or physical time; no native
propagation, dimension reduction or observer quotient is inferred.

## 2. Polynomial construction retained in full

On degree<=n-1 polynomials in z, write D=d/dz and

    Psi_b(D)=sum_(k=0)^(n-1) b^k D^k/(k+1)!,
    U(epsilon;a,c)=Psi_(ma epsilon)(D)
                    Psi_(m(a+c) epsilon)(D)^(-1).

The inverse is a finite nilpotent polynomial: if V=Psi_b-I, then
Psi_b^(-1)=sum_(h=0)^(n-1)(-V)^h. Thus U is polynomial in the two
variables a epsilon and c epsilon, with rational m-dependent coefficients.

The same source defines polynomial/rational matrices

    Q_i(epsilon,v)=product_(j=0)^(m-1)[1+v+epsilon(theta_i+j)],
    Q(epsilon,v)=product_i Q_i(epsilon,v),
    H(epsilon,v)_(p,q)=epsilon^(-n)
       sum_i w_i (1+epsilon theta_i)^(p+q)/Q_i(epsilon,v),
    W(epsilon,v)=Q(epsilon,v) H(epsilon,v), 0<=p,q<=n-1.

Its finite-difference divisibility gives W in Q[epsilon,v] entrywise, with
only nonnegative exponents. The determinant identity is

    det W(epsilon,v)=K(1+v+lambda epsilon)Q(epsilon,v)^(n-1),
    lambda=(m^2+1)/(2m),
    kappa=m^(-n(n-1)/2) product_(j=1)^(n-1) j!,
    K=kappa^2 (product_i w_i)(-1)^n n! m^(1-n) != 0.

Use subscripts A for v=0 and B for v=mc epsilon, and sigma=sign(K).
The exact polynomials from the source are

    Dgap=sigma Q_A det W_B
         =|K| Q_A [1+(mc+lambda)epsilon] Q_B^(n-1),
    Ngap=sigma[Q_B tr(adj(W_B) U^T W_A U)-n Q_A det W_B].

For every S>=0,a,c>0, the inherited identity is Gap=Ngap/Dgap, and
Dgap>=d0:=|K|>0. Polynomial divisibility and the first-variation calculation
give

    Ngap=c Z(epsilon;a,c),
    Z(0;a,c)=0,
    [epsilon]Z=alpha:=|K|m(m^2-1)>0.

For fixed m, write its finite expansion as

    Z=alpha epsilon + sum_(j>=2,p,q>=0) z_(j,p,q) epsilon^j a^p c^q.

No numerical coefficients need to be generated to prove the following
support statement or theorem. All constants below are finite rational
expressions computable from this explicit construction.

## 3. The additional weighted-support lemma

Every nonzero z_(j,p,q) satisfies

    p+q <= j-1.                                                (WS)

Proof. Consider the subring

    R=Q[epsilon, a epsilon, c epsilon] within Q[epsilon,a,c].

Its monomials epsilon^j a^p c^q have p+q<=j, and conversely every such
monomial lies in R. The entries of U lie in R by their explicit construction.
The entries of W_A lie in Q[epsilon]; those of W_B lie in Q[epsilon,c epsilon]
because W is polynomial in epsilon,v before substitution. The same is true
of Q_A,Q_B. Closure under sums and products shows that adjugates, determinants,
trace products and therefore Ngap lie in R. This includes n=1, for which the
adjugate of the 1-by-1 matrix is [1].

Because Ngap is divisible by c as a polynomial, every surviving monomial
epsilon^j a^p c^(q+1) of Ngap obeys p+q+1<=j. Division by c therefore gives
(WS). Cancellations can remove monomials but cannot create forbidden support.
In particular Ngap is divisible by c epsilon, and Z/epsilon is polynomial.
The source's independent first-variation identity fixes its constant term
to alpha. This proves the lemma. QED.

This argument does not infer the support bound from sample coefficients or
from analyticity alone: polynomial W before substituting v=mc epsilon and
the scaled finite transfer U are both load-bearing.

## 4. Effective unbounded cone theorem

Define the nonnegative rational coefficient sum

    Bm=sum_(j>=2,p,q>=0) |z_(j,p,q)|,
    delta_m=1 if Bm=0, otherwise min(1,alpha/(2Bm)).

Then delta_m>0 is computable from m alone. For every S>=0,a,c>0 satisfying

    rho=(1+a+c)/(m(S+a)) <= delta_m,                           (C)

the complete trace obeys the explicit strict lower bound

    Gap(S,a,c) >= c alpha / [2m(S+a) Dgap(1/[m(S+a)];c)] > 0.  (P)

Proof. Put t=max(epsilon,a epsilon,c epsilon); then 0<t<=rho<=delta_m<=1.
By (WS), a remainder monomial after division by epsilon is

    epsilon^(j-1-p-q) (a epsilon)^p (c epsilon)^q.

It is a monomial of total degree j-1>=1 in the three nonnegative quantities
epsilon,a epsilon,c epsilon. Its absolute value is at most t^(j-1)<=t.
Consequently

    |Z/epsilon-alpha| <= Bm t <= Bm delta_m <= alpha/2,

with the Bm=0 case immediate. Multiply by c epsilon/Dgap>0 to obtain (P).
QED.

The condition is a conservative sufficient cone, not an optimal boundary or
evidence of negativity outside it. The constant is not evaluated numerically
in this paper. The theorem is fixed m; no positive uniform delta over all m
is claimed. It does not solve the all-S, arbitrary-positive-gap target.

## 5. Uniform error and unbounded sublinear paths

Expand Dgap in its finite form

    Dgap(epsilon;c)=d0 + sum_(j>=1,0<=q<=j) d_(j,q) epsilon^j c^q,
    Em=sum_(j>=1,q) |d_(j,q)|.

The indicated support follows either from its explicit positive product or
from the same subring argument. For t<=1,

    |Dgap-d0| <= Em t,
    |Z/(epsilon Dgap)-alpha/d0|
       <= Cm t,
    Cm=Bm/d0 + alpha Em/d0^2.                                 (E)

Indeed Dgap>=d0 and the preceding bound on Z/epsilon yield (E) by writing
(Z/epsilon)/Dgap-alpha/d0=(Z/epsilon-alpha)/Dgap
                        +alpha(d0-Dgap)/(d0 Dgap).
Thus, whenever rho<=1,

    |Gap/c - (m^2-1)/(S+a)|
       <= Cm(1+a+c)/[m^2(S+a)^2].                             (A)

In particular, for any positive real functions a(S),c(S) with
a(S)+c(S)=o(S) as S tends to infinity, (C) holds eventually and

    Gap(S,a(S),c(S))/c(S)
        = (m^2-1)/(S+a(S)) * (1+o(1)) > 0 eventually.

No differentiability, monotonicity or positive lower bound for the gap paths
is required. They may grow unbounded, shrink arbitrarily fast or oscillate
while satisfying the stated sublinear condition. This is a pointwise
evaluation/asymptotic statement; it does not assert monotonicity along those
paths and does not differentiate a(S) or c(S).

The cone also includes linear paths a=A S,c=C S with A,C>0 satisfying
(A+C)/(m(1+A))<delta_m, for all sufficiently large S. The strict limiting
inequality is required in this direct corollary; equality alone does not
remove the extra 1/[m(S+a)] in (C).

## 6. Reuse, deduplication, evidence and next unit

The toolbox coverage lookup and the monthly Student/Parity catalogue were
read before developing this argument. Resolution: COMPOSE_APPLIED. We reuse
the exact original Gram/adjugate construction and elementary polynomial
coefficient majorants; no generic mechanism, helper calculus or T family is
invented. The additional content is (WS) and its unbounded cone consequence.
The inspected predecessor explicitly restricts its theorem to bounded sectors;
its two source files and the monthly catalogue do not contain this cone
statement. This is a scoped internal dedup check, not an exhaustive external
novelty assertion. Other ongoing chats' live ownership is UNKNOWN because the
canonical inventory request was refused by the server quota; no claim is
made and no formal Task state is changed.

No scientific computation, m7 certificate, P11 core98/fixed233 run, matrix
enumeration, archived checker rerun or numerical parameter scan was executed.
The proof is symbolic paper mathematics. A distinct reviewer should verify
the subring membership of W/U, division-by-c support shift, n=1 case,
denominator positivity and the unbounded-path quantifiers.

Remaining frontiers: effective numerical size of delta_m; more permissive
linear cones from the full scaled limiting matrix; all-S arbitrary-gap
positivity; m-uniform control; and separate coefficient-sign claims. The
present result leaves all of these open. The next fair portfolio unit should
serve T6/formal or P11 rather than immediately extending this source line.
