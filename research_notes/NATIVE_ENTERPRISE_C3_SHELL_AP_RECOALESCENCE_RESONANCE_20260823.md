# Enterprise C3 shell arithmetic-progression decomposition and modular recoalescence

Status: `FREE_RESEARCH_EXACT_STRUCTURE / COMPUTATIONAL_RESONANCE_CHECK / NOT_CANONICAL_FOUNDATION`

Date: `2026-08-23`

Researcher-ID: `EM-FREE-NEPS-239A6D`

Parent: `NATIVE_ENTERPRISE_C3_BISECTOR_PRIME_BOUQUET_20260823.md`

## 1. Exact shell decomposition

In the frozen tri-sector allocation, shell `r` contains exactly `3r` labels. Let

`B_r = 3r(r-1)/2 + 1`

be the first label of shell `r`.

For every side offset

`t = 0,1,...,r-1`,

the three cyclically corresponding C3 addresses have labels

`B_r+t`, `B_r+t+r`, `B_r+t+2r`.

Therefore every shell is partitioned exactly into `r` C3 orbits, and every orbit is a three-term arithmetic progression whose common difference is the native shell index itself:

`C3_ROTATION_STEP = NATIVE_SHELL_INDEX = r`.

This is placement-combinatorial and does not use a Euclidean metric.

## 2. Universal triple-prime shell gate

Suppose all three entries of one C3 orbit are primes greater than 3.

If `r` is odd, the middle term has opposite parity from the two outer terms, so one term is an even integer greater than 2.

If `3 does not divide r`, then the three terms occupy all three residue classes modulo 3, so one is divisible by 3 and exceeds 3.

Hence every non-exceptional fully bright C3 orbit satisfies

`6 | r`.

Thus the basic native prime-shell quantization is

`FULL_C3_PRIME_ORBIT => r = 0 mod 6`.

The checker verifies this for every shell through `r=5000`.

## 3. Equal-coordinate midpoint is the reflection-fixed orbit

When `r` is even, the unique side midpoint has `t=r/2`, corresponding to the equal-coordinate loci

`(m,m,0)`, `(0,m,m)`, `(m,0,m)`

with `r=2m`.

Its labels are

`M_-(r) = (3r^2 - 2r + 2)/2`,

`M_0(r) = (3r^2 + 2)/2`,

`M_+(r) = (3r^2 + 2r + 2)/2`.

Equivalently in `m`:

`6m^2-2m+1`, `6m^2+1`, `6m^2+2m+1`.

They obey the exact balance law

`M_0-M_- = M_+-M_0 = r`.

So the arithmetic common difference of the three prime candidates is literally the native shell number.

## 4. Exact 210-shell modular recoalescence

The previous exact 3*5*7 gate gives

`SIMULTANEOUS_MIDPOINT_PRIMALITY => 105 | m`.

Since `r=2m`, this becomes the native-coordinate statement

`SIMULTANEOUS_MIDPOINT_PRIMALITY => 210 | r`.

For `r=210k`, all three labels satisfy

`M_-(r) = M_0(r) = M_+(r) = 1 mod 210`.

Thus three different cyclic sectors, while distinct as addresses and integer labels, recoalesce to one residue class after the mod-210 readout:

`THREE_SECTOR_MIDPOINTS -> ONE MODULAR READOUT CLASS 1 (mod 210)`.

Conversely, because the three labels differ by `r`, common congruence modulo 210 forces `210 | r`; with the midpoint formula the common class is then exactly 1.

This is the current native interpretation of the old “105 gate”.

## 5. Pairwise coprimality

For every positive `m`, the three midpoint labels are pairwise coprime.

Write `F0=6m^2+1` and `F±=F0±2m`. Since `gcd(F0,m)=1` and all three values are odd,

`gcd(F0,F±)=gcd(F0,2m)=1`,

and similarly

`gcd(F-,F+)=1`.

Therefore every prime divisor of the product is routed into exactly one of the three C3 lanes. The small-prime gate is not produced by a common factor shared by the three values.

## 6. Maximum-saturation selection principle

Every primitive native ray produces three quadratic label polynomials. Their product has degree at most six and constant term 1. Therefore, modulo a prime `q`, the union of all lane roots has at most six residue slots unless a degree drops, which only decreases the bound.

Hence a single prime can cover every nonzero residue class only if

`q-1 <= 6`,

so no prime `q>7` can be a complete mandatory-divisibility gate for any such C3 quadratic orbit.

Thus `3*5*7=105` is the absolute largest product obtainable from individual complete-coverage odd-prime gates in the three-quadratic C3 architecture.

The equal-coordinate ray `(u,v)=(1,1)` attains all three gates 3,5,7. Exhaustive primitive-ray enumeration shows:

- `(1,1)` is the only primitive class with `u+v<37` attaining all three saturated gates;
- the next classes are `(1,36)` and `(36,1)`, at complexity `u+v=37`.

So the midpoint is currently selected simultaneously by:

1. reflection/C3 presentation symmetry;
2. low C3 prime-rate imbalance in the frozen census;
3. minimum primitive complexity;
4. attainment of the theoretical maximum small-prime saturation gate.

## 7. Four-color higher-prime root spectrum

For midpoint polynomials and every odd prime `q>5`, the exact root-union count is

`omega(q)=3+2*(-20/q)+(-24/q)`

and belongs to `{0,2,4,6}`.

The two quadratic characters have joint conductor 120, so the root count depends only on `q mod 120`. Among the 32 reduced residue classes mod 120, each root-count color occupies exactly eight classes:

`omega=0`: `13,17,19,37,71,91,113,119`;

`omega=2`: `11,31,53,59,73,77,79,97`;

`omega=4`: `23,41,43,47,61,67,89,109`;

`omega=6`: `1,7,29,49,83,101,103,107`.

The exceptional prime 7 belongs to the six-root color and is exactly small enough that its six roots exhaust all six nonzero residues. Later primes in the same color have six roots but cannot saturate because `q-1>6`.

## 8. No second single-class gate beyond 210

After writing `r=210k`, multiplication by 105 is invertible modulo every prime `q>7`, so the same `omega(q)` controls excluded `k` residues.

For every `q>7`,

`q-omega(q) >= q-6 >= 5`.

For any finite collection `S` of primes greater than 7, the Chinese remainder theorem therefore leaves exactly

`product_{q in S} (q-omega(q))`

admissible classes modulo `product S`, in particular at least `5^|S|` classes.

Hence there is no second finite prime-by-prime saturation stage that recoalesces the surviving `k` values to one residue class.

The architecture changes after 210:

`SATURATED RECOALESCENCE (2,3,5,7) -> BRANCHING SURVIVOR BASIN (q>7)`.

This is an exact negative result, not a failed search.

## 9. Whole-shell prime resonance

For a general shell `r`, each of its `r` C3 orbits is a linear prime triple in the side-offset `t`:

`n`, `n+r`, `n+2r`.

For a prime `p>3`, the local root count is one if `p|r` and three if `p does not divide r`. Relative to a shell not carrying `p`, adding `p|r` multiplies the standard local triple-prime singular factor by

`(p-1)/(p-3)`.

Therefore shells carrying extra small prime factors are predicted to be “bright” C3-resonance shells.

Finite census through `r=5000` gives:

- hottest shell: `r=4620 = 4*3*5*7*11`, with 27 fully-prime C3 orbits;
- `r=2310 = 2*3*5*7*11` has 18;
- the ten highest raw counts are at `4620,4950,4260,3990,3570,2310,4830,4290,4200,3690`.

After the crude opportunity normalization `r/log(1.5 r^2)^3`, the Pearson correlation with

`R(r)=product_{p|r,p>3}(p-1)/(p-3)`

is approximately `0.625606875` over admissible shells `30<=r<=5000`.

This finite statistic is only an empirical resonance check; the local-factor mechanism is classical prime-tuple arithmetic. The Enterprise-specific content is that the factorization acts directly on the native shell coordinate `r`.

## 10. Large midpoint check

Using deterministic 64-bit Miller-Rabin after the exact `r=210k` reduction:

- `k<=200,000`: 794 simultaneous midpoint-prime events;
- `k<=1,000,000`: 3,071 events.

For `k<=1,000,000`, the largest tested labels are below `2^64`.

A Bateman-Horn-style local-density calculation using the exact root profile and a prime product through `10^6` predicts about `3,026` events at this scale, within about 1.5% of the observed count. This is heuristic agreement, not an infinitude proof.

## 11. Current structural picture

The native allocation now has a hierarchy:

`SHELL r`

`-> r C3 ORBITS`

`-> EACH ORBIT IS A 3-TERM AP WITH GAP r`

`-> FULL PRIME ORBIT REQUIRES 6|r`

`-> REFLECTION-FIXED MIDPOINT MAXIMALLY STRENGTHENS THIS TO 210|r`

`-> THREE MIDPOINT LANES RECOALESCE TO 1 mod 210`

`-> HIGHER PRIME SIEVES NO LONGER RECOALESCE; THEY BRANCH IN A 120-PERIODIC FOUR-COLOR ROOT SPECTRUM`

`-> SMALL PRIME FACTORS OF r CREATE WHOLE-SHELL C3 PRIME RESONANCE`.

This is currently the strongest “beautiful distribution” mechanism found in the native Enterprise coordinate system.
