# Streamed public-clock runner: source-specific static review

Status: PASS_STATIC_FOR_DECLARED_TWO_INPUT_RUNS / NOT_EXECUTED_BY_REVIEWER / NOT_ADMITTED. No blocking issue found in the complete reviewed source and plan. This is a shared-context review, not independent formal admission or a runtime guarantee.

Frozen candidates reviewed:

- `streaming_public_clock.py`: `e4cde846c1d5c0238b881e05f3128c184fb599366f7da1f3e55161c8fbf5b86b`.
- `PLAN.md`: `d861ea6b08801f457816e7a18752409d053f6e13174b2070320e0206511f87af`.
- Both exact public input files: full supplied decimal N first, displayed block second, each with fixed k=3. They contain no factors, orders or expected results.

I read the complete source, plan and current input files, the frozen `lazy_modular.Arithmetic` methods and accounting, and the original `typed_jacobi_trace` recurrence. Two erroneous literal dependency hashes in an earlier unexecuted draft were reported and corrected before this candidate. The final eight literal dependency pins match their files. The runtime loads `lazy_modular` directly, verifies its loaded path and the loaded sparse/typed source hashes, and admits the actual native catalog after STARTED. It does not use the invalid `hbw.old` interface from the separate v1 input check.

The streaming subclass changes `_retain`, not add/compare/multiply/divide. It deletes the accumulating operations list and issues monotone per-stream IDs. Every returned primitive trace and its accounting is serialized before the ID returns. Parent modular multiplication/subtraction only consume returned IDs; they do not index an operations list. No hidden ordinary multiply, modulo, pow or gcd replaces scientific arithmetic. Public exponent digits, sign changes, comparisons used to classify observed labels, and the inherited Jacobi parity/shift rules are explicit wiring.

The Jacobi recurrence matches the frozen algorithm on its deliberately narrower nonnegative principal-residue domain. Each denominator swap uses an actual typed long division; both supplements, factor-of-two shifts and label cost are retained. The public E=N-j is produced by a typed add or positive compare/difference. Its ordered trace pair starts at (2,k); each public bit uses one cross product and one selected square, with typed modular subtractions. The two final signed joint gcds consume the actual tau/w producers, and proper factors receive an actual exact division certificate. There is no reciprocal fold, second-clock quotient, answer-dependent proposal, or supplied p/q path.

The terminal conic test is paid validation and explicitly insufficient by itself to certify history. Correctness depends on the whole initial-state and bit-transition record. Discriminant saturation is DEGENERATE, and a proper setup gcd is a separately retained factor outcome. The regular identity/antipodal return contract applies to arbitrary admitted odd N, including prime powers; the fixed trials do not invoke a two-prime probability formula. For fixed k=3 the two character numerators coincide; the plan correctly declines to call them independent labels.

The evidence sink closes and fsyncs each independent gzip member before fsyncing its index line. Each index entry contains global sequence, exact offset/size, compressed/decoded hashes and, for primitives, stream-local ID. SUMMARY hashes both complete files. A previous-record hash chain is not needed for this declared completed-record integrity contract, provided the saved-record reader checks exact contiguous bounds, sequences, all hashes, all operation references and no trailing bytes. Proper-factor events are themselves durable first-result records; a separate small checkpoint file was not promised.

A failed write poisons the sink, retains the available pending record and never licenses continued computation. A crash between data and index commits can leave an unindexed member; an interrupted member can leave a truncated tail. Neither is a COMPLETE result. Existing output markers prevent accidental repeat/overwrite. Returned primitive records and completed public state are retained where available; a primitive exception before returning may lack internal cells. This is correctly labelled FAILED_NOT_RESUMABLE, not a universal interruption snapshot or automatic resume mechanism.

Costs are accumulated per arithmetic stream and separated into production and terminal validation. Catalog calls, digit cells, inherited host bit wiring and explicit Jacobi wiring remain distinct. Filesystem/JSON/gzip/hash/control overhead is not claimed to be included in digit costs. Roughly 64 KiB serialization buffering removes excessive token-sized compression calls but is not scientific acceleration. One complete primitive trace is still built in memory, so streaming removes cumulative retention only; O(n squared) per-operation digit storage and O(n cubed) composed digit work are honestly stated.

Nonblocking scope: `json.loads` accepts duplicate object keys in general. The two reviewed immutable input files have no duplicates and are byte-bound, so this is not an ambiguity in the declared runs. A future untrusted general-input interface should reject duplicate keys. No source change is requested for the frozen finite unit.

The coordinator may execute the two declared single runs in fresh processes using the real current guard, PLAN hash and knowledge-read pin, full input first. This statement does not claim that either trial will find a factor, fit a particular time budget, or complete Shor.

Global-Knowledge-Sync: main@b304760 / GLOBAL_KNOWLEDGE_V1, reviewer's actual canonical read. Runtime bindings separately retain the source author's and coordinator's actual reads.
