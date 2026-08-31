# Native Enterprise sharp-nine prime island: endpoint holography and dual-tangent local sieve

Status: `FREE_RESEARCH_EXACT_VALUE_DYNAMICS + FINITE_LOCAL_SIEVE_CLASSIFICATION / NOT_CANONICAL_FOUNDATION`

Date: `2026-08-23`

Researcher-ID: `EM-FREE-NEPS-239A6D`

Parents:

- `NATIVE_ENTERPRISE_NINE_PRIME_FILAMENT_MULTISCALE_CURVATURE_20260823.md`;
- `NATIVE_ENTERPRISE_SHARP_NINE_MOD5_TANGENCY_CODE_20260823.md`;
- `NATIVE_ENTERPRISE_GLOBAL_TYPED_CELL_PRIME_INCIDENCE_ISLAND_SHARP_NINE_20260823.md`.

## 1. Universal typed filament potential

On the long sigma-1 typed filament with transverse coordinate

`h=t-ceil(r/2)`, the Cell label is

`C_r(h)=h + 3*r^2/2 + 1 + (1-(-1)^r)/4`.

Equivalently:

- even `r`: `C_r=h+3*r^2/2+1`;
- odd `r`: `C_r=h+3*(r^2+1)/2`.

This formula is prime-free. A sharp nine-prime island is one run

`p_j=C_{r+j}(h)`, `j=-4,...,4`,

whose nine values all happen to be prime.

Let

`chi=(-1)^r`.

Then identically

`p_j = p_0 + 3*r*j + 3*j^2/2 + (chi/2)*1_{j odd}`.

This unifies the previously frozen square-curvature ladder.

## 2. Curvature flattening

Define

`p_tilde_j = p_j - 3*j^2/2 - (chi/2)*1_{j odd}`.

Then

`p_tilde_j = p_0 + 3*r*j`.

Thus after removing the universal native curvature and one parity chirality bit, the nine prime values lie on one exact affine line.

Equivalent recurrence forms include

`p_{j+3}=p_{j+2}+p_{j+1}-p_j+6`,

and

`p_{j+4}-2*p_{j+2}+p_j=12`.

The adjacent second differences are

`p_{j+2}-2*p_{j+1}+p_j = 3-chi*(-1)^j`.

These statements are geometry-forced for every corresponding typed filament segment; primality supplies a sharp prime realization rather than the recurrence itself.

## 3. Endpoint holography of the sharp nine

For the two extreme values `p_-4,p_+4`:

`p_+4-p_-4 = 24*r`,

because the chirality correction vanishes at even scale 4.

Therefore the central native shell is recovered from the two endpoint prime values alone:

`r=(p_+4-p_-4)/24`.

Also the scale-4 curvature is 48, so

`p_0=(p_-4+p_+4-48)/2`.

Then

`h = p_0 - 3*r^2/2 - 1 - (1-(-1)^r)/4`.

Hence

`TWO ENDPOINT PRIME VALUES -> (r,h,chi) -> ALL NINE CELL VALUES`.

Explicitly, for `j=-4,...,4`:

`p_j = p_0 + 3*r*j + 3*j^2/2 + (chi/2)*1_{j odd}`.

The known even-chiral sharp island endpoints recover exactly

`(r,h)=(10690,-2474)`,

and the known odd-chiral packet endpoints recover

`(r,h)=(107815,7624)`.

Here `r` is the central Cell shell, four steps after the run start.

Thus the sharp nine is a two-boundary-value self-localizing code: seven interior prime values are forced once a valid endpoint pair is given.

## 4. Symmetric reconstruction laws

For every `j=1,...,4`:

`p_+j-p_-j = 6*r*j`,

and

`p_-j-2*p_0+p_+j = 3*j^2 + chi*1_{j odd}`.

Therefore

`p_±j = p_0 + (3*j^2 + chi*1_{j odd})/2 ± 3*r*j`.

The antisymmetric part carries shell scale; the symmetric part carries universal square curvature plus the single chirality bit.

## 5. Local prime obstruction as nine lines

Fix an odd prime `q` and a chirality `chi`. In the parameter plane `(r,c)` with `c=p_0`, the condition

`q | p_j`

is the affine line

`L_j^chi : c = -3*j*r - (3*j^2 + chi*1_{j odd})/2`.

For `q>7`, the nine slopes are distinct.

The lines have an exact dual-parabola interpretation:

- even `j` lines are the five tangents, at `r=-j`, to
  `c=(3/2)r^2`;
- odd `j` lines are the four tangents, at `r=-j`, to
  `c=(3/2)r^2-chi/2`.

Thus the sharp-nine local sieve is a sampled tangent arrangement of two vertically shifted parabolas.

## 6. Triple-concurrence criterion

For `q>7`, three lines of one parity cannot concur because they are distinct tangents to one nondegenerate parabola.

Mixed-parity concurrence is exact.

If `j,k` are even and `l` is odd, concurrence occurs iff

`3*(l-j)*(l-k) == -chi (mod q)`.

If `j,k` are odd and `l` is even, concurrence occurs iff

`3*(l-j)*(l-k) == chi (mod q)`.

Over the finite index window `-4,...,4`, the nonzero integer obstruction values have absolute values

`{2,4,8,10,14,16,20,22,26,28,44,46,62,64,104,106}`.

Therefore the only primes `q>7` at which any three of the nine lines can become concurrent are

`{11,13,23,31,53}`.

In particular, 53 is the final exceptional local prime channel.

## 7. Generic local survivor count

For every prime

`q>7`, `q not in {11,13,23,31,53}`,

all 36 pairwise line intersections are distinct and no triple concurrence occurs.

Hence the union of nine bad lines contains

`9q-36`

points of `F_q^2`, and the fully q-avoiding parameter count is exactly

`N_q^chi = q^2-9q+36`.

This value is independent of chirality.

## 8. Exceptional local table

For the five exceptional primes the exact survivor counts are:

| q | N_q^(chi=+1) | N_q^(chi=-1) |
|---:|---:|---:|
| 11 | 51 | 51 |
| 13 | 84 | 85 |
| 23 | 354 | 353 |
| 31 | 716 | 716 |
| 53 | 2366 | 2366 |

Only `q=13` and `q=23` distinguish the two chiralities at the level of total local survivor count.

Consequently, after the already-frozen small-prime channels, the ratio of the two Hardy-Littlewood-type local products is predicted entirely by these two channels:

`S_+/S_- = (84/85)*(354/353) = 29736/30005 ~= 0.9910348275`.

This is a local-model prediction, not an asymptotic theorem for actual sharp-nine island counts.

## 9. Boundary

Quadratic sequences, finite-field line arrangements, conic tangents, and local prime-tuple sieves are classical mathematics. No external novelty claim is made for those ingredients.

The research-specific exact chain is

`NATIVE TYPED INCIDENCE FILAMENT`

`-> SHARP NINE PRIME ISLAND`

`-> PARITY-CORRECTED QUADRATIC VALUE LAW`

`-> TWO-ENDPOINT SELF-LOCALIZATION`

`-> CURVATURE FLATTENING`

`-> NINE DUAL TANGENT LINES`

`-> FINITE EXCEPTIONAL LOCAL PRIME SPECTRUM ENDING AT 53`.

Current verdict:

`SHARP_NINE_VALUE_DYNAMICS = TWO-BOUNDARY HOLOGRAPHIC + DUAL-TANGENT LOCAL-SIEVE CLASSIFIED`.
