# C26 finite positive data image and normalized recovery

AUTHOR_PROVED / LOCAL_UNREVIEWED / APPLIED_CONSUMER_APPENDIX.
Classification: same-family RESULT_ONLY_STANDARD_COMPOSE; noncanonical appendix,
not a new paper, generic Tool, principal theorem or priority claim.
Sole new applied-consumer author: EM-DVR-BFF6DC.
Actual original SID: MCP-47562f9f432d4978a7bea0dd60ecc4aa.
Actual original DA: DA-144D0C4639CACEEE75DC. Researcher RA: none.
First local artifact creation: 2026-10-17 10:42:10 UTC.
Author Source: PENDING. Independent technical whole: PENDING.
Root supplies CONTROL/routing and zero mathematical construction/votes.

This appendix supplies all finite proof steps for the actual data-image question
on the explicitly conditional C26 model. It does not register the original
source author, revive any denied operation or extend the actual target family.
The same model can be identifiable while its minimal design accepts every
strictly positive complete data table. This concerns exact mathematical tables,
not empirical statistical fit, sampling, noise, physical mechanisms or cost.
No research program, numerical calculation, solver or enumeration was used.

This is a new finite mathematical question on the same explicit conditional C26 model, not a claim that the original unregistered/conditional source or physical model has been accepted. No sample/estimation/physical-noise/cost conclusion is asserted.

## 1. Actual input and precise question
Use the exact model in accepted17238, author Source c1c633fec98a2e5ce02e93972045551ec662b33f,
research_notes/owner_goal_20261017/c26_returned_control_schedule_criterion_4a56e9/C26_ARBITRARY_RETURNED_CONTROL_SCHEDULE_DRIFT_ALIAS_IFF_AUTHOR_COMPOSE_APPENDIX_V1.md
(17238B/e9936a2f886d866339364acc5526b3d6945539e199142755112983bfa7fb6427/e292a9a04f0fa5aaab051dca325cb7d794f219a4).
BFF already genuinely whole-read this and its literal11047 source, and completed own authorSource/exact and technical19043 whole/Source custody. This phase only reread the actual17238 opening/sections1-4 and beginning5 from the existing fixed local file. No new upstream API/whole claim. C24 remains unwhole/UNKNOWN and supplies no theorem.

Let Y be finite nonempty, fix y0, strictpositive known matrix T, d>=0, distinct known nonnegative integer positions n_j, L>=1, and binary b_j. The actual model is
P_j(y) proportional Q(y) [product_(k=1)^d D_k(y)^V_jk] K(y) r_K(y)^b_j,
V_jk=binom(n_j,k), k=0..d, r_K=(TK)/K.
K>0 has uniform mean1, Q>0 sum1, D_k>0 and D_k(y0)=1.
The original admissible target family F is a specified nonempty subset of these K. It may contain extra source-family constraints; these are never erased.
Given arbitrary complete strictlypositive normalized distributions P_j, ask exactly when a model exists. Old17238 proved uniqueness/aliases only AFTER admissibility was assumed, and explicitly excluded this image question.

Write ell_j(y)=log(P_j(y)/P_j(y0)), let V be the L by(d+1) matrix, and H=[V b]. Define condition E_H: for every y, ell(y) lies in col_R(H). Because H is rational, E_H is equivalent to finitely many exact positive product equations
product_j [P_j(y)/P_j(y0)]^w_j=1
for an integer basis of its rational left kernel (denominators cleared). These are mathematical complete-distribution identities, not executed logarithms/root solvers or native readouts.

