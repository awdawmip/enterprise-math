# Shared-context static review of the structural shortcut successor

Verdict: no blocking implementation or checker defect found in the complete
candidate below. It is suitable for the coordinator's declared bounded run
after its actual startup guard. This is source review, not executed correctness,
independent review, admission, timing evidence or a full Shor result.

Reviewed complete files and exact SHA-256:

| File | SHA-256 |
|---|---|
| `shortcut_two_bit.py` | `874d5d79f67ef5a00176b48faa2959811b925820031a90f71f80b6ba6fd5a34b` |
| `check_shortcut_two_bit.py` | `e7dca9fe712c367ed5434ed88ac2027178bbf05fff1fb94373d77c8c01d39e22` |
| `DESIGN.md` | `b41ebf07ab34b9fa6981f529a5d230952b050786dd97f64eb1886827b1b3d667` |

I read these sources in full, the frozen structural proof `845df9a8...cfda7f`,
and the relevant frozen degree-three arithmetic source. The predecessor and
direct private progression contracts were already fully reviewed. This review
did not import a scientific module, compile or execute the checker, calculate
new numerical scientific values, or modify any implementation or design.

## Routing and arithmetic

`two_negative` (line 245) retains strict integer/stride/range validation and the
original `V|R` admission. It first constructs V and records R/V; a nonzero
alignment remainder rejects before constructing or testing original U/R.
Original U is `2^k`, not the compressed high bit. The cancellation result is a
typed zero, with explicit absence of orientations or progression execution.
The source does not use this theorem to silently widen its input domain.

On a surviving query, compressed U is obtained by exact typed original-U/V.
All scientific scales and coefficients use the frozen typed runner. Public bit
indices select the top-bit affine formula; no historical answer or measured cost
selects the route. Both outer heads are evaluated before either orientation,
matching the actual recorded chronological order. At r=0 the second head is R;
equal half-modulus heads retain two separate orientation records.

`_affine_progression` (line 146) computes each head's own canonical length. Its
q selection consumes typed `U-head`, a reached division, and typed
`candidate-n`, followed by a recorded selected count. The branch comparison is
on an observed result, not a host-arithmetic substitute for that result.
`_affine_T` (line 132) records every factor and exact division by two. At s=0,
the intermediate s-1=-1 is legal signed arithmetic and its product remains zero.
The final formula is the reviewed `M(2q-n)+T(n)-4T(q)`, with exact shared-junction
and empty-progression handling. Every shifted call recomputes n and q.

`_branch` (line 191) reads parity from the original compressed head. If the
observed low remainder is zero, it does not construct a shifted head or call a
shifted progression. The omission record has no invented result, length or
operation interval. For nonzero remainder it retains both sums, the signed
weights, independent canonical counts, and a typed proof that any removed
shifted point is exactly M. Thus A_one(M)=0 remains an empty overlap.
Non-top queries use the frozen direct private progression, not its whole-query
API. Raw denominator exponent 2g is preserved.

Host arithmetic in structural counters, list indices and raw exponent metadata
does not replace scientific sums or divisibility. The limits of eight private
progressions and sixteen top-level tables do not hide recursive moment or digit
cost. Empty requested progressions and omitted progressions are distinguished.

## Evidence, rejection and failure state

`two_negative` rejects an existing inflight request at its first entry, before
validation or new work. Export also refuses incomplete work. A paid unaligned
failure is therefore terminal for that observer; a fresh object is required.
It is not a resumable mathematical certificate. Snapshots and completed
certificates are deep copies.

`verify_shortcut_certificate` (line 323) applies the inherited strict JSON
semantics, source/proof/schema bindings, exact input field set, and actual
fresh replay. The final complete semantic comparison binds route reasons,
counts, scalar outputs, all nested moments and typed traces. Only the declared
native cache-call delta is excluded. Boolean and non-string-key mutations are
not normalized into valid integers or keys. With capture enabled, a completed
replay is preserved before mismatch rejection; a paid exception preserves an
incomplete snapshot. This is replay under trusted pinned synchronous source,
not an adversarial proof about an altered runtime.

The checker retains current observers, outputs, replay captures, typed-key
forgeries, input attempts and native CALLS for its main-run failure path. The
documented limitation is accurate: branch dictionaries still local at an
exception need not be present, though their completed raw operations remain in
the runner. Import failures and errors during failure-file persistence are not
covered. Existing success/failure paths cause refusal before another run.

## Declared checker and historical reuse

`load_history` (line 135) consumes the complete pinned predecessor gzip/payload,
checks the three old source pins and guard, imported arithmetic/proof pins,
positive replay semantics, values, tuple order and 720 saved pair records.
It imports neither the old checker nor its pair comparator. The new comparison
uses the saved 36 values; historical production, replay and pair enumeration
are not charged or advertised as newly executed.

The six planned fresh positive replays round-trip through JSON. The sixteen
tamper mutations address real reachable fields and change them: eleven require
a complete paid replay; one changes an input to an unaligned request and
requires a retained partial replay before the zero test; four reject early.
The ten early input controls and two paid unaligned controls retain their
separate categories. Two valid-input attempts on failed observers assert an
unchanged full snapshot and no additional native call; no subsequent work is
permitted on those objects.

Coverage checks distinguish cancellation, affine and direct fallback routes,
omission, nonzero shifted tails, empty calls, q=0/q=n/junction, negative values,
r=0 and half-modulus multiplicity. The design explicitly discloses that the
surviving even-compressed-step propagation branch is not re-exercised by this
six-tuple grid after a failed cancellation test. Its source logic remains
reviewed, but this run must not claim that missing execution coverage.

Costs are separated into new production, positive replay, paid input rejection
and negative replay. CALLS intervals are required to partition the actual
process record; digit, typed/signed, arithmetic wiring, bit-length and moment
counts remain distinct. Historical costs are comparison columns only. The
checker time includes history reading and later checks before serialization;
it is not a matched timing benchmark or evidence of general speedup.

The static checks establish no new actual cost or completed execution. Further
arbitrary-modulus top-bit theory is a separate unit and does not alter this
successor's aligned admission, source pins or intended evidence scope.

Global-Knowledge-Sync: main@9f0e65b / GLOBAL_KNOWLEDGE_V1
