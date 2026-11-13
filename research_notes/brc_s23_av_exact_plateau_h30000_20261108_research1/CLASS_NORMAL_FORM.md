# S23/AV at H=30000: finite unimodular normal form of all adjacent-gap classes

Date: 2026-11-08 Asia/Shanghai. Status: exact finite classification against the complete certified H30000 class table; independent review pending. Frozen scientific input: awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34.

## Finite classification

Put f=(11,60), g=(2,11), w=(79,431). The integer determinant det(f,g)=121-120=1 and w=7*f+g.

In T_30000, sorted by the exact real order of t(v,j)=r*v-j, r=ln(7)/ln(10/7), **all** 78 distinct consecutive displacement vectors are exactly the disjoint union of:

| Family | Integer displacement vectors | Distinct types | Occurrences |
|---|---|---:|---:|
| A | {w} | 1 | 434874286 |
| B | {f-m*w : 1<=m<=58} | 58 | 14946825 |
| C | {f} | 1 | 192721 |
| D | {p*f-w : 2<=p<=7} | 6 | 30246 |
| E | {f-k*g : 1<=k<=5} | 5 | 845 |
| F | {f-6*g} | 1 | 36 |
| G | {2*f-11*g}={(0,-1)} | 1 | 36 |
| H | {(1,j): 0<=j<=4} | 5 | 5 |
| TOTAL | 8 disjoint finite families | 78 | 450045000 |

The local checker VERIFY_CLASS_NORMAL_FORM.py constructs the eight disjoint sets and checks their equality with the 78 different vectors of the complete CLASS_H30000.csv (including each multiplicity); it checks family count totals, det(f,g)=1 and w=7f+g. This finite classification follows from the previously published exhaustive rational-order-certified H30000 stream. It provides a compact normal form of the already certified finite class table, **not** a universal class-generation theorem for arbitrary H.

The unimodular pair f,g and w=7f+g suggest a continued-fraction/lattice-cut mechanism for adjacency, with the exceptional g- and (1,j)-families recording boundary effects in the triangular domain.

## Counterexample to a tentative class-count formula

The tempting extrapolation C_H=floor(H/510)+20 (C_H=number of distinct adjacent displacement classes) matches several large sampled H, but complete integer-key streams gave C_1000=22 and C_2000=24, versus extrapolated 21 and 23. The universal extrapolation is therefore false. These exact finite counterexamples motivate a boundary-aware or piecewise formula.

## Executed check

The checker was run against the very same complete 78-row class CSV published at immutable commit a792f1686bea5370ab77b1ed82353a0a8ebe2a4e, and produced:

    PASS_H30000_EXACT_UNIMODULAR_NORMAL_FORM 30000 450045001 78
    FAMILY_COUNTS 434874286 14946825 192721 30246 845 36 36 5

The CSV and original PROOF.md, C++ enumerator, class witness checker and run evidence remain in the same directory.

## Next

Derive the eight families (or their successor families) without enumerating thresholds at variable H. Target exact formulas for each class's count and maximal left endpoint V,J and minimal endpoint sum S, including the changes at the triangle boundary. Cross-check against H7000/H10000/H20000/H30000 and locate the first H>30000 where n=2455069 fails exact prefix saturation. The model remains the BRC joint-count two-point auxiliary sign observer; mother-model mapping and four-observation minimax delta_4 remain separate.
