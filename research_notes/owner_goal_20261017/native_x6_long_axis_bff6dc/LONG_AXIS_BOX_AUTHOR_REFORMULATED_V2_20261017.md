# Long-axis boxes: all-mass interval connectivity and sharp move mass

NEW REFORMULATED AUTHOR ARTIFACT V2, 2026-10-17.
Sole new author: BFF / EM-DVR-BFF6DC, original session
MCP-47562f9f432d4978a7bea0dd60ecc4aa and
DA-144D0C4639CACEEE75DC; no Researcher RA.
Classification: same-family finite RESULT_ONLY / COMPOSE.
Local unreviewed as this new artifact; no new Source or final context.

This is a new durable reformulation of the complete earlier long-axis
CHAT mathematical argument, with the actual temporary independent
review history below. It is NOT a recovery of the old file's bytes,
token count, SHA256 or Git blob. It neither replaces nor overwrites the
old path. The old successful write/full-read and the later missing-file/
unavailable-pin observations remain distinct facts. The mathematical
scope and the already reviewed argument are not enlarged.

## 1. Fixed six-coordinate model and exact statement

Work in the same fixed restricted discrete six-coordinate chart.
A finite state is an integer-valued nonnegative function on Z^6, written
as a polynomial when its support is in the box below. Its mass is the
sum of its coefficients. These are finite classical observer coordinates
within the declared fixed model, not new Native dynamics or a change of
the underlying six-dimensional spatial semantics.

There are seven joint readouts. The six axis readouts are sums on cosets
of each coordinate axis Ze_i. The seventh is the sum on cosets of the
diagonal Z(1,1,1,1,1,1). In Laurent polynomial language their kernels
are respectively the ideals

    (X_i-1), i=1,...,6, and (X_1...X_6-1).

These are full joint coset readouts, not only six one-coordinate
marginals. A fiber consists of all nonnegative integer states supported
in the SAME fixed box and having ALL seven readouts equal.

Write x=X_1, Y=(X_2,...,X_6), U=X_2...X_6, and let d>=1 be an integer.
The box is

    B_d={0,...,d+1} x {0,1,2}^5.                       (1)

Every intermediate state of a connecting path must be supported in
B_d and have nonnegative integer coefficients at EVERY actual site.
A move is an integer array with zero seven readouts. We treat a palette
as a set of UNORIENTED moves: one member represents both signs.
The move mass is mu(P)=||P||_1/2 for a zero-total-mass move.

Set

    A(Y)=product_(i=2)^6(Y_i-1),
    G=(xU-1)(x-1)A,
    I_(i,j)=G sum_(h=i)^(j-1)x^h
           =x^i(xU-1)(x^(j-i)-1)A,
           0<=i<j<=d.                                (2)

The claims, for each fixed d, are:

* Every all-mass seven-readout fiber in B_d is connected by the literal
  finite palette {+/- I_(i,j):0<=i<j<=d}.
* Every universal connecting palette for ALL such fibers must contain
  every I_(i,j) up to sign. Thus this is the unique inclusion-minimal
  UNORIENTED palette, of cardinality d(d+1)/2.
* mu(I_(i,i+1))=63, and mu(I_(i,j))=64 when j-i>=2.
  The least possible maximal move mass for a universal palette is 63
  for d=1 and 64 for every d>=2.

No literal uniqueness of chosen signed orientations is asserted.
The support diameters and the number of moves grow with d. This does
not give a uniformly bounded-range palette on the full unbounded chart,
does not settle another box geometry, and does not restate the separate
fixed-total-mass/shared-background isolation problem.

## 2. Integer kernel factorization and support localization

We first prove the entire integer kernel needed here rather than
assuming that a rational or real decomposition is integral.
Let

    R=Z[X_1^(+/-1),...,X_6^(+/-1)], D_*=X_1...X_6.

For a finite signed array P, equality to zero under an axis-coset
readout is equivalent to P becoming zero after X_i=1. Division by the
monic X_i-1, or grouping terms on each coset, proves equivalence to
P in (X_i-1), over the INTEGER Laurent ring. The same statement for
the diagonal follows by changing the integer Laurent basis: its kernel
is (D_*-1). The quotient by D_*-1 is again a Laurent ring in five
variables, since X_6=(X_1...X_5)^(-1).

