# Two-positive raw X6 stability

The sole advertised public API is:

```python
audit_two_positive_stability(case_id, mu_atoms, nu_atoms, denominator=1)
```

Each population is finite and consists of pairs of canonical
`x6_signed.Spatial6` cells and strictly positive integer numerators. The
common denominator must also be a strictly positive integer. Booleans and
integer subclasses are rejected; cells must have the exact canonical class,
not a substitute or subclass. Both populations must refer to the same
external anchor and labelled signed X6 chart. That provenance is a caller
premise, not something that six integer coordinates can establish.

The consumer aggregates duplicate cells and cancels shared mass before
requiring p<=2 for the true Jordan positive support. The signed difference is
an auxiliary analysis ledger, not negative branch weights in a BRC primitive.
The original one-positive consumer is imported by its ordinary module name;
its canonical cell and arithmetic objects are reused without constructing a
private replacement package.

## Raw ledger and proof branches

The consumer uses the existing `population`, `raw_projection`, and
`verify_joint_projection` interfaces. It reconstructs all twenty raw
three-axis tables from the Jordan difference, verifies their native joint
slice roundtrips, and independently checks the reported rows and norms against
those projections. Each raw row retains its address, signed numerator,
canonical can3 address and per-slice common offset. Explicit zero rows are
kept as cancellation evidence; missing addresses have zero mass.

Write P and N for Jordan positive and negative mass numerators, M=P+N, and D
for the sum of the twenty table L1 numerators. D is neither an average nor a
maximum. All proof calculations use integers. The common unit, M and D masses,
bound constant and nonzero M/D ratio are canonical unevaluated DIV nodes.
Their literal numerators and denominators are not reduced or evaluated.

For p=0 or p=1, the unchanged old `audit_case` is called on reconstructed
positive populations. Its P, N, M, D and each of its twenty raw norms are
compared with the new ledger. Its stronger one-positive `3/20` and equal-mass
`1/10` bounds and zero/equality statuses remain in the certificate. That old
API is never called on a p=2 input.

For p=2, let d be the number of axes on which the two positive cells differ.

- For d=1 use k=10; for d>=3 use k=7. Every actual negative point lists all
  tables in which its projection avoids both positive projections and is
  checked to avoid at least k tables. The point-weighted count equals the sum
  of the per-table avoided negative masses. The consumer checks
  `D >= 20P+(2k-20)N`, `D >= 20(N-P)`, and the exact nonnegative-gap identity
  `(40-k)D-20kM = 20*(D-[20P+(2k-20)N]) + (20-k)*(D-20(N-P))`.
  Since `20k > 4(40-k)`, these branches give `D>4M` for their nonzero inputs.
- For d=2, the four H tables contain both differing axes. Their coefficient
  b is +1 at a positive projection address and -1 elsewhere. The other
  sixteen L tables use 0 at positive addresses and -1 elsewhere. The
  certificate records b and `|h|-b*h` at every actual raw address. It checks
  F=4 at both positive cells and F<=-4 at every actual negative cell, where
  F is the sum of the twenty b values. If a negative cell has a positive
  diagonal tuple but changes a common axis, the stricter F<=-7 case is
  checked explicitly. Every negative cell records all twenty coefficients,
  its H and L sums, changed common axes and `(-F-4)*n` gap.

The d=2 branch verifies the complete identity

```text
D - 4M = sum_tables sum_addresses (|h|-b*h)
         + sum_negative_cells (-F-4)*n.
```

Every displayed summand is nonnegative. In particular, checking only F=-4 on
negative cells is insufficient for sharpness: the table gaps must also vanish.
For N=0 the consumer checks D=20M directly and never divides by N. The zero
difference is separate, with M=D=0, `sharp_nonzero=False`, and `ratio=None`.
No 0/0 node is manufactured.

## Exact nonzero equality

Every nonzero equality is checked in the original Jordan coordinates. It must
have exactly two positive diagonal corners and exactly the two negative cross
corners of a coordinate rectangle. The positive cells differ on exactly two
axes, the four other coordinates agree, and all four absolute mass numerators
are equal and positive. Endpoints may have arbitrary distinct integer values;
unit spacing is not assumed.

The structural classification is required to agree with M>0 and D=4M, and
thus with zero complete gap in the d=2 branch. It never infers an original
rectangle from compressed representatives. Common population mass cancelled
before Jordan decomposition does not alter the classification.

The first executed case was the unit rectangle, with P=N=2, M=4, D=16,
zero table and negative gaps, and exact original-coordinate sharpness.

## Bounded certificate

The saved certificate has 17 cases, 340 raw tables and 18 expected rejections.

