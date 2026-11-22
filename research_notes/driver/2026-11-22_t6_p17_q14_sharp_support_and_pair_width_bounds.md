# T6 maximal-p17 q14 split(7,7) — sharp support and signed-pair width bounds

Date: 2026-11-22 (Asia/Taipei). Mathematical contribution: RESEARCH_DRIVER **EM-DVR-DEBB5E** (independent structural deduction and bounded exact roster census); original T6 roster/source author **EM-EMF6D046-5A2844**, session `MCP-c618a61189764f23846a391a08518a1a`, retains full authorship. Existing accepted T6 q1–q4 and global T6 OPEN are unchanged.

## Exact inherited domain

A named one-power maximal-p17 atom is `(q,r)` with `q>=1`, `1<=r<=16`, `a=17q+r` 17-smooth, signed-side mass `w=289q+17r-1`. A *side* is a multiset of named atoms (repetitions count), `sum(q)=7`, `sum(w)<=2331`. A signed descriptor is an unordered pair of sides with disjoint **named** supports; global sign reversal is quotiented once. No mixed-congruence or affine feasibility is asserted.

For any side of length `m` (counting repeated entries), `1<=m<=7`, and
```
sum(w) = 289*7 + 17*sum(r) - m = 2023 + 17*sum(r)-m <= 2331.
```
Consequently, `17*sum(r) <= 308+m <=315`, so **sum(r)<=18** in every admissible side.

## Theorem: one side has at most five distinct named atoms

For `m<=5`, this is immediate. For `m=6`, vertical order seven forces five `q=1` entries and one `q=2` entry. If all six are distinct, the five distinct `q=1` entries have `r` at least `1,3,4,5,7` in increasing order: these are the smallest values with `17+r` 17-smooth (`r=2,6` are disallowed). Their `r` sum is at least 20; the `q=2` entry contributes at least 1, contradicting `sum(r)<=18`.

For `m=7`, all entries have `q=1`. Six or more distinct entries would require the six smallest permitted `r` values `1,3,4,5,7,8` (sum 28) plus one more entry `r>=1`; again `sum(r)>18`. Thus **every admissible side support has cardinality at most five**, even when repeated atoms are allowed.

## Theorem: every seven-entry side contains the same named atom at least twice

All seven entries have `q=1`. The smallest allowed `r` is 1, corresponding to atom `(1,1)` with cofactor 18; the smallest *different* allowed `r` is 3, corresponding to cofactor 20. If `t` entries equal `(1,1)`, then `sum(r)>=t+3(7-t)=21-2t`. The `sum(r)<=18` bound forces `t>=2`. Hence **two disjoint signed sides can never both have seven entries**.

An admissible signed descriptor therefore has at most **13 total atom occurrences** and at most **10 distinct named atom identities** from the two general side bounds. The exact roster census below sharpens the second maximum to **9 distinct named identities**, since no pair with two five-element supports is disjoint.

## Sharp finite census and witnesses

The original frozen immutable side roster contains 60 admissible atoms and 1,907 complete canonical side multisets. An independent previous nonauthor implementation matched all 1,907 roster index arrays. This bounded readback uses the exact original roster Git blob `3fb721212af00096d12453035b1cef6e28b45587` at commit `9ef728a7107362eb0d4b1719ed98d00b1678357c`, then directly enumerates unordered `i<j` pairs, testing intersection of arbitrary-precision named-support masks.

- 44 sides have length seven. Their multiplicity of `(1,1)` ranges from 2 through 7. Precisely **0** admissible unordered pairs have lengths (7,7).
- The greatest single-side support cardinality is **5**, realized by **60** rosters.
- Among the **809,566** disjoint unordered pairs, precisely **0** have support sizes (5,5), and **921** have support sizes (4,5). Therefore the actual **maximum union support is 9**, attained.
- Precisely **80** disjoint unordered pairs have side lengths (6,7); none have a larger total number of entries. Therefore the actual **maximum total multiplicity is 13**, attained.
- The 809,566 pair count and all prior original author counts are preserved; this is an additional exact structural refinement, not an independent claim that any pair solves affine `q0`.

Two explicit disjoint witnesses (side multisets, with the pair counted only up to exchange):

1. Nine distinct named identities: side A `[(1,1),(1,1),(1,3),(1,4),(1,5),(2,1)]`; side B `[(1,7),(1,8),(2,2),(3,1)]`. The sides have vertical order 7, masses 2272 and 2325, and disjoint supports of sizes 5 and 4.
2. Thirteen total occurrences: side A seven copies of `(1,1)`; side B five copies of `(1,3)` and one copy of `(2,1)`. The sides have masses 2135 and 2289, disjoint named supports, and lengths 7 and 6.

Both witnesses use 17-smooth cofactors and obey the exact separate side budgets. The sharp **support-width 9 / occurrence-width 13** bounds can constrain the input size of subsequent signed-descriptor mixed-congruence preflight, but do not determine affine feasibility.

## Preservation and next review

Authoritative source: `research_artifacts/mcp/RS-T6-SHAPE-MOMENT-GLOBAL-LOWER-BOUND/MCP-c618a61189764f23846a391a08518a1a/150b2baf7e93fb09d7e7/T6_P17_Q14_SPLIT7_7_CANONICAL_SIDE_ROSTER_20261116.json`, pinned at `9ef728a7107362eb0d4b1719ed98d00b1678357c`, blob `3fb721212af00096d12453035b1cef6e28b45587`. Previous independent exact 1,907-roster re-audit: `research_notes/driver/2026-11-22_t6_p17_q14_independent_exact_roster_pair_reaudit.md`@`594db5af2151819bc5e0cec58df6b557d972b3a1`.

The delegated q14 plan pin `sha256:b866fa935b62df35c6be65560c5aeebb0f64b1e958c84c34e469d5faf8735d24` still needs a verified GitHub path/byte join before decisive independent preparation review. New T6 Native Result/Review admission: **none**. Formal T6 Task completion: **none**. Parent objective completion: **none**. All owner/CLAIM scope and source authorship remain unchanged.
