# R5 next smallest unit — lower-ratio off-diagonal corner and dual certificate

Date 2026-11-08 Asia/Shanghai. Current author-side mathematical frontier is LOW_RATIO_WEDGE.md in this directory; RATIO_BRIDGE.md solves full saturated-v physical capacity rectangles for 1/2<=b/a<=1. The new LOW_RATIO_WEDGE.md solves the entire capacity **diagonal** u/u_max=w/w_max for 1/4<=b/a<=1/2, including all 0<=g,s<=1 (s<=g), z∈[0,s/10] and source-target interpolations. Frozen science pins are global a01383f825ef9d43b4b754254303298c64041568 and EM 86149263e38c22292c9def1e0f69092efa1be77e.

Two eta=1/4 exact rational seedless targets and full seven-by-seven calibrated matrices at diagonal corners (p,q)=(0,0) and (1,1) are in ETA_QUARTER_CORNERS.json. Original exact Fraction checker and 729 new exact cases passed in VERIFY_LOW_RATIO.py / EXACT_LOW_RATIO_OUTPUT.txt. The all-real theorem is by affine common-face interpolation, not grid extrapolation.

**Smallest unfinished discriminating input**: test the eta=1/4, g=a=1, b=1/4, v=9/160, z=0 source for off-diagonal corners:
A=(1,1,1/4,0,9/160,9/64,0) (p=0,q=1);
B=(1,1,1/4,21/64,9/160,0,0) (p=1,q=0).
The prior SciPy/HiGHS numerical linear program with seedless target constrained to F={z=a/10, v-z=9b/40} found no solution for A or B. This is not a mathematical impossibility proof.

Rebuild each finite affine-face linear program over exact rational coefficients, with five target variables (g,a,b,u,w), 49 nonnegative Q entries, seven row/7 Q column/7 P-weighted column constraints, equal stopping times, and physical flow inequalities. Either:
(1) produce a rational Farkas certificate proving exact infeasibility **only within this particular F**, or
(2) produce an exact rational feasible Q and y, revising the preliminary numerical signal.
If (1), independently search other seedless affine faces or the original quadratic seedless manifold; do not expand a fixed-face no-go into a universal negative.

The mother R5 question remains full FULL_HIST versus seedless LR pointwise four-observer image equality. Native Owner / formal CLAIM unresolved: observed BACKEND_IDENTITY_OR_VERSION_MISMATCH, STATUS_DATABASE_UNAVAILABLE, operation_sent=false and Site research_authority_granted=false. All branch materials are author-side pending independent review/admission.
