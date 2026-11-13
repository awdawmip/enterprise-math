# R5 — Exact optimal-face segment and a full physical-source fiber for the 16-edge atlas escape cost

Date: 2026-11-09 (Asia/Shanghai). Status: AUTHOR_PROVED / EXACT_FRACTION_EXECUTED / INDEPENDENT_REVIEW_PENDING / NOT_ADMITTED.

## Scientific inputs and scope

This is a follow-up to author-side PR #1855, immutable commit `2a36e7806a815354b66788aca9aff4c27c890ba4`, with its seven common LR nodes, physical FULL_HIST mass/stop-time maps, fixed 16-edge atlas `S=SA∪SB`, source `x`, seedless-F target `y`, 13-positive-edge primal coupling `P`, and 21-coordinate dual `z`. The observer kernel `K` and capacity slacks derive from author-side PR #1849, immutable commit `81e25545ee3ae6aeeab6c054c3c6bb706191fb95`; chamber observations are detailed in #1851. Frozen science/task pins as identified in #1851 are GLOBAL `a01383f825ef9d43b4b754254303298c64041568`, EM `86149263e38c22292c9def1e0f69092efa1be77e`. Normative rules are read at current main independently. Neither P000 nor prior task publications or reviews are changed.

This note studies *one exact marginal pair* and all physical source representatives with its fixed observer. It gives a complete classification of its atlas-escape-optimal Blackwell couplings and an exact nontrivial family of physical source realizations. All finite calculations use exact rational arithmetic; each all-real claim follows from linear equalities, nonnegative affine inequalities, and the dual inequality.

Let `r=(1/10,1/2,3/4,1,5/4,3/2,19/10)`. Write `E_(i,j)≥0` for mass sent from source LR index `j` to target LR index `i`; the seven row, seven column, and seven LR-moment equations are

`sum_j E_(i,j)=mu_i`, `sum_i E_(i,j)=nu_j`, `sum_i r_i E_(i,j)=r_j nu_j`.

For the frozen `g=b` source face, `nu_4=0`, while extremal columns 0 and 6 can only use `(0,0)` and `(6,6)`. Thus the effective edge universe has **30** allowed edges. The cost is `eps_S(E)=sum_(i,j)∉S E_(i,j)`; `S` is the 16-edge union defined in the attached checker and predecessor.

## Theorem 1 — the full optimal coupling face is exactly one closed segment

Use the precise source/target marginal pair from #1855, reproduced in `VERIFY.py`. The predecessor established the exact primal–dual optimum

`c = 225713944957 / 3385915560000 > 0`.

For that pair, **every** nonnegative Blackwell coupling minimizing `eps_S` has the form

`E(t)=P+tH,     0 ≤ t ≤ 3997/690000`,

where `P` is the predecessor's exact 13-edge coupling and `H` has exactly six nonzero entries:

| Edge `(i,j)` | `H_(i,j)` |
|---|---:|
| (0,1) | -10/13 |
| (2,1) | 23/13 |
| (4,1) | -1 |
| (0,2) | 10/13 |
| (2,2) | -23/13 |
| (4,2) | 1 |

**Proof.** The predecessor's explicit feasible dual vector `z` satisfies the 30 rational edge-price inequalities `z_i+z_(7+j)+r_i z_(14+j) ≤ 1[(i,j)∉S]`, and `P` attains `z·b=c`. For every optimum, equality of the primal and dual objectives and nonnegative transport weights force zero weight on every edge with **strict** dual inequality (complementary slackness). Direct exact inspection shows the following, and no others, have zero dual slack:

`T={(0,0),(0,1),(2,1),(4,1),(0,2),(2,2),(4,2),(5,2),(0,3),(1,3),(3,3),(4,3),(4,5),(5,5),(6,5),(6,6)}`.

