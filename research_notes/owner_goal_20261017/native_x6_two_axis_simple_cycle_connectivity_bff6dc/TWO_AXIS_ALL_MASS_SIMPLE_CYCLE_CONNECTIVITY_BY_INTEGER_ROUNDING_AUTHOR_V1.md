# All-mass two-axis connectivity by actual simple-cycle moves

First complete LOCAL AUTHOR WORKING / UNREVIEWED.
New mathematical author: BFF / EM-DVR-BFF6DC, original session
MCP-47562f9f432d4978a7bea0dd60ecc4aa, authority DA-144D0C4639CACEEE75DC.
This is a finite same-family RESULT_ONLY / COMPOSE candidate, not a new
general Tool, principal-paper claim, Native dynamics or formalTask.
Root coordinates scope/control and supplies zero mathematical votes.

## 1. Literal model, palette and result

Keep the original chart c+Z^6, the SAME seven full joint coset readouts O
(six coordinate-line directions and the primitive all-ones diagonal),
and precisely

    B={0,1,2,3}^2 x {0,1,2}^4.                                  (1)

A state is an actual N0 array on B, extended by zero. All intermediate
states below are actual arrays in this same box and have the same O.
No change of Student/model parameter, observer, positivity or support
category occurs. A path is an auxiliary finite graph path, not time.

Write x,y for the two long coordinate variables and Z1,...,Z4 for the
four short variables. Set

    U=product Zi, A=product(Zi-1), T=(x-1)(y-1),
    Phi(H)=(xyU-1) H A, G=Phi(T), L(H)=(xy-1)H.                 (2)

The accepted13283 two-axis kernel interface says every integer O-zero
array supported in B is uniquely GQ with Q separately of degree <=1
in x and y. Equivalently H=TQ is an integer 3-by-3 table, supported in
{0,1,2}^2, with zero row and column sums. Conversely every such table
gives a supported integer O-zero array Phi(H).

Let S consist of the actual Phi images of all simple transportation
cycles of the bipartite K3,3 row/column graph, with both signs allowed.
A simple cycle table has alternating unit entries on four or six sites.
There are nine unoriented four-cycles and six unoriented six-cycles.

**Theorem.** S connects EVERY actual N0 O-fiber in B, at every mass.
More precisely, write f-g=Phi(H), H=TQ, and Q=a+bx+cy+dxy. Put
t=a+d-b-c and

    D=max(|a|,|b|,|c|,|d|,|t|).

There is a legal path from f to g with at most2D simple-cycle moves.
D=0 means f=g and the empty path. The bound is in coefficient variables,
not a Native time or implementation-complexity assertion.

Every member of S has positive/negative mass <=96. Thus S is a finite
universal connecting palette with that conservative mass bound. This
does NOT assert that96 is sharp or classify all universal palettes.
The older actual two-state mass93 obstruction remains a separate lower
bound. The new accepted mass124 actual-conformal indecomposable example
remains correct: the present path is NOT required to be actual-site
conformal or between its endpoint occupancies.

## 2. Complete actual-site inequalities and five potentials

Fix any starting state f>=0. Parameterize every other same-O array by

    k=f-Phi(H), H=TQ, Q=a+bx+cy+dxy.                           (3)

With x indexing rows and y columns, the nine entries of H are

    [ a       c-a        -c ]
    [ b-a     t          c-d ]
    [ -b      b-d        d ],       t=a+d-b-c.                (4)

Thus the five potentials (a,b,c,d,t) obey the single balance equation

    a+d-b-c-t=0.                                             (5)

The last-coordinate cubes supporting A and UA are {0,1}^4 and {1,2}^4.
Their only common point is e=(1,1,1,1). Both common coefficients are+1.
Each exclusive cube has15 sites and contains both signs (7 and8).
For epsilon and gamma the respective unit coefficients, the exact
array at every site is

    lower exclusive:  -epsilon H(i,j);
    upper exclusive:   gamma H(i-1,j-1);
    common e:          H(i-1,j-1)-H(i,j)=L(H)_(i,j).            (6)

H is zero outside its 3-by-3 support. Other transverse sites are zero.
Hence k>=0 at all exclusive sites is exactly a collection of integer
lower and upper bounds on each H_ij. All these bounds are obtained from
the corresponding actual f occupancies; both signs really occur.
No coefficient is removed and there is no surrogate table positivity.

