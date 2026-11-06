# EC49FCD — all 210 late-window quartets are 158-edge rigid

Date: 2026-11-06. Status: AUTHOR-SIDE FINITE EXACT THEOREM / INDEPENDENT DRIVER REVIEW PENDING.

Frozen science pin: fc0f038e7bfd12c886b4d37f900bfb770c0f61ab.
Parent: EC49FCC, commit c1bfe81423ddbb1c503e55c3ade5c470d2b8744f.
158-edge baseline: EC49FBU, commit b3b43ef6abe2fd816d979792d18a67ee5d0aad50.
Generator: EC49FBY, commit 5b10f1c296cb8826d4b69f6fd83dba89d765df1c.

## Exact proposition

Retain the frozen 24 operation words: four H2/H3 roots and 20 H4–H9 observation slots. The original horizon, complete six-coordinate positive BRC cache key (L=(4,2,1,0,0,0) for H4/H5 and M=(7,3,2,0,0,0) for H6–H9), and nine-state DFA terminal signature are required for every slot. Keep 20 words fixed and select four distinct late slots among the ten H7/H8/H9 slots (4+4+2). Each selected slot can be replaced by any candidate operation word satisfying its original requirements. The original signed-X6 native primitive expansion and all nonempty ordered prefixes define cost.

**Theorem.** For each of the C(10,4)=210 late-only slot sets, the minimum number of distinct native signed primitive prefix edges is exactly 158.

## Complete finite argument

For a four-slot set I, R is the prefix union from the 20 fixed words, and B(w) is the complete native signed-step prefix set of legal word w. Let D(w)=B(w) minus R. Strict improvement is equivalent to the existence of one candidate in each chosen slot with
  |D(w1) union D(w2) union D(w3) union D(w4)| < 158 - |R|.

EC49FBY's finite generator exhaustively recurses through all nonnegative operation multiplicity solutions of the cache keys, six legal operation letters and all nine DFA transitions. It distinguishes native sign, order, prefix and signature. The bitset maps each distinct complete native primitive prefix to its own integer bit, so bitwise OR/popcount exactly computes set union size.

For each I, discard residual candidate sets already of cardinality at least 158-|R|, collapse exact duplicate residual sets within their own slot (same future effect on this fixed objective), and order the remaining pools by size. Prune a partial pair/triple as soon as its prefix union reaches this bound, since adding more sets cannot reduce a union. Exhaustively test every fourth residual set remaining. This tests every possible strict-improvement configuration. No group produced a cost below 158. The frozen baseline itself is feasible at 158 in every group, hence equality.

This proof applies to the fixed 24 slots, nine-state DFA, BRC key schedule and native signed-X6 primitive prefix objective. It makes no stronger global schedule claim.

## Recorded exact computation

All 210 groups were executed by a locally reconstructed copy of the immutable EC49FBY generator and the exact verifier algorithm provided here, in disjoint ranges. There were 196 regular groups with at least 144 fixed prefix edges and 14 deeper-overlap groups with 137 or 138 fixed edges. The result merger enforced indices 0..209 exactly once, unique groups and equality of every cost.

Raw candidate four-tuples: 1,069,546,816,890,000.
Individual-residual filtered product total: 23,804,059,817,376.
Pruned two-candidate pairs: 8,327,983.
Pruned surviving three-candidate prefixes: 10,223,623.
Actually evaluated fourth-candidate unions: 670,296.
Minimum: **158** in all 210 groups.

Five disjoint representative slot sets were independently checked with integer signed-step tuples and frozenset unions instead of encoded string/int bitsets, giving 158 in every case. The original full local 210-row report has SHA-256 a4bb3ba6e86076fc364aff4e79d5d75f3804983af6f0e4deefd8890f690c9050. SUMMARY_EC49FCD.json contains the published aggregates; VERIFY_EC49FCD.py regenerates the full 210-row certificate. Use disjoint start/stop ranges covering 0..210 and then run merge.

The published verifier was also actually run for indices 0..3 against the same frozen generator model. Its exhaustive search and monotonic pruning logic matches the actual full local 210-group implementation. The independent tuple checker was executed on five samples using the same native signed integer step semantics.

## Cumulative frontier

EC49FBZ/FCA/FCB/FCC proved 3,435 other four-slot sets. EC49FCD adds 210 disjoint late-only sets. Exact four-slot rigidity coverage is now 3,645/4,845 (about 75.2%). The remaining 1,200 sets choose one early H4–H6 slot and three late H7–H9 slots. The mother problem includes five-or-more coordinated replacements and alternative BRC cache-key schedules.

Next EC49FCE: test the 1,200 early-one/late-three sets using groupwise monotone prefix bounds or an exact residual-pair dynamic program, seeking either a 157-edge witness or a complete fixed-schedule four-exchange theorem. This is an author-side research result for independent Driver consideration; formal task CLAIM/Source Result depends on current actual authority. P000 and ACTIVE worldview remain unchanged.
