# R5 — complete ten interior collision transfer census and endpoint coincidences

Date: 2026-11-12 (Asia/Shanghai). Status: researcher-side exact rational finite computation, independent Source Result/adversarial review pending. External frozen P/Q–BRC Blackwell auxiliary observer; no change to P000 or X6 native semantics.

## Provenance and precise question

Continue Draft PR #2122, exact branch commit \`8b4be0afaf82d00c9a7d8299c250158d57f13cbf\`, which established the two sharp affine-prefix-minimizer domains and all collision locations. Retain frozen global science pin \`a01383f825ef9d43b4b754254303298c64041568\`, EM science pin \`86149263e38c22292c9def1e0f69092efa1be77e\`, original 28-rational vector X and fifteen labeled kernel moves from PR #2102, and \`H\` with source-3 target components (-23,+28,-5) at (1,2,6), with opposite source-1 components.

Let \`x=155682221/25142124560000000\`, \`r=eta/x\`, and \`epsilon_max=9/115400000\`. The proven affine spectrum for each nonempty atom subset S on \`-1/4945<=r<=1/2507\` consists of fixed times \`F_n=36x/n\`, moving times \`Q_q=(x-23eta)/q\` (q=3,12,15), the terminal epsilon_max, and subset times beyond that terminal endpoint. We ask: when one F_n and one Q_q exchange order, how many of the 15! labeled atom schedules move from losing feasibility at F_n to losing feasibility at Q_q?

## Exact theorem: all ten interior collisions

For a fixed sign of eta, as the absolute perturbation increases from zero, each row below describes the consecutive fixed and moving phase events before and after the displayed crossing. Counts are exact integers of labeled atom permutations that become infeasible as epsilon crosses the corresponding phase. Transfer is \`moving loss after - moving loss before\`; negative means transfer *toward the fixed phase*.

| eta/x crossing | fixed n | moving q | fixed loss before -> after | moving loss before -> after | exact transferred |
|---|---:|---:|---:|---:|---:|
| +1/12443 | 541 | 15 | 959619024 -> 648765504 | 379780599984 -> 380091453504 | +310853520 |
| +1/9959 | 433 | 12 | 638087144 -> 348132356 | 138525464060 -> 138815418848 | +289954788 |
| +1/6233 | 542 | 15 | 1036269792 -> 971275392 | 380091453504 -> 380156447904 | +64994400 |
| +1/4991 | 434 | 12 | 838670712 -> 828739752 | 138815418848 -> 138825349808 | +9930960 |
| +1/4163 | 543 | 15 | 1921542048 -> 1046932848 | 380156447904 -> 381031057104 | +874609200 |
| +1/3335 | 435 | 12 | 1358449320 -> 655687656 | 138825349808 -> 139528111472 | +702761664 |
| +1/3128 | 544 | 15 | 778933584 -> 685198512 | 381031057104 -> 381124792176 | +93735072 |
| -1/12397 | 539 | 15 | 915295200 -> 915295200 | 379627579392 -> 379627579392 | 0 |
| -1/9913 | 431 | 12 | 909233764 -> 1748035204 | 138461493728 -> 137622692288 | -838801440 |
| -1/6187 | 538 | 15 | 1233247536 -> 1728228192 | 379627579392 -> 379132598736 | -494980656 |

In every row, fixed plus moving losses remain exactly the same on both sides. Distinct signs have distinct chamber counts. Positive collisions always transfer loss to the moving event for these seven interior rows; two later negative collisions transfer loss to the fixed event. In particular the first negative collision is an exact zero-transfer example, while the next two negative collisions are not.

### Endpoint coincidences, not an extrapolation beyond the proven domains

At the **positive** endpoint \`r=1/2507\`, three pairs meet at three *different epsilon phase values*: \`(q,n)=(3,109),(12,436),(15,545)\`. The exact combined loss at those events, respectively, is:

- \`(3,109): 13052609496\`;
- \`(12,436): 141045371248\`;
- \`(15,545): 382755125232\`.

At the **negative** endpoint \`r=-1/4945\`, the \`(q,n)=(12,430)\` combined event has loss \`138152275016\`.

These are values at the boundary itself; comparing across the boundary requires the next affine-minimizer regime. The positive three pairs collide at one perturbation parameter but not at one epsilon phase: their losses must therefore not be aggregated as a single phase event.

## Complete finite proof and reproduction

For each subset mask S (1 through 32767), compute the integral vector
\`P_S=36 sum_(a in S) M_a\`. Its first-zero time is

\`tau_S(eta)=min_{k:P_S[k]<0} 36 (X_k+eta H_k)/(-P_S[k])\`.

On the two certified sign-domains, classify a subset whose first-zero time lies in the closed ray by one of \`F_n,Q_q,epsilon_max\`; label a subset with \`tau_S>epsilon_max\` as \`O\`, safe for all queried epsilon phases. The check on \`r=+/-1/1000000\` yields 1149 distinct labels on either side (1144 fixed, three moving, one endpoint, one beyond-endpoint class). Positive sign subset counts: F=14657,Q=11002,O=6809,E=299. Negative: F=14662,Q=10997,O=6809,E=299. The prior certified affine-minimizer theorem proves each classification remains valid throughout its sign-domain, including endpoint ties.

For a fixed \`r\` and a tested epsilon phase theta, define W(empty)=1 and for each nonempty mask \`S\`:

\`W_theta(S) = 0\` if \`tau_S(eta)<theta\`; otherwise \`W_theta(S)=sum_{a in S} W_theta(S\\{a})\`.

This counts feasible labeled permutations by their last atom; all prefixes must remain nonnegative. The number lost *at* theta equals the result with \`tau>=theta\` permitted minus the result with only \`tau>theta\` permitted. It is an exact integer DP on 32768 masks, never a floating-point simulation.

For every one of the ten interior collision parameters, use rational midpoints between consecutive listed collision parameters in absolute \`r\`, on both sides; evaluate the fixed and moving drops separately. No third phase crosses within such a chamber by the PR #2122 collision exhaustiveness result. The two drops in each row sum to the same count as a second independent internal consistency check. At endpoint collision parameters calculate their combined single-event losses directly using equality of F and Q; do not extrapolate the sign-chamber beyond its proven boundary.

\`VERIFY_ALL_COLLISIONS.py\` is self-contained, using Python standard-library \`fractions.Fraction\`, transcribed original X and exact atom coefficients from [original frozen source](https://github.com/awdawmip/enterprise-math/blob/435e77af0d180eac32bd1f9c4c464bc4010b7551/research_notes/brc_r5_sharp_nonlocal_fifteen_ray_20261111/VERIFY_R5_SHARP_RAY.py). No imported external checkout script or numerical tolerance. \`EXACT_OUTPUT.txt\` records the verified execution of the equivalent locally transcribed rational algorithm. The ten original model-bytes Phase-1/phase-positive first-collision counts match PR #2122, providing an additional regression check. This calculation verifies all 32767 nonempty subset thresholds and exact integer DP for each of the specified finite event chambers; its uniform open-chamber extension uses the separately proved PR #2122 affine-minimizer and collision spectrum.

## Next exact question

Determine the next prefix-affine envelope past \`r=+1/2507\` and \`r=-1/4945\`, beginning with the two known witness masks (11236 and 14357). Compute their first new active affine forms and the first new collision parameters; preserve the frozen scientific inputs and the complete observer. This is the smallest unfinished step toward full parameter-space phase classification.
