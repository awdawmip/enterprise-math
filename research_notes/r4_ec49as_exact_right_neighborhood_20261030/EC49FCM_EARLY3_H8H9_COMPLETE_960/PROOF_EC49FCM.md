# EC49FCM — 960 complete early3+H8+H9 five-path exact optima

Date: 2026-11-06. Frozen scientific input: fc0f038e7bfd12c886b4d37f900bfb770c0f61ab.
Status: AUTHOR_EXACT_FINITE_CHECK / PORTABLE_DRAFT / UNREVIEWED.

## Theorem

Retain the exact frozen 24 observation words, nine-state signature observer (T, SIG), ordered signed primitive-prefix edge identity and full BRC cache-key constraints L=(4,2,1) and M=(7,3,2). Of the ten H4–H6 slots select three; select one of four H8 slots and one of two H9 slots. Replace these five paths by any paths in their exact frozen slot-specific legal word pools, while keeping the other 19 original paths fixed.

For **every one of C(10,3) × 4 × 2 = 960** distinct selected slot sets, the minimum number of distinct nonempty ordered signed primitive-prefix edges is **158**.

## Exact exhaustive argument

For a chosen five-slot set S, put F = union(P(w)) over the 19 unchanged paths, where P(w) is the nonempty ordered signed primitive-prefix set of word w. For slot s, the legal candidate pool Q_s is generated exactly by frozen_model.candidates. The cost of a chosen tuple is

C = |F| + |union_{s in S} (P(w_s) \ F)|, with w_s in Q_s.

The original frozen 24-word construction lies in every slot's legal pool and has C=158; this gives a feasible upper bound. Let c=158-|F|. The bitset verifier enumerates each distinct candidate residual, filters residues having size >= c, and successively enumerates distinct unions of five residual choices while keeping precisely those with cardinality < c. At any stage a discarded union A cannot become smaller after union with later residues because |A union T| >= |A|. Equal residual states have identical continuations. Hence the final retained states are precisely sufficient to decide whether an admissible cost below 158 exists. For all 960 groups the final stage has no strict improvement, and the original feasible witness attains 158.

The verifier executed five contiguous index ranges [0,40), [40,300), [300,600), [600,850), [850,960); each of 960 groups has exact minimum 158. The combined unpruned pool-product cardinality is 26,775,318,528,000, a candidate-space count rather than performed loop operations. The largest intermediate bitset-state family contains 72 states.

A separate independent algorithm used actual signed primitive-prefix strings in frozenset objects and inclusion-minimal antichains rather than integer bitsets. This checked all 960 combinations, agreeing in slot identifiers, unchanged-prefix cardinality, and optimum 158. Its sound pruning follows from A subseteq B implying A union T subseteq B union T. This is an exact finite computation in Python integers and finite sets, with no floating-point inference.

## Representation, validity and reproduction

Frozen signed words map ±1, ±2, ±3 injectively to primitive ±E1, ±E2, ±E3 steps of a selected native-X6 chart, preserving ordered prefix equality. This finite theorem concerns this frozen path family inside the X6 ambient word model; tests with E4–E6 or different cache-key arrangements are separate mathematical research questions.

Model source is the identical Git blob c21336ba1f3719cfa03b07c3a7e9722e4cd1e84b, reused from the immutable EC49FCL predecessor. Python 3, standard library only: run EC49FCM_VERIFY.py over four disjoint intervals [0,240), [240,480), [480,720), [720,960); run EC49FCM_CROSSCHECK.py --step 1 --output independent.json for an independent full 960-group audit. EC49FCM_SUMMARY.json records the exact source pin, ranges and calculated totals. Complete raw runs and a group-indexed compact certificate also exist in the archived author evidence of this turn.

Native CLAIM/Result and independent Driver mathematical admission await authentic Source authority.
