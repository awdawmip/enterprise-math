# Frozen BRC R5: a sharp one-addition bound and 79 certificates of non-nested optimal samples

Date: 2026-11-13. Scientific input: immutable `awdawmip/enterprise-math@435e77af0d180eac32bd1f9c4c464bc4010b7551`.
Predecessor evidence: #2302 (`c3989b2846f81cdda694efa1bf1b043150a8169a`) and #2307 (`76f8c46d4693bb45721e285aa5c3a507a4cbb7c2`). This is a scalar event-distance observer result with joint certificate provenance retained in the frozen source; it does not modify P000 or claim native six-axis equivalence. Independent author reconstruction below uses only the pinned 15 atoms and rational thresholds.

## Model

Let `X={x_0<...<x_{N-1}}` be a finite set of **distinct integers**. For a center set `S subset X`, write `d_S(x)=min_{s in S}|x-s|`; call S radius-2 feasible when `max_{x in X}d_S(x)<=2`. For feasible budgets define `J_2(K)=min_{|S|=K}sum_{x in X}d_S(x)`. Costs and distances here are scalar integer event steps.

## Theorem: sharp incremental improvement bound

For every radius-2 feasible S and every new candidate center `t in X\S`,

```
0 <= sum_x d_S(x) - sum_x d_{S union {t}}(x) <= 3.
```

**Proof.** Any improved x must satisfy `|x-t|<d_S(x)<=2`. Because X contains distinct integers, the only possible improved points are `t-1,t,t+1` (when present). At t the saving is `d_S(t)` and is either 1 or 2 (t is not already in S). If `d_S(t)=1`, a previous center exists at t+1 or t-1: the adjacent point on that side cannot improve, and the other adjacent point can save at most one. Total saving <=1+1=2. If `d_S(t)=2`, an old center exists at t+2 or t-2: its intermediate neighboring point (when present) is already within distance 1, so cannot improve; the other neighboring point can save at most one. Total saving <=2+1=3. All other points are unchanged. QED.

**Sharpness (single-center addition, not necessarily optimal).** Set X=`{-3,-1,0,1,2}`, old feasible S=`{-3,2}`, and t=0. Old pointwise distances are `(0,2,2,1,0)`; after adding t they are `(0,1,0,1,0)`. The total saving is exactly 3.

## Corollary: exact non-nesting certificate

If `J_2(K)-J_2(K+1)>3`, **no** optimal (K+1)-center solution contains **any** optimal K-center solution. Otherwise such a nested pair would be related by one center addition, contrary to the theorem. In particular a budget sweep that merely adds one center to the previously optimal set cannot attain every optimum at these transitions. A correct marginal-heap merge of separately *reoptimized* component cost curves is not ruled out.

A seven-coordinate standalone witness is `X=(0,1,3,4,6,7,8)`, radius 2:
- At K=2, unique optimal set `(1,6)` with cost `J_2(2)=8`.
- At K=3, exactly four optimal sets `(0,3,7)`, `(0,4,7)`, `(1,3,7)`, `(1,4,7)`, each with cost `J_2(3)=4`.
All center subsets of sizes 2 and 3 are enumerated in the accompanying program. The gain 4 exceeds the sharp one-addition bound, and none of the K=3 optima contains both 1 and 6.

## Frozen R5 exact result

Rebuild the 15 signed atoms of the frozen R5 certificate, the q=3,12,15 rational threshold families, and multiplicities. This gives 953 distinct rational walls, 954 boundary coordinates, 1065 events, and 4383 radius-2 directed transitions. An independent integer dynamic program recomputes every feasible budget K=213..954 from these source coefficients, rather than reading the earlier CSV as an oracle.

Its 741 adjacent marginal gains have histogram:

| Gain J(K)-J(K+1) | Number of transitions |
|---|---:|
| 1 | 603 |
| 2 | 36 |
| 3 | 23 |
| 4 | 70 |
| 5 | 8 |
| 6 | 1 |

There are **79 certified non-nested transitions** (70 of gain 4, 8 of gain 5, 1 of gain 6). The first is K=213 -> 214: `1070 -> 1064`, gain 6. The nine transitions with gain greater than 4 run from K=213->214 through K=221->222; an additional 70 transitions with gain 4 are also excluded from nested optimality by the sharp bound.

The independent full-budget recomputation gives `sum_{K=213}^{954}J_2(K)=292961`, `sum K*J_2(K)=130909193`, `J_2(351)=603`, and `J_2(954)=0`, agreeing with the previous all-budget exact output. Its 7-coordinate counterexample is separately exhaustively checked.

## Verification method and scope

`VERIFY_R5_R2_NONNESTING.py` is self-contained Python 3 standard library only, using exact integers, `Fraction`, Gray-code subset enumeration, and a fresh explicit center-to-center interval DP. Its graph recurrence is exact because a point between two neighboring centers is served by the nearer of those two; the first and last chosen center serve their exterior tails. Radius-2 feasibility for all intermediate points is tested explicitly. At most five index steps separate consecutive selected centers in a valid solution on distinct integer coordinates; the code includes all such transitions, including physically long gaps with no intermediate coordinates.

`EXACT_OUTPUT.json` is from executing the script locally in this research run. No stochastic tests or floating arithmetic are used for these conclusions. The earlier #2307 block decomposition and convex-merge observations remain available but are not prerequisites to the non-nesting theorem.

## Next live scientific question

Find a characterization or tight certificates for *which* budget transitions admit nested optimal center sets despite marginal gains <=3, and characterize reconfiguration cost (minimal symmetric difference) at the 79 obstructed transitions. Independently pursue the original 28-coordinate/8192-prefix-query end-to-end replay; the present proof concerns the scalar radius-2 sampling optimizer only.

Control: scientific draft, formal R5 Task owner/CLAIM not asserted by this file; Research Activity and independent review have their own Source contracts.
