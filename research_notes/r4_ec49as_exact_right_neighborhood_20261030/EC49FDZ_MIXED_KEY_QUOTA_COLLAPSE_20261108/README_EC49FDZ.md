# EC49FDZ — Mixed-key rank-and-quota collapse to 64 triples

Date: 2026-11-08 (Asia/Shanghai). Frozen scientific input: fc0f038e7bfd12c886b4d37f900bfb770c0f61ab. Status: author-side finite proof and exact integer census; independent canonical Driver review pending.

## Exact theorem

Use the original six ordered typed native-X6 operations a,c,d,e,f,g, the full positive BRC cache key k=(x,y,z), signed displacement +2E1, the original nine-history observer and six permitted nonzero terminal signatures. The exact number of distinct complete words in H4,...,H9 is (2,4,2,4,4,2). Each horizon must have rational observation rank nine.

Let T consist of the 6734 unordered triples of distinct later BRC keys classified by EC49FDU: all three keys jointly offer rank nine at every H4 through H9, while no pair of keys does so at all six horizons. Allow any mixture of the three keys within each window, with only the stated exact word quotas.

**Theorem:** Exactly **64** triples in T admit all six rank-and-quota requirements. The other **6670** fail at H4, H6, or H9. The surviving 64 triples are exactly the old single-key three-phase Cartesian family A × B × C:

A = {(3,2,1),(4,1,1)}; H4.
B = {(3,4,1),(5,2,2),(6,1,1),(6,1,2)}; H5 and H6.
C = {(4,6,1),(5,5,1),(6,4,2),(7,3,1),(7,3,2),(8,2,1),(8,2,2),(8,2,3)}; H7, H8, H9.

Every rank-and-quota-feasible triple of T therefore admits a three-block witness, switching after H4 and H6, even though arbitrary intra-window mixing was permitted. This is a classification of key *sets*, not a claim that mixing cannot improve the signed primitive prefix cost for one of the 64 survivors.

## Proof and coverage

The original nine-history observer has Boolean terminal mask m and exact rational rank-nine criterion

(m & 18) != 0 and (m & 20) != 0 and (m & 33) != 0 and (m & 40) != 0.

These four clauses are respectively (16 OR 2), (16 OR 4), (32 OR 1), (32 OR 8). One complete word supplies exactly one of six terminal signatures. Two distinct selected words cover all four clauses if and only if one has signature 16 and one has signature 32. For four selected words, rank-nine support together with at least four available distinct words suffices: choose one witness per clause, remove duplicate selections, and extend to exactly four words. Minimal terminal-signature covers are {16,32}, {16,1,8}, {32,2,4}, and {1,2,4,8}.

To count eligible complete words, use an exact nonnegative-integer DP over (number of each of the six operators, nine-history state). Appending operator i increments its operation count and applies the original state transition. The endpoint condition +2E1 is equivalent here to n_e=n_a+1. For each accepted word its full typed positive BRC key is

k = (2n_e+n_c+n_d+n_f, n_c+n_d+n_g, n_e).

No truncation or approximate arithmetic is used. The DP supplies exact terminal-signature multiplicities for each (h,k). It finds 155 distinct later keys and 124 rank-feasible two-key sets, agreeing with EC49FDU, then enumerates all unordered three-key sets and selects precisely 6734 satisfying the definition of T.

Across those 6734 triples, the minimum numbers of accepted complete words at the four-word windows H5, H7, H8 are respectively **10, 14, 16**. Those windows are therefore automatically quota-feasible under the defining rank condition. The *entire* quota question reduces to existence of signature-16 and signature-32 words at the two-word windows H4, H6, H9.

The exact census partitions the 6734 triples as follows:

| Failed two-word windows | Number of key triples |
| --- | ---: |
| H4 only | 360 |
| H6 only | 154 |
| H9 only | 104 |
| H4 and H6 | 672 |
| H4 and H9 | 1864 |
| H6 and H9 | 484 |
| H4, H6 and H9 | 3032 |
| None (all quotas feasible) | **64** |

The 64 survivors are checked for exact set equality against the 2 × 4 × 8 Cartesian family displayed above. Each member of A independently supplies H4 rank and quota, each member of B supplies H5 and H6, and each member of C supplies H7, H8 and H9; hence the advertised three-block witnesses exist. The four H4-mixed exceptional triples from EC49FDU fail the H6 two-word test: their only H6-capable key (6,4,1) supplies terminal signatures 1,2,4,8, rather than the required 16 and 32.

## Verification and evidence

Run the standard-library script EC49FDZ_MIXED_KEY_QUOTA_CENSUS.py in this directory. It executes the complete exact DP and triple census, checks all claimed numeric identities, re-enumerates literal native operator words for **57** (h,key) tests at H4/H6/H9, and checks their signed X6 displacement, BRC primitive counts and exact signature multiplicities against the DP. It outputs the exact RESULT and all 64 surviving key triples as JSON. No non-BRC physical fallback, pi/trigonometric expansion or approximate reference physics is involved.

Independent full-witness cross-check: the previously published EC49FDV 128 explicit H2–H9 systems were re-checked this run using VERIFY_EC49FDV_INDEPENDENT.py and exact Fraction Gaussian elimination: **128/128** full constructions and **1024/1024** rank-nine horizon tests passed. Their 64 later-key sets equal all EC49FDZ surviving sets. These are explicit realizations, not a native prefix-cost optimality or formal task acceptance certificate.

Source lineage: EC49FDU commit 73c954d996082450c632f7150688ec1de0473375; EC49FDV commit 7e3b0450c17c4fe1b6e604b5749fb762d3eca63e; EC49FDY latest fixed-schedule optima at cd72977b7b821e13c138b0b0e12d4502ea084567. Frozen scientific pin remains fc0f038e7bfd12c886b4d37f900bfb770c0f61ab.

## Next unit EC49FEA

Within the 64 surviving later-three-key sets, jointly optimize full signed native prefixes while permitting *mixed keys in each horizon* and fixed H2/H3 initially. Separately examine the late-key families containing a rank-feasible two-key subset, and changed early key spending. The original five-key mother objective seeks a complete H2–H9 system with at most **93** native prefix edges; the validated mother-problem bound is still **94** from the earlier construction.
