# R749SL — Exact affine-vs-nonlinear rank gap for a full gated signed-Port posterior

Date: 2026-11-12 / 2026-11-13 Asia/Shanghai. Continuation of R749SK on the same independent scientific branch, with frozen R749 input `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389` and the exact R749SF conditional BSC kernel. Author-side exact proof and full finite X6 support-class check; this is no native triadic PASS or independent review.

## Model

For any of the 120 directed unsigned supports `A={i,j},B={j,k}`, condition on forced support completion `C=A△B`. The new sign `Y_i` follows an independent binary symmetric channel of correlation `θ=8p/(1+7p)` from `X_i`, while `Y_j=X_j` and `Y_k=X_k`. A gate succeeds with likelihood `ell(Y_i,Y_j)=(2+Y_i+Y_j)/4`. This gate vanishes precisely when `(Y_i,Y_j)=(-1,-1)`, leaving SIX possible final sign states (two values of `Y_k` for each of the other three sign pairs).

The complete conditional output observation `F_p(mu)` is the six-component probability vector of these permitted final signed states, given gate success. Initial mu ranges over the open seven-dimensional simplex of strictly positive eight-lift source distributions.

## Theorem 1 — Sharp minimum affine initial-Walsh carrier

For all `p∈(0,1]`, **exactly six independent affine-linear statistics of the initial signed-source moments** are necessary and sufficient to compute the complete gated six-state posterior for every initial prior. At `p=0`, exactly **three** are necessary and sufficient.

**Proof.** For each allowed final sign state y, its unnormalized gated weight is the affine functional `N_y(mu)=ell(y)Σ_x mu(x)T_p(x,y)`. The common denominator is `D(mu)=Σ_{y:ell(y)>0}N_y(mu)`; all six output components are nonconstant fractions `N_y/D` on the positive prior simplex. R749SK's exact minimum-affine-ratio theorem says their joint minimal input coordinate dimension is the rank, *on the prior-simplex tangent space*, of the rows `N_y` and `D`. Since D is their sum, only the six N_y rows matter.

For p>0, θ>0, so the forced signed transition `T_p=BSC_θ⊗I_2⊗I_2` is invertible as a linear map on eight signed probabilities (its two-state factor has eigenvalues 1 and θ). Selecting any six distinct output coordinates of the invertible T_p and multiplying each by a strictly positive gate weight yields six independent linear forms on R^8. Their restrictions to the seven-dimensional normalized-probability tangent space are still independent: otherwise a nonzero linear combination of these six rows would equal the all-ones constant functional; composing with the inverse T_p would express the all-ones output functional as a combination of only six coordinate functionals, impossible because TWO output coordinates are absent. Thus tangent rank is six. Row-basis sufficiency and Theorem A's necessity give exactly six.

At p=0, θ=0 and Y_i is a fair coin independent of the initial source. The complete final distribution and gate depend on initial mu only through the four values `nu_{jk}=Pr(X_j=j,X_k=k)`; these sum to one, hence have three independent affine coordinates. Each of the four (j,k) choices contributes at least one positive gated output row, so the six rows span precisely the three-dimensional tangent variation of nu. Therefore the sharp minimal affine-coordinate count equals three.

The statement is sharp on the full interior of the initial eight-lift simplex; p=0 is an exact rank-change point, rather than a numerical threshold.

## Theorem 2 — Different notions of minimum for the same observer

For p>0, the normalized gated posterior lives on the six allowed output states and attains an open subset of the five-dimensional probability simplex. Consequently it has a **five-parameter nonlinear output representation**, but it needs six affine-linear source statistics to be computed uniformly from the unknown initial prior. The apparent gap is the source-dependent gate normalization factor. At p=0 the complete posterior image has three degrees of freedom, agreeing with the minimum three affine source coordinates. The differing counts refer to different declared carrier classes, not conflicting statements.

At the narrower one-parity query of R749SK the exact affine minimum is two for p>0 and one for p=0. Expanding the observation language from one posterior parity to all six gated final-state probabilities changes the minimum from 2→6 (p>0) and 1→3 (p=0).

## Validation

`R749SL_FULL_POSTERIOR_AFFINE_RANK_CHECK.py` enumerates all 120 legal initial directed unsigned supports, p∈{0,1/2,1} and all six permitted final sign states, constructs their full 8-entry exact gated transition rows, computes the exact rational rank on the seven-dimensional prior-simplex tangent space, checks each posterior is nonconstant and the uniform-prior six-state posterior normalizes to one. All 360 support/parameter rank checks PASS with `Fraction` arithmetic. The all-p theorem is established by the invertibility/rank argument above, not by interpolation.

## Next

Study whether sparse or adaptive gate families admit low-dimensional *online* sufficient source states with exact conditional normalization, and whether the 6-to-3 source-dimension transition persists under nonforced resets and multi-time observations. Keep V29/V39 native permission and explicit signed-Port/BRC provenance separate.
