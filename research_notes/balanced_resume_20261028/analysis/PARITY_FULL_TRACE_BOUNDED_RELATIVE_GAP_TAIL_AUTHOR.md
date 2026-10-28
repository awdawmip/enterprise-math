# Full unequal-gap Parity trace: all bounded relative gaps at large total scale

Author: EM-ANALYSIS-1E507F; activity RA-9C879FA5E6538D45DD9AE10F.
Status: NEW_AUTHOR_PAPER_CANDIDATE_AWAITING_DISTINCT_REVIEW. 2026-10-28.

This is a second-round direct research continuation addressing gaps comparable
to the total scale. It is not a formal Task takeover, Result/Driver vote,
Working Truth, Foundation change or new global tool family. The original
all-parameter trace problem remains open. No scientific program, matrix scan,
small-m certificate, m7 stopped branch, P11 core98/fixed233 computation or
symbolic algebra package was executed for this proof.

## 1. Precise theorem and what is new

Fix an integer m>=2 and a positive rational C. There is a computable rational
R_m(C)>=1 such that the ORIGINAL complete normalized signed secant trace obeys

    Gap(S,a,c)=tr(B^(-1)A)-(m-1)
       >= (m-1)/2 * [(1+c/(S+a))^(m+1)-1]
       >= (m^2-1)c/[2(S+a)] >0                              (1)

for all real parameters

    S>=0, a>0, 0<c<=C(S+a), S+a>=R_m(C)/m.                 (2)

There is no upper bound on a, no positive lower bound on a or c, and no
requirement that either gap be sublinear in S. In particular S=0 with large
a and any fixed bounded ratio c/a is included. Every prescribed bounded
range of relative second-gap ratios has its own effective threshold.

The previous bounded-sector tail kept a,c bounded. The first-round small
cone allowed unbounded but sufficiently small scaled gaps. Here the full
limiting signed Gram comparison is positive for EVERY first-gap fraction
lambda in [0,1] and EVERY relative second gap nu>0. This establishes (2) for
any finite C, using a common centered parity decomposition. It is not merely
a better coefficient-majorant constant for the earlier small cone.

The theorem does not give one threshold uniform in m or unbounded C, does
not cover all S+a, and does not establish coefficientwise positivity of P1,
higher faces or the whole mother objective. All matrices remain external
classical auxiliary objects. Heartbeat World retains the signed six-axis
Cell torsor, no native plane, and separately typed time when relevant; no
physical propagation or native observer quotient is inferred here.

## 2. Sources, normalization and inherited results

The complete trace and polynomial identities come from

1. EM-PERFECT-9821E2,
   `research_notes/owner_goal_20261016/parity_tail_independent_review/PARITY_UNEQUAL_GAPS_UNIFORM_BOUNDED_SECTOR_TAIL_AUTHOR.md`,
   read at 1a553d4d28a105230ecebd5a555dc8adbab8ee28,
   blob f05b0b5be5c7d78c7faf58ae1f818bc67cea103c.
2. EM-DVR-BFF6DC's uniform limiting-metric argument in
   `research_notes/owner_goal_20261016/p11_independent_native_driver/parity_all_m_c1_uniform_sum_tail_addendum_v2_author/PARITY_ALL_M_C1_POSITIVE_TOP_HOMOGENEOUS_FACE_AND_UNIFORM_SUM_TAIL_AUTHOR_V2.md`,
   read at the same commit, blob c94088a17f4a09dd2d16171162c09ed13807a8bf.
   Its additional scalar-boundary contribution is attributed there to
   EM-DVR-F73673. That c1 theorem's review does not review the present whole
   trace theorem.
3. This author's first-round weighted-support lemma, source published at
   59fd52bb8c3a3cbd7a135918579eafd311b39fec under
   `research_notes/balanced_resume_20261028/analysis/PARITY_UNBOUNDED_SMALL_CONE_AUTHOR.md`,
   SHA256 f9a9415455b9b004f9e2854e999eaebd4934acd7211084b87bf1bc5c0634e921.

