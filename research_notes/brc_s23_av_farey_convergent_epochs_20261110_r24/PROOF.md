# R24 — exact convergent-error risk epochs through the 7,621st cut

Date: 2026-11-10 (Asia/Shanghai). Scientific input remains **enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34**, S23/AV *auxiliary scalar-circle observer*, historical cut count m=128. Previous overlapping frontiers: PR #1885 (through n=1270) and PR #1891 (through n=1174). This author-side result is unreviewed and does not claim native X6 transfer or formal Task CLAIM.

## Definition and exact statement

For 0 <= j < n put phi_j={j theta}, P_n={phi_j:0<=j<n}. For each of the 128 clockwise historical arcs I between consecutive points of P_128, let M_n(I) be the longest elementary arc remaining after inserting P_n. Define

    R_n = R(128,n-128) = 1 - sum_{I in P_128 historical arcs} M_n(I).

Throughout this note theta is irrational and satisfies the **strict rational enclosure**

    262204504569236716045286 / 10^24 < theta
       < 262204504569236716045287 / 10^24.

For integers n=1270,...,7621, R_n has the exact initial value

    R_1270 = -18559 + 70784 theta,

and the subsequent increments R_n-R_(n-1) are given by the fourteen consecutive ranges in EPOCHS.tsv. In particular, writing

    g = 333 - 1270 theta > 0,  h = 3257 theta - 854 > 0,

we have the following **new finite exact results**:

* n=1271,...,1823: 553 consecutive zero increments.
* n=1824,...,1890 and 1927,...,1987: respectively 67 and 61 consecutive increments g, separated by 36 zeros.
* n=1988,...,3093: 1106 consecutive zero increments.
* n=3094,...,3160 and 3197,...,3257: another 67 and 61 increments g, separated by 36 zeros.
* n=3258,...,4363: another 1106 zero increments.
* n=4364,...,4430 and 4467,...,4527: respectively 67 and 61 increments h, separated by 36 zeros.
* n=4528,...,7620: **3093 consecutive zero increments**, with next strict increase h at n=7621.

Endpoints include the exact identities

    R_1823 = -18559 + 70784 theta,
    R_1987 = R_3093 = 24065 - 91776 theta,
    R_3257 = R_4363 = 66689 - 254336 theta,
    R_4527 = R_7620 = -42623 + 162560 theta,
    R_7621 = -43477 + 165817 theta.

The two positive increments g and h are the absolute errors of consecutive continued-fraction convergents 333/1270 and 854/3257. The certified plateau lengths include 553, 1106, 1106, 3093. These relations are exact observations for the specified observer and window; their possible general continued-fraction block law is the next research question.

## Exact incremental max-gap lemma

Suppose an insertion falls into the historical arc I and splits one current elementary gap G=X+Y into X,Y>0. Let H be the largest unaffected elementary gap in the same historical arc, with H=0 if none exists. Then

    R_(n+1)-R_n = max(G,H) - max(X,Y,H).

All other historical arcs have unchanged maxima. Thus the increment is a nonnegative affine expression A+B theta whenever the phase order and comparison types are constant.

## Uniform exact verification over the ENTIRE open interval

VERIFY_R24.py is a standalone Python-standard-library rational verifier; all reported comparisons use integer-affine pairs (A,B), representing A+B theta, and evaluate exact signs at **both enclosure endpoints**. No floating-point theta or rounded equality test is used. The rational midpoint is used only to select a candidate phase ordering. The verifier:

1. checks that floor(j theta) is the same at both endpoints for every visited j;
2. checks every historical arc and every new split gap is strictly positive at both endpoints, so the circular order and each insertion location are valid for every theta in the enclosure;
3. checks each selected historical maximum dominates every other elementary gap at both endpoints, so its identity remains valid throughout the enclosure;
4. applies the exact max-gap lemma to all 6,351 updates n=1271,...,7621, testing nonnegativity and comparing each consecutive increment against the complete 14-row EPOCHS.tsv certificate;
5. **independently** reconstructs a complete sorted P_n and calculates 1 - sum_I M_n(I) at 35 designated endpoints plus 96 fixed-seed randomly selected points, with overlap removed (131 distinct values);
6. groups the full ordered, source-labelled pre-insertion fibres into 161 maximal runs in which all labels translate by +s, the split destination and gap coefficients are unchanged, and the historical endpoints remain distinct valid historical labels. The generated FIBRE_TEMPLATES.json retains all source labels and split identities.

Each sign is an affine function of theta; endpoint inequalities imply its sign throughout the open rational interval. These finite checks therefore certify the displayed piecewise affine formulas **for every theta in the interval** and every integer n in the specified window; irrationality is the stated observer assumption. The template compression is a certified finite grouping rather than a claimed sublinear event-generation algorithm.

The executed verifier output reports 14,986 strict new-gap checks, 265,157 max domination comparisons, 131 independent full-partition recomputations, 161 complete-fibre source-preserving translation families and the final PASS marker. Proof strength: author-side exact finite certificate plus the exact one-insertion lemma. A separate independent mathematical review is pending.

## Relation to project ontology and source use

This is an auxiliary scalar circular readout with an explicitly limited observer and prediction horizon; all insertion source indices, multiplicities and destination arcs remain available in the verifier. The retained source-labelled fibres follow BRC-style residual provenance rather than erasing them under equal scalar gap values. Neither a native X6 dynamics model nor a physical time calibration is inferred. P000 and the frozen scientific pin remain unchanged.

## Next discriminating unit

Derive a **non-enumerative** rule producing the 67/36/61 growth/tie blocks and the plateau lengths from the continued-fraction denominator transitions (553, 717, 1270, 3257, ...). Prove which historical fibre maxima survive each transition, preserve exact cut labels and future insertion destinations, then compare the new jump generator against these 14 exact epochs. Separately check whether the other S23 shared task has a currently active owner before any formal shared CLAIM.
