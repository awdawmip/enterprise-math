# R5 — Alternating-cycle collapse: unrestricted one-bit Set controllers equal paired-loop covers

Date: 2026-11-16. Frozen science commit: **435e77af0d180eac32bd1f9c4c464bc4010b7551**; this scientific pin has not been rebased. Author-side portable research. Independent review: **NOT_REVIEWED**. This is a genuine source-labelled auxiliary integer repair model; native X6, Heartbeat and BRC promotion are not asserted.

## The previously open mathematical gap

The preceding **R5_RESET_IDEMPOTENT_NORMAL_FORM_THEOREM.md** shows that each internal Set transition of a finite controller can be made idempotent by taking a suitable power without changing output correctness or increasing state count. The preceding **R5_SINGLE_RESET_PAIRED_LOOP_THEOREM.md** proves that internally cross-reset-absorbing controllers have an exact weighted-cover minimum W(k,s). For the nine-node ring, s=2, the previous solver computed a 43-library static optimum and a 44-state paired-loop optimum. The general dynamic minimum had remained 43 or 44.

**New result:** Every unrestricted finite one-bit named Set controller can be converted to a paired-loop controller with no more states. The cross-command residual cannot reduce the optimal state count in this auxiliary model. The reduction works for any finite tail set, output labels and snapshot feasibility relation, not only the cyclic quadratic cost.

## Theorem — General finite one-bit reset collapse

Let T be a finite nonempty set of fixed tails, X=T×{0,1}, and two physical commands R_b(t,c)=(t,b) for b=0,1. Let Y be any set of actual typed output libraries, with a current-output correctness predicate G_b(t,v): library v is feasible for physical state (t,b), including its required source labels and resource budget.

A finite deterministic Moore controller consists of Q, an output o:Q→Y, internal maps f_0,f_1:Q→Q, and a total initialization relation I⊆X×Q. For each physical state x there is at least one initial internal state, and *every* selected (x,q) is output-correct after the empty word and every finite command word. Overlapping beliefs, unused/transient states and arbitrary non-absorbing internal transitions are permitted. Outputs are fixed per Moore state; there is no additional online tail input.

For a pair (a,b) of output libraries define the fixed-tail coverage

P(a,b) = {t∈T : G_0(t,a) and G_1(t,b)}

and cost c(a,b)=1 if a=b, otherwise c(a,b)=2. Let W be the minimum total cost of a family of such pairs whose coverage sets together equal T.

**Claim.** The minimum number N_dyn of internal states in any correct finite deterministic controller satisfies

**N_dyn = W.**

More strongly: from any correct m-state controller one can obtain a correct controller with both reset-absorption identities

δ_b(δ_c(q)) = δ_b(q),  for all q and b,c∈{0,1},

using at most m states, selecting its output libraries from the original controller's existing output labels.

### Proof, part I — individual-power normalization

Set L=lcm(1,...,m), where m≥1, and g_b=f_b^L. Every orbit of a self-map on m elements enters a cycle within m−1 steps, and its cycle length divides L, hence g_b²=g_b. Replace f_b by g_b while keeping Q, I and o. Every word for the new controller is a word for the original in which each command b is repeated L times. Physically R_b^L=R_b. Therefore the original correctness at all finite prefixes establishes correctness of the new controller for every word. This uses the prior proven normalization lemma without assuming cross-absorption.

### Proof, part II — disjoint recurrent projections

On the finite phase-lift Z=Q×{0,1}, define the deterministic alternating map

F(q,b) = (g_(1-b)(q),1-b).

Every directed recurrent cycle C of F contains both phases (the lift alternates phases). Every (q,b) on such a cycle has a predecessor whose incoming transition is g_b, hence q lies in im(g_b)=Fix(g_b) by idempotency.

**Crucial disjointness.** If distinct recurrent cycles shared a Q-state q at the same phase b, determinism would make them the same directed cycle. If they shared q at opposite phases, q would lie in Fix(g_0)∩Fix(g_1), so

F(q,0)=(q,1), and F(q,1)=(q,0).

Both occurrences then belong to the same two-phase cycle. Thus the projections of **distinct recurrent cycles to Q are pairwise disjoint**, even when cycles have more than two phase-labelled vertices.

### Proof, part III — extract a source-feasible weighted cover

For each tail t choose an initial q for (t,0), and apply the infinite alternating command sequence 0,1,0,1,... solely to determine the eventually recurrent cycle C_t of the finite lift. Every visited step is a finite input prefix of the original correctness requirement. At any recurrent (q,b), the physical state is (t,b); thus G_b(t,o(q)) holds.

