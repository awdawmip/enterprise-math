# T6 p13 q-order9 split(4,5), positive (1,1,2), negative (1,1,1,2): complete exact author exclusion

Date: 2026-11-23. Mother: `RS-T6-SHAPE-MOMENT-GLOBAL-LOWER-BOUND`. Scientific input frozen at `awdawmip/enterprise-math@d84bd940cfb093cdc60e569f15cad58772a51dca`. Source evidence: `research_checks/T6_P13_Q9_SPLIT45_POS112_NEG1112_FULL_AUTHOR_EXACT_CERT_20261123.json`. Exact repository replay: `research_checks/T6_P13_Q9_SPLIT45_POS112_NEG1112_REPLAY_20261123.py` (published after author execution, not independently rerun).

## Claim and domain

For maximal prime 13 and 13-valuation one, the original two-side exponent-mass bounds `M_+,M_- <= 2331`, exact named denominator `13(13q+r)`, signed multiplicity and six necessary 13-adic congruences from `H_0,...,H_6`, the vertical order-9 split `(4,5)` with positive q partition `(1,1,2)` and negative q partition `(1,1,1,2)` contains **no admissible pair**. The result depends on the previously saved cancellation of 13-valuation >=2 atoms and saturated 12D q0 lattice. It is an author-level finite theorem over this exact family, not a proof that all T6 or the entire p13 layer is closed.

A vertical atom `(q,r)`, `1 <= r <= 12`, is denomination `13(13q+r)`, exponent cost `169q+13r-1`. An integer q0 correction `u_r` refers to denomination `13r`, exponent cost `13r-1`. For every `j=1,...,6` the necessary congruence is

```
sum_r u_r * r^(-j) + sum_(q,r) in plus (13q+r)^(-j)
 - sum_(q,r) in minus (13q+r)^(-j) = 0 (mod 13^j).
```

The q0 solution space is the previously saturated rank-12 integer lattice of index `13^21 = 247064529073450392704413`. Its exact rational Gram–Schmidt minimum square

```
78577530278042129705264382752517501995032553011464356025
/4243983974238642688103181306691645151538473248349
```

exceeds the maximum necessary sphere radius `2*2331^2 = 10867122`. For any fixed vertical pair, every lattice representative inside the original budget's necessary Euclidean ball is covered by testing the two nearest integers at each GS coordinate; all comparisons and modular inverses are exact.

## Complete finite calculation

The positive q partition has `C(13,2)*12 = 936` named multisets; the negative partition has `C(14,3)*12 = 4368`. The full ordered product is `4,088,448` named signed pairs. Seven contiguous nonoverlapping ranges `[0,24),[24,124),[124,436),[436,1000),[1000,2000),[2000,3000),[3000,4368)` exhaust all 4368 canonical negative rosters. The positive complete 936 roster is visited for each negative roster. Canonical order is combinations-with-replacement `r=1..12` within equal q groups, q1 then q2, with negative outer loop. Each range's complete stats, pair-order digest, roster digest and local JSON SHA256 are in the certificate.

| Count | Value |
|---|---:|
| All raw ordered pairs | 4,088,448 |
| Exact named atoms shared by both signs (cancel to earlier strictly lower-order families) | 1,718,784 |
| Disjoint-support pairs receiving complete exact q0 affine enumeration | 2,369,664 |
| Excluded on vertical mass alone | 0 |
| Exact GS recursion nodes | 4,889,804 |
| Affine sphere leaves | **0** |
| Original two-side-budget-valid leaves | **0** |

The complete primitive disjoint-support search has no necessary ball representative. Shared-support pairs are exact signed cancellations into previously author-excluded lower vertical orders (all relevant q-orders 0–8), so they do not produce a new primitive order-9 collision. No unvisited range is included in the conclusion.

## Validation, provenance and next action

A fresh local Python Fraction/SymPy exact implementation executed all seven ranges with per-range digests and no leaves. Its source SHA256 is `976a1e67dd6497f58a9c093f468af620e1b5ce12118323d534428f08747f1dfe`; original per-range JSON files were local at author execution. The repository replay wrapper imports the previously published exact q0 kernel, but was not separately rerun after publication. These are **AUTHOR_EXACT_FINITE_EXECUTED / UNREVIEWED / NOT_ADMITTED** data, not an independent Review, Native semantic PROGRESS or Result.

Next minimal science: order-9 split `(4,5)`, positive q partition `(1,1,2)`, negative q partition `(1,1,1,1,1)` (4368 negative rosters ×936 positive); then positive `(1,1,1,1)` against the complete order-5 negative roster. Keep p13 higher orders, lower maximal primes, H0 completion and global hard target `T6=2332` OPEN. Native Source p17 q14 assigned work remains a separate ownership track; the ordinary Research lane does not borrow its claim.
