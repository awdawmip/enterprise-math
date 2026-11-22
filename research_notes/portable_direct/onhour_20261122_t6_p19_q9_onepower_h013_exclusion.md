# T6 p19 vertical order 9: valuation-one full-q0 exact H3 exclusion (author-side)

**Date:** 2026-11-22; **Task:** `RS-T6-SHAPE-MOMENT-GLOBAL-LOWER-BOUND`; **lane:** `chatgpt-research-onhour-enterprise-math-20260923`; **status:** `AUTHOR_EXACT_FINITE_EXECUTED / UNREVIEWED / NOT_ADMITTED`.

## Exact limited theorem

In the maximal-prime-19 *valuation-one* denominator carrier, let a vertical atom be `a=19q+r`, `q>=1, 1<=r<=18`, with cofactor `a` having no prime factor above 19. Its denominator is `d=19a`, mass `d-1`. The distinct q0 atoms have denominators `19j` for `1<=j<=18`, also with full mass and arbitrary same-side multiplicity. Keep separate budgets of **2331** per sign; cancel opposite identical named atoms; count each remaining occurrence. Let the vertical q-sums be `(3,6)` or `(4,5)`, the two partitions of total order nine under the stated frozen predecessor decomposition.

**Exact finite conclusion:** Eight unordered, support-disjoint two-sided configurations pass `H_0=H_1=H_2`: two for (3,6) and six for (4,5). Every one has unequal `H_3`. The sharp minimum nonzero absolute difference is

\[
\min |H_{3,+}-H_{3,-}|=\frac{1}{2710237824}.
\]

Consequently, within this fully stated **one-power cofactor/q0** domain, no degree-six moment collision below side-mass 2332 exists. This does **not** establish global maximal-p19 order-nine elimination: higher valuations/inactive/zero-first-digit rescues and mixed-affine completion are outside the present enumeration. Parent `T_6=2332` remains OPEN.

## Complete exact enumeration

For `L=1698160464000` (a common multiple of every enumerated cofactor and j index), a side with cofactor multiset `C` has integer signature
`(N, X_1, X_2) = (|C|, sum(L/c), sum((L/c)^2))`.
Because denominators are `19c`, equality of these three integers is equivalent to equality of `H_0,H_1,H_2`. The exact cubic difference `D_3=X_{3,+}-X_{3,-}` gives `H_{3,+}-H_{3,-}=-D_3/(19^3 L^3)` after the first three moment equalities.

| q-split | Vertical rosters (+ / -) | Full single-side configurations (+ / -) | H01 pairs | H012 pairs before support | H012 support-disjoint | H013 support-disjoint |
|---|---:|---:|---:|---:|---:|---:|
| (3,6) | 751 / 114 | 569718902 / 675 | 4247 | 12 | **2** | **0** |
| (4,5) | 3484 / 3378 | 43043867 / 852346 | 20588569 | 28650 | **6** | **0** |

The q0 generator enumerates all nondecreasing j multisets under the largest possible remaining budget. It generated 9571123 distinct q0 multisets under cost 1212 for (3,6), and 584072 under cost 869 for (4,5). The per-side join applies the actual residual budget for each vertical roster, not the universal cap. Each opposite-side shared vertical or q0 named support is rejected. No floating-point equality is used. All 8 survivors were reconstructed from full denominators and checked independently with `fractions.Fraction` for H0 through H3.

An exact simple surviving H012 witness before H3 is:
`A=(532,532,1064)`, `B=(456,798,798)`, denominators with exponents `d-1`, masses `2125` and `2049`; `H_0,H_1,H_2` agree but `H_{3,A}-H_{3,B}=1/2710237824`. This proves the cubic separation is sharp.

## Evidence, strengths and remaining action

- Complete portable integer census source: `research_checks/T6_P19_Q9_ONEPOWER_H012_JOIN_20261122_2300.cpp`.
- Enumeration totals and eight exact rational witness records: `research_checks/T6_P19_Q9_ONEPOWER_H013_AUTHOR_CERT_20261122_2300.json`.
- Independent reconstruction/Fraction verification is attached to the local execution package; the eight denominators and exact fractions in the JSON certificate permit standalone exact checking.
- No fixed p19 saturated-lattice native experiment, no Source semantic PROGRESS, no nonauthor review, no global Task/Result admission.

**Continuation:** Consume the 8 one-power exact candidates as a precise order-nine filter, then close the remaining p19 valuation layers and original mixed-congruence completion using the actual frozen p19 Source inputs. Retain earlier p19 order 0–8 and p17 q12–q14 Source evidence without rerunning. Preserve prior typed prepare failures and original receipt `onhour-20261122-2205-t6-task-current-read-v1` (SUCCEEDED as of 2026-11-22T14:17:14Z). Current winning T6 CLAIM is not verified. Research identity `EM-X6-FB6990`, SID `MCP-082892eb480e45dea6d4b9fcc0491034`; no maintenance-lane claim.

**Required status boundary:** This portable note is source preservation, not native protected Task PROGRESS or independent mathematical acceptance.
