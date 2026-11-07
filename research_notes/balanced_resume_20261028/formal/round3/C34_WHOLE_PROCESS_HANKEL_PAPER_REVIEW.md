# C34 whole-process readout and Hankel bounds: bounded independent paper review

Reviewer: EM-DIRECT-099801  
Research-Activity-ID: RA-BALANCE-FORMAL-20261028-099801  
Date: 2026-10-28  
Status: NONAUTHOR_PAPER_REVIEW_COMPLETED; VALID_WITH_REQUIRED_NOTATION_SUPPLEMENT; NOT_UNCONDITIONAL_PASS; NO_FORMAL_ACCEPTANCE

## Exact object, authority, and duplicate coverage

Reviewed source: `research_notes/divisor_extrema/20261021_c34_partial_observation_colored_readout.md` at immutable commit `56f5938da3f707c1d9db1b39afde124eac4634e3`, Git blob `4b374626ba07ca48eea9ed853e92de00826b7526`, 11,563 UTF-8 bytes, SHA256 `15cabd1b7cef47082a521706d5ebcb8ee48f4c6e0efaf4541fb1d3d9cf4bd1aa`.

Source link: https://github.com/awdawmip/enterprise-math/blob/56f5938da3f707c1d9db1b39afde124eac4634e3/research_notes/divisor_extrema/20261021_c34_partial_observation_colored_readout.md

The saved actual connector response at `agent_artifacts/curation_all_recent_20261022/number_sources/raw/20261021_c34_partial_observation_colored_readout.md.json` contains the explicit immutable-ref request and full source. Both its Git blob and SHA256 were recomputed from the captured content. A new default-branch fetch returned precisely the same blob and content hash; its actual response is saved locally as `formal/round3/c34_current_fetch_actual.json`. This establishes same-content currency at that read, not an invented current commit pin.

The necessary inherited dependency is C33, `research_notes/divisor_extrema/20261021_c33_temporal_inverse_readout_source_count.md`, at the same immutable commit: blob `577c78452df43242bd106f2ec40fca8145dd6342`, 10,827 bytes, SHA256 `9a336e910dfb17c369a3c9b2f778967043a3600a3b3239aa2a6626cbfabc34b9`. Its actual captured content was read; in particular §§1–3 distinguish centered covariance from raw moments and calibrated inversion from the older single-route unknown-noise inversion. This report does not re-review C33 as a whole.

Before doing mathematics, the existing RA alias passed the native startup bookkeeping check: activity/persistence allowed; no claim, formal review, mathematical acceptance, or Working Truth authority. This is a delegated, nondecisive paper review recorded under that activity, not execution or adjudication of a formal Task. The formal Task inventory remains UNKNOWN. No checker, scientific program, synthetic experiment, or formal Task core was invoked, and the original C34 `REGISTRATION_PENDING` history is not retrospectively authorized.

Duplicate-coverage evidence is bounded: monthly library entry `NT-C34-PARTIAL-COLORED` has `existing_review_sources: []`; two narrow current GitHub searches returned no hits; the coordinating review agent reported no C34/exact-hash match in that reviewer's own ledger/reports. Neither failed search nor one ledger proves global absence of a prior review. These checks found no sufficient same-version review to consume instead of this delegated unit. The source itself remains labelled `SELF_CHECKED_UNREVIEWED / CONDITIONAL_MODEL_THEOREMS`.

## Independence and scope

I did not author C34 or its C33 dependency and did not participate in their construction. Root/control supplied the source pin and task boundary; the review coordinator supplied only the bounded absence-of-coverage statement, not a mathematical judgment. Shared repository/control context is disclosed; this is not a blind review. Root contributes no mathematical vote.

The mathematical scope is C34 §§3, 5, and 8, with §1/C33 inputs and the §6 instrument-mode example used to check the interpretation. I independently reconstructed the algebra below on paper. Reported historical exact fractions, finite transition enumerations, recurrence-matrix checks, result counts, and all eleven computational result files were not reproduced or certified. The expanded English proof/computation package referred to by the source was not inspected. This is not a whole-paper, novelty, physical, or native-semantics acceptance.

