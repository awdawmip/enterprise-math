# Native Enterprise C3 secondary unit-basin spectrum after the 210 shell gate

Status: `FREE_RESEARCH_EXACT_LOCAL_CLASSIFICATION / FINITE_RATE_EXPERIMENT / NOT_CANONICAL_FOUNDATION`

Date: `2026-08-23`

Researcher-ID: `EM-FREE-NEPS-239A6D`

Parent: `NATIVE_ENTERPRISE_C3_IDENTITY_FIBER_PARITY_SELECTION_20260823.md`

## 1. The 210 survivor basin is U(210)

Restrict to resonant shells

`r = 210 k`.

Every fully-prime C3 fiber must have shell residue

`rho in U(r)`.

In particular its reduction modulo 210 lies in

`U(210)`,

which has exactly 48 classes.

Thus after the saturated `2*3*5*7` shell gate, the next folded state space is naturally a 48-class unit basin rather than a single midpoint line.

## 2. Fixed unit-residue lanes

Fix `u in U(210)`. For `k>=2`, the shell is large enough that the unique folded fiber with

`rho == u (mod r)`

lies on the stable centered branch with

`c = 3r^2/2 + u`.

Its three labels are

`P_-^u(r)=3r^2/2-r+u`,

`P_0^u(r)=3r^2/2+u`,

`P_+^u(r)=3r^2/2+r+u`.

With `r=210k`:

`P_-^u(k)=66150 k^2 - 210 k + u`,

`P_0^u(k)=66150 k^2 + u`,

`P_+^u(k)=66150 k^2 + 210 k + u`.

The canonical midpoint bouquet from the previous stage is exactly the unit identity class `u=1`.

## 3. Exact local activation spectrum for q>7

Let `q>7` be prime. Since `210` is invertible modulo q, root counting in k is equivalent to root counting in the shell variable r.

After multiplying the three equations by 2, the quadratic discriminants are:

- each outer lane: `4(1-6u)`;
- middle lane: `-24u = 4(-6u)`.

If `q does not divide u`, the three root sets are pairwise disjoint, and the exact union count is

`omega_u(q) = 3 + 2 Legendre((1-6u)/q) + Legendre((-6u)/q)`.

Hence

`omega_u(q) in {0,2,4,6}`.

The four states correspond to the two quadratic-character bits

`( Legendre((1-6u)/q), Legendre((-6u)/q) )`.

If `q|u`, the three root sets meet at `r=0`; direct factorization gives the exact union

`omega_u(q)=3`.

Thus every shell unit class carries a prime-indexed activation word over

`{0,2,3,4,6}`,

with the value 3 occurring only when q divides u.

For `u=1`, the formula reduces to the earlier equal-coordinate root profile and its four-color `q mod 120` specialization.

## 4. Finite local-factor diagnostic

For `Q>=11`, define

`S_u(Q) = product_{11<=q<=Q, q prime} (1-omega_u(q)/q)/(1-1/q)^3`.

This is a finite classical local-sieve diagnostic for the three quadratic lanes. It is not a proof of an asymptotic prime-tuple law.

At `Q=5000`, the highest scores among the 48 unit classes are:

1. `u=131`: `S≈2.7980403560`;
2. `u=103`: `S≈2.0331256695`;
3. `u=101`: `S≈1.8969302812`;
4. `u=1`: `S≈1.7488757701`;
5. `u=79`: `S≈1.6451535269`.

The top ordering `131,103,101,1,79,169` is already stable from `Q=500` through at least `Q=20000` in the finite diagnostic.

## 5. Deep finite prime scan

Exact 64-bit primality scanning was run for

`k = 2,...,50000`

on all 48 fixed unit classes.

The largest simultaneous-prime counts are:

- `u=131`: 395;
- `u=103`: 309;
- `u=101`: 271;
- `u=1`: 258;
- `u=169`: 233;
- `u=173`: 231;
- `u=89`: 230;
- `u=79`: 224;
- `u=41`: 223;
- `u=53`: 212.

The mean over all 48 classes is about `148.17`.

The Pearson correlation between

`log S_u(5000)`

and the 48 observed simultaneous-prime counts is approximately

`0.95694`.

Therefore most of the very large between-class rate variation is explained by ordinary higher-prime local obstruction profiles.

## 6. Important falsification / selection result

If the rule were simply

`choose the unit residue with the most observed primes`,

the finite winner would be `u=131`, not the canonical midpoint `u=1`.

But `u=131` has no currently known native geometric selection principle; its advantage is almost completely predicted by its classical local sieve spectrum.

By contrast, `u=1` is selected before primality by:

- multiplicative identity in the shell residue ring;
- parity-driven axis-to-midpoint switch;
- equal-coordinate geometry on even shells;
- exact recoalescence to `1 mod r`;
- minimum-complexity maximal 105/210 gate from the earlier ray classification.

Hence the research should not replace the midpoint by a numerically richer but geometrically arbitrary unit class.

Freeze distinction:

`ARITHMETICALLY PRIME-RICH != NATIVE-CANONICAL`.

The identity class is rank 4/48 in the deep finite scan, so native canonicality does not require sacrificing all arithmetic enrichment, but enrichment is not the selection axiom.

## 7. New basin picture

The current native distribution hierarchy is now:

`raw shell fibers`

`-> shell-residue ring Z/rZ`

`-> primitive/unit basin U(r)`

`-> on 210-resonant shells: 48 classes U(210)`

`-> each class carries a higher-prime quadratic-character activation spectrum`.

This is a cleaner prime-distribution object than a visually selected ray.

## 8. Boundary

The quadratic-character and local-factor machinery is classical. No novelty claim is made for it.

The Enterprise-specific research object is the derivation of the 48-class secondary basin from the native shell-residue collapse, together with the separation between native canonicality and arithmetic local enrichment.

Current verdict:

`SHELL_UNIT_BASIN = SURVIVES AS NATIVE STRUCTURE`.

`RAW PRIME-RATE MAXIMIZATION = REJECTED AS CANONICAL SELECTION RULE`.
