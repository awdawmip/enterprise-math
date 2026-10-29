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
