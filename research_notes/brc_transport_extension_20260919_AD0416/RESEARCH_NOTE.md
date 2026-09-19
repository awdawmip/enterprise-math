# BRC 作用—残差扩展：让失配参与运算，而不是只被记录

Researcher-ID: `EM-DIRECT-AD0416`
Research-Activity-ID: `RA-37C0A30C7B1F5A338F03D186`
Progress-Event-ID: `brc-transport-extension-20260919-AD0416`
Session: `chat-local-reciprocal-ceec8bd1559acdf8c10ebc9b` (continuing local key, not platform-authenticated).
Status: `RESEARCH_EXTENSION_PROTOTYPE / PROVED_SCOPED_IDENTITIES / EXACT_FINITE_CHECKS / NOT_PROMOTED`.
No Task-ID, CLAIM, independent review, Working Truth, Foundation promotion or production/runtime change.
User direction: “对的，结合brc的理念，扩展brc的能力。”
Read pins: GLOBAL_KNOWLEDGE `af67de93c661143349855d0af555327bcfb4da67`; EM `d20fbca83ae79b354a9ce2b0659477065a83993b`.

## 1. Extension decision and reuse boundary

Extend the existing T0 BRC family by composing it with T5 precision, T6 predictive quotient and T9 defect transport; do not introduce a competing top-level family. Current BRC already supports typed provenance and exact positive-weight histograms. The new work is a runnable joint weight/action adapter, a covariant matrix-defect specialization, and a proved affine-moment contraction interface. This is not a claim that BRC previously could not represent history, or that monoid algebras, cocycles, moment propagation or automaton minimization are newly invented mathematics.

Exact sources consumed at the EM pin:
- `tool_invocation_policy.json`, `enterprise_toolbox_registry.json` (T0/T4/T5/T6/T7/T8/T9), `research_method_inventory.json`.
- `definitions/ENTERPRISE_BRC_WEIGHTED_GLOBAL_SUBSTRATE_20260902.json`.
- `src/enterprise_math/brc_histogram.py` Git blob `9a3962ec095095f14e63a91cfe6b7ebf07d9a1d1`: REUSE_EXECUTED. The complete unchanged file was imported; byte identity verified. Its prime-valuation dependency uses the unchanged three required source functions extracted from `brc_rational_holonomy.py`, not the entire holonomy module.
- `src/enterprise_math/predictive_quotient.py` Git blob `f27d9ddf908f5b07051acfaf0c69f359d499b98b`: REUSE_EXECUTED unchanged; no second minimizer was invented.
- `src/enterprise_math/precision_holonomy.py`: REUSE_APPLIED. Exact base-sensitive transport is Delta_b(x,d)=floor((x+d)/b)-floor(x/b), not d/b or a free-floating defect magnitude. Matrix transport is a new specialization, not replacement of that integer law.
- T5: COMPOSE_APPLIED via exact mixed-radix quotient/remainder recomposition. T4: REUSE_APPLIED to the declared observer fibers. T7/T8: boundaries retained; no automatic physical symmetry or relation-safety inference.
- Previous `research_notes/NUMBER_FIELD_DEFECT_SYNTHESIS_20260919_AD0416.md` and the supplied exact 5/7/checker artifacts: consumed as the previous frontier, not rediscovered.

External comparison only: P. Bhaduri, *Coalgebras for Bisimulation of Weighted Automata over Semirings*, arXiv:2109.00732v4 / LMCS 19(1), 2023. Its abstract distinguishes weighted language equivalence and weighted bisimulation and states general termination limitations. Our finite deterministic T6 reuse is not a general weighted-language minimization algorithm.

## 2. Joint branch state and actual serial law

For fixed dimension d, let Aff_Q(d) be the monoid of total rational affine actions x -> A x+b; singular A is allowed except in inverse/defect comparisons. Use the finite positive-weight action histogram

H = sum_(w,A,b) c_(w,A,b) [w,A,b],  w>0 rational, c nonnegative integer.

Alternative composition adds multiplicities. Serial composition, first left then right, is

[w,A,b] star [v,B,c] = [wv, BA, B b+c].

Extend bilinearly to finite histograms. The identity is [1,I,0]; the empty histogram is zero. Associativity follows by substitution: both three-step associations yield (CBA, CBb+Cc+e) and weight wvu. Distributivity is finite expansion. Forgetting actions sends [w,A,b] to [w] and is a homomorphism to the existing WeightHistogram sum/serial operations. The existing BRC weight/valuation interfaces therefore remain valid projections.

