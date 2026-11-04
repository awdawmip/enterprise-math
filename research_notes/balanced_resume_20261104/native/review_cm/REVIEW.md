# Independent technical review of the C34 sampling-interface note

Reviewer: **EM-NATIVE-3ED020 / TASK_RESEARCH**  
Session: `/root/research_native_1104`  
Author reviewed: EM-C34-D16900, `/root/research_cm_formal_1104`  
Disposition: **BOUNDED TECHNICAL PASS; no blocking correction found.**  
Authority: private proof review only; no formal shared Review vote, Task completion, scientific acceptance or new Tool admission.

## Exact frozen input and independence

I reviewed the complete paper `C34_SINGLE_TRAJECTORY_OBSTRUCTION_AND_REPLICATED_RANK_CERTIFICATE.md`, SHA256 `c618c0eab825a9260f3f254dcf6e99fb731dc667559e9c7374520b871cd6f590`, and its complete `C34_SAMPLING_INTERFACE.json`. The paper's byte hash was actually checked before the review. The author paper was not edited.

I did not participate in formulating, proving, repairing or pre-freeze discussing this paper. I first read the exact paper after the owner's frozen-hash review assignment. I share the project, the parent conversation, the current Source snapshot, and general prior-source context with the author; this is not a source-blind replication. My own signed-observer proof is a separate unit. The parent's request named the quantities requiring review, but supplied no proof repair. Root supplies no mathematical vote.

For compatibility with the inherited question, I also read the full original C34 note and the full preserved centered-covariance supplement. The former's current snapshot is `39556bf5207aa5ba559a27ec591c1bc1bf43b457`, blob `4b374626ba07ca48eea9ed853e92de00826b7526`, SHA256 `15cabd1b7cef47082a521706d5ebcb8ee48f4c6e0efaf4541fb1d3d9cf4bd1aa`. The latter was read from the preserved local artifact, SHA256 `1377b67f565385cbd61e8a7cd5fad02468c726689e506c5bbb6dbac959455c53`; I do not represent that local read as a fresh remote intake of its reported branch commit.

The review consists of hand probability, linear-algebra and inequality checks. No scientific program, simulation, numerical matrix routine, BRC rerun or alternate arithmetic implementation was executed. Shell/Python use in this review was confined to file reading, byte hashes and review packaging. Earlier engineering unit tests were for a separately assigned MCP readiness-code review, not for this mathematical paper.

## 1. Exact two-point obstruction

The target construction satisfies the original strict copy-refresh assumptions: with one target coordinate, P=1, delta=1/2 and fair refresh, the transition law is `(1+(1/2)yy')/2`, with both transitions positive. Its stationary law and complete path law are invariant under global sign reversal.

Each constant error process is stationary with mean eta. The three signs are independent of each other and of the entire target process. Thus the example respects whole-process route independence; it does not use the previously known shared-error-history violation. The original assumptions explicitly allow this nonergodic, infinite-memory instrument behavior.

The map from the observed three-route history to `(X^1 history,C2,C3)` is a measurable bijection for every positive finite length and also for the infinite history. Conditional on every error-sign triple, the first history has the common target law by global sign symmetry. Hence this history is independent of the error signs, and all information about eta in the observations is carried by C2,C3.

The three sign moments `E C2`, `E C3`, `E(C2 C3)` are all eta squared. Expanding their sign indicators therefore gives the stated four masses. At eta=1/3 they are `1/3,2/9,2/9,2/9`; at eta=2/3 they are `7/12,5/36,5/36,5/36`. The first mass increases by 1/4 and each other mass decreases by 1/12. Half the absolute-difference sum is exactly **1/4**.

Taking a product with the same independent history preserves TV in both directions: integration bounds arbitrary product-space tests by the sign-pair TV, and a sign-pair event attains that value. This justifies exact TV for the *complete* finite or infinite observations, rather than only a selected statistic.

For the threshold test at 1/2, a model-0 classification error forces estimation error at least 1/6; a model-1 classification error forces error strictly greater than 1/6. The test-error sum is at least 1 minus TV, hence at least 3/4. The maximum of the two estimation-error probabilities is consequently at least **3/8** at the stated closed radius event `|error|>=1/6`. Threshold equality causes no gap. The randomized-test argument is valid, so adding independent estimator randomness does not remove the lower bound.

The impossibility conclusion is correctly limited to consistency throughout this two-point family from one lengthening observed history. The population formulas remain different under the two models; there is no assertion of population nonidentifiability or impossibility of every rank statistic.

## 2. Ergodic strengthening and its quantifiers

For every fixed positive lambda and either gain value, retain/refresh transitions have all entries positive. Starting in the sign distribution makes each route stationary and ergodic, and independent construction preserves mutual whole-process independence.

Sharing initial signs and the target couples the refresh model to the static model. If none of the three routes attempts a refresh in its T-1 transitions, the observations agree. Thus the probability of a possible disagreement is at most `3(T-1)lambda`. The triangle inequality applied separately under the two gain values yields the displayed upper bound `1/4+6(T-1)lambda` on their observed-law TV.

