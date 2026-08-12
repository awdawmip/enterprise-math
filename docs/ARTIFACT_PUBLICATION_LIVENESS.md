# Enterprise Math Artifact Publication Liveness

Status: `ACTIVE / CANONICAL PUBLICATION-LIVENESS SUPPLEMENT`
Effective: 2026-08-12
Scope: post-research artifact generation, checkpoint persistence, duplicate-writer avoidance, and user-visible liveness.
Authority: supplements `docs/GITHUB_INTERACTION_BUDGET.md`; if wording conflicts, the stricter liveness rule applies for artifact publication.

## Core invariant

> **Research completion must not be followed by a second, long-running publication project.**

Artifact persistence is a bounded checkpoint operation, not a place to optimize Git history aesthetics or build a custom Git-data pipeline.

## Required post-research path

Once the mathematical/research payload is coherent:

1. generate the complete task artifact set locally once;
2. run the task-relevant checker/validation pass once on that frozen set;
3. freeze the artifact manifest only if the task actually requires one;
4. take one current owner-branch/head snapshot immediately before publication;
5. if that same owner generation has already advanced with an equivalent checkpoint, consume/reconcile that checkpoint instead of building a duplicate publication;
6. publish the frozen set in one bounded source checkpoint;
7. create/update at most one Draft PR for the owner generation when useful;
8. stop publication work and return to research/handoff/user-facing completion.

## Prohibited publication choreography

Do not turn a completed research result into a long critical path such as:

`artifact regeneration -> repeated checker reruns -> manifest -> ZIP -> minify large JSON -> chunk-read it -> create_blob per file -> assemble tree -> assemble commit -> choose again between Git-data API and contents API`.

In particular:

- do not minify or chunk-read artifacts merely to make Git blob creation convenient;
- do not create one Git blob per artifact merely to obtain a cosmetically single commit when a simpler bounded publication path is available;
- do not repeatedly compare contents-API versus Git-data/tree strategies after the artifact set is already frozen;
- do not regenerate/check/package the same frozen artifacts multiple times unless a concrete failure changes the payload;
- do not create ZIP/bundle/manifest artifacts unless required by the task, handoff, or user request;
- do not spend materially more effort on commit shape than on preserving the semantic checkpoint.

If a connector cannot atomically publish the whole directory, prefer a small number of straightforward contents writes or the available normal git push path. A slightly less elegant commit history is preferable to a long, failure-prone publication choreography.

## Duplicate-writer / concurrency guard

Before the first source publication write, take exactly one owner-head snapshot for the branch/generation being published.

If the branch has advanced since the research payload was frozen:

- determine whether the new head is the same task/generation and contains an equivalent or superseding checkpoint;
- if yes, do not publish a second independently assembled commit; consume, compare, or add only a genuinely missing delta;
- if no, preserve owner isolation and follow the normal conflict/reconciliation rules;
- a non-fast-forward discovered after building an unattached duplicate commit is a publication-liveness failure signal, not a reason to keep rebuilding commits.

Do not poll the branch repeatedly. One pre-publication snapshot is the default; recheck only after a concrete publication failure or new semantic input.

## User-visible liveness

Mechanical publication is still part of the active user interaction.

For any long-running publication/checkpoint operation, follow the platform/user-update cadence: surface a concise progress update after roughly 15 seconds or 2-3 tool calls, whichever comes first. The update should say what semantic milestone is already complete and what bounded mechanical step remains.

Do not leave the UI appearing frozen while performing a long chain of artifact or Git operations.

## Failure classification

Use these process signals when helpful:

- `PUBLICATION_CRITICAL_PATH_EXPANDED` — artifact persistence has become a long multi-stage workflow after research is already complete;
- `DUPLICATE_PUBLICATION_PATH_DETECTED` — another same-generation checkpoint advanced while a second publication was being assembled;
- `UNATTACHED_DUPLICATE_COMMIT` — a locally/remotely created commit object is not attached because an equivalent owner checkpoint already won the race;
- `PUBLICATION_SIMPLIFY_REQUIRED` — switch to the simplest bounded contents/git publication path;
- `REMOTE_BUDGET_EXCEEDED` remains a performance signal, never a mathematical `HARD_BLOCK`.

None of these signals invalidates completed mathematics. Preserve the research payload, simplify the persistence path, and continue.

## R046 incident provenance

This rule was added after R046 (`Engineering-Success Inversion`) completed its research but spent a long period in post-research artifact persistence: 13 files were generated/re-read/compressed, 32 checker items were run, manifest/ZIP work was added, large JSON files were minified/chunk-read, multiple Git blobs were created, and a tree/commit strategy was assembled. Individual GitHub blob calls were typically sub-second; the delay came from serial orchestration and missing progress updates. A parallel same-Researcher-ID checkpoint later advanced the branch while another unattached commit was assembled, exposing duplicate publication work.

The correction is operational, not mathematical: **generate once -> check once -> one owner-head guard -> one bounded checkpoint publication**.
