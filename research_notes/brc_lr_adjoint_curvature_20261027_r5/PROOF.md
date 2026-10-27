# R5 — Adjoint curvature certificate for likelihood-ratio compression

**Date:** 2026-10-27; **classification:** PORTABLE AUTHOR / UNREVIEWED / NOT_ADMITTED. This is a finite external probability-tree statement, not P000 native X6 dynamics, an admitted theorem, a native CLAIM or a Driver review.

## Frozen inputs, reuse, observer

Account source: `awdawmip/chatgpt-global-knowledge@7dd3a2481543bc82bd83e9993c6646a06738f304`; bootstrap, manual, ACTIVE worldview, P000 projection and original P000 were checked (Git blob `770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc`). Project source: `awdawmip/enterprise-math@4f9653b3b03cd94f69c6a914a02cf757ea06720f`, including autonomous operations and portable protocol. Mathematical predecessor: [full-to-LR predictive diameter theorem](https://github.com/awdawmip/enterprise-math/blob/d246c865427d3383570f83778dc18e05995a4f3a/research_notes/brc_full_to_lr_predictive_diameter_tv_20261027_r5/PROOF.md).

BRC typing: positive Q-branch mass, P/Q ratio, exact hidden-history provenance, and observer `Z=(tau,R_tau,D)`, `O=(P(D=Q),Q(D=P),E_P tau,E_Q tau)`. Future operations are finite stop/continue/declare. Method/tool reuse: `T0_BRC` branch/provenance laws and `T6_OPERATION_SAFE_QUOTIENT` observer-scoped fiber testing — **REUSE_APPLIED**. The existing `brc.affine_effect_transport` API covers fixed-weight degree-two moments, not the occupancy and nonlinear stopping payoff here; no execution or new toolbox-family claim is made.

## Model

A finite strictly-positive P,Q observation tree has horizon `N>=2`. At history h of time t, `R_t(h)=P(h)/Q(h)`; policy coins do not affect observation kernels. Full behavioral policy pi selects `continue`, `stop declare P`, or `stop declare Q` using its full history; at N declaration is compulsory. A seedless LR policy uses only `(t,R_t)` and independently resamples local coins.

Define Q-alive history mass `w_t^pi(h)`, observed alive mass `d_t^pi(r)=sum_{R_t(h)=r}w_t^pi(h)`, and Q-occupancy conditional action probabilities

`alpha_t(a|r)=sum_{R_t(h)=r}w_t^pi(h) pi_t(a|h)/d_t^pi(r)`

on positive fibers; elsewhere choose any valid probabilities. Let bar_pi be the seedless-LR policy using these alpha tables and `c_t(r)=alpha_t(continue|r)`. Given a positive continued mass, `K_t^pi(r,y)` and `K_t^bar(r,y)` are the conditional next-LR laws of the full and projected processes. Each is a convex mixture of hidden Q observation kernels `K_h(y)=Q(R_{t+1}=y|h)`; unused conditional rows can be extended by any kernel mixture from the same fiber.

For any signed `lambda=(a,b,u,v) in R^4`, its payoff is exactly a Q expectation of

`g_lambda(t,r,D)=a*r*1[D=Q]+b*1[D=P]+(u*r+v)*t`,

because `dP/dQ=R_tau` on stopped outcomes. Let `V_{t+1}^{bar,lambda}(y)` be expected future g using bar_pi's time-inhomogeneous projected Q transition matrices, starting from observed active state `(t+1,y)` (choose any valid extension at q-unreachable rows).

## Theorem 1 — exact finite-horizon adjoint identity

For EVERY full-history behavioral pi, its Q-occupancy-averaged seedless projection bar_pi, and every real signed lambda,

```text
J_lambda(pi)-J_lambda(bar_pi)
 = sum_{t=1}^{N-1} sum_r d_t^pi(r) c_t(r)
       sum_y [K_t^pi(r,y)-K_t^bar(r,y)] V_{t+1}^{bar,lambda}(y).   (1)
```

**Proof.** Augment each observed alive LR state with absorbing labels `(s,r',D)` recording every earlier stop. Although the full observed process need not be Markov, its ONE-TIME active/absorbed marginal has an exact forward recursion through its conditional observed transition matrix `T_t^pi` (disintegration). Bar_pi has analogous `T_t^bar`, with the same initial observed distribution. At active state `(t,r)` the stop/P and stop/Q entries coincide by construction of alpha. The entire row difference is its continued mass `c_t(r)` times `K_t^pi-K_t^bar`. Absorbed rows are identities and final mandatory-declaration rows coincide. Hence the exact matrix product telescoping formula

```text
T_1^pi ... T_N^pi - T_1^bar ... T_N^bar
 = sum_{t=1}^N
      (T_1^pi ... T_{t-1}^pi)(T_t^pi-T_t^bar)(T_{t+1}^bar ... T_N^bar)
```

paired with terminal payoff g gives (1): each full prefix supplies `d_t^pi(r)`, the local row defect supplies `c_t(r)(K_t^pi-K_t^bar)`, and the q suffix supplies `V_{t+1}^{bar,lambda}`. The N-th term vanishes. This uses finite algebra, so the result includes all real policy randomization and requires no Markov assumption on the original projected full path. QED.

## Theorem 2 — affine-annihilating curvature bound

All hidden kernels have total mass 1 and likelihood-ratio Q martingale mean r:

`sum_y K_h(y)=1`, `sum_y y K_h(y)=r`.

Therefore `Delta K=K_t^pi-K_t^bar` satisfies **both** `sum_y Delta K(y)=0` and `sum_y y Delta K(y)=0`. It annihilates EVERY affine function `A+B*y`. Let `Y_{t,r}` be the union of all next-LR supports in the fiber, and let

```text
rho_{t,r}^{bar,lambda}
 = inf_{A,B in R} osc_{y in Y_{t,r}}(V_{t+1}^{bar,lambda}(y)-A-B*y).
delta_t(r) = max_{h,h':R_t(h)=R_t(h')=r} TV(K_h,K_h').
```

Since `|sum_y(k-l)f(y)| <= TV(k,l)*osc(f)`, apply this to `f=V-A-By`, then minimize over A,B. Both effective kernels lie in the convex hull of the hidden kernels, so `TV(K_t^pi,K_t^bar)<=delta_t(r)`. Formula (1) yields

```text
|J_lambda(pi)-J_lambda(bar_pi)|
 <= sum_{t,r} d_t^pi(r)c_t(r) TV(K_t^pi,K_t^bar) rho_{t,r}^{bar,lambda}
 <= sum_{t,r} d_t^pi(r)c_t(r) delta_t(r) rho_{t,r}^{bar,lambda}. (2)
```

For a fixed pi and lambda, if rho is zero at every occupied continued state, `J_lambda(pi)=J_lambda(bar_pi)`, even if hidden next-LR kernels are different. This is an OBSERVER-SPECIFIC equality, not general terminal-law equality. Given full optimal pi*, `0<=V_LR(lambda)-V_full(lambda)<=|J_lambda(pi*)-J_lambda(bar_pi*)|` and (2) bounds the signed support gap.

**Universal two-successor corollary:** if for every `(t,r)` the UNION of possible next-LR values over all hidden histories in that fiber has at most 2 values, the unit mass and mean r uniquely determine each hidden kernel. Thus `delta_t(r)=0` for all states. For every finite N, all full-history terminal Q laws and all four-observer vectors are attained by seedless LR policies; `O_full=O_LR`. This hypothesis is on EVERY one-step fiber, not merely the final layer.

## Exact 12-leaf positive-rational witness

Time 1: hidden a or b each Q=P mass 1/2. Time 2: conditional u/v each Q=P mass 1/2. All these LR values equal 1. Time 3: `Y=(1/2,1,3/2)` with `K_a=(1/4,1/2,1/4)`, `K_b=(1/8,3/4,1/8)`. All 12 P and Q leaves are strictly positive, and `P(leaf)=R_3(leaf)*Q(leaf)` is normalized.

Full pi: at t=1 continue on a with probability 3/4 and b with 1/4; otherwise stop/P. At t=2 continue probabilities are `(a,u):1, (a,v):1/2, (b,u):1/4, (b,v):3/4`; otherwise stop/P. At t=3 declare Q exactly when y=1/2 and P otherwise. Occupancy-averaged bar_pi has `c_1=1/2, c_2=11/16`, with the same other actions.

At t=2 the full alive mass is 1/2; among continued histories a contributes 9/32, b contributes 1/16. Therefore

```text
K_t^pi  = (9/11) K_a + (2/11) K_b = (5/22,6/11,5/22)
K_t^bar = (K_a+K_b)/2 = (3/16,5/8,3/16)
TV(K_a,K_b)=1/4; TV(K_t^pi,K_t^bar)=7/88.
```

For `lambda=(1,1,0,0)` the q suffix payoff is `f(y)=min(y,1)=(1/2,1,1)`. Its optimal affine-oscillation residue is exactly `rho=1/4`: for any affine L, `(f-L)(1)-[(f-L)(1/2)+(f-L)(3/2)]/2=1/4`, implying osc>=1/4; linear interpolation of the endpoint f-values attains osc=1/4. Thus the first inequality in (2) is SHARP:

```text
J_full-J_bar = -7/1024
|J_full-J_bar| = (1/2)(11/16)(7/88)(1/4) = 7/1024
diameter-only curvature bound = (1/2)(11/16)(1/4)(1/4)=11/512
O_full=(5/128,59/64,59/32,59/32)
O_bar=(33/1024,479/512,59/32,59/32)
O_full-O_bar=(7/1024,-7/512,0,0).
```

A second one-step history-dependent continue/stop policy on these same kernels yields `J_full-J_bar=-1/64`, also sharp for the actual-kernel-TV curvature bound. The witness certifies a PROJECTION ERROR, not a strict optimum/support gap; the selected full policy is not claimed optimal.

## Validation, reach, and unfinished question

Adjacent `VERIFY.py` (Python `fractions.Fraction`) was executed on a six-denominator exact test instance with the declared full policy, induced q, and 12 strictly positive P/Q leaves; `EXACT_OUTPUT.txt` records output. The finite program tests the exact kernel laws, four-observers, identity and saturation. Theorem 1, Theorem 2 and the universal two-successor corollary are proved algebraically for every finite positive model and all real local policy probabilities; the program is not the proof of their quantifiers. The finite-rational `rho` problem is a rational LP; new general code is not claimed.

Next: the explicit finite rational LP dual certificate and polyhedral signed-objective chambers of `rho(lambda)`, then exact all-direction convex-hull screening before attempting any real-parameter nonattainability proof. The stronger mother question `conv(O_LR)=O_full` but `O_LR != O_full` remains open. See `NEXT_TASK.md`.
