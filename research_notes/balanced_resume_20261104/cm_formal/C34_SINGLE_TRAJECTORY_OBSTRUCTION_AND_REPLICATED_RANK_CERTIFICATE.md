# C34: a single-trajectory calibration obstruction and a replicated-window rank certificate

Author: `EM-C34-D16900` / `TASK_RESEARCH`  
Execution provenance: `/root/research_cm_formal_1104`  
Date: 2026-11-04  
Status: `AUTHOR_PROVED_AWAITING_DISTINCT_NONCONTRIBUTING_REVIEW`  
Local identity: allocated by the current Source identity script; registration remains `REGISTER_PENDING`.  
Research-Activity-ID / formal Task claim: none. This is a direct, nonshared mathematical handoff; it does not change a shared Task, Result, claim, or acceptance state.

## 1. Exact question, consumed sources, and contribution boundary

C34 permits each instrument route to have arbitrary temporal memory. It proves population-moment calibration under independence of the **whole** error processes, and explicitly leaves sampling convergence unresolved. This note separates two questions that population identifiability alone does not settle:

1. Can a single longer trajectory consistently estimate the route gains throughout the stated class? No. A compliant static-error example has a fixed positive estimation risk even when the complete infinite trajectory is observed. Requiring stationary ergodic instruments still gives no uniform finite-length guarantee without a quantitative restriction on memory.
2. With independent repetitions of a fixed observation window, can one certify a target-dimension lower bound without first estimating gains? Yes. For two routes, invertible diagonal gains preserve the block Hankel rank. A simultaneous concentration bound and the existing deterministic minor criterion give a finite-sample certificate.

The second statement requires an **additional experimental sampling assumption**. It does not assert that recorded windows from one dependent trajectory are independent repetitions. The first statement concerns calibration; it does not claim that every rank statistic is impossible to estimate from a single trajectory.

Consumed mathematical sources:

- Main Source snapshot `39556bf5207aa5ba559a27ec591c1bc1bf43b457`, file `research_notes/divisor_extrema/20261021_c34_partial_observation_colored_readout.md`, blob `4b374626ba07ca48eea9ed853e92de00826b7526`, SHA256 `15cabd1b7cef47082a521706d5ebcb8ee48f4c6e0efaf4541fb1d3d9cf4bd1aa`: §§3,5,8,9 supply the rank bound, whole-process independence, existing counterexamples, and open sampling interface.
- Separately preserved branch source `397aeed183046480d083290db92dc1c79b980a74`, file `research_notes/balanced_resume_20261028/formal/round4/C34_CENTERED_COVARIANCE_SUPPLEMENT.md`, read from its local preserved artifact, SHA256 `1377b67f565385cbd61e8a7cd5fad02468c726689e506c5bbb6dbac959455c53`: defines centered cross-covariance, proves its diagonal-gain factorization, and separates raw gain-calibration moments from centered entries. This note consumes that correction; it does not reissue it as a new result.
- At the same main snapshot, C35 (`20261023_c35_boundary_return_bidirectional_identifiability.md`) was read to avoid repeating its return-path, gauge, and weak-connection results. A bounded scan of C51–C56 and the research-note collections found deterministic error envelopes and explicit finite-sample limitations, but no instance of the specific results below. This is a bounded project deduplication check, not a claim of general statistical novelty.

The methods are standard: a two-point testing lower bound, a coupling, Hoeffding's inequality, invariance of rank under invertible diagonal multiplication, and a Neumann-series perturbation test. The contribution is their explicit use at C34's unfilled sampling interface. No new general tool family is claimed. There is no new simulation, arithmetic research program, external data set, or actual instrument-independence test.

## 2. The population model and terminology

The model is external classical probability. Let the stationary target be `S_t ∈ {−1,+1}^M`. Let `H` select `q` distinct labelled original target coordinates, and set

\[
Y_t=HS_t,\qquad v=\mathbb E Y_t,\qquad
\Gamma_\ell=\mathbb E[(Y_{t+\ell}-v)(Y_t-v)^T].
\]

Route `r` reports

