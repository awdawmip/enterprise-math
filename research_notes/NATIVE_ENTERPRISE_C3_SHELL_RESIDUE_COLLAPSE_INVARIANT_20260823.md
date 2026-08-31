# Native Enterprise C3 shell-residue collapse invariant

Status: `FREE_RESEARCH_EXACT_INVARIANT / NOT_CANONICAL_FOUNDATION`

Date: `2026-08-23`

Researcher-ID: `EM-FREE-NEPS-239A6D`

Parent: `NATIVE_ENTERPRISE_C3_PROJECTIVE_PRIME_SIEVE_20260823.md`

## 1. Centered C3 fiber

For a folded shell fiber `(r,t)`, let

`c = B_r + t + r`,

where

`B_r = 3r(r-1)/2 + 1`.

The three pre-collapse labels are

`F(r,t) = {c-r, c, c+r}`.

The gap between adjacent members is exactly the native shell index `r`.

## 2. Shell-residue collapse

Define the shell-residue collapse

`SRC_r(F) = rho = c mod r in Z/rZ`.

Because the three members differ by multiples of `r`,

`c-r == c == c+r == rho (mod r)`.

Thus `SRC_r` is a genuine three-to-one arithmetic recoalescence attached to the native shell gap. It is defined without first choosing any prime modulus.

For the fixed monotone tri-sector allocation, `t -> rho` is a bijection on every shell.

Explicitly:

- if `r` is odd, `rho = t+1 mod r`;
- if `r=2m` is even, `rho = t+m+1 mod r`.

Hence every residue class in `Z/rZ` occurs exactly once among the `r` folded fibers of shell `r`.

Freeze:

`C3_FOLDED_SHELL <-> Z/rZ` as a shell-residue inventory.

This is an inventory statement for the fixed allocation; arbitrary common within-sector permutations can change which geometric side address carries a particular residue, but they do not change the unordered numeric fiber collection or the residue attached to a given numeric fiber.

## 3. Integral collapse defect

Define

`D(r,t) = gcd(c,r) = gcd(rho,r)`.

Since

`gcd(c-r,r) = gcd(c,r) = gcd(c+r,r)`,

`D` is the common shell-divisor content of the entire C3 fiber.

For every prime `q|r`:

- `q|D` iff all three fiber labels are divisible by `q`;
- `q does not divide D` iff the three labels recoalesce modulo `q` to one nonzero class and are all safe from `q`.

Therefore the earlier family of separate resonant projective-q outcomes factors through one integral invariant:

`D(r,t)`.

In particular, the projective readout `[c:r] mod q` is undefined/killed exactly when `q|D`; otherwise, if `q|r`, it is the safe point at infinity.

## 4. Primitive shell fibers and the totient theorem

Call a folded fiber shell-primitive when

`D(r,t)=1`.

Because `t -> rho` is a bijection, the shell-primitive fibers are exactly the unit residues

`rho in (Z/rZ)^*`.

Hence the number of shell-primitive C3 fibers is exactly

`phi(r)`.

Freeze exact theorem:

`# {t: D(r,t)=1} = phi(r)`.

No primality assumption is involved.

## 5. Prime-fiber consequence

If all three labels `c-r,c,c+r` are distinct primes, then necessarily

`D(r,t)=1`.

Indeed, if `D>1`, every member of the fiber is divisible by the same divisor `D`, so three distinct positive labels cannot all be prime.

Therefore

`FULL_BRIGHT_C3_FIBERS subset of UNIT_FIBERS U(r)`.

Equivalently, the full-bright count satisfies

`T(r) <= phi(r)`.

This refines the earlier shell count by introducing the canonical normalized occupancy

`Theta(r)=T(r)/phi(r)`

on the primitive shell-residue basin.

## 6. Relation to projective uniformization

For a prime `q|r`, reducing `SRC_r` further along

`Z/rZ -> Z/qZ`

recovers the resonant local readout.

Thus all shell-prime projective-infinity recoalescences are quotient shadows of one shell-native integral collapse:

`C3 fiber -> rho in Z/rZ -> rho mod q`.

This is stronger as a native organizational object than introducing one `P^1(F_q)` readout independently for every prime q.

## 7. Exact finite checks

Direct enumeration verifies through `r<=5000`:

- `t -> rho` is bijective for every shell;
- `D(r,t)=gcd(rho,r)`;
- the number of `D=1` fibers is exactly `phi(r)`;
- every one of the 3919 fully-prime C3 fibers in the census is shell-primitive.

## 8. Boundary

Residue rings, gcd, units and Euler's totient are classical mathematics. No novelty claim is made for those objects.

The research-specific content is the derivation chain

`native tri-sector shell`

`-> C3 AP fiber with gap r`

`-> integral shell-residue recoalescence Z/rZ`

`-> one gcd defect encoding every resonant shell divisor`

`-> unit-group support constraint for full prime fibers`.

Current verdict:

`SHELL_RESIDUE_COLLAPSE = STRONG_NATIVE_INVARIANT_CANDIDATE`.
