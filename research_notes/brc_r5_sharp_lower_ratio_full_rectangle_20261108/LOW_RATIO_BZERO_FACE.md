# R5 — Complementary low-ratio full-capacity seedless b=0 Blackwell face

Date: 2026-11-08 Asia/Shanghai. Author-side exact proof under frozen GLOBAL pin `a01383f825ef9d43b4b754254303298c64041568` and EM pin `86149263e38c22292c9def1e0f69092efa1be77e`. Follows `RESEARCH.md` in this directory; its model formulas and likelihood nodes are unchanged.

## New all-real complementary theorem (full physical p,q rectangle)

For all real `0<=s<=g<=1`, `0<=eta<=1/40`, `0<=p,q,h<=1`, set

```text
u=s*(13/40+eta/80)*p
w=s*(3/40+21*eta/80)*q
x=(g,s,eta*s,u,9eta*s/40,w,0).
```

Then there exist a lawful seedless flow `y` on the **different affine face** `G={b=0,v=z}` and a nonnegative calibrated 7x7 Blackwell matrix transferring every real 7-node randomized terminal declaration on `x_h=(1-h)x+h*y` to an equivalent declaration on y, preserving exactly `(e_P,e_Q,T_P,T_Q)`.

The source history residual is `R(x)=-9eta*s^2/10`. This gives a second low-ratio all-real band, complementary to the `46/705<=eta<=1` full-rectangle band in `RESEARCH.md`. This theorem deliberately fixes source `z=0`; the family with `theta>0` at small eta remains a separate question.

## Four new exact rational corner certificates

`ETA_1_40_BZERO_CORNERS.json` contains four lawful Q-mass matrices at `g=a=1,b=1/40,v=9/1600,z=0` and each `(p,q)=(0,0),(0,1),(1,0),(1,1)`. All four y targets satisfy `b_y=0,v_y=z_y`, hence seedless independently of other flow variables. New exact corner target (p,q)=(0,1), inaccessible to face F below its sharp threshold, is

`y=(1091/1120,519/560,0,0,519/5600,1557/22400,519/5600)`.

One more exact rational `7x7` certificate `ETA_1_20_RATIO_ZERO.json` gives a stronger isolated p=1,q=0 point at eta=1/20, with

`x=(1,1,1/20,521/1600,9/800,0,0)`,

`y=(901/920,901/920,0,11713/36800,343/4600,0,343/4600)`,

`(T_P,T_Q)=(8257/3200,4579/1600)`.

Both are on the legal original model and y is seedless on face G. This eta=1/20 instance lies **below** the sharp bound 46/705 established for the other face F; it shows directly why the F obstruction must be kept face-specific.

## Proof for all real eta in [0,1/40]

At eta=0 every saturated-v corner source with arbitrary p,q has b=0 and v=z=0, so it is itself a lawful seedless G-face flow; take target equal to source and diagonal identity Q transport. At eta=1/40 use the four new rational matrices. Both endpoint source corner flows depend affinely on eta, and all seedless targets lie on the same **linear face G**, so interpolate corresponding endpoint triple `(x,y,Q)` with coefficient `40eta` in [0,1].

For arbitrary p,q combine the four corners with nonnegative bilinear coefficients `(1-p)(1-q),p(1-q),(1-p)q,pq`; Q row, Q column, likelihood-weighted P column and both stop times are affine and preserve validity. Since physical capacities `13a/40+b/80` and `3a/40+21b/80` are affine in eta, this yields exactly the source with both independent physical p,q coordinates.

Introduce `E0=(0,0,0,0,0,0,0)` and `E1=(1,0,0,0,0,0,0)` in G. Combine the normalized (g=a=1) source and target with weights `(1-g),(g-s),s`; target remains G, Q stays calibrated and nonnegative. Finally mix x and y with h, and Q with the diagonal target mass matrix. The induced randomized declaration is `d'_i=(sum_j Q[i,j]d_j)/M_i(y)` for positive M_i(y). The Q and P identities imply equality for all real terminal declarations, not only those tested.

`VERIFY_LOW_G.py` (depending on this directory's `VERIFY.py`) checks all 4 exact eta=1/40 corner certificates and 729 rational interpolation combinations with three randomized declarations each. `EXACT_LOW_G_OUTPUT.txt` preserves actually observed stdout from local Python Fraction execution. The all-real statement follows from the displayed nonnegative interpolation. The separate eta=1/20 transport is exactly checked by a rational linear-system solution and explicit row/column/moment identities in the exploratory extraction; its sparse rational matrix is provided for independent checking.

## Scope and next direction

Together the two verified author-side bands now cover full p,q physical rectangles for `0<=eta<=1/40` with z=0 and for `46/705<=eta<=1` with all legal z. The open interval `(1/40,46/705)` and small-eta positive z are the immediate opportunities. Seek another common seedless face or direct nonlinear seedless targets; no global separation is inferred from one face. These are author-side proofs awaiting independent review and native task intake.
