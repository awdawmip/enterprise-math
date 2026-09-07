# #1162 — resolution admissibility correction and derivative-free finite tests

Status: RESEARCH_NOTE / USER_SCOPE_CORRECTION_PLUS_ELEMENTARY_DERIVATIONS / NOT_PROMOTED
Researcher-ID: EM-DIRECT-B62D
Research-Mode: TASK_RESEARCH
Progress-Event-ID: 1162-resolution-admissibility-correction-20260907-b62d
At: 2026-09-07T20:48:01+08:00
Source project snapshot: 7335db562542ffdd43c7f4ba27538d66de53cd3c
Source global snapshot: f2fb6932d608e234bb1dd11fc856d2533b28f806

## 1. Direct user correction and scope

User: “不太对，在我们的离散理论里，细微处求导本身就会因为粗糙关系失去稳定性。”

This correction concerns the admissibility and stability of microscopic differential observations in the project's discrete/rough substrate. It is not an instruction to alter the protected worldview, to discard correct conditional classical mathematics, or to declare all derivatives globally forbidden.

The previous note `research_notes/1162_chi29_cm_not_lcm_20260907.md` remains a classical analytic result for its explicitly selected function h29 and ordinary probability convolution. Its order-39 sign certificate is not, without an additional bridge, a certificate about native discrete refinement or BRC serial composition. In particular the bound excluding identical m-fold probability-convolution roots for m>=60 must not be relabeled as a prohibition of m-way native refinement.

The original note already distinguished holonomy-sector refinement from identical convolution roots. Preserve that distinction. The present correction changes the research priority: establish finite-resolution admissibility before pursuing another analytic root-classification question as though it settled the native discrete problem.

Differentiation there is with respect to the analytic readout parameter z, not automatically a microscopic spatial coordinate. A finite discrete structure can have an exactly defined smooth external generating parameter. Discreteness alone therefore does not invalidate an analytic derivative. What is missing is an explicit theorem identifying the allowed native observation, its relation to this derivative, its choice-independence and its stability at the permitted precision.

No rerun or new independent verification of the chi29 order-39 certificate is claimed in this correction.

## 2. Observer factorization obligation

Let Q record the retained discrete observations. Before treating an analytic quantity D as a property of that observation class, require either exact factorization D = Dbar composed with Q, or a proved quantitative variation bound on each admissible Q-fiber strong enough to preserve the asserted sign.

If X and Y are indistinguishable at the declared resolution but D(X) and D(Y) have opposite signs, that sign is not an observation-class invariant. A very accurate evaluation of D on one chosen representative does not repair this defect.

Three errors must remain distinct: arithmetic rounding; interpolation/completion choice; discrepancy between the declared native model and the analytic readout. The old rational interval certificate addresses the first for its chosen exact expression, not automatically the other two.

## 3. Explicit sample-fiber counterexample

This is a conditional example for the observer that retains only equally spaced values; it is NOT a claim that arbitrary interpolants satisfy every Enterprise Math relation.

Take a positive analytic function h near a sampled interval, grid z_j=z0+j*delta, delta>0, and an integer M>=1. Set

h_(eta,M)(z) = h(z) exp(eta sin(2*pi*M*(z-z0)/delta)).

Then h_(eta,M)(z_j)=h(z_j) for every integer j in the grid, and h_(eta,M)>0. Also the log discrepancy is bounded by |eta| on the real axis. Nevertheless

(d^39/dz^39 log h_(eta,M))(z0)
= (d^39/dz^39 log h)(z0) - eta*(2*pi*M/delta)^39.

Thus the grid samples alone do not determine even the sign of this derivative; increasing M allows arbitrarily large derivative changes with arbitrarily small fixed log-amplitude. If a normalized value at zero must also be preserved, choose a grid containing zero and the center; alternatively impose that additional interpolation constraint separately.

This example establishes the need for an admissibility/definability bridge. It does not prove that the actual project carrier admits these oscillatory perturbations, nor that the fixed exact h29 is ill-defined.

## 4. Finite differences with declared precision

For a permitted step delta>0 define the unnormalized alternating difference

B_(k,delta)[f](z) = sum_(j=0)^k (-1)^j binom(k,j) f(z+j*delta)
                  = (-1)^k Delta_delta^k f(z).

If the retained samples f_j have certified total errors |f_j - fhat_j|<=epsilon_j, the triangle inequality gives

|B[f]-B[fhat]| <= sum_(j=0)^k binom(k,j) epsilon_j = E_k.

