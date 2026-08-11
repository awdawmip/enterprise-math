<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-R031-RESEARCHER-AUTONOMY-DELAYED-REASONING-ADVERSARY",
  "title": "R031 Researcher Autonomy, Delayed Reasoning Adversary, and Anti-Anchoring Evaluation",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P0",
  "leverage": "RESEARCH_PRODUCTIVITY_FOUNDATION",
  "frontier": "Determine whether reasoning tools should remain passive until a researcher independently frames a problem, and whether claim-triggered/delayed adversarial use can preserve open-ended research autonomy while still recovering the error-detection value found by R029/R030.",
  "next_action": "Formalize a direction-neutral reasoning-adversary contract, distinguish startup knowledge from post-framing challenge tools, compare delayed/pull-based modes against R030 preselection, measure anchoring and diversity as well as error detection, and return whether any researcher-startup integration is justified.",
  "dependencies": [
    {
      "target": "R029 Draft PR #512",
      "action": "CONSUME_TYPED_REASONING_REGISTRY_AND_COMPOSITION_BOUNDARIES_WITHOUT_ASSUMING_STARTUP_INJECTION",
      "satisfied": true
    },
    {
      "target": "R030 Draft PR #511",
      "action": "USE_MINIMUM_CRITICAL_COVER_AS_PRESELECTION_CONTROL_ONLY_NOT_AS_ACCEPTED_ARCHITECTURE",
      "satisfied": true
    },
    {
      "target": "Issue #508",
      "action": "CONSUME_DRIVER_HOLD_AND_ANTI_ANCHORING_CORRECTION",
      "satisfied": true
    }
  ],
  "source_refs": [
    "R029 Draft PR #512 / reasoning_tools.json / R029_TOOL_COMPOSITION_MATRIX.json",
    "R030 Draft PR #511 / research_context compiler and historical backtest",
    "Issue #508 Driver correction: startup MCC not approved",
    "Issue #513 anti-anchoring experiment tracker",
    "R020/R023/R023I/R025/R028 historical examples of late distinctions and over-strengthening risks"
  ],
  "evidence_status": "RESEARCHER_AUTONOMY_ANTI_ANCHORING_GATE",
  "last_progress_ref": "User rejected preselected startup reasoning packs because they effectively pre-coordinate research direction; Driver froze R030 startup integration and reframed reasoning tools as post-framing adversaries",
  "last_progress_at": "2026-08-12T07:00:00+08:00",
  "hard_block": null,
  "tags": [
    "R031",
    "meta-research",
    "researcher-autonomy",
    "anti-anchoring",
    "reasoning-tools",
    "delayed-adversary",
    "claim-triggered",
    "open-world-research",
    "novelty-preservation"
  ],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "DRIVER_APPROVED",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "identity_lane": "R031",
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:a03b06c1c6d29ca2776592fd12aa77406f45a21afb8fc1a8431b25cd41963c77",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# R031 — Researcher Autonomy, Delayed Reasoning Adversary, and Anti-Anchoring Evaluation

Status: `READY / P0 / META-RESEARCH / ANTI-ANCHORING / NOT CANONICAL`

## 0. Correction being tested

R029 established that logic/philosophy distinctions can be compiled into typed research tools. R030 established that a sparse task-relative selector can recover historical late distinctions more efficiently than ALL_MATCHES.

That is not enough to justify startup injection.

The user identified the stronger objection:

> selecting reasoning tools before research begins already chooses which distinctions deserve attention, so the system may silently predefine the research direction.

R031 treats that objection as theorem-critical for research infrastructure.

The target architecture is no longer:

`TASK -> PRESELECT REASONING TOOLS -> RESEARCH`

but:

`TASK + ACCEPTED KNOWLEDGE -> INDEPENDENT FRAMING -> CLAIM-TRIGGERED ADVERSARY -> RESEARCH`.

The reasoning registry is a passive library until the researcher has generated a concrete commitment to attack.

---

## 1. Preserve the distinction between knowledge and direction

The researcher may start with accepted mathematical knowledge, exact source/status information, frozen negative theorems/counterexamples, and the task-specific contract. These are part of the known problem state.

Do not equate those with reasoning-direction suggestions.

R031 must distinguish:

- `KNOWN_FACT`: accepted external/project knowledge;
- `TASK_CONSTRAINT`: what the task explicitly asks or excludes;
- `RESEARCHER_COMMITMENT`: a hypothesis, representation, implication, regime split, proof plan, or evidence upgrade proposed by the researcher;
- `REASONING_CHALLENGE`: a post-commitment attack or check;
- `INTERPRETIVE_LENS`: optional reframing with direction-bearing potential.

Only the last two come from the reasoning registry.

---

