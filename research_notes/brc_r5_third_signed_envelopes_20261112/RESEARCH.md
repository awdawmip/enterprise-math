# R5 — third signed affine-prefix chambers and six exact collision transfers

Date: 2026-11-12 (Asia/Shanghai). Status: **author-side exact finite result, pending formal Source Result and independent review**. Model: frozen external P/Q–BRC Blackwell auxiliary observer, not native X6 dynamics.

## Scientific provenance and scope

Continue [R5 second signed cells](../brc_r5_next_signed_envelopes_20261112/RESEARCH.md), parent commit `7970d58caf220c46682ddc387f53080646d84908`, Draft PR #2127. All fixed 28-entry rational transfer masses, 15 **labeled** BRC residual atoms and observer constraints remain unchanged.

- Frozen Global science pin: `a01383f825ef9d43b4b754254303298c64041568`.
- Frozen Enterprise Math science pin: `86149263e38c22292c9def1e0f69092efa1be77e`.
- Original immutable fixture and equations: `435e77af0d180eac32bd1f9c4c464bc4010b7551` / `research_notes/brc_r5_sharp_nonlocal_fifteen_ray_20261111/VERIFY_R5_SHARP_RAY.py`.
- P000 and ACTIVE worldview unchanged. No native Task/CLAIM ownership, independent review or Source admission is claimed.

Put `x=155682221/25142124560000000`, `r=eta/x`, `X(r)=X+x*r*H`, where H changes source-3 targets 1,2,6 by (-23,+28,-5) and source-1 by the opposite amounts, so `obs(H)=0`. The existing 15 **labeled** operations are `M_a` and the maximal full-ray endpoint is `epsilon_max=9/115400000`.

For nonempty subset S, set `P_S=36 sum_(a in S) M_a`, an integer 28-vector, and define

`tau_S(r) = min_(k:P_S[k]<0) 36*(X[k]+x*r*H[k])/(-P_S[k])`.

The complete finite domain has `2^15-1=32767` nonempty prefix subsets and 28 transfer coordinates.

## Theorem 1 — next two sharp minimizer chambers

Immediately beyond the previously certified sharp boundaries, the first-zero winning coordinate for *every* nonempty subset stays constant throughout these open chambers:

- Positive: **`1/1265 < r < 5/5083`**.
- Negative: **`-1/1633 < r < -1/2461`**.

At the new positive endpoint `r=5/5083`, exactly masks **14597, 31509** switch their winning coordinate from (target 0, source 3) to (target 1, source 3), indices 14 -> 15. At the new negative endpoint `r=-1/1633`, mask **15109** switches from (target 1, source 3) to (target 0, source 3), indices 15 -> 14, as r decreases. There is **no earlier winner switch** in either interval.

Across the *starting* boundaries `1/1265` and `-1/2461`, exactly 7 positive and 2 negative subset first-zero tags respectively switch. The original maxima and all 15-atom endpoint mass constraints remain valid for the entire corresponding **closed** intervals.

**Proof (finite and exhaustive).** For each of the 32767 masks enumerate all its negative-capacity coordinates. Each contributes a rational-affine candidate `a_(S,k)+r*b_(S,k)`. At the start boundary, choose the winning tied line having least slope for increasing r, respectively greatest slope for decreasing r. For every other line whose slope can eventually overtake the winner, solve the exact rational intersection `(a_w-a_k)/(b_k-b_w)` and retain only parameters strictly beyond the start in the chosen direction. The first global intersections are exactly `5/5083` and `-1/1633`, attained by the masks listed above. Affine comparisons prove all interior parameters at once, not just a sampled grid.

At both endpoints of each closed new chamber, the initial 28 masses are strictly positive and the complete 15-operation final masses are nonnegative, checked in exact rational arithmetic. Since each coordinate is affine in r, all intermediate parameter values have the same property. The original final zero mass at (target 0, source 2) is preserved, establishing that the maximal terminal ray time is still `epsilon_max`.

## Theorem 2 — six exact moving/fixed phase collisions

Inside both new open chambers, the first-zero threshold tags use the same **1144 fixed phase forms**

