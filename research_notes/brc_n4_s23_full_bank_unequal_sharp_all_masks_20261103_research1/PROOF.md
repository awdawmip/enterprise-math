# BRC N=4/S23: sharp complete-bank inverse for all unequal overwrite constants

Date 2026-11-03. Author analytical proof, exact Fraction tests; UNREVIEWED / NOT_ADMITTED.
Frozen scientific source: awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34.
Predecessor: PR #1765@1e9f620fd25f93713ffb2611cce94ca7017e2d14, full-bank beta_N=beta_E=0 theorem and nine-feature inverse.

## Population, observation, target

State z=(z_0,...,z_10) belongs to [0,1]^11; recover x=(z_2,...,z_10).
Each of six sources follows the four-outcome stopping law
R(p,q,r)=(p,(1-p)q,(1-p)(1-q)r,(1-p)(1-q)(1-r)).
Source index triples are A=(0,0,0,1,1,1), B=(2,2,3,2,2,4), C=(5,6,7,8,9,10).
Labeled prepared-source mixing is M/20 where
M=[[10,10,0,0,0,0],[9,11,0,0,0,0],[0,0,20,0,0,0],[0,0,0,10,10,0],[0,0,0,2,18,0],[0,0,0,0,0,20]].

Choose F in {(3,31),(7,27),(11,23),(15,19)}; N denotes the mask without bit 2, E the mask with bit 2. The two views overwrite their indicated indices among 0,...,4 by beta_N and beta_E in [0,1), respectively. No original observation. Delete one common source row j from both views. Keep all four outcomes of every other row, and add the previous minimal scalar repair: E-row-j outcome 2 for j=0,1,3,4; for j=2 or 5 add U_g-row-j outcome 1 and V_g-row-j outcome 2, where g=3 or 4, U_g leaves that gate original and V_g overwrites it. This leaves 41 or 42 distinguishable tagged real event probabilities. D_full is the maximum absolute coordinate difference across all these events. All assertions have this fixed two-view/future-operation horizon and preserve provenance.

## Exact global theorem

Let a=1-beta_N>0 and b=1-beta_E>0. For every deleted row j and all z,w in the complete real cube:

||x(z)-x(w)||_infinity <= C_F D_full(z,w),

with sharp (least possible) coefficient

C_(3,31) = max(21/b^2, 1/a);
C_(7,27) = C_(11,23) = C_(15,19) = max(21/b^2, 1/a^2).

Thus using the complete 41/42 scalar bank never improves the sharp global inverse coefficient of the nine selected event readings, even for unequal, nonzero overwrite constants. In the requested (3,31), deleted row 0, beta_N=9/10 and beta_E=0 case, the exact answer is C=21. This is scoped to this max-coordinate event metric; it is not observer redundancy for all later operations, sampling models or correlations.

## Proof

UPPER: The nine-feature decoder from the predecessor consists of actual coordinates of this same complete, repaired bank. Its exact globally linear inverse has infinity operator norm max(21/b^2,1/a) for (3,31), or max(21/b^2,1/a^2) otherwise. Since the nine-coordinate supremum is at most D_full, these are upper bounds for the complete bank over the full cube.

SHARPNESS WITNESS A (21/b^2): Take 0<h<=1/42, set z_2=w_2=1, all other coordinates 1/2 except z_5=1/2+21h, w_5=1/2-21h, z_6=1/2-19h, w_6=1/2+19h. The target separation is 42h. Both first two N-view source groups have their r branch blocked by the original gate z_2=1, so their entire N output does not change. In E, p and q are overwritten by beta_E, leaving branch multiplier b^2. Source mixtures (z_5+z_6)/2 and (9z_5+11z_6)/20 change by +2h and -2h. Thus E outcomes 2/3 of rows 0/1 each change in absolute value 2b^2h; all other source rows and repair readings are unchanged. If row 0 or 1 is removed, the missing E outcome-2 repair still supplies the requisite difference. Therefore D_full=2b^2h and the ratio is 21/b^2 simultaneously for all 24 instruments. This source-boundary witness is the key extension beyond the beta=0 predecessor: at z_2=1, additional N data cannot resolve the E mixture's near-kernel.

SHARPNESS WITNESS B (1/a): Keep all except z_2 fixed, vary z_2 by 2h in the cube. E overwrites z_2 and is unchanged. In N, every potentially affected source has first-stage survival factor a; event 1 changes by 2ah, event 2 and 3 by at most 2ah. At least one of source rows 0/1 remains after deleting one row, hence D_full=2ah and the target difference is 2h. This realizes 1/a in every mask.

SHARPNESS WITNESS C (1/a^2): For each of the three other masks there is a downstream gate g in {3,4} overwritten by N but retained in E. Hold z_g=w_g=1 and vary only z_7 if g=3 or z_10 if g=4 by 2h. E's third branch is blocked by its original gate, while N's third-stage factor is a^2. Precisely source row 2 or 5, respectively, changes its event-2/3 probabilities by 2a^2h. If this row was removed, its mandated V_g=N event-2 repair retains the same difference. No other row changes. The global event distance is 2a^2h, giving inverse ratio 1/a^2. The maximum of the necessary witness ratios equals the preceding upper bound, proving sharpness over all real states. QED.

## Exact small-error minimax

For arbitrary coordinatewise event noise at most eta and all estimators T, write C=C_F. For 0<=eta<=1/(2C),

inf_T sup_z sup_{||Y-B(z)||_infinity<=eta} ||T(Y)-x(z)||_infinity = C eta.

Upper bound: nine-feature linear inverse, with row-sum norm C. Lower: scale whichever symmetric witness A/B/C has ratio C until its bank separation is 2eta and target separation 2Ceta. The displayed eta range places both endpoints in [0,1]^11. Along each witness the full bank is affine in the changing parameter(s), holding each stop gate used in a coefficient fixed. Therefore the arithmetic midpoint of the two complete banks equals the complete bank of the midpoint state, a coherent four-outcome probability reading, and lies at distance eta from both witnesses. Any estimator incurs target error at least Ceta on one of them. The result includes eta=0 by exact reconstruction. QED.

## Exact verification, BRC and authority scope

VERIFY.py uses standard-library fractions.Fraction for all original source stopping laws, all four mixing rows/pairs, all intervention masks, deleted rows and actual repair events. It executed 1152 rational state-pair reconstruction and global bound checks, 396 exact sharpness witnesses with coherent-midpoint assertions, and 144 max-coefficient mode checks over four masks, six deleted rows and six rational beta pairs. The analytic proofs, not these samples, establish the continuum claims.

BRC retention: serial branch probabilities, six original source labels, prepared row mixtures, view and outcome tags, repair provenance and the future-operation scope are preserved. The nine-feature inverse certifies a sharp recovery bound only for the nine-dimensional target under this event metric, not erasure of other BRC data. P000 X6, six primitive spatial axes and independently typed Heartbeat time are unchanged; this is an explicitly typed statistical observer calculation, not a physical-time experiment. Native Owner/CLAIM remains unconfirmed (CONTROL_QUOTA, static read-only Site); GitHub authorship is not independent mathematical admission.