The common positions range over {0,1,2,3}^2. Of the sixteen positions,
the ten boundary expressions are individual entries with a sign:

    negatives: -H00,-H01,-H02,-H10,-H20;
    positives:  H20, H21, H22, H02, H12.

The two positions(0,3),(3,0) have expression0. These constraints merely
tighten the individual H-entry intervals. The four interior expressions
are, exactly,

    (1,1): a-t;
    (1,2): d-a;
    (2,1): d-a;
    (2,2): t-d.                                              (7)

Consequently all actual nonnegativity constraints are EXACTLY:
integer interval bounds on the nine forms in(4), together with

    a-t<=c11, d-a<=min(c12,c21), t-d<=c22,                     (8)

where cij=f(i,j,e) are actual nonnegative integers. Positions that were
zero in(6) remain unchanged nonnegative f positions.

Call the resulting real feasible set P_f, including balance(5).
It is convex because every constraint is linear. Its integer points
are in bijection with the ENTIRE actual O-fiber of f, by(3)-(6).
In particular0 is feasible, and the target potentials in section1 are
feasible. Every integer potential step preserves all original O bins
and total mass; nonnegativity is equivalent to membership in P_f.

All constraints, apart from balance, are integer individual bounds or
integer difference bounds. The only possible directed difference edges
i->j for an inequality x_i-x_j<=integer are

    a<->b, a<->c, d<->b, d<->c;
    a->t, t->d, d->a.                                        (9)

The double arrows allow either/both directions from an interval bound.
Individual potential bounds follow from H00,H20,H02,H22,H11, and
bounds on the remaining four H entries give the first four pairs.
The three common bounds give precisely the oriented triangle in(9).
There are NO additional reverse common inequalities silently assumed.

## 3. A small directed-graph fact

Give vertices a,d weight+1 and b,c,t weight-1. For ANY directed subgraph
of(9), every strongly connected component has total weight in

    {-1,0,1}.                                                (10)

Here a singleton is allowed. This is verified completely as follows.

A component containing no positive vertex has no edges among its
negative vertices, so it must be a singleton. A component containing
both positive vertices cannot consist only of{a,d}: the only direct
edge is d->a, so returning requires at least one negative vertex.
Its weight is therefore at most1, and at least-1 even if all three
negative vertices are present.

A component containing exactly one positive vertex has weight between
1 and-1 unless it contains all three negative vertices. The possible
four-vertex sets of that exceptional type are{a,b,c,t} and{d,b,c,t}.
In the former set, t has no outgoing edge to another vertex: its only
possible outgoing edge goes to d, which is missing. In the latter set,
t has no incoming edge from another vertex: its only possible incoming
edge comes from a, which is missing. Neither set can be strongly
connected. This proves(10), with all component possibilities covered.

This fact is about allowed directed constraints, not a false claim that
all connected subsets have balanced weights or that every vertex of
P_f is integral.

## 4. Feasible integer rounding inside a unit box

**Rounding lemma.** For every real p in P_f there is an integer z in P_f
with, in each of the five coordinates,

    floor(p_i)<=z_i<=ceil(p_i).                              (11)

Let n_i=floor(p_i), theta_i=p_i-n_i. Coordinates with theta_i=0 are
already fixed. At every fractional coordinate choose z_i=n_i+u_i with
u_i in{0,1}.

An individual integer interval containing p also contains both its floor
and ceiling. For a difference constraint p_i-p_j<=k with integer k,
feasibility gives n_i-n_j<=k. If n_i-n_j<=k-1, every rounding of those
two coordinates is safe. If n_i-n_j=k, precisely the implication

    u_i<=u_j                                                (12)

is required, and p feasibility gives theta_i<=theta_j.
A fixed theta=0 coordinate cannot be the nonfractional target of an
implication from a fractional coordinate, since that would require
positive theta_i<=0. Fixed-source implications are harmless. We may
therefore use a directed implication graph only on fractional vertices.
It is a subgraph of(9); within each of its strongly connected
components all theta values are equal and all rounding bits must agree.

