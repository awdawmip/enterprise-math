# Conjecture Asset Governance

Status: `ACTIVE_CANONICAL_GOVERNANCE`
Effective: `2026-09-06`
Scope: `awdawmip/enterprise-math`

## Purpose

Enterprise Math explicitly permits useful unproved mathematical statements and unproved tool contracts to be registered and used during exploration without being mistaken for proved truth.

The governing principle is:

> Conjectures may participate in the discovery loop, but they may not masquerade as proof. Use first when useful; prove later; preserve the dependency taint until proof is discharged.

This policy supplements, and does not replace, `research_axiom_candidate_state_machine.json`, `research_result_contract.json`, `research_architecture.json`, `enterprise_toolbox_registry.json`, or Foundation/canonical promotion gates.

## Asset classes

### 1. Conjectural theorem

`CONJECTURAL_THEOREM` is a precise, falsifiable mathematical statement whose stated scope is not yet proved.

It may have finite, numerical, heuristic, literature-analogue, or exact bounded evidence. None of those enlarge the statement beyond the recorded claim scope.

### 2. Conjectural tool

`CONJECTURAL_TOOL` is a reusable input/output transformation, criterion, estimator, reduction, certificate procedure, or model adapter whose soundness or advertised scope depends on at least one unproved mathematical claim.

A conjectural tool must still satisfy the ordinary Enterprise tool-shape requirements: reusable input/output, a structural law or certificate target, an explicit failure boundary, and a meaningful reuse target. It is routed separately from `enterprise_toolbox_registry.json` until its conjectural dependencies are discharged and ordinary tool acceptance occurs.

### 3. Objects that are not conjectures

Do not force the following into the conjecture registry:

- an open question with no asserted direction;
- a theorem or identity already proved, even if its Enterprise implementation is missing;
- an exact algorithm whose correctness is proved but whose performance/usefulness is still experimental;
- a candidate tool based entirely on established mathematics that merely awaits implementation/reviewer acceptance;
- a raw axiom candidate governed by `research_axiom_candidate_state_machine.json`;
- a numerical observation that has not yet been formulated as a precise claim.

These remain open problems, implementation/tool candidates, axiom candidates, or empirical findings as appropriate.

## Epistemic states

Every conjecture asset has one primary `epistemic_status`:

- `CONJECTURE`: unproved; evidence may exist but does not certify the full claim scope.
- `EMPIRICALLY_VALIDATED`: the claim has passed a declared, reproducible validation envelope strong enough to support exploratory reuse, but no proof covers the full claim scope.
- `PROVED`: a proof/certificate covers the exact registered claim scope and has passed the applicable Enterprise review/promotion gate.

Lifecycle state is separate:

- `ACTIVE`
- `RESTRICTED`
- `REFUTED`
- `SUPERSEDED`
- `PARKED`

A restriction narrows the valid claim/tool envelope; it does not silently rewrite history. Supersession points to the replacement asset.

## Evidence typing

Every validation record must say which of the following it is:

- `EXACT_BOUNDED_EXHAUSTIVE`
- `EXACT_BOUNDED_SAMPLED`
- `INTERVAL_CERTIFIED_NUMERICAL`
- `FLOATING_NUMERICAL`
- `SYMBOLIC_DERIVATION_PARTIAL`
- `HEURISTIC_MODEL`
- `INDEPENDENT_REPLICATION`
- `LITERATURE_ANALOGUE`
- `COUNTEREXAMPLE`

Discovery evidence and independent validation evidence remain distinct, consistent with the existing axiom-candidate governance.

## Bounded proof rule

If an asset's statement is explicitly finite/bounded and its entire stated domain is exhaustively verified by a replayable exact certificate/checker, the bounded statement itself may become `PROVED`.

This never proves an unstated infinite/asymptotic extension.

Example:

`P(n) holds for every 1 <= n <= 10^8`

may be proved by an exact exhaustive certificate over that whole range. It does not establish

`P(n) holds for every n`.

## Conjectural dependency propagation

This is the central invariant.

For any theorem, tool, result, or downstream conjecture `X`, let `C(X)` be the transitive set of unresolved conjectural dependencies.

`X` may be called unconditionally proved only if:

1. its own derivation/proof obligations are discharged; and
2. every member of `C(X)` is `PROVED` for the exact scope used.

