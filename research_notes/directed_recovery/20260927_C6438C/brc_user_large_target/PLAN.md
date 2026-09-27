# Fixed public-clock test of the two supplied target interpretations

Status: FROZEN_INPUT_PLAN / CODE_ONLY_AT_AUTHOR_HANDOFF / NOT_YET_EXECUTED / NOT_ADMITTED.

This unit evaluates one public proposal, k=3, on each of two explicitly separated inputs. It does not substitute the displayed block for the complete decimal input. The coordinator's separate actual typed input-integrity run established that the supplied p and q multiply to the block and that the complete input is divisible by that block. Those reference factors and the input-integrity computation are not arguments, dependencies or decision inputs of this runner. Neither candidate is changed after observing its result.

## 1. Fixed inputs and order

1. `input_full.json`: N = `505246541734676269885345827299505246541734676269885345827299`, k = `3`; output directory `runs/full`.
2. `input_block.json`: N = `505246541734676269885345827299`, k = `3`; output directory `runs/block`.

Run the complete input first, then the block in a fresh process. Both JSON files contain only the decimal strings N and k. No supplied prime, factor, order, eigenvalue, local character, accepted class or expected result is supplied. The complete input is not presumed to be a product of two distinct primes. Any reported proper divisor is justified by the actual final division, independently of such a presumption. No finite-proposal probability claim is attached to either result.

The source at handoff is `streaming_public_clock.py`, SHA-256 `e4cde846c1d5c0238b881e05f3128c184fb599366f7da1f3e55161c8fbf5b86b`. Author validation so far is source inspection, AST-only dependency-pin comparison and `py_compile`; no scientific module was imported or run by the author. The actual coordinator supplies the immutable current activity guard, its actual record SHA and the current actual knowledge-read SHA when running. The runner binds these files and this PLAN before the exclusive STARTED marker, and rechecks them after the computation.

## 2. Scientific interface and output

All nontrivial unsigned additions, comparisons/subtractions, multiplications and divisions call the frozen `lazy_modular.Arithmetic` methods with an explicit streaming subclass that changes only retention. Modular products and gcds are composed from those actual typed operations. The eight full-adder input columns are admitted through the actual native catalog after STARTED; complete admission receipts and process-wide native calls are saved separately from digit costs.

Setup constructs two, four, k squared and Delta=k squared minus four modulo N, verifies odd N by typed division by two, and evaluates gcd(N,Delta). A proper setup gcd is followed by actual N/divisor division and is a complete SETUP_FACTOR outcome. A saturated discriminant is DEGENERATE, not a successful regular-path test. The regular path retains the setup gcd cost; the new source does not construct unused old companion/inverse matrices and does not claim literal reuse of the old setup bill.

On the regular path, the new explicit streamed Jacobi routine follows the frozen generic algorithm for nonnegative principal numerators. It uses typed division, with the original parity, shift, mod-4, mod-8 and sign wiring recorded separately. It computes j=Jacobi(Delta,N) and e=Jacobi(k+2,N), retaining two distinct arithmetic streams. These characters are observations, not rejection filters in this fixed-proposal unit. For k=3, Delta=k+2=5 modulo N: j and e necessarily coincide and supply no independent second label. Both calls remain charged; they are not silently deduplicated.

The public exponent E=N-j is constructed by an actual typed add or compare/difference operation. Its public binary digits drive the ordered pair (V_m,V_(m+1)), initially (2,k). At each bit, one actual cross product and one selected square yield the two new traces, with the two actual modular subtractions. Orientation is never folded. The finite ordered bit schedule, initial state, every primitive record and every outer producer link establish the claimed trace index.

The two outputs are the main signed primitive return observers:

- identity: tau=V_E-2, w=V_(E+1)-k, d=gcd(N,tau,w);
- antipodal: tau=V_E+2, w=V_(E+1)+k, d=gcd(N,tau,w).

Each output is classified UNIT, SATURATED or PROPER_FACTOR. Every proper divisor is accompanied by an actual typed division N/d with zero remainder and a proper cofactor range check. Both signed main outputs are retained even if the first is proper. This unit does not evaluate the scalar union gcd, E+2 clock, its exact quotient, or an additional parameter proposal.

The regular-case mathematical contract is the previously reviewed translated trace mark with 2 and Delta units. It holds over any admitted odd modulus, including prime powers; the separate two-prime fiber probability theorem is not used to infer a distribution for these fixed inputs.

## 3. Validation and source provenance

There is one separately charged terminal conic consistency check: V_E squared minus k V_E V_(E+1) plus V_(E+1) squared plus Delta equals zero modulo N. This is necessary consistency, not a sufficient history certificate. The record explicitly sets `history_certificate_sufficient` false. No old full-matrix exponentiation, host modular power, host gcd or numeric ideal reference is used as a comparator.

