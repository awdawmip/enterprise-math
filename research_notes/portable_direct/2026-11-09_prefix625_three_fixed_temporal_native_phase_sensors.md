# PREFIX-625 — Three fixed native phase sensors at two adjacent times suffice, and three is sharp

Date 2026-11-09. Status: **author-side exact theorem, checker and evidence; independently reviewable, not formally admitted**. Science pin `awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d`. Original X6 STAR, weights `(1,1,1,1,0,0)`, four-point probe `d=e4+e11+e14+e32`, 48-phase, 96-port/576-action original BRC. Uses author-side PREFIX-617/620 eight-state intertwiner and PREFIX-624 two-consecutive-full-phase native port decoder.

## Exact observation question

Unknown `a,b>=0`, probe amplitude `lambda>0` and subsequent nonnegative gates; known relative tail time `t>=0`. A fixed sensor set measures the **same original phase indices** at the two consecutive times `t` and `t+1`. The goal is complete phase-state reconstruction at both times and recovery of the intervening gate. Time is original discrete transition index, not physical heartbeat duration.

## Theorem 625.1 — exact minimum 3 fixed sensors in a two-frame window

The original phase sensor set **`S={3,4,17}`**, read at times `t,t+1`, reconstructs both 48-phase states and the unknown gate **for every t>=0 and every nonnegative gate sequence**. For every fixed `t>=2`, two fixed original phase sensors (four scalar readings in two frames) are insufficient. Thus `3` is the sharp uniform minimum for this observation model.

### Explicit decoder

The original BRC eight-state intertwiner gives

`x_t=H_C c_t+H_B w_t`,

`c_t=theta_t(e_((t+2)%4)+e_((t+3)%4)), theta_t=4*2^t*lambda`,

`w_(t+1)=(4(q_(t+1)+3)w_(t,3),w_(t,0),w_(t,1),w_(t,2))`.

The exact nonnegative original-phase matrices are sparse:

`H_C` column supports `(2,3,15), (5,28,29), (27,38,39), (16,17,41)`.

`H_B` columns `{3:1,14:1,15:1}, {17:2,40:2,41:2}, {26:4,27:4,39:4}, {4:4,5:8,29:8}`.

Let `(a,b,c)=(x_t[3],x_t[4],x_t[17])`, `(A,B,C)=(x_(t+1)[3],x_(t+1)[4],x_(t+1)[17])`. Always put `w3=b/4,w2=B/4` and `r=t mod 4`:

| r | w0 | theta | w1 | q_(t+1) |
|---|---|---|---|---|
| 0 | `a` | `(C-2a)/2` | `(c-theta)/2` | `(A-2theta)/(4w3)-3` |
| 1 | `C/2` | `a-w0` | `(c-theta)/2` | `(A-2theta)/(4w3)-3` |
| 2 | `C/2` | `a-w0` | `c/2` | `A/(4w3)-3` |
| 3 | `a` | `(C-2a)/2` | `c/2` | `A/(4w3)-3` |

The initial four-dimensional sensitive state is `w_0=(lambda(b+3),lambda(a+3),lambda,lambda/2)`, with every coordinate positive. Each BRC update shifts coordinates and multiplies one by `4(q+3)>0`, so `w3>0` at every time. Thus all divisions are valid. Substitute into the exact row supports to verify the table. With `theta,w,q` recovered, lift the two full states by the fixed `H_C,H_B` matrices, proving the upper bound. This inverse is exact rational algebra; no generic rank assertion is needed for sufficiency.

### Universal lower bound for two sensors

At every fixed `t>=2`, the attainable five-coordinates `(theta_t,w_t)` contain an open subset of positive `R^5`. At `t=2`, their explicit dependence on free positive `lambda,a,b,q1,q2` is

`(16lambda,4(q2+3)lambda,2(q1+3)lambda,(b+3)lambda,(a+3)lambda)`.

This has nonsingular triangular Jacobian after selecting `lambda`; hence it parametrizes an open five-dimensional set. For larger `t`, fixing all additional gates gives an invertible BRC cyclic update on `w` and a positive scaling on `theta`; the open reachable set persists. The embedding `x_t=H_Cc_t+H_Bw_t` is rank 5 at each residue.

Now fix even the next gate `q`. At two fixed sensor positions, the four readings (two times times two sensors) are a **4×5 linear map** of the five state coordinates `(theta_t,w_t)`. Its nontrivial kernel gives different nearby admissible phase states with the same four readings. Thus two sensors cannot recover the complete phase state. Together with the explicit inverse for three sensors, minimality follows. ∎

## Corollary 625.2 — latest labelled action flows from three frames

Read the fixed triple at `t-1,t,t+1`. Applying the two-frame reconstruction to both adjacent pairs obtains the full phase vectors at all three times and the newest gate. PREFIX-624's original dual-row phase decoder uses `x_(t-1),x_t` to obtain all **96 source ports at t**. Therefore every original 576 labelled action flow for the step `t->t+1` equals its reconstructed nonnegative source-port mass times the actual edge weight. With the known original initial embedding, the complete three-sensor time trace also determines all earlier labelled one-step actions. No claim that just the single endpoint frame stores ancestry is made.

## Reproducible original BRC evidence

`PREFIX625_three_temporal_sensors_checker.py` independently rebuilds the original phase kernel and the sparse intertwiner, verifies 40 affine basis cases (two gate endpoints, five state generators, four time residue classes), and runs 120 deterministic rational nonnegative experiments. All **2,131** adjacent-pair inversions, **204,576** phase-coordinate equalities and **2,131** gate recoveries pass. The exact six-parameter time-pair Jacobian determinants for `S={3,4,17}` at `q=1,w3=1` across residues 0..3 are `(256,-256,-256,256)`. An exhaustive finite *witness search* over the 560 triples of 16 potentially active phase positions finds 24 with full generic Jacobian rank in all residues; this check is supplementary, not the proof of global minimality.

Theorems apply to this native positive-BRC family and exactly declared temporal sampling semantics. No general physical clock or space-dimensionality reinterpretation, constant-bit-cost output promise, native Result, independent Driver review, Working Truth or Foundation promotion follows.

## Next

Find a minimal time-window/spatial-sensor tradeoff for reconstructing **all 576 labelled action flows**, rather than just consecutive phase states, with unknown initial calibration. Study missing readings/unknown time residue and exact bit-cost bounds. Retain P000, provenance and future-operation observation scopes.
