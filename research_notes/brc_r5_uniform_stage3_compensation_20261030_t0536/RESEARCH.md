# Enterprise Math R5 — exact stage-3 same-sign P-error compensation envelope

Date: 2026-10-30 (Asia/Shanghai). Classification: **AUTHOR_PROVED / EXACT_BIGINT_RATIONAL_CHECKED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING**. This is a finite two-probability-measure stopping experiment, not a native X6/heartbeat physical derivation. Previous frontier: PR #1663, commit `238e91a96e5b10ba2ba672cf84fb6e2c41ceed63`, `research_notes/brc_r5_optimal_time_penalty_20261030_t0440/RESEARCH.md`.

## Frozen source and status

GLOBAL_KNOWLEDGE_V1 verified canonical main: `ea1ec326d006b42227fe130821942e42504b9dae`; Enterprise Math canonical main: `58d3995828b0ab3b3ebc9d015b8f7c9e751822ad`. Read global bootstrap/manual, P000 startup projection (canonical P000 Git blob `770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc` confirmed), ACTIVE worldview, TASK_RESEARCH route, source AGENTS, portable research protocol, and prior immutable R5 proof. The native gateway version 0.6.11 reports `research_authority_granted=false` and an Owner inventory attempt returned `CONTROL_QUOTA`; no authorized current Owner, CLAIM, Result, independent review or admission is inferred. Preservation here is author-side research evidence.

Mother question: find a finite positive two-law stopping model with equal FULL and seedless exact-likelihood-ratio (LR) **convex hulls**, but unequal actual four-observer images, or prove a scoped impossibility. The previous rank-four, doubly colliding model failed the convex-hull equality test. This note derives the exact effect of a new compensator rather than claiming a mother counterexample.

## Exact positive BRC path carrier

Natural history tree and probability cylinder masses are exactly those of the preceding proof. At time 1:
`P(A)=1/3, P(B)=2/3, Q(A)=2/3, Q(B)=1/3`.
At time 2, the `Y=1` conditional pairs `(P,Q)` are `A:(1/2,1/4)`, `B:(1/4,1/2)`.
At time 3, the `Z=1` conditional pairs are:
`A0:(1/2,2/5), A1:(1/2,1/4), B0:(1/2,3/5), B1:(2/3,1/3)`.
All complementary transitions have strictly positive probabilities. At each natural cylinder `h`, keep its provenance and both exact masses `P(h),Q(h)`; `L(h)=P(h)/Q(h)` is a projection, not the entire state. The exact LR collisions are `L(A1)=L(B1)=1` at time 2 and `L(A11)=L(B11)=2` at time 3. The relevant BRC masses are

```text
P(A1)=P(B1)=1/6,
(P(A11),Q(A11))=(1/12,1/24),  (P(B11),Q(B11))=(1/9,1/18),
P(A11)+P(B11)=7/36,
P(A11)+Q(A11)+P(B11)+Q(B11)=7/24.
```

Stop decisions are available at times 1, 2 and 3; time 4 is a forced stop, with no extra nature observation. FULL may condition on the entire labelled history. Seedless LR may only use the current `(t,L)` and fresh behavioral randomness, with one shared stop probability at each collision. Observable `O=(e_P,e_Q,T_P,T_Q)`: the two stopped-cylinder Bernoulli-error expectations and two expected stop times.

At each stopped cylinder define

```text
p0(t,h)=1/5+t/20+(t+1)/(100 L(h)),
q0(t,h)=2/5-t/30+(t+2)L(h)/200.
p(2,A1)=p0+epsilon; p(2,B1)=p0-epsilon,
q(3,A11)=q0+eta; q(3,B11)=q0-eta,
p(3,A11)=p0+kappa; p(3,B11)=p0+kappa,
```

and keep all other rates at baseline. In the exact verified instance `epsilon=eta=1/1000`, `kappa=rho*epsilon`. For all `0<=rho<=75/44`, every resulting error probability is strictly inside (0,1); all the natural masses are positive. Larger rho values are covered by the algebraic formulas only while the rates remain admissible.

The change of measure `P(h)=L(h)Q(h)` gives the *unperturbed* identity `e_P^0=21/100+T_P/20+T_Q/100`, and analogously `e_Q^0=41/100+T_P/200-T_Q/30`. Set

```text
R = e_P-21/100-T_P/20-T_Q/100,
D = 8-T_P-T_Q >=0,
Phi = R-(epsilon/22)*D.
```

This signed observer is linear-affine on the original four-dimensional observation; a Q-only change cannot affect it.

## Theorem — exact uniform stage-3 compensation

For every `rho>=0` with admissible error kernels, the exact all-real support values are

```text
max_FULL(Phi)/epsilon =
    max(3/22, rho/12-1/176) + max(0, rho/9-1/132),

max_LR(Phi)/epsilon =
    max(0, 7*rho/36-7/528).
```

Consequently, `Delta(rho)=max_FULL(Phi)-max_LR(Phi)` satisfies

```text
Delta(rho)/epsilon =
    3/22                   for 0 <= rho <= 3/44,
    25/176-rho/12          for 3/44 <= rho <= 75/44,
    0                      for rho >= 75/44 (if admissible).
```

The third-stage same-sign P compensator therefore cannot erase this exact support obstruction at any `0<=kappa<75 epsilon/44`. At the transition, this *one* supporting direction ceases to separate; that does not establish full convex-hull equality.

### Proof, including all real behavioral policies

Every history reaches any given LR decision key `(t,L)` at most once along a natural trajectory; the same holds for each FULL history key. Therefore each of the four stopped expectations is a **multi-affine** polynomial of the independent behavioral stop parameters. Each linear support functional has a maximum at a deterministic (0/1) corner; this covers the entire real policy hypercube, including zero probabilities and unreachable histories. The positive BRC cylinder masses ensure that this reduction does not silently merge source identities.

