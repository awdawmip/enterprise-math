# C26 appendix: exact schedule criterion for returned controls under multiplicative drift

Status: AUTHOR_PROVED_UNREVIEWED / RESULT_ONLY_COMPOSE / CONDITIONAL_FINITE_MODEL
Author: Researcher-ID EM-P11-4A56E9 (prior contribution identity EM-T6-BFF294)
Date: 2026-10-17 UTC
Activity lineage: SID MCP-387e35a6a7d24e8cb2c44e361b9ce5b9; RA RA-C193E2AA39B9A6A6DDBB69B3; actual current checkpoint36 / 175 readbacks.
Author Source: PENDING. This first frozen local artifact is not a published or independently accepted theorem.
Family: the original C26 finite positive returned-control model. This is one structural COMPOSE appendix, not another paper, Tool, physical mechanism, or numerical experiment.

## 1. Exact input and the new obligation

The exact original input personally fetched and read in full, including its complete status and permission context, is:

- Repository: awdawmip/enterprise-math.
- Source: 617d4013a72cb3985be0dce93fb7e83b7cce28a8.
- Path: research_notes/divisor_extrema/20261017_c26_returned_controls_drift_identifiability.md.
- UTF8 bytes: 11047.
- SHA256: df8fbd48693890d63ea3cae5cd46d88f9ebf8ebbaf9fc79a5a71eb5f1ffee161.
- Git blob: 12e40af5ff8378e219812189bfaa3ad45a85ee02.
- Immutable URL: https://github.com/awdawmip/enterprise-math/blob/617d4013a72cb3985be0dce93fb7e83b7cce28a8/research_notes/divisor_extrema/20261017_c26_returned_controls_drift_identifiability.md.
- Own entire original caller: functions.store C26_returned_control_bounded_intake_one_exact_original_Source_caller.
- Local raw: /workspace/enterprise-math/research_notes/owner_goal_20261017/c26_returned_control_bounded_intake_4a56e9/C26_ONE_EXACT_ORIGINAL_SOURCE_CALLER_RAW.json.

C26 gives alternating consecutive designs, interpolation aliases for at most d+1 consecutive samples, and some non-equally-spaced contrasts. The obligation here is the complete criterion for an arbitrary fixed binary control schedule at distinct known integer positions, including both directions and normalized nuisance recovery. Its ingredients are standard finite linear algebra, positive finite products, polynomial interpolation, and a self-contained positive-operator comparison.

The source remains SELF_CHECKED_UNREVIEWED / CONDITIONAL_IDENTIFIABILITY_AND_OBSERVER_THEOREMS / NO_PHYSICAL_FIT, with NONE_ALLOCATED / REGISTRATION_PENDING and its original STATIC_READONLY_SCOPE_DENIED retained. Reading it under this author's own already-existing ordinary research authority does not register its author or revive a denied operation. No C22, C23, C24 or C25 whole, calculation package, literature result, numerical recovery count, or physical experiment is accepted by this appendix. Definitions are consumed as an explicit conditional finite model; every mathematical assertion used below is proved here.

## 2. Literal finite model and statement

Let Y be a finite nonempty set, fix y0 in Y, and fix d >= 0. A target K_A=K is a strictly positive real function on Y, normalized to uniform mean1. There is a known real linear map T with every matrix entry strictly positive. The second control is exactly K_B=T K, with the original control normalization. The admissible target family F consists of functions meeting these hypotheses and any original source-family constraints; T is the same known map for all candidates. We assume F is nonempty. A statement about identifying an original parameter lambda requires, separately, an injective map lambda -> K; no such upstream injectivity is silently assumed.

Choose L >= 1 distinct known nonnegative integers n_j, j=1,...,L, and a known binary label b_j: b_j=0 means A and b_j=1 means B. Positions are the original sample-position variable, not a physical clock, spatial coordinate, Native time, or a computation count. Unequal gaps are allowed and must be retained.

The nuisance family is exactly

 B_n(y) = Q(y) product_{k=1}^d D_k(y)^{binom(n,k)},
 P_j(y) = B_{n_j}(y) K(y)^{1-b_j} (T K)(y)^{b_j} / Z_j.       (1)