Set n=m-1, r0=mS, L=ma, N=m(a+c), r=r0+L=m(S+a),
s=r0+N=r+mc. For i=0,...,n put theta_i=(i+1)/m,
w_i=(-1)^i binom(n,i), and

    D_r[i,i]=(n!/m)w_i / product_(h=0)^(m-1)(r+theta_i+h).

Let phi_j(x)=(x)_j/j!, 1<=j<=n, with rising factorials, and

    G_L[i,j]=[phi_j(r0+theta_i+L)-phi_j(r0+theta_i)]/L,
    A=G_L^T D_r G_L, B=G_N^T D_s G_N.

This is the original complete normalization in source 1. The source's
constant sign-diagonal congruence preserves the original normalized Q/H
trace. Both secant frames and the whole signed metric are retained.

On degree<=n-1 polynomials, with monomial coefficient differentiation matrix
J[j-1,j]=j, J^n=0, set

    F_L(J)=sum_(k=0)^(n-1) L^k J^k/(k+1)!.

The derivative polynomials phi_j'(r0+theta) form an invertible common basis,
depending only on r0. Hence an invertible constant matrix U(r0) gives
G_L=Y F_L U(r0), where Y[i,j]=theta_i^j. The same U occurs at N.
Removing this identical congruence yields the relative trace of

    H_L=F_L^T Q_r F_L, H_N=F_N^T Q_s F_N,
    Q_r=Y^T D_r Y.                                           (3)

No L derivative is taken in this proof, so no moving-frame derivative is
implicitly dropped. U is canceled between two exact forms at fixed r0.

Source 2 establishes the analytic metric germ

    Q_r=C_r A_m(epsilon) C_r,
    epsilon=1/r,
    C_r=diag(r^(j-m+1/2)), 0<=j<=n-1,
    A_m(0)=M,                                                (4)

where A_m is analytic at epsilon=0 and independent of L,r0 separately.
The limiting matrix is explicitly

    M[j,k]=kappa [u^(m-1)] u^(j+k)(1+u)^(-m),
    kappa=(-1)^(m-1)((m-1)!)^2/m^m.

In the centered basis (u+1/2)^j, write M_c=T^T M T,
T=exp(J/2). The inherited residue/Fourier Gram proof gives zero cross-parity
blocks, a positive-definite even block and a negative-definite odd block.
The possibly empty odd block for m=2 is harmless. In particular M_c is
nonsingular. This is a limiting-metric statement, not a finite-r definite
metric assertion.

## 3. The common centered input removes the dangerous relative translation

The finite nilpotent identity

    F_L=exp(LJ/2) E_L,
    E_L=sum_(2h<n) (LJ/2)^(2h)/(2h+1)!                      (5)

is the truncated identity (exp(z)-1)/z=exp(z/2)sinh(z/2)/(z/2).
The h=0 term is I, so E_L is unipotent. It contains only even powers of J.

Use the SAME input basis (theta+r0/2)^j for H_L and H_N; its coefficient
change is T0=exp(r0 J/2). Since all factors commute,

    F_L T0=exp(rJ/2) E_L,
    F_N T0=exp(sJ/2) E_N.                                   (6)

The centers r/2 and s/2 differ in the output, but the input change T0 is
identical. Using different input centers would not justify a relative trace
comparison; (6) is the needed exact common-frame identity.

Define the centered analytic germ

    A_c(epsilon)=T^T A_m(epsilon) T, A_c(0)=M_c.

From C_r J C_r^(-1)=J/r it follows exactly that

    exp(rJ/2)^T Q_r exp(rJ/2)=C_r A_c(epsilon) C_r,
    C_r E_L=E_lambda C_r, lambda=L/r=a/(S+a).

Consequently the earlier form in the common input basis is

    T0^T H_L T0=C_r E_lambda^T A_c(epsilon) E_lambda C_r.       (7)

