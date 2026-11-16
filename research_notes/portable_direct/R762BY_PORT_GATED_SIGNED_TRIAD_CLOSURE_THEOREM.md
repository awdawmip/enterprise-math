# R762BY — Signed X6 triad events: exact port-gated holonomy and BRC information repair

Date: 2026-11-16 (Asia/Shanghai). Formal target task: RS-X6-TRIADIC-CLOSURE-DYNAMICS; immutable publication TP2-8B7E13C5904A2D6F1142.

**Status: AUTHOR-PROVED / EXACT FINITE CHECKS / NOT_REVIEWED. Conditional event-model construction; native TRIADIC_CLOSURE_E event licensing remains OPEN.**

## Scientific source boundary

Frozen task input stays **awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json**; taskbook research_tasks/RS_X6_TRIADIC_CLOSURE_DYNAMICS_20260906.md. Current normative context was separately read on 2026-11-16. P000 defines six native spatial axes with signed Cell displacement, separate time, pairwise Enterprise PERP_E (native 120°) and primitive nonzero stable closure of exactly three forces satisfying TRIADIC_CLOSURE_E. No Euclidean vector-sum-zero rule is imported.

V17 source: research_notes/X6_ACTIVE_TRIAD_HOLONOMY_CONTROL_V17_20260906.md, Git blob 42b810a8f82c504833027da17884cc4fb2943e5b. Prior independently preserved author-side results are R762BV PR #2535 (ungated S3 spectrum), R762BW PR #2537 (directed-ledger collisions) and R762BX PR #2541@0f581a76392963bfb5d7d18396c3441f9594f4dc (all-length conditional repair theorem). This note changes the event alphabet, not those historical files or frozen input pins.

## A typed candidate realization

At any chosen Cell anchor c in the native X6 torsor and positive integer quantum q, attach three **named** force Ports p=0,1,2 to c. Each Port has signed native direction (sigma_p, a_p), sigma_p in {+1,-1}, with three distinct labels a_p in {1,...,6}. The internal Link relation is the directed cyclic incidence 0→1→2→0. Define candidate closure for these equal-quantum three-force nodes, retaining the P000 rule on all other force populations. Signs denote typed provenance, **not** a classical signed-vector sum.

A hypothetical relation event selects one eligible occupied Port p, whose axis is x=a_p, and replaces x by an absent native axis y. Cell anchor c, magnitude q, three Port names, signs, and cyclic Links stay fixed; the other two Port labels retain their slots. This exactly implements the V17 canonical active-frame switch as a conditional model. Relational time is the order of such events, not a physical duration.

Fix a static eligible-Port subset J of {0,1,2}, k=|J|. Replacements are allowed precisely in slots p∈J. Distinct choices J may have the same k; conclusions below are invariant under merely renaming the three Port slots.

The signed state X=(c,q,(a0,a1,a2),(sigma0,sigma1,sigma2),Links) is fully typed. For fixed c,q, there are 6×5×4=120 ordered label frames and 2³=8 Port-sign configurations: **960 states**. Each frame has exactly 3k events, yielding 960·3k distinct directed signed-state edges for a fixed J.

## Theorem A: exact holonomy group for each Port gate

Start at ordered frame 123; a based return is a finite permitted event history ending at any ordering of the same unordered original triad {1,2,3}. Its terminal ordered permutation is its holonomy h. **The based-return holonomy group is precisely S_J**, the symmetric group on the original labels occupying eligible Port slots, fixing every ineligible slot.

Consequently the smallest fixed-length worst-case binary repair index for the terminal ordering, given the unordered returned triad, is

**b(J)=ceil(log2(k!))**, with k=0,1,2,3 giving **0,0,1,3 bits**.

Proof: labels in ineligible slots never change, so every reachable terminal permutation is in S_J. Choose two eligible slots containing labels a,b and any absent axis y. Three replacements, in order, (slot i:a→y), (slot j:b→a), (slot i:y→b), exchange a,b and return the unordered triad. Every transposition of eligible labels is realized; these generate S_J. For k≤1 only identity remains. At least k! distinguishable final orderings imply the bit lower bound; an index of the group elements attains it. This is an exact terminal-interface theorem, not a proof of full historical provenance compression. QED.

## Theorem B: sharp holonomy support at every exact path length

Let H_{J,m} be the terminal holonomy set at length exactly m. Then:

- m=0: only identity, for every J.
- m=1: no based return, for any nonempty J; J=empty also has no positive-length history.
- m=2: only identity for every nonempty J.
- k=1: identity for every m≥2.
- k=2: all of S2 for every m≥3.
- k=3: at m=3 identity and the three transpositions; **all S3 for every m≥4**.