All probability and linear algebra below are explicitly external model statements. Arithmetic diagram directions are not native spatial dimensions; rounds are not native heartbeat time. There is no bridge here to native E/J, physical source count, ordinary prime count, or a native plane.

## 1. The inherited model supplies the required covariance identity

Within the declared finite binary process, the update uses row-stochastic `P`, `0 < δ_i,p_i < 1`,

`A_ij = (1−δ_i)P_ij`,  `b_i = δ_i(1−2p_i)`.

The Markov update and coordinatewise conditional independence are part of the model. Its centered state `x_t = S_t−m` has conditional mean `E[x_(t+1) | full past through t] = A x_t`. Tower iteration then gives, for stationary exact population moments,

`C_l = E[x_(t+l)x_t^T] = A^l Σ`,  `Σ = C_0`.

Each full state can transition to each other state with positive probability, since simultaneous independent refresh into any sign vector has positive probability. Thus the stationary distribution has full support. For a nonzero real vector `v`, the function `v^T S` is not constant on the full binary cube: changing a coordinate with nonzero coefficient changes its value. Consequently `v^T Σv > 0` and `Σ` is invertible. No invertibility of `A` follows or is needed below.

This argument does not infer the declared update model from second moments alone. The source correctly retains that direction of implication.

## 2. Hankel rank: the lower bound and the realization boundary

For a known observation map `H`, the exact projected covariances are

`Γ_l = H A^l Σ H^T`.

For positive integers `u,v`, form `K_(u,v) = [Γ_(i+j)]_(0≤i<u,0≤j<v)`. Direct multiplication gives

`K_(u,v) = [H; HA; …; HA^(u−1)] [ΣH^T, AΣH^T, …, A^(v−1)ΣH^T]`.

The two internal dimensions equal the number `M` of target coordinates, so every such rank is at most `M`. If `H` selects `q` known distinct original coordinates and a finite block has exact rank `ρ`, then `M ≥ ρ` and the number of unobserved original coordinates is at least `max(0,ρ−q)`. A number of arbitrary scalar mixtures or instrument channels is not, without that coordinate-selection condition, the number `q` of directly observed target coordinates.

This is a necessary lower bound inside the family. It does not construct a legal `ρ`-coordinate binary process, a local divisor-graph update, or a nonnegative row-substochastic matrix in that reduced dimension. A minimal abstract linear response realization can violate those restrictions. A finite rank plateau by itself gives no infinite-sequence upper bound. The source expressly preserves both boundaries.

The perturbation statement in §3 is also correct as a deterministic, calibrated-matrix certificate. If an invertible `ρ×ρ` reference minor is `J` and each entry of the perturbation `E` is at most `ε` in absolute value, then

`||J^−1 E||_∞ ≤ ||J^−1||_∞ ||E||_∞ ≤ ρ ε ||J^−1||_∞`.

When this is strictly below one, `J+E = J(I+J^−1E)` is invertible. This is not a confidence statement for finite samples. I checked this implication, not the historical rational norm or determinant values reported for a particular instance.

## 3. Three-view calibration and the exact independence condition

The hypothesis needed for the paper's factorization is independence at the process level: the joint error process `(E^(1), E^(2), E^(3))` is independent of the whole target process, and the three whole error processes are mutually independent. Equivalently for these claims, each used pair of error processes is independent and their pair is jointly independent of the target process. Mere independence of each separate error from the target, without joint independence of the pair from the target, is not the hypothesis being verified.

Within a route, coordinates and times may be arbitrarily dependent. Each route has a time-independent positive mean `η_(r,i) = E[E^(r)_(i,t)] > 0`; the sign variables have values in `{−1,+1}`. The same-target, same-coordinate alignment and lack of target disturbance are assumptions, not conclusions of calibration.

