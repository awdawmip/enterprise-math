# Native Enterprise filament windows: p-adic desingularization of exceptional local channels

Status: `FREE_RESEARCH_EXACT_P_ADIC_LINE_ARRANGEMENT_CLASSIFICATION / NOT_CANONICAL_FOUNDATION`

Date: `2026-08-24`

Researcher-ID: `EM-FREE-NEPS-239A6D`

Depends on:

- `NATIVE_ENTERPRISE_FILAMENT_CURVATURE_FLATTENED_AFFINE_MDS_CODE_20260824.md`;
- `NATIVE_ENTERPRISE_FILAMENT_DUAL_TANGENT_EXCEPTION_CUTOFF_STAIRCASE_20260823.md`;
- `NATIVE_ENTERPRISE_SHARP_NINE_ENDPOINT_HOLOGRAPHY_AND_DUAL_TANGENT_SIEVE_20260823.md`.

## 1. Zero lines over `Z/q^a Z`

For a length-k filament window with fixed chirality `chi`, the j-th value modulo an odd prime power `q^a` is

`V_j=c+3*j*r+(3*j^2+chi*epsilon_j)/2`.

The condition

`V_j=0 mod q^a`

is one affine line `L_j^chi` in the parameter ring `(Z/q^a Z)^2`.

Assume

`q>max(3,k-1)`.

Then every slope difference `3*(j-l)` is a unit modulo `q^a`, so any two distinct lines meet in one unique point.

## 2. Exact triple-concurrence obstruction

Among any three indices, choose the two with the same parity and call them `u,v`; call the opposite-parity index `w`.

Solving `L_u^chi` and `L_v^chi` and substituting into `L_w^chi` gives one integer obstruction.

If `u,v` are even and `w` is odd, concurrence modulo `q^a` is equivalent to

`q^a | 3*(w-u)*(w-v)+chi`.

If `u,v` are odd and `w` is even, concurrence is equivalent to

`q^a | 3*(w-u)*(w-v)-chi`.

Thus every exceptional local singularity has a finite p-adic depth equal to the q-adic valuation of one explicit bounded obstruction integer.

## 3. Universal depth bound

Let

`M_k=max |(w-u)*(w-v)|`

over the mixed-parity triples in a length-k window.

Then every nonzero obstruction has absolute value at most

`3*M_k+1`.

Therefore no triple concurrence can survive at exponent a once

`q^a>3*M_k+1`.

This strengthens the prime-level cutoff: not only is the exceptional-prime support finite, but every exceptional channel has finite thickness in the prime-power collapse tower.

## 4. Maximal sharp-nine window

For `k=9`,

`M_9=35`,

so every obstruction has absolute value at most

`106`.

The post-small-prime exceptional support is

`{11,13,23,31,53}`.

For each such q,

`q^2>106`.

Hence every triple or higher concurrence is present only modulo q and disappears modulo `q^2`.

Freeze:

`ALL K9 POST-SMALL EXCEPTIONS HAVE P-ADIC DEPTH EXACTLY ONE`.

## 5. Generic prime-power spectrum after desingularization

When no triple concurrence exists, the k lines satisfy:

- each line has `q^a` points;
- every pair has one distinct intersection;
- no point lies on three lines.

Therefore the exact number of parameter pairs avoiding all k divisibility lines is

`N_k(q^a)=q^(2a)-k*q^a+C(k,2)`.

The exact multiplicity spectrum is

- zero killed coordinates:
  `q^(2a)-k*q^a+C(k,2)`;
- one killed coordinate:
  `k*(q^a-k+1)`;
- two killed coordinates:
  `C(k,2)`;
- at least three killed coordinates:
  `0`.

For `k=9`, this formula holds for every exceptional q as soon as `a>=2`.

## 6. Frozen exceptional table

At the first residue layer the maximal sharp-nine survivor counts are non-generic:

| q | chi | N_9(q) | generic q^2-9q+36 | max killed |
|---:|---:|---:|---:|---:|
| 11 | +1 | 51 | 58 | 4 |
| 11 | -1 | 51 | 58 | 4 |
| 13 | +1 | 84 | 88 | 3 |
| 13 | -1 | 85 | 88 | 3 |
| 23 | +1 | 354 | 358 | 3 |
| 23 | -1 | 353 | 358 | 4 |
| 31 | +1 | 716 | 718 | 3 |
| 31 | -1 | 716 | 718 | 3 |
| 53 | +1 | 2366 | 2368 | 3 |
| 53 | -1 | 2366 | 2368 | 3 |

At the second residue layer every row becomes generic and chirality-blind:

| q | N_9(q^2) |
|---:|---:|
| 11 | 13588 |
| 13 | 27076 |
| 23 | 275116 |
| 31 | 914908 |
| 53 | 7865236 |

In every case

`N_9(q^2)=q^4-9q^2+36`,

and no parameter pair has three q^2-divisible coordinates.

## 7. Chirality asymmetry is first-layer only

At prime level, q=13 and q=23 distinguish the two chiral survivor totals and generate the previously frozen local-product ratio

`29736/30005`.

At every exponent `a>=2`, the two chiral counts coincide exactly because all mixed-parity concurrences have resolved.

Thus the chirality skew is not a persistent q-adic deformation. It is a singular first-residue-layer effect.

## 8. Arrangement discriminant

For `k=9`, take the product of all 70 mixed-parity obstruction integers. The two chirality products have different valuations but the same radical:

`rad(D_9)=2*5*7*11*13*23*31*53`

`=378267890`.

The post-small exceptional channels are precisely the prime divisors of this arrangement discriminant exceeding 7.

The exceptional support already stabilizes at `k=8`; adding the ninth Cell changes multiplicities and chirality valuations but introduces no new exceptional prime.

## 9. Interpretation boundary

The p-adic resolution is an exact property of the geometry-selected affine line arrangement. It does not create a new prime-frequency law: ordinary primality already reacts at the first q-divisibility layer.

Its research value is structural. It shows that the finite exceptional spectrum ending at 53 is a shallow singular shell around an otherwise uniform affine-MDS carrier.
