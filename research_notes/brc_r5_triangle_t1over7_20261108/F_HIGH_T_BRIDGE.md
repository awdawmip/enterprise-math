# R5: exact upper triangular F-face bridge, 7/39 ≤ t ≤ 1/5

Date: 2026-11-08; status AUTHOR_PROVED / EXACT_FRACTION_EXECUTED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY. Same inherited frozen seven-node P/Q-BRC statistical observer model and science pins as sibling `EXTENSION_T3OVER20.md` (GK a01383f825ef9d43b4b754254303298c64041568; EM 86149263e38c22292c9def1e0f69092efa1be77e). Current P000/ACTIVE world model remains unchanged.

## Theorem

Let
[
x=(1,t,1,(13t/40+1/80)p,;9kappa/40+t	heta/10,;(3t/40+21/80)q,;t	heta/10).
]
For **every real**
[
oxed{rac7{39}le tlerac15,quad0le ple qle1,quad0le	heta,kappale1},
]
there exists a lawful seven-coordinate seedless LR flow `y` on **one common affine F face**
[
z'=a'/10,qquad v'-z'=9b'/40
]
and a nonnegative seven-node martingale Blackwell coupling from the target to source preserving the likelihood-ratio weighted terminal laws, both stop times, and thus the four observables `(e_P,e_Q,T_P,T_Q)` for every randomized seven-node terminal declaration.

This proves a second substantial low-ratio triangular segment above the previously proved `t≤3/20` triangle, reducing the remaining interior gap to `3/20<t<7/39`. The earlier predecessor PR #1800 supplies coverage at `t≥1/5` for the broader physically lawful class; the local F-face certificate in this note is self-contained for the stated interval.

## Fully exact finite vertex construction

Write triangle barycentric weights `β00=1-q`, `β01=q-p`, `β11=p`; these are nonnegative, sum to one, reconstruct p/q from vertices (0,0),(0,1),(1,1). At each t endpoint 7/39 and 1/5, for each of three triangle vertices, for θ=0/1 and κ=0/1, provide a seven-coordinate exact rational target. `VERIFY_F_HIGH_T.py` contains all 24 rational targets as a literal table. There are **no numerical LP floats in the certificate**: LP was exploratory, then the targets were reconstructed by exact rank-7 rational linear systems and all source/target relations checked with `fractions.Fraction`.

For any real point in the box, interpolate the 24 target vectors with the product of `s=(t-7/39)/(1/5-7/39)`, triangle barycentric, θ, and κ Bernoulli weights. All 24 targets lie on the same linear seedless F face. The source is separately affine in the corresponding variables: its mixed terms `tp,tq,tθ` are interpolated by the same nonnegative weights. The seven LR mass constraints, first LR moment, physical capacities, two stop-time equalities, and five interior hinge convex-order comparisons are all affine in flow coordinates, hence remain true at all real points. Finite Strassen martingale coupling theorem supplies a nonnegative 7×7 declaration-independent transport with `Σ_j E_ij=M_i(y)`, `Σ_i E_ij=M_j(x)`, `Σ_i r_i E_ij=r_jM_j(x)`. This proves the theorem including irrational/boundary inputs.

## Exact execution

Run `python3 VERIFY_F_HIGH_T.py` in this source directory; it imports only sibling standard-library `VERIFY_TRIANGLE_T3OVER20.py`, which in turn contains the full calibration independent of predecessor PR files. Actual executed stdout 2026-11-08:

```
PASS_24_F_FACE_EXACT_CORNERS
PASS_201_EXACT_INTERIORS
PASS_24_EXACT_BOUNDARIES
THEOREM_ALL_REAL_T_7_OVER_39_TO_1_OVER_5_P_LE_Q_ALL_THETA_KAPPA
```

The exact output is preserved in `EXACT_OUTPUT_F_HIGH_T.txt`. The analytic interpolation and exact vertex check prove all real inputs; the 201 regression points check the implementation.

## Next exact unit

Bridge the remaining open region
[
oxed{3/20<t<7/39,quad0le ple qle1,quad0le	heta,kappale1}.
]
On `p=q=1`, G ceases to be feasible at `κ=0` above `t=3/20`, while F remains feasible there; on `p=0,q=1,	heta=0`, F becomes feasible at `κ=0` only at a higher ratio. Try triangular subdivision in (p,q,t,κ), switching between F and G at an interior subtriangle with overlapping exact endpoint certificates, rather than demanding a single global G/F seam. The observed LP feasibility is chart-local exploratory evidence, not an impossibility result for the mother model. Formal Task CLAIM, Source checkpoint, and independent review remain open.
