# R762AC — Two-slot hub theorem for a source-typed P000 triadic port-exchange candidate

Date: 2026-11-14 (Asia/Shanghai). Scientific status: **AUTHOR-SIDE CONDITIONAL CONSTRUCTION / PROVED STAR-MODEL THEOREMS / EXACT FINITE VERIFICATION / NOT_REVIEWED / NOT_ADMITTED**.

Parent task: RS-X6-TRIADIC-CLOSURE-DYNAMICS, publication TP2-8B7E13C5904A2D6F1142.
Provenance: Researcher EM-X6-3050F6, Activity RA-6068F717D991DF54FBBDDEED, pre-existing successful native CLAIM MCP-e4b33a56e2686c66e7cd5ca2 / RUN-53ab7d7bffccaaf2c0af47a4. The current native resume action was blocked by the tool safety boundary. This GitHub author-side note is not a native checkpoint or formal Result.

Frozen scientific input: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389. Reuses signed X6 Cell torsor; conditional V17 active-triad frame transport; V29 nonnegative PASS/TRANSFER ledger; V39 (j,h) based-loop observer. Prior R762V and R762AB remain at their exact original scope.

## 1. Explicit P000-compatible local candidate

Let c be any chosen native X6 Cell. Choose three distinct underlying native axes a,b,d from six and signs sigma_i in {+1,-1}. Put p_i=c+sigma_i e_i. The only spatial moves allowed in this candidate are one signed primitive X6 axis step p_i -> c or c -> p_i. Three *individually labelled* equal, nonzero force quanta occupy p_a,p_b,p_d with distinct source identities and are declared incident to c via their three signed spokes.

At each **completed macro boundary**, all three equally weighted, distinct-axis quanta are present. The equal-quantum three-force closure is P000's canonical primitive balance premise. During elementary transfers, partial populations are transient and are not asserted to be stable. The ability to store a quantum at c and the move-enabling rule are **new explicit candidate conditions** requiring native admission; neither follows from P000 alone.

Each outer port holds at most one quantum. The central Cell c has buffer capacity B. The hub starts empty; there is no external spare port and no simultaneous exchange. In a generalized star with n outer ports, a labelled source i must end at port pi(i), where pi is a prescribed permutation. For a signed distinct-axis X6 star n<=6.

## 2. Theorem AC1: exact minimal hub capacity and transfer number

For every n>=2 and every nonidentity permutation pi of individually labelled tokens on fully occupied outer ports, a legal one-spoke realization exists **if and only if B>=2**. If m tokens must change ports, the minimum number of primitive spoke transfers is exactly 2m.

**Necessity of two slots.** With B=0 no move exists. With B=1, the first incoming token creates a vacancy only at its own original port. Every other outer port is occupied. The sole hub token can exit only back to its original port, restoring the original configuration. By induction no completed series of single moves changes any source attachment. Thus B>=2 for a nonidentity pi.

**Transfer lower bound.** Every moved token must enter the central Cell at least once and later exit it at least once. Hence >=2m transfers.

**Attainment.** Decompose pi into disjoint nontrivial cycles. For a cycle (1 2 ... r), source i must go to port i+1 modulo r. Pull sources 1 and 2 into c; send source 1 to port 2. Then for i=3,...,r pull source i into c and send source i-1 to port i. Finally send source r to port 1. Every destination is vacant when used; hub occupancy never exceeds two. The cycle consumes exactly r arrivals plus r departures, and cycles can be processed serially. This realizes 2m transfers. QED.

**Three-port consequence.** A clockwise or anticlockwise three-source port cycle needs exactly six native signed-axis steps and a central buffer of size two in this model. The construction respects each of the 20 underlying three-axis choices and eight sign configurations, giving 160 sign-typed X6 instances without imposing Euclidean vector addition.

## 3. Theorem AC2: exact shortest chronological BRC multiplicity

For a single oriented n-cycle, n>=2, and hub capacity B=2, the number of distinct *labelled shortest transfer serializations* is

\[
N_{\rm min}(n)=n\,2^{n-1}.
\]

**Proof.** For n=2, the two arriving tokens can arrive in either order and depart in either order: four traces. For n>=3, every shortest realization has one ingress and one egress per token. The first two operations must be arrivals from adjacent vertices of the directed target cycle: with a nonadjacent pair, neither token in the full hub has a vacant target and no shortest continuation exists. There are n adjacent pairs and two arrival orders, or 2n possibilities. The first egress is forced. The remaining not-yet-arrived sources occupy a contiguous segment of the cycle, and the next arrival can be selected from either end at each of the next n-3 stages; the corresponding egress is forced. After the final arrival, the two remaining tokens in the hub have distinct vacant destination ports; their two departure operations commute and have two orders. Thus 2n times 2^(n-3) times 2 equals n*2^(n-1). QED.