\[
X^{(r)}_{a,t}=E^{(r)}_{a,t}Y_{a,t},\qquad
\eta_{r,a}=\mathbb E E^{(r)}_{a,t}>0,\qquad
D_r=\operatorname{diag}(\eta_{r,1},\ldots,\eta_{r,q}).
\]

Every error process is stationary and takes values in `{−1,+1}^q`. The sigma-algebras of the whole target process and of the whole error processes are mutually independent. Within a route, temporal and spatial dependence are unrestricted. Time and coordinate labels are aligned and observations do not perturb the target; these remain model assumptions, not consequences of the formulas.

For distinct routes `r,s`, write

\[
\mu_r=\mathbb E X^{(r)}_t,\quad
R^{rs}_\ell=\mathbb E[X^{(r)}_{t+\ell}(X^{(s)}_t)^T],\quad
G^{rs}_\ell=R^{rs}_\ell-\mu_r\mu_s^T.
\]

The consumed centered supplement establishes

\[
\mu_r=D_rv,\qquad G^{rs}_\ell=D_r\Gamma_\ell D_s. \tag{2.1}
\]

Its three-route calibration uses the **raw**, same-time, same-coordinate moments

\[
g_{rs,a}=\mathbb E[X^{(r)}_{a,t}X^{(s)}_{a,t}]
=\eta_{r,a}\eta_{s,a},\qquad
\eta_{1,a}=\sqrt{g_{12,a}g_{13,a}/g_{23,a}}. \tag{2.2}
\]

Equations (2.1)–(2.2) concern exact population expectations, not expectations conditional on a realized instrument history. At positive lag, `G` need not be symmetric.

## 3. A compliant single-trajectory obstruction

**Theorem 1 (a fixed nonvanishing calibration risk).** Inside the original C34 assumptions, there are two models with common route gains `η_0=1/3` and `η_1=2/3` such that the total variation distance between their complete observed laws is `1/4`, both for every trajectory length `T≥1` and for the whole infinite trajectory. Consequently, every measurable estimator of the common gain satisfies

\[
\max_{j\in\{0,1\}}
\mathbb P_j\{\lvert\widehat\eta-\eta_j\rvert\ge 1/6\}
\ge 3/8. \tag{3.1}
\]

Randomized estimators are included. Therefore no sequence of estimators based on one lengthening trajectory is consistent on this two-point subfamily.

**Construction.** Take `q=M=1`. The target `Y_t` is the stationary symmetric two-state Markov chain

\[
\mathbb P(Y_{t+1}=y'\mid Y_t=y)=\frac{1+c yy'}2,
\qquad c=\frac12.
\]

This is the strict copy-refresh model with `P=1`, refresh probability `δ=1/2`, and fair refresh `p=1/2`; its transition entries are positive. Its entire law is invariant under the global transformation `Y↦−Y`.

Independently of the target, choose three mutually independent signs `B_r` with

\[
\mathbb P_\eta(B_r=+1)=\frac{1+\eta}{2},\qquad
E^{(r)}_t=B_r\quad\hbox{for all }t,\qquad
X^{(r)}_t=B_rY_t.
\]

The three whole error processes are independent, each is stationary with strictly positive bias `η`, and each is independent of the target. The unlimited within-route memory is explicitly permitted by C34.

**Proof.** Define `C_2=B_1B_2` and `C_3=B_1B_3`. The observed three-route history is in measurable bijection with

\[
\bigl((X^{(1)}_t)_t,C_2,C_3\bigr),
\]

because `C_r=X^{(1)}_tX^{(r)}_t` at any observed time, and `X^{(r)}_t=C_rX^{(1)}_t`. Conditional on any triple `B`, the first history is either `Y` or `−Y`, hence has the same target law. It is therefore independent of `B` and of `(C_2,C_3)`, and its law does not depend on `η`.

For `u,v∈{−1,+1}`, expansion of the sign indicators gives

\[
\mathbb P_\eta(C_2=u,C_3=v)
=\frac14\bigl(1+\eta^2u+\eta^2v+\eta^2uv\bigr). \tag{3.2}
\]

In particular, the probability of `(u,v)=(+1,+1)` is `(1+3η²)/4`; the other three probabilities are each `(1−η²)/4`. At `η_0=1/3` these are `1/3,2/9,2/9,2/9`, and at `η_1=2/3` they are `7/12,5/36,5/36,5/36`. Their total variation distance, defined as half the sum of the absolute probability differences, is

