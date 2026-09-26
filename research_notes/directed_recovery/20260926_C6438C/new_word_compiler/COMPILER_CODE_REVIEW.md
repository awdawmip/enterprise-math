# Shared code review: compiled native-word factorization

Status: **SHARED_CONTEXT_SOURCE_REVIEW; TWO IDENTIFIED DEFECTS FIXED; NO REMAINING SUBSTANTIVE FINDING IN THE REVIEWED SNAPSHOT.** This is neither an independent reviewer admission nor an execution of unbounded compilation. The reviewer shares the authoring context and previously contributed proofs and sparse arithmetic. The review made no changes to implementation files and ran no new scientific or ideal-reference calculation.

Activity: `RA-CAAAC604CB513AEA8BBC1DFC`. Control Source: `f0e5fb6f478a5a380ab5a7533d2585f7f43ee3bf`. Global knowledge: `main@441ebef / GLOBAL_KNOWLEDGE_V1`. Review date: 2026-09-26.

## Files actually reviewed

SHA-256 values were read after the fixes described below.

| File | SHA-256 |
| --- | --- |
| `compiled_factorization.py` | `eb1f12abb9d9b5faf140d2a49a2611bbf6cc18cc4aae8e4b911a43a05e32639d` |
| `derive_compiled_factorization.py` | `fbfc0aa7e7feea1fb0a2244a777da3918d4d4aa1d487ae7f30a3d9c525b0f105` |
| `compiled_factorization_core.py` | `e10a32bb028a38fc387baec4feb2052bd3f2f4905a18f0ed5a944711d6fe8b43` |
| `compiled_streaming.py` | `d0f980b7ff5fb41438e9e0ad40af65a190bcd6f83660c821f8362643190a558c` |
| `certified_word_compiler.py` | `9ae28f9aaefb6687d6cac00b6d26eb8ba93bae5f470334eb3eb3e00e014224e4` |

The original `integration/complete_factorization.py`, generation manifest, frozen quarter-turn/identity-tail classes, compiler checks and available author result summaries supplied the immediate contracts. The mathematical error and success proof is reviewed separately in `COMPILER_SHARED_REVIEW.md`; this report does not silently enlarge it.

## Defects found and corrected

1. **The provider crashed while constructing its seed bank.** The original comprehension read `bank[m].inverse_phase_word` at every `m >= 2`. The frozen `QuarterTurn` at `m = 2` has no such attribute, so a composite needing the provider raised `AttributeError` before reaching either compilation or the recoverable `CompilationPending` branch. The provider now explicitly uses `(('swap',0,1),('neg',1))` for the exact inverse quarter-turn and reads legacy word seeds only for `m >= 3` (`compiled_factorization.py:38`). Frozen `IdentityTail` objects used at the far tail do have the required empty inverse word. This correction was read back in the hashed source above.

2. **The streaming importer accepted an unproved target-error assertion.** Its earlier version required a nonempty certificate and replayed the claimed word, but did not replay the certificate proving that word's distance to the target. A substituted identity word, false zero error and consistently altered total could therefore import a bank with an unsupported TV claim. The importer now calls `verify_phase_record(record)` before using its bound (`compiled_streaming.py:164`), and records the verification in its binding evidence. The current verifier binds phase, carrier, word, source, certificate hash and the error assertion, then forces fresh native-column and target-observer replay. This closes the specific substitution path rather than relying on an external hash alone.

Both defects were reported to the parent and corrected by the responsible author. No implementation was edited by this reviewer.

## Compilation interruption preserves the factorization ledger

The generated core differs from the original core only by the declared `CompilationPending` exception handling plus its necessary declaration/import placement. A source-text derivation check, without importing scientific modules, returned `source_pin_matches = true`, `output_pin_matches = true`, `only_declared_rewrite = true`, and `catch_count = 1`. The generation manifest's original source hash is `96ea1eda5a689106515420b06826bb0bb6a11c4d4fb41ae50bcfb33a87fb7aee`.

At an unresolved composite node the provider is called before a base or readout RNG draw. If its finite compilation budget stops, the catch at `compiled_factorization_core.py:83` records the entire current cofactor, its multiplicity, its existing non-perfect-power and composite certificate identifiers, the target width and the resumable compilation report. It appends that same cofactor and multiplicity to `unresolved`, then continues any other pending nodes. It does not drop the original cofactor, divide by a guessed factor, mark it prime, or count compiler failure as a failed Shor measurement.

The inherited even and perfect-power branches preserve multiplicities. Every returned prime has its actual typed primality certificate; a failed retry or compilation branch cannot establish primality. The final product includes both certified prime powers and unresolved cofactor powers. Actual typed powers and products reconstruct the original input. `COMPLETE` is possible only when the unresolved list is empty.

