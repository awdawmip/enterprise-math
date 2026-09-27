# Large-target native arithmetic: streaming record review requirements

Status: **STATIC_SOURCE_REVIEW / PRE_EXECUTION_REQUIREMENTS / NOT_EXECUTED / NOT_ADMITTED**.
This review reads the existing typed arithmetic and evidence readers. It does not fix the still-pending target interpretation, choose parameters from supplied factors, implement a new scientific runner, or run arithmetic. The target, proposal schedule and actual run remain the coordinator's separate frozen execution unit.

## 1. What the existing source actually retains

`lazy_modular.Arithmetic._retain` appends each complete trace to `self.operations`. Merely changing the final exporter to gzip will therefore leave all historical operations resident. `typed_integer_prechecks.multiply` and `divide` also construct each individual operation's complete nested trace before returning. Streaming at operation boundaries can remove cumulative trace retention; it cannot remove the peak memory of the largest single operation without a separately implemented and reviewed lower-level change.

The actual arithmetic is preserved if a new adapter calls the same typed functions and only changes retention. Addition is a carry transducer over the eight previously executed full-adder input columns. Multiplication is shift-add, retaining selected and bypassed digits. Division is binary long division with two full-adder passes for each comparison/subtraction. None of these three primitives has a loop over all residues modulo N.

Let n be the bit length of N and suppose both multiplication inputs are canonical residues below N. The product width is at most 2n and there are at most n selected additions, giving at most 2n^2 full-adder digit cells for multiplication. The product division has at most 2n binary steps. Its running remainder stays below N; hence the next shifted remainder is below 2N, each comparison width is at most n+2, and the two adder passes give at most 4n(n+2) cells for this reduction. These are symbolic upper bounds on saved digit cells, not measured bytes or timing predictions.

Thus 100--200-bit labels avoid a full-N carrier enumeration but still produce substantial records. The largest-operation peak remains O(n^2) cells plus integer labels, Python objects and serialization buffers. A public exponent with O(n) bits entails O(n^3) digit work for the existing modular power path, before setup, characters and observers. No claim of constant memory, practical runtime, or general factoring advantage follows from these bounds.

## 2. Safe adapter boundary

A new explicit streaming adapter can override retention while keeping the scientific primitive and its returned values unchanged. Its required contract is:

1. Each completed operation receives a monotonically increasing stream-local operation ID. Clearing `operations` must not restart IDs at zero. Outer links use an unambiguous `(run, route, stream, operation)` identity.
2. Compute costs from the complete returned trace using the pinned accounting rule. Preserve the whole trace, including carry, bypass, quotient and discarded comparison outputs. Do not replace it by the final answer or a host-computed checksum of an expected answer.
3. Serialize and durably commit the operation before returning its stable ID to the caller. Only then release every retained reference to that trace. A `deepcopy`, route export, closure, debug list or delayed outer record must not secretly keep a second full copy.
4. Retain a compact scalar result/ID ledger for outer wiring. Its growth and storage remain reported; operation streaming does not by itself make all metadata constant-space.
5. Reusing the old `typed_jacobi_trace` as-is still allocates its own `Arithmetic` and retains its operation list. A successor needs an explicit adapter/factory interface or a separately pinned implementation with the same recurrence. Silently monkeypatching the old module's global `Arithmetic` does not constitute an unchanged frozen interface.

An override may use the inherited typed entrypoints, account a completed operation, emit the temporary record, clear the list and return an independent monotone ID. It must not return the inherited `len(operations)-1` after clearing. Writer failure should leave a failed terminal observer with the last committed ID, not permit later calls to pretend the missing operation never occurred.

## 3. Durable stream and interruption boundary

One defensible framing is a concatenation of independently closed gzip members, each containing one newline-terminated JSON operation/event. Encode incrementally to avoid constructing a second full-size JSON string or compressed blob. Close the member, flush the underlying file, and apply the declared durability policy before exposing a committed byte offset. Ordinary flushing of one never-closed gzip member is not equivalent to a complete CRC/trailer-verified member.

The header should bind the literal input representation, parsed target, source/PLAN/dependency hashes, actual guard, schema, parameter policy and actual native full-adder catalog. Each subsequent record includes its type, sequence, route, referenced IDs and previous-record digest. The final manifest pins the complete raw/packed byte counts, hashes, committed record count and last digest. Hashing and serialization are administrative work; they never produce a mathematical result.

A small checkpoint names the last completely committed member/offset and the public algorithm stage. A malformed or truncated tail must not be silently accepted as a completed run. Recovery may verify the committed prefix, but it must distinguish a verified prefix from a complete final result. Unless a resumable operation-level state machine is separately proved, a failure is **FAILED / NOT_RESUMABLE**, with preserved completed records, current stage and available partial information.

The frozen primitive cannot expose every cell if it raises before returning its trace. State this limitation explicitly. Do not call the log a complete primitive-interruption snapshot. Likewise a process kill, disk-full failure or partial last member is not a valid successful footer. Exclusive STARTED, SUCCESS and FAILED protections must reject accidental repeat runs and preserve original failure bytes.

