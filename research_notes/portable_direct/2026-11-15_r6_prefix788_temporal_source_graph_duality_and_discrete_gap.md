# PREFIX-788 / R6 — Temporal provenance-graph duality, exact path-gap witnesses, and subset-sum hardness

Date: 2026-11-15 (Asia/Shanghai). Status: AUTHOR_PROVED / EXACT_INTEGER_RATIONAL_REGRESSION / UNREVIEWED / NOT_ADMITTED.
Research provenance: independent R6 scalar observer unit, continuing PREFIX-787 (researcher history EM-DIRECT-E77192, activity RA-66BBE259AEE1AD543D9454A3); not a shared-task CLAIM.
Frozen scientific baseline: `awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d`.
Predecessor: `research_notes/portable_direct/2026-11-15_r6_prefix787_branch_union_common_dual_certificate.md`.

## Question and exact model

Can sequentially correlated signed source histories be kept in a tractable exact certificate, without replacing mutually exclusive paths by independently selectable scalar observations?

Let G=(V,E) be a finite directed acyclic multigraph with one source s, one target t and at least one s-to-t path. Each edge e bears an independently selectable contribution in a nonempty compact convex polytope K_e contained in R^m. These edgewise choices are independent **conditional on the full chosen path**; the graph encodes the allowed temporal and provenance transitions. Fix A,B in R^m, q>0. For a path p and z_e in K_e define

    v(q,p,z)=A-qB + sum_(e in p) z_e,
    a(q,p,z)=(v,-v).

The reflected scalar observer a has both signs exactly when v != 0, and has sign amplitude ||v||_infinity. Define the true uniform amplitude rho_path as the infimum of this norm over q>0, paths p and their permitted edge contributions. Define rho_hull by convexifying the union of full-path contribution sets **after** enforcing the graph transitions. Put

    Lambda={lambda in R^m : ||lambda||_1 <= 1, lambda dot B <= 0},
    w_e(lambda)=min_(z in K_e) lambda dot z,
    F_p(lambda)=lambda dot A + sum_(e in p) w_e(lambda).

This is an external affine scalar observer model. No native X6 dimension or Cell/Link/Port/time transport is assumed.

## Theorem 788.1 — Exact temporal path duality

For every graph and compact polytopes as above,

    rho_path = min_(p:s->t) max_(lambda in Lambda) F_p(lambda),
    rho_hull = max_(lambda in Lambda) min_(p:s->t) F_p(lambda),
    0 <= rho_hull <= rho_path.

All displayed maxima over Lambda are attained. Therefore rho_path>0 iff every permissible full path p admits a path-dependent lambda_p in Lambda with F_p(lambda_p)>0. In contrast rho_hull>0 iff one common lambda in Lambda satisfies F_p(lambda)>0 for every permissible full path. The sharp amplitudes coincide iff a common lambda satisfies F_p(lambda)>=rho_path for every p.

**Proof.** Fix p. Its attainable contribution set K_p=sum_(e in p) K_e is a compact convex Minkowski sum. Since `||x||_infinity=max_(||lambda||_1<=1) lambda dot x`, the convex linear minimax/LP dual for q>=0 and z in K_p gives

    inf_(q>=0,z in K_p)||A-qB+z||_infinity
      = max_(lambda in Lambda)[lambda dot A + min_(z in K_p) lambda dot z]
      = max_(lambda in Lambda) F_p(lambda).

For a lambda with lambda dot B>0 the infimum of `-q lambda dot B` over q>=0 is minus infinity, so feasible dual witnesses obey lambda dot B<=0. The infimum over q>0 equals that over q>=0 by continuity at q=0; a boundary infimum need not be attained by a strictly positive q. Taking the minimum over the finite path family proves the first formula. The convex hull of the finite union of compact K_p is compact convex. A linear functional has the same minimum over this convex hull as over its generating union, hence `min_p sum_e w_e(lambda)`. Applying the same dual gives the second formula. The inclusion of the actual path union in its hull gives the inequality. Lambda is compact; each F_p is continuous and concave (each support minimum is concave), so all maxima are attained. Positivity and equality criteria follow by the two formulas and attained maxima. QED.

## Theorem 788.2 — Bellman oracle for a common certificate

For any fixed lambda in Lambda, define H_lambda(t)=0 and, in reverse topological order,

    H_lambda(x) = min_(e=(x,y)) [ w_e(lambda) + H_lambda(y) ]

for all x from which t is reachable. Then

    min_(p:s->t) F_p(lambda) = lambda dot A + H_lambda(s).

**Proof.** Every path from x begins with one outgoing edge and then a path from y. Additivity of the independent edge-contribution support minima makes the displayed recurrence exact, by reverse induction in the DAG. QED.

