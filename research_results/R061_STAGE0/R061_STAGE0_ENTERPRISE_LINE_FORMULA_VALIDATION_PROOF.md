# R061 Stage 0 — Enterprise Line Formula Validation Proof

Task-ID: `RS-R061-STAGE0-ENTERPRISE-LINE-FORMULA-ALGEBRAIC-PATH-LIFT-VALIDATION`  
Taskbook source: `0936ade269bcdc3a58b3d8b4c2148c6197dc1a63`  
Owner branch: `research/r061-stage0-line-formula-path-lift-validation`

## Final status

`ENTERPRISE_LINE_FORMULA_VALIDATED = false`

Strongest typed result:

`COORDINATE_LIFT_VALID_BUT_NATIVE_PATH_LIFT_INCOMPLETE`.

Also established:

- `SHUFFLE_THEOREM_VALID_BUT_PI_CELL_NONTRIVIAL_OR_UNDERDETERMINED`;
- `FORMAL_SECTOR_COVARIANCE_VALID_BUT_NATIVE_GLUE_OPEN`;
- `ORIGIN_OFFSET_BREAKS_NAIVE_ENDPOINT_TYPING`;
- `THIRD_AXIS_COUNTEREXAMPLE_TO_MINIMUM_JUMP_COMPLETENESS`.

No Stage A is opened and no candidate is frozen as canonical.

## 1. Scalar -> coordinate fiber

Validated.

For every `N`, the coordinate fiber

`D_N={(a,b)>=0:a^2+b^2=N}`

is exact. Factorization/norm arithmetic in

`A_E=Z[J]/(J^2+1)`

provides a complete algebraic extraction route independent of brute target
search. Exhaustive `N=0..100000` gives zero mismatches against direct integer
ground truth. All square hypotenuse cases `r<=4096` give zero mismatches
against complete Euclid parameterization.

This part of the proposed line formula survives unchanged.

## 2. Coordinate pair -> free noncommutative fiber

Validated.

For every `(a,b)`,

`[u^a v^b](uX+vY)^(a+b)`

is exactly the sum of all free words containing `a` copies of `X` and `b`
copies of `Y`, each once, cardinality `binom(a+b,a)`.

All 8,388,607 words for all pairs `a+b<=22` were explicitly enumerated and
checked. Compressed Pascal validation through `a+b<=512` has zero mismatches.

This part also survives unchanged as a formal theorem.

## 3. Exact class generated

The free lift generates exactly the finite class of directed
coordinate-monotone two-positive-generator words.

It is not automatically the native line-path fiber.

On the actual triangular nearest-center carrier, the preserved carrier
relation gives `-t3=t1+t2`. Consequently the carrier graph distance to formal
interior displacement `(a,b)` is `max(a,b)`, not `a+b`.

Minimal positive interior witness:

`N=2`, `(a,b)=(1,1)`.

The shuffle produces two two-step words `X1X2` and `X2X1`, while one
nearest-center inverse-third-family step `-X3` reaches the same carrier center.

Therefore the shuffle is not all minimum-jump realizations and omits legitimate
third-family nearest-center paths.

## 4. Native cell realization / Pi_cell

Not validated.

`O_E` is a triple cell-boundary intersection, not a cell. Center-transition
letters cannot act directly on it. A type-correct native realization requires
a start-incidence operator

`Sigma_O`

that selects one of the three incident cells before any center transition.

The current foundation does not specify the affine map from those incident
cells to absolute integer center addresses. Therefore the formal displacement

`End_formal(w)=(#X,#Y)`

cannot be silently identified with the absolute native endpoint address.

The `N=0` boundary case is the smallest typing witness: the formal empty word
exists, but there is no native circle-cell state at the origin.

Accordingly `Pi_cell` is neither proved identity nor derivable as an exact
projection from the current premises.

## 5. 3-4-5 case

`D_25={(0,5),(3,4),(4,3),(5,0)}` is recovered exactly.

For `(3,4)`, the free lift has `binom(7,3)=35` words, each of seven letters.

What is **not** proved is that seven letters equal the native
origin-to-endpoint center-transition count. Type-correct native replay is only
of the form