Proof: one replacement changes the unordered triad; a two-event return must reverse the first replacement. A nontrivial three-event return uses a temporary absent label to swap two original labels; a three-cycle cannot be realized in fewer than four switches. Exact finite reachability, with a complete 3k-branch induction enumerator, establishes the base cases at lengths 3/4 for k=2 and 4/5 for k=3, including every claimed terminal permutation. A two-event loop in any eligible slot is x→y→x and a three-event loop is x→y→z→x, with y,z labels absent from the current triad at the necessary steps. Both preserve the entire ordered terminal frame. Every integer m≥4 (respectively m≥3 for k=2, m≥2 for k=1) is one of the two consecutive base lengths plus a nonnegative sum of 2 and 3. Appending the same eligible-slot loops extends every base witness to all later admissible m. The verifier exhaustively generates the finite base cases and validates transitions. QED.

Concrete witnesses, with each three-character token an *ordered* Port frame:

- k=2, three-event exchange: **123 → 423 → 413 → 213**.
- k=3, four-event cycle: **123 → 423 → 421 → 431 → 231**.
- k=3, second four-event cycle: **123 → 423 → 413 → 412 → 312**.
- k=3, five-event cycle: **123 → 423 → 523 → 521 → 531 → 231**.

These are graph events in the conditional model, not certified native physical force transitions.

## Theorem C: native-axis symmetry does not choose Port permissions

For any fixed J, the event relation is equivariant under all 720 axis-label permutations S6, acting on six signed Cell-chart axes and on the a_p labels. This is because the conditions of membership in J and y being absent are unchanged by simultaneous relabeling.

Let internal Port rotation R act by cyclically permuting the three named Port positions, rotating Links with the positions and sending (a0,a1,a2) to (a1,a2,a0). Then the J-gated transition relation is invariant under R **if and only if J=empty or J={0,1,2}**. Indeed, rotation changes the eligible Port subset to R(J); event sets agree exactly iff R(J)=J, and a three-cycle has only empty and whole-space invariant subsets. QED.

Thus if the actual, independently established **native** rotation acts as this internal Port cycle and event licensing respects it, a nontrivial static Port gate within this candidate family must allow all three slots, leading to S3 holonomy. If native rotation instead preserves a distinguished Port, proper gates remain possible and yield smaller holonomy. Determining the actual rotation/event correspondence is a falsifiable next modeling distinction. No particular V29/V39 physical event predicate is assumed in the proof.

## Exact BRC branch-count observer and evidence

Population: all ordered histories over permitted Port switches, with Port, Link, signed directions, X6 anchor and time order preserved. For a declared **terminal frame-count observer only**, exact positive integer branch masses are pushed forward by

**N_{m+1}(g) = sum over permitted f→g of N_m(f), N_0(123)=1.**

This algebra counts path multiplicity without claiming positive mass models signed amplitude/physical cancellation. For every k the complete branch count at length m is (3k)^m (with the empty-event convention for k=0).

| Eligible Ports k | Based-return multiplicity for m=0,1,2,3,4,5,6,7,8 | Number of distinct terminal holonomies |
|---|---|---|
| 0 | 1,0,0,0,0,0,0,0,0 | 1,0,0,0,0,0,0,0,0 |
| 1 | 1,0,3,6,21,60,183,546,1641 | 1,0,1,1,1,1,1,1,1 |
| 2 | 1,0,6,18,138,762,4698,27930,168090 | 1,0,1,2,2,2,2,2,2 |
| 3 | 1,0,9,36,369,2952,26937,239148,2155617 | 1,0,1,4,6,6,6,6,6 |

For k=1 one Port label walks among four permitted values in K4 without a self-loop, giving the separate exact expression A_m=(3^m+3(-1)^m)/4 for the return multiplicity, by the elementary two-state recurrence for the starting label versus the three others.

The companion executable checker independently verifies all the above finite path counts through m=8, all 960 signed-state degrees, **1,555,200** S6-transported legal-event edge comparisons across all 720 permutations, cyclic Port invariance at each k, finite base-case witnesses and agreement of k=3 marginal totals with previously saved V17 research. The JSON companion carries the run tables and declared coverage. Author-side Python 3 exact integer test: PASSED. Independent review: NOT_REVIEWED. No floating-point or classical pi/trigonometric input.

## Outcome, provenance, and next scientific question

A concrete P000-compatible signed Cell/Port/Link triadic closure *candidate* with a reproducible finite event alphabet and exact BRC terminal-holonomy theorem now exists. P000 plus canonical conditional V17 slot transport **allows different Port-permission choices with different residual capacities**: for k=1,2,3 they require respectively 0,1,3 bits. Thus the decisive unresolved input is the genuine licensed **TRIADIC_CLOSURE_E** signed Cell/Link/Port event predicate together with the true native V17/V29/V39 rotation and source-sensitive transducer.

Next: read the task-pinned native event and rotation sources; test whether any of the above explicit paths is licensed, and restrict the frame graph by true Cell movement, signs, Port/Link incidence and order. Recompute native BRC fibers and minimal future-safe repair on that permitted graph. Unlicensed transitions remain conditional examples. Preserve prior R762BU/BV/BW/BX material, contributor history, exact frozen P000 inputs, and Source authorization boundaries without redoing their calculations.