# R5: exact lawful seven-edge Blackwell instance and complete five-vertex two-dimensional sheet

Date: 2026-11-10 (Asia/Shanghai). Research mode: author-side exact rational proof and local independent verification. **Original frozen scientific input commits remain unchanged:** global `a01383f825ef9d43b4b754254303298c64041568`, Enterprise Math `86149263e38c22292c9def1e0f69092efa1be77e`.

Predecessor: [nine-edge author-side PR #1972](https://github.com/awdawmip/enterprise-math/pull/1972), immutable verification source `b01a5a84669d1bb3cd43d4eaa3c0976da5a67aab`. This document concerns the frozen **seven-likelihood-ratio P/Q–BRC auxiliary statistical Blackwell transport observer** with 30 allowed transfer edges and the original 21 marginal/martingale equations; it makes no new P000/native-time, Shor or physical-residual claim. This is not a global seven-edge lower bound over all legal physical pairs (the separate PR #1945 already constructs globally three-edge legal instances).

## Exact result

**Theorem 1 (legal minimum seven, unique support at the displayed point).** A concrete rational legal physical pair has precisely seven strictly positive Blackwell transfer weights, with support

[
S_7=\{(0,0),(3,3),(4,3),(4,5),(6,5),(6,6),(0,3)\}.
]

Its minimum number of positive edges among **all** admissible 30-edge nonnegative couplings with the same full observed right-hand side is **exactly seven**. The above support is the unique seven-edge support at this point.

The seven-coordinate source and target physical vectors `(g,a,b,u,v,w,z)` are:

```text
SOURCE
188243222214404826834936/188261165596929649956875
188243222214404826834936/188261165596929649956875
188243222214404826834936/188261165596929649956875
635320874973616290567909/1882611655969296499568750
3382124709305907675014711480339/106170260860719669952479570000000
217435298781768720561599/1026879085074161727037500
185740015/21009033552
TARGET
1
1
220096942483365833/294030275273996250
7864884099607268333/23522422021919700000
928115624721059763947477/9212164544517818510000000
2128739147931553331/7840807340639900000
1/10
```

Corresponding ordered edge masses (same order as `S_7`) are exactly:

```text
6791982739304366220543319/33163792360264146636000000
7838808238739414046339481/16581896180132073318000000
5687179445433109/117612110109598500
11374358890866218/147015137636998125
5687179445433109/117612110109598500
13426806402256164506965957/99491377080792439908000000
5687179445433109/423403596394554600
```

Direct substitution gives all five original physical equality constraints, all 26 physical capacity inequalities, and **all 21 unabridged** Blackwell marginal/martingale equations. Every mass above is strictly positive. Zero capacity slack indices (zero based): `[1,4,6,14,15,19,21,23]`.

## Certificate of global minimum support at the fixed point

The 15-row reduced system `C e=q` is an exact row-rescaling/selection of the original 21 equations using the explicit row indices `(0,1,2,3,4,5,6,7,8,9,10,12,15,16,17)`; rows originally numbered at least 14 are multiplied by 20. Its 30 columns retain the original allowed-edge identities.

The six edges

[
F_6=\{(0,0),(3,3),(4,3),(4,5),(6,5),(6,6)\}
]

are individually **forced**: for each one, the verifier provides a 15-entry exact rational dual vector `y_f`, checks `y_f^T C_e <= 1_{e=f}` for *every one* of 30 columns, and checks `y_f^T q>0`. Thus every nonnegative feasible coupling must contain each of these six edges. In particular this is a full-30-edge bound, not a restriction to the constructed support.

Their six columns have rank six, and the exact left annihilator `L_6` satisfies `L_6 q != 0`. No coupling using only these six edges is possible. All **24** other candidate seventh columns are checked by exact augmented ranks in the quotient; exactly `(0,3)` matches `L_6 q`. This proves the claimed minimum and uniqueness of the seven-edge support at the fixed rational instance. All six dual vectors and complete checking loops are embedded in `VERIFY_7.py`.

## Theorem 2 (closed bounded two-dimensional seven-edge polygon)

Hold fixed the same original frozen physical restriction map and the 8D physical perturbation space used by PR #1972. Let `M_7` be the seven selected 15-row columns and `T` the exact 15-by-8 statistical right-hand-side Jacobian. The exact left-annihilator matrix `N_7` obeys

[
\mathrm{rank}(N_7T)=6,
qquad \dim\ker(N_7T)=2.
]

On the complete two-dimensional physical affine fiber `z_7+\ker(N_7T)`, enforce the original **26** capacities plus nonnegativity of all seven selected weights. Exact pairwise rational intersections among the resulting affine halfspaces produce precisely **five** feasible vertices. A separate exact recession-direction check proves the polygon is bounded. There are 231 candidate pairs of nonconstant inequality boundaries in an independently executed verifier.

At all five vertices, each of the seven selected weights is strictly positive. Exact minima (one per edge, in the order in Theorem 1):

```text
(0,0) 570031933801575355927/3025154085489542635200
(3,3) 14170803349658977/52340117054042400
(4,3) 239395417525/4981713920508
(4,5) 95758167010/1245428480127
(6,5) 239395417525/4981713920508
(6,6) 16939155808730941927/3025154085489542635200
(0,3) 1196977087625/89670850569144
```

The six forcing dual lower bounds are **also strictly positive at all five vertices**, as checked by the integrated verifier. Convexity propagates these strict bounds to the entire closed polygon, while the seventh weight remains positive and the seventh column is independent of the six forced columns. Consequently **every** point of this five-vertex polygon has minimum positive support exactly seven; no six-edge point lies in the entire closed seven-edge affine physical fiber.

This is an exact locally two-dimensional stratum with globally bounded closed extent inside the specified 8D auxiliary family. Six-edge examples elsewhere may use different support/observer fibers.

## Construction and verification

Two explicit rational perturbations from PR #1972's nine-edge point suffice to reproduce the center:

1. Within the four-dimensional kernel of the nine-edge support, use coordinates `s8=(63/250,3/125,-3/500,1904037272845196213852040637/24234128183825913403050000000)` to annul edge `(2,2)`; eight other masses remain positive.
2. Within the resulting three-dimensional eight-edge kernel, use `s7=(47/10000,-3/40,3343991687719263127/31363229362559600000)` to annul edge `(5,5)`; seven other masses remain positive.

The combined exact checker `VERIFY_7.py` contains the unchanged immutable [PR #1972 nine-edge verifier](https://github.com/awdawmip/enterprise-math/blob/b01a5a84669d1bb3cd43d4eaa3c0976da5a67aab/research_notes/brc_r5_exact_nine_edge_20261110_t1543/VERIFY_9.py) with a deterministic seven-edge/polygon extension. It uses Python `fractions.Fraction` and SymPy with no floating-point search in acceptance tests.

Independent local reconstruction `VERIFY_STANDALONE.py` (not byte-identical to the composite verifier) was executed with Python/SymPy and yielded `EXACT_OUTPUT.txt`: the complete original 21 equations pass, 26 capacities pass, six strict dual certificates pass all 30 columns, 24 singleton quotient tests yield only `(0,3)`, affine fiber dimension is 2, bounded polygon has exactly five vertices, and every edge mass is uniformly positive on all vertices. Both mathematical constructions and all constants are supplied for independent reproduction. The earlier floating LP was used for **candidate discovery only**, followed by exact rational reconstruction and proof.

## Scope, control and continuation

Status: **author-side exact proof/computation, awaiting independent review and formal Source Result admission**. This work does not modify P000 or existing ownership and does not claim an R5 canonical task when the native control lookup returns `NO_CURRENT_IMMUTABLE_PUBLICATION`. The mathematical result concerns a precise auxiliary statistical model under frozen source pins.

Next independent mathematical unit: find lawful minimal-six support on a different face and construct a precise adjacency/transition certificate linking the seven-edge polygon to a six-edge family, or establish an exact intervening support-switch mechanism. The present bounded polygon has no edge-mass-vanishing six-edge contact on its own support fiber.
