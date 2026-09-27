# Saved elliptic translated-mark execution review

Status: **PASS / COMPLETE SAVED-RECORD READBACK / SHARED-CONTEXT / NOT ADMITTED**.

This review consumed the existing one-run results with a standard-library reader. It did not import the scientific runner or its arithmetic modules, rerun the experiment, compute a modular reference, or call host gcd/power/curve arithmetic. It extends the source-bound pre-run review with complete saved evidence and cost checks; it does not certify a generic factoring algorithm or an independent admission.

## Immutable records read

- Executed `elliptic_mark.py`: `a0186eb10a02f7ad3ed4106cd1395d495379e18e12f03b82b212db7c90fb60da`.
- Executed `PLAN.md`: `8f8660262c7b60fc20def4ddc58164757aa908b9c1854d948bd0093fcb0599fc`.
- Raw JSON: 2,295,574 bytes, SHA-256 `6a2d9b2243f14c73faa5352af041e850b4fcb3d0cb63215ea31277143f7d46da`.
- `ELLIPTIC_MARK_RESULTS.json.gz`: 119,267 bytes, SHA-256 `3f381e2603b9a512f0aea2dd9eb3c8087e36487a7651b742ff2ab49408550c9b`.
- `STARTED.json`, summary, guard bytes and immutable record hash, proof dependencies, old wrapper files and the actual native source bindings were checked against the saved run. No success/failure artifact was overwritten.

The accompanying `read_elliptic_records.py` only AST-selects named record-audit definitions from the three pinned older I/O readers. No top-level code from those readers or any scientific source executes. The new observer-specific review follows each saved operation role, input, result and child ID, and consumes every outer record in chronology. `ELLIPTIC_RECORD_REVIEW.json` retains the exact bindings, pins, native call metadata, counts, case outputs and route-by-route accounting.

## Complete checks and outcomes

All **44 arithmetic streams**, **40,878 saved native digit cells**, **1,416 typed operations** and **712 outer records** passed. Each saved digit transition was checked against the actual admitted native column catalog. The one catalog invocation is separately recorded as `recurrent_mass_power`, 12 states, depth 1; it is not substituted for the replay or arithmetic cost.

The reader checked all setup links and paid smoothness/unit gcds; the 10 differential additions and 10 selected Kummer doublings; fixed-P difference and public-bit routing; all intermediate primitive-pair checks; the translated expression; three distinct readouts; and every proper-factor division certificate. The **39 common-gcd requests** cover **88 coordinates** with **161 actual Euclidean division links**, including coordinate-to-coordinate accumulator handoff and terminal zero remainders. Direct route counters and cached gcd work were separately consumed.

Paid full-point validation includes 10 complete curve/primitive checks and 7 Jacobian doublings, the transformed coefficients and initial point, all retained full-point states, terminal original-x cross relations, equality of the marked divisor with the full-point return divisor, and the ordinary Kummer square-valuation comparisons. This validates EP independently of the x-only arithmetic. The adjacent `(E+1)P` contract remains the checked ladder induction, rather than a second full-point propagation.

| Input `(N,A,E)` | Ordinary Kummer gcd | Marked joint gcd | Single-W gcd | Full-point gcd |
| --- | ---: | ---: | ---: | ---: |
| `(9,0,4)` | 9 | 3 | 3 | 3 |
| `(35,4,8)` | 5 | 5 | 5 | 5 |
| `(19,0,4)` | 1 | 1 | 1 | 1 |

The N=9 result confirms the intended prime-power saturation repair in a predeclared observation fixture. The N=35 case preserves a proper factor, and N=19 retains no-hit. These are finite observation outcomes, not a sampled success-rate estimate. No factor or expected residue was supplied to the production program.

## Complete cost ledger

The numbers below are native full-adder digit replays reconstructed from all saved streams. They are not wall-clock measurements or field-operation estimates.

| Input | Setup | Ladder | Ordinary | Mark expression | Marked gcd | Single W | Validation | Production, all three probes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `(9,0,4)` | 666 | 1,497 | 8 | 57 | 78 | 124 | 2,749 | 2,430 |
| `(35,4,8)` | 1,790 | 6,409 | 158 | 56 | 124 | 158 | 15,945 | 8,695 |
| `(19,0,4)` | 1,254 | 3,081 | 176 | 118 | 122 | 74 | 6,234 | 4,825 |

Production including setup and all three probes totals **15,950**; validation adds **24,928**; total **40,878**. Host bit wiring is **440,052** and arithmetic bit-length calls are **8,568**. All seven categories match the saved summary and route invoices. Native catalog initialization is one call, reported separately. The retained evidence and input/output records are not constant-space merely because the live point register count is small.

No material discrepancy was found. The evidence supports an actually executed typed elliptic ladder and an unsquared translated identity observation, including the deliberately selected prime-power repair. It does not establish a faster factoring procedure, a useful exponent or curve selector, or a Shor closure. No timing or generic performance claim is made.

Global-Knowledge-Sync: shared-author policy context and the coordinator's actual execution guard/read SHA are retained verbatim in the reviewed binding; this I/O review does not manufacture a fresh independent activity handshake.
