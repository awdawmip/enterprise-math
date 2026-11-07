# EC49FCY — eight exact seven-slot signed-native prefix minima

Date: 2026-11-07 (Asia/Shanghai).
Status: AUTHOR_FINITE_EXACT_PROOF / LOCAL_COMPUTATION_EXECUTED / UNREVIEWED / NOT_ADMITTED.
Scientific input pin: `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`.
Frozen source: `EC49FCS_EARLY_H4_H5_LATE_H7_H8_H9_256/frozen_model.py`, Git blob `7e97065ac9a0ff70435b92ee2f4bd718c9bf1859`. Original 24 slots, nine-state trap-avoiding observer, signed ordered native primitive-step prefixes, BRC fixed keys L=(4,2,1) (H2–H5), M=(7,3,2) (H6–H9).

## Exact finite proposition

For each a in {16,32} and r in {1,2,4,8}, allow all the legal frozen candidates at exactly seven slots, fixing the other 17 original witness paths:
- a=16: S=(4:r,5:16,6:1,7:1,8:2,8:4,9:16).
- a=32: S=(4:r,5:32,6:1,7:1,8:1,8:8,9:32).

For **every one of these eight precisely specified seven-slot domains**, the exact minimum number of distinct nonempty ordered signed primitive prefixes is **158**.

The original witness has 158 edges and gives a feasible upper bound. The complete exact trie DP below supplies an equal lower bound; every mutable signature language is exhaustively generated from the unchanged frozen DFA/multiset operator constraints. Each case has candidate sizes 12,12,30,540,3150,1890,1680 in its selected slot order, i.e. 23,332,385,664,000,000 mathematical combinations per case before compression. We do not claim to have evaluated that many tuples individually.

## Exact method

Let F be the union of the prefix sets of the 17 fixed original paths. Insert every signed primitive expansion of every legal candidate word into ONE common rooted trie. Each candidate terminal carries the bit(s) for every selected slot for which it is legal; thus a common signed prefix edge is paid only once. A trie edge has weight 0 exactly when its complete prefix is in F, and weight 1 otherwise.

For node v, let D_v(M) be the least additional edge weight needed inside its subtree to cover a required set M of the seven slot labels. Initialize Q_v(M)=0 for M contained in the labels ending at v, and infinity for other M. For every child u, process in any order:

`Q'_v(M) = min_{K subset M} [Q_v(M\K) + D_u(K) + (K != empty ? c(v,u) : 0)]`.

After all children, set D_v=Q_v. Answer: `|F| + D_root({all 7 labels})`.

**Proof:** Every complete choice of one legal candidate for each selected slot induces a rooted union of prefix paths. At each trie node, labels realized by child subtrees can be partitioned into the labels assigned to that child and to other subtrees/terminal; the recurrence includes that partition and pays the child's incoming edge exactly once when used. Conversely every finite recurrence partition selects a rooted family of terminal paths covering all required labels. If it selects more than one terminal for a label, drop extras without increasing the union. Induction on trie height proves exact optimality. Cost O(E 3^7) time and O(V 2^7) memory after finite candidate generation. There is no numeric approximation or unproved prefix collapse.

## Results (actual compiled C++ execution)

| branch | H4 slot | fixed edges | trie nodes | optimum added edges | exact total |
|:---|:---|---:|---:|---:|---:|
| a=16 | 4:1 | 111 | 53,165 | 47 | **158** |
| a=16 | 4:2 | 118 | 53,165 | 40 | **158** |
| a=16 | 4:4 | 119 | 53,165 | 39 | **158** |
| a=16 | 4:8 | 119 | 53,228 | 39 | **158** |
| a=32 | 4:1 | 111 | 51,878 | 47 | **158** |
| a=32 | 4:2 | 119 | 51,955 | 39 | **158** |
| a=32 | 4:4 | 119 | 51,973 | 39 | **158** |
| a=32 | 4:8 | 118 | 51,878 | 40 | **158** |

The exact per-row DP transition counts and pool sizes are in `EC49FCY_8_CERTIFICATE.json`. Input generation used the literal frozen signed-native expansions, preserving the original source pin. `BUILD_EC49FCY_TRIES.py` emits eight complete labelled trie instances; `EXACT_PREFIX_TRIE_DP.cpp` is the actual separately implemented C++ recurrence. Local validation used Python 3 and `g++ -O3 -std=c++17`; all eight runs returned 158. Three control runs using the same program reproduced the published six-slot case (a=16,H6:1,H7:1) and the two independent three-slot boundary domains, each giving 158. The C++ engine is independent of EC49FCX's Python DP implementation, though both consume the same declared frozen model. Original witness replay is given by the 24 frozen words; exact union cardinality was independently checked as 158 in input generation.

To reproduce from this directory: `python BUILD_EC49FCY_TRIES.py /tmp/ec49fcy_input`; `g++ -O3 -std=c++17 EXACT_PREFIX_TRIE_DP.cpp -o /tmp/ec49fcy_dp`; `for f in /tmp/ec49fcy_input/*.trie.txt; do /tmp/ec49fcy_dp "$f"; done`. The frozen source is read from the sibling EC49FCS directory of this same branch; its immutable Git blob is identified above.

## Frontier and next question

These eight seven-slot results are distinct from the previously reported 8,284 five-slot results and 32 six-slot results. Follow-up EC49FCZ: vary H6 or H7 across its other frozen signatures while retaining all carrier slots in each branch, or add a second H6/H7 replacement to obtain eight-slot domains; seek an explicit <158 legal witness or certify more exact minima with a separate computational implementation. A separate line may change the legal L/M cache-key regime, declaring the changed model and total construction cost. The complete nine-window 93-edge mother target remains open.

GitHub author-side publication is source preservation, not Source CLAIM, Source Result or independent Driver admission. At this run the native backend returned BACKEND_IDENTITY_OR_VERSION_MISMATCH, operation_sent=false; current active owner is unconfirmed. No registered execution authority is claimed.
