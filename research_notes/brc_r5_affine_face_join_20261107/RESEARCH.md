# R5 — Calibrated Blackwell affine-face join theorem

Author-side scientific continuation, 2026-11-07 (Asia/Shanghai). Predecessor: immutable `awdawmip/enterprise-math@194f81437a86b5fa24947d3dedd3e0f9bfed03be`, `research_notes/brc_r5_full_side_rectangle_20261107/RESEARCH.md`, `CONE_EXTENSION.md`, `VERIFY.py`. Frozen scientific pins unchanged: GLOBAL `a01383f825ef9d43b4b754254303298c64041568`, EM `86149263e38c22292c9def1e0f69092efa1be77e`. Current behavioral norms were loaded separately. This mathematical result applies to the frozen four-stage seven-key P/Q-BRC stopping model, with four observers `(e_P,e_Q,T_P,T_Q)`.

## Exact objects and hypotheses

Write the flow as `x=(g,a,b,u,v,w,z)` with likelihood ratio keys `r=(1/10,1/2,3/4,1,5/4,3/2,19/10)`. Legal flows satisfy
```
0 <= a,b <= g <= 1
0 <= u <= 13*a/40+b/80
0 <= w <= 3*a/40+21*b/80
0 <= z <= a/10
0 <= v-z <= 9*b/40
```
A legal flow is seedless LR when `9*b*z=4*a*(v-z)`. The seven affine Q stopping masses `M_i(x)` and two affine stop-time functionals `T_P,T_Q` have their explicit definitions in `VERIFY.py`, retained from the immutable predecessor.

Define the following **convex** polytopes of legal flows:
```
C = { (g,s,s,u,9*s/40,w,0) : 0<=s<=g<=1, 0<=u,w<=27*s/80 }
F = { (g,a,b,u,a/10+9*b/40,w,a/10) : 0<=a,b<=g<=1,
      0<=u<=13*a/40+b/80, 0<=w<=3*a/40+21*b/80 }.
```
Every flow in `F` is seedless, by the exact equality `9*b*(a/10)=4*a*(9*b/40)`. The predecessor's all-real four-parameter cone theorem proves: for each `c in C` there exists a legal `L(c) in F` and a nonnegative seven-by-seven **Q-mass transport** matrix `Q_c` satisfying
```
sum_j Q_c[i,j]      = M_i(L(c))
sum_i Q_c[i,j]      = M_j(c)
sum_i r[i]*Q_c[i,j] = r[j]*M_j(c)
T_P(L(c))=T_P(c), T_Q(L(c))=T_Q(c).
```
The predecessor establishes these via four exact rational corner transports and two successive exact interpolations. We use that exact proved object, including all edge cases, rather than treating convex-hull support equality as pointwise equality.

## New theorem — entire convex join has an exact seedless lift

**For every real `x in conv(C union F)` and every real declaration `d in [0,1]^7`, there exist a legal seedless LR flow `y in F` and row-stochastic `K` preserving exactly `(e_P,e_Q,T_P,T_Q)`. Once `x` is fixed, the *same* `y,K` serve all declarations `d` simultaneously.**

**Proof.** Since `C,F` are nonempty convex sets, `x` can be written `x=(1-t)c+t f`, `c in C, f in F, 0<=t<=1`. Define
```
y=(1-t)L(c)+t*f,
Q=(1-t)Q_c+t*diag(M(f)).
```
The defining linear equalities `z=a/10`, `v-z=9*b/40` and legal inequalities are preserved by convex combination, so `y in F` and hence is seedless LR. Also `Q>=0`. Each of the three transport identities and both time identities is affine in the flow/matrix, so the predecessor's equalities and the diagonal identity transport of `f` imply the corresponding five equalities for `x,y,Q`.

For `M_i(y)>0` set `K_ij=Q_ij/M_i(y)`; when a row mass vanishes set that row of `K` to the identity row. Then `K` is row stochastic. For any `d in [0,1]^7`, `d'=Kd` also belongs to the unit cube, and the calibrated column equations imply
```
e_Q(y,d') = sum_i M_i(y)d'_i = sum_j M_j(x)d_j = e_Q(x,d)
1-e_P(y,d') = sum_i r_i*M_i(y)d'_i
            = sum_j r_j*M_j(x)d_j = 1-e_P(x,d).
```
The stop times are identical by construction. This proves the result for **all real** parameters and declarations, including irrational and boundary values. QED.

## Explicit new five-parameter family and residual

Choose `0<=s<=g<=1, 0<=p,q,t<=1`,
```
c=(g,s,s,27*s*p/80,9*s/40,27*s*q/80,0) in C,
f=(g,s,s,27*s*p/80,13*s/40,27*s*q/80,s/10) in F.
```
The joined FULL_HIST source is
```
x(g,s,p,q,t)=(g,s,s,27*s*p/80,9*s/40+s*t/10,27*s*q/80,s*t/10).
T_P=1+g+49*s/40+27*s*p/160+81*s*q/160+s*t/10
T_Q=1+g+49*s/40+27*s*(p+q)/80+s*t/10
R=9*b*z-4*a*(v-z)=-9*s*s*(1-t)/10.
```
It has an exact single seedless LR lift for every real declaration. The join theorem also supplies flows with `a!=b`, beyond this five-parameter family.

A checked exact witness outside the predecessor cone uses `(g,s,p,q)=(1,1/2,2/3,3/4)`, `t=2/5`, and face anchor `f` with `(g,a,b)=(1,1/2,3/4)`, `u` equal to one third of its legal bound and `w` equal to two thirds of its bound:
```
x=(1,1/2,3/5,217/2400,31/200,443/3200,1/50)
T_P=57031/19200; T_Q=5633/1920
R=-81/500.
```
Thus this exact transported source has `a!=b` and simultaneous `u,w,z>0`.

## Verification, status and next unit

The published `VERIFY.py` extends the predecessor's four rational corner matrices with a Fraction-only transport/interpolation checker. The predecessor already tests 4 certificates, 512 binary declarations and 25 interpolation points. The appended checker tests 1350 additional exact rational convex joins with varied `C` parameters, nonzero `u,w`, multiple `F` anchors, `t=0,1`, intermediate `t`, zero mass and `a!=b`. Every row, Q column, P-weighted column, legality, seedless face, normalization and stop-time equation is checked. The **all-real** conclusion is proved by the analytic argument, not finite extrapolation. `EXACT_OUTPUT.txt` contains the executed separate local full-model checker outcome; independent math review and formal native admission remain pending.

Next question: classify the complement of `conv(C union F)` inside the legal saturated-v polytope `H={x: v-z=9*b/40}`, starting with `a!=b,z=0,u,w>0`. Try a new explicit rational lift and 7x7 calibrated transport; if a proposed affine face fails, distinguish that failure from full seedless infeasibility. Keep the frozen scientific pins and four-observer horizon.

Control observation (2026-11-07): native `em_status` and `em_control_tasks` returned `BACKEND_IDENTITY_OR_VERSION_MISMATCH / STATUS_DATABASE_UNAVAILABLE`, `operation_sent=false`. This note is author-side research evidence, not a CLAIM, Result or mathematical admission.
