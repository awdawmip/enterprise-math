# HBW marked-section pre-run review

Status: PASS_FOR_DECLARED_BOUNDED_RUN / SHARED_CONTEXT / NOT_ADMITTED. This is full static source/plan review and metadata hashing only. The reviewer did not import the scientific module, call its arithmetic, compile it, or execute either fixture. No expanded grid is requested.

## Exact reviewed inputs

| File | SHA-256 |
|---|---|
| `hbw_marked_section.py` | `e2929468d9b430f9a0ef93a3412f132c692ce994c7b5061bece21a3960974851` |
| `PLAN.md` | `45790e24d270fdd3382d8012e9539979818499f6c5126967eef893dc9c664ea6` |
| `STARTUP_GUARD.json` | `c9087341fe2db3f62b8be1d2a74f78398a1021b973a790cb239dd1c5383d37fc` |
| `../HBW_MARKED_SECTION_CONJUGACY.md` | `fbec0b42234fe7a126e5bf03b14842ee0935d7801836b4dce99e5b6167346ce1` |

The copied startup guard is byte-identical by SHA-256 to the root `CHECKPOINT_GUARD.json`; the source binds the declared activity and immutable record hash. The complete inherited `native_relative_port.py` was previously read, and its actual `Arithmetic.add/compare/divide/modmul/modsubtract` signatures and table/inverse costs were checked again for this integration. Frozen conic source, plan, gzip and decoded payload pins are checked before scientific imports. The current code also checks its source/plan/declared dependency bytes at the end.

## Mathematical and operational checks

No blocking defect found for the declared main N35/a2/t3 comparison and N25/a2/u6 observer fixture.

* Setup computes b, delta, k and their gcd through the typed route. It distinguishes SETUP_FACTOR and DEGENERATE; neither branch is being represented as executed by these two regular fixtures.
* The same original a,b,k,delta and marker L are retained across all layers. Forward and inverse matrices are squared separately; the scalar square chain is validation work. No layer substitutes the current multiplier into a different marker.
* All matrix entries, negative-one construction, matrix products, matrix-vector products, modular sums/subtractions, marker evaluations and canonical comparisons use the inherited actual typed arithmetic. The reference values only enter equality assertions after the corresponding computation.
* `validate_matrices` checks both inverse orders, S squared, S M S, and the **modular** P intertwining relation. It is a finite check using the common typed matrix implementation, supported by the separate symbolic proof; it is not an independent matrix algorithm or proof of equality on the unreduced lattice.
* Each live branch is observed before folding. Identity multiplicity is `2[1/4]`, directional multiplicities are one each, and an absorbed factor transports `[1]` with the original factor and first-hit depth. The source retains complete microscopic histograms, not just their masses.
* The saved inverse-pair representative was chosen by u, while the new representative is chosen by w. `reference_projection` correctly applies typed P, checks the old/new gcd, applies typed S-folding, and recoalesces via the existing histogram interface. It does not compare incompatible representative integers or overwrite colliding fibers. Every main layer and the terminal output are compared.
* The prime-power fixture pays for the inverse of 6, checks its unit product, maps with P, and computes original, naive-trace, marked and S-reflected marked gcds. The expected `(5,25,5)` tuple is an asserted observation, not supplied factor information used to construct the trajectory.

The source does not claim that the residue states are public Cell addresses or that a macro-arrow is one primitive spatial step. Its source/header/plan consistently scope the experiment to a modular observer quotient. This is an observer-faithful bridge; regular P is a bijection, so it establishes neither orbit compression nor an order readout, and does not close native Shor.

## Receipts, failure and accounting

The six distinct routes are main setup, production, matrix schedule, validation, prime-power setup and prime-power fixture. `route_cost` counts each route's direct arithmetic plus its cached gcd/inverse and any modular table setup/column ledgers once. Wiring references do not cause the embedded operations to be charged again. Saved conic costs are historical metadata, not a new run or timing benchmark. The one native catalog count is separate from total digit/host-bit replay work.

`observed_gcd` deliberately obtains an explicit difference link and then calls the inherited observer, which recomputes the difference. This is extra paid work, fully retained in the direct route ledger; no first-grid optimization is requested. Production uses direct typed matrix arithmetic and should have no state inverse certificates or modular tables, as checked by the source.

Before scientific imports, existing STARTED/success/failure files are rejected and STARTED is exclusively created. `Work.begin` registers an INCOMPLETE outer record before its child calls; completed operation IDs, partially filled branch records, registered routes, completed cases and native CALLS remain available to the exception snapshot. Successful matrix lists are replaced rather than mutated when advancing the square schedule, avoiding retroactive change of earlier layer records.

The failure schema is explicitly `FAILED_NOT_RESUMABLE`. An exception inside an unreturned underlying primitive can precede that primitive's ledger append; this review does not promise its internal state. Nor is the evidence writer an infallible recovery mechanism for filesystem/serialization failure. The plan appropriately avoids calling this a complete mid-operation checkpoint. A successful raw file is never overwritten if a subsequent summary write fails.

This pre-run review approves the existing bounded experiment under the coordinator's actual guard. Result equality, cost or performance is not reported as observed until the coordinator's separate execution produces evidence. No serialized-importer/tamper suite, nonregular setup fixture or full raw-Cell/carry execution is claimed by this unit.

Global-Knowledge-Sync: main@7a63984 / GLOBAL_KNOWLEDGE_V1.
