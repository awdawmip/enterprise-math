# R5 — two exact 14-edge Blackwell charts cover a physical segment across a support-change facet

**2026-11-09 (Asia/Shanghai)**. Author-side theorem, exact rational certificate executed locally; independent mathematical review and formal Result not asserted. Source: frozen seven-LR-node P/Q-BRC statistical observer. Scientific pins unchanged: global `a01383f825ef9d43b4b754254303298c64041568`; Enterprise Math `86149263e38c22292c9def1e0f69092efa1be77e`. Direct source predecessors: PR #1839 at `bede5ad6f9624b476bae9df16578509f598afe22`, and PR #1841 at `9a90b8af0a25efd04ade5cde85c4224b60b1741d`. This is a construction in the frozen statistical model, not a new X6 dynamic claim.

## Exact question and theorem

In PR #1841, a fixed 14-edge affine coupling is positive in a physical open box around (x_0,y_0), but its entry E_(4,2) becomes negative for the independent lawful (x_1,y_1) from PR #1831. Can the two instances be joined continuously by 14-edge couplings **without retaining that fixed support**?

Let the flow coordinates be (g,a,b,u,v,w,z) and LR nodes

```
r=(1/10, 1/2, 3/4, 1, 5/4, 3/2, 19/10).
x0=(999/1000, 1/6, 999/1000, 1/20, 29/240, 11/160, 1/120).
y0=(871/1000, 9/40, 5/6, 273/4000, 21/100, 143/1000, 9/400).
x1=(1, 1/10, 1, 27/800, 1/100, 27/400, 1/100).
y1=(4673/6400, 1311/6400, 4673/6400, 38759/512000,
    47301/256000, 103999/512000, 1311/64000).
```

For **every real lambda in [0,1]**, put x(lambda)=(1-lambda)x0+lambda*x1 and y(lambda)=(1-lambda)y0+lambda*y1. Then x(lambda) is lawful FULL_HIST with g=b, y(lambda) is lawful seedless LR on the F face, the two stopping-time coordinates agree, and a nonnegative declaration-independent Blackwell Q transport with **at most 14 positive edges** exists. No integrality or rationality is required of lambda.

The support is **one of two explicitly given 14-edge sets**, switched at lambda=1/2:

```
S_A = (0,0) (6,6) (0,1) (2,1) (0,2) (2,2) (3,2)
      (5,2) (3,3) (1,5) (2,5) (4,5) (5,5) (6,5).
S_B = (0,0) (6,6) (0,1) (2,1) (0,2) (2,2) (3,2)
      (3,3) (0,5) (1,5) (3,5) (4,5) (5,5) (6,5).
```

They share 12 of 14 edge positions. For 0<=lambda<=1/2, use S_A and the affine interpolation between certificates A0, AH below with parameter 2*lambda. For 1/2<=lambda<=1, use S_B and the interpolation between BH, B1 with parameter 2*lambda-1. At the switch both are valid nonnegative transports, though generally different joint distributions.

## Full proof

The source and target mass map M and the stopping-time maps T_P,T_Q are **affine** in the seven flow coordinates (exact formulas are in VERIFY.py, preserved from frozen R5). All physical capacity inequalities are affine; consequently they hold along the segment because the endpoints satisfy them. Both endpoints have g=b in the source. Both target endpoints lie on the same linear seedless F face z'=a'/10 and v'-z'=9b'/40; throughout the segment these identities hold and imply the nonlinear seedless equation 9b'z'=4a'(v'-z'). At each endpoint T_P(x)=T_P(y), T_Q(x)=T_Q(y); affine dependence gives these equalities throughout the segment.

Write mu=M(y(lambda)), nu=M(x(lambda)). A Q-weighted Blackwell transport is E>=0 such that

```
sum_j E[i,j] = mu[i]          (7 row equations)
sum_i E[i,j] = nu[j]          (7 column equations)
sum_i r[i]*E[i,j] = r[j]*nu[j] (7 column-LR moment equations).
```

All 21 right-hand-side values depend **affinely** on lambda. The four endpoint certificates in VERIFY.py specify nonnegative rational E at lambda=0,1/2,1/2,1, on S_A,S_A,S_B,S_B respectively. The program checks every one of the 21 equations for all four certificates *exactly* with `fractions.Fraction` and checks lawful capacities, the F-face seedless identities, normalized Q/P mass and both stopping times. Each support has 14 positions. Convexly interpolating the two A certificates or the two B certificates gives nonnegative E for every real lambda in the respective half interval and preserves all 21 equations. This completes the all-real proof including the switch and endpoints; it is not a finite-sampling extrapolation.

The four endpoint certificates are written **literally** as ordered vectors A0, AH, BH, B1 in VERIFY.py, in the respective S_A or S_B support order. Positive-edge counts are 14, 14, 14, and 12; the minimum entry at B1 is zero. Execution output is retained in EXACT_OUTPUT.txt.

## Sharp witness against retaining the old chart

The PR #1841 fixed-chart E_(4,2) is 13/18400 at lambda=0 and -2109829/147200000 at lambda=1. Since that chart is affine, the entry first vanishes exactly at

```
lambda_* = 104000/2213829  (~0.0469774).
```

Thus **the original support fails well before the switching time 1/2**, while the new two-support construction remains nonnegative throughout. This positively repairs that specific support bottleneck without changing source/target strategies.

## Scope, reusable method and next question

This proves a continuous one-dimensional physical connection across an explicit chart obstruction, not a uniform 14-edge theorem over all lawful g=b source/seedless-target pairs. It supplies an exact reusable method: seek two support sets whose affine endpoint transport cones overlap on a rational cut, then glue using nonnegative interpolation; solve the relevant 21 equations in exact arithmetic before publishing.

Next investigate whether a *finite atlas of <=14-edge support cones* covers a physically meaningful higher-dimensional subset of the time-matched F-face stratum, or construct one lawful physical marginal pair requiring 15 positive edges. Keep the exact R5 observer and frozen task science; independent review of the predecessor all-flow proof (#1831) remains pending. No activity, owner, CLAIM, Result or independent review is inferred from this author artifact.
