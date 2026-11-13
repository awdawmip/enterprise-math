# Frozen R5: exact domination-number distribution for all 2^28 gap closures

Date: 2026-11-14. Status: **author-side exact finite result, not independently reviewed**.
Science frozen at `awdawmip/enterprise-math@435e77af0d180eac32bd1f9c4c464bc4010b7551`.
Source methodology extended from immutable precursor `b0f90a317145c7f031dfa2157126ab34cae84259`, especially `research_notes/brc_r5_multicut_domination_20261114/RESEARCH.md` and its exact verifier. This is an auxiliary integer-boundary sampling observer, not a native X6 equivalence or the 2,520-byte certificate/8,192-query performance experiment.

## Proposition 1 (exact partition-weight polynomial)

Let `B_0,...,B_{B-1}` be consecutive blocks of strictly increasing integer event coordinates separated by **exact gaps R+1** and let each of the `B-1` gaps be either unchanged or shortened by one. A closed cut joins the two neighboring blocks across gap R. For every interval of block indices `[a,b]` let `d(a,b)` be the exact minimum number of radius-R centers, chosen among the event coordinates, covering the merged consecutive blocks after closing all cuts a,...,b-1.

Define a polynomial with nonnegative integer coefficients:

`H(0,0;z)=1`, other inadmissible states zero; for `1<=s<=i<=B`,

`H(i,s;z)=sum_{j=s-1}^{i-1} H(j,s-1;z) z^{d(j,i-1)}`.

Then, for `q=0,...,B-1`:

`[z^k] H(B,B-q;z) = #{C subset {0,...,B-2}: |C|=q, D_R(X_C)=k}`.

The full census has generating polynomial `T(z)=sum_{s=1}^B H(B,s;z)`. Every monomial counts its closure subset exactly once.

**Proof.** The chosen subset of closed cuts uniquely partitions the ordered blocks into maximal merged intervals; an unchanged gap of R+1 prevents any radius-R center from covering points on both sides. Consequently the exact minimal covering-cardinality is the sum of interval costs. Remove the last merged interval `[j,i-1]` of any partition of the first i blocks into s intervals. Its contribution is `d(j,i-1)`, and the remaining partition is uniquely counted by `H(j,s-1;z)`. Summing j enumerates each closure subset once. Taking coefficients and setting s=B-q proves the identity.

This recurrence computes every multiplicity with 435 interval costs for B=29, without enumerating all 268,435,456 closure subsets.

## Proposition 2 (monotone closure coupling)

Under the same integer-coordinate setting, if `C subset C'`, the translated coordinates retain their strict order and every pairwise separation is unchanged or decreases. Holding the indices of any original feasible centers fixed, same-side distances are unchanged and cross-cut distances decrease. Thus the original centers remain feasible and

`D_R(X_{C'}) <= D_R(X_C)`.

In particular, for independent Bernoulli-p closures, `D_R(X_C)` is stochastically nonincreasing as p rises (couple all cuts using common uniforms). Exact probabilities at arbitrary rational p are obtained by

`Pr_p(D_R=k)=sum_{q=0}^{B-1} [z^k]H(B,B-q;z) p^q(1-p)^{B-1-q}`.

## Exact frozen R5 census

The original 15 atoms yield 953 rational activation thresholds, 954 boundary points and 1,065 events. There are 28 gap cuts and B=29. For each arbitrary closure subset, the optimal radius-2 center count is one of 207 through 213:

| Minimum centers | Exact number of closure subsets |
|---:|---:|
| 207 | 229,376 |
| 208 | 5,111,808 |
| 209 | 36,151,296 |
| 210 | 93,896,704 |
| 211 | 93,421,568 |
| 212 | 35,209,216 |
| 213 | 4,415,488 |
| **Total** | **268,435,456** |

For independent fair closure of each of the 28 gaps, the exact random minimum center count D has

`E[D] = 13471/64 = 210.484375`;
`Var(D) = 4115/4096 = 1.004638671875`.

The complete conditional distributions for every exact number q of closed gaps (29 rows, all 7 possible center counts) are in `EXACT_OUTPUT.json`. As a check, q=11 yields exactly two patterns with 207 centers and 782,145 patterns with 213 centers, agreeing with the predecessor extrema/count study.

## Reproducibility and evidence scope

- The supplied self-contained `VERIFY_R5_DISTRIBUTION.py` rebuilds all 15-atom rational events, creates 435 exact interval costs, computes every polynomial coefficient by integer DP, and asserts the exact count and moments.
- Full, direct closure enumeration was executed locally for all subsets with q<=4, i.e. 24,158 distinct full-scale patterns; each direct greedy minimum matched the polynomial coefficient.
- An independent complete check of the polynomial against explicit pattern enumeration covered 360 small block configurations (2 to 5 blocks, each 1 to 3 integer coordinates), under the same gap semantics.
- The distribution/moments were also recomputed in an independently written JavaScript integer/rational-key implementation at GitHub publication time, matching all seven frequencies and both rational moments.
- The author executed the equivalent standalone Python verifier and obtained `PASS_EXACT_R5_ALL_PATTERN_DISTRIBUTION`. Independent mathematical review and an exact-byte rerun of the published GitHub script remain separate.

## Next scientific direction

Compute the full **fixed-K total nearest-center correction cost frontier** over arbitrary multi-cut patterns, rather than only their minimum feasible center counts. Determine whether a compact transfer state can retain both q and K while allowing reconstruction of optimal center configurations, with event provenance and the original 28-coordinate certificate query semantics preserved for future integration. The underlying Heartbeat World/P000 scientific premises and frozen input remain unchanged.
