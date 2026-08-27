<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-PRIME-FACTOR-SEMIPRIME-SHELL-RESIDUAL-VALIDATION",
  "title": "Prime-Factor Semiprime Shell Residual Validation on the Progressive Plane",
  "kind": "RESEARCH",
  "owner": "research/prime-factor-semiprime-shell-residual-validation",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "MEDIUM",
  "frontier": "Determine whether semiprime thin shells encoded by prime-factor coordinates retain reproducible cross-scale residual structure after deterministic small-prime, multiplicative-boundary, residue-class, and first-order prime-density effects are removed.",
  "next_action": "Build an exact-integer shell enumerator, freeze discovery/holdout scales and shell widths before inspecting holdout results, then compare raw, trimmed, prime-rank, and density-flattened residual maps against two independent null families.",
  "dependencies": [
    "RELATIONAL_AXIS_CONVENTION.md@main",
    "research_notes/DIAGONAL_GAUGE_DERIVED_DISPLACEMENT_THEOREM_PACKAGE_20260826.md@main"
  ],
  "source_refs": [
    "RELATIONAL_AXIS_CONVENTION.md@main",
    "research_notes/DIAGONAL_GAUGE_DERIVED_DISPLACEMENT_THEOREM_PACKAGE_20260826.md@main"
  ],
  "evidence_status": "DIRECT_USER_HYPOTHESIS / PRELIMINARY_EXACT_COUNTS_ONLY / NO_REGISTERED_CROSS_SCALE_RESIDUAL_RESULT",
  "last_progress_ref": null,
  "last_progress_at": "2026-08-27T21:19:16+08:00",
  "hard_block": null,
  "tags": [
    "prime-factor-coordinates",
    "semiprimes",
    "thin-shells",
    "progressive-plane",
    "A2",
    "residual-statistics",
    "cross-scale-validation",
    "falsification"
  ],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-PRIME-FACTOR-SEMIPRIME-SHELL-RESIDUAL-VALIDATION",
  "parent_objective_id": "PROGRESSIVE_PLANE_PRIME_SEMIPRIME_COORDINATE_DISCOVERY",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "PFSSV",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "NEW_DIRECTION",
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

# Prime-Factor Semiprime Shell Residual Validation on the Progressive Plane

Status: `PUBLISHED_REGISTERED / RESEARCHER-PUBLISHED / FALSIFICATION-FIRST`

## Mother question

Let a semiprime be \(n=pq\) with primes \(p\le q\), including \(p=q\). Encode the factor pair by the nonnegative min-zero triple

\[
D(n)=(p,q,0)
\]

and, for visualization only, by its full coordinate-permutation orbit

\[
\mathcal O(n)=S_3\cdot(p,q,0).
\]

For thin multiplicative shells

\[
\mathcal S_{X,\eta}
=
\{pq:\ p\le q,\ p,q\ \text{prime},\ X<pq\le (1+\eta)X\},
\]

determine whether the resulting factor-coordinate occupancy has any reproducible cross-scale residual structure that is not already explained by small prime factors, the boundary \(pq\approx X\), prime-density variation, or elementary residue-class restrictions.

The task is explicitly allowed to return a negative result. A visually striking raw six-wing picture is not itself evidence of a new arithmetic law.

## Frozen inputs and scope

Primary data are exact integer prime-factor pairs \((p,q)\); no floating-point primality or probabilistic factorization is allowed in the reference dataset.

Use these discovery scales:

\[
X\in\{10^5,\ 3\cdot10^5,\ 10^6,\ 3\cdot10^6,\ 10^7\},
\]

and these holdout scales, which must not be inspected until the primary statistics and phase/sign rules are frozen:

\[
X\in\{3\cdot10^7,\ 10^8\}.
\]

Use shell widths

\[
\eta\in\{10^{-2},\ 3\cdot10^{-3},\ 10^{-3}\}.
\]

Run all of the following primary views:

1. raw factor coordinates \((p,q)\) and their \(S_3\)-orbit visualization;
2. small-factor trim \(p>31\);
3. scale trim \(p>X^{1/4}\);
4. prime-rank coordinates \((\pi(p),\pi(q))\);
5. a density-flattened factor-balance coordinate based on \(u=\log p/\log X\), with the exact transform frozen before holdout inspection.

