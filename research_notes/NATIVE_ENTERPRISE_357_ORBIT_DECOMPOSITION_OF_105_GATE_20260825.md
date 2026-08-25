# Native Enterprise 3/5/7 orbit decomposition of the 105 gate

Status: `FREE_RESEARCH_EXACT_SMALL_CHARACTERISTIC_UNIFICATION / NOT_CANONICAL_FOUNDATION`

Date: `2026-08-25`

Researcher-ID: `EM-FREE-NEPS-239A6D`

Depends on:

- `NATIVE_ENTERPRISE_MOD5_K4_ORBIT_TO_C3_LANE_WEIGHT_BRIDGE_20260825.md`;
- `NATIVE_FILAMENT_INTRINSIC_HYPERBOLA_QUOTIENT_AND_BREAKER_SYMMETRY_20260825.md`;
- `NATIVE_ODD_SECTOR_CENTRAL_FIBER_SATURATION_GATE_THEOREM_20260825.md`.

## 1. Native C3 root partitions

For the native equal-coordinate bouquet

`F_-(m)=6m^2-2m+1`,

`F_0(m)=6m^2+1`,

`F_+(m)=6m^2+2m+1`,

the nonzero root partitions are:

### mod 3

- `F_-`: `{2}`;
- `F_0`: empty;
- `F_+`: `{1}`.

Lane multiplicity:

`1 : 0 : 1`.

### mod 5

- `F_-`: `{1}`;
- `F_0`: `{2,3}`;
- `F_+`: `{4}`.

Lane multiplicity:

`1 : 2 : 1`.

### mod 7

- `F_-`: `{2,3}`;
- `F_0`: `{1,6}`;
- `F_+`: `{4,5}`.

Lane multiplicity:

`2 : 2 : 2`.

All nonzero residue classes are saturated for each of 3,5,7.

## 2. Native split hyperbola normalization

For the nondegenerate odd characteristics use the native normalization

`3(y^2-x^2)=-1`.

The Klein-four sign group acts by independent sign changes of `(x,y)`.

Projection to the transverse bouquet parameter is

`m=y-x`.

For `q=5,7`, this projection can be compared directly with the C3 root partition.

## 3. q=5: one regular orbit -> 1:2:1

Modulo5 the hyperbola has `q-1=4` points and the `K_4` action is regular.

Choose base point

`(x,y)=(1,2)`.

Its four sign states project to

`m=1,2,3,4`.

By C3 lane divisibility:

- one state lands on `F_-`;
- two states land on `F_0`;
- one state lands on `F_+`.

Thus one regular four-point orbit contributes

`1:2:1`.

This is the previously frozen mod5 Hamming-weight bridge.

## 4. q=7: one regular orbit plus one ramified orbit

Modulo7 the same hyperbola has `q-1=6` points:

`{(0,3),(0,4),(3,2),(3,5),(4,2),(4,5)}`.

The `K_4` action decomposes them into exactly two orbits.

### Ramified two-point orbit

`O_ram={(0,3),(0,4)}`.

This orbit is fixed by the sign change of `x` because `x=0`; it therefore has size2 instead of4.

Projection `m=y-x` gives

`{3,4}`.

These kill respectively

- `F_-` at `m=3`;
- `F_+` at `m=4`.

Hence the ramified orbit contributes

`1:0:1`.

### Regular four-point orbit

`O_reg={(3,2),(3,5),(4,2),(4,5)}`.

Projection gives

`{1,2,5,6}`.

These distribute as

- one root of `F_-`: `m=2`;
- two roots of `F_0`: `m=1,6`;
- one root of `F_+`: `m=5`.

Hence the regular orbit contributes

`1:2:1`.

Adding the two orbit contributions gives

`(1:0:1)+(1:2:1)=(2:2:2)`.

Freeze:

`MOD7 UNIFORM LANE SATURATION = REGULAR K4 ORBIT + RAMIFIED OUTER-PAIR ORBIT`.

## 5. q=3: degeneration leaves the outer-pair pattern

At `q=3`, the native curvature coefficient satisfies

`3|B`.

Therefore the nonsingular split-hyperbola model degenerates: the quadratic backbone disappears modulo3 and the longitudinal hyperbola torsor is not present in the same form.

The transverse C3 bouquet nevertheless has the exact root pattern

`1:0:1`.

Thus the smallest gate factor is the degenerate boundary analogue of the outer-pair contribution that reappears as the ramified orbit inside the nondegenerate q=7 hyperbola.

This is a structural analogy, not an isomorphism of the degenerate q=3 fiber with the q=7 ramified orbit.

## 6. General K4 orbit decomposition on the hyperbola

For odd `q`, `BC!=0`, consider

`R={(x,y): B(y^2-x^2)=C}`.

The only possible nonregular `K_4` orbits arise on the coordinate axes:

- `x=0` occurs iff `C/B` is a square;
- `y=0` occurs iff `-C/B` is a square.

Each existing axis pair is one size-2 orbit.

Let

`a_q = 1_[C/B square] + 1_[-C/B square]`.

Then:

- number of size-2 ramified orbits = `a_q`;
- remaining points = `q-1-2a_q`;
- number of regular size-4 orbits = `(q-1-2a_q)/4`.

Hence total quotient size is

`a_q + (q-1-2a_q)/4`

`=(q-1+2a_q)/4`,

which is equivalent to the Burnside / quadratic-character formula.

For native q=5:

`a_5=0`, so there is one regular orbit.

For native q=7:

`a_7=1`, so there is one ramified orbit and one regular orbit.

## 7. 105 gate as a three-regime packet

The three factors of the native gate now have distinct but related geometric statuses:

### 3

`quadratic-backbone degeneration + transverse outer-pair saturation`.

### 5

`one regular K4 orbit; simultaneously the longitudinal universal breaker and transverse complete saturation`.

### 7

`one regular K4 orbit plus one ramified axis orbit; transverse complete saturation but longitudinal nonbreaker`.

Thus

`105=3*5*7`

is not a product of three copies of one mechanism.

It packages:

`DEGENERATION`

`x REGULAR ORBIT COLLAPSE`

`x REGULAR+RAMIFIED ORBIT COMPLETION`.

## 8. Why only 5 breaks longitudinally

At q=5 the complete hyperbola is exactly one regular symmetry orbit, so its quotient has one class and transparency is zero.

At q=7 the complete hyperbola has two symmetry classes, so transparency count is

`2-1=1`.

Therefore q=7 can still saturate the finite three-lane transverse packet while failing to break the infinite longitudinal filament.

This gives an exact local/global explanation of why both5 and7 enter the 105 bouquet gate but only5 belongs to the longitudinal breaker spectrum.

## 9. Prior-art boundary

Finite group orbit decompositions, ramification/fixed points and quadratic residues are classical.

The research-specific candidate is the exact identification of the native 3/5/7 bouquet saturation patterns with degeneration/regular/ramified orbit regimes of the same geometry-selected quadratic carrier.