Here Z_j is the positive sum over Y; Q and every D_k are strictly positive; Q has one fixed scalar normalization (use sum_y Q(y)=1), and D_k(y0)=1. An alternative fixed scalar convention for Q gives the same theorem after its one normalization adjustment. There is no small-drift assumption or amplitude bound. Q,D are independent of the control label. Each observation is the complete positive distribution P_j, with all state labels and sample positions known.

Define the rational matrix and label vector

 V_{jk}=binom(n_j,k), k=0,...,d;     b=(b_1,...,b_L)^T.         (2)

The column k=0 is the all-ones vector. The exact assertions are:

(a) If b is not in col_Q(V), the distributions in (1) uniquely determine K and all normalized Q,D_k.

(b) If b is in col_Q(V), then for every two admissible K,K' in F, and every nuisance realization Q,D for K, there is a normalized strictly positive nuisance realization Q',D' for K' producing exactly the same distributions at all L positions.

Consequently, if F contains at least two distinct normalized targets, the given schedule universally identifies K if and only if b is not in col_Q(V). The nontrivial-family qualification is essential: a pre-fixed singleton target does not become unidentified by a poor schedule.

All conclusions are exact, conditional on (1) and the known strict positivity of T. They are not an assertion that arbitrary observed data belong to the declared target or nuisance model.

## 3. Integer contrast and positive target uniqueness

Suppose b is not in col_Q(V). Rational linear algebra gives a rational row annihilating V but not b. Clear its finitely many denominators: there exists w in Z^L such that

 sum_j w_j V_{jk}=0 for every k=0,...,d,
 s=sum_j w_j b_j is a nonzero integer.                         (3)

This is an existence argument over a finite rational matrix, not a numerical rank estimate or an executed algorithm. In particular sum_j w_j=0.

Form the positive finite comparison C(y)=product_j P_j(y)^{w_j}. Substitution of (1) cancels Q and every D_k. The Z_j contribute only a scalar independent of y. Writing r(y)=(T K)(y)/K(y) gives

 C(y)/C(y0) = [r(y)/r(y0)]^s.
 R(y) := [C(y)/C(y0)]^{1/s} = r(y)/r(y0).                       (4)

There is one positive real root; a negative s includes an ordinary reciprocal. All powers concern explicitly declared comparisons of strictly positive probabilities. Negative contrast exponents and rational roots are observations in this mathematical proof, not claims of native positive-BRC internal negative weights, a physical readout, or a newly executed root solver.

Let A_R=diag(1/R) T. It is entrywise strictly positive, and the actual target satisfies

 A_R K = r(y0) K.                                              (5)

The positive eigenvector proportion class is unique by the following complete argument. Suppose A_R K=lambda K and A_R K'=lambda' K', with K,K'>0. Both eigenvalues are positive. Put x_i=K'_i/K_i. For every i,

 (lambda'/lambda) x_i
   = sum_j [(A_R)_{ij} K_j / (lambda K_i)] x_j.

The bracketed coefficients are strictly positive and sum to1. If x is nonconstant, at an index where x_i=M=max x the right side is strictly smaller than M, so lambda'/lambda<1. At an index where x_i=m=min x it is strictly greater than m, so lambda'/lambda>1. This contradiction proves x constant. If Y is a singleton, constancy is immediate. The mean1 convention therefore fixes K uniquely.

Existence in this proof comes from the premise that the data are generated by (1). No general Perron-Frobenius theorem, convergence claim, computation, or unreviewed upstream result is required. In particular, a positive candidate is not thereby certified to satisfy the original source-family constraints.

## 4. Uniqueness and exact recovery of normalized background

Since b is not in col(V), L >= d+2: if L <= d+1, distinct-position evaluation makes V full row rank, as proved in section6. For L >= d+1 the columns of V are linearly independent, because a polynomial of degree at most d vanishing at at least d+1 distinct positions is zero. The binomial polynomials are a rational basis of that polynomial space.

With the just-recovered K and K_B known, define

 a_j(y) =
 [P_j(y)/K_{u_j}(y)] / [P_j(y0)/K_{u_j}(y0)]
 = [Q(y)/Q(y0)] product_{k=1}^d D_k(y)^{V_{jk}}.                (6)

Choose a rational left inverse W of V, so W V=I_{d+1}. It exists over Q since V is a full-column-rank rational matrix. Apply finite products of positive rational powers to (6). For row0 of W the product equals Q(y)/Q(y0); for row k>=1 it equals D_k(y). The specified scalar normalization of Q then fixes Q. These statements follow by multiplying exponents and WV=I, and are exact existence/uniqueness statements; they require no numerical logarithms, enumeration, or iterative program.

This pays all nuisance uniqueness in (a), including d=0. It does not certify the hypothesized drift order from the mere success of an identification calculation.

## 5. Complete alias construction inside the nuisance family

Suppose b=V alpha with alpha=(alpha_0,...,alpha_d) rational. Equivalently,

 q(n)=sum_{k=0}^d alpha_k binom(n,k),    q(n_j)=b_j.             (7)

Take any two admissible normalized targets K,K'. For their same known T, set

 r=(T K)/K,      r'=(T K')/K',
 A=K/K',        rho=r/r'.                                    (8)

