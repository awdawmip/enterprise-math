# Collision mass, exact row sharing, and implicit Gram continuation

Status: AUTHOR_SYMBOLIC_ANALYSIS / SHARED_CONTEXT / UNREVIEWED /
NOT_ADMITTED. This unit contains algebraic derivations and explicit test
specifications, not a new numerical reference, scientific run, or independent
admission. The parent owns current activity/source registration and external
persistence. Researcher EM-DIRECT-C6438C and the existing shared scientific
constraints are retained; P000 is unchanged.

The derivation starts from the actual native branch identity proved in
`sep26-shor-alternative/math_route/STREAMING_SHOR_PROOF.md`, section 6,
and implemented by `algorithm_intake/terminal_instrument.py`. The phase
objects are complete, actually certified native words. No ideal QFT, hidden
order, known factor, deletion of residuals, or branch renormalization is
inserted. A symbol r used below is an analysis quantity, not an algorithm
argument.

## 1. The exact branch mass needs only collisions

At a round boundary the active control and shared spectator are zero. Write
the unnormalized state as

    v = sum_(w in S) |w> tensor (n_w/d),

where every n_w is the complete nonzero integer row in R^61, d>0 is a common
denominator, and missing labels denote zero rows. Let P be the current
certified modular permutation, and let T=A/h be the current full-carrier
feedback word: A is integral, h>0, and A^T A=h^2 I. Its temporal phase order
is exactly the old ascending control-index loop. Different phase words need
not commute. Work transport and a label-independent internal T commute with
each other; this is distinct from assuming that different T factors commute.

The two actual native H4 operations and intermediate gates have the inherited
macro identity

    v_sigma = (v + sigma (P tensor T)v)/2,  sigma=+1,-1.   (1)

The spectator returns by this identity, not by a reset. Define integers

    M = sum_(w in S) n_w^T n_w,
    G = sum_(w in S, P(w) in S) n_(P(w))^T A n_w.        (2)

All 61 coordinates, including signed residuals, enter these dot products.
Expanding (1), using orthogonality and the bijectivity of P, gives

    mass(parent) = M/d^2,
    mass(child_sigma) = (hM + sigma G)/(2h d^2),
    Pr(0 | history) = (hM+G)/(2hM),                      (3)
    Pr(1 | history) = (hM-G)/(2hM).

For M>0, Cauchy--Schwarz proves |G|<=hM, so these are valid probabilities
and sum to one. A zero parent is a separate empty branch, never a division.
Taking |G|, discarding negative cross terms, or ignoring complement modes
would change the conditional law.

After selecting sigma, its exact integer state can be constructed as

    u_z = h n_z + sigma sum_(w:P(w)=z) A n_w,
    d_child = 2hd,       z in S union P(S),               (4)

followed by the frozen exact common-factor reduction. Because P is a
permutation, the sum has at most one source. Neither its inverse table nor
the order r is needed: push each source row to its actually observed P(w).
Only identically zero full rows may be removed. This is not normalization
by the child mass.

**Immediately checkable optimization.** During the mass pass, apply the
actual feedback T only to source rows whose P(w) also lies in S. Noncollision
rows contribute exactly zero to G. Their feedback can be postponed until
the selected child is materialized. Parent mass M is obtained without T;
complete orthogonality accounts for the other quadratic term in (1).
The selected materialization then fills all missing transformed rows.

The inherited conditional-uniform random-source contract is unchanged.
If drawing the next bit is interrupted, preserve the raw parent and prefix;
there is no selected child to commit or discard.

## 2. Complete row sharing helps arithmetic, but counts alone lose geometry

Let q be the number of distinct complete integer row tuples among S, all
over the same denominator. Feedback results A n_w may be cached by the
whole tuple. Let q_c be the number of such tuples at collision sources.
Then the mass pass requires at most q_c distinct feedback applications,
and the full selected child at most q, rather than one per source label.
This is an exact, measurable optimization criterion when q is small.

If a common row dictionary contains x_1,...,x_q, let c_j count labels carrying
x_j, and let c_ij count sources w carrying x_j whose P(w) carries x_i.
Then

    M = sum_j c_j ||x_j||^2,
    G = sum_ij c_ij x_i^T A x_j.                         (5)

Thus row multiplicities plus the correct directed collision table suffice
for this one mass query. The collision table is additional information:
the row histogram alone does not determine it. A tuple cache may reduce
61-dimensional arithmetic and duplicate row storage while the map from work
labels to tuple IDs still has |S| entries. Rank<=61 of the matrix of rows is
also not, by itself, a compressed description of that label map.

### Explicit residual-bearing counterexample to histogram-only sampling

Take N=15, P(w)=2w mod 15 on the unit labels, T=I_61, d=2, and
u=e_0+e_5. Consider the two valid normalized states

    state A: n_1=u, n_2=u;
    state B: n_1=u, n_4=u.

Both have the same two-row histogram, M=4, and mass one. For state A,
P({1,2})={2,4}, so G=2 and Pr(0)=3/4. For state B,
P({1,4})={2,8}, so G=0 and Pr(0)=1/2. Coordinate 5 is a retained residual
coordinate. Replacing it with coordinate 17 gives the same counterexample
in the arbitrary-input 61-mode contract, but lies outside the new reachable
six-mode codec and must be rejected by that codec.