A first proper-factor result should be committed only after its actual factor-division witness, then exposed in a durable small result/checkpoint. A no-hit candidate should also have a committed outcome before the next candidate begins. Neither outcome needs to wait for a large final in-memory payload. Any partial batch status must distinguish completed candidates from an incomplete current one.

## 4. Arithmetic and outer-link invariants for the reader

The new reader should stream one operation/member at a time, reject duplicate JSON keys and invalid types, and verify the exact committed boundary. It can reuse hash-pinned I/O-only trace-checking definitions; importing scientific modules or rerunning their arithmetic is unnecessary.

Required native digit checks are the complete input-bit/carry code, catalog-column output, next carry, reconstructed low label, declared width and final carry. For multiply, consume the exact low-to-high bit order, incoming partial value, shifted term, selected/bypass decision and retained adder output. For divide, consume high-to-low input bits, prior remainder, wired shift, both compare adders, quotient bit and selected next remainder. The mathematical invariant is that the processed prefix equals quotient times divisor plus a remainder below the divisor; the reader should certify this through the saved native steps rather than using host multiplication/division as a replacement oracle.

For modular multiplication, the exact multiplication output must feed the reduction's dividend and the declared target must be its remainder. Modular subtraction must bind canonical inputs, the comparison and any actual add-N branch. Euclid must bind each saved dividend/divisor to the preceding remainder and retain the zero termination. A common-coordinate gcd must carry the accumulator and consume every declared coordinate in order. Proper factors require the recorded positive-divisor test and actual N/factor division with zero remainder, never the supplied reference factors.

For Jacobi, bind its typed initial numerator/remainder, all factor-of-two wiring, reciprocity sign updates, descending denominators and terminal gcd to the exact producer of Delta or k+2. For the public clock, bind the actually computed character to actual typed construction of E=N-j. For adjacent traces, bind each public exponent bit to the ordered incoming pair, cross multiplication, selected square, both subtractions and outgoing pair. Do not fold orientation: the translated second-clock observer is not invariant under that fold.

Every signed expression, joint gcd, scalar union and exact second-clock quotient needs explicit chronological IDs. A claimed quotient must use the actual union and first-clock divisor, with an actual zero remainder and factor validation when proper. Matching values alone cannot substitute for links to the correct run, target, sign and clock.

## 5. Input isolation and honest costs

The supplied full decimal target and the separate p,q values are presently distinct user data. Freeze the selected interpretation only after the coordinator resolves it. Do not silently replace the full string by a remembered product. If a product comparison is requested, perform it through a separately charged typed validation path and record that path's input provenance. The reference p,q values must not influence k, character acceptance, clocks, retry order, stopping policy or candidate construction. An input mismatch is evidence to report, not a license to repair the target silently.

Report separately the actual native catalog calls; typed operation and digit-replay totals; label bit wiring; source/guard verification; record bytes and persistence costs; rejected proposals; mathematical production; reference-input checks; factor validation and any independent replay. A cached catalog call count of one is not a claim that the full computation cost one BRC operation. The frozen `trace_cost` scope excludes serialization, allocation and Python internals; preserve that qualification.

The current task provides a source-based memory/correctness review, not a feasibility benchmark. Final approval needs the actual new source, PLAN, target/schedule binding, writer and reader failure semantics. No scientific run has been started by this review.

## Read sources and provenance

- `D:/em/TEMP/sep26-shor-general/optimization/lazy_modular/lazy_modular.py`: Arithmetic retention and accounting; SHA `08df3595a2a56dc2501bb481828093481bf76e4ac53c8b966990d233fefac1e4`.
- `D:/em/TEMP/sep26-shor-general/completion/typed_integer_prechecks.py`: full multiply/divide/add/compare implementations; SHA `0a817aa8124cceb5440233d543073dae71de6ac1d0d4e5d50f4ee2b4808d99eb`.
- `D:/em/TEMP/sep26-shor-general/sparse/sparse_modular.py`: actual native full-adder catalog and digit records; SHA `fd9cbb019418a3c00890ba6e8cca5760e7e4d792bfd7b48306a71a66de301c46`.
- `D:/em/TEMP/sep27-brc-native-tool-discovery/native_relative_port.py`: Route ownership/export retention; SHA `0821cf958b99988b5dbb95f5a42b97629155ca80c07e1f5bee8e2e9165bc39a8`.
- `D:/em/TEMP/sep27-brc-native-tool-discovery/read_native_port_review.py`: existing I/O-only native-cell and typed-operation audit pattern; SHA `dc88b155de7ec5bf8222b940a942f08d4963e478f9a5bf66c5826d244b7d2825`.
- `D:/em/TEMP/sep27-qft-research/character_certificates/typed_jacobi.py`: the generic Jacobi function's local Arithmetic retention and typed remainder recurrence; no QFT schedule theorem is reused.

Only the named interfaces/sections were reviewed for this bounded task. Frozen sources were not changed or imported. Global-Knowledge-Sync: main@b304760 / GLOBAL_KNOWLEDGE_V1, reusing this agent's actual helper lease and complete canonical entry-file read from the ongoing phase. Shared-context author review, not independent admission.
