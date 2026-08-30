# GEO6 Sphere-Packing Density Bridge — Research Return

Task: `RS-GEO6-SPHERE-PACKING-DENSITY-BRIDGE`  
Publication: `TP2-69A99643C0A144D7453E`  
Researcher: `EM-G6PACK-A4C9E2`  
Execution record: `ER-126E8C130FD47B8AD60A`  
Claim: `chatgpt-g6pack-20260830-1112-a4c9e2`  
Date: `2026-08-30`

## Terminal disposition

`SUCCESS` at the declared-model strength.

Hard target disposition:

`P000_NATIVE_6D_PACKING_DENSITY_OR_NONOVERLAP_INVARIANT_CLASSIFIED`

More precisely:

`FINITE_NATIVE_OCCUPANCY_EXACT / PERIODIC_TRANSLATIONAL_DENSITY_EXACT_WITH_EXPLICIT_EXTRA_DATA / BARE_P000_GLOBAL_DENSITY_NOT_CURRENTLY_CANONICALLY_TYPED`.

The positive result is an exact six-dimensional discrete Cell packing theorem on an explicitly declared periodic model. The negative result is a typing/canonicality boundary for **bare current P000**, not a claim that no future P000-derived metric, translation action, or invariant mean can ever be constructed.

No Working Truth, Foundation, or canonical P000 promotion is asserted by this return.

---

## 1. Frozen semantic boundary

The following project constraints are retained throughout.

1. P000 fixes six native spatial dimensions and a discrete Cell ontology; rotation is primary.
2. The FCC carrier is the currently selected coordinate carrier, but carrier readout is not native Cell identity.
3. Carrier `S4` is an accepted carrier rotation algebra, not the complete bare-P000 native rotation group.
4. Euclidean `R^6`, the `E6` root lattice, Euclidean radius, Lebesgue volume and Euclidean Fourier transform are external comparison structures only.
5. Contact, exclusion/non-overlap and global packing density are kept as distinct types.

Accordingly, this task does **not** define native packing by importing Euclidean ball volume. It first defines a Cell conflict relation and only then counts admissible occupied Cells.

## 2. Tool-reuse resolution

The project toolbox was checked before introducing any general mechanism.

- `T1_SCALE_ENUMERATION_VALUATION`: `REUSE_APPLIED` for finite Cell counts and boundary-count control.
- `T5_PRECISION_REFINEMENT`: `REUSE_APPLIED` for exact finite cover/refinement pullback.
- `T7_FINITE_SYMMETRY_EQUIVARIANCE`: `REUSE_APPLIED` for orbit/equivariance checks.
- `T4_FINITE_FIBER_CAPACITY_COLLISION_MINIMA`: `NOT_APPLICABLE_AS_GEOMETRY_DEFINER`; it can reason about representative packing only after an observation/quotient is already semantically declared and therefore cannot invent the native non-overlap relation required here.

No new global toolbox family is proposed.

---

## 3. Native finite packing object

A **finite Cell packing datum** is a pair

`M=(X,C)`

where:

- `X` is a finite set of native Cell states/locations in the declared model;
- `C subset {{x,y}:x,y in X, x!=y}` is a symmetric irreflexive **conflict relation**.

An occupied set `S subset X` is non-overlapping iff

`{x,y} notin C` for all distinct `x,y in S`.

Equivalently, `S` is an independent set of the conflict graph `G_M=(X,C)`.

Define

`occ_M(S)=|S|/|X|`,

and the optimum finite occupancy

`delta(M)=alpha(G_M)/|X|`.

This is a rational number defined by finite Cell counting alone once `X` and `C` are declared. It uses no Euclidean volume.

### Proposition 3.1 — finite automorphism invariance

If `g:X->X` is a bijection satisfying

`{x,y} in C iff {g(x),g(y)} in C`,

then

`occ_M(gS)=occ_M(S)` and `delta(M)` is unchanged.

This gives the exact finite translation/rotation law whenever the relevant transformation is genuinely realized as an automorphism of the declared native model.

