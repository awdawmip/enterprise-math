# Executed intermediate coherence skips with complete recovery

Status: AUTHOR_ACTUAL_BOUNDED / SHARED_CONTEXT / NOT_ADMITTED.
Activity RA-CAAAC604CB513AEA8BBC1DFC. This is a native-instrument experiment,
not an ideal-QFT reference or a general Shor factoring benchmark.

## What the implementation changes

`coherence_skip.py` learns one fixed set A from 32 independent preparation
paths at depth 2, freezes it, then tests it on 96 independent held-out paths.
For each held-out W it observes the single union event

    W outside A OR P_2 W inside A.

The two constituent events are correlated and are never counted as independent
trials. The exact existing typed binomial-tail observer tests r<=d with
confidence budget 1/32. There is one predetermined attempt, not repeated
selection until passing. Conditional on a valid certificate, replacing the
whole depth-2 score by a fair bit has joint error at most sqrt(d(1-d)).
Unconditionally the one-attempt outer algorithm has error at most that value
plus 1/32. A failed certificate automatically runs the complete exact sampler.
Different software seeds are test fixtures, not a proof of random independence.

At every other step the sampler queries the complete exact rows for its
actually recorded history. It preserves all 61 internal coordinates and the
complete noncommuting native feedback. There is no approximate state field.
On a zero-reference parent label the original exact-only transition routine
could reject the trajectory. The new routine instead uses the exact score
whenever its queried pair is nonzero and a fair extension when both rows are
zero. The error proof uses the norm-law invariant only under the exact
reference process; it never assumes it for the approximate process.

The fixed source/state contract is the same admitted live program. Metadata,
certificate, history and external latent replacement checks are implemented;
detecting arbitrary runtime monkeypatches of dependencies is not claimed.

## Actual full joint-law checks

All three cases use the actual t=4, full-D61 bank. Each checks all 15 parent
histories and the entire terminal joint law of measured history and work label.

| N,a | cap | d | observed union misses / 96 | actual r | route | terminal joint TV |
|---|---:|---:|---:|---:|---|---:|
| 35,2 | 8 | 1/16 | 0 | 0 | certified intermediate skip | 0 |
| 129,4 | 8 | 3/8 | 24 | 1/4 | certified intermediate skip | 324022679/4294967296 |
| 129,4 | 1 | 1/16 | 75 | 3/4 | automatic exact fallback | 0 |

The second case has nonzero actual error and two subsequent transition plans
whose incoming parent row has exact norm zero. They successfully recover via
the full nonzero row pair. The separate N3/a1 impossible-history fixture
executes the both-rows-zero extension. These are concrete tests of the
off-reference interface, not only a symbolic assertion that it is needed.

The checker verifies both the measured local absolute-coherence telescoping
bound and the union-event bound. Raw positive path observers, full exact
states, point-row receipts, table instances and actual core calls are stored.
Rehashed false miss counts and externally changed latent labels are rejected.
Interrupted random sources preserve the previously drawn auxiliary bit.

The full checker made 45,065 actual native core calls in one local run of
136.95 seconds. Those counts include exhaustive validation, certificate
replay, negative controls and resume tests; they are not per-output costs.
Payload SHA256: 291b0b73a4d130df2e670312ca5c12faead5cbd474b44c792eec8dcfa1158159.
Gzip SHA256: 681b822fd5113b902c060991a158b75116ab921fd1f24bd2f87d5cf44e5b005e.

## A matched query comparison that prevents a false speedup claim

`check_matched_cost.py` reads back the actual serialized training/validation
certificates and runs the ordinary exact sampler and the new sampler on the
same feasible all-zero proposal/readout tape, using separately admitted
programs. This tape specifies a positive-probability path; it is not presented
as fresh uniform randomness or a distributional timing benchmark.

| N,a | distinct exact row queries | distinct skip row queries | final query-key sets |
|---|---:|---:|---|
| 35,2 | 26 | 26 | identical |
| 129,4 | 20 | 20 | identical |

The skipped round does make zero row queries immediately. However, later
queries recursively construct the same missing ancestor rows. Therefore
these intermediate skips show **no reduction in distinct row queries on the
compared paths**. Certificate training, holdout and replay add work. A total
runtime or memory improvement is not established. A terminal suffix can have
different behavior because no later exact query reconstructs its rows.

The cost checker also actually stops at a point-query budget of one, increases
the explicit budget and resumes both accepted cases without losing cached rows
or redrawing the pending auxiliary choice. No incomplete run is discarded or
conditioned away. It made 4,782 actual native core calls including constructor,
certificate replay, baseline, sample and resume work.
Payload SHA256: 8d92f3330310f5122d036550a13343ff829b598157569ff8b173fe7d96452e8f.
Gzip SHA256: 969ce9e93619f307b07f359473e33175d6472d1719df8f5ffbffdd8fc9cbde61.

Full instance accounting is a separate file: inherited branch-evaluator
counters alone omit this row/proposal route, and cached calls are not zero
work. Constructor verification, modular digits, core calls, random draws,
query requests, retained rows and complete evidence are distinct resources.

## Consequence for the research direction

This proves and executes a correct approximate layer replacement with actual
later recovery. It does not solve the expensive coherent-row backend. The
separate exact preparation-fidelity formula shows why all norm-only label
partitions become weak in a substantial standard Shor regime. The next useful
improvement must avoid reconstructing skipped ancestors and use signed/internal
correlations or another stronger representation, with a complete cost proof.
