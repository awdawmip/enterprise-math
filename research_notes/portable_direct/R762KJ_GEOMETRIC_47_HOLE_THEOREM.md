# R762KJ — Structural 47-hole theorem for the three-inactive-Port Euler observer

Date: 2026-11-23. **AUTHOR_EXACT_FINITE_CHECKED / NOT_REVIEWED.**
This is a geometric decision criterion and incidence refinement of R762KI, not a promotion of the auxiliary unsigned graph to native signed P000 dynamics.

## Exact provenance and scope

Frozen P000 input: `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json`. Scientific predecessor: `awdawmip/enterprise-math@211070ca0d144092298fe3883fd1a16712a1a021:research_notes/portable_direct/R762KI_M3_TWO_UPGRADE_AFFINE_OBSTRUCTION_THEOREM.md`; its matching exact checker and evidence are at the same commit.

The observer is the **unsigned six-axis Port–Euler graph**, with inactive Ports 01,23,45 and the remaining twelve Ports active. Each support abc permits one event edge joining two active two-axis Ports contained in abc. Twelve supports have one forced edge, eight have three edge choices; all twelve forced supports occur with arbitrary positive multiplicity, and all eight flexible supports occur exactly once. A realization is connected, keeps the exact support counts and has strictly positive even degree at each active Port.

P000's primitive signed TRIADIC_CLOSURE_E, Cell/Link/Port transition data and ordered BRC residual provenance retain their distinct scientific types. This result claims no observer-safe projection of native dynamics.

## Three even-subset grids

The forced edges form three 4-cycles, on Boolean 2-by-2 Port grids:

- `A = {02,03,12,13}`, coordinates `(i,j)` where i in {0,1}, j in {2,3}.
- `B = {04,05,14,15}`, coordinates `(i,k)` where i in {0,1}, k in {4,5}.
- `C = {24,25,34,35}`, coordinates `(j,k)` where j in {2,3}, k in {4,5}.

Normalize each coordinate to 0 or 1. The forced-edge boundary space `F` is the direct sum of three 4-vertex even-subset spaces, hence dimension 9 and cardinality **512**.

An even subset of a grid has size 0,2, or4. A size-2 subset is a **line** when its points agree on one coordinate, and a **diagonal** otherwise. A line has a fixed coordinate and its value, and a variable coordinate. The parity label of a diagonal is `delta = first_bit XOR second_bit` for either of its two points.

## Theorem KJ.1 — Geometric 47-hole criterion

For any forced boundary `b` in `F`, the eight-singleton-flexible inventory has a full Euler realization **if and only if** `b` avoids the following four families:

1. **At least two full grids.** If exactly two grids contain all four Ports, the third is a doubleton; or all three grids are full. Number of boundaries: `18+1=19`.
2. **Exactly one full grid, and two aligned lines.** If A is full, B and C are lines varying their shared k coordinate. If B is full, A and C vary their shared j coordinate. If C is full, A and B vary their shared i coordinate. Number: `3*2*2=12`.
3. **Three diagonal doubletons with inconsistent cycle parity.** All A,B,C are diagonals and `delta_A XOR delta_B XOR delta_C = 1`. Number: `4`.
4. **One diagonal and two aligned lines with the same fixed shared-coordinate value.** Either (A and B vary second coordinates with equal fixed i, C diagonal), or (A varies first and C second with equal fixed j, B diagonal), or (B and C vary first with equal fixed k, A diagonal). Number: `3*2*2=12`.

Thus there are exactly **47** inaccessible forced boundaries, by disjoint families. Their sorted grid-weight profiles are
`(2,2,2):16; (2,2,4):12; (2,4,4):18; (4,4,4):1`.
Every other member of the 512-element forced boundary space, including every profile with an empty grid, is attainable.

### Exact finite proof

Each of the eight flexible supports corresponds to one vertex of the binary 3-cube and has precisely three legal intercomponent edge choices of types AB,AC,BC. Selecting one edge in each of the eight supports yields exactly `3^8 = 6561` choices. The XOR of endpoint bits computes the twelve-Port flexible degree boundary. The full graph is connected exactly when at least two different intercomponent edge types occur, because the twelve forced edges connect each of the three four-Port components internally.

The accompanying standard-library checker directly enumerates all 6561 choices and intersects their connected boundary set with the exact 512-element forced boundary space. It **independently** computes the four-family geometric predicate on all 512 boundary vectors and asserts equality with the exhaustive missing set. Both have size 47. All operations are exact integers; no sampling or floating-point approximation occurs.

The positive forced multiplicities affect only the parity of their fixed edge boundaries; their edges remain present, so the same complete condition holds for all positive forced counts. This is a finite computational proof with a small explicitly enumerable domain. A nonenumerative sufficiency derivation is still open.

## Theorem KJ.2 — Incidence of the 28 two-upgrade affine obstruction planes

For `U` one of the 28 pairs of flexible supports, let `E_U` be R762KI's four-point affine obstruction set when those two supports instead have counts at least two. Define `m(b)=#{U: b in E_U}` for one of the 47 zero-upgrade holes. Then `m(b)` depends **only on the sorted grid weights**:

| Grid weights | Hole count | m(b) | Incidences |
|---|---:|---:|---:|
| (2,2,2) | 16 | 1 | 16 |
| (2,2,4) | 12 | 1 | 12 |
| (2,4,4) | 18 | 4 | 72 |
| (4,4,4) | 1 | 12 | 12 |
| **Total** | **47** | — | **112=28×4** |

More strongly, a pair `U` at cube **Hamming distance 1** has an obstruction plane with weight profile `{(2,2,4):1, (2,4,4):2, (4,4,4):1}`. A pair at distance **2 or 3** has `{(2,2,2):1, (2,4,4):3}`. The three pair-distance classes contain respectively 12,12,4 pairs.

The checker recomputes each four-point `E_U` by GF(2) reachable-boundary propagation for the minimum counts 1/2. It asserts its XOR is zero, its union is exactly the 47-hole set, every distance-specific plane profile is correct and each point's membership multiplicity has the tabulated value. This incidence theorem strengthens KI's description of *how* the affine planes overlap; it does not independently re-prove KI's arbitrary-flexible-multiplicity extension.

## Reproduction, next question and evidence level

Run `python R762KJ_GEOMETRIC_OBSTRUCTION_VERIFY.py` in the same directory. Checks: 6561 direct flexible choices, 512 target boundaries, four structural families, 28 upgraded affine planes, their 12/12/4 distance types and all membership multiplicities. Result: all assertions passed, zero failures in local execution. Paper and checker are author-originating; independent mathematical review remains `NOT_REVIEWED`.

**Next:** Derive a nonenumerative cube-flow or Fourier-character proof of the 47-hole predicate; then obtain a direct formula for a given `E_U` without performing a state enumeration. Test whether analogous short predicates exist with one or two inactive Ports. A signed P000/BRC lifting theorem needs separately proved order, branch and residual preservation.
