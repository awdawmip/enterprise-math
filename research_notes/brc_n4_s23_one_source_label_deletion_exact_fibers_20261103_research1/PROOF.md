# BRC N=4 / S23 — exact fibers after removing one source-label row

Date: 2026-11-03 Asia/Shanghai. Classification: AUTHOR_ANALYTIC_PROOF / EXACT_RATIONAL_EXECUTED / UNREVIEWED / NOT_ADMITTED.

## Frozen experiment

Frozen scientific pin: awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34. Highest verified predecessor: a0ade50c788dc119e8a43403a2f5d17cf1339046, complete six-row two-overwrite fibers, same PR.

For z in [0,1]^11 let

    A=(0,0,0,1,1,1), B=(2,2,3,2,2,4), C=(5,6,7,8,9,10).
    R(p,q,r)=(p,(1-p)q,(1-p)(1-q)r,(1-p)(1-q)(1-r)).
    M=((10,10,0,0,0,0),(9,11,0,0,0,0),(0,0,20,0,0,0),
       (0,0,0,10,10,0),(0,0,0,2,18,0),(0,0,0,0,0,20)).
    P_j(z)=sum_{i=0}^5 (M[j,i]/20) R(z[A_i],z[B_i],z[C_i]).

The two masks are any of (3,31), (7,27), (11,23), (15,19). For each pair N omits bit 2 and E covers bit 2; each mask covers 0,1 and neither covers indices >=5. For known real beta_N,beta_E in [0,1), a view overwrites each masked coordinate among 0,...,4 by its own beta. Observe the two resulting collections of six labeled, four-outcome distributions, with NO original-state observation. Psi_minus_j deletes the SAME designated row index j from BOTH observed views, retaining all other rows with their labels.

## Complete fiber theorem (universal over all real states and betas in the domain)

For each base z in [0,1]^11, the entire set of w with Psi_minus_j(w)=Psi_minus_j(z) is described by the following table. In every row w0,w1 are arbitrary in [0,1]; every original coordinate not explicitly mentioned in that row is fixed at w_k=z_k.

| Missing row j | Additional exact freedom |
|---|---|
| 0 | (w5,w6) in [0,1]^2 satisfying 9w5+11w6=9z5+11z6 |
| 1 | (w5,w6) in [0,1]^2 satisfying w5+w6=z5+z6 |
| 2 | w3,w7 independently arbitrary in [0,1] |
| 3 | (w8,w9) in [0,1]^2 satisfying w8+9w9=z8+9z9 |
| 4 | (w8,w9) in [0,1]^2 satisfying w8+w9=z8+z9 |
| 5 | w4,w10 independently arbitrary in [0,1] |

Thus the nine-coordinate quotient fiber is a full two-cube for j=2 or 5. For j=0,1,3,4 it is a nondegenerate affine line segment unless the relevant positive-weight mean equals 0 or 1, in which case the segment is a singleton. Consequently complete eleven-coordinate fiber dimensions are 4, or 3/2 at the paired-label interior/endpoint cases, respectively.

**Corollary:** All six labeled rows are necessary for GLOBAL nine-coordinate identification by these two overwritten views: deleting any row yields distinct legal nine-coordinate states with the same reduced observation for every beta_N,beta_E<1. Source-label redundancy must therefore be assessed relative to the declared observation and future-operations scope.

## Analytic proof, including all boundary points

For every source in every overwritten view the first gate is p=beta_v<1, and the middle gate for group g is q_v(g)=beta_v when g is overwritten, otherwise q_v(g)=z_g. Each row from sources 0,1 shares middle gate g=2 and each row from sources 3,4 also shares that gate. The source function R is affine in its downstream r at fixed p,q. Hence the four paired mixed rows are EXACTLY R(beta_v,q_v(2),t_j) with

    t_0=(z5+z6)/2,    t_1=(9z5+11z6)/20,
    t_3=(z8+z9)/2,    t_4=(z8+9z9)/10.

Rows 2 and 5 are individually R(beta_v,q_v(3),z7) and R(beta_v,q_v(4),z10), respectively.

For every middle coordinate g=2,3,4, at least one of the two masks does not overwrite g. In a retained row involving g in such a view, its second event is (1-beta_v)z_g, so z_g can be uniquely recovered. If a pair row (0,1) is missing, the other intact pair (3,4) still recovers z2; if a pair row (3,4) is missing, intact pair (0,1) recovers z2. If row 2 is missing, g=3 occurs in no remaining row, and if row 5 is missing, g=4 occurs in no remaining row. These middle gates are exactly the free coordinates claimed.

For downstream recovery, view E covers z2, so q_E(2)=beta_E<1. Its third outcome for any retained paired row equals (1-beta_E)^2 t_j, determining that row's downstream mean even at every original z2 boundary point. Both mixing rows survive in an intact pair, and the coefficient vectors (1,1),(9,11), respectively (1,1),(1,9), are linearly independent. Therefore both members of an intact pair are uniquely recovered; a pair with one missing row retains exactly the sole stated weighted-mean constraint. If singleton row 2 survives, the mask that covers g=3 gives a view with q=beta_v<1, so its third event recovers z7; similarly singleton row 5 recovers z10 through a view covering g=4. When a singleton row is removed, its unique middle and downstream coordinates occur nowhere in the reduced view.

Conversely every retained observed row is given by one of the formulas above. Any w satisfying the listed coordinate equalities and retained weighted means leaves all its rows exactly unchanged in both views. These equalities are therefore simultaneously necessary and sufficient. A positive-weight two-variable mean in [0,1] has an affine clipped segment as its level set; this is a point precisely at mean 0 or 1. The theorem and dimension claims follow. QED.

## Validation, evidence and interpretation

The separately executed Python standard-library Fraction verifier (VERIFY.py) checks 4 mask pairs x 3 rational beta pairs x all 6 deleted labels, exact indistinguishable witnesses, full-observation distinction, root perturbations, 9-coordinate off-fiber probes, further affine perturbations and extreme weighted-mean boundaries. RUN_EVIDENCE.json records its actual execution: 896 assertion groups, zero false positives. Finite tests support reproducibility; the analytic argument proves the real-domain universal statement.

The experiment is a frozen six-source stochastic abstraction. Deleting labels here is a *candidate information-loss operation*, not a change to the retained underlying six-source branch/provenance state and not a native X6 or physical time evolution. This author result has no verified native CLAIM/Result or independent mathematical acceptance.

## Follow-up

Construct minimal source-preserving contrast measurements repairing the missing line or two-cube, quantify inverse noise stability, and continue the separate mother S23 ten-decoder minimax objective. The full six-label nine-parameter sharp inverse modulus remains an open quantitative target.