Each of these seven principal ideals is prime: its quotient is an
integer Laurent polynomial domain. No two of the seven generators
divide each other. For example, setting X_i=1 does not make D_*-1 zero,
and setting X_j=1 for j different from i does not make X_i-1 zero.
The diagonal quotient likewise does not annihilate X_i-1.

Consequently a polynomial divisible by all seven generators is divisible
by their product over R. To see this without a comaximality assumption,
successively remove each prime factor: because a new prime divides
the product already removed times the current quotient, and does not
divide any removed generator, it must divide that quotient. Therefore

    zero all seven readouts <=> P=G Q, Q in R.          (3)

No claim that the seven ideals are pairwise comaximal is needed.
The ring is a domain, so Q is unique.

For each variable separately, minimum and maximum exponents of a product
add: view it as a Laurent polynomial in that variable with coefficients
in the integral Laurent ring of the other variables. The leading and
trailing coefficients cannot cancel. The minima and maxima of G in
EVERY variable are 0 and 2. If P is supported in (1), (3) therefore
forces every Y exponent of Q to be zero and its x exponents to lie
between 0 and d-1. Thus

    Q(x)=sum_(h=0)^(d-1) q_h x^h, q_h in Z.            (4)

Conversely every (4) gives an integer signed kernel array supported
in B_d. The case P=0 has Q=0. This proves the COMPLETE kernel and the
integer coordinates for the box, not only a selected sublattice.

## 3. A difference-coordinate bijection and all actual-site inequalities

Extend q by q_(-1)=q_d=0 and by zero outside 0,...,d-1. Put

    t_k=q_k-q_(k-1), k=0,...,d,
    t_(-1)=t_(d+1)=0.                                 (5)

Then sum_(k=0)^d t_k=0. Conversely each integer vector t_0,...,t_d with
this sum has the unique inverse q_h=sum_(k=0)^h t_k, 0<=h<=d-1.
The sum-zero condition gives q_d=0. This is an integer bijection,
not a division over Q or R.

Expanding G in (3) gives at every x level k=0,...,d+1

    P_t(k,Y)=A(Y)t_k-U A(Y)t_(k-1).                    (6)

Let e=(1,1,1,1,1). The supports {0,1}^5 of A and {1,2}^5 of UA meet
only at e. Define

    L={0,1}^5 minus {e},
    H={1,2}^5 minus {e},
    epsilon_a=[Y^a]A in {+1,-1},
    gamma_b=[Y^b]UA in {+1,-1}.

At e, [Y^e]A=+1 and [Y^e]UA=-1. In L there are 15 plus and 16 minus
epsilon sites. In H there are 16 plus and 15 minus gamma sites.
Consequently (6) says exactly

    P_t(k,a)=epsilon_a t_k,        a in L;
    P_t(k,b)=-gamma_b t_(k-1),     b in H;
    P_t(k,e)=t_k+t_(k-1).                              (7)

At every other Y site it is zero. The stated sign counts follow directly
from product(Y_i-1), whose sign at a in {0,1}^5 is (-1)^(5-|a|),
and its translate. All the sign groups used below are nonempty.

Fix any nonnegative integer state f supported in B_d. Its whole fiber
has the unique parametrization f-P_t, where t satisfies (5) and
nonnegativity at every actual site. At a lower-only site this is
f(k,a)-epsilon_a t_k>=0; at an upper-only site it is
f(k,b)+gamma_b t_(k-1)>=0. These give for every i=0,...,d

    l_i=max{
       -min_(a in L,epsilon_a=-1) f(i,a),
       -min_(b in H,gamma_b=+1) f(i+1,b)},
    u_i=min{
        min_(a in L,epsilon_a=+1) f(i,a),
        min_(b in H,gamma_b=-1) f(i+1,b)},
    l_i<=t_i<=u_i.                                    (8)

Common-site nonnegativity gives

    t_(k-1)+t_k<=f(k,e), 1<=k<=d,                      (9)

and the two endpoint constraints
t_0<=f(0,e), t_d<=f(d+1,e). Fold these two constraints into u_0,u_d
by taking the corresponding minimum.

