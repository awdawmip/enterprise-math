# EC49FBP — Exact six-signature H8/H9 native prefix-union costs

Date: 2026-11-05. Research line: EC49AS nine-window, native signed six-axis X6 and complete positive BRC key. Frozen scientific input: `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Scientific continuation: EC49FBO at `d7b6ddda14389e465ef3881a84ba5b10027fab5f`. The full H2–H9 five-key mother question remains open.

## Finite theorem (proved by exhaustive exact trie DP and independently executed implementations)

Fix the original six primitive operation expansions:
`a=(-1,-1), c=(1,2,-1,-2), d=(2,1,-2,-1), e=(3,1,1,-3), f=(1,-1), g=(2,-2)`, where `±i` is an oriented unit step on signed native axis `i` of the six-axis model.

Use the frozen nine-state observer transition table and signatures `1,2,4,8` at H8 and `16,32` at H9. Let `M=(x,y,z,0,0,0)` satisfy `x+y=10, 1<=z<=4, 2z+1<=x<=9`. This is the complete 16-key population permitting H9 F/G. Every valid word at these windows has exactly `18+2z` native primitive steps.

Define `C_89(M)` as the minimum number of *distinct oriented primitive-prefix edges* in a union of observer-accepted complete H8/H9 paths carrying all six required signatures. The exact value on all 16 eligible keys is:

| z | x (y=10-x) | C_89(M) |
|---|---|---|
| 1 | 3, 9 | 86 |
| 1 | 4,5,6,7,8 | **54** |
| 2 | 5, 9 | 94 |
| 2 | 6,7,8 | **58** |
| 3 | 7, 9 | 102 |
| 3 | 8 | **62** |
| 4 | 9 | 132 |

Equivalently, for `z<=3`, interior keys `2z+2<=x<=8` have `C_89=50+4z`; edge keys `x=2z+1` or `x=9` have `C_89=78+8z`. For `z=4`, the sole key `(9,1,4)` has 132.

## Exact domain and lower-bound certificate

From the complete key/count relations, each H8 word has `a=z-1, e=z, f=x-2z-1, g=y-1, c+d=1`. H9 has `a=z-1, e=z, f=x-2z, g=y, c+d=0`. Generate *all distinct ordered operation words* with the former counts (both c and d), and the latter counts; run each through the frozen nine-state DFA, retaining H8 signatures 1/2/4/8 and H9 signatures 16/32. Expand every accepted operation word into its **ordered signed native-axis primitive path**, without projecting away axis, sign, order or branch provenance.

Insert all paths into a rooted oriented-edge prefix trie. Each accepted terminal is marked by its signature bit. At every node `v`, store for each of the 64 masks `S` the minimum count of descendant edges needed to connect `v` to a set of terminals whose union of signatures is exactly `S`. Initialize mask zero with cost zero; a terminal's singleton mask with cost zero. Combining a nonempty child mask adds its exact child cost plus the one connecting edge. Combine sibling masks by bitwise OR and take the minimum. Tree induction proves the DP computes the true minimum for each mask; at root mask 63 is `C_89(M)`. All edge weights are nonnegative, so one terminal per required signature suffices for an optimum.

Both scripts enumerate the original DFA/complete-key word populations and independently execute the exact prefix-trie DP; all 16 minimum costs, signature populations and trie node counts agree. `EXACT_REPORT_EC49FBP.json` preserves every result, per-signature candidate counts and six exact word witnesses for each key. The witness set is independently checked by recomputing the signed native endpoint and the primitive-prefix edge union, giving the recorded upper bound that matches the exact DP lower bound.

## Example witnesses and interpretation

For `M=(7,3,2)`, the minimum union is **58** primitive edges. One optimal selection is:
- H8: `gaeeffgd` (sig 1), `faeefggd` (sig 2), `faeefggc` (sig 4), `gaeeffgc` (sig 8).
- H9: `faeefgggf` (sig 16), `gaeeffggf` (sig 32).

The pairwise H8/H9 overlap bound of EC49FBO does not alone determine six-path union cost. In particular, `M=(9,1,4)` has `C_89=132`, while the middle keys at z=1 achieve 54. Shared-prefix *arrangement across all six observer signatures*, not raw candidate population or one longest-overlap pair, determines the optimum. This exact finite result is scoped to H8/H9 and the fixed original DFA; it is a reusable local certificate for full nine-window optimization.

## Verification

Run `python VERIFY_EC49FBP.py` to regenerate the full exact report; run `node CROSSCHECK_EC49FBP.js` for the independent Node.js implementation. The two originally executed programs agreed on all 16 keys (including per-signature counts and trie node counts). The report's `optimal_words` are actual native path constructions, not synthetic optimizer masks. Source identity is GitHub connector user `awdawmip`; formal Source CLAIM/Result and independent Driver admission remain under the separate service role boundary.

## Next question

Integrate the 16 exact local costs and selected witnesses into the 27+28 rank-feasible complete H2–H9 key schedules (EC49FBM), measuring **full shared-prefix union** rather than summing separate window costs. Search for a complete legal construction with at most 93 native edges, or certify a larger candidate class's best cost. Preserve the H2/H3 fixed root and five-key budget for the initial controlled experiment, then broaden the root structure.