Write sigma=(+1,-1,-1,+1,-1) in coordinate order(a,b,c,d,t).
The integer balance required of u is

    sum sigma_i u_i = r := -sum sigma_i n_i
                         = sum sigma_i theta_i.              (13)

The last quantity is an integer because p satisfies(5).
For 0<h<1 let I_h={i:theta_i>=h}. Each I_h is closed under all outgoing
implications by theta_i<=theta_j. Moreover

    r = integral_0^1 weight(I_h) dh.                         (14)

Order the distinct fractional levels from high to low. At a single
level, add its strongly connected components in reverse topological
order, so every prefix remains closed under outgoing implications;
components at greater levels are already included. This yields a chain
of closed sets from empty to all fractional vertices, containing every
threshold set I_h. By(10) the weight changes by at most1 at each step.

The integer r lies between the minimum and maximum weights of threshold
sets, by(14), and hence between the minimum and maximum along the
refined chain. An integer walk with increments in{-1,0,1} attains every
integer between its extremes. Choose a closed set of weight r and use
its indicator for u. Then(12) and(13) both hold. All difference bounds,
individual bounds and balance are preserved, proving(11).

This is a feasibility rounding statement. It neither claims a convex
combination representation nor wrongly infers integral vertices.

## 5. The full simple-cycle list in potential coordinates

For clarity, the fifteen unoriented simple-cycle directions are written
as Q polynomials. The nine four-cycles are

    1, x, y, xy,
    1+x, 1+y, x+xy, y+xy,
    1+x+y+xy.                                                (15)

Their cycle tables H=TQ are T times the corresponding row/column interval sums.
The six six-cycles are

    1+x+y, 1+x+xy, 1+y+xy, x+y+xy,
    x-y, 1-xy.                                               (16)

Direct substitution into(4) gives exactly six alternating unit entries
in each case in(16). For example1+x+xy gives the old mass93 cycle.
There are only nine choices of two rows/two columns for four-cycles
and six unoriented Hamilton cycles of K3,3 for six-cycles; alternatively
the displayed distinct tables exhaust the usual simple cycles directly.
Both signs of every displayed direction are allowed.

A nonzero five-coordinate difference delta in{-1,0,1}^5 satisfying(5)
has two or four nonzero entries, since the nonzero signed balance
terms are all+1 or-1 and must sum to0. Every balanced two-coordinate
direction is one of(15)-(16): there are six same-sign pairs between
{a,d} and{b,c,t}, three opposite-sign pairs within{b,c,t}, and one
opposite-sign pair within{a,d}. Their Q forms are precisely

    1,x,y,xy, 1+x,1+y,x+xy,y+xy, x-y,1-xy.                   (17)

The remaining five directions in(15)-(16) have four nonzero potentials:
- all four potentials increase, with a negative vertex omitted
  (omit t, b or c); these give respectively
  1+x+y+xy, 1+y+xy, 1+x+xy;
- a is omitted and d,b,c increase while t decreases: x+y+xy;
- d is omitted and a,b,c increase while t decreases: 1+x+y.
Their negatives give the opposite orientations.

## 6. Every feasible balanced unit-box jump splits into <=2 cycles

Let v,w be integer feasible points of P_f with
||w-v||_infinity<=1. Coordinate bounds are respected by every point
obtained by flipping any subset of the changed coordinates from v to w.

For a difference inequality, if the two coordinates move in opposite
directions or one stays fixed, every partial flip puts their difference
between its two endpoint values, hence is safe. Only coordinates moving
in the SAME direction can cause an excursion; flipping both or neither
preserves their difference. This observation applies to every allowed
difference inequality, including its actual orientation.

If w=v there is no step. For two nonzero changes,(17) is already one
simple-cycle move. For four changes the following cases exhaust balance.

First suppose the omitted vertex is negative (b,c or t). The remaining
vertices have two positive and two negative weights. Up to reversing
v,w, either all four increase, giving a direct cycle listed above, or
exactly two increase and two decrease, each pair having one positive
and one negative weight. In the latter case flip the whole increasing
pair first. It is balanced. Within each same-direction pair either both
or neither have flipped, so their differences do not change; differences
across the two groups move monotonically between endpoints. Thus this
intermediate point is feasible. Each of the two pair moves is in(17).

