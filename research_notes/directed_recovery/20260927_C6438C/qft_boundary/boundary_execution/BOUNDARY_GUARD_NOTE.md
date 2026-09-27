# Boundary-checked uniform policy: implementation and bounded evidence

This is an author-executed guard optimization in the existing actual native
program. It changes where immutable word-certificate metadata is checked. It
does not change a phase word, gate-omission decision, Gram recurrence, signed
residual, measurement normalization, or error-charge rule. It is not a new
efficient Gram oracle or a formal independent mathematical admission.

## Implementation contract

`BoundaryCheckedUniform` inherits the frozen `UniformFeedbackGram` and its paid
`WordCertificateBank` admission. The constructor checks both dependency files
against pinned SHA-256 values. Every outer call to `gamma`, `mass`,
`probabilities`, `advance`, `prepare_next`, `cursor`, `evidence`, or `report`
checks the actual program snapshot and ledger, the exact certificate-bank
Python type, its admitted binding identity, and the bank's complete strict
serialized program/provenance view. Nested calls during that synchronous
operation retain the original `AdaptiveFeedbackGram._check` snapshot and
committed/pending ledger checks but omit repeated full bank serialization.

A reentrancy counter and thread owner bracket each public entry. `finally`
restores the counter even after an error. Concurrent use of an already active
object from a different thread is rejected. The contract still uses ordinary
trusted Python objects: private underscore methods are not public entry points,
arbitrary monkeypatching is outside the boundary, and the caller must not mutate
the program externally during one synchronous outer operation. This is not a
thread-safe or hostile-object API. No substitution of ordinary Python equality
for the strict certificate serialization has been made.

Conditional correctness follows directly. At outer admission the complete
bank/program/type/provenance binding is checked. Under the no-external-mutation
condition, it remains valid until return. The existing snapshot and ledger
checks continue at internal computational boundaries. All numerical methods
then execute the same inherited code with the same state and admitted words.
Their returned numerical values and committed word/charge ledger therefore
remain those of the frozen uniform policy. The additional guard accounting is
host metadata, not a native arithmetic operation.

`BaseException` unwinding restores the guard depth. This does **not** strengthen
the inherited transaction contract: the inherited `advance` rolls back a
provisional history on `Exception`, including `QueryBudgetExhausted`; it does
not promise full ledger rollback on a `KeyboardInterrupt` during the commit.

The new cursor is `BRC_BOUNDARY_UNIFORM_CURSOR_V1`, with a distinct policy,
implementation hash, uniform-source hash, and guard-contract field. Restore
uses the inherited deterministic prefix replay and exact strict-byte cursor
comparison. Old-stage cursor bytes are intentionally incompatible. The object
does not claim durable restoration of its query cache or an RNG tape.

## Executed bounded scope

`check_boundary_precheck.py` uses the existing admitted direct-word bank, full
61-column admission, and exact first-six reachable-carrier codec. It compares
old and new policies on `(N,a,t)=(21,2,4)` and `(21,4,4)`, each following the
positive prefix `1000`, with error budget `1/3`. At all eight transitions it
checks exact equality of both conditional child masses, prepared policy
decisions, full signed covariance at residue one, selected-child positivity,
raw committed mass, and the full executed word/charge ledger. It also compares
all retained correlation records. No ideal-QFT reference was used.

All eight public entry points reject all five malformed-input classes before
any native or observer operation: strict metadata `True` replaced by integer
`1`, a changed word, a changed native column, a changed codec, and a history
inconsistent with the committed ledger. The word/column fixtures replace a
frozen dataclass instance temporarily; they are never propagated. All 40
rejections leave the outer guard at depth zero. The test restores each malformed
input before any further honest call.

Six changed serialized cursor fields/types and one old-stage cursor are
rejected. The new cursor passes serialized replay, including a prepared pending
decision, followed by the same next bit. A query budget of two triggers the
inherited provisional-commit rollback; the pending decision remains, the
selected bit is uncommitted, and guard depth is zero. Increasing the budget and
retrying that same bit gives exactly the fresh one-bit cursor and mass. Failed
replay/rollback evidence and the later successful replay evidence are retained
separately. Evidence captured before further mutation is detached with
`deepcopy`; otherwise inherited evidence contains live receipt/list references.

The final checker passed with 1,251 native-core calls in 17.8909774 seconds.
This elapsed value includes admission, comparisons, negative controls and
replays. It is **not** a matched performance benchmark or a complete-law run.

| Fixture | Old/new native phase-vector actions | Old/new distinct Gram queries | Old/new positive-path observations | Old/new full-bank checks |
|---|---:|---:|---:|---:|
| N21, a2, prefix1000 | 120 / 120 | 22 / 22 | 80 / 80 | 117 / 23 |
| N21, a4, prefix1000 | 168 / 168 | 13 / 13 | 126 / 126 | 93 / 23 |

These counters are the retained fixture evidence snapshots after this checker's
explicit comparison/inspection calls. They must not be presented as costs of
one minimal sampled trajectory. Native vector actions, native-core calls,
typed digit work, and host serialization are different resource units. Shared
program modular-table reports are cumulative and must not be summed across
old/new snapshots. The complete raw evidence retains the table instances and
native calls; no complete host bit-cost claim is made.

The boundary object recorded maximum nested depth five, while each completed
outer result records depth zero. A nested report embedded in outer evidence
can correctly show depth one at the moment that nested report returned; the
outer `boundary_guard` diagnostic is the final zero-depth snapshot.

## Evidence binding and execution history

- Implementation: `875133020ba713af755d19b121f416938193835c3e2c9b7e6ab228c19b814c83`.
- Final checker: `75c459d8b52378e9018a5cdf2158eec7705d7b70caded5545e209529c39058a5`.
- Frozen uniform dependency: `755d398a19881508112c9e360c94bf10133681af8d3cbdbb103accdecc306e28`.
- Frozen word-bank dependency: `c3e8156b5c7573778cd1e781f23e82394c83842a9f4655b59c9659035dc62ce3`.
- Raw payload: 14,004,778 bytes, SHA-256 `41cfe8eb1a88c10153c99f6524efcd10a9784cd363da48e8229aed32e1300b71`.
- Gzip payload: 479,959 bytes, SHA-256 `e2f1edabc9223bc9216abcca83fd98b065c6ef53439ac62d23ff4c28802a15f9`.

An earlier checker attempt stopped before writing its final artifact because
its malformed-input fixture tried to assign a field of a frozen gate object.
That attempt's native receipts were not persisted, so its work is neither
included in the final 1,251-call total nor described as passing evidence. Static
review also identified live intermediate evidence references; both checker
issues were corrected before the final run. The algorithm source did not
change between these attempts. The final log and raw artifact are retained.

The next controlled comparison may alternate old/new order on the same paid
bank and matched warm modular tables, timing only matching public computational
calls. Cold admission and evidence serialization must be accounted separately.
Reducing repeated metadata checks is demonstrated here; a general Shor speedup
or a full-program wall-time improvement is not established by this precheck.
