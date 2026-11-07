# EC49FDH — independent H6/H7 keys give an exact 92-edge native signed-prefix construction

**Date:** 2026-11-07. **Status:** AUTHOR_EXACT_FINITE_RESULT / EXECUTED / UNREVIEWED / NOT_ADMITTED.
**Scientific pin:** `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`.
**Frozen operation/DFA/signed primitive source:** `EC49FCZ_H4H6H7_SIGNATURE_COMPLETE_128/frozen_model.py`, Git blob `7e97065ac9a0ff70435b92ee2f4bd718c9bf1859`.
**Predecessor:** EC49FDG at commit `ff5a9ccd4b06476d16d70158b34a783edfa8722b`.

## Exact finite theorem

Keep the original 24 labels, nine-state DFA, six-axis ordered signed-native operation expansion, and literal nonempty native signed prefixes. The original H2/H3 four operation words (`fe,ge,feg,gef`) stay fixed and together cost 16 prefixes. Hold H4 and H5 key `(4,2,1)`, H8 key `(6,5,1)`, and H9 key `(6,4,1)`. Let H6 and H7 each choose an **independent, legal integer BRC cache key**. For every key choose one word for every required terminal signature from its *entire legal ordered operation language*.

Exactly **22 H6** and **34 H7** keys cover all required observation signatures; the full product is **748 key pairs**. A full-candidate signed-prefix Trie exact 20-label-mask dynamic program was actually executed on every pair. **Minimum across all 748 models is 92 distinct nonempty signed-native prefixes**, attained at precisely two key pairs:

- H6 `(5,3,1)`, H7 `(5,4,1)`;
- H6 `(5,3,1)`, H7 `(6,4,1)`.

The 24 operation words for the second minimizer are in `WITNESS_92.json`; native signed prefix expansion gives **92**, a 14-edge improvement from EC49FDG's 106. The sorted signed-prefix union has SHA256 `e8f50fe9b7daa7e70f5e39757baa4a67139e2177b6c02f21bb1fc3d7118ea55c`.

## Exhaustion argument and exact DP proof

For horizon `h` and key `(x,y,z)`, operation multiplicities obey
`a=z-1, c+d=x+y-h-1, e=z, f=h+1-y-2z, g=h+1-x`. Exhaust integer triples with `1<=z<=floor((h+1)/2)`, `1<=x<=h+1`, `0<=y<=h+1-2z`, `x+y>=h+1`; for each `c=0..c+d`, enumerate every ordered multiset operation word and apply every nine-state transition, rejecting the dead state. A key is accepted when all its required signatures have a nonempty word set. This proves completeness of the 22 and 34 classes.

For each key pair build a prefix Trie of all H4–H9 words after *ordered signed-native expansion*. Each terminal has a 20-bit mask of compatible observation labels. Give each edge cost zero precisely when its literal signed prefix is in the 16 fixed H2/H3 prefixes; otherwise cost one. Define `D_v(S)` as minimal paid edges below node `v` to select exactly label set `S`. Initialize all submasks of labels terminating at `v` at zero. For each child `u`, merge **disjoint** subsets `A,B` by `D_new(A∪B)=min(D_old(A)+D_u(B)+cost(v,u)*[B != empty])`. Induction on Trie height proves the DP covers every legal assignment and charges each distinct nonfixed prefix once. Add the 16 fixed prefixes at the root. All arithmetic is integer; neither heuristics nor truncated word pools are used.

**Observed execution:** 748/748 instances, 12,424,911,386 C++ inspected DP state-pairs total, largest Trie 52,372 nodes. The 22×34 lossless per-pair optimum table is `MATRIX_H6_H7_748.txt.gz.b64` (decoded SHA256 `74fdebcbc34582aada4daf31693182b141c8fc47956ee5d77cc53818b489f548`). The 748 full per-case raw JSONL was executed and locally captured (SHA256 `4f8c80e370d757f3c9c429b8f06bd4c44283262e8c16ad4f40e00372b11e6f69`) and the generator can reproduce it.

For the second minimizer, **independent Python exact Trie** reconstructed language, Trie and subset DP using the separately published EC49FDE verifier: 92 optimum (16+76), 30,059 Trie nodes, 5,612 legal operation words, 25,815,852 inspected subset state-pairs, 1,048,576 root mask states. Exact C++ solver agrees.

## Source and reproduction

- `VERIFY_EC49FDH.py` reads the witness, checks 24 labels, BRC multiplicity languages, nine-state DFA and signed prefixes, optionally invokes existing `../EC49FDG_WINDOW_SPLIT_LATE_KEY_800_106/DP_EC49FDG.cpp` on the exact key pair or all 748 pairs.
- `INDEPENDENT_PYTHON_EXACT_92.py` independently builds the 92-minimizer's full-candidate native Trie and performs uncapped dict subset DP, reusing `../EC49FDE_ALTERNATE_BRC_LATE_KEY_EXACT_112/VERIFY_EC49FDE.py` as the already-published independent model source.
- `REPRODUCE_748.py` executes all 748 models, records detailed per-pair JSONL and checks compressed matrix. Compile existing solver with `g++ -O3 -std=c++17 ../EC49FDG_WINDOW_SPLIT_LATE_KEY_800_106/DP_EC49FDG.cpp -o exact_solver`.

This **92 <= 93** gives a stronger-than-93 numerical signed-prefix construction for the declared 24-label model. The original nine-window mother-task's *cross-horizon* cache-key compatibility requirements, if any, require a separately pinned admissibility check before formal parent-goal closure.

## Next EC49FDI

Audit the original mother-task 93-edge contract for any shared-cache-key or cross-horizon coupling not present in this finite model. Then preserve the 92-edge witness and explore H4/H5 independent keys or an independently justified key-compatibility construction. This will distinguish an actual mother-goal resolution from a useful expanded-model optimum.

## Control state

GitHub connection identity `awdawmip` has repository admin permission. Native Enterprise Math `em_status` returned `BACKEND_IDENTITY_OR_VERSION_MISMATCH`, `operation_sent=false`; no current authenticated active owner/CLAIM/Source Result/independent Driver verdict verified. This is durable author-side mathematical evidence. P000 and the ACTIVE worldview were not edited.
