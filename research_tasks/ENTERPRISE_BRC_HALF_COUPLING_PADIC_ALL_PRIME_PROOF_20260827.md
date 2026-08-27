<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-ENTERPRISE-BRC-HALF-COUPLING-PADIC-ALL-PRIME-PROOF",
  "title": "Enterprise BRC Half-Coupling p-adic All-Prime Proof",
  "kind": "RESEARCH",
  "owner": "research/enterprise-brc-half-padic-all-prime-proof",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "Prove or exactly refute, for every prime p>3, the mod-p^3 congruence for the half-coupling weighted Enterprise kernel that survived the preregistered clean-room blind test, without using finite computation as proof.",
  "next_action": "Start from the exact binomial/hypergeometric form of S_p, audit the Sun A14(ii) conjectural refinement and the Beukers modular-form framework, then pursue at least two structurally distinct exact proof lanes until one closes the all-prime mod-p^3 theorem or yields an exact obstruction/counterexample.",
  "dependencies": [
    "research_tasks/ENTERPRISE_BRC_HALF_COUPLING_BLIND_PADIC_FINGERPRINT_20260826.md@e41eb88014573f1ba47d726c27cc4d0b085239ba",
    "research_result_records/RS-ENTERPRISE-BRC-HALF-COUPLING-BLIND-PADIC-FINGERPRINT/RR-555C18BA67F41C218B86.json@feb976e6644315c43447fed247f8aefc95276596",
    "research_artifacts/ENTERPRISE_BRC_HALF_COUPLING_BLIND_PADIC_FINGERPRINT_20260826/independent_audit_20260827.json@feb976e6644315c43447fed247f8aefc95276596"
  ],
  "source_refs": [
    "Zhi-Wei Sun, Open Conjectures on Congruences, arXiv:0911.5665, Conjecture A14(ii)",
    "Frits Beukers, Supercongruences using modular forms, arXiv:2403.03301",
    "research_returns/ENTERPRISE_BRC_HALF_COUPLING_BLIND_PADIC_FINGERPRINT_RETURN_20260826.md@feb976e6644315c43447fed247f8aefc95276596"
  ],
  "evidence_status": "NONBLIND_EXACT_PROOF_TASK / PARENT_BLIND_PASS_VERIFIED_AS_FINITE_EVIDENCE / ALL_PRIME_THEOREM_UNPROVED",
  "last_progress_ref": "External clean-room run and independent intake audit verified the preregistered m=2 character law on all discovery and untouched holdout primes; a third exact implementation reproduced all 132 preregistered residues, while the all-prime statement remained unproved. User directed issuance of the exact-proof successor task.",
  "last_progress_at": "2026-08-27T08:08:00+08:00",
  "hard_block": null,
  "tags": [
    "p-adic",
    "supercongruence",
    "all-prime-proof",
    "hypergeometric",
    "modular-forms",
    "creative-telescoping",
    "half-coupling",
    "exact-proof"
  ],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-ENTERPRISE-BRC-HALF-COUPLING-PADIC-ALL-PRIME-PROOF",
  "parent_objective_id": "ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "EBP2",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-ENTERPRISE-BRC-HALF-COUPLING-BLIND-PADIC-FINGERPRINT",
  "successor_gate": {
    "new_information_gap": "The clean-room blind experiment establishes a strong finite arithmetic fingerprint but does not prove the congruence for every prime p>3.",
    "why_parent_result_does_not_close_it": "The parent return is explicitly FINITE_COMPUTATIONAL_EVIDENCE_ONLY; Sun A14(ii) is a prior conjectural refinement, and the modular-form framework has not yet been specialized into a complete proof of this exact weighted p-term truncation.",
    "discriminating_outcomes": [
      "A complete proof for every prime p>3 modulo p^3.",
      "An exact counterexample that refutes the target.",
      "A rigorous proof on a proper prime congruence class together with a sharply identified unresolved complementary class.",
      "An exact route-specific obstruction that rules out a proposed proof mechanism without refuting the theorem."
    ],
    "kill_condition": "Any exact prime p>3 violating the target immediately refutes the theorem. A framework citation whose hypotheses or specialization are not proved for this exact sum is not accepted as closure and that route must be killed or repaired.",
    "alternative_route_or_free_exploration_considered": "Closure at finite evidence was considered and rejected because the new gap is theorem-level. Independent alternatives include p-adic hypergeometric/gamma methods, finite-field hypergeometric and CM methods, WZ or creative telescoping, modular parametrization, and direct binomial-harmonic congruence methods; free exploration remains available if all scoped proof lanes expose genuine obstructions.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "The parent task was a preregistered blind experiment whose evidentiary protocol must remain frozen. The present work is intentionally nonblind, literature-aware, and theorem-strength, so it requires a separate owner, proof contract, and return boundary rather than mutating the completed blind task."
  },
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:aad427281b91d39273ba54d3f3d5779600ff28f651927cc9b44c20d6694acb58",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# Enterprise BRC Half-Coupling p-adic All-Prime Proof