## 2. Finite positive-matrix existence and uniqueness, fully paid here
For ANY strictpositive finite square A, let C=max_column sum_i A_ij. On the compact feasible set
x>=0, sum_i x_i=1, 0<=lambda<=C, Ax>=lambda x,
maximize lambda. It is nonempty, and x uniform shows its maximum lambda_*>=min_i sum_j A_ij>0.
For any feasible pair, summing Ax>=lambda x gives lambda<=C. Let x be a maximizer and e=Ax-lambda_*x>=0. If e is nonzero, x'=Ax>0 and
Ax'=lambda_*x'+Ae,
where Ae is strictlypositive. Thus epsilon=min_i(Ae)_i/x'_i>0 gives Ax'>=(lambda_*+epsilon)x'. Normalizing x' yields another feasible pair with a larger lambda, contradiction (the summed inequality automatically keeps it <=C). Hence e=0, and Ax>0 with lambda_*>0 implies x>0. A positive eigenvector exists.
For uniqueness, if Ax=lambda x and Ay=mu y with both vectors positive, set u_i=y_i/x_i. The normalized rows A_ij x_j/(lambda x_i) are strictlypositive probabilities, and
(mu/lambda)u_i=sum_j probability_ij u_j.
At a maximum and minimum of a nonconstant u this forces mu/lambda<1 and >1 respectively. Thus u is constant and mu=lambda. Mean1 fixes the positive eigenvector uniquely.
This is the classical finite Perron argument proved here as ordinary standard composition; no new generic Tool.

## 3. Good schedule: b not in col_Q V
Since V,b are rational this is also b not in col_R V. Distinct-position polynomial evaluation gives rankV=min(L,d+1). Good schedules force L>=d+2, so H has full column rank d+2.
If E_H holds, there are UNIQUE coefficients a_0(y),...,a_d(y),h(y) with
ell(y)=V a(y)+b h(y).
At y0 all these are zero. Set R(y)=exp(h(y)), so R(y0)=1. The strictpositive matrix A_R=diag(R^-1)T has, by section2, a unique mean1 positive eigenvector K_R and positive eigenvalue gamma. Its equation says
(TK_R)(y)/K_R(y)=gamma R(y);
at y0 gamma=r_(K_R)(y0), hence r_(K_R)(y)/r_(K_R)(y0)=R(y).

The EXACT image criterion is:
E_H AND K_R belongs to the original admissible family F.
The second condition must remain explicit. It is automatic only when F is the entire positive mean1 target family. No arbitrary K_R is claimed to have an original lambda representation or satisfy unproved source constraints.

Necessity: an actual model gives
ell_j(y)=log[Q(y)K(y)/(Q(y0)K(y0))]
+sum_(k>=1)V_jk log D_k(y)+b_j log[r_K(y)/r_K(y0)].
This gives E_H, and uniqueness of the coefficient decomposition/Perron vector forces actualK=K_R inF.
Sufficiency: when K_R inF set
D_k(y)=exp(a_k(y)),
Q(y) proportional exp(a_0(y)) K_R(y0)/K_R(y).
All functions are strictlypositive, D_k(y0)=1, and Q is normalized by its one positive sum. Substitution yields exactly ell_j(y). Both the produced row and P_j are normalized probability vectors, so equal ratios relative y0 imply equality of the ENTIRE row. This restores every row normalizer and all positive nuisances, rather than just a contrast.
For this schedule the recovered K,Q,D are unique, because H and the positive eigenvector are unique.

## 4. Bad schedule: b in col_Q V
Then colH=colV. Write b=V beta with rational beta. E_H is again necessary.
It is also sufficient for EVERY chosen K in nonemptyF, not just for some abstract target: choose real g(y) with Vg(y)=ell(y), and g(y0)=0. Such a selection exists under E_H; it can be any fixed linear right inverse on colV, hence sends0 to0. Put kappa(y)=log[K(y)/K(y0)] and h_K(y)=log[r_K(y)/r_K(y0)]. Define
a_0(y)=g_0(y)-kappa(y)-beta_0 h_K(y),
a_k(y)=g_k(y)-beta_k h_K(y), k>=1.
Set Q(y) proportional exp(a_0(y)) and D_k(y)=exp(a_k(y)).
Then log row ratios equal
V a+kappa*1+b h_K
=Vg-(Vbeta)h_K+b h_K=ell.
All positivity, D_k(y0)=1, Q sum1 and complete row-normalization requirements hold. Thus E_H is the exact criterion and every original admissible target is compatible. Nuisance uniqueness is NOT asserted if V is rank-deficient.
If L<=d+1, V has full row rank, so E_H is vacuous and every positive observation table is realizable for every chosen K inF. This is consistent with the original complete alias theorem.

