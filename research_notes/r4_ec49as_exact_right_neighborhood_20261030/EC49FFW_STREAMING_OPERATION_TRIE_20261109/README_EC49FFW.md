# EC49FFW — Exact operation-code trie and unrestricted H2/H11–H13 optima

**2026-11-09 · AUTHOR_SIDE_COMPUTATION_ASSISTED_FINITE_THEOREM · UNREVIEWED / NOT_ADMITTED.** Frozen scientific input: `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Original signed-X6 operation codes and nine-state BRC observer: EC49FFT/EC49FFV (see source refs below). Mathematical and computational authority is separate from Source CLAIM/Result/Driver admission.

## Exact new results

For original BRC windows H2,Hh, each demanding one operation word of each original signature {1,2,4,8}, all paths using positive complete keys, with any number of distinct keys permitted, let C count distinct nonempty **ordered signed native X6 microstep prefixes** of all eight selected paths. Then the following **three new finite global minima** hold:

| h | admissible low-signature candidate words | viable operation-prefix trie nodes, including root | unrestricted exact minimum |
|---:|---:|---:|---:|
| 11 | 15,233,900 | 27,639,185 | **86** |
| 12 | 74,884,944 | 136,180,483 | **90** |
| 13 | 367,524,430 | 669,712,759 | **94** |

Thus `C_min(H2,Hh)=4h+42` for **h=11,12,13**, extending the earlier independent H10=82 calculation to the finite range 10..13. No infinite-h lower bound is claimed. H14 was attempted, but the run timed out and **has no completed result**.

## Reuse of the exact EC49FBS operation-code prefix identity (all finite word families)

The original signed native six-axis words are

```
a = (-1,-1)           c = ( 1, 2,-1,-2)
d = ( 2, 1,-2,-1)    e = ( 3, 1, 1,-3)
f = ( 1,-1)          g = ( 2,-2)
```

**Prior work.** This exact identity and its combinatorial proof were already established in `EC49FBS_LOSSLESS_PRIMITIVE_TRIE/README_EC49FBS.md` (2026-11-05), for all finite operation-word families. EC49FFW is not claiming priority for the identity. The **new** work here is the exact streaming observer-constrained subset DP, its H11–H13 exhaustive runs and witness certificates. We independently rechecked the earlier identity on a different candidate domain.\n\nTheir first **two** signed microsteps are pairwise distinct. In particular, the code is prefix-free; only c/f share their **first** microstep, and only d/g share their first microstep.

For any finite set W of complete operation words, form its operation-prefix trie. Let S(P) be the set of outgoing operation labels at operation-prefix P. Then the exact native microstep prefix edge count is

```
C_native(W) = sum_{P operation prefix} F(S(P)),
F(S) = sum_{u in S} len(code(u)) - 1_{c,f subset S} - 1_{d,g subset S}.
```

**Proof.** Complete native codewords have distinct two-step beginnings, so any two encoded paths with unequal operation histories cease sharing native prefixes during their first unequal operation. Different operation-prefix nodes therefore have disjoint *new* microstep-prefix edges. At one node, all outgoing codewords share no microstep except the two indicated first-step pairs. Counting the union at each node and summing proves the equality for arbitrary finite W, irrespective of window, complete key, or observer.

For a fixed baseline operation-word set W0 (the four forced H2 words), let B(P) denote baseline outgoing labels at P. Selecting outgoing labels S(P) at a node adds the exact local cost `F(B(P) union S(P)) - F(B(P))`. This yields an **exact dynamic program directly on operation prefixes**, without constructing an expanded signed-microstep trie.

## Completeness and integer optimization

Any length-h operation word eligible for a positive complete BRC key has counts

```
#e = #a + 1 >= 1,     2 #e + #f <= h,
x = h+1-#g,           y = h+1-2#e-#f,       z=#e,
#c+#d = x+y-h-1.
```

Conversely, every length-h word meeting those integer conditions corresponds to the indicated positive complete key; the original DFA then selects only terminal signatures 1,2,4,8. The streaming C++ solver enumerates all feasible operation prefixes with state `(depth,#e,#a,#f,DFA-state)` and exact memoized suffix feasibility. It does **not** approximate or sample candidate paths. Baseline H2 paths are exactly `ce,ec,ed,de` (28 signed native-prefix edges). Its bottom-up DP `D(P,M)` minimizes additional native cost for each demanded subset M of the four Hh signature bits; child subsets may be assigned disjointly, since repeating any one signature cannot improve the union cost. Children are combined in independent groups `{a}`, `{c,f}`, `{d,g}`, `{e}` with the exact local F-difference cost. Thus `28 + D(root,15)` is the global minimum.

This is an exhaustive finite calculation with an explicit reproducible integer algorithm, not an accepted formally checked proof. The streamed prefix recursion uses memory bounded by the model-state memo and recursion depth, avoiding the 16-row-per-node storage of the materialized trie; **time still depends on the number of viable prefixes**, which grows rapidly with h.

## Attaining witnesses and independent signed-native recount

For each h=11,12,13, the H2 words are `ce, ec, ed, de`. At Hh take complete key `K_h=(4,h-2,1)` with sig4 `fe g^(h-3) c`, sig2 `fe g^(h-3) d`, sig8 `gfe g^(h-4) c`, sig1 `gfe g^(h-4) d` (spaces only for readability). For h=11 this is:

```
sig4  feggggggggc       sig2  feggggggggd
sig8  gfegggggggc       sig1  gfegggggggd
```

DFA signatures, complete keys, endpoint six-axis signed displacement (2,0,0,0,0,0), and direct signed-microstep prefix union are checked independently. Each attains 4h+42, so the exact DP lower bound closes.

## Executed verification and limitations

- `ec49ffw_operation_trie.cpp`: independent *materialized operation-trie* exact DP, h=3..11, reproduces the previous unrestricted minima 36,44,52,59,65,71,77,82 and newly computes 86 for H11.
- `ec49ffw_streaming_dp.cpp`: second exact algorithm enumerating viable operation prefixes by direct state-feasibility recursion; matches the materialized algorithm for h=6..11 and computes H12=90, H13=94. Reports are in `EXACT_REPORT_EC49FFW.json`.
- Exact operation trie identity independently checked for all 156,832 legal low-signature words across H2..H8, with **zero** mismatch: 225,952 operation edges versus 623,044 native microstep edges (both exclude root). This is a *node/edge representation reduction of 63.73%* in that finite full candidate trie, not an end-to-end running-time claim.
- The h14 streaming attempt timed out without an answer; no result or negative mathematical inference is drawn from timeout.

## Prior-work attribution, authority and next discriminating question

Earlier operation-trie theorem: `research_notes/r4_ec49as_exact_right_neighborhood_20261030/EC49FBS_LOSSLESS_PRIMITIVE_TRIE/README_EC49FBS.md` (2026-11-05); its compressed 0–1 formulation was proposed but not executed. EC49FFW extends it to a streaming exact 16-mask solver and new complete H11–H13 results. Frozen model source: `research_notes/r4_ec49as_exact_right_neighborhood_20261030/EC49FFT_H2_CROSSOVER_20261109/VERIFY_EC49FFT.py`, and `EC49FFV_H9_H10_UNRESTRICTED_20261109/README_EC49FFV.md` at immutable commit `de8f6306e63828368b972509a78ceea0b358401d`. EC49FFW is a separate author-side finite extension and reusable exact compression. It does not alter P000, the frozen science pin, a current Owner, Claim, Result or reviewed Working Truth.

**Scope separation:** The auxiliary H2/Hh instance here has **four low signatures at H2**, whereas the historical frozen mother template in EC49FDF fixes **high signatures 16/32 at H2/H3** and 24 labels. Therefore the 86/90/94 bounds are **not automatically lower bounds on that different mother problem**. Check the exact task publication before applying any inequality.\n\n**Next:** use the streaming recursion with tighter exact dynamic programming or symbolic recurrence certificates to decide H14 and test whether the `4h+42` pattern extends beyond the verified finite range; separately route the full frozen 22-demand problem, including H3 high signatures and the <=5 complete-key and <=93 native-edge limits, through an actual current task publication and owner authorization.