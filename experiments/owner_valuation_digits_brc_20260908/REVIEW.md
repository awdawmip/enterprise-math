# Bounded internal digit DIV migration assessment

Result: **PASS for this TEMP-only local migration candidate**. No source file, method registry, branch, task, or formal status was changed. This is auxiliary reuse R&D, not a mathematical L4 admission and not whole-tool arithmetic compliance.

## Fixed source and small patch

Published source: `909ed4c3c81adca8d5d653994a83df316faf1365`; the actual local immutable object read was `0b45bbacfd7df7f8b0f678bf57ea136e75b18891`, tree `6f7a6294828c75f27352fea7f32eeb37199abe15`. Their publication equivalence is the parent's already verified source receipt. The local test records its actual object rather than pretending to read a remote ref.

Target: `research_notes/owner_arithmetic_20260907.py`, source SHA256 `71f0214cc414c9d1291facd3ec8a727989fafe1bc21e0db5001b7d5e5655a79d`. The original registry's public APIs remain `SignedValuationSpectrum` and `signed_valuation_spectrum`. `digits_lsd` is internal.

`digits_lsd_brc.patch` changes exactly one import group and the internal digit helper. It directly uses the existing `division` -> `brc_evaluate_division` -> `BRCDivisionTrace` interface. No additional arithmetic wrapper or tool family was introduced. Reuse resolution: `REUSE_EXECUTED`, scoped only to this local digit entry; the native BRC facade and its P007 dependencies are unmodified.

The optional keyword-only `arithmetic_trace` collector receives the actual frozen native trace objects. The existing public caller remains byte-for-byte `digits_lsd(radius, prime)`: it passes no collector, and neither returns nor persists these traces. This explicit visibility gap remains for any future whole-public-tool evidence contract. The current change must not be described as making the entire historical valuation chain natively compliant.

## Valid-domain preservation

For `n >= 0` and integer `p >= 2`, the facade returns the unique Euclidean state `n = p*q + r`, `0 <= r < p`, and the collapsed state `p*q`. For positive `n`, `0 <= q < n`, so repeated evaluation terminates. Uniqueness gives exactly the old least-significant-first remainder tuple at every step. The zero case still returns `(0,)`, with zero evaluations and zero appended traces.

The entire suffix beginning at `_digit_coefficients`'s `@lru_cache` decorator is byte-identical, including the coefficient recurrence, dataclass, public signature/default budgets, all carry transitions, signed weights, active-axis output, and final construction. `_integer` and `ComputationBudgetExceeded` are also byte-identical. This establishes a local semantic substitution under the same downstream dependency behavior. It is not a freshly executed comparison of all signed-spectrum outputs.

Standalone invalid inputs now reject explicitly through existing `_integer`: negative/noninteger `n`, and bases below 2/noninteger bases. These were outside the preserved valid domain; old base-1 or negative-input nontermination was not executed. The helper still accepts composite bases and introduces no resource cap. The public caller retains its existing primality and `max_prime` / `max_digits` restrictions. `N` remains shortest event length, not the quadratic-shell parameter; signed endpoint counts are not unit-step path counts.

## One bounded actual run

Actual command: `python -B -X utf8 review.py`, in this package directory, Python 3.12.14.

- 10 fixed valid digit tuples passed. Inputs were formed by exact integer multiplication/addition from those tuples; the oracle did not execute an old `divmod` chain. Cases include zero, powers and their predecessors, mixed base-31 digits, the 256-digit boundary, a composite helper base, and a one-digit 17,001-bit input outside the public prime budget.
- Every trace passed input/denominator binding, low-first remainder equality, `n = p*q + r`, collapse equality, basin bounds, strict quotient descent, final `q = 0`, exact native class identity, and collector-prefix preservation.
- Real code-object profiling observed 288 calls each to `division`, `brc_evaluate_division`, `euclidean_state`, and `multiple_collapse`; 576 `integer_quotient` calls occurred strictly inside the existing P007 facade implementation. The helper-only cases account for 284 DIV calls; the unchanged caller's last-allowed small-budget probe adds four.
- 8 standalone invalid inputs rejected before any DIV call or collector append. 11 caller checks verified validation and budget routing, with two stopping at the first histogram constructor. Caller primality used a disclosed finite test stub, not the real primality implementation.
- A guard reached the old `divmod` entry and raised before computing any quotient. The same guard remained installed throughout candidate execution and was never reached. A local AST check found no `divmod`, `/`, `//`, `%`, `Fraction`, or `Decimal` in the new helper. This is not a whole-file or transitive arithmetic-policy gate.
- The actual elapsed test time was 0.099590300 seconds. The global integer-to-decimal limit stayed 4300; large inputs and trace content are represented by compact hashes over unambiguous hexadecimal integer encodings. `review.py` constructs every case exactly for replay.

The three exact frozen facade/dependency files were loaded through a test-only namespace package, bypassing the repository's broad package initializer. The real histogram and primality modules, carry loop, full spectrum, legacy validation scripts, and Fraction chain were not executed. Native implementation identity and code-object counts are recorded in `review.json`; this isolation is an explicit test boundary, not a replacement production package.

## Evidence and remaining boundary

`inputs.json` pins the candidate, patch and eight exact source/dependency files. `review.json` contains each case's input/output/trace hashes, actual counts, source hashes, preserved function hashes, and the executed script hash. `execution-tool-receipt.json` binds the actual tool invocation and stdout without rerunning it. `original_validation_preservation.json` confirms the old check script and old result JSON still match their fixed source bytes; neither was executed or rewritten. Eight selected owner worktree files were also equal before and after the run.

Candidate SHA256: `209c5f38dee8dcd0f61b895ef3c2b1e3d4e2b46724bb3bf7326dd210f813b2ce`.

Patch SHA256: `1ac2dc1ec0cf318702fb8135f94f34ea155b145cf689242f81d0705c05ee8c01`.

Executed review script SHA256: `0289460c3a3901a2e2c3bf4e9b5f1efca0b8c085d5b324aafac70030e8254033`.

Actual review JSON SHA256: `9e0bcc45502a2f14c9939d2229f4ecf90921534d820c90be3df7404e68e227ed`.

Reproduction requires only this captured package and Python: `python -B -X utf8 review.py`. `prepare.py` documents the one-time immutable Git capture; it refuses to overwrite existing captured inputs. Frozen files preserve their original bytes, including any historical line endings. Newly written candidate, scripts, patch, metadata and this note use UTF-8, LF and terminal LF.

The next bounded decision is whether to adopt this exact internal substitution while retaining its partial-evidence label. Any later complete valuation-tool migration separately needs a caller-visible trace receipt contract and analysis of the existing primality/histogram arithmetic and broad imports. No such migration, new theorem, new multiplicity claim, or review acceptance is asserted here.

Driver-ID: EM-DVR-01E1D9 / CONTROL_PLANE
Global-Knowledge-Sync: main@a624e4d / GLOBAL_KNOWLEDGE_V1
