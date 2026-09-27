# Free-trace complete saved-record review

Result: **PASS_STDLIB_SAVED_RECORD_REVIEW / NOT_INDEPENDENT_ADMISSION**. The coordinator executed the frozen runner once (reported chunk `f05651`, exit 0). This review read that complete saved result and checked its source-bound records. It did not import a scientific module, rerun any fixture, evaluate a host modular-power/gcd reference, or add another scientific input.

## Exact evidence

| Artifact | SHA-256 |
|---|---|
| `free_trace_probe.py` | `2f0981f1dd25e8160bcd80207a6bc92d080e291b545f3be62b95eddffdd36708` |
| `PLAN.md` | `c05b238b7c1f1c72319f6bbe3e41652f2d274f41cc05b6cdaf85e7c6a9e4cb52` |
| Results uncompressed bytes (1,822,824) | `bd9ccd13f75e41b44edcfd294990ce1bd5673011fe906b4780c05662dfe70158` |
| `FREE_TRACE_RESULTS.json.gz` (109,481 bytes) | `2b714edc7cd51728377ef5269451724feb96a8896af3037fcb60101ef09e37c5` |
| `read_free_trace_records.py` | `5c4bb5ab416376d922dc15bbc05f553686011ef89f7ca4060d138a870785533d` |
| `FREE_TRACE_RECORD_REVIEW.json` | `e272d126118e70fe5c528235d7cf7f5afa1ecfe46d6892d4f7e3e8518432832a` |

The reader also binds the actual STARTED record, summary, frozen proof/wrapper/runtime files, guard bytes and activity-record hash `b56f4d69570979d37027ea355b312144de37a658307bb40bec5c6e98ea0e76b9`. The saved execution lease is `8c23cca3ed79ca2d6ecbdf76734606eabd94fd0d`. No failure artifact was present. The review uses only selected function/class definitions from the previously frozen stdlib record readers; their top-level scripts and all scientific sources are excluded from execution.

## Saved results and observer distinction

| Public input (N,k,E) | Identity coordinate gcds | Identity common / trace gcd | Antipodal coordinate gcds | Antipodal common / trace gcd |
|---|---|---|---|---|
| (77,3,4) | (7,1) | 1 / 1 | (7,7) | 7 / 7 |
| (77,3,8) | (7,7) | 7 / 7 | (7,11) | 1 / 1 |
| (49,3,8) | (7,7) | 7 / 49 | (7,1) | 1 / 1 |

These entries are copied from checked saved typed outputs, not independently recomputed answers. All three discriminant setups were regular. For N=49 the common return preserves the proper factor while the trace saturates, confirming the declared valuation fixture. For N=77,E=8 the antipodal y coordinate alone finds 11 even though the common antipodal return is a unit. Already at E=4 the x coordinate finds 7 while the identity common return does not. Therefore the stronger matrix-return contract does not imply an earlier or universally better factor probe than the individual coordinates.

The extra signed-partition audit uses only equality: in each saved case one signed common gcd is 1 and the other equals the saved x-coordinate gcd. This checks the proposed product relation in these cases via multiplication by the identity, without executing any new host multiplication or gcd on scientific values. It is an administrative record comparison, not an additional production primitive or general numerical test of that theorem.

## Complete wiring and typed provenance

The reader consumed all 36 arithmetic streams, 1,035 typed top-level operations, 37,719 full-adder digit cells and 513 chronological outer nodes. Every saved digit is linked to the actual admitted native full-adder column catalog. The sole global catalog record is the existing 12-state, depth-1 `recurrent_mass_power` call; one catalog call is not substituted for the actual digit-work count.

Checks include every polynomial square and append-M step, both signed target residuals, cached single-coordinate gcd operands, complete common-coordinate Euclidean chains and their remainders, all proper-factor division receipts, trace readouts, all independent validation matrix products, the cyclic residual identities, and both signed trace-square gcd identities. All direct arithmetic cursors and standalone gcd ledgers close with no unconsumed operations or outer nodes. Source and guard bindings match the actual result and summary. Full matrix validation and all failed-to-factor or saturated observations remain present.

## Costs, including validation

| Input | Setup digits | Polynomial power | All readouts | Validation | Setup + power + readouts |
|---|---:|---:|---:|---:|---:|
| (77,3,4) | 389 | 1,019 | 3,183 | 7,398 | 4,591 |
| (77,3,8) | 389 | 2,055 | 3,238 | 9,536 | 5,682 |
| (49,3,8) | 354 | 1,538 | 1,679 | 6,941 | 3,571 |
| Total | 1,132 | 4,612 | 8,100 | 23,875 | 13,844 |

The complete total is 37,719 digit replays, with 400,899 modeled host bit-wiring operations and 6,508 arithmetic bit-length calls. The power chains contain 11 squares and three append-M steps; validation adds 17 full matrix products. Counting native catalog calls alone would hide this work. Metadata sums in this review do not rerun arithmetic. No matched wall-clock benchmark was requested or inferred.

The result establishes the declared finite modular observer implementation and its exact return-ideal/trace distinction. It does not execute raw HBW Cell trajectories or carries, a first-hit histogram, a favorable-exponent selector, or a general factorization success law. The prime-power input was intentionally selected by a symbolic identity. Alternate proper-discriminant and degenerate branches, failure recovery, and arbitrary larger inputs were not tested here. The algebra is the standard Lucas/companion mechanism realized with actual typed BRC receipts; no cheaper-than-Lucas claim or completed Shor algorithm follows.

Recheck command (stdlib saved-record inspection only):

```powershell
& 'D:/kimi-query-bridge/.venv/Scripts/python.exe' -X utf8 'D:/em/TEMP/sep27-brc-hbw-free-trace/native_probe/read_free_trace_records.py' --raw-sha256 bd9ccd13f75e41b44edcfd294990ce1bd5673011fe906b4780c05662dfe70158 --gzip-sha256 2b714edc7cd51728377ef5269451724feb96a8896af3037fcb60101ef09e37c5 --raw-bytes 1822824 --gzip-bytes 109481
```

The reader refuses to overwrite its existing review JSON. A repeat administrative check should use a restored review workspace, preserving these frozen artifacts. No repeat scientific execution is needed.

Global-Knowledge-Sync: reviewer main@7a63984; execution shared coordinator lease main@8c23cca3 / GLOBAL_KNOWLEDGE_V1.
