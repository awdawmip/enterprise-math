# Final-run cost audit of adaptive feedback

This is a shared-context read-only accounting audit of the **second, final** execution. It adds no scientific run and makes no independent-admission claim. The extractor imports only the Python standard library and reads the final raw evidence, not `prior_validation/`.

The final raw SHA-256 is `3e356df6befcbf201801657016f64072e2bccebbc0a877a51570f77748d7b78b` (118,117,750 bytes). Its gzip SHA-256 is `36a6460fbda4d081d1416bbfa48fa0fd641f96d0df235d2d168a7ac06aa5a9c0` (4,807,682 bytes). Both hashes and lengths were checked against the summary. The current source files and every saved Gram execution were checked against adaptive source `86263eb4a70fe53f8960aae2c1f0b8695dbca40a597b2711af90f20667ed3c45`, checker source `cd77bc2ff17a6b2938665a622a74c332e7e24cbe362ba359225fc071716510d3`, and inherited Gram source `468de944518fbc6afa81a17555676436376da63921a784c810ffe8fab3ca17e9`.

## What was counted

Each fixture has two complete-law checks, low budget `1/3` and reference budget `0`. Each proposes all 16 length-four histories with a fresh Gram object; impossible histories stop early. Thus there are **128 actual leaf-replay invocations**, with 448 checked prefix/selected-child comparisons. These are deterministic exhaustive repetitions, **not 128 independent trials or timings of sampled trajectories**.

The native phase action count is the inherited counter of calls to the admitted word-boundary vector adapter, including candidate-defect construction. Here it acts on six encoded coordinates with a previously verified full-61-column provenance. This is not a count of additional native-kernel calls: the encoded adapter uses cached certified columns. The frozen explicit-state checker did not separately instrument its own vector-action count, so the accounting leaves that field `null`, rather than inferring it from observer calls.

`COST_ACCOUNTING.json` retains every leaf's counters, observer label totals, graph-size counters, and retained cache counts. Sums of matrices across fresh objects describe actual repeated work/storage; they are neither a shared cache nor peak process memory. The extractor separately identifies identical history-specific queries and verifies identical recorded matrices when deduplicating, solely as an audit comparison.

## Low/reference full-law costs

Every slash below is **low / reference**. Queries, cached matrices and peak scalar slots happen to agree between the two routes in each fixture.

| N, a | Phase-vector actions | Gram requests | Cache hits | Sum of separately retained matrices | Gram observer operations | Explicit-checker observer operations |
|---|---:|---:|---:|---:|---:|---:|
| 21, 2 | 2,556 / 1,536 | 1,216 / 1,216 | 864 / 864 | 352 / 352 | 1,360 / 764 | 2,517 / 1,257 |
| 21, 4 | 3,708 / 2,880 | 928 / 928 | 720 / 720 | 208 / 208 | 1,832 / 1,236 | 2,306 / 1,046 |
| 65, 3 | 1,788 / 768 | 1,552 / 1,552 | 992 / 992 | 560 / 560 | 1,144 / 548 | 3,025 / 1,593 |
| 15, 2 | 60 / 24 | 344 / 344 | 264 / 264 | 80 / 80 | 128 / 124 | 181 / 149 |

For the four fixtures, the maximum retained cache sizes of one leaf object are respectively 792, 468, 1,260 and 576 scalar slots, excluding temporary matrices, retained receipts, Python objects and the explicit checker state. The audit unions of history-specific query matrices are 82, 61, 104 and 22 per route. Those unions were **not implemented as shared caches**; shared repeated ancestors are therefore still a potential optimization rather than measured savings.

The low route performed 34, 34, 34 and 2 candidate tests. Accepted omissions occur 8, 8, 8 and 0 times across repeated leaves, corresponding to only 4, 4, 4 and 0 distinct actual prefix decisions. Each accepted omission drops one word from a prepared feedback product; these figures are not vectors saved, independent successes, or measured time savings. In the first three fixtures, maximum stored correlation denominator bit length falls from 156 to 116 (numerator maxima 151→111, 152→112, 151→111). Nevertheless the measured Gram vector-action and observer counts are **higher for low in every fixture**. The current evidence demonstrates correctness of the adaptive choice, not an execution-speed improvement.

The joint TV is nonzero only for `N=21,a=4` in these four fixtures, exactly as the scientific summary records. Coincidence of the other three complete laws is not evidence of a general zero-error rule.

## Shared modular tables: count instances once

