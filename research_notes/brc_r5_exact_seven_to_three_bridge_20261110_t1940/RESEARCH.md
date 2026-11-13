# R5 — A lawful exact 7-to-3 bridge with a support cliff and tapered exclusion tubes

**Date:** 2026-11-10 Asia/Shanghai. **Status:** author-side exact mathematical derivation; standalone Fraction checker executed; the full composite verifier below incorporates prior exact checks but is *not* claimed byte-identically executed in this turn. Independent review and formal Source Result pending.

## Model and frozen inputs

The unchanged seven-likelihood-ratio P/Q–BRC statistical Blackwell transport problem has 30 admissible nonnegative arcs, 21 original marginal/martingale equations, five affine physical equalities and 26 affine nonnegative capacity slacks. The fixed scientific source pins are GLOBAL a01383f825ef9d43b4b754254303298c64041568 and EM 86149263e38c22292c9def1e0f69092efa1be77e. Statistical likelihood-ratio labels are *not* P000 native spatial axes.

The complete closed, lawful, five-vertex, two-dimensional 7-edge polygon P7 and its strict whole-polygon forcing duals are from PR #1976 at b9d0da58b74a18fe45f4b29bb238b70df79b96bc. The global lawful 3-edge minimizer family is from PR #1945 at 47f7b275401d6eca7ea4293dde93aa75505ae50f. The prior RHS uniform exclusion radius R_q is from PR #1982 at d78d5bcbb1d8d038d59740b3231a4fd2559050ee. The eight-dimensional physical dual radius R_z and fixed 15x8 Jacobian T are from PR #1986 at 590b50e71a58632b02c5fb930f9a5c8b1c1219f5. These are immutable author-side predecessor sources, not independently accepted Results.

## New theorem: exact minimum support on an entire lawful join

For any source–target pair p7 in the closed polygon P7, choose its seven-positive coupling E7 with constant support

    S7 = {(0,0), (3,3), (4,3), (4,5), (6,5), (6,6), (0,3)}.

For every v in [1/10,13/40], set x3(v)=(1,1,1,27/80,v,27/80,1/10) and p3(v)=(x3(v),x3(v)). Let

    s(v) = 7933/36000 + (67/162)(v-1/10).

The unique three-positive coupling E3(v) uses (0,0), (3,3), (6,6) with respective masses s(v), 1-2s(v), s(v); these stay positive throughout the interval.

For any real 0<=t<=1, interpolate physical parameters and *labeled* coupling masses:

    p_t = (1-t)p7 + t p3(v),   E_t = (1-t)E7 + t E3(v).

**Theorem.** Every p_t meets the original physical constraints, and E_t solves all 21 original Blackwell equations. Among *all* 30-arc nonnegative couplings for p_t,

    N_min(p_t)=7    if 0<=t<1,
    N_min(p_t)=3    if t=1.

In particular the lawful bridge passes from an entire seven-edge polygon to an entire three-edge minimizer segment without attaining a minimum of 4, 5 or 6 at an interior bridge parameter. No claim is made about transverse paths or low-support strata elsewhere in the model.

### Proof

(1) Both endpoints are physically lawful, all five physical equalities and all 26 capacity slacks are affine, and all seven physical source/target masses are affine in the physical parameters. Thus their convex interpolation is lawful. The 21 marginal/martingale equations are linear in the labeled coupling weights and source/target masses, hence E_t solves them. The terminal three diagonal edges are a subset of S7; every weight of E7 is positive over P7. Therefore all seven coefficients of E_t are strictly positive for t<1, proving N_min <=7.

(2) Use the exact equivalent 15-row rescaling of the original 21 equations: retained original rows (0,1,2,3,4,5,6,7,8,9,10,12,15,16,17), with rows >=14 multiplied by 20, and call its matrix C, RHS q. From PR #1976 take the rational dual y_f for each forced f in

    F6={(0,0),(3,3),(4,3),(4,5),(6,5),(6,6)}.

