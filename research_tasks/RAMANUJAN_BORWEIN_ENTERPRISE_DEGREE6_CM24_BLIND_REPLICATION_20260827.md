<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-RB-ENTERPRISE-DEGREE6-CM24-BLIND-REPLICATION",
  "title": "Ramanujan–Borwein × Enterprise Degree-6 CM(-24) Blind Reconstruction",
  "kind": "RESEARCH",
  "owner": "research/rb-enterprise-degree6-cm24-blind-replication",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "Independently reconstruct or refute, under a blind-forward protocol, a degree-6 algebraic map from the frozen genus-4 source D to the principal discriminant -24 CM elliptic target with the prescribed principal differential direction, without access to the existing explicit map or its symbolic replay.",
  "next_action": "Using only the task-local blind inputs, reconstruct the degree-6 map by exact algebraic geometry or function-field methods; freeze an explicit X/Y candidate or a rigorous refutation, its branch divisor, target elliptic equation, pullback differential coefficient, period-scaling derivation, and SHA256 before any unblinding or broader repository/literature comparison.",
  "dependencies": [],
  "source_refs": [],
  "evidence_status": "BLIND_REPLICATION_PREREGISTERED / EXPLICIT_MAP_WITHHELD / SELF_AUDIT_EXISTS_BUT_IS_NOT_PHASE_A_INPUT",
  "last_progress_ref": "User requested independent blind replication of a closed theorem-package candidate; explicit formula withheld.",
  "last_progress_at": "2026-08-27T21:16:00+08:00",
  "hard_block": null,
  "tags": [
    "blind-replication",
    "Ramanujan-Borwein",
    "Fermat-24",
    "CM-24",
    "elliptic-correspondence",
    "degree-6",
    "exact-algebra",
    "independent-validation"
  ],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-RB-ENTERPRISE-DEGREE6-CM24-BLIND-REPLICATION",
  "parent_objective_id": "RB_ENTERPRISE_THEOREM_PACKAGE_V2_INDEPENDENT_VALIDATION",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "RBV2REP",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "REPLAY",
  "parent_task_id": null,
  "successor_gate": null,
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:497a0467870c4d495d4dbf161cf492e9d3d4a51d0a7b34e685086f25daa395f4",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# Ramanujan–Borwein × Enterprise Degree-6 CM(-24) Blind Reconstruction

Status: `PUBLISHED_REGISTERED / DIRECT_USER_DIRECTION / REPLAY / BLIND_FORWARD`

## Mother question

Can an independent researcher reconstruct or refute, without seeing the originating explicit formula, a degree-6 algebraic map from the frozen genus-4 curve

\[
D:\qquad w^4=(R+2)^2R(R^2-3)
\]

to the principal discriminant \(-24\) CM elliptic target, with pullback invariant differential proportional to the frozen principal direction below?

The purpose is independent falsification. A rigorous proof that no such degree-6 map can exist under the frozen inputs is a valid terminal outcome.

## Frozen inputs and scope

### Phase A allowed input

The blind reconstruction may use exactly the following task-local mathematical data.

1. Source curve:
   \[
   D:\quad w^4=(R+2)^2R(R^2-3).
   \]

2. Intermediate coordinate:
   \[
   t=\frac{w^2}{R+2},\qquad t^2=R^3-3R.
   \]

3. Principal differential direction:
   \[
   \phi=\frac{dR}{w}\left(1+\frac{k}{t}\right),
   \qquad
   k=-i\,3^{1/4}(\sqrt6-2).
   \]

4. Target Legendre modulus:
   \[
   \lambda_*=35+24\sqrt2-20\sqrt3-14\sqrt6.
   \]

5. The target is an algebraic twist of
   \[
   y^2=x(x-1)(x-\lambda_*),
   \]
   and its \(j\)-invariant is the principal discriminant \(-24\) CM value.

6. The required source-to-target degree is \(6\).

7. A sufficient coefficient-field bound is
   \[
   \mathbf Q(i,3^{1/4},\sqrt2).
   \]

8. For the independent period normalization, define only
   \[
   B_1=B(1/24,5/24),
   \qquad
   \Omega_P=\pi\theta_3(e^{-\pi\sqrt6})^2.
   \]
   The value of \((B_1/\Omega_P)^2\) is not an allowed Phase A input.

