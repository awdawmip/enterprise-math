# Fixed-mass resolution of the boxed sqrt2 polynomial readout

LOCAL FROZEN AUTHOR CANDIDATE / UNREVIEWED.
Same-family RESULT_ONLY / COMPOSE; not a new generic Tool or principal paper.
Sole new quantitative author: BFF / EM-DVR-BFF6DC.
Original SID MCP-47562f9f432d4978a7bea0dd60ecc4aa and
DA-144D0C4639CACEEE75DC; no Researcher RA.
No author Source or independent review of this new argument exists at
creation. Root supplies scope/control coordination and zero mathematical vote.

## 1. Literal model, the minimum being taken, and the statement

Keep the known chart c+Z^6, the fixed box

    B={0,1,2,3} x {0,1,2}^5,

and the original seven FULL joint coset readouts O: the six coordinate
integer-line coset sums and the primitive diagonal integer-line coset
sum. No original readout has errors or missing bins in this problem.
A state is f:B->N_0, extended by zero outside c+B, and mass(f)=sum f.
The integer coordinate u of c+u is used to evaluate a polynomial.

Fix once for all the polynomials, independently of M and of the state,

    P_7(u)=u_1^2 product_(j=2)^6 u_j,
    P_8(u)=u_1^3 product_(j=2)^6 u_j,
    P_*(u)=P_7(u)+sqrt(2)P_8(u),
    T(f)=sum_(u in B) f(c+u)P_*(u).                    (1)

The output T is viewed in its usual real embedding. Our new question
concerns absolute separation in that embedding, not exact symbolic
access to its two rational coordinates.

For an integer M>=0 define the finite set of pairs

    C_M={(f,g): f,g in N_0^B, mass(f)=mass(g)=M,
                  O(f)=O(g), f!=g}.                   (2)

When this set is nonempty put

    delta(M)=min_((f,g) in C_M) |T(f)-T(g)|.            (3)

For an empty set use delta(M)=+infinity. Because B is finite and M
fixed, the state set, and hence C_M, is finite. The minimum in (3)
is an actual minimum over the ORIGINAL nonnegative states, not an
infimum over arbitrary real kernel vectors. The statements are

    C_M empty for M<63; C_M nonempty for EVERY M>=63,
    4/M <= delta(M) <= 2^16/M for EVERY integer M>=63. (4)

The constants are deliberately not optimized. The substantive result
is a matching inverse-population scale for this ONE fixed readout on
this ONE box, with original O exact and the same M on both states.
No other box, probability model, moving polynomial, approximate O,
Native physical noise law or coefficient-field cost assertion is made.

A direct representation-level consequence is that absolute error less
than 2/M in T is sufficient for uniqueness within any exact O-fiber
at known mass M. Conversely no fixed positive absolute-error tolerance
works uniformly across all masses and all these fibers. These are
mathematical separation statements, not numerical algorithms.

## 2. Exact accepted integer interface and the finite response repaid here

Use the previously accepted boxed integer kernel, not a real-nullspace
substitute. In the integer Laurent variables X_1,...,X_6 put x=X_1 and

    G=(X_1...X_6-1)product_(j=1)^6(X_j-1).

For every signed integer array h supported in B,

    O(h)=0 iff H_h(X)=G(a+bx), with UNIQUE a,b in Z,    (5)
    mu(a,b)=mass(h_+)=mass(h_-)
            =32(|a|+|b|)+31|a-b|.                    (6)

Conversely every integer pair gives such a supported signed array.
This is the exact accepted19788 interface, with real personal author/
Source history recorded in Section7. It is not borrowed from the new
19092 working artifact as an already accepted new theorem.

If f,g have difference h, pointwise nonnegativity gives f>=h_+ and
g>=h_-. Thus a pair in C_M necessarily has mu(a,b)<=M.
Conversely for ANY signed h in (5), and ANY integer M>=mu(a,b), choose
one fixed voxel u_0 in B and let

    f=h_+ +(M-mu(a,b))1_(u_0),
    g=h_- +(M-mu(a,b))1_(u_0).                         (7)

These are actual nonnegative integer states supported in B, both have
mass M, have equal O, and their T difference is precisely T(h).
The background is shared, so it changes neither their difference nor
the equality of ANY original coset bin. This supplies the real fixed-
mass bridge needed for both the lower and upper bounds.

