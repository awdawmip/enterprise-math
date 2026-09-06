# Conjecture historical backfill audit — generation 1

Status: `GOVERNANCE BACKFILL / NO THEOREM PROMOTION`
Date: `2026-09-06`
Registry: `conjecture_registry.json`
Contract: `conjecture_asset_contract.json`
Policy: `docs/CONJECTURE_ASSET_GOVERNANCE.md`

## Objective

Create the first durable historical conjecture inventory without converting empirical findings, open questions, theorem-backed implementation gaps, or raw axiom candidates into false mathematical conjectures.

This is a classification/backfill pass. It changes no mathematical proof status.

## Sources inspected in generation 1

The scan used the current Enterprise control plane together with recent durable mathematical records in `awdawmip/chatgpt-global-knowledge` and `awdawmip/enterprise-math`, including:

- `research_axiom_candidate_state_machine.json`;
- `research_result_contract.json`;
- `enterprise_toolbox_registry.json`;
- `research_architecture.json`;
- `knowledge/projects/enterprise-math/nt-rh-landau-widom-critical-repair-band-20260906.md`;
- `knowledge/projects/enterprise-math/nt-rh-shell-shannon-response-rank-20260906.md`;
- `knowledge/projects/enterprise-math/nt-rh-prime-boundary-reflection-frame-20260906.md`;
- `knowledge/projects/enterprise-math/nt-tool-wiener-hopf-phase-space-spectral-count-20260906.md`;
- `knowledge/projects/enterprise-math/pde-modulation-branch-dimension-frontier-20260906.md`;
- `knowledge/projects/enterprise-math/poincare-brc-q-qo-empirical-controls-20260906.md`;
- `knowledge/projects/enterprise-math/candidate-tool-digital-automatic-arithmetic-20260905.md`;
- `knowledge/projects/enterprise-math/candidate-tool-finite-character-spectral-20260905.md`;
- `research_notes/2026-09-06-1162-first-order-rotation-brc-frontier.md`;
- `research_notes/1162_theta_positivity_cm_gate_20260906.md`;
- `research_notes/1162_chi5_logcm_levy_injection_20260906.md`.

The global `knowledge/hypotheses/` directory was also checked and is not currently a complete Enterprise Math conjecture registry; recent explicit RH hypotheses were instead stored among project records.

## Registered conjecture assets

### `CJ-TH-20260906-001`

Old-eigenbasis Weil square-shell repair crossover has Landau-Widom order.

The original finite observation was already weakened by later response-SVD/inertia work, so the backfilled asset is born `RESTRICTED`: it applies only to the forced old-eigenbasis repair carrier. The stronger interpretation that optimal response rank equals `4 n^2 log n` is not registered.

### `CJ-TH-20260906-002`

Prime-dominated Weil response rank obeys a phase-space dangerous-region law.

This is the current replacement RH response-rank hypothesis: exact prime-frame reductions and classical Wiener-Hopf/Szego-Widom machinery exist, but the normalized RH response symbol/model and transfer bounds remain unproved.

### `CJ-TH-20260906-003`

Navier-Stokes phase-aware effective modulation dimension is at most one on the Enterprise closure route.

The fixed-modulation lattice-sphere and bilinear estimates are exact; the conjectural residue is the uniform aggregation/cancellation law `M_N <= C_epsilon N^(1+epsilon)` in the full typed interaction network.

### `CJ-TL-20260906-001`

Prime-response phase-space rank predictor.

The generic Wiener-Hopf/Szego-Widom theorem family is not conjectural. The conjectural tool is only the RH-specific adapter that predicts response rank from a candidate normalized prime-dominated symbol. It explicitly depends on `CJ-TH-20260906-002` and is research-only.

## Deliberate non-registrations

The generation-1 scan rejected several plausible-looking items from conjecture intake:

- digital automatic arithmetic: established mathematical substrate, pending Enterprise tool implementation/review;
- finite character spectral calculus: established mathematical substrate, pending Enterprise tool implementation/review;
- Poincare Q/QO control observer: exact bounded controls plus experimental utility, but no frozen general unproved soundness claim;
- chi5 weighted-theta positivity: local theorem proved; remaining problem is classification;
- chi5 logarithmic complete monotonicity: local theorem proved; `CM => LCM?` remains an open question without a frozen asserted direction.

This exclusion discipline is intentional. The new registry must not become a bag of everything unfinished.

## Dependency handling demonstrated by the first registry

`CJ-TL-20260906-001` depends conjecturally on `CJ-TH-20260906-002`.

Therefore successful use of the rank predictor cannot produce an unconditional theorem merely because its downstream algebra is rigorous. Outputs remain exploratory/conditional unless independently certified for the particular bounded result.

This is the model for future dependency propagation.

## Proof queue after generation 1

Current highest-value proof/falsification targets are:

1. `CJ-TH-20260906-002` — derive the normalized prime-dominated response symbol/model and a rigorous spectral-count transfer theorem; high RH-route impact.
2. `CJ-TH-20260906-003` — define the phase-aware effective-modulation norm canonically and prove or kill the `N^(1+epsilon)` aggregation bound; high PDE-route impact.
3. `CJ-TL-20260906-001` — validate quantitative predictions only after the RH-specific symbol/model is frozen; tool proof follows the theorem dependency.
4. `CJ-TH-20260906-001` — lower priority because later work already showed the carrier is non-optimal and narrowed its relevance.

High priority means urgent to prove or falsify, not more likely true.

## Remaining historical scan frontier

Generation 1 is the first high-confidence backfill, not a claim that every historical note has been exhausted.

Subsequent backfill generations should walk older research notes/results/journals systematically, using the marker set in `conjecture_asset_contract.json`. Each generation must preserve:

- source path/record ID;
- the strongest precise asserted claim actually present;
- evidence envelope;
- later weakening/supersession;
- non-registration reason for false positives when useful.

The scanner is also part of research closeout going forward: new precise empirical laws or unproved tool contracts should be captured at the same durable checkpoint instead of waiting for another historical cleanup.
