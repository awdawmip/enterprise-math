# R5 — Complete continuous asymmetric-time phase diagram for signed P/Q-BRC support

Date: 2026-11-07 Asia/Shanghai. Status: AUTHOR_PROVED / EXACT_FRACTION_EXECUTED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.

## Question, source and precise scope

Continue the frozen four-stage P/Q-BRC likelihood-ratio observer of PR #1767, after the exact two-section result at epsilon=+/-1/100 (predecessor commit 43b8f702f3608fa8b28b47ebf2408bedddf3d4a8). Task scientific pins are unchanged: Global `a01383f825ef9d43b4b754254303298c64041568`, EM `86149263e38c22292c9def1e0f69092efa1be77e`. The mother question is equality or separation of four-observer images `O4(FULL_HIST)` and `O4(seedless LR)`, where `W=(eP,eQ,TP,TQ)`.

All variables, seven stopping Q masses M_j, likelihood ratios r=(1/10,1/2,3/4,1,5/4,3/2,19/10), timing formulas and sixteen affine feasibility inequalities are exactly those in this directory's `VERIFY.py`. We retain the distinct central history contributions through z. The reduced seedless identity is `9*b*z = 4*a*(v-z)`. We optimize all randomized terminal declarations; at each key their optimal coefficient is `[1-(1+lambda)*r_j]_+`. This is an internal finite LR observer problem, with no assertion that the finite reduction supplies a complete native X6 dynamical model.

Set `TP=31/10+epsilon`, `TQ=31/10-epsilon`, and `U_lambda=eQ-(1+lambda)*(1-eP)`.

## Theorem: complete two-parameter closed strip (all real points)

For **every real** `epsilon in [-1/56,9/344]` and `lambda in [-1/10,1/10]`,

```
max_FULL_HIST U_lambda = max_seedless_LR U_lambda = H(epsilon,lambda).
```

Define breakpoints `m=-26217/398347`, `l=-351/17291`, `h=351/16589`. The function H is given by the following exact affine-in-lambda formulas (epsilon is a free real parameter in the respective row).

For `0 <= epsilon <= 9/344`:

| lambda interval | Exact H(epsilon,lambda) | attaining seedless family |
| --- | --- | --- |
| [-1/10,l] | 966/3875 + 174*epsilon/3875 + (1352*epsilon-3932)*lambda/11625 | P_outer |
| [l,0] | 13269/53000 + 27*epsilon/6625 - (903896*epsilon+136239)*lambda/477000 | I_inner |
| [0,h] | 13269/53000 + 27*epsilon/6625 - (1000216*epsilon+101919)*lambda/477000 | I_inner |
| [h,1/10] | 966/3875 + 174*epsilon/3875 - (46808*epsilon+1897)*lambda/11625 | P_outer |

For `-1/56 <= epsilon <= 0`:

| lambda interval | Exact H(epsilon,lambda) | attaining seedless family |
| --- | --- | --- |
| [-1/10,m] | 966/3875 + 2481*epsilon/7750 + (20213*epsilon-7864)*lambda/23250 | N_far |
| [m,l] | 966/3875 - 216*epsilon/3875 - (168854*epsilon+11796)*lambda/34875 | N_outer |
| [l,0] | 13269/53000 + 27*epsilon/6625 - (903896*epsilon+136239)*lambda/477000 | I_inner |
| [0,h] | 13269/53000 + 27*epsilon/6625 - (1000216*epsilon+101919)*lambda/477000 | I_inner |
| [h,1/10] | 966/3875 - 216*epsilon/3875 + (25466*epsilon-5691)*lambda/34875 | N_outer |

The optimizing-flow switch loci in this rectangle are therefore **vertical lines of constant lambda**, rather than nonconstant curves: `lambda=m` when epsilon<0, and `lambda=l,h` on both sides. At epsilon=0, `P_outer(0)=N_far(0)=N_outer(0)`, so the m-switch becomes a degenerate tie. The lambda=0 declaration-key transition is separate.

## Four explicit affine seedless certificates

Let the ordered flow be `(g,a,b,u,v,w,z)`. For each real epsilon, the attaining flows are:

```
P_outer: (28/31+344e/93, 28/31-1144e/93, 28/31+344e/93,
          0, 91/310-37e/93, 0, 14/155-572e/465).
I_inner: (1, 44/53-504e/53, 44/53+344e/53,
          0, 143/530+27e/53, 0, 22/265-252e/265).
N_far:   (28/31+40e/31, 28/31+40e/31, 28/31+40e/31,
          -4e, 91/310+13e/31, 0, 14/155+4e/31).
N_outer: (28/31-168e/31, 28/31-168e/31, 28/31+328e/31,
          0, 91/310+57e/31, 0, 14/155-84e/155).
```

The P_outer family is feasible on [0,9/344]; I_inner on [-1/56,9/344]; N_far and N_outer on [-1/56,0]. In every case `v=a/10+9*b/40` and `z=a/10`, so `9*b*z=4*a*(v-z)` identically; all time, mass and LR-moment identities also hold. Exact endpoint checks suffice for the affine legal inequalities across each real interval.

## Rigorous universal upper bound and proof

The predecessor gives eleven exact nonnegative dual multipliers `mu_i`, unrestricted time multipliers `nuP,nuQ`, and eight-coefficient identities `S_lambda - sum_i(mu_i L_i) - nuP TP - nuQ TQ = K` at the distinct endpoint certificates. Since `L_i<=0`, each is a universal FULL_HIST upper bound for its lambda and for **every** feasible epsilon. We recheck all eleven identities exactly from the inherited Fraction code.

This run verifies that, for each of the nine rectangles listed above, its named affine seedless family realizes both endpoint dual values at both epsilon endpoints. The primal and dual values are affine in epsilon at each fixed lambda endpoint, so their equality extends to every real epsilon within the rectangle. For fixed epsilon, `S_lambda(x)` and the interpolation of the two nonnegative dual certificates are affine in lambda on each rectangle (no LR declaration sign changes in its interior). Their equal endpoint values extend to every real lambda. This proves simultaneous exact primal attainment and universal upper bounds in the **entire continuous strip**. No discretization, grid extrapolation or floating-point step appears in the proof.

The exact checker adds four families and nine all-real rectangles to the predecessor's eleven rational dual identities. It verifies four epsilon-band feasibility endpoints with a midpoint quadratic check, all seven Q masses and their first LR moment, timing, seedless equality, 18 families/dual endpoint matches and all nine rectangle sign sets. The local Python standard-library Fraction execution produced `PASS_R5_FULL_CONTINUOUS_EPS_LAMBDA_EXACT_9_RECTANGLES_11_DUAL_CERTIFICATES`, with stdout in `EXACT_OUTPUT.txt`. Mathematical status remains author-checked, pending independent review.

## Meaning and next question

The two isolated asymmetric sections at e=+/-1/100 now belong to one exact **continuum** of unequal stopping times. The apparently ε-dependent branch-switch curve is actually constant over these intervals, with a new negative-side branch `m` that disappears through optimizer degeneracy at zero. The mother problem of entire four-observer image equality versus strict separation remains open. Next optimize a general time-tilted four-observer normal, allowing both time values to vary jointly; see `NEXT_UNIT.md`.

BRC reuse classification: REUSE_APPLIED to the frozen seven-mass P/Q-BRC LR observer and its full history branch variable z; no native BRC operator execution or X6 physical transfer is claimed. The historical mixing residual is retained until the declared O4 observer is evaluated. Formal Owner/CLAIM/Result and independent Review are separate from this portable scientific source.
