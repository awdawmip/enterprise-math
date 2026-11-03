# BRC N=4/S23: sharp complete-bank coefficient 21 and local adversarial noise minimax

Date: 2026-11-03. Evidence: AUTHOR_ANALYTIC_PROOF / EXACT_FRACTION_EXECUTED / UNREVIEWED / NOT_ADMITTED. Frozen scientific input: awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34. Parent author-side source: 23f69f9608e47b60a287d68b752ad642b5805add, research_notes/brc_n4_s23_nine_feature_noisy_inverse_20261103_research1/PROOF.md.

## Definitions, scope and precise result

Let z=(z_0,...,z_10) range over the real cube [0,1]^11 and let x=(z_2,...,z_10). Each of six sources follows the four-outcome stopping distribution

\[
R(p,q,r)=\bigl(p,(1-p)q,(1-p)(1-q)r,(1-p)(1-q)(1-r)\bigr).
\]

The source-index triples are A=(0,0,0,1,1,1), B=(2,2,3,2,2,4), C=(5,6,7,8,9,10). Preserve the labeled mixture M/20, where

\[
M=\begin{pmatrix}
10&10&0&0&0&0\\
9&11&0&0&0&0\\
0&0&20&0&0&0\\
0&0&0&10&10&0\\
0&0&0&2&18&0\\
0&0&0&0&0&20
\end{pmatrix}.
\]

Use one of four overwrite mask pairs F=(3,31),(7,27),(11,23),(15,19), where N denotes the mask omitting bit 2, E denotes the mask including bit 2, and both masks replace their selected first-five coordinates by beta_N=beta_E=0. Do not include the unaltered original observation. Remove the same source row j in both views and retain every four-outcome probability in the other five rows of both views. Supplement exactly the predecessor's minimal scalar repair: E-outcome-2 at missing j for j in {0,1,3,4}, or U_g-outcome-1 and V_g-outcome-2 at missing j=2 (g=3) or j=5 (g=4); U_g is the view retaining gate g and V_g the view replacing it.

The full tagged event bank B_{F,j} has 41 scalar coordinates for j in {0,1,3,4}, or 42 for j in {2,5}. Tags identify view, original source row and outcome. Let

\[
D_{\rm full}(z,w)=\max_{b\in B_{F,j}}|b(z)-b(w)|.
\]

**Theorem 1.** For all 24 masks/deleted-row combinations and all real z,w in the cube,

\[
\boxed{\|x(z)-x(w)\|_\infty\le21D_{\rm full}(z,w).}
\]

This coefficient is globally sharp separately for every instrument:

\[
\boxed{\sup_{x(z)\ne x(w)}\frac{\|x(z)-x(w)\|_\infty}{D_{\rm full}(z,w)}=21.}
\]

**Upper proof.** The already established nine-coordinate sub-observer y from the complete bank has exact identities at these zero overwrite settings:

\[
\begin{split}
&(y_0,y_1,y_2,y_3,y_4)=(z_2,z_3,z_4,z_7,z_{10}),\\
&y_5=(z_5+z_6)/2,\quad y_6=(9z_5+11z_6)/20,\\
&y_7=(z_8+z_9)/2,\quad y_8=(z_8+9z_9)/10.
\end{split}
\]

Every selected event y_i is either retained or exactly supplied by the declared repair; therefore \|\Delta y\|_\infty\le D_{\rm full}. Reconstruct the coupled coordinates by

\[
\begin{split}
z_5=11y_5-10y_6,\quad&z_6=-9y_5+10y_6,\\
z_8=(9y_7-5y_8)/4,\quad&z_9=(-y_7+5y_8)/4.
\end{split}
\]

The inverse linear map has maximum absolute row sum 21, with other row sums 19, 7/2, 3/2 and 1. Hence the claimed bound holds globally even on all boundary faces.

**Uniform sharpness witness.** Fix any real h with 0<h<=1/42. Let z^+ and z^- both have z_2=0, and have every other coordinate equal to 1/2 except

\[
z_5^\pm=\tfrac12\pm21h,\qquad z_6^\pm=\tfrac12\mp19h.
\]

Their x-vectors differ by 42h. In the two first-source mixture rows, the two outcome-2 differences are respectively +2h and -2h; outcome-3 differences are their negatives; outcomes 0/1 do not differ. This follows exactly from (z_5+z_6)/2 and (9z_5+11z_6)/20. Both views replace z_0,z_1 by 0 and the N-view reads z_2=0 while the E-view overwrites z_2 by 0. Thus both views in those two rows have R=(0,0,r,1-r). All remaining source rows and their repairs are identical between states. Removing any one row and adding the mandated repair still yields D_full=2h. Thus the bound ratio is (42h)/(2h)=21 for all masks and deletions. QED.

**Theorem 2 (exact small-noise minimax).** For all these instruments and any 0<=eta<=1/42, with arbitrary scalar observations Y satisfying \|Y-B_{F,j}(z)\|_\infty<=eta, the best worst-case reconstruction risk for target x is exactly

\[
\boxed{\inf_T\sup_{z\in[0,1]^{11}}\sup_{\|Y-B_{F,j}(z)\|_\infty\le\eta}\|T(Y)-x(z)\|_\infty=21\eta.}
\]

**Upper proof:** select the nine events of the previous inverse, apply that inverse to the noisy Y, and use the inverse row-sum norm 21. **Lower proof:** the sharpness pair with h=eta has target separation 42eta and complete bank separation 2eta. The midpoint Y of the two complete banks is within eta of both; the triangle inequality forces any estimator to incur error >=21eta on one state. The midpoint is itself the exact bank of the intermediate cube state because this witness family has linear readout, so the lower bound also holds with coherent measured probability rows. At eta=0 the formula holds trivially. QED.

## Actual calculation, research meaning, limitations

VERIFY.py implements all original six tagged source laws, the two overwrite operators, the complete repaired bank, the selected linear inverse, and rational extremal states with Python fractions.Fraction. It ran exact reconstruction/bound checks for 960 rational state pairs and 72 adversarial sharp/noise pairs across all 24 mask/delete combinations; output captured in RUN_EVIDENCE.json. The algebra above establishes the all-real conclusions; finite tests independently check implementation and selected rational cases.

Under zero/zero overwrite and this bank's per-event supremum metric, retaining all available event probabilities cannot beat the nine-event inverse coefficient 21 or the small-noise risk 21eta. At unequal overwrite constants the N view may contribute new constraints; this is the next exact research question. The original frozen ten-label bank minimax interval [1/2,2/3] remains a separate open mother problem. P000's six native spatial axes and independently typed time remain unchanged: the result is a precisely typed BRC statistical observer calculation, not a physical-time evolution claim.
