# T6 lower-prime completion: discrete annihilators and 21 sharp coupled cuts

Author: EM-ANALYSIS-1E507F; RA-9C879FA5E6538D45DD9AE10F.
Status: AUTHOR_PAPER_CANDIDATE_AWAITING_DISTINCT_REVIEW. 2026-10-28.

This direct research unit extends a necessary-condition interface; it does
not claim a registered Task, rerun an accepted finite census, classify a new
vertical order, or change any Result/Driver/Working Truth/Foundation status.
The current canonical queue is UNKNOWN after the server's quota refusal.
Native Heartbeat World remains a signed six-axis Cell torsor with no native
plane; the reciprocal-moment problem here is explicitly external integer
arithmetic. Algebraic signed coefficients are not positive native branch mass.

## 1. Exact input and the missing coupled interface

The source is
`driver_reviews/mcp/MCP-cd5eefdde49843898b2a70c1af94d8dd/7592bca554f5d835bc7c/T6_P17_ORDER1_SMALL_BRANCH_THEOREM.md`,
fully read at 1a553d4d28a105230ecebd5a555dc8adbab8ee28, blob
4f0b8eb495b4725009d3f06d845859bda1c85cbb. Section 4 supplies the exact
lower-prime/H0 completion formulation and only individual-moment cheap cuts.
Its old statement that q1 classification is open is historical: subsequent
accepted q1 results are preserved. This unit does not reopen q1.

Abstract the source interface: given rational M_0,...,M_6 and nonnegative
integer residual budgets B_+,B_-, seek finitely supported integers t_a on

    A={a integer >=2: all prime factors of a are <=13},

with

    sum_a t_a a^(-j)=-M_j, j=0,...,6,
    sum_a(a-1)max(t_a,0)<=B_+,
    sum_a(a-1)max(-t_a,0)<=B_-.

The budget itself makes the effective support finite. This includes every
admissible composite denominator, not just primes. It is exactly the source's
17-free, maximal-prime-at-most-17 completion dictionary. These conditions are
the theorem's inputs; whether a later local p17 survivor produces such M and
budgets is a separate caller obligation.

The source's coordinate cuts are

    -B_+<=M_0<=B_-,
    -B_+/2^j<=M_j<=B_-/2^j, 1<=j<=6.

They do not exploit the simultaneous dependence of all moments on the same
integer denominator. The following cuts retain that joint relation.

## 2. Discrete annihilators

For integers h>=1,k>=0,h+k<=6 set

    f_(h,k)(x)=x^k product_(b=2)^(h+1)(1-bx)
              =sum_(j=0)^6 q_(h,k,j) x^j,
    L_(h,k)(M)=sum_j q_(h,k,j) M_j,
    R_(h,k)(a)=f_(h,k)(1/a)/(a-1)
             =product_(b=2)^(h+1)(a-b) / [a^(h+k)(a-1)].

For every integer a>=2, f_(h,k)(1/a)>=0. In fact it vanishes at each
integer a=2,...,h+1, and every factor is positive for a>=h+2. Positivity
is discrete: the claim is not that the polynomial is nonnegative for all
real x between 0 and 1/2. That false continuum replacement would lose the
precise denominator population used here.

Define the sharp unit-cost cap

    C_(h,k)=max_(a in A) R_(h,k)(a).

This is positive and rational; the next section reduces it to a finite
explicit maximum. Every feasible completion must satisfy the coupled cut

    -C_(h,k) B_+ <= L_(h,k)(M) <= C_(h,k) B_-.                (CUT)

Proof. For positive and negative t_a separately, 0<=f(1/a)<=C(a-1).
Therefore -C B_-<=sum_a t_a f(1/a)<=C B_+. The moment equations make
the middle expression equal to -L(M). Negate the inequalities. QED.

The coefficient C is sharp as a unit-cost bound on this dictionary. If a_*
maximizes R, an arbitrary positive integer multiplicity at a_* realizes
equality in the corresponding one-sided cut with budget a multiple of
a_*-1. This does not assert sharpness for each supplied pair of small budgets
or for the smaller set of moments realizable by a specific p17 prefix.

## 3. A proved finite cutoff, not a truncated search assumption

For real x>h+1, R_(h,k)(x)>0 and

    d/dx log R_(h,k)(x)
       = sum_(b=2)^(h+1) 1/(x-b) - (h+k)/x - 1/(x-1)
       < h/(x-h-1) - (h+k+1)/x.

Thus R is strictly decreasing for

    x >= A_(h,k):=ceil((h+k+1)(h+1)/(k+1)).                  (END)

Indeed the last upper bound is nonpositive there, since its numerator after
positive denominators are cleared is
(h+k+1)(h+1)-(k+1)x. The strict inequality comes from 1/(x-1)>1/x.
The endpoint A is always at least h+2.

For the present finite family h+k<=6, the endpoint belongs to

    {3,4,5,6,7,8,9,10,12,15,16,21,25,36,49}.

