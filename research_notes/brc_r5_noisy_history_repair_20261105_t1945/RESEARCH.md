# R5 — Noisy history-repair tags: exact finite-signal support and sharp rational threshold

2026-11-05 (Asia/Shanghai). AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.

## Mother objective and source

The R5 mother question is whether strictly positive finite P/Q stopping BRC admits equal **complete four-observer** convex hulls for full-history FULL_HIST and seedless LR, despite unequal **actual real-behavior** observation images. We retain the frozen scientific inputs GLOBAL `a01383f825ef9d43b4b754254303298c64041568` and EM `86149263e38c22292c9def1e0f69092efa1be77e`, and reuse the verified shared-gate theorem at EM commit `e121e1927232baee2e5b49863c72c01d406010ed` and the strictly positive four-stage model S at EM commit `8275f4043ca50e00ca8078d52bb7448c54189243`. The complete observation is `O4=(P[declare Q],Q[declare P],E_P[tau],E_Q[tau])`. Behavioral policies permit arbitrary real probabilities, but no external persistent seed.

We introduce the intermediate observer **LR+TAG**, which sees (time, likelihood ratio) and a noisy incoming-history tag at one merged nonterminal node. This new observer is a controlled BRC information-repair experiment, not a change to the original R5 FULL or LR definitions. BRC branch carriers retain positive rational mass and provenance labels until the relevant future observer operations can be certified to descend. No native X6 physical dynamics is asserted; P000 and the ACTIVE worldview remain unchanged.

## Theorem 1 — finite stochastic tag theorem

For a fixed linear direction in four-observer space suppose the **complete globally optimized** finite stopping problem admits the exact reduction

$$
J=C+\sum_{i=1}^m w_i a_i(A_i+u_i z_i).
$$

Here `m>=1`, `w_i>0`, and independently controllable upstream `a_i in [0,1]` correspond to distinct observable incoming keys. `A_i,u_i` are real increments; FULL_HIST selects independent downstream `z_i`, while LR must select one common `z`. Let a finite tag alphabet Y be emitted after upstream selection, with stochastic kernel `T(y|i)>=0`, `sum_y T(y|i)=1`. Conditional on incoming history, the tag is independent of upstream private action randomization and affects only the permitted downstream choice `z_y`, not transition laws or costs. Write `[x]_+=max(0,x)` and `T(S|i)=sum_{y in S}T(y|i)`. Then, **for all real behavior probabilities**,

$$
\boxed{h_{\mathrm{TAG}}=C+\max_{S\subseteq Y}\sum_i w_i[A_i+u_iT(S|i)]_+.}
$$

The baselines are

$$
h_{\mathrm{FULL}}=C+\sum_i w_i\max(0,A_i,A_i+u_i),\qquad
h_{\mathrm{LR}}=C+\max\left\{\sum_i w_i[A_i]_+,\sum_i w_i[A_i+u_i]_+\right\}.
$$

Thus `h_LR<=h_TAG<=h_FULL`. If `T2` is a stochastic postprocessing of `T1`, then `h_TAG(T2)<=h_TAG(T1)`.

**Proof.** Fix the vector `z=(z_y)`. Incoming history i receives effective downstream continuation `t_i=sum_y T(y|i)z_y`, and hence the objective becomes `C+sum_i w_i a_i(A_i+u_i t_i)`. Maximizing the independent `a_i` gives `C+sum_i w_i[A_i+u_i t_i]_+`, a convex function of the finite vector `z in [0,1]^|Y|`. Every z is a convex combination of the cube's binary vertices, and a convex function at z is no greater than its largest vertex value. Vertices correspond to subsets S of emitted tag symbols. The LR/FULL formulas follow by, respectively, restricting all z_i equal and allowing each history its own gate. An observer with channel T1 can privately simulate any garbling T2 and perform its subsequent behavior, proving information monotonicity. QED.

The independent a_i and global Bellman-reduction assumptions are essential; an application checks all alternative stop actions and unmerged branches before applying the expression.

## Theorem 2 — sharp binary symmetric repair threshold

Use model S and support direction

$$
n=(-1,-1,-3/25,1/50).
$$

The predecessor's exactly verified Bellman coefficients are

$$
C=-43/40,\quad (w_1,w_2)=(1/2,1/2),
\quad (A_1,u_1)=(1/200,-9/500),
\quad (A_2,u_2)=(-47/400,49/400).
$$

The histories enter the merged time-3 likelihood ratio 1. Add only at this node a binary symmetric tag that reports the incoming history correctly with probability `1-eta` and incorrectly with probability `eta`, for `0<=eta<=1/2`. The conditional tag law is the same under P and Q given the incoming path, leaving likelihood ratio 1 after the tag. For `0<eta<1/2`, both tag outcomes have strictly positive probability, with the original model's P/Q transition rows strictly positive. The exact values at this direction are

$$
\boxed{
h_{\mathrm{TAG}}(\eta)=-43/40+1/400+[1/400-281\eta/4000]_+.
}
$$
[
h_{m TAG}-h_{m LR}=[1/400-281eta/4000]_+,qquad
h_{m FULL}-h_{m TAG}=min(281eta/4000,1/400).
]

The **sharp direction-specific threshold** is `eta*=10/281`. The tag improves LR's support precisely for `0<=eta<10/281`; at and above the threshold it adds zero value in this direction. For every `eta>0` the full-history advantage remains strictly positive.

**Proof.** Theorem 1 requires four downstream binary tag gate vectors `(z1,z2)`. Both uniform vectors (0,0) and (1,1) yield `1/400` above C. The reverse-label vector (1,0) yields zero because its upstream terms `(-13+18 eta)/1000` and `(-47+49 eta)/400` are negative throughout `0<=eta<=1/2`. The label-following vector (0,1) yields

$$
V_{\mathrm{follow}}=\frac12[(1/200-9\eta/500)_++(1/200-49\eta/400)_+].
$$

For `0<=eta<=2/49`, this equals `1/200-281 eta/4000`. Beyond `2/49`, the second term vanishes and the first, halved, never exceeds the uniform gate's `1/400`. On the initial interval, `V_follow=1/400` exactly at `eta=10/281`, which is smaller than `2/49`. Taking the maximum of these four values proves the tag formula. From the precursor `h_FULL=-107/100=C+1/200` and `h_LR=-429/400=C+1/400`, subtraction proves both information-gap identities. QED.

This threshold concerns one exact four-observer direction. The complete all-directions hull-equality question remains open.

## Actual executable verification

The accompanying `VERIFY.py` uses only Python 3 standard-library `fractions.Fraction` and checks all positive P/Q row identities (including conditional ratio moments). For the seven exact tag errors `{0,1/1000,1/50,10/281,1/20,1/4,1/2}`, it checks the four-selector analytic formula against independent **full four-stage tree** evaluation over 128 Bayes-reduced deterministic stop/continue patterns each, 896 evaluations in total. Optimal terminal Bayes declarations suffice at the given support direction. All formula, threshold and FULL-gap assertions passed; actual stdout is in `EXACT_OUTPUT.txt`. The general real-behavior and continuous-eta claims rely on the above proof, with finite tests supporting implementation accuracy.

## Next exact question

On all rational Bellman sign cones in the complete four-dimensional direction space, use the finite-tag formula and exact polyhedral feasibility to test the residual support gaps, then independently test real LR-image convexity under any candidate all-direction hull equality. The exact parent R5 goal is still open. Tool resolution: `REUSE_APPLIED` (BRC positive history carrier and observer semantics; predecessor shared-gate theorem). Scientific status remains authored, checked at stated scope, and unreviewed.
