# R059D Stage W — Triaxial Integer-Cell Root-Collapse Atlas

Researcher-ID: `EM-R059D-9C6B2A`  
Taskbook source: `ce0c98cb2e729d8773443b1f3ebdf8fb4328365b`  
Frozen parent: `a9929a5bd666e621cb1bd77adb464df0d35db399`

## Semantic reset

`CELL_COORDINATES_ARE_INTEGER_ONLY`.

A radical such as `sqrt(2)` is a `PRECOLLAPSE_ALGEBRAIC_VALUE`; it is never stored as a crystal-cell address.

Stage-U stabilizer selection, superseded Stage-V post-credit selection, nearest rounding, probability, Euclidean distance/angle/length, the old zero-sum raw coordinate sheet, and the old `(1,-1,0)` transfer coordinate were not used as positive premises.

## W0 constructional dependency

The task requires cell identity to be fixed before coordinate fitting and requires mixed-path recoalescence. The explicit W0 construction used here is the minimal homogeneous triaxial translation grid:

- abstract cell identities form the Cayley adjacency graph of `Z^3` under commuting unit moves `±u,±v,±w`;
- the abstract exponent triple `(a,b,c)` is an `ADJACENCY_INDEX`, not the stored cell coordinate under test;
- inverse moves exactly undo one another;
- a named direction has one homogeneous coordinate increment throughout the atlas.

This dependency is explicit. If only six unrelated labeled walk moves are supplied, with no commuting/homogeneous translation closure, the universal-cover walk tree does not determine nontrivial recoalescence or unique shell-2/shell-3 coordinates. Therefore the positive atlas below is conditional on this W0 constructional typing.

## Integer cell atlas

Frozen first-step readouts:

- `+u -> (1,-1,-1)`
- `+v -> (-1,1,-1)`
- `+w -> (-1,-1,1)`
- negative directions by exact sign inversion.

The resulting stored coordinate map is

`coord(C[a,b,c]) = (a-b-c, -a+b-c, -a-b+c)`.

Its matrix is

`[[1,-1,-1],[-1,1,-1],[-1,-1,1]]`

with determinant `-4`. Hence the map is injective over integer adjacency indices: distinct declared cells cannot acquire the same stored coordinate.

Shell counts are:

- shell 0: `1`
- shell 1: `6`
- shell 2: `18`
- shell 3: `38`

so the radius-3 ball contains `63` cells.

Thus `(1,-1,-1)` one-step semantics is globally self-consistent on the declared W0 translation atlas.

## Multi-path / off-axis gates

All shortest-path permutations and selected reversal-loop paths were evaluated exactly. The radius-3 test contains `289` path-coordinate checks and `378` inverse-transition checks.

Examples:

- `C[1,1,0]` is reached by `+u,+v` and `+v,+u`; both give `(0,0,-2)`.
- `C[1,-1,0]` is reached by `+u,-v` and `-v,+u`; both give `(2,-2,0)`.
- `C[1,1,1]` is reached by all six shortest permutations of `+u,+v,+w`; all give `(-1,-1,-1)`.

Cyclic relabeling and global inversion pass exactly.

## Root-family test

The frozen candidate registry is `r_p(n)=n^(1/p)` for `p=1..6`, with exact tables for `n=0..36`. Noninteger roots are precollapse values only. For an interval `k^p<n<(k+1)^p`, both integer completion magnitudes `k` and `k+1` are propagated; neither is preferred a priori.

### p=1

`r_1(n)=n` exactly regenerates the frozen ray coordinates

`(n,-n,-n)`

and therefore survives all radius-3 gates. It is an identity count relation, not a nontrivial radical collapse.

### p=2..6

At `n=2`, all `p>=2` candidates have legal integer root levels `1` and `2`:

- lower gives `(2,-1,-1)` and contradicts the frozen atlas;
- upper gives `(2,-2,-2)` and is therefore `FORCED_UPPER_BY_ATLAS` at this one point.

At `n=3`, all `p>=2` candidates still have legal levels only `1` and `2`, while the frozen cell `C[3,0,0]` is `(3,-3,-3)`.

Therefore both branches fail:

`NEITHER_SELF_CONSISTENT`.

Hence every nontrivial tested root order `p=2..6` is `REJECTED_BY_THIRD_SHELL`.

The square-root candidate is therefore:

`SQUARE_ROOT_PRECOLLAPSE_REJECTED` within the declared W0 atlas and tested registry.

## 5 -> 4 / 9

The taskbook permits the `sqrt(5)` control only if square root survives earlier gates. It does not: the square-root model is already killed at `n=3`.

Therefore Stage W does **not** force either:

- `5 -> 4`, or
- `5 -> 9`.

The correct disposition is:

`FIVE_TO_FOUR_OR_NINE_NOT_ADJUDICATED_BECAUSE_SQUARE_ROOT_MODEL_FAILS_BEFORE_n=5`.

`sqrt(5)` remains a valid algebraic number, but it is not a surviving coordinate-precollapse law in this atlas.

## Mandatory controls

- floor-only sqrt: rejected at shell 2;
- ceiling-only sqrt: shell 2 passes but shell 3 rejects;
- nearest-integer sqrt: rejected at shell 2 by exact comparison `sqrt(2)<3/2`;
- midpoint threshold sqrt: rejected at shell 2;
- alternating lower/upper parity variants: rejected by shell 2 or shell 3;
- fixed `u`-axis preference: rejected by off-axis cell `C[1,1,0]`;
- old raw `x+y+z=K`: rejected by first shell because `(1,-1,-1)` changes the sum from `0` to `-1`;
- old raw `(1,-1,0)` transfer coordinate: directly contradicts the frozen first-step control.

## Simplest surviving rule

Within the declared W0 translation atlas, the simplest rule is direct integer recurrence:

- `+u: (x,y,z)->(x+1,y-1,z-1)`
- `+v: (x,y,z)->(x-1,y+1,z-1)`
- `+w: (x,y,z)->(x-1,y-1,z+1)`
- negatives are exact inverses.

Equivalently:

`coord(C[a,b,c])=(a-b-c,-a+b-c,-a-b+c)`.

Within the frozen root-order registry, `p=1` is the unique radius-3 survivor. No nontrivial root-collapse rule is established.

## Required final statements

- `CELL_COORDINATES_ARE_INTEGER_ONLY`: **ESTABLISHED by protocol and atlas**.
- Radicals are `PRECOLLAPSE_ALGEBRAIC_VALUES`, not coordinates: **FROZEN**.
- `(1,-1,-1)` one-step semantics: **globally self-consistent on the explicitly declared W0 commuting/homogeneous triaxial translation atlas**.
- Square root: **REJECTED_BY_THIRD_SHELL** in this atlas.
- Collapse branch: upper is locally forced at `n=2` for `p>=2`, but at `n=3` neither branch works, so no global nontrivial root-collapse rule survives.
- `5->4/9`: **INAPPLICABLE / NOT ADJUDICATED** because square root fails before `n=5`.
- Off-axis/multi-path tests: **PASS for the integer translation atlas; they reject an axis-preference control**.
- Remaining unidentified: whether a different independently justified non-translation adjacency/coordinate-transition construction could support a nontrivial root law; no such alternative is established here.
- `UNIVERSAL_BRC_LAW_NOT_ESTABLISHED`.

## Checker

Deterministic checker: `1918 / 1918 PASS`.

Checks digest:

`8e2dd3883f0ae137a6ed7e630bccf5eb0200912ef3722793ea1ec221c3e91ca6`

`STOP_FOR_DRIVER_REVIEW`
