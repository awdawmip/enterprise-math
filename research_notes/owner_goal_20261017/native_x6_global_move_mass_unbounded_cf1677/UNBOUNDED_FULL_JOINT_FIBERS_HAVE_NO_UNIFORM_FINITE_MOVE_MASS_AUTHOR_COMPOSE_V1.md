# Full joint fibers admit no uniform finite move-mass bound

LOCAL AUTHOR CANDIDATE / UNREVIEWED.
Same-family RESULT_ONLY / COMPOSE; no independent Tool or principal-paper claim.
Sole new author: CF1677 / EM-FREE-CF1677, original warm execution.
Root coordinates scope and custody and supplies zero mathematical vote.
No author Source, independent review or final acceptance of this new whole
exists at creation. The proof below is ordinary finite mathematics, with no
scientific program, enumeration, search, Native execution or physical-time claim.

## 1. Original object, new quantifiers and the result

Keep the original restricted native6DCell integer chart c+Z^6. A state is a
finitely supported function f:c+Z^6 -> N_0. Its mass is the sum of its actual
integer multiplicities. The same original seven FULL readouts O are retained:
for each of the six coordinate directions e_i and for d=(1,1,1,1,1,1), one
records the sum on EVERY integer-line coset of Z e_i or Z d. There is no
discarded bin, selected-moment replacement or additional observer. All charts,
directions and readouts here are the original restricted model, not a claim
that an arbitrary auxiliary graph supplies Native geometry or a time law.

A signed move h is a nonzero finitely supported integer array with O(h)=0.
Its positive and negative parts h_+,h_- have the same mass; write

    mu(h) = mass(h_+) = mass(h_-).

Indeed any one of the full coordinate readouts determines the total sum.
For a finite D>=0 let C_D contain ALL such signed arrays with mu(h)<=D,
with both signs, all translates, every finite support and no range bound.
This is generally an infinite library. A legal step is f -> f+h for h in
C_D when the entire destination is nonnegative. A path consists of finitely
many such steps. It preserves every original bin and the original mass.
The path graph is a comparison object; it is not Native or physical time.

The new question has the quantifiers

    Does some finite D connect every full O-fiber, at every mass M?

The result is the opposite:

    For every finite D there is a finite original N_0 state f_0 whose
    GLOBAL full O-fiber consists of exactly two states {f_0,f_1}, and
    mu(f_1-f_0)>D. Both states are isolated under the complete C_D library.
                                                                    (1)

Thus arbitrary translations, arbitrary ranges and infinitely many available
moves do not give a uniform finite move-mass bound for all these fibers.
The proof constructs an unbounded family, rather than promoting a fixed-box
obstruction or a single first-failure example to an all-D statement.

## 2. Full integer kernel and confinement, repaid for this whole

Write X^u=X_1^{u_1}...X_6^{u_6}, and identify a finite signed array with its
integer Laurent polynomial in

    A = Z[X_1^{+/-1},...,X_6^{+/-1}].

For a primitive integer direction v, the full coset-sum readout is precisely
the group-ring quotient map to Z[Z^6/Zv]. Its kernel is (X^v-1). This can be
seen after completing v to an integer basis: the quotient sets the variable
for v equal to 1, and ordinary division by that variable minus 1 leaves
exactly the coset sums as remainder. The coefficients stay integral.

Each e_i and d is primitive, and its quotient group is free abelian. Thus
each of X_i-1 and X^d-1 is a prime element: its quotient ring is an integral
Laurent polynomial ring over Z. The seven factors are pairwise nondividing.
For example, setting X_i=1 leaves a nonzero coordinate factor X_j-1 for
j!=i and leaves the nonzero diagonal factor product_{j!=i}X_j-1. In the
diagonal quotient, e_i is nonzero modulo Zd, so X_i-1 also stays nonzero.

If all seven readouts vanish, each of these prime factors divides the signed
polynomial. Primality and pairwise nondivisibility then let one remove the
factors successively. Conversely their product kills each readout. Hence

    O(h)=0  iff  H_h = G Q for a unique Q in A,
    G=(X_1...X_6-1) product_{i=1}^6 (X_i-1).          (2)

This is the integer Laurent kernel, not a real nullspace or a rational
coefficient substitute. Uniqueness follows because A is an integral domain.

There is also a useful GLOBAL consequence of retaining every original bin.
For N>=3 put

    B_N={0,...,N} x {0,...,N} x {0,1,2}^4.           (3)

