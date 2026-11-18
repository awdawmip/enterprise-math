# EC49FAV — Exact H2/H3 cache-key/edge Pareto theorem and a restructured nine-window construction

Date: **2026-11-05 (Asia/Shanghai)**. Prior author-side frontier: EC49FAU at `f5dd5d5c85a757c7060cb9b0e96bd8ef2c6e411c`. Frozen scientific input: `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Status: author-side exact finite theorem plus a full legal alternative construction, pending Source/independent Driver admission.

## Problem and exact result

Use the frozen seven operations as ordered signed native-X6 primitive steps:

```text
a=(-1,-1); b=(-2,-2); c=(+1,+2,-1,-2); d=(+2,+1,-2,-1)
e=(+3,+1,+1,-3); f=(+1,-1); g=(+2,-2)
```

A horizon-h path is a length-h operation word with native displacement `(+2,0,0,0,0,0)`. Its full six-coordinate positive BRC key counts positive occurrences of each native axis in its **ordered primitive expansion**. The permitted nine-history observer signatures are D=`de`, E=`ed`, C=`ce`, J=`ec`, F=`feg`, G=`gef`; at each horizon rational rank 9 is equivalent to EC49FAR's exact four clauses `(E or F) and (C or F) and (D or G) and (J or G)`. Each nonempty ordered **signed primitive** prefix costs one edge, counted once across all selected words.

Let `L23(k)` be the minimum number of distinct primitive-prefix edges among *all* H2 and H3 selected families with rank 9 at each horizon, using at most k distinct full positive BRC keys across the two horizons. The exact Pareto frontier is

| maximum distinct full keys | 1 | 2 | 3 | 4 | 5 |
|---|---:|---:|---:|---:|---:|
| **exact minimum edges** | **42** | **31** | **16** | **16** | **16** |

For k=1 one attaining witness is H2=`ce,de,ec,ed`, H3=`feg,gef` (42 edges). For k=2 it is H2=`de,ec,fe`, H3=`feg,gef` (31 edges). For k=3 the family H2=`fe,ge`, H3=`feg,gef` has **16 edges**, and 16 edges is the unrestricted minimum even at k=4 or k=5. The three full keys of this witness are `(2,1,1,0,0,0)`, `(3,0,1,0,0,0)`, `(3,1,1,0,0,0)`.

## Exact proof and certificate coverage

The native endpoint condition forces `#b=0` (operation b is the only unbalanced negative E2 operator) and `#e=#a+1`. Thus all legal H2/H3 candidates appear in complete literal enumeration of respectively `6^2` and `6^3` ordered words over `a,c,d,e,f,g`. The original nine-history DFA filters these to **6** permitted H2 words and **38** permitted H3 words (8 distinct full keys over the combined pools). Of the 63 nonempty H2 subsets, exactly **25** meet rank nine.

For each of those 25 H2 selections S2, the program computes the exact native prefix set `P(S2)` and uses it as free edges while optimizing the H3 primitive trie. At each trie node the DP state `(m,q)` records the **bitwise OR** of six signature bits and of eight full-key bits over chosen terminal words, and its value is the minimum number of additional charged primitive edges. Choosing nothing has state (0,0) and cost 0. At an eligible leaf a selected word contributes its exact signature/key bits. Independent child states combine by OR on both masks and addition on costs; a selected nonfree node pays 1 edge. By induction from the leaves, this min-plus recurrence is exact over every possible H3 subset. The H3 states satisfying all four rank clauses are evaluated against the union of H2 and H3 keys, and minimized over all H2 choices. The resulting five minima are the table above. **This is exhaustive over the declared two-horizon finite domain**, not a heuristic search.

The delivered `VERIFY_EC49FAV.js` was executed directly in a V8 JavaScript runtime and its actual output is `EXACT_REPORT_EC49FAV.json`. Independently, a Python standard-library implementation of the trie DP produced the same five values, and a distinct SciPy/HiGHS binary integer model encoded all native word/prefix/key/observer constraints. HiGHS returned **optimality status 0, zero MIP gap** at budgets 1,2,3,4,5 with values **42,31,16,16,16**. The independent checker and report are adjacent artifacts. The JS checker is reproducible with Node.js >=18, with no external packages.

## Exact full nine-window witness — distinct from optimum search

A separate complete explicit construction keeps the 16-edge H2/H3 optimum and successfully extends it with just **two further full cache keys**:

```text
H2: fe, ge
H3: feg, gef
H4: fegc, fegd, gefc, gefd
H5: feggf, gefgf
H6: fegccc, fegddd, gefccc, gefddd
H7: fegccfg, fegddgf, gefccfg, gefddgf
H8: feggfgfc, feggfgfd, gefgfgfc, gefgfgfd
H9: feggfgfgf, gefgfgfgf
```

The verifier expands every word to **signed native-X6 steps** and checks all eight horizon lengths, the exact (+2 E1) endpoint, permitted six signatures, the rank-nine four-clause condition and full six-coordinate positive keys. The union has **112 native primitive-prefix edges**, exactly **five** full cache keys, and exactly six permitted signatures. Cumulative edge costs through H2,...,H9 are `12,16,32,38,70,82,106,112`. The H4/H5 key is `(4,2,1,0,0,0)`, and H6–H9 share `(6,4,1,0,0,0)`.

For the 16-edge H2/H3 witness, EC49FAM's lifespan formula bounds its original three keys to horizons at most 2,2,3; hence a full five-key completion may use only **two new full keys from H4 onward**. This explains the new resource tradeoff: 26 fewer early edges than the original one-key H2/H3 base, but two additional early keys consumed. The completed 112-edge construction proves that this different early profile is compatible with the original nine-window constraints, and supplies a reproducible point in the design space.

## Next research unit: EC49FAW

Jointly optimize H4–H9 using the remaining two full cache keys after the 16-edge H2/H3 witness. Consider the actual key-schedule example `(4,2,1)` for H4/H5 and `(6,4,1)` for H6–H9, and examine other feasible pair covers and first-horizon prefix reuse. Also compare the 31-edge at-most-two-key H2/H3 family where a third late key remains possible. Seek an exact **93-edge** complete construction or a rigorous lower bound on a declared restructured family. The unrestricted nine-window mother's previous author-side range remains `80 <= E*_H9 <= 94`.

Source version: global `main@74b16ebf12a1897da88c35563f0d500bd90b97e7`, Enterprise Math `main@325e8187ed2aa5656f04da794a5d3ae843d0b99a`. Current method: `research_priorities/research_method.json`; normative entry: `docs/RESEARCH_CONTINUATION_PROTOCOL.md#current-normative-context`. P000 and ACTIVE worldview unchanged. This authored study grants no task CLAIM, Result, or mathematical admission.