These exact values are a test specification derived from (2)-(3), not a
claim that this document ran them. A conforming optimization must retain
the label collision relation and distinguish the two probabilities.

## 3. Simple probabilities can coexist with doubling support

If S and P(S) are disjoint, G=0 and both conditional probabilities are 1/2.
Nevertheless, since T is invertible and every row in S is nonzero, (4) has
exactly 2|S| nonzero rows for either outcome. There is no cancellation across
distinct labels. Therefore collision-free rounds are cheap mass queries
but expensive explicit-state expansions. Probability simplicity is not a
bound on explicit state size.

This gives a stronger exact statement for the inherited Shor schedule.
Let the analysis-only order of a modulo N be r. The first i processed
modular exponents are 2^(t-1),...,2^(t-i), so the possible work labels are

    a^[2^(t-i) j] mod N,       0<=j<2^i.                 (6)

They are all distinct if and only if

    r / gcd(r,2^(t-i)) >= 2^i.                           (7)

Indeed, equality of two labels is equivalent to r dividing
2^(t-i)(j-k); the least positive possible difference producing equality is
r/gcd(r,2^(t-i)). Before the first collision, each subset of preparation
choices contributes to a different work label. Its internal coefficient is
2^(-i) times a signed product of the actual orthogonal feedback words applied
to e_0. It is nonzero and has norm 2^(-i), regardless of the measured history.
Consequently, whenever (7) holds:

    every history has exactly 2^i work rows after i rounds,
    its unconditional mass is 2^(-i),
    every preceding conditional bit probability is 1/2.  (8)

Write r=2^s d with d odd. At the default t=2ceil(log2 N), set
i=floor(log2 d). Since r<N, t-i>=s; hence (7) holds. For d>1 this yields
at least 2^floor(log2 d)>d/2 nonzero work rows along every explicit trajectory.
No choice of certified orthogonal internal phases removes this initial
growth. When d=1 the statement is only the trivial i=0 bound; no stronger
claim about pure power-of-two orders is inferred.

This is a lower bound for the current explicit work-row representation,
not an impossibility theorem for all classical samplers or implicit
representations. In particular, a lazy representation may defer these
collision-free expansions. The algorithm need not know r to exploit a
round: S intersect P(S)=empty is a direct finite check on already available
labels. The r-based condition is used only to explain the scope of growth.

## 4. A sufficient exact class-compression theorem, and its limitation

Suppose a work-label domain has a certified partition C_1,...,C_q with known
cardinalities m_j, the current full row is constant x_j on C_j, and each
future P_i maps every C_j bijectively onto some C_(pi_i(j)). Suppose also
that these class actions, sizes and initial rows have exact certificates
that do not first enumerate the full domain. Then the class update

    x'_j = (x_j + sigma T_i x_(pi_i^-1(j)))/2             (9)

and mass sum_j m_j ||x'_j||^2 reproduce the complete labelled dynamics.
Proof: all labels in a destination class have a preimage in the same source
class, so their full updated rows are equal. Induction preserves this property.
All internal signs and residual coordinates remain in x'_j.

This is genuine quantity compression if q and its certificates are much
smaller than the occupied label count. Merely declaring a partition, or
enumerating all its labels first, does not establish a resource improvement.
The exact action property is a checkable sufficient condition, not a necessary
condition for every possible compressed representation.

There is an immediate obstruction for a fixed globally invariant partition
on the starting a-orbit. Initially |work=1> tensor e_0 forces the class
containing 1 to be a singleton. If multiplication by a permutes the classes,
its successive images {a^j} are all singleton classes. Thus q>=r. The complete
Shor schedule includes multiplication by a, so this simple fixed block-class
strategy cannot compress that initial orbit below r classes. Dynamic classes,
symbolic expressions, or more general invariant modules are not ruled out.

## 5. An exact implicit Gram recurrence that avoids immediate expansion

For a fixed measured prefix i, let v_(i,w) denote the complete unnormalized
real row (including its denominator). Define a D by D matrix for every
integer shift z, with D=61 or a separately certified reachable encoding,

    Gamma_i(z) = sum_w v_(i,w) v_(i,a^z w)^T.             (10)

The sum is over the work orbit, with zero extension. The definition for a
negative z is a proof object; an executor need not compute an inverse since

    Gamma_i(-z) = Gamma_i(z)^T.                          (11)

If the next actual modular exponent is b=2^(t-1-i), its feedback is T_i,
and its selected sign is sigma, expansion of (1) and a change of work index
give the exact recurrence

    Gamma_(i+1)(z) = 1/4 [ Gamma_i(z)
      + sigma Gamma_i(z-b) T_i^T
      + sigma T_i Gamma_i(z+b)
      + T_i Gamma_i(z) T_i^T ].                          (12)