At minimum, control separately for:

- fixed small-prime channels \(p=2,3,5,7,\ldots\);
- the multiplicative shell boundary;
- the diagonal square locus \(p=q\);
- mod-\(30\) and, if needed by a detected effect, mod-\(210\) admissible residue classes;
- first-order local prime-density variation.

The \(S_3\) orbit is a derived diagnostic representation only. Do not reinterpret the experiment as changing the native ontology of the current relational plane.

Secondary colorings such as next-prime gap, semiprime gap, carry, holonomy, or Prime Fusion phase are outside the primary success gate. They may be recorded only after the occupancy test is frozen, and they cannot rescue a failed primary result.

## Hard target and required outputs

Hard target:

`SEMIPRIME_FACTOR_SHELL_CROSS_SCALE_RESIDUAL_STRUCTURE_VALIDATED_OR_REFUTED`.

Required outputs:

1. an exact-integer generator for all shell factor pairs and an independent recomputation path for spot checks;
2. a machine-readable experiment manifest that freezes discovery scales, holdout scales, shell widths, trims, binning, transforms, primary statistics, and null procedures before holdout inspection;
3. raw and corrected occupancy summaries for every \((X,\eta)\);
4. at least two independent null families:
   - one local-density null matched to the observed prime counts in coarse logarithmic bands and admissible residue classes;
   - one structure-destroying surrogate that preserves one-dimensional prime-gap or factor-margin information while breaking cross-scale phase coherence;
5. a cross-scale residual profile in a fixed normalized factor coordinate, together with signed phase/correlation statistics across discovery scales;
6. a max-statistic or equivalent family-wise empirical threshold from the null ensembles, so the result is not selected from whichever bin happens to look best;
7. a blind holdout evaluation on \(3\cdot10^7\) and \(10^8\) using the already-frozen statistic and sign/phase rule;
8. a return report that classifies the strongest result into one of the terminal classes below and includes exact counts, effect sizes, null ranks, and failure modes.

Figures are diagnostic output, not the acceptance criterion.

## Research value to preserve

This experiment separates two very different possibilities.

The first is that the apparent factor-coordinate geometry is only a repackaging of known multiplicative facts: small primes create the wings, \(pq\approx X\) creates the shell curve, prime squares create a diagonal ridge, and residue classes create periodic texture.

The second is that, after those effects are removed and coordinates are density-normalized, a signed residual feature remains aligned across scales. Such a survivor would be a concrete new object: a scale-stable residual statistic attached to semiprime factor shells on the current three-carrier representation. It could then be compared with prime gaps, carry/holonomy, or Prime Fusion channels in a later task without contaminating this primary test.

A clean negative result is equally valuable because it kills the naive occupancy route and prevents repeated rediscovery of deterministic small-factor artifacts.

## Success, kill, and return criteria

Return `CROSS_SCALE_RESIDUAL_CANDIDATE` only if one predeclared residual feature satisfies all of the following:

- it has the same sign and compatible normalized location on at least four of the five discovery scales;
- it appears for at least two of the three shell widths;
- it survives both \(p>31\) and \(p>X^{1/4}\) trims, or the return explicitly proves why one trim removes signal rather than only background;
- it remains present in prime-rank or density-flattened coordinates rather than existing only in raw prime magnitudes;
- it exceeds the predeclared family-wise empirical threshold under both null families;
- the already-frozen feature reproduces with the same sign/phase on both holdout scales.

Return `DETERMINISTIC_SMALL_FACTOR_ARTIFACT` if the apparent geometry is explained by fixed small-prime channels or disappears under the registered trims.

Return `RESIDUE_OR_DENSITY_ARTIFACT` if the residual is accounted for by admissible residue classes, shell geometry, or local prime density.

Return `NO_STABLE_RESIDUAL_STRUCTURE_AT_TESTED_SCALES` if no feature survives the full discovery-plus-holdout gate.

A candidate result is empirical and does not by itself establish an all-scale theorem, a prime-generating law, or a factorization shortcut. Freeze the strongest reproducible residual or the strongest negative decomposition and return at task scope.
