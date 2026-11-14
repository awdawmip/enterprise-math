# EC49FAL — exact 94-edge optimum for four H6-rooted nine-window BRC families

**Date:** 2026-11-04. **Classification:** AUTHOR_ANALYTIC_FINITE_THEOREM / EXACT_SIGNED_X6_CENSUS_PASS / PORTABLE_DRAFT / UNREVIEWED / NOT_ADMITTED.

## Source, mother question and frozen inputs

Continue **EC49FAK** at immutable author commit `a0ea2b18bd38420054b1c52547feffa633104321`. Frozen scientific parent `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Applicable behavioral policies are read from their current authoritative branches separately. P000 and ACTIVE worldview remain unchanged.

The mother question is the least number of **distinct nonempty ordered signed native X6 primitive-step prefixes** needed for horizons H2–H9, exactly five complete six-coordinate positive BRC cache keys, at most six nine-history observation signatures, one key per horizon, and rank nine over Q of every horizon's nine-history transfer observation matrix. The seven-letter native operations, observation DFA, and signed primitive prefixes are exactly those in the parent EC49FAK verifier; no model or observer substitution occurs.

For each source rank 1512, 1513, 2200 and 2203, fix **every H2–H7 selected word** as in EC49FAB/EC49FAK. This fixes 72 native prefix edges, four complete cache keys, and six observation signatures. Now allow **every** admissible H8 and H9 word that starts with either of the **two H6 words**, not merely the two H7 words. Thus H8 has an arbitrary zero-net *two-letter* suffix and H9 an arbitrary zero-net *three-letter* suffix; their later paths may diverge before H7. They must still satisfy the full displacement, key, signature and rank constraints.

## Theorem

For **each of the four fixed H2–H7 schedules**, the complete H6-rooted suffix family has exact optimum

\[
\boxed{E^*_{H6\text{-rooted}}=94}.
\]

In particular no 93-edge solution exists within these four H6-rooted families. The wider H9/M5/S<=6 mother problem retains the previously reported author-side bounds \(80\le E^*_{H9}\le94\).

## Proof: complete input reduction

1. Expand the native operations into signed primitive X6 directions and check zero net displacement in **all six** coordinates. There are exactly **18** zero-net suffixes of operation-length 2 and **88** of length 3. The checker enumerates all \(7^2\) and \(7^3\) operation tuples; there is no preselected subset of suffix syntax.
2. A source H2–H7 schedule already uses six distinct observation signatures. Hence every allowed H8/H9 word must use one of these six. Filter by the actual nine-history DFA and full positive BRC key. Exhaustion yields **no** eligible H8 word at any of the four old cache keys. Therefore H8 must introduce the fifth key and H9 must use that same fifth key. In each case exactly **three** keys occur in both eligible H8 and eligible H9 pools.
3. The rank-nine test is **exact over Q**: a rank-nine \(9\times 5t\) binary matrix has a nonzero \(9\times9\) integer minor. By Hadamard every such minor has absolute determinant at most \(3^9=19683<1000003\). Therefore full rank modulo the prime \(1000003\) is **equivalent** to full rational rank; neither an approximate rank test nor a one-sided false rejection is involved.
4. For each common fifth key \(K\), exhaust all nonempty H8 subsets (at most \(2^8-1\)), retain those of rank nine, and compute the exact minimum extra native prefixes \(\Delta_8\) over the fixed 72-edge base. For the two keys having six eligible H9 words, also exhaust **all** nonempty H9 subsets (at most 63), retain rank-nine subsets, and compute the least additional prefixes \(\Delta_9^{\mathrm{all}}\) relative to the union of the base with **every** eligible H8 prefix. This gives H9 an *optimistically enlarged* set of reusable prefixes. For any actual H8 subset \(A\), its preexisting prefixes are contained in that enlarged union, so

\[
 E\ge72+\Delta_8+\Delta_9^{\mathrm{all}}.
\]

   The third common key has \(\Delta_8=30\), so the lower bound \(72+30=102\) suffices without enumerating its 24-word H9 subset lattice.

## Exact finite certificates

| Source ranks | Shared fifth key \((x,y,z)\) | H8/H9 eligible words | Rank-nine H8 subsets | Minimum \(\Delta_8\) | Rank-nine H9 subsets | Optimistic \(\Delta_9^{\mathrm{all}}\) | Certified lower bound |
|---|---|---:|---:|---:|---:|---:|---:|
| 1512, 2200 | (5,5,1) | 8 / 6 | 81 | 16 | 49 | 6 | **94** |
| 1512, 2200 | (6,4,1) | 8 / 6 | 81 | 20 | 49 | 6 | **98** |
| 1512, 2200 | (6,5,1) | 4 / 24 | 1 | 30 | Not needed | Not needed | **102** |
| 1513, 2203 | (7,3,1) | 8 / 6 | 81 | 16 | 49 | 6 | **94** |
| 1513, 2203 | (6,4,1) | 8 / 6 | 81 | 20 | 49 | 6 | **98** |
| 1513, 2203 | (7,4,1) | 4 / 24 | 1 | 30 | Not needed | Not needed | **102** |

These are **lower bounds per fifth-key class**, not claims that the 98/102 cases possess matching constructions. For every source rank, the minimum of the three bounds is 94. The known EC49FAJ/EC49FAK **94-edge** explicit construction is contained in the H6-rooted family, completing the equality.

## Reproduce and evidence scope

Execute `node VERIFY_EC49FAL.js > EXACT_REPORT_EC49FAL.json` with Node v22 or another BigInt-capable JavaScript runtime. `VERIFY_EC49FAL.js` embeds the unchanged actual EC49FAK signed-X6 and observation checker, followed by the new exhaustive H6-rooted routine. The JSON file in this directory is the actual V8 execution result of the new routine. A separate Python exact-native-prefix implementation was run in the local author workspace and reproduced every \(\Delta_8\), \(\Delta_9^{\mathrm{all}}\) and class lower bound; the durable standalone JS and its generated output are sufficient for reproduction.

**Extension over EC49FAK:** H8/H9 can now change the **last H7 operation** and its continuation, because they are independently rooted at H6. The next discriminating search must allow at least one H8/H9 word to branch **before** H6, or revise H2–H7, to seek a 93-edge construction under the original global model. This necessary condition refers to the four fixed early schedules only.

**Status:** Author-side exact finite theorem, not a canonical Source CLAIM/Result, independent Driver mathematical acceptance, or a theorem about unrestricted nine-window schedules. No protected axiom or freezing pin is changed.
