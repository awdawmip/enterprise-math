# SO trace policy: pre-execution code review

Status: **PASS_STATIC_REVIEW / SHARED_CONTEXT_REVIEW / NOT_FORMAL_ADMISSION**. No material defect was found in the two inspected files. This is a static assessment of the already authorized bounded test scope, not a claim that its execution passed. No scientific calculation was run and no implementation file was edited by this review.

Inspected source bindings:

- `policy_execution/so_trace_feedback.py`: `62121d7c1e1a7eafff452990b991ddfe027e65ada5e980881aa4d716de92bd20`.
- `policy_execution/check_so_trace_policy.py`: `1c041d9c45d1e0d3907da60acb87cafe10c39d7c328dea08e38eafe8c19aadad`.

The review also read the pinned Uniform and Boundary source and the relevant Adaptive constructor, checks, transaction, evidence and cursor routines. The complete native SO bank was separately reviewed in `SO_TRACE_BANK_REVIEW.md`; that actual bank execution does not by itself establish this new policy's runtime result.

## Bound semantics and history selection

Both new constructors require the exact `SOTraceBank` type; the guarded class repeats this requirement and the admitted binding-identity check at outer public entry. There is no old-bank type impersonation or modification of a frozen class. Policy decisions use `bound_valid`, with method and exactness retained separately. They do not treat a generic SO trace upper bound as an exact norm.

The policy retains the same temporal reference list and removes only its first, oldest word. Past choices come from immutable committed steps; the currently prepared choice comes from pending state. No commutation of different phase words is assumed: removing the end factor preserves the relevant operator-distance bound under the remaining orthogonal product. The complete-carrier certificate applies through the already admitted exact codec.

The actual signed observer evaluates `8s-s²-16e²`, after requiring `0<=s<=4`; the inherited constructor requires `0<=epsilon<=1` and the actual remaining-charge check enforces `0<=e<=epsilon`. Because `sqrt(s/2-s²/16)` is increasing on this interval, a valid squared-norm upper bound is sufficient. The determinant-minus-one bound 4 is handled correctly, even though this bounded checker uses the existing three SO words.

The omission policy makes no prefix covariance or mass observation. Its zero-mass extension is a valid state-independent operator bound, while inherited probabilities still refuses zero-mass conditioning and advance refuses a zero-mass child. This does not confer an ideal-QFT accuracy certificate on arbitrary native words; the comparison reference remains the admitted actual bank. Spending the entire remaining budget on an accepted omission is unchanged from the frozen policy.

## Transaction, guard and restore

Adaptive `_check`, `_gates`, recurrence, probabilities and advance are inherited. Internal reentrant calls retain the Adaptive source snapshot/history/pending-ledger checks. The exact pinned public-boundary context manager supplies outer bank checks, owner/depth diagnostics and `finally` unwinding for all eight public methods. The inherited synchronous trusted-object contract remains necessary; this is not a concurrent-object or arbitrary-Python-tamper API.

On an ordinary exception during the new-depth mass validation, the inherited advance restores the previous history, steps and pending decision, discards uncommitted deeper cache entries, and retains the actual work and interruption record. The same selected bit can be retried. Guard unwinding covers `BaseException`, but full ledger rollback still covers `Exception` only; the new code adds no general KeyboardInterrupt transaction promise.

The reused classmethod restore constructs its `cls`, so the new constructor and public transactions actually run. It is not an old-class reconstruction. Full strict cursor bytes bind the new schema, policy, source, SO bank, parent/template sources and guard contract. Typed Boolean history is rejected before construction; other valid-shaped corrupted cursors may pay deterministic replay before rejection. Old cursor bytes intentionally fail. Cache contents and random tape are not restored.

The old restore routine catches replay exceptions after construction and attaches the new object's evidence. As with the separately reviewed bank, a constructor failure before that object exists is not a general partial-constructor receipt API. The checker supplies an outer failure record for unexpected exceptions. Inherited evidence contains live lists, so the checker correctly deep-copies stored intermediate and completed snapshots.

## Bounded checker and accounting

The planned two fixtures are N21/a2 and N21/a4, t4, history `1000`. They compare each actual conditional mass, full signed covariance, selected word/charge/bit semantics and raw mass. They also compare the complete saved correlation and signed-observer streams, while deliberately allowing new certificate hashes and cursor bytes. Numeric equality here is not used to bypass certificate binding: strict cursor equality is used for new-policy replay, and full source/bank admission precedes comparison.

The planned negative controls cover seven malformed/old cursors plus old-bank rejection at construction and outer entry. Attached failed replay evidence is detached and checked after guard depth returns to zero. The query-budget-two case captures the failed parent, increases the budget, retries the same bit, and compares against a fresh path. These checks are meaningful and bounded; their PASS assertions have not yet been consumed as executed evidence by this review.

Initial admission, both cold bank receipts, complete global native-call records, per-failure call intervals, and final distinct program table snapshots are retained. The outer unexpected-failure handler uses an exclusive new artifact and preserves source hashes, context, traceback and actual calls rather than emitting PASS. Its existence is not proof that its own failure path was exercised. Per-fixture timing and exhaustive host/digit/memory cost are not supplied, so no matched performance result follows from this checker. Shared cumulative table snapshots must not be summed repeatedly when costs are later extracted.

The declared scope is appropriate: eight fixed positive prefix steps, strict restore and rollback checks, not full output laws or a random sampler, and not a general Shor complexity improvement. Final execution claims require the resulting raw artifact and source hashes to be checked after the authorized run.
