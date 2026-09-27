# Adjacent-trace source review

Status: **STATIC PASS / SHARED CONTEXT / NOT EXECUTED / NOT ADMITTED**.

Complete final files reviewed:

| File | SHA-256 |
| --- | --- |
| `adjacent_trace.py` | `d1b0d497ecf8c028e6f4cec8b8322f47d30fa2437c2828825bd79f727d3dda87` |
| `PLAN.md` | `590b59350b55e38121c3517cd8c94dd842fd562c0c36aaa619d1b44f4fb9c050` |
| Comparison contract | `d0a334328bcf1d2be5860a2eca7970aebb3916a9586890e7d0acd4228d21cbf8` |

The author confirmed these source and plan bytes as the final pre-run candidate. This reviewer read the full source and plan and the relevant frozen setup, common-gcd, factor-check, matrix-validation and modular wrapper interfaces. No scientific module was imported, no fixture or numerical reference was evaluated, and no source was modified by this review. The existing translated-trace and two-clock proofs, and the separate geometric review, supply the mathematical contracts.

## Findings

No blocking defect was found for the declared four-case grid. The first three cases are the historical matched inputs; the fourth `(77,3,6,8)` is retained as an unpaired second-clock test. The supplied Eplus2 label is independently checked by an actual unsigned addition to E, charged in setup. It is not used as an unverified replacement for E+2.

The ordered-pair induction is correct. Each bit uses the old pair for its cross product and selected square, subtracts the fixed original k and two through the typed wrappers, and only then commits the appropriate ordered result. Both branches cost two modular multiplications and two modular subtractions at the wrapper-call level, including the leading bit. No inversion fold or discarded orientation is introduced. This count is not asserted to equal the total digit or execution cost.

Both signed expressions implement the right residuals. The antipodal expressions use actual modular addition. The first clock is obtained from the common ideal of tau and w; the union from the single w gcd; the second clock from actual positive integer division with a zero-remainder check. The frozen factor checker supplies exact N/divisor receipts for every proper result. All signs and probes run even after an earlier factor is found, as stated. The implementation does not compute a point order or use a saved answer in production.

The separate validation route independently computes complete matrices at E and the checked E+2, forms two actual successive M products, and compares chronology. It compares both adjacent traces, inverse and determinant identities, all four residual entries and their complete common gcds for both clocks and signs. The cyclic residual reconstruction has signs `[[y-kx,x],[-x,y]]`; the transformed expressions are `2y-kx` and `ky-2x`. Both are correctly implemented. The two clock divisors are checked coprime using the actual common-gcd path, and their product is checked with an actual non-modular multiplication against the union gcd. Thus the exact quotient is compared with a separately computed full-matrix event, not an expected factor.

The regular setup condition is enforced before using the discriminant-unit theorem. Unexpected setup failure on this declared grid is retained as failure, not silently replaced by another trace. The reused old setup is literal, while the additional clock check is separately linked and billed. No inverse or modular table is expected in any new route, and this is checked after each case.

## Comparison, accounting and provenance

The seven categories separate setup, power, signed expressions, joint gcds, single gcds, quotient and validation. Direct arithmetic includes the exact clock product and factor divisions; cached gcd receipts remain chargeable through the unchanged collector. The small native catalog call count is not substituted for digit replay or host bit costs. Validation remains separately visible and is not a production speed claim.

The baseline gzip and decoded payload have fixed hashes. Baseline reading occurs only after every new case and its paid validation has completed. The comparison checks equal inputs/setup, V_E and both signed first-clock gcds/classes. It preserves historical extra point/single-coordinate outputs and their invoices. The fourth case is explicitly unpaired, and the result metadata disclaims an equal-output end-to-end ratio. This follows the comparison contract: the two power components produce different representations and the complete interfaces differ.

Source, plan, guard and frozen dependencies are checked before import and rechecked before successful persistence. STARTED and outputs use exclusive creation; existing failure artifacts also reject blind rerun. Case and parent records are registered before child work, and failure snapshots preserve available routes, outer records, completed or partial outputs and native calls. As the plan states, an unreturned constructor or primitive may lack its final internal record. The failure status is not a resumable checkpoint and no intentional failure experiment is added by this review.

The residual-cocycle and geometric notes are separate symbolic extensions. This program does not silently execute a J register, add a defect observer, or claim a complete HBW branching histogram. Its mathematical mechanism is the stated classical adjacent Lucas recurrence through actual native arithmetic plus certified marked return observation. Favorable parameter/exponent selection, generic success probability and Shor closure remain open.

Conclusion: the final source is suitable for the already declared single finite run once the coordinator supplies the actual current guard. This review certifies only the static source/contract agreement; saved numerical results and complete costs require their own post-run evidence audit.

Global-Knowledge-Sync: shared-author previously read canonical context; the implementation distinguishes its author's actual policy snapshot from the coordinator's execution read SHA. This reviewer makes no claim of another independent handshake.
