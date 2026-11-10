# EC49FGK — Exhaustive raw-cache-key coverage taxonomy for original BRC 24 demands

Date: 2026-11-10 (Asia/Shanghai). Author-side finite exact combinatorial research; not a native Result or independent Driver admission.

Frozen scientific input: `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Original nine-state BRC observer and signed X6 expansions: `EC49FCZ_H4H6H7_SIGNATURE_COMPLETE_128/frozen_model.py`, immutable Git blob `7e97065ac9a0ff70435b92ee2f4bd718c9bf1859`. Existing exact seven-key 94-edge witnesses: `EC49FGJ_SEVEN_KEY_94_20261110/`.

## Exact mathematical statement

Define demand labels `D={(2,16),(2,32),(3,16),(3,32),(4,1),(4,2),(4,4),(4,8),(5,16),(5,32),(6,1),(6,2),(6,4),(6,8),(7,1),(7,2),(7,4),(7,8),(8,1),(8,2),(8,4),(8,8),(9,16),(9,32)}`. A key `K=(x,y,z)` is a **raw complete key**: the number of positive signed-X6 steps on axes 1,2,3 of a legal length-h BRC operation word ending at displacement (+2,0,0,0,0,0). Zero is retained, and distinct triples are distinct keys. Let `S(K)` be all labels realized by at least one legal word with that key. A k-key cover is an unordered set of exactly k **distinct** such keys with union of supports equal to D.

**Theorem (finite exact enumeration).** Among all legal raw keys supporting at least one of D, exactly 94 distinct keys occur and there are 178850 legal matching operation words when counted separately by window/key/signature. The number of k-key support covers is:

| Exactly k raw keys | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Covers of all 24 labels | 0 | 0 | 0 | 0 | 0 | **16** | **2004** | **108434** |

Every such cover, for any k, contains `(2,1,1)` and `(3,0,1)`: respectively the unique keys that can satisfy H2 signature 32 and H2 signature 16. Of the 108434 seven-key covers, **1956 omit `(3,1,1)`**, and 106478 include it. Thus the third key of the 16 canonical five-key covers is no longer forced at seven keys.

An explicit seven-key *support cover* omitting `(3,1,1)` is `{(2,1,1),(3,0,1),(2,2,1),(4,0,1),(4,2,1),(5,4,1),(6,4,1)}`. This is an allowed-key inventory satisfying demand coverage, not a claim of 93 signed-microstep prefixes.

## Derivation and completeness

The frozen positive-key count equations for a length-h legal word, writing `a=z-1`, `b=c+d=x+y-h-1`, `f=h+1-y-2z`, `g=h+1-x`, require `a,b,f,g >= 0`. Thus an exhaustive finite key search uses `1<=x<=h+1`, `0<=y<=h+1`, `1<=z<=floor((h+1)/2)` for each h=2..9. For every admissible key, enumerate all nonnegative splits `c+d=b`, all distinct operation-code permutations with counts `(a,c,d,z,f,g)`, and pass each prefix through the literal nine-state DFA (reject sink state 8). Record only final signatures required by D. This gives the 94 exact per-key support masks; there are 21 distinct support-mask classes, **not** cost-equivalence classes.

Number the 24 demand labels and represent `S(K)` by its 24-bit mask `m(K)`. For the first i keys in a fixed enumeration, let `F_i(k,U)` be the number of unordered subsets containing exactly k of those keys and having union mask U. Initialize `F_0(0,0)=1`, others 0. On adding key i with mask m, update `F_{i+1}(k,U) = F_i(k,U) + sum_{V : V OR m = U} F_i(k-1,V)`. This is an exact integer recurrence: every subset either includes or excludes the new key, and the cases are disjoint. At U=2^24-1 the recurrence yields the table.

The two H2 signature masks each have a unique key in the complete catalogue, establishing the forced pair. Deleting `(3,1,1)` and re-evaluating the same recurrence gives 1956 seven-key covers without that key. The dynamic-program state counts at k=0..7 are `[1,21,171,716,1793,3002,3746,3951]`.

## Executed verification

`VERIFY_EC49FGK.py` reproduces every candidate key and supporting word from the frozen DFA, exports `EC49FGK_key_masks.txt`, performs the exact integer union-mask DP, checks both forced H2 keys, and emits `EXACT_REPORT_EC49FGK.json`. Executed locally: `PASS exact_cover_count k=5,6,7: [16, 2004, 108434]`; `PASS seven_without_3_1_1: 1956`; `PASS catalogue: 94 keys, 178850 matching words`.

`VERIFY_EC49FGK_CPP.cpp` is a separately compiled direct subset enumerator. Compile with `g++ -O3 -std=c++17 VERIFY_EC49FGK_CPP.cpp -o verify_cover`, then run `./verify_cover EC49FGK_key_masks.txt`. Executed locally and returned exit status zero: `EXACT_5 16`, `EXACT_6 2004`, `EXACT_7 108434`, `SEVEN_WITHOUT_3_1_1 1956`, `SEVEN_WITH_3_1_1 106478`. It counts all `92 choose 3/4/5` subsets after the analytically forced H2 pair, using a separately implemented enumeration rather than the Python DP. It consumes the Python-generated support catalogue, so the DFA and key extraction are a shared scientific input.

## Mother objective and next discriminating unit

Original mother optimization: 24 labels, signed ordered native-X6 microstep prefixes, and a cap on the number of distinct raw complete keys. Previous results: 5 keys cost 112 in the solver-backed optimum; 6 keys have a 100-edge construction; 7 keys have two 94-edge constructions; 8 keys have a 93-edge construction.

The exact seven-key question is `C_min(7) <= 93 ?`. This classification supplies **108434 concrete allowed-key subsets** and exposes **1956 seven-key alternatives lacking `(3,1,1)`**. The next algorithmic step is to use cheap support/mask grouping and rigorous lower bounds to prune subsets, then run the signed-prefix MILP on remaining allowed-key sets. A support cover alone does not determine the signed native-prefix cost: code order, sibling sharing and microstep prefixes remain the optimization variables. Retain fixed key cardinality, original observer, endpoint and signed-prefix verification.

## Authority, provenance and status

Read: current global canonical main `7c1e5455406fbfb25548a0762e481bed5d8fb4da`; EM main `5922034412fed9c0a663cef6ab3354926af1ca0d`. Research source predecessor PR #1730 `8a4b18ce30f1efa92df2b7590d1b82eee6871fc1`; scientific pin unchanged. Researcher-ID `EM-DIRECT-F4374F`, native Research-Activity-ID `RA-31878E628876370CC15873E4` (the session/activity canonical Source record was confirmed). Native exact task query for historical `EC49AS` returned `CANONICAL_REJECTED: NO_CURRENT_IMMUTABLE_PUBLICATION`; author-side work retains no CLAIM or formal Result. Project P000 and ACTIVE worldview unchanged.

Status: `AUTHOR_EXACT_FINITE_CLASSIFICATION / PYTHON_DP_PASS / C++_BRUTE_FORCE_PASS / PORTABLE_DRAFT / UNREVIEWED / NOT_ADMITTED`. The GitHub branch commit and readback report separate persistence from mathematical acceptance.