**Guard:** a carrier permutation is not automatically such a native automorphism; a lift/model realization must be declared or proved.

---

## 4. Periodic density theorem with explicit translation datum

Bare P000 does not presently provide all data needed below. Therefore this section is explicitly conditional on a declared translation model.

Let

`Gamma = Z^6`

act freely and transitively on a Cell carrier `X`. Let `C` be a `Gamma`-invariant conflict relation. Let `H <= Gamma` have finite index, and put

`Q=X/H`.

Let `I subset Q` be an independent set and let `I_tilde subset X` be its full periodic lift.

### Theorem 4.1 — Følner-independent periodic density

For every Følner sequence `(F_k)` in `Gamma=Z^6`,

`lim_k |I_tilde intersect F_k|/|F_k| = |I|/|Q|`.

#### Proof

The `H`-cosets form the finite quotient `Gamma/H`. For any two cosets `a+H` and `b+H`, choose `t=b-a`. Translation by `t` maps the first coset bijectively to the second. Hence the difference between their counts inside `F_k` is bounded by

`|F_k Delta (F_k+t)|`.

The Følner property makes this `o(|F_k|)`. Since the finitely many coset counts sum to `|F_k|`, every coset has limiting proportion `1/[Gamma:H]`. Summing over the `|I|` occupied cosets gives the claim. `QED`.

Thus a periodic occupancy has a window-independent infinite density **after** a native translation action and its finite-period quotient have been declared.

### Proposition 4.2 — exact finite boundary certificate

More generally, if a periodic fundamental-domain tiling is fixed, every complete fundamental tile contributes exactly the quotient density. All finite-window error is confined to incomplete boundary tiles. Therefore for a finite window `W`,

`| |I_tilde intersect W| - delta |W| | <= |B(W)|`,

where `B(W)` is the set of Cells of `W` lying in incomplete fundamental tiles and `delta=|I|/|Q|`.

This is a finite combinatorial boundary statement; no continuum limit is being assumed.

---

## 5. Exact six-dimensional native pressure-test model

For every even integer `n>=4`, define the declared six-dimensional periodic Cell model

`T_n=(Z/nZ)^6`.

The six coordinates are typed by `E1,...,E6`. Define the non-overlap conflict relation by

`x C_n y`

iff

`y-x = +e_i or -e_i (mod n)`

for some one of the six axis types.

This is a 12-regular finite conflict graph for `n>=4`. It is a **declared P000-compatible six-axis discrete model**, not an assertion that bare P000 or the current FCC carrier is canonically identical to this torus.

### Theorem 5.1 — exact optimum `delta(T_n)=1/2`

For every even `n>=4`,

`alpha(T_n)=n^6/2`,

hence

`delta(T_n)=1/2`.

#### Lower construction

Define the parity class

`P_n={x in T_n : x_1+...+x_6 = 0 (mod 2)}`.

Parity is well-defined because `n` is even. Every conflict edge changes exactly one coordinate by `±1`, hence flips parity. Therefore `P_n` is independent. Exactly half the `n^6` vertices have even parity, so

`|P_n|=n^6/2`.

#### Independent upper mechanism 1 — perfect matching

Pair every vertex whose `E1` coordinate is even with the vertex obtained by adding `e_1`. These are conflict edges, disjoint, and cover all `n^6` vertices. An independent set contains at most one endpoint from each pair, so

`alpha(T_n)<=n^6/2`.

Combined with the lower construction, equality follows.

### Independent upper mechanism 2 — finite spectral/LP analogue

The adjacency eigenvalues of the Cayley conflict graph are

`lambda(k)=2 sum_{j=1}^6 cos(2 pi k_j/n)`.

For even `n`, the least eigenvalue is exactly `tau=-12`, attained at `k_j=n/2` for all `j`; the degree is `d=12`.

For a `d`-regular graph, the Hoffman inequality gives

`alpha/N <= -tau/(d-tau)`.

Here it yields

`alpha/n^6 <= 12/24 = 1/2`.

