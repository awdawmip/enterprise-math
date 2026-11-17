# R5 — Exact temporal-facet transfer with a persistent answer separator

**Date:** 2026-11-02 Asia/Shanghai. **Type:** author-side proved statement for an explicitly defined finite two-measure stopping DAG, with exact `Fraction` arithmetic confirmation. **Status:** `AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING`.

## Scope and frozen scientific input

Scientific starting pins remain `awdawmip/chatgpt-global-knowledge` `main@a01383f825ef9d43b4b754254303298c64041568` and `awdawmip/enterprise-math` `main@86149263e38c22292c9def1e0f69092efa1be77e`. The immediate verified predecessor is `research_notes/brc_r5_three_key_temporal_and_correlation_20261102_t0640/RESEARCH.md`, immutable EM commit `43d23ab850d4f6faa520a8d9da16de4504e5fced`. Current behavioral rules are loaded independently from latest canonical `main`; P000, ACTIVE worldview and source firewall stay unchanged. These are **auxiliary two-law positive BRC-provenance flows**; no native X6 / heartbeat evolution or physical time calibration is asserted.

## 1. Fully specified modified stopping model

Reuse the predecessor's actual three-key `I=(t1, LR1) → J=(t2, LR1) → K=(t3, LR1)` stopping DAG, its root probabilities `1/2` to I, `1/4` to J via B, `1/4` to K via C, and its equal-P/Q natural `1/2` branches I→J or K, and J→K or answer at t3. Stop at t1, t2 or t3 returns P with certainty; terminal answer at t returns answer-P probability `p` under law P and `q` under law Q. The observer is `O=(e_P,e_Q,T_P,T_Q)` with `e_Q=P_Q(answer Q)=1-q`. A terminal branch arriving at t4/t5 reaches t5 with P/Q conditional probabilities `(dP,dQ)` and otherwise t4. The terminal answer probabilities `(p,q)` are independent of that time branch.

The J natural-answer probability pairs remain `B:(2/5,3/5)` and `I:(3/5,2/5)`. The four source-labelled K terminal kernels are:

| Source | p | q | dP | dQ(lambda) |
|---|---:|---:|---:|---:|
| C | 3/4 | 1/4 | 1/4 | 3/4 - (5/8)lambda |
| I | 1/4 | 3/4 | 3/4 | 1/4 |
| BJ | 2/3 | 1/3 | 1/3 | 2/3 - (1/2)lambda |
| IJ | 1/3 | 2/3 | 2/3 | 1/3 |

Parameter: `lambda∈[0,1]`. Only **two Q-law final-time probabilities** have been varied. For every lambda in this closed interval, all natural P/Q and terminal Bernoulli probabilities, and their complements, are strictly between zero and one. Source identity persists in a positive provenance flow. Every predecision natural branch has the same law-P and law-Q probability, so the shared time–likelihood-ratio keys remain exact. No decision follows a source-specific final kernel.

FULL has seven independent stop parameters `(x,jB,jI,kC,kI,kBJ,kIJ)` in `[0,1]^7`; LR identifies `jB=jI=y` and all K parameters `=z`, retaining `(x,y,z)∈[0,1]^3`. In both classes the observer is multiaffine in the behavioral parameters, so support extrema over the complete **real** behavioral cubes occur at their `2^7=128`, respectively `2^3=8`, binary corners.

## 2. Uniform real-parameter temporal support classification

Take `D=T_P-T_Q`, normal `n_D=(0,0,1,-1)`. Define `a(lambda)=-1/8+5lambda/32`, `b(lambda)=-1/24+lambda/16`. Full positive provenance accounting gives the **identity at every real FULL strategy**

```
D_FULL = a(lambda)(1-kC) + (1-x)(1-kI)/8
       + b(lambda)(1-jB)(1-kBJ)
       + (1-x)(1-jI)(1-kIJ)/24.
```

The first and third terms can each independently be switched off by its K decision. The two nonnegative terms reach `1/8` and `1/24` simultaneously at `x=jI=kI=kIJ=0`; this does not constrain the independent choices for the first/third terms. Thus

```
h_FULL(D) = 1/6 + max(0,a(lambda)) + max(0,b(lambda))
          = 1/6                     if 0 <= lambda <= 2/3,
            1/8 + lambda/16        if 2/3 <= lambda <= 4/5,
            7lambda/32             if 4/5 <= lambda <= 1.
```

For LR, substitution yields the **real-domain identity**

```
D_LR = (1-z)[lambda(7/32-y/16) - x(4-y)/24].
```

Since `lambda≥0`, `0≤x,y,z≤1`, the expression is at most `7lambda/32`, attained by `(x,y,z)=(0,0,0)`. Therefore, exactly for all real lambda in `[0,1]`,

```
Delta_D(lambda) := h_FULL(D)-h_LR(D)
 = 1/6-7lambda/32,  0 <= lambda <= 2/3;
   1/8-5lambda/32,  2/3 <= lambda <= 4/5;
   0,                4/5 <= lambda <= 1.
```