There is no commutation assumption on different feedback words. The only
group fact is that the actual work permutations are powers of the same
modular multiplication. The required mass and cross term are

    m_i = trace Gamma_i(0),
    g_i = trace(T_i Gamma_i(b)),
    Pr(0 | prefix) = (m_i+g_i)/(2m_i).                   (13)

At the initial state,

    Gamma_0(z) = e_0 e_0^T  if a^z = 1 mod N,
                 0         otherwise.                  (14)

The test in (14) is equality of an explicitly requested modular power to one.
It does not receive or assume the unknown least order. For negative shifts
use (11) first. For nonnegative shifts, two queries with the same actually
verified residue a^z mod N have identical Gamma_i and can be memoized under
the same key (i,residue). Computing those residues must use the authorized
exact modular arithmetic path if this design is implemented scientifically.

Equations (10)-(14) give an alternative mass-query representation. A lazy
state DAG may retain the successive actual operators and selected signs,
sharing its previous node instead of expanding all work labels. If later
requested, it still denotes the complete state (1); correlations are exact
observers, not a replacement ideal dynamics or a projection of residuals.
For the existing control-only readout followed by CF/gcd, the recursively
computed conditional probabilities are sufficient. If a caller additionally
requests a terminal work label or the full state, that output needs its own
query/expansion procedure and costs; it is not obtained for free.

### Conditional, checkable resource statement

Let J be the number of distinct memoized (level,residue) queries visited
while evaluating (13) along a chosen history. Each instance of (12) needs
at most three prior queries and a bounded number of D by D rational matrix
operations using the actual T_i coefficients. Given polynomial bit bounds,
polynomial-cost modular residue queries, and J polynomial in t and log N,
this exact mass evaluator has polynomial cost at fixed D. All three premises
are explicit; the new missing premise is a uniform polynomial bound on J.

The recurrence supplies no such general bound on its own. It can generate
many shifts and distinct residues; memoization has only the coarse orbit
ceiling O(t r), and evaluating a compact expression's norm can be much more
expensive than storing that expression. An implementation should expose J,
its cache size and exact arithmetic bit sizes, use a declared finite budget,
and return a resumable incomplete query if that budget is exhausted. An
exponentially growing query set must not be called polynomial compression.

This direction is a concrete next representation to test, with the exact
recurrence and scalar observables fixed before any run. This document does
not implement or execute the Gram evaluator, and does not assert it solves
the worst-case collision problem.

A future scientific implementation must bind each multiplication by T_i to
the actual complete native-word action (for example columnwise, with the
transpose action implemented by its certified inverse) and each signed
correlation/trace combination to an authorized exact observer. Merely
evaluating (12) with ordinary reference matrices and attaching a BRC label
would not discharge that execution obligation. The matrices in this section
are exact derived correlation objects, not an ideal dynamics substituted
for the native word.

## 6. Reachable internal encoding is compatible, but is a different saving

The parent's direct-word carrier codec checks actual complete 61-column
actions for W=W_6 direct-sum I_55, with zero cross blocks, and encodes only
states certified to have zero tail outside coordinates 0,...,5. For the
four-square construction this follows symbolically from its normal being
supported there and W=D0(2zz^T-I); exact m2 preserves the same subspace.
External H4 control/spectator steps and modular work transport do not mix
these internal coordinates. Induction therefore permits exact word-boundary
embedding of the reachable six-coordinate state into all 61 coordinates.

This is a certified reachable-subspace encoding. It does not delete a
nonzero residual: coordinates 2,...,5 remain; an arbitrary input with a
nonzero tail must be rejected or handled through the full carrier. Nor may
an executor truncate coordinates inside an indexed/canonical native word,
whose routing can temporarily occupy them. Only the verified complete-word
boundary action has the invariant. No common-root or cross-phase commuting
identity is required.

The codec changes the constant D in row/Gram arithmetic, not the work-label
count in (6)-(8). These are computational labels, not six spatial axes or
a derivation of physical dimension. P000 is unchanged.

## 7. What counts as progress beyond scheduling constants

- Selected-child materialization removes the discarded child's allocation;
  collision-only mass evaluation and complete-row caches reduce repeated
  transformations. They preserve explicit label support and therefore do
  not defeat the growth result (8).
- The exact reachable codec reduces a proven internal constant from 61 to
  six at word boundaries. It does not compress the modular orbit.
- A certified small class action as in (9), or a demonstrated small exact
  Gram query closure as in (12), can reduce quantities that grow with the
  number of work labels. Their verification and construction costs must be
  included.
- The earlier Stage92 scheduling/operation-constant savings do not, without
  such an additional representation theorem, imply work-support compression.
  Reordering phases on an unproved common-root/commutation premise is not an
  allowed shortcut here.

The next bounded checks can compare (3) with both complete actual children,
compare only-materialized selected states after exact common reduction, and
exercise the explicit residual-bearing histogram counterexample. Those
checks belong to the implementing agents and must retain their own actual
receipts. This author's symbolic derivation does not relabel their future
or previously saved outputs as its own execution.

Global-Knowledge-Sync: main@61e00d2a2a3ab41f3ec43990385f46e8a7806d41 / GLOBAL_KNOWLEDGE_V1