For completeness, the Hoffman step follows directly by writing the independent-set indicator as `x=p 1 + y`, using `x^T A x=0`, `A1=d1`, and `y^T A y>=tau ||y||^2`.

This is the reusable part of the Euclidean LP idea: positivity/spectral constraints plus a sign/exclusion condition can bound packing without Euclidean volume.

---

## 6. Translation, rotation-readout and refinement laws

### 6.1 Translation

Every translation `x -> x+v` of `T_n` preserves `C_n`, hence preserves optimum occupancy.

For the explicit parity optimizer:

- if `sum_i v_i` is even, the translation fixes `P_n`;
- if it is odd, it exchanges `P_n` with its complementary parity class.

Both classes have density `1/2`.

### 6.2 Carrier-S4 readout realization

Inside this declared model, coordinate permutations realize the accepted Gen12 axis-readout generators

`a_xi=(E1 E2 E3)(E4 E6 E5)`,

`b_xi=(E2 E4)(E3 E5)` with `E1,E6` fixed.

They satisfy

`a_xi^3=b_xi^2=(a_xi b_xi)^4=id`

and preserve both `C_n` and `P_n`.

This establishes an **equivariant model realization** of the carrier-S4 axis action on this pressure-test model.

It does **not** establish

`BARE_P000_NATIVE_ROTATION_GROUP = S4`,

nor does the larger coordinate-permutation automorphism group of this toy model become native P000 symmetry.

### 6.3 Exact cover-refinement

For integers `k>=2`, reduction modulo `n` gives

`q_{k,n}:T_{kn}->T_n`.

Every fiber has size `k^6`. Fine conflict edges map to coarse conflict edges. Hence if `S subset T_n` is independent, its full preimage is independent and

`|q_{k,n}^{-1}(S)|/(kn)^6 = |S|/n^6`.

For even `n`, the parity optimizer pulls back exactly to the parity optimizer because reduction modulo even `n` preserves parity.

Therefore the declared quotient-refinement preserves the exact density `1/2`.

**Typing guard:** this is a finite cover/refinement law. It is not yet a claim that `n -> kn` is the unique physical P000 scale refinement; a physical scale interpretation would require an additional scale map.

---

## 7. Exact adversarial boundary law for the parity packing

Lift the parity packing to `Z^6`. Partition `Z^6` by the global `E1` matching

`(2m,x_2,...,x_6) <-> (2m+1,x_2,...,x_6)`.

For any finite window `W subset Z^6`, let `b_M(W)` be the number of vertices in `W` whose matched partner lies outside `W`.

Every complete matching pair inside `W` contributes exactly one occupied parity Cell. Therefore

`|2|P intersect W|-|W|| <= b_M(W)`,

or equivalently

`| |P intersect W|/|W| - 1/2 | <= b_M(W)/(2|W|)`.

This is an exact finite boundary error certificate and handles shifted, thin, odd-sided and otherwise adversarial finite boxes. The deterministic checker includes such cases.

---

## 8. External six-dimensional benchmark: `E6`

The external Euclidean benchmark is represented exactly by the `E6` simple-root Gram matrix

```text
G =
[ 2 -1  0  0  0  0]
[-1  2 -1  0  0  0]
[ 0 -1  2 -1  0 -1]
[ 0  0 -1  2 -1  0]
[ 0  0  0 -1  2  0]
[ 0  0 -1  0  0  2]
```

Exact arithmetic gives

`det(G)=3`.

The minimum nonzero squared norm is `2`. In this simple-root basis there are exactly `72` norm-2 roots. Completeness of the finite enumeration range follows from

`c_i^2 <= (c^T G c)(G^{-1})_{ii}`;

for norm `2`, the largest diagonal entry of `G^{-1}` is `6`, so `|c_i|<=3`.

Thus the lattice covolume is `sqrt(3)`, the maximal equal-sphere radius from the minimum norm is `1/sqrt(2)`, and the ordinary Euclidean lattice packing density is

`Delta(E6) = (pi^3/6)(1/sqrt(2))^6 / sqrt(3)`

