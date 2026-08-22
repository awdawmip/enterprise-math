# Enterprise Math Axiom Candidate Protocol

Status: `ACTIVE / CANONICAL GOVERNANCE / V2`
Date: `2026-08-22`
Driver-ID: `EM-DVR-K7Q4N8`
Machine state machine: `research_axiom_candidate_state_machine.json`

## Purpose

This protocol prevents three different objects from being collapsed into one:

1. an independently discovered **candidate axiom**;
2. a Driver-frozen **research direction / Working Truth**;
3. a **canonical foundation statement**.

They are different lifecycle states and require different evidence.

## Phase A — discovery

A free researcher searches from a frozen current foundation snapshot while the current research agenda is withheld as a discovery prior.

Before opening current/prior route context, freeze a candidate packet containing:

- candidate ID and statement;
- foundation snapshot ref;
- relevant worldview snapshot ref or `none`;
- primitive dependencies;
- semantic layer;
- structural motivation independent of an active route;
- immediate consequences;
- obvious falsifiers/counterexamples;
- blindness status `CLEAN` or `ANCHOR_EXPOSED`;
- timestamp/content hash when practical.

This packet is provenance. Do not rewrite its origin story after seeing existing work.

## Phase B — audit

Only after freeze, open current Enterprise Math and external comparison context.

Mandatory questions:

1. Is the candidate already present under another name?
2. Does the current foundation imply it, making it a theorem rather than an axiom?
3. Does it depend on an implementation coordinate/carrier choice?
4. Does it contradict a frozen current premise, and if so is that a genuine replacement candidate or a typing error?
5. Does a small exact model/counterexample falsify it?
6. Does relevant prior art reclassify novelty?
7. Does it collide with an active route only after comparison, or was that route already part of discovery?

Allowed Phase-B classifications are defined by the machine state.

## Driver intake

A raw blind packet is not dispatchable.

Driver intake begins only after Phase B has produced an audited classification.

The Driver may:

- park/reject;
- return it as duplicate/prior art/derived theorem;
- request independent replication;
- open an explicit research task;
- open a Foundation question.

Only when the Driver explicitly freezes a task direction does `WORKING_TRUTH` become applicable.

`AXIOM_CANDIDATE != WORKING_TRUTH`.

`WORKING_TRUTH != CANONICAL_FOUNDATION`.

## Transition to explicit task

If an audited free candidate becomes a selected task, the taskbook must preserve its origin:

- `origin_kind=FREE_AXIOM_CANDIDATE`;
- `origin_candidate_id=<candidate_id>`;
- `origin_candidate_state=<audited intake-eligible state>`.

Do not relabel the same origin as `DRIVER_ROADMAP` merely because the Driver has now selected it.

Selection changes **control-plane status**, not discovery provenance.

Working Truth still does not activate automatically at the moment of candidate classification; it requires the explicit Driver direction/task freeze.

## Evidence roles

Evidence used to choose or shape a candidate is **discovery evidence**.

Evidence that did not participate in that adaptive choice, or whose reuse is explicitly corrected/disclosed, may serve as **validation evidence**.

Freeze:

`DISCOVERY_EVIDENCE != INDEPENDENT_VALIDATION_EVIDENCE`.

This is the research analogue of the account-level post-allocation principle: later evidence may reclassify the candidate, but the same adaptive evidence cannot silently be reused as if it independently validated the chosen claim.

## Independent replication

For strong independence evidence:

- use a fresh context;
- freeze the same foundation/worldview snapshot when comparability matters;
- do not expose another run's candidate before the new run freezes its own;
- compare afterwards.

Record one of:

- `CLEAN_INDEPENDENT_CONTEXT`;
- `SHARED_AMBIENT_CONTEXT_DISCLOSED`;
- `NOT_INDEPENDENT`.

A new Researcher-ID alone does not prove independence if the contexts share salient project memory, candidate packets or agenda exposure.

Convergence is a salience/compression signal, not proof. Divergence must be preserved before Driver selection.

## Foundation backflow

Only the following free-research outputs are eligible for Foundation intake:

- `AUDITED_AXIOM_CANDIDATE`;
- `AUDITED_REPLACEMENT_CANDIDATE`;
- `EXACT_NEGATIVE_OBSTRUCTION`.

Even then, Foundation intake is a classification event, not canonicalization.

A raw candidate cannot automatically:

- open a Foundation question;
- enter the scheduler;
- become a taskbook;
- modify current Foundation truth.

## Canonicalization

Canonicalization uses the normal Enterprise Math evidence, ownership and L4 promotion gates.

There is no direct path:

`BLIND_CANDIDATE -> main`.

There is no direct path:

`AUDITED_CANDIDATE -> main`.

The object must first become an explicit research/Foundation payload and survive the existing proof/verification/promotion process.
