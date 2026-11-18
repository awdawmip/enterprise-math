# EC49FIY–FIZ — Exact six-path released-key B=5/B=7 barriers (2026-11-11)

## Problem, frozen provenance and scope

Author-side continuation of EC49FIX on the **same frozen 24-label nine-state BRC problem**, pin `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Two original EC49FGJ witnesses A/B each have seven **complete original raw cache keys** and 94 distinct nonempty, *ordered and signed six-axis native-microstep prefixes*. The original scientific parser and both 94-prefix witnesses are located at sibling `EC49FGW_RADIUS5_EXACT_SCREENS_20261110/`: `EC49FGW_RADIUS5_SCREEN.py` and `EC49FGJ_SEVEN_KEY_94_WITNESSES.json`. There are 24 original observation demands, 178,850 legal operation words, 94 complete raw-key types and 9,838 legal words using the seven keys of each witness.

For a six-label replacement position `Q ⊆ {0,...,23}`, `|Q|=6`, the other 18 original words produce an exact native-prefix background `F(Q)`. Define `P(w)` to contain each ordered signed native prefix of the legal word `w`. The objective for this *fixed-background six-path* subproblem is the minimum `|F(Q) ∪ ⋃_{i∈Q}P(w_i)|`, subject to all original observations and at most seven **full raw keys**. This manuscript classifies precisely the new released-key cases `|F|=88` and the remaining forced-key cases `|F|=86`, without changing any scientific pin or the locked P000.

## Exact finite result EC49FIY: released-key B=5

Here `|F|=88`, leaving `B=93-88=5` new prefixes if a 93-edge completion existed. For **each** of A and B, all `C(24,6)=134,596` positions were enumerated. Exactly **2,880** six-label positions have the stated released-original-key B=5 condition. They fall into **16 distinct exact native-prefix backgrounds**, each shared by 180 positions. The 94-key coverage oracle checked 3,120 deleted-original-key exclusions per witness and found each released original key **mandatory** under the seven-key limit. Hence all replacement words must use the original seven full keys.

Twelve fixed-prefix background classes have two H8 observations and four have three. Exhaustively computing the union of all admissible new-prefix sets for these H8 demands returns **minimum 6** in every one of the sixteen classes, where for triple classes pairwise minima can be less than six. Therefore `|F|+6=94` is a lower bound. The original A or B witness realizes 94, proving exact optimum 94 for all **2,880 per witness**, **5,760 combined**.

## Exact finite result EC49FIZ: forced-key released B=7

Here `|F|=86`, leaving `B=7`. For **each** of A/B, complete enumeration yields 7,523 released-key positions, of which 117 still potentially allow reallocation and 7,406 force all original seven keys (by an exhaustive 94-type key-coverage oracle). Among the forced 7,406, a previously established single-observation bound covers 6,938; the **468 remaining previously unresolved positions** fall into **18 distinct exact native-prefix backgrounds**, each repeated 26 times.

Six groups have two H8 demands and twelve have three. Full original-seven-key H8 new-prefix-union minimization returns **8 in every group**; triple H8 minima are computed jointly, not inferred from pairwise minima. Hence each of these 468 cases per witness needs at least `86+8=94` native prefixes. Original witnesses attain the bound. This newly certifies **936 cases across A+B**. Cases previously covered by the singleton result or still potentially reallocating keys are not double-counted.

**Combined newly certified finite subproblems: `5,760+936=6,696`.** This concerns two original witnesses' radius-six replacement neighborhoods and is an author-side exact finite result. The unconstrained seven-key original mother problem retains only its known upper bound `C_min(7) <= 94`; the global lower bound and possible 93-edge witness remain open.

## Finite proof kernel and verification

1. Enumerate every one of the `C(24,6)` replacement positions and group by **complete native-prefix set `F`**, not only `|F|`. Preserve all original signed microstep order and full raw key identities.
2. In each released-original-key case, for every old key absent from fixed words, forbid it and exhaustively test whether `<=7` distinct raw keys could cover all six replacement observation signatures, using all 94 possible complete raw key types. If not, that key is mandatory. When all seven original keys are forced, any candidate replacement set is contained in those seven.
3. For every H8 observation `i` in the replacement set, enumerate all legal candidate paths using allowed old keys. Form exact `D_F(w)=P(w)\F`; retain only `|D_F(w)|<=B` (necessary for any hypothetical <=93-edge completion). Deduplicate actual new-prefix sets; minimize the cardinality of their **union** over every 2- or 3-observation tuple. In all sixteen B=5 groups this minimum is six; in all eighteen B=7 groups it is eight.
4. Any full six-path completion contains that H8 subset and therefore cannot add fewer new prefixes. The original feasible A/B path set supplies the matching upper bound 94.

The executed Python verifiers preserve byte-level ordered signed-prefix representations and use integer/finite-set exact operations, without rounding or asymptotic inference. The computed grouping multiplicities and the raw-key coverage oracle give full finite coverage for the declared classes.

Actual captured program outputs:
```text
EC49FIY_PROFILE_PASS A 2880 groups 16 key_recovery_tests 3120
EC49FIY_PROFILE_PASS B 2880 groups 16 key_recovery_tests 3120
EC49FIY_EXACT_PASS 5760
EC49FIZ_PROFILE_PASS A 468
EC49FIZ_PROFILE_PASS B 468
EC49FIZ_EXACT_PASS 936
```

Exact original-file SHA256 values:

| Artifact | Original SHA256 |
| --- | --- |
| `VERIFY_EC49FIY.py` | `cfb32021081d381d8b5ed1a2d0d11331970a3c7e30a56e3e77c32cfdc10482f1` |
| `EXACT_REPORT_EC49FIY.json` | `4e0b7e327ecf0acba8e8b479dd6422dee3ea2d0ef95dd360c8a2be2663266ce6` |
| `VERIFY_EC49FIZ.py` | `17a45ea59d86cca8768b16dc4ede52ae47d728a6e6b78ed9dc61ccb7ec1ea080` |
| `EXACT_REPORT_EC49FIZ.json` | `13d8b08a696c7b048629e417120c59b8b61c6c8fc4441659abb1c3281427fcc1` |

Those original executable Python programs were **actually run locally**, generating the full JSON reports. The repository stores lossless gzip + base64 versions of exactly those bytes (four corresponding `.gz.b64` files). Decode each with `base64 -d < FILE.gz.b64 | gzip -d > FILE`, restore sibling original `EC49FGW_RADIUS5_SCREEN.py` and `EC49FGJ_SEVEN_KEY_94_WITNESSES.json` in the same execution directory if necessary, then run `python VERIFY_EC49FIY.py` and `python VERIFY_EC49FIZ.py`. Both scripts use the pinned original legal-word grammar and original EC49FGJ witnesses, not a newly fabricated replacement model.

## Actual status and next discriminating unit

`AUTHOR_FINITE_EXACT / EXACT_NATIVE_PREFIX_CHECK_PASS / PORTABLE_DRAFT / UNREVIEWED / NOT_ADMITTED`. The source artifacts and this proof are author research material, not an authenticated immutable Task Result or independent Driver review. A GitHub PR or Source activity registration does not grant a CLAIM. No P000 or ACTIVE worldview changes.

**Next EC49FJA:** Examine six-path positions releasing original keys with `B>=9` where key recovery is forced and the known singleton obstruction is inconclusive. Group by full `F`, derive H8/H9 multi-observation union minima in a bounded exact search, and isolate any background on which a 93-edge completion remains feasible. Cross-reference EC49FIW and EC49FIX before counting any new exclusion.