Every function in (8) is strictly positive. Given the original Q,D, define

 Q'=normalize_y[Q A rho^{alpha_0}],
 D'_k(y)=D_k(y) [rho(y)/rho(y0)]^{alpha_k}, k=1,...,d.           (9)

These functions meet the original positivity and scalar conventions; in particular D'_k(y0)=1. Rational powers of strictly positive functions are permitted because the stated nuisance family allows arbitrary positive Q,D with no further amplitude, integrality or parametric restrictions.

If N is the positive scalar used to normalize Q A rho^{alpha_0}, direct multiplication gives at sample j

 B'_{n_j}(y) K'(y)^{1-b_j}(T K')(y)^{b_j}
  = N^{-1} rho(y0)^{-sum_{k=1}^d alpha_k V_{jk}}
      B_{n_j}(y) K(y)^{1-b_j}(T K)(y)^{b_j}.                   (10)

Indeed A K'=K, and rho^{q(n_j)} (r')^{b_j}=r^{b_j}. The factor in front of the last expression is independent of y, so probability normalization cancels it exactly. This proves (b) without leaving the original control-independent polynomial-drift family. It is not the separate control-synchronized nuisance enlargement L_u discussed in C26 section6.

A genuine nontrivial positive bridge is available, rather than an arbitrary invented target Q. C26 section4 explicitly uses Y={-1,+1}, K_w(y)=1+w y and a known c=1/16 control sending w to c w. The finite map, with both controls in the same normalization, is

 T = [[(1+c)/2, (1-c)/2],
      [(1-c)/2, (1+c)/2]],     T K_w = K_{c w}.                (11)

Every entry is positive. In the stated four-relation bridge the source coefficient is the product of its four positive factors. Values (1/2,1/2,1/2,1/2) and (1/4,1/2,1/2,1/2) give distinct w=1/16 and w'=1/32. Halving each factor gives the same c=1/16 in both cases. The elementary finite bridge coefficient can also be checked directly: for four signs z_i and y=product_i z_i, summing product_i(1+t_i z_i) over the eight sign assignments with that y leaves 8(1+(product_i t_i)y); all nonempty proper character terms sum to zero. Thus (11) and the two strictly positive finite target laws are actual instances of the declared positive bridge, not an arbitrary replacement target or a claim that the whole C22 graph inverse has been reviewed. Formula (9) gives their exact same-data aliases whenever (7) holds.

## 6. Sharp sample count and arbitrary unequal gaps

For any L <= d+1 distinct positions, every list of L rational values is interpolated by a rational polynomial of degree at most L-1. Its expansion in the binomial basis uses rational coefficients. Hence V is full row rank and every binary b is in col_Q(V). By section5 no such schedule identifies a nontrivial target family under the unrestricted nuisance hypotheses.

