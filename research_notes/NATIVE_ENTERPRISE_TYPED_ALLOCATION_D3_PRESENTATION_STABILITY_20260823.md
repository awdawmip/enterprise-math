# Native Enterprise typed-Cell allocation：D3 presentation stability of prime-incidence connectivity

Status: `FREE_RESEARCH_EXACT_PRESENTATION_EQUIVARIANCE / NOT_CANONICAL_FOUNDATION`

Date: `2026-08-23`

Researcher-ID: `EM-FREE-NEPS-239A6D`

## 1. Presentation family

The typed Cell allocation has two harmless presentation choices:

1. which of the three cyclic sector charts is assigned numeric block 0;
2. which direction is called increasing side coordinate t inside every sector.

This gives `C3 x C2`, equivalently the six presentations of the dihedral symmetry of the tri-sector carrier.

For typed shell s the forward label is

`N(s,t,sigma)=B_s^C+t+block(sigma)*(s+1)`.

Global reversal replaces

`t -> s-t`.

## 2. Cyclic relabeling

Changing the first sector block cyclically is carried by the native C3 rotation of the three typed sector charts.

The carrier elementary-triangle incidence relation is C3-equivariant, so the corresponding labeled incidence graphs are isomorphic after rotating physical sector identities.

Hence any graph property that does not privilege a named sector is unchanged, including:

- existence/nonexistence of cross-sector fully-prime incidence;
- component-size spectrum;
- bounded/unbounded connectivity class;
- sharp maximum component size.

## 3. Global orientation reversal

Reversing the side coordinate in all three sectors is the reflected carrier presentation.

It exchanges the two elementary triangle orientations A/B and reverses local chirality, but preserves the unordered elementary incidence hypergraph.

The seam consecutive-pair no-go remains valid after reflection, and the mod-6 / mod-5 filament analysis is transported to the reflected transverse coordinate.

Thus the reversed graph is again isomorphic at the level relevant to connectivity.

## 4. Six-presentation exact replay

An independent global carrier checker replayed all six combinations

`3 cyclic starts x 2 side orientations`

through typed shell `s<=180`.

For every presentation:

- fully mod-6-eligible cross-sector seam triangles: `0`;
- maximum mod-30 eligibility component size: `9`.

This finite replay is a regression check for the exact equivariance argument, not its proof.

## 5. Consequence

The strongest connectivity statements are presentation-stable:

- long mod-6 connectivity collapses to one-dimensional filaments;
- inclusion of prime 5 cuts every filament;
- global mod-30 component size is at most 9;
- the actual prime graph realizes a nine-Cell island.

Freeze:

`SHARP NINE + PRIME-5 CONNECTIVITY BREAK = D3 PRESENTATION-STABLE`.

The sign of local curvature chirality remains presentation-equivariant rather than absolute, as already corrected in the curvature notes.