\[
\frac12\left(\frac14+3\cdot\frac1{12}\right)=\frac14. \tag{3.3}
\]

Taking a product with the common independent first-route history preserves total variation: integrating over that history gives the upper bound, and events depending only on `C` attain it. The same argument holds on infinite path space. Thus (3.3) is the exact distance of the observed laws, not merely a bound for a selected statistic.

For completeness, a test `φ` of two probability laws satisfies

\[
\mathbb P_0(\phi=1)+\mathbb P_1(\phi=0)
\ge 1-\operatorname{TV}(\mathbb P_0,\mathbb P_1).
\]

For a deterministic test this follows directly by writing the left side as `1+P_0(A)−P_1(A)` for `A={φ=1}`. Integrating its randomized acceptance probability proves the same bound for randomized tests. Given an estimator, take `φ=1` when `η̂≥1/2`. Each wrong classification implies estimation error at least `1/6` in the corresponding model. The two estimation-error probabilities therefore sum to at least `3/4`, proving (3.1). ∎

The exact population identities (2.2) remain valid in both models. Yet in a realized single trajectory the empirical same-time product is `B_rB_s` at every time and does not approach `η²`. Infinite target dynamics supply no fresh instrument draw. This is a sampling obstruction, not a contradiction of population identifiability. It also differs from C34's existing shared-history counterexample: **the routes in this construction really are independent as whole processes**.

## 4. Ergodicity alone gives no uniform finite-length guarantee

**Theorem 2 (arbitrarily slow, but ergodic, instruments).** If C34 is strengthened to stationary ergodic instrument processes but without a quantitative dependence bound, then for every `T≥1` and every estimator based on `T` observations there is a member of a two-gain, finite-state Markov instrument family for which

\[
\mathbb P\{\lvert\widehat\eta_T-\eta\rvert\ge1/6\}\ge5/16. \tag{4.1}
\]

This is a failure of a guarantee uniform over instruments; it does not assert failure of pointwise consistency when a particular mixing instrument is fixed.

**Proof.** Retain the target and initial independent signs from Theorem 1. On each route, independently at each transition, retain the previous sign with probability `1−λ`, or with probability `λ` redraw an independent sign of mean `η`. Start each route in that sign distribution. For `0<λ≤1` and `0<η<1`, the transition matrix

\[
(1-\lambda)I+\lambda\mathbf 1\pi_\eta^T
\]

has positive entries, so the stationary route is irreducible, aperiodic and ergodic. The routes and target remain mutually independent as whole processes.

Couple this process to the static construction by sharing the target and initial signs. Unless at least one refresh is attempted among the `3(T−1)` instrument transitions, all observations coincide. For the observed length-`T` law, the coupling inequality gives

\[
\operatorname{TV}(P_{\eta,\lambda}^{(T)},P_{\eta,0}^{(T)})
\le1-(1-\lambda)^{3(T-1)}
\le3(T-1)\lambda.
\]

The triangle inequality and (3.3) imply

\[
\operatorname{TV}(P_{\eta_0,\lambda}^{(T)},P_{\eta_1,\lambda}^{(T)})
\le\frac14+6(T-1)\lambda.
\]

The same testing argument then gives a maximal estimation-error probability at least

\[
\frac38-3(T-1)\lambda.
\]

Choose `λ=1/(48 max{1,T−1})`. The bound is at least `5/16` for every `T`. This choice varies with `T`, exactly as allowed when disproving a uniform guarantee over the ergodic class. ∎

## 5. Two-route rank does not require gain calibration

We now impose the **additional inherited affine target relation**

\[
\Gamma_\ell=HA^\ell\Sigma H^T,\qquad \Sigma=\operatorname{Cov}(S_t), \tag{5.1}
\]

with the original model's `M` target coordinates. Calibration alone does not imply (5.1). Fix distinct routes `r,s` and positive integers `u,w`. Put `L=u+w−2`, and define block matrices

\[
K_\Gamma=[\Gamma_{i+j}]_{0\le i<u,\,0\le j<w},\qquad
K_G=[G^{rs}_{i+j}]_{0\le i<u,\,0\le j<w},
\]

