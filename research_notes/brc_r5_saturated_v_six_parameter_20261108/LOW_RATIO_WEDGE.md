# R5 — New exact lower-ratio diagonal Blackwell wedge (1/4 ≤ b/a ≤ 1/2)

Date 2026-11-08 Asia/Shanghai. Status: author-side theorem proved by exact rational certificates plus convex interpolation; independent review/native admission pending. Frozen scientific pins: global `a01383f825ef9d43b4b754254303298c64041568`, EM `86149263e38c22292c9def1e0f69092efa1be77e`. Immediate predecessor in this same directory: `RATIO_BRIDGE.md` proves **full physical rectangles** for `1/2<=b/a<=1`. This new note expands into a structurally distinct lower-ratio region.

## Exact theorem with a correlated physical diagonal

For all real `0<=s<=g<=1`, `1/4<=eta<=1/2`, `0<=t,theta,h<=1`, set

```
u=s*(13/40+eta/80)*t
w=s*(3/40+21*eta/80)*t
z=s*theta/10
x=(g,s,eta*s,u,9*eta*s/40+z,w,z).
```

Here `u` and `w` traverse **the common fractional-capacity diagonal** of their full physical rectangle, with the same `t`. For every randomized seven-node declaration `d in [0,1]^7`, this FULL_HIST flow admits a legal seedless LR target `y` and a nonnegative calibrated 7×7 Q-mass transport `Q` matching the four observations `(e_P,e_Q,T_P,T_Q)` exactly. The same target also matches every `x_h=(1-h)x+h*y` via `Q_h=(1-h)Q+h diag(M(y))`.

Exact residual:
`R(x)=9bz-4a(v-z)= (9/10)*eta*s^2*(theta-1)<=0`.

The common stopping times are given by the frozen affine formulas, equivalently
`T_P=1+g+(15+34eta)*s/40+u/2+3w/2+z`,
`T_Q=1+g+(20+29eta)*s/40+u+w+z`.

## New rational certificates for eta=1/4

At `g=a=1`, `b=1/4`, `z=0`, `v=9/160`, the two *diagonal* endpoints are `p=q=0` and `p=q=1`.

- Endpoint 00 source `c00=(1,1,1/4,0,9/160,0,0)`; legal seedless target
  `y00=(2183/2913,2183/2913,5761/11652,721/5826,86777/466080,0,2183/29130)`.
- Endpoint 11 source `c11=(1,1,1/4,21/64,9/160,9/64,0)`; legal seedless target
  `y11=(1,19/20,1/5,249/800,7/50,99/800,19/200)`.

The attached `ETA_QUARTER_CORNERS.json` records full exact rational **13-edge** and **9-edge** Q-mass matrices. For each endpoint, `VERIFY_LOW_RATIO.py` executes the exact checks:
`Q[i,j]>=0`;
`sum_j Q[i,j]=M_i(y)`;
`sum_i Q[i,j]=M_j(c)`;
`sum_i r_i Q[i,j]=r_j M_j(c)`;
`T_P(y)=T_P(c)`; `T_Q(y)=T_Q(c)`;
`sum_i M_i(c)=sum_i r_i M_i(c)=1`, likewise for the target. Both targets satisfy the *same linear seedless-face equations*
`z=a/10`, `v-z=9b/40`.

These are **new exact certificates for the fixed eta=1/4 saturated-v source family** and extend the earlier proved lower limit eta=1/2. Numerical linear programming was used only to discover the candidates; the persisted mathematical evidence is the exact rational matrix verification.

## Proof of the all-real diagonal wedge

For real `t in [0,1]`, interpolate these two new `eta=1/4` certificates with weights `1-t,t` to obtain a legal source `c_L(t)`, a seedless target `y_L(t)` in the same affine face F, and calibrated nonnegative matrix `Q_L(t)`. Since the endpoint sources have `(u,w)` equal to either both zero or both full physical capacity, this interpolation yields precisely `u=t*21/64`, `w=t*9/64` at `eta=1/4`.

