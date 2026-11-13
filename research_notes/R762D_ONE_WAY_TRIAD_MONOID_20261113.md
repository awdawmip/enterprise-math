# R762D — A single admitted chirality per triad still generates the full A6 port monoid

Date: 2026-11-13 (Asia/Shanghai). Classification: author-side exact candidate-algebra theorem and exhaustive finite calculation; NOT_REVIEWED / NOT_ADMITTED as native force dynamics.

Parent: RS-X6-TRIADIC-CLOSURE-DYNAMICS; immutable publication TP2-8B7E13C5904A2D6F1142.
Frozen scientific inputs: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389 (unchanged).
Predecessor: R761S, Draft PR #2249, head befa98585e057304e08c3cb4d3c3c5a1888685aa. R761, Draft PR #2241. P000, ACTIVE worldview and original task are unchanged.

## Precisely declared candidate and observer

Take one chosen X6 Cell, the *six positive native-axis port names* I={0,1,2,3,4,5}, and six distinct persistent provenance labels. Every candidate event uses three equal positive force-quanta q on distinct ports and *one* supplied cyclic orientation. The event only permutes the three labels by a 3-cycle; the other labels and ports remain. The event trace preserves its Cell, three source labels, support, orientation, event order and time as typed metadata. An event changes the symbolic port-label placement, not native Cell position.

For each 3-set s={a,b,c}, a<b<c, choose exactly one of the 3-cycles g_s=(a b c) and g_s^{-1}=(a c b). An event alphabet E consists of three *distinct* supports and one designated chirality per support. **This paper assumes each selected event is admissible again after every generated state and that successive events compose without a further state-dependent guard.** Such unconditional repeatability is a stipulated algebraic language, not established P000 Cell/Link/Port admission. In particular, this is not a simulation of V29 PASS/TRANSFER or V39 frame transport.

The observer asks for the final source label at every one of the six ports after arbitrary finite candidate operations, including future continuations. Branch/timestamp/source-event history remains available separately for broader observers. The finite port register is not a claim of lossless native physical state compression.

## Theorem 1: one chirality per support suffices for the same reachability group

Let E be any finite collection of distinct 3-supports on I. For each s∈E, choose exactly one orientation g_s, a 3-cycle. Denote by M_+(E) the monoid of all finite forward words (including empty) in these chosen directed generators and by G_±(E) the group generated using *both* orientations of every support.

Then

    M_+(E) = G_±(E).

In particular, by the incidence/component theorem of R761S, this monoid is the direct product of the alternating groups A_C on connected components C of the 3-uniform support hypergraph E (with isolated vertices fixed).

**Proof.** Every g_s has order three: g_s^3=e. Therefore the inverse of each chosen generator can be realized with two *forward* copies, g_s^{-1}=g_s^2. The monoid contains every inverse of each generator, hence every word in the group G_±(E). Conversely every monoid word is a group word. Equality follows. The component classification is R761S Theorem 1 applied to the same supports; it does not depend on the orientation choices. □

This matters precisely when only one chirality per support can be admitted, but the repeated application assumption holds. It trades at most two same-direction events for one inverse event.

## Theorem 2: exactly three directed event types are necessary and sufficient for A6 reachability

Any two 3-supports either intersect, in which case their union occupies at most five of the six ports, or are disjoint, in which case the generators act on separate components. Either way they cannot generate a transitive A6 port action. Thus at least three distinct *directed* event types are necessary.

Three suffice, choosing

    s1={0,1,2}, s2={0,3,4}, s3={1,3,5}

and the forward cycle on each listed ascending triple. The hypergraph is connected and covers all six ports, so Theorem 1 gives M_+(E)=A6, with exactly 360 reachable port-label states. The minimal number of directed event types is therefore **three**. R761S's six-type result assumed two individually available orientations for each of these three supports; the present result only assumes one choice per support is indefinitely repeatable. □

## Theorem 3: sharp directed word diameter seven; complete classification

Fix exactly three distinct supports from the 20 possible 3-supports, and one of two orientations on each. There are

    binom(20,3)*2^3 = 1140*8 = 9120

