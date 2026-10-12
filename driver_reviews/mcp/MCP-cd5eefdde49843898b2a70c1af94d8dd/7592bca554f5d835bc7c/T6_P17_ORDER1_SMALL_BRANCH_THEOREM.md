# T6 p17 order1: a small exact branch bound and completion interface

Status: **proved local paper bounds; no affine census, native Result or global T6 theorem**. Root directed this preparation. It reuses the fresh Source-pinned p17 certificate and the previous independent static reconstruction. Source remains `2f257c02d95b9cd630c23284bea2516a1be3f853`; the original 28-output RR and its negative/partial verdict are unchanged.

The proposed refinement is a corollary of standard exact lattice enumeration and the particular budgets. It is not a new global tool family or a novelty claim. `SMALL_BRANCH_BOUND_SECOND_PASS.md` records a second independent paper challenge of ties, path dependence and signed budgets. `p17_order1_branch_bound.py` performs only small exact norm/subset comparisons; it constructs no affine representative and visits no search path.

## 1. Exact signed-budget unit

After the validated valuation guard, the maximal-p17 layer has denominators `17m`, with 17 not dividing m. Write `m=s+17q`, s=1,...,16. A q0 atom has exponent cost `w_s=17s-1`; a vertical atom has cost `289q+w_s` and order q.

At total vertical order1 there is one q=1 atom, up to global sign. Choose it positive, at residue r. Its denominator and cost are

`a_r=17(17+r)`, `v_r=a_r-1=288+17r`.

The complete q0 net coefficient vector u therefore satisfies

`sum_s u_s s^(-k)=-(17+r)^(-k) mod17^k`, k=1,...,6,

and the exact two side constraints

`P(u)=sum_s(17s-1)max(u_s,0) <= C_r=2331-v_r=2043-17r`,

`N(u)=sum_s(17s-1)max(-u_s,0) <=2331`.

Common equal atoms on opposite sides are canceled first, so these net signed masses exactly represent the normalized p17 contribution. Cancellation preserves all seven observers and weakens both budgets. The negative vertical orientation is obtained by global sign reversal; it is not a missing independent case.

Because positive and negative coordinate supports are disjoint,

`||Wu||² <= C_r²+2331² = R_r² <=2026²+2331²=9,538,237`.

This is a necessary sphere relaxation, not a replacement for P(u), N(u). The final integer vector must satisfy both original inequalities independently.

## 2. Farther-choice theorem

Let b_i be any full-rank row basis with exact Gram–Schmidt squared lengths D_i. Write an affine point as `v+sum_i n_i b_i`. Descending from i=n-1, its exact orthogonal coordinate is

`n_i+c_i`, where `c_i=h_i+sum_(j>i)n_j μ_ji`.

All norm contributions are nonnegative and their sum is the point's exact squared norm. If every D_i>R², a feasible coordinate interval has radius below1. It can contain only floor(-c_i), ceil(-c_i), with coincident values counted once.

Define the preferred integer to be the closer of these two; at exact half-integer ties choose the smaller integer. Define the other distinct integer, when present, as nonpreferred. The nonpreferred integer has distance at least1/2 from -c_i, including a tie. Its squared contribution is therefore at least D_i/4.

Consequently any feasible path with nonpreferred index set S obeys

`sum_(i in S) D_i <=4R²`.

For a fixed S, the full integer coefficient path is uniquely determined, if it exists: starting at the highest index, each center depends only on already determined higher coefficients; take preferred or nonpreferred exactly as specified by S. A failed norm test terminates that S, and coincident floor/ceil makes a requested nonpreferred branch nonexistent. Thus dependence of lower centers on upper choices does not multiply paths for one S.

**Corollary for this p17 certificate.** All D_i>9,538,237 and `3 min_i D_i>4*9,538,237`. Every feasible path has at most two nonpreferred coordinates. Uniformly, each affine class has at most

`1+16+binomial(16,2)=137`

potential complete paths, and all sixteen relaxed classes have at most2192. This already replaces the earlier crude `16*2^16=1,048,576` bound.

## 3. Exact weighted bound

Use the individually certified D_i rather than just their minimum. All sixteen singleton nonpreferred sets are allowed by the static necessary test for every residue. Only pairs satisfying `D_i+D_j<=4R_r²` need be retained. Triple sets fail uniformly. The exact small comparisons give:

| r | q1 cost | positive q0 budget | eligible nonpreferred pairs | complete-path upper bound | actual maximal-p17 membership |
|---:|---:|---:|---:|---:|---|
| 1 | 305 | 2026 | 19 | 36 | yes |
| 2 | 322 | 2009 | 17 | 34 | no: cofactor19 |
| 3 | 339 | 1992 | 15 | 32 | yes |
| 4 | 356 | 1975 | 14 | 31 | yes |
| 5 | 373 | 1958 | 13 | 30 | yes |
| 6 | 390 | 1941 | 11 | 28 | no: cofactor23 |
| 7 | 407 | 1924 | 9 | 26 | yes |
| 8 | 424 | 1907 | 7 | 24 | yes |
| 9 | 441 | 1890 | 6 | 23 | yes |
| 10 | 458 | 1873 | 6 | 23 | yes |
| 11 | 475 | 1856 | 5 | 22 | yes |
| 12 | 492 | 1839 | 3 | 20 | no: cofactor29 |
| 13 | 509 | 1822 | 1 | 18 | yes |
| 14 | 526 | 1805 | 0 | 17 | no: cofactor31 |
| 15 | 543 | 1788 | 0 | 17 | yes |
| 16 | 560 | 1771 | 0 | 17 | yes |

