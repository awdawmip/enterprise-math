# EC49FEE — 28 early schedules × two late BRC triples: exact native-prefix integer formulation

Date: 2026-11-08. Author-side portable research; no native CLAIM/Driver acceptance. Frozen scientific input `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. This preserves the actual signed six-axis native word expansion, original nine-state DFA, full positive BRC keys, H2–H9 path quotas, and the original P000 model.

## Precise question and two results

A full system has H2…H9 quotas (4,2,2,4,2,4,4,2), 24 distinct literal words, signed native endpoint displacement +2E1, observation rank 9 at each horizon, and at most five distinct **full** BRC keys k=(x,y,z). Its cost C_native is the number of different nonempty signed X6 native-step prefixes after expanding every operator.

Here only two eligible fixed late schedules are studied:
- T0: H4 A=(4,1,1), H5/H6 B=(5,2,1), H7/H8/H9 C=(7,3,1).
- T1: H4 A=(3,2,1), H5/H6 B=(4,3,1), H7/H8/H9 C=(5,5,1).

H2/H3 range over **all 28** early choices from EC49FED (the actual finite enumeration, 35/38/39/42 native edges, including four with only one early BRC key). All 18 late words are freely optimized subject to the fixed schedule.

**Result:** For both T0 and T1, the MILP-reported minimum over all 28 early choices is **109** native edges. In *each case*, the distribution of optimal complete-system costs is 109×4, 112×4, 113×4, 116×12, 118×2, 122×2. The post-early incremental edge cost distribution is 74×24, 76×2, 80×2. Thus 56 of 56 optimization calls returned HiGHS status=0, mip_gap=0, integer objective equal the reported MIP lower bound. This is a computational mixed-integer optimum for these two declared schedules, not an exact rationally checkable branch-and-bound certificate. Original broader mother problem has a previously published 94-edge feasible witness and seeks <=93; other triples and H5 mixing remain candidates.

## Analytic proof: exact 0–1 native Trie reduction

For each horizon h and full key (x,y,z), enumerate literal accepted words with `n_a=z-1; n_e=z; n_c+n_d=x+y-h-1; n_f=h+1-y-2z; n_g=h+1-x`, and validate the nine-state DFA, complete full key and signed six-axis endpoint. Let the fixed early native prefix union be F. In both fixed late schedules, H4/H6/H9 each have only nonzero signatures {16,32}; H5/H7/H8 have only {1,2,4,8}. The original rank-nine predicate is `mask&18 !=0 && mask&20 !=0 && mask&33 !=0 && mask&40 !=0`. Together with the exact two/four word quotas it requires one distinct word from each of 18 (h,signature) groups.

Let x_w be binary for each allowed late word and y_p binary for each nonempty eligible native prefix p not already in F. Impose exactly one x in each group; x_w <= y_{Native(w)} for a complete native word outside F; and y_p <= y_parent(p) whenever the parent is not in F. Minimize |F| + sum_{p outside F} y_p.

**Exact equivalence lemma:** The integer optimum equals the minimum number of distinct signed-native prefixes of the actual selected complete words. For any legal word selection assign y to its native prefix closure (outside F), yielding equal cost. Conversely, for any feasible integer assignment the 18 required x choices each force all their native ancestor prefixes via the inequalities, so the objective is at least the native prefix union; delete extraneous y to achieve equality. The model has no quotient that conflates native paths or full BRC keys.

## Computational coverage and independent replay

Used Python 3.13.5, SciPy 1.17.0 / HiGHS `scipy.optimize.milp`; 56 fixed-(T,early-choice) instances fully solved with reported zero MIP gap. Native certificate replay by a **different standard-library integer/signed-tuple implementation** verified 56/56 complete 24-word systems, 448/448 horizon rank checks, 1344/1344 literal paths with endpoint and full-key checks, and both literal signed-native prefix count and independent weighted operator Trie identity; all passed. Explicit witness records, solver reported lower/primal bounds, full sources and verifier are preserved in the accompanying lossless `.tar.xz.b64` evidence archive. One 109-edge T0 witness and one T1 witness are also in the summary.

The 56 exhaustive 28-choice checks are for **two** late triples. A broader exploratory sweep was not completed and contributes no global exhaustive assertion. The reported solver gap is numeric solver evidence; an independently verified exact rational lower-bound certificate is an open upgrade for Driver review.

## Reproduce

Base64-decode `EC49FEE_complete_research_evidence.tar.xz.b64` into a tar.xz and extract it. Files include:
`EC49FEE_OPT_TRIE.py` (native-prefix MILP), `EC49FEE_EARLY28_SWEEP.py` (two schedules x 28), original `EC49FED_NATIVE_CORE.py` and `EC49FED_EARLY_CERT.json`, complete `EC49FEE_EARLY28_CASE0.jsonl` and `CASE1.jsonl` (56 records with full words and bounds), `EC49FEE_SUMMARY.json`, independent `VERIFY_EC49FEE_INDEPENDENT.py` and `EC49FEE_INDEPENDENT_AUDIT.json`. Archive SHA256: `52dbea0225b3e86826ce78fd35faee23ac1ed2c59fa6db3e4cd5e1d40335c692`.

Run `python VERIFY_EC49FEE_INDEPENDENT.py` in extracted folder; Python+NumPy+SciPy regenerate optimizer results with `python EC49FEE_EARLY28_SWEEP.py --case 0 --limit 8` and corresponding `--case 1`. Avoid appending duplicate JSONL records to previously executed output files.

## Next unit EC49FEF

Use lower bounds, branch-size and early-prefix estimates to prioritize the remaining 106 triples, then try H5 mixed-key choices and more general early schedules. Seek <=93 edges while preserving full native BRC/X6 semantics, or extend lower bounds to a wider clearly specified model.

Current canonical normative reads: Global main fdd93b211aa4b72d835bf632913350d2f7327673 and EM main 58f7216ed9bbe9ae8317551a0d067d3aa32e4d71; frozen science pin unchanged. Native `em_status` and `em_control_tasks` returned `BACKEND_IDENTITY_OR_VERSION_MISMATCH / STATUS_DATABASE_UNAVAILABLE`, `operation_sent=false`; no authentic Source owner, CLAIM, Result or Driver review verified. GitHub-side artifact publication is evidence preservation only.
