# EC49FHB — B witness exact five-path budget-19 exclusion

Frozen scientific input: `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. The observer is the original 9-state BRC model with 24 H2–H9 demands and ordered, signed native X6 microstep-prefix cost.

## Result

For each five-label subset Q of the 24 demands, fix all other 19 words as in the exact 7-cache-key, 94-native-edge **EC49FGJ witness B**. If the fixed 19 words still exhibit all seven baseline complete raw cache keys and the target native 93-edge budget for the replacement set is exactly `B(Q)=19`, then there exists **no** legal replacement of those five words meeting both original BRC signatures and `C_native<=93` with at most seven complete raw cache keys.

The eligible domain has exactly **144** five-label subsets Q. Exhaustive exact finite calculation returns **144 infeasible; zero feasible**. The same 144-case result for **witness A** is recorded independently in EC49FHA. Consequently, under the two specified 94-edge witnesses, all non-key-release five-path positions with replacement budget **19 or less** have now been excluded, combining this computation with EC49FGX–EC49FGZ.

## Exact proof method

For each old native prefix p retain its exact support mask `S(p)` over the 24 baseline paths. The prefix disappears from the fixed background precisely when its entire support is inside Q. Therefore `B(Q)=#{p:S(p) subset Q}-1`.

For each eligible Q, list all legitimate BRC paths for each of five labels, retaining only the seven already-present keys. The code uses the complete **178850-word** frozen catalog and its **9838** words with witness B's keys. Represent each candidate's native ordered signed prefix difference from the fixed background as an exact integer bitset. Check the complete union-cover decision with the existing EC49FGX five-way inclusion-minimal antichain DP. Deleting a state Y in favor of X subset Y is exact since `X union Z subset Y union Z` for every future choice Z.

Locally executed verifier completed:

`EC49FHB_B_B19_EXACT_PASS: 144 positions, zero 93-edge completions`

The attached compressed-base64 JSON contains all 144 five-position sets, per-label candidate counts, and the zero-feasibility outcomes; decode by `base64 -d EXACT_REPORT_EC49FHB.json.gz.b64 | gzip -d > EXACT_REPORT_EC49FHB.json`. The verifier also regenerates it.

## Reproduce and next question

Run `python VERIFY_EC49FHB.py` alongside existing EC49FGW and EC49FGX sibling directories on PR #1730. Original 7-key witness and frozen observer remain unchanged. This is a scoped finite author-side theorem, pending independent Driver review. The global seven-key 94-edge optimum is still unresolved.

Next: budget 20–25 within the fixed seven-key five-path neighborhoods (164 positions each in the previous candidate accounting), then 4898 cache-key-release positions per witness; a global search beyond neighborhoods remains relevant.