The 21×16 constraint matrix restricted to `T` has **rank 15**. An explicit 15×15 minor, with rows `(0,1,2,3,4,5,6,7,8,9,10,12,15,16,17)` and columns `(0,1,2,3,4,5,7,8,9,10,11,12,13,14,15)` in the displayed ordering of `T`, is exactly **`-299/1600`**. The displayed nonzero `H` is in the kernel of all 21 equations, proving rank ≤15; the minor proves rank ≥15. Thus the affine equality solution space for `T` is precisely `P+tH`, `t∈R`.

The only potentially limiting nonnegativity constraints on `t` are those of its six nonzero coefficients. Their exact intersection is

`max_(H_e>0)(-P_e/H_e)=0`, `min_(H_e<0)(-P_e/H_e)=3997/690000`,

so this segment is **exactly** the optimal face. All its points have cost `c` because `H` lies in the equality matrix kernel and is supported on dual-tight edges. Its two endpoints each have **13 strictly positive edges**, and every strict interior point has **14**. These statements are for the fixed marginal pair; the theorem classifies *all* optimal couplings, not merely a selected path. QED.

## Theorem 2 — a complete physical-source fiber reuses the entire optimal face

Fix the source physical flow

`x=(999/1000,1/6,999/1000,1/20,29/240,11/160,1/120)`

and fixed target

`y=(1,2002911/10904720,26095487/40892700,442758619/6542832000,11037627/68154500,394502727/2180944000,2002911/109047200)`.

The established exact FULL_HIST observer kernel is

`K=(-49400/295513,-49400/295513,-49400/295513,-33345/591026,132145/295513,-33345/591026,1)`.

The full set of physically lawful source representatives of `x` having exactly the same seven P/Q masses and both stop times is

`x(h)=x+hK`, with **`-295513/49400000 ≤ h ≤ 295513/36054360`**.

Here `g=b` throughout. At the lower endpoint the capacity slack `1-g` vanishes, and at the upper endpoint the capacity slack `a/10-z` vanishes. All 13 capacity slacks are nonnegative throughout the interval. The verifier computes each slack's *affine* directional derivative as `s_i(K)-s_i(0)` (important for `1-g`) and checks that these two bounds dominate all remaining admissible bounds. Because `M(K)-M(0)=0` and `T(K)-T(0)=0`, the marginal pair and dual optimum remain exactly the same at every real `h` in this full closed fiber.

Consequently, for every real parameter pair

`(h,t) ∈ [-295513/49400000, 295513/36054360] × [0,3997/690000]`,

`x(h)` is a valid source, `y` is a valid seedless target with the same stop times, and `E(t)=P+tH` is an **atlas-escape-optimal** Blackwell coupling of cost `c`. Both endpoints of the `t`-interval have 13 positive edges; its interior has 14. The product contains uncountably many distinct physically lawful source states and, independently, distinct optimal transport matrices, while **the statistical observer and target are fixed**. It is a two-parameter family in the *physical-flow × coupling* representation, not a two-dimensional observer image. QED.

## Evidence and next research question

`VERIFY.py` is a standalone Python standard-library `fractions.Fraction` checker. It replays the exact predecessor inputs, verifies physical capacities, full 21 Blackwell equations, all 30 dual edge inequalities, the complete tight set, rank 15, the exact minor `-299/1600`, the six-edge kernel, both support counts, both exact fiber endpoints and observer invariance. `EXACT_OUTPUT.txt` is actual local stdout. The min/max and rank arguments are exact finite certificates and extend to all real parameters by affine linearity and nonnegativity.

**Next:** determine how the 16 dual-tight edges and one-dimensional optimal face change as the *statistical marginals* vary away from this fixed pair. One precise local question is to construct a new 14-edge chart with an open eight-dimensional observer image near these marginals, or to identify a tight-edge/positive-mass obstruction. In parallel, the global physical 14-versus-15-edge uniform upper bound remains open; none of the present two-parameter fiber construction implies that broader bound.

BRC typing: the `h` parameter retains a physical-flow residual erased by the explicitly declared static observer, while the `t` parameter retains coupling choice for fixed marginals. These are separate fibers with explicit provenance and no identification with native X6 spatial axes, time, or unmodeled path history. This is author-side research evidence, not a formal Task CLAIM, Result, independent Driver review, or admission.
