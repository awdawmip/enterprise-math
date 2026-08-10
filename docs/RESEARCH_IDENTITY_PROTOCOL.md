# Enterprise Math Research Identity Protocol

Status: `ACTIVE / CANONICAL VISIBLE IDENTITY CONTRACT`
Effective: 2026-08-11

## 1. Purpose

Enterprise Math may run many parallel ChatGPT research conversations. Task IDs identify work, but they do not reliably identify which research conversation produced a statement, artifact, commit, PR, or handoff.

This protocol gives every research conversation a stable, human-readable `Researcher-ID` and makes that identity visible in chat and persisted artifacts.

A Researcher-ID identifies a **research conversation/session instance**, not a human legal identity and not a theorem owner by itself.

## 2. ID grammar

Preferred researcher handle:

`EM-R<LANE>-<NN>`

Examples:

- `EM-R011-01`
- `EM-R012-01`
- `EM-R012-02`
- `EM-R005A-01`
- `EM-R005C-01`

The lane is normally the compact task/program tag. `NN` distinguishes parallel or replacement research conversations on the same lane.

The canonical Driver handle is:

`EM-DRIVER-01`

A handle is stable for the life of that conversation. Do not silently change it because a branch, PR, or stage changed. If work is transferred to a genuinely new research conversation, allocate a new handle and record `handoff_from` / `handoff_to` in the directory or handoff.

## 3. Assignment is separate from identity

Keep these concepts distinct:

- `Researcher-ID`: which research conversation produced this;
- `Research-Role`: `RESEARCHER` or `RESEARCH_DRIVER`;
- `Research-Task`: the current official task ID or `CONTROL_PLANE`;
- theorem owner/source: mathematical provenance, which may be different from the current researcher.

A Researcher-ID never grants task authority, theorem ownership, Driver authority, or canonical status.

## 4. Visible chat marker

Every substantive final response from an Enterprise Math researcher/Driver should end with a visible identity line:

`Researcher-ID: <ID> / <TASK-or-CONTROL_PLANE>`

Examples:

`Researcher-ID: EM-R012-01 / RS-R012-A3A4-RELATION-GENESIS-CATEGORY-BOUNDARY`

`Researcher-ID: EM-DRIVER-01 / CONTROL_PLANE`

If a `Global-Knowledge-Sync:` marker is also required, the identity line appears immediately **before** it, so the sync marker remains the final non-empty line.

Do not emit the identity marker for unrelated non-Enterprise-Math conversations.

## 5. Commit identity

Identity must be visible in GitHub's ordinary commit list, not only hidden inside commit details.

### 5.1 Commit subject prefix

Research semantic-checkpoint commit subjects should begin with the Researcher-ID:

`[EM-R012-01] R012: formalize genesis-index`

`[EM-R011-01] R011: prove frozen T01-T03 targets`

Driver/control-plane commits use:

`[EM-DRIVER-01] governance: update researcher directory`

This makes the producing research conversation visible without opening the commit.

### 5.2 Git trailers

The same commit should also include machine-readable trailers when the write surface supports them:

```
Researcher-ID: EM-R012-01
Research-Task: RS-R012-A3A4-RELATION-GENESIS-CATEGORY-BOUNDARY
Research-Role: RESEARCHER
```

For Driver/control-plane commits:

```
Researcher-ID: EM-DRIVER-01
Research-Task: CONTROL_PLANE
Research-Role: RESEARCH_DRIVER
```

Legacy commits are not rewritten solely to add identity metadata.

If a connector/tool cannot add trailers to an already-created commit, preserve the ID in the commit subject, PR body, artifact, or handoff and use full trailers on the next writable semantic checkpoint. Missing identity metadata is a provenance defect, not a mathematical `HARD_BLOCK`.

## 6. PR and handoff identity

### 6.1 PR title

Research PR titles should begin with the Researcher-ID so the authoring conversation is visible in the PR list:

`[EM-R012-01] R012: category/relation genesis closure`

Driver-only governance PRs use `[EM-DRIVER-01]`.

Do not rename historical PRs solely to retrofit this convention.

### 6.2 PR body

PR descriptions should include a compact identity block near the top:

```
Researcher-ID: EM-R012-01
Research-Task: RS-R012-A3A4-RELATION-GENESIS-CATEGORY-BOUNDARY
Research-Role: RESEARCHER
```

### 6.3 Handoff/artifact metadata

Machine-readable handoffs/manifests should carry fields equivalent to:

```json
{
  "researcher_id": "EM-R012-01",
  "research_task": "RS-R012-A3A4-RELATION-GENESIS-CATEGORY-BOUNDARY",
  "research_role": "RESEARCHER"
}
```

Reports intended for humans should show the same identity in their header or metadata block.

## 7. Directory

The current human-readable directory lives in account-level GLOBAL_KNOWLEDGE:

`projects/enterprise-math/RESEARCHER_DIRECTORY.md`

The directory is maintained by the Driver and records, at minimum:

- Researcher-ID;
- role;
- current/last task;
- plain-language responsibility;
- status (`ACTIVE`, `WAITING_RETURN`, `DONE`, `PARKED`, `RETIRED`);
- handoff relation when relevant.

The directory is routing/continuity metadata only. It is not theorem evidence.

Update it when:

- a new researcher conversation is dispatched;
- an existing conversation receives a new official assignment;
- a handoff creates a replacement researcher;
- a route becomes done/parked/retired.

Do not update it for every chat turn or commit.

## 8. Driver responsibility

The Driver allocates IDs and prevents collisions.

When the Driver gives the user a continuation/research prompt, the prompt should include the assigned identity and instruct the researcher to keep it visible in future responses and persisted artifacts.

If a researcher returns without an ID, the Driver may retroactively associate the return with a known directory entry when the mapping is unambiguous. If ambiguous, do not guess; create/assign a new handle at the next dispatch boundary and preserve the ambiguity in provenance.

## 9. Identity does not replace task isolation

Researcher-ID is an observability/provenance feature. It does not weaken:

- task-isolated context;
- theorem owner isolation;
- proposal/Driver authority;
- canonical promotion gates;
- status discipline.

The intended effect is simple: the user and Driver should be able to look at a chat, commit, PR, report, or handoff and immediately know which research conversation produced it and what work that conversation was assigned.
