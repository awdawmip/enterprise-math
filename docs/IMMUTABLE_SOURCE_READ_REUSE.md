# Request-local source reuse

The hosted read runner may enter `immutable_source_view(root)` for its private,
fixed input. This reuses parsed execution/publication/Driver source records and
review evidence objects while bootstrap installs operational adapters. Each
caller receives its own mutable JSON containers. A new native invocation gets
a new view; failures and closed inherited contexts do not retain cached data.

Raw input reuse is distinct from `read_view(root)`, which begins only after
bootstrap and can reuse derived validation. A follow-up authority map in that
derived view is keyed by its actual operational Result/Review readers. Adapter
installation is never memoized as a fixed authority result.

No writer or direct CLI opts in. Owner/role/claim/generation checks, alias byte
validation, the native omission fence and Source CAS remain at their existing
boundaries. There is no persistent cache, worker, credential or new startup read.

One isolated frozen local fixture with an empty comment stream measured the
same complete task output before/after. With the same cProfile instrumentation,
time changed from 41.151 to 30.407 seconds, and the execution store was actually
parsed once rather than 198 times. A separate unprofiled run on the same fixed
input took 14.797 seconds before and 9.498 seconds after, with equal complete
output and the same observed 66,796 KiB peak RSS. These are engineering fixture
observation, not production latency, fleet percentiles, a complete-history
migration proof or mathematical acceptance. Current production observations
and remaining event-collection work belong in the host's deployment handoff.
