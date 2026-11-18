# EC49FGK Addendum — Inclusion-minimal support covers

Date: 2026-11-10 (Asia/Shanghai). Same frozen model and pin as `README_EC49FGK.md`.

A *cover* of 24 original BRC demand labels by exactly k distinct raw complete cache keys is **inclusion-minimal** if deleting any one of its k keys loses coverage of at least one label. This notion concerns 24-bit demand-support masks, **not** signed-X6 native-prefix optimization. In particular, keys whose deletion preserves support might still permit shorter native prefix costs via extra path choices, so these counts should not be used as a completeness-preserving filter for optimizing all seven-key cost solutions.

## Exact classification

| k keys | All support covers | Inclusion-minimal support covers | Inclusion-minimal covers omitting (3,1,1) |
| --- | ---: | ---: | ---: |
| 5 | 16 | **16** | 0 |
| 6 | 2,004 | **628** | **16** |
| 7 | 108,434 | **4,904** | **612** |

This distinguishes a strict minimal-support seven-key subfamily with 4,904 possibilities, including 612 that avoid the original third five-key member. It is a tractable **prioritized heuristic search family**, while full mathematical optimality questions retain all 108,434 seven-key covers and, where the optimization allows fewer actual keys, relevant lower-cardinality covers.

## Complete finite proof and executed checker

In the already established exhaustive list of 94 raw keys, H2 demand 16 forces key `(3,0,1)` and H2 demand 32 forces `(2,1,1)`. Therefore every support cover consists of these two forced keys plus `k-2` keys chosen without repetition from the remaining 92. For each candidate set, form the bitwise OR of the k support masks; it is a cover iff it equals `(1<<24)-1`. Because the two H2 keys are universally forced, each is automatically essential. The cover is inclusion-minimal exactly when, for every one of the remaining `k-2` keys, the OR after deleting it fails to equal the full 24-bit mask. This is a necessary and sufficient test of inclusion minimality.

`VERIFY_EC49FGK_MINIMAL.cpp` performs a direct exact-integer enumeration of all `92 choose 3`, `92 choose 4` and `92 choose 5` combinations. It uses only the 94-mask frozen-model catalogue from `VERIFY_EC49FGK.py`. The independently run local code, before adding input checks and final equality assertions to the published version, returned:

```text
K=5 covers=16 inclusion_minimal=16 minimal_without_3_1_1=0
K=6 covers=2004 inclusion_minimal=628 minimal_without_3_1_1=16
K=7 covers=108434 inclusion_minimal=4904 minimal_without_3_1_1=612
```

The source, finite-domain derivation and exact output are preserved. The added published version checks catalogue length and exit-code consistency; the published version's extra guards were not separately executed in the original local run.

## Next scientific unit

Use the 4,904 minimal-support seven-key covers to test inexpensive signed-X6 prefix lower bounds and identify promising shared-prefix designs. In parallel, retain nonminimal support covers as admissible (they can offer additional word choices and lower cost). The immediate discriminating target is an explicit seven-key original-24-label legal signed-path certificate with at most 93 native prefixes or a valid complete lower bound of 94 over all eligible seven-key inventories.

Provenance: Author-side researcher `EM-DIRECT-F4374F`, activity `RA-31878E628876370CC15873E4`; historical task EC49AS current publication unavailable, no CLAIM/Result or independent Driver review. No P000 or ACTIVE worldview change.