With a uniform sample error epsilon this is E_k=2^k epsilon. For a normalized difference delta^(-k)B the bound is 2^k epsilon/delta^k. The bound is sharp for independent box uncertainties because alternating choices of the errors attain it. Structured/correlated native uncertainty may permit a sharper bound and should not be replaced by an independent-box assumption without justification.

A robust negative witness requires B[fhat]+E_k<0. If the enclosure meets zero, this test is inconclusive, not a proof of either sign. At k=39 the coefficient amplification is exactly 549755813888. These epsilon_j must include native-to-readout uncertainty, not just floating or interval rounding.

For log h or h^r, propagate the original positive sample intervals through log or the power first; their errors are not automatically those of h. Every stencil must fit the allowed domain and observation horizon. A finite list of passing differences does not establish all-order complete monotonicity.

A negative derivative of the fixed smooth interpolant does imply a negative sufficiently small-step finite difference by continuity and repeated integration, but this yields a native witness only if that step and the required k+1 samples are admissible and the negative margin survives the model/readout errors. No such project-specific step or error envelope was established for the chi29 witness.

## 5. A derivative-free finite resolvent law

Fix a declared finite self-adjoint positive-semidefinite operator A with retained eigenvalues lambda_l>=0, and let u>0 and delta>0 be allowed probe values. Define

R_A(u)=sum_l 1/(lambda_l+u).

Then for every integer k>=0,

B_(k,delta)[R_A](u)
= k! delta^k sum_l 1/prod_(j=0)^k (lambda_l+u+j*delta) > 0

when the retained spectrum is nonempty.

Proof: for a scalar x>0, the k=0 identity is immediate. If F_k(x)=k! delta^k/prod_(j=0)^k(x+j*delta), then

F_k(x)-F_k(x+delta)
= (k+1)! delta^(k+1)/prod_(j=0)^(k+1)(x+j*delta).

Induction proves the scalar identity and summation proves the finite spectral formula. No delta->0 limit or classical derivative is used.

This law is exact conditional finite-matrix mathematics. Native admissibility of A and the probe parameter remains a separate obligation; the identity must not itself be promoted into an unproved native metric or continuum definition. It also does not decide the powers of h29, which is a different function.

Local exact sanity checks used Python Fraction arithmetic for 4 eigenvalues (0,1/3,2,11/7), 3 probes (1/5,1,9/4), 3 steps (1/10,1/2,2), and k=0,...,7: 288 scalar identities, all exact. This finite check supplements rather than replaces the induction proof.

## 6. BRC and project semantics

REUSE_APPLIED: the BRC observer/future-operation fiber-constancy requirement from `knowledge/procedures/BRC_RESEARCH_PRIORITY_AND_USAGE_20260905.md`, blob d9271e084d318b807398583e564b235c6715b03f. Retained carrier: labeled allowed sample values and certified uncertainty, or a declared finite operator and exact resolvent. Future operations: the declared finite stencil, positive algebraic composition and explicitly specified refinement. Derivatives below the declared observation scale are not silently added to that language.

NOT_APPLICABLE: positive finite-rational recurrent/port-collapse theorems as automatic certificates for signed infinite character kernels, arbitrary smooth completions or microscopic derivatives.

Source policy: `native_semantics_admissibility.json`, blob 58ad0af8c2e3df56b353575bf0004095507bffbf, especially NSA-02, NSA-04, NSA-11 and NSA-13; `GEOMETRIC_TOOL_REFOUNDATION_POLICY.md`, blob 57d87c9dda9a21dd? No: verified blob is 57d87c9dda9bfbe5356492d11372d03490e2eb0f. Its rule is REFOUND_NOT_REJECT.

Classify the original analytic chi29 theorem as CONTINUUM_ANALYTIC_READOUT. Its transfer to native rough refinement is UNESTABLISHED. This is a restriction of applicability, not a mathematical refutation of the fixed analytic theorem and not evidence that its forbidden classical convolution roots exist.

## 7. Next exact frontier

Return #1162 to finite rotation matrices and integer holonomy-sector refinement. Declare the exact rough observation relation, allowed finite parameter increments, stencil order/window and native-to-readout error envelope. Then seek a finite robust sign or composition certificate that factors through that observation. Do not substitute finer arithmetic or increasing derivative order for this missing bridge. Preserve the existing analytic proofs as optional compatibility results.

External reference used only for the distinction between differentiated interpolation and a controlled derivative remainder: NIST DLMF sections 3.3 and 3.4. No novelty investigation or new historical-priority claim was made.