Suppose f is supported in c+B_N and g is any finite nonnegative state on
the whole chart with O(g)=O(f). If g(c+u)>0 outside this box, some coordinate
j of u lies outside its allowed interval. Choose a coordinate i!=j. The
coordinate-i coset through u retains coordinate j, so it contains no point
of B_N. Its full original sum for f is zero, but its sum for g is positive,
a contradiction. Therefore

    Every GLOBAL nonnegative state in the fiber of f is in c+B_N.       (4)

The same applies to every state reached by any legal move or path. This is
not an imposed box restriction on C_D: it is forced by the original full
readouts and nonnegativity. It does not use a range bound on the move.

## 3. An exact arbitrary-size table model on actual six-dimensional sites

Set x=X_1, y=X_2 and use z_3,...,z_6 for the other variables. Put

    Z=z_3 z_4 z_5 z_6,   E=product_{j=3}^6(z_j-1),
    G=(xyZ-1)(x-1)(y-1)E.

If a nonzero jointkernel array is supported in B_N, (2) bounds its quotient
Q without any field extension. For each individual variable, the minimum
and maximum exponents of a product of two nonzero Laurent polynomials add:
the extreme coefficients multiply nontrivially in the integral domain in
the remaining variables. The minimum and maximum exponents of G are 0
and 2 in EVERY variable. Thus Q has minimum exponents at least zero; its
degree in x and y is at most N-2, and its degree in each z_j is at most
zero. It is an integer polynomial in x,y alone.

Define

    H(x,y)=(x-1)(y-1)Q(x,y)=sum_{i,j=0}^{N-1} H_ij x^i y^j.

The integer N by N table H has all row sums and all column sums zero.
Conversely every such integer table is divisible by (x-1)(y-1) over Z:
evaluation at x=1 gives the first divisibility, and evaluation at y=1
after that division gives the second. The quotient degrees are at most
N-2 in each variable. Consequently the exact boxed kernel is the injective
integer map

    Phi_N(H)=(xyZ-1)H(x,y)E,
    H an integer N by N table with zero row and column sums.           (5)

The zero array corresponds to H=0. Both directions in (5) have now been
proved on the original sites, including the actual support bounds.

We will need the signs of actual site coefficients, not just an abstract
table dimension. Extend H_ij by zero outside 0<=i,j<=N-1, and for
eta in {0,1}^4 write s_eta=(-1)^{4-|eta|}. At an actual site (i,j,nu),
where nu is the last four coordinates, the coefficient of Phi_N(H) is

    -s_nu H_ij,                  nu in {0,1}^4 except 1^4;
     s_(nu-1) H_(i-1,j-1),       nu in {1,2}^4 except 1^4;
     H_(i-1,j-1)-H_ij,           nu=1^4;
     0,                          all other nu.                        (6)

This is direct multiplication of (xyZ-1)HE. The two four-dimensional
binary layers overlap only at nu=1^4. In particular every table entry has
fifteen exclusive unshifted copies and fifteen exclusive shifted copies.
They are distinct actual six-dimensional sites, so no cancellation among
these thirty copies has been suppressed. Their contribution gives

    ||Phi_N(H)||_1
      =30 sum_ij |H_ij| + sum_ij |H_(i-1,j-1)-H_ij|,
    mu(Phi_N(H)) >= 15 sum_ij |H_ij|.                (7)

The finite sums in (6)-(7) use zero extension, including boundary indices.
The equality of positive and negative mass follows from (2), or directly
from the zero augmentation of xyZ-1.

Two particular exclusive sites are important. At nu=(0,0,0,0), the
coefficient is -H_ij. At nu=(1,0,0,0), it is +H_ij. Neither is the overlap
site. Both are actual sites in B_N for every table index i,j. Hence the
two opposite signs needed below are present in the original state carrier;
they are not invented slack variables or added readouts.

## 4. A genuine global two-state fiber for every cycle length

For N>=3 take the integer table C=C_N with

    C_(i,i)=+1,
    C_(i,i+1 mod N)=-1,            0<=i<=N-1,
    all other entries zero.                                           (8)

The two entries in a row are distinct. Each column also has one plus and
one minus, so all margins vanish. Its bipartite support is one connected
alternating cycle with 2N edges. The notation mod N only labels the last
column of this finite table: the original chart remains c+Z^6, with no
periodic quotient, torus identification or Native time interpretation.

Let

    h_N=Phi_N(C_N),    f_0=(h_N)_-,    f_1=(h_N)_+,
    M_N=mu(h_N).

