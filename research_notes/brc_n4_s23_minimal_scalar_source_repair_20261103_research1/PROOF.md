# BRC N=4 / S23 — minimal scalar restoration of any missing source label

Date: 2026-11-03. Status: AUTHOR_ANALYTIC_PROOF / EXACT_RATIONAL_EXECUTED / UNREVIEWED / NOT_ADMITTED. Frozen science: `43ec6098b1330ae86d0a7863be336c5d97f6ef34`. Predecessor: PR #1765, `dfcef016a6c64662e1b55cca302f1ef80c3ae733`, one-source-label deletion fiber theorem.

## Model and exact scope

For `z in [0,1]^11`, six latent sources use `A=(0,0,0,1,1,1)`, `B=(2,2,3,2,2,4)`, `C=(5,6,7,8,9,10)`; their four-outcome stopping law is
`R(p,q,r)=(p,(1-p)q,(1-p)(1-q)r,(1-p)(1-q)(1-r))`.
The prepared row `P_j` mixes these source laws by `M/20`, where
```
M = [ [10,10,0,0,0,0], [9,11,0,0,0,0], [0,0,20,0,0,0],
      [0,0,0,10,10,0], [0,0,0,2,18,0], [0,0,0,0,0,20] ].
```
The two constant-overwrite views are one of `(3,31),(7,27),(11,23),(15,19)` as five-bit masks. Call the mask omitting bit 2 `N` and the mask covering bit 2 `E`; constants `beta_N,beta_E` are independently known elements of `[0,1)`. Both overwrite original coordinates `z0,z1`. The reduced observer records both four-outcome distributions for each labeled row other than a fixed deleted `j`, without an original-state observation. Its previous exact fiber classification is assumed at its **stated scope**. Coordinates `z0,z1` are always unidentifiable; the objective here is the other nine coordinates, `z2,...,z10`.

## Theorem A: minimum additional continuous scalar readouts

**For every real `beta_N,beta_E<1` and each of the four pairs, global recovery of the nine coordinates is restored by exactly ONE additional real scalar if `j=0,1,3,4`, or exactly TWO if `j=2,5`. These counts are minimal among continuous real-valued measurements on the deleted-row source preparations, with arbitrary postprocessing of the retained observer.**

Write `P^v_{j,t}` for outcome index `t=0,1,2,3` in view `v=N,E`. A sufficient minimal instrumentation is:
* For `j=0,1,3,4`: add the single `P^E_{j,2}`.
* For `j=2` (respectively `j=5`), let `g=3` (respectively `g=4`), `U` be the unique view **not** overwriting `g`, and `V` the view overwriting `g`. Add `P^U_{j,1}` and `P^V_{j,2}`.

These are labeled stopping-event probabilities; the six original source identities, four time labels, and fixed preparation matrix are retained in the experimental definition. No native X6 dynamics is asserted.

### Constructive inverse

In view E, the middle gate `z2` is overwritten by `beta_E`. Put `k=(1-beta_E)^2>0`. The third-outcome probabilities of paired rows satisfy
```
P^E_{0,2}=k t0, t0=(z5+z6)/2
P^E_{1,2}=k t1, t1=(9z5+11z6)/20
P^E_{3,2}=k t3, t3=(z8+z9)/2
P^E_{4,2}=k t4, t4=(z8+9z9)/10 .
```
For a deleted paired row, its retained partner already determines the other `t`. The new scalar determines the missing `t`, and exact inversion gives
```
z5 = 11t0-10t1,     z6 = -9t0+10t1
z8 = (9t3-5t4)/4,   z9 = (-t3+5t4)/4 .
```
All other previously identified coordinates stay determined by the retained observer.

For `j=2,5`, the deleted singleton's middle gate is `g=3,4`, downstream coordinate `c=z7,z10`, respectively. In the nonoverwriting view U and overwriting view V,
```
P^U_{j,1}=(1-beta_U) z_g,
P^V_{j,2}=(1-beta_V)^2 c .
```
Both factors are strictly positive, yielding `z_g=P^U_{j,1}/(1-beta_U)` and `c=P^V_{j,2}/(1-beta_V)^2` even at `z_g=1`. This decouples the two lost coordinates on the full closed parameter cube.

### Minimality and boundary scope

The previous exact fiber theorem gives, for `j=0,1,3,4`, a genuine nondegenerate segment for every interior weighted mean (only extreme means 0 or 1 collapse to a point). A zero-scalar extension is constant on such a segment, so one is globally necessary. For `j=2,5`, the reduced fiber contains an entire closed square of independently free `(z_g,c)`. There is no continuous injection from this square into the line: restriction to its boundary circle would give a continuous injection of a circle into a compact interval, impossible since removing an interior image point disconnects the interval, whereas deleting one point from a circle leaves it connected. Thus at least two continuous scalar coordinates are necessary. The explicit construction attains both minima. This is a **global** minimum, not a claim that one is needed at a paired-fiber endpoint.

## Theorem B: sharp inverse stability conditional on the fixed reduced observation

Compare two states with **identical deleted-row observers** (same original remaining-row data for both views); write `Delta` for their hidden nine-coordinate difference and `eta` for the maximum absolute difference in the additional scalar(s). Then
`||Delta||_infty <= C_j eta`, with the following **exact best possible** constants:
```
j    C_j
0    11/(1-beta_E)^2
1    10/(1-beta_E)^2
3    9/[4(1-beta_E)^2]
4    5/[4(1-beta_E)^2]
2,5  max(1/(1-beta_U), 1/(1-beta_V)^2)
```
The numerator constants for paired rows come from the column of the displayed 2x2 inverse associated with the missing mean, with the retained mean held fixed. For singleton rows the repair map is diagonal. Each constant is attained by sufficiently small admissible variations about an interior state within the same reduced fiber: for j=0 use `(Delta z5,Delta z6)=h(11,-9)`, j=1 use `h(-1,1)`, j=3 use `h(9,-1)`, j=4 use `h(-1,1)`. For j=2 or 5 vary only the coordinate corresponding to the larger of the two reciprocal scales. Therefore these are actual sharp fiber-relative inverse constants, not claimed as optimal constants for an observer that includes additional outside measurements or independent measurement-noise on retained rows.

## Theorem C: operation-closed obstruction without a new source measurement

Even an arbitrary finite **adaptive** sequence of views that overwrite any subset of upstream gates `z0,...,z4` by chosen known constants, while deleting the same row `j` every time, cannot globally distinguish the nine-coordinate states. For `j=2,5`, the missing middle/downstream coordinates occur only in the deleted row. For paired `j`, the only surviving row from that pair always depends on its downstream two coordinates through exactly the same retained weighted mean; changing upstream gates does not change its source mixture coefficients. Choose distinct states from the corresponding predecessor fiber, fixing all other coordinates. They yield identical retained distributions for **every** permitted upstream overwrite. By induction the same adaptive choices are made from identical observation histories. The new scalar measurements above break that exact quotient, rather than merely repeating upstream perturbations.

## Evidence and limits

`VERIFY.py` executed locally with standard-library `Fraction`: 4 schemes x 3 rational beta pairs x 6 row deletions = 72 constructed fiber/inverse cases, and 6912 exact upstream-overwrite indistinguishability checks. Execution output is `RUN_EVIDENCE.txt`. The real-domain theorems follow from the analytic proofs; the finite checks only test the formulas and witnesses.

This is a frozen BRC six-latent-source statistical-model result. Retaining source provenance is part of its typing; the result is not a native P000 six-dimensional spatial or heartbeat-time correspondence, and it neither revises the mother ten-decoder minimax interval nor establishes independent review or admission.
