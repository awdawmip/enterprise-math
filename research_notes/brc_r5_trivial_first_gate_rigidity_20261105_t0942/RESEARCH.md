# R5 — Degenerate first-gate rigidity via a two-step classification threshold

Date: 2026-11-05 (Asia/Shanghai). Research state: AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.

Mother R5 target: finite strictly positive P/Q BRC stopping model with `conv O4(FULL)=conv O4(seedless LR)` but `O4(FULL) != O4(seedless LR)`, where `O4=(eP,eQ,TP,TQ)`. This note proves a rigidity theorem for a special model family, closing the trivial-first-experiment case left open by the immediate predecessor `a72fab502e08b6ab9df6ebf67215744ac2c631a4`. Scientific input pins remain GLOBAL `a01383f825ef9d43b4b754254303298c64041568` and EM `86149263e38c22292c9def1e0f69092efa1be77e`; contemporary rules are read separately.

## 1. Model and exact theorem

Take finitely many source histories `h` with strictly positive weights `w_h`, summing to 1, and the same conditional P and Q weight at time 1 (likelihood ratio 1). The first continuation experiment is **trivial**: on continuation every source deterministically reaches time 2 with likelihood-ratio key 1. At both time 1 and time 2 all STOP/P, STOP/Q and CONTINUE choices are legal. At time 2, continuation leads to time 3, where termination and either P/Q declaration are required. Each source has a strictly positive Q terminal probability law `M_h(s)` on one fixed finite support `S ⊂ (0,∞)` with `Σ_s M_h(s)=1` and `Σ_s s M_h(s)=1`; the P terminal law is `s M_h(s)`, also positive. FULL can condition on source history; seedless LR sees only `(time, likelihood ratio)`. Arbitrary real behavioral randomization is admitted.

**Degenerate-first-gate rigidity theorem.** In this family, the following are equivalent:

(A) `conv O4(FULL) = conv O4(seedless LR)`;

(B) `O4(FULL) = O4(seedless LR)` for all real behavioral-policy observations;

(C) `M_h=M_h'` as terminal Q laws for every pair of sources `h,h'`.

Thus when the first experiment is concentrated at ratio 1, distinct source-specific terminal distributions still force strict four-coordinate supporting-hyperplane separation. Together with the predecessor's nontrivial-common-first-kernel theorem, common first kernels of both types are covered for this two-decision-gate model. Source-dependent first-stage kernels and richer topologies remain to be investigated.

## 2. Proof of (A) implies (C): exact source-sensitive support

For any `k>0`, define `C_k(r)=max(-r,-k)=-min(r,k)` and

`G_h(k) = Σ_s M_h(s) C_k(s) - C_k(1) >= 0`; `Gbar(k)=Σ_h w_h G_h(k)`.

Nonnegativity follows from convexity of `C_k` and `E_Mh[s]=1`. For any `c>=0`, choose the four-observer normal `n=(-1,-k,-c,0)`, so one unit of expected P stopping time incurs cost `c`. The weighted one-step time cost at the initial and second ratio-1 keys is `c`; at the terminal the conditional expected P time charge is also `c` per step because `Σ_s s M_h(s)=1`.

At source `h` there are three relevant deterministic continuations: stop at time 1, stop at time 2, or continue to time 3 and optimally declare according to `C_k(s)`. Their respective conditional Q-scaled payoffs are

`C_k(1)-c`, `C_k(1)-2c`, and `C_k(1)+G_h(k)-3c`.

For `c>=0` the middle payoff cannot beat the first. Therefore the FULL support is exactly

`h_FULL(n)=C_k(1)-c+Σ_h w_h (G_h(k)-2c)_+`.       (1)

Seedless LR must use the same time-1 and time-2 decisions for every source. Its terminal Bayes optimum uses the aggregated Q law `Mbar=Σ_h w_h M_h`; hence

`h_LR(n)=C_k(1)-c+(Gbar(k)-2c)_+`.                (2)

These formulae hold for the complete real-policy classes: each payoff is multi-affine in independently randomized behavioral choices, so deterministic choices attain the support maxima. Their exact support gap is the positive-part Jensen defect

