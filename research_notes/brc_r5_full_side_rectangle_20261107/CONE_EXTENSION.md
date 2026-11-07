# R5 extension: all-real four-parameter seedless Blackwell cone

Author-side exact theorem, 2026-11-07, same frozen R5 scientific pins and observer as `RESEARCH.md` in this directory. This extends the two-parameter `(u,w)` maximal-continuation rectangle to all early continuation scales `0<=s<=g<=1`.

## Theorem

For every real `0<=s<=g<=1`, `p,q in [0,1]`, and every real declaration vector `d in [0,1]^7`, the legal FULL_HIST flow

`x(g,s,p,q)=(g,s,s,27sp/80,9s/40,27sq/80,0)`

has a legal seedless LR flow, a seven-by-seven calibrated row-stochastic Blackwell kernel, and exact four-observer agreement after transforming declarations. The matched times are

`T_P=1+g+49s/40+27sp/160+81sq/160`,

`T_Q=1+g+49s/40+27s(p+q)/80`.

This is a four-real-parameter region (with boundary faces) inside the FULL_HIST model's flow domain. The history residual equals `-9s^2/10`, strictly negative for `s>0`.

## Exact proof

Let `E0=(0,0,0,0,0,0,0)` and `E1=(1,0,0,0,0,0,0)` denote the two baseline FULL_HIST flows. They are seedless LR, are legal, and have identical experiments, so each admits a diagonal transport `diag(M(Ek))`. Let `x_R(p,q),y_R(p,q),Q_R(p,q)` be the two-parameter source, seedless lift and exact transport proven and explicitly defined in `RESEARCH.md` and `VERIFY.py`.

Set nonnegative weights `a0=1-g`, `a1=g-s`, `aR=s`; their sum is one. Define

`x=a0 E0+a1 E1+aR x_R`, `y=a0 E0+a1 E1+aR y_R`,

`Q=a0 diag(M(E0))+a1 diag(M(E1))+aR Q_R`.

The first combination gives exactly `x(g,s,p,q)` coordinate by coordinate. All three seedless inputs obey the common *linear* equalities `z=a/10` and `v-z=9b/40`, so their convex combination is seedless LR, in addition to being legal. Stopping Q masses and both stopping-time functionals are affine in flows. Therefore the 7 row mass identities, 7 Q column identities, 7 likelihood-weighted P column identities and the two time equalities remain exact under these weights. All entries of Q are nonnegative. Normalizing Q's positive-mass rows into K and using identity zero-mass rows gives a stochastic kernel. For every real seven-key declaration vector, `d'=Kd` preserves `e_Q` and `1-e_P` by the two column identities, and hence preserves `e_P`, `e_Q`, `T_P`, `T_Q`. This is valid for arbitrary real values, including irrational parameters and boundaries. QED.

`VERIFY_CONE.py` reuses the four exact rational corner certificates from `VERIFY.py` and executes 108 distinct rational `(g,s,p,q)` checks, including degenerate boundaries, and all exact mass/time and seedless equations. Actual standard-library `Fraction` stdout is in `EXACT_CONE_OUTPUT.txt`. This is author-side mathematical evidence pending independent review and Source admission.

## Next scientific unit

Relax `v=9s/40` and `z=0` while retaining the joint `u,w` face. Seek a compatible finite affine seedless certificate family or classify the exact parameter obstruction. The full R5 mother question of all FULL_HIST flows and declarations remains open.
