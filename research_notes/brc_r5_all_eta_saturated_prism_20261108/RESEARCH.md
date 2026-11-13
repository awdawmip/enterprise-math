# R5 — all-ratio saturated physical prism via G/F face-switch Blackwell calibration

**Date:** 2026-11-08. **Research level:** AUTHOR_PROVED / EXACT_FRACTION_EXECUTED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY. Frozen scientific pins: GLOBAL `a01383f825ef9d43b4b754254303298c64041568`, EM `86149263e38c22292c9def1e0f69092efa1be77e`. Current behavioral rules were read from canonical main separately. No changes to P000, worldview or immutable scientific input. Native task Owner/CLAIM query failed (`BACKEND_IDENTITY_OR_VERSION_MISMATCH / STATUS_DATABASE_UNAVAILABLE`); this is author-side source evidence.

## Exact theorem

Fix seven P/Q likelihoods `r=(1/10,1/2,3/4,1,5/4,3/2,19/10)`. For **every real** `0<=eta,theta,p,q,h<=1` and `0<=s<=g<=1`, define lawful saturated FULL_HIST

```
x=(g,s,eta*s,
   s*(13/40+eta/80)*p,
   s*(9*eta/40+theta/10),
   s*(3/40+21*eta/80)*q,
   s*theta/10).
```

There exists a lawful seedless LR target `y=(g',a',b',u',v',w',z')` satisfying `9*b'*z'=4*a'*(v'-z')` and a nonnegative calibrated `7x7` Blackwell transport `Q[target_i,source_j]` such that for all terminal declaration vectors `d∈[0,1]^7`, the normalized row-conditional declaration `d'_i=Σ_j Q[i,j]d_j/M_i(y)` on positive target rows (0 otherwise) yields identical four observers `(eP,eQ,TP,TQ)`. The same target supports every source-to-target interpolation `x_h=(1-h)x+h*y` by `Q_h=(1-h)Q+h diag(M(y))`. The transport is chosen *independently of d*. Thus the saturated source family's **entire** physical `(eta,theta,p,q)` prism, including the formerly open `1/40<eta<46/705`, lifts for all real parameters, not only rational grid points.

Lawfulness for `f=(g,a,b,u,v,w,z)` requires `0<=a,b<=g<=1`, `0<=u<=13a/40+b/80`, `0<=w<=3a/40+21b/80`, `0<=z<=a/10`, `0<=v-z<=9b/40`. The labeled Q-masses and stop times are

```
M0=509u/900+47z/180+67(v-z)/162+w/100
M1=13a/40+b/80-u
M2=(g-a)/2
M3=1-g+a/10+9b/40-v+191(u+w)/450+43z/90+14(v-z)/81
M4=(g-b)/2
M5=3a/40+21b/80-w
M6=u/100+47z/180+67(v-z)/162+509w/900
TP=1+g+3a/8+5b/8+u/2+v+3w/2
TQ=1+g+(a+b)/2+u+v+w.
```

A calibrated triple obeys `Σ_j Q[i,j]=M_i(y)`, `Σ_i Q[i,j]=M_j(x)`, `Σ_i r_i Q[i,j]=r_j M_j(x)`, and `TP(y)=TP(x),TQ(y)=TQ(x)`. These equations preserve both error probabilities for any `d`, since each positive target row is a convex declaration average. They refer to the frozen *seven-node statistical/BRC observers*, not a new X6 physical dynamics assertion.

## Constructive proof (all real)

Use two **linear seedless target faces**: `G={b=0,v=z}` and `F={z=a/10,v-z=9b/40}`. A convex mixture of lawful calibrated triples with targets on the *same* face stays seedless, lawful, nonnegative and calibrated because every branch mass and both stop times are affine. We never interpolate G targets against F targets.

Define the piecewise-affine switching height `c(eta)` from the knots

```
eta:       0     1/40     1/30      46/705       1
c(eta):    1      3/4      1/2         0         0
```

Equivalently, `c(eta)=1-10eta` for `[0,1/40]`, `3/2-30eta` for `[1/40,1/30]`, `(47/3)(46/705-eta)` for `[1/30,46/705]`, and zero for `[46/705,1]`.