### Phase A blind firewall

Before the raw reconstruction freeze, do not inspect any source that exposes the originating degree-6 map coefficients, its common base point, target twist constant, exact symbolic replay, or the originating period-scaling answer. In particular, do not use account-level Global Knowledge, prior conversations, broad project journals, result-specific source history, or external search targeted at locating the withheld formula.

If the executing context has already been exposed to the originating explicit formula or its exact coefficients, that execution is not eligible to return a blind verdict.

Numerical reconnaissance and exact algebraic computation are allowed, but a numerical fit alone is not a proof.

### Raw reconstruction freeze

Before any unblinding, freeze a machine-readable artifact containing:

- the explicit candidate \(X,Y\), or a rigorous nonexistence/refutation certificate;
- coefficient field used;
- degree and branch-divisor calculation;
- target elliptic equation and exact \(j\)-invariant;
- exact pullback differential coefficient;
- independently derived value of \((B_1/\Omega_P)^2\), if a map is reconstructed;
- SHA256 of the canonical serialized artifact;
- phase marker `BLIND_RECONSTRUCTION_FROZEN`.

### Phase B comparison

Only after the raw freeze may the researcher inspect the originating result, broader project context, literature, and existing exact replay. An independently reconstructed map counts as agreement if it is equivalent under source automorphism, target automorphism, algebraic twist/unit, or an equivalent line-bundle presentation.

## Hard target and required outputs

Hard target:

`RB_ENTERPRISE_DEGREE6_CM24_BLIND_RECONSTRUCTED_OR_REFUTED`.

Required outputs:

1. an explicit algebraic map \(D\to E\) of degree \(6\), or an exact proof that the frozen target is impossible;
2. an exact degree proof including any common-base-point cancellation or equivalent divisor argument;
3. exact description of the four target 2-torsion fibers \(X=0,1,\lambda_*,\infty\);
4. an exact function-field identity for the target elliptic equation;
5. the exact pullback of an invariant differential and its proportionality to \(\phi\);
6. exact target \(j\)-invariant and identification of the principal discriminant \(-24\) CM class;
7. an independent derivation of \((B_1/\Omega_P)^2\) from the reconstructed correspondence, without importing the originating value;
8. a deterministic exact replay checker whose load-bearing identities do not depend on the numerical discovery stage;
9. the raw-freeze SHA256 and phase marker;
10. post-freeze comparison against the withheld originating formula and a prior-art/dedup audit;
11. a durable return at `research_returns/RB_ENTERPRISE_DEGREE6_CM24_BLIND_REPLICATION_RETURN_20260827.md`.

## Research value to preserve

The current Ramanujan–Borwein × Enterprise theorem-package candidate has passed an exact self-audit, but the same exposed context cannot provide genuinely independent replication of its hardest final bridge. This task preserves a clean falsification path: a second execution must reconstruct the degree-6 Fermat/CM(-24) correspondence from sparse typed data or produce an exact contradiction. Agreement would materially strengthen the theorem-package evidence; disagreement would reopen the exact final bridge rather than being hidden by self-confirmation.

## Success, kill, and return criteria

Freeze exactly one primary verdict:

- `BLIND_DEGREE6_CM24_RECONSTRUCTION_PASS` — the withheld correspondence is independently reconstructed with exact degree, elliptic identity, differential, and period scaling;
- `BLIND_EQUIVALENT_RECONSTRUCTION_PASS` — an algebraically equivalent degree-6 correspondence is independently reconstructed under allowed source/target equivalences;
- `BLIND_DEGREE6_CM24_REFUTED` — an exact contradiction proves the frozen degree-6 target impossible;
- `BLIND_INCOMPLETE_EXACT_REDUCTION` — the task reaches a strictly smaller exact reconstruction certificate but does not complete or refute the map;
- `BLINDNESS_BROKEN` — the originating explicit formula or its load-bearing coefficients were exposed before the raw freeze.

On `BLINDNESS_BROKEN`, terminate the blind run rather than relabeling it independent. Do not claim success from high-precision fitting without an exact function-field proof. A PASS validates only the stated correspondence/theorem-package evidence and does not by itself alter shared project foundations.
