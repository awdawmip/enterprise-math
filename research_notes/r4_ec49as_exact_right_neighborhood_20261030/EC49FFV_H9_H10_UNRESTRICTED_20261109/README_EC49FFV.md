# EC49FFV — H2/H9 and H2/H10 exact unrestricted-key native BRC optima

**2026-11-09 · AUTHOR_EXACT_FINITE_CERTIFICATE · EXECUTED_INTEGER_DP · UNREVIEWED / NOT_ADMITTED.** Frozen science input: `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Original signed native X6 / nine-state observer: EC49FFU source blob `0add7216c2f636ff28a79b4eb0a7a7b4989b05d1`.

## Theorem

For two observation windows H2 and Hh, at each window realize the four original BRC signatures {1,2,4,8} with one legal word per signature, each word having a positive complete key K=(x,y,z). Count the union of all nonempty **ordered signed native X6 microstep prefixes**. Permit **arbitrarily many** distinct complete cache keys for all eight paths.

The exact global minima are

```
C_min(H2,H9) = 77
C_min(H2,H10) = 82.
```

Both minima are realized with **exactly two complete keys** (the minimum feasible key count): H2 necessarily has key (3,1,1), which cannot support any length-9 or length-10 word.

These are finite exhaustive theorems under the frozen BRC model. H10 closes the prior 82-edge upper-construction gap; H9 extends the earlier fixed-H9-key 77 classification to *all possible multi-key* solutions.

## Original model and exact lower certificate

Native operation words: a=(-1,-1), c=(1,2,-1,-2), d=(2,1,-2,-1), e=(3,1,1,-3), f=(1,-1), g=(2,-2). For an h-letter word with complete key (x,y,z), the legal quotas are

```
#a=z-1, #e=z, #c+#d=x+y-h-1,
#f=h+1-y-2z, #g=h+1-x.
```

Enumerate all positive keys satisfying nonnegativity, all splits of #c+#d and every distinct operation permutation. The original nine-state DFA selects terminal signatures 1,2,4,8. Every operation word has exactly one complete key, so this enumerates the complete finite input without a key-number assumption.

H2's four low-signature words are exactly sig1=de, sig2=ed, sig4=ce, sig8=ec, all at (3,1,1), and they have 28 distinct nonempty signed prefixes. Insert *all* h-window legal low-signature words of all keys into **one unified signed-prefix trie**. Charge an edge zero if and only if its **whole prefix** is one of the 28 H2 baseline prefixes, one otherwise. At a terminal record its attainable signature bit.

For node v and demand mask M in {0,...,15}, D_v[M] is the minimum additional selected edge count for covering the mask below v. Initialize D_v[0]=0 and D_v[M]=0 for a nonempty subset M of signatures terminating exactly at v. Merge each child u by

```
next[A|B] = min(next[A|B], D_v[A]+D_u[B]+cost(v,u))
for A&B=0, B!=0;
```

and allow skipping a child. Disjoint assignment is complete because duplicating a signature demand never helps an optimum. Every selected path is a root-to-terminal path, and the objective counts each selected prefix exactly once. The recurrence therefore proves a **global lower bound**, and reconstructing a legal four-word witness proves attainment. Final answer: 28+D_root[15].

## Exact machine output and direct witnesses

| h | nonnegative-quota positive keys | keys with low-signature candidates | candidate words | shared-trie nodes | reachable DP mask states | exact cost |
|--:|--:|--:|--:|--:|--:|--:|
| 9 | 90 | 70 | 625,050 | 3,081,383 | 6,289,168 | **77** |
| 10 | 120 | 95 | 3,091,460 | 15,180,307 | 30,843,840 | **82** |

An H9 witness, all at key (10,1,1): sig1 `defffffff`, sig2 `efffffffd`, sig4 `cefffffff`, sig8 `efffffffc`.

An H10 witness reconstructed by unrestricted DP: sig1 `gfffffffed`, sig2 `ffffffffed`, sig4 `ffffffffec`, sig8 `gfffffffec`. It uses large-window keys (10,2,1) and (11,1,1). A simpler **two-key-total** witness, from EC49FFU and checked anew, uses H2 key (3,1,1) plus H10 key (4,8,1): sig4 `fegggggggc`, sig2 `fegggggggd`, sig8 `gfeggggggc`, sig1 `gfeggggggd`, exactly 82 prefixes.

## Validation and continuation

`exact_multikey.cpp` is an actually executed C++17 complete enumeration + DFA + signed-prefix-trie + integer-subset-DP program. `verify_witness.py` independently recomputes each selected word's DFA signature, complete key, signed X6 displacement, and direct native prefix-union count. It also checks the two-key H10 construction. The exact algorithm was regression-tested at h=3,...,8 against independent EC49FFT global optima (36,44,52,59,65,71). The H9/H10 run reports and witness report are attached. The trie implementation keeps a missing-base-prefix sentinel, avoiding any false re-entry into the baseline trie.

**Scientific next:** test H11 with resource-aware tail compression, seek an infinite-h lower certificate or an improved family, and apply these reusable H2/Hh subquota bounds to the original frozen **22-demand** problem including H3 high signatures and the requirement of <=5 complete keys and <=93 native-prefix edges. Exact Result/Driver admission and any active Owner/CLAIM remain governed separately by Source.