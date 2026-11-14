# R762AR — Exact chronological token-deficit BRC residual and periodic replay criterion

**Status:** AUTHOR-PROVED CONDITIONAL; exact finite cross-check; NOT_REVIEWED / NOT_NATIVE_ADMITTED.
**Task:** RS-X6-TRIADIC-CLOSURE-DYNAMICS; publication TP2-8B7E13C5904A2D6F1142.
**Author provenance:** EM-X6-3050F6, original SID MCP-4b2d70a97f594366a7c94a0f8b45df38.
**Frozen scientific input:** awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389.
**Predecessors:** R762U (conditional causal-token V29 lift, PR #2347), R762V (signed X6 path BRC, PR #2351), R762AQ (auxiliary adaptive reset, PR #2432).

## Model and precise theorem

Let V be a finite set of **typed Cell:Port vertices**. A chronological event word
w=((a_1,b_1),...,(a_m,b_m)) consists of individually identified V29-like PASS or TRANSFER
occurrences; a_i,b_i are directed endpoints in V, and loops a_i=b_i are allowed.
Each event is enabled only when at least one integer token is at its tail; its
execution moves one token to its head. Token inventories are nonnegative integers.
This is the explicit **conditional causal-token lift** introduced in R762U,
not a physical force admissibility law. Event IDs and ordering remain in the source
word; inventory tokens are indistinguishable for the present observer.

For v in V, define the prefix net demand

D_w(v,k) = # outgoing occurrences at v among i<=k
          - # incoming occurrences at v among i<=k,   D_w(v,0)=0,

the final net demand Delta_w(v)=D_w(v,m), and the **pre-fire peak demand**

H_w(v)=max( {0} union {D_w(v,i-1)+1 : 1<=i<=m, a_i=v} ).

The +1 at the firing boundary is essential for self-loops.

**Theorem AR1 (sharp chronological seed).** For every nonnegative integer
inventory n:V->N, the entire ordered word w executes iff
n(v)>=H_w(v) for every v. Upon successful execution the final inventory
is n(v)-Delta_w(v). Consequently the unique componentwise least starting
inventory is H_w, and the least total starting stock is sum_v H_w(v).

*Proof.* Before event i, the inventory at v is n(v)-D_w(v,i-1).
Firing at tail a_i requires n(a_i)-D_w(a_i,i-1)>=1, i.e.
n(a_i)>=D_w(a_i,i-1)+1. These are precisely the inequalities defining H_w.
They are simultaneously necessary and sufficient for every sequential firing.
Inventory conservation at each move gives the terminal formula. The lower bound
is attained by n=H_w, so it is sharp. This argument also covers a_i=b_i. QED.

**Theorem AR2 (ordered BRC composition and minimal observer).**
On pairs (Delta,H) define

(Delta,H) * (Delta',H') =
(Delta+Delta', max(H,Delta+H')),

with componentwise maximum. The ordered event word map
R(w)=(Delta_w,H_w) is a monoid homomorphism from concatenation to this
associative monoid; the empty word has residual (0,0).

Furthermore, for the declared observer that, for every initial inventory n,
returns either FAILURE or SUCCESS together with the final full inventory,
two words have identical input-output behavior for all n **iff** their
(Delta,H) pairs agree. Thus R is the exact minimal future-sufficient
equivalence-class label for this input-output interface (although the pair
itself need not be the smallest bit encoding of that label).

*Proof.* A suffix v begins after u with inventory n-Delta_u. It is executable
iff n>=Delta_u+H_v, while u requires n>=H_u. This proves the product law,
and associativity follows either from concatenation or by direct max-plus
calculation. Equality of residuals plainly implies identical behavior. If
the Delta vectors differ, choose n dominating both H vectors: both words
succeed but their terminal inventories differ. If Delta is equal but H
differs at a port p, choose all other initial ports sufficiently large and
n(p) between the two integer thresholds: feasibility differs. Hence distinct
residuals can be distinguished. QED.

