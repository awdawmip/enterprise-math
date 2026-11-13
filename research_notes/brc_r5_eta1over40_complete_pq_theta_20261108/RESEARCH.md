# R5 — Complete mixed side-branch physical rectangle at η=1/40 by two calibrated BRC faces

Date: 2026-11-08 (Asia/Shanghai). Status: **AUTHOR_PROVED / EXACT_FRACTION_EXECUTED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY**. Predecessor: `research_notes/brc_r5_lowratio_p10_gf_switch_20261108/FULL_LOW_RATIO_BRIDGE.md` at `70fa2a872eceb389045c5a2da2393cd693d7806e`. Scientific pins remain global `a01383f825ef9d43b4b754254303298c64041568`, EM `86149263e38c22292c9def1e0f69092efa1be77e`. These are frozen scientific sources, distinct from the current normative main.

## Theorem (all real parameters)

Fix η=1/40. For every real `0<=s<=g<=1` and `0<=theta,p,q,h<=1`, the lawful FULL_HIST seven-coordinate source

```text
x=(g,s,s/40,
   s*(13/40+1/3200)*p,
   s*(9/1600+theta/10),
   s*(3/40+21/3200)*q,
   s*theta/10).
```

admits a lawful **seedless LR** target `y` and one nonnegative calibrated 7×7 BRC Blackwell transport `Q`. For every seven-component terminal declaration `d in [0,1]^7`, the interpolated source `x_h=(1-h)x+h*y` has exactly the same `(eP,eQ,TP,TQ)` as `y` with transported declaration `d'_i=sum_j Q_h[i,j]d_j/M_i(y)` on positive rows, with 0 elsewhere, where `Q_h=(1-h)Q+h*diag(M(y))`. Target and kernel depend on the flow parameters but **not** on d. This statement includes all irrational and boundary parameters.

The seven likelihoods are `r=(1/10,1/2,3/4,1,5/4,3/2,19/10)`. With `f=(g,a,b,u,v,w,z)`, branch Q masses are

```text
M0=509u/900 + 47z/180 + 67(v-z)/162 + w/100
M1=13a/40+b/80-u
M2=(g-a)/2
M3=1-g+a/10+9b/40-v+191(u+w)/450+43z/90+14(v-z)/81
M4=(g-b)/2
M5=3a/40+21b/80-w
M6=u/100+47z/180+67(v-z)/162+509w/900
TP=1+g+3a/8+5b/8+u/2+v+3w/2
TQ=1+g+(a+b)/2+u+v+w
```

A triple `(x,y,Q)` is calibrated precisely when `Q[i,j]>=0`, `sum_j Q[i,j]=M_i(y)`, `sum_i Q[i,j]=M_j(x)`, `sum_i r_i Q[i,j]=r_j M_j(x)`, and both stop times match. The target must satisfy `9*b*z=4*a*(v-z)`. Seven labeled branch masses and their likelihood-weighted counterparts are retained; preservation refers to the stated four observers, not unlisted future operations.

## Fifteen exact anchor certificates and analytic interpolation

`CERTIFICATES.json` supplies **15** rational target vectors plus **147** nonzero Q matrix edges. Every other edge is zero. `VERIFY.py` checks each certificate by exact `fractions.Fraction` arithmetic for the full lawful bounds, seedless equation, both probability mass normalizations, each row, each Q column, each P-weighted column, and the two stop times.

Define two *linear* seedless faces

```text
G: b=0, v=z
F: z=a/10, v-z=9b/40.
```

Inside either single chosen face, a nonnegative convex mixture of calibrated triples stays lawful, seedless and calibrated. The source masses, each transport constraint, and stopping times are affine. The construction does not interpolate between distinct seedless faces.

**Part I: 0<=theta<=3/4.** At both theta endpoints `0,3/4`, six G anchors comprise the triangle `(p,q)=(0,0),(1,0),(1,1/2)`, and eight F anchors comprise the quadrilateral `(0,0),(0,1),(1,1),(1,1/2)`. First, for each such anchor vertex, interpolate its *same-face* endpoint triples with `t=4theta/3` and nonnegative weights `(1-t,t)`.

For `q<=p/2` combine G vertices `(0,0),(1,0),(1,1/2)` with barycentric weights `(1-p,p-2q,2q)`.

For `q>=p/2` define `t2=(q-p/2)/(1-p/2)` (denominator at least 1/2), and combine F vertices `(0,0),(0,1),(1,1),(1,1/2)` with weights `((1-t2)(1-p),t2(1-p),t2*p,(1-t2)*p)`.

The weights are nonnegative, sum to 1, and reproduce the required *source* because the normalized source is affine in theta, p and q. On `q=p/2`, either feasible face is sufficient; matching target choices across the switch is not needed for an existential result.

**Part II: 3/4<=theta<=1.** The remaining fifteenth certificate is the F anchor at `(theta,p,q)=(3/4,1,0)`. Together with the four F anchors already at theta=3/4, all four corners of the p/q square are covered. At theta=1, each original source is itself seedless on F, yielding the diagonal transport `diag(M(x))`. Interpolate each corner's F triple between theta=3/4 and 1 with `t=4theta-3`, then combine the four corners `(0,0),(0,1),(1,0),(1,1)` with weights `((1-p)(1-q),(1-p)q,p(1-q),pq)`. This is an exact continuous construction on F.

**Scaling and declaration interpolation.** Mix the normalized triple with seedless identity triples `E1=(1,0,0,0,0,0,0)` and `E0=(0,0,0,0,0,0,0)`, assigning weights `s,g-s,1-g` to `(normalized,E1,E0)`. Both identity flows lie on G and F. This produces the displayed source and keeps all exact calibration identities. Finally mix with the target identity triple using weights `1-h,h`; the new Q is exactly `Q_h`. Nonnegative calibration makes the declaration transform stochastic on positive target rows and preserves both P and Q error probabilities for every d.

**Conclusion:** These two face regimes cover the entire compact cube `(theta,p,q) in [0,1]^3` at eta=1/40, as well as scaling and h. The all-real proof is the positive affine construction plus exact rational vertex identities; finite regression is a consistency check, not an extrapolation.

## Validation and scope

Exact sparse supports were first sought by SciPy HiGHS LP, then the active linear systems were solved over the rationals and the complete resulting certificates checked with exact fractions. The self-contained standard-library checker uses no optimization dependency, and `EXACT_OUTPUT.txt` records the actual local execution: **15 anchor checks and 348 exact regression triples passed**. New result: the previously open **mixed p/q** and full theta rectangle at eta=1/40 is now covered, extending the previous maximal-u-only theorem and low-theta rectangle.

This is a theorem of the finite frozen R5 P/Q-BRC statistical model. Protected P000 / six-axis heartbeat worldview are retained but no new native X6 interpretation is asserted. Formal admission and independent mathematical review remain separate. Native task read reported `BACKEND_IDENTITY_OR_VERSION_MISMATCH / STATUS_DATABASE_UNAVAILABLE`, `operation_sent=false`; the Site gateway reported `research_authority_granted=false`. This branch preserves author-side evidence without claiming an authenticated Owner, CLAIM, Result or Review.

Next: search for an exact all-theta mixed p/q continuation across eta below 1/40, then into the prior open interval `1/40<eta<46/705`; see `NEXT_UNIT.md`.
