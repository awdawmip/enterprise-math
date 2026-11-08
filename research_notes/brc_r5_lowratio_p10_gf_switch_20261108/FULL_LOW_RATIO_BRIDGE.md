# R5: Complete low-ratio maximal-u physical corner for every eta and theta

2026-11-08. **New stronger author-proved theorem**, extending the same folder's `RESEARCH.md`. Frozen scientific pins unchanged: global `a01383f825ef9d43b4b754254303298c64041568`, EM `86149263e38c22292c9def1e0f69092efa1be77e`. Source matrices are the three exact rational anchors `G0,G34,F23` in `CERTIFICATES.json`; seven-node model and Blackwell calibration equations are in `RESEARCH.md`.

## Theorem: entire low-ratio maximal-u, zero-w source prism

For **all real** `0<=eta<=1/40`, `0<=theta<=1`, `0<=s<=g<=1`, `0<=h<=1`, set

```text
x=(g,s,eta*s,s*(13/40+eta/80),s*(9eta/40+theta/10),0,s*theta/10).
```

There exist a lawful **seedless LR** flow `y` and a **single nonnegative calibrated seven-by-seven Blackwell kernel** `Q` which, for every seven-component terminal declaration `d in [0,1]^7`, realize precisely the four FULL_HIST observers `(e_P,e_Q,T_P,T_Q)` of the interpolated source `x_h=(1-h)x+h*y`. The kernel and target are chosen from the flow parameters, independent of d. All boundary parameters and irrational real parameters are included.

### Proof: two overlapping triangular seedless faces

First put `g=s=1,h=0` and let `lambda=40 eta in [0,1]`. The normalized source `x_eta(theta)` is **jointly affine in (eta,theta)**. In particular, if `x0(t)=x_0(t)`, all `x0(t)` lie on both seedless faces at t=1, and on G for all t (because b=0,v=z). At `theta=1`, every `x_eta(1)` lies on F since z=a/10 and v-z=9b/40.

Let `I(t)=(x0(t),x0(t),diag(M(x0(t))))` be the identity triple. Let `(x_k,y_k,Q_k)` denote the three exact anchor triples in `CERTIFICATES.json`.

**G lower and upper edges.** Form
```text
G_lower(lambda)=(1-lambda)*I(0)+lambda*G0,
G_upper(lambda)=(1-lambda)*I(1)+lambda*G34.
```
(Triples are combined componentwise.) The G_lower source is `x_eta(0)`; the G_upper source is `x_eta(theta_G)` with
```text
theta_G(lambda)=1-lambda/4.
```
Both targets lie on the same linear seedless face `G={b=0,v=z}`. For `0<=theta<=theta_G`, combine G_lower and G_upper with weight `theta/theta_G`. Since `theta_G>=3/4>0`, these are nonnegative convex coefficients. The resulting source is exactly `x_eta(theta)`, the target stays lawful seedless on G, and Q stays calibrated.

**F lower and upper edges.** Form
```text
F_lower(lambda)=(1-lambda)*I(1)+lambda*F23,
F_upper(lambda)=identity triple of x_eta(1).
```
Their sources are `x_eta(theta_F)` and `x_eta(1)`, where
```text
theta_F(lambda)=1-lambda/3.
```
Both targets lie on the linear seedless face `F={z=a/10,v-z=9b/40}`. For `lambda>0`, any `theta_F<=theta<=1` is obtained by weights `1-t,t` with `t=(theta-theta_F)/(1-theta_F)`. At `lambda=0`, the G construction already covers all theta, so division by zero is never used.

**Complete real-parameter coverage.** The two intervals overlap because
```text
theta_F = 1-lambda/3 <= 1-lambda/4 = theta_G.
```
Therefore their union covers all `[0,1]` for every `eta in [0,1/40]`. At every point the selected target stays on **one** of the two linear seedless faces, and all row-Q/column-Q/likelihood-weighted column-P/time identities are preserved under convex mixing. This is an exact constructive universal proof; the proof does not rely on floating-point LP coverage.

For general `0<=s<=g<=1`, combine the normalized source/target/kernel triple with identity triples at `E1=(1,0,0,0,0,0,0)` and `E0=(0,0,0,0,0,0,0)` with weights `s,g-s,1-g`. Both seedless faces contain E0 and E1. For arbitrary `h`, replace source by `(1-h)x+h*y` and Q by `(1-h)Q+h*diag(M(y))`. The target still lies on its chosen seedless face; branch masses, the two likelihood measures and both stop times are preserved exactly. The declaration map in `RESEARCH.md` applies to **every** `d`.

## Exact tests and evidence

`VERIFY_FULL.py` builds these two wedges directly from the three saved anchor transports and the identity triples. An independent local Python `fractions.Fraction` checker executed 450 exact source/target/transport cases spanning eta=0,1/1000,1/160,1/80,1/40, including both moving face boundaries, overlap interiors, theta=0/1 and g/s/h boundaries. All passed. The exact output is in `EXACT_FULL_OUTPUT.txt`. The all-real claim is proved by the displayed nonnegative coefficients and exact anchor identities; finite checks validate implementation.

**Research consequence.** The entire eta/theta domain of this specified maximal-u/zero-w corner is now settled within R5, including the previous unfinished `0<eta<1/40,theta>3/4` strip. The mother problem remains the full physical p/q rectangle and arbitrary lawful FULL_HIST flows. The remaining next unit is revised in `NEXT_UNIT.md`.

This work remains author-side evidence on the Draft PR: independent review, native Owner/CLAIM, Result and Working Truth admission are separate controls. Prior native Source status calls returned `BACKEND_IDENTITY_OR_VERSION_MISMATCH / STATUS_DATABASE_UNAVAILABLE`.
