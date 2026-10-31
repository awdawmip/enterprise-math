# Result reducer reader simplification

The public Result reducer now passes its result, review and synthesis readers
as ordinary keyword arguments to the compatibility reducer. It no longer
replaces four module-global functions for every reduction and restores them
in `finally`. Calls in different threads or overlapping scopes therefore do
not depend on LIFO restoration of those globals.

The default compatibility readers remain unchanged. Result selection, review
disposition, follow-up and parallel-evidence rules are not altered. Existing
persistent bootstrap adapters and other Result/Review wrappers are separate
work, not claimed fixed by this change.

Six focused tests execute the actual reducer function bodies with controlled
readers, covering defaults, explicit injection, exceptions, non-LIFO threads,
parallel synthesis and the public facade. Both touched modules compile. These
checks do not load the complete production research history or constitute a
full Source integration run. No research records are rewritten.

## Request-local follow-up reads

A small in-memory read view now reuses completed follow-up quarantine validation
for equal review inputs within a single immutable backend read request. It does
not serialize, hash or certify inputs. Outer cause validators and their existing
snapshot scope still execute; unsuccessful and recursive partial computations
are not retained. Input/result copies preserve the previous fresh-return
behavior. Scope exit clears values, including inherited closed contexts.

The backend opts in only tasks/task/dispatch/continuation, after bootstrap has
finished installing its existing adapters. CLI and writer operations do not
opt in. A demand retry starts a fresh runner/view. Seven additional focused
tests cover scope lifetime, root separation, changed inputs, failures,
reentrancy, threads and a 100-call follow-up wrapper (one inner validation).
Together with the reader-injection tests, 13 focused tests pass. This count
is not a measurement of full-catalog runtime or full historical integration.

## Activity bookkeeping, not tool-wrapper self-attestation

The current activity guard checks the actual repository record and session
association. It no longer replays connector tool names, display URLs, call IDs
or every historical checkpoint readback before allowing ordinary progress.
Its authority fields remain false; real claims/reviews/execution keep their
own authorization. Retrospective records remain tracking-only, not live actors.

Appending a checkpoint validates that new event and preserves history, with
idempotent event IDs and current-byte CAS. Missing or malformed old receipt
metadata does not freeze an unrelated append. The old registration-json CLI
option remains accepted but is no longer opened. Overview explicitly reports
metadata, not evidence revalidation. Nine activity tests pass; combined direct
Source additions now total 22 focused tests. New-source native registration is
also exercised by the backend integration fixture.

This requires coordinated delivery with the backend removal of its old
activity_registration_binding refresh adapter. Do not deploy only that removal
against the old Source guard and claim full compatibility.
