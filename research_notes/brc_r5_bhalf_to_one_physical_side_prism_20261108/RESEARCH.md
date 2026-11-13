# R5: four-real-parameter full physical side-flow Blackwell lift for 1/2 ≤ b ≤ 1

Date: 2026-11-08 (Asia/Shanghai). Frozen science GLOBAL `a01383f825ef9d43b4b754254303298c64041568`, EM `86149263e38c22292c9def1e0f69092efa1be77e`, unchanged. Locked P000 and ACTIVE worldview unchanged. This is author-side exact evidence in the seven-likelihood-key, four-stage P/Q-BRC **probabilistic decision model**, not a physical heartbeat simulator or theorem admission.

## New all-real four-parameter theorem

For **all real** `b in [1/2,1]`, `p,q,t in [0,1]` and **every** real declaration `d in [0,1]^7`, define the FULL_HIST flow

```
U(b)=13/40+b/80, W(b)=3/40+21b/80
x(b,p,q)=(g,a,b,u,v,w,z)=(1,1,b,p U(b),9b/40,q W(b),0).
```

There exists one legal seedless LR target flow `y(b,p,q)` and one nonnegative calibrated seven-key Blackwell Q-mass transfer, independent of `d`, such that the FULL_HIST flow `x_t=(1-t)x+t y` with arbitrary declaration `d` has **exactly the same four observations** `(e_P,e_Q,T_P,T_Q)` as that seedless LR target with a stochastic transformed declaration. In particular, the claim includes the entire **physical legal (u,w) side-flow rectangle for each fixed b** within the specified source face `g=a=1,v=9b/40,z=0`. Source history residual `R(x)=9bz-4a(v-z)=-9b/10 < 0`; targets have `R(y)=0`.

The underlying likelihood ratios are `r=(1/10,1/2,3/4,1,5/4,3/2,19/10)`. The complete frozen seven-key stopping Q-mass function `M_i(f)` and stopping times `T_P=1+g+3a/8+5b/8+u/2+v+3w/2`, `T_Q=1+g+(a+b)/2+u+v+w` are reproduced in the actual Python checker. All legal flow constraints are linear.

## Exact eight-corner certificate construction

At b=1/2, use the four certified rational target corner flows and full nonnegative 7x7 Q transport matrices from predecessor `576ab9f0e46f593c91a4abdc7e20e10c00117fa0`, `research_notes/brc_r5_full_physical_side_rectangle_20261108/VERIFY.py` (Q supports of 14,13,13,9 nonzero entries). The source physical capacities are `U=53/160, W=33/160`. At b=1 use the four independently encoded rational matrices from predecessor `194f81437a86b5fa24947d3dedd3e0f9bfed03be`, `research_notes/brc_r5_full_side_rectangle_20261107/RESEARCH.md` and `VERIFY.py` (13,9,9,7 nonzero entries); the source physical capacities are `U=W=27/80`. The current checker replays both sets of exact corner identities. All eight seedless target corners are fully specified in the current Python source as `YC` and `YC1`, and all eight exact matrices are supplied via previous already-published `C` plus current literal `E1`. Hence verification is executable in a checkout of the present PR branch without requiring the old unmerged branch.

All eight target corners obey the **same affine seedless face** `z=a/10, v-z=9b/40` and are legal. Every nonnegative Q-mass kernel `Q^c` (target likelihood rows, FULL source likelihood columns) satisfies all 21 exact equations:

```
sum_j Q^c[i,j]     = M_i(y_c)           for i=0..6,
sum_i Q^c[i,j]     = M_j(x_c)           for j=0..6,
sum_i r_i Q^c[i,j] = r_j M_j(x_c)       for j=0..6.
```

Both target/source stop times match exactly at each corner; all Q/P stopping masses have total and likelihood-weighted first moments exactly one. Thus each corner already implements a valid every-declaration Blackwell lift.

## Proof for every real b,p,q,t and declaration

For either endpoint `b_0=1/2` or `b_1=1`, and arbitrary real `p,q in [0,1]`, let `h=((1-p)(1-q),p(1-q),(1-p)q,pq)`. Take `y_{b_k}(p,q)=sum_c h_c y_{b_k,c}` and `Q_{b_k}(p,q)=sum_c h_c Q_{b_k,c}`. Nonnegative bilinear interpolation preserves Q nonnegativity, the 21 Q/P calibration identities, both stop-time equalities and legal target constraints, because each quantity depends **affinely** on the flow and transport. It also preserves the common linear seedless face.

For any real `b in [1/2,1]`, put `theta=2b-1`. Both physical capacities `U(b),W(b)` are affine in b. At **fixed p,q**, the entire source flow obeys

```
x(b,p,q)=(1-theta)x(1/2,p,q)+theta x(1,p,q).
```

Set `y(b,p,q)=(1-theta)y_{1/2}(p,q)+theta y_1(p,q)`, and `Q(b,p,q)=(1-theta)Q_{1/2}(p,q)+theta Q_1(p,q)`. Each of the 21 calibrated mass equalities and both stopping times survives this convex interpolation. The target remains legal and seedless since the shared face constraints `z=a/10,v-z=9b/40` are linear; the transport remains nonnegative. These two interpolation stages prove the `t=0` theorem for *all real* b,p,q, not just rational grids.

For arbitrary real `0<=t<=1`, define `x_t=(1-t)x+t y`, `Q_t=(1-t)Q+t diag(M(y))`. Diagonal transport is the identity on y; flow-to-mass and stopping-time maps are affine, so `Q_t` is calibrated from y to x_t. For any `d_j in [0,1]`, define `k_i=(sum_j Q_t[i,j]d_j)/M_i(y)` if `M_i(y)>0`, and `k_i=0` on zero-mass target rows. Row sums guarantee `0<=k_i<=1`. Column and weighted-column identities imply

```
sum_i M_i(y)k_i     = sum_j M_j(x_t)d_j,
sum_i r_i M_i(y)k_i = sum_j r_j M_j(x_t)d_j.
```

Thus Q-decision mass and P-decision mass, hence both error probabilities, match exactly; so do T_P,T_Q. This establishes the theorem for arbitrary real and irrational b,p,q,t,d, all boundary cases included. **QED**.

## Execution, novelty and continuation

Ran Python standard-library `fractions.Fraction` checker `VERIFY.py` locally: **eight** exact 7x7 rational corner certificates, **625** exact rational `(b,p,q,t)` cases, each checking legal flow, both times, all mass/calibrated Q/P identities, seedless face and sample declarations. Actual unedited stdout is `EXACT_OUTPUT.txt`. The all-real theorem is the finite-corner algebraic interpolation proof, not an extrapolation from 625 samples. This expands the previously separate complete physical b=1/2 and b=1 rectangles to a **continuum b ∈ [1/2,1]**. Existing BRC mass/observer interfaces reused, no new numerical/physical kernel introduced.

Mother objective remains complete pointwise four-observation image equivalence (or exact separation) for **every** legal FULL_HIST strategy, beyond this source prism. Next seek exact certificate at some `b<1/2` retaining both full u,w capacities, or relax fixed `a=g=1,v=9b/40,z=0`, or construct a precisely scoped rational dual obstruction. Native Owner/CLAIM still unconfirmed due to `WAITING_RESOURCE / EVENT_COLLECTION_IO / OSError`; author proof awaits independent mathematical review and admission.
