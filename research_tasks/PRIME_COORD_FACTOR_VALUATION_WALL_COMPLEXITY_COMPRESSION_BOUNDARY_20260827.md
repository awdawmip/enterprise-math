<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-PRIME-COORD-FACTOR-VALUATION-WALL-COMPLEXITY-COMPRESSION-BOUNDARY",
  "title": "Prime Coordinate Factor Valuation-Wall Complexity Compression Boundary",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "Determine whether the exact N-only valuation-wall splitter can be evaluated asymptotically faster than its current Theta(p) streaming recurrence, or freeze the precise classical-equivalence or scoped lower-bound barrier that prevents a genuine speedup.",
  "next_action": "Audit existing factorial/product-tree and deterministic factoring methods, formalize the admissible cost model, then try to replace sequential A_s recurrence by an exact public fast-index evaluator while proving every modular division legal or factor-revealing.",
  "dependencies": [
    "research_result_records/RS-PRIME-COORD-FACTOR-NONLY-VALUATION-WALL-GCD-EXTRACTOR-INDEPENDENT-REPLAY/RR-F24971D684C868A325E2.json@cc0106285c579998747c3e777c11c35a3304a274"
  ],
  "source_refs": [
    "research_tasks/PRIME_COORD_FACTOR_NONLY_VALUATION_WALL_GCD_EXTRACTOR_INDEPENDENT_REPLAY_20260827.md@cc0106285c579998747c3e777c11c35a3304a274",
    "research_returns/PRIME_COORD_FACTOR_NONLY_VALUATION_WALL_GCD_EXTRACTOR_INDEPENDENT_REPLAY_RETURN_20260827.md@cc0106285c579998747c3e777c11c35a3304a274",
    "scripts/check_prime_coord_factor_nonly_valuation_wall_replay.py@cc0106285c579998747c3e777c11c35a3304a274"
  ],
  "evidence_status": "PCF4R_EXACT_N_ONLY_GCD_EXTRACTOR_VERIFIED / NO_SPEEDUP_CLAIM / THETA_P_STREAMING_FRONTIER_OPEN",
  "last_progress_ref": "RR-F24971D684C868A325E2 closes exact extractor existence on distinct odd semiprimes with 3<p<q; the remaining algorithmic residue is asymptotic access to the valuation wall.",
  "last_progress_at": "2026-08-27T12:10:00+00:00",
  "hard_block": null,
  "tags": [
    "prime-coordinate",
    "factorization",
    "n-only",
    "valuation-wall",
    "complexity",
    "fast-factorial",
    "pcf5"
  ],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-PRIME-COORD-FACTOR-VALUATION-WALL-COMPLEXITY-COMPRESSION-BOUNDARY",
  "parent_objective_id": "ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "PCF5",
  "origin_kind": "DRIVER_ROADMAP",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-PRIME-COORD-FACTOR-NONLY-VALUATION-WALL-GCD-EXTRACTOR-INDEPENDENT-REPLAY",
  "successor_gate": {
    "new_information_gap": "The parent proves exact factor extraction but only with a streaming recurrence whose worst-case seed scale is Theta(p); it does not decide whether A_s mod N can be accessed at public dyadic/fallback indices in o(p) work.",
    "why_parent_result_does_not_close_it": "The parent explicitly freezes NO_SPEEDUP_CLAIM and treats complexity compression as outside its hard target.",
    "discriminating_outcomes": "Produce a rigorously faster exact N-only evaluator and composed splitter, prove equivalence to a known deterministic factorial-factorization method with no new asymptotic advantage, or prove a lower bound for a precisely stated admissible algorithm class.",
    "kill_condition": "Reject any claimed compression that uses hidden factors, factor-derived tuning, unproved division by a possible nonunit, prime scanning disguised as indexing, constant-factor timing only, or an unscoped claim of a universal factoring lower bound.",
    "alternative_route_or_free_exploration_considered": "The sealed benchmark is already a separate active program task and larger finite semiprime scans add little. Lean formalization and broader prime-coordinate exploration remain separate portfolio options.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "Extractor existence is terminally closed at the parent scope; asymptotic evaluation is a new algorithmic question with different success criteria and can be killed independently by classical-equivalence or model-barrier evidence."
  },
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:b78f85af4629ddb714870c44535ad0393418dbc3bebe06da142a90c0c6b9075e",
    "review_state": "PASS",
    "temporary_overrides": []
  },
  "program_id": "PRIME_COORD_FACTOR_EXTRACTION_PROGRAM_20260827",
  "requested_risk_tier": "CRITICAL"
}
-->

# Prime Coordinate Factor Valuation-Wall Complexity Compression Boundary

Status: `PUBLISHED_REGISTERED / READY / PCF5 COMPLEXITY BOUNDARY`

## Mother question

The accepted parent result gives, for every distinct odd semiprime

\[
N=pq,\qquad 3<p<q,
\]

an exact factor-blind splitter built from

\[
A_s=\frac{(2s)!(3s)!}{(s!)^5}
=\binom{2s}{s}^2\binom{3s}{s},
\]

public dyadic probes, gcd, and the synchronized fallback near \(\sqrt N/3\).

Its current implementation reaches the first factor-bearing wall by streaming \(A_s\bmod N\) through \(\Theta(p)\) recurrence steps in the worst case. Can the same exact N-only mechanism be evaluated at the needed public indices in asymptotically less work, or is the apparent improvement exactly a repackaging of a known factorial-factorization method or a route blocked in a precisely defined algorithm model?

