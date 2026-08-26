<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-PERFECT-PRIME-TABLE-CRITICAL-COFACTOR-ALL-M-PROOF",
  "title": "Perfect Prime Table Critical Cofactor All-m Proof",
  "kind": "RESEARCH",
  "owner": "research/perfect-prime-table-critical-cofactor-all-m-proof",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "For the exact critical d=m-2 Perfect Prime Table cofactor system, prove det(M_m) != 0 for every admissible m, with small-m cases explicitly classified, or produce an exact integer counterexample. Prior exact computations reported full rank for selected m through 40, but no all-m proof.",
  "next_action": "Reconstruct and independently verify the exact square matrix M_m from the mixed-difference condition; reproduce the reported finite certificates; then attack the all-m determinant through the falling-factorial positive-transfer/Jacobi boundary-minor reduction, with strict total positivity or an exact determinant formula as the primary closure routes while running an independent exact counterexample search.",
  "dependencies": [],
  "source_refs": [],
  "evidence_status": "RECOVERED_FRONTIER / EXACT_FINITE_REPORT_THROUGH_M40_REVERIFY_REQUIRED / ALL_M_OPEN",
  "last_progress_ref": "Recovered prior research frontier: the critical d=m-2 coefficient matrix was reported exact full rank for m=4,...,16,18,20,22,25,30,35,40, with largest checked square size 1521; an all-m determinant proof remained open.",
  "last_progress_at": "2026-08-26T20:02:30+08:00",
  "hard_block": null,
  "tags": [
    "perfect-prime-table",
    "critical-cofactor",
    "all-m",
    "determinant",
    "total-positivity",
    "Jacobi-minor",
    "exact-integer",
    "counterexample"
  ],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-PERFECT-PRIME-TABLE-CRITICAL-COFACTOR-ALL-M-PROOF",
  "parent_objective_id": "PERFECT_PRIME_TABLE_CRITICAL_COFACTOR_CLOSURE",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "PPT1",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "NEW_DIRECTION",
  "parent_task_id": null,
  "successor_gate": null,
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:aad427281b91d39273ba54d3f3d5779600ff28f651927cc9b44c20d6694acb58",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# Perfect Prime Table Critical Cofactor All-m Proof

Status: `PUBLISHED_REGISTERED / DIRECT_USER_DIRECTION / NEW_DIRECTION / ALL_M_PROOF_OR_EXACT_COUNTEREXAMPLE`

## Mother question

For the exact critical Perfect Prime Table cofactor problem at degree

\[
d=m-2,
\]

is the associated square coefficient matrix \(M_m\) nonsingular for every admissible integer \(m\), or does there exist an exact counterexample?

The target is not another finite-range rank extension. The task must convert the observed full-rank phenomenon into a uniform theorem, or identify the first exact obstruction.

## Frozen inputs and scope

### Exact table and cofactor system

For integer \(m\ge 2\), use

\[
A_{ij}=\prod_{k=0}^{m-1}\bigl(1+i+mj+k m^2\bigr),
\qquad 1\le i,j\le m.
\]

At the critical degree \(d=m-2\), write

\[
c(x,y)=\sum_{a,b=0}^{m-2}u_{ab}x^a y^b,
\qquad D_{ij}=c(i,j)A_{ij}.
\]

The row-plus-column condition on \(D\) is equivalent to the vanishing of all mixed second differences

\[
D_{ij}-D_{i1}-D_{1j}+D_{11}=0,
\qquad 2\le i,j\le m.
\]

Thus the critical coefficient matrix is the \((m-1)^2\times(m-1)^2\) matrix indexed by rows \((i,j)\in\{2,\ldots,m\}^2\) and columns \((a,b)\in\{0,\ldots,m-2\}^2\),

\[
M_m[(i,j),(a,b)]
=
A_{ij}i^a j^b-A_{i1}i^a-A_{1j}j^b+A_{11}.
\]

The load-bearing statement is

\[
\det M_m\ne 0.
\]

The researcher must independently reconstruct this derivation before relying on any reported computation.

### Recovered finite frontier to reverify

Prior research reported exact full rank at the critical degree for

\[
m=4,5,\ldots,16,18,20,22,25,30,35,40,
\]

with the largest checked matrix having size

\[
(40-1)^2=1521.
\]

These are recovered claims, not fresh certificates. Reproduce enough of them with exact arithmetic to verify that the reconstructed matrix agrees with the earlier object. Explicitly classify the small cases \(m=2,3\) if the final theorem is stated from \(m\ge2\).

No finite cutoff, however large, may be promoted to an all-\(m\) theorem.

### Falling-factorial transfer structure

Use the falling-factorial basis

\[
F_{r,s}(i,j)=i^{\underline r}j^{\underline s}.
\]

For every scalar shift \(\alpha\), the multiplication operator satisfies the exact identity

\[
(i+mj+\alpha)F_{r,s}
=
F_{r+1,s}+mF_{r,s+1}+(r+ms+\alpha)F_{r,s}.
\]

For the table factors take

\[
\alpha_k=1+k m^2,
\qquad k=0,\ldots,m-1.
\]

All transfer coefficients in the natural degree filtration are nonnegative and the diagonal weights are strictly positive. A primary route is to turn this positive transfer structure into an exact statement about the critical complementary minor, with all index sets, normalizations and signs written explicitly.

### Reciprocal moment structure

The reciprocal table has the exact moment representation

\[
\frac1{A_{ij}}
=
\frac{m^{2(1-m)}}{(m-1)!}
\int_0^1 x^{i+mj}(1-x^{m^2})^{m-1}\,dx.
\]

