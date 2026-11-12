# Current observations for historical Activity summaries

Older Activity events may contain an `EM_REPRESENTED` summary and exact Source
pins, but no complete connector-observation sidecar. The loader preserves those
events as historical reports. It does not invent a past response or treat the
summary as a currently verified observation. Partial or malformed receipt fields
still fail validation; normal observations still require exact stored bytes.

The explicit `audit` operation reports unresolved legacy events as
`REOBSERVE_LEGACY_EM_SOURCES_AND_APPEND_CURRENT_REPAIR`. Re-read each exact
immutable repository/commit/path, check blob SHA1 and SHA256, and append a new
checkpoint using the existing `repairs_event_id` operation and actual complete
observation. A local `observation_id` records present provenance; it is neither
an invented historical tool call ID nor a signed server attestation. Keep old
event values, Activity ID, Researcher and original session unchanged.

This delivery applies that operation to Issue #2187, Activity
`RA-5E3FE1E761E4963EC461A892`: four historical events are retained and five exact
existing public Source files were actually read again. Four new current repair
events reference their original events. The five full observation sidecars are
new evidence; their time is not backdated. They do not rerun any mathematical
program or validate a theorem, Task, CLAIM, Result or Driver decision.

Publish the record and all its new sidecars together through Source CAS. Read
the immutable published record back, then run the explicit observation audit with that real
registration observation and the original session. The ordinary `guard` remains
the already-reviewed lightweight bookkeeping/session association check; it does
not demand connector envelopes or replay historical evidence. A source file's persistence,
an Activity guard result and formal execution authority remain separate facts.

The metadata overview exposes historical-summary events and recorded repairs;
only the explicit audit revalidates observations and resolves repair debt. Runtime
code packages must preserve their existing reviewed modules when picking up this
helper; updating this one helper does not authorize a whole-main executable swap.

No new or repeated tests are part of this change. The real-record migration,
Source byte/readback checks and guard acceptance are reported separately from
unperformed broad workflow or mathematical verification.
