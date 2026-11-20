# X6 R45 — Observer-label erasure, Boolean-BRC future quotients, and exact path-multiplicity preservation in the R44 rotation carrier

Date: 2026-11-20 (Asia/Shanghai).
Lineage: RS-X6-NATIVE-TIME-DYNAMICS / R42 → R43 → R44 → R45.
Historical contributor context: EM-X6-214D9C; portable scientific work, not a native CLAIM/PROGRESS/Review.
Status: CONDITIONAL_AUTHOR_PROOF / EXACT_INTEGER_FINITE_GRAPH_PASS / NOT_INDEPENDENTLY_REVIEWED.

## Source and frozen model

The scientific starting point is the task-frozen P000 V5 at awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389, including p000_reality_foundation.json, definitions/P000_DISCRETE_DIRECTION_TRIADIC_BALANCE_20260905.md, and definitions/ENTERPRISE_JOINT_RELATION_OBSERVER_PRESERVATION_20260905.json. The 6D discrete X6 Cell torsor, the non-primitive status of non-axis paths, and the indivisibility of a primitive three-force closure remain assumed. No physical R/T transition is derived here.

This note uses *exactly* the finite conditional R44 transition law in research_notes/portable_direct/2026-11-20_x6_r44_rotation_reoccupation_future_residual.md (prior published blob 70bdc396c7e9ab22081c27f28f4e48f598852157). The two sources A,B each execute one whole triadic transfer using one of p named Ports (p>=1). Port 0 targets a common Cell; nonzero Ports have private targets. An occupied Cell blocks the other Port-0 transfer. R releases current occupancy, retaining source consumption. Once exactly one source has fired and the shared Cell is empty, T can occur once. T reoccupies the Cell iff the fired source originally used Port 0. Each word is a finite successful serial event history, with positive unit BRC weight; no signed amplitudes or cancellation.

For p=3 this is the native *candidate* three-Port geometry. p>3 is a combinatorial extension, not a proposal for additional primitive physical Ports.

## Exact observation question

Let q be a reachable decorated R44 state. Let L_pi(q) be the set of all finite successful future words after a label map pi. Define C_pi(q,w) as the **number of original named future words** projected to w. Thus C takes values in the nonnegative integers and remembers multiplicity even where labels are erased. Erasure does not identify or discard original paths before counting.

Three observer maps are compared:

1. N (named): Ai ↦ Ai, Bi ↦ Bi, R ↦ R, T ↦ T.
2. S (source): Ai ↦ A, Bi ↦ B, R ↦ R, T ↦ T.
3. F (source-blind): Ai,Bi ↦ F, R ↦ R, T ↦ T.

For each pi, q≡_pi^Bool q' iff L_pi(q)=L_pi(q'). The positive-path equivalence is q≡_pi^Count q' iff C_pi(q,w)=C_pi(q',w) for every finite w.

These are **observer-typed equivalences**; they make no claim that the underlying source, selected Port, Cell identity or path provenance can be physically deleted under every different future intervention.

## R45.1 — Exact future-language and path-count quotient

For every positive integer p the numbers of state-future classes are exactly:

| Observer | p=1 | p>=2 |
| --- | ---: | ---: |
| N, full source and Port names | 11 | 13 |
| S, source name retained but Port index erased | 11 | 13 |
| F, source and Port both erased | 7 | 8 |

For **each observer and every p>=1**, its Boolean and positive-integer path-count equivalence relations agree on the R44 reachable states. Consequently the minimal fixed-length future class index is four bits for N and S, and three bits for F. In particular the native-candidate three-Port case p=3 has 47 decorated states, 13 S classes and 8 F classes; source blindness merges five pairs of source-oriented future classes even when all projected path multiplicities are retained.

### Proof by a finite weighted transition skeleton valid for all p

Let X denote the single fired source and Y its unused counterpart. The following eight *source-blind roles* exhaust all reachable states (remove Cn if p=1):

- U: both sources unused.
- O0: precisely one source used; Cell occupied; T not used.
- O1: precisely one source used; Cell occupied; T used.
- C0: precisely one source used; Cell clear; T not used; used source originally selected Port 0.
- Cn: precisely one source used; Cell clear; T not used; used source selected a nonzero Port.
- C1: precisely one source used; Cell clear; T used.
- D1: both sources used; Cell occupied.
- D0: both sources used; Cell clear.

All transitions below are counted over the source-blind alphabet {F,R,T}. An omitted transition has multiplicity zero. The notation k·Z means k distinct named choices leading to role Z after the *same* coarse event.

~~~text
U   --F--> 2·O0 + 2(p-1)·Cn
O0  --F--> (p-1)·D1          --R--> C0
O1  --F--> (p-1)·D1          --R--> C1
C0  --F--> D1 + (p-1)·D0    --T--> O1
Cn  --F--> D1 + (p-1)·D0    --T--> C1
C1  --F--> D1 + (p-1)·D0
D1  --R--> D0
D0  --(no transition)-->
~~~

Each row follows directly from R44's complete indivisible-source transfer and R/T rules. Every state assigned the same role has precisely the displayed successor **multiplicities**; the state graph is finite and acyclic. Induction on remaining event length therefore proves equality of every projected C_F(w), and hence of L_F, inside a role. For p>=2 all eight roles are reachable. For p=1 Cn is absent, leaving seven.