different labelled directed alphabets. Define d(E) as the maximum over reachable permutations of the shortest number of *forward* generator applications. The accompanying standard-library verifier enumerates every alphabet and exhaustively BFS-enumerates its finite monoid from the identity.

| Reachable monoid | Directed alphabets |
|---|---:|
| A4 on four ports, order 12 | 480 |
| A5 on five ports, order 60 | 4,800 |
| A6 on six ports, order 360 | 3,840 |
| **All** | **9,120** |

Among the 3,840 A6 alphabets, the directed diameters have this exact distribution:

| Maximum minimum directed events | Number of alphabets |
|---:|---:|
| **7** | **720** |
| 8 | 240 |
| 9 | 2,160 |
| 10 | 720 |

All A6 alphabets fall into R761S's three support-incidence types, further split by selected orientation:

| Pairwise support intersection multiset; triple intersection | Diameter → number |
|---|---|
| (0,1,2); 0 | 9 → 720, 10 → 720 |
| (1,1,2); 1 | 9 → 1,440 |
| (1,1,1); 0 | 7 → 720, 8 → 240 |

For the explicit optimal supports s1=012, s2=034, s3=135 and all three forward chirality bits (0,0,0), BFS gives all 360 states with layer counts for distances 0 through 7:

    (1, 3, 9, 24, 63, 135, 115, 10).

Thus every even six-port permutation is reachable in **at most seven forward triadic events** under this particular three-type repeatable candidate language, and ten states require seven. The exhaustive 9,120-alphabet calculation proves that seven is the *smallest possible worst-case forward depth* among the precisely specified three-support one-chirality-per-support alphabets.

For the same supports but bits (0,1,0), the diameter becomes eight and the corresponding layer counts are (1,3,9,24,61,124,117,19,2). The orientation choice affects *directed event depth* while it does not affect reachability. Relative to R761S's optimal five-event symmetric alphabet, one-sided chirality removes the need to admit inverse events individually, at the price of seven-event optimal directed depth.

**Exhaustiveness certificate.** The verifier enumerates the 20 increasing three-supports, all 1,140 unordered triples, and all eight binary orientation assignments for each. Each 3-cycle is an exact six-integer image tuple. For a state p and allowed event g, the BFS transition is p∘g (consistent on every calculation). First discovery yields its shortest forward word length; closure is detected when no new tuple remains. Assertions require the above 9,120 count, group-order classes, incidence-by-diameter counts, two explicit depth histograms and exact 360-state cardinality. No floating point, randomized sampling, classic physical propagation, or non-BRC numerical dynamics is used. The finite result is a fully specified exhaustive certificate whose checker must be run for its computational corroboration; the group-equality and three-generator minimality are independent algebraic proofs.

## BRC/source-observer and physical interface

This is a *scope-typed* finite residue/state quotient: 360 distinguishable final port placements require exactly ceil(log2 360)=9 fixed-width bits and are sufficient for future candidate-port permutations. A compact state cannot replace an ordered provenance ledger when timestamps, signed port incidence, event multiplicity, V29, V39 or native force observations are requested. This use of BRC is a structural observer-fidelity classification, **not** a claim that an actual typed BRC numerical kernel has been run or that auxiliary A6 is the previous A7 frame representation.

P000 fixes the primitive force arity and native 120-degree PERP_E balance starting point; it does not by itself establish that the selected three supports and even one chirality each are admitted as *repeatable* force events. This theorem says: **if** the native event-to-port map admits these three directed events, preserves their ordered source/port labels, and makes their repeatability legal, **then** the candidate final-label reachability and seven-event bound follow. The conditional interface must first check signed Cell/Link/Port incidence, the three-force quantum, time and trigger rules, then actual V29 PASS/TRANSFER and V39 update. No P000 revision is proposed.

## Next discriminating step

At the frozen task pin, read actual force-incidence definitions and derive the native legality predicate for one *oriented* event at support 012, then its second consecutive application. The exact question is whether a second same-chirality event remains admitted after the first transfer/label change. Test supports 034 and 135 and the same event composition. If any required transfer or provenance property fails, record the first failing type condition and the true admissible alphabet. Recompute its **state-dependent** reachability graph rather than silently applying the present unlimited-repeat monoid theorem. Verify owner/CLAIM through completed current Source continuation before any formal claim-bound publication.

