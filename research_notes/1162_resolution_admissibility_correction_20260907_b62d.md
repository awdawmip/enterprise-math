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

This concerns admissibility and stability of microscopic differential observations in the project's discrete/rough substrate. It is not an instruction to alter the protected worldview, discard correct conditional classical mathematics, or declare all derivatives globally forbidden.

The previous note `research_notes/1162_chi29_cm_not_lcm_20260907.md` remains a classical analytic result for its explicitly selected function h29 and ordinary probability convolution. Its order-39 sign certificate is not, without an additional bridge, a certificate about native discrete refinement or BRC serial composition. In particular the exclusion of identical m-fold probability-convolution roots for m>=60 must not be relabeled as a prohibition of m-way native refinement.

The original note already distinguished holonomy-sector refinement from identical convolution roots; preserve that distinction. This correction changes research priority: establish finite-resolution admissibility before pursuing another analytic root-classification question as though it settled the native problem.

The old derivative is with respect to the analytic readout parameter z, not automatically a microscopic spatial coordinate. A finite discrete structure can have an exactly defined smooth external generating parameter. Discreteness alone therefore does not invalidate an analytic derivative. What is missing is an explicit theorem identifying the allowed native observation, its relation to this derivative, its choice-independence and its stability at the permitted precision.

No rerun or new independent verification of the chi29 order-39 certificate is claimed here.

## 2. Observer factorization obligation

Let Q record the retained discrete observations. Before treating an analytic quantity D as a property of that observation class, require exact factorization D=Dbar composed with Q, or a proved quantitative variation bound on each admissible Q-fiber strong enough to preserve the asserted sign.

If X and Y are indistinguishable at the declared resolution but D(X) and D(Y) have opposite signs, that sign is not an observation-class invariant. Accurate evaluation on one representative does not repair this defect.

Keep three errors distinct: arithmetic rounding; interpolation/completion choice; discrepancy between the declared native model and analytic readout. The old rational interval certificate addresses the first for its chosen expression, not automatically the other two.

## 3. Explicit sample-fiber counterexample

This is conditional on an observer retaining only equally spaced values. It does NOT assert that arbitrary interpolants satisfy every Enterprise Math relation.

Take positive analytic h, grid z_j=z0+j*delta with delta>0, and integer M>=1. Define

h_(eta,M)(z)=h(z) exp(eta sin(2*pi*M*(z-z0)/delta)).

Then h_(eta,M)(z_j)=h(z_j) at every grid point, h_(eta,M)>0, and the real-axis log discrepancy is at most |eta|. Nevertheless

(d^39/dz^39 log h_(eta,M))(z0)
=(d^39/dz^39 log h)(z0)-eta*(2*pi*M/delta)^39.

Increasing M allows arbitrary derivative changes with arbitrarily small fixed log-amplitude while preserving all grid values. If normalization at zero is also required, take a grid containing zero and the center, or impose that extra interpolation constraint separately.

The conclusion is non-identifiability from these samples alone, not failure of the exact h29 definition. Additional exact structural constraints may rule out the perturbations; that is precisely an extra bridge to prove.

## 4. Finite differences with declared precision

For a permitted step delta>0 set

B_(k,delta)[f](z)=sum_(j=0)^k (-1)^j binom(k,j) f(z+j*delta)
                =(-1)^k Delta_delta^k f(z).

If |f_j-fhat_j|<=epsilon_j, the triangle inequality yields

|B[f]-B[fhat]|<=sum_(j=0)^k binom(k,j) epsilon_j=:E_k.

Uniform error epsilon gives E_k=2^k epsilon. A normalized difference delta^(-k)B has bound 2^k epsilon/delta^k. This is sharp for independent box uncertainties, by choosing alternating errors. Structured/correlated native uncertainties may admit tighter bounds and must not be silently replaced by a box model.

A robust negative certificate requires B[fhat]+E_k<0. An enclosure meeting zero is inconclusive. At k=39 the coefficient amplification is exactly 549755813888. Sample errors must include native-to-readout uncertainty, not merely computation rounding.

For log h or h^r, propagate positive input intervals through the nonlinear operation first. The resulting errors are not automatically the errors of h. Every stencil must fit the allowed domain and observation horizon. A finite list of passing differences does not establish all-order complete monotonicity.

For a fixed smooth interpolant, a negative derivative does imply a negative sufficiently small-step difference by continuity and repeated integration. This becomes a native witness only when the required step and k+1 samples are admissible and its negative margin survives model/readout errors. No such project-specific step or error envelope was established for the chi29 witness.

## 5. Replace differentiation of integer layer N by actual refinement