`verify_factorization` independently reconstructs that deterministic product and replays the claimed prime/precheck certificates. It rejects hidden unresolved factors and a status inconsistent with the ledger. Its result explicitly states `stochastic_budget_verified: false`: it is not a certificate for the distribution of a supplied RNG or for an arbitrary altered retry transcript.

The compilation catch sets `guaranteed_budget = false`. This correctly withdraws the uninterrupted-run retry-limit bound from an interrupted run. It does **not** assert that the compiled algorithm has zero success probability, nor that the remaining cofactor is intrinsically unresolvable.

## Accuracy and finite versus unbounded budgets

The provider requests `epsilon = 1/(8*t)`. The core sets `t = 2*n` at each actual stochastic node, hence the request is exactly `1/(16*n)`, as required by the success theorem. It checks that the adapted whole-program terminal-TV bound lies between zero and this epsilon. The core derives its success margin and retry count from the returned certified bound, rather than assuming every bank saturates epsilon. This is appropriate because the compiler allocates `delta = epsilon/(2*L)` and the exact quarter-turn contributes zero; the actual total can be smaller than the request.

An integer `pair_budget >= 0` bounds the number of candidate/isolation pairs in one compiler request. Boolean and negative values are rejected. It is not a bound on all native calls, all replay work, wall-clock time, or all requests across a recursive factorization. Legacy-seed loading and verification of already completed certificates can consume work even with a zero pair budget.

The wrapper's `pair_budget = None` repeatedly advances the saved cursor in finite chunks of 256 until it receives `CERTIFIED`. Its mathematical termination rests on the separately proved dense alphabet, convergent strict observer and fair enumeration; this code review and the available bounded tests do not execute or measure that unbounded limit. A finite budget returns a typed, visible `PARTIAL` with a cursor, not a false certificate.

The provider caches successfully certified banks by width. A requested bank depends on width, declared epsilon, source/profile and the preselected seed policy; it receives no order, factor, measured result or ideal distribution.

## Fairness, cursor reuse and certificate binding

For the single-phase search, stage `s` visits offsets `i = 0,...,s`, candidate `i`, and observer depth `start + s - i`. Every finite candidate index is therefore revisited at arbitrarily fine observer depth. Seeds occupy a finite prefix, followed by complete length-lexicographic enumeration of the fixed alphabet. A candidate with equality at one tested threshold cannot stall the enumeration.

The cursor binds the complete request and its digest: phase index, positive tolerance, seeds, observer start depth and source. The stage/offset and triangular processed-pair count are checked. An externally advanced but internally consistent finite cursor may skip a finite prefix; it cannot manufacture a certificate and does not remove the later infinite revisits needed for mathematical termination.

The bank resume request binds `t`, epsilon, the derived delta, source, seeds and observer settings. Its completed phase keys must be exactly `2,...,next_phase-1`. Every retained completed record is sent through `verify_phase_record`, and its phase index and error bound must match the current bank allocation (`certified_word_compiler.py:436-441`). Thus completed phases cannot be imported from a looser budget just by modifying the bank's aggregate bound. The active phase cursor is subsequently checked by the single-phase compiler. Whole-program error is recomputed from verified phase bounds with the actual occurrence counts `t-m+1`.

The exact-quarter-turn exception is narrow: `m = 2`, record bound zero, the exact-quarter flag, and a replayed zero squared-error upper bound. The certificate itself still has its positive requested tolerance and strict accepted margin. A general phase cannot claim zero error by copying that flag. The adapter correctly verifies the record and then reads its supported record bound; it does not replace the exact zero by the verifier's positive requested tolerance.

The verifier checks full carrier dimension, determinant component, actual word and inverse columns, all source hashes, target root-isolation evidence, strict observer margin and certificate digest. Its native-column and isolation replay bypass the compiler caches. The importer then reconstructs all 61 actual signed columns and verifies inverse/Gram identities, retaining every residual mode. The ideal target is used only by the observer and never substitutes for the actual propagator.

## RNG and resume scope

The compiler consumes no RNG. Compiler interruption occurs before the affected node's base/readout draws. Existing stochastic driver behavior keeps an exhausted external base/readout source visible as an incomplete source with the available state/history rather than deleting its outcome. The usual retry theorem remains conditional on fresh uniform legal bases and the stated readout-randomness contract; explicit base overrides are separate replay policies.

`phase_cursors` resume **compiler search**. Calling the wrapper again repeats the factorization entrypoint and deterministic prechecks; it does not import the former prime ledger as a live continuation or restore a random generator. Previously returned prime certificates remain valid, but the compiler cursor alone does not reproduce earlier random histories or the exact prior stochastic transcript. The result's resume note states this distinction. No stronger checkpoint semantics should be advertised from this interface.

## Available execution evidence and limits