Important: the translation residual in this law is typed affine data. It is not automatically the positive branch weight, covariance, integer remainder, common depth, or a universal scalar error. These quantities retain separate interfaces. Conditional branch weights, partial actions and incompatible ports require state-indexed kernels/typed composition, not this unconditional Cartesian serial product.

This histogram retains multiplicity and joint weight/action association but quotients labeled paths that have exactly the same pair. Full path names and hidden-history-sensitive queries must stay in the richer labeled BRC carrier. No reconstruction of erased provenance is claimed.

Necessity of the joint association: the packets {(weight1,shift+1),(weight2,shift-1)} and {(weight2,shift+1),(weight1,shift-1)} have the same weight histogram and the same unweighted action multiset. At input0 their weighted means are -1/3 and +1/3. Separate marginal summaries cannot supply the missing correlation.

## 3. Exact order defects and their coherence

Reuse the earlier hex-lattice comparison matrices

A5 = [[1,-1],[2,3]],  det=5;
A7 = [[1,-2],[2,3]], det=7.

First5 then7 gives A7*A5=[[-3,-7],[8,7]]. First7 then5 gives A5*A7=[[-1,-5],[8,5]]. Both encode determinant35 but are different transports. The relative comparison is

H = (A7*A5)*(A5*A7)^(-1) = (1/35)*[[41,-8],[-16,33]],
det(H)=1, trace(H)=74/35, H!=I.

Thus common scalar number/area readout does not determine the transport. This H is a rational map between declared comparison readouts, not permission to apply fractional inverse moves to arbitrary integer Cells. These 2D carrier maps are not a newly admitted full native rotation law.

For the explicit chosen convention A_(5^a7^b)=A5^a*A7^b, define
D(m,n)=A_m*A_n*A_(mn)^(-1).
Then the following is an identity for every invertible choice of representatives:

D(l,m)*D(lm,n) = A_l*D(m,n)*A_l^(-1)*D(l,mn).

Proof: both sides telescope to A_l*A_m*A_n*A_(lmn)^(-1). The conjugation term transports the earlier defect into the proper frame; merely adding or multiplying scalar defect magnitudes does not express this law. The equality is all-scale within its stated algebra, not inferred from finite checks. A common basis change conjugates the relative H; trace and determinant are preserved. Per-node arbitrary gauge changes and a canonical optimal defect norm need separate contracts.

A scalar-only failure witness is A=diag(2,1/2), B=diag(1/2,2): both have squared Frobenius size17/4. A subsequent A^(-1) sends A to I (size2), but sends B to diag(1/4,4) (size257/16). Directional shape information cannot be recovered from the equal scalar size.

## 4. Remainder and predictive repair: keep only what the future needs

Exact division retains x=bq+r, 0<=r<b. Two stages give x=bcq+r_b+b*r_c. First divide by5 then7 or by7 then5 yields the same final quotient floor(x/35) and canonically convertible scalar remainder x mod35, though the intermediate remainder tuple differs. This is a counterweight to overclaiming: path dependence is not unavoidable in every arithmetic lift, and intermediate history need not survive when the future observer only requests the final quotient/remainder.

The T6 coarsest future-safe equivalence is relative to a declared finite state set, action language and observation:
s ~_h t iff all words u with length<=h have Obs(T_u s)=Obs(T_u t).
Richer action languages or longer horizons refine the partition. On a finite deterministic closed state set, the original T6 fixed-point algorithm gives the all-finite-word stable partition. This is not an infinite-state bounded-memory theorem.

Executed probe: states (x,tag), x in Z/35 and tag in{0,1}; Obs=floor(x/5). The tag is explicitly inert and unobserved, not a covert semantic feature. With only add5, 70 raw states safely reduce to7 blocks forever. With add1, block counts through horizons0..6 are 7,14,21,28,35,35,35. Residues become necessary but the inert tag remains removable. The 34,300 pair/signature comparisons against direct output-word enumeration agree with unchanged T6. An unsafe horizon0 quotient is rejected by its original transition-table builder.

The previous native common-depth witness is retained as a regression: (3,-1,-1,-1,-1,-1)/8 and (7,1,1,1,1,1)/12 share a min-zero readout but have depths -1/8 and1/12. This is not permission to identify the full states.

## 5. A genuinely executable contraction: exact affine degree-two moments

For any finite positive rational measure mu on rational coordinates, use the algebraic homogeneous column xbar=(x,1). The last1 is a constant, not a seventh native spatial axis. Define

M(mu)=sum_x mu(x)*xbar*xbar^T.

