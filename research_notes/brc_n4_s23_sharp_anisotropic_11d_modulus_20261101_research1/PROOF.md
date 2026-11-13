# BRC N=4 / S23: exact 11-control anisotropic continuity modulus

2026-11-01. **Author-side analytic proof and executed exact-rational checks; UNREVIEWED / NOT_ADMITTED.** This concerns the finite six-source S23 BRC statistical experiment, not P000 native X6 spatial/time dynamics, nor the unrestricted 10-label minimax value.

## Frozen model and question

The 11 lawful behavior controls are ordered
`(a_A,a_B,b_U,b_AV,b_BV;c_AU0,c_AU1,c_AV,c_BU0,c_BU1,c_BV) in [0,1]^11`.
The six **distinct statistical sources**, indexed 0..5, are AU0, AU1, AV, BU0, BU1, BV; their causal parameter indices are

```
A=(0,0,0,1,1,1)
B=(2,2,3,2,2,4)
C=(5,6,7,8,9,10)
M20=((10,10,0,0,0,0),(9,11,0,0,0,0),(0,0,20,0,0,0),
     (0,0,0,10,10,0),(0,0,0,2,18,0),(0,0,0,0,0,20))
M=M20/20.
```

The shared `b_U` remains one legal control for both AU and BU. Source `x` has four-stop law
`F(a,b,c)=(a,(1-a)b,(1-a)(1-b)c,(1-a)(1-b)(1-c))`.
Preparation `i` has law `p_i(theta)=sum_x M[i,x]F(theta[A[x]],theta[B[x]],theta[C[x]])`.
All mixtures are BRC positive-rational/real stochastic mixtures with explicit source provenance. Statistical source labels are **not** the six primitive P000 spatial axes.

Prior result (PR #1765, `9cd60a7dfb87da4b9b09b5cce62d32920cb01e24`) proved the sharp *isotropic* bound `1-(1-epsilon)^3`, and established the following anisotropic expression only as an upper bound for cell error. The new question: is it **exact**, simultaneously for all six prepared rows and all 11 coordinate budgets?

## Theorem: sharp anisotropic prepared-law modulus, all real budgets

For any `epsilon=(epsilon_0,...,epsilon_10) in [0,1]^11`, define

`w_x(epsilon)=1-(1-epsilon[A[x]])(1-epsilon[B[x]])(1-epsilon[C[x]])`,

`Omega_i(epsilon)=sum_x M[i,x]w_x(epsilon)` and `Omega(epsilon)=max_i Omega_i(epsilon)`.

Then, simultaneously for every preparation `i`,

`sup_{theta,phi in [0,1]^11 : |theta_j-phi_j|<=epsilon_j for every j} TV(p_i(theta),p_i(phi)) = Omega_i(epsilon)`.

Consequently,

`sup_{theta,phi : |theta_j-phi_j|<=epsilon_j} max_i TV(p_i(theta),p_i(phi)) = Omega(epsilon)`.

**Proof of upper bound.** Couple the three stopping decisions on each latent source with common stage-uniform variables. Their first disagreement has probability at most
`1-(1-d_a)(1-d_b)(1-d_c)` where `d_a,d_b,d_c` are the respective absolute control differences. This is the three-stage causal coupling proved in the cited predecessor. Since these differences are bounded by the corresponding entries of `epsilon`, `TV(F_x(theta),F_x(phi)) <= w_x(epsilon)`. Convexity of total variation under the same positive, row-stochastic BRC mixture gives
`TV(p_i(theta),p_i(phi)) <= sum_x M[i,x]w_x(epsilon) = Omega_i(epsilon)`.

**Attainment, for *all rows at once*.** Set `theta=(0,...,0)` and `phi=epsilon`. This is a valid **shared-control** S23 pair even when `b_U` affects two groups. All six source laws at `theta` equal the fourth-time point mass `e4`. At `phi`, source `x` assigns fourth-time mass exactly
`(1-epsilon[A[x]])(1-epsilon[B[x]])(1-epsilon[C[x]])`.
Hence `p_i(theta)=e4` while `p_i(phi)_4=1-Omega_i(epsilon)`. For any probability law `q`, `TV(e4,q)=1-q_4`, so equality holds for every row `i` simultaneously. The asserted suprema are maxima. QED.

## Corollary: best possible bank-independent risk continuity bound

Let `E` be any fixed policy-independent row-stochastic encoder and let `{D_l}` be any nonempty finite collection of fixed stochastic decoder kernels. Put `q_li=(M E D_l)_i`, `L_l(theta)=max_i TV(p_i(theta),q_li)`, and `G(theta)=min_l L_l(theta)`. Then

`|G(theta)-G(phi)| <= Omega(epsilon)` whenever the coordinate differences are bounded by `epsilon`.

Proof: total-variation reverse triangle inequality bounds each input/label loss variation by the corresponding prepared-law variation; maximum and minimum preserve a common additive bound. The constant **cannot be improved uniformly over all admissible fixed encoder/banks**: choose a one-label decoder that always emits `e4`, whatever the storage state. Then `G(0)=0` and `G(epsilon)=Omega(epsilon)`. This does **not** assert sharpness for the *specific* ten-label bank in PR #1765. QED.

## Exact per-control sensitivities and adaptive-cell consequence

When only control `j` may vary by `d`, the exact modulus is `c_j d`, with

| control | a_A | a_B | b_U | b_AV | b_BV | c_AU0 | c_AU1 | c_AV | c_BU0 | c_BU1 | c_BV |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| c_j | 1 | 1 | 1 | 1 | 1 | 1/2 | 11/20 | 1 | 1/2 | 9/10 | 1 |

These are calculated exactly from the six positive rows of `M`, and attained by `theta=0,phi_j=d`. Thus the matrix's source-resolving asymmetry matters to subdivision priorities: e.g. changing only the AU0 third-stage control has exactly half the effect of changing the AV third-stage control at equal budget.

For an axis-aligned parameter cell of widths `h_j`, rounding to a nearest corner gives coordinate errors at most `h_j/2`, hence

`0 <= sup_{theta in cell}G(theta)-max_{corner v}G(v) <= Omega(h/2)`.

This improves the isotropic `1-(1-max_j(h_j)/2)^3` when few controls vary. For a cell in which only `c_AU0` has width `1/2`, the *provable* risk sampling gap is at most `1/8`, versus the isotropic bound `37/64`. These are upper bounds for a given bank, not necessarily attained by that bank. This sampling lower-side certificate is distinct from the valid fixed-label upper-side certificate `min_l max_corner L_l`.

## Executed exact evidence and scope

`VERIFY.py` (Python stdlib `fractions.Fraction`) validates the six row mixtures and 11 causal indices, performs **2048** exact mask-attainment tests (also using the one-label constant-e4 risk witness), checks all 11 sharp one-coordinate coefficients, tests an anisotropic cell certificate, and checks **256** deterministic-seed exact-rational strategy pairs. `RUN_EVIDENCE.txt` is the actual output. The universal quantifiers follow from the analytic coupling/attainment proof, **not** extrapolation from these finite tests.

This result sharpens a continuity tool; it does **not** close the unrestricted `k=4,6`, ten-label S23 minimax interval `[1/2,2/3]`, establish native P000 X6/time correspondence, validate S2 information-set transfer, or constitute an independent review. The next step is a jointly redesigned ten-bank plus continuum-certified adaptive cover.