For the stronger sixteen-class relaxation, the upper bound is **398 potential complete paths**. An implementation that shares prefixes and rejects forbidden nonpreferred sets before evaluating children needs at most **3909 labeled feasible-prefix nodes**, including roots. Without prefix sharing, simply evaluating each allowed S once uses at most398*16=6368 coordinate choices. These are structural operation bounds, not measured execution time or a count of actual candidates.

For the original maximal-p17 domain, r=2,6,12,14 are excluded directly: their q1 denominators have a prime factor above17. This is an exact domain-membership certificate, not proof that those four relaxed affine classes are empty. Record all four exclusions explicitly; do not call them a prime-only sieve or erase their records. The remaining twelve cofactors are all composite and have prime factors at most13; they are retained in full.

The actual p17 order1 search therefore needs at most **299 potential complete paths**, or **2946 shared-prefix nodes** under the stated pruning scheme. Independent evaluation of allowed sets uses at most299*16=4784 coordinate choices. The optional stronger sixteen-class regression remains bounded by398 paths.

## 4. Exact lower-prime / H0 completion interface

Suppose an admissible residue r and a signed-budget feasible u survives. Define its known reciprocal-moment contribution

`M_0=1+sum_s u_s`,

`M_k=a_r^(-k)+sum_s u_s(17s)^(-k)`, k=1,...,6.

Write `Q_k=(17+r)^(-k)+sum_s u_s s^(-k)`. The local mixed congruences give `Q_k in17^k Z_(17)`, where `Z_(17)` denotes rationals with denominator coprime to17. Therefore `M_k=17^(-k)Q_k in Z_(17)`: each reduced rational M_k has no denominator divisible by17. This removes the p17 pole obstruction, but it does not construct a completion.

Define residual side budgets

`B_+=2331-v_r-P(u)`, `B_-=2331-N(u)`.

Both must be nonnegative. Let A contain **all** remaining integer denominators a>=2 with 17 not dividing a, no prime factor above17, and fitting an applicable residual side budget. Since a has no factor17, its maximal prime is at most13. This includes the composite relation background; no prime-only replacement is permitted.

A full normalized collision extending this p17 layer exists if and only if there are integers t_a on this finite carrier satisfying

`sum_(a in A) t_a a^(-k) = -M_k`, k=0,...,6,

`sum_a(a-1)max(t_a,0)<=B_+`,

`sum_a(a-1)max(-t_a,0)<=B_-`.

Necessity follows by splitting a normalized full collision into its 17-divisible and 17-free denominators. Sufficiency follows by taking the positive and negative signed multiplicities as the two exponent shapes; the binomial triangular change restores H0,...,H6 equality. The q1 atom ensures nontriviality. A local modular survivor alone establishes neither a full collision nor impossibility of completion.

Cheap necessary completion cuts are

`-B_+ <=M_0<=B_-`,

`-B_+/2^k <=M_k<=B_-/2^k`, k=1,...,6.

Indeed each remaining atom has cost at least1 and reciprocal k-th moment at most2^(-k). These cuts are only necessary; passing them does not solve the integer completion problem. If a local kernel fails a completion cut, retain it as `LOCAL_FEASIBLE / FULL_COMPLETION_EXCLUDED_BY_NAMED_CUT`, not as an empty affine class.

## 5. Precise outcome boundaries

Proved now: signed-budget derivation; exact sphere radius; deterministic farther-choice theorem;2192/398/299 structural path bounds; four exact maximal-prime exclusions; the necessary-and-sufficient finite completion formulation and its cheap necessary cuts.

Independently checked by small arithmetic now: the p17 certificate hash and previously reconstructed exact norms, all norm/subset inequalities, costs and admissible residue membership. `P17_ORDER1_BRANCH_BOUND_RESULTS.json` contains every eligible pair and prefix count. The two executions of the small script reflect adding the domain-membership refinement; neither constructed affine centers or ran a census.

Still OPEN: whether any of the twelve admissible classes has a feasible q0 point; whether any survivor admits lower-prime/H0 completion; all higher p17 orders and the global T6 target. No class is labeled EMPTY by this preparation. The original p19 Source campaign is not rerun or retroactively made an independent census.

Recommended formal unit: produce a sixteen-row domain/status ledger, with four `OUTSIDE_MAXIMAL_P17_DOMAIN` rows and exact EMPTY or complete feasible-vector lists for twelve admissible rows. Use the299-path bound and preserve completion obligations. The stronger398-path relaxation may be retained as an optional validation control, not an unstated extra hard target.