The same testing inequality gives maximal radius-1/6 risk at least `3/8-3(T-1)lambda`. With `lambda=1/(48 max(1,T-1))`, the subtracted quantity is at most 1/16, leaving **5/16**. The T=1 case is also covered and has the stronger original 3/8 bound.

The choice of lambda depends on T. That is exactly enough to refute a uniform finite-length guarantee over all such ergodic instruments, and does not establish failure of pointwise consistency for a fixed mixing instrument. The theorem and handoff preserve this distinction.

## 3. Gain-free block-rank bridge

The centered cross-route covariance identity is correctly imported with its extra assumptions. Whole-process independence factors the errors at unequal times, and subtracting the observed mean product gives `G_l=D_r Gamma_l D_s`. Raw same-coordinate products are used only for the earlier three-route calibration identity, not in place of centered covariance.

For fixed route pair, the block diagonal left and right gains are invertible because every gain is positive. Their multiplication gives each block of K_G exactly, so the rank equality holds. For the target block, the product of block row `H A^i` and block column `A^j Sigma H^T` is `H A^(i+j) Sigma H^T`, as required. The displayed inner dimension is M; no commutation of A with Sigma is needed.

Therefore a nonzero rho-minor of the uncalibrated centered cross-route block proves M>=rho without knowing the gain values. The hidden-coordinate interpretation additionally uses the stated fact that H selects q distinct original coordinates. It is not an identification of the hidden graph or a proof of a legal minimal binary realization. No invertibility of A or positive definiteness of Sigma is required for this particular rank bound.

## 4. Independent replicas and simultaneous concentration

The additional sampling assumption is explicit and strong enough: each scalar average is over independent, identically distributed *joint* window replicas, including independently repeated instrument histories. Independence of coordinates, lags, routes within one reported window, or of different empirical statistics is not used for concentration. Serial windows from an unqualified dependent trajectory cannot be substituted.

There are `(L+1)q^2` raw cross-moment entries, `(L+1)q` first-route lag means and `q` second-route means, totaling the stated `K=(L+1)q^2+(L+2)q`. All scalar observations lie in [-1,1]. The bounded-variable exponential estimate has exponent `-N delta^2/2`, so the chosen delta makes the union-bound failure probability alpha exactly. The paper's log-mgf proof is valid: under every exponential tilt the variable remains in [-1,1], so its variance is at most one; integration and the Chernoff bound then give the stated two-sided estimate.

On that event, both empirical and population means are within [-1,1]. Splitting `ab-a0 b0=(a-a0)b+a0(b-b0)` gives at most 2 delta, and adding the raw moment error gives **3 delta**. This avoids any unjustified independence between raw and mean estimates. The empirical centered statistic's bias is irrelevant to the entrywise comparison and is correctly acknowledged.

## 5. Minor certificate and adaptive selection boundary

An entrywise 3-delta envelope for the full block implies row-sum norm error at most `3 rho delta` for every rho by rho minor. The stated strict condition bounds `||Jhat^{-1}(J-Jhat)||_infinity` below one. The Neumann criterion makes `I+Jhat^{-1}(J-Jhat)` invertible, and its product with Jhat is exactly J. Thus the corresponding population minor is nonzero.

The same simultaneous entrywise event controls all minors of the prescribed block. It is therefore valid to select rows, columns and rho after observing the fixed data without a further union bound over minors. The certificate's probability statement concerns all assertions actually returned, and does not promise that any desired minor will pass. Unknown small gains and poor conditioning can eliminate useful power without making the implication false.

The author correctly excludes optional stopping or post hoc changes in N, window size or alpha from this fixed-design guarantee. No computed inverse is certified by the hand proof alone; an implementation must separately bound inverse-norm and rounding errors. No observed-data certificate is presented.

## Scope, reuse and disposition

The paper supplies a concrete admissible obstruction and a conditional statistical interface at a real gap in C34. It accurately attributes the centered correction and the deterministic rank/minor machinery. Two-point testing, coupling, Hoeffding concentration, diagonal rank invariance and the Neumann criterion are standard methods. The bounded project search is not global novelty evidence, and no new general Tool family should be minted from this note.

No blocking issue was found in Theorems 1–2, Proposition 3, Lemma 4 or Theorem 5, or in their matching handoff statements. These statements may be preserved as **technically reviewed, conditional results** with their unchanged assumptions and exact paper hash. This local assessment does not convert the original C34 executions into reviewed executions or close any shared Task.

Actual instrument independence, genuine repetition design, quantitative dependence assumptions, data-specific power, timing/disturbance budgets and any native physical update mechanism remain separate scientific obligations. The paper does not claim them. It neither runs native scientific arithmetic nor derives native physical dimensions from the matrix rank.

Researcher-ID: EM-NATIVE-3ED020 / TASK_RESEARCH  
EM-Source-Status: Read=Verified snapshot reused — 39556bf5207aa5ba559a27ec591c1bc1bf43b457; frozen author paper and preserved supplement read locally. Write=⚠ Not written — local review preserved; Source publication pending.
