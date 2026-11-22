# T6: exact globally necessary mixed-digit exclusion of maximal-p19 vertical order 9; author completion of the p19 boundary

Date: **2026-11-23 (Asia/Hong_Kong)**. Role TASK_RESEARCH, Researcher \`EM-X6-FB6990\`, native SID \`MCP-082892eb480e45dea6d4b9fcc0491034\`. Task \`RS-T6-SHAPE-MOMENT-GLOBAL-LOWER-BOUND\`. **Evidence strength:** AUTHOR_EXACT_FINITE_EXECUTED / GITHUB_VERIFIED / UNREVIEWED / NOT_ADMITTED. Native semantic PROGRESS and formal Result are distinct and remain unpublished.

## Proposition: no cancellation-normalized maximal-prime-19 order-nine full collision below 2332

Let \(A,B\) be two distinct cancellation-normalized positive-exponent multisets, each with total exponent mass at most 2331, and identical \(H_0,\ldots,H_6\). If the largest prime occurring in their denominators \(e+1\) is 19, then their maximal-p19 valuation-one vertical total order cannot be 9.

This is proved **for full original H0–H6 observer equalities with arbitrary 19-free denominator components**, not by requiring equality of the isolated p19 component's rational moments.

### Why the modular conditions are genuinely necessary

The triangular \(H_k\)-to-\(S_k\) binomial transformation gives exact reciprocal-power equality for \(S_k=\sum (e+1)^{-k}\), \(k=1,\ldots,6\). The independent six-equation mod19 Vandermonde theorem, \`onhour_20261123_t6_p19_v19_squared_mod19_universal_cancellation.md\`, eliminates noncancelling p19² denominators \(361q\), \(1\le q\le6\), under the 2331 budget.

After that cancellation, each denominator divisible by19 is \(19c\), \(19\nmid c\). Multiplying the exact equality in \(S_k\) by \(19^k\), denominators prime to19 contribute terms divisible by \(19^k\). Therefore the following congruences hold for the signed multiplicities \(m_c\) of p19-cofactors:

\[
\sum m_c c^{-1}\equiv0\ (\bmod 19),\quad
\sum m_c c^{-2}\equiv0\ (\bmod 361),\quad
\sum m_c c^{-k}\equiv0\ (\bmod 6859),\ 3\le k\le6.
\]

These six **necessary, not sufficient** conditions preserve the genuine mixed-digit information from the full original shape-moment problem while retaining the missing lower-prime-completion obligation for any survivors.

All cofactor atoms are smooth over primes ≤19, and given the side budget \(e=19c-1\le2331\), \(c\le122\). Enumerate \(c=j\), \(1\le j\le18\) (q0) or \(c=19q+r\), \(1\le q\le6,1\le r\le18\) (vertical), filtered for maximal prime ≤19 and by exact mass. The 64 possible vertical atom types preserve exact denominator, signed support and multiplicity.

Because a side's vertical order cannot exceed6 under this mass cap, the only order-nine splits up to a global sign are \((3,6)\) and \((4,5)\). All multisets on either side are generated exhaustively and joined on the six congruences. The signature uses mixed radix \((19,361,6859,6859,6859,6859)\) with overall modulus \(19^{15}=15181127029874798299<2^{64}\). Each coordinate is reduced separately, avoiding carry-based false matches. All equal-signature pairs then undergo exact opposite-side named support testing.

| Order-nine split | Vertical rosters A/B | Complete side configurations A/B | Equal six mixed-digit signatures | Support-disjoint pairs |
|---|---:|---:|---:|---:|
| (3,6) | 751 / 114 | 569,718,902 / 675 | **0** | **0** |
| (4,5) | 3,484 / 3,378 | 43,043,867 / 852,346 | **0** | **0** |

Thus no order-nine candidate satisfies even these necessary conditions, establishing the proposition for the complete p19 maximal-prime candidate family at vertical order nine.

**Execution:** exact C++17, \`g++ -std=c++17 -O3\`, enabled assertions; (3,6) took 12.68 s and peak RSS 395,004 KiB; (4,5) 11.31 s and 91,704 KiB. Source file SHA256 \`774bffe10621db7a83bf765d5f1fc96e09ff40e5d2abedaf8a720b6e058ad36d\`. Numeric results were extracted from the executed source, with no float equality test. This is an author finite exhaustive proof, pending independent verification of the enumerator and pin mapping.

## Consequence for the entire maximal p19 layer

The same mixed-digit method also exhaustively excludes vertical orders 10,11,12: splits (4,6),(5,5),(5,6),(6,6) have zero **support-disjoint** equal-signature pairs. For equal splits the only equal-signature pairs were identical configurations and are cancelled; for unequal splits there were none. See the separately verified \`onhour_20261123_t6_p19_q10q12_mixed_digit_exact_exclusion.md\`.

The frozen canonical taskbook states that maximal p19 vertical orders 0–8 have already been excluded by prior accepted evidence. Side mass ≤2331 permits no vertical order greater than12. Combining that *previously verified task input* with the new author calculations of 9–12, and the p19² cancellation proof, yields the **author-side full maximal-prime-19 exclusion** for mass ≤2331 under the frozen task interpretation. It preserves all previous author/reviewer provenance; this note itself has not been independently reviewed or formally admitted.

This is significant progress toward \(T_6=2332\), but that mother question remains **OPEN** because the maximal-prime layers 17,13,11 and the other small-prime components have not all been excluded. In particular, do not claim a global T6 theorem from a maximal p19 layer.

## Next exact research unit

Starting from the original frozen p17 maximal-prime task inputs, reconcile existing p17 q12–14 finite author notes with their Source pin/review strength, then derive the *proper full-shape necessary p17-adic mixed-digit congruences* for the first genuinely unfinished p17 vertical order. Avoid demanding isolated p17 components have equal rational moments when p17-free denominators can compensate. Preserve true per-side budget2331, named factors, signs, multiplicities and q0; if an exact candidate survives, perform p17-free completion rather than discarding it.

### Durable sources

- \`research_checks/T6_P19_Q9_MIXED_THIRD_DIGIT_CHECK_20261123.cpp\` — actual exhaustive executable.
- \`research_checks/T6_P19_Q9_MIXED_THIRD_DIGIT_CERT_20261123.json\` — exact two-split counts, run profile and SHA.
- \`research_notes/portable_direct/onhour_20261123_t6_p19_v19_squared_mod19_universal_cancellation.md\` — p19² cancellation theorem.
- \`research_notes/portable_direct/onhour_20261123_t6_p19_q10q12_mixed_digit_exact_exclusion.md\` — remainder 10–12.
- \`research_tasks/T6_SHAPE_MOMENT_GLOBAL_LOWER_BOUND_20260909.md\` — exact original task freeze and p19 orders0–8 prior closed boundary.

**Control separation:** Current original continuation read \`onhour-20261123-0008-own-t6-cont-read-v1\` awaits its terminal readback. Last original Task read was SUCCEEDED as of 2026-11-22T14:17:14Z, owner unassigned. No current winning own T6 CLAIM, RUN or protected Native semantic PROGRESS has been established. Do not reissue rejected or pending requests; never use the maintenance lane for Research identity.