The complete record remains available for a later saved-record-only audit: bind every full-adder cell to the actual admitted catalog, every typed multiplication/division to its saved digits, every modular wrapper to the corresponding returned operation IDs, every Jacobi step to its producer and preceding state, and every ordered bit transition to its incoming pair and public bit. Such an audit must consume the whole chronology, not accept just the terminal residual or final factors. A scientific replay, if separately requested later, is a new billed run rather than an administrative readback.

The source checks eight literal dependency hashes, including frozen lazy arithmetic, typed arithmetic, sparse digit composition, the original Jacobi source, the adjacent algorithm and its conic/public-clock/translated-mark proofs. Runtime native source admission records the actual frozen catalog/vendor source. The complete dependency map and actual loaded source bindings are in STARTED and the stream. The new Jacobi implementation is explicit; it does not monkeypatch the old generic function or claim to return its unchanged schema.

## 4. Streaming evidence and failures

Each completed primitive gets a monotone stream-local operation ID. Before that ID returns, its full trace and accounting are serialized to one independently closed gzip member, the data file is flushed/fsynced, and the index line is flushed/fsynced. The index binds the global sequence, kind, byte offset, compressed and decoded sizes/hashes, and the stream/op ID. Outer records contain only values, links and compact control state. JSON tokens are merged in roughly 64 KiB buffers before compression; byte content and scientific arithmetic are unchanged.

`EVIDENCE.jsonl.gz` is a concatenation of complete independent gzip members, one newline-terminated JSON record each. `MEMBER_INDEX.jsonl` contains one durable index entry per committed member. Final SUMMARY hashes the complete evidence and index files and records member counts. A crash after data fsync but before index fsync may leave a complete unindexed member; a crash during a member may leave a truncated tail. Neither is a complete final outcome. A reader must verify exact member bounds and reject silent truncation, duplicate/missing IDs and unexpected trailing bytes for a COMPLETE claim.

Existing evidence is never overwritten or truncated by failure handling. Available incomplete records are written only to new failure files, with the last completed public state, costs, catalog calls and committed count. The frozen primitive builds a whole individual trace before returning; an exception inside it can therefore lack its unreturned intermediate cells. The failed result is explicitly FAILED_NOT_RESUMABLE, not an automatically restored computation. Its saved committed prefix can still be audited and used to decide an authorized next execution. No original researcher or conversation is required to read that evidence or continue this task.

The standalone run rejects any existing STARTED, success, failure or evidence outputs in its selected directory. A failed directory must be preserved. A future retry requires an explicitly separate execution unit/directory; this PLAN does not authorize repeated attempts until a factor appears.

## 5. Honest resource contract

Report all streams: setup arithmetic, setup gcd, character-input construction, both Jacobi divisions and label wiring, public-clock construction, power, signed expressions, main gcds, exact factor divisions and terminal validation. Summary provides per-stream and aggregate arithmetic totals, with production and validation separated. Process-wide native catalog calls remain distinct from typed operations, digit replays and host bit wiring. The frozen accounting excludes Python control, allocation, JSON, gzip, hashes, fsync and operating-system work; wall-clock and file sizes are separate measured quantities.

Streaming removes cumulative retention of full primitive histories. It does not change the frozen multiply/divide routines, which still construct a complete individual trace. For n-bit residues the largest primitive retains O(n squared) digit cells plus integer labels, Python objects and buffers; no constant-memory or linear-memory claim is made. The O(n)-bit public exponent still entails O(n cubed) digit work with this arithmetic composition. Its actual memory, time and output bytes must be learned from the run, not asserted from a small native catalog-call count.

This is a bounded native public-clock test, with no factor input and complete output/failure retention. It is not a general factoring success theorem or a completed Shor algorithm. The implementation reuses classical Lucas/Jacobi mathematics through actual native arithmetic; the present engineering change is streamed evidence for the larger requested inputs.

## 6. Invocation after coordinator review and actual guard binding

In two separate processes, substitute the real PLAN SHA, guard path, guard record SHA and knowledge-read SHA returned by the coordinator. Use the complete input first:

```powershell
& 'D:/kimi-query-bridge/.venv/Scripts/python.exe' -X utf8 'D:/em/TEMP/sep27-brc-user-large-target/streaming_public_clock.py' --input-json 'D:/em/TEMP/sep27-brc-user-large-target/input_full.json' --plan 'D:/em/TEMP/sep27-brc-user-large-target/PLAN.md' --plan-sha256 ACTUAL_PLAN_SHA --guard-file ACTUAL_GUARD_PATH --guard-record-sha256 ACTUAL_RECORD_SHA --global-knowledge-sha ACTUAL_KNOWLEDGE_SHA --output-dir 'D:/em/TEMP/sep27-brc-user-large-target/runs/full'
```

The second command changes only `input_full.json` to `input_block.json` and `runs/full` to `runs/block`. Preserve both command/tool outcomes, including failure. Input-integrity cost is recorded in its existing separate unit and is not hidden in or charged again as either native search run.

Global-Knowledge-Sync: main@a668c14 / GLOBAL_KNOWLEDGE_V1. This is the author's actual canonical read; the run additionally records the coordinator's actual current read. Shared-context author work, not independent formal admission.
