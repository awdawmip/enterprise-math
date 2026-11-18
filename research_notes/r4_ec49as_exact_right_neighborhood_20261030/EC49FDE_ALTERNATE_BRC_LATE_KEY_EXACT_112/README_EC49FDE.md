# EC49FDE — changed BRC late cache key: exact 112-edge optimum

Date: 2026-11-07. **Scientific baseline frozen pin:** `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`.
Class: **AUTHOR_EXACT_FINITE_THEOREM / EXPLICIT_24_SLOT_WITNESS / UNREVIEWED / NOT_ADMITTED**.
Predecessor: [EC49FDD complete fixed-key 20-slot theorem](../EC49FDD_FULL_H4_H9_20_SLOTS/README_EC49FDD.md).

## Result

The previous key `L=(4,2,1), M=(7,3,2)` has an exactly established 158-edge minimum with H2/H3 held fixed and H4..H9 (20 slots) freely varying under their own full endpoint-signature languages. This experiment **preserves the same signed six-axis primitive alphabet, nine-state DFA, 24 slot labels, and every H2/H3 literal word**, but sets the late key to **`M'=(6,4,1)`**, retaining `L=(4,2,1)`. All H4..H9 word choices again vary independently in *complete* legal multiset/signature languages under the indicated key.

**Exact theorem:** The changed-key 20-variable signed-primitive-prefix union minimum is **112 edges**. This is a genuine **46-edge decrease** relative to the different fixed-key 158-edge problem. The nine-window 93-edge mother objective remains open.

## Why the new key is admissible

For horizon `h` and key `(x,y,z)`, the frozen typed word language is generated with counts
`a=z-1, e=z, c+d=x+y-h-1, f=h+1-y-2z, g=h+1-x`.
These counts are all nonnegative at every `h=6,7,8,9` for `(6,4,1)`; `c,d` range over all nonnegative splits of their sum. The exact frozen 9-state DFA is applied to every ordered word, dropping dead state 8 and retaining labels `1,2,4,8` for H6–H8 and `16,32` for H9. Each required label has at least one word. All 20 variable slots and each fixed H2/H3 word therefore have valid signatures.

## Witness

The complete 24-label witness comprises H2:16=`fe`, H2:32=`ge`, H3:16=`feg`, H3:32=`gef` and the 20 variable-label words included in both `VERIFY_EC49FDE.py` and `EXACT_RESULTS_EC49FDE.json`. A literal independent signed-primitive prefix-set calculation counts **112** distinct nonempty prefixes. It retains order, signs, branch labels and exactly one full word per designated slot.

## Exact lower bound (all candidate words)

Keep the 16 distinct original H2/H3 signed primitive prefixes as the zero-cost fixed set `F`. Insert **all 4,372 labelled legal H4..H9 words** into a signed-letter prefix Trie, producing **26,705 nodes**. The incoming edge cost is 0 if its entire signed prefix is already in `F`, else 1.

At each Trie node `v`, let `D_v(S)` be the minimum added cost of choosing precisely the variable slot labels `S` from terminal words in that subtree. Initialize all subsets of the terminal mask at cost 0. When combining a child `u`, minimize over disjoint masks `A,B`:
```
D_new(A | B) = min(D_new(A | B), D_old(A)+D_u(B)+edge_cost(u)*[B != 0]).
```
The disjointness condition prevents selecting two words for one label; subtrees have disjoint non-root signed prefixes, so each used incoming edge is charged exactly once. Structural induction gives complete correctness. Exact root full-mask result is **96 new edges**; adding `|F|=16` gives **112**.

The independent Python dictionary DP checks **21,972,032** mask pairs, **5,977,571** compatible pairs and all **1,048,576** root masks, with optimum 112. A locally compiled C++ sparse-mask DP adapted without changing the recurrence also returns 112 at cap 112 and unrestricted cap 300; cap 111 yields no full-mask solution. Python and C++ use different DP representations. The evidence archive contains both executed programs and complete local reports.

## Complete integer late-key census (same typed key family)

Nonnegative H6–H9 counts imply `z>=1, x<=7, y+2z<=7, x+y>=10`, yielding exactly **seven** integer triples. Enumerating all seven and then requiring every terminal signature gives four feasible keys. Full 20-variable exact Trie DP yields:

| Late key M | All 14 late labels feasible? | Exact 20-variable optimum |
| --- | --- | ---: |
| (5,5,1) | Yes | 138 |
| **(6,4,1)** | **Yes** | **112** |
| (6,5,1) | No: H9:16 and H9:32 empty | — |
| (7,3,1) | Yes | 138 |
| (7,3,2) | Yes (original key) | 158 |
| (7,4,1) | No: H9:16 and H9:32 empty | — |
| (7,5,1) | No: H9:16 and H9:32 empty | — |

Consequently **112 is exact across this entire finite integer late-key family**, with early key L and H2/H3 words fixed and all H4..H9 slots allowed full legal variation. The census enumerator, compiler source, numerical certificate and 112 literal signed prefixes are in the accompanying evidence package; its full data are summarized in `EXACT_RESULTS_EC49FDE.json`.

## Reproduction and source boundaries

`VERIFY_EC49FDE.py` imports the **unchanged** [frozen_model.py](../EC49FCZ_H4H6H7_SIGNATURE_COMPLETE_128/frozen_model.py) (Git blob `7e97065ac9a0ff70435b92ee2f4bd718c9bf1859`) for primitive signs and nine-state observation, and replaces only the explicitly experimental late key in local candidate generation. Run from this folder using `python VERIFY_EC49FDE.py`. The existing [FDD C++ solver](../EC49FDD_FULL_H4_H9_20_SLOTS/SPARSE_PREFIX_TRIE_DP.cpp) is reusable unchanged on the trie generated by the companion census script in the evidence package.

The fixed baseline is still `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`; the alternative late-key value is a **new investigated parameter**, not a silent change to baseline data. The selected model is static six-axis native path combinatorics; its output does not automatically assert any heartbeat dynamics. P000 and the ACTIVE worldview remain unchanged.

**Next EC49FDF:** Let H2/H3 also respond to a consistent changed early key rather than staying fixed, or expand the admissible signed primitive operations while preserving the observer and provenance. Seek a fully typed 93-edge 24-word witness or determine the next exact obstruction. Owner, formal CLAIM, native Result and independent Driver review require separate real Source authority.