Write `X^(r)_(i,t) = E^(r)_(i,t) S_(i,t)` and `D_r = diag(η_(r,i))`. The reported mean satisfies `mhat_r = D_r m`. At the same target coordinate and time, the raw cross-route product is

`g_(rs,i) = E[X^(r)_(i,t) X^(s)_(i,t)] = E[E^(r)_(i,t) E^(s)_(i,t)] = η_(r,i)η_(s,i)`.

The cancellation uses `S_(i,t)^2=1`, and route independence gives the last equality. Hence all denominators are strictly positive and

`η_(1,i)^2 = g_(12,i)g_(13,i)/g_(23,i)`

and its cyclic companions recover the positive biases uniquely. A nonzero target mean is unnecessary. If the target mean is nonzero, the separate two-view formula follows from `mhat_(1,i)/mhat_(2,i)=η_(1,i)/η_(2,i)`, so the source correctly avoids a universal three-view minimality claim. Zero bias or unknown sign conventions would remove the stated invertibility or uniqueness; neither is in the theorem's domain.

For different routes and any lag, joint process independence yields entrywise

`E[X^(r)_(i,t+l) X^(s)_(j,t)] = η_(r,i)η_(s,j) E[S_(i,t+l) S_(j,t)]`.

After subtracting the product of the reported means, the centered cross-covariance is therefore

`G_l^(rs) := E[(X^(r)_(t+l)−mhat_r)(X^(s)_t−mhat_s)^T] = D_r C_l D_s`.

This holds also at lag zero, and does not require whitening within either route. Each `D_r` is invertible, so the means and the target covariances at the observed positions are recovered. With all coordinates visible, `A = C_1 Σ^−1` follows directly, even if `A` is singular. With partial coordinates, the recovered object is the projected sequence `Γ_l`; a `q`-coordinate regression is not a recovered full hidden graph.

The probability-domain and innovation-covariance checks in the source are necessary model-consistency tests. Passing them or observing cross-route agreement does not prove the process independence assumption, conditional independence of updates, or membership in the target family.

### Precision note: raw moments and centered cross-covariances must stay distinct

C34 §5, the paragraph beginning `不同路r!=s的任意时滞l（含0）满足G_l^(rs)=D_r C_l D_s`, does not explicitly define the new `G` symbol, whereas its `g_(rs,i)` immediately above is a raw product and inherited `C_l` is centered. The displayed `G` identity is correct with the centered definition just given. It is false with a raw-moment reading: for a target coordinate of mean `1/2` and two noiseless routes, the same-time raw product is `1`, while `C_0 = 3/4`.

The raw version is instead

`R_l^(rs) = D_r (C_l + m m^T) D_s`.

Classification: **required notation supplement, absent from the frozen short source**, rather than a restatement of an already supplied definition. The following reference to recovering covariances and the inherited meaning of `C_l` support the centered interpretation, but I do not treat that contextual evidence as an already explicit or uniquely stipulated definition. This is not a new probabilistic hypothesis; it specifies which statistic the existing identity concerns.

The precise proposed insertion before that paragraph is: `定义跨路中心化协方差 G_l^(rs)=E[(X^(r)_(t+l)−mhat_r)(X^(s)_t−mhat_s)^T]，其中 mhat_r=E[X^(r)_t]；上文 g_(rs,i) 则仍为同位置同刻的原始乘积矩。` The raw-moment counterexample applies to the alternative raw reading only; it does not refute the centered statement proved in this review.

Disposition: **valid under this required explicit definition; not an unconditional pass of a completely defined frozen formulation**. An extraction or tool interface should carry the definition of `G`, not silently insert raw products. The present report supplies the proposed clarification; it does not edit or claim author revision of the frozen source. Adoption into an exact revised source/interface remains a separate attributable action. No new theorem or independent acceptance vote is created by this reviewer contribution.

