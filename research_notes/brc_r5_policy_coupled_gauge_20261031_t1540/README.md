# R5 — Policy-coupled Q-terminal robustness and time-affine observer gauge

**Date:** 2026-10-31 (Asia/Shanghai). **State:** `AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING`. This is an auxiliary finite two-law STOP/CONTINUE observer result; not a native X6 theorem.

## New exact mathematics
For a fixed FULL witness in a finite stopping model with a finite seedless-LR deterministic strategy set, let `A_f-B_j` be baseline signed-support margins against LR deterministic policy `j`. Let `q_f(h),q_j(h)` be the actual Q cylinder occupancies where terminal Q-error labels `r_h` may change by common legal `delta_h in [L_h,U_h]`. Then the EXACT worst attainable fixed-witness support margin (over all legal joint changes) is

`min_j [ A_f-B_j + sum_h min( c*(q_f(h)-q_j(h))*L_h, c*(q_f(h)-q_j(h))*U_h ) ]`.

Here `L_h=max(-epsilon,-r_h)`, `U_h=min(epsilon,1-r_h)`, and `c` is the coefficient of Q-error in the support direction. It follows by exchanging the finite minimum over LR deterministic policies and legal perturbations, then minimizing each affine coordinate. No all-real policy grid extrapolation is needed. An exact two-cylinder auxiliary example shows crude independent-support Lipschitz bounds can lose a factor two in the allowable error amplitude; this is not a construction realizing the R5 mother target.

If every Q terminal history with stopping time `tau` receives a legal common adjustment `r_new=r_old+a+b*tau`, the four-observer vector is transformed by the invertible affine shear `(eP,eQ,TP,TQ) -> (eP,eQ+a+b*TQ,TP,TQ)` of determinant one. Thus FULL/LR hull equality, real behavioral observer-image equality, nonconvexity and affine rank are preserved. This holds only for global terminal history labels, not an arbitrary post-merger-only edit.

## Conditional R5 quantitative consequence
Inherited UNREVIEWED predecessor baseline at `alpha_0=1/4, alpha_1=1/8`: `J=41 eQ-12 TQ`, `Delta_J^0=2`, uniform Q postmerger occupancy bound `3/8`. For legal final labels decomposing as `r_new=r_old+a+b*tau+eta` with `eta` postmerger-only and `|eta|<=rho`, the transported direction `J_b=41 eQ_new-(12+41*b)TQ` has

`Delta_(J_b) >= 2 - (123/4)*rho`.

At `rho=1/16`, the certified gap lower bound is `5/64`, and a FULL point lies at least `(5/64)/(41+|12+41*b|)` away from the full LR convex hull in L-infinity norm. Numerics are conditional on the previous Bellman support identity, which was NOT independently re-proved in this run. A nonzero legal shear on the actual R5 branch/error table is NOT certified.

## Complete actual evidence and inputs
[Download the full evidence archive](EM_R5_20261031_1540_policy_coupled_gauge_evidence.tar.gz) (7,987 bytes; SHA256 `83d98f6341cc0b97d5922a5b572c61639949cb60dd819b8600f44b84164c4432`). It contains complete `RESEARCH.md`, executed standard-library `VERIFY.py`, literal `EXACT_OUTPUT.txt` and `NEXT_TASK.md`. Actual executed marker: `PASS_EXACT_R5_POLICY_COUPLED_GAUGE_ROBUSTNESS`. Exact tests cover five perturbation sizes, auxiliary witnesses, a positive three-distribution toy legal gauge, and rational conditional R5 constants, NOT the full original R5 Bellman enumeration or native X6 experiments.

Frozen GLOBAL_KNOWLEDGE_V1 `main@0f56e103e335e81db09f4169fb389c29f06815b6`; Enterprise Math `main@d26fed9696ab2e230c7c9e8bbe64f684be6bb7ce`. Predecessor R5 commit `0d01d50eef898384a993ab39e79fb6df1ab8fb3d`; earlier positive double-merger model `e7916482f44a925e11ece98e406309f4655fb1f1`. P000 and ACTIVE worldview untouched.

Native `DIRECTED_RESEARCH` authority reported `authority_granted=false`. Owner query returned `CONTROL_QUOTA`; no Source CLAIM, Result, Driver review or formal activity admission was acquired. GitHub storage is portable author-side evidence, not mathematical or Source admission.

**Next:** independently recover the complete R5 source-labelled terminal-cylinder occupancy matrix from the prior positive double-merger evidence; apply the exact fixed-witness minimax formula to actual R5, then test joint legitimate terminal kernels above the previous `8/123` threshold for exact all-signed four-hull equality (primal <=5-point certificates or Farkas separators). Only thereafter test real seedless-LR observer nonmembership, while retaining provenance.
