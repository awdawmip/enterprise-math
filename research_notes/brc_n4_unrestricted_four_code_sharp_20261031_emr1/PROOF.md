# BRC N=4 — unrestricted stochastic four-code exact minimax

**Author analytic proof / exact integer check / UNREVIEWED / NOT_ADMITTED.** 2026-10-31. Continuation of the existing five-code exact theorem in PR #1757 at `f8e934df7c9a7897af16fe8770c040491e6845ad`. This proof derives a strictly stronger and new result for **four**, not five, encoder symbols. No physical X6 dynamics or native role admission is claimed.

## Exact experiment and claim

The original strictly positive P/Q 16-leaf experiment has prepared input `x=(S,b)`, with `S∈{AU,AV,BU,BV}`, `b∈{Q,P}`. Every `(S,J)` has two equally likely conditional K leaves. In order `AU_Q,AU_P,AV,BU_Q,BU_P,BV`, the P/Q-independent prepared conditional law of the six third-stage likelihood-ratio classes `AU0,AU1,AV,BU0,BU1,BV` is

```
M = (1/20) [
  [10,10, 0, 0, 0, 0],
  [ 9,11, 0, 0, 0, 0],
  [ 0, 0,20, 0, 0, 0],
  [ 0, 0, 0,10,10, 0],
  [ 0, 0, 0, 2,18, 0],
  [ 0, 0, 0, 0, 0,20]
].
```

AV_P/AV_Q and BV_P/BV_Q have identical conditional futures and can be represented by one row apiece. The real source is still eight prepared inputs. A common, arbitrary **row-stochastic** encoder E maps all eight inputs to at most four symbols **before** J is drawn and before a lawful future strategy H is chosen. A strategy-dependent stochastic decoder D_H sees only the code and H. It may synthesize a fresh future record; same-realized-path restoration is not part of the target. The public record `O=(T,Decision,Z_BU)` includes a BU-only sensor `Z=J xor Bernoulli(ε)`, with absent symbol for non-BU and `0≤ε≤1/2`. All original lawful S23/S2 causal stop/decision strategies are allowed, including randomized and adaptive strategies.

For F equal to all lawful S23 or all lawful S2 strategies, define

`R4(F;ε) = inf_{E, |code|≤4} sup_{H∈F} inf_{D_H} max_x TV(L_H(.|x), (E D_H)(.|x))`.

**Theorem.** For every real `ε∈[0,1/2]`,

```
R4(all S23;ε) = R4(all S2;ε) = 1/5.
```

The encoder may be stochastic and cross-source-sharing; decoders may vary with H. This completes the formerly open unrestricted four-symbol case and shows stochastic cross-source mixing does not improve the known deterministic 1/5 rate in this model.

## All-encoder lower bound, without stochastic restrictions

For each of the 64 subsets A of the six third-stage likelihood-ratio classes, define a lawful H_A: continue at stage two for every S, stop at stage three, declare Decision=P exactly when its class lies in A. These policies satisfy S2's AU/BU equal-continue requirement and S23's equal-likelihood-ratio action requirement. They do not read a future K. The event `Decision=P` has conditional probabilities `M 1_A` across the six prepared rows.

Let E be **any** row-stochastic 6×4 encoder matrix (restrict any eight-row encoder to the six distinct prepared rows; pad to four columns if needed). The homogeneous system

`w^T E=0,  w_AU_Q=w_AU_P`

has six unknowns and at most five independent linear equations. Consequently some nonzero real w solves it. Because `E·1=1`, this w also satisfies `sum_i w_i=0`.

Every policy-specific decoder for the public record induces a decision-P probability vector `d_A∈[0,1]^4`. If the worst full-record TV error is at most δ, then in every row `|M_i(A)-(E d_A)_i|≤δ`. Multiplication by w and summation gives

`|sum_{j∈A}(w^T M)_j|≤δ ||w||_1`.