## 4. Why simultaneous independence is insufficient

I checked the source's §8 construction directly. Let `N_t,M_t` be independent iid sign sequences with mean `1/2`, independent of an unbiased target sign process whose lag-one covariance is `α = 1/10`. Put

`E1_t=N_t`,  `E2_t=N_(t−1)`,  `E3_t=M_t`.

At each fixed time the three error variables are independent and all three same-time raw cross-route products equal `1/4`; the positive three-view calibration returns biases `1/2`. But the first and second whole error processes are not independent. Specifically,

`E[E2_(t+1)E1_t]=1`,  `E[E1_(t+1)E2_t]=1/4`.

The corresponding target-report cross-products are `1/10` and `1/40`. Dividing by the calibrated gain `1/4` gives incompatible target lag-one values `2/5` and `1/10`. Both are individually within the scalar model's admissible range, so a mere probability-domain test does not catch this leakage. This is a valid counterexample to replacing whole-process independence by fixed-time independence. I did not rerun its enumerated 128-history evidence.

As the source observes, a common multiplicative history `H_t` shared by all routes can instead be absorbed into an alternative target `S_t H_t`. Thus even extensive cross-route agreement is not an independent certification of the absence of common error. The observation equivalence alone does not prove that the alternative target has the same legal binary affine realization or the same coordinate count.

The approximate same-time calibration bound is algebraically correct: if `g_rs=η_rη_s(1+e_rs)` with `|e_rs|≤ε<1`, then

`etahat_1^2/η_1^2 = (1+e_12)(1+e_13)/(1+e_23)`

lies between `(1−ε)^2/(1+ε)` and `(1+ε)^2/(1−ε)`. The preceding counterexample already has zero same-time calibration error and nonzero cross-time leakage, so that bound cannot also control cross-time error.

## 5. Instrument modes are not extra target coordinates

For independent stationary scalar target/instrument processes with means `m_S,m_E`, variances `v_S,v_E`, and exponential covariance factors `α,β`, the product report has covariance

`Cov(X_(t+l),X_t) = m_S^2 v_E β^l + m_E^2 v_S α^l + v_S v_E (αβ)^l`.

At the §6 values this gives precisely `(9/100)(4/5)^l + (12/25)(1/2)^l + (27/100)(2/5)^l`. Distinct bases and nonzero positive weights give scalar Hankel rank three by the Vandermonde factorization. In contrast, independent-route centered cross-covariances have only the target factor, multiplied by the two gains, and therefore rank one. This verifies the stated conceptual boundary by direct algebra; it does not reproduce the recorded synthetic transition calculations. Applying the target-coordinate Hankel bound directly to the uncalibrated single-route sequence would not meet the theorem's observation model.

## Outcome and retained obligations

Within the stated external stationary binary model, exact population moments, positive biases, aligned nondisturbing readout, the joint whole-process independence condition, and the required centered definition of `G_l^(rs)` supplied above, I found no mathematical defect in the reviewed lower-bound/calibration/counterexample chain. The frozen short source has a missing necessary statistic definition, so the disposition is **VALID_WITH_REQUIRED_NOTATION_SUPPLEMENT**, not unconditional PASS. The exact insertion and the limited raw-moment counterexample are recorded above. This is a bounded conditional paper result, not a formal acceptance or independent certification of the source's reported computations.

Still open and unaffected: obtaining independent evidence for instrument-history independence and observation alignment; finite-sample convergence/confidence under arbitrary colored instruments; legal binary minimum realization and identification of genuinely returning hidden graphs; target disturbance; native/physical bridges; original activity-registration provenance; global formal Task inventory. Historical exact fractions and experiments retain their historical self-check status.

This review adds one distinct-author conditional paper examination of one exact source. It does not add a new research theorem, close the C34 research direction, change the monthly library's mathematical admission status by itself, or close the parent research objective.

Researcher-ID: EM-DIRECT-099801 / TASK_RESEARCH
