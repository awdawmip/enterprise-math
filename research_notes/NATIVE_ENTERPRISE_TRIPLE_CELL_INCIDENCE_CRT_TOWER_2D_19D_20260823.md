# Native Enterprise triple-cell incidence CRT tower: 2D through 19D

Status: `FREE_RESEARCH_HIGH_DIMENSIONAL_INCIDENCE_CANDIDATE / EXACT_CODE_TOWER + FINITE_CENSUS / NOT_CANONICAL_FOUNDATION`

Date: `2026-08-23`

Researcher-ID: `EM-FREE-NEPS-239A6D`

Parents:

- `NATIVE_ENTERPRISE_TRIPLE_CELL_DISCRETE_CURVATURE_CODE_20260823.md`;
- `NATIVE_ENTERPRISE_TRIPLE_CELL_MOD30_INCIDENCE_CODE_20260823.md`.

## 1. Base dimension is the native six-state incidence code

For primes greater than 3, the q=2 and q=3 channels together form the exact six-state mod-6 incidence hexacode

`H_6 = {A0,A1,A2,B0,B1,B2}`

with one nonconstant `+-1` residue word attached to each local triple-cell incidence type.

This is taken as collapse-channel dimension `d=2`, because the first two prime channels 2 and 3 are already fused into the primitive geometric six-state readout.

No Cartesian or orthogonal spatial axes are introduced.

## 2. One new incidence channel for every q>=5

For an odd prime q>=5, let

`K=4` on A incidences and `K=2` on B incidences.

Since K is invertible modulo q, normalize an incident triple `(x,y,z)` by

`(X,Y,Z)=K^{-1}(x,y,z) mod q`.

The exact curvature equation becomes the orientation-independent punctured plane

`H_q = {(X,Y,Z) in (F_q^*)^3 : X-2Y+Z=1}`.

Its exact size is

`|H_q| = q^2-3q+3`.

The absolute integer curvature K still retains A/B orientation; the normalized q-channel carries the residual local incidence state after orientation normalization.

## 3. Incidence collapse dimension d

Let `p_1=2,p_2=3,p_3=5,...` be the primes.

Define

`I_2 = H_6`.

For d>=3 define

`I_d = H_6 x product_{i=3}^d H_{p_i}`.

The exact state count is

`|I_d| = 6 * product_{i=3}^d (p_i^2-3p_i+3)`.

The d-th channel is therefore not a Euclidean coordinate. It is one additional finite-field incidence-curvature readout.

## 4. Canonical downward collapse

The map

`Pi_d : I_d -> I_{d-1}`

forgets only the newest `H_{p_d}` coordinate.

Every lower state has exactly

`p_d^2-3p_d+3`

formal incidence-code lifts.

Thus

`I_19 -> I_18 -> ... -> I_2`

is an exact inverse collapse tower.

CRT gives an equivalent combined-modulus description: a state in `I_d` is exactly an admissible ordered prime-residue triple modulo the primorial modulus `P_d`, together with the native incidence normalization implicit in the mod-6 base code.

## 5. Exact 2D-19D basin sizes

Selected rows:

- d=2, channel 3: `|I_2|=6`;
- d=3, add q=5 with factor 13: `|I_3|=78`;
- d=4, add q=7 with factor 31: `|I_4|=2418`;
- d=5, add q=11 with factor 91: `|I_5|=220038`;
- d=8, after q=19: `|I_8|=2165233550298`;
- d=12, after q=37: `|I_12|=833517763963414808445258`;
- d=19, after q=67: `|I_19|=618926425438401790806456406844216777632288040754`.

The complete table is frozen in the companion CSV.

## 6. Geometry makes an increasingly thin code inside ambient prime residues

At modulus `P_d`, arbitrary ordered triples of residues coprime to `P_d` occupy an ambient cube of size

`phi(P_d)^3`.

The incidence code occupies only `|I_d|` of those states.

The exact code fraction decreases rapidly:

- d=2: `0.75`;
- d=3: about `0.1523`;
- d=4: about `0.02186`;
- d=8: about `4.743e-7`;
- d=12: about `6.201e-13`;
- d=19: about `5.856e-25`.

Thus the native triple-cell incidence relation cuts out an increasingly thin, exactly defined high-dimensional residue manifold inside the ambient prime-compatible cube.

## 7. Finite prime-event occupancy

Use the frozen interior triple-prime census through `r<=3000`, giving 17404 nonexceptional full-prime incidence events in total.

Project their ordered residue words into the first incidence-code levels.

Observed occupancy:

- d=2 / mod 6: `6/6` states occupied;
- d=3 / mod 30: `78/78` states occupied;
- d=4 / mod 210: `2415/2418` states occupied;
- d=5 / mod 2310: `16914/220038` states occupied.

At the dense lower levels, empirical counts are close to uniform on the geometry-selected code rather than concentrated on a small subset.

Reduced chi-square against uniform code-state occupancy:

- d=2: about `0.9902`;
- d=3: about `0.8901`;
- d=4: about `0.9666`.

At d=5 the sample is sparse; the observed occupied count 16914 is close to the uniform-sampling occupancy baseline of about 16733.5 states for N=17404 draws.

These are finite diagnostics, not equidistribution theorems.

## 8. Comparison with the earlier shell-residue CRT tower

The previous shell-residue tower used one scalar unit residue per prime channel and was quantitatively dominated by classical Hardy-Littlewood local sieve structure.

The present tower is more geometry-native because its local channel is selected by the primitive three-cell coordinate-vertex incidence and its exact discrete curvature equation.

Nevertheless finite-field CRT and residue equidistribution are classical, and the observed near-uniform prime occupancy can still be compatible with ordinary local arithmetic.

Therefore the novelty boundary remains strict:

`EXACT NATIVE INCIDENCE CODE = ESTABLISHED IN THIS EXPERIMENT`.

`NEW PRIME-DISTRIBUTION THEOREM BEYOND CLASSICAL ARITHMETIC = NOT ESTABLISHED`.

## 9. Current research picture

The emerging native allocation hierarchy is now

`three positive-axis sector atlas`

`-> integer shell allocation`

`-> primitive triple-cell coordinate vertex`

`-> discrete curvature K=2/4`

`-> six-state mod-6 incidence hexacode`

`-> punctured curvature planes H_q`

`-> 2D-19D incidence-channel collapse tower`.

This construction supplies a genuine 2-to-19-dimensional exploration object without importing orthogonal Euclidean axes.

## 10. Next hard test

The next discriminating observable should use the **incidence graph between adjacent coordinate vertices**, not only the marginal residue state at one vertex.

Specifically, test whether prime-bearing incidence-code states have transition/holonomy statistics around elementary loops that survive matched local-congruence controls. A loop statistic would depend on how native incidence events glue, not merely on the one-vertex residue sieve.