`          = pi^3/(48 sqrt(3))`

`          ~= 0.3729475455820649`.

Its center density is

`1/(8 sqrt(3))`.

As a freshness check, Henry Cohn's maintained sphere-packing table currently lists the same best-known six-dimensional packing density `0.3729475455820649...` and an upper bound `0.4103032818801865`, so the six-dimensional Euclidean optimum remains unresolved as of this run.

### Required mapping data before `E6` can say anything native

At minimum, an `E6 -> P000` packing comparison would require all of the following extra structure:

1. a typed readout/embedding `phi:X_native -> R^6` or an equivalent exact distance readout;
2. a theorem relating the native conflict predicate to a Euclidean separation threshold;
3. a normalization relating native Cell counting/fundamental domains to Euclidean covolume or measure;
4. an equivariance statement relating native rotations/translations to the external Euclidean action.

Without these data,

`E6_LATTICE != P000_NATIVE_CELL_SPACE`

and

`Delta(E6) != NATIVE_PACKING_DENSITY_THEOREM`.

---

## 9. What survives from Cohn-Elkies LP, and what does not

The classical Cohn-Elkies program uses auxiliary functions to turn pairwise exclusion plus Fourier positivity into upper bounds for Euclidean sphere-packing density. The 2024 work of de Courcy-Ireland, Dostert and Viazovska proves that this two-point LP bound is not sharp in dimension six, so even in the external Euclidean problem it is not the final six-dimensional mechanism.

### Structurally transferable layer

The following abstract steps can survive after suitable native data are declared:

1. encode non-overlap as pairwise forbidden relations/differences;
2. choose a test kernel/observable with a positivity certificate;
3. impose a sign constraint on forbidden or allowed off-diagonal pairs;
4. sum the kernel over occupied pairs;
5. use the diagonal contribution plus positivity to derive a global occupancy upper bound;
6. average over an actually realized symmetry group;
7. on finite periodic Cell quotients, replace continuous Fourier analysis by exact character/eigenvalue or PSD-matrix calculations when a finite translation group is declared.

The Hoffman proof in Section 5 is an exact finite instance of this transferable positivity layer.

### Strictly Euclidean/analytic layer that does not transfer automatically

The following require additional structure and cannot be silently imported into P000:

- a Euclidean norm and radial distance variable;
- Schwartz functions on `R^6`;
- the continuous Fourier transform on `R^6`;
- Fourier positivity with respect to Lebesgue measure;
- Euclidean ball volume;
- Poisson summation for a Euclidean lattice and its dual;
- modular-form constructions tied to the Euclidean/Fourier LP;
- any numerical Euclidean LP or SDP bound as a native Cell-density bound.

Thus the native bridge is **positivity/spectral-exclusion**, not “copy the Cohn-Elkies numerical bound.”

External references used for this boundary:

- Henry Cohn and Noam Elkies, *New upper bounds on sphere packings I*, Annals of Mathematics 157 (2003), DOI `10.4007/annals.2003.157.689`.
- Matthew de Courcy-Ireland, Maria Dostert, Maryna Viazovska, *Six-dimensional sphere packing and linear programming*, Mathematics of Computation 93 (2024), DOI `10.1090/mcom/3959`.
- Henry Cohn, maintained sphere-packing data table, `https://cohn.mit.edu/sphere-packing/`, checked 2026-08-30.

---

## 10. Bare-P000 canonical-density boundary

The current P000 foundation grants, among other things, a six-dimensional discrete Cell ontology and rotation-first geometry. The current FCC carrier documents explicitly guard that carrier readout is not native Cell identity and that carrier `S4` is not the full native rotation group.

The currently frozen primitive interface does **not** itself supply all of:

- a canonical global native non-overlap/conflict relation;
- a free/cofinite native translation action `Gamma` on all Cells;
- a canonical exhaustion/Følner class or invariant mean;
- a measure/volume normalization;
- a physical refinement map compatible with the above.

Therefore the expression

`lim |S intersect W_n|/|W_n|`

