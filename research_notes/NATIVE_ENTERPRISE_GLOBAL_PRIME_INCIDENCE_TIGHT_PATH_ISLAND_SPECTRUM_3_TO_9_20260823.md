# Native Enterprise global prime-incidence hypergraph：tight-path island spectrum 3 through 9

Status: `FREE_RESEARCH_EXACT_GLOBAL_TOPOLOGY_CLASSIFICATION / NOT_CANONICAL_FOUNDATION`

Date: `2026-08-23`

Researcher-ID: `EM-FREE-NEPS-239A6D`

Depends on:

- typed-Cell lift of the tri-sector allocation;
- global seam fully-prime-incidence no-go;
- global sharp-nine prime-incidence island theorem.

## 1. Hypergraph object

Take the complete typed-Cell carrier. A vertex of the hypergraph is a typed circle Cell whose assigned integer is prime. A 3-uniform hyperedge is one elementary carrier triangle whose three Cell labels are all prime.

Connected components of this hypergraph are called prime-incidence islands.

## 2. No branching

The exact mod-6 classification has three sector slots.

### Slots sigma=0 and sigma=2

Eligible elementary triangles occur only as isolated triangles or as one paired A/B pair sharing exactly two prime Cells. Hence every component is either

- one 3-Cell hyperedge; or
- two 3-Cell hyperedges sharing two Cells, giving a 4-Cell tight path.

No third eligible triangle can continue the component.

### Slot sigma=1

Every long eligible triangle belongs to a constant-h zigzag filament

`C_r,C_{r+1},C_{r+2}`

with consecutive r. The next eligible hyperedge, if fully prime, is

`C_{r+1},C_{r+2},C_{r+3}`.

Thus consecutive hyperedges overlap in exactly two Cells. There is no second branch direction.

### Sector seams

No fully-prime elementary incidence triangle crosses a typed-sector seam, so separate sector paths cannot reconnect globally.

Therefore every nonempty global prime-incidence component is a **3-uniform tight path**.

## 3. Component size and incidence-vertex count

A tight path on k Cell vertices has exactly

`k-2`

triple-prime coordinate-vertex hyperedges.

The global sharp-nine theorem gives

`3 <= k <= 9`.

Hence the only possible nonempty component sizes are contained in

`{3,4,5,6,7,8,9}`.

## 4. Every allowed size is realized by actual primes

Deterministic finite searches plus the sharp-nine packet give explicit witnesses for every size.

### k=3

Prime Cells:

`37,53,73`.

One triple-prime incidence hyperedge.

### k=4

Prime Cells:

`17,29,43,61`.

The two hyperedges are

`(17,29,43)` and `(29,43,61)`.

### k=5

Prime Cells:

`3767,3919,4073,4231,4391`.

This is a sigma-1 constant-h chain beginning at legacy Cell layer `r=50`, with `h=16`.

### k=6

Prime Cells:

`63611,64231,64853,65479,66107,66739`.

Constant-h chain beginning at `r=206`, `h=-44`.

### k=7

Prime Cells:

`363269,364747,366227,367711,369197,370687,372179`.

Constant-h chain beginning at `r=492`, `h=172`.

### k=8

Prime Cells:

`1370471,1373341,1376213,1379089,1381967,1384849,1387733,1390621`.

Constant-h chain beginning at `r=956`, `h=-434`.

### k=9

Prime Cells:

`171283421,171315481,171347543,171379609,171411677,171443749,171475823,171507901,171539981`.

Constant-h chain beginning at `r=10686`, `h=-2474`.

All displayed values have been checked prime in the corresponding deterministic research checkers; the largest sharp packet was independently checked by direct trial division through square roots.

## 5. Exact island spectrum

Since every size 3 through 9 is realized and no size above 9 is possible:

`GLOBAL NONEMPTY PRIME-INCIDENCE ISLAND SIZE SPECTRUM = {3,4,5,6,7,8,9}`.

Equivalently the dual coordinate-vertex path lengths are exactly

`{1,2,3,4,5,6,7}`.

There are no branching prime-incidence trees, cycles, or two-dimensional prime meshes in this hypergraph.

## 6. Extremal collapse hierarchy

For the sharp k=9 island, taking consecutive odd-width rolling windows gives the natural incidence hierarchy

- 9 prime Cells;
- 7 triple-prime coordinate vertices (width 3 windows);
- 5 maximal five-prime flowers (width 5 windows);
- 3 width-7 overlapping packets;
- 1 width-9 extremal island.

Hence the extremal native object carries the canonical nested count pattern

`9 -> 7 -> 5 -> 3 -> 1`.

This hierarchy is combinatorial once the sharp island is fixed; the prime-specific theorem is that the top size is exactly 9 and is attained.

## 7. Interpretation

The prime distribution in the frozen native typed-Cell coordinates is not a percolating two-dimensional mesh. Its complete triple-incidence topology is a finite path-island spectrum with seven possible sizes.

This is a stronger statement than prime density or visual line enrichment: it classifies every connected shape allowed by the prime-incidence relation.

## 8. Boundary

The result is exact for this typed Enterprise integer allocation and incidence carrier. It is not promoted to canonical foundation and no external novelty claim is made without a dedicated prior-art review.
