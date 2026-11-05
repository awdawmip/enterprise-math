# EC49FBX — Exact two-early/one-late triple rigidity in native signed X6

Date: 2026-11-06. Scientific input frozen at `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Parent: EC49FBW `1eaf17da5dd0f26c9ab6e600cd40324749f37c3c`; the 158-edge source witness is EC49FBU `b3b43ef6abe2fd816d979792d18a67ee5d0aad50`. This is an **author-side exact finite certificate**.

## Theorem

Fix the 24 signature-indexed native operation words of EC49FBU; fix H2/H3 and positive BRC keys `L=(4,2,1,0,0,0)` at H4/H5, `M=(7,3,2,0,0,0)` at H6–H9. Retain the frozen nine-state DFA and the signed native-X6 primitive expansion of each operation. The primitive-prefix union cost of the witness is exactly 158.

Choose **any two distinct required signature slots** from the ten H4/H5/H6 slots, and **any one** of the ten H7/H8/H9 slots. Replace precisely those three selected words by arbitrary valid words for each respective window, exact full positive-BRC key, and terminal DFA signature. Keep the other 21 slots fixed. **Every one of the 450 such three-slot neighborhoods has exact minimum cost 158.**

Together with EC49FBW's 120 all-early triples, the exact local optimum 158 is established for every three-slot replacement containing *at least two H4/H5/H6 slots*: 570 of the 1140 possible unordered signature-slot triples. EC49FBV establishes all one/two-slot replacements.

## Finite proof and pruning certificate

The operation alphabet is `acdefg`; its native signed-axis expansions are `a=(-1,-1)`, `c=(1,2,-1,-2)`, `d=(2,1,-2,-1)`, `e=(3,1,1,-3)`, `f=(1,-1)`, `g=(2,-2)`. These are ordered steps along six native axes, with no projection to endpoint-only data. The frozen DFA transitions and signature map are embedded in the verifier. For horizon `h` and key `(x,y,z)`, the exact operation counts obey `b=x+y-h-1`, `#a=z-1`, `#e=z`, `#c+#d=b`, `#f=x-b-2z`, `#g=y-b`. Exhaust all `#c` splits and their valid operation words, retaining precisely the required DFA signatures.

For a triple of slots, let `R` be the signed primitive-prefix set of its other 21 fixed words. For a valid replacement `w`, let `B(w)` be its full prefix-bitset. The exact cost is

```
|R| + popcount((B(w1) | B(w2) | B(w3)) & ~B(R)).
```

The prefix-to-bit correspondence is injective and includes the ordered native signs. Define `a=B(w1)&~B(R)`, `b=B(w2)&~B(R)` and `cut=158-|R|`. If `popcount(a|b)>=cut`, **every third word** has cost at least 158, by monotonicity of set union. Those pairs may be omitted when searching for a strict improvement. For all remaining pairs the verifier enumerates every possible third word and computes exact bit counts. Every triple's fixed original witness attains 158. This gives matching upper and lower bounds of 158 for every group.

## Actual exact run and independent spot checks

`python3 VERIFY_EC49FBX.py` generated `EXACT_REPORT_EC49FBX.json` and returned **PASS**: 450 triples, **258,552,000** full Cartesian combinations, **2,105,760** combinations enumerated after sound monotonic pruning, 162,000 early candidate pairs considered, 160,540 pairs ruled out for strict improvement, and minimum 158 throughout. Candidate counts by horizon and signature are included in the compact saved certificate.

A separately executed **unpruned Cartesian** cross-check (using independent residual-prefix masks) tested:
- `(4:1,5:16,7:2)`: 103,680 combinations, minimum 158;
- `(5:32,6:1,8:8)`: 1,134,000 combinations, minimum 158;
- `(6:1,6:4,9:32)`: 1,512,000 combinations, minimum 158.

The exact Python verifier is the reproducible proof program; `EXACT_SUMMARY_EC49FBX.json` is its compact publication certificate. Running the verifier regenerates the complete per-group report.

## Next unresolved question

The remaining 570 three-slot neighborhoods consist of 450 with one early plus two late slots, and 120 entirely in H7/H8/H9. A branch-and-bound or exact prefix-trie search can cover these without changing the frozen observer, key, or signed-native objective. Coordinated changes of at least four slots and alternative cache schedules remain independent routes toward the full nine-window mother objective. No formal Driver admission is claimed.