All 30 column inequalities y_f^T C_e <= indicator(e=f) were previously checked and are checked again by the composite verifier. At every p7 in P7 all six y_f^T q(p7)>0. Their values on the three diagonal *columns*, in the S3 order ((0,0),(3,3),(6,6)), are exactly

    f=(0,0):  (1,0,0)
    f=(3,3):  (0,1,0)
    f=(4,3):  (0,0,0)
    f=(4,5):  (0,0,0)
    f=(6,5):  (0,0,0)
    f=(6,6):  (0,0,1).

Consequently y_f^T q(p3(v)) is respectively s(v), 1-2s(v), 0, 0, 0, s(v), all nonnegative, for *every* terminal v. By linearity y_f^T q(p_t)>0 for t<1. For any nonnegative solution e of Ce=q(p_t), the all-column inequalities imply e_f >= y_f^T q(p_t)>0, forcing six distinct edges.

(3) Reuse the exact sparse annihilator ell with entries ell_3=-5/23, ell_10=25/23, ell_14=-1/23 (zero based). All ell^T C_f vanish on F6; ell^T C_(0,3)=1; ell^T C also vanishes on each terminal diagonal edge. Therefore ell^T q(p3(v))=0, while ell^T q(p7)=E7_(0,3)>0 everywhere on P7. Hence ell^T q(p_t)=(1-t)E7_(0,3)>0 for t<1. A solution with only the six forced edges would have ell^T Ce=0, contradiction. The 7-edge E_t attains the lower bound. At t=1, three positive source columns require at least three arcs and E3 attains three. QED.

## Further new corollary: linearly tapering quantitative stability cones

The predecessor uniform 15D RHS exclusion radius and direct physical-parameter radius are

    R_q = 2502770274125 / 3676504873334904,
    R_z = 254087337130964128905 / 142439520168704998753514.

For *every* bridge point with 0<=t<1, every **feasible** right-hand side q' satisfying

    ||q'-q(p_t)||_infinity < (1-t)R_q

requires at least 7 nonzero transfer weights among all 30 allowed arcs. Also, with the *same fixed* 15x8 physical-direction Jacobian T from PR #1986, every feasible q'=q(p_t)+T delta with ||delta||_infinity < (1-t)R_z requires at least seven. In particular this applies to lawful physical perturbations in those directions.

**Proof.** On the join, each of the six forcing margins and the seventh ell margin is at least (1-t) times its certified positive uniform P7 minimum; the terminal evaluations are nonnegative. Apply the same seven predecessor L1-Linfinity dual perturbation estimates after multiplying their exact positive bounds by (1-t). The radii are sufficient bounds, not proved nearest physical 6-edge contact distances.

## Validation and research typing

VERIFY_BRIDGE.py includes the exact immutable predecessor seven-edge and five-vertex checker, followed by a new symbolic/rational bridge extension verifying both physical endpoints, original 21-equation transport, 30-column forcing inequalities, the complete 6-by-3 diagonal dual table, ell, and an exact 1/2 midpoint. That integrated source is provided for future full rerun; this turn's EXACT_OUTPUT.txt records an independently *executed* fresh standalone Fraction implementation of those new endpoint/table/midpoint tests, not a claim of byte-identical execution of the published composite script. The original five-vertex enumeration and physical norm calculation are reused, not independently rerun in this turn.

**BRC resolution:** REUSE_APPLIED to typed positive rational labeled support, dual forced edges and exact annihilator; COMPOSE_APPLIED to whole-polygon lower bounds, three-edge global minimizer and affine physical feasibility. This statistical observer result keeps edge provenance, multiplicity and positive weight typing, does not introduce signed-amplitude cancellation, native-X6 displacement, heartbeat time or a new Foundation theorem.

**Remaining question:** classify *transverse* 4/5/6-edge strata and tangent-cone entry at t=1, using exact physical capacities and new forcing/annihilator certificates. Independently replicate predecessor P7 five-vertex bounds before formal admission. Native R5 task lookups in this execution returned NO_CURRENT_IMMUTABLE_PUBLICATION; no shared R5 CLAIM, independent review or Source Result is asserted.
