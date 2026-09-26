# Shared static review of the general direct phase constructor

Status: AUTHOR_STATIC_CROSS_CHECK / SHARED_CONTEXT / UNREVIEWED /
NOT_ADMITTED. The reviewer also wrote the shared constructive theorem and
reviewed the earlier bounded constructor. This is not independent admission.

Researcher EM-DIRECT-C6438C; activity RA-CAAAC604CB513AEA8BBC1DFC.
Scientific Control Source `f0e5fb6f478a5a380ab5a7533d2585f7f43ee3bf` and primitive
source `0852cad130c1d877174d235687cf60c19f318c58` remain frozen. Current global
control snapshot 8446003 was read from the root agent's freshly verified
canonical snapshot; this subreview did not independently refresh the remote.

## Result and inspected sources

No material implementation defect was found in the generalization at source
SHA256 `830b2f0c0c206a53e2b349fe377976d369ebfb76d4dfc5aad494db88ab6e0c63`.
The implementation now accepts every integer m>=3 and every explicit positive
rational tolerance, selects the least sufficient B by actual strict probes,
and permits the square-label resource bound to grow without a hard cap.

I read the full source, profile, the source diff against the previously
reviewed bounded constructor, the four saved demonstration payloads, the
boundary-check script/payload, and the final general-constructor note.
Hashing, diffing and JSON inspection were ordinary artifact inspection only.
I did not rerun a scientific executor or construct another phase for this
review. The unchanged arithmetic, dictionary matching, ordered gate routing
and whole-carrier verifier are also covered by
`../direct_word_compiler/SHARED_CONSTRUCTOR_REVIEW.md`.

Bindings:

- General source: `830b2f0c0c206a53e2b349fe377976d369ebfb76d4dfc5aad494db88ab6e0c63`.
- General profile: `6c868c98b8b81f45f6f4c1c77ed4389c813dbc02513a55ac78ec0f7d3acb669d`.
- Frozen strict compiler: `e8f7048e2e73292bda230a2adad4aaa76f0b3cd5525f8f0899628bd649d1d81d`.
- Constructive theorem: `8bc25b5c26d3016de69913f2dae666a0c80b14fe71af13066baccd15ded7b6d9`.

## 1. Input and least-scale selection

`build(m,tolerance,pair_budget,square_label_limit,previous)` validates m>=3
as an integer excluding bool; tolerance as an explicit positive rational;
and both budgets as nonnegative integers excluding bool. Floating target
inputs are not silently rounded. Rational strings are normalized before
source/target binding, so equivalent representations denote the same target.
The exact m2 phase belongs to the existing separate exact-quarter interface.

`choose_scale` starts at B=2 and observes `2^B*delta^2-128` through actual
positive paths for every successive B. It returns only at the first strictly
positive observation. Since delta>0, such a finite B exists. No candidate is
skipped; all earlier observations are retained, proving minimality among B>=2.
An equality must advance, not accept.

The saved quarter-tolerance example records zero at B=11 and positive at B=12.
The eighth-tolerance example records zero at B=13 and positive at B=14. Thus
the exact-threshold branch appears in both execution records, not merely in
an untested source condition. Setting h=B+4 matches the theorem's sufficient
strict full-Frobenius certificate depth.

Large or very small positive tolerances cause no fixed mathematical cutoff:
large tolerances can use B=2, while smaller tolerances lead to more actual
scale probes. The selected B is a composite-word resource; no primitive
coefficient or legacy target32/vector64 record is changed.

## 2. The generalized target path stays aligned

The selected m and B replace all four prior fixture constants. Normal
construction still observes q_(m+1), rounds c(u) and s(l) downward, and verifies
K>=0 and K<5S by the native path observer. `FixedRotor` receives the same
selected B used by the integer normal. The final strict certificate receives
m, delta and observer depth B+4. Thus there is no surviving hardcoded m3 or
quarter-tolerance target in the synthesis/verification path.

The ordered canonical expansion and 61 indexed-versus-canonical comparisons
are unchanged. All complete column, inverse, source/target and strict-margin
checks remain enabled. The direct word is freshly constructed; the general
implementation does not load a frozen phase seed bank.

By the already derived bounds, `S>128/delta^2` and h=B+4 give
`E_upper<84/S<delta^2`. Therefore the code's expectation that this one candidate
passes the frozen verifier has a uniform mathematical justification, rather
than an extrapolation from the two examples.

## 3. Square resources and genuine continuation

The earlier fixed CLI restriction at 256 is removed. The default is still
256, but any nonnegative integer square-label limit is accepted. The loop
observes every square and stops either at the first actual square exceeding K
or at the caller's current resource bound. A resource stop is `PARTIAL`, not
a mathematical no-solution result.

The first excluded label is finite because K is finite. Increasing the square
limit eventually completes that table. Its accepted entries are exactly the
labels from zero through floor(sqrt(K)); this conclusion follows from their
actual comparisons and does not require a numerical square-root evaluation.

Once the table is complete, the unchanged observed-pair search is finite and
complete. Its dictionary matches only actual observed integer sums and
complements. A candidate witness is independently squared and added again by
native paths, and the complete integer normal receives the existing actual
norm check before any word is accepted.

There is a simple terminating continuation policy: increase the square-label
bound until its table completes, then keep supplying a positive finite budget
of new pairs. A complete table has only finitely many ordered pair records;
each unfinished continuation advances through them. The API permits this
policy but does not silently run it forever on behalf of a bounded caller.
Passing zero new-pair budgets indefinitely is not claimed to terminate.

## 4. Cursor integrity and resource semantics