Here the response of (1) is checked anew as a finite identity.
For a polynomial P let Delta_w P(q)=P(q+w)-P(q). Multiplication of
a finite array by X^w-1 is adjoint in the literal finite pairing
<P,H>=sum h_u P(u) to Delta_w. Expanding the seven factors of G gives

    <P,X^p G>=D P(p),
    D=Delta_(1,1,1,1,1,1) Delta_(e_1)...Delta_(e_6).   (8)

For P_7 and P_8, first applying the five differences e_2,...,e_6
removes the five linear factors. The e_1 difference leaves,
respectively, 2q_1+1 and 3q_1^2+3q_1+1. The final diagonal difference
shifts q_1 by one. Hence

    D P_7(q)=2, D P_8(q)=6(q_1+1),
    (<P_7,G>,<P_7,xG>)=(2,2),
    (<P_8,G>,<P_8,xG>)=(6,12).

Therefore every actual h in (5) has EXACT response

    R(a,b)=T(h)=2(a+b)+6sqrt(2)(a+2b).                 (9)

This finite calculation does not require the unread10946 whole or
final acceptance of19092. A's polynomial choice and field-readout
motivation are credited, but all load-bearing response arithmetic for
the present quantitative statement is actually supplied above.

For a nonzero integer pair in (6), mu>=63. Indeed if |a|+|b|=1,
then |a-b|=1 and mu=63; if |a|+|b|>=2, then mu>=64.
Equality63 is attained by (a,b)=(1,0). Thus C_M is empty below63,
and (7) with h=G makes it nonempty at EVERY integer M>=63.
This proves the exact nonempty boundary in (4).

## 3. A real separation lower bound from the integer quadratic norm

For a pair in C_M write

    u=a+b, v=a+2b,
    a=2u-v, b=v-u.

This is an integer invertible change of coordinates. Since h!=0,
(a,b)!=(0,0), and therefore (u,v)!=(0,0).
The integer u^2-18v^2 is nonzero: if v!=0 its vanishing would make
sqrt(18)=3sqrt(2) rational, and if v=0 it would force u=0.
Consequently

    |u^2-18v^2|>=1.

With S=|a|+|b|, the actual fixed-mass condition (6) implies S<=M/32.
Moreover |u|<=S and |v|<=2S, so

    |u-3sqrt(2)v|<=(1+6sqrt(2))S
                        <=(1+6sqrt(2))M/32.

The conjugate is nonzero, so factoring the integer norm in (9) gives

    |R(a,b)|=2|u+3sqrt(2)v|
       >=64/[(1+6sqrt(2))M] >4/M.                    (10)

For the last simple payment, sqrt(2)<3/2 gives
1+6sqrt(2)<10 and 64/10>4.
This lower bound applies to EVERY pair in the actual finite minimum.
It also independently proves the requisite injectivity for this
readout; no unreviewed exact-injectivity verdict has been assumed.

## 4. Explicit integer small values satisfying the actual response lattice

A generic irrational-approximation assertion would not be enough:
the response lattice in (9), the signed mass and the nonnegative
original configurations must all be paid. We give explicit integers.

Let

    epsilon=17+12sqrt(2)>1,
    epsilon^(-1)=17-12sqrt(2)>0,

using 17^2-2*12^2=1. Define nonnegative integers u_k,w_k, k>=0, by

    u_0=1, w_0=0,
    u_(k+1)=17u_k+72w_k,
    w_(k+1)=4u_k+17w_k.                               (11)

Finite multiplication shows

    u_k+3w_k sqrt(2)=epsilon^k,
    u_k-3w_k sqrt(2)=epsilon^(-k).                     (12)

Thus no external existence theorem, search, enumeration or program is
needed. In particular u_k>0, w_k>=0. Set

    v_k=-w_k,
    a_k=2u_k+w_k>0, b_k=-u_k-w_k<0.                   (13)

These are actual integer a,b in the original kernel (5), not arbitrary
quadratic-field coefficients. Formula (9) gives the small REAL output

    R(a_k,b_k)=2epsilon^(-k).                         (14)

