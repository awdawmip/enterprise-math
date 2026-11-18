# EC49FFU supplement — exact fixed-H2 / single-full-Hh-key classification (2026-11-09)

**Scientific pin** `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`, original signed native X6 BRC DFA and key equations. Status: `AUTHOR_EXACT_FINITE_THEOREM / EXACT_INTEGER_DP_EXECUTED / UNREVIEWED`.

## Finite result

Fix the four H2 observations with their uniquely available original operation words `ce, ec, ed, de` (sig4,8,2,1), all at key `(3,1,1)`. For Hh require one original operation word for each of sig1,2,4,8, all using **one additional common full cache key** K=(x,y,z), positive. Minimize distinct nonempty **ordered signed-X6 native microstep prefixes** over all allowed K, c/d splits and operation permutations.

Exhaustive enumeration and a weighted 16-subset native-prefix-tree integer DP yields:

| Hh | All legal full keys K | Eligible original words (all keys) | Exact minimum over any one Hh key | All minimizer Hh keys |
|---|---:|---:|---:|---|
| H8 | 50 | 125,680 | **71** | `(x,10-x,1)`, x=3..9 (7 keys) |
| H9 | 70 | 625,050 | **77** | `(x,11-x,1)`, x=3..10 (8 keys) |

All 120 complete keys are included, including z>1. The h=8 row agrees with independently published EC49FFT **unrestricted** H2/H8 exact global minimum 71; the h=9 row solves the **specified one-Hh-key subclass**. Every key row and candidate-word count is in `FIXED_KEY_REPORT_EC49FFU.json.gz.b64`.

## Exactness certificate / recurrence

For each fixed (h,K), enumerate nonnegative counts `#a=z-1, #e=z, #c+#d=x+y-h-1, #f=h+1-y-2z, #g=h+1-x`; split #c/#d in every possible way and enumerate all distinct operation orders; evaluate each word with the original nine-state observer and retain signatures 1,2,4,8. Insert every retained word as its **ordered signed-X6 microstep** sequence into a rooted trie.

Let P2 be the set of 28 H2 baseline nonempty signed prefixes. Weight a trie edge by zero if its signed prefix is already in P2, otherwise by one. For each node v and subset S of four signatures, let D_v[S] minimize the weight of selected edges below v covering exactly the required S. Terminal labels at v cost 0; distribute disjoint submasks among children (each nonempty child assignment adds its connecting edge weight), minimizing total. By induction on tree height, each DP value is the exact minimum of a selected rooted subtree; each cover yields real original words. Add the baseline 28 edges. Minimizing these **exact integer** results over all legal K proves the two finite rows. Duplicate signature paths cannot lower nonnegative union cost.

Code `VERIFY_EC49FFU_FIXED_KEY_DP.py` is an independent exact enumerator/weighted DP using the same-directory frozen original model; executed locally for H8 and H9, returning exactly the values above. Reproduce with `python3 VERIFY_EC49FFU_FIXED_KEY_DP.py 8 9 > FIXED_KEY_REPORT.json`. Uncompressed report is 30,496 bytes (SHA-256 `7756d434e16cfeeb7a867c5d2d557b109f1cb71010d226a1722aae3db6b20494`); published gzip+base64 payload uses deterministic gzip mtime=0. Extract using `base64 -d FIXED_KEY_REPORT_EC49FFU.json.gz.b64 | gzip -d > FIXED_KEY_REPORT_EC49FFU.json`.

## New open question

Does unrestricted all-full-key H2/H9 improve the 77-edge construction if H9 signatures may be split across several cache keys? Independently check the same for H10, where the exact two-key 82-edge counterexample refutes the candidate lower bound 83. The parent frozen 22-demand problem still requires its H2/H3 and high-signature quota with <=5 complete keys, <=93 native prefix edges.

**Scope**: h8/h9 exact weighted fixed-H2 / one-common-Hh-key minima. Author-side finite proof and data; no formal native CLAIM, Result or Driver admission.
