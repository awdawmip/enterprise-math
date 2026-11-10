# EC49FGJ — Two exact seven-key, 94-native-prefix BRC constructions

**Date:** 2026-11-10 (Asia/Shanghai). **Research status:** author-side constructive exact result. Immutable scientific pin: `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. The original nine-state DFA and six signed-X6 operation expansions are frozen in `EC49FCZ_H4H6H7_SIGNATURE_COMPLETE_128/frozen_model.py` (Git blob `7e97065ac9a0ff70435b92ee2f4bd718c9bf1859`). P000 and ACTIVE worldview are unchanged.

## Mathematical result

Let `C_min(k)` be the smallest number of distinct nonempty **ordered, signed native X6 microstep prefixes** among families meeting all 24 original demand labels, using at most `k` distinct raw complete positive-axis triples (zero coordinates are counted as distinct, not dropped). The frozen demands are H2/H3/H5/H9 signatures {16,32} and H4/H6/H7/H8 signatures {1,2,4,8}. Every operation word has exactly its H-window length, valid original DFA terminal signature, and signed-X6 displacement (+2,0,0,0,0,0).

**New exact constructive theorem:**
```
C_min(7) <= 94.
```
Two separate explicit 24-word certificates attain exactly **seven complete raw keys and 94 native prefixes**. Their seventh keys added to the existing six-key construction are respectively `(7,4,1)` (profile A) and `(6,5,1)` (profile B). All 48 words, two raw-key inventories, the operation DFA, six signed microstep expansions, and endpoint checks are in the adjacent portable witness and verifier. Direct literal prefix-set replay checks the two certificates, independent of optimization software.

The previous EC49FGH exhibited six keys and 100 prefixes, so the new witness decreases the **known constructive upper bound by six edges**. EC49FGD previously found a relaxed eight-key construction with 93 edges, hence the currently known attainable costs at these points are `k=6: <=100`, `k=7: <=94`, `k=8: <=93`. No global seven-key optimality is claimed.

## Reproducible fixed-allowlist optimization

Enumerate all legal words for each H window and each key in the following two allowlists:
```
K_base6 = {(2,1,1),(3,0,1),(3,1,1),(4,2,1),(5,4,1),(6,4,1)}
A = K_base6 U {(7,4,1)}
B = K_base6 U {(6,5,1)}
```
Use the EC49FGF exact candidate generator and BRC operation-trie native-prefix cost formula, with binary prefix selectors, sibling microstep overlap discounts and 24 terminal-signature covering constraints. Actual SciPy 1.17/HiGHS MIP runs independently returned fixed-allowlist `objective=94, dual_bound=94, gap=0, status=0` for **both** profiles. Each model has 16,963 nonroot operation-trie nodes and 3,098 sibling-overlap discount variables; LP relaxations were respectively 87.0 and 86.9. Reproducer: `SOLVE_EC49FGJ.py` (needs sibling `EC49FGF_EXACT_16_CLASS_DUAL_20261110/VERIFY_EC49FGF.py`). This is solver-backed optimality **only within the two specified key allowlists**, not a portable integer UNSAT certificate and not a global seven-key classification.

## Run exact independent constructive audit

```sh
python VERIFY_EC49FGJ.py WITNESSES_EC49FGJ.json
```

Expected output:
```
PASS A demands 24 raw_keys 7 signed_microstep_prefix_edges 94
PASS B demands 24 raw_keys 7 signed_microstep_prefix_edges 94
```

Two independent replays (including a separate local checker) completed on 2026-11-10. Check uses integers, signed ordered prefixes and the original nine-state DFA, no floating point. The MIP call is separate evidence; it is **not** needed to prove the upper bound. The frozen 24-signature/demand model is used unchanged. This proof does not make claims about physical dynamics or use a modified observer.

## Preservation, scope, next

Input provenance: EC49FGI five-key solver-backed 112 result; EC49FGH six-key 100 witness; EC49FGF enumeration and cost model; EC49FGD relaxed 8-key 93 witness. Current historical task `EC49AS` has no present immutable publication (`NO_CURRENT_IMMUTABLE_PUBLICATION` as of this run). No formal claim/Result or independent Driver admission is asserted; this is an independent author-side exact research record.

**Next discriminating question:** can **any** seven raw complete keys realize `C_native <= 93`? Explore alternate key covers with explicit 7-key activation constraints (not merely either fixed allowlist) and seek either a seven-key 93-edge word certificate or an independently checkable exact integer lower-bound certificate. Preserve the six-axis native endpoint and 24 frozen labels.
