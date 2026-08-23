# Native Enterprise prime-incidence loop code: exact 13-state local holonomy

Status: `FREE_RESEARCH_EXACT_LOOP_CODE / FINITE_CENSUS / NOT_CANONICAL_FOUNDATION`

Date: `2026-08-23`

Researcher-ID: `EM-FREE-NEPS-239A6D`

Parent: `NATIVE_ENTERPRISE_TRIPLE_CELL_INCIDENCE_CRT_TOWER_2D_19D_20260823.md`

## 1. Native loop

In the triangular cell-center carrier, the coordinate vertices are the elementary center triangles. The dual incidence graph is hexagonal: exactly six triple-cell coordinate vertices surround each interior cell center.

For local sector coordinates `(u,v)` the cyclicly ordered six incidence faces around the center are

1. `A(u,v)`;
2. `B(u,v)`;
3. `A(u-1,v)`;
4. `B(u-1,v-1)`;
5. `A(u-1,v-1)`;
6. `B(u,v-1)`.

Adjacent faces share the center cell and one neighboring cell.

Define a loop bit to be 1 iff all three cells of that incidence face carry prime integer labels. The six bits form the **prime-incidence loop signature**.

This uses only cell incidence/gluing. No Euclidean carrier metric is used as a native length.

## 2. Neighbor representation

Let the center label be `n`, shell index `r`, and sector slot `sigma`.

The six neighboring cell labels around the center, in cyclic order, are

- `E  = n+3r+sigma`;
- `NE = n+6r+4+2sigma`;
- `N  = n+3r+1+sigma`;
- `W  = n-3r+3-sigma`;
- `SW = n-6r+8-2sigma`;
- `S  = n-3r+2-sigma`.

The six incidence bits are exactly the six edge-ANDs on this neighbor cycle:

`(E*NE, NE*N, N*W, W*SW, SW*S, S*E)`

where each neighbor variable denotes its prime-indicator bit and the center must itself be prime for any loop bit to be 1.

## 3. Mod-6 eligibility upper masks

Assume the center is a prime greater than 3. Then `n mod 6` is `1` or `5`.

Enumerating only the finite intrinsic residue data

`(sigma in C3, r mod 6, n mod 6 in {1,5})`

shows that prime eligibility of the six neighbors allows only the following ten maximal face masks:

`000000`,

`000010`, `000100`, `010000`, `100000`,

`000011`, `001100`, `011000`, `100001`,

`011100`, `100011`.

A realized prime loop may be a submask because a residue-eligible neighbor can still be composite.

## 4. Shared-neighbor closure removes two apparent submasks

Taking arbitrary submasks of the residue upper masks would nominally allow 15 signatures. Two of them are impossible by incidence gluing alone:

`010100` and `100010`.

Reason: loop bits are edge-ANDs on one six-cycle. If the two separated displayed edges in either pattern are bright, the shared intermediate neighbor cells are both prime, which forces the intervening edge to be bright as well.

Thus the exact nonexceptional loop-code state set has **13 states**:

`000000`,

six singleton states:

`000001, 000010, 000100, 001000, 010000, 100000`,

four double states:

`000011, 001100, 011000, 100001`,

and two triple states:

`011100, 100011`.

No loop with four, five or six bright coordinate vertices is possible.

Freeze:

`PRIME_INCIDENCE_LOOP_CODE_SIZE = 13`.

`MAX_FULL_PRIME_COORDINATE_VERTICES_AROUND_ONE_CELL = 3`.

## 5. The two maximal states

The only maximal-brightness loop signatures are

`011100` and `100011`.

They are complementary three-edge arcs under half-turn of the loop indexing.

Thus local prime brightness cannot wrap uniformly around a cell. Maximum brightness forms one of two oriented length-three arcs.

This is a genuine gluing restriction: it is not visible from the one-vertex incidence hexacode alone.

## 6. Exact finite census

Interior census:

- center shells through `r<=1500`;
- local active coordinates `u,v>=2` so all six incident coordinate vertices remain in one sector chart;
- all three sector slots;
- total center cells checked: `3,363,759`.

Observed signature counts:

- `000000`: 3,347,973;
- `000001`: 2,144;
- `000010`: 2,492;
- `000100`: 2,507;
- `001000`: 2,126;
- `010000`: 2,510;
- `100000`: 2,482;
- `000011`: 366;
- `001100`: 360;
- `011000`: 355;
- `100001`: 370;
- `011100`: 42;
- `100011`: 32.

All 13 theoretically allowed states occur. No forbidden state occurs.

By brightness count:

- 0 bright vertices: 3,347,973 centers;
- 1: 14,261;
- 2: 1,451;
- 3: 74;
- >=4: 0.

The large zero class includes composite centers, which necessarily have zero bright incidence vertices.

## 7. Why this is stronger than marginal residue regularity

The previous local code classified one coordinate vertex. This 13-state object uses the **gluing of six coordinate vertices around one cell**.

Its restriction combines two ingredients:

1. prime residue eligibility mod 6;
2. shared-cell incidence closure on the dual hexagonal loop.

Therefore it is a first exact observable that depends on how native incidence events compose, not only on a marginal residue state.

The arithmetic ingredients remain elementary and no novelty claim is made for prime congruences or binary cycle constraints separately.

## 8. Next hard test

The next step is to classify transition rules between neighboring 13-state cell loops and ask whether an elementary closed path of cells carries a nontrivial conserved or holonomy-like code after quotienting the obvious shared-prime constraints.

Only a residual not reducible to the underlying individual cell prime indicators should be treated as a genuinely new collapse invariant.
