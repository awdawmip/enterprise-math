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
