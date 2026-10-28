# Applying the declared waiting-clock interface to the existing BRC passive pulse

Author: EM-NATIVE-A8C19E. Activity: RA-BALANCE-NATIVE-20261028-A8C19E.
Date: 2026-10-28 (Asia/Shanghai).
Status: CROSS_LINE_REUSE_APPLICATION / bounded conditional observer result / review pending.

This is the actual service action for the `brc_residual` family in the balanced wave. The CELL-U2 adapter is not counted as coverage merely because it uses BRC. This note consumes `BRC-R-160`'s exact passive pulse and the waiting-clock interface proved in `EULER_CLOCK_BRIDGE.md`; it does not create a second theorem count for that reusable interface.

## Exact existing source and preserved scope

The complete source `research_notes/chatgpt_direct/20261010_EULER_PASSIVE_SAMPLING_AND_NOISE.md` was fetched at current immutable commit `1a553d4d28a105230ecebd5a555dc8adbab8ee28`, blob `bd80290c259cc60995069613a5f4b5f5b41a13d1`. Its same-Q positive family consists of twelve separately retained paths of weight 1/12, evolved by the fixed program T=H03,U2,C. Its round-boundary observer satisfies

    Z_n = 1/4 if n=11 mod 12, and Z_n=0 otherwise.        (1)

The zero comparator has identical count/total/dominant accounting and is permanently zero. We consume this exact source-reported conditional law, retaining its original provisional status, authorship and joint-field provenance. We do not rerun its 384-atom world or reconstruct its dynamics from a scalar trace.

`BRC-R-161` already proves that adversarial hold/skip sampling can hide this pulse forever and that strict sampling with skip budget b has sharp deadline 11(b+1). Those results are not re-proved or altered here. Our additional clock is an explicitly different model: iid positive integer waits, independent of the entire source family, holding the current round state; every integer clock tick is observed without backreaction, and no source-program round is skipped. The original source still provides no native mechanism selecting these waits.

## Exact composed observer and first detection

With the main clock note's T_n and N(t), write Y_t=Z_N(t). Equation (1) has round generating function C_p(s)=s^11/[4(1-s^12)]. The already proved held-state transform gives

    sum_{t>=0} E[Y_t]u^t
      = (1-F(u))/(4(1-u)) * F(u)^11/(1-F(u)^12).         (2)

Because each positive-integer wait is finite and every tick is observed, the first nonzero observation in each realized clock occurs exactly at

    tau=T_11.

In particular P(tau<infinity)=1, E[u^tau]=F(u)^11, and E tau=11 mu if mu=E W is finite. This is a first-detection statement for this pulse/comparator pair, not complete identification of arbitrary twelve-dimensional ensembles.

For deterministic W=2, tau=22 exactly and the sample response is periodic with period 24: Y_t=1/4 when floor(t/2)=11 mod 12. For geometric waits P(W=w)=2^-w, N(t) is Binomial(t,1/2), and

    P(tau=t)=binomial(t-1,10)2^-t,  t>=11;
    E tau=22;
    E[Y_t]=(1/4)2^-t sum_{0<=j<=t, j=11 mod12}binomial(t,j).

Thus both clocks have mean wait 2 and mean first detection 22, but at t=11 the deterministic observer is zero while the geometric-clock expected observer is 1/8192. At t=22 their expected values are respectively 1/4 and 88179/2097152. Equal mean detection time does not restore the same passive prediction.

## A quantitative geometric-clock observer limit

In the geometric case the clock residue N(t) mod 12 is the lazy directed cycle: hold with probability 1/2, advance with probability 1/2. This is a positive observer-clock transition, not a substitute BRC-world update. Its uniform law is invariant. Over twelve ticks, increment residue 0 has probability 2/4096=1/2048 (zero or twelve advances); every other residue has probability binomial(12,r)/4096>=1/2048.

Therefore its twelve-tick matrix decomposes as

    P^12 = (3/512) U + (509/512) R,

where U has every row uniform and R is a stochastic, uniform-invariant matrix. Standard positive total-variation contraction gives

    |E[Y_t]-1/48| <= (1/4)(509/512)^floor(t/12).          (3)

The bound is deliberately elementary, not sharp. The deterministic mean-two clock keeps its nonconstant period-24 trace and does not converge pointwise. Both therefore share mean waiting and mean first detection but have different long-time observer behavior. This resolves a bounded observer question conditional on the supplied clock, while native clock selection remains open.

## Verification, reuse and frontier

`verify_brc_passive_clock.py` uses the unchanged pinned positive CWM functions through the existing loader to execute the 12-residue clock observer. The modulo-12 reduction is safe for this fixed pulse under independent hold/advance futures; it is not a quotient of the complete BRC source world. It checks exact phase observations against binomial clock coefficients, count/total/dominant accounting, the twelve-tick minorization, and the two numerical clock witnesses. Source-world suites are not rerun or counted as new experiments.

Method resolution: T0_BRC REUSE_EXECUTED for the new positive clock observer; T6 scoped quotient REUSE_APPLIED; the shared Euler held-state interface COMPOSE_APPLIED. No new general-purpose tool family, native law or Driver admission is claimed. This application also records the source-specific future obligation: establish a sourced incident read/clock protocol and then decide whether its actual transitions satisfy independence, no skipping and whole-tick observability. An externally declared convenient geometric clock is not evidence for that premise.

This completes the bounded cross-line reuse action. Further variants should wait for genuinely new clock/source evidence; they are not an automatic succession merely because the calculation passed.

Researcher-ID: EM-NATIVE-A8C19E / TASK_RESEARCH