These are different finite nonnegative integer states in c+B_N with the
same seven full original readouts and equal mass M_N. Site multiplicities
are allowed to exceed one: this is the original N_0 configuration model,
not a binary matching model. Since C_N has 2N nonzero entries, (7) gives

    M_N >= 30N.                                                       (9)

We now prove that there are NO other states anywhere in the global fiber.
Let g be any finite nonnegative state with O(g)=O(f_0). By (4) it is
supported in c+B_N. By (5), g-f_0=Phi_N(H) for an integer zero-margin
table H. At the unshifted exclusive site with coefficient -H_ij,
nonnegativity of g gives

    0 <= (C_ij)_+ - H_ij.

At the other unshifted exclusive site with coefficient +H_ij, it gives

    0 <= (C_ij)_- + H_ij.

Thus, at every table entry,

    min(0,C_ij) <= H_ij <= max(0,C_ij),   H_ij integer.                (10)

Every entry off the cycle is therefore zero. On the diagonal let
H_(i,i)=eta_i in {0,1}. The zero sum of row i forces its only other
possible entry to be H_(i,i+1 mod N)=-eta_i. The sum of column j now
forces eta_j=eta_(j-1 mod N). Around the connected cycle all eta_i are
equal. Hence either H=0 or H=C_N.

It follows that g=f_0 or g=f_1. No sufficiency assertion about partially
filled central-layer inequalities is needed: the two endpoints already
are actual nonnegative states. We have proved the exact GLOBAL equality

    {g finite N_0 on c+Z^6 : O(g)=O(f_0)} = {f_0,f_1}.                (11)

Every full bin, not merely the fixed-box table margins, is preserved in
this argument. Confinement is the step that rules out an arbitrary-range
detour through other parts of the original chart.

## 5. All finite move-mass bounds fail

Fix any finite D>=0. Choose an integer N>=3 with 30N>D. For the fiber
(11), the only possible nontrivial legal change between its states is
h_N or -h_N. By (9) each has move-mass M_N>D. Neither is in C_D.

Any putative path starting at either endpoint must stay in its original
global fiber, because each step preserves O and nonnegativity. That fiber
has only the two endpoints, so it has no possible first nontrivial step
from C_D. Both endpoints are isolated. This proves (1).

The library in this statement already contains every signed jointkernel
move of mass at most D, not just a prescribed finite palette, translated
templates or moves of bounded spatial range. Increasing the cardinality
or range of that bounded-mass library cannot change the two-state fiber.
The obstruction comes from the necessary mass of its only possible jump.

## 6. Exact scope, old coverage and the bounded research decision

The distinction from the personally accepted old results is in the
quantifiers. The old global C_63 consumer proves connectivity up through
mass 63 and a first failure at 64. It explicitly does not prove a global
all-mass move bound or its failure for EVERY finite D. The old literal
fifteen-cycle/sharp-96 appendix concerns a single 4 by 4 by 3^4 box. Its
exclusive-site and two-state method is relevant, but its fixed-box result
does not imply (1). The new work here pays the arbitrary N table lift,
all original site signs, a growing genuine jump-mass, and confinement of
ALL global intermediates. Those are the additional logical obligations.

The kill conditions were: stop as REUSE if an exact previously frozen
all-D/full-chart theorem is actually supplied; stop as HOLD if only a
bounded-range obstruction or isolated fixed-D examples are available, if
actual-site nonnegativity or confinement fails, or if unbounded jump-mass
is inferred merely from support diameter. The single explicit family
(3),(8)-(11) pays these obligations without enumeration or a parameter
sweep. No all-library novelty or first-discovery claim follows from the
bounded coverage check.

The theorem is NOT a statement that every large mass fails, that M_N is
optimal or has an exact formula, or that any fixed background preserves
this two-state fiber. Adding a common background can create new legal
intermediate states, and no such extension is claimed. We do not classify
all minimal palettes, all primitive moves or the full Graver structure.
The proof also does not assert a globally optimal Markov-degree function.

The carrier remains finite N_0 states on the specified original 6D integer
chart and the full seven original joint readouts. The legal-step graph is
an auxiliary exact comparison relation. There is no physical time, noise
model, new native direction, law, causal mechanism, negative intermediate
state or atomic macro convention. Nothing here repairs missing GEO6 laws,
CM24 lifts, LC/rank4 callers, Parity signed cancellation or any budget STOP.

This is an applied classical integer-cycle/confinement COMPOSE result in
the existing observer family. It is not offered as a new generic Tool or
independent principal-paper unit. Its research value is the precise
global all-D negative answer, not another coefficient/range variant of a
previous fixed-box statement.