Because a_k and b_k have opposite signs,

    |a_k|+|b_k|=|a_k-b_k|=3u_k+2w_k,
    m_k=mu(a_k,b_k)=63(3u_k+2w_k).                    (15)

Here m_k is a population, unrelated to the Student-weight parameter m
in other research. We use the symbol only in (15)-(18); no Student
model, norm or auxiliary time is involved in this observer problem.

The sequence m_k consists of positive integers, starts at m_0=189,
is strictly increasing, and is unbounded. Indeed u_(k+1)>=17u_k.
For its successive ratio, (11) yields

    m_(k+1)=63(59u_k+250w_k)<=125 m_k.                 (16)

There is also the useful product bound. From (12),

    u_k=(epsilon^k+epsilon^(-k))/2<=epsilon^k,
    w_k=(epsilon^k-epsilon^(-k))/(6sqrt(2))
                                      <=epsilon^k/6.

Consequently

    m_k<252epsilon^k,
    m_k R(a_k,b_k)<504.                              (17)

Every step is explicit integer arithmetic or the two real embeddings
of the displayed unit. No congruence or factor3 has been suppressed.

## 5. Upper bound for every fixed mass, with full original positivity

If M>=189, choose the largest k with m_k<=M; it exists because the
sequence is strictly increasing and unbounded. Then

    m_k<=M<m_(k+1)<=125m_k.

Use the actual signed array h_k=G(a_k+b_k x) and the shared-background
construction (7). The two states are different, nonnegative at every
actual voxel, supported in B and have the SAME integer mass M and
all seven original readouts equal. Their T difference is (14).
Therefore (16)-(17) give

    M delta(M)<=M R(a_k,b_k)<125*504=63000<2^16.       (18)

If 63<=M<189 instead take h=G, with mu(1,0)=63 and
R(1,0)=2+6sqrt(2)<11. Add the shared background of mass M-63 in (7).
Then M delta(M)<189*11=2079<2^16.
These two cases give the upper bound in (4) for EVERY integer M>=63,
not merely a subsequence of masses admitting a convenient unit.

The proof uses actual sign parts, so it does not infer a legal
nonnegative configuration from an abstract small quadratic-field
number. It does not require that a path under a prescribed palette
connect the two states: the question is separation of their original
readout values within an exact fiber.

Together (10) and (18) prove (4). No claim about optimal constants,
the exactly minimizing pair, an exact formula for delta(M), or its
monotonicity is included.

## 6. The precise resolution consumer and its limits

Fix M and the exact original O-value. If an approximate real output
lies at distance LESS than 2/M from the true T-value, there cannot
be two candidate states of that exact fiber and mass satisfying
that same error bound: their T-values would be less than4/M apart,
contradicting (4). This is a uniqueness certificate. It does not
supply a search algorithm or computational complexity bound.

Conversely let any fixed error tolerance eta>0 be proposed uniformly
over all masses and all O-fibers. Choose an integer M>=63 with
2^16/M<2eta. The actual upper-bound construction in Section5 gives
two different states of mass M, with the same exact O and T-values
less than2eta apart. Their midpoint is a real observation within
eta of both values. Thus a mass-independent positive tolerance
cannot guarantee unique recovery in the worst case.

The upper bound concerns some difficult fiber at each M; it does
not say that EVERY individual fiber has this small a gap.
Both conclusions keep O and M exact. No errors in those original
data are modeled.

The A field-valued theorem is about one EXACT element of Q(sqrt(2)),
which contains two rational coordinates if represented symbolically.
Here we deliberately test one REAL EMBEDDING value with absolute
error and a known finite population. These information formats must
not be interchanged. There is no assertion that irrational arithmetic
or two rational coordinates are cost-free, no floating-point
implementation, no physical-sensor count and no Native noise law.
The result supplies an explicit mathematical representation-
stability interface, not a cure for GEO6 missing laws, CM24 lifts,
Parity signed Ae/commutator control or full Psi/coefficient HOLD.

## 7. Actual input history, new authorship and publication boundary

The one newly consumed working object was A's full19092-byte
author artifact:

    repository awdawmip/enterprise-math
    Source 114a5e1b27430553512dc4f6b15171db60c1ae14
    research_notes/owner_goal_20261016/
    native_x6_boxed_polynomial_readout_field_bridge_7cda51/
    BOXED_ALL_MASS_POLYNOMIAL_READOUT_COEFFICIENT_FIELD_BRIDGE_WORKING_AND_CONTEXT.md
    Git blob e14466f7c836477c7194076150f8549a45126ba3.