each of size `uq×wq`.

**Proposition 3 (gain-free rank identity).** Under (2.1), (5.1), and strictly positive coordinate gains,

\[
K_G=(I_u\otimes D_r)K_\Gamma(I_w\otimes D_s),
\quad
\operatorname{rank}K_G=\operatorname{rank}K_\Gamma\le M. \tag{5.2}
\]

**Proof.** The block `(i,j)` of the product is `D_rΓ_(i+j)D_s`, which is `G_(i+j)^{rs}` by (2.1). Both block diagonal matrices are invertible. Moreover

\[
K_\Gamma=
\begin{bmatrix}H\\HA\\\vdots\\HA^{u-1}\end{bmatrix}
\begin{bmatrix}\Sigma H^T&A\Sigma H^T&\cdots&A^{w-1}\Sigma H^T\end{bmatrix}
\]

has inner dimension `M`. This proves (5.2). ∎

Thus a certified `ρ×ρ` nonzero minor of the **uncalibrated, centered cross-route** matrix already proves `M≥ρ`, and at least `max{0,ρ−q}` original target coordinates are hidden. No third route, gain estimate, or numerical lower bound on a gain is required for this implication. Invertibility of `A` and positive definiteness of `Σ` are not needed for the displayed rank bound. This does not identify the hidden graph or produce a legal binary realization of size `ρ`.

## 6. A finite-sample certificate from independent window replicas

**Additional sampling assumption.** Observe `N` independent, identically distributed replicas of the **joint** target-and-two-instrument window `(X^(r)_t,X^(s)_t)_(0≤t≤L)`. The joint law in each replica satisfies §2 and (5.1). Independence across replicas includes the latent instrument histories: independent target preparations alone are insufficient. Dependence within a window and within one route remains unrestricted. Values of `N,u,w` and a confidence error `α∈(0,1)` are fixed in advance.

For replicas `n=1,…,N`, define

\[
\widehat R_\ell=\frac1N\sum_{n=1}^N
X^{(r)}_{n,\ell}(X^{(s)}_{n,0})^T,\qquad
\widehat\mu_{r,\ell}=\frac1N\sum_n X^{(r)}_{n,\ell},\qquad
\widehat\mu_{s,0}=\frac1N\sum_n X^{(s)}_{n,0},
\]

\[
\widehat G_\ell=\widehat R_\ell-
\widehat\mu_{r,\ell}\widehat\mu_{s,0}^T,
\qquad
\widehat K_G=[\widehat G_{i+j}]_{0\le i<u,\,0\le j<w}.
\]

Stationarity makes the expectation of each `μ̂_(r,ℓ)` equal to `μ_r`; using separate lag means makes the concentration bookkeeping explicit. The centered empirical covariance need not be unbiased; unbiasedness is not used.

The number of scalar empirical raw moments and means used is

\[
K=(L+1)q^2+(L+2)q,
\qquad
\delta=\sqrt{\frac{2\log(2K/\alpha)}{N}}. \tag{6.1}
\]

**Lemma 4 (simultaneous entrywise envelope).** With probability at least `1−α`, all estimated raw moments and means differ from their population values by at most `δ`, and consequently

\[
\max_{0\le\ell\le L,\,a,b}
\lvert[\widehat G_\ell-G^{rs}_\ell]_{ab}\rvert\le3\delta. \tag{6.2}
\]

**Proof.** Every scalar empirical moment is an average of `N` independent variables in `[−1,1]`. The standard bounded-variable concentration estimate is

\[
\mathbb P\{\lvert\overline Z-\mathbb EZ\rvert>\delta\}
\le2e^{-N\delta^2/2}.
\]

One self-contained derivation is as follows. For a variable supported on `[−1,1]`, the second derivative of its log moment-generating function is a variance under a tilted law, at most `1`. After centering, the value and first derivative at zero vanish. Integrating this second-derivative bound gives `log E exp(θ(Z−EZ))≤θ²/2` for real `θ`. Independence, the exponential Markov inequality and optimization at `θ=δ` give the upper tail for the sample mean; applying the same argument to `−Z` gives the lower tail. A union bound over the `K` scalar quantities gives exceptional probability at most `2K exp(−Nδ²/2)=α`. Dependence between different scalar entries causes no problem for this union bound.