Low and reference, explicit checks, and later control tests share one program's table objects. Summing each Gram report's cumulative table counters would count the same setup and columns repeatedly. Conversely, combining tables only by `(N,b)` would erase costs: an inverse cache can have the same multiplier as another factory cache and still be a distinct constructed object.

The extractor uses `(program, factory multiplier)` and `(program, inverse-of-factory multiplier)` identities. It verifies the factory prefix of each snapshot, the inverse pairing, nondecreasing counters, matching permutation certificates, and inclusion/identity of recorded columns, then selects each object's final maximal snapshot. Factory final snapshots are also checked against the program export. Setup digits are checked against the inverse certificate; column digits and wiring counts are checked by summing the individual column receipts. Program-construction verification was executed once per distinct factory multiplier, although its receipt repeats in the four-entry schedule; those receipts are counted once according to the frozen constructor's explicit `verified` cache.

| N, a | Actual table instances | Requested columns | Newly computed columns | Setup digit replays | Column digit replays | Verification digit replays | Total digits |
|---|---:|---:|---:|---:|---:|---:|---:|
| 21, 2 | 6 | 1,470 | 29 | 2,165 | 2,290 | 1,027 | 5,482 |
| 21, 4 | 4 | 920 | 12 | 1,496 | 960 | 748 | 3,204 |
| 65, 3 | 8 | 1,836 | 57 | 5,371 | 9,140 | 2,661 | 17,172 |
| 15, 2 | 6 | 284 | 19 | 1,263 | 729 | 580 | 2,572 |
| **Total** | **24** | **4,510** | **117** | **10,295** | **13,119** | **5,016** | **28,430** |

The `N=21,a=2` totals include the later serialized-resume, rejected-replay and rollback/retry work. No artificial low/reference allocation is made for shared setup or cache savings. The JSON includes the table arithmetic's documented host-wiring subset, but it does **not** claim complete host-bit cost or charge all Python/rational operations.

## Rejected replay, recovery and whole-run accounting

The original and restored resume objects each record 162 phase-vector actions, 67 requests, 45 hits, 22 retained matrices and 135 observer operations. Restoration recomputes the committed prefix and pending certificate; it does not restore a persisted cache or RNG tape.

Seven malformed cursors each cause a real failed replay before rejection: 162 vector actions, 34 requests, 24 hits, 10 retained matrices and 95 observer operations. Thus the failures contribute **1,134 vector actions and 665 observers**, all retained in the raw exception evidence and counted separately. The other three negatives (`bool_history`, uncommitted history and changed program) reject before Gram/observer work through the explicit schema or immutable-state checks; no scientific failure trace is silently assumed for them.

The interrupted-and-retried object records 11 requests, 6 hits, 4 retained matrices and 2 observers; its separate fresh comparison records 8 requests, 4 hits, the same 4 matrices and 2 observers. Both have zero phase-vector actions. The retry object's counters include the failed attempt; the raw file does not contain a complete separate cost snapshot at the precise interruption, so that interval is not invented. The interruption event, preserved pending certificate and same-bit retry are retained in the accounting.

The complete native-call list contains **20,725 calls**, decomposed without overlap as:

- 8,075 Gram/policy positive-path observer operations across laws and controls;
- 12,074 explicit-state checker observer operations;
- 332 joint-TV comparison observer operations;
- 244 remaining native calls for bank/vendor/codec/two-H4 or arithmetic setup, left as an unattributed remainder rather than guessed subcategories.

The all-route Gram vector-action total including controls is 14,778. The recorded native-call elapsed sum is 109.6708839 seconds; the checker interval is approximately 129.345 seconds and excludes final JSON/gzip serialization. These timings include full-law validation and control overhead, are machine-specific, and do not estimate single-output sampling complexity. Neither number measures all integer-bit work.

## Concrete next step, not executed here

For dropping the oldest word, the remaining suffix is a common orthogonal left factor in `T-S`, so a uniform operator-norm certificate for the omitted word can be precomputed from complete actual columns and reused without each prefix's full Gram defect construction. This can trade a more conservative acceptance test for lower certification cost. Any stronger rank-two identity must itself be certified for the specific actual word family. The present audit neither implements that fast path nor claims its savings; it identifies why the current state-dependent certificate costs more than the omitted work on these fixtures.

Reproduce this accounting with `python extract_cost_accounting.py`. It verifies the frozen input/source hashes and rewrites only `COST_ACCOUNTING.json`; it does not import the scientific modules or rerun the experiment.
