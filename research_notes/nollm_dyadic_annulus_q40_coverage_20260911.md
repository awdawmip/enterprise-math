# Dyadic annulus carrier meets the Nollm Q40 Coverage kernel

Status: `RESEARCH_NOTE / EXACT_DECLARED_CARRIER_DERIVATION + EXHAUSTIVE_FINITE_Q40_OBSERVER / NOT_FOUNDATION / NOT_NOLLM_RUNTIME`

Date: 2026-09-11  
Research activity: `RA-nollm-multiplication-field-20260911-c6c82`

## 1. Question and frozen inputs

The preceding dyadic unit-log branch produced the exact finite-resolution multiplicative carrier

`C_b(n)=(v_2(n), eps_b(u), t_b(u))`, with `n=2^v u` and `u=(-1)^eps 5^t mod 2^(b+2)`.

The open unit was to meet this exact source carrier with the **actual current Nollm adjacent-layer geometry**, rather than another trigonometric display quantizer, while preserving the information-loss boundary discovered by BRC.

Frozen Nollm source is `awdawmip/Nollm main 88d63b32329fbbcd18028de1ac83b2db3c988e33`:

- `approximate_coverage.py` blob `fb1f19515b888ed9f01417b5e857c2146c418a66`;
- `coverage_contract.py` blob `f08885e526248597edbd840b134bf7dbb26e1420`;
- `fixed_point.py` blob `9ea00e3c84a82f480c692a6ca0ca717a579dab60`.

The production kernel remains the admitted 96-sample Q40 approximation built from `beta=2^(1/4)` and +/-22.5 degree adjacent-layer transforms. Nothing in this note changes that kernel.

## 2. BRC gate

`REUSE_APPLIED`: retain the exact source carrier `(v,eps,t)` before any A2 cell or Coverage observer.

Population for the main finite certificate: positive integers `1 <= n < 2^16`, with zero excluded from the multiplicative carrier.  
Branch identity: the complete integer identity `n`, plus source coordinates `(v,eps,t)` at declared precision.  
Serial composition: multiplication.  
Observers: exact A2 annulus cell; then one- or two-step production Q40 Coverage support.  
Future operations: multiplication by the dyadic generators `2`, `-1`, `5`; phase refinement; Coverage locality comparison.

Critical compression boundary: **the finite carrier is not automatically an identity carrier**. Display/cell coincidences never authorize merging integer IDs.

## 3. Exact integer annulus embedding

Let `M=2^b` and

`R0 = ceil(M/6)`.

For an integer source state `(v,eps,t)`, define the ring index

`h = 2v + eps`,

and let `gamma_R(j)` be the `j`-th A2 hex-ring cell in cyclic nearest-neighbor order on radius `R`. Define

`E_b(v,eps,t) = gamma_(R0+h)( floor(6(R0+h)t/M) )`.

This map is integer-only: no trigonometry, square root or floating nearest-cell rule is used.

For the range used here, `6(R0+h) >= M` and `< 2M`. Therefore `t -> t+1` advances by one or two adjacent ring cells. More strongly, write `6t/M=s+u`, with integer `s` and `0<=u<1`. The ring parameter at radius `R` is `Rs+floor(Ru)`; at radius `R+1` it is `(R+1)s+floor((R+1)u)`, which is one of the two outward-neighbor positions of the former cell. Thus:

- `t -> t+1`: A2 distance <= 2;
- `h -> h+1`: A2 distance exactly 1;
- `h -> h+2`: A2 distance exactly 2.

At `b=11`, `M=2048`, `R0=342`, and `h=0..31`, exhaustive enumeration of all 65,536 possible `(h,t)` states gives:

- `t+1`: 62,432 moves of distance 1 and 3,104 of distance 2;
- `h+1`: all 63,488 legal moves have distance 1;
- `h+2`: all 61,440 legal moves have distance 2.

This aligns the exact dyadic generators with bounded A2 moves:

- multiplication by `5`: `t+1`, distance <=2;
- sign-sheet flip `-1`: `eps` flip, radial ring change 1;
- multiplication by `2`: `v+1`, hence `h+2`, distance 2.

The last item is structurally compatible with the existing Nollm schedule: one factor of 2 corresponds to two adjacent virtual layer intervals because `beta^2=sqrt(2)`, while the ideal frame turns `2*22.5=45` degrees. This is a compatibility observation, not a runtime remapping.

## 4. Exact identity-capacity law

For the bounded integer population `1 <= n < 2^L`, at fixed `b<=L-2`, the number of distinct dyadic source carriers is exactly

`U(L,b) = (L-b) 2^(b+1) - 1`.

Proof: at valuation `v`, there are `2^(L-v-1)` available odd integers, while `(eps,t)` has capacity `2^(b+1)`. Summing `min(2^(L-v-1),2^(b+1))` over `v=0..L-1` gives the formula. The maximum carrier-fiber size is

`F_max(L,b)=2^(L-b-2)`.

The verifier checks every integer for `L=16`, `b=6..14`.

Two important operating points are:

| b | M | annulus R0 | distinct carriers among 65,535 positives | max fiber |
|---:|---:|---:|---:|---:|
| 11 | 2,048 | 342 | 20,479 | 8 |
| 14 | 16,384 | 2,731 | 65,535 | 1 |