Since the coordinates of `w^T M` sum to zero, maximizing the left side over the **64 lawful subsets** A yields exactly `||w^T M||_1/2`. Thus, for any nonzero such w,

```
δ ≥ ||w^T M||_1 / (2 ||w||_1).                    (1)
```

If decoder infima are not attained, apply the argument to δ+η and send η to zero; the same result follows. Note that this bound uses only a measurable event of the **complete** public output and is therefore valid for every ε.

Now prove the specific sharp reverse inequality that is valid on the four-dimensional hyperplane `w_AU_Q=w_AU_P` intersected with the zero-sum constraint. Write

`w=(a,a,b,c,d,e)`, `2a+b+c+d+e=0`, `s=c+d`, and `B=2|a|+|b|+|e|`.

The zero-sum relation gives `B≥|s|`. Direct multiplication by the *exact* M yields

```
||w^T M||_1
 = B + |c/2+d/10| + |c/2+9d/10|
 = B + max(|s|, (4/5)|d|)
 ≥ B + (4/5)|d|.                                   (2)
```

By the triangle inequality and `B≥|s|`,

```
||w||_1 = B + |s-d|+|d|
        ≤ B + |s|+2|d|
        ≤ 2B + 2|d|.                                (3)
```

Combining (2)–(3), with `B≥0`,

`||w^T M||_1 ≥ B+(4/5)|d| ≥ (2/5)(2B+2|d|) ≥ (2/5)||w||_1.`

This is sharp for `w=(0,0,0,1,-1,0)`, whose ratio equals 2/5. Substituting in (1) proves `δ≥1/5` **for every** stochastic encoder with at most four symbols. The one extra linear equation `w_AU_Q=w_AU_P` is precisely why this proof does not improperly give the five-code lower bound 1/5.

## Constructive upper bound for the entire lawful language

Use exactly four deterministic codes `{AU*,AV,BU*,BV}` by retaining S and discarding the preparation b. For both AU preparations the common decoder draws `J=1` with probability `21/40`, the midpoint of `1/2` and `11/20`. For both BU preparations it draws `J=1` with probability `7/10`, the midpoint of `1/2` and `9/10`. AV and BV use their exact common `J=1/2`. Thereafter it samples fair K if reached, runs the declared independent BU sensor with error ε, and executes the exact chosen H; these conditional kernels are shared by P/Q.

In the complete labeled future, AU prepared error is exactly `1/40`; BU prepared error is exactly `1/5`; AV/BV errors are zero. Any lawful terminal record is a further stochastic map of that future. Total-variation data processing gives worst full-record error at most `1/5` for **every** stochastic or adaptive S2/S23 policy, for every real ε. For H that distinguishes BU0 from BU1 via Decision, this bound is attained. Together with the lower bound,

`R4(all S23;ε)=R4(all S2;ε)=1/5.`

## Validation and scientific scope

`VERIFY.js` actually executed with exact integral arithmetic. It rebuilt P/Q's 16 strictly positive leaves and both 240/240 normalizations; checked 14640 nonzero integer w samples in the hyperplane as a consistency grid, the sharp BU witness, and the complete publicly observed distributions for 64 legal H_A × six prepared states × ε∈{0,1/8,1/4,1/2} = 1536 exact comparisons. The maximal L1 numerator was 128 over common denominator 320, hence TV=128/640=1/5. `RUN_EVIDENCE.txt` preserves the actual output. **The continuum, arbitrary stochastic encoder, and all adaptive lawful-policy conclusions rest on the preceding algebra and data-processing proof, not the finite grid.**

This is a precise statistical experiment/Blackwell-deficiency rate-distortion instance, not a claimed novel general theorem of statistical comparison. BRC interpretation retains all source-preparation and branch labels until the observer-specific quotient is certified. The native Heartbeat World remains a six-axis Cell torsor with time separately typed; no physical transition, causal timing calibration, or genuine X6 source-preparation mechanism is inferred. This is portable author-side mathematics, not a native CLAIM, Result, reviewer signoff or Foundation admission.