**Theorem AR3 (exact r-fold replay and indefinitely repeatable schedule).**
For every integer r>=1,

Delta_(w^r) = r Delta_w,
H_(w^r)(v) = H_w(v) + (r-1) max(0,Delta_w(v)).

The exact least total seed stock for r prescribed consecutive copies is

K_r(w)=sum_v H_w(v)+(r-1) sum_v max(0,Delta_w(v)).

A fixed finite starting inventory permits arbitrarily many repeats of this
unchanged word iff Delta_w(v)=0 for every v. For nonzero Delta, the required
seed grows linearly, with exact positive slope sum_v max(0,Delta_w(v)).

*Proof.* Apply AR2 to the r prefixes; for each port, the peak is the maximum
of H_w(v)+j Delta_w(v), j=0,...,r-1, giving the displayed formula.
Every move conserves total token count, so sum_v Delta_w(v)=0.
If Delta is nonzero, at least one component is positive and its minimum
seed diverges with r; if Delta=0, H_(w^r)=H_w for all r. QED.

## Source-sensitive witnesses and V29 replay

For distinct ports A,B, compare the two ordered four-event words

w_grouped = (A->B)(A->B)(B->A)(B->A),
w_alternating = (A->B)(B->A)(A->B)(B->A).

Both have the same directed edge multiset and Delta=0. Yet their H_A values
are 2 and 1 respectively, so their sharp seeds differ permanently for
every r>=1. The count ledger and total mass alone are not sufficient for
the chronological availability observer.

For a self-loop w=(A->A), Delta=0 while H_A=1. This shows why only tracking
post-event prefix divergence would incorrectly predict execution from zero stock.

Reusing the **specified 22-occurrence schedule** of R762U: three A-port
PASSs forming A0->A1->A2->A0, nine A-to-B outbound TRANSFERs with
multiplicities (2,4,3), and ten B0->A3 transfers. For the original
network, where the nine outbound transfers arrive at B1, the calculated
H sum is 19 and positive Delta sum is 19: K_r=19r.
For R762U's *different network* with all nine transfers arriving at B0,
the same ordered schedule has H sum 10 and positive Delta sum 10:
K_r=10r. In both cases K_4 is 76 and 40 respectively.
These figures preserve the two distinct topologies and agree at r=1
with R762U's optimal inventory theorem. They are not native force closures.

## Verification and BRC information boundary

The standard-library Python checker independently enumerates every ordered
word of lengths 1 through 6 on three labeled vertices with all nine directed
edge choices, including loops: 597,870 words in total. For each of the
four repetition factors r=1,2,3,4, it verifies the exact replay formula,
minimal-stock replay success, each one-token-at-one-port sharp failure, and
the terminal inventory. It also verifies every split composition for
lengths 1 through 5 and the two historical network examples.
Integer operations only; no floating point, trigonometry or untyped phase
propagation. Finite exhaustive checks support the independent general proofs.

R(w) is an **ordered, source-port-typed BRC feasibility residual**.
Its observer intentionally forgets individual event IDs and path ordering
after extracting Delta and H: such erasure is safe only for this exact
token-feasibility/terminal-inventory interface and its serial composition.
Signed force, native triad closure, V17 activity frame and V39 holonomy are
not thereby erased or reconstructed. No claim is made that R(w) is the
minimum sufficient state for full P000 dynamics.

## Next question

On an actually admitted TRIADIC_CLOSURE_E macro-event, establish whether
multiple V29 PASS/TRANSFER occurrences are atomic or sequential and
whether the allowed restart preserves a common Cell/Link/Port token state.
If the event admits a causal-token simulation, use its true ordered
subevent word to calculate Delta,H and test AR3 against repeated native
legality. A native force closure predicate, source and frame transport, and
V39 based-loop observer must still be supplied before native admission.