## 5. Actual consumer and finite stopping point
For unrestricted positive mean1 F, ANY schedule has exact image E_H. In log-odds coordinates its codimension is
(|Y|-1)(L-rankH).
For a minimally identifying design L=d+2 with b outside colV, H is square/invertible, hence EVERY strictlypositive table is realizable, with unique K,Q,D. Such a minimal identifying experiment therefore supplies no internal exact model-consistency restriction in this unrestricted family. At least one extra row is needed for a nonvacuous contrast-consistency test; for L>d+2 the exact restrictions are the integer left-kernel products above. For |Y|>=2 these extra-row restrictions are nonvacuous. For |Y|=1 every row is the singleton distribution and the codimension remains0 at every L. This is a complete-distribution algebraic statement, not a statistical goodness-of-fit or sample complexity theorem. If F is restricted, its explicit K_R membership can itself impose additional restrictions even at the minimal design.

The missing new obligation was general positive eigenvector existence plus the return from arbitrary log-odds to all actual Q/D/normalizers. Sections2-4 pay it. This is not merely the old admissible-model uniqueness theorem or a change of a stability constant. Standard finite linear algebra/positive-matrix composition suffices, so classify RESULT_ONLY_STANDARD_COMPOSE within C26; no new paper/Tool/Source is proposed.

## 6. History and limits
BFF new internal construction NONZERO and sole argument construction. 4A provided only existing coverage/occupation metadata:17238 did not cover arbitrary-data image, and she was not occupying it; no formula/repair was supplied. Root supplied routing/CONTROL, zero mathematics. The old private/warm C26 histories remain NONBLIND; no independent review is claimed for this new argument.
No C22/C24 whole, source-family lambda injection, physical fit/registration status, external computations, Native/formalTask, additional query, RA/identity/helper/budget or Source permission is inferred. The complete author chat argument was genuinely selfread at 2026-10-17 10:39:00 UTC and remains intact in its original store. This is its first noncanonical local applied-consumer appendix. The new artifact has no independent whole acceptance or actual author Source at creation; its complete selfreading and external oncefreeze are subsequent observations. Original17238/19043 and their histories are unchanged. The coefficient-caller locator gap is a separate retired intake, not the premise for this C26 result.
Global-Knowledge-Sync: main@67a02007 / GLOBAL_KNOWLEDGE_V1

### Actual input, contribution and observation ledger