For `theta<=c(eta)`, split the square along `q=p/2`. On `q<=p/2`, use **G** triangle vertices `(p,q)=(0,0),(1,0),(1,1/2)` with weights `(1-p,p-2q,2q)`. On `q>=p/2`, use **F** quadrilateral vertices `(0,0),(0,1),(1,1),(1,1/2)`; writing `t=(q-p/2)/(1-p/2)`, use weights `((1-p)(1-t),(1-p)t,pt,p(1-t))`. Both weight systems are nonnegative and reproduce the source coordinates at fixed eta and theta.

The accompanying exact rational endpoint transports are the **43 certificates** in the compressed data file, with a standard-library decoder/checker in `VERIFY.py`:

- eta=0, theta=0: four F-quadrilateral transports (G is an exact identity at eta=0, all theta);
- eta=1/40, theta=0 and theta=3/4: G triangle at both, F quadrilateral at zero and full F square at the switch (14);
- eta=1/30, theta=0 and theta=1/2: the analogous 14;
- eta=46/705, theta=0: G triangle and F square (7);
- eta=1, theta=0: F square (4).

For any eta between neighboring knots, fix `(p,q)` and interpolate the two endpoint-eta triples: at `theta=0` and at `theta=c(eta)`. Because the source `u,w` are affine in eta **at fixed p,q**, and `c(eta)` is affine on each knot interval, these mixtures have exactly the desired source at those two heights. Mix the resulting same-face endpoint triples along `0<=theta<=c(eta)`. At `theta=c(eta)`, F independently has all four square corners (the latter include `(1,0)`, even where F fails at theta=0), and `theta=1` is an F *identity* since the saturated source is then itself seedless. Mix these F triples to cover `c(eta)<=theta<=1`. For `46/705<=eta<=1`, F corner certificates at theta=0 and identities at theta=1 cover the square directly. Every eta, theta, p, q including irrational values and all shared boundaries is covered.

For `0<=s<=g<=1`, mix the normalized triple with diagonal seedless identity transports at `E1=(1,0,0,0,0,0,0)` and `E0=(0,0,0,0,0,0,0)`, with weights `s,g-s,1-g`. Both identity targets belong to both faces. Finish with `Q_h=(1-h)Q+h diag(M(y))`. All displayed interpolations are nonnegative, keep their selected target face and preserve the exact mass/likelihood/stop-time equations. This proves the theorem over **all real parameters**.

## Verification and provenance

The data file stores `zlib`-compressed UTF-8 JSON (base64 wrapped), with each certificate specifying its exact eta/theta/p/q, face, seven rational target entries, and sparse rational `Q[i,j]` edges. The checker reconstructs source masses independently and verifies the 43 anchor matrices by **exact** `fractions.Fraction`: lawful policies, both measure normalizations, all 7 row-mass equations, all 7 Q-column equations, all 7 r-weighted P-column equations, two stop times, nonnegative edges, and all seven basis declaration vectors. The local checker was also run for 1,950 mixed parameter values, 780 moving-boundary cases, and four general `(s,g,h)` cases. `EXACT_OUTPUT.txt` gives the actual local execution. These finite checks are a reproduction test; the universal proof is the preceding same-face interpolation argument.

The sparse supports were discovered using SciPy HiGHS linear feasibility, then converted to exact rational solutions via Sympy linear algebra. Floating feasibility is **not** used to justify the theorem. This proof is a new self-contained extension of the previous R5 frontiers, particularly `b16791024c053bb3afd1883d008855a8fb34ed14`, but remains **unreviewed author mathematics**, not a canonical Result, Working Truth or Foundation admission. Frozen source/model scope is preserved.

## Next unresolved unit

The saturated relation `v-z=9b/40` is solved for the stated physical prism. The full legal FULL_HIST family also permits `v-z=9*kappa*b/40`, `0<=kappa<=1`. The complementary unsaturated **negative-residual** G-face theorem now covers `z=0`, `0<=eta<=1/30`, `0<=kappa,p,q<=1` with eight exact rational anchor kernels; see `NEGATIVE_RESIDUAL_G_CUBE.md` in this same directory. The prior universal nonnegative-residual theorem already covers `kappa<=theta` for normalized `z=theta/10`, since `R=(9eta/10)(theta-kappa)`. Thus start with `0<theta<kappa<1` or `theta=0,eta>1/30` beyond the newly proved cube. Test exact G/F feasibility and rational calibrated kernels or **face-specific** obstructions; explore a third surface when useful. If these faces do not cover a case, search a third seedless representation. The broader R5 all-lawful-flow four-observer mother question remains open.
