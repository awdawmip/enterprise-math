# General direct native-word constructor

Status: **AUTHOR_IMPLEMENTATION_WITH_BOUNDED_ACTUAL_EVIDENCE / SHARED_CONTEXT / NOT_ADMITTED**.
Activity `RA-CAAAC604CB513AEA8BBC1DFC`; control Source
`f0e5fb6f478a5a380ab5a7533d2585f7f43ee3bf`; frozen primitive Source
`0852cad130c1d877174d235687cf60c19f318c58`.

This directory parameterizes the separately frozen bounded four-square
constructor. It accepts every integer phase index `m >= 3` and every explicit
positive rational tolerance `delta`, derives its own denominator and observer
depth, and returns either a fully verified actual native word or a resumable
budget-limited `PARTIAL`. It has no fixed phase cutoff, no old seed dependency,
and no fixed upper bound on the new construction denominator or square-table
resource. Two genuinely new bounded cases were executed successfully.

## Interface and mathematical contract

```python
build(m, tolerance, pair_budget=5000, square_label_limit=256, previous=None)
```

`tolerance` is an integer, exact `Fraction`, or explicit rational string.
Floats and booleans are rejected. `m` is an integer at least three; both work
budgets are nonnegative integers. The exact `m = 2` quarter-turn remains in
the existing compiler rather than being unnecessarily approximated here.

Starting at `B = 2`, actual signed positive-path observations test
`2^B * delta^2 - 128`. The first strictly positive result determines B, so
equality is not accepted and the selected exponent is the least allowed one.
The target observer depth is `h = B + 4`. These two new resources belong to
the direct word construction. They do not change the frozen target32/vector64
bank or any H4/sign/swap coefficient.

The actual `q_(m+1)` root interval supplies lower bounds for the two coordinates
of the half-angle normal. Actual positive-path comparisons determine their
scaled floors. The squared deficit, integer square table, pair sums and pair
complements are all actual signed observations. An exact dictionary matches
only those observed integer labels. The returned four-square witness and
complete 61-coordinate norm are then checked again through the actual kernel.

Frozen `synthesize_unit` and `FixedRotor` generate the indexed word. Adjacent
swap conjugation expands it to the precise 62 fixed letters. All 61 actual
columns of the indexed and canonical words are checked for equality. The
canonical word is the sole newly constructed candidate supplied to the
frozen `compile_phase` interface, with its target `q_m`, requested delta and
derived h. The same frozen `verify_phase_record` forces fresh complete-column,
inverse, target-interval and strict-error replay.

The general proof is
`../new_word_compiler/CONSTRUCTIVE_FOUR_SQUARE_FRONTIER.md`. It supplies
`K < 5S`, with `S = 2^B`, a four-square witness on four retained completion
coordinates, and the full-carrier strict certificate bound
`E_upper < 84/S < delta^2`. Thus for each valid input, sufficiently large
finite budgets contain a completing witness and an accepted word. This is a
general mathematical and implementation contract, not a claim that infinitely
many inputs have been executed.

The pair search enumerates `0 <= x <= y <= floor(sqrt(K))`. It never evaluates
an ordinary square root: the observed square table supplies that last label
and one strictly excluded successor. Every four-square witness can be divided
into two such unordered pairs; whichever matching pair appears second finds
the first in the dictionary. Hence this search is complete. Its number of
pair-observer steps is at most `(R+1)(R+2)/2`, with `R = floor(sqrt(K))`, and
therefore O(K+1). This counts arithmetic observations, not an asserted
wall-clock or adversarial hash-table complexity bound. It also does not remove
the full Shor simulator's work-state or factor-precheck costs.

## Budget and continuation semantics

`square_label_limit` is the inclusive maximum label tried in the current
square-table construction. The table must also observe the first square
strictly above K to be complete. If the limit is reached first, the result
contains `PARTIAL`, all observations and the next square label. The resource
can be increased on the next call. It is not a maximum phase index or a
maximum mathematical precision.

`pair_budget` counts **new** pair observations in a call after replaying any
saved prefix. A finite exhausted budget returns `PARTIAL` with the exact
source/target binding and ordered pair records. Resume verifies that binding,
recomputes the minimal B and h, reconstructs target/floor/square evidence,
replays every saved pair record through the actual observer, and then
continues. The displayed next-pair summary does not skip observations; the
ordered replayed records are authoritative.

The square-label budget may be retained or increased on resume, and cannot
be reduced in a way that would discard prior completed work. The pair budget
may independently control how many additional pairs are allowed. Budgets
are excluded from the mathematical target binding, so increasing them does
not invalidate a valid source/target cursor. Changing m, delta, the derived
denominator, source or profile is rejected. Source changes require a new
source-bound computation rather than silently relabelled old receipts.

These limits do not bound root-observer work, prefix replays, full-column
verification or elapsed time. A completed finite call is the persistence
boundary; external interruption of a running call is not claimed to have
written a checkpoint. The CLI records every returned result and exact
uncompressed-payload hash.

## Two new actual cases

| Quantity | `m = 4, delta = 1/4` | `m = 3, delta = 1/8` |
| --- | --- | --- |
| Minimal B / observer h | `12 / 16` | `14 / 18` |
| Leading integer coordinates | `4017, 799` | `15136, 6269` |
| Actual deficit K | `2526` | `36599` |
| Four-square witness | `0, 50, 1, 5` | `3, 95, 3, 166` |
| Observed pair count | `56` | `737` |
| Indexed word length | `196` | `220` |
| Canonical 62-letter length | `8112` | `8384` |
| Complete columns/inverses verified | `61 / 61` | `61 / 61` |
| Final-call actual core calls | `664` | `2196` |
| Final status | `CERTIFIED`, fresh `VERIFIED` | `CERTIFIED`, fresh `VERIFIED` |

The exact full-carrier squared-error upper bounds are, respectively,

    191514090365828812991 / 153703173796158569971712 < 1/16,
    3750978093348286315397167 / 3398349075850160959913984000 < 1/64.

Acceptance comes from the positive actual cross-multiplied margin recorded
in each frozen compiler certificate. The ideal target matrix is never used
to propagate a dynamic state. All residual directions remain present.

The second case was deliberately executed across three processes:

1. Square-label limit 32: `PARTIAL`, 258 actual core calls, no pair phase.
2. Resume with square-label limit 256 and two new pairs: `PARTIAL`, 582 calls.
3. Resume with 5,000 new pairs permitted: `CERTIFIED`, 2,196 calls; the two
   previous pair records were actually replayed before the 735 new pairs.

This tests both growth of the square resource and continuation of the pair
resource. The successful two phase records are available as
`json_payload['phase_record']`, suitable for the existing frozen phase-record
verifier and bank adapter. This directory does not itself run a Shor program
or assert a whole-program error allocation for those two unrelated requests.

## Boundary and mutation checks

`check_general_boundaries.py` performed 12 rejection controls: zero, negative
and floating tolerance; phase index below three or boolean; negative pair and
square budgets; altered phase and tolerance in resume; a reduced square
budget; a substituted derived denominator; and a corrupted observed pair sum.
All were rejected. The first ten consumed no actual kernel calls; the derived
denominator check consumed 13 scale probes, and the pair check consumed 580
actual replay calls.

Two further actual scale-boundary checks cover the lower clamp and strict
inequality: delta 8 selects B2 immediately; delta 4 gives observed margins
`-64, 0, 128` at B2, B3 and B4, selecting B4. The boundary artifact has 597
actual core calls in total. No extra phase, ideal reference or Shor execution
was performed for these checks.

## Reproduction

```powershell
& 'D:/kimi-query-bridge/.venv/Scripts/python.exe' -B -S 'D:/em/TEMP/sep26-shor-general/direct_word_compiler_general/construct_general_word.py' --phase-index 4 --tolerance 1/4 --pair-budget 5000 --out 'D:/em/TEMP/sep26-shor-general/direct_word_compiler_general/M4_DELTA_QUARTER.json.gz'
& 'D:/kimi-query-bridge/.venv/Scripts/python.exe' -B -S 'D:/em/TEMP/sep26-shor-general/direct_word_compiler_general/construct_general_word.py' --phase-index 3 --tolerance 1/8 --square-label-limit 32 --pair-budget 2 --out 'D:/em/TEMP/sep26-shor-general/direct_word_compiler_general/M3_EIGHTH_SQUARE_PARTIAL.json.gz'
& 'D:/kimi-query-bridge/.venv/Scripts/python.exe' -B -S 'D:/em/TEMP/sep26-shor-general/direct_word_compiler_general/construct_general_word.py' --phase-index 3 --tolerance 1/8 --square-label-limit 256 --pair-budget 2 --resume 'D:/em/TEMP/sep26-shor-general/direct_word_compiler_general/M3_EIGHTH_SQUARE_PARTIAL.json.gz' --out 'D:/em/TEMP/sep26-shor-general/direct_word_compiler_general/M3_EIGHTH_PAIR_PARTIAL.json.gz'
& 'D:/kimi-query-bridge/.venv/Scripts/python.exe' -B -S 'D:/em/TEMP/sep26-shor-general/direct_word_compiler_general/construct_general_word.py' --phase-index 3 --tolerance 1/8 --square-label-limit 256 --pair-budget 5000 --resume 'D:/em/TEMP/sep26-shor-general/direct_word_compiler_general/M3_EIGHTH_PAIR_PARTIAL.json.gz' --out 'D:/em/TEMP/sep26-shor-general/direct_word_compiler_general/M3_DELTA_EIGHTH.json.gz'
& 'D:/kimi-query-bridge/.venv/Scripts/python.exe' -B -S 'D:/em/TEMP/sep26-shor-general/direct_word_compiler_general/check_general_boundaries.py'
```

Each `.json.gz` artifact contains the full certificate/receipt payload; its
parallel `.summary.json` is a convenience view. Existing bounded examples and
the frozen compiler are unchanged.

## Source and payload hashes

| File or payload | SHA-256 |
| --- | --- |
| `construct_general_word.py` | `830b2f0c0c206a53e2b349fe377976d369ebfb76d4dfc5aad494db88ab6e0c63` |
| `DIRECT_WORD_PROFILE.json` | `6c868c98b8b81f45f6f4c1c77ed4389c813dbc02513a55ac78ec0f7d3acb669d` |
| Frozen certifier | `e8f7048e2e73292bda230a2adad4aaa76f0b3cd5525f8f0899628bd649d1d81d` |
| General construction proof | `8bc25b5c26d3016de69913f2dae666a0c80b14fe71af13066baccd15ded7b6d9` |
| M4 quarter-tolerance uncompressed payload | `1a4ca56447d32704376d4537da3e28550800ac4245093d6e303cef4b4918268c` |
| M3 eighth-tolerance uncompressed payload | `0a712b1a918aa7326785605bdbc0e30453962c897286d9e293710f41318858d6` |
| M3 square-partial uncompressed payload | `170c7b3f190931df88066e66bdc2223a23c70bc0215d9b9d580968de963244a6` |
| M3 pair-partial uncompressed payload | `bda8da740bed8aea9e865cf6f9823484362cee2d8c24f02e95ff0854a56c5e54` |
| Boundary-check uncompressed payload | `970be04308c78b3bd8a568815410b8e6b3ba28cc1439e4243af90579435ab2cc` |

The scientific claims remain symbolic general termination plus these finite
actual executions. They do not establish practical complexity at arbitrary
inputs, polynomial-time classical factoring, physical randomness, formal
admission or an ideal-reference numerical benchmark.

Global-Knowledge-Sync: main@441ebef / GLOBAL_KNOWLEDGE_V1
