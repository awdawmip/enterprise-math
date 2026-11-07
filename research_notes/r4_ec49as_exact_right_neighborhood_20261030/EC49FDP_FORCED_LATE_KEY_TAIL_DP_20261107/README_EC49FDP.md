# EC49FDP — forced late key and exact signed-X6 tail-prefix bounds

**Date:** 2026-11-07. **Frozen scientific input:** `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. **Provenance:** EC49FDO's exact 15-slot-feasible critical-key exchanges per EC49FAJ family, EC49FDL's six primitive signed-X6 generator/DFA, EC49FDN's fixed early seed, and the immutable project P000. This is an author-computed finite result; native Source Result and independent Driver admission remain open.

## New theorem 1: late-window forced-key and exact signature allocation

For the four EC49FDO 94-edge seed families (1512/1513/2200/2203), fix the original six H2/H3 words `H2={de,ed,ce,ec}`, `H3={feg,gef}`, accounting for exactly 42 distinct **signed native primitive** nonempty prefixes. Hold their first four complete positive cache keys fixed (including the H2/H3 key `(3,1,1)`) and replace the critical last key by one of the *15 previously slot-feasible replacement keys for that family*. Total horizon quotas remain `(4,2,2,2,4,2)` or `(2,4,2,2,4,2)` for H4–H9, with **exactly five distinct complete cache keys**.

All four retained keys have `x+y <= 8`; all 15 replacement keys in each family have `x+y=10`. For a length-`h` operation word using key `k=(x,y,z)`, nonnegative `c+d` multiplicity requires
`r_h=x+y-h-1 >= 0`.
It follows **every H8 and H9 word uses the *new* key**, in all 60 named family/replacement events; the remaining keys generate no eligible H8/H9 word. With the new key:
- `H8: r_8=1`, hence **exactly one** operation `c` or `d` per word;
- `H9: r_9=0`, hence **zero** `c,d` operations per word.
- The number of signed native primitive steps is `2h+2(r_h+z)` because `a,f,g` contribute 2 and `c,d,e` contribute 4 each. Both H8 and H9 words therefore contain exactly `18+2z` native steps.

For every listed candidate key the frozen nine-state DFA produces H8 signatures exactly `{1,2,4,8}`, and H9 exactly `{16,32}` (bitmasks 15 and 48). The rank-nine clauses are `(18,20,33,40)`: each clause must intersect the selected signature union. Since H8 has four slots and H9 two slots, the clauses force **exactly one H8 word of each signature 1,2,4,8 and one H9 word of each signature 16,32**. These constraints are necessary for every complete five-key candidate in this family.

## New theorem 2: exact six-label native-prefix lower bound

Let `P0` denote the set of 42 signed native prefixes of the six fixed H2/H3 words. For a replacement key K, let `L8(s,K)` and `L9(s,K)` denote *all* operation words with the required horizon, complete positive cache key and DFA signature. Define:

```text
T(K) = min_{w1 in L8(1,K), w2 in L8(2,K),
           w4 in L8(4,K), w8 in L8(8,K),
           w16 in L9(16,K), w32 in L9(32,K)}
        | union_{s in {1,2,4,8,16,32}} Prefix_X6(w_s) \ P0 |.