Status: `PUBLISHED_REGISTERED / DIRECT_USER_DIRECTION / CONTINUATION / EXACT_PROOF`

## Mother question

For every prime `p > 3`, prove or exactly refute

\[
S_p
=
\sum_{n=0}^{p-1}
(6n+1)
\frac{(2n)!(3n)!}{(n!)^5\,216^n}
\equiv
p\left(\frac{-3}{p}\right)
\pmod{p^3}.
\]

Here `((-3)/p)` is the Legendre symbol. The target is an all-prime arithmetic theorem. Finite computation, however extensive, is regression evidence only and cannot close the task.

The primary mathematical question is therefore:

> Does the weighted `216` truncation satisfy the exact `p * chi_{-3}(p)` congruence modulo `p^3` for every prime `p>3`, and if so what exact mechanism forces it?

## Frozen inputs and scope

### Exact target objects

For `n >= 0`, define

\[
A_n=\frac{(2n)!(3n)!}{(n!)^5}.
\]

For prime `p>3` define, in `Z/(p^3)Z`,

\[
S_p=\sum_{n=0}^{p-1}(6n+1)A_n\,216^{-n}.
\]

Since `p>3`, `216` is invertible modulo `p^3`.

The following exact identities may be used after verifying them algebraically:

\[
A_n=\binom{2n}{n}^2\binom{3n}{n},
\]

and

\[
A_n
=
108^n
\frac{(1/2)_n(1/3)_n(2/3)_n}{(n!)^3}.
\]

Thus the half-coupling denominator converts the summand to a weighted truncated order-3 hypergeometric object at argument `1/2`.

For primes `p>3` one may also use the exact character identity

\[
\left(\frac{-3}{p}\right)=\left(\frac{p}{3}\right).
\]

### Parent evidence and its status

The predecessor blind task and its clean-room intake audit are admissible as motivation, regression evidence, and a source of exact finite vectors. Their theorem status is frozen as finite only.

The audited predecessor reported:

- discovery law `(k,c,d)=(1,1,-3)` for `m=2`;
- `HOLDOUT_PASS` on every untouched holdout prime;
- no preregistered character law for controls `m=3,4`;
- a third independent exact replay with `132/132` preregistered residues matching;
- post-freeze finite evidence consistent with the stronger mod-`p^3` target.

None of those finite checks may be cited as proof of the all-prime statement.

### Prior art that must be audited, not merely cited

The researcher may use the literature without a blind firewall.

At minimum, audit:

1. Zhi-Wei Sun, *Open Conjectures on Congruences*, arXiv:0911.5665, Conjecture A14(ii). Its `a=1` specialization is a stronger conjectural refinement modulo `p^4`; determine exactly what it implies and what remains conjectural.
2. Frits Beukers, *Supercongruences using modular forms*, arXiv:2403.03301. Determine whether the general modular-form machinery actually specializes to this exact coefficient system, CM value, weight `(6n+1)`, truncation `0..p-1`, and modulus `p^3`.

A theorem name, framework, or nearby formula is not sufficient. Every imported result must have its hypotheses and specialization checked line by line.

### Proof lanes

The researcher is free to combine methods, but must seriously pursue at least two structurally distinct lanes before returning `PROOF_NOT_CLOSED` unless one lane already yields a complete proof or an exact counterexample.

Preferred lanes are:

**Lane A — p-adic hypergeometric / Gamma / Dwork.**  
Rewrite the truncation as a hypergeometric quantity, control the weighted derivative/operator producing `(6n+1)`, and account explicitly for every power of `p` through modulus `p^3`.

**Lane B — modular form / CM specialization.**  
Identify the precise modular parametrization at the relevant CM point, prove the finite truncation congruence from the modular object, and derive the quadratic character without assuming the desired conclusion.

**Lane C — WZ / creative telescoping.**  
Seek a finite identity or parameter deformation whose telescoping boundary terms are explicitly divisible by the required powers of `p`.

**Lane D — direct binomial-harmonic congruences.**  
Split the summation by `p`-adic valuation, expand factorial/binomial ratios to sufficient order, and reduce to explicit harmonic or character sums.

**Lane E — finite-field hypergeometric / character sums.**  
If used, the bridge from finite-field objects back to the exact truncated classical sum must itself be proved to the required precision.

The researcher may introduce a stronger modulo-`p^4` statement if it genuinely simplifies the proof, but the present task is closed only when the stated modulo-`p^3` target is rigorously settled.

### Exclusions

Do not:

- infer an all-prime theorem from any finite prime range;
- treat Sun A14(ii) as a proved theorem unless an actual proof is located and its exact specialization is verified;
- infer the arithmetic congruence from the infinite Ramanujan-type real series alone;
- replace the weighted `p`-term truncation by an unweighted or differently truncated sum;
- silently discard primes in one residue class modulo `3`;
- claim arithmetic novelty without a dedicated prior-art audit;
- promote the arithmetic result to a physical, BRC, packet/path, or Foundation theorem inside this task.

## Hard target and required outputs

Hard target:

`ENTERPRISE_BRC_HALF_COUPLING_PADIC_MOD_P3_ALL_PRIMES_PROVED_OR_REFUTED`

Required outputs:

1. A precise theorem statement for all primes `p>3`, or an exact counterexample/refutation.
2. A complete human-auditable proof if the theorem survives.
3. An explicit dependency map listing every imported theorem and the exact hypotheses used.
4. A separate treatment of the `p ≡ 1 (mod 3)` and `p ≡ 2 (mod 3)` character cases whenever the proof mechanism distinguishes them.
5. Full `p`-adic precision bookkeeping showing why all discarded terms vanish modulo `p^3`.
6. For any modular/hypergeometric framework, a written specialization from the general statement to this exact `A_n`, weight `(6n+1)`, denominator `216^n`, truncation `n=0..p-1`, and character `((-3)/p)`.
7. A deterministic exact-integer checker retained only as regression support for the final formula and critical intermediate lemmas.
8. A prior-art classification separating: already proved theorem, previously conjectured statement, new proof if any, and any stronger unproved refinement.
9. If only a restricted prime class is proved, the exact complementary class and the first unresolved lemma must be isolated.
10. A durable return at `research_returns/ENTERPRISE_BRC_HALF_COUPLING_PADIC_ALL_PRIME_PROOF_RETURN_20260827.md`.

A proof is not complete if its central step is stated only as “follows from standard supercongruence machinery,” “by modularity,” “by a known hypergeometric transformation,” or equivalent without an exact theorem reference or self-contained derivation.

## Research value to preserve

The predecessor blind experiment established that the half-coupling sample has a sharply different finite p-adic fingerprint from its preregistered controls. The unresolved question is no longer whether a pattern can be detected, but whether the pattern is forced for every prime.

This task is valuable on all outcomes:

- a complete proof converts finite cross-domain evidence into an exact arithmetic theorem;
- a counterexample cleanly kills the all-prime interpretation;
- a restricted-class proof identifies the precise arithmetic symmetry responsible for part of the phenomenon;
- an exact obstruction to a modular, WZ, or p-adic route prevents repeated false closures and narrows the next proof search.

The proof task does not depend on any physical interpretation of half-coupling. Even if the Enterprise interpretation is later revised, the arithmetic theorem remains independently meaningful.

## Success, kill, and return criteria

Freeze exactly one primary task verdict:

- `ALL_PRIME_MOD_P3_PROVED` — a complete proof is obtained for every prime `p>3`.
- `TARGET_REFUTED` — an exact prime counterexample is produced and independently checked.
- `KNOWN_THEOREM_SPECIALIZATION_PROVED` — a previously proved theorem is located and its hypotheses are rigorously specialized to yield the exact target; this counts as theorem closure but not proof novelty.
- `RESTRICTED_PRIME_CLASS_PROVED` — a proper infinite prime class is proved but the all-prime theorem remains open; the complementary class must be explicit.
- `PROOF_ROUTE_EXACT_NO_GO` — one or more serious proof lanes are ruled out by exact obstructions, but the theorem itself is neither proved nor refuted.
- `PROOF_NOT_CLOSED` — all scoped lanes are exhausted without theorem closure, with the smallest exact unresolved lemma frozen.

Immediate kill/refutation rule:

If any prime `p>3` is found with

\[
S_p\not\equiv p\left(\frac{-3}{p}\right)\pmod{p^3},
\]

recompute it by a second exact method, freeze the exact residue and summation data, and return `TARGET_REFUTED`.

Proof acceptance rule:

`ALL_PRIME_MOD_P3_PROVED` or `KNOWN_THEOREM_SPECIALIZATION_PROVED` requires a complete chain of exact implications. Numerical agreement, heuristic modular matching, symbolic pattern recognition, or a conjectural literature statement is insufficient.

Restricted-result rule:

A proof for only `p ≡ 1 (mod 3)` or only `p ≡ 2 (mod 3)` is valuable but must not be relabeled all-prime. Continue into the complementary class unless a genuine exact blocker remains.

Return rule:

The task may stop only with the strongest exact statement reached, a precise proof-status classification, and a smallest unresolved lemma or exact refutation where applicable. No physical or Foundation interpretation is part of the terminal criterion.
