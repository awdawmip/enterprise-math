# Shared-author static review of the direct four-square constructor

Status: AUTHOR_STATIC_CROSS_CHECK / SHARED_CONTEXT / UNREVIEWED /
NOT_ADMITTED. The reviewer wrote the preceding constructive theorem and had
access to the same research conversation. This is not independent admission,
an external review, or a fresh scientific execution.

Researcher EM-DIRECT-C6438C; activity RA-CAAAC604CB513AEA8BBC1DFC.
Control Source `f0e5fb6f478a5a380ab5a7533d2585f7f43ee3bf`.

## Scope and result

I read the complete constructor, its profile, cursor negative-control script,
execution note, and the saved partial/complete/negative-control payloads. File
and decompressed-payload hashing and JSON inspection were ordinary artifact
inspection. I did not invoke the constructor, a native scientific executor,
an ideal reference, or a new four-square search during this review.

No material inconsistency was found between the stated bounded m3 construction
and the four-square theorem. The half-angle, rounding direction, native
arithmetic, canonical routing, whole-carrier certificate and successful cursor
continuation agree with their declared contracts. The scope limits in section
7 remain essential; this finding does not convert the one-case implementation
into a general arbitrary-input constructor.

Reviewed bindings:

| Item | SHA256 |
| --- | --- |
| `construct_direct_word.py` | `c5089d39d6beb95a031f066d54098d9589430064379e20dfa56eefe0e211f7ad` |
| Direct profile | `e554697f67080ffc741ca2beb3910d124a327d929c0295027db6803627e696ee` |
| Frozen general compiler | `e8f7048e2e73292bda230a2adad4aaa76f0b3cd5525f8f0899628bd649d1d81d` |
| Constructive theorem | `8bc25b5c26d3016de69913f2dae666a0c80b14fe71af13066baccd15ded7b6d9` |
| Complete uncompressed payload | `d29cd6b789cc07eafe430117c31b3e5fe918cda041550ea6e0b1894154a5ab82` |
| Partial uncompressed payload | `34feb2a04bd5e26ac7b0baecf24ff6a8d48e82fd85f866d4d98c939159fd894e` |
| Negative-control uncompressed payload | `f6d7bc24214103a31b9f1182ffabd4e4b17c6625f9c4902094e9fa52074d831a` |

## 1. Target index, sign and floor choices

`construct_leading_normal` requests `isolate_target(M+1, OBSERVER_BITS)`.
For the fixed fixture this is q4 at depth 16, while the final strict phase
certificate is for m3. The distinction is correct: c(q4),s(q4) describe the
unit normal at half the phase angle, and the reflection pair doubles that
angle into U3. There is no off-by-one phase index.

The first floor uses the upper root endpoint in c:

    floor(S*(1-u^2)/(1+u^2)),

and the second uses the lower endpoint in s:

    floor(S*2l/(1+l^2)).

Thus both coordinates are lower bounds, as required to make K nonnegative.
`floor_ratio` does not evaluate a floating ratio or call an ordinary square
root. It runs signed positive-path comparisons at each binary-search label
and retains the two final floor boundary inequalities. Its upper range is
checked by another actual comparison. The initial lower label zero is valid
because the numerator is nonnegative and denominator positive.

The scale test, S squared, leading-coordinate squared deficit, and K<5S test
all pass through the actual positive-path observer. The saved values are
S=4096, leading numerators 3784 and 1567, and K=3071. These were read from the
artifact; this review did not recompute an ideal half-angle approximation.

The frozen `FixedRotor` produces the temporal sequence

    g ; D0 ; reverse(g) ; D0,

whose matrix is `D0 G^T D0 G = D0(2zz^T-I)`. This is precisely the negative
phase convention `[[c,s],[-s,c]]` used by the current compiler. The argument
does not accidentally reverse the phase.

## 2. The four-square search observes the arithmetic it uses

Every integer square-table entry is returned by `PositivePathObserver`, then
compared with K by another actual signed observation. The table terminates at
the first excluded label and retains its strict witness; in the saved example
labels 0 through 55 are included and 56 is excluded.

`four_square_search` observes each pair sum and then its complement K minus
that sum. The Python dictionary stores those already observed integer labels
and their source-coordinate labels. Dictionary membership computes neither a
missing square nor a missing complement, and inserts no runtime gate weight.
The counter/bisection/routing integers are finite control labels; scientific
squares, sums and comparison expressions are executed by the actual observer.

The matching algorithm is complete once the square table is complete. Every
four-square witness can be grouped into two pairs and sorted within each pair.
Both pairs appear in the x<=y enumeration; the later pair finds the earlier
observed sum. If the pairs coincide, insertion before the lookup correctly
allows reuse of that pair, as four-square representations permit repeated
coordinates. Pair sums exceeding K cannot participate and are safely skipped.

Most importantly, a dictionary match is not the final arithmetic certificate.
All four returned coordinate labels are freshly squared and added by actual
paths, and their difference from K must be zero. The complete 61-coordinate
integer vector is then checked by the frozen `brc_square_budget` positive
paths and compared with S squared. The saved witness is `(1,55,3,6)` and the
saved complete norm observation is 16777216 with difference zero.

The imported Lagrange theorem justifies existence for general mathematical
inputs; it is not passed off as an executed arithmetic oracle. For this
bounded case, the explicit observed witness suffices to establish completion.

## 3. Actual word synthesis and exact 62-letter routing

`FixedRotor` invokes the existing `synthesize_unit`, and checks the generated
full word on all 61 actual basis columns and inverse recoveries. Its rank-one
formula appears only as the frozen native-word quotient check inside that
constructor; the direct script does not apply an ideal target propagator to
a dynamic state. No Shor state is propagated in this unit.

The routing function resets its position map for each indexed letter. After
processing slot j, that slot contains the jth requested original coordinate;
earlier filled slots are never disturbed because each remaining requested
coordinate is distinct and therefore lies at or to the right of its slot.
Moving it left by adjacent swaps preserves the induction. If P denotes those
actual swaps, the temporal expansion is P, then the canonical gate, then
P inverse, giving the required indexed gate by conjugation. In particular,
the order of the four H4 input coordinates is preserved, not merely their set.

Every expanded letter is checked against the frozen canonical alphabet.
Routing may temporarily move any intervening coordinates, but the inverse
routing restores their labels. All 61 actual indexed columns are compared
with all 61 canonical columns, providing a concrete whole-carrier equality
check in addition to the symbolic conjugation argument.

The saved indexed word has 190 letters; its canonical expansion has 8114.
Both are within the constructive theorem's conservative bounds at B=12.
The determinant-positive test is applied to the actual canonical word. All
residual coordinates are retained, including the four completion modes.

## 4. The returned error claim is bound to the new actual word

The canonical word is submitted as one finite candidate to the unchanged
compiler. The API parameter is named `seeds`, but the value is the newly
constructed word; no old bank is opened or imported as a candidate source.

The returned phase record retains the word, m3, dimension 61, requested
tolerance 1/4, all actual columns, inverse recovery and target interval. Its
strict full-carrier squared Frobenius upper bound is recorded as

    20131175847326871336023 / 13274693657165679533490176,

against threshold 1/16. The native signed margin is positive. Acceptance comes
from the existing actual positive-path margin observer and complete-column
orthogonality contract, not from the constructive asymptotic estimate alone.

`verify_phase_record` is called afterward. That function cross-binds the
external record to its certificate and forces fresh actual columns, inverse,
root-probe and margin replay. Therefore an arbitrary word or a merely claimed
bound cannot be attached to a nonempty certificate dictionary. The saved final
phase certificate hash is
`025bcd68659b2db680f7fbfee38080fe214e998cbdefabaaf25e2114108da7a8`.

## 5. Source binding and continuation do not trust saved arithmetic

The request binds the constructor code hash, direct profile hash, construction
proof hash, exact fixture parameters, full compiler binding and frozen compiler
hash. Resume requires exact equality of that request and status `PARTIAL`.
The previous normal, square table or display counters are not trusted as
scientific inputs: the constructor regenerates them through actual observers.

The authoritative search cursor is the ordered pair-record prefix. Each prior
record is recomputed in deterministic enumeration order and compared with its
saved labels, ordinal, observed sum and observed complement before continuing.
A purported partial prefix that already contains a completing witness is
rejected. This prevents a saved prefix from silently skipping an earlier
success or replacing arithmetic by its serialized output.

The `next_pair` and `next_pair_ordinal` fields are non-authoritative summaries;
the code never uses them to jump forward. Altering them cannot skip new
observations. This is safe and is now explicitly stated in the execution note.
A shortened prefix can cause recomputation, but cannot fabricate a certificate.

The complete artifact records two pairs replayed and 167 newly observed pairs,
for 169 total. Its request agrees with the earlier partial. The three saved
negative controls report rejection of a changed target tolerance, a false
completed cursor, and a corrupted observed pair sum. Their evidence is separate
from this static review: I inspected it, but did not rerun those calls.

## 6. Resource and execution evidence

The first partial payload reports 280 actual core calls and no phase record.
The resumed complete payload reports 754 calls and 497 constructor observer
operations, including fresh phase verification. The negative-control payload
reports 278 calls for the corrupted-pair replay and zero calls for the two
request/status rejections. These counts describe the author's saved runs,
not an independent execution performed by this reviewer.

`pair_budget` counts only new pair observations. Root/floor/square construction,
prefix replay and final certification are additional finite work. The square
limit separately bounds its label search. Neither resource is a hard wall-clock
limit or a guarantee that interruption during an in-progress call leaves a
checkpoint. The execution note states this distinction correctly.

## 7. Scope limits, without turning them into research blockers

The current implementation hardcodes m3, delta=1/4, B=12 and h=16; its CLI caps
the square-label limit at 256. That matches the requested bounded fixture.
It does not yet implement a general parameter-selecting direct constructor for
every m and delta. The general existence, explicit depth and cost statements
remain in the separate symbolic theorem; the previously implemented fair
compiler still supplies the general interface.

This direct fixture is not a new full Shor run, random-frequency experiment,
efficient classical factorization result or independently admitted physical
measurement model. Its useful new output is concrete: a fresh canonical word,
actual four-square and full-carrier error certificates, and a replayable
partial-to-complete construction route. No code changes are required by this
review for that declared result.

Global-Knowledge-Sync: main@441ebef / GLOBAL_KNOWLEDGE_V1