BFF personally located that immutable commit's one added path,
then made one managed full UTF8 fetch and genuinely read ALL nine
sections, all formulas and the entire author context in one
untruncated output. The actual caller is stored as
bff_field_readout_actual_authorfile; the separate commit locator
is bff_field_readout_author_commit_locator. BFF did not read its
new4A peer, did not perform a new GitData/compare intake, and does
not describe that working claim as already finally accepted.
The old10946 moment body is still not personally whole-read by
BFF. It is not a hidden premise: the needed finite response was
actually recalculated in Section2.

The mathematical old kernel/mass interface (5)-(6) is the accepted
BFF19788 single-long-axis boxed whole:

    Source bc863ad9b2383898d727c850d768e075e1f8973c
    research_notes/owner_goal_20261016/
    native_x6_boxed_seven_observer_fiber_connectivity_bff6dc/
    BOXED_SEVEN_OBSERVER_ALL_MASS_CONNECTING_PALETTE_AND_SHARP_MOVE_MASS_WORKING.md
    19788 bytes
    SHA256 80e543b28dac68ab8be779b7163b86b402fb45b7a114218e2ae8b8ab792ede43
    Git blob 0ede6637cf9488256efc322355093a9fb4f51667.

Its genuine A whole review is Source
7788ddc3b3dcb35fcf47afb89691d182cc36a90d,
research_notes/owner_goal_20261016/reviews/
native_x6_boxed_connectivity_nonauthor_7cda51/
BOXED_SEVEN_OBSERVER_CONNECTIVITY_COMPLETE_WHOLE_REVIEW_AND_CONTEXT.json,
16885 bytes, SHA256
cedfa8972f5736ca518ba2c630b6b9c50e4d04f2cd00f26f2257c8c5a58b24e6,
Git blob 3ad1ffb42e059e07b7878d7cd57477fed70c2489.
BFF's original full author reading, actual author Source custody,
complete ordinary true-peer semantics and own actual peer Source/
exact comparison had genuinely closed two Sources/36673 bytes.
That old history is reused without new old-body fetches, hashes or
claims of somebody else's API.

Coverage was bounded. A's original19092 explicitly excluded noise/
finite-precision/separation estimates. Asked only for existing
coverage/occupation metadata, A reported no frozen exact delta(M)
locator in her personal coverage and no occupation of that scope;
she performed no new search or derivation for BFF. This is not an
all-library absence claim. On seeing the question, A truthfully
reported a general new internal feasibility association NONZERO.
She was not supplied BFF's unit recurrence, bounds or proof and
is not preselected as a zero-candidate reviewer of this new scope.

BFF's old moment question-triggered internal associations were
already NONZERO; its old boxed authorship, new two-axis authorship
and current field-artifact reading remain warm. The present
quantitative construction is BFF's new author work, internal
history NONZERO. A retains the polynomial choice and exact-field
consumer credit in19092; BFF's old boxed kernel credit is retained.
A is not automatically a coauthor of the new quantitative proof,
and neither Root nor a future reviewer supplied a proof patch.

The new obligation was a population-dependent real-resolution
bound, different from a polynomial degree/output-count result
and different from movement/connectivity thresholds. The kill
condition was to stop if only abstract irrational approximation
or a subsequence remained without the exact response lattice,
true sign parts, all fixed masses or original readout equality.
Sections2-5 explicitly pay those obligations. This is standard
quadratic-field arithmetic COMPOSE applied to the literal finite
state interface, not a new Diophantine Tool family.

No scientific code, matrix/coefficient generation, enumeration,
numerical sample, external search, Native execution, helper, RA,
formal Task, identity or budget reset was used. Only prose
persistence and necessary byte metadata are local administrative
execution. All old STOP/HOLD/UNKNOWN and authored/reviewer
histories remain. No independent peer has yet reviewed this
new proof; no new author Source or final artifact acceptance is
prefilled. Author self-reading and the actual local byte freeze
are separate subsequent observations. Old19092,19788 and every
earlier frozen author/review file are unchanged.