Artifacts: R762D_ONE_WAY_TRIAD_MONOID_20261113.md, R762D_VERIFY.py, R762D_EVIDENCE.json, R762D_HANDOFF.md. This is author-side scientific research; no Source formal Result, independent Driver review, or mathematical promotion is asserted.

## Theorem 4: a V29 count-ledger factorization obstruction

This section uses verified prior V29 source at awdawmip/enterprise-math@deb8bbbf9d844c0ceb777631e576763a634eed99:research_notes/X6_NETWORK_EVENT_LEDGER_AND_CONTRAST_TRANSDUCER_V29_20260906.md and V39 source at the same source commit:research_notes/X6_CYCLE_CURRENT_S3_OPERATION_SAFE_PORT_V39_20260906.md. These are comparison dependencies; the parent's frozen scientific input is unchanged.

V29's *primitive counting grammar* distinguishes PASS(x;a->b), which adds one to a nonnegative M_x[a,b] count, and matched TRANSFER(x:a->y:b), which adds one each to nonnegative Rout_x[a] and Rin_y[b]. Each concrete occurrence contributes a **nonzero nonnegative** increment to the absolute ledger L=(M,Rin,Rout). The event language carries a count history and does not itself supply a triadic-force scheduler, a physical inventory guard, or an admitted force->PASS/TRANSFER map. V39, separately, defines based-loop (j,h) with j net cycle current and h an S3 frame; this scope is *not* the same as an absolute V29 count-ledger observer.

**Exact conditional no-go.** Let Sigma be the selected directed triadic symbols of the present repeatable candidate, phi:Sigma* -> A6 the positional permutation map, and suppose a putative force-to-V29 mapping assigns to at least one symbol s a fixed nonzero V29 count increment delta(s) in N_0^D, with count updates accumulating additively for repetitions. Let L(w)=sum of the increments of the letters of w, starting from zero. Then **L does not factor through phi**, even if the candidate algebra reaches all of A6.

**Proof.** The letter s has phi(s)^3=e. Thus empty history eps and sss have identical phi, but L(eps)=0 while L(sss)=3 delta(s) !=0, since delta(s) is a nonzero nonnegative count vector. Therefore no function F:A6->N_0^D can satisfy L=F o phi. More strongly, phi(s^(3n))=e while L(s^(3n))=3n delta(s) are all distinct for n>=0. Consequently **no finite state carrier** suffices for the observer that queries the full unbounded absolute V29 count ledger after arbitrary repetitions. QED.

**Exact observer-safe repair under fixed increments.** For the declared candidate future language of appending any alphabet word and querying both final port labels and all absolute V29 counts, the joint signature

    Sigma_poscount(w)=(phi(w),L(w))

is predictive: Sigma_poscount(wv)=(phi(w)phi(v),L(w)+L(v)), with multiplication convention fixed by the same image-tuple event order as the verifier. Equal pairs remain equal under every common future word. Because both coordinates can be queried directly, distinct pairs are distinguishable immediately: this is the coarsest exact quotient for that *declared* observer/future operation language. It is generally infinite-state because counts are unbounded. The nine-bit A6 port register remains exact for its earlier, narrower label-only observer.

The no-go does not assert the existence of a native force-to-V29 event mapping, nor that each physical event is repeatable. It identifies a precise incompatibility that **any proposed mapping claiming to recover absolute V29 occurrence counts from the A6 label state alone** must resolve. A finite horizon, signed contrast-only observer, or a non-repeatable native scheduler is a different scoped problem needing its own certificate. A V39 based-loop (j,h) observer likewise requires its own typed map and cannot be identified with either L or the A6 port permutation.

**Sharper next native test.** At the source frozen pin, test the first and second applications of the *same* proposed oriented primitive force event: (1) is the second event still admitted? (2) if it is, does it contribute a second nonzero V29 PASS/TRANSFER count occurrence? (3) what is the independently specified V39 frame readout? These three questions determine whether the present candidate action and the conditional V29 no-go are instantiated by a true native bridge.