```

Here `Prefix_X6` is the set of all **ordered signed primitive X6 prefixes** of an operation word, not operation-letter prefixes, endpoint counts or compressed signatures. Trie dynamic programming, labeling the terminal by its single required signature bit and combining child masks by bitwise OR, computes `T(K)` **exactly**. Each distinct Trie edge is charged one unit iff it is outside `P0`. At each subtree the DP enumerates every possible six-bit covered mask; induction on Trie height proves completeness and optimality. Every selected complete H2–H9 system in the specified replacement family has
`Cost >= 42 + T(K)`
because its H8/H9 paths alone must cover all six labels. The DP deliberately omits H4–H7, making it a genuine **relaxation-based lower bound**.

### Complete finite classification: 16 distinct key values across the 60 events

| New late key K | T(K), new primitive edges over P0 | Full 22-path lower bound `42+T` | >=94 (rules out <=93)? |
|---|---:|---:|:---:|
| (3,7,1) | 57 | 99 | Yes |
| (4,6,1) | 38 | 80 | No |
| (5,5,1) | 38 | 80 | No |
| (5,5,2) | 65 | 107 | Yes |
| (6,4,1) | 38 | 80 | No |
| (6,4,2) | 42 | 84 | No |
| (7,3,1) | 38 | 80 | No |
| (7,3,2) | 42 | 84 | No |
| (7,3,3) | 73 | 115 | Yes |
| (8,2,1) | 38 | 80 | No |
| (8,2,2) | 42 | 84 | No |
| (8,2,3) | 46 | 88 | No |
| (9,1,1) | 57 | 99 | Yes |
| (9,1,2) | 65 | 107 | Yes |
| (9,1,3) | 73 | 115 | Yes |
| (9,1,4) | 98 | 140 | Yes |

The seven excluded keys `(3,7,1),(5,5,2),(7,3,3),(9,1,1),(9,1,2),(9,1,3),(9,1,4)` occur in **all four** 15-event replacement lists. **28/60** named exchanges therefore cannot yield <=93 in the frozen seed + single critical-key replacement family; **32/60** remain possible and merit full integer optimization. The common threshold is exact for this family, not a statement about all five-key solutions with different early seeds or multi-key exchanges.

A useful regression is the old key `(5,5,1)`: the late-window lower bound is 80, while the already verified full optimum in the original 1512 family is 94. The extra 14 edges arise from enforcing the intervening windows and other global constraints. For `(9,1,4)`, the late-window lower bound alone is 140.

### Reproducible output and witnesses

`EC49FDP_TAIL_EXACT_DP.py` is standard-library Python. It enumerates all accepted operation words for h=8,9 under the frozen transition table, generates signed native X6 primitive strings, constructs a Trie, solves each of 16 exact six-label DP instances, traces back six explicit operation-word witnesses, independently recomputes each witness's prefix-union edge count and checks the native endpoint/cache key and operation length.

Run:
```bash
python EC49FDP_TAIL_EXACT_DP.py > tail_results.json
```

Example minimizing six words for `K=(4,6,1)` (signature `1,2,4,8,16,32` in that order):
`gefggggd; fegggggd; fegggggc; gefggggc; fegggggfg; gefggggfg`. Their signed primitive-prefix union adds 38 edges beyond the 42-edge seed.

Example witness for `K=(9,1,4)`:
`deaaaeee; eaaaeeed; ceaaaeee; eaaaeeec; fegaaaeee; gefaaaeee`, adding 98 edges. (One representative per signature; these H8/H9 witnesses are not claims that the full middle horizons are solvable for <=93.)

**Verification:** Actual local Python execution enumerated all 16 rows. All 16 DP witnesses passed direct prefix-union recount and signed native displacement/key/length audit; an independent Fraction-based nine-state observer audit found `rank_Q(H8)=rank_Q(H9)=9` for each. Number of candidate words and Trie edges are emitted per key by the script. Exact integer arithmetic is used for all costs/DP; rational arithmetic for the separate rank verification.

**Next EC49FDQ:** For the 32 surviving family/exchange events, use `42+T(K)` as an admissible pruning bound and run full H4–H9 prefix MILPs with hard threshold 93, prioritizing `K=(4,6,1),(6,4,1),(7,3,1),(8,2,1),(5,5,1)` as applicable. The independent early-seed alteration route remains active. Preserve all original frozen science, P000 and five-key constraints.

## Evidence and status

Author evidence: this report, reproducible `EC49FDP_TAIL_EXACT_DP.py`, and complete JSON emitted by that program. Existing prior sources: EC49FDO `SCREEN_EC49FDO.py` and `EXACT_REPORT_EC49FDO.json`; EC49FDL `REPLAY_EC49FDL_PORTABLE.py`. New programs compute only the stated finite relaxation, without asserting canonical task/result admission. Original <=93 mother target remains open.