For p>=2, their immediately allowed F/R/T masks already differ except (U,C1), (O0,O1), and (C0,Cn). The respective distinguishing words are FF, RT, and TR. Here FF is legal from U because a first nonzero Port leaves the other source able to fire; after C1 only one source remains. RT succeeds from O0 but not O1. TR succeeds from C0 but not Cn because T reoccupies only after original Port 0. All other pairs differ at the first event. Thus eight Boolean classes are necessary.

For p=1 the allowed masks have three collisions: U versus C1 (both {F}), and O0/O1/D1 (all {R}). The latter three separate within two events by RT and RF; U and C1 agree through two observed events (their languages up to length two are exactly {ε,F,FR}) but are distinguished by FRF, successful only from U. All seven classes are therefore necessary. This proves the F row.

For S, distinguish the identity of the single fired source X using the remaining source-name label Y; for p>=2 the five one-fired roles each split into an A-oriented and B-oriented class. U,D1,D0 do not split. The resulting 1+2·5+2=13 classes are all distinct within two events by the same role-specific words and by their available named A/B transfers. For p=1 the absent Cn role gives 1+2·4+2=11. The S transition counts for these oriented classes are identical within each class (replace the coarse F by the actual remaining source label Y); hence these are exact *weighted* classes.

Finally, R44 already established 13 (or 11) distinct classes for N. Every N class lies within an oriented S role and there are exactly as many S roles as N classes. Therefore erasing just the Port index introduces no further merger. Source/Port classes already collapse unused nonzero-Port distinctions where their entire declared future is equal.

In all three maps, the count partition is **at most as coarse** as the Boolean partition because positive counts reveal support. The displayed weighted transition skeleton (and its source-oriented refinement) shows every Boolean class has identical counts; the two partitions coincide. This completes the proof for arbitrary p>=1.

## R45.2 — Sharp distinguishing-horizon bounds and a provenance obstruction

The greatest, over all future-inequivalent reachable state pairs, of the shortest distinguishing observation-word length equals:

| Observer | p=1 | p>=2 |
| --- | ---: | ---: |
| N | 2 | 2 |
| S | 2 | 2 |
| F | 3 | 2 |

The role-pair witnesses in R45.1 provide the upper bounds, and O0/O1 force length two for N/S at every p. For F when p=1, U versus C1 force length three; for p>=2, O0/O1 force length two. Thus the bounds are sharp.

Consider A0 and B0 from the initial state. They differ under the named or source observer (the remaining source action is B or A, respectively). Yet the A↔B exchange is a label-preserving automorphism **under observer F**, so their entire F future languages and *all positive integer path multiplicities* are exactly equal. Repeated future event counting cannot recover which source fired. This is an explicit, exact loss-of-provenance certificate for the source-blind observer, not a claim that provenance is absent from the full native state.

The earlier R44 three-Port pair A0 R versus A1 is still distinguishable after erasing Port labels: projected TR is legal after A0 R but not after A1, because T reoccupies the shared Cell only in the first case. The earlier Port-specific witness T B0 disappears under that observer, but the temporal occupancy witness TR replaces it without changing the full S/F quotient cardinality.

## Independent reproducible finite checks

Program: research_notes/portable_direct/x6_r45_observer_erasure_verify.js.
Output: research_notes/portable_direct/x6_r45_observer_erasure_results.json.
Run: node research_notes/portable_direct/x6_r45_observer_erasure_verify.js.

The JavaScript function was executed using exact integer counting. It builds every reachable R44 state, recursively enumerates each successful future *named* word once, projects to each declared observer, accumulates nonnegative integer multiplicities, and compares all ordered decorated-state pairs for Boolean and weighted equivalence. It explicitly checks the state formula 2p²+8p+5 and complete named-word formula 4p²+16p-3, and the shortest distinguishing horizons. For each p=1,...,8, every asserted comparison passed. At p=3 the verifier found 47 states, 81 successful named histories including ε, the quotient cardinalities (13,13,8), and maximum shortest distinguishing lengths (2,2,2). The general-p claims use the role-skeleton proof above, not inference from these eight checks.

## Scope of the result and next genuinely open scientific bridge

These are exact positive Boolean/weighted serial-trace results for the **conditional R44 automaton**. They do not certify a legitimate physical R, T, clock period, or actual Cell/Link/Port update for TRIADIC_CLOSURE_E. P000's joint-relation and native multipath preservation principle continues to require source, branch, ordered microsteps and multiplicity until a certificate explicitly names its observer and operations. R45 shows that source-only observation can suffice for the R44 *future language*, while full source identity cannot be reconstructed from a source-blind history even if coarse path counts are saved.

The next physical question is to read the task-frozen native Cell/Link/Port event contracts and build either a precise trace-preserving implementation of R/T or a precise typed obstruction. A useful follow-on mathematical extension is to add a native-admissible provenance-query or rotation operation and test whether it separates the two F-equivalent source-swapped states. Preserve the original frozen science pins, R42–R44 authorship, conditional evidence status and existing owner/CLAIM rules.