## Frozen inputs and scope

Treat `RR-F24971D684C868A325E2` as the accepted theorem-level input at exactly its stated scope. Preserve simultaneously the earlier fixed-public-prefix no-go: the present task may use indices that depend on `N`, but no constructor step may read `p`, `q`, a factor-labelled coordinate, a factor-derived phase, or a tuning parameter chosen after the hidden factorization is known.

Use

\[
n=\lceil\log_2 N\rceil
\]

for bit complexity. The hidden smaller factor \(p\) may appear in proofs and complexity upper/lower bounds, never as constructor input.

Before inventing a new general mechanism, audit current internal method coverage and standard exact factorial/product-tree, blocked-product, multipoint-evaluation, baby-step/giant-step, and deterministic factoring methods. A rediscovery is a valid result if the equivalence is proved and the asymptotic boundary is stated correctly.

Separate three algorithm classes rather than mixing them:

1. sequential recurrence access to every \(A_1,\ldots,A_s\);
2. exact random-index evaluation of \(A_s\bmod N\) or of an equivalent numerator/denominator product;
3. the full public splitter, including dyadic detection, the synchronized fallback, gcd checks and any preprocessing.

Every modular division must be justified as division by a unit. If a denominator or interpolation factor is a nonunit, the algorithm must either extract the resulting gcd exactly or stop with an explicit admissibility failure. Do not silently assume field arithmetic over \(\mathbb Z/N\mathbb Z\).

Wall-clock timing, memory reduction, or replacing \(O(p)\) recurrence steps by \(O(p)\) product work does not count as asymptotic compression.

## Hard target and required outputs

Hard target: `VALUATION_WALL_COMPLEXITY_COMPRESSED_OR_CLASSICAL_EQUIVALENCE_OR_SCOPED_BARRIER_PROVED`.

Required outputs:

1. a precise algebraic and bit-complexity model for the three access classes above;
2. an exact derivation of the sequential baseline and its unavoidable first factor-bearing index inside that restricted model;
3. an attempt to construct a public fast-index evaluator for \(A_s\bmod N\), preferably by blocked products or polynomial evaluation, with a proof of correctness over the composite modulus;
4. a complete accounting of all gcds, inversions, preprocessing, product-tree or multipoint costs, including what happens when an intermediate quantity is a nonunit;
5. composition with the parent dyadic/fallback theorem to obtain the strongest proved total splitter complexity;
6. a genuine compression threshold: any positive speedup verdict must prove \(O(p^{1-\delta}\operatorname{poly}(n))\) work for some explicit \(\delta>0\), or a stronger bound, rather than a constant-factor improvement;
7. a current prior-art comparison sufficient to decide whether the construction is asymptotically new, equivalent to a known deterministic factorial-factorization route, or weaker;
8. an independently written exact checker that cross-checks fast-index residues against direct bounded values and verifies every returned divisor by exact division;
9. a durable return at `research_returns/PRIME_COORD_FACTOR_VALUATION_WALL_COMPLEXITY_COMPRESSION_BOUNDARY_RETURN_20260827.md`.

If a fast evaluator is found but the composed method remains exponential in \(n\), state the exact exponent and do not call it polynomial-time factoring.

## Research value to preserve

The parent result changed the question from “is there a factor-blind observable that deterministically breaks every promised semiprime?” to “can that observable be reached cheaply enough to matter algorithmically?”

That distinction is decisive. An \(o(p)\) exact evaluator would convert the current theorem into a quantitatively stronger deterministic factoring method. Conversely, a proved equivalence to a known factorial method, or a clean lower bound for a well-defined access model, would prevent the coordinate program from mistaking an exact extraction theorem for a computational breakthrough.

The most valuable outcome is therefore not necessarily a faster algorithm; it is a sharp complexity classification that survives hidden-factor leakage checks and separates genuine new leverage from classical arithmetic already present in another form.

## Success, kill, and return criteria

Freeze exactly one strongest primary verdict:

- `VALUATION_WALL_COMPLEXITY_COMPRESSED` — a public exact splitter beats the \(\Theta(p)\) recurrence scale by a proved asymptotic factor and all composite-modulus operations are legal or factor-revealing;
- `CLASSICAL_FACTORIAL_METHOD_EQUIVALENCE_FROZEN` — the best valid compression is proved asymptotically equivalent to an already known deterministic factorial/product method, with no unsupported novelty claim;
- `SEQUENTIAL_MODEL_BARRIER_PROVED_FAST_INDEX_OPEN` — an \(\Omega(p)\) barrier is proved for sequential recurrence access but random-index acceleration remains unresolved;
- `SCOPED_FAST_INDEX_BARRIER_PROVED` — a lower bound is proved for an explicitly stated stronger evaluator class without claiming a universal factoring lower bound;
- `NO_PROGRESS_WITH_EXACT_BLOCKER` — no compression or barrier is closed, but the smallest exact obstruction is isolated.

Kill any candidate immediately if it requires the hidden factors to choose block size or probe location, smuggles a prime scan into preprocessing, assumes arbitrary inverses modulo `N`, proves only finite timing improvements, or compares costs under inconsistent arithmetic models.

Bounded computation is regression only. A positive asymptotic verdict requires proof. A negative lower-bound verdict must name the exact algorithm class it applies to. If prior-art comparison proves equivalence, freeze that equivalence rather than renaming the method.
