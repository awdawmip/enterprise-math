# EC49FDG — split H8/H9 BRC cache keys: exact 106-edge minimum for 800 finite models

Date: 2026-11-07. Status: **AUTHOR_EXACT_FINITE_RESULT / EXECUTED / UNREVIEWED / NOT_ADMITTED**.
Frozen scientific input: `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`.
Frozen signed primitive/observer source: `EC49FCZ_H4H6H7_SIGNATURE_COMPLETE_128/frozen_model.py`, Git Blob `7e97065ac9a0ff70435b92ee2f4bd718c9bf1859`.
This is a project-side extension of EC49FDF's exact common-key 112 result; P000 and ACTIVE worldview are unchanged.

## Result

Keep all 24 observation labels, the nine-state DFA and complete ordered **six-axis signed primitive prefixes**. Fix H2:16=`fe`, H2:32=`ge`, H3:16=`feg`, H3:32=`gef`; give H4/H5 the same early key `L=(4,2,1)`, H6/H7 the same late key `M=(6,4,1)`. Allow H8 and H9 to use **independent** integral BRC cache keys `K8,K9`, requiring their individual operation counts to be nonnegative and *all required observer endpoint signatures* to be realizable. At each label, every valid ordered operation word in that label's key-specific language is freely selectable.

**Exact finite theorem:** There are exactly 50 feasible H8 keys and 16 feasible H9 keys. For each of the 800 pairs, a complete all-candidate-label-mask signed-prefix-Trie dynamic program gives the exact minimum number of distinct nonempty native signed prefixes. The minimum over all 800 pairs is **106 edges**, attained for 10 pairs:

`K8=(6,5,1)` or `(7,4,1)`; independently `K9=(4,6,1),(5,5,1),(6,4,1),(7,3,1),(8,2,1)`.

This improves the preceding common late-key 112-edge construction by **six** edges within the new horizon-specific model. The other 790 exact optima and all 800 values are preserved in `FULL_800_MATRIX.txt`.

### Explicit complete 106-edge witness

The H2/H3 words are the four fixed words above. The other 20 **operation words** (before literal signed primitive expansion), with `K8=(6,5,1), K9=(6,4,1)`, are:

```text
4:1   gefd       4:2   fegd       4:4   fegc       4:8   gefc
5:16  feggf      5:32  geffg
6:1   gefddd     6:2   fegddd     6:4   fegccc     6:8   gefccc
7:1   gefddgf    7:2   fegddgf    7:4   fegccfg    7:8   gefccfg
8:1   gefddgfg   8:2   fegddgfg   8:4   fegccfgg   8:8   gefccfgg
9:16  feggffgfg  9:32  geffggffg
```

Each word has the declared operation count, its H label's terminal signature, and its exact signed primitive expansion from the frozen source. A direct string-prefix union of the 24 expansions contains 106 nonempty prefixes. Omitting H8 gives 98 prefixes, and the four listed H8 words add exactly two new prefixes each.

## Coverage / proof method

For horizon `h` and key `(x,y,z)` let `a=z-1; e=z; b=c+d=x+y-h-1; f=h+1-y-2z; g=h+1-x`. For each `c=0..b`, enumerate every ordered permutation of the exact multiset `(a,c,d,e,f,g)`, following the pinned nine-state transition table and discarding the dead state. Nonnegative counts imply `z>=1, 1<=x<=h+1, 0<=y<=h+1-2z, x+y>=h+1`. These bounds exhaustively enumerate every integer key for each individual horizon. Requiring all four H8 (or two H9) terminal labels yields 50 (or 16) keys.

Let `F` be the 16 fixed H2/H3 signed prefixes. Make a Trie of *all* legal candidate signed-native words for H4–H9, with a 20-bit label mask at each terminal. Each edge has cost 0 iff its complete prefix is in `F`, else cost 1. At node `v`, `D_v(S)` is the least additional edge cost when selecting exactly the labels in `S` below `v`. Initialize all submasks of terminal labels at cost zero. Merge each child with **disjoint** masks `A,B`:

`D_new(A∪B) = min(D_old(A)+D_child(B)+w_child*[B != ∅])`.

By induction on Trie height, selecting disjoint labelled terminal subsets covers each admissible assignment exactly and charges each distinct prefix edge once; the root full-mask optimum plus `|F|` is exact. No random optimization, floating point, limited word samples or heuristic cutoffs are involved.

A newly compiled `DP_EC49FDG.cpp` was run on all 800 keys; the 800 output optima are preserved in the 50×16 matrix and the full per-case author evidence package. Total DP state-pair inspections: **14,881,638,748**; largest signed Trie: **118,203 nodes**. For the concrete minimizer `K8=(6,5,1),K9=(6,4,1)`, C++ reports 106 at 31,159 Trie nodes / 5,492 candidate words / 21,984,948 inspected state pairs. An independent Python literal-string Trie DP of this full 20-label model also produced exactly 106 (1,048,576 root mask states, 21,984,948 inspected pairs). A separately generated signed-prefix witness is checked independently of the optimizer.

## Evidence and reproduction

`VERIFY_EC49FDG.py` reproduces the complete horizon-specific key classes, all candidate operation languages, direct witness and exact cases. `DP_EC49FDG.cpp` is the exact integer solver. Compile with `g++ -O3 -std=c++17 DP_EC49FDG.cpp -o exact_solver`, then run `python VERIFY_EC49FDG.py --case 6,5,1 6,4,1` or `python VERIFY_EC49FDG.py --all`. The full run writes `EXACT_REPLAY_EC49FDG.json`, including full per-case counts.

Author-side complete original 800-case JSONL SHA-256: `0ca4669cd009d1a0af5507b87e2172470ae98bf4e6ec6181e16fad72c6b50e2a`. Published compact matrix SHA-256: `c76ff2019dde4d4ac3249d61ea3a9b8f36fcf916cdd4ed801713b4766181ae92`. The matrix provides every optimum; raw rows also preserve the pair-level candidate and Trie counts in the local handoff bundle. Evidence is author-side until an independent Driver review.

## Next EC49FDH

Open H6/H7 to independent legal BRC keys, first keeping the 106-edge H8/H9 pair fixed, and look for a <=105 full 24-label explicit witness or a new exact lower bound. Alternatively examine an H4/H5 key split or a new native primitive language with the same full observer/provenance semantics. The nine-window 93-edge mother target remains open.

## Authority and admission

The connected GitHub identity can write the existing research PR branch, but native Enterprise Math `em_status` returned `BACKEND_IDENTITY_OR_VERSION_MISMATCH`, `operation_sent=false` in this run. There is no confirmed native owner/CLAIM/Source Result, nor an independent mathematical Driver review. The current publication is author-side durable evidence.
