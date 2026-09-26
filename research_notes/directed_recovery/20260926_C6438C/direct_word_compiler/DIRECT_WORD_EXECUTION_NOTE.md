# A directly constructed native phase: actual bounded execution

Status: **AUTHOR_ACTUAL_BOUNDED_EXECUTION / SHARED_CONTEXT / NOT_ADMITTED**.
Researcher `EM-DIRECT-C6438C`; activity `RA-CAAAC604CB513AEA8BBC1DFC`.
Control Source `f0e5fb6f478a5a380ab5a7533d2585f7f43ee3bf`.
Frozen primitive Source `0852cad130c1d877174d235687cf60c19f318c58`.

The new constructor actually generated a phase word without reading a legacy
phase bank or its seeds. It completed the bounded case `m = 3`, `delta = 1/4`
on all 61 retained coordinates. Its canonical word uses only the existing 62
fixed generators and passes the frozen compiler's strict full-column error
certificate and fresh verifier replay. No Shor state, ideal distribution,
trigonometric evaluator or alternative propagator was executed here.

## Concrete result

| Quantity | Actual observation or construction |
| --- | --- |
| Native-word denominator exponent | `B = 12`, `S = 4096` |
| Algebraic observer depth | `h = 16` |
| Half-angle root used to construct normal | `q4` |
| First two integer coordinates | `3784, 1567` |
| Observed squared-norm deficit | `K = 3071` |
| Observed four-square witness | `1, 55, 3, 6` |
| Complete normal | `(3784,1567,1,55,3,6,0,...,0)/4096`, 61 coordinates |
| Observed complete integer squared norm | `16777216 = 4096^2` |
| Integer square table | Labels `0,...,55`; label `56` excluded by actual difference `3071-3136 = -65` |
| Observed two-square pairs before witness | `169` |
| Indexed native phase word | `190` letters |
| Exact 62-letter expansion | `8114` letters: 24 H4, 164 negations, 7926 adjacent swaps |
| Complete columns and inverse recovery | All `61` passed |
| Indexed versus canonical expansion | All `61` actual columns exactly equal |
| Frozen verifier status | `VERIFIED`, operator error strictly below `1/4` |

The frozen observer's full-carrier squared Frobenius upper bound is

    20131175847326871336023 / 13274693657165679533490176 < 1/16.

Its actual cross-multiplied signed margin is positive:

    809537177725528099507113 / 9671406556917033397649408 > 0.

This bounds arbitrary full-carrier inputs, including residual modes. It is
stronger than checking just the two initially occupied coordinates. No
residual component was dropped, reset, renormalized or postselected.

## Actual arithmetic and retained provenance

`construct_direct_word.py` uses the existing compiler's
`PositivePathObserver` and `isolate_target`. The latter runs the frozen
polynomial probes and the previously defined closed-endpoint extension for
the target recursion. The constructor observes squares of the `q4` interval
endpoints, forms the positive rational floor-comparison expressions, and
finds the two floors using signed positive-path comparisons in integer-label
bisection. It never obtains the floors from an ordinary floating evaluation.

The scale sufficiency, leading squared-norm deficit, `K < 5S` bound, every
integer square-table entry, each pair sum and each complement `K - pair_sum`
are actual endpoint observations. The dictionary merely matches exact
integer labels already returned by these observers. It computes no missing
square or complement and supplies no runtime gate coefficients. For each
processed pair the certificate retains the labels, observed sum and observed
complement, together with the positive-path graph operations and endpoints.

The four returned coordinates are squared and summed again by the actual
observer; their difference from K must be zero. The full 61-coordinate norm
is independently executed by the frozen `brc_square_budget` positive paths
and compared with `S^2`. The existing `synthesize_unit` and `FixedRotor` then
produce and check the literal native phase. The constructor does not use its
rank-one quotient as a new propagator.

Each indexed native gate is expanded as a permutation conjugate of a
canonical generator. Ordered source coordinates are moved to the first one,
two or four positions by adjacent swaps; the canonical gate is applied; the
same swaps are reversed. This preserves the order of H4's indexed inputs.
Every expanded letter is checked for membership in the frozen 62-generator
alphabet, and every full actual column is compared with the original indexed
word. The expansion has positive determinant.

The newly generated word is submitted as the sole finite candidate to the
unchanged compiler (`pair_budget = 1`). This argument is named `seeds` in its
API, but its contents are the new four-square word, not a loaded legacy seed.
The target of this final certificate is correctly `q3`; `q4` appears only in
the candidate-normal construction. `verify_phase_record` then forces fresh
native-column, inverse, root-observer and strict-margin replay.

The complete certificate includes the constructor source/profile hashes,
proof hash, frozen compiler and native source binding, complete polynomial
probe evidence, every constructor observation, 61-column comparisons, both
word forms, routing receipts, final compiler certificate and actual kernel
call receipts.

## Bounded interruption and the executed resume

