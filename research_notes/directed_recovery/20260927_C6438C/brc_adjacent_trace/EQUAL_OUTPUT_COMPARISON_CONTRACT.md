# Equal-output comparison contract for the adjacent-trace successor

Status: **PRE-RUN COMPARISON DESIGN / SHARED CONTEXT / NO NEW SCIENTIFIC EXECUTION**. This contract reads the frozen old source, plan and actual summary. It neither generates answers for the new program nor revises the old experiment.

## Historical reference and fixed scope

The three paired inputs, in order, are `(N,k,E)=(77,3,4), (77,3,8), (49,3,8)`. The additional new input `(77,3,6)` tests the second return clock. It has no old paired execution and must not enter a paired cost total, average, percentage or claimed matched improvement.

The historical directory is `../sep27-brc-hbw-free-trace/native_probe/`:

| File | SHA-256 |
| --- | --- |
| `free_trace_probe.py` | `2f0981f1dd25e8160bcd80207a6bc92d080e291b545f3be62b95eddffdd36708` |
| `PLAN.md` | `c05b238b7c1f1c72319f6bbe3e41652f2d274f41cc05b6cdaf85e7c6a9e4cb52` |
| `FREE_TRACE_SUMMARY.json` | `73fd0e23753e4a8dd46a02c7d24d2bc123c0e267a789a734d6e6fd6bc516c41e` |
| Raw `FREE_TRACE_RESULTS` JSON | `bd9ccd13f75e41b44edcfd294990ce1bd5673011fe906b4780c05662dfe70158` |
| `FREE_TRACE_RESULTS.json.gz` | `2b714edc7cd51728377ef5269451724feb96a8896af3037fcb60101ef09e37c5` |
| `FREE_TRACE_RECORD_REVIEW.json` | `e272d126118e70fe5c528235d7cf7f5afa1ecfe46d6892d4f7e3e8518432832a` |

The old plan's CODE_ONLY marker is its historical pre-run state. Its actual summary and complete record review establish the completed run. Do not rewrite or backdate that plan marker.

## Outputs that can and cannot be matched

For `M=[[0,1],[-1,k]]`, the old production returns coefficients `(c0,c1)` for `M^E=c0 I+c1 M`; the marked column `M^E(0,1)`; `V_E=trace(M^E)`; and, for both signs epsilon, the two individual coordinate gcds, their joint gcd `d_E^epsilon`, and the ordinary trace gcd `gcd(N,V_E-2epsilon)`. It also supplies factor-division certificates. Its separately paid validation constructs the full matrix and further conic, determinant, cyclic-ideal and trace-square checks.

The new adjacent-trace production is intended to return `(V_E,V_(E+1))`, signed translated expressions, the exact same primitive return divisors `d_E^epsilon`, and the extra second-clock divisors `d_(E+2)^epsilon` via exact quotient. This is a different output interface.

Match these common fields only when actually produced with their receipts:

1. Identical public inputs and compatible admitted odd regular setup, including the discriminant residue and gcd/classification.
2. `V_E`, with its residue representative convention explicitly the same.
3. Each signed `d_E^epsilon` and its classification, comparing old joint-coordinate observation with new joint translated-trace observation.
4. Ordinary trace residual/gcd and proper-factor certification only if the new program actually requests those outputs; do not imply they exist for free because they are mathematically recoverable.

The old point coordinates, coefficient pair and individual-coordinate gcds are **not** interchangeable with the new trace pair or the two-clock section. The old N=77,E=8 antipodal single-coordinate observer finds an additional proper factor although the joint antipodal return is a unit; omitting that observable changes available information. Conversely, the old run has no production `V_(E+1)` or E+2 quotient output. Neither route dominates the other's complete recorded output merely by preserving `d_E^epsilon`.

The fourth input must check its E and E+2 clocks using new paid validation, not a supplied expected factor. Historical values are read after production for equality checks, with their hashes bound; they must never choose a scientific branch, initialize a register or replace an operation. Reusing old records is not rerunning the old scientific case.

## Allowed cost statements

Keep setup, power, each readout group and validation separate on both sides. Preserve all rejected/degenerate work and proper-factor divisions. Native catalog calls, digit replays, host bit wiring, bit-length calls, public-bit control and retained evidence sizes are different metrics. No wall-clock ratio is authorized by historical runs performed under different conditions.

The historical digit bills are already actual observations:

| Input | Setup | Polynomial power | Complete old readout | Old validation | Old production |
| --- | ---: | ---: | ---: | ---: | ---: |
| `(77,3,4)` | 389 | 1,019 | 3,183 | 7,398 | 4,591 |
| `(77,3,8)` | 389 | 2,055 | 3,238 | 9,536 | 5,682 |
| `(49,3,8)` | 354 | 1,538 | 1,679 | 6,941 | 3,571 |

Their production total is 13,844 and validation total 23,875. These are the **complete old interfaces**, not a hypothetical minimal old implementation computing only the shared outputs.

Report per-input new setup and new power bills next to their old counterparts. A literal identical setup subprogram can support a matched setup comparison. The power comparison is a measured component comparison between two representations: the old component returns `(c0,c1)`, while the new component returns adjacent traces. State these different contracts alongside the counts. Do not call a power-only ratio an equal-output end-to-end speedup; on the old side extraction of `V_E` occurs in the readout route, and on the new side signed return gcds also require readout work.

For a claimed comparison restricted to common outputs, require a source-bound attribution to those outputs' complete recorded dependency closure, including shared arithmetic, cache-producing gcd receipts and exact factor divisions. Count each retained operation/certificate once. If a common observer reuses work first executed by an extra observer, that work remains chargeable to the common-output closure. Removing a displayed field is not proof that its upstream work can be removed. Such an extraction is an **attribution of the executed record**, not an executed standalone minimal program, timing benchmark or permission to recompute a cheaper old reference on the host.

If that attribution is not implemented and audited in this unit, use the safer report: common-output equalities; measured setup/power component bills; complete old and new production invoices with explicit interface differences; and both validation invoices. A lower complete new invoice can then be reported as a finite observed cost of its specified interface, without presenting an unequal-output ratio as a matched optimization theorem.

Both signs and all requested observers remain charged even after a proper factor is encountered. Exact division for the second-clock quotient and subsequent N/factor certificates must appear in the new invoice. A symbolic two-multiplication-per-bit identity does not predict digit cost: residue sizes, reductions, setup and observers all matter.

## Execution and review gate

This document performs only source and metadata reading. The implementation author will bind its hash together with the complete new source, plan, proof and historical record pins. The coordinator may run the fixed declared grid once after source review and the actual current guard under the existing research authorization. A future authorized conversation can continue the mathematical work and interpret the portable records without the original author or a particular local runtime; actual numerical execution remains subject to the native typed-arithmetic contract.

The post-run audit should identify the three matched cases and fourth unpaired case explicitly, verify common output equality, reconstruct all bills from saved records, and state any cost regressions. It must retain validation separately and make no generic factoring, useful-exponent selection, success-probability or Shor-closure claim.

Global-Knowledge-Sync: shared-author reuse of the previously actually read canonical context; the new execution must retain its coordinator-supplied current read SHA and guard. No fresh independent handshake or scientific execution is asserted by this comparison contract.
