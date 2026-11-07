# EC49FBZ — Exact early-four-slot rigidity of the 158-edge signed-X6 BRC witness

Date: 2026-11-06. Status: author-side exact finite calculation with independently checked prefix objective; independent Driver mathematical admission pending.

## Fixed scientific context

Frozen scientific input: `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Input proof/witness: EC49FBU `b3b43ef6abe2fd816d979792d18a67ee5d0aad50`; immediate predecessor source and frozen generator: EC49FBY `5b10f1c296cb8826d4b69f6fd83dba89d765df1c`.

Retain the complete signed native-X6 primitive path expansion, ordered prefix identity, the nine-state DFA and signature indexing. Fix H2/H3 as `{fe,ge}` / `{feg,gef}`. H4/H5 use full positive BRC key L=(4,2,1,0,0,0); H6–H9 use M=(7,3,2,0,0,0). There are ten variable early slots H4–H6 (H4: 4; H5: 2; H6: 4) and ten later H7–H9 slots. The EC49FBU construction has 158 distinct primitive-prefix edges.

## New finite theorem

For **each** of the C(10,4)=**210** four-element subsets I of the ten early signature slots, keep the other twenty signature words (including all later words) unchanged and independently replace the words in I by **arbitrary valid words** with the same respective window, full positive BRC key and terminal nine-state observation. The minimum complete signed-X6 primitive-prefix union cost is exactly **158**.

This augments EC49FBY's full radius-three local result by a complete radius-four subfamily. The full four-exchange space has C(20,4)=4,845 slot groups; the 210 groups here are those wholly in H4–H6.

## Exact finite argument

Let B(w) be the set of all nonempty signed-native primitive prefixes of candidate word w, and let R be the union of B(w) from the twenty unchanged signature words. Set K=158−|R|. A strict improvement requires
`|B(w1)\R ∪ B(w2)\R ∪ B(w3)\R ∪ B(w4)\R| < K`.
Every individual residual set must first have size <K; then any first two, and any first three residual sets with union size >=K can be excluded by monotonicity. Enumerate the surviving fourth candidates and calculate exact bitset cardinality; the original witness gives a valid upper bound 158. For all 210 groups, no lower result survives. This is exhaustive because every discarded partial union already meets the threshold, regardless of subsequent words.

The candidate source is the frozen EC49FBY generator `VERIFY_EC49FBY.py`, which enumerates the complete BRC count constraints and DFA terminal signatures. Code here imports that exact algorithm rather than re-specifying the scientific sample.

## Executed results

The Python integer-bitset program and a second implementation of the objective using **tuples of signed primitive integers and ordinary prefix sets** were executed on 2026-11-06 using the same frozen generator semantics. Both returned PASS, the same per-group exact minima and identical fourth-candidate evaluation counts.

- 210 four-slot groups, each exact minimum 158;
- 24,708,240 unpruned candidate four-tuples accounted for;
- 3,001 surviving exact fourth-slot evaluations; 792 filtered pairs and 1,577 filtered triples excluded by monotonic lower bounds;
- 210/210 per-group cost and fourth-evaluation counts match the independent direct-set check.

The source scripts regenerate `EXACT_REPORT_EC49FBZ.json` (per-group detailed certificate) and `DIRECT_REPORT_EC49FBZ.json` (per-group direct-objective cross-check) in this directory. The compact `SUMMARY_EC49FBZ.json` saves the exact executed totals and provenance.

Reproduce from the research directory: `python3 EC49FBZ_EARLY_QUARTET_RIGIDITY/VERIFY_EC49FBZ.py`; `python3 EC49FBZ_EARLY_QUARTET_RIGIDITY/VERIFY_DIRECT_EC49FBZ.py`. Python standard library only.

## Next discriminating question

Study four-exchanges with three H4–H6 slots and one H7–H9 slot. Carefully account for late-candidate pool size and preserve the exact full signed-X6 observer. Try a 157-edge witness or an exhaustive lower-bound certificate for a stated new subfamily; the full nine-window mother objective remains distinct from this fixed L/M route.

Source delivery in the existing PR #1730 is author-side portable research and does not alter P000, the frozen pin, CLAIM/owner, Source-native Result or Driver review state.
