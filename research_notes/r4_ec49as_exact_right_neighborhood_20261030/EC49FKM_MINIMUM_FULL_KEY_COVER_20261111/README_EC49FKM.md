# EC49FKM — exact minimum full raw-key covering number for the frozen signed-X6 BRC catalogue

Date: 2026-11-11. Research status: author-side finite exact theorem and independently executed arithmetic audit; independent Driver review pending.
Frozen scientific input: `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Existing primitive/candidate sources: the `EC49FGW_RADIUS5_SCREEN.py` nine-state BRC enumerator and `EC49FGJ_SEVEN_KEY_94_WITNESSES.json` in the sibling `EC49FJD_RELEASE_B11_COMPLETE_20261111/` directory of PR #1730. Inputs and 24 observation labels are unchanged.

## New theorem — five full raw keys suffice, and four do not

Consider all 178,850 admissible ordered words in the frozen catalogue, each with its uncompressed full raw key `k(w)=(number of +E1,+E2,+E3 native steps)` and labelled observer `(window,signature)`. There are 94 distinct complete raw keys and 24 required labels. Let a key cover a label if at least one admissible literal word with that key yields that label.

The smallest set of keys covering **all 24 labels** has size exactly **5**. Moreover, all inclusion-minimal five-key covering sets are **exactly the following 16 sets**:

```
K0 = {(2,1,1), (3,0,1), (3,1,1)}
U  = {(3,3,1), (4,2,1), (5,1,1), (5,1,2)}
V  = {(5,5,1), (6,4,1), (7,3,1), (7,3,2)}
Solutions = { K0 union {u,v} : u in U, v in V }.
```

### Lower-bound proof with five mutually incompatible observation labels

Take `S={(2,16),(2,32),(3,16),(4,1),(7,1)}`. Direct complete enumeration gives respectively `1,1,2,7,34` raw keys capable of meeting these labels; the five key families are pairwise disjoint. Thus each of these five labels needs a *different* raw key, proving `key_count >= 5` for any complete solution, irrespective of its native prefix cost. This is a key-incidence statement; no unsigned endpoint or scalar cache-key collapse is used.

At exactly five keys every solution must select one member from each of those five disjoint families. Their Cartesian product has `1*1*2*7*34=476` choices. For each combination, OR the exact 24-bit observation masks from all catalogue words possessing the selected keys. Exactly 16 combinations cover every label; they equal the parameterized sets above. Thus this enumerates all five-key possibilities, including the impossibility of four keys.

An explicit complete 24-word solution using `K0 union {(3,3,1),(5,5,1)}` has **136** distinct ordered, signed native-X6 nonempty prefixes. This is a feasible upper bound at five keys, **not** a claim that 136 is optimal within that fixed key set. The previous seven-key 94-prefix witnesses remain the known better prefix-cost constructions.

## Execution and reproduction

1. `python VERIFY_EC49FKM.py`: independently enumerates the generator's 178,850 legal words; computes 94 key/24 label incidence, exact five-label disjointness and all 476 candidate quintuple covers; independently validates the supplied 24-word, 136-native-prefix construction.
2. `g++ -std=c++17 -O2 INDEPENDENT_BRUTE_X6.cpp -o /tmp/ec49fkm && /tmp/ec49fkm`: separate C++ DFS of all admissible 6-operation words up to length nine, independently checking DFA transitions, signed six-axis net displacement, key counts, label supports and all 476 quintuple combinations. Actual run printed `INDEPENDENT_BRUTE_ALL_WORDS 178850 keys 94 labels 24 patterns 21` and `EXACT_FIVE_KEY_SETS 16`.
3. `EXACT_RESULT_EC49FKM.json` states the exact identities and the complete 24-word constructive witness. The frozen input pin remains unchanged. All counted words come from the BRC/X6-specific typed paths, with no pi, trigonometry, matrix exponential or unrelated number generator.

## Follow-on scientific question

Can the sixteen exact five-key keysets be assigned all 24 BRC demands with fewer than 136 signed native prefixes, or can a rigorous lower bound exceed 93 for every one? Then test six-key sets; eventually global question `C_min(7) ?= 94`. Incidence-optimality (fewest raw keys) and prefix-optimality are distinct objectives, and this finite theorem provides a globally valid key-side reduction.

**Provenance and authority:** author-side standalone research, same PR #1730, original task family EC49AS; this publication does not assert a current immutable Task CLAIM, formal Result, independent Driver acceptance, or P000 amendment. The authenticated native research activity for this run is `RA-A71834BDE6B74E1F7BED9D6A`, Researcher-ID `EM-DIRECT-AC5248`. Source activity and GitHub artifact persistence are separately tracked.
