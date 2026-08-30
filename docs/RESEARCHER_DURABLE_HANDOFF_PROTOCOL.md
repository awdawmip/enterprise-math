# Enterprise Math Researcher Durable Handoff Protocol

Status: `ACTIVE / DRIVER-RESEARCHER HANDOFF BOUNDARY / V1`
Effective: `2026-08-30`
Classification: `NO_NEW_MATHEMATICS`
Driver contract: `docs/RESEARCH_DRIVER_OPERATING_CONTRACT.md`
Role source: `research_role_policy.json`

## 1. Operational host fact

In the current execution environment, a Researcher execution must be treated as **ephemeral / one-shot unless continued access to that exact conversation is positively available**.

Freeze:

`RESEARCHER_ID = PROVENANCE_IDENTITY`.

`RESEARCHER_ID != ADDRESSABLE_MAILBOX`.

`RESEARCHER_FINAL_RESPONSE != GUARANTEE_OF_FUTURE_DIRECT_CONTACT`.

The Driver must not plan a multi-stage workflow on the assumption that it can later send another question, request another file, or resume voice discussion with the same Researcher after that Researcher execution has ended.

## 2. Durable handoff requirement

If any material may be needed after the Researcher execution ends, the dispatch must require the Researcher to persist it **before final response** on an externally durable surface and return an exact locator.

This includes, when relevant:

- proofs, derivations, reports, task-local notes, checkers, code, Lean files, manifests, datasets and generated outputs;
- intermediate artifacts needed for later Driver review or another Researcher continuation;
- source/working packets that cannot be reconstructed safely from the final prose answer;
- transcripts, audio, voice notes, diagrams or other material needed for later oral/voice-style continuation;
- any handoff packet that another one-shot Researcher must consume.

`CHAT_ONLY_MATERIAL_REQUIRED_LATER -> HANDOFF_INCOMPLETE`.

## 3. Allowed durable surfaces

### GitHub

Prefer GitHub for repository-native material:

- text and Markdown;
- code and checkers;
- Lean/formalization files;
- task/result/review records;
- manifests and reasonably sized research artifacts.

Return the repository-relative path and commit/ref; include Git blob/SHA-256 identity when the governing task requires exact byte provenance.

### Google Drive

Use Google Drive for material that is unsuitable for the repository, especially:

- large binary artifacts;
- audio or voice recordings;
- large datasets or bundles;
- external document formats;
- auxiliary handoff folders containing multiple non-repository files.

Return the exact Drive file/folder locator, human-readable filename, and version/hash metadata when available or required.

GitHub remains canonical authority for repository control/theorem/runtime records. Google Drive is durable material transport/storage and does not by itself grant task, theorem, Driver, Working Truth, Foundation or promotion authority.

## 4. Required handoff manifest

When durable handoff is required, the Researcher final response must identify at minimum:

- `task_id`;
- `Researcher-ID`;
- durable surface: `GITHUB` or `GOOGLE_DRIVE`;
- exact path/file/folder locator;
- commit/ref/version where applicable;
- short inventory of persisted material;
- the durable frontier or conclusion represented by the material;
- the smallest recommended next action for the Driver or successor Researcher.

If exact byte identity is task-critical, also include the required Git blob SHA / SHA-256 / manifest digest.

A prose statement such as “I have the files” or “we can continue later” is not a durable handoff.

## 5. Driver dispatch rule

Before launching a Researcher, the Driver must ask:

`WILL_ANY_OUTPUT_OR_CONTEXT_BE_NEEDED_AFTER_THIS_RESEARCHER_ENDS?`

If `YES`, the dispatch envelope/prompt must include a durable handoff clause naming GitHub and/or Google Drive as the required persistence surface and must require the handoff manifest before final response.

Do not wait until after the Researcher final to discover that missing files or oral context were never persisted.

## 6. Driver intake rule

After a Researcher execution has ended:

1. consume the returned durable locator first;
2. verify that the required material exists and corresponds to the claimed task/frontier;
3. review or redispatch from the durable material, not from an assumption that the prior Researcher can be contacted again;
4. if required handoff material is missing, classify `HANDOFF_INCOMPLETE` and recover from the best durable frontier that actually exists;
5. do not invent missing private conversation context or treat unpersisted oral/chat material as repository evidence.

A successor Researcher receives the persisted handoff packet plus the exact governing task authority. The successor is not expected to share hidden conversational state with the predecessor.

## 7. Voice / oral continuity

If the intended workflow depends on later voice-style explanation, discussion, or oral transfer, persist the transferable content before the one-shot Researcher ends.

Acceptable forms include:

- audio/voice file in Google Drive;
- transcript or structured voice notes in Google Drive;
- transcript/notes in GitHub when repository-appropriate.

`EXPECTED_FUTURE_VOICE_CONTINUITY + NO_DURABLE_AUDIO_OR_TRANSCRIPT -> HANDOFF_INCOMPLETE`.

## 8. Boundary

This protocol changes handoff durability only. It does not alter mathematical truth, task scope, Driver review authority, Working Truth, Foundation status, source-firewall restrictions, or promotion rules.