Stopping at non-reward nodes can only lower `Phi`, because it creates no residual `R` and incurs an extra nonnegative time deficit `D`; hence such stops can be omitted when maximizing. For FULL, early root stops are similarly dominated by continuing and selecting downstream actions separately. On the A source branch there are three optimal alternatives: stop at `A1` at time 2, yielding normalized score `1/6-(2/3)/22=3/22`; continue to time 3 and stop at `A11`, yielding `rho/12-(1/8)/22=rho/12-1/176`; or never stop early, yielding zero. On the B source branch, stopping at `B1` at time 2 yields a negative score, so only time-3 stopping at `B11` with score `rho/9-(1/6)/22=rho/9-1/132` or no early stop can maximize. Independent sum gives the displayed FULL formula.

For LR, let `alpha,beta` denote continuation at roots A,B, `y` the shared stop action at time-2 collision A1/B1, and `z` the shared stop action at time-3 collision A11/B11. All lie in [0,1]. After eliminating non-reward stop nodes, the exact reduced objective is

```text
Phi/epsilon =
  y*(alpha-beta)/6
  + rho*(1-y)*z*(alpha/12+beta/9)
  - (1/22)*[3*(2-alpha-beta)
            +(2/3)*y*(alpha+beta)
            +(1-y)*z*(alpha/8+beta/6)].
```

It is multi-affine in its four variables. At its 16 deterministic corners, group by `m`, the total P mass stopped at the two time-3 compensator nodes. The maximum zero-rho intercept for each `m` is exactly:

| m | 0 | 1/12 | 1/9 | 7/36 |
|---|---:|---:|---:|---:|
| LR max `Phi(0)/epsilon` | 0 | -25/176 | -19/132 | -7/528 |

For every `rho>=0`, the middle two affine lines lie strictly below the `m=7/36` line, and the remaining envelope is `max(0,7rho/36-7/528)`. This proves LR exactness without sampling real behavioral probabilities. The analogous independently enumerated FULL intercepts for `m=0,1/12,1/9,7/36` are `3/22,-1/176,17/132,-7/528`. Subtraction at the exact breakpoints `3/44` and `75/44` proves the piecewise claim.

## Fully four-dimensional exact rational exclusion at rho=1

Set `rho=1` so `kappa=epsilon=eta=1/1000`. Then

```text
max_FULL(Phi)=(95/396)*epsilon,
max_LR(Phi)=(287/1584)*epsilon,
Delta=(31/528)*epsilon=31/528000 >0.
```

The FULL policy stopping at `A1` at time 2 and `B11` at time 3, continuing elsewhere until time 4, gives

```text
Ostar=(509/1200, 16597/54000, 32/9, 65/18).
```

Every real LR policy and every mixture of such policies satisfies

```text
17424000 e_P - 870408 T_P - 173448 T_Q <= 3668533.
```

But `Ostar` gives left side `3669556` and the **integer separation gap 1023**. With the L1 norm of the normal vector, the exact L-infinity distance obeys

```text
dist_infinity(Ostar,conv(O_LR)) >= 31/559632.
```

The LR four-dimensional affine-span certificate is independently checked using five deterministic LR points (in order `O0,O1,O2,O3,O4`):

```text
O0=(9/20,89/300,4,4)
O1=(2621/6000,2143/7200,15/4,59/15)
O2=(873/2000,239/800,15/4,39/10)
O3=(879/2000,64567/216000,137/36,281/72)
O4=(671/2000,23113/72000,23/12,71/24)
det[O1-O0,O2-O0,O3-O0,O4-O0]=1/12960000000 !=0.
```

Thus this candidate has an honest full-dimensional LR hull (and FULL contains LR), yet fails the **all-signed convex-hull equality** condition. No theorem of actual FULL/LR image inequality under hull equality is claimed.

## Executed evidence, scope and reuse

`VERIFY.js` runs with JavaScript BigInt exact fractions, no external package, and reconstructs the full strict-positive two-law tree. The V8 run at authoring executed **16,384 deterministic FULL policies and 4,096 deterministic LR policies**, computed the four exact intercept groups, checked the two breakpoints and the rho=1 support values, valid error rates at rho=1 and 75/44, the four-observer FULL/LR witness values, the integer separator, nonzero four-dimensional determinant, and the distance bound. `EXACT_OUTPUT.txt` contains the actual returned text, ending `PASS_EXACT_R5_UNIFORM_STAGE3_COMPENSATION_ENVELOPE`. The all-real result follows from the proof and multi-affine extreme-point reduction; finite enumeration checks the exact model and intercept table.

BRC reuse: `REUSE_APPLIED` to the source-labelled positive rational cylinder-mass interface `P(h)=L(h)Q(h)`, preserving path provenance before LR-key quotient. The residual observer detects information the quotient discards. This is typed auxiliary stochastic probability, with no assertion of a native six-dimensional geometry embedding or native BRC-Shor runtime.

## Next discriminating problem

Analyze **independently signed** P-error compensators at `A11` and `B11` and P-errors on time-2 noncollision/history nodes, searching the exact compensator cone for which all signed supports could agree. Retain `epsilon,eta>0`, two LR collisions and four-dimensional affine span. Start with exact multi-parameter support envelopes and full binary-policy convex hull: every FULL vertex must have an LR nonnegative rational decomposition with at most five LR points (or an exact Farkas separator). Only after that exhaustive hull test succeeds should one attempt the semialgebraic actual-image nonmembership proof. Research status remains **UNREVIEWED / NOT_ADMITTED** pending true native authority and independent Driver review.