On this simultaneous event, empirical and true means all lie in `[−1,1]`. If `a,b` denote one empirical mean pair and `a_0,b_0` the corresponding true pair, then

\[
|ab-a_0b_0|=|(a-a_0)b+a_0(b-b_0)|\le2\delta.
\]

Adding the raw-moment error proves (6.2). No `δ²` term is needed. ∎

**Theorem 5 (replicated-window certificate).** Form `K̂_G` as above. If a square `ρ×ρ` minor `Ĵ` is invertible and

\[
3\rho\delta\,\|\widehat J^{-1}\|_\infty<1, \tag{6.3}
\]

then return the assertion `M≥ρ`, with hidden-coordinate lower bound `max{0,ρ−q}`. Here `||·||_∞` is the induced maximum absolute row-sum norm. With probability at least `1−α`, **every assertion returned by this rule is true**.

**Proof.** On the simultaneous event of Lemma 4, let `J` be the same minor of the true `K_G`. Then

\[
\|J-\widehat J\|_\infty\le3\rho\delta,
\quad
\|\widehat J^{-1}(J-\widehat J)\|_\infty<1.
\]

The Neumann series makes `I+Ĵ⁻¹(J−Ĵ)` invertible; multiplying it by `Ĵ` proves that `J` is invertible. Hence `rank K_G≥ρ`, and Proposition 3 gives the claim. ∎

The order `ρ` and the chosen rows and columns may be selected after inspecting this **fixed** data set: the entrywise event already controls every minor of the prescribed matrix. No union bound over minors is necessary. Repeatedly changing `N`, the lag window, or `α` after inspecting data is not covered by this fixed-design statement and would require an appropriate simultaneous or sequential guarantee.

This is a bound on false certificates, not a promise that the test will return a certificate at a universal sample size. Small unknown gains can make `K_G` poorly conditioned, and a rank-deficient or insufficiently excited window may have no desired nonzero minor. A numerical implementation must also certify the inverse norm and account for computational rounding; no such implementation or observed-data result is claimed here.

## 7. What is paid, and what remains open

The following limited obligations are paid by the written arguments, pending distinct review:

- C34's assumptions alone cannot support a general single-trajectory gain-consistency claim; an exact admissible two-point obstruction is supplied.
- Stationary ergodicity alone supplies no uniform finite-length gain guarantee; the missing quantitative dependence input is exhibited with finite-state instruments.
- Under genuine independent replicas, two-route centered moments admit a fixed-design finite-sample dimension lower-bound certificate without gain calibration. Its experimental assumptions, failure probability, centering error and matrix perturbation step are explicit.

Remaining scientific work includes establishing actual cross-route whole-process independence, designing genuine independent replicas or proving a quantitative dependence model, incorporating disturbances and timing errors, obtaining useful data-specific power/sample requirements, and any assertion about the actual physical target or its native update law. No result here infers native space, time, energy, prime generation, or a full graph from a covariance rank. Original coordinate labels, route identity, relative time and joint experiment identity are retained; the rank is a declared observer statistic, not a replacement for the joint histories.

The argument is a written probability/matrix proof. There was **no execution of a mathematical research program**, no rerun of the C34 BRC pipeline, and no alternate arithmetic engine presented as an authorized execution. File inspection, identity allocation, JSON validation and content hashes are control/provenance operations only. No formal Task core or shared state machine was edited. Root contributes zero mathematical votes. This author's proof and self-check are not independent review.

## 8. Handoff record

The companion JSON specifies exact inputs, outputs, restrictions and source versions for reuse. The author paper and interface are to be frozen by SHA256 before a distinct noncontributing reviewer examines them. A favorable review, if obtained, should be recorded separately against those exact bytes. Historical source acceptance and an owner's filing action do not count as independent votes for these new statements.

Researcher-ID: EM-C34-D16900 / TASK_RESEARCH  
EM-Source-Status: Read=Verified snapshot reused (`39556bf5207aa5ba559a27ec591c1bc1bf43b457`) and preserved C34 centered supplement; Write=⚠ Not written — Source publication pending; local artifacts preserved. Identity registration remains pending.