`Δ(k,c)=Σ_h w_h (G_h(k)-2c)_+ - (Σ_h w_h G_h(k)-2c)_+`.    (3)

Suppose two source distributions differ. For finite positive support, the stop-loss transforms `E_M[min(S,k)]` determine the distributions: away from atoms, the derivative with respect to `k` is `Pr_M(S>k)`, and the jumps recover each atom. Thus there is a `k>0` for which the `G_h(k)` are not all equal. Let `t` lie strictly between their minimum and maximum. As all `G_h(k)>=0`, choose `c=t/2>0`. Some `G_h-t` are strictly positive and some strictly negative, making (3) strictly positive. Therefore (A) implies (C).

## 3. Proof of (C) implies (B)

Assume the terminal kernel is a common `M`. Given any FULL real behavioral policy, average its three action probabilities at time 1 over source Q weights, producing a shared seedless action. This matches total time-1 P and Q stopping/continuing masses because the ratio is 1. Average the time-2 action probabilities over the resulting source-conditional Q occupation, producing a shared seedless time-2 action. This preserves aggregate time-2 occupation and time-3 continuation mass. Since the terminal kernel is common `M`, it also preserves time-3 occupation at each terminal ratio `s`; on every time/ratio fiber P mass is `s` times Q mass. At time 3, average FULL's declaration-P probabilities against the corresponding Q occupation. This retains both error coordinates, and preserved time occupancies retain `TP,TQ` exactly. Thus every FULL four-observer vector is attained by a seedless LR behavioral policy. Reverse inclusion is immediate. (B) implies (A), completing the equivalence.

## 4. Exact rational witness and separation certificate

Set sources `A,B` with `w_A=w_B=1/2`; all time-1 and time-2 likelihood ratios equal 1. Terminal support `S=(1/2,1,3/2)` with

`M_A=(1/4,1/2,1/4)` and `M_B=(3/8,1/4,3/8)`.

All Q masses and induced P masses are strictly positive and both conditional P/Q distributions sum to 1. At `k=1`, `G_A=1/8`, `G_B=3/16`, `Gbar=5/32`. Choose `t=Gbar=5/32`, `c=t/2=5/64` and `n=(-1,-1,-5/64,0)`. Equation (3) gives `Δ=1/64`.

The exact supports are `h_FULL=-17/16` and `h_LR=-69/64`. One maximizing FULL policy is: source A STOP/Q at t=1; source B CONTINUE at t=1 and t=2; at t=3 for source B declare Q at ratio 1/2 and P at ratios 1 and 3/2. Its observer is

`W=(19/32,5/16,2,2)` and `n·W=-17/16`.

Since `||n||_1=133/64`, Hölder duality yields the exact distance certificate

`dist_infinity(W,conv O4(seedless LR)) >= Δ/||n||_1 = 1/133`.

`VERIFY.py` uses Python standard-library `Fraction` to independently enumerate all 5,184 FULL and 72 seedless LR deterministic policy assignments, check P/Q normalization and moment relations, match Bellman supports, verify W, and repeat full enumeration for six rational thresholds. Captured output is `EXACT_OUTPUT.txt`, ending `PASS_EXACT_R5_DEGENERATE_FIRST_GATE_RIGIDITY`. The quantified real-parameter theorem is proved analytically; enumeration verifies the rational instance.

## 5. BRC meaning, evidence scope, and next unit

The source label is the branch/provenance information discarded by the seedless LR quotient. Even when both early time keys are identical and the early P/Q experiment reveals no information, source-conditioned **future** terminal distribution can be tested by the four-coordinate time/error support normal. This is a typed observer-safety result for a finite stochastic BRC model; the X6 spatial ontology is unchanged.

Next discriminator: **source-dependent first-stage Q kernels** `K_h` with `Σ K_h r=1` and strict conditional positivity, where branches merge at shared time/ratio keys. Construct a small finite rational model, enumerate ALL deterministic O4 vectors, compare full convex hulls by complete rational inclusion/separation certificates, and test actual behavioral image nonmembership for a hull-equality candidate. Retain free declarations and both stopping-time coordinates. R5 mother objective remains open.

No CLAIM/Result/independent Driver admission is asserted by this author-side result.