If the derivation of `X` is rigorous conditional on conjecture `C`, record it as `CONDITIONALLY_PROVED_ON(C)` or the equivalent typed dependency state. Do not relabel it `PROVED`.

Empirical success never clears conjectural dependency taint.

When a conjecture becomes `PROVED`, re-evaluate downstream assets. Do not auto-promote them if their own proof obligations remain open.

When a conjecture becomes `REFUTED` or `RESTRICTED`, every downstream asset that used the invalidated scope becomes `REVIEW_REQUIRED` until re-derived, restricted, or retired.

## Call policy

### Conjectural theorem

May be used:

- to derive conditional theorems;
- to select experiments, targets, coordinates, and proof strategies;
- to generate candidate algorithms/tools;
- to prioritize proof work.

Every substantive downstream use must preserve its asset ID in provenance/dependencies.

### Conjectural tool

May be invoked during research before proof, provided each invocation records:

- conjectural tool ID and version;
- exact input scope;
- whether the input lies inside the validated envelope;
- conjectural dependencies;
- output disposition: `EXPLORATORY_ONLY`, `CONDITIONAL_RESULT`, or `BOUNDED_CERTIFIED_RESULT` when an independent exact certificate verifies that particular output.

Outside the validated envelope, use is always `EXPLORATORY_ONLY` unless a separate exact certificate closes the particular result.

A conjectural tool is never silently inserted into `enterprise_toolbox_registry.json`.

## Registration minimum

A new conjecture asset must contain:

- stable ID;
- kind;
- title;
- precise statement or tool contract;
- claim/soundness scope;
- epistemic status and lifecycle status;
- proved and conjectural dependencies;
- validation envelope and evidence type;
- known counterexamples/failure regions;
- source/provenance references;
- downstream references when known;
- falsifier/kill condition;
- proof or promotion target;
- priority metadata;
- version and dates.

IDs are never reused:

- conjectural theorem: `CJ-TH-YYYYMMDD-NNN`
- conjectural tool: `CJ-TL-YYYYMMDD-NNN`

## Scan and backfill protocol

The conjecture scanner has three duties.

### A. Historical backfill

Scan prior research records, notes, journals, findings and durable frontiers for markers such as:

`HYPOTHESIS`, `TESTING`, `empirical`, `numerical`, `conjecture`, `candidate law`, `expected`, `appears`, `suggests`, `frontier`, `unproved`, `not proved`, `smallest unresolved unit`, and precise directional research targets.

For every hit:

1. identify the strongest precise asserted claim actually supported by the source;
2. separate proved lemmas from the unproved residue;
3. reject mere open questions or implementation gaps from conjecture intake;
4. register the conjecture only if a falsifiable statement/tool contract can be frozen;
5. retain exact source references and validation boundaries;
6. record supersession/restriction when later research already weakened the original form.

### B. Research-closeout scan

Every substantial research closeout should inspect `unresolved_residue`, `method_harvest`, proposed laws, empirical regularities and tool proposals for conjecture candidates. Registration must not delay the research return, but durable conjecture candidates should not be left orphaned.

### C. Dependency revalidation

Whenever a conjecture changes epistemic/lifecycle state, traverse recorded downstream dependencies and mark affected assets for upgrade or review.

## Priority for proving conjectures

Proof work is prioritized by a transparent combination of:

1. downstream impact / number and importance of dependent results;
2. empirical stability inside the validated envelope;
3. structural centrality (for example BRC/native-coordinate bridge value);
4. expected proof cost;
5. falsification risk and cost of continuing to depend on the claim.

High-use conjectures are not treated as more true; they are treated as more urgent to prove or kill.

## Relationship to ordinary tools and Working Truth

`enterprise_toolbox_registry.json` remains the router for accepted ordinary tools. A conjectural tool lives in `conjecture_registry.json` until its conjectural soundness dependencies are discharged and the existing tool acceptance/reviewer gates approve promotion.

Conjecture registration does not grant Foundation status, canonical theorem status, or Working Truth automatically. Exact task semantics or explicit Driver direction may permit a conjecture to be used as a temporary working assumption, but the conjectural provenance tag remains mandatory.

## Scanner ownership

Historical and closeout conjecture scanning is an explicit research-governance responsibility. The scanner may register, restrict, supersede, or flag conjectures for proof review, but it may not upgrade an asset to `PROVED` without the applicable evidence/review gate.