```json
{
  "schema": "C26_DATA_IMAGE_APPLIED_CONSUMER_ACTUAL_CONTEXT_V1",
  "actual_created_at_UTC": "2026-10-17 10:42:10 UTC",
  "mathematical_author": "EM-DVR-BFF6DC",
  "classification": "NONCANONICAL_SAME_FAMILY_RESULT_ONLY_STANDARD_COMPOSE",
  "necessary_literal_input": {
    "source": "c1c633fec98a2e5ce02e93972045551ec662b33f",
    "path": "research_notes/owner_goal_20261017/c26_returned_control_schedule_criterion_4a56e9/C26_ARBITRARY_RETURNED_CONTROL_SCHEDULE_DRIFT_ALIAS_IFF_AUTHOR_COMPOSE_APPENDIX_V1.md",
    "UTF8bytes": 17238,
    "SHA256": "e9936a2f886d866339364acc5526b3d6945539e199142755112983bfa7fb6427",
    "GitOID": "e292a9a04f0fa5aaab051dca325cb7d794f219a4",
    "immutableURL": "https://github.com/awdawmip/enterprise-math/blob/c1c633fec98a2e5ce02e93972045551ec662b33f/research_notes/owner_goal_20261017/c26_returned_control_schedule_criterion_4a56e9/C26_ARBITRARY_RETURNED_CONTROL_SCHEDULE_DRIFT_ALIAS_IFF_AUTHOR_COMPOSE_APPENDIX_V1.md",
    "literal_model_scope": "Section2 equations1-2: arbitrary finite nonemptyY/y0, original strictlypositive known linearT, distinct nonnegative integer n_j, binaryb, d>=0, original nonempty admissibleF, positiveK mean1, positiveQ sum1, arbitrarypositiveDk(y0)=1, complete normalized positive observations. Original family constraints/control conventions are retained.",
    "use": "Literal model only. All new positive-eigenvector existence, image necessity/sufficiency and full nuisance/normalizer constructions are proved in this appendix. Old schedule/uniqueness theorems are contextual comparisons, not substitutes for new image proof.",
    "personal_reading": "BFF genuine prior entire17238 and original11047 semantic reads, own exact authorSource and technical19043 custody genuinely completed earlier. This phase only actual focused17238 opening/sections1-4/beginning5 printed from the existing local frozen file. No new upstream API/compare/whole claim."
  },
  "original_source_provenance": {
    "source": "617d4013a72cb3985be0dce93fb7e83b7cce28a8",
    "path": "research_notes/divisor_extrema/20261017_c26_returned_controls_drift_identifiability.md",
    "UTF8bytes": 11047,
    "SHA256": "df8fbd48693890d63ea3cae5cd46d88f9ebf8ebbaf9fc79a5a71eb5f1ffee161",
    "GitOID": "12e40af5ff8378e219812189bfaa3ad45a85ee02",
    "status": "Original SELF_CHECKED_UNREVIEWED/conditional model, NONE_ALLOCATED/REGISTRATION_PENDING/STATIC_READONLY_SCOPE_DENIED preserved. No physical fit/admission/old authority is conferred."
  },
  "coverage_and_credit": {
    "old17238_author": "EM-P11-4A56E9 actual original schedule theorem/model credit retained",
    "new_argument": "BFF sole new image-consumer construction NONZERO. General finite matrix/linear algebra methods are classical; no first-discovery claim.",
    "other_contribution": "4A supplied existing coverage/occupation metadata only, no proof formula or repair. Root CONTROL/math0. No independent reviewer has repaired or accepted this new argument.",
    "original_selfread_store": "bff_C26_exact_image_complete_author_argument",
    "original_actual_selfwhole": "bff_C26_exact_image_complete_author_selfwhole_and_bounded_closure",
    "actual_focused_read": "bff_C26_realizability_actual_literal_model_focused_readback"
  },
  "first_artifact_delta_from_complete_chat": "Title/status/context and Markdown heading formatting; original chat-only history made an explicit prior cut; singleton codimension caveat made explicit. No estimate, mathematical construction, model, theorem domain or proof repair changed.",
  "precise_limits": "OriginalF membership remains necessary in good schedule and is never inferred from positivity; original lambda parametrization is not supplied or certified. Bad schedule compatible with every existingK in nonemptyF, not nuisance uniqueness whenV deficient. Codimension/no-internal-test consequence only unrestrictedpositiveF. Mathematical complete observations only, no numerical algorithm/cost/noise/statisticalfit/Native/formalTask.",
  "unread_old": "No C22 lambda-injection or C24 positive-kernel theorem is consumed; their unwhole/UNKNOWN boundaries stay unchanged.",
  "pending": {
    "author_artifact_actual_selfread": "Future actual observation after this write",
    "external_oncefreeze": "Future after actual entire newartifact read",
    "authorSource": null,
    "independent_whole": null
  },
  "permissions": "Same SID/DA/noRA, all STOP/UNKNOWN/budgets retained; no main grant/program/query/helper/identity change. Goal OPEN.",
  "knowledge_sync": "main@67a02007 / GLOBAL_KNOWLEDGE_V1"
}
```

Global-Knowledge-Sync: main@67a02007 / GLOBAL_KNOWLEDGE_V1