The first process was limited to two new pair observations. It returned
`PARTIAL` with its exact source/target request, square table, pair records and
next pair cursor. It made 280 actual core calls and emitted no phase word or
false error certificate.

A fresh process loaded this file, checked the same constructor/compiler,
profile and target binding, reconstructed the target/floor/square witnesses,
and replayed the two stored pair records through the actual observer. It then
processed 167 new pairs and returned `CERTIFIED`, including fresh phase
verification. This process made 754 actual core calls. Resume deliberately
replays the finite observed prefix; it does not trust stored arithmetic
results as a substitute for native execution.

The authoritative pair continuation is the ordered `records` prefix, which is
recomputed and compared exactly. The saved `next_pair` and ordinal are display
summaries; they are not trusted to skip unobserved pairs. Altering a summary
cannot change the resumed enumeration or create a false certificate.

The constructor also has a bounded square-label limit. If it is exhausted,
the output records `PARTIAL` and the next square label. A continuation may
increase this resource bound and reconstruct the finite prefix. Current CLI
scope caps this label limit at 256 and fixes the scientific example to
`m = 3, delta = 1/4, B = 12, h = 16`; it is not an arbitrary-precision driver.

The new cursor negative controls rejected three changes: a substituted target
tolerance; a false completed status; and an altered observed pair sum. The
first two were rejected before any scientific call. Pair corruption was
rejected after 278 actual replay calls. These checks are stored separately;
they do not rerun an ideal comparison or broaden the example.

## Reproduce the bounded artifacts

Use the same pinned source environment and Python runtime. The first command
produces a resumable partial file, the second completes that cursor, and the
third checks the new cursor rejection paths:

```powershell
& 'D:/kimi-query-bridge/.venv/Scripts/python.exe' -B -S 'D:/em/TEMP/sep26-shor-general/direct_word_compiler/construct_direct_word.py' --pair-budget 2 --out 'D:/em/TEMP/sep26-shor-general/direct_word_compiler/DIRECT_WORD_PARTIAL.json.gz'
& 'D:/kimi-query-bridge/.venv/Scripts/python.exe' -B -S 'D:/em/TEMP/sep26-shor-general/direct_word_compiler/construct_direct_word.py' --pair-budget 5000 --resume 'D:/em/TEMP/sep26-shor-general/direct_word_compiler/DIRECT_WORD_PARTIAL.json.gz' --out 'D:/em/TEMP/sep26-shor-general/direct_word_compiler/DIRECT_WORD_CERTIFICATE.json.gz'
& 'D:/kimi-query-bridge/.venv/Scripts/python.exe' -B -S 'D:/em/TEMP/sep26-shor-general/direct_word_compiler/check_direct_cursor.py'
```

The scripts return all status information in the saved JSON, with deterministic
gzip metadata and a separate concise summary. Finite `PARTIAL` is not evidence
that a word does not exist. An external termination before a call returns is
not claimed to be a persisted checkpoint.

## Artifact bindings and scope

| Artifact | SHA-256 |
| --- | --- |
| `construct_direct_word.py` | `c5089d39d6beb95a031f066d54098d9589430064379e20dfa56eefe0e211f7ad` |
| `DIRECT_WORD_PROFILE.json` | `e554697f67080ffc741ca2beb3910d124a327d929c0295027db6803627e696ee` |
| Frozen `certified_word_compiler.py` | `e8f7048e2e73292bda230a2adad4aaa76f0b3cd5525f8f0899628bd649d1d81d` |
| Construction proof | `8bc25b5c26d3016de69913f2dae666a0c80b14fe71af13066baccd15ded7b6d9` |
| Partial uncompressed payload | `34feb2a04bd5e26ac7b0baecf24ff6a8d48e82fd85f866d4d98c939159fd894e` |
| Complete uncompressed payload | `d29cd6b789cc07eafe430117c31b3e5fe918cda041550ea6e0b1894154a5ab82` |
| Complete `.json.gz` bytes | `94fd5ce96376cef3532e5a9c8c2b9930ddcfccca6255afc3e5d2450696c373f9` |
| Final phase certificate | `025bcd68659b2db680f7fbfee38080fe214e998cbdefabaaf25e2114108da7a8` |
| Negative-control uncompressed payload | `f6d7bc24214103a31b9f1182ffabd4e4b17c6625f9c4902094e9fa52074d831a` |

The symbolic general construction is in
`../new_word_compiler/CONSTRUCTIVE_FOUR_SQUARE_FRONTIER.md`; this directory adds
one actual independent-candidate fixture and its finite resume/replay path.
It does not replace the frozen fair compiler or the full factorization
driver, and does not claim every requested phase or tolerance was executed.
The new denominator exponent and algebraic observation horizon are explicitly
part of this new native-word constructor. The legacy target32/vector64 bank
and all primitive coefficients remain unchanged. The full simulator still
has its work-state costs; this result is not a claim of efficient classical
factoring or a derived physical measurement law.

Global-Knowledge-Sync: main@441ebef / GLOBAL_KNOWLEDGE_V1
