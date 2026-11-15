# EC49FPZ — Complete exact price envelope for native BRC class 16995

**2026-11-15 | AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED**

Frozen scientific input pin `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. New quantitative continuation of the independently published EC49FPY [PR #2505](https://github.com/awdawmip/enterprise-math/pull/2505) (qualitative sensor-use phases), and existing EC49FPS/EC49FPU–FPW/EC49FPN finite policies. All source bytes and P000 remain unchanged.

## Exact finite theorem

The complete legal native-BRC root domain represented by configuration **16995** contains **242 original source configurations**, **112 distinct named-root cost states**, 324 legal complete-terminal observations T, 96 legal named-root/subset observations R, and 395 different response partitions. Observations return exact integer values. An R observation costs `r>0`, a T observation `t>0`. Source prior is uniform on the **242 original configurations** (including profile multiplicities). Target: identify the full named-root profile. Adaptive tree depth is unrestricted.

For **every r,t>0**, the globally minimal expectation is

`E_min(r,t) = (1/242) min_{(R,T) in W}(R*r+T*t)`,

where W is the following **15 exact feasible source-weighted sensor-count pairs**. On each open interval, the displayed line is globally optimal; at each rational transition, the neighboring lines tie (and possibly additional policies tie).

| Ratio interval x=r/t | Weighted R | Weighted T | Optimal expected cost |
|---|---:|---:|---|
| `0 < r/t < 44/79` | 841 | 0 | `(841r+0t)/242` |
| `44/79 < r/t < 39/70` | 762 | 44 | `(762r+44t)/242` |
| `39/70 < r/t < 3/5` | 692 | 83 | `(692r+83t)/242` |
| `3/5 < r/t < 11/18` | 687 | 86 | `(687r+86t)/242` |
| `11/18 < r/t < 2/3` | 669 | 97 | `(669r+97t)/242` |
| `2/3 < r/t < 11/16` | 657 | 105 | `(657r+105t)/242` |
| `11/16 < r/t < 31/45` | 641 | 116 | `(641r+116t)/242` |
| `31/45 < r/t < 9/13` | 371 | 302 | `(371r+302t)/242` |
| `9/13 < r/t < 7/10` | 358 | 311 | `(358r+311t)/242` |
| `7/10 < r/t < 3/4` | 348 | 318 | `(348r+318t)/242` |
| `3/4 < r/t < 7/8` | 316 | 342 | `(316r+342t)/242` |
| `7/8 < r/t < 37/41` | 252 | 398 | `(252r+398t)/242` |
| `37/41 < r/t < 40/41` | 170 | 472 | `(170r+472t)/242` |
| `40/41 < r/t < 1` | 129 | 512 | `(129r+512t)/242` |
| `1 < r/t < infinity` | 0 | 641 | `(0r+641t)/242` |

All **14 exact positive switch ratios** are `44/79, 39/70, 3/5, 11/18, 2/3, 11/16, 31/45, 9/13, 7/10, 3/4, 7/8, 37/41, 40/41, 1`. This gives a *complete numerical price diagram*, beyond the qualitative mandatory-mixing result in EC49FPY. For example at r:t=3:5, the exact weighted integer optimum is 2491, and at r:t=3:4 it is 2316. Weighted query counts sum over 242 source paths, not the number of available sensor types.

## Global lower and upper certificates at every rational transition

For state subsets M of the 112 cost profiles and source multiplicities w_i>0, write w(M)=sum_(i in M) w_i. Each legal sensor q partitions M into exact response fibers M_(q,v). A positive-price nonsplitting sensor can be dropped. The complete unrestricted Bellman problem is

```
F({i}) = 0
F(M) = min_{q splitting M} [ c(q)*w(M) + sum_{v:|M_qv|>1}F(M_qv) ],
where c(q) is r for root sensors, t for terminal sensors.
```

Strictly splitting queries always decrease branch state-set cardinality, so this recurrence represents **every finite distinguishing adaptive tree**, with no depth cutoff or assumption that a particular heuristic policy is optimal. Equivalent query response partitions are deduplicated; on the certified domain r<=t a duplicate R is no dearer than T. All **395** classes of responses are kept.

A fully executed exact C++ Bellman solver computed the **global root value at each of the fourteen boundary ratios**. A second independent C++ verifier then checked a finite lower-bound *subsolution* L on 20k–23k information-state masks at **every splitting partition**:

```
L(M) <= c(q)*w(M) + sum_v L(M_qv).
```

For an unlisted nonsingleton mask we define L(M)=r*w(M), and for a singleton L=0; this is always a valid subsolution at any 0<r<=t because any splitting sensor itself costs at least r*w(M). Induction on |M| therefore proves L(M)<=F(M) for **all** information subsets, including masks not visited by the solver. An explicit identifying tree constructed by the solver has cost exactly L(all 112) at each knot. Thus feasible upper and checked lower match and establish global Bellman optimality independently of solver branch ordering/pruning.

| r:t | Exact weighted F(all) | Memo masks | Independent lower check |
|---|---:|---:|---|
| 44:79 | 37004 | 20154 | PASS |
| 39:70 | 32798 | 20145 | PASS |
| 3:5 | 2491 | 20532 | PASS |
| 11:18 | 9105 | 20694 | PASS |
| 2:3 | 1629 | 21358 | PASS |
| 11:16 | 8907 | 21734 | PASS |
| 31:45 | 25091 | 21746 | PASS |
| 9:13 | 7265 | 21763 | PASS |
| 7:10 | 5616 | 21860 | PASS |
| 3:4 | 2316 | 22148 | PASS |
| 7:8 | 4948 | 22808 | PASS |
| 37:41 | 25642 | 22714 | PASS |
| 40:41 | 26152 | 21732 | PASS |
| 1:1 | 641 | 21121 | PASS |

The 14 memo files and the *actual executed* separate verifier, with 6.9m–7.9m exact partition/mask comparisons per knot, are preserved in the accompanying offline evidence archive. The JSON certificate records SHA256 for each of the fourteen lower memo files.

### Proof between the boundary ratios (not interpolation by sampling)

For any fixed feasible decision tree P, its source-weighted price is affine in x=r/t, namely R(P)*x+T(P). Each candidate listed in the 15-line table is itself a feasible tree, so is an upper bound everywhere. At each closed interval between two consecutive boundary knots, the candidate line equals the **unrestricted Bellman global optimum at both endpoints**. For any competing P, the affine difference `C(P,x)-C(candidate,x)` is nonnegative at both endpoints and therefore throughout the entire interval. This proves global optimality for the **uncountable continuum of all intermediate positive prices**, without a numerical grid assumption. A strict change of adjacent slopes confirms the asserted genuine switches.

**New structural corollary — uniquely forced total sensor counts inside each open phase.** Fix one of the fifteen listed open price intervals, and let P be *any* globally optimal identifying tree at one strictly interior ratio x0. Relative to the listed optimal line, P's weighted price difference is affine in x, nonnegative on the whole interval by the theorem, and zero at the interior point x0. An affine function nonnegative on an interval and zero at an interior point vanishes identically. Thus P has **exactly the listed source-multiplicity-weighted pair (R,T)**; different optimal tree structures may exist but their aggregate counts cannot change inside a phase. At every positive rational knot, adjacent distinct aggregate pairs are both feasible and optimal, so the weighted-count pair is not unique there. This proves the transitions are genuine changes of optimal policy resource usage, not merely changes among interchangeable tree encodings.

For 0<x<44/79 and x>1, the prior EC49FPY exact global endpoint and affine monotonicity arguments prove pure-root (841,0) and pure-terminal (0,641), respectively. At both endpoints the present checks agree. Thus the theorem is global for every r,t>0.

## Exact source identity and reproducibility

- Frozen master: `frozen_original_master.txt` SHA256 `cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e`.
- Native root cost CSV: `EC49FPG_PROFILE.csv` SHA256 `a61a3ee4d2f13f9d216f52cd3529c72d395c1250bfb1d7ae96a1adf5a6837c1f`.
- Pure-R verified source tree: `research_notes/portable_direct/EC49FPS_CONFIG_WEIGHTED_HALF_PRICE_CERT.json` @ `ab9f585d097492931704a4dd408afdc3948d439d`.
- EC49FPY qualitative proof: PR #2505 @ `3dbb3fc76111eb0493e6cf1da84f6a585c55bd42`, not duplicated.
- Witness trees from EC49FPU–FPW and EC49FPN, PRs #2498 and #2479.

The attached `VERIFY_EC49FPZ.py` is a standalone exact-integer Bellman **recomputation** extending the predecessor's checker to all 14 knots, and additionally checks the 15-line envelope at every knot. Invoke with the above two frozen inputs plus the pure-R certificate:
```
python VERIFY_EC49FPZ.py frozen_original_master.txt EC49FPG_PROFILE.csv EC49FPS_CONFIG_WEIGHTED_HALF_PRICE_CERT.json
```
The available full offline research archive additionally contains all fourteen independent subsolution memos, verifier and solver C++17 source, original master+native cost data, incumbent trees, validation logs and SHA256 manifest. Local C++ finite checks were actually executed; the GitHub Python script is published for reproducibility, not claimed here to have been executed by GitHub. A Git commit does not imply mathematical peer review.

## Boundaries and next question

This is an **exact finite result for class 16995**, preserving named-root identity and original-source multiplicity. It does **not** imply a result for all 625 legal classes, an asymptotic complexity theorem, a native X6 physics law, or formal Lean verification. P000 and protected worldview were not changed. No new formal Task/CLAIM/Result/Review or Foundation admission is asserted. Current task topic RS-EC49AS had no verified immutable publication directory at the bounded read; independent non-overwriting portable research preservation is used.

**Next:** quantify optimal-tree degeneracy and alternate optimal sensor sequences at the rational knots, and extend this parametric envelope method to the 16943 class with terminal-invisible named-root residuals.