The earlier formal generator A_m=2m+N*d/dN is not a native derivative on an arbitrary sequence indexed by integer N. Retain it only as optional notation on an explicitly chosen smooth interpolation.

For a fixed positive integer m and integer q>=2 define directly on sequences

(E_q^(m) f)(N)=q^(2m) f(qN).

These finite operations obey E_p^(m) E_q^(m)=E_(pq)^(m), and

E_q^(m)[N^(-2r)]=q^(2m-2r) N^(-2r).

Thus the scale eigenvalues used in finite-polynomial correction arguments survive without differentiation in N. On a sequence proven to have the form f(N)=sum_(r=0)^m a_r N^(-2r), the exact polynomial

P_(m,q)(y)=prod_(r=0)^(m-1) (y-q^(2r))/(q^(2m)-q^(2r))

satisfies P_(m,q)(E_q^(m)) f=a_0. This uses finitely many refinements and the proved polynomial correction structure. It does not assert that arbitrary rough sequences have such a structure.

For the existing cycle Basel model, put L_N=2I-R_N-R_N^* for N>=3 and

b_N=(2/N^2) Tr L_N^+=(N^2-1)/(6N^2).

The finite recurrence b_(2N)=b_N/4+1/8 is rational and derivative-free. The angular normalization B_N=pi^2 b_N and its relation to the classical Basel limit remain separately typed compatibility statements; no native pi or Euclidean metric is thereby manufactured.

## 6. A derivative-free finite resolvent law

Let A be a declared finite self-adjoint positive-semidefinite operator with retained eigenvalues lambda_l>=0. For u>0 define R_A(u)=sum_l 1/(lambda_l+u). For every permitted delta>0 and integer k>=0,

B_(k,delta)[R_A](u)
=k! delta^k sum_l 1/prod_(j=0)^k(lambda_l+u+j*delta)>0

when the retained spectrum is nonempty.

Proof: set F_k(x)=k! delta^k/prod_(j=0)^k(x+j*delta) for x>0. The k=0 case is immediate, and

F_k(x)-F_k(x+delta)
=(k+1)! delta^(k+1)/prod_(j=0)^(k+1)(x+j*delta).

Induction proves the scalar identity and summation proves the spectral formula. No delta->0 limit or classical derivative is used.

This is exact conditional finite-matrix mathematics. For the integer cycle L_N and rational u,delta, resolvents can be evaluated by rational matrix algebra without trigonometric diagonalization. Native admissibility of the selected operator/probe still requires its own declaration. This theorem does not decide powers of the different function h29.

Local exact sanity checks used Python Fraction arithmetic for eigenvalues (0,1/3,2,11/7), probes (1/5,1,9/4), steps (1/10,1/2,2), and k=0,...,7: 288 scalar identities, all exact. The finite check supplements the induction proof.

## 7. BRC reuse and semantic authority

REUSE_APPLIED: BRC observer/future-operation fiber constancy, from `knowledge/procedures/BRC_RESEARCH_PRIORITY_AND_USAGE_20260905.md`, blob d9271e084d318b807398583e564b235c6715b03f. Carrier: labeled allowed samples and certified uncertainty, or a declared finite operator. Future operations: allowed finite stencils, positive algebraic compositions and explicit integer refinement. Below-resolution differentiation is not silently added to this language.

NOT_APPLICABLE: finite positive-rational recurrent/port-collapse theorems as automatic certificates for signed infinite character kernels, arbitrary smooth completions or microscopic derivatives.

Project policy sources:
- `native_semantics_admissibility.json`, blob 58ad0af8c2e3df56b353575bf0004095507bffbf, especially NSA-02, NSA-04, NSA-11 and NSA-13.
- `GEOMETRIC_TOOL_REFOUNDATION_POLICY.md`, blob 57d87c9dda9bfbe5356492d11372d03490e2eb0f: REFOUND_NOT_REJECT.

The chi29 theorem is classified here as CONTINUUM_ANALYTIC_READOUT. Transfer to native rough refinement is UNESTABLISHED. This is an applicability restriction, not a mathematical refutation and not evidence that the excluded classical convolution roots exist.

## 8. Next exact frontier

Return #1162 to finite rotation matrices and integer holonomy-sector refinement. Declare the exact rough observation relation, permitted finite increments, stencil order/window and native-to-readout error envelope. Seek a finite robust sign or composition certificate factoring through that observation. Increasing arithmetic precision or derivative order does not substitute for this bridge. Preserve existing analytic proofs as compatibility results rather than restarting them.

External reference used only to check differentiated-interpolation hypotheses and derivative remainders: NIST DLMF sections 3.3 and 3.4. No novelty investigation or historical-priority claim was made.
