# T6 one-power maximal-p17 q12 split(6,6): complete canonical q0 and sharp H3 exclusion

Date: 2026-11-22, TASK_RESEARCH, **author-side exact finite computation; UNREVIEWED / NOT_ADMITTED**. Formal Task: `RS-T6-SHAPE-MOMENT-GLOBAL-LOWER-BOUND`. The original Research logical lane is `chatgpt-research-onhour-enterprise-math-20260923`; the previous author's last recorded SID is `MCP-082892eb480e45dea6d4b9fcc0491034`, Researcher `EM-X6-FB6990`. This portable note gives no live CLAIM, RUN, Source semantic PROGRESS or mathematical acceptance.

## Theorem, precisely scoped

Fix the original per-sign exponent mass bound **2331**. Consider cancellation-normalized two-sided multisets of *named* denominator atoms at maximal prime 17, valuation exactly one in the following **frozen canonical cofactor/vertical-order decomposition**:

- Vertical atom \((q,r)\), \(q\ge1, 1\le r\le16\): cofactor \(a=17q+r\), denominator \(d=17a\), exponent \(e=d-1=289q+17r-1\), admitted when \(a\) is 17-smooth. Each side has **vertical order \(\sum q=6\)**.
- The q0 terms are denominators \(17j\) for **\(j=1,\dots,16\)**, full exponent cost \(17j-1\), arbitrary same-side multiplicity.
- Identical denominator/named atoms on opposite signs must cancel; identical same-sign occurrences retain their full multiplicity; quotient overall exchange of the two signs once.
- Required observers are \(H_k(D)=\sum_{d\in D}(1-1/d)^k\), \(k=0,\dots,6\).

**Exact result:** There are precisely **four** unordered support-disjoint signed pairs satisfying \(H_0=H_1=H_2\) on both sides. None satisfies \(H_3\). On these four pairs the minimum *nonzero* \(|H_{3,+}-H_{3,-}|\) is **\(1/647101056\)** and the bound is attained. Thus this exact q12(6,6), one-power maximal-p17 subclass contains **no full six-moment collision** under the frozen budget.

The result is only this subset. It does **not** decide other total orders, split types, higher 17-adic valuations, lower maximal primes, mixed-affine congruence completions or the parent threshold \(T_6=2332\).

## Exhaustiveness and rational-integer proof

For \(q=6\), minimum vertical mass equals \(1766\), leaving at most \(565=2331-1766\) for q0 terms. A nondecreasing index DFS enumerates every admitted vertical multiset of total q-weight 6 (including repeats). A separate integer recursion enumerates all q0 multiplicity vectors over \(j=1,\dots,16\) of mass at most 565. Cartesian combining with the actual per-side 2331 bound enumerates *every* admissible side state exactly once.

Let \(L=99\,891\,792\,000\), an integer multiple of every admitted cofactor \(a\) and q0 index \(j\) used here. Each side is encoded with exact integer signature
\[
\bigg(N,\ \sum L/a,\ \sum (L/a)^2\bigg)
\]
where \(a\) runs over every vertical cofactor **and** every q0 index with multiplicities. Equal signatures are equivalent to equality of \(H_0,H_1,H_2\): \(H_0=N\), and \(H_k\) is binomially triangular in reciprocal powers. The common outer factor 17 has no effect on equality.

The C++17 checker sorts every complete state by this signature, examines **all** equal-signature unordered pairs, and excludes each pair whose two sides share any vertical or q0 named support. Full multiplicity is retained in the integer moments and cost; bit masks are used **only** for opposite-side support exclusion. For the remaining pairs, equality of \(H_3\) is equivalent to equality of the third reciprocal-power sum. All powers are accumulated in unsigned 128-bit integers; the maximum here lies below \(2^{128}\). The additional Python verifier independently reconstructs the four witnesses from the raw row indices and checks \(H_0,H_1,H_2,H_3\) using exact `fractions.Fraction`.

| Exact intermediate | Count |
|---|---:|
| Admissible named vertical atoms for q≤7 | 60 |
| Vertical order-six complete rosters | 11,105 |
| Canonical q0 multisets (j=1..16, cost≤565) | 54,000 |
| Full per-side configurations | **6,992,576** |
| Distinct H012 integer signatures | 6,988,554 |
| Signatures with multiple side configurations | 4,019 |
| Unordered same-signature pairs before support cancellation | 4,025 |
| Pairs after opposite-side named support cancellation | **4** |
| Those also equal in H3 | **0** |

