# R5: exact full-observer Blackwell equivalence on the low-ratio triangular prism, t ≤ 1/7

Date: 2026-11-08. Research unit: seven-node P/Q-BRC terminal-observer R5. Status: AUTHOR_PROVED / EXACT_FRACTION_EXECUTED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY. This is model-internal finite-support martingale geometry, not a physical X6/BRC–Shor dynamics or native residual claim.

## Provenance and inherited scientific inputs

Predecessor: [PR #1821](https://github.com/awdawmip/enterprise-math/pull/1821), immutable head `edd5391600d24eade7958aeb794f78f0f15caa68`, especially `research_notes/brc_r5_full_box_t1over30_20261108/RESEARCH.md`, `VERIFY.py`, `EXTENSION_T1OVER13.md`. Scientific input pins retained verbatim: GLOBAL_KNOWLEDGE `a01383f825ef9d43b4b754254303298c64041568`, Enterprise Math `86149263e38c22292c9def1e0f69092efa1be77e`. Normative rules read separately at current main; protected P000 and ACTIVE worldview unchanged. Authenticated Task CLAIM and independent admission are not claimed.

We use the same seven likelihood-ratio nodes
[
r=(1/10,1/2,3/4,1,5/4,3/2,19/10)
]
and exactly the physical-flow legality, seven node masses `M_i`, calibrated stopping times `T_P,T_Q` and hinge functions `H_j=∑_i(r_i-r_j)_+M_i` implemented independently in `VERIFY_TRIANGLE.py`; their definitions match the inherited `VERIFY.py`. The Blackwell direction is `H_j(y)≥H_j(x)` at all five interior nodes, with equal probability masses and first LR moment.

## New all-real theorem

Let `x=(g,a,b,u,v,w,z)` be the lawful FULL_HIST family
[
x(t,p,q,θ,κ)=
(1,t,1,(13t/40+1/80)p,;9κ/40+tθ/10,;
(3t/40+21/80)q,;tθ/10).
]
For **every real tuple**
[
oxed{0le tle1/7,quad 0le ple qle1,quad 0leθ,κle1}
]
there exists a lawful seedless LR flow `y` and a nonnegative seven-by-seven declaration-independent martingale/Blackwell transport `E` with
[
sum_j E_{ij}=M_i(y),qquad
sum_i E_{ij}=M_j(x),qquad
sum_i r_i E_{ij}=r_jM_j(x),
quad i,j=0,ldots,6,
]
and `T_P(y)=T_P(x), T_Q(y)=T_Q(x)`. Consequently the four terminal observables `(e_P,e_Q,T_P,T_Q)` are preserved for every randomized seven-node terminal declaration. The result covers irrational inputs and all triangular boundary faces.

Relative to the full-physical-prism theorem `t≤1/13` in PR #1821, the **entire triangle `p≤q`** now reaches `t=1/7` while retaining independent full ranges of θ and κ.

## Explicit triangular G/F seam and full proof

Write the triangular barycentric weights
[
eta_{00}=1-q,qquadeta_{01}=q-p,qquadeta_{11}=p.
]
They are nonnegative, sum to one and reconstruct both `p,q` exactly from vertices `(0,0),(0,1),(1,1)`.

Choose the three exact seam vertices
[
S_{00}=1/4,qquad S_{01}=1/3,qquad S_{11}=1/50,
]
and the affine triangular seam
[
S(p,q)=eta_{00}/4+eta_{01}/3+eta_{11}/50,quad
h(t,p,q)=1-7tigl(1-S(p,q)igr).
]
Throughout the domain, `1/50≤h≤1`. Split κ into the two charts:

* `0≤κ≤h`: G, `λ=κ/h`, with target face `a'=z'=0`.
* `h≤κ≤1`: F, `λ=(κ-h)/(1-h)` when `h<1`, with face `z'=a'/10,;v'-z'=9b'/40`. When `h=1` the G chart covers the entire admissible κ interval.

These faces each satisfy the seedless polynomial `9b'z'=4a'(v'-z')`.

**Exact vertices.** `VERIFY_TRIANGLE.py` contains all `2 charts × 3 triangular vertices × 2 θ endpoints × 2 λ endpoints = 24` exact rational seven-coordinate target certificates at `t=1/7`. Each certificate satisfies: source and target physical bounds; nonnegative seven-node calibrated masses; mass sums `ΣM_i=Σr_iM_i=1`; two exact stopping-time equalities; all five exact hinge inequalities; the selected seedless face. At the `t=0` endpoint, a further 24 identity certificates hold: the source itself lies on G for `κ=λ`, and on F for `κ=1`.

**All-real extension.** Let `s=7t`. Within either fixed chart, source `x(t,p,q,θ,κ)` at `κ_G=λh` or `κ_F=h+λ(1-h)` is multilinear in `s`, the triangle barycentric coordinate, `θ` and `λ`. Form the target `y` by interpolating the 48 verified endpoint certificates with the nonnegative product weights of `(1-s,s)`, `(β00,β01,β11)`, `(1-θ,θ)`, `(1-λ,λ)`. Exactly the same weights interpolate the sources, so the calibrated time equations hold. All physical laws, five hinge inequalities and LR normalization are affine in the seven flow coordinates; hence all persist under these weights. The targets remain inside one common linear seedless face on each chart. Since the seven LR nodes have the same total mass and mean under both distributions, the five hinge inequalities imply convex order and finite Strassen's martingale theorem supplies `E` with the claimed marginal and conditional-expectation equations. This establishes the result for all real parameters, not merely the regression points.

Reference for martingale convex-order equivalence: Leskelä and Vihola, *Conditional convex orders and measurable martingale couplings*, Bernoulli **23** (2017), 2784–2807, DOI 10.3150/16-BEJ827; [author record](https://mooc.math.aalto.fi/~lleskela/paper018.html). The finite hinge reduction is elementary: the five interior piecewise-linear call payoffs plus affine functions generate every convex function on this fixed seven-node ordered support.

## Independent exact execution and frontier

Executed on 2026-11-08 with Python 3 standard library `Fraction` (no floating arithmetic in the verifier):
```
PASS_EXACT_24_NONTRIVIAL_PLUS_24_ZERO_ENDPOINTS 48
PASS_EXACT_201_INTERIOR_REGRESSIONS
PASS_EXACT_24_BOUNDARY_REGRESSIONS
THEOREM_ALL_REAL_T_LE_1_OVER_7_P_LE_Q_FULL_THETA_KAPPA
```
The full stdout is preserved as `EXACT_OUTPUT.txt`. The 201 samples check the interpolator implementation; the all-real statement follows from the finite exact certificate and algebraic interpolation.

Discovery used floating LP followed by exact rational reconstruction of all 24 targets. Discovery optimizers are not treated as proof. A single G/F affine seam for the **entire** square `(p,q)∈[0,1]^2` was not found at `t=1/7`; this is scoped to that chart search, consistent with the separate `p=1,q=0,θ=1` full-axis theorem already established by PR #1821.

**Next discriminating unit:** determine the largest rational `T>1/7` for which a triangular G/F seam admits exact certificates at all three `(p,q)` vertices, for both θ endpoints; if the `(1,1)` corner fails, find its exact dual obstruction or replace the F/G face. In parallel, bridge the triangular `p≤q` zone to a neighborhood of the already-known special `p=1,q=0,θ=1` family by a refined third chart. Independent review and native canonical Result/Review are pending.
