# Adjacent-trace saved-record execution review

Status: **PASS_STDLIB_ADJACENT_TRACE_SAVED_RECORD_REVIEW_NOT_ADMISSION**.
This is a shared-context source-and-record review by EM-DIRECT-C6438C under the existing activity RA-CAAAC604CB513AEA8BBC1DFC. It is not independent admission. The reviewer ran only the standard-library evidence reader, with no scientific module import, new native call, modular reference calculation, or rerun of either experiment.

## Bound execution and complete record coverage

The actual execution receipt reports chunk `c117ac`, exit code 0. Its parsed output equals `ADJACENT_TRACE_SUMMARY.json`. The reader checked the source, PLAN, declared dependencies, STARTED binding, startup guard and raw/gzip bytes. The later-added `reused_interfaces` binding is explicitly distinguished from STARTED; the remaining execution binding agrees.

| Artifact | SHA-256 |
|---|---|
| `adjacent_trace.py` | `d1b0d497ecf8c028e6f4cec8b8322f47d30fa2437c2828825bd79f727d3dda87` |
| `PLAN.md` | `590b59350b55e38121c3517cd8c94dd842fd562c0c36aaa619d1b44f4fb9c050` |
| Uncompressed result, 3,598,285 bytes | `21eefcdd65c06eff0ef932eee3b0c80a0d62345273ef3c810daa8937b621b216` |
| Result gzip, 192,274 bytes | `3d14f0eb84432a1f0b7b6a5ea3e7637b147c2acfa08519d7d482ed2fe177111f` |
| `ADJACENT_TRACE_SUMMARY.json` | `a81116ae57fe1f9af33b3ec035c1de4b17967a12456f75c557d8291d4dccf566` |
| `ACTUAL_EXECUTION_TOOL_RESULT.json` | `39b1a8e3b93de4b18a1108c9f49ef674a3990bb91eac7160ac1a5ff3ee917df4` |
| `read_adjacent_trace_records.py` | `fbbcc0f5c7282439e2ec2ae8ab098f60eeafee89abdd3fdb26afcbbdcc61f139` |
| `ADJACENT_TRACE_RECORD_REVIEW.json` | `1f4231e16943ff6c5e295fe2fc8e335e9815b5103813cf7813f4b3897254d09f` |

The reader uses only selected AST definitions from hash-pinned prior I/O readers; it does not import their scientific dependencies. It consumed every saved native digit cell and typed operation, every chronological outer record, and all route cursors. The total is **40 arithmetic streams, 77,933 native-column digit replays, 1,990 typed operations and 1,017 outer wiring nodes**. There is one saved native catalog call, `recurrent_mass_power` on 12 states at depth 1. That call count is reported separately from the much larger digit-replay work.

The new wiring checks cover all 14 public exponent bits; the selected square, cross product and two subtractions per bit; both signed translated expressions; 32 common-coordinate gcd records with 96 coordinates and 206 Euclidean divisions; all eight exact second-clock divisions and proper-factor division receipts; and all eight signed two-clock full-matrix checks. The validation consumes 53 matrix products, eight independent matrix powers and 16 complete signed matrix-residual ideals. It also checks the cyclic-coordinate/trace bridge, matrix chronology, determinants, inverse relations and the saved paid product/coprimality validation. No extra host gcd, power or modular propagation supplies an expected answer.

## Observed results

Each tuple below gives `(main divisor, union divisor, exact second-clock divisor)` from the saved typed outputs. Identity and antipodal signs remain separate; their factors are not inferred from a merged trace.

| Input `(N,k,E)` | Identity | Antipodal |
|---|---|---|
| `(77,3,4)` | `(1,1,1)` | `(7,7,1)` |
| `(77,3,8)` | `(7,77,11)` | `(1,1,1)` |
| `(49,3,8)` | `(7,7,1)` | `(1,1,1)` |
| `(77,3,6)` | `(1,7,7)` | `(1,1,1)` |

The saturated union 77 in the second case is split by the marked first-clock divisor and an actual exact quotient. This is a useful two-clock interface result. It is **not a newly discovered factor relative to every old observer**: the old `(77,3,8)` antipodal single-coordinate output already included factor 11. The prime-power case preserves primitive divisor 7 despite the identity trace residual being zero modulo 49. The fourth case tests a second-clock hit when the main-clock divisor is 1; it has no paired old run and is excluded from paired cost totals.

The historical comparison uses the already saved free-trace raw payload `bd9ccd13f75e41b44edcfd294990ce1bd5673011fe906b4780c05662dfe70158` and gzip `2b714edc7cd51728377ef5269451724feb96a8896af3037fcb60101ef09e37c5`. The reader verified the common setup values, trace and both signed primitive divisors for the first three cases. The historical file is equality and invoice evidence, not an input to scientific propagation. No historical experiment was rerun.

## Complete costs and comparison boundary

All entries below are saved native-column digit replays, administratively recounted from the underlying records.

| Input | Setup | Power | Expressions | Joint | Single | Quotient | Validation | Production |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `(77,3,4)` | 393 | 605 | 234 | 758 | 892 | 28 | 15,576 | 2,910 |
| `(77,3,8)` | 394 | 1,123 | 174 | 604 | 166 | 138 | 19,652 | 2,599 |
| `(49,3,8)` | 359 | 1,007 | 156 | 284 | 518 | 28 | 14,947 | 2,352 |
| `(77,3,6)` | 393 | 788 | 231 | 386 | 658 | 76 | 17,365 | 2,532 |
| Total | 1,539 | 3,523 | 795 | 2,032 | 2,234 | 270 | 67,540 | 10,393 |

Production includes every requested setup/readout/quotient operation. Validation is charged separately and included in the **77,933** total. The full ledger also reports **827,495 host bit-wiring operations** and **13,048 arithmetic bit-length calls**; these are not native catalog calls and are not omitted. New setup includes the paid integer check of the public `Eplus2=E+2` relation, so its total is not asserted equal to the older setup bill.

For the first three shared inputs, the new power component costs **2,735** digit replays versus **4,612** in the old polynomial-coordinate implementation. This is an observed component reduction between different internal representations. Old power returns coefficients/point information, whereas the new power returns ordered adjacent traces; their complete output interfaces differ. The two-multiplication-per-bit statement follows the saved new operation links, not elapsed time.

For transparency, the first-three whole production invoices are 7,861 new versus 13,844 old, while validation is **50,175 new versus 23,875 old**. The new validation additionally computes the second clock and checks the quotient decomposition; the old production includes coordinate outputs that the new production does not return. These are complete invoices with differing output contracts, **not an equal-output end-to-end speed ratio**. The fourth case and its validation are not added to the old comparison. No matched wall-clock benchmark, general success-rate guarantee or polynomial-time factoring result follows from this unit.

## Scope and continuation

No substantive record or source mismatch was found. This audit establishes that the declared finite execution and its seven cost categories are fully supported by the saved typed/native records. It does not replace the symbolic regularity and two-clock proofs, validate arbitrary altered Python objects, or claim arbitrary interrupted primitives are resumable. No failure occurred in this run; the source's available-record failure snapshots remain explicitly non-resumable.

The frozen comparison contract and pre-run review remain applicable. Jacobi filtering, new clock schedules and off-conic history observers are separate symbolic proposals and were not executed here. Any authorized conversation can continue from the pinned proofs, interfaces and complete saved evidence without relying on the original driver identity.

Policy provenance: retained author and coordinator actual-read markers from the execution binding; no new independent Global Knowledge handshake or formal admission is asserted by this saved-record audit.