## All four H012 aliases, exactly checked

Cofactors are shown separately from actual denominators (multiply every entry by 17). q0 entries use the same cofactor convention.

| Pair | A vertical / q0 | B vertical / q0 | A/B mass | Exact \(H_{3,A}-H_{3,B}\) |
|---|---|---|---:|---:|
| 1 | (21,42,56) / none | (24,28,84) / none | 2020 / 2309 | \(-1/647101056\) |
| 2 | (35,70) / (12,12) | (20,21,84) / (10) | 2189 / 2291 | \(1/96294800\) |
| 3 | (18,36,63) / (8,9) | (21,21,72) / (7,12) | 2273 / 2256 | \(1019/26207592768\) |
| 4 | (24,24,36,36) / (4,4,6) | (18,18,72) / (3,8,9,9) | 2271 / 2322 | \(11/8989056\) |

Every line separately satisfies both budgets, preserves same-side repeats and has no common named cofactor on opposite sides within its vertical/q0 types. All H0-H2 equalities and the displayed unequal H3 differences were recalculated as exact fractions.

## Scope correction from the frozen source

The original [frozen p17/q4 schema](https://github.com/awdawmip/enterprise-math/blob/main/research_artifacts/T6_P17_TOTAL_ORDER4_LITERAL_20261012/Q4_FROZEN_COMPLETE_DFS_SCHEMA_SPECIFICATION.json) gives **`q0_weight_j: 17*j-1 for j=1..16`**. This q12 certificate therefore uses j=1..16. The prior q13(6,7) author-side calculation expanded its so-called q0 catalog to j=33; for j≥18 those denominators duplicate the \((q\ge1,r)\) cofactor domain and are not part of this frozen canonical q0 alphabet. Its no-H013 conclusion can still imply exclusion of the narrower original j=1..16 subcase, because the broader scan contains that subcase, but the larger-side counts should be labeled **relaxation counts** and must not be promoted as canonical q0 counts without a frozen-plan reconciliation. This is a scope/provenance audit observation, **not** an independent Result review or a mathematical-axiom change.

## Reproduction and committed evidence

1. Compile and execute `g++ -O3 -std=c++17 research_checks/T6_P17_Q12_SPLIT6_6_H013_CANONICAL_CHECK_20261122.cpp -o /tmp/t6q12 && /tmp/t6q12 > /tmp/q12_raw.json`.
2. Run `python research_checks/T6_P17_Q12_SPLIT6_6_H012_WITNESS_VERIFY_20261122.py /tmp/q12_raw.json`.
3. Compare the exact integer totals and all four rational witnesses with the saved raw output and certificate.

- C++ source: [exact scanner](../../research_checks/T6_P17_Q12_SPLIT6_6_H013_CANONICAL_CHECK_20261122.cpp).
- Raw output: [indices and exact scan totals](../../research_checks/T6_P17_Q12_SPLIT6_6_H013_RAW_OUTPUT_20261122.json).
- Rational verifier: [independent witness checker](../../research_checks/T6_P17_Q12_SPLIT6_6_H012_WITNESS_VERIFY_20261122.py).
- Full certificate: [four witnesses and sharp gap](../../research_checks/T6_P17_Q12_SPLIT6_6_H013_EXACT_CERT_20261122.json).

A C++17 run on the local calculation host examined 6,992,576 side states in 2.12 seconds, with observed peak RSS about 444,304 KiB. The independently written rational witness reconstruction passed for all four. The mathematical completeness of the general model is still subject to nonauthor source-plan review; no affine/native experiment is represented as executed.

## Remaining mother objective and control

The formal parent objective remains **OPEN**. Next scientific direction: verify the original frozen higher-order plan/split mapping and select the next unsolved p17 one-power vertical split or higher-valuation class under the actual canonical routing; in particular do not generalize q12 or q13 to all p17. T6 execution requires a current Source owner/readback, typed continuation with real predecessor CAS and an authentic winning Research CLAIM/RUN. Previous original typed-prepare failures due to metadata budget and GitHub limit are preserved and not replayed. Separate X6 triad action and C24/C3 sensor deficits remain unresolved.

Author scientific state: **AUTHOR_EXACT_FINITE_EXECUTED / UNREVIEWED / NOT_ADMITTED**. Source science publication and Activity association are distinct from protected semantic PROGRESS, review, acceptance and Foundation.
