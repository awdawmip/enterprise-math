# EC49FHE — exact released-cache-key five-path exclusion up to budget 15 (2026-11-11)

**Scientific input:** frozen `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. **Scope:** the original typed nine-state BRC observer; all 178,850 admissible length-H operator words for H2–H9; each word's ordered, signed native X6 microstep prefixes; 24 original observations; EC49FGJ seven-cache-key, 94-prefix witnesses A and B.

## Finite result

For each of witnesses A and B, select five labels Q to replace, leaving the other 19 original paths unchanged. Let F(Q) be their native-prefix union, and B(Q)=93-|F(Q)|. A complete replacement using at most seven full raw cache keys has native-prefix cost at least **94** whenever at least one of the witness's original seven keys is entirely released by Q and B(Q)<=15.

The 17,346 key-releasing five-label choices for **each** witness divide into:
- B(Q)=-1: 4,576 positions, fixed background alone costs 94;
- 1<=B(Q)<=15: **12,544 positions**, all excluded by exact finite enumeration and key-constrained prefix-set dynamic programming;
- B(Q)>15: **226 positions**, still to resolve (210 change both H9 observations; eight change only H9/16, and eight change only H9/32).

Of the previously unsolved **4,898** released-key positions per witness (EC49FGW through EC49FHD), **4,672** receive their first exact joint prefix/key exclusion here. The remaining count is **226** per witness. Prior work fully closes all five-label choices retaining seven keys. Taken together, the two witnesses are now confirmed local cost-94 minima for all radius-five changes except the explicitly listed 226 released-key positions each.

The 4,672 newly excluded positions per witness, grouped by B(Q), are B3:1248; B5:448; B7:50; B9:1780; B11:584; B12:244; B13:68; B14:40; B15:210. There are zero feasible 93-edge completions in these groups. The two witnesses yield **9,344** newly excluded witness/position instances (not 9,344 distinct global constructions).

## Proof of the exact finite reduction

Let E be the complete 94-prefix union of the witness and P(w) be all nonempty, ordered signed-native prefixes of a candidate word w. For the fixed 19 paths, F(Q) subset E. A replacement is 93-edge feasible exactly when there exist five BRC-legal words, one for each label in Q, such that

`|(P(w1) ∪ ... ∪ P(w5)) \ F(Q)| <= B(Q)`,

and `|K(F(Q)) ∪ {raw_key(wi)}| <= 7`.

To avoid scanning irrelevant candidate words for each Q, retain only words with `|P(w) \ E| <= B(Q)`. This is a **complete** filter because F(Q) subset E implies `|P(w) \ F(Q)| >= |P(w) \ E|`. A second exact filter retains words with `|P(w) \ F(Q)| <= B(Q)`. The original nine-state BRC catalog generator is not altered.

After these filters, process the five observation-label groups by dynamic programming. A state is `(U,N)`: U is the exact set of newly used signed-native prefixes outside F(Q), and N is the set of new full raw cache keys not already present among the 19 fixed words. For every candidate w with `D(w)=P(w)\F(Q)`, transition to `(U∪D(w), N∪({raw_key(w)}\K(F(Q))))` if `|U∪D(w)|<=B(Q)` and `|K(F(Q))|+|N|<=7`. Identical new-key-set states admit subset dominance: `U1⊆U2` implies any later union feasible from U2 is also feasible from U1. The DP thus tests existence exhaustively without a positive candidate being lost.

As a separate necessary screen, an exact five-label key-coverage DP tests whether the filtered groups can be covered using the available new-key slots. This may reject a position earlier; all positions counted as **new joint exclusions** passed singleton and key-only coverage, so their exclusion is additional scientific information.

## Exact computation and evidence

`VERIFY_EC49FHE.py` uses the frozen `EC49FGW_RADIUS5_SCREEN.py` and `EC49FGJ_SEVEN_KEY_94_WITNESSES.json` from the sibling `EC49FGW_RADIUS5_EXACT_SCREENS_20261110` directory. The original generator yields exactly 178,850 BRC-legal words. Execute `python VERIFY_EC49FHE.py` to generate the full per-case JSON `EC49FHE_EXACT_REPORT.json` (all 12,544 budget-positive key-releasing cases per witness), with explicit classifications for every label set. The matching local run yielded `PASS`; separate literal Cartesian-product enumeration checked all 1,664 initially singleton-surviving B3 positions for each witness and 12 additional cases across B3/B5/B9. The independent checks found no 93-edge completion. The complete locally generated per-case report SHA256 is `5b497c8dd70697d48b9e203e3bf8821e7990e5e47055bde66a6c2de82150fcd9` (report JSON bytes produced by the locally run equivalent source).

This is a finite, author-side computational proof within the specified frozen BRC model, not a full seven-key global lower bound. No formal EC49AS CLAIM/Result or independent Driver admission is implied by publication.

## Next exact subproblem

The only unresolved five-label positions for each witness release keys and have B in {17,18,19,20,21}; there are 226, of which 220 release one key and six release two. Apply the prefix-tree group-cover recurrence under one or two globally chosen *additional key identities* (or equivalent key-aware branch-and-bound), using a budget bound before expanding candidate words. Previous direct key/set-state DP on these higher budgets became computationally expensive; that run did not establish a conclusion for them. Preserve the globally open question `C_min(7) ?= 94` separately.
