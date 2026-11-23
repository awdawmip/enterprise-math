# T6 maximal-p13 order9 split (0,9): exact exclusion of 1–5 vertical-atom rosters

2026-11-23, Asia/Hong_Kong. Existing parent \`RS-T6-SHAPE-MOMENT-GLOBAL-LOWER-BOUND\`. Frozen scientific source: \`d84bd940cfb093cdc60e569f15cad58772a51dca:research_tasks/T6_SHAPE_MOMENT_GLOBAL_LOWER_BOUND_20260909.md\`; neither source nor P000/worldview changed. Research logical lane declared \`chatgpt-research-onhour-enterprise-math-20260923\`, kept separate from maintenance. **AUTHOR_EXACT_FINITE_EXECUTED / UNREVIEWED / NOT_ADMITTED**.

## Precise new statement

Assuming the previously saved p13 higher-valuation cancellation and exact saturated q0 lattice results, consider any original T6 degree-6 collision candidate with each side's exponent mass at most **2331**, maximal prime 13, residual 13-valuation-one vertical total order 9, split \`(0,9)\` (positive side contains no positive-q atoms). If the negative side has **at most five named positive-q atoms counted with multiplicity**, the six global 13-adic necessary congruences have **no solution** respecting both original mass budgets. This rules out 249,184 complete named negative-side rosters; it makes no assertion about rosters containing 6–9 atoms or other order9 splits.

A named vertical atom is \`(q,r)\`, denominator \`a=13(13q+r)\`, original exponent mass \`169q+13r-1\` with \`q>=1\`, \`1<=r<=12\`. The signed q0 fiber \`u_r\` is the exponent-multiplicity difference at denominator \`13r\`, retaining sign, residue, named composite atoms and both individual masses. This labeled valuation/BRC carrier is not replaced by prime-only counts or a total-only observer. The exact observer requirement is original \`H_0..H_6\` equality; binomial inversion and p13 localization yield, for \`j=1,...,6\`:

\[
 \sum_{r=1}^{12} u_r r^{-j}
 -\sum_{(q,r)\in V_-}(13q+r)^{-j}
 \equiv0\pmod{13^j}.
\]

All 13-free smaller-prime atoms are allowed, so this is a **global necessary** test, not an unjustified equality of the local p13 rational moments.

## Reproducible finite coverage and exact arithmetic

For each integer partition of 9 having length 1–5, enumerate every multiset of residues \`r=1..12\`, sorted within each equal-\`q\` group. There are **23** partition patterns. The pattern-level counts are in the accompanying exact certificate. This enumerates \`249184\` distinct named rosters; all satisfy the negative vertical budget before adding q0 atoms.

For each roster, form the exact inhomogeneous congruence coset using the previously validated 12-dimensional saturated q0 lattice, index \`13^21\`. Its LLL-reduced *weighted* basis was recomputed using exact HNF/LLL and rational Gram–Schmidt; the least Gram–Schmidt diagonal square is the original exact rational \`78577530278042129705264382752517501995032553011464356025/4243983974238642688103181306691645151538473248349\`, greater than \`2*(2331)^2=10867122\`. For a vertical side of mass \`c\`, every admissible q0 solution satisfies the necessary sphere \`||W u||^2 <= 2331^2+(2331-c)^2\`. At each descending GS coordinate only its two adjacent integers can lie in that sphere. Branching both, using exact fractions throughout, is exhaustive; exact separate-side mass tests and all six congruences confirm any remaining leaves.

| Vertical atom count | Complete rosters | Exact GS recursive nodes | Sphere leaves | Both original budgets |
|---:|---:|---:|---:|---:|
| 1–3 | 8,944 | 25,249 | 0 | 0 |
| 4 | 53,664 | 150,325 | 1 | 0 |
| 5 | 186,576 | 518,602 | 2 | 0 |
| **Total** | **249,184** | **694,176** | **3** | **0** |

The three sphere leaves are genuine modular candidates rather than empty-sphere assertions; their full signed q0 coordinate vectors and two-sided masses appear in the JSON certificate. The pairs of mass budgets are \`(2407,6041)\`, \`(2732,5038)\`, \`(2571,5397)\`, so each violates at least one 2331 cap. Stable source-order hashes for each completed segment and all per-pattern counts are preserved in the certificate. Original local author checks completed and were internally assertion-checked; the separately published compact replay checker has **not** been rerun after its GitHub publication, nor independently reviewed.

The source-order partition does not alter the frozen T6 carrier. The 2026-11-23 q9 full input preflight counted **1,669,720** order9 rosters (of which 1,513,291 are individually below 2331). We have completed 249,184 of the 1,669,720; the remaining **1,420,536** include vertical lengths 6–9, which are not declared EMPTY here.

## Source and control separation

- Replay code: \`research_checks/T6_P13_Q9_SPLIT0_9_LEN1TO5_REPLAY_20261123.py\`.
- Exact certificate: \`research_checks/T6_P13_Q9_SPLIT0_9_LEN1TO5_AUTHOR_EXACT_CERT_20261123_0804.json\`.
- Prior exact input census: \`research_notes/portable_direct/onhour_20261123_t6_p13_q9_exact_roster_mass_preflight.md\`.
- Native canonical Source frontier separately delegates a p17 q14 split(7,7) preflight to its own lineage. This *portable* p13 derivation does not replace its claim, formal requested benchmark or documented resource gates.
- The current Sites subject does not authenticate the previous bridge Researcher SID; historical author Activity attribution differs. Thus no new Research Activity event, Native CLAIM/RUN, semantic PROGRESS, RR/DR, independent review or Result admission is asserted. Existing Activity328 remains unmodified.

Next scientific action: consume any newer owner/author frontiers; for this p13 order9 split, resume the first unexamined vertical-length6 pattern, using efficient groupwise multiset generation and bounded complete source-order slices. Preserve a partial boundary if a run stops. A true budget-valid modular candidate must undergo low-prime rational-moment completion; never silently discard it. Other p13 q9 splits and remaining lower-prime cases remain open. The mother \`T6=2332\` remains OPEN.