| Cases | Checked boundary |
| --- | --- |
| Unit and sign-reversed rectangles | Sharpness with either positive diagonal. |
| Unequal-total-mass rectangle and equal-total-mass unequal-corner rectangle | F=-4 at both negatives but positive table gap; neither is sharp. |
| Nonunit rectangle on axes 1 and 4 in shifted signed coordinates | Original-coordinate equality with arbitrary spans and common-axis values. |
| Positive-diagonal tuple with a changed common coordinate | Actual F=-7, positive negative-site gap. |
| Value outside the two endpoints of a differing axis | Extra negative-site penalty; not a cross corner. |
| d=1, d=3, d=6 | Integer counting branches; the d=3 case reaches exactly seven avoided tables for an actual negative point. |
| Several pre-cancellation mu sites reducing to p=2 | Exact equality of the Jordan ledger and every raw/dual table with the unit rectangle. |
| 2053-bit denominator `2^2052+1` | Literal DIV nodes retained; the sharp ratio remains DIV(28,112). |
| N=0, negative-only p=0, old p=1 boundary, empty zero, cancelled zero | Stronger and degenerate contracts retained. |

The eighteen refusals cover invalid weights and denominators, including
booleans and integer subclasses; noncanonical/subclass cells; a true p=3
input; actual raw-row and raw-norm tampering; a changed original rectangle
corner; a false-negative sharp flag; and the false claim that rectangle
support alone certifies unequal corner masses. The table and equality
refusals use the same internal checkers as successful API calls. They do not
replace any expected numerical assertion with an earlier unrelated failure.

No LP, weight optimization, full carrier enumeration, p>=3 extension,
microscopic-history recovery or physical equivalence is asserted.

## Frozen sources and observation scope

The sixteen exact source pins comprise the old consumer's twelve original
dependencies, that consumer itself, and these three proof sources:

- [Two-positive bound](../../research_notes/OWNER_TWO_POSITIVE_RAW_STABILITY_BOUND_REVIEW_20260908.md), SHA256 `1bb732a50cccbbec6c8c11950104c62eed9afc15f326fcc39d9142bd13b24a35`.
- [Independent bound proof](../../research_notes/OWNER_TWO_POSITIVE_RAW_STABILITY_INDEPENDENT_AUDIT_20260908.md), SHA256 `f610e3d642b53279efa91dec15ad3b392270768f73ad0a31edf38212b60be61c`.
- [Complete nonzero equality classification](../../research_notes/OWNER_TWO_POSITIVE_EQUALITY_CLASSIFICATION_REVIEW_20260908.md), SHA256 `1a50237cb4a92a3ec2ef7168b7bd8e90598f69aba394217221f24c83fa810ec7`.

The old consumer and three new papers are pinned before the import; the old
consumer checks its own twelve sources. The fixed build checks all sixteen
again before and after its observed work. Earlier nineteen-item catalog
coverage is historical reuse evidence only and is not a dynamic runtime pin.
The coverage decision remains EXTEND_EXISTING_TOOL. This implementation does
not invoke or modify the separate compression consumer.

The fixed build records actual selected native/helper call counts. For the
required population, raw, joint, old boundary, canonical cell, slice and DIV
functions, it checks the code source file and observes exact frame code-object
identity. The certificate records each function's source pin, module,
qualified name, observed count and bytecode digest. Bytecode and finite call
counts are interpreter-dependent; the certificate records the Python version.

The observation window starts after canonical imports. It rejects observed
Fraction arithmetic, quotient/root materialization and unrequested legacy
multiplicity paths during this build. It does not certify import-time
historical package initialization, unexecuted transitive code, or every C
internal operation. Pinned source bytes and actual observed code objects are
reported with those limits; no transitive migration claim follows.

## Reproduce

From the repository root, the default command is read-only:

```powershell
python -X utf8 -B experiments/owner_two_positive_stability_20260908/check_two_positive_stability.py
python -X utf8 -B tools/check_exact_arithmetic_policy.py experiments/owner_two_positive_stability_20260908/check_two_positive_stability.py
```

After a reviewed source/interpreter change, explicitly rebuild only this
directory's certificate with:

```powershell
python -X utf8 -B experiments/owner_two_positive_stability_20260908/check_two_positive_stability.py --write
```

The default compares the reconstructed certificate byte for byte and never
repairs it silently. The checker SHA256 is part of the certificate. `--write`
is the only file-writing route in the program and targets this directory's
`certificate.json`. No formal Task, Result, claim, Working Truth, Foundation
or catalog transition is granted by the executable evidence. The finite
certificate audits the implementation; the pinned papers carry the stated
all-input proof.

Global-Knowledge-Sync: main@eb09a0a / GLOBAL_KNOWLEDGE_V1
