# R5 — a direct 8-dimensional forced-edge certificate and 530.63× larger exclusion neighborhood

Date: 2026-11-10 (Asia/Shanghai). Evidence status: author-side exact-rational proof and local execution, independent mathematical review pending.

## Scientific object and original pins

Frozen scientific input snapshots are GLOBAL a01383f825ef9d43b4b754254303298c64041568 and EM 86149263e38c22292c9def1e0f69092efa1be77e. Original seven-likelihood-ratio auxiliary P/Q–BRC Blackwell transport observer: 30 allowed nonnegative edges, 21 original equations, and their exact equivalent 15-row rescaling. This is an auxiliary statistical transport result; all original P000 and native-X6 semantics are unchanged.

Inputs: the five-vertex closed two-dimensional lawful seven-edge sheet from [PR #1976](https://github.com/awdawmip/enterprise-math/pull/1976), commit b9d0da58b74a18fe45f4b29bb238b70df79b96bc, and its six exact dual edge-forcing certificates. Predecessor [PR #1982](https://github.com/awdawmip/enterprise-math/pull/1982), commit d78d5bcbb1d8d038d59740b3231a4fd2559050ee, supplies the seventh sparse annihilator and the previous uniform sufficient radius. Predecessor vertex minima are reused at their established exact scope, and are not claimed to be recomputed here.

## Exact new theorem

Let P7 be the complete closed five-vertex lawful polygon in the original eight-dimensional auxiliary parameterization. Let q(z)=q0+Tz be its 15D rescaled Blackwell RHS. Put

    R_direct = 254087337130964128905/142439520168704998753514
             = 0.001783826123747284...

For every real z in P7 and every real z' with infinity norm |z'-z| < R_direct, any nonnegative solution e to C e = q(z') has at least seven strictly positive edges. In particular, for physically lawful z' with an existing transport, its minimum positive support is at least seven. All six-edge and smaller full-30-edge transports are thereby excluded from this open parameter neighborhood, uniformly over the whole closed P7.

The previous sufficient physical 8D radius was

    R_old = 500554054825/148898447370063612
          = 0.000003361714401097493... .

The exact improvement ratio is

    R_direct / R_old =
    2135036514615518482543260765558/4023588903931094069375068265
      = 530.6298843128736... .

This is the largest uniform positivity radius obtained with the exact seven stated functionals. It is a certified bound; the nearest genuinely feasible six-edge physical point is a separate research question.

## General subspace-aware forced-edge separation lemma

Let C have finite columns indexed by the allowed edges, e>=0 and q(z)=q0+Tz. Let K be any nonempty parameter set. Suppose m-1 distinct forced edge candidates f have functionals y_f with y_f^T C_e <= 1 if e=f and <=0 otherwise, for all allowed columns e. Suppose ell^T C_f=0 for all forced columns f. Define

    beta_f = inf_{z in K} y_f^T q(z) > 0
    beta_ell = inf_{z in K} ell^T q(z) > 0

and assume they are verified lower bounds. Set

    R = min( beta_f / ||T^T y_f||_1 for all f,
             beta_ell / ||T^T ell||_1 )

with a zero denominator interpreted as +infinity. For any z in K and ||z'-z||_infinity < R, any e>=0 solving C e = q(z') has at least m positive entries.

Proof. For every f, |y_f^T T(z'-z)| <= ||T^T y_f||_1 ||z'-z||_infinity < beta_f whenever the norm is nonzero; it is unchanged when zero. Thus y_f^T q(z')>0 and e_f >= y_f^T q(z')>0 by the column inequalities and e>=0. Similarly ell^T q(z')>0. If only those m-1 forced edges were positive, ell^T C e would vanish, contradiction. Hence a further positive edge occurs. QED.

## Explicit complete certificate

Forced support:

    F6 = {(0,0), (3,3), (4,3), (4,5), (6,5), (6,6)}.

Sparse seventh functional, 0-based 15D row indices:

    ell[3]=-5/23, ell[10]=25/23, ell[14]=-1/23; all other ell[i]=0.

For all six forced columns, ell^T C_f = 0; for column (0,3), ell^T C_(0,3)=1. For this actual frozen 15-by-8 physical Jacobian T, the exact physical L1 norms of the seven row functionals and their polygon minima are:

| Edge/function | Uniform beta | Direct physical norm ||T^Ty||1 | Radius |
|---|---|---|---|
| (0,0) | 570031933801575355927/3025154085489542635200 | 2003/2025 | 1710095801404726067781/8976864641830450219712 |
| (3,3) | 9386098186912477/52340117054042400 | 335783/32400 | 253424651046636879/14645767937297932666 |
| (4,3) | 5506094603075/179341701138288 | 281443/43200 | 550609460307500/116839042577461087 |
| (4,5) | 95758167010/1245428480127 | 26371/6000 | 191516334020000/10947731483143039 |
| (6,5) | 239395417525/4981713920508 | 509/416 | 1915163340200/48763315106511 |
| (6,6) | 16939155808730941927/3025154085489542635200 | 1017037/324000 | **254087337130964128905/142439520168704998753514** |
| ell / seventh | 1196977087625/89670850569144 | 13493/9936 | 55060946030750/5601522160784537 |

The binding member is the (6,6) forcing dual. The exact smallest dual margin is attained at one polygon vertex by the verified predecessor, and a sign-selected perturbation reaches zero for that particular functional at R_direct. Therefore this uniform radius is exact for the displayed fixed functional list, rather than for all possible support certificates.

The prior physical estimate first bounded all independent 15D RHS directions, then used ||T||_(infinity->infinity)=405/2. Directly calculating each ||T^T y||1 exploits the actual 8-dimensional physical representation, eliminating that extra worst-direction loss.

## Reproduction

Execute: python VERIFY_PHYSICAL_DUAL_TUBE.py

Requirements: Python, fractions (standard library), SymPy. The script reconstructs the 5 physical equalities, 21 original observation rows, 15D rescaling, all 30 admissible columns and exact T. It verifies the original 405/2 matrix norm, all 30-column inequalities for the six forcing functionals, ell's exact annihilation, the seven physical dual norms, exact comparisons, limiting certificate, and improvement factor. No floating-point tolerance is used in any assertion. The adjacent EXACT_OUTPUT.txt is a real local execution of this identical program. The six vertex margin constants and seventh positive mass are reused from the immutable PR #1976 exact five-vertex computation.

## Frontier and remaining question

1. Construct a lawful path from P7 to the six-edge diagonal family of PR #1945, then solve the earliest candidate support transition with exact linear feasibility.
2. Optimize valid forced-edge duals and annihilators against the physical sensitivity norm to seek stronger bounds and determine whether the current local certificate can be improved.
3. Independently replicate the full five-vertex minima and review the manuscript before project mathematical admission.

Control observation: current native R5 lookup returned NO_CURRENT_IMMUTABLE_PUBLICATION. This is source-side independent research; no R5 CLAIM, official Result or Foundation promotion is asserted. Persist only non-sensitive proof and code; preserve original source pins.
