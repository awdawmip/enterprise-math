# EC49FTS — validation evidence and continuation

**Date:** 2026-11-19. **Unit:** external prior-level analysis for native BRC16943-derived price optimizer (scientific pin fc0f038e7bfd12c886b4d37f900bfb770c0f61ab).

Locally executed exact rational verifier in Python 3 using only standard-library fractions.Fraction and json. Exit status: **0**. Reproduced numerator and denominator of the all-box clipping probability, both exact conditional CDF values, their positive rational difference, and five strict TP2 cross minors. Separately used symbolic rational integration to derive and crosscheck the closed-form masses. No native Bellman 228-observer rerun and no independent formal theorem review were performed.

Reproduction command, from the directory containing the submitted script:

    python EC49FTS_PRIOR_SCORE_RIDGE_VERIFY.py

Expected exact outputs: clip probability 66463162673/147612931200, CDF at m=23 equals 142919525557120/375702410965173, CDF at m=93/4 equals 257409057608064/2434591469005301, CDF difference equals 251241454128026688021270338048/914681884620533840389663382073, strict TP2 minors checked 5.

**New mathematics:** (1) exact prior-coordinate change and prior-score formula for the mixed top-atom ratio; (2) coordinatewise decreasing joint priors force strict increase of the atom/continuous ratio; (3) any positive decreasing logconcave nonlinear sum-ridge prior h(a,b)=rho(a+b) has TP2 conditional kernel and strict first-order stochastic increase on high-gap interval; (4) the correlated exact polynomial prior h=(3-a-b)^2 yields the stated all-box clipping probability. The continuous theorem uses analytic monotonicity, not the finite regression.

**Inherited parents:** native optimum EC49FTH PR #2774@999bf1069403306b3813e0e390dae4435d7b4b8c; mixed TP2 theorem EC49FTR PR #2795@6e6da57541f965b0c02c27ceed97daddff2e1417. These are author-proved/NOT_REVIEWED. No formal native CLAIM/Result/Review or Activity is claimed here.

**Open frontier:** classify non-coordinate-monotone joint priors with positive prior-score balance, ideally sharp parameter boundaries; preserve independent native Bellman low-z extension. Do not repeat the parent 228-query search solely to validate this external price model.