The reviewer read the author-generated `CERTIFIED_WORD_COMPILER_SUMMARY.json`: actual bounded `m = 2` and `m = 3` certificates, a resumed bank, six rejected mutation controls and 738 actual core calls; status remains `AUTHOR_ACTUAL_BOUNDED_EXECUTION_NOT_ADMITTED`. The controls include substituted words, unsupported smaller errors, changed full columns, changed strict margins, altered completed-cursor records and altered cursor targets.

The reviewer also read `COMPILED_STREAMING_SUMMARY.json`: two small same-actual-word full/streaming comparisons (`N = 15, t = 4` and `N = 21, t = 6`), 6,724 actual core calls, rejection of the two imported-certificate substitutions, prevention of program construction from a partial bank, and successful bounded resume. These are exact comparisons of two executions of the same native words, not numerical comparisons to an ideal Shor reference. The summary limits its claim to one terminal instrument and explicitly declines a whole-retry-transcript TV claim.

Those author artifacts support bounded executed integration. They do not establish practical complexity, a polynomial-time compiler, exhaustive arbitrary-width execution, independent admission, or a full factorization test result that had not yet been published at review time. No additional source-level blocker was found in the hashed snapshot.

Global-Knowledge-Sync: main@441ebef / GLOBAL_KNOWLEDGE_V1

## Addendum: standalone decimal I/O and CLI entrypoint

This additive readback preserves the historical hashes above. The updated `certified_word_compiler.py` SHA-256 is **`e8f7048e2e73292bda230a2adad4aaa76f0b3cd5525f8f0899628bd649d1d81d`**. The newly reviewed `run_compiled_factorization.py` SHA-256 is **`5298a19b982d0a5395cbeb6de07d70da4ca47e7cb954fc166248218df92e24ea`**. Scope remains shared-context source and I/O review; this reviewer did not rerun scientific checks.

A source-text comparison against the retained `prior_4300_digit_cap/certified_word_compiler.py` shows exactly two changes: the guarded import-time call `sys.set_int_max_str_digits(0)` and the assignment `self.sign_count = self.neg_count`. The first removes Python's decimal integer parsing/serialization length limit, so sufficiently long exact certificates do not fail solely because they exceed the default 4,300-digit cap. The second exposes the existing negative-letter count under the adapter's expected metadata name. Neither changes native columns, target isolation arithmetic, signed margins, search order, determinant, tolerance, or dynamic state propagation. It does not change the frozen target32/vector64 parameters.

The author-generated `LARGE_CERTIFICATE_IO_SUMMARY.json` reports a 5,001-digit integer JSON round trip starting from the 4,300-digit cap, ending with cap zero and zero BRC calls. The newly read compiler summary reports the same bounded arithmetic checks and six negative controls, with 738 actual core calls and new payload hash `3092df8ed31d39709868ee1d3193e2492e40b158d857ecf0f4c618b9a12839fe`. These are attributed author results, not reviewer executions. Since the compiler source hash forms part of the certificate source binding, old-source certificates/cursors must not be relabelled as current evidence; `EXECUTION_CHANGE_LOG.json` records this transition and requires regeneration. The full integration/factorization reruns remain the parent's responsibility.

The CLI forwards finite `--compiler-pairs`, explicit `--unbounded-compiler`, observer depth, attempt override and failure bits to the existing validated wrapper. Unbounded mode explicitly selects `None`; finite exhaustion remains a successful production of a visible `PARTIAL` result, not an exception disguised as `COMPLETE`. System randomness is the default; a supplied seed selects the explicitly labelled software demonstration. The output retains `random_source_physically_certified: false`, the deterministic verifier's separate result, and `stochastic_budget_verified: false` in the printed summary.

`--resume-cursors-from` reads raw or `.gz` JSON, accepts the CLI result envelope or a direct wrapper result, and extracts only `native_word_compiler.phase_cursors`. The existing compiler verifies any used cursor's source, request and phase records; the CLI does not trust a saved prime ledger or restore its RNG. Reuse of a valid phase bank across different factorization inputs is sound because its target depends on width and declared error rather than the integer's unknown factors. The resume contract continues to mean bounded compiler continuation, not recovery of an interrupted stochastic transcript.

Decimal input parsing and resume-JSON reading occur before the provider's lazy compiler import. The actual CLI import chain already imports the frozen `terminal_instrument.py`, whose line 16 clears the digit cap before `argparse` or `read_result` runs. Thus the CLI does not retain a second 4,300-digit barrier at that earlier boundary. The new standalone compiler guard covers the separate direct-import path.

The CLI verifies the deterministic factorization/product ledger before writing, serializes through the existing exact-value encoder, uses deterministic gzip metadata when requested, and hashes the uncompressed payload printed in its summary. It creates parent directories and writes the user-selected output file only after a returned result. It does not promise crash-atomic writes or save a cursor during an externally interrupted unbounded call; use completed finite calls for its supported persisted-resume interface. No additional substantive source-level defect was found in these two changes.

Global-Knowledge-Sync: main@441ebef / GLOBAL_KNOWLEDGE_V1