For each recurrent cycle C that receives at least one such tail, choose one phase-0 vertex (q_0,0) and one phase-1 vertex (q_1,1), and put a_C=o(q_0), b_C=o(q_1). Every tail assigned to C eventually visits every vertex of C, so is covered by P(a_C,b_C). Together these pairs cover all T.

Let V_C be the set of distinct Q-states appearing in C. If a_C=b_C, the pair costs one. If the labels differ, the fixed Moore output implies q_0≠q_1, so |V_C|≥2 and the pair costs two. Hence in both cases c(a_C,b_C)≤|V_C|. By disjointness from part II,

W ≤ Σ_C c(a_C,b_C) ≤ Σ_C |V_C| ≤ |Q|=m.

Only individual finite-prefix correctness was used; the infinite alternating sequence is a finite-state cycle-selection device, not a claim about physical-time convergence.

### Proof, part IV — constructive converse

Take a minimum weighted cover. For each (a,b), construct one internal state with output a if a=b; otherwise construct two states with outputs a and b. In either case define command c to send every state in that component to its designated c-state. Initialize (t,c) in a component whose pair covers t, at its c-state. The physical tail never changes; both selected source outputs remain feasible for that tail after any command. These components satisfy both cross-reset absorption identities, use exactly the chosen weight, and together initialize every raw state. Thus N_dyn≤W. Combined with part III gives N_dyn=W. □

## Frozen cycle-of-triangles specialization

For k≥3, take tails t∈{0,...,2^(k−1)−1}, raw mask u=2t+b, and an admissible nonnegative integer slack s. The inherited canonical genuine-source library L(r) serves u exactly when

u AND NOT r = 0,  and  0 ≤ q_k(r)−q_k(u) ≤ s,

where q_k(u)=Σ_(i modulo k) u_i u_(i+1), with bit indices modulo k.

The inherited common-source canonicalization theorem replaces any output source library serving a collection of raw states by a genuine source centre of no greater cost serving that collection. Therefore the general weighted cover W is exactly the previously defined canonical pair-cover optimum W(k,s). Consequently

**N_dyn(k,{0},s) = N_reset-coherent(k,{0},s) = W(k,s)**

for all k≥3 and admissible s, under the exact source-cost and common-source assumptions. This is a symbolic theorem for arbitrary k; it does not depend on a numerical solver.

For k=9,s=2 the previously stored source-labelled 44-state witness gives an integer-checked upper bound. The previous HiGHS integer program reports W(9,2)=44 as an optimal zero-gap solution using 221 nondominated weighted candidates. The equality above transfers **that same solver-dependent finite numerical lower-bound status** to N_dyn(9,{0},2)=44. An independently exported exact integer lower certificate is still wanted; the new mathematical theorem is independent of solver correctness.

## Finite exact reproduction

Companion source **VERIFY_R5_ONE_BIT_CYCLE_COLLAPSE.js** runs using Node's standard library. It checks all 66,282 ordered pairs of arbitrary internal self-maps on m=1,2,3,4 labels, their power normalization and recurrent-cycle disjointness (99,214 cycles). A four-phase recurrent cycle occurs: the proof does not silently reduce arbitrary recurrent dynamics to only two vertices.

It separately checks the inherited k=9 genuine-source 44-state witness over all 256 tails/512 masks, 65,024 finite word cases and 328,704 exact transition checks. It tests an 88-state nonidempotent doubled controller and extracts cycles after powering its resets. Evidence is stored in **EXACT_R5_ONE_BIT_CYCLE_COLLAPSE_EVIDENCE.json**. The universal theorem is the four-part proof above; these tests are finite cross-checks, not a replacement for proof. No new MILP solver optimum was computed in this turn.

## Source, control boundary, next questions

Inherited theorem/source paths:
- research_notes/portable_direct/r5_single_reset_pair_loop_20261116/R5_SINGLE_RESET_PAIRED_LOOP_THEOREM.md @ fdca33bd777759d4162a71e8f9cc920fd1b70281
- research_notes/portable_direct/r5_reset_idempotent_normal_form_20261116/R5_RESET_IDEMPOTENT_NORMAL_FORM_THEOREM.md @ 3147b4ee67ac2a2ba8069fa6a84ff101c71784ea

Historical author provenance: EM-DIRECT-B78E55, RA-33C87C2B703418F0706695E9, MCP-c57574161f4a48c5920fddd2ea07a141. These references do not assert a current Task, CLAIM, Result or independent review. P000 and ACTIVE worldview remain unchanged, and transfer to native X6/BRC would require an explicit typed structure-preserving bridge.

Next: (1) find an independently checkable integer lower-bound certificate for the inherited 221-candidate W(9,2)≥44 instance; (2) investigate multi-coordinate named Set, where alternating cycle projections may overlap and the one-bit disjointness proof must be reconsidered.