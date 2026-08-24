# Odd-curvature no-break control: a twelve-prime filament for B=15

Status: `FREE_RESEARCH_EXACT_FINITE_WITNESS / CONTROL_EXPERIMENT / NOT_CANONICAL_ENTERPRISE_GEOMETRY`

Date: `2026-08-25`

Researcher-ID: `EM-FREE-NEPS-239A6D`

Parent theorem family:

- `NATIVE_FILAMENT_ODD_CURVATURE_DEFORMATION_MASTER_THEOREM_20260825.md`;
- `NATIVE_FILAMENT_ODD_CURVATURE_BREAKER_PHASE_DIAGRAM_MOD60_20260825.md`.

The actual Enterprise tri-sector model is B=3. The B=15 family is a controlled odd-curvature / odd-sector comparator only.

## 1. Purpose

The native B=3 filament has an exact maximal prime-incidence run cap9 because channel5 is a universal breaker.

The general phase theorem predicts that B=15 has no universal breaker at any prime:

- B=3 mod4 -> channel2 nonbreaking;
- 3|B -> channel3 nonbreaking;
- 5|B -> channel5 has three transparent classes;
- every q>=7 has at least one transparent class.

This removes every finite congruence obstruction to long prime runs, but does NOT prove that arbitrarily long all-prime runs exist.

A finite control search was therefore run to test whether actual prime runs can exceed the native hard cap9.

## 2. Exact twelve-prime witness

Take

`B=15`,

`R=610`,

`H=977767522784021`.

For

`F_B(H,r)=H+(B*r^2+eps(r))/2`,

the twelve consecutive values at shells

`r=610,...,621`

are:

1. `977767525574771`
2. `977767525583929`
3. `977767525593101`
4. `977767525602289`
5. `977767525611491`
6. `977767525620709`
7. `977767525629941`
8. `977767525639189`
9. `977767525648451`
10. `977767525657729`
11. `977767525667021`
12. `977767525676329`

All twelve are prime.

They are below `2^64`, so primality was checked with the standard deterministic Miller--Rabin base set for 64-bit integers. An independent SymPy `isprime` replay also returned prime for all twelve values.

## 3. Gap word

The consecutive gaps are

`9158, 9172, 9188, 9202, 9218, 9232, 9248, 9262, 9278, 9292, 9308`.

They satisfy the B=15 alternating-curvature law.

The second differences of the values alternate

`14,16,14,16,...`,

which are exactly

`B-1,B+1`.

Thus the witness lies on the frozen odd-curvature filament dynamics rather than being an unrelated prime tuple.

## 4. Strong control conclusion

The native theorem says

`B=3 -> channel5 breaker -> no all-prime run can exceed9`.

The present explicit comparator says

`B=15 -> no universal breaker -> an actual all-prime run of length12 exists`.

Therefore the sharp native cap9 is NOT a generic consequence of

- quadratic growth;
- parity alternation;
- the fourth-order recurrence;
- or the affine/MDS flattening alone.

It is specifically tied to the arithmetic breaker phase selected by B=3.

Freeze the control statement:

`NATIVE SHARP9 IS BREAKER-PHASE SPECIFIC, NOT ODD-CURVATURE UNIVERSAL`.

## 5. Search protocol

For B=15, a transverse class H was first chosen by CRT to be transparent to every prime up to29.

The resulting arithmetic progression of H values was additionally sieved against primes up to500 for each finite window before deterministic primality testing.

This is only a search acceleration. The final witness is independent of the search procedure and is directly checkable from the displayed integers.

Earlier in the same search, length10 and length11 witnesses were also found. The length12 packet supersedes them as the strongest frozen control witness.

A length13 search was attempted but the current compute window timed out. No conclusion in either direction is drawn from that failed search.

## 6. Boundary

The witness proves only existence of one length12 prime run in the B=15 deformation family.

It does not prove:

- arbitrarily long prime runs;
- an infinitude theorem;
- a Bateman--Horn / Schinzel-type statement;
- or any corresponding result in the actual B=3 Enterprise geometry.

Its role is a controlled counterexample to the hypothesis that the native 9-cap is forced merely by the generic quadratic/parity filament form.