`Sigma_O ; w`

after a start cell is selected, and the missing affine address anchor prevents
an exact off-by-one resolution. Native length remains exactly `5` by the
sector metric, independent of jump count.

## 6. Third-axis completeness

Failed.

The `(1,1)` witness is exact at the carrier incidence level and uses no
carrier Euclidean metric as native length. More generally every
nondegenerate `(a,b)` has full-carrier minimum jump count `max(a,b)`, so the
two-positive shuffle cannot be the set of all minimum-jump realizations.

## 7. Sector covariance and gluing

Formal cyclic covariance passes. Coordinate-level axis deduplication also
passes: the same physical positive axis appearing in two adjacent charts is
identified by `(axis label, radial coordinate)`.

Full native path covariance/gluing does not pass because origin incidence,
absolute affine start addresses, and cross-sector trajectory maps are not
defined, and because third-family paths are missing from the sector-local
shuffle.

## 8. Forward / reverse consistency

The formal diagram

`word -> coordinate -> N`

and

`N -> D_N -> formal words`

is exact and fiber-valued.

The native diagram is not proved because native path -> absolute address is
not yet defined for the candidate realization.

## 9. Acceptance gates

1. `COORDINATE_FIBER_COMPLETE = true`
2. `ALGEBRAIC_FACTOR_EXTRACTION_COMPLETE = true`
3. `NONCOMMUTATIVE_COEFFICIENT_LIFT_EXACT = true`
4. `PATH_CLASS_TYPED_FINITE_AND_CANONICAL = false`
5. `CELL_ADMISSIBILITY_EXACT = false`
6. `ORIGIN_AFFINE_OFFSET_RESOLVED = false`
7. `THIRD_AXIS_COMPLETENESS_PASS = false`
8. `THREE_SECTOR_COVARIANCE_PASS = false`
   - formal-only subgate: `true`
9. `AXIS_GLUE_DEDUP_PASS = false`
   - coordinate-only subgate: `true`
10. `FORWARD_REVERSE_FIBER_CONSISTENCY_PASS = false`
    - formal-only subgate: `true`
11. `NO_CARRIER_EUCLIDEAN_METRIC_LEAKAGE = true`
12. `LARGE_DETERMINISTIC_VALIDATION_PASS = false`
    - coordinate/formal computational validation: `true`
    - native realization validation: `false`

Because not all gates pass:

`ENTERPRISE_LINE_FORMULA_VALIDATED = false`.

## 10. Smallest preserved counterexamples

### CE-R061-ORIGIN-000

`N=0`.

Formal object: one empty word.

Native fact: `O_E` is not a cell.

Breaks: full-fiber `Pi_cell=identity` typing.

### CE-R061-THIRDAXIS-11

`N=2`, coordinate branch `(1,1)`.

Formal shuffle: `{X1X2,X2X1}`, two jumps.

Missed carrier path: `{-X3}`, one nearest-center jump.

Breaks: completeness for all nearest-center/minimum-jump native realizations.

Both are retained in `R061_STAGE0_COUNTEREXAMPLES.json`.

## 11. Strongest formula that survives

The exact surviving theorem is formal:

`FORMAL_LIFT_E^(ij)(N)
 = disjoint_union_{a^2+b^2=N} Sh_{a,b}(X_i,X_j)`.

This is an exact scalar-to-coordinate-to-free-word fiber.

It is **not** yet a native circle-cell line formula.

A native formula requires an additional, independently specified realization
layer carrying at least origin incidence, absolute affine addressing,
cross-sector transitions, and a canonical finite native path class. If that
class is the downstream all-minimum-jump realization, it must include the
third-direction families exposed above and cannot equal the current shuffle.

## Driver review boundary

The validation package is complete for Stage 0. The result is intentionally
left for Driver classification among the taskbook's review outcomes
(`REJECT_WITH_COUNTEREXAMPLE`, `CORRECT_AND_RETEST`,
`OPEN_NEXT_FOUNDATIONAL_QUESTION`, etc.).

No canonical freeze and no R061 Stage A opening is performed.
