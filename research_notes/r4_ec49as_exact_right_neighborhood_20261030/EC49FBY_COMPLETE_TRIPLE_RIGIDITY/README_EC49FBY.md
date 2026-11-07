# EC49FBY — Complete radius-three local rigidity of the signed-X6 BRC 158-edge witness

Date 2026-11-06. Author-side exact finite result. Frozen scientific input: fc0f038e7bfd12c886b4d37f900bfb770c0f61ab. Source EC49FBU immutable commit b3b43ef6abe2fd816d979792d18a67ee5d0aad50; predecessor EC49FBX commit 452ba5628c4c0fb9c2e67d6dead3d74b53a10cf4.

## Statement

Fix the 24 required signature-indexed operation words of EC49FBU, the frozen nine-state DFA, and their full signed-native-X6 primitive-prefix expansion. H4 and H5 use positive BRC key L=(4,2,1,0,0,0); H6–H9 use M=(7,3,2,0,0,0). H2 and H3 root paths remain fixed. Replacing any set of at most three distinct H4–H9 signature slots with arbitrary valid words for exactly the same window, positive BRC key and terminal signature, while fixing the other slots, has minimum primitive-prefix-union cost **158 edges**. The original construction attains 158.

This round proves the remaining 570 three-slot groups (450 one-early plus two-late, 120 all-late). Together with EC49FBW's 120 early triples and EC49FBX's 450 two-early/one-late triples, all C(20,3)=1140 triple groups are exactly certified. EC49FBV certified the one/two-slot cases.

## Finite proof

The alphabet is acdefg, with primitive signed-axis expansions a=(-1,-1), c=(1,2,-1,-2), d=(2,1,-2,-1), e=(3,1,1,-3), f=(1,-1), g=(2,-2). The six-dimensional native axis basis and the order and signs of each primitive step are preserved. The exact nine-state DFA and required signature map appear in VERIFY_EC49FBY.py. For horizon h and complete positive key (x,y,z), enumerate #a=z-1, #e=z, #c+#d=x+y-h-1, #f=x-(x+y-h-1)-2z, #g=y-(x+y-h-1), over every c/d split; reject forbidden DFA states and group by final signature.

For triple slots I, R is the union of the other 21 fixed paths' primitive prefixes. Write B(w) for the full signed primitive-prefix set of a candidate. Put K=158-|R| and D(w)=B(w)\R. A strict improvement must satisfy |D(w_i)|<K for each replacement. For the surviving candidates, if |D(w_1) ∪ D(w_2)|>=K then no third candidate can improve the cost; prune that pair. Exhaustively evaluate all remaining third words with exact set unions. The original 158-edge witness gives the upper bound, and all surviving triples have cost >=158. Hence each group has exact minimum 158. This pruning is valid for arbitrary sets, not an approximation to the underlying prefix objective.

## Actually executed calculations

On 2026-11-06, Python standard-library verifier completed PASS for all 570 new groups. Full Cartesian candidate count: **454,230,417,600**. Sound pruning reduced exact third-word evaluations to **241,564**, excluding **667,736 filtered candidate pairs**. All per-group minima are 158, with no improving triple. 16,156 complete candidate words and 109,972 distinct primitive signed prefixes were indexed. The executable generates EXACT_REPORT_EC49FBY.json (one record per 570 groups). The original report was 225,629 bytes, SHA256 ed13519154636deb3d4b464467957ff0cbec5cb9ce0978764d09626d07742c13. Its full content is deterministically reproducible by the verifier.

Independent VERIFY_SPOTCHECK.py constructs tuple-valued primitive signed prefixes without the bitset encoding. It checks three representative triples, and separately starts from 3,499,200 unfiltered candidate combinations for (4:1,7:1,7:4), pruning only by a valid two-word lower bound; its exact minimum is 158.

Run in this directory: python3 VERIFY_EC49FBY.py; python3 VERIFY_SPOTCHECK.py. Dependencies: Python 3 standard library. The summary JSON is an executed-results receipt; rerun the verifier to obtain the complete per-group certificate.

## Forward problem

Study coordinated exchange of four or more signature slots and other admissible cache-key schedules. For a four-slot neighborhood, use the same signed-prefix monotonicity and incrementally prune singletons, pairs and triples, then test all surviving fourth words. The overall nine-window objective includes earlier smaller-cost configurations, so this theorem belongs to the fixed L/M route. It is author-side mathematical work awaiting the project's independent Driver review, not a Source-native accepted Result.