is not a canonical bare-P000 term until the window/action data selecting the `W_n` are derived or supplied. Choosing the FCC carrier's classical volume cannot repair this typing gap, because the foundation explicitly forbids identifying carrier readout with native identity.

The exact classification at current strength is therefore:

`BARE_P000 + DECLARED_FINITE_CELL_SET + DECLARED_CONFLICT -> EXACT_FINITE_OCCUPANCY`,

`BARE_P000 !-> CURRENTLY_CANONICAL_GLOBAL_PACKING_DENSITY`,

while

`P000 + NATIVE_CONFLICT + Z^6_TRANSLATION_MODEL + FINITE_PERIOD_QUOTIENT -> EXACT_PERIODIC_DENSITY`.

This is the valid no-go component required by the task: the missing structure is named exactly rather than replaced by Euclidean volume.

---

## 11. Deterministic verification

Checker:

`research_checks/GEO6_SPHERE_PACKING_DENSITY_BRIDGE_CHECK_20260830.py`

The checker uses no external Python packages and verifies:

1. carrier-readout generator relations `a^3=b^2=(ab)^4=id` on the six axis slots;
2. `T_4`: 4096 Cells, exact parity construction 2048, exact perfect matching 2048;
3. `T_6`: 46656 Cells, exact parity construction 23328, exact perfect matching 23328;
4. every parity Cell has no declared conflict neighbor in the occupied set;
5. unit translations exchange the two optimal parity phases;
6. the declared carrier-S4 coordinate actions preserve conflicts and the parity optimizer;
7. `T_8 -> T_4` full-fiber refinement preserves exact density `1/2`;
8. shifted/thin/odd-sided adversarial boundary windows satisfy the exact matching-boundary inequality;
9. external `E6` Gram determinant `3`, minimum squared norm `2`, and exactly `72` norm-2 roots in the certified range.

Observed deterministic output:

```text
PASS GEO6 sphere-packing density bridge
T_4: cells=4096, independent=2048, matching_pairs=2048, density=1/2
T_6: cells=46656, independent=23328, matching_pairs=23328, density=1/2
refinement T_8 -> T_4: full-fiber parity lift preserves density=1/2
E6 benchmark: det(Gram)=3, min norm^2=2, norm-2 roots=72
all symmetry and adversarial boundary checks passed
```

---

## 12. Research value and unresolved residue

### Established

- A native finite packing invariant exists once Cell conflict is declared: normalized independence number.
- An explicit six-dimensional periodic P000-compatible model has exact optimum density `1/2` with independent lower and upper certificates.
- The density is equivariant under translations and the declared carrier-S4 axis-readout realization.
- A precise cover/refinement law preserves the density.
- Periodic infinite density is independent of Følner window choice once `Z^6` translation and finite period are declared.
- The transferable Cohn-Elkies content is isolated as positivity/spectral exclusion; Euclidean Fourier/volume machinery is kept external.
- `E6` is represented exactly as a benchmark without identifying it with the native carrier.

### Unresolved / explicitly not claimed

- No canonical global non-overlap relation has been derived from bare P000.
- No canonical bare-P000 translation group, invariant mean or physical refinement has been established.
- The torus model is a declared pressure-test model, not the unique P000 geometry.
- The current FCC carrier is not replaced by `Z^6` or `E6`.
- The exact Euclidean `R^6` sphere-packing optimum remains open and is not solved here.
- No native analogue of the full Euclidean Cohn-Elkies or three-point SDP bound is promoted.

## 13. Driver-review recommendation

Review this result as a **model-relative positive theorem plus bare-language no-go**.

The highest-value successor, if authorized, is not “optimize a larger torus.” It is to decide whether the current P000/FCC native relation language can **derive** one of the missing data:

`NATIVE_NONOVERLAP_RELATION`, `NATIVE_TRANSLATION/FOLNER_STRUCTURE`, or `PHYSICAL_REFINEMENT_COMPATIBILITY`.

Only after such a derivation should a global native packing-density extremal problem be promoted.
