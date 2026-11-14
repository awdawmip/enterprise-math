# Exact review/follow-up validation in one immutable read view

The host already limits its immutable and derived read contexts to task,
continuation, dispatch and inventory reads. Within that existing scope, the
review-audit validator and the composed follow-up validator can reuse their
first successful result. They retain the same schema, blob, hash and exact error
checks. Results are copied for each caller and discarded with the invocation.

Raw review/result records may be reused across bootstrap because their JSON
bytes are immutable. Derived validation is reused only after bootstrap installs
its operational adapters. Validator and operational-reader identities are part
of the cache inputs, so replacing them forces recomputation. Exceptions are not
cached. Direct CLI and protected writer paths do not opt in and continue to
revalidate normally. No current owner, role, lease or authority is granted.

The diagnosed frozen input contains 1,293 captured public Issue comments,
1,121 normalized events and a fixed evaluation time. Before this change one
profiled dispatch called exact review validation 588 times and the composed
follow-up validator 232 times. Full input and guarded scoped input produced
identical outputs; the profiles took 137.119s and 184.078s respectively, including
profiler overhead. They are local observations, not live percentiles.

The first candidate produced the same complete output as the baseline: profiled
full/scoped timings changed to 95.350s / 130.225s. Its 45 regressions and 39
subtests passed. A further JSON-container copy fast path retains shared aliases,
cycles and custom deepcopy protocols; its final same-input timing is reported
separately. These frozen comparisons use a counterfactual evaluation time;
they do not reconstruct historical live ownership.
This optimization does not omit authenticated event history, remove a quarantine,
change a review disposition or migrate formal authority. Activity and independent
scientific publication remain separate from protected Result/Review actions.
