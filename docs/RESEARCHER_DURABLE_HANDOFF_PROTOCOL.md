# Enterprise Math Researcher Durable Handoff Protocol

Status: `ACTIVE / DRIVER-RESEARCHER HANDOFF BOUNDARY / V1.1`
Effective: `2026-09-01`
Classification: `NO_NEW_MATHEMATICS`
Driver contract: `docs/RESEARCH_DRIVER_OPERATING_CONTRACT.md`
Role source: `research_role_policy.json`

## 1. Operational host fact

A Researcher execution is ephemeral/one-shot unless continued access to that exact conversation is positively available.

Freeze:

`RESEARCHER_ID = PROVENANCE_IDENTITY`.

`RESEARCHER_ID != ADDRESSABLE_MAILBOX`.

`RESEARCHER_FINAL_RESPONSE != GUARANTEE_OF_FUTURE_DIRECT_CONTACT`.

The Driver must not plan later questions or file retrieval on the assumption that the same Researcher conversation can be resumed.

## 2. Durable handoff requirement

Any material needed after the Researcher execution ends must be persisted before final response on an externally durable surface and returned with an exact locator.

This includes, when relevant:

- proofs, derivations, reports and task-local notes;
- checkers, code, Lean files and manifests;
- datasets and generated outputs;
- intermediate artifacts needed for review or successor execution;
- source/working packets that cannot safely be reconstructed from final prose;
- transcripts, audio, diagrams or other transferable continuity material.

`CHAT_ONLY_MATERIAL_REQUIRED_LATER -> HANDOFF_INCOMPLETE`.

## 3. Allowed durable surfaces

### GitHub

Use GitHub for repository-native material: text, Markdown, code, checkers, Lean/formalization files, task/result/review records, manifests and reasonably sized artifacts.

A valid GitHub locator identifies:

- repository;
- retained branch or tag keeping the commit reachable;
- immutable full commit SHA;
- exact repository-relative path(s);
- Git blob/SHA-256 identity when required by the governing task.

### Google Drive

Use Google Drive for large binaries, audio, large datasets/bundles, external document formats or auxiliary folders unsuitable for the repository.

Return the exact file/folder locator, human-readable name and version/hash metadata when available or required.

GitHub remains canonical authority for repository control/theorem/runtime records. Drive is durable material transport/storage and does not itself grant task, theorem, Driver, Working Truth, Foundation or promotion authority.

## 4. Pull Requests are optional review surfaces

A durable GitHub handoff does not require an open Pull Request. The storage primitive is a reachable ref plus immutable commit and exact paths.

Freeze:

`DURABLE_HANDOFF != OPEN_PR`.

`OPEN_PR != REQUIRED_DURABLE_LOCATOR`.

`CI_PENDING_NONBLOCKING -> CONTINUE_PARENT_TASK`.

Default checkpoint behavior:

1. batch the coherent checkpoint on the owner branch;
2. persist one immutable commit;
3. return branch, commit SHA, exact paths, inventory, frontier and next action;
4. record the HANDOFF `progress_ref` against that durable commit/path when scheduler coordination is required;
5. keep the branch/tag reachable until the material is accepted, superseded or deliberately archived;
6. do not open a PR solely to obtain a locator, trigger CI, produce a conversation stopping point or create a review queue item.

Open or update at most one PR for a bounded owner generation only when:

- the exact task explicitly requires a PR;
- an authorized Driver has begun actual review/integration;
- a concrete merge, promotion or conflict-resolution attempt is happening now;
- the PR discussion surface itself is needed for a bounded decision.

An existing PR may remain a useful locator or review surface, but pending CI, mergeability or review does not suspend independent parent work.

## 5. Required handoff manifest

A required handoff identifies at minimum:

- `task_id`;
- `Researcher-ID`;
- durable surface: `GITHUB` or `GOOGLE_DRIVE`;
- exact branch/tag or Drive locator;
- immutable commit SHA or durable version;
- exact persisted paths/files;
- short inventory;
- durable frontier/conclusion;
- smallest recommended next action.

When exact byte identity is task-critical, include the required Git blob SHA, SHA-256 or manifest digest.

“I have the files” or “we can continue later” is not a durable handoff.

## 6. Driver dispatch rule

Before launching a Researcher, determine whether any output/context will be needed after the execution ends. When yes, include the durable handoff clause in the dispatch envelope before research begins.

Do not discover after final response that necessary material was left only in chat.

A required GitHub handoff should ask for a retained branch/commit/path manifest. It should not impose a PR or CI wait unless review/integration is itself part of the exact task.

## 7. Driver intake rule

After a Researcher execution ends:

1. consume the durable locator first;
2. verify that the material exists and matches the claimed task/frontier;
3. review or redispatch from durable material rather than assumed hidden conversation state;
4. if required material is missing, classify `HANDOFF_INCOMPLETE` and recover from the best durable frontier that exists;
5. do not invent missing private context;
6. open a review/integration PR only when that bounded subflow actually begins.

A successor receives the persisted handoff packet plus exact governing task authority. It is not expected to share the predecessor's hidden conversational state.

## 8. Voice/oral continuity

When later voice-style transfer matters, persist audio, transcript or structured notes before the one-shot execution ends.

`EXPECTED_FUTURE_VOICE_CONTINUITY + NO_DURABLE_AUDIO_OR_TRANSCRIPT -> HANDOFF_INCOMPLETE`.

## 9. Boundary

This protocol changes handoff durability and GitHub interaction burden only. It does not alter mathematical truth, task scope, Driver review authority, Working Truth, Foundation status, source firewalls or promotion rules.
