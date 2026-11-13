# R5 — full-theta mixed-sign Blackwell prism from a new C_(4/5) chart

Date: 2026-11-08. Evidence: AUTHOR_PROVED / EXACT_FRACTION_EXECUTED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.

Scientific input pins, preserved (not rebased): Global `a01383f825ef9d43b4b754254303298c64041568`; Enterprise Math `86149263e38c22292c9def1e0f69092efa1be77e`. Previous independent author-side frontier: PR #1803 @ `8613b2b8d6721938dfd310a4a1fafb25b6c5c785`. P000 and ACTIVE worldview unchanged.

## Exact new theorem: positive-residual four-parameter box

Use the frozen seven-node P/Q-BRC typed statistical model with likelihood ratios
`r=(1/10,1/2,3/4,1,5/4,3/2,19/10)`, and the same affine node-mass and stopping-time maps given below. For **every real**
`1/100<=t<=1/5, 0<=p,q<=1, 3/4<=theta<=1`, with `kappa=3/4`, put
```
x(t,p,q,theta)=(1,t,1,
  (13*t/40+1/80)*p,
  t*theta/10+27/160,
  (3*t/40+21/80)*q,
  t*theta/10).
```
For each such source there exists a lawful seedless-LR target `y=(g,a,b,u,v,w,z)` on the **single shared chart**
```
C_(4/5) = { z=(2/25)*a,  v-z=(9/50)*b },
```
and a nonnegative declaration-independent 7x7 Blackwell array Q with
```
sum_j Q[i,j] = M_i(y)                              for i=0..6
sum_i Q[i,j] = M_j(x)                              for j=0..6
sum_i r_i Q[i,j] = r_j M_j(x)                      for j=0..6
T_P(y)=T_P(x),  T_Q(y)=T_Q(x).
```
Thus any seven-node terminal decision vector can be pulled through Q, preserving `(eP,eQ,TP,TQ)`. Every real source–target interpolant `x_h=(1-h)x+h*y`, `0<=h<=1`, admits the same observer via `Q_h=(1-h)Q+h diag(M(y))`.

The signed history residual of the source is `R=9*t*(theta-3/4)/10`, strictly positive for `theta>3/4`, and zero at `theta=3/4`. This is the new adjoining positive-residual region beyond the previously proved negative-residual theta prism (PR #1803).

## Explicit model functions and reproducible verification

For `f=(g,a,b,u,v,w,z)` define
```
M0=509*u/900 +47*z/180 +67*(v-z)/162+w/100
M1=13*a/40+b/80-u
M2=(g-a)/2
M3=1-g+a/10+9*b/40-v+191*(u+w)/450+43*z/90+14*(v-z)/81
M4=(g-b)/2
M5=3*a/40+21*b/80-w
M6=u/100+47*z/180+67*(v-z)/162+509*w/900
TP=1+g+3*a/8+5*b/8+u/2+v+3*w/2
TQ=1+g+(a+b)/2+u+v+w.
```
A legal target has `0<=a,b<=g<=1`, `0<=u<=13a/40+b/80`, `0<=w<=3a/40+21b/80` and nonnegative node masses. The chart constraints above imply the seedless residual equation `9*b*z=4*a*(v-z)` exactly.

A JSON map with **16 fully specified exact rational certificates (158 positive transfer edges total)** is stored as zlib+base64 in `CERTIFICATES.zlib.b64`. Decode with `zlib.decompress(base64.b64decode(...))` to recover UTF-8 JSON keyed by `t|p|q|theta`; each item has exact rational `target=[g,a,b,u,w]` and `edges={"i,j":"numerator/denominator"}` using 0-based indices.

The complete independent standard-library `Fraction` verifier in `VERIFY.py` tests every endpoint: nonnegativity, seedless equality, legal capacities, Q/P node normalizations, 7 target-row marginals, 7 source-column marginals, 7 likelihood-weighted columns and both expected stopping times. It also tests 601 exact rational interior reconstructions. `EXACT_OUTPUT.txt` preserves actual local stdout. Linear programming (SciPy HiGHS) was only a discovery tool; candidate supports were solved exactly using rational linear algebra, and the published checker has no optimization or floating point dependence.

## Proof for every real point (not a mesh inference)

Let `a_t=(t-1/100)/(1/5-1/100)`, `a_theta=4*(theta-3/4)`. For a vertex `e=(t_e,p_e,q_e,theta_e)` of the binary 4-cube, assign the product weight
```
W_e=(a_t if t_e=1/5 else 1-a_t)
   *(p if p_e=1 else 1-p)
   *(q if q_e=1 else 1-q)
   *(a_theta if theta_e=1 else 1-a_theta).
```
All weights are nonnegative and total one. The source coordinates are **separately affine in each of t,p,q,theta**, hence `x=sum_e W_e*x_e` identically for all real parameters, including irrational values and boundary points. Let `y=sum_e W_e*y_e`, `Q=sum_e W_e*Q_e`. The target chart `C_(4/5)`, all legal capacity inequalities, node masses, calibrated row/column/weighted equations, and stopping-time maps are affine; thus their certified vertex equations pass through nonnegative mixing without an approximation. This proves the theorem for the full real box.

## Combination with previous exact frontier

PR #1803 already has a separate author-side proof on chart `C_(3/4)` for all `0<=t<=1/5, p,q∈[0,1], 0<=theta<=3/4`, at `kappa=3/4`. Together with this new theorem, these two charts cover
```
1/100 <= t <= 1/5; p,q,theta ∈ [0,1]; kappa=3/4
```
for both signs of the history residual, with a shared seam at theta=3/4. The combination consumes the prior author's exact mathematical proof in its stated scope; our 16 new C_(4/5) certificates independently establish the positive-residual half.

## Reuse, status, and next step

BRC P/Q seven-node observer: REUSE_APPLIED; existing likelihood-ratio weighted mass transport and signed residual observer are used unchanged. The result is for this declared four-dimensional statistical observation, not an unrestricted native X6 future-operation quotient.

Native Researcher-ID: `EM-DIRECT-D41404`, session `MCP-c62e63caf2c546dc999c64ff9b3143aa`, Source research activity `RA-25D3E492799088B30BBD4A1B`. These are real backend-issued identity/activity records but **no active task CLAIM or owner execution authority has been established**. Artifact is therefore submitted as author-side evidence for independent review, not a Result/Review or Working Truth promotion.

Next exact unit: determine the lowest t>0 where full p,q-capacity at theta∈[3/4,1], kappa=3/4 can be covered by C_(4/5), and test alternate charts allowing a bridge to t=0. In exact LP tests t=1/100 was feasible at every endpoint, while t=1/120 failed for p=0,q=1 on this fixed chart; numerical infeasibility is not yet an exact impossibility certificate.