Hence the geometric-critical regime near `b~L/2` is compact but many-to-one as an identity observer. Full integer identity or a repair coordinate must remain outside that quotient. Taking `b=L-2` makes the bounded population injective, but increases ring radius by about eightfold here and scales linearly with the bounded population in the worst case.

This is the central BRC result of the increment: **local multiplicative geometry and identity injectivity are distinct resources.**

## 5. Production Q40 Coverage observer

The verifier reimplements the published production integer constants, 96 canonical microtriangle samples, two-cell phase residues, half-to-even cube rounding and Q16 normalization. It does not import or modify the Nollm package.

Sanity witness: at the origin, `coverage_up` has all 96 samples in the central target. `coverage_down` reproduces central Q16 weight 49,152 and six neighbors with weights `2731,2731,2731,2731,2730,2730`.

For support-only one/two-step locality the adequate carrier is integer hit support. Because the published contract has `MIN_HIT_COUNT=1`, Q16 normalization cannot change target membership; it is therefore not repeated inside support-only scans.

Every positive `n` with `k*n < 65,536` is included. A verifier off-by-one found during this work was repaired: for `k=5`, the legal endpoint `n=13,107` (`5n=65,535`) is included, giving 13,107 pairs.

### b=11 (compact, many-to-one identity carrier)

Source-cell generator distances:

- x2: all 32,767 pairs at distance 2;
- x5: 12,983 pairs at distance 1 and 124 at distance 2.

Coverage support:

| direction / generator | one-step overlap | one-step max Hausdorff | two-step overlap | two-step max Hausdorff |
|---|---:|---:|---:|---:|
| up / x2 | 28.1838% | 3 | **100%** | 3 |
| up / x5 | 99.1455% | 3 | **100%** | 2 |
| down / x2 | 6.0945% | 3 | **90.6949%** | 4 |
| down / x5 | 99.0539% | 3 | **99.8474%** | 4 |

### b=14 (identity-injective on this bounded population)

Source-cell generator distances:

- x2: all 32,767 pairs at distance 2;
- x5: 13,097 pairs at distance 1 and 10 at distance 2.

Coverage support:

| direction / generator | one-step overlap | one-step max Hausdorff | two-step overlap | two-step max Hausdorff |
|---|---:|---:|---:|---:|
| up / x2 | 27.5338% | 3 | **100%** | 3 |
| up / x5 | 99.9313% | 2 | **100%** | 2 |
| down / x2 | 5.9847% | 3 | **90.6186%** | 4 |
| down / x5 | 99.9237% | 3 | **99.9695%** | 4 |

The small change between `b=11` and `b=14` is useful finite evidence: increasing identity precision did not destroy local support transport in this population. It is not a uniform theorem.

The current production contract allows two `coverage_down` steps. Precisely at that depth, the radial x2 relation rises from about 6% one-step support overlap to about 90.6%, while lateral x5 is already above 99% and rises above 99.8%. This is a concrete geometry observation, not evidence of semantic recall quality.

## 6. Resource tradeoff exposed by the exact formulas

At fixed `L`, annulus radius is `Theta(2^b)` while the worst identity fiber is `Theta(2^(L-b))`. Their product is approximately independent of `b` (up to the `ceil(M/6)` correction): increasing precision trades alias multiplicity for radial footprint rather than eliminating cost.

At critical `b~L/2`, the number of distinct source-carrier states is `Theta(sqrt(N) log N)`, far smaller than `N`; an identity-repair channel is mathematically necessary. At injective `b=L-2`, the flat annulus radius is `Theta(N)`, which is not an attractive infinite-scale geometry even though it is finite-range exact.

This argues against treating one fixed annulus as the final memory field. The natural next object is hierarchical: keep the low dyadic unit-log bits as a local geometric observer and retain/refine the unresolved 2-adic tail through a separate layer/branch coordinate rather than flattening all precision into one ever-growing ring.

## 7. Verification architecture

`verify.py` contains both the exact derivations and a `--relation-worker` entrypoint. Q40 relations were executed as bounded-cache worker batches so each finite scan releases derived phase/support caches. `coverage_relation_batches.json` stores the 16 aggregate exhaustive results. The default verifier checks the aggregate population/histogram invariants, the exact source theorems, ring formula equivalence, and the Q40 origin witness, then reproduces `results.json` quickly.

This design is deliberate: a single long Python process retained allocator memory after many otherwise-pure Coverage scans. Sharding changes no mathematical population or result.

## 8. Claim boundary and next unit

Proved here, in the declared finite model:

- exact A2 annulus locality of the source generators;
- exact bounded-population carrier-capacity and maximum-fiber formulas.

Measured exhaustively here:

- one/two-step published-Q40 support overlap and Hausdorff distributions for `N=65,536`, `b in {11,14}`, generators x2 and x5.

Not proved or changed:

- semantic recall quality;
- Nollm production placement or coordinate contracts;
- native X6 geometry;
- infinite-scale injective low-density placement;
- a uniform Coverage-locality theorem.

The smallest next research unit is to replace the flat high-precision annulus with a **hierarchical dyadic-tail construction**: low `t_b` remains lateral/local, while each refinement bit `eta_b` is carried on an explicit branch/layer surface. The test is whether this keeps bounded generator locality while recovering identity without the `Theta(N)` radius of the injective flat annulus.