Thus, a proposed common dual lambda can be evaluated with one shortest-path pass rather than enumerating all histories. For rational polytope data, a full common-certificate optimization is an exact rational LP: impose `lambda dot (A+sum_(e in p) z_e) >= r` for all paths p and all vertices z_e of K_e, together with lambda in Lambda, then maximize r. Bellman's recurrence provides an exact separation oracle for any proposed lambda. The potentially exponential path/vertex constraints are substantive; the oracle alone is not a claim of a polynomial-time algorithm for the true pathwise amplitude.

## Proposition 788.3 — Same time-slice marginals, different exact uniform margins

Take m=2, A=(1,0), B=(1,0), two consecutive time stages, and deterministic edge contributions `(0,M*sigma_i)` with sigma_i in {-1,+1} and M>0. Give the graph exactly the two permitted histories `(+,+)` and `(-,-)`, i.e. sigma_2=sigma_1. Then

    v=(1-q, 2M) or (1-q,-2M),
    rho_path=2M.

A common dual does not exist: a candidate lambda=(lambda_1,lambda_2) in Lambda obeys lambda_1<=0, and the minimum of the two branch dual values is `lambda_1-2M*|lambda_2|<=0`. On the other hand each branch has the sharp witness `(0,+1)` or `(0,-1)`.

A second graph has exactly the same marginal choices `{+M,-M}` at **each individual stage** but permits all four sign histories. Its crossed histories `(+,-)` and `(-,+)` give v=(1-q,0), hence at q=1 its margin is 0. The correlated and uncorrelated models therefore have the same per-stage source ranges but exact margins 2M and 0, with an arbitrarily large difference. Convexification of the correlated graph's full-path source set also gives margin 0. This is a temporal source/provenance effect, not an additional spatial coordinate.

## Theorem 788.4 — Exact pathwise cancellation is NP-complete in a restricted integer family

Let positive integers a_1,...,a_n and target T>=0 be given in binary (the SUBSET-SUM decision instance). Construct a layered DAG with two parallel edges per stage: an unselected edge with deterministic contribution (0,0) and a selected edge with contribution (0,a_i). Take m=2, A=(1,-T), B=(1,0), and edge polytopes as those singletons. For the path corresponding to subset S,

    v(q,S)=(1-q, sum_(i in S) a_i - T).

Since q=1>0 is permitted,

    rho_path = min_(S subset {1,...,n}) |sum_(i in S) a_i - T|.

Therefore deciding `rho_path=0` is NP-complete even with deterministic integer edge labels, two output components and one shared positive scalar parameter. A subset S is a polynomial-size certificate for membership in NP; the displayed polynomial reduction from SUBSET-SUM proves hardness. Equivalently, deciding `rho_path>0` is coNP-complete for the same family. With 0<=T<=sum_i a_i, the convex hull of the full-path sums contains T, so rho_hull=0 regardless of whether any exact subset exists. In particular, a no-instance with integer data has rho_path>=1 while rho_hull=0.

**Exact instance.** a=(3,5), T=4. Permitted source sums are {0,3,5,8}; rho_path=1, but their convex hull contains 4 and rho_hull=0. This instance provides a small falsification test for any algorithm that replaces reachable histories with their convex hull before answering exact cancellation.

## Reproducible evidence and scope

Companion program: `research_notes/portable_direct/PREFIX788_R6_TEMPORAL_PATH_CERTIFICATE_CHECK.py`.
Companion result: `research_notes/portable_direct/PREFIX788_R6_TEMPORAL_PATH_CERTIFICATE_RESULTS.json`.
The program uses Python standard-library `fractions.Fraction` and exact integer enumeration. Regression scope: 168 deterministic subset instances; 11,088 rational common-dual shortest-path oracle comparisons against full path enumeration; 159 positive rational M values for matched-sign temporal correlation; 11,912 exact assertions. It returns `ALL_CHECKS_PASS PREFIX788 TEMPORAL_BRANCH_DUAL_AND_SUBSET_GAP`. The general theorems depend on the proofs above, not the finite regression count. Polynomial-time claims apply only to fixed-lambda DAG oracle evaluation, with per-edge support values available; the NP-completeness statement concerns pathwise exact cancellation on binary-encoded inputs.

## Next live scientific frontier

Extract a **verified** source-transition graph from native BRC/X6 Cell/Link/Port/signed-source/event-time observations, including the concrete representation of reachable edges, constraints between edge sources, and any relation between q and allowed paths. Test whether independent K_e choices conditional on a path actually hold. If they do, calculate branchwise margins and a Bellman common-dual test. If source memory couples edge contributions beyond the path graph, replace the separable edge model by an explicit joint path polytope; do not assume independent edge supports. The original native comparator grid-exclusion tally is unchanged. The frozen input pin and all prior PREFIX-787 artifacts are preserved.
