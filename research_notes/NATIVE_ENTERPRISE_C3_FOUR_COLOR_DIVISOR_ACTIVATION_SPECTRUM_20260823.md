# Native Enterprise C3 midpoint: four-color prime-divisor activation spectrum

Status: `FREE_RESEARCH_EXACT_CLASSIFICATION / NOT_CANONICAL_FOUNDATION`

Date: `2026-08-23`

Researcher-ID: `EM-FREE-NEPS-239A6D`

Parent: `NATIVE_ENTERPRISE_C3_BOUQUET_ROOT_PROFILE_20260823.md`

## 1. Setup

For the midpoint bouquet

`F_-(m)=6m^2-2m+1`,

`F_0(m)=6m^2+1`,

`F_+(m)=6m^2+2m+1`,

fix an odd prime `q>5`.

The two outer lanes have discriminant `-20`; the central lane has discriminant `-24`. Hence each outer lane has

`1+Legendre(-20/q)`

roots and the central lane has

`1+Legendre(-24/q)`

roots. Each lane is therefore either inactive (0 roots) or active (2 roots).

The root sets are pairwise disjoint for q>5.

## 2. Active-lane number

Define

`A(q)=number of bouquet lanes on which q can occur as a divisor for some m mod q`.

Then

`A(q)=omega(q)/2`

with

`omega(q)=3+2*Legendre(-20/q)+Legendre(-24/q)`.

Therefore

`A(q) in {0,1,2,3}`.

The four possibilities are exact:

- `A=0`: both characters are -1; q divides none of the three lane values for any integer m;
- `A=1`: outer character -1, central character +1; exactly one lane is active;
- `A=2`: outer character +1, central character -1; exactly the reflection-paired two lanes are active;
- `A=3`: both characters +1; all three lanes are active.

Although the name of an individual lane depends on presentation, the active-lane cardinality is invariant for the unordered bouquet.

## 3. Exact mod-120 color classes

The joint character pair has conductor 120. Among the 32 invertible residue classes modulo 120, the four activation colors each occupy exactly eight classes:

### A=0 / omega=0

`13,17,19,37,71,91,113,119`.

### A=1 / omega=2

`11,31,53,59,73,77,79,97`.

### A=2 / omega=4

`23,41,43,47,61,67,89,109`.

### A=3 / omega=6

`1,7,29,49,83,101,103,107`.

Thus the prime-divisor interaction with the native midpoint bouquet is a four-color residue law:

`PRIME q > 5 -> q mod120 -> 0/1/2/3 active C3 lanes`.

## 4. Dark-divisor primes

For `A(q)=0`, q has no root on any lane. Therefore

`q never divides F_-(m)F_0(m)F_+(m)`

for any integer m.

Examples include primes in the listed classes such as 13,17,19,37,71,113, and so on.

This is an exact exclusion, not a low-frequency statement.

## 5. Fully active primes and the q=7 boundary

For `A(q)=3`, q has two roots on each lane, six disjoint root residues total.

At q=7, six roots exhaust all six nonzero residue classes, producing the last saturated gate and forcing `7|m` for simultaneous primality.

For later fully active primes such as 29 or 83, the same six-root C3 activation exists but `q-1>6`; finite safe branches remain.

Thus q=7 is the unique point where the fully-active color and the small size of the projective residue line coincide to give complete saturation.

## 6. Large finite color balance

As a scale diagnostic, among primes `5<q<=1,000,000` the four activation types occur in counts approximately

- `A=0`: 19,702;
- `A=1`: 19,654;
- `A=2`: 19,638;
- `A=3`: 19,501.

The near quartering is consistent with the exact 8-of-32 residue-class split. This finite count is not needed for the exact classification.

## 7. Research interpretation

The native equal-coordinate bouquet does not merely arrange prime outputs. It induces a second distribution on possible prime divisors:

`q -> how many C3 lanes can q see?`

The answer is a rigid four-color activation spectrum controlled by q modulo 120.

Classical quadratic-residue theory explains the character calculation. The Enterprise-specific research content is that the two discriminants and the resulting 0/1/2/3 lane-activation spectrum arise from the C3 midpoint bouquet selected by the native shell allocation.