The temporal support gap is strictly positive for `lambda<4/5` and exactly zero for `lambda≥4/5`. On this latter interval all four `dP-dQ` are nonnegative, and both classes can stop at K to make `D=0`; hence both `D` and `-D` have equal FULL/LR support for every `lambda∈[4/5,1]`. This is a genuine removal of the predecessor's temporal separator while keeping every natural branch strictly positive.

## 3. Persistent independent answer separator

Consider `E=e_P+e_Q`. It does **not depend on lambda** because the terminal answer kernels `(p,q)` do not change with the time-4/time-5 coin. At K, the stop reward is `E=1`, while the continue reward is `1+p-q`. In source order C/I/BJ/IJ the continue rewards are `(3/2,1/2,4/3,2/3)`. At J, the final-natural rewards are `B:4/5`, `I:6/5`.

An exact backward maximization/minimization through the finite FULL DAG gives

```
max_FULL E = 7/6,   min_FULL E = 5/6.
```

For the LR subclass all eight binary tuples `(x,y,z)=(000,001,010,011,100,101,110,111)` produce the following **exact, lambda-independent** E values:

```
1, 1, 1, 1, 137/120, 39/40, 9/8, 1.
```

Multiaffine interpolation then gives the sharp all-real bounds

```
max_LR E = 137/120,   min_LR E = 39/40.
```

For the signed normal `n_E=(-1,-1,0,0)` this yields the **parameter-uniform** support gap

```
Delta_E = h_FULL(n_E)-h_LR(n_E)
        = -5/6 - (-39/40) = 17/120 > 0.
```

In fact, the fixed FULL policy `(x,jB,jI,kC,kI,kBJ,kIJ)=(0,0,0,1,0,1,0)` has, for **every** lambda,

```
W = (29/48, 11/48, 175/48, 167/48).
```

Its `E(W)=5/6` while every real LR strategy, and therefore every convex combination thereof, has `E>=39/40`. By the `l1`/`l∞` dual bound (normal l1 norm 2),

```
dist_infty(W, conv(LR([0,1]^3))) >= (17/120)/2 = 17/240.
```

The prior temporal facet can disappear completely while a different answer facet remains **uniformly separated**. This establishes the desired precise diagnostic, not a global impossibility theorem for arbitrary stopping DAGs.

## 4. Four-dimensionality survives the interpolation

Select the five LR deterministic strategies `000,001,010,100,101`. Subtract observation at `000` from the other four; the 4×4 affine determinant for their four observation columns equals

```
A(lambda) = (1-lambda)/5120 + lambda*(401/98304) > 0
```

throughout the interval. Linearity follows because only the `T_Q` row varies with lambda (the other three observer rows are unchanged). Thus the LR convex hull remains full-dimensional, including the interval where the temporal support gap is zero.

At the full interior policy with every FULL stop probability `1/2`, the FULL 4×4 Jacobian minor in columns `(x,jB,jI,kC)` equals

```
J(lambda) = -(1-lambda)/5120 - lambda*(109/3932160) < 0.
```

Again only the `T_Q` row varies affinely in lambda. The exact endpoint minors and affine interpolation prove rank four for **every** real lambda. In particular temporal-gap removal did not destroy the full-rank route toward the mother problem.

## 5. Verification range and research consequence

The companion `VERIFY.py` actually executed using Python standard-library `Fraction`: 1,517 assertions and 1,512 complete positive-terminal-flow evaluations. It checks all 128 FULL and 8 LR vertices at eight distinct rational lambda values including the two exact breakpoints, the temporal and answer support extrema, fixed witness, LR affine determinant, four FULL Jacobian minors and 384 nonbinary FULL time identities. Actual captured stdout is `EXACT_OUTPUT.txt`; it ends with `PASS_EXACT_R5_TEMPORAL_FACET_TRANSFER_AND_ANSWER_RESIDUAL`. These checks corroborate the **above algebraic real-domain proofs**; the eight lambda samples are not used as the logical basis for an all-real assertion.

The mother target remains: find a genuine stopped-branch DAG where FULL and LR four-dimensional **convex hulls coincide**, yet their actual real images differ. This family instead has an exactly specified **persistent answer obstruction**, even after both temporal supports coincide. The result supports replacing the *answer-conditioned K kernels* or topology next, while preserving the positive dual-law provenance and rank. The abstract source-correlation benchmark from the predecessor remains a separate valid mathematical model, not a native stopping realization.

## Provenance / control

Current authenticated connected GitHub identity: `awdawmip`, with push permission. On this run the Sites connection remains `static_machine_readonly`, `research_authority_granted=false`, `write_relay_enabled=false`; the bounded native task/owner inventory returned `CONTROL_QUOTA`. Hence this author-side result obtains no live CLAIM, registered Activity, canonical Result, or independent Driver Review. Existing PR publication is a durable portable handoff, not research admission. No P000, protected worldview, frozen source pin, Task V2 record, control event, identity or service permission is changed by this paper.