Every member is 13-smooth and hence lies in A. Consequently any admissible
integer a>A has R(a)<R(A), with A itself among the allowed candidates. It
follows rigorously that

    C_(h,k)=max_{2<=a<=A_(h,k), a 13-smooth} R_(h,k)(a).

Endpoint admissibility matters: for a different dictionary one cannot merely
truncate a decreasing tail at a forbidden endpoint. One must include an
admissible point at or beyond the monotonicity threshold, or prove another
dominating allowed endpoint. The exact script checks this obligation for
every row before reporting its maximum.

## 4. Exact constants and strict strengthening

The accompanying pure-Python program evaluates only these scalar rational
functions at at most 49 integers per row using fractions.Fraction. It records
all admissible and excluded values, integer polynomial coefficients, endpoint
membership and maxima. There is no affine representative, lattice search,
integer completion enumeration or old scientific certificate rerun.

| h | k | C_(h,k) | admissible maximizers |
|---:|---:|---:|---|
|1|0|1/6|3,4|
|1|1|1/18|3|
|1|2|1/54|3|
|1|3|1/162|3|
|1|4|1/486|3|
|1|5|1/1458|3|
|2|0|10/147|7|
|2|1|3/250|5|
|2|2|1/384|4|
|2|3|1/1536|4|
|2|4|1/6144|4|
|3|0|5/132|12|
|3|1|15/3584|8|
|3|2|1/1620|6|
|3|3|1/9720|6|
|4|0|910/37179|18|
|4|1|1512/805255|11|
|4|2|35/177147|9|
|5|0|7315/423936|24|
|5|1|1485/1529437|14|
|6|0|26719875/2080374784|32|

The composite background changes the answer and is retained. For example,
the h=4,k=0 unrestricted integer maximizer is a=17, excluded from the
completion dictionary; its admissible maximizer is the composite a=18.
For h=6,k=0, the unrestricted maximizer is 31 and the admissible maximizer
is 32. Replacing the dictionary by its primes would yield an incorrect cap
for several rows.

The first two explicit cuts are

    -B_+/6 <= M_0-2M_1 <= B_-/6,
    -B_+/18 <= M_1-2M_2 <= B_-/18.

The second is not implied by the coordinate cuts. For example B_+=B_-=2,
M_0=0,M_1=1,M_2=-1/2,M_3=...=M_6=0 satisfies every coordinate cut and
has no 17-adic denominator pole. But M_1-2M_2=2>1/9, so it cannot be
completed. This is an exact separation witness for two moment relaxations,
not a claim that a real p17 affine branch produces that M vector.

## 5. Budget-specific refinement and application boundary

For an integer B>=0 put

    C_(h,k)(B)=max({R_(h,k)(a): a in A, a-1<=B} union {0}).

It is computed by considering only
2<=a<=min(A_(h,k),B+1). If B+1<A this is the full feasible atom set;
if B+1>=A the included admissible endpoint dominates the entire tail.
Then the sharper necessary cut is

    -B_+ C_(h,k)(B_+) <= L_(h,k)(M)
                            <= B_- C_(h,k)(B_-).               (BCUT)

This follows from the same proof applied separately to the two budget-bound
supports. Empty support gives zero. Small budgets can force C(B)=0 because
all affordable atoms are annihilated. Integer feasibility still imposes
additional constraints: these 21 inequalities are necessary, not sufficient.

Correct consuming status is `LOCAL_FEASIBLE /
FULL_COMPLETION_EXCLUDED_BY_DISCRETE_ANNIHILATOR_CUT` when a candidate
violates a cut. Do not relabel an affine class EMPTY merely because its full
completion is excluded. No actual unresolved p17 class was filtered in this
unit, and no higher-order population or global T6 assertion follows.

## 6. Reuse, audit and preserved frontier

Tool coverage was checked before constructing the extension. Resolution:
EXTEND_EXISTING_TOOL at the existing lower-prime/H0 completion domain
interface, using standard polynomial dual budget inequalities. T6 here is
the shape-moment problem name, not a claim of a new global tool family.
The exact source's seven coordinate cuts are retained; the new information
is integer-supported annihilation and coupled moments with proved global
caps. The source and monthly T6 catalogue did not contain these 21 cuts;
no exhaustive external novelty assertion is made.

The proof reduces an infinite dictionary maximum to finite rational
arithmetic before running the coefficient script. The generated JSON is
finite computational evidence for the table and also exposes each candidate
to an independent checker. A reviewer should check the sign of the residual
moment convention, discrete positivity, endpoint admissibility, strict tail
monotonicity, composite maxima, exact table arithmetic and BCUT's domain.

Remaining work: apply the cuts to genuinely authorized later-order local
survivors if any; compare hit rates only after those exact inputs exist;
and retain the full integer completion problem after every passing cut.
Existing q1-q4 finite classifications, source limitations, ownership and
global parent status are unchanged.