`F_n=36*x/n`

and the same **three moving forms**

`Q_q=x*(1-23*r)/q`, where `q in {3,12,15}`.

Their subset tag counts are:

| Chamber | F masks | Q masks | Beyond ray | Ray endpoint |
|---|---:|---:|---:|---:|
| Positive | 14,648 | 11,011 | 6,809 | 299 |
| Negative | 14,666 | 10,993 | 6,809 | 299 |

For generic r there are 1147 distinct internal first-zero phase times. Exactly three new moving/fixed crossings occur in each chamber, each with the following *transfer of complete legal labeled permutation loss to the moving phase*:

| Direction | r | Moving q | Fixed n | Transfer to Q |
|---|---|---:|---:|---:|
| Positive | `11/12673` | 15 | 551 | +268,206,336 |
| Positive | `1/1127` | 12 | 441 | +339,142,284 |
| Positive | `1/1058` | 15 | 552 | +80,117,424 |
| Negative | `-1/2047` | 15 | 534 | -63,350,880 |
| Negative | `-5/9821` | 12 | 427 | -194,644,632 |
| Negative | `-7/12259` | 15 | 533 | -179,781,408 |

All six are strict interior crossings. For each crossing, the change in the fixed-phase loss equals minus the change in the moving-phase loss, so their paired total loss is invariant.

**Exact proof.** The equality `Q_q=F_n` yields `r=(n-36q)/(23n)`. Enumerating every n from the 1144 fixed forms and q in {3,12,15} finds precisely three crossings per interval. At exact rational midpoints immediately before and after each crossing, count legal labeled permutations using the Boolean-lattice integer recurrence `ways(empty)=1`, `ways(S)=0` for any forbidden prefix, and otherwise `ways(S)=sum_(a in S) ways(S minus {a})`. The difference of inclusive and strict counts at a threshold is the loss of complete labeled orders at that threshold.

Detailed checked pairs (first coordinate is F loss; second Q loss):

| r | Before F, Q | After F, Q |
|---|---|---|
| `11/12673` | 1,276,121,520; 384,181,985,520 | 1,007,915,184; 384,450,191,856 |
| `1/1127` | 1,235,944,984; 140,657,487,480 | 896,802,700; 140,996,629,764 |
| `1/1058` | 2,151,595,488; 384,450,191,856 | 2,071,478,064; 384,530,309,280 |
| `-1/2047` | 694,728,336; 377,728,635,456 | 758,079,216; 377,665,284,576 |
| `-5/9821` | 254,255,856; 137,055,984,032 | 448,900,488; 136,861,339,400 |
| `-7/12259` | 572,917,392; 377,665,284,576 | 752,698,800; 377,485,503,168 |

In both chambers, the exact number of legal complete 15-operation orderings at the maximal terminal ray time is **3,514,190,816**. At the next positive boundary `r=5/5083`, `Q_12=F_442`; at the next negative boundary `r=-1/1633`, `Q_12=F_426`. These phase-value coincidences and the coordinate-minimizer switches are distinct events.

## Reproduction and verification scope

`VERIFY_THIRD_SIGNED_ENVELOPES.py` invokes the pinned ancestor fixture, enumerates all 32767 nonempty masks, checks all rational-affine candidate lines, validates closed-interval endpoint nonnegativity, and computes exact six-event paired schedule counts with integer dynamic programming. The full 28 coordinates and original observer conditions remain in use.

`EXACT_OUTPUT.txt` records an **actually executed locally equivalent reconstruction** using original 28 rational X masses and 15 original labeled atom coefficients, transcribed from the immutable original fixture. The published GitHub wrapper itself has **not** been independently rerun from its uploaded bytes. The exact finite result is limited to this frozen external transport observer; it is not a native X6 or a universal 15-step connectivity claim.

## Next unfinished unit

Cross `r=5/5083` and `r=-1/1633`. Determine whether the set of 1144 fixed phase-value forms changes in the following minimizer cells, and compute subsequent moving/fixed crossings and order-count transfers. Preserve original scientific pins, P000, all live owners and existing task/Result/review authority.
