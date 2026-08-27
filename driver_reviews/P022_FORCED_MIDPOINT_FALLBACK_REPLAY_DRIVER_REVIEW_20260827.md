# Driver Review — P022 Forced-Midpoint Fallback Replay

Status: `DRIVER_FINAL / ACCEPTED / BOUNDED_REPLAY_CLOSED / PARENT_P022_REMAINS_OPEN / NO_PROMOTION`

Date: `2026-08-27`

Driver-ID: `EM-DRIVER-01 / CONTROL_PLANE`

Task: `RS-P022-OBSERVATION-HISTORY`

Publication: `TP2-D78DBA0243911E0363FA`

Execution: `ER-8ACA59C27ECCC2B0CD3F`

Researcher-ID: `EM-P022-A4FCE7`

Result: `RR-4D51F40A41E59F28BA98`

Source result PR: `#702`

Owner-lineage integration: `program/p022-geometry-v2@126bb0f3f1a8e5a6bc4870af0ac6a0583f3348b9`

## 1. Final disposition

`DRIVER_DISPOSITION = ACCEPTED`.

`HARD_TARGET = ACHIEVED`.

`P022_FORCED_MIDPOINT_FALLBACK_CAPTURE_EXACT_AND_INDEPENDENTLY_REPLAY_VERIFIED = true`.

`RESULT_CLASS = EXACT_BOUNDED_THEOREM / LEGACY_REPLAY_FREEZE`.

`DESTINATION = ARCHIVE / P022_OWNER_LINEAGE`.

`FOUNDATION_MUTATION = NONE`.

`WORKING_TRUTH_PROMOTION = NONE`.

`SUCCESSOR_FROM_THIS_REPLAY = NONE`.

The bounded replay is accepted. This closes only the primitive-twin regime `q<6r-1` addressed by this publication. It does not close the P022 parent objective and does not authorize an all-`q` observability claim.

## 2. Decisive theorem audit

Let `q>5` be prime with `q=5 or 23 (mod 24)`, let `m=(q-1)/2`, `B=(q+1)/6`, and suppose the first positive Franel zero modulo `q` is a nontrivial twin center `r`.

The range conversion is exact:

`q<6r-1` iff `q+1<6r` iff `B<r`.

The central-binomial relation at the midpoint has the following complete support above `B`:

- for `q=5 (mod 24)`: only `(m-1,+1)`;
- for `q=23 (mod 24)` with composite `m`: only `(m-1,+1)`;
- for `q=23 (mod 24)` with prime `m`, writing `h=(m+1)/2`: exactly `(h-1,+1),(h,-1),(m-1,+1)`.

Because every support index at most `B` lies below the primitive rank, those terms are `q`-units. The forced midpoint gives `z_m=v_q(F_m)>0`, while adjacent-zero exclusion gives `z_(m-1)=0`.

Hence in the ordinary cases `v_q(D_m)=z_m>0`.

In the prime-midpoint case put `d=h-1=(q-3)/4`. The exact midpoint valuation is

`v_q(D_m)=z_m-z_d+z_h-z_(m-1)`.

If `z_d=0`, then `v_q(D_m)=z_m+z_h>0`.

If `z_d>0`, primitivity gives `d>=r`; equality is impossible because every nontrivial twin center is `0 (mod 3)` while `d=2 (mod 3)`, so `d>=r+2`. The hypothesis `q<6r-1` gives `d<2r-1`. Moreover `2d-1=m-2` is a nontrivial multiple of three in the class `q=23 (mod 24)`, so the defect `D_d` exists. The already-frozen twin-blackout theorem applies on `r+2<=d<2r-1` and gives

`v_q(D_d)=z_d-z_(d-1)`.

Adjacent-zero exclusion gives `z_(d-1)=0`, hence `v_q(D_d)=z_d>0`.

Therefore every target in this bounded regime is detected by `D_d` or `D_m`, no later than `m`.

## 3. Independent regression boundary

The clean-room checker reconstructs the Franel recurrence and central-binomial exponent basis without importing the P022 implementation under test.

Frozen regression:

- target primes `q<50,000` in classes `5,23 (mod 24)`: `1,294`;
- prime-midpoint special-support cases: `193`;
- primitive twin first-zero cases: `12`;
- bounded `q<6r-1` cases: `6`;
- verified bounded captures: `6/6`;
- failures: `0`.

This is accepted only as falsification/regression evidence. The general result rests on the exact support and valuation proof above.

## 4. Method harvest and scope

Method harvest remains:

`RECOVERED_SAME_TASK_OWNER_THEOREM_PLUS_INDEPENDENT_REPLAY`.

This is not a new general-purpose method direction and requires no toolbox mutation. The replay usefully freezes a historically overgrown P022 subgeneration at its exact strength.

The surviving parent frontier is explicitly

`q>=6r-1`.

A later distinct P022 publication/result already attacks the high-range boundary, so this Driver review does not create or redispatch another midpoint-fallback successor.

## 5. Integration boundary

PR `#702` contained only the frozen return, immutable execution/result records, the independent checker and regression artifact. It has been merged into the P022 owner lineage as

`126bb0f3f1a8e5a6bc4870af0ac6a0583f3348b9`.

No CI-success claim is made for this review; the acceptance is based on the exact theorem audit and the independently reconstructed regression evidence.

## 6. Final freeze

`RR-4D51F40A41E59F28BA98 = ACCEPTED`.

`TP2-D78DBA0243911E0363FA = BOUNDED_REPLAY_TERMINAL`.

`P022_q<6r-1_FORCED_MIDPOINT_REPLAY = CLOSED`.

`P022_PARENT_OBJECTIVE = OPEN`.

`REDISPATCH_SAME_REPLAY = FORBIDDEN`.

`NEXT_CONTROL_PLANE_ACTION = REVIEW_EXISTING_DISTINCT_P022_HIGH_RANGE_RETURN_IN_QUEUE`.