## 2. Independent Framing Checkpoint

Before any diagnostic/lens tool is proactively surfaced, require an `INDEPENDENT_FRAMING_CHECKPOINT` produced from task + accepted knowledge only.

Minimum content:

- current object/type model;
- at least two plausible research directions when the problem is genuinely open-ended;
- explicit conjectures or questions, if any;
- proposed observables/carriers/representations;
- evidence plan;
- uncertainties and unresolved choices;
- statements the researcher is not yet willing to claim.

The checkpoint is not judged against R029/R030 gold labels before it is frozen.

Do not rewrite it after the challenger pass; preserve before/after for comparison.

---

## 3. Claim-triggered invocation contract

Reasoning tools may be proactively invoked only after the researcher produces a typed commitment.

Suggested trigger classes:

- `IMPLICATION_CLAIM`: A => B;
- `EQUIVALENCE_CLAIM`: A iff B / same object / same information;
- `UNIVERSAL_CLAIM`: all / arbitrary / every horizon;
- `MINIMALITY_CLAIM`: minimal / unique / coarsest / optimal;
- `COMPOSITION_CLAIM`: one-step result reused under iteration/composition;
- `CARRIER_COMPRESSION`: one carrier/summary replaces another;
- `RESOURCE_PARETO_CLAIM`: cheaper/faster/smaller/better;
- `EVIDENCE_UPGRADE`: executable/finite evidence elevated toward theorem status;
- `COVERAGE_CLAIM`: build/test/check covers a new artifact;
- `CAUSAL_ATTRIBUTION`: cause/contribution/credit language;
- `RECOALESCENCE_OR_FORGETTING`: information is declared discardable;
- `PRIOR_ART_OR_NOVELTY_CLAIM`;
- explicit `RESEARCHER_REQUEST_FOR_LENS`.

A tool selected from a trigger must consume the researcher-generated commitment as its primary input. It must not invent the commitment from task keywords.

---

## 4. Direction-neutrality requirement

Classify tool actions by direction-bearing potential:

### A. `CHECK_ONLY`
Tests validity/preconditions of a researcher assertion. May reject or narrow; does not suggest a preferred replacement research program.

### B. `COUNTEREXAMPLE_ATTACK`
Attempts to kill a researcher conjecture within a declared search class. May return a witness or no witness; does not rank unrelated hypotheses.

### C. `ALTERNATIVE_BOUNDARY_CHALLENGE`
Surfaces a logically adjacent missing case only because the current commitment quantifies over or excludes it. Example: equality/zero/degenerate boundary attack after a threshold claim.

### D. `DIRECTION_BEARING_LENS`
Introduces a new ontology, analogy, causal framing, duality, category, or research decomposition not already present in the researcher's commitment.

A/B/C may be eligible for delayed proactive use. D is opt-in only.

R031 must test whether some R029 diagnostics currently classified as advisory should be retyped because they are actually direction-bearing.

---

## 5. Four comparison modes

Evaluate at least:

1. `NO_META_TOOL`
   - task + accepted knowledge only.

2. `STARTUP_PRESELECT`
   - R030-style task-relative MCC before researcher framing.
   - control condition only; not presumed desirable.

3. `DELAYED_CHALLENGER`
   - independent framing frozen first;
   - A/B/C tools selected only from concrete commitments;
   - D lenses hidden unless requested.

4. `PULL_ONLY`
   - registry completely passive unless researcher explicitly requests a check/lens/tool.

If behavioral multi-run evidence is unavailable, do not fake it. Return a static/structural result and explicitly mark `BEHAVIORAL_FIELD_TRIAL_REQUIRED`.

---

## 6. Historical backtest is necessary but insufficient

Historical tasks may still be used for failure detection:

- R020: static correctness vs dynamically reusable state;
- R023: Boolean support vs richer carriers;
- R023I: build pass vs actual root/module coverage;
- R025: threshold/equality/aligned islands and zero boundary;
- R028: declared vs realized future.

But do not optimize the new mechanism solely for post-hoc gold recall.

Historical gold can answer:

> would the challenger have caught an error after the researcher made the relevant claim?

It cannot answer:

> would preloading this distinction improve open-world research without suppressing another valid framing?

Freeze this epistemic boundary explicitly.

---

## 7. Anti-anchoring metrics

In addition to error-detection recall/precision, define and measure where possible:

### Framing preservation
- number of independent initial research directions;
- fraction of initial directions surviving challenge when not falsified;
- whether challenger output introduces ranking language not justified by a failed claim.

### Directional convergence
- similarity between researcher framing and registry taxonomy before/after tool exposure;
- whether startup preselection causes earlier convergence toward registry-named categories than delayed mode.

