# Segmented view correctness execution and cost

The single declared bounded execution passed. This is shared-context author
evidence, not formal independent admission or a general Shor-complexity result.
The scientific source and checker were unchanged between review and execution:

- `segmented_so_view.py`: `90c773c74a81ed239e32fcc12fa8d238032d6fbcfef3f4d6eb2056856666ed99`.
- `check_segmented_so_view.py`: `6e226c8d54e41020aeb0d5d5126ba31b2c10f3dedcba7d17d5fd45550815db03`.

The new-stage startup guard was actually PASS. The run retained complete stdout
in `SEGMENTED_VIEW_EXECUTION_LOG.txt`, all native calls and successful table
instances in `SEGMENTED_VIEW_RESULTS.json.gz`, and compact metadata in
`SEGMENTED_VIEW_SUMMARY.json`. `extract_segmented_view_cost.py` only decompresses,
checks hashes and accounts for existing receipts; it imports no scientific code.
It verified the saved source hashes against the current files and reconciled all
1,116 native core calls. No failed-execution artifact was produced and no second
scientific run was made.

## Observed correctness

For N21/a2 and N21/a4, t4, epsilon 1/3 and history 1000, all eight positive steps
matched the frozen SO boundary: conditional plans, pending decisions, numeric
committed ledger, terminal masses, complete saved signed covariance matrices,
entire observer streams, native/policy counters and guard-call topology. The
6-coordinate carrier used only the existing exact codec following full 61-column
native admission. No residual coordinate or noncommuting word was dropped by the
new guard. Cursors deliberately have a new schema, policy, source and view token.

New-version pending restore replayed deterministically. Eight cursor negatives
were rejected: source, profile, token hash, bank hash, selected word, charge,
Boolean history and an old SO cursor. A bounded query interruption retained its
pending decision, restored public guard depth and successfully retried the same
bit once. The failed attempt had one observer receipt; the final retried object
had two, so those snapshots are overlapping evidence rather than three observers.

All 15 runtime controls rejected before any new native core call or observer.
These include changed phase metadata at all eight public entries, changed codec
metadata, a copied token, wrong bank type, a distinct same-content exact SO bank,
wrong constructor bank type, and actual frozen-word/column replacements. The nine
metadata changes reached the frozen compatibility reject path; native replacements
were rejected by the unchanged Adaptive snapshot. Every rejected public entry
returned to depth zero with no owner retained.

Eight pure-JSON examples also passed, including the noncanonical numeric-key
compatibility acceptance. That acceptance is a metadata predicate example, not
an actual t10 scientific program. The actual t4 programs exercised normal fast
acceptance and frozen slow rejection. Their tokens were never refreshed.

## Nonoverlapping cost allocation

| Component | Actual native core calls |
|---|---:|
| Complete native bank/program admission | 244 |
| One unchanged cold SO certificate bank | 36 |
| Four fixed-prefix engine objects | 412 |
| Original restore object and fresh replay | 144 |
| Rejected cursor fresh replays | 276 |
| Interrupted/retried object plus fresh comparator | 4 |
| **Total** | **1,116** |

The six modified non-Boolean pending cursors each consumed 34 actual observers
before strict replay rejection; the old full SO cursor consumed 72. Boolean
history was rejected before replay. These 276 calls are retained as failed work,
not silently omitted from the total. Runtime metadata/type/object negatives cost
zero native calls but still performed host validation work.

The unchanged cold bank used 36 signed observations. Its three words still
required complete forward, inverse and recovery basis traversal, at least
549 full-vector basis actions. A warm lower-level primitive cache does not make
that native replay free. Its observed setup time was 1.5464755999855697 seconds;
this is one cold setup observation, not a performance comparison.

| Fixed prefix route, each old/new | Native phase vector actions | Gram requests | Distinct matrices | Observers |
|---|---:|---:|---:|---:|
| N21/a2 | 120 | 76 | 22 | 80 |
| N21/a4 | 168 | 58 | 13 | 126 |

Each honest old and new fixture recorded 22 logical binding checks including its
constructor, with identical nested guard topology. The old implementation invoked
the whole frozen check 22 times. The new implementation invoked it once at
construction and performed 21 complete segmented fast comparisons. Thus the
optimization preserves complete binding checks; it changes their representation.

Across the 13 nonoverlapping constructed segmented-engine snapshots (including
replays), the recorded totals are 13 constructor checks/token derivations, 122
segmented attempts, 113 fast accepts, nine compatibility checks and nine
compatibility rejects. No actual program compatibility acceptance occurred.
There were two bank-identity rejections and one token-identity rejection. The
actual old frozen method was invoked 22 times on these segmented objects, equal
to 13 constructors plus nine slow checks. The two old comparison objects account
for another 44 invocations. These are host counters, not extra native calls.

Each token retains three payloads of 235,766, 235,524 and 235,745 bytes: 707,035
additional segment bytes per token. This excludes Python object and allocator
overhead and transient encodings. Multiplying it by every historically created
object would not establish peak live memory. The already-stored bank view remains
available; source hashes and token hashes do not replace the bytewise comparison.

The two programs shared ten concrete factory/inverse table instances across all
routes and replays. Counting these final instances once gives 3,661 setup plus
3,116 column adder-digit replays, and 2,833 program permutation-verification digit
replays. The table caches contain 39 computed columns, with 296 requests and 257
hits. Per-engine cumulative table reports are not summed again.

## Evidence and limitations

The raw payload is 15,658,784 bytes with SHA-256
`12f5528102c5c6f84ff35d2fa6bef1c601ccb09111129365114a67622b4cfbf3`.
The gzip is 594,656 bytes with SHA-256
`3578a052c1fda612f854fe2f0a479ccdca4f0feb6b42d48f0100b84eaee79b8a`.
The entire checker took 14.359182399930432 seconds before final compression. This
is correctness-run wall time; it proves no speedup. No matched benchmark,
full-history law enumeration, stochastic trial estimate, total host bit-cost or
process-memory measurement was performed in this execution.

Predicate equivalence is restricted to a fixed original bank after the
constructor's canonical-wrapper gate. The new identity contract is intentionally
stricter about replacing that bank with another instance. Both retain the ordinary
synchronous trusted-Python boundary. Source/schema pins and the canonical gate
are not claims of resistance to arbitrary monkeypatching.

The unexpected-failure collector was inspected and compiled, but no new injected
scientific failure was run to test it. It preserves available engine fields,
completed blocks, attached replay evidence and the independent actual call
stream. An unfinished constructor object is not available; unexpected-failure
capture does not separately promise all mutable program-table receipts. The
successful payload does include full final table instances. Frozen modules and
the completed scientific source remain unchanged. A separately reviewed future
benchmark is required before any warm host-performance claim.