Equations (8),(9), the integer condition, and sum t_i=0 are NECESSARY
AND SUFFICIENT. Sites outside L union H union {e} are unchanged from f.
The endpoint common sites have been included, not lost. Every P_t has
zero total mass by (3), so the parametrization preserves the original
mass as well as every readout.

Thus the original nonnegative fiber is exactly an integer path problem:
node intervals, upper caps on adjacent sums, and a fixed total sum.
In particular the common-site constraints are one-sided caps. Replacing
them by equality, by two-sided caps, or by a sign-conformal assumption
would alter the actual original model.

## 4. The finite path-exchange lemma

Here is the new nonnegative-path obligation in full.
Let t and s be two integer vectors indexed by 0,...,d, both satisfying
the SAME node intervals, the same caps on adjacent sums, and the same
total sum. If t differs from s, there is a deficit index j with t_j<s_j
and an excess index i with t_i>s_i such that

    t'=t+e_j-e_i                                      (10)

also satisfies every constraint. Moreover ||t'-s||_1=||t-s||_1-2.
Repeating (10) therefore terminates in s.

Node intervals are automatically safe: t_j+1<=s_j<=u_j and
t_i-1>=s_i>=l_i. An adjacent-sum cap can only be endangered at an edge
incident to j. An edge whose cap has positive integer slack is still
safe after adding one. An edge between i and j has net change zero.
Thus a deficit j with no tight incident edge allows any excess i.
A deficit j with exactly one tight incident edge allows that edge's
other endpoint, provided it is an excess.

For such a tight edge {i,j}, set delta_j=s_j-t_j>0. Target feasibility
and current tightness give

    s_i+s_j<=t_i+t_j,
    b_i=t_i-s_i>=delta_j>0.                            (11)

So its other endpoint IS an excess with enough units for one transfer.

It remains to prove that not every deficit has two tight incident edges.
Suppose the contrary. Every deficit is then interior. At each positive
integer height h define

    D_h={j:s_j-t_j>=h},
    E_h={i:t_i-s_i>=h}.

By (11) every neighbor of D_h lies in E_h. The distinct left neighbors
j-1 of j in D_h provide |D_h| elements, and the right neighbor of the
largest j in D_h is one more distinct element. Hence, whenever D_h
is nonempty,

    |E_h|>=|neighbors(D_h)|>=|D_h|+1.                  (12)

Summing this finite inequality over heights gives

    sum_(excess i)(t_i-s_i)
       >sum_(deficit j)(s_j-t_j),

contradicting equality of the total sums. Therefore a deficit with at
most one tight incident edge exists and (10) is legal. Its deficit and
excess both fall by one, proving the L1 decrease. The induction is
finite because that L1 distance is a nonnegative integer.

This argument includes d=1 and boundary nodes: they have at most one
interior incident edge, while endpoint common caps already belong to
the node bounds. It never interprets a signed sum as a probability,
uses a fractional transfer, or leaves an actual coefficient negative.

## 5. Translation back to literal interval moves

Under the inverse q_h=sum_(k=0)^h t_k, the change e_i-e_j with i<j
adds one exactly on i<=h<j. Multiplying by G gives I_(i,j) in (2);
the opposite transfer gives its negative. Thus every legal step of
the path lemma is exactly an allowed literal move from the stated
finite palette, and by Section3 it is nonnegative at every actual
site in the original state.

Given any two states f and g in a fiber, use f as the base. The first
state has t=0, and the unique integer kernel representation of f-g
gives the feasible target t for g. Apply the finite path lemma and
translate every step back by (6). This proves all-mass connectivity
in the fixed B_d. At no point do we borrow a probabilistic coupling
or claim an evolution law: the problem here
is the finite integer observer model of Section1.

A useful distinction from a smaller-box sign argument is visible already
at d=3. The kernel P=G(1+x^2) has difference coordinates
t=(1,-1,1,-1). Its common-site coefficients are +1 at x^0, -1 at x^4,
and zero at x^1,x^2,x^3. No interval I_(i,j) has its common-site support
inside just those two endpoints: a length-one interval has endpoint
distance two, and a longer interval has additional nonzero common sites.
Thus a full-site sign-conformal interval reduction is unavailable for
this example. The path proof did not assume one; it used precisely
the genuine one-sided common caps. This prevents an unjustified
extension of a smaller-box conformality argument.