### Novel distinction yield
- valid distinctions introduced by the researcher that are absent from the registry;
- whether challenger preserves, ignores, or suppresses them.

### Error correction
- false implication/minimality/composition/evidence claims caught;
- time/checkpoint distance from commitment to correction;
- false-positive challenge rate.

### Context/attention cost
- injected tool count/tokens;
- number of irrelevant challenges;
- number of valid research directions abandoned without a counterexample or proof-based reason.

Do not collapse all metrics into one scalar unless a later theorem justifies it.

---

## 8. Required mutation tests

At minimum create fixtures for:

1. a task whose wording contains `support` but whose researcher framing never uses Boolean support as a carrier;
2. a task where the researcher independently invents a useful distinction absent from R029;
3. a claim that is valid but resembles a historically dangerous pattern;
4. a threshold claim where equality is already explicitly excluded by the researcher;
5. a resource comparison with already equal semantic contracts;
6. a composition claim with a supplied congruence proof;
7. a causal-looking task where the researcher makes only predictive claims;
8. a philosophically rich task where no lens is requested;
9. a researcher request for an alternative ontology/lens after the first framing checkpoint;
10. a deliberately false universal claim that should trigger a challenger quickly.

The challenger should stay quiet on 1/3/4/5/6/7/8 when the relevant risk is already discharged, and should activate appropriately on 9/10.

---

## 9. Relationship to R029

R029 remains valuable as a registry of typed operations and composition boundaries.

R031 must not conclude that R029 itself is invalid merely because startup injection is invalid.

Instead determine which registry tools are:

- safe as post-commitment checkers;
- safe only with explicit preconditions;
- direction-bearing and therefore pull-only;
- redundant with accepted theorem/common-surface knowledge;
- unsuitable for automated invocation.

Produce a proposed `invocation_mode` field for registry entries if useful:

- `POST_COMMITMENT_AUTO`
- `POST_COMMITMENT_CONDITIONAL`
- `PULL_ONLY`
- `MANUAL_INTERPRETIVE_ONLY`.

---

## 10. Relationship to R030

Treat R030's compiler as an experimental control and artifact parser, not accepted startup infrastructure.

Potentially salvage:

- Task Semantic Signature extraction for audit/inspection;
- deterministic source snapshots;
- historical replay machinery;
- context cost accounting;
- mutation harness.

Potentially reject or repurpose:

- startup tool preselection;
- MCC as default startup objective;
- gold-recall as the primary success metric;
- task-derived diagnostic injection before independent framing.

R031 should say exactly which R030 components survive and why.

---

## 11. Open-world field-test design

Design at least one feasible future field trial using genuinely fresh research tasks.

Preferred design:

- multiple independent researcher conversations;
- same task and accepted knowledge;
- randomized support mode among NO_META / STARTUP_PRESELECT / DELAYED_CHALLENGER / PULL_ONLY;
- initial framing frozen before any challenger in delayed/pull modes;
- blind Driver scoring of correctness, framing diversity, novel-valid distinctions, and error rate;
- registry updated only after the trial batch is frozen.

If that trial is not executed in R031, return a fully specified protocol rather than pretending static replay settles behavioral anchoring.

---

## 12. Required deliverables

At minimum:

1. `docs/R031_RESEARCHER_AUTONOMY_REPORT.md`
2. machine-readable anti-anchoring contract/schema;
3. claim-trigger taxonomy;
4. R029 invocation-mode reclassification proposal;
5. R030 salvage/kill matrix;
6. mutation fixtures and executable oracle;
7. historical post-commitment replay results;
8. open-world field-test protocol;
9. machine summary;
10. explicit `META_TOOL_DELTA` describing whether startup injection is killed, narrowed, or retained only for non-directional checks.

---

## 13. Preferred return classes

Strong positive replacement:

`STARTUP_PRESELECTION_REJECTED / CLAIM_TRIGGERED_REASONING_ADVERSARY_FOUND / RESEARCHER_AUTONOMY_PRESERVED_BY_CONTRACT / HISTORICAL_GUARDS_RETAINED / FIELD_TRIAL_READY / NOT_CANONICAL`

If only static safety can be established:

`STARTUP_PRESELECTION_REJECTED / DELAYED_CHALLENGER_STATIC_CONTRACT_FOUND / BEHAVIORAL_ANCHORING_UNRESOLVED / FIELD_TRIAL_REQUIRED / NOT_CANONICAL`

If even delayed automation is too direction-bearing:

`AUTOMATIC_REASONING_TOOL_INVOCATION_REJECTED / PASSIVE_PULL_BASED_REGISTRY_ONLY / NOT_CANONICAL`

Negative result is valid. Do not preserve R030 startup injection merely because it has better historical gold recall.