Now suppose a positive vertex is omitted. Reverse v,w if necessary so
that the remaining positive vertex increases. Balance forces two of
the negative vertices to increase and the third to decrease.
If t decreases, this is already one of the two direct four-coordinate
cycles in section5. Otherwise t and one ordinary negative vertex
k in{b,c} increase, and the other j in{b,c} decreases.

If a is omitted, d,k,t increase and j decreases. First flip only d and k
upwards. This is a balanced pair. The sole possible same-direction
difference between a flipped and unflipped changed vertex is t-d:
it has DECREASED by1, so its only common constraint t-d<=c22 is
relaxed. There is no edge between the negative vertices k and t.
The d,k difference is unchanged; every other relevant difference is
between its endpoint values. Thus this intermediate point is feasible.
The second pair flips t up and j down. Both are simple-cycle directions.

If d is omitted, a,k,t increase and j decreases. First flip only t up
and j down. This is balanced. The sole analogous excursion is a-t:
it has DECREASED by1, so a-t<=c11 is relaxed. There is no edge between
k and t. The a,k pair is still unflipped; all other differences are
between endpoint values. Again the intermediate point is feasible.
The second pair flips a and k up, and both pairs are in(17).

This covers every sign pattern, omitted vertex, zero difference and
reverse orientation. Every intermediate lies coordinatewise between
v and w in POTENTIAL coordinates. No assertion of actual occupancy
conformality was used. At most two genuine simple-cycle moves suffice.

## 7. Global path, all actual sites, and mass bound

Let v,w be any two integer points of P_f. If they differ, put
D=||w-v||_infinity, a positive integer. By convexity,

    p=v+(w-v)/D

lies in P_f. Apply section4 to obtain feasible integer z between its
coordinatewise floor and ceiling. Each z_i is between v_i and w_i;
also |z_i-v_i|<=1. At any coordinate with |w_i-v_i|=D, p_i is exactly
v_i+sign(w_i-v_i), an integer, so z_i equals that value.
At every other coordinate |w_i-v_i|<=D-1. Therefore

    ||w-z||_infinity<=D-1,  ||z-v||_infinity<=1.               (18)

Section6 joins v to z by at most two S steps in P_f. Repeat with z,w;
the integer distance drops by at least1 each round. Induction gives
a path with at most2D steps. If D=1, p=w and section6 already applies.
If D=0 the empty path applies.

Use v=0 and w the target potentials for f-g. At each intermediate
integer point, equations(3)-(8) give an actual nonnegative state in B,
not merely a table or a real point. Every difference is exactly one
unit simple-cycle Phi image, not a positive combination, batch,
multiple, approximate step or path using another readout. All original
bins and mass remain unchanged. This proves the theorem for every
fiber and every mass, including empty movement at zero/singleton fibers.

For a simple-cycle table C, ||C||_1 is4 or6. The disjoint site types
in(6) give the exact identity

    ||Phi(C)||_1=30||C||_1+||(xy-1)C||_1
                <=32||C||_1<=192.                           (19)

Since its total is0, positive and negative masses are half its L1 norm,
so every palette move has mass<=96. This is an upper certificate, not
a sharpness claim. On low-mass fibers, the constructed path simply
cannot use a move whose sign part the current state cannot support:
actual feasibility at every step has already been proved, not assumed.

The accepted19286 example (1+xy)G has actual-conformal indecomposability
and a necessary temporary common-site buffer in its three-state fiber.
It remains a counterexample to a stronger, FALSE method. Our proof
allows temporary occupancy at zero-endpoint sites and only keeps the
five potentials between selected round endpoints. It therefore neither
contradicts nor silently reinstates actual-site conformal lifting.

## 8. Real inputs, contribution history and stopping scope

The two new research-intake objects were genuinely managed-fetched and
completely read by BFF, all primary eight sections/(1)-(18)/context and
all peer seven sections/context. Original entire returns are retained as
bff_twoaxis_conformal_intake_author and
bff_twoaxis_conformal_intake_peer. They are:

A author19286:
 Source298f59d8342fbefd214e866b846e504a03b7243b,
 research_notes/owner_goal_20261017/native_x6_two_axis_site_conformal_lift_7cda51/TWO_AXIS_SIMPLE_CYCLE_CONFORMAL_LIFT_FAILURE_AND_THREE_STATE_FIBER_WORKING_AND_CONTEXT.md,
 SHA2560e48ebdb040ea3bdadb36ec35de241dadeb6c6bac52f39c36153e38de76154eb,
 GitOID59fdf33c3f9b97c911ba9a66d13ba33657e98006.
4A genuine peer18362:
 Sourceefe4920b5c8b4abe0cae37434f3dafe9a2e9efd1,
 research_notes/owner_goal_20261017/reviews/native_x6_two_axis_site_conformal_lift_nonauthor_4a56e9/TWO_AXIS_SITE_CONFORMAL_LIFT_AND_THREE_STATE_FIBER_INDEPENDENT_WHOLE_REVIEW_AND_CONTEXT.md,
 GitOIDd70e1e30633ed89221eba054e61aa2c13ccbe443.
Root routed these as actually accepted after both actors' own Source
and A ordinary2/37648 closure. My new immutable full-file calls bind
both whole bodies and OIDs/URLs. I do not claim to have repeated their
commit comparisons, borrowed their APIs, or supplied another peer vote.

The necessary older complete two-axis kernel/site interface is my
accepted13283 whole at Source3c6c0fe93149bbdc0b65479ad0c0a9b1284bb0f5,
 research_notes/owner_goal_20261017/native_x6_two_long_axes_bff6dc/TWO_LONG_AXES_MASS64_EXTENSION_OBSTRUCTION_AUTHOR_V1.md,
 SHA256b1602d579c3b7ac64e37fcf34647d904ca6b960167f511db69cfd663829a2b6c,
 GitOID899134e1235770a27b9aa3d96773255706824735.
The filename is historical; its theorem is the mass93 two-state
obstruction and complete actual kernel, not a mass64 upper result.
A's true13983 peer is Source4f91987a99ec1279abe783a2ff54052829644694,
 GitOIDe1fdfdd3ffb52959c6c7602a04340ced038f22bb.
My true ordinary2/27266 whole/full-source acceptance already closed.
These old personal histories are honestly reused with no new old API,
hash or old compare. The older single-axis19788 model work is background,
not an automatic two-axis connectivity premise.

Before A's new19286 proof I had disclosed unclosed internal transport
cycle/common-site compatibility strategy NONZERO, with no actual proof
or repair supplied to A. A alone authored her new table, indecomposability,
three-state fiber and buffer path; 4A gave its independent whole review.
Those credits and all old warm authorships remain. After consuming
these two accepted objects I selected the previously OPEN universal S
connectivity question. A replied only metadata: no frozen full-S
locator/occupation, and her own unclosed later internal ideas NONZERO.
No formula, witness, proof patch or repair was requested or received.

The new five-potential exact reduction, directed-component balance
bound, feasible integer rounding, full unit-box case split and global
all-site path proof in THIS note are BFF's new construction. A/4A/CF
are not automatically coauthors because of upstream work or private
associations, and no clean/cold candidate history is invented for them.
No independent review of this new whole or actual author Source exists
at creation. Root supplied no mathematical construction or vote.

The discriminator was full actual N0 cycle connectivity versus a
genuine disconnected fiber, not merely a formal table decomposition.
The former is now author-proved by sections2-7; it remains UNREVIEWED.
The scope is only this fixed two-long-axis box and the original seven
readouts, with arbitrary actual N0 configurations/mass. It does not
classify minimal palettes, prove sharp93/96, handle other boxes or
more long axes, or assert Native dynamics/physical laws. It supplies
no Student/Ae/Psi, field-readout, resolution or other-family result.

All reasoning was finite hand mathematics. No coefficient program,
enumeration, numerical experiment, solver, external query, new Native
or formalTask was run. Tools only persist/read prose and necessary
new-file byte metadata. Existing Driver/DA/noResearcherRA, all previous
STOP/HOLD/errors/UNKNOWN budgets and GoalOPEN remain unchanged.
There is no new helper, identity, budget reset or Source window.
Author Source=PENDING; independent whole/context review=PENDING;
acceptance=PENDING. Original inputs and their creation words are not
edited. First exact file pin and actual full self-read are established
by the separate readback, not predicted in this creation text.
