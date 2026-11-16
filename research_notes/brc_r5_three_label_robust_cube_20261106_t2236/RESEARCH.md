# R5 — Constructive real four-observer LR cube with three declaration keys

**Research date:** 2026-11-06 (Asia/Shanghai). **Status:** AUTHOR_PROVED / EXACT_FRACTION_EXECUTED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.

**Scientific pins:** GLOBAL `a01383f825ef9d43b4b754254303298c64041568`; Enterprise Math `86149263e38c22292c9def1e0f69092efa1be77e`. Current behavioral rules were read separately from canonical main. The four-stage positive-kernel P/Q-BRC tree is an auxiliary, scope-typed observer model, not a claim about native Heartbeat X6 dynamics.

## Theorem — a 3.415-fold enlargement of a four-observer LR cube

Use the frozen model with delta=1/4, observer `W=(eP,eQ,TP,TQ)`, where `eQ=Q(declare P)` and `eP=P(declare Q)`. Let

```text
W* = (161801/180000, 6499/18000, 267/80, 137/40).
h  = 1/1000.
```

Every **real** point, including the boundary, in the closed cube `||W-W*||_infinity <= h` is realized by an exact, legal **seedless likelihood-ratio (LR)** policy. One fixed common timing choice suffices for the entire cube:

```text
g = u0 = 1,    u1 = v = 33/40.
```

At the time-3 LR keys `(1/2,1,3/2)`, choose common continuation probabilities `z_j=X_j/V_j`, with `V=(1073/3200,457/1600,933/3200)` the Q incoming masses. At stopped LR keys, use only `a=1/10, b=1/2, c=1` for declaring P, each with a common probability across all histories bearing that key. All other stopped keys declare Q.

For any target W, write `dp=eP-eP*, dq=eQ-eQ*, sp=TP-TP*, sq=TQ-TQ*`, and define the exact affine inverse:

```text
X2 = 51/1000 - (111/70)(dp+dq) + sp - (17/35)sq
X0 = (10v-3)/40 + 2(sq-sp) + X2
X1 = (4-3v)/4 + 2sp - sq - 2X2

Ea = 51/250 + (23/100)(dp+dq) - (5/9)sp + (21/25)sq
D  = eP+eQ-1
Eb = 2D - (9/5)Ea
E1 = eQ-Ea-Eb
```

Here `E_r` is stopped Q mass at LR key r assigned to declaration P. For each active key use declaration probability `E_r/M_r`, where `M_r` is its Q stopped mass; the exact positivity check below ensures the denominator is nonzero. All inactive keys declare Q.

## Exact model and observer identities

Use the frozen conditional Q kernels

```text
q3[0] = (13/20,1/5,3/20)
q3[1] = (1/40,9/20,21/40)
q4[i,0] = (509/900,382/900,9/900), i=0,1
q4[0,1] = (47/180,43/90,47/180)
q4[1,1] = (67/162,14/81,67/162)
q4[i,2] = (9/900,382/900,509/900), i=0,1
```

The time-2 LR keys are `(3/4,5/4)`, time-3 `(1/2,1,3/2)`, and terminal `(1/10,1,19/10)`. Set `x_ij=(u_i/2)q3[i,j] X_j/V_j` for `u=(1,v)`. The **seven-key** stopped Q masses are assembled by adding `(1-v)/2` at time-2 key `5/4`, `V_j-X_j` at time-3 keys, and `sum_ij x_ij q4[i,j,z]` at terminal keys. At equal key `1` all contributions are pooled before selecting the single declaration probability. This retains the original time/history provenance in the model while using the declared four-coordinate observer for the output.

These kernels obey their exact conditional LR-moment equations. For all legal X, `sum_r M_r=1` and `sum_r r M_r=1`. The observer readout is

```text
TQ = 2 + (1+v)/2   + X0+X1+X2
TP = 2 + (3+5v)/8 + X0/2+X1+3X2/2
eQ = Ea+Eb+E1
eP = 1-Ea/10-Eb/2-E1.
```

Direct substitution of the displayed inverse returns the four prescribed coordinates exactly.

## All-real feasibility proof by rational affine margins

Every essential legality slack is affine in `(dp,dq,sp,sq)`, so its minimum on the real closed cube occurs at a vertex. `VERIFY.py` checks all 16 vertices using standard-library `Fraction` and obtains the following **exact global minimum slacks**, all strictly positive:

| Slack | Minimum across the entire real cube |
| --- | ---: |
| X0 | 24719/140000 |
| X1 | 38203/140000 |
| X2 | 811/17500 |
| V0-X0 | 82531/560000 |
| V1-X1 | 1/280000 |
| V2-X2 | 132107/560000 |
| Ea | 18193/90000 |
| Eb | 18377/125000 |
| E1 | 683/1125000 |
| M_a-Ea | 9574109/57582000000 |
| M_b-Eb | 1007/2800000 |
| M_1-E1 | 2502094771/14395500000 |

Because `0<X_j<V_j`, common LR continuation probabilities lie in (0,1). The active declaration masses are positive and below their aggregate stopped masses. All other stopped masses are nonnegative from the positive frozen kernels, and inactive declaration masses vanish. Hence every point in the **entire continuous real cube** has a valid seedless LR realization. QED.

The preceding best certified cube at the same center had half-radius `145/495224` with `u1=57197/61903`, `X2=0`, and just two declaration keys. The new half-radius improves its size by the **exact factor**

```text
(1/1000)/(145/495224) = 61903/18125 = 3.415337931...
```

This enlargement uses independent `X2` flow and a declaration coordinate at the pooled key `1`. It establishes a larger **constructive lower bound** on the LR image and makes no global optimum assertion.

## Verification, source status, and follow-up

`VERIFY.py` uses exact rational arithmetic only. It checks every frozen time-3/time-4 row for positivity, unit sum and conditional LR moment; all 16 vertices of the legality cube; 625 rational targets as an independent recovery check; stopped-mass normalization and LR moment; and exact restoration of the original four observations. Output in `EXACT_OUTPUT.txt`: `PASS_EXACT_R5_FIXED_FLOW_THREE_LABEL_CUBE_1_OVER_1000`. The universal all-real conclusion comes from affineness plus the 16 exact margins, rather than finite-grid extrapolation.

This uses the existing seven-bin BRC stopped-mass/provenance representation; no new shared tool is claimed. The original mother question whether `O4(FULL_HIST)=O4(seedless LR)` over **all** policies and four-dimensional observations remains open. Previous strict separation after adding a fifth stopped-mass observer is a separate scoped result.

**Next discriminating unit:** optimize the fixed-`v` three-key affine section beyond this lower bound, or seek a rational FULL_HIST four-observer witness outside this certified cube, build its exact seven-variable `K(W)`, and determine whether `F=(A+B)J-X1(alpha A+beta B)` can vanish for any real seedless LR policy. Track positive and negative outcomes under their precise observer scope. Native active R5 owner/CLAIM and independent mathematical review require separate Source evidence.
