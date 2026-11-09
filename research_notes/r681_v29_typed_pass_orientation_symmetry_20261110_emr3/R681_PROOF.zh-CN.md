# R681｜V29 三元 PASS 的类型化旋转闭包与曲率—未来记忆代价

Date: 2026-11-10 Asia/Shanghai  
Task: RS-X6-GLOBAL-TRIADIC-FIELD-NETWORK-LAW / TP2-47D65B35A7D48082EFBB  
Frozen scientific input: R462@18783e01e3646c72b7aab3b16d3f565e83e6446f  
Predecessors: R675@7beceb012a43d6c7c0ad005d8793bc96f4a38383; R679@fab76ba01a87745b098ab57a0219d958707bdbb9; R680@63857b98f4069ff31158bdcb4b5db5c9577fa63f  
Status: AUTHOR-SIDE PROOF AND EXACT FINITE VALIDATION; INDEPENDENT DRIVER REVIEW PENDING.

## Model and exact question

Use the original frozen V29 update law at one shared X6 Cell with four typed internal ports, observing the three-port subalphabet 0,1,2 (port 3 remains in the complete state). V29 PASS(a→b) increments nonnegative M[a,b] by 1. Derived contrasts are Ω=M−Mᵀ and u=Ω1+Rin−Rout; PASS preserves the cell scalar sum of u and global network Q. We keep the R675 typed port action σ=(0 2), fixing ports 1,3. The X6 six native axes and time-order remain separate types. The R679 oriented PASS batch is F={A:0→1,B:1→2,C:2→0}. This is an exact local event-algebra study; the once-only scheduler used below is an explicitly declared auxiliary restriction.

Question: What is the smallest atomic PASS event alphabet closed under σ, how does signed three-port circulation transform, and how many states does a named future observer need?

## Theorem A: smallest equivariant event alphabet

σF={2→1,1→0,0→2}=F⁻¹ and F∩σF=∅. Consequently the unique smallest σ-closed alphabet containing F is E=F∪σF, with exactly six directed PASS labels.

Proof. Apply σ separately to the source and target of each of the three directed events. σ is an involution, and none of the three images belongs to F. Closure requires all three images, and the resulting six-element set is itself closed. QED.

## Theorem B: exact nonnegative completion cost

Start with M=0 and execute each member of F once. Any completion exclusively by nonnegative V29 PASS increments to a σ-invariant final M requires at least three additional events. The unique three-event completion *multiset* is exactly the reversed triple σF (one of each). Then M=Mᵀ, Ω=0, and the six PASS events have total Δu=0.

Proof. σ-invariance requires M01=M21, M12=M10 and M20=M02. Initially the first entry on the left of each equality is 1 and the corresponding right entry is 0. Each of these three distinct right entries must be incremented, requiring at least three events. Incrementing precisely those entries once attains equality with no extra changes. The final matrix counts one occurrence in both directions for each of the three unordered port pairs, hence is symmetric and has zero net u increment. QED.

This result concerns a **fixed ledger**. In a fully equivariant dynamics a nonfixed clockwise state may be paired with its counterclockwise image, so nonzero intermediate curvature is compatible with covariance.

## Theorem C: orientation-odd circulation

Define the signed three-port circulation κ(M)=Ω01+Ω12+Ω20. For every integer 3×3 count matrix M,

κ(σM)=−κ(M).

This follows by direct substitution under the transposition 0↔2. Thus σM=M implies κ=0. R679's forward three PASSs produce κ=+3; their image produces κ=−3; the minimum σ-fixed completion above has κ=0, Ω=0. More general σ-fixed count matrices can have other nonzero skew components while still satisfying κ=0; this theorem singles out the oriented three-cycle component.

## Theorem D: labeled future memory and BRC multiplicity

In the declared once-only six-label scheduler, every subset S⊆E is reachable. All future legal event words, current V29 ledger and signed score contrasts depend only on S, with transition δ(S,e)=S∪{e} for e∉S. Different S differ in immediate admissible named labels. Hence the **minimal labeled future machine has 2⁶=64 states**.

Under σ, E consists of three transposed pairs. There are 2³=8 invariant subsets. Burnside's lemma therefore gives (64+8)/2=36 symmetry orbits. The orbit quotient is a valid statistic for simultaneous state/event relabeling, but is NOT sufficient for unchanged named-port future legality: S={0→1} and σS={2→1} are in one orbit, yet 0→1 is forbidden after the former and allowed after the latter.

As an exact positive, labeled BRC carrier, assign mass 1 to each ordered injective prefix word over E. There are 1,957 such histories, split by length as (1,6,30,120,360,720,720). Each S of size k has exactly k! serializations, so μ(S)=k!. It preserves multiplicity, but is not signed cancellation, complex amplitude, or physical evolution.

## Theorem E: effect on the R679 static V27 selector

For each of the six R679 ||u₀||₁=19 baseline biases, adding the three reverse PASSs to the clockwise three-PASS batch returns Δu=0 and Ω=0, leaving Φ(s,t)=u₀·c(t). The resulting V27 nearest-triad graph remains globally strict for all twenty source triads (checked by exact V23 matching codes). In a finite undirected no-self-loop neighbor graph, a strict fixed-potential maximizer f(v)=argmax_{w~v} P(w) can have only directed cycles of length 2: if a cycle has n≥3, for every i one has P(v_{i+1})>P(v_{i-1}); summing gives a strict inequality of identical sums. Thus these symmetrized static V27 selectors have only flat reciprocal V17 transport cycles. For the six biases the exact checker finds three 2-cycles each.

This local result identifies an explicit cost of naive fixed-state symmetrization: the nontrivial R679 six-cycle holonomy disappears in the static Ω=0 branch. Pairing clockwise/anticlockwise states or creating truly event-dependent updates are two distinct subsequent hypotheses to investigate.

## Reproduction, scope, and next question

The accompanying Python exact checker enumerates all 1,957 once-only ordered PASS prefixes, 64 labeled subsets, 720 complete six-event orders, 729 small nonnegative off-diagonal count matrices, all six V27 baseline fixed-potential maps, and validates the analytic invariants. Run: python R681_VERIFY.py; expected marker R681_V29_PORT_ORIENTATION_SYMMETRY_COMPLETION_EXACT_PASS. It also writes the JSON evidence. All infinite-count-matrix assertions above have algebraic proofs independent of the finite checker.

Prior exact definitions: enterprise-math@18783e01e3646c72b7aab3b16d3f565e83e6446f:research_notes/X6_NETWORK_EVENT_LEDGER_AND_CONTRAST_TRANSDUCER_V29_20260906.md. Mathematical scope is V29 counted PASS and the R675 *port* action, with a specifically declared once-only submodel. Per-PASS V17 frame transport, V39 j, genuine autonomous V27 scheduling and physical correspondence remain open, and no formal CLAIM or independent review follows from this proof.

Next: inspect Source-licensed V39 loop-current and per-PASS frame-time interfaces; in the full X6 shared-Cell network, test future sufficiency of (S,h,j,typed orientation context), and local covariance under R675 before attempting additional state compression.
