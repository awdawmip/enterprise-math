# EC49FGO — Exact one-incoherent H7/H8 local obstruction

2026-11-10. AUTHOR_EXACT_FINITE_CERTIFICATE / EXECUTED_TWO_INDEPENDENT_CHECKERS / UNREVIEWED / NOT_ADMITTED. Frozen scientific pin: fc0f038e7bfd12c886b4d37f900bfb770c0f61ab. Frozen nine-state BRC operation and ordered signed-native X6 model: EC49FCZ/frozen_model.py, Git blob 7e97065ac9a0ff70435b92ee2f4bd718c9bf1859. Existing full 24-demand 7-key 94-prefix witnesses are in sibling EC49FGJ/WITNESSES_EC49FGJ.json. Predecessor EC49FGN proved the four-coherent-pair subcase.

## Finite theorem

For either EC49FGJ witness A or B, hold the sixteen paths outside H7 and H8 fixed as literal ordered signed native paths. Replace the four H7 and four H8 original BRC low signatures (1,2,4,8) with any lawful words ending at native displacement (2,0,0,0,0,0). If at least three same-signature H7/H8 word pairs are operation-prefix coherent (H7 word equals first seven operations of H8 word), the number of distinct nonempty ordered signed X6 microstep prefixes is at least 94. Original witnesses attain 94. This lower bound allows *unlimited* raw complete cache keys.

Hence a <=93 solution under either fixed-16 background must break coherence in at least two signatures; another valid direction is changing at least one fixed background word. No claim is made about the global all-seven-key optimum.

## Complete enumeration

Let F be the signed microstep-prefix union of the fixed 16 words (both cases size 78), and D(w) be each candidate's exact microstep prefixes outside F. Every <=93 completion must have at most 15 additional prefixes, so every chosen variable word individually satisfies |D(w)|<=15. This filter is exhaustive.

Rather than relying on the prior 94-key catalog, the attached reproducible script enumerates every six-operation-count vector (a,c,d,e,f,g) whose sum is H7/H8 and where e=a+1, a necessary and sufficient endpoint condition in this frozen operation system. It generates every permutation allowed by the nine-state DFA. Per-signature legal counts: H7 5724/6806/5724/6806; H8 28063/34777/28063/34777. All intermediate native prefixes are encoded by an injective map of full ordered signed step tuples into integer bit positions.

For each exceptional signature t, choose coherent pairs for the other three signatures. A coherent pair contributes exactly its H8 prefix mask. Enumerate all three-mask unions costing <=15, replace superset triples by contained legal triples where possible, and test every H7 and H8 candidate word for t against each three-mask union. Apply the necessary per-word remainder test before examining the complete union. Each accepted combination is tested and every resulting union is >15; in zero-pair cases all candidate pairs fail the necessary per-word filter.

| Witness | Exceptional signature | Three-coherent unions <=15 | Exact final pair comparisons | <=93 exists |
| --- | ---: | ---: | ---: | --- |
| A | 1 | 1232 | 0 | No |
| A | 2 | 1712 | 128 | No |
| A | 4 | 1552 | 0 | No |
| A | 8 | 1776 | 128 | No |
| B | 1 | 1776 | 128 | No |
| B | 2 | 1776 | 128 | No |
| B | 4 | 1296 | 0 | No |
| B | 8 | 1616 | 0 | No |

Two separately implemented local programs produced the same counts. VERIFY_EC49FGO.py is the short actual executed program (two separate runs A and B). EXACT_AUDIT_EC49FGO.json is its structured compact report. Further full detailed report, two-run stdout and independent longer checker are in the author evidence archive.

Run from this folder using Python standard library:
  python3 VERIFY_EC49FGO.py --profile A
  python3 VERIFY_EC49FGO.py --profile B

Next: with the same fixed 16-word background permit two incoherent H7/H8 signatures while the other two remain coherent; apply <=7 raw complete keys separately. A candidate <=93 must be validated with the original nine-state observer, exact X6 endpoint, every ordered signed microstep prefix and complete raw cache-key count. The complementary route changes one or more of the background words.

Researcher-ID EM-DIRECT-A55F45 / TASK_RESEARCH; Source-native Research-Activity-ID RA-D88D73E8E56FCD09B1C9CDF4. Historical EC49AS control query: NO_CURRENT_IMMUTABLE_PUBLICATION. No formal CLAIM, Result or independent Driver review.