In particular n=3 yields **12 distinct shortest six-transfer schedules per fixed cyclic source permutation**. This is positive, labelled Path/BRC multiplicity under the stated microstep model, not an assertion of 12 independently admitted physical force events.

## 4. Exact V29 boundary-only lift and V17/V39 observer residual

Give each outer Cell a named spoke port and the central Cell three corresponding ports. Every primitive spatial move is recorded as exactly one V29 matched inter-Cell TRANSFER. This is a valid **boundary-only transfer-lift** with M=0 and no internal PASS counters. Each complete three-port permutation sends one token inward and one token outward along every spoke. Therefore the final nonnegative R_in and R_out ledgers, local contrast u, and antisymmetric Omega coincide for clockwise and anticlockwise three-cycles: u=0 and Omega=0 at all Cells. The global scalar Q is conserved after every TRANSFER. Every star edge is traversed once each way, so the based net integer transfer current is j=0.

Keep the **active triad support and V17 internal frame fixed**, with no active-triad replacement steps in this local source-exchange macro. Its conditional V17 transport is h=id. Thus for both three-cycles, the V39 observation is (j,h)=(0,id), although their labelled source permutations differ:

- clockwise: source a goes to port b; source b to d; source d to a;
- anticlockwise: source a goes to d; source d to b; source b to a.

The full boundary-only V29 count ledger and the V39 signature cannot distinguish these *source-to-port maps*. A future source-sensitive query such as "which source is at port a?" can. This is a concrete operation-safe observer-loss witness. For source-sensitive future languages, the source permutation P (or an exact sufficient quotient for the allowed updates) must be retained in addition to (j,h). It is **not** V17 frame holonomy, which is identity here.

For any k>=1 completed macro cycles, with independently chosen clockwise/anticlockwise orientation on each, every spoke has k incoming and k outgoing boundary TRANSFERs, and (j,h) remains (0,id). But the final source permutation is P_+^r with r=(#clockwise-#anticlockwise) mod 3. At fixed k=1 there are 2 possible residues; at every fixed k>=2 there are exactly 3. A **two-bit repair** is information-theoretically sufficient and necessary for the full source permutation over these fixed-k>=2 families. A known, single fixed orientation and event count need no additional repair.

Posting an internal PASS(c;i->pi(i)) for each completed hub traversal would yield a directed M that distinguishes the two orientations. Such an attachment is a **separate possible V29 coupling law**, not a deduction that every two-TRANSFER journey must be double-entered as an internal PASS. The true native event attachment remains the outstanding admission question.

## 5. Exact verification and open native interface

Companion executable: research_notes/R762AC_STAR_BUFFER_VERIFY.py. Evidence: research_notes/R762AC_STAR_BUFFER_EVIDENCE.json.

The independent standard-library BFS exhausts all reachable placements of individually labelled tokens on n unit-capacity outer ports plus a central hub, for n=2,...,6 and B in {1,2}, checking distances and counts. It obtains (n,min transfers,shortest schedules) = (2,4,4), (3,6,12), (4,8,32), (5,10,80), (6,12,192), and no nontrivial cycles for B=1. It checks the explicit two-buffer construction and the 160 signed three-port X6 assignments, and enumerates cyclic source residue classes at k=1,...,6. All arithmetic uses exact integers and tuples. Universal theorems rest on their separate combinatorial proofs.

This creates an explicit P000-compatible, *conditional* Cell/Link/Port construction with source provenance, occupancy-dependent legality, exact repeatable macro boundaries, a sharp capacity threshold, and a V29/V17/V39 observer-loss mechanism.

The remaining task-level obligations are to check whether the real TRIADIC_CLOSURE_E allows this hub incidence and transient occupancy, whether a physical passage must generate a paired internal PASS as well as boundary TRANSFERs, and how nontrivial active-triad changes couple to V17/V39 holonomy. Preserve the original P000 and task frozen pins.

## 6. Publication and control boundary

This note, checker and evidence are author-side GitHub artifacts; they are not a native Run checkpoint, formal Result, independent review, or Working Truth. The original owner CLAIM was previously verified successful, but an attempted native execution_resume in this invocation was blocked by the tool safety boundary. No rejected mutation was replayed or replaced by a Drive write. Native Source progress may be performed only by the genuinely authorized original session, after canonical reauthorization.
