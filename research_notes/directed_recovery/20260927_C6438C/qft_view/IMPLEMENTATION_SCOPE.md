# Segmented view adapter: implementation and declared bounded check

Status: source implementation and compile-only validation. No adapter import,
metadata predicate trial, native scientific execution or performance experiment
has been run for this unit. `DESIGN.md` remains the earlier frozen design; this
file records the subsequent implementation scope.

`segmented_so_view.py` defines `SegmentedBoundarySOTrace`, a new subclass of the
frozen `BoundaryCheckedSOTrace`. It accepts the same program, rational epsilon,
query budget and optional exact `SOTraceBank`. The old scientific modules and
bank remain unchanged. The constructor runs the frozen actual bank constructor
or supplied-bank check before deriving its token. It retains the old dependency
checks and adds explicit pins for the policy, SO bank and native-view helper.
These duplicate constructor checks are paid host work; they are not repeated
source-file reads on every public entry.

The immutable token is derived only from the admitted bank's `_view_bytes`.
Its three byte strings, profile, bank binding and new adapter source are fixed.
Each outer public call still runs the original complete `_program_view` and
compares all three byte strings. A mismatch invokes the exact frozen
`SOTraceBank.check`; slow acceptance never updates the token. The supplementary
token hash is provenance, not a replacement for full bytes.

The parent constructor does not call a public entry before token initialization.
Six decorated public methods are inherited. `cursor` and `evidence` each have
one decorator and call the undecorated SO policy implementation directly, so
their existing nested-call topology is preserved. Every inner recurrence still
uses the original Adaptive snapshot and committed-ledger check. The new cursor
schema/profile/source intentionally differ. The inherited classmethod restore
constructs this new class, performs admission, derives a fresh token, replays
the actual committed/pending policy and compares the complete strict cursor.
Neither an external token nor a serialized claimed hash can skip admission.

The equality claim concerns the program-view predicate **with one fixed admitted
bank after the constructor's canonical-wrapper gate succeeds**. Specifically,
`S(J(bank._view_bytes)) == bank._view_bytes` must hold before deriving E; otherwise
normalization of native fields could make E correspond to a different wrapper.
The source correctly rejects such a noncanonical wrapper. The constructor domain
can therefore be narrower than all hypothetical frozen-bank wrappers, even
though the ordinary generated native tuples/lists/primitive values pass this
gate. No universal bank-constructor acceptance equivalence is claimed.

This adapter additionally requires the bank object to be the original
object, as the design specifies. An otherwise honest second bank with the same
binding is therefore rejected, although the prior SO boundary accepted it.
No claim is made that the entire mutable-object API has the identical acceptance
set. Ordinary synchronous trusted Python objects remain the boundary: arbitrary
method replacement, mutation of private reference baselines or frozen fields
through low-level bypasses, and concurrent external mutation are not supported.

The counters distinguish constructor frozen checks, attempted segmented checks,
fast accepts, frozen compatibility checks/accepts/rejects, raw-view construction
failures and identity failures. Inherited `bank_check_*` and policy binding
counters describe logical successful binding operations, not the count of old
method invocations. An attempted component encoding that raises is an attempted
segmented check, but is not a compatibility check. The full old method invocation
count is explicitly constructor checks plus compatibility checks. All counters
are host diagnostics. The retained guard restores depth/owner with `finally`;
that is not a stronger `BaseException` transaction-rollback promise.

The proposed checker has one unchanged full native admission and cold SO bank,
then N21/a2 and N21/a4, t4, epsilon 1/3, positive history 1000. It compares old SO
boundary and new adapter conditional plans, full retained signed covariances,
observer streams, numeric committed ledger, native/policy counters and guard-call
topology. These are fixed-prefix correctness checks, not independent random
trials, a complete-law experiment or a matched wall-time benchmark. Shared typed
modular caches are recorded once by concrete factory and inverse instance.

The checker also declares:

- Eight pure-JSON predicate examples, including numeric-key compatibility
  acceptance, no token refresh, bool/int and float/int distinctions, and the
  tuple/list equality already imposed by JSON. These are schema examples, not
  real program admission or native arithmetic.
- Fifteen actual runtime rejection controls: changed phase metadata at all eight
  public entries, one codec-metadata change, forged same-content token, wrong bank
  type, distinct same-content bank identity, wrong constructor bank type, and
  frozen word/column replacements. Rejection must unwind to depth zero with no
  new native core call or observer. Word replacements use `dataclasses.replace`,
  preserving the immutability of the frozen native word objects.
- New-version pending restore, eight cursor rejection cases including old SO
  cursor, and a bounded query interruption followed by the same selected bit.
  Intermediate inherited evidence is detached before any continuation because
  its contained receipt lists are otherwise live.

Any prior success, summary or `FAILED_EXECUTION_*.json.gz` refuses a new run;
existing evidence is never overwritten. An unexpected failure is retained
under a distinct `FAILED_EXECUTION_*.json.gz`, with the actual call stream,
known stage, hashes, traceback and any attached replay evidence. A private LIVE
registry retains completed blocks and current constructed engines. The exception
collector reads existing observer operations, correlation-cache numerators and
denominators, history, committed steps, pending decision, certificates,
interruptions and native/policy/guard counters. It does not invoke `evidence`,
`report`, `mass`, a guard or any other scientific method. Each block/field encoding
failure is recorded separately, and source/attached-evidence capture failure
does not prevent preserving the independent complete actual call stream.
Completed fixture/negative/restore/retry blocks are retained as they become
available. This collector has only been inspected/compiled; no new scientific
failure-injection run is claimed. Constructor
failures are not newly guaranteed to attach a complete partial object; the
outer checker still preserves the calls already made. This is the same limited
failure-evidence boundary already stated by the frozen parent bank.

The only design-level testing deviation is that the noncanonical key-order
compatibility success uses a pure JSON fixture. It does not enlarge the admitted
actual phase bank from t4 to t10 merely to create that metadata ordering. Actual
program tests cover the fast route and mismatching frozen rejection route. The
equivalence proof, not an unexecuted large-bank example, covers the remaining
accepted noncanonical views.

After source review and a current new-stage `STARTUP_GUARD.json`, the declared
command is:

```powershell
& 'D:/kimi-query-bridge/.venv/Scripts/python.exe' 'D:/em/TEMP/sep27-qft-view/check_segmented_so_view.py'
```

This command has not been run. There is no speed, scientific-accuracy or general
Shor compression result in this compile-only unit. The segmented token consumes
additional persistent metadata memory; the fast path still serializes every
complete native field and both binding payloads once.
