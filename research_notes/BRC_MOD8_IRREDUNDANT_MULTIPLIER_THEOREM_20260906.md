# BRC odd-N mod-8 irredundant multiplier reduction

Status: `PROVED ELEMENTARY REDUCTION / EXECUTABLE SCAN IMPROVEMENT / NOVELTY UNVERIFIED`
Date: `2026-09-06`
Parent: `t0.brc_multiplier_priority_jump`

## Question

The current prioritized odd-N multiplier scan safely removes `m == 2 (mod 4)`, leaving 75 candidates in `1..100`. Can the feasible class `m == 4 (mod 8)` also be removed without losing any factor witness?

**Yes.** It is feasible as a difference of squares, but every immediate ceiling witness is redundant with the smaller multiplier `m/4`.

## Theorem

Let `N` be odd and let

`m = 4*l`, with `l` odd.

Assume the immediate ceiling-square test succeeds at m:

`x = ceil(sqrt(mN))`,
`y^2 = x^2-mN`.

Then there are integers `X,Y` with

`x=2X`, `y=2Y`,

such that

`lN = X^2-Y^2`,

and moreover

`X = ceil(sqrt(lN))`.

Therefore the same immediate ceiling-square witness already exists at the smaller multiplier `l=m/4`. Since N is odd,

`gcd(x-y,N) = gcd(2(X-Y),N) = gcd(X-Y,N)`.

So the reduced multiplier exposes the same gcd factor.

## Proof

Because `mN == 4 (mod 8)`, the successful difference

`x^2-y^2 == 4 (mod 8)`.

Squares modulo 8 are `0,1,4`. A difference congruent to 4 cannot be the difference of two odd squares (that is 0 mod 8), so x and y must both be even. Write `x=2X`, `y=2Y`; division by 4 gives

`lN=X^2-Y^2`.

Now set `z=lN`. Since

`2X = ceil(2*sqrt(z))`,

the ceiling inequality gives

`2X-1 < 2*sqrt(z) <= 2X`.

Dividing by 2,

`X-1/2 < sqrt(z) <= X`,

hence `ceil(sqrt(z))=X`.

Finally N is odd, so multiplication by 2 is invertible for the purpose of gcd with N:

`gcd(2(X-Y),N)=gcd(X-Y,N)`.

This proves exact scan redundancy.

## Consequence: exact representative residues

For odd N:

- `m == 2 or 6 (mod 8)` is impossible as a difference of two squares;
- `m == 4 (mod 8)` is possible but every successful immediate witness reduces to `m/4`;
- residues `0,1,3,5,7 (mod 8)` must remain as the scan-complete representative set.

Thus the exact irredundant residue set is

`{0,1,3,5,7} mod 8`.

For `m=1..100` this leaves 62 candidates, compared with 75 after the prior mod-4-only reduction and 100 in the raw scan.

So the raw scan reduction is

`100 -> 62`,

an exact 38% candidate deletion, with no factor-witness loss.

The incremental gain over the already-landed mod-4 rule is

`75 -> 62`,

13 additional redundant candidates removed.

## Bounded regression

An external research harness checked odd `N<20000` and every `m<=1000` with `m == 4 (mod 8)`. Among 66,224 actual nontrivial immediate factor witnesses at those larger multipliers, every witness reduced to `m/4` and returned the same proper gcd factor. No counterexample was observed.

Repository regression keeps a smaller deterministic version of the same implication, in addition to the existing direct-jump equivalence tests.

## Relation to prior work

MIT PRIMES work by Tejas Gopalakrishna and Yichi Zhang, *Analysis of the One Line Factoring Algorithm* (2020), reported the iterator set `{0,1,3,5,7} mod 8` as an OLF optimization and described the `4 mod 8` first-hit exclusion as a large experimentally tested conjectural observation.

Reference:
`https://math.mit.edu/research/highschool/primes/materials/2019/Gopalakrishna.pdf`

The elementary reduction above gives an exact proof inside the present immediate-ceiling / odd-N semantics. No claim of global novelty or priority is made; the result is recorded as an exact Enterprise derivation and executable simplification.

## Tool integration

`src/enterprise_math/brc_multiplier_priority_jump.py` now keeps the old distinction between:

- `odd_n_multiplier_is_difference_square_feasible(m)`: feasibility, still true for 4 mod 8;
- `odd_n_multiplier_is_scan_irredundant(m)`: exact scan representative test;
- `odd_n_multiplier_scan_representative(m)`: returns `None`, `m/4`, or `m` according to the exact mod-8 reduction.

`prioritized_odd_multiplier_order` now uses the scan-irredundant set. The same-parity factor-pair ordering within that exact set remains heuristic.

## Boundary

This result reduces redundant candidates but does not alter the Hart/Lehman `N^(1/3)` multiplier-scale boundary established in the parent research line. It is a constant-factor exact simplification, not an asymptotic factorization speedup.
