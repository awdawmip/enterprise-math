# EC49FQL — Exact full-prior bifurcations at named-root:terminal price 2:1

Date: 2026-11-16. Classification: AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED. Scientific input remains frozen at \`fc0f038e7bfd12c886b4d37f900bfb770c0f61ab\`. Research lineage: EC49FQI (#2539) → EC49FQJ (#2542) → EC49FQK (#2545). Research topic \`RS-EC49AS\` remains unpublished as a canonical Task as of Source \`bae50d8a34ca9bea2d8095d777b7a2be0a159014\` (read 2026-11-16T01:36:03.517526Z), so this is independent portable research, not a CLAIM/Result.

## Problem and exact theorem

Fix the original native BRC class selected by configuration 16943: 310 original configurations, 141 distinct complete named-root profiles with multiplicities \`m_i>0\`, 144 full-terminal scalar observations \`q=0,...,143\` and 84 named-root scalar observations \`q=144,...,227\`. The objective is to identify the full profile, including root distinctions which all terminal observations may miss. At each internal node, a physical observation must strictly split the remaining profiles. Any finite adaptive correct decision tree is allowed. A terminal observation costs \`t>0\`; a named-root observation costs \`r=2t\`.

For all **real** \`0≤λ≤1\`, use the full-profile prior

\`p_λ(i)=(1−λ)/141+λ m_i/310\`.

Let

\`γ=310/7219\` and \`β=620/3299\` (\`0<γ<β<1\`).

**Theorem.** The complete unrestricted minimum expected identification cost at price ratio \`r/t=2\` is

\`\`\`text
V(λ;2t,t)/t =
  (1−λ)*302/141 + λ*763/310, 0 ≤ λ ≤ γ;
  (1−λ)*303/141 + λ*714/310, γ ≤ λ ≤ β;
  (1−λ)*305/141 + λ*695/310, β ≤ λ ≤ 1.
\`\`\`

The set of **all** physically indexed globally optimal first observations, with the original \`q\` indexing preserved, is:

| Prior interval | All optimal physical first actions |
| --- | --- |
| \`0≤λ<γ\` | \`{32,34}\` |
| \`λ=γ\` | \`{32,34,140,142}\` |
| \`γ<λ<β\` | \`{140,142}\` |
| \`λ=β\` | \`{16,23,140,142}\` |
| \`β<λ≤1\` | \`{16,23}\` |

All these first actions are terminal observations (\`q<144\`); descendant decisions can use any of the 228 native observations.

This is a new **full \`λ∈[0,1]\` slice at the non-equal price ratio 2**, not an extrapolation of the old \`r=t\` prior interpolation.

## Proof: exact global Bellman at four anchors

For a nonempty subset \`S\` of profiles, write \`W(S)=Σ_{i∈S} w_i\` with exact integer weights at \`λ=a/b\`:

\`w_i=310(b−a)+141 a m_i\`, so \`W(all)=141·310·b\`.

The cost \`C(S)\` satisfies the exhaustive Bellman equation

\`C(S)=min_{q splits S}{c_q W(S)+Σ_z C(S∩q^{−1}(z))}\`, \`C({i})=0\`,

where \`c_q=1\` for \`q<144\` and \`c_q=2\` for \`q≥144\`. Every legal query decreases the surviving set cardinality, so the recurrence is exhaustive over unrestricted finite-depth correct trees. The 228 original physical queries induce 209 distinct response partitions. Partition representatives are sufficient for the Bellman optimum, while all 228 original actions are explicitly reexamined for the forced-first optimum/ties.

The following integer-rational computations were independently recomputed (state counts are memoized nontrivial Bellman masks in the second implementation):

| \`λ\` | Exact \`V/t\` | All optimal first \`q\` | Bellman states |
| --- | --- | --- | ---: |
| \`0\` | \`302/141\` | \`32,34\` | 6590 |
| \`310/7219\` | \`15561/7219\` | \`32,34,140,142\` | 6869 |
| \`620/3299\` | \`7185/3299\` | \`16,23,140,142\` | 7018 |
| \`1\` | \`695/310=139/62\` | \`16,23\` | 6914 |

The independent calculation reconstructs the same 141 exact native response profiles and verifies the original source SHA-256. Both breakpoint anchors include **full correct witness trees for each listed physical first action**, independently replayed on all 141 profiles with the original 310-config multiplicities. Their exact profile-uniform (\`U\`) and configuration-weighted (\`M\`) cumulative observation counts are:

| q | \`U_R\` | \`U_T\` | \`M_R\` | \`M_T\` |
| --- | ---: | ---: | ---: | ---: |
| \`32,34\` | 6 | 290 | 6 | 751 |
| \`140,142\` | 5 | 293 | 5 | 704 |
| \`16,23\` | 5 | 295 | 5 | 685 |

At \`r/t=2\`, these give the three affine policy cost lines \`A(λ),B(λ),C(λ)\` in the theorem. Direct exact subtraction gives

\`A−B=−(1−λ)/141+49λ/310\`,

\`B−C=−2(1−λ)/141+19λ/310\`.

Their zeros are exactly \`γ=310/7219\` and \`β=620/3299\`. All inequalities and their strict sides follow by rational arithmetic.

For any **fixed** correct finite decision tree \`T\`, its expected cost is affine in \`λ\` at the fixed price 2. On \`[0,γ]\`, the line \`A\` is the cost of a single replayed correct native tree and equals the exhaustive Bellman optimum at both endpoints. For any competing tree, the difference from \`A\` is an affine function nonnegative at both endpoints, hence nonnegative throughout the interval. The same argument using \`B\` on \`[γ,β]\` and \`C\` on \`[β,1]\` proves the entire continuum theorem, with no interpolation of unproved numerical results.

For the **complete physical first-action sets**, necessity follows similarly: an action optimal at an interior point of one affine segment must also be optimal at both segment endpoints (a nonnegative affine difference with an interior zero vanishes identically). Intersections of the independently enumerated endpoint sets give exactly the interior sets in the theorem. Sufficiency follows from individually replayed witnesses for all six relevant physical indices, with the count vectors displayed above, achieving the corresponding affine optimum throughout their claimed interval. At the two boundary parameters, exact forced-first Bellman gives the stated four-way ties.

## Source, verification, and open problem

Frozen input bytes:
- \`frozen_original_master.txt\` SHA-256 \`cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e\`.
- \`EC49FPG_PROFILE.csv\` SHA-256 \`a61a3ee4d2f13f9d216f52cd3529c72d395c1250bfb1d7ae96a1adf5a6837c1f\`.
- Frozen science commit: \`fc0f038e7bfd12c886b4d37f900bfb770c0f61ab\`. Original source and independent reconstructors retained in the EC49FQK/EC49FQL portable packages. The full GitHub code and compact endpoint witness-index record accompany this report.

The new endpoint certificate SHA-256 digests are:
- \`λ=0\`: \`a934acf73cac9d83bfebf9f40323af1052010e08ba2894380bcb7577378f0a72\`.
- \`λ=310/7219\`, four-way tie with all first trees: \`ffc3bde64e09a6eba818b743b8d714c9dbb6c6b0cac2ec02883119e8becbc1c2\`.
- \`λ=620/3299\`, four-way tie with all first trees: \`cd2ed2b34dab8933d327e86505ff9dd30c7e7603446fe4c7f0b76125b9388526\`.
- \`λ=1\`: \`b3a01fc576d45c19b36543bb388b1ae46083f1d9e2a6e2ceef2467b663d9290d\`.

An independent implementation recomputed all four Bellman optima, all 228 physical forced-first actions, and replayed eight physical optimal-first trees at the two breakpoints, returning \`EC49FQL_ALL_PRIOR_AT_PRICE_2_FULL_PHASES_PASS\`. No floating point is used in a proof step.

**Open frontier.** Determine the exact adjoining two-parameter phase boundary in the \`(λ,x=r/t)\` half-strip \`1<x<3\` between the \`q32/q34\` and \`q140/q142\` first-action phases. The explicit policy competition curve \`λ=310(3−x)/(7557−169x)\` (obtained from the old q32 and q140 witness trees) is a candidate boundary; its global sharpness for intermediate \`x\` is **unresolved**. The new result proves sharpness on the entire slice \`x=2\`. Preserve the previously certified \`x=1\` and high-price \`x≥3\` results.

Status: author proof and independent exact finite computation completed; not independently mathematically reviewed/admitted. No P000, physics, formal Task/CLAIM/Result or Source Activity assertion is introduced.