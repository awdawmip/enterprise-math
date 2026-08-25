# Odd-sector central fiber saturation-gate theorem

Status: `FREE_RESEARCH_EXACT_ODD_SECTOR_SIEVE_GEOMETRY / NOT_CANONICAL_ENTERPRISE_GEOMETRY`

Date: `2026-08-25`

Researcher-ID: `EM-FREE-NEPS-239A6D`

Depends on:
`NATIVE_ENTERPRISE_C3_BOUQUET_AS_UNFOLDED_CENTRAL_FILAMENT_20260825.md`.

Only `s=3` is native Enterprise geometry. General odd `s` is the controlled shell-allocation family.

## 1. The s-slot even-shell packet

Let `s` be positive odd and put

`h=(s-1)/2`.

On even shell

`r=2m`,

the central filament value is

`c_s(m)=1+2s*m^2`.

Unfolding across the `s` sector slots gives the packet

`P_(s,j)(m)=2s*m^2+2j*m+1`,

for

`j=-h,-h+1,...,h`.

This is an s-term arithmetic progression in the slot variable `j`, with common difference `2m`.

For `s=3`, these are exactly

`6m^2-2m+1`,

`6m^2+1`,

`6m^2+2m+1`.

## 2. Automatic saturation for every odd prime q<=s

Fix an odd prime `q<=s` and a nonzero residue

`m mod q`.

The divisibility equation

`P_(s,j)(m)=0 mod q`

is linear in `j`:

`2jm = -1-2s*m^2 mod q`.

Because `2m` is invertible modulo `q`, there is exactly one residue class

`j mod q`

solving it.

The allowed lane indices form `s` consecutive integers. Since `s>=q`, they contain at least one representative of every residue modulo `q`.

Therefore for every nonzero `m mod q`, at least one lane is divisible by `q`.

At `m=0`, every lane equals `1 mod q`.

Hence:

`ALL s LANES AVOID q-DIVISIBILITY`

iff

`m=0 mod q`.

Freeze:

`EVERY ODD PRIME q<=s IS A MANDATORY CENTRAL-FIBER GATE`.

## 3. Primorial core

Let

`G_core(s)=product_{q<=s, q odd prime} q`.

Then any parameter `m` whose entire central-fiber packet avoids divisibility by every odd prime at most `s` satisfies

`G_core(s)|m`.

For a simultaneous-prime packet whose entries are all larger than these small primes, the same divisibility is necessary.

Thus sector count alone produces a growing odd-primorial gate before any quadratic-character analysis is used.

## 4. Large-prime root profile

Now let `q` be an odd prime with

`q>s`.

Then the lane indices `j=-h,...,h` are distinct modulo `q`.

If two distinct lanes shared a nonzero root `m`, subtracting their equations would give

`2m(j-k)=0 mod q`,

impossible.

So all lane root sets are disjoint.

The discriminant of lane `j` as a quadratic in `m` is

`Delta_j=4(j^2-2s)`.

For `q` not dividing `2s`, the number of roots in that lane is

`1+Legendre(j^2-2s,q)`.

Therefore the total number of distinct bad nonzero residues is

`omega_s(q)`

`=s + sum_(j=-h)^h Legendre(j^2-2s,q)`.

This generalizes the frozen C3 root profile exactly.

For `s=3`, the discriminants are

- outer lanes: `4(1-6)=-20`;
- center lane: `4(0-6)=-24`;

and therefore

`omega_3(q)=3+2 Legendre(-20,q)+Legendre(-24,q)`.

## 5. Universal root-slot bound

Each of the `s` quadratic lanes has at most two roots.

Hence for `q>s`, complete nonzero-residue saturation requires

`q-1<=2s`.

Therefore

`q<=2s+1`.

Freeze:

`NO ADDITIONAL MANDATORY SATURATION PRIME CAN EXCEED 2s+1`.

Thus the saturation problem splits exactly into two ranges:

1. `q<=s`: automatic saturation from lane-index coverage;
2. `s<q<=2s+1`: finite Legendre-profile test;
3. `q>2s+1`: saturation impossible.

## 6. Complete finite gate set

Define

`S_s={odd primes q<=s}`

union

`{primes q with s<q<=2s+1 and omega_s(q)=q-1}`.

Then the complete modular gate for the central s-slot packet is

`G_s=product_(q in S_s) q`.

Outside the finite tiny cases where a q-divisible packet entry is itself equal to q, simultaneous primality of all s lanes requires

`G_s | m`.

## 7. First examples

Direct exact enumeration gives:

- `s=1`: saturated primes `{3}`, gate `3`;
- `s=3`: `{3,5,7}`, gate `105`;
- `s=5`: `{3,5,7}`, gate `105`;
- `s=7`: `{3,5,7}`, gate `105`;
- `s=9`: `{3,5,7,11,13}`, gate `15015`;
- `s=11`: `{3,5,7,11}`, gate `1155`;
- `s=13`: `{3,5,7,11,13}`, gate `15015`.

These examples show that the primorial core is universal, while the interval `(s,2s+1]` contributes genuinely arithmetic extra gates.

## 8. Native s=3 interpretation

For `s=3`, the automatic core gives only prime `3`.

The Legendre-profile interval is

`3<q<=7`,

and both candidate primes `5` and `7` saturate.

Thus

`G_3=3*5*7=105`.

So the native `105` gate decomposes canonically into

`sector-count automatic core 3`

plus

`two extra quadratic saturation channels 5 and7`.

## 9. Relation to longitudinal breaker geometry

The same central carrier has a distinct longitudinal readout.

For `s=B=3`, channel `5` is the first universal longitudinal breaker, whereas channel `7` is not a breaker.

Transversely, both `5` and `7` saturate the entire nonzero `m` residue set of the three-slot C3 packet.

Thus the central carrier distinguishes two notions:

- `transverse lane saturation`;
- `longitudinal filament breaking`.

The native value `5` belongs to both mechanisms; `7` belongs only to the transverse saturation mechanism.

This is one reason the gate product is `3*5*7` even though the longitudinal breaker spectrum stops at `5`.

## 10. Prior-art boundary

Polynomial root counts, Legendre symbols and primorial divisibility are classical.

The research-specific candidate is the exact gate generated by the odd-sector central-fiber shell allocation and its coupling to the longitudinal breaker geometry.