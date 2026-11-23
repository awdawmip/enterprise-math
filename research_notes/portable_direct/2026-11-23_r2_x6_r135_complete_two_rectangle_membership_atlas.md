# X6 R135 — complete Port-10 strict-near membership atlas inside both R134 (B,D) rectangles

Date: 2026-11-23. Status: **AUTHOR ALGEBRAIC PROOF + 33 EXACT FULL-DIRECTION FRACTION REPLAYS; NOT INDEPENDENTLY REVIEWED**.

## Scope and immutable scientific inputs

This is the conditional six-pair BRC observer on a declared three-coordinate *slice/readout* of native X6, **not** native six-axis dynamics, a new three-dimensional independent world, or a change to P000.

Freeze R121's Port-10 physical integer direction set, R122's global strict-near necessary candidate envelope, and R134's two fixed-optimizer/no-outsider rectangle theorems:

- R121: `enterprise-math@8085ff663b5987c58a1bc0a4a3b1d7da3a1d89fd:research_notes/portable_direct/2026-11-23_r2_x6_r121_small_port_exact_optimizer.md`.
- R122: `enterprise-math@0687aa24f5402da3b35f914dd6907967a9805b94:research_notes/portable_direct/x6_r122_small_port_near_exclusion_certificate.json`.
- R134: `enterprise-math@f1b00131adf435d400d1486652c4635bdba01772:research_notes/portable_direct/2026-11-23_r2_x6_r134_two_parameter_nonradial_stability_polygons.md`.

An integer triple `a=(x,y,z)` is admissible when `0<q(a)<=10`, `q=max(sum positive components, sum negative magnitudes)`, modulo simultaneous sign reversal **only**. Set `h=(0,x+3y+6z,3x+12y+30z,7x+39y+126z)`, `g_ij=|h_i-h_j|`, `s_ij=w_i+w_j`, `F_w(a)=max_{i<j} g_ij/s_ij`, `eta=min_a F_w(a)`, and `N={a:2F_w(a)<3eta}`. All six pairs are retained.

## Theorem I — complete membership in the first rectangle

For `w=(136,B,176,D)`, `0<B<=20`, `150<=D<=220`, R134 proves `eta=3/(136+B)` and forbids any direction outside the following eight from entering:
`a1=(1,0,0),a2=(1,3,-1),a3=(4,-4,1),a4=(5,-4,1),a5=(5,-1,0),a6=(6,-1,0),a7=(7,-1,0),a8=(9,-5,1)`.

Define strict predicates
`P: 3D>B+544`, `T: B<20`,
`V: 9D>22B+1408`, `U: 9D>20B+1496`.

**Exact individual membership** (necessary AND sufficient in the whole rectangle):

| Direction | Membership |
|---|---|
| a1, a4, a5, a8 | P |
| a2 | P and T and V |
| a3, a6 | always |
| a7 | P and T and U |

Hence **for every real pair (B,D)** in the rectangle,

```text
|N_I(B,D)| = 2 + 4*[P] + [P and T and V] + [P and T and U].
Possible counts: exactly {2,6,7,8}.
```

For `0<B<20` let
`d_P=(B+544)/3`, `d_V=(22B+1408)/9`, `d_U=(20B+1496)/9`; here `d_V<d_U`. Thus `D<=d_P` gives 2; `D>d_P` gives `6+[D>d_V]+[D>d_U]`. For `B=20` the only possibilities are 2 and 6.

This yields a **complete vertical first-entry bifurcation**: for `0<B<=8`, the crossing of `d_P` is `2 -> 8`; for `8<B<=224/19`, it is `2 -> 7 -> 8`; for `224/19<B<20`, it is `2 -> 6 -> 7 -> 8`; and for `B=20` it is `2 -> 6`. Equality belongs to the lower-count side because the nearness is strictly `<3/2`.

## Theorem II — complete membership in the second rectangle

For `w=(722,B,240,D)`, `350<=B<=600`, `1<=D<=200`, R134 proves `eta=3/(240+D)` and forbids outsider entry. Its eight eligible directions are
`b1=(1,0,0),b2=(3,-4,1),b3=(3,3,-1),b4=(4,-4,1),b5=(6,-1,0),b6=(7,-8,2),b7=(7,-1,0),b8=(9,-5,1)`.

Define
`P: 9B>3D+2880`, `T: 5D<243`,
`W: 20D<9B-2640`, `U: 11D<1698`.

| Direction | Membership |
|---|---|
| b1, b2, b8 | P |
| b3 | T |
| b4, b5 | always |
| b6 | T and W |
| b7 | P and U |

