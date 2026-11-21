# X6 R96 — The exact T=11 cross-section: full Port-sensitive tie atlas for every S≥1

Date: 2026-11-22 (Asia/Shanghai).
Status: SYMBOLIC_AUTHOR_PROOF / EXACT_FRACTION_AUTHOR_CHECK_PASS / NOT_INDEPENDENTLY_REVIEWED.
Research scope: the conditional positive-count fourth-order BRC star-moment histogram observer with unknown common additive offset. This is not a complete native X6 Cell/Link/triadic-force/time observer. Frozen scientific input: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json. Applicable current P000/worldview/joint-preservation and research protocols were read separately; no alteration to the frozen input. Science antecedents: R90–R95, particularly research_notes/portable_direct/2026-11-22_x6_r95_midT_vertical_strip_and_sharp_endpoint.md.

## Exact model

For a nonzero a=(x,y,z) in Z³ identify a and −a (unoriented direction). Set

\[
q(a)=\max\{\sum_i\max(a_i,0),\,\sum_i\max(-a_i,0)\},
\quad u=x+3y+6z,\quad v=3x+12y+30z,\quad h=7x+39y+126z.
\]

For weights w=(1,1,S,11), S≥1 real, define

\[
F(a;S)=\max\left\{\frac{|u|}{2},\frac{|v|}{S+1},\frac{|h|}{12},
\frac{|v-u|}{S+1},\frac{|h-u|}{12},\frac{|h-v|}{S+11}\right\},
\qquad \eta^*(p;S,11)=\min_{\substack{a\ne0\\q(a)\le p}} F(a;S).
\]

## Theorem 1 — exact optimum for all S≥1 and integer p≥11

\[
\boxed{\eta^*(p;S,11)=
\begin{cases}
\frac12,& p\le26\text{ or }S\le11,\\
\frac6{S+1},&p\ge27\text{ and }S>11.
\end{cases}}
\]

In the second case, c=(24,−14,3) is the unique optimal unoriented integer difference over the entire unbounded lattice.

## Theorem 2 — exact complete tie atlas

The table specifies all seven possible directions. The S-threshold is inclusive, and q is the minimum Port budget.

| Unoriented direction | q | S-threshold for F=1/2 | (u,v,h) |
|---|---:|---:|---|
| a1=(10,−5,1) | 11 | 1 | (1,0,1) |
| a2=(5,−4,1) | 6 | 5 | (−1,−3,5) |
| a3=(9,−5,1) | 10 | 5 | (0,−3,−6) |
| a4=(15,−9,2) | 17 | 7 | (0,−3,6) |
| a5=(19,−10,2) | 21 | 7 | (1,−3,−5) |
| a6=(14,−9,2) | 16 | 11 | (−1,−6,−1) |
| a7=(24,−14,3) | 27 | 11 | (0,−6,0) |

Whenever S≤11 or p≤26, the complete set of minimizers is exactly {ai: q(ai)≤p and S≥S-threshold(ai)}. Whenever S>11 and p≥27, the complete set is {a7}.

At p≥27 the minimizer counts are respectively 1 for 1≤S<5, 3 for 5≤S<7, 5 for 7≤S<11, 7 at S=11, and 1 for S>11. The two new ties enter simultaneously at S=7. For p=17 the counts are 1,3,4,5 on 1≤S<5, 5≤S<7, 7≤S<11, S≥11.

## Proof, no infinite enumeration

Integer identities:

\[
v\in3\mathbb Z,\quad h-u=6(x+6y+20z)\in6\mathbb Z,\quad
h-u-6v=-12(x+3y+5z).
\]

Thus h−u ≡ 6v (mod 12). The exact inverse moment map is

\[
(x,y,z)=\left(\frac{h+19u}{2}-4v,\ \frac{-h-14u+7v}{3},\
\frac{h+11u}{12}-\frac v2\right).
\]

**Strict-improvement lemma.** The feasible s=(10,−5,1), q=11, has F(s;S)=1/2 for every S≥1. If F(a;S)<1/2, the first gap makes u=0, the third gives |h|<6, and the fifth gives |h−u|<6. Since h−u is divisible by six, h=0. The inverse map and v∈3Z force v=6k and a=−k(24,−14,3), k a nonzero integer. Such a has q=27|k| and F=6|k|/(S+1). Thus no strict improvement exists if p≤26 or S≤11. If S>11 and p≥27, a7 is feasible with F=6/(S+1)<1/2; any competitor with F≤F(a7) must be on this line and |k|=1 is uniquely optimal. This proves Theorem 1 and the unique-optimum case of Theorem 2.

**Case S≤11.** At fixed a, F(a;S) is nonincreasing in S (only denominators S+1 and S+11 vary). Hence F(a;S)≤1/2 implies F(a;11)≤1/2. At S=11 the six inequalities give

\[
|u|\le1,\quad |h|\le6,\quad |h-u|\le6,\quad
|v|\le6,\quad|v-u|\le6,\quad|h-v|\le11.
\]

Modulo orientation, the integer/divisibility constraints leave only (u,h)=(0,0),(1,1),(0,6),(1,−5). If h=u, v is a multiple of 6; otherwise v≡3 (mod 6). The remaining inequalities force respectively: (0,0) has v=±6 (v=0 gives the excluded zero vector); (1,1) has v=0 or 6; (0,6) has v=±3; (1,−5) has v=±3. The inverse map gives exactly a1,...,a7. Direct substitution of all six gaps in F≤1/2 gives the listed S thresholds. Applying q≤p proves the exact atlas when S≤11.

**Case S>11 and p≤26.** Even at arbitrary large S, F≤1/2 still forces |u|≤1, |h|≤6, |h−u|≤6, and therefore the same four (u,h) classes up to sign. Put v=6k if h=u; otherwise put v=6k+3. The inverse map gives first coordinate x equal, respectively, to −24k, 10−24k, −9−24k, −5−24k in classes (0,0),(1,1),(0,6),(1,−5). Because q≥|x| and q≤26, the allowed k are: first class ±1 (whose actual q is 27, so excluded), second class 0,1, third 0,−1, fourth 0,−1. These are precisely a1,...,a6, with no further candidates even if S tends to infinity. Comparing their F values gives the same S thresholds. This completes Theorem 2.

## Author-side exact reproducibility

The companion Python script x6_r96_t11_wall_verify.py uses fractions.Fraction to enumerate all 110,740 unoriented differences with q≤40. At nine rational S values and nine Port budgets, it performs 2,093,292 in-budget exact comparisons across 81 cases and checks both the predicted exact optimum and the complete tie set. All assertions passed locally; x6_r96_t11_wall_results.json records the finite verification coverage. The unbounded conclusion rests on the integer/congruence proof above. No independent scientific review was performed.

The histogram observer is conditional. Native P000 requires preservation of six-dimensional Cell and signed displacement, Link/path provenance, triadic-force events and separately typed time for any declared future-operation reduction. No native observer-fiber conservation certificate or physical evolution claim is inferred from this conditional BRC result.

## Research continuation

The exact T=11 cross-section is now closed for S≥1 and p≥11, including all ties. Next independent mathematical target: T>11 chambers and the first new h−u=±6 strata, with Port-sensitive boundaries. Formal Task RS-X6-NATIVE-TIME-DYNAMICS ownership/CLAIM/Result/Review remain separate from portable GitHub scientific publication.