This gives a strict-total-positivity route for the reciprocal kernel in its natural ordered variables. Such a route is admissible only if it is connected exactly to the determinant or complementary minor that controls \(M_m\). Generic total-positivity language is not a substitute for that bridge.

### Primary closure routes

Work the following routes in whichever order gives the sharpest exact progress:

1. **Transfer-minor positivity.** Express the critical determinant, or its Jacobi-complementary reduction, as a positive path/minor quantity generated by the falling-factorial transfer matrices, and prove strict positivity for every \(m\).
2. **Strict-total-positivity spectral/minor bridge.** Use the reciprocal moment kernel to prove the exact required minor nonzero, including any oscillation or eigenvalue exclusion step actually needed by the reduction.
3. **Closed determinant formula or recurrence.** Derive a product, condensation identity, or recurrence for \(\det M_m\) or the reduced boundary determinant and prove every factor is nonzero.
4. **Independent exact counterexample search.** Search increasing \(m\) using exact integer/rational arithmetic and rank/determinant certificates. This is a falsification route and must remain logically independent of the proof heuristic as far as practical.

A previously suggested Jacobi complementary-minor reduction from the \((m-1)^2\)-dimensional determinant to a boundary minor of dimension \(2m-1\) is high priority, but it is not frozen as true input. Reconstruct it from first principles and record the exact ambient matrix, selected row/column sets, scaling factors and determinant sign before using it.

### Exactness requirements

- Floating-point rank, singular values or numerical conditioning may guide experiments but cannot certify the theorem or a counterexample.
- If symbolic factorization is used, retain an independently checkable exact identity.
- If a total-positivity theorem is imported, verify every hypothesis and the precise ordering of variables/minors.
- Do not infer positivity of an arbitrary mixed or complementary minor merely from the statement that a parent kernel is strictly totally positive.
- If two independent exact implementations disagree, freeze the discrepancy and resolve it before using either output as evidence.
- If the full theorem does not close, isolate the smallest remaining lemma with explicit quantifiers rather than replacing it with a broad methodological slogan.

## Hard target and required outputs

Hard target:

`CRITICAL_COFACTOR_ALL_M_NONVANISHING_PROVED_OR_EXACT_COUNTEREXAMPLE`

Required outputs:

1. an exact derivation of the square matrix \(M_m\) from the cofactor/mixed-difference equations;
2. exact re-verification of the recovered finite frontier sufficient to pin object identity, plus explicit treatment of the smallest admissible \(m\);
3. a complete falling-factorial transfer representation with degree filtration and boundary indexing;
4. if the Jacobi route survives, a fully explicit complementary-minor identity reducing the critical determinant to the claimed boundary object;
5. either a rigorous all-\(m\) proof that \(\det M_m\ne0\), or an exact counterexample \(m=m_0\) with a checkable nonzero kernel vector or equivalent rank certificate;
6. if strict total positivity is used, the exact theorem-to-target bridge rather than only positivity of the reciprocal table;
7. if a determinant recurrence/product is used, exact base cases and proof that every denominator and factor used in the induction is nonzero;
8. an independent exact checker/counterexample search and a machine-readable certificate artifact for the finite computations actually cited;
9. a route ledger distinguishing proved identities, computational evidence, failed routes, and conjectural bridge lemmas;
10. if the hard target remains open, one uniquely identified smallest unresolved lemma with explicit quantifiers and a concrete next attack;
11. a durable return at `research_returns/PERFECT_PRIME_TABLE_CRITICAL_COFACTOR_ALL_M_PROOF_RETURN_20260826.md`.

## Research value to preserve

The finite critical-rank phenomenon is already strong enough that extending the cutoff by another handful of \(m\)-values has low marginal value. The high-leverage question is structural: why the critical cofactor matrix should remain nonsingular for arbitrary \(m\), or exactly where that pattern fails.

A proof would convert a large exact computation into a reusable theorem about the Perfect Prime Table transfer/moment structure. A counterexample would be equally valuable because it would stop an unjustified extrapolation and identify the first obstruction. A rigorous reduction to one sharply stated boundary lemma is also useful because it turns a quadratic-size determinant problem into a focused linear-size frontier without overstating closure.

## Success, kill, and return criteria

Freeze exactly one primary verdict:

- `ALL_M_NONVANISHING_PROVED` — a complete exact proof establishes \(\det M_m\ne0\) for every stated admissible \(m\);
- `EXACT_COUNTEREXAMPLE_FOUND` — an exact \(m_0\) is exhibited with a reproducible singularity certificate;
- `BOUNDARY_REDUCTION_PROVED_CLOSURE_LEMMA_OPEN` — the large determinant has been rigorously reduced to a smaller exact family, but its uniform nonvanishing remains unproved;
- `STRUCTURAL_ROUTE_REFUTED` — a load-bearing proposed bridge, such as the claimed boundary reduction or required total-positivity implication, is exactly false, while the original determinant question remains open;
- `CHECKER_DIVERGENCE` — independent exact implementations disagree and the discrepancy is not resolved within task scope.

Only `ALL_M_NONVANISHING_PROVED` and `EXACT_COUNTEREXAMPLE_FOUND` satisfy the hard target.

Do not declare success from finite evidence, heuristic positivity, or a numerically stable determinant. If a primary structural route is refuted, preserve the exact obstruction and continue through another route unless the original hard target is already settled. If no route closes, return the strongest exact partial theorem and the smallest unresolved lemma without weakening the target statement.
