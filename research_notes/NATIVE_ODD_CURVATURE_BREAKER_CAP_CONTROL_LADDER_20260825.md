# Odd-curvature filament: breaker-cap control ladder 1 / 5 / 9 / >9

Status: `FREE_RESEARCH_EXACT_PHASE_CONTROLS / NOT_CANONICAL_ENTERPRISE_GEOMETRY`

Date: `2026-08-25`

Researcher-ID: `EM-FREE-NEPS-239A6D`

Only B=3 is the current native Enterprise specialization. Other B values are controlled comparator families.

## 1. Purpose

The odd-curvature phase theorem predicts that the first universal breaker can only be 2, 3, or 5, with sharp breaker-coprime run capacities

- q=2 -> 1;
- q=3 -> 5;
- q=5 -> 9.

The no-break phase has no finite congruence cap forced by any finite prime wheel.

This note records exact / actual-prime controls across all four phases.

## 2. First-breaker-2 phase

Take any odd B with B=1 mod4, for example B=1.

Modulo2 the shell values alternate parity for every transverse H. Therefore every two consecutive values contain an even value.

Once both values exceed2, they cannot both be prime.

Hence the nonexceptional all-prime run cap is exactly1.

This is an exact parity theorem; no search is required.

## 3. First-breaker-3 phase: actual sharp 5-prime realization

Take

`B=7`, `H=15`, `R=1`.

Then

`F_7(H,r)=H+(7r^2+eps(r))/2`.

At shells r=1,...,5 the values are

`19, 29, 47, 71, 103`.

All five are prime.

The next value is

`F_7(15,6)=141=3*47`.

Thus the exact first-breaker-3 capacity

`2*3-1=5`

is attained by actual primes.

## 4. First-breaker-5 phase: native sharp9

The actual tri-sector coefficient is B=3.

Channels2 and3 are nonbreaking and channel5 is the first universal breaker.

The already-frozen native prime-incidence theorem gives an actual nine-prime filament / island attaining the exact cap

`2*5-1=9`.

Therefore the q=5 phase capacity is also prime-realized.

## 5. No-break phase: the 9-cap disappears

Take B=15, a no-break phase.

The separately frozen control witness

`R=610`, `H=977767522784021`

contains twelve consecutive actual prime filament values.

Therefore the native 9-cap is not a generic quadratic/parity cap.

It is specific to the B=3 first-breaker-5 phase.

No assertion of an unbounded prime-run length is made in the no-break phase; the twelve-prime packet is only a finite control witness.

## 6. Phase-control table

| phase | representative B | first breaker | exact finite cap | actual prime realization |
|---|---:|---:|---:|---|
| 2-break | 1 | 2 | 1 | trivial one-prime states |
| 3-break | 7 | 3 | 5 | `19,29,47,71,103` |
| 5-break | 3 | 5 | 9 | frozen native sharp-nine packet |
| no-break | 15 | none | no finite breaker cap | explicit 12-prime packet |

## 7. Interpretation

The control ladder isolates the role of the universal breaker:

`FIRST BREAKER q`

`-> PERIOD 2q COVERING`

`-> SHARP BREAKER-COPRIME RUN CAP 2q-1`,

with actual prime realizations at q=3 and q=5.

The B=15 control shows that when the breaker mechanism is removed, prime runs can already exceed the native q=5 cap.

This supports the causal statement

`NATIVE SHARP9 IS BREAKER-PHASE SPECIFIC`.

## 8. Boundary

The finite witnesses do not imply arbitrary-length prime runs. The phase caps concern congruence eligibility / universal-breaker obstructions; actual prime realization beyond the displayed finite packets remains a separate prime-tuple problem.