## 6. A two-state fiber forces every interval member

Fix i<j and write I=I_(i,j)=I^+-I^- with disjoint nonnegative
integer parts. Both parts are supported in B_d and have identical
seven readouts by (3). Set f=I^+ and g=I^-.

Consider ANY state in their fiber, not only one reachable by the
proposed palette. By Section2 it must be f-P_(t') for an integer
sum-zero vector t'. The difference coordinates of I itself are

    t_i=+1, t_j=-1, all other t_k=0.

For k not in {i,j}, f(k,a)=0 for every lower-only site a in L.
The plus and minus epsilon groups in (7) therefore force t'_k=0.
At k=i, the lower-only plus group of f has value one and the minus
group has value zero, so 0<=t'_i<=1.
At k=j, the plus group has value zero and the minus group has value
one, so -1<=t'_j<=0. Integrality and sum t'_k=0 imply either

    t'=0, or t'_i=1,t'_j=-1 with all other entries zero.

These give exactly f and g. There are no further states; upper-only
and common sites cannot add another one, and both displayed states
are already feasible. This is an exact TWO-STATE fiber.

A path between its two vertices must use their difference I or -I
as a single edge; no other intermediate state exists. Hence EVERY
palette universally connecting all fibers in B_d must contain
I_(i,j) up to sign, for every i<j. Combined with sufficiency, this
proves the unique inclusion-minimal UNORIENTED palette and the exact
cardinality d(d+1)/2. Directed representative choices are not unique:
replacing any member by its negative denotes the same unoriented move.

This necessity argument does not merely use that the proposed moves
generate the integer kernel; it uses a genuine nonnegative two-state
fiber, which is why a different integer generating set cannot evade
an interval member.

## 7. Exact move masses and sharpness

Let L=j-i. Removing the harmless monomial x^i, (2) is

    I_L=(xU-1)(x^L-1)A
        =x^(L+1)UA-x^L A-xUA+A.                       (13)

Both A and UA have 32 coefficients of absolute value one. If L=1,
the middle x-level is -A-UA. Its two supports meet only at e, where
their coefficients +1 and -1 cancel. All the other 31+31 coefficients
have absolute value one, so this level has L1 norm 62. The bottom and
top levels each have norm32. Therefore

    ||I_1||_1=32+62+32=126, mu(I_1)=63.                (14)

If L>=2, the four x levels 0,1,L,L+1 are distinct. Each contributes
32, with no cancellation between levels. Thus

    ||I_L||_1=128, mu(I_L)=64, L>=2.                  (15)

For d=1 there is only the length-one interval, so (14) and the
two-state necessity prove the sharp maximal-move-mass threshold63.
For every d>=2, a length-two interval exists and is forced by its own
two-state fiber. Thus every universal connecting palette has a move
of mass at least64, while the interval palette never exceeds64.
This proves sharpness64 with all original nonnegative and integer
conditions, not only a real linear span calculation.

The constants 63 and64 describe move mass inside these finite boxed
families. They do not claim that an arbitrary total-mass state has
mass63 or64, or that one fixed finite range works simultaneously for
all d. Those are different quantifiers.

## 8. Real version history, temporary review and exact limits

The earlier fixed short-axis boxed whole was genuinely frozen and accepted:

    author Source bc863ad9b2383898d727c850d768e075e1f8973c
    research_notes/owner_goal_20261016/
    native_x6_boxed_seven_observer_fiber_connectivity_bff6dc/
    BOXED_SEVEN_OBSERVER_ALL_MASS_CONNECTING_PALETTE_AND_SHARP_MOVE_MASS_WORKING.md
    19788 bytes
    SHA256 80e543b28dac68ab8be779b7163b86b402fb45b7a114218e2ae8b8ab792ede43
    Git blob 0ede6637cf9488256efc322355093a9fb4f51667;

    A true peer Source 7788ddc3b3dcb35fcf47afb89691d182cc36a90d
    research_notes/owner_goal_20261016/reviews/
    native_x6_boxed_connectivity_nonauthor_7cda51/
    BOXED_SEVEN_OBSERVER_CONNECTIVITY_COMPLETE_WHOLE_REVIEW_AND_CONTEXT.json
    16885 bytes
    SHA256 cedfa8972f5736ca518ba2c630b6b9c50e4d04f2cd00f26f2257c8c5a58b24e6
    Git blob 3ad1ffb42e059e07b7878d7cd57477fed70c2489.

BFF personally closed that author's actual Source custody, then the
complete ordinary peer semantics and actual peer Source/exact one ADD,
two Sources/36673 bytes. That old status is not a prior vote for the
present all-d long-axis argument. The complete proofs above make
explicit the new all-site path-exchange and necessity obligations.

BFF subsequently constructed this all-d extension as one bounded
same-family branch. The first historical local author file was

    /workspace/enterprise-math/research_notes/owner_goal_20261016/
    native_x6_long_axis_box_interval_palette_bff6dc/
    LONG_AXIS_BOX_ALL_MASS_INTERVAL_PALETTE_AND_PATH_EXCHANGE_AUTHOR_WORKING.md.

Its apply_patch succeeded. The subsequent actual complete cat returned
chunk f5fd95, exit0,5268 tokens without truncation. BFF genuinely read
that complete original body and checked its argument. Before its
metadata could be acquired, execution transport failed. The first
hash cell failed with the reported transport disconnection; the next
hash wait produced no successful identity stdout and was terminated.
No original file byte count, SHA256 or Git blob was ever obtained.
No functions.store key was created for the original patch or cat
bytes. A later Root-only focused environment check found that exact
old path absent in the currently available filesystem. This does not
prove permanent loss or reconstruct the original bytes.

Root explicitly prohibited probing, cloning, changing environments,
overwriting that old path or inventing an old digest. Root later
authorized this NEW independent 20261017 reformulation from the full
already complete author chat argument. This file has its own future
identity. Neither its prose nor its identity is represented as equal
to the old5268-token disk file. No hidden byte recovery is claimed.

Before receiving the precise new long-axis argument, 4A disclosed zero
new body/formula, internal candidate, construction and repair for this
scope. First title/theme metadata was NONZERO; old mass63/moment/CF
background remained warm. 4A had NOT personally whole-read the old
19788 author or16885 peer, and did not claim their old whole or
Source comparison. Root then routed BFF's complete chat Sections2-8,
not only an outline, for a temporary independent paper review.

4A's complete outcome, received and accurately acknowledged by BFF, was

    ARGUMENT_ONLY_PASS_BOUNDED,
    0 mathematical must-fix / 0 construction or repair,
    pending actual durable artifact, pin, Source and final context.

The review independently checked the seven prime factors over the
integer Laurent ring, exponent localization and unique integer q,
the difference-coordinate bijection, all actual-site sign/cap
inequalities, the height-count path argument and its L1 termination,
the literal interval steps, the two-state necessity, and the exact
63/64 payments. It also checked the d=3 nonconformal example. It
accepted the already stated UP-TO-SIGN minimal category, not literal
uniqueness of signed representatives. No reviewer proof patch or
scope enlargement was supplied.

This temporary review is an opinion on the complete chat mathematical
argument. It is NOT a claim that chat bytes equal either original or
new disk bytes, not a Source-bound whole review, and not final
acceptance of this reformulated artifact/context. 4A is now exposed
to this argument and will not be described as prebody0 again.
Future final artifact/Source reception must actually consume the real
new body and context and bind any new Source.

All work here is manual finite algebra and proof. No code enumeration,
scientific program, numerical sample, new search, Native execution,
formal Task, RA, identity or budget reset was used. Prose persistence
and necessary file metadata are the only local execution. No Source
window is conferred by this write. Old observer/classification
authorship, distinct finite-palette/shared-background scopes, old
STOP/HOLD/UNKNOWN and warm histories remain intact. This result is
only the exact finite-box connectivity and minimal palette theorem
above, not a physical law, new full-chart bounded-range library,
global32 conclusion, new Tool or Goal closure. Root supplied control
coordination and no mathematical vote.

