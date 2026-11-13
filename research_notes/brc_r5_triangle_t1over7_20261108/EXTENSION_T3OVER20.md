# R5 stronger triangular prism: exact extension to t ≤ 3/20

Date: 2026-11-08. Status: AUTHOR_PROVED / EXACT_FRACTION_EXECUTED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY. Extends the preceding `RESEARCH.md` theorem on the same frozen seven-node P/Q-BRC model. Scientific pins remain GK `a01383f825ef9d43b4b754254303298c64041568`, EM `86149263e38c22292c9def1e0f69092efa1be77e`.

## Stronger all-real theorem

For all real
[
oxed{0le tle 3/20,quad 0le ple qle1,quad0le	heta,kappale1},
]
the lawful FULL_HIST seven-coordinate flow
[
x=(1,t,1,(13t/40+1/80)p,;9kappa/40+t	heta/10,;(3t/40+21/80)q,;t	heta/10)
]
has a lawful seedless LR target `y` and a nonnegative declaration-independent seven-by-seven Blackwell martingale coupling, preserving both calibrated stop times `T_P,T_Q` and all randomized seven-node declaration observables `e_P,e_Q`.

## Constructive G/F triangular seam, including singular corner

Reuse triangle barycentric weights
[
eta_{00}=1-q,qquad eta_{01}=q-p,qquad eta_{11}=p.
]
Set the exact seam vertices
[
S_{00}=1/4,quad S_{01}=1/3,quad S_{11}=0,
]
then
[
S(p,q)=eta_{00}/4+eta_{01}/3,qquad
h(t,p,q)=1-rac{20t}{3}(1-S(p,q)).
]
Throughout this real domain `0≤h≤1`; `h=0` occurs at `t=3/20,p=q=1`. For `h>0` and `κ≤h` use G, `λ=κ/h`, target face `a'=z'=0`. Otherwise use F, `λ=(κ-h)/(1-h)`, target face `z'=a'/10,;v'-z'=9b'/40`. In the exceptional `h=0` case, F applies to every `κ∈[0,1]` and its `λ=κ`; the denominator `1-h` is one. At `h=1` use G for every `κ` and avoid the F denominator. Thus all points are covered with well-defined coordinates.

At `t=3/20`, `VERIFY_TRIANGLE_T3OVER20.py` gives 24 exact rational target vertices indexed by chart, one of `(0,0),(0,1),(1,1)`, `θ∈{0,1}`, and `λ∈{0,1}`. The G vertices at `(p,q)=(1,1)` have `S=0` and duplicate the same source `κ=0`; F vertices handle that entire boundary in the theorem. In the `t=0` limit, all 24 source vertices themselves satisfy the selected seedless face and exact identity transport.

All 48 endpoints were checked with Python standard-library exact `Fraction` arithmetic for: physical capacity, nonnegative seven LR masses, probability/first LR moment normalization, both stop-time equations, five hinge inequalities, and the G/F seedless face constraints. Each selected face is affine. Interpolate these vertices using product weights of `s=t/(3/20)`, the three triangle barycentric coefficients, `θ`, `λ`. The source coordinates are multiaffine in these variables within either chart, since `κ_G=λh` or `κ_F=h+λ(1-h)`; the target remains on the same seedless face, and every physical, hinge, mass and time check is affine in the flow vector. Finite support Strassen convex-order martingale coupling theorem therefore supplies the nonnegative transfer at every real point. At `h=0` use the F-side interpolation, as above.

This is a new complete two-dimensional triangular capacity region with both remaining physical parameters fully variable, and the `t` boundary advances from `1/7` to `3/20`. All-real coverage follows from the analytic interpolation and five-point finite hinge characterization, not the test sample count.

## Reproduction and evidence

Run `python3 VERIFY_TRIANGLE_T3OVER20.py` from the evidence directory; direct independent local execution on 2026-11-08 yielded:

```
PASS_EXACT_24_NONTRIVIAL_PLUS_24_ZERO_ENDPOINTS 48
PASS_EXACT_201_INTERIOR_REGRESSIONS
PASS_EXACT_24_BOUNDARY_REGRESSIONS
THEOREM_ALL_REAL_T_LE_3_OVER_20_P_LE_Q_FULL_THETA_KAPPA
```

Exact stdout is also stored in `EXACT_OUTPUT_T3OVER20.txt`. The rational targets were reconstructed from exploratory floating linear programming; the published rational certificate and deterministic checker supply the proof-facing evidence. The original t≤1/7 theorem and its verifier are retained as a reusable nonsingular-seam construction.

## Exact next question

The corner `(p,q)=(1,1)` is saturated at `t=3/20` for the current **two-face triangular seam**, `S_{11}=0`. Determine a rational dual certificate for a face-local threshold, or build a third legal seedless face to extend the triangular real domain beyond `t=3/20`. The existing `p=1,q=0,	heta=1` all-t family in PR #1821 is independent bridging evidence. This is a model-specific author construction; no formal task CLAIM or independent theorem admission is asserted.