## 7. Actual inputs, authorship, warm history and publication boundary

The following two exact old objects had already been genuinely whole-read
and Source-bound by CF before this scope. Their actual old proof/custody
is honestly reused; no fresh old-body API, whole reread or compare is
claimed for preparing this manuscript.

1. CF's old global first-failure consumer, 15999 UTF8 bytes:

       repository awdawmip/enterprise-math
       Source f97e552dcee5987b757cbb7293db9a8ac96c23c4
       research_notes/owner_goal_20261017/native_x6_mass_capped_library_cf1677/
       UNBOUNDED_MASS63_LIBRARY_FIRST_FAILURE64_AUTHOR_V1.md
       SHA256 3f8166c8b559c6b8e0b1790c9c4385eb338cf77bf1a728c6793036c00e43c275
       Git blob f56d627a8c8d9d2ba8b16e1846e2e4ad7a4bf135

   Its true author self-whole/own full Source/exact diff and the complete
   11789-byte 4A true-peer ordinary consumption/own Source binding had
   closed two objects/27788 bytes. Its original creation and temporary
   chat-review history remain unchanged. Only its actual limited scope
   and the old full-readout confinement method are reused here.

2. BFF's literal fixed-box minimality/sharp-mass appendix, 11168 bytes:

       Source 407c056cb34cfb67ee3a864eb8a58cf13a1f22be
       research_notes/owner_goal_20261017/
       native_x6_two_axis_simple_cycle_connectivity_bff6dc/
       TWO_AXIS_LITERAL_PALETTE_MINIMALITY_AND_SHARP_MASS_COMPOSE_APPENDIX_V1.md
       SHA256 30f9e248d5526b7ce04bdc42a1db55cb1eedafd30439e68283889190d1a1d543
       Git blob 3b8ec4a2c158323145770b42a5efb2ac9e7659ed

   CF truly read its whole proof/context, bound its immutable Source and
   exact one-added-path commit, and supplied a separate 14104-byte whole
   technical peer. The author's ordinary full peer consumption/own
   Source binding closed two objects/25272 bytes. BFF retains credit for
   that fixed-box cycle necessity/exclusive-site method; CF's old peer
   role is not new authorship of the BFF appendix. No old vote is moved
   to the present global theorem.

A focused local literal-scope lookup reused these two already held files.
Its rg display was truncated at 3000 output tokens; it is not described
as a new complete whole read. It confirmed the explicit old global-degree
nonclaim and the fixed-box appendix scope. The earlier actual whole
readings, not this keyword lookup, support the old semantic reuse.

Occupation-only messages to A, BFF and 4A supplied no new proof, formula or
repair. Each reported no current occupation or personally held frozen
exact all-D/global-chart result; each personal coverage remains UNKNOWN,
not all-library absence. BFF identified his 20507/12976 long-axis pair as
a fixed-family interval-palette result, not a global theorem. CF has not
whole-read that pair and does not use it as a mathematical premise.

The scope freeze was an actual warm decision at 2026-10-17 08:57:42 UTC.
Selection-stage private reasoning had ALREADY considered an arbitrary-size
zero-margin cycle-table lift, exclusive actual sites and global confinement.
That pre-freeze construction history is NONZERO. This is not blind FREE
Phase A, a new identity, or a zero-construction eligibility declaration.
The present complete author proof was written after that scope freeze.
All original authorship, prior reviewer roles and other warm histories
remain. Sole new responsibility for the arbitrary-N/global-uniform lift
and proof is CF; no other actor supplied its construction or repair.

After this global scope had been selected and its rough proof privately
developed, Root separately routed 4A's finite-torus typed 3-matching
vacancy-barrier whole. At creation of this manuscript CF had received
only that object's scope metadata, exact path and byte pins, and had not
opened its proof body. It is a different matching/reserve-release carrier,
not a premise for this original N_0/full-readout result. The finite cycle
in (8) does not borrow a torus identification or matching exclusion rule.

The same original CF1677 execution remains canonical25/108, with original
LOCAL/composite session, all STOP/HOLD/UNKNOWN and CASUNKNOWN histories,
five false task-ending flags and Goal OPEN. This new after-cut work has
not been recorded by a new checkpoint. No helper26, current main write,
Researcher RA, formal Task, budget reset or Native authority is implied.
Only prose persistence and byte identity are administrative execution;
no mathematical program, enumeration, numeric trial or external query
was used for this proof. A subsequent actual complete author self-read,
byte freeze, independent technical review and any Source publication
must be observed separately. None is prefilled by this creation text.
