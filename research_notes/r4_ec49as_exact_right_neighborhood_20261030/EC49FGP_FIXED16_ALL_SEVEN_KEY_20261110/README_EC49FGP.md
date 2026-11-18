# EC49FGP — Seven-key fixed-16 obstruction without coherence assumptions

**2026-11-10** · Frozen scientific pin: `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab` · **AUTHOR_EXACT_FINITE_CERTIFICATE / LOCALLY_EXECUTED / INDEPENDENT_LOCAL_CROSSCHECK / NOT_DRIVER_REVIEWED / NOT_ADMITTED**.

Source model: frozen nine-state BRC transition table and the six ordered signed-native operation expansions, from `EC49FCZ_H4H6H7_SIGNATURE_COMPLETE_128/frozen_model.py`, Git blob `7e97065ac9a0ff70435b92ee2f4bd718c9bf1859`. Baseline 24-path, seven-raw-key, 94-prefix witnesses A/B: `EC49FGJ_SEVEN_KEY_94_20261110/WITNESSES_EC49FGJ.json` (Git blob `e65c1598ad9fa2680558046ed1e59d83806536b8`).

## Exact finite theorem

For **either** EC49FGJ witness `W=A` or `W=B`, keep its 16 complete ordered signed-native paths outside windows H7 and H8 *literally fixed*. Replace the other eight paths by **any** legal operation words of length H7/H8 that meet the four original signatures 1,2,4,8 at each window and native displacement (2,0,0,0,0,0), using **at most seven distinct complete raw cache keys in all 24 paths**. Then

\[
\boxed{\min C_{\mathrm{native}}=94\quad(W=A\text{ or }B).}
\]

Both original witnesses attain 94 and use seven keys. No operation-prefix coherence between H7 and H8 is assumed. This strengthens EC49FGN/FGO in a different direction: *all* H7/H8 word arrangements are covered under the stated seven-key limit and fixed 16-path background.

## Exhaustive certificate and proof

The fixed 16 paths have exactly 78 distinct nonempty signed-X6 prefixes and occupy the same six complete raw keys for both profiles:

`K_0 = {(2,1,1),(3,0,1),(3,1,1),(4,2,1),(5,4,1),(6,4,1)}.`

Thus a total cost ≤93 could add **at most 15** prefixes outside the fixed set `F`. Each selected H7/H8 word `w` must separately have `|P(w)\\F|≤15`; this filter cannot discard a counterexample.

In this frozen model the six original operations are `a,c,d,e,f,g`; only `a` and `e` have nonzero net first-axis displacement, so the native endpoint condition for H7/H8 is precisely `#e=#a+1`. Exhaustively enumerate all nonnegative operation multiplicities satisfying that identity, all their DFA-accepted orderings, and signatures. The exact legal-word counts are:

| Window | Signature 1 | 2 | 4 | 8 |
| --- | ---: | ---: | ---: | ---: |
| H7 | 5,724 | 6,806 | 5,724 | 6,806 |
| H8 | 28,063 | 34,777 | 28,063 | 34,777 |

Legal H8 words use 50 complete raw keys. Since the fixed background occupies six, a ≤7-key completion either uses no new key in H8 or uses **one** `k` from the 49 H8 keys outside `K_0`. These **50 cases** exhaust *all* seven-key completions, including cases where the only new key appears at H7.

For each case `K=K_0∪{k}`, compute each legal candidate's exact ordered signed-microstep prefix set `D_F(w)=P(w)\\F`; represent it losslessly as an arbitrary-precision bit mask. Enumerate the retained H8 pair unions for signatures (1,2) and (4,8) whose size is ≤15, then their **complete cross product, including disjoint pairs**. Each resulting H8 four-signature union of size ≤15 is also tested against **all** legal H7 choices for each of the four required signatures. Since any candidate path must contribute a subset of that H8 union, this final subset check is exact.

Results:

| Profile | Seven-key possibilities | H8 four-signature unions costing ≤15 | Full H7+H8 completions costing ≤15 |
| --- | ---: | --- | ---: |
| A fixed 16 | 50 | **0 across all 50 cases** | **0** |
| B fixed 16 | 50 | **8 only when extra key is (7,3,1)** | **0** |

For B's sole exceptional key `(7,3,1)`, there are 338 distinct surviving (1,2) masks and 480 (4,8) masks. Their complete 162,240 pair-union comparisons produce **8** distinct H8 four-signature unions with ≤15 new prefixes; seven provide no legal H7 word for **any** of the four signatures, and one provides an H7 word only for signature 4. Hence none extends to the required eight paths. In particular, a low H8-only prefix count need not yield a valid two-window completion.

The existing seven-key/94-prefix A and B witnesses attain the lower bound, finishing the finite proof within the specified backgrounds.

## Evidence and reproduction

`VERIFY_EC49FGP.py` (distributed in the attached evidence bundle) is the complete stdlib-only finite verifier: literal frozen DFA and X6 steps; complete count-vector enumeration; exact prefix-set/mask union; all 50 seventh-key cases for both A/B; and the exceptional B H7 test. It also checks the original 24 demand labels, observer signatures, native endpoints, raw-key counts and 94-prefix witness costs. `EXACT_REPORT_EC49FGP.json` contains the complete 50-case-per-profile machine output.

An independently written `VERIFY_EC49FGP_CROSSCHECK.py` uses a full Cartesian alphabet enumeration (`6^7` and `6^8`, rather than count vectors) and signed-character prefixes, and reproduces the exceptional B case: exactly 8 H8 unions, 0 complete H7/H8 extensions. Its output is `CROSSCHECK_EC49FGP.json`.

The evidence bundle is stored as `EC49FGP_evidence_20261110.tar.xz.b64` (base64 of a tar.xz archive containing all four UTF-8 files). Reconstruct with `base64 -d ... | tar -xJf -` and run both Python scripts. This is author-side exact computational evidence; it has no independent Driver admission.

## Next independent scientific unit

The new theorem removes both A/B **fixed-sixteen-background** branches from the ≤93 seven-key search. Test a one-word change among the sixteen background paths, jointly with the H7/H8 completion, with the exact ≤7-key limit. Prioritize changing the H5/H6 high/low paths that occupy one of the six mandatory background keys, and preserve original 24 labels, nine-state observer, endpoints, full key identities and exact ordered signed-X6 microstep prefixes. The unrestricted global question `C_min(7) ?= 94` remains open.

**Identity:** `EM-DIRECT-2DB58A / TASK_RESEARCH`; `RA-935AA5804C9E55D0349873F5` from native current Source. Historical `EC49AS` task authority query returned `CANONICAL_REJECTED: NO_CURRENT_IMMUTABLE_PUBLICATION`; this work is an independent author research unit, not a formal CLAIM/Result.
