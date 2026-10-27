# R1—N14: LR-fiber-constant quotient can have a nonconvex two-law observer image

Date: 2026-10-27. **Status:** author-level exact external finite-path proof, not a native Source CLAIM/Result, independent Driver review, Lean verification, or P000-native X6 theorem.

## Frozen source and prior frontier
GLOBAL_KNOWLEDGE_V1: `awdawmip/chatgpt-global-knowledge@6190a3375e2e7cf63d5f0c303f9b44956700f960`; P000 blob `770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc` (startup projection matches). Initial Enterprise Math snapshot: `awdawmip/enterprise-math@673e3dcb3416f3a033e8978fb2eb421e7f03dd2e`. The two canonical global entry files, P000, ACTIVE worldview, project routing, math/code policies, BRC priority, and current `docs/PORTABLE_RESEARCH_PROTOCOL.md` were read from these fixed pins. The previous frontier is `research_notes/r1_n14_brc_two_law_fresh_coin_nonconvex_n2_20261027_r1t11/NEXT_TASK.md`; its N=2 witness does not satisfy LR constancy. The concurrent N=3 predecessor-kernel rank result explicitly had no image nonmembership proof.

## Theorem
There exist *distinct* strictly-positive rational non-IID probability laws P and Q, horizon N=3, and a recursively updatable deterministic compressed state x with Q(h)/P(h) constant on **every x fiber**, such that the paired terminal image `(Law_P(T,o(x(H_T)),D), Law_Q(T,o(x(H_T)),D))` of **common law-independent, current-x-only fresh-coin randomized stop/decision strategies** is nonconvex. Take the identity observer `o(x)=x`. The root must continue; allowing time-zero stopping does not repair the counterexample, because the midpoint has no time-zero mass.

### Model and LR property
At each time the alphabet is {0,1,2}. The first and second symbols are independent uniform {0,1,2} under both P and Q. Let the hidden origin group be A if the first symbol is 0, and B otherwise. The third-symbol conditional kernels are:

| origin | law | Pr(0) | Pr(1) | Pr(2) |
| --- | --- | ---: | ---: | ---: |
| A | P | 1/8 | 5/8 | 1/4 |
| B | P | 1/4 | 1/4 | 1/2 |
| A | Q | 1/4 | 5/8 | 1/8 |
| B | Q | 1/2 | 1/4 | 1/4 |

All rows sum to one and every edge is positive. The pointwise ratios Q/P in the third step, for both origin groups, are `r=(2,1,1/2)`. The time-typed compressed state is

* `x(empty)=(0,root)`;
* `x(a1)=(1,A)` if a1=0, else `(1,B)`;
* `x(a1a2)=(2,merged)` for all length-two histories;
* `x(a1a2a3)=(3,a3)` for all terminal histories.

This is recursively updatable: at each step x_new is a deterministic function of x_old and the new symbol. For every history of length <=2, Q(h)/P(h)=1; at length 3, Q(h)/P(h)=r[a3]. Therefore each of the 7 compressed states has a **constant history likelihood ratio**. The model is *not* strongly lumpable: different hidden origin groups at the time-two merged state have different third-step P/Q kernels.

### Two admissible strategies
Strategy U: at time 1 continue iff group A, otherwise stop with D=0; at time 2 always continue; at time 3 decide D=0. Strategy V: at time 1 continue iff group B, otherwise stop D=0; at time 2 always stop D=0. Both use only current x and do not need any persistent random seed.

Let M be the componentwise average of their paired terminal distributions. For P its nonzero probabilities are:

| terminal (T,x,D) | M under P |
| --- | ---: |
| (1,A,0) | 1/6 |
| (1,B,0) | 1/3 |
| (2,merged,0) | 1/3 |
| (3,0,0) | 1/48 |
| (3,1,0) | 5/48 |
| (3,2,0) | 1/24 |

Under Q the first three values agree; the last three become 1/24, 5/48, 1/48. Each vector sums to one.

### Polynomial nonmembership certificate valid for ALL real randomized quotient policies
Consider **any** admissible current-x-only randomized strategy with arbitrary real action probabilities that is claimed to produce M. Its observed time-one stop masses force continuation masses `u_A=1/3-1/6=1/6` and `u_B=2/3-1/3=1/3`. At time two every surviving history has *the same x*, and fresh-coin x-only control forces one common continuation probability c, independent of hidden group. Its total P time-three mass is `R=c(u_A+u_B)`; from M, `R=1/6`, so `c=1/3`.

Denote `W_j=P(T=3,x=j)`, and let p_Aj,p_Bj be the third-step P probabilities in the table. Since the time-two step is neutral and the time-two continuation kernel cannot depend on the forgotten origin, every possible real-parameter quotient strategy obeys the polynomial identity

`(u_A+u_B)*W_j - R*(u_A*p_Aj + u_B*p_Bj)=0`  (★).

At M, for j=0 the left side equals
`(1/2)(1/48) - (1/6)((1/6)(1/8)+(1/3)(1/4)) = 1/96-5/288 = -1/144 != 0`.

Equivalently every policy matching M's time-one and time-two totals is forced to produce `W_0=5/144` rather than M's `1/48=3/144`. The P gap is **1/72**. Under Q the analogous forced and desired values are 5/72 and 1/24, gap **1/36**, with polynomial residual **-1/72**. No time-three randomized decision can fix a discrepancy after summing over D. This excludes **every real-valued** admissible common policy, not only tested rational choices. As U and V themselves are admissible, M is outside their attainable image. **The paired image is nonconvex.** QED.

## Scope / BRC audit
This is an exact ordered-positive-path counterexample for an external **finite non-IID** probability model. The readout retains time-one origin and time-three final symbol; it is NOT a proof of nonconvexity for the coarser `(T,D)` readout. The phenomenon is a future-relevant branch-provenance residual that LR-only compression loses. The BRC-compatible carrier is positive rational mass with ordered branch ID, survival/action flow, observer and allowed future continuation; no signed or phase cancellation and no BRC–Shor/Heartbeat/native-residual physical operation was attempted. The user-protected P000 assumptions are unchanged. There is no established P000 X6 embedding, independent research review, Lean checker receipt, or external prior-art novelty determination.

## Exact verification, limitations and next unit
`VERIFY.py` enumerates all `1+3+9+27=40` ordered prefixes using Python `fractions.Fraction`, checks strict-positive normalized kernels, the seven constant LR fibers, actual full terminal joint laws, and the polynomial obstruction at M. Its result `RESULT.json` contains `PASS`, P residual `-1/144`, Q residual `-1/72`. The **all-real exclusion** is the displayed algebraic proof (★), not a numerical search. Reproduce: `python VERIFY.py > RESULT.json`.

The control query `em_control_tasks` yielded `CONTROL_QUOTA`; `em_session_start` was rejected `STATIC_READONLY_SCOPE_DENIED` with `operation_sent=false`. Thus active Source owner, formal CLAIM and execution authority are **unverified**. GitHub authenticated author-side storage does not imply native execution or task admission. Next precise unit: test coarser `(T,D)` observer and N=2 minimality under LR-fiber constancy; see `NEXT_TASK.md`.