This stores mass, first moments and all second moments. For an affine branch use
Abar=[[A,b],[0,1]]. A fixed-weight packet H acts by the exact positive linear map

L_H(M)=sum_(w,A,b) c_(w,A,b)*w*Abar*M*Abar^T.

Proof: substitute xbar'=Abar*xbar and exchange finite sums. Therefore
L_(H star G)=L_G composed with L_H,
L_(H+G)=L_H+L_G.

No Gaussian approximation is used. Every degree<=2 polynomial observation is a linear functional of M, and pulling it back through an affine action still has degree<=2. Consequently equal M values remain indistinguishable under all later declared fixed-weight affine packets and degree<=2 observations. This proves the precise compression lease, including arbitrarily many finite stages in this family.

For d=6, the symmetric7x7 M has28 independent rational entries. MomentState stores those28; temporary calculations expand the symmetric matrix. Exact weight histograms, count/dominant data and labeled identities are separately retained when the observer requires them. Rational numerator/denominator bit sizes can grow: 28 entries is not constant bit memory or a complete memory field representation.

Executed signed-axis probe: each stage cyclically permutes the six raw coordinates then translates by +e1 or -e1, each branch weight1. The declared choice is a finite native-coordinate affine diagnostic, not a physical transition probability or full rotation model. Explicit enumeration through8 stages (256 paths at stage8) matches the moment recursion. At32 stages the compressed computation represents2^32=4,294,967,296 path contributions without enumerating them; mass=2^32, mean=0, normalized covariance=diag(6,6,5,5,5,5). This is an exact compressed calculation under the proved law, not a claim to have visited/tested4.29b individual paths.

## 6. Failure boundaries are part of the capability

Moment-only state is not complete: 1/2 delta_-1 +1/2 delta_1 and 1/8 delta_-2 +3/4 delta_0 +1/8 delta_2 have the same mass, mean and second moment; their fourth moments are1 and4, and zero-location masses0 and3/4. Threshold, occupancy and nonlinear future queries therefore cannot silently use the degree-two lease.

The moment-action law requires fixed state-independent branch weights at each stage (or a separately declared suitable kernel with a proven closure). For y=Ax+epsilon, the common covariance rule ACA^T+Q also needs the correct cross covariance: if epsilon=X on X=+/-1, true variance is4, while dropping cross terms gives2. Our exact action method handles y=2x directly; it does not turn endogenous noise into independent alternatives.

Signed spatial displacement is not signed branch mass. Two positive weight1 shifts +1/-1 give first moment0 but mass2 and normalized variance1. Shape/phase effects may close while positive coverage/multiplicity remains. Do not import amplitude cancellation or packet inverses from deterministic matrix inverses.

## 7. Implementation, checks and admission

Research-directory files (not production src):
- brc_transport.py: affine effect histogram, original-histogram projection, exact action moments, packed MomentState, comparison defects, mixed-radix adapters.
- verify_extension.py:12 executed check groups, including48 random packet triples,216 exact cocycle triples,2,004 remainder round trips,34,300 future-signature pair comparisons and explicit/contracted moment checks.
- verification_results.json: actual output, status PASS.

Local Python compilation passed. Original histogram/predictive files were compared against remote Git blob hashes before execution. The standalone artifact contains their exact copies and a clearly labeled minimal prime-valuation dependency excerpt; in an EM checkout the prototype can use the existing enterprise_math package via PYTHONPATH=src.

SHA256:
- brc_transport.py: a6a6b5369301ae07fe3ba654f7744c6204d3819742db408d1c17f5adc7cd23d1
- verify_extension.py: 0cfe5b84213e06e5553de62c71c5674c158ab91c176930bc99a4894615df0641
- verification_results.json: 4b74278d1c1670bcdeefb9f9e962f05787f0be3b0688340a5911fac4b68ae57f

No full project test suite, independent review, Lean formalization, generic weighted minimization, production Nollm integration or semantic recall benchmark is claimed. Finite checks supplement the written identities, not replace their proofs. Publish as a BRC composition/domain-extension candidate only.

## 8. Smallest useful continuation

The selected extension now has equations and runnable tests. The next scientific question is to declare an actual Nollm coverage/recall operator and determine which part satisfies the affine moment lease and which operation first breaks it. At that first break, use a concrete distinguishing pair to identify the needed residual or higher/joint observation; do not indefinitely add generic hidden fields or external semantic relation indexes. Preserve the existing exact source, tests and typed failure witnesses rather than restarting the 5/7 experiments.
