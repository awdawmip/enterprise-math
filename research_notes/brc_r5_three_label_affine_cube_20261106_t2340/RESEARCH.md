# R5 — A 15% larger all-real four-observer seedless LR cube

Research date: 2026-11-06, Asia/Shanghai. Status: **AUTHOR_PROVED / EXACT_FRACTION_EXECUTED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY**.
Frozen science: GLOBAL `a01383f825ef9d43b4b754254303298c64041568`; Enterprise Math `86149263e38c22292c9def1e0f69092efa1be77e`. Latest reused R5 parent: `3c1e0dae02b92a4b377461e7e6ec157a67ebfc42` (prior cube radius 1/1000). The auxiliary four-stage P/Q-BRC experiment is not an asserted native X6 physical dynamics theorem.

## Theorem (explicit 15% larger continuous cube)

In the frozen strictly positive four-stage P/Q experiment at delta=1/4, fix the seedless likelihood-ratio (LR) timing policy `g=u0=1, u1=33/40`. For the observer
`W=(eP,eQ,TP,TQ)`, with `eQ=Q(declare P)` and `eP=P(declare Q)`, set

```
W* = (161801/180000, 6499/18000, 267/80, 137/40)
h = 23/20000.
```

Then **every real target** in the closed cube `||W-W*||infinity <= h`, including all boundaries and irrational targets, is attained by a legal seedless LR policy. The certified half-radius improves the preceding `1/1000` by the exact factor `23/20=1.15`. This is a constructive lower bound, with no assertion of global maximality.

Write `t=(W-W*)/h`, so each real component `t_i` belongs to `[-1,1]`. Define two free affine inverse coordinates

```
X2 = (51487 - 1824*t0 - 1824*t1 + 1150*t2 - 559*t3)/1000000
Ea = (204079 + 264*t0 + 264*t1 - 639*t2 + 967*t3)/1000000
```

and recover the remaining coordinates exactly by

```
v = 33/40
tp = TP - (2 + (3+5*v)/8)
tq = TQ - (2 + (1+v)/2)
X0 = X2 + 2*(tq-tp)
X1 = 2*tp - tq - 2*X2
D  = eP+eQ-1
Eb = 2*D-(9/5)*Ea
E1 = eQ-Ea-Eb
```

At the stopped LR keys `a=1/10, b=1/2, 1`, assign Q declaration-to-P masses `Ea,Eb,E1` respectively. At every other stopped LR key assign zero. A single declaration probability `E_r/M_r` is used across all histories with the same LR key, as required by the seedless LR class.

## Frozen transition laws and likelihood-ratio mass construction

The time-2 LR keys are `r2=(3/4,5/4)`; time-3 keys `r3=(1/2,1,3/2)`; terminal keys `r4=(1/10,1,19/10)`. Frozen conditional Q kernels are

```
q3[0] = (13/20, 1/5, 3/20)
q3[1] = (1/40, 9/20, 21/40)
q4[i,0] = (509/900, 382/900, 9/900), i=0,1
q4[0,1] = (47/180, 43/90, 47/180)
q4[1,1] = (67/162, 14/81, 67/162)
q4[i,2] = (9/900, 382/900, 509/900), i=0,1.
```

Every row is strictly positive, sums to one and has the relevant exact conditional likelihood-ratio moment. Set

```
V_j = (q3[0,j] + v*q3[1,j])/2
V = (1073/3200,457/1600,933/3200)
x_ij = (u_i/2)*q3[i,j]*X_j/V_j, u=(1,v)
M_(5/4) += (1-v)/2
M_(r3[j]) += V_j-X_j
M_(r4[z]) += sum_{i,j} x_ij*q4[i,j,z].
```

Pool the contributions at repeated LR key 1. These definitions imply `sum_r M_r=1` and `sum_r r*M_r=1` and exactly the frozen readout identities

```
TQ = 2+(1+v)/2 + X0+X1+X2
TP = 2+(3+5*v)/8 + X0/2+X1+3*X2/2
eQ = Ea+Eb+E1
eP = 1-Ea/10-Eb/2-E1.
```

Substitution of the displayed inverse returns the requested W componentwise.

## Universal feasibility certificate

All 12 conditions `X_j>=0`, `V_j-X_j>=0`, `Ea,Eb,E1>=0` and `M_a-Ea, M_b-Eb, M_1-E1>=0` are **affine in t**, because `v` is fixed. Each therefore attains its global minimum on `[-1,1]^4` at one of the 16 vertices. Executed `Fraction` checker `VERIFY.py` obtained:

| Slack | Exact minimum over all 16 vertices |
|---|---:|
| X0 | 88099/500000 |
| X1 | 67737/250000 |
| X2 | 4613/100000 |
| V0-X0 | 292073/2000000 |
| V1-X1 | 21/1000000 |
| V2-X2 | 469437/2000000 |
| Ea | 40389/200000 |
| Eb | 730087/5000000 |
| E1 | 2393/22500000 |
| M_a-Ea | 1207849/68550000000 |
| M_b-Eb | 31/2000000 |
| M_1-E1 | 298306313/1713750000 |

All are positive; the **smallest is 31/2000000**. Consequently `0<X_j<V_j` and the pooled LR declaration probabilities lie in (0,1) for the three active keys throughout the entire real cube. All inactive keys declare Q. This is an exact legal seedless LR witness for every target W in the cube. QED.

## Evidence and scope

The published checker is standard-library Python `fractions.Fraction` only. It checks every conditional Q kernel's unit sum, strict positivity and conditional LR moment; the mass normalization and first LR moment; all 16 vertex minima; 625 additional exact rational points; and exact reconstruction of all four observer coordinates. The actual program output is in `EXACT_OUTPUT.txt`, ending with `PASS_EXACT_R5_THREE_KEY_CUBE_RADIUS_23_OVER_20000`. The all-real conclusion follows from affine corner extrema and the exact inverse, not from extrapolation of the 625 grid cases.

This improves one constructive **four-observer** LR inner region. It neither resolves the R5 mother question `O4(FULL_HIST)=O4(seedless LR)` globally nor changes the earlier **five-observer** strict separation statement. Formal active owner/CLAIM and independent mathematical review must follow actual Source authority rather than author-side persistence.

## Next scientific unit

At fixed `v=33/40`, characterize the maximal center cube in the entire convex polytope of `(X0,X1,X2,Ea,Eb,E1)` (without requiring a shared affine inverse). A rational upper certificate together with explicit 16-corner policies would determine its exact Chebyshev radius. In parallel, seek a rational FULL_HIST four-observer W outside certified LR inner bounds, build full seven-variable `K(W)`, and test quadratic `F=(A+B)J-X1(alpha*A+beta*B)` for real zero / strict-sign separation. Keep source pins and the four-observer readout unchanged.
