# Blind packet — native tri-sector maximal-flower filament

Status: `FROZEN_BLIND_REPLICATION_INPUT`

Date: `2026-08-23`

Packet-ID: `PRIME_NATIVE_FILAMENT_BLIND_REPLICATION_PACKET_20260823`

## 1. Evidence firewall

Before freezing the independent return, use only this packet, elementary number theory, exact integer computation written by the receiving researcher, and the repository-wide primitive definitions expressly named here.

Do not read or search for any source note, source script, free-research conversation, journal entry, theorem package, branch diff, witness list, residue table, or later comparison concerning native prime flowers or filaments.

The packet deliberately does not disclose the source run's claimed sharp bound, extremal residue channel, or explicit witness.

## 2. Frozen carrier and integer allocation

Use coordinates

`(r,t,sigma)` with `r>=4`, `sigma in {0,1,2}`, and an interior side coordinate `2<=t<=r-2`.

Define

`B_r = 1 + 3*r*(r-1)/2`,

`N(r,t,sigma) = B_r + t + sigma*r`.

Primality is evaluated only after this allocation is fixed. Coordinate choice may not depend on primality.

For a center label `n=N(r,t,sigma)`, the six ordered nearest-neighbor labels are

`n + 3*r + sigma`,

`n + 6*r + 4 + 2*sigma`,

`n + 3*r + 1 + sigma`,

`n - 3*r + 3 - sigma`,

`n - 6*r + 8 - 2*sigma`,

`n - 3*r + 2 - sigma`.

Only events for which all relevant labels are positive are admissible.

## 3. Maximal prime flower

A center is a `maximal prime flower` when

1. the center label is prime and greater than `3`;
2. exactly four of its six ordered nearest-neighbor labels are prime;
3. the five prime labels are treated as a set, with the center distinguished before any sorting.

The researcher must independently determine whether condition 2 forces additional adjacency or slot restrictions. Nothing about the center slot, parity class, prime gap word, or residue channel is supplied.

## 4. Rolling overlap filament

Let `F_j` be maximal prime flowers whose centers lie on consecutive shells `r_j=r_0+j`.

A sequence `F_0,...,F_{L-1}` is a `rolling overlap filament of length L` when every consecutive pair

- has adjacent centers in the frozen nearest-neighbor graph; and
- has prime-label sets with intersection cardinality exactly four.

The definition is representation-first: do not assume in advance that there is a conserved transverse coordinate or a preferred sector slot. Those facts, if true, must be derived.

The filament uses the union of all prime labels appearing in its flowers. Small-prime exceptional cases must be separated explicitly from the nonexceptional regime.

## 5. Exact research questions

Independently determine:

1. whether a center prime can ever have five or six prime nearest neighbors;
2. the complete coordinate and residue classification of maximal prime flowers;
3. the exact transition law for two consecutively overlapping maximal flowers;
4. whether every rolling filament carries a conserved integer or residue coordinate;
5. whether rolling filament length is globally bounded in the nonexceptional regime;
6. if bounded, the exact sharp bound and a fully verified witness attaining it;
7. if unboundedness cannot be decided, the strongest proved upper/lower bounds and the exact obstruction to closure.

A finite search without a global modular or structural argument does not settle item 5.

## 6. Mandatory counterexample pressure

At minimum test:

- all three sector slots;
- both shell parities;
- global reversal of the within-sector side coordinate;
- cyclic relabeling of the three sectors;
- all primes `2,3,5` as possible exceptional divisors;
- boundary versus interior cells;
- chains that share four prime values but fail center adjacency, and chains with adjacent centers but the wrong overlap cardinality.

Do not silently identify presentation-equivariant statements with presentation-invariant statements.

## 7. Executable evidence requirements

The independent checker must:

- generate the carrier and neighbors directly from the formulas in this packet;
- use exact deterministic primality for every certified witness;
- enumerate all local residue states needed by the proof;
- verify every value in any extremal witness independently of a bulk sieve;
- expose its search bounds, seeds, and expected frozen digest;
- include negative controls in which one neighbor formula or one shell-transition rule is intentionally perturbed and the claimed invariant fails.

## 8. Source-comparison boundary

After the independent return has been committed and frozen, the Driver may compare it with the withheld source branch. The receiving researcher must stop before that comparison.