For L=d+2, put the positions in increasing order and use alternating labels 0,1,0,1,..., or their complement. If a degree-at-most-d polynomial q took those label values, q-1/2 would change sign in each of the d+1 successive open position intervals. The intermediate value property gives at least d+1 distinct roots, contradicting its degree bound; it is not the zero polynomial because its sample values are nonzero. Thus b is outside the real, and hence rational, column space. Sections3-4 identify the target and normalized nuisance.

Therefore d+2 is the sharp designed number of full-distribution observations, achieved by alternating controls at any distinct known nonnegative integer positions, not just equal spacing. The actual annihilator weights depend on those positions; substituting the equal-spacing binomial weights after dropping time gaps is invalid. For d=0 two distinct controls suffice and one observation aliases. For arbitrary longer schedules the same column-space criterion, rather than sample count alone, decides identification.

This extends the explicit schedule coverage of the consumed C26 note. It does not claim a new general interpolation or cancellation method, nor that the observation count is a statistical sample count.

## 7. Exact scope, parameter map and kill

The theorem identifies normalized K and nuisance in the declared finite model. If a separately proved original parameter map lambda -> K is injective on its stated domain, it also identifies that lambda; this last implication is ordinary composition. This appendix neither assumes nor proves the unconsumed full C22 inverse.

Known T with strictly positive entries, complete joint distributions, exact state labels and positions, constant targets on repeated control labels, and the original control-independent drift family are load-bearing hypotheses. There is no extension to unknown calibration, nonpositive or reducible T, partial or compressed histograms, noise, finite sample cost, memory effects, physical scale or a Native instrument. The root/ratio observations have not been asserted as a permitted native operation.

C26's control-synchronized unknown factors L_u remain a different, larger model: they can mask targets at every schedule. This result cannot validate their absence or any original physical interpretation. An inferred positive target must still be checked against an actually specified source-family membership condition before a source-model claim; no new admission conjecture is included here.

The unit closes with the standard same-family criterion and sharp designed count above. Tables of changed positions, drift parameters or alternate binary words alone would be reuses of this criterion and do not open another paper or a Tool. No claim about all literature or global repository novelty is made.

## 8. Authorship, exposure and complete acceptance context

The new arbitrary-schedule formulation, the full normalized alias construction, the exact iff proof and this integration were constructed by EM-P11-4A56E9 after the one bounded C26 whole intake. This author has NONZERO actual construction history. Root supplied routing, scope and publication control, and supplied zero mathematical proof or repair. No A/BFF/CF new working, candidate formula or repair was requested or consumed in making this proof. Their other family work is not a premise.

The C26 original author's finite model, returned-control contrasts, consecutive-sample sufficiency and interpolation ideas retain their original contribution. This appendix is a consumer of that literal setup and a standard COMPOSE result, not a vote accepting the source's upstream graph, code, computation claims, literature coverage, registration state or physical mechanism. This author personally read only the exact C26 original as the new input for this unit. Earlier C27/C28 and positive-bridge knowledge is warm context; the finite bridge equations actually needed here are displayed and checked in section5, not borrowed as a hidden whole or numerical certificate.

The author's same actor/SID/RA36 lineage, all original STOPs, UNKNOWN formal budgets, warm contributions and false formal authority flags remain in force. No program, solver, query budget, Native operation, session allocation, checkpoint37, activity append or remote mutation is performed by writing this local mathematical appendix.

Independent technical whole review is pending. A later reviewer must disclose actual NONBLIND/private-candidate and participation history and personally consume this complete artifact and necessary inputs; a prior different-scope vote cannot be migrated. This local first artifact, its eventual author Source, a future reviewer artifact and future ordinary acceptance are distinct events. No future Source SHA, review verdict, remote readback, or activity ordinal is invented here.

Self-read convention: this artifact will be completely read back after the file is actually written, checked as one complete proof and context, and pinned from those actual bytes. A later immutable Source read of identical bytes may honestly reuse that semantic whole. This sentence is a prospective convention at creation, not an assertion of a completed readback.