Therefore,

```text
|N_II(B,D)| = 2 + 3*[P] + [T] + [T and W] + [P and U].
Possible counts: exactly {2,5,6,7,8}.
```

Write `d_P=3B-960`, `d_T=243/5`, `d_W=(9B-2640)/20`, `d_U=1698/11`. In the declared rectangle: if `D>=d_P` the count is 2; if `D<d_P` it equals `5+[D<d_T]+[D<min(d_T,d_W)]+[D<d_U]`. Every threshold is strict and is evaluated with exact equality.

When `B<1204/3`, the `W` wall occurs before the `T` wall during increasing D, giving the initial `8 -> 7 -> 6`; at or above `B=1204/3`, the two departures coincide or reverse, giving `8 -> 6`. At `B=350,D=90` the P wall removes four directions simultaneously (`6 -> 2`); D=90 itself has count 2. These phase behaviors are exact within the specified rectangle.

**Monotonicity consequence:** with B fixed, the count is nondecreasing in D in Theorem I and nonincreasing in D in Theorem II. There is no direction re-entry along any such vertical segment inside either rectangle. This is a local conclusion, not a global monotonicity claim for other parameter rays.

## Proof of the membership tables

R134 already proves (i) the stated optimizer over each entire rectangle, and (ii) exclusion of every direction outside the listed center eight. Thus only the 48 strict comparisons for each center are relevant.

Let `k=01` in I, `k=23` in II. Since `eta=3/s_k`, a listed direction is strictly near iff **all** six affine forms
`L_(a,ij)=9*s_ij - 2*g_ij(a)*s_k` are positive. Substitute the four h-values above and the physical weights.

For I, the only comparisons that can vanish or become negative within the rectangle are:
- pair 13 on a1,a2,a4,a5,a7,a8, whose form is `-3B+9D-1632`, equivalent to P;
- pair 02 on a2,a7, whose form is `360-18B`, equivalent to T;
- pair 23 on a2, whose form is `9D-22B-1408`, equivalent to V;
- pair 03 on a7, whose form is `9D-20B-1496`, equivalent to U.
Every other form is **strictly positive at all four closed-rectangle vertices** and therefore everywhere in the physical rectangle by affinity. Moreover `U=>V` because `(20B+1496)-(22B+1408)=88-2B>0` when B<=20. This proves I.

For II, the potentially active comparisons are:
- pair 13 on b1,b2,b3,b6,b7,b8: `9B-3D-2880`, equivalent to P;
- pair 02 on b3,b6: `1458-30D`, equivalent to T;
- pair 12 on b6: `9B-20D-2640`, equivalent to W;
- pair 03 on b7: `1698-11D`, equivalent to U;
plus pair 03 on b3 (`738-15D`), pair 12 on b3 (`9B-18D-2160`), and pair 03 on b6 (`1218-13D`). The latter three are strictly positive whenever T holds, since then D<243/5, B>=350, and the corresponding lower bounds are respectively `9`, `576/5`, `2931/5`. Under T, P also follows with lower bound `9B-3D-2880>621/5`. All remaining comparisons are strictly positive on the whole rectangle. The table and indicator formula follow.

The possible-count sets are exhaustive by the indicator formulas and attained by integer sample weights: I at `(B,D)=(19,180),(19,190),(19,207),(19,211)` gives `2,6,7,8`; II at `(350,100),(465,160),(465,49),(350,26),(465,48)` gives `2,5,6,7,8`. The strict boundary and phase assertions follow by comparing the displayed rational thresholds.

## Reproducibility and evidence status

The attached `x6_r135_rectangular_complete_membership_verify.py` computes every one of the 1,935 Port-10 unoriented integer directions, all six gap scores and the exact minimizing score with Python `fractions.Fraction` for **33 specified rational samples including equality endpoints**. Exact set equality and exact optimizer agreement passed: I 17/17; II 16/16. This is an independent finite **sample replay**, not the logical basis for the all-real-parameter claim; the latter is the affine argument above plus the pinned R134 theorem. No floating-point tolerance is used.

Status: author conditional analytic proof with exact full-direction samples; not independent mathematical review, not a formal Result/Review, and no native X6 dynamics or P000 promotion.

## Next discriminating unit

Move beyond the two frozen rectangles **across an optimizer-switch wall**. Compute both adjacent optimizer branches and verify outsider entry (including candidates outside the original eight), then derive a complete adjacent-cell membership formula. Maintain the original task pins and native/conditional observation distinction.