For the later endpoint put

    nu=mc/r=c/(S+a), v=1+nu,
    lambda'=(lambda+nu)/(1+nu),
    D_v=diag(v^(j-m+1/2)).

Then C_s=C_r D_v, 0<=lambda'<=1 whenever 0<=lambda<=1,nu>=0,
and the exact common-scaled pair after canceling C_r is

    A_* = E_lambda^T A_c(epsilon) E_lambda,
    B_* = D_v E_lambda'^T A_c(epsilon/v) E_lambda' D_v.         (8)

In particular Gap+n=tr(B_*^(-1)A_*) exactly for epsilon>0 in the
physical domain. The scalar powers in D_v are real positive because v>0.

## 4. Positivity of the COMPLETE finite-dimensional scaling limit

At epsilon=0 replace A_c by M_c in (8), and call the resulting matrices
A_0(lambda), B_0(lambda,nu). Since E_lambda, E_lambda' contain only even
derivatives and D_v is diagonal, every factor preserves the same even/odd
subspaces. Therefore A_0 and B_0 are both positive definite on the even
subspace and both negative definite on the odd subspace.

On either nonempty block the generalized eigenvalues of (A_0,B_0) are
strictly positive real numbers: negate both matrices on the odd block and
use the ordinary positive-definite congruence. Thus all n eigenvalues
rho_1,...,rho_n of B_0^(-1)A_0 are positive. This conclusion is about the
COMPLETE limiting relative trace, not any finite-r inner signed block.

Because det E_lambda=det E_lambda'=1,

    product_i rho_i = det A_0/det B_0
       =det(D_v)^(-2)=v^(m^2-1),

using 2 sum_(j=0)^(n-1)(j-m+1/2)=-(m^2-1). The scalar AM-GM inequality
for these positive eigenvalues gives

    G0(lambda,nu):=tr(B_0^(-1)A_0)-n
       >= n[(1+nu)^((m^2-1)/n)-1]
       = n[(1+nu)^(m+1)-1],                                (9)

for every lambda in [0,1] and nu>=0. It is strictly positive when nu>0.
For nu>0, Bernoulli's elementary inequality yields

    G0(lambda,nu)/nu >= n(m+1)=m^2-1.                       (10)

The limiting boundary lambda=0 is an analytic extension used for uniform
estimates; the physical theorem retains a>0. No probability interpretation
of the signed full metric is used. The positive eigenvalues result from
the shared parity split established in (6)-(8), not from indefiniteness
being ignored.

## 5. A finite rational uniform tail, including arbitrarily small nu

Uniform convergence of Gap to G0 alone would not suffice when nu can tend
to zero. We use exact divisibility to keep that small-gap factor.

Source 1 gives the exact polynomials

    Gap=c Z(epsilon;a,c)/Dgap(epsilon;c),
    Dgap=|K| Q(epsilon,0)[1+(mc+ell_m)epsilon]
                 Q(epsilon,mc epsilon)^(n-1),
    Q(epsilon,w)=product_(i=0)^n product_(j=0)^(m-1)
                      [1+w+epsilon(theta_i+j)],
    ell_m=(m^2+1)/(2m),
    K=kappa_H^2(product_i w_i)(-1)^n n! m^(1-n) !=0,
    kappa_H=m^(-n(n-1)/2) product_(j=1)^(n-1) j!.

K is the H-germ determinant constant of source 1; it is not kappa in (4).
Put d0=|K|. The first-round support lemma states that in
Z=sum z_(j,p,q) epsilon^j a^p c^q every monomial satisfies p+q<=j-1.
Hence the exact rescaled expression

    P(epsilon,lambda,nu)
      =Z(epsilon;lambda/(m epsilon),nu/(m epsilon))/epsilon
      =sum z_(j,p,q) epsilon^(j-1-p-q)(lambda/m)^p(nu/m)^q

extends to a polynomial in Q[epsilon,lambda,nu]. Its construction has
no negative epsilon powers. Likewise set

    D(epsilon,nu)=d0 Q(epsilon,0)(1+nu+ell_m epsilon)
                                      Q(epsilon,nu)^(n-1).

For epsilon,nu>=0, both D(epsilon,nu) and D(0,nu) are >=d0>0.
The ORIGINAL trace satisfies the exact factorized identity

    Gap = nu F(epsilon,lambda,nu),
    F=P/(mD).                                               (11)

For nu>0, (8) and continuity identify F(0,lambda,nu)=G0(lambda,nu)/nu.
Polynomial/rational extension makes F continuous also at nu=0, so (10)
implies F(0,lambda,nu)>=m^2-1 on the entire compact rectangle
0<=lambda<=1, 0<=nu<=C. No division by a physical zero gap is asserted.

Expand the FINITE polynomials as

    P=sum p_(i,p,q) epsilon^i lambda^p nu^q,
    D=sum d_(i,q) epsilon^i nu^q.

For the supplied positive rational C define nonnegative rational sums

    A_C=sum_(i>=1,p,q) |p_(i,p,q)| C^q,
    B_C=sum_(i>=1,q) |d_(i,q)| C^q,
    H_C=sum_(p,q) |p_(0,p,q)| C^q,
    E_C=(A_C/d0 + H_C B_C/d0^2)/m,
    R_m(C)=max(1,2E_C/(m^2-1)).                              (12)

For 0<=epsilon<=1, 0<=lambda<=1, 0<=nu<=C,

    |P(epsilon)-P(0)|<=epsilon A_C,
    |D(epsilon)-D(0)|<=epsilon B_C,
    |F(epsilon,lambda,nu)-F(0,lambda,nu)|<=epsilon E_C.        (13)

The last inequality follows by expanding the quotient difference, with
both denominators bounded below by d0 and |P(0)|<=H_C. These are finite
coefficient-defined constants, not unevaluated infima over unknown functions.
No numerical evaluation or complexity claim is made.

If S+a>=R_m(C)/m, then epsilon<=1/R_m(C), so epsilon E_C<=(m^2-1)/2.
By (9), (11) and (13),

    Gap >= G0(lambda,nu)-nu(m^2-1)/2
        >= n[(1+nu)^(m+1)-1]-nu n(m+1)/2
        >= n/2[(1+nu)^(m+1)-1],

where the last step again uses (1+nu)^(m+1)-1>=(m+1)nu.
This proves (1)-(2), including all arbitrarily small positive second gaps.

## 6. Deduplication, method harvest and remaining objective

The source check specifically found the older c1 top-homogeneous theorem,
which already handles lambda in [0,1] for a logarithmic derivative and one
coefficient. Its limiting parity metric is reused with attribution. That
source explicitly does not assert the full trace at arbitrary c. Source 1
handles full trace but only bounded a,c. Neither of those inspected source
statements gives (9) for arbitrary finite nu or (2) for whole trace.
Accepted small-m proofs are not reconstructed or counted as new here.

Tool coverage was consulted before this construction. Resolution:
COMPOSE_APPLIED. The substantive new bridge is the same input center in
(6), which makes BOTH scaled endpoint forms share the definite parity blocks,
followed by the determinant-ratio AM-GM argument and exact nu-factor error.
The underlying nilpotent secant calculus, limiting metric, polynomial
majorants and AM-GM are existing tools. No new T family or global novelty
claim is made.

The general compact-total-scale region and c/(S+a) unbounded with a uniform
threshold remain open. Optimizing R_m(C) is not automatic follow-up work.
The direct next question, if selected through fair portfolio routing, is
whether the exact centered finite-r forms admit a substitute for the shared
limiting parity split on a genuinely new region, or whether a complete trace
counterexample exists there. Losing signed/cross-parity terms is not an
acceptable proof of either outcome.

Independent review must check the common-centered-input identity, scaling
order in B_*, positivity only at the limit, determinant exponent, the exact
rescaled polynomial substitution and the small-nu uniform-error argument.
The earlier c1, bounded-sector, small-cone or unrelated Driver verdicts do
not supply this new theorem's independent review.
