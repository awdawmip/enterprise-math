# R5 — Three-stage likelihood-ratio observer: exact convexity of real behavior images

Date: 2026-11-05 Asia/Shanghai. Author-side TASK_RESEARCH portable mathematics. Frozen scientific pins: global `a01383f825ef9d43b4b754254303298c64041568`, EM `86149263e38c22292c9def1e0f69092efa1be77e`. Immediately preceding verified scientific result: `f5916724487fa09acaa957fc2fbe21ba2d4d0246:research_notes/brc_r5_quiet_refinement_time_invisible_20261105_t1440/RESEARCH.md`. Independent review and admission pending.

## Target and exact model

R5 seeks a finite strictly positive P/Q stopping BRC with equal *complete O4 convex hulls* but different actual real-behavior O4 images for FULL versus seedless LR. The model below is a scoped subfamily of that question, with a single common first ratio node and exactly two decision gates.

Fix positive hidden source weights `w_h` summing to 1, finite positive likelihood-ratio alphabets `R=(r_j)` and `S=(s_l)`, and strictly positive Q kernels `K_hj`, `M_hjl`, satisfying `sum_j K_hj=1`, `sum_j r_j K_hj=1`, `sum_l M_hjl=1`, `sum_l s_l M_hjl=r_j`. First observation at t=1 is ratio 1. At t=2 one observes `r_j`; at t=3 one observes `s_l`. Stop and freely declare P/Q at t=1 and t=2, or continue. At t=3 declare P/Q without further continuation. P/Q masses are connected by the likelihood-ratio factors `1, r_j, s_l` at each stopping observation. Seedless LR policies see only (time, current ratio), while FULL additionally sees source h; neither is assumed to remember earlier j at the terminal declaration. All behavioral randomization probabilities range independently over the full real [0,1]. Set O4=(e_P,e_Q,T_P,T_Q), with e_P=P(declare Q) and e_Q=Q(declare P).

## Theorem (linear occupancy convexification)

**For every such finite strictly positive three-stage experiment, O4(seedless LR) and O4(FULL) are already compact convex polytopes as sets of actual real randomized behavioral observations. Therefore**

`conv O4(FULL)=conv O4(seedless LR)  iff  O4(FULL)=O4(seedless LR)`.

The kernels K and M may both depend on source h; terminal likelihood ratios may overlap completely across sources and previous second-stage branches. No small-variance or weak-continuation condition is required.

### Proof: seedless LR

Let `q_j=sum_h w_h K_hj>0`, `C_jl=sum_h w_h K_hj M_hjl>0`. These fixed coefficients satisfy `sum_j q_j=sum_j r_j q_j=1`, `sum_l C_jl=q_j`, `sum_l s_l C_jl=r_j q_j`. Write a for probability to continue at t=1; b_j for conditional continuation at t=2; d1,d2_j,d3_l for probability to declare P at each stop/declaration key.

Define occupation variables `u=a`, `v_j=a*b_j`, `z1=(1-u)*d1`, `z2_j=q_j*(u-v_j)*d2_j`, `Q_l=sum_j C_jl*v_j`, and `z3_l=Q_l*d3_l`. They satisfy the **finite linear system**

```
0 <= u <= 1
0 <= v_j <= u
0 <= z1 <= 1-u
0 <= z2_j <= q_j*(u-v_j)
Q_l = sum_j C_jl*v_j
0 <= z3_l <= Q_l.
```

Conversely, every solution of this linear system is implemented by a genuine seedless LR policy: set `a=u`; `b_j=v_j/u` when u>0; `d1=z1/(1-u)` when 1-u>0; `d2_j=z2_j/(q_j*(u-v_j))` when its denominator is positive; `d3_l=z3_l/Q_l` when Q_l>0. At any zero denominator set its associated conditional action to 0, which is harmless at a zero-mass key. All quantities lie in [0,1]. Thus these linear constraints describe the *actual* behavioral policies' occupancy image, not merely its convex hull. A terminal ratio s_l can be reached from different j and h, but its P/Q factor is always s_l; because terminal decisions have no successor states, there is no hidden conditional transition constraint to preserve after such merging.

Their four observed quantities are the following affine-linear functions:
```
e_Q = z1 + sum_j z2_j + sum_l z3_l
e_P = (1-u-z1)
    + sum_j r_j*(q_j*(u-v_j)-z2_j)
    + sum_l s_l*(Q_l-z3_l)
T_Q = 1 + u + sum_j q_j*v_j
T_P = 1 + u + sum_j r_j*q_j*v_j.
```
A bounded linear polytope under an affine map is a compact convex polytope. To realize the exact O4 mixture of any two LR policies, take the linear mixture of their occupancy variables and reconstruct a *single* seedless LR policy using the inverse ratios just displayed. This works for every real mixture coefficient, without a shared persistent random seed.

### Proof: FULL

Repeat separately for each source h: use `q_hj=K_hj`, `C_hjl=K_hj*M_hjl` and source-indexed `u_h,v_hj,z1_h,z2_hj,Q_hl,z3_hl`. Each source's feasible occupancy set has the same linear description and explicit behavioral-policy inverse; unrestricted FULL source-specific policy choices realize the product of these polytopes. The aggregate O4 is its fixed linear `sum_h w_h*(source O4)` image, hence is a compact convex polytope. Every seedless policy is an admissible FULL policy that ignores source. Thus both sets equal their own convex hulls, proving the equivalence. QED.

### Exact scope of the classification

This theorem covers any finite number of hidden sources and arbitrarily strong source-dependent first and second experiments for the stated t1/t2/t3 topology. It does **not** decide the R5 mother question for topologies with a nonterminal merge followed by further source/path-dependent information or decisions. In those topologies, the conditional outgoing kernel at a shared later LR key may depend on earlier stopping-policy choices, invalidating the fixed linear coefficients C_jl used here.

## Exact rational checks

`VERIFY_CORE.py` runs with Python 3 standard-library Fraction. It builds sources of weights (2/5,3/5), R=(1/2,1,3/2), S=(1/4,1/2,1,3/2,7/4), K_A=(1/4,1/2,1/4), K_B=(3/8,1/4,3/8), and strictly positive *different* terminal kernels M_A and M_B with exact means r_j. For each information class it tests 120 deterministic-seeded pairs of rational behavioral strategies, forms occupancy mixtures with exact rational mixture weights, reconstructs one policy in the same class, and asserts equality of occupancies and complete O4 vectors. A separately executed, larger local validation harness also checked 120 pairs per class and the full four-dimensional coordinates. This computation tests examples; the general theorem follows from the affine-system proof.

## Next discriminating research unit

Construct a minimal *nonterminal* merge and subsequent split, retaining two distinct observed histories that reach the same (time, LR) key but carry different conditional future information. Derive its source-blind occupancy constraints and test with exact polynomials whether mixtures of actual LR behavioral policies remain realizable. If a real-image nonconvexity witness is found, examine the much stronger equality of FULL/LR convex hulls with an independent all-directions certificate, then test actual-image nonmembership. Preserve the R5 frozen scientific pins and parent status.

Interpretation: the finite likelihood-ratio observer is an external auxiliary measurement model compatible with preserving structural provenance under P000; it is not a theorem about native six-dimensional dynamics.

Status: AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.
