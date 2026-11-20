# R762GS — Minimal state repairs for future named-Port and signed-Cell observers

Date: 2026-11-20 (Asia/Shanghai). Author-side portable research continuation of R762GR, Draft PR #2839 at immutable commit `2faa14abfa240300d19293628f81cba72b9416e7`.

Formal Task: `RS-X6-TRIADIC-CLOSURE-DYNAMICS`; publication `TP2-8B7E13C5904A2D6F1142`; frozen taskbook `enterprise-math@857280d1012943290d141d1317179c40ec3cbdf8`; frozen science P000 `enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389`. Historical author lineage `EM-X6-3050F6` is provenance, not a current CLAIM. Independent mathematical review: **NOT_REVIEWED**.

## Question and exact model

R762GR proved that absorption time in the *constructed* signed K4-STAR moving-Port candidate has a coarsest 75-state strong BRC quotient (74 transient orbits and an absorbing sink). Does this compressed state retain the ability to observe a **named Port**, its future legal actions, and a signed six-axis Cell update?

Take the six edge labels `E=(01,02,03,12,13,23)` of K4, and let `A_6` act on their six edge axes. For each K4 vertex `v` define its incident triple `S_v`, its indicator vector `H_v in Z^6`, and the 3-cycle `g_v` on the ordered incident axes as fixed in R762GR. For orientation `p`, current named Port `e(p)=p(01)`. The **partial labeled action**

`delta(p;(v,s)) = p g_v^s`, with `v in endpoints(e(p))`, `s in {+1,-1}`,

has signed Cell increment `b(p;(v,s))=s p H_v`; all other named letters are rejected. From `p=id`, the accessible orientation set `R` has 350 elements: 290 transient states and 60 absorbing states with Port 23. Every state admits exactly four of the eight global named letters. A BRC step samples those four legal signed source branches with equal positive weight 1/4. The source word, time order and six-axis Cell increments remain separate information; a STAR is a three-step composite, not a primitive direction. The frozen P000 triadic-force permission is **not** assumed for this candidate action.

## Theorem 1 — Observer-specific minimal exact quotients

Consider exactly the reachable 350-state directed partial transition system above, with these observer contracts:

**(A) Absorption-only observer.** It observes whether Port 23 has been entered and all future BRC absorption probabilities. The coarsest strong probability-lump has **75 states** (R762GR, reused unchanged).

**(B) Named-Port observer.** At every step it reads the exact named edge `e(p)`. A future experiment either chooses a global *named* signed letter `(v,s)` and sees whether it is admissible and the next Port, or samples the four legal BRC letters without retaining their names and observes the next Port. In both cases the coarsest exact quotient has

`291 = 290 + 1` states:

each reachable transient orientation is a distinct class; the 60 absorbing orientations constitute one class. The labeled named-action trace and the unlabeled 1/4-BRC Port observation induce the **same final partition**, despite different intermediate refinement sequences.

**(C) Named-Port plus full signed Cell-increment observer.** It observes `e(p)`, named-letter admissibility, and on every legal letter the complete six-dimensional increment `s p H_v`, together with all future such observations. Its coarsest exact deterministic quotient has **350 states**, one for each reachable orientation.

Thus a compression justified for absorption alone generally destroys future Port/Cell information. Any exact observer-preserving repair of the 75-state absorption quotient requires at least 291 states for Port observation and 350 states for signed six-axis Cell transfer. These bounds concern **orientation states** in this particular candidate, not full historical source-word multiplicity or native TRIADIC_CLOSURE_E.

## Exact finite certificate and proof of minimality

For a partition coloring `c` of reachable states, define a deterministic refinement

`D(c)(p)=(e(p), ( c(delta(p,a)) if a is permitted else REJECT )_{a in V x {+,-}} )`.

Initialize `c_0(p)=e(p)` and assign new colors by equality of complete signatures. The exact numbers of classes are:

| Observer | initial | first refinement | second | third | fourth |
|---|---:|---:|---:|---:|---:|
| Named signed-letter / Port trace | 6 | 131 | 291 | 291 | — |
| BRC Port-only Markov strong lump | 6 | 46 | 266 | 291 | 291 |
| Named signed-letter / Port + Cell-increment trace | 6 | 320 | 350 | 350 | — |

For BRC use instead the exact integer-count signature

`B(c)(p)=(e(p), multiset{c(delta(p,a)): a permitted})`.

All four branches have equal probability, so the successor-class multiset is precisely the strong Markov-lumping criterion (counts, not Boolean support). For the Cell observer replace each permitted letter entry in `D` by the pair `(s p H_v, c(delta(p,a)))`.

In each row the last refinement preserves class membership exactly and therefore gives a stable congruence. Any quotient with the specified observations and future-operation semantics must refine the initial Port partition and every subsequent signature partition (induction on future test length); hence it must refine the stabilized partition. Conversely the stabilized partition has the matching transition/observer semantics by construction and is exact. The class counts and sizes are exhaustively checked by `R762GS_CHECK.py`, which directly enumerates all 360 even permutations and performs a complete breadth-first reachability traversal, without relying on prior computed adjacency files. The first two final partitions have 290 singleton transient blocks and one 60-element absorbing block. The last has 350 singleton blocks. This proves the finite minimum for each declared observer.

For every pair of distinct transient orientations, a named-Port observation distinguishes them either immediately (33,600 unordered pairs), after one named event (8,065 pairs), or after two named events (240 pairs). The total `33,600+8,065+240 = 290*289/2 = 41,905` exhausts every unordered transient pair. Thus the length-two horizon is sufficient and sharp.

One sharp two-event witness is

`p=(1,0,2,3,5,4)`, `q=(1,0,2,4,3,5)`.

Both initially display Port `02`, and their entire one-letter Port signatures agree. Their same legal signed word `((0,+1),(1,-1))` leads to named Ports `23` and `12` respectively. The coarser absorption-oriented state cannot identify their future Port.

As a separate structural witness, among R762GR's 74 nonabsorbing H-orbits, 60 contain four *different* present named Port labels and 14 contain just one. Hence the old absorption quotient already loses a present Port observation on many fibers.

## Evidence and interpretation

`R762GS_CHECK.py` is standard-library-only, exhaustively builds transitions, identifies reachable/absorbing states, checks H-orbits, repeats the three refinement algorithms, verifies pair-discriminator counts and replays the explicit two-letter witness. It prints `R762GS_EVIDENCE.json`. All author-side exact assertions passed. This is a finite complete computation with an elementary partition-minimality argument; independent review remains **NOT_REVIEWED**.

P000's six native spatial axes, one independent time dimension, native PERP_E at 120 degrees, signed primitive directions, three-force closure arity and source-history fidelity remain unchanged. No Euclidean 90-degree orthogonality, primitive two-force balance or two-dimensional native plane is introduced. This theorem lives only within the constructed signed-STAR candidate transition. Neither the 75-, 291- nor 350-state orientation quotient preserves all Cell positions, signed path words or BRC source histories without a separately proven repair.

## Next discriminating scientific question

Specify the **actual frozen-native** `TRIADIC_CLOSURE_E` Cell/Link/Port/time event permission and legal transport. Test a particular native admissible event and its conjugates under the four H edge relabelings. If the native law admits a correspondence to this candidate, re-run exact observer-specific quotient refinement for native legal events with full provenance; otherwise preserve the counterexample and build the appropriate typed BRC carrier. Do not promote the candidate's minimality to an original primitive-force or physically measured probability claim.

Source files: `R762GS_PORT_OBSERVER_REPAIR_MINIMALITY.md`, `R762GS_CHECK.py`, `R762GS_EVIDENCE.json`. Proposed publication is a draft scientific research branch; Activity linkage, current CLAIM/PROGRESS, independent Review and Result admission are distinct operations.