Before scientific reconstruction, the cursor must have status `PARTIAL` and
match schema, source, m, normalized delta and dimension. The caller must retain
or increase the previous square-label resource bound. This prevents a completed
square table and its pair prefix from being replaced by an earlier square-only
partial. Changing a resource limit does not change the mathematical target.

B and h are then recomputed by actual scale probes, and the complete derived
request must exactly match the saved request. Altered derived parameters are
therefore not trusted merely because the base target fields agree. The source
binding includes the direct source/profile, constructive theorem, frozen
compiler, primitive source and kernel.

The implementation regenerates the normal and square observations and replays
every saved pair record in deterministic order. Previously observed arithmetic
is not treated as fresh execution merely by deserialization. As in the bounded
version, `records` is the authoritative prefix; displayed next-pair counters
do not direct an unchecked jump. A forged prefix containing a successful
witness under status `PARTIAL` is rejected.

The budgets are deliberately separate. `square_label_limit` bounds the label
frontier for that call; `pair_budget` bounds newly observed pairs after replay.
Scale/root/floor work, square reconstruction, prefix replay and final full-word
certification are extra finite work. Neither budget is a wall-clock deadline,
and zero pair budget does not mean zero scientific calls. Interruption during
a call is not an automatically persisted checkpoint; a returned `PARTIAL`
is the durable continuation object.

## 5. Saved execution evidence inspected

These are the implementer's actual run records, not new runs by this reviewer.

| Case | Result | B/h | Saved calls | Relevant evidence |
| --- | --- | --- | --- | --- |
| m4, delta=1/4 | CERTIFIED | 12/16 | 664 | 56 pairs; 8112 canonical letters; all 61 columns |
| m3, delta=1/8, square limit 32 | PARTIAL | 14/18 | 258 | next square label 33; no phase certificate |
| Same target, square limit 256, two pairs | PARTIAL | 14/18 | 582 | table complete; exactly two saved pair records |
| Same target, resumed pair search | CERTIFIED | 14/18 | 2196 | two pairs replayed, 735 new pairs; 8384 letters; all 61 columns |

The quarter case has K=2526 and witness `(0,50,1,5)`. The eighth case has
K=36599 and witness `(3,95,3,166)`. Both complete payloads retain the source-bound
phase record and fresh frozen verifier result. The partial payloads contain
neither a phase word nor a false completed phase certificate.

Decompressed payload SHA256 values:

- `M4_DELTA_QUARTER.json.gz`:
  `1a4ca56447d32704376d4537da3e28550800ac4245093d6e303cef4b4918268c`.
- `M3_EIGHTH_SQUARE_PARTIAL.json.gz`:
  `170c7b3f190931df88066e66bdc2223a23c70bc0215d9b9d580968de963244a6`.
- `M3_EIGHTH_PAIR_PARTIAL.json.gz`:
  `bda8da740bed8aea9e865cf6f9823484362cee2d8c24f02e95ff0854a56c5e54`.
- `M3_DELTA_EIGHTH.json.gz`:
  `0a712b1a918aa7326785605bdbc0e30453962c897286d9e293710f41318858d6`.

## 6. Actual boundary and mutation evidence inspected

The saved `GENERAL_BOUNDARY_CHECKS.json.gz` payload has SHA256
`970be04308c78b3bd8a568815410b8e6b3ba28cc1439e4243af90579435ab2cc`.
Its source binding matches the general source and profile above. I inspected
the complete rejection records and scale probes and verified this decompressed
payload hash; I did not rerun these controls.

All 12 rejection controls passed. Zero/negative/floating tolerance, an
out-of-domain or boolean phase, negative pair/square budgets, changed cursor
phase/tolerance, and reduced square resource were rejected before any actual
kernel call. Substituting the derived B was rejected after 13 actual scale
probes, and corrupting a saved observed pair was rejected after 580 actual
reconstruction/replay calls. These latter controls exercise reconstruction,
rather than merely trusting cursor serialization.

Two additional scale-only cases exercise the lower clamp and exact boundary:
delta=8 accepts B=2 with observed margin 128; delta=4 observes -64, 0, 128 at
B=2, 3, 4 and accepts only B=4. Their four calls bring the boundary artifact
to 597 actual calls. These are scale and mutation checks, not additional
complete phase or Shor executions.

The final `GENERAL_CONSTRUCTOR_NOTE.md`, SHA256
`d1876c86c1a2c5c940bdfa7ce3e4f9d8377c46f46b1bc4a2bfdfbe58ff8e34ba`,
states the same constructor, budget, continuation and bounded-evidence scope.
Its O(K+1) bound counts pair-observer steps in the meet-in-the-middle search;
it does not claim a wall-clock hash-table bound or a polynomial-time factoring
algorithm. I found no discrepancy between that note and the inspected source
or saved payloads. Its historical global-control marker is retained; this
review records the later parent-verified global snapshot separately above.

## 7. Remaining scope, without a new blocker

The interface generalizes the constructor; the demonstrations validate stated
inputs and continuation boundaries. They do not execute every m or tolerance.
The general mathematical result rests on the construction proof plus the
source-level parameter mapping checked here. The current entry point returns
one phase; a whole-bank allocator and direct-word Shor integration are separate
composition steps. No such execution is inferred from these phase records.

The phase-compiler cost result is not a polynomial-time classical factoring
claim. Full retained work-state propagation and the current primality baseline
still have their previously documented costs. No code change is required by
this review for the declared general-constructor interface and bounded runs.

Global-Knowledge-Sync: main@8446003 / GLOBAL_KNOWLEDGE_V1