The immutable eta=1/2 four-corner predecessor supplies `c_H(t),y_H(t),Q_H(t)` by its exact bilinear interpolation at the same `p=q=t`. Every target likewise belongs to F. For `eta in [1/4,1/2]`, set `alpha=4eta-1` and interpolate the two triples with weights `1-alpha,alpha`. Because the physical capacities
`u_max=13a/40+b/80`,
`w_max=3a/40+21b/80`
are *affine in b*, the interpolated source is exactly
`c=(1,1,eta,(13/40+eta/80)t,9eta/40,(3/40+21eta/80)t,0)`.
The calibrated matrix and target remain legal and the target remains in the common seedless affine face F.

For each such source c, form the additional legal seedless endpoint
`c^+=c+(0,0,0,0,1/10,0,1/10)` in F with diagonal identity transport. Use the base `E0=(0,0,0,0,0,0,0)` and `E1=(1,0,0,0,0,0,0)`, also in F. Convex-combine sources with weights `1-g`, `g-s`, `s(1-theta)`, `s theta`, replacing only c by its already constructed target to obtain y and the corresponding convex transport Q. Every coefficient is nonnegative and the four sum to one. Legality is preserved by linear constraints; seedlessness follows from F's linear equations, avoiding any assumption that the entire seedless quadratic hypersurface is convex.

Stopping masses, both stop-time functions, and all three sets of calibrated Q matrix identities are affine; therefore the exact source/target identities persist under each interpolation. Finally `Q_h=(1-h)Q+h diag(M(y))` calibrates `x_h` against the same y. Row normalization gives a stochastic declaration transformer for any real d. This proves the all-real theorem including irrational parameters and boundaries, with a single seedless target independent of declaration.

## Exact irrational-domain proof versus finite regression

`VERIFY_LOW_RATIO.py` reads the two new exact Q matrices from `ETA_QUARTER_CORNERS.json`, imports the old immutable rational eta=1/2 four-corner checker (`BASE_CERTIFICATES.py`), checks all two new endpoint identities, and executes **729 distinct exact Fraction parameter cases** over g,s,eta,t,theta,h (g takes 0,1/2,1; s takes 0,g/2,g). Each case verifies 7 row, 7 Q-column and 7 likelihood-weighted P-column relations, nonnegative Q entries, physical flow legality, full residual and both times, h interpolation and 3 declaration vectors. The algebraic nonnegative-interpolation proof above establishes all-real coverage; samples are independent reproducibility checks. Local stdout is in `EXACT_LOW_RATIO_OUTPUT.txt`; the original predecessor source was also published verbatim at an immutable GitHub ref in this directory.

For an interior witness `g=s=1,eta=3/8,t=1/2,theta=1/2,h=0`:
```
x=(1,1,3/8,211/1280,43/320,111/1280,1/20)
y=(442741/466080,109957/116520,62683/155360,6788287/37286400,
   3451753/18643200,1059/12800,109957/1165200)
(T_P,T_Q)=(473/160,1967/640)
R(x)=-27/160; R(y)=0
```

## Exploratory signal and next exact question

A SciPy/HiGHS **floating linear-programming search** constrained to this *specific* affine seedless face F found the exact candidate Q matrices at eta=1/4 diagonal corners 00,11. At the off-diagonal physical corners `p=0,q=1` and `p=1,q=0`, the same numerical feasibility setup returned no candidate. **This is only an exploratory signal for the chosen linear face F**, not an exact impossibility certificate and not a verdict on other seedless representations. The bounded next task is to derive a rational Farkas dual for either off-diagonal face-restricted LP or obtain a new exact off-diagonal certificate in another seedless face. Both outcomes inform whether the lower-ratio diagonal wedge can expand into a full physical rectangle.

The full four-observer pointwise FULL_HIST vs seedless LR mother question remains open. GitHub identity `awdawmip` had repository admin permission; native task/status returned `BACKEND_IDENTITY_OR_VERSION_MISMATCH / STATUS_DATABASE_UNAVAILABLE` and `operation_sent=false`; Site `research_authority_granted=false`. Materials are author-side `PORTABLE_ONLY / UNREVIEWED / NOT_ADMITTED`, with no formal CLAIM.
