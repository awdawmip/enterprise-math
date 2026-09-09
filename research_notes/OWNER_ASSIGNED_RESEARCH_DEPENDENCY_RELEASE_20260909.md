# Assigned research consumes typed artifact-dependency releases

Mode: CONTROL_PLANE_MAINTENANCE / NO_NEW_MATHEMATICS.

## Problem and owning evidence

The q=78553 research task retains one declared artifact dependency on the
Correction review. Its real UNBLOCK5602494875 and current canonical replay
already record HANDOFF_READY / NEEDS_DISPATCH. The initial directed-research
entry supported only an empty dependency list, so it could not consume this
existing release without a separate verified satisfaction model.

The release is not just prose. Its unchanged
[server envelope](https://github.com/awdawmip/enterprise-math/blob/bd88c3ee7f5fa120e878027d813a64cf99ad5dc2/driver_reviews/R005_LINE_DRIVER_81273A_20260909/seam_release_server_envelope.json)
names the exact obligation task/publication, Driver authority, original Result
digest, ACCEPTED DR and ready DFU. The
[Driver dossier](https://github.com/awdawmip/enterprise-math/blob/bd88c3ee7f5fa120e878027d813a64cf99ad5dc2/driver_reviews/R005_LINE_DOSSIER.md)
declares the artifact prerequisite fulfilled while preserving the separate
governance task and both open parent objectives. This maintenance does not
review that mathematics again or invent a governance Result/DONE event.

## Supported model and checks

The new read-only checker consumes artifact dependencies with exact task_id
and required_artifact fields and unique task IDs. Every obligation must have
a typed mapping in a canonically applied UNBLOCK bound to the current target
publication. The already issued single-obligation shape is supported as-is;
the list shape covers several obligations exactly once. No requirement text,
filename or generic readiness label is interpreted as proof of satisfaction.

The checker validates the unedited authenticated server envelope, publication
clock and Driver authority active when the release was issued. It then checks
current operational obligation publications and taskbook bytes, the underlying
Result's current publication and raw digest, the exact current ACCEPTED
immutable DR, and the exact ready DFU bound to the same digest. Review and
follow-up records must predate the release. Current assignment authority,
recipient/claim/session, parent, cohort and canonical derived-state gates remain
separate. Later applied blocks/terminal transitions and later untyped releases
cannot silently reuse an older proof.

The full evidence remains in the returned route. Compact startup carries its
digest, release comment/body binding and obligation count. This keeps the
startup packet bounded without deleting the full evidence or replacing the
existing Issue240/task/Result/review stores.

The checker uses the installed canonical definition facade. Its older
single-record constructor does not expose all current parent metadata and was
therefore unsuitable for the prototype's full binding comparison.

## Actual verification and limits

The new and existing suites passed together: 64 tests across artifact-release,
assigned-research, assigned-GOV and registered-event composition boundaries.
Coverage includes a real-reducer positive route, a real reblock and later
untyped release, current publication/result drift, record tampering, revoked
historical authority, incomplete or duplicate coverage, stale review/follow-up
bindings, timing errors, and bounded startup transport. An early duplicate
test met the existing raw-comment parser's rejection before reaching the new
checker; the assertion now recognizes that actual earlier boundary.

The [recorded-input proof receipt](../research_artifacts/ASSIGNED_DEPENDENCY_RELEASE_20260909/actual_release_proof_receipt.json)
uses the same 765 real comments frozen by the
[JT2 source packet](https://github.com/awdawmip/enterprise-math/blob/d41d432b8b9cea81b96224015300a15678c4b95a/research_artifacts/JT2_PERSISTENT_LINE_DRIVER_20260909/formal_research_entry_57ccce_20260909/actual_selection_refusal_manifest.json),
evaluated at its recorded time. The final prototype resolved the real R005
release and the original RR/DR/DFU bindings in 8.109 seconds. Its development
workbench is explicitly d40 plus the already-admitted 4306 control overlay;
it is not described as a complete current-main execution snapshot. This is a
dependency-proof check, not a real R005 assignment, CLAIM or execution grant.

The original nonempty task dependency, taskbook, publications, release,
Result, DR and DFU are unchanged. Unsupported dependency languages,
unavailable evidence and parallel/synthetic review authorities remain scoped
refusals. The extension grants no mathematical acceptance, catalogue
completeness, q=78553 frontier increase or parent closure. A real receiving
researcher and current scoped Driver assignment still have to use the normal
prepare/CLAIM/authorize path after main admission.
