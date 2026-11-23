# T6 portable author exact unit: p13 q10 signed (1,9), negative q=(1,1,1,1,2,3), first 32,000 named rosters

- Scientific pin: `awdawmip/enterprise-math@d84bd940cfb093cdc60e569f15cad58772a51dca` (unchanged).
- Source prior frontier: `research_notes/portable_direct/onhour_20261123_t6_p13_q10_signed_neglen6_111114_author_continuation_1425.json`, verified main blob `d1c6a8529453cf6f3ce42f5159ffda8437343805`.
- Parent: `RS-T6-SHAPE-MOMENT-GLOBAL-LOWER-BOUND` (OPEN). Portable author computation only; no current native CLAIM/PROGRESS, no Result/admission/independent review.
- Source certificate: `research_checks/T6_P13_Q10_SPLIT1_9_NEG111123_FIRST32000_AUTHOR_EXACT_CERT_20261123.json`.

## Exact finite proposition (conditional on existing p13 reduction/complete saturated q0-lattice)

For positive q-pattern (1), negative q-pattern (1,1,1,1,2,3), first 32,000 negative named multisets ordered by nondecreasing residues in the four q=1 slots followed by q=2 and q=3 residues 1..12, there is no pair of positive residue 1..12 and negative roster with no common vertical atom, original positive and negative mass at most 2331, and all six necessary 13-adic mixed congruences.

**Exact integer coverage:** 32,000 negative rosters × 12 positive residues = **384,000 raw pairs**. Of these 105,536 share a named atom and belong to the established common-atom cancellation case; 0 fail the vertical-only mass budget; 278,464 were subjected to the full exact q0 affine lattice search (672,102 GS recursion nodes). **One** affine relaxed-sphere leaf satisfies all six congruences but has original masses **(3682, 4614)**, exceeding both side budgets. Thus 0 feasible configurations in this bounded scope.

The leaf has positive `(q,r)=(1,2)`, negative `[(1,1),(1,1),(1,3),(1,7),(2,2),(3,8)]`, signed q0 vector `(-37,33,18,4,9,-13,-2,3,1,6,-4,-4)`. Its six exact modular residues are all zero.

## Arithmetic and coverage semantics

At p13, the q0 mass weights are `w_r=13r-1` for `r=1..12`; vertical atom weights are `169q+13r-1`. The signed q0 coefficients satisfy
[
\sum_{r=1}^{12}u_r r^{-j} + \sum_{v\in V_+}(13q_v+r_v)^{-j} - \sum_{v\in V_-}(13q_v+r_v)^{-j}\equiv0 \pmod{13^j},\quad j=1,\ldots,6.
]
The previously published saturated q0 basis has determinant index `13^21`. Convert its weighted 12-dimensional basis by exact LLL then exact rational Gram–Schmidt, with
`dmin=78577530278042129705264382752517501995032553011464356025/4243983974238642688103181306691645151538473248349 > 2*2331^2`.
For each pair, after removing common atoms and vertical-only overbudget cases, center the affine coset at its exact rational representative and enumerate nearest-two integers at every descending GS coordinate, retaining nodes within
`R²=(2331-M_{+,vertical})²+(2331-M_{-,vertical})²`.
Since `R² <= 2*2331² < dmin`, every coordinate can contribute at most the two nearest integers; the branch recursion is complete for the budget ball. Each leaf is reconstructed to integral 12-component q0 coefficients, checked against the six exact modular equations and the two original mass inequalities. The pair-order SHA256 in the certificate hashes all 384,000 ordered raw pairs, including the cancelled ones.

This computation used the exact q0 kernel already published at `research_checks/T6_P13_Q9_SPLIT1_8_NEG_LEN1TO4_EXACT_REPLAY_20261123_0900.py` and applied its `pair_search` to q-pattern (1,1,1,1,2,3). The local adapted script and local JSON hashes are recorded in the certificate; the adapted script is not independently published or replayed, hence this is **author execution, unreviewed and not admitted**.

## Recovery

Do not repeat negative roster indices `[0,32000)`. Next contiguous interval starts at **32000** in the same canonical negative-roster order and continues to `196560`. This portable p13 work remains independent of the formal Source p17 q14 preflight/claim frontier. Identity-protected semantic checkpoint and Activity linkage await the genuine Research-session/owner path.
