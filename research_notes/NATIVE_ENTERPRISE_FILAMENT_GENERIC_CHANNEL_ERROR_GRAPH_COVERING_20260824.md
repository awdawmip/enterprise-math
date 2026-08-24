# Native Enterprise filament codes: generic-channel covering of the error graph

Status: `FREE_RESEARCH_EXACT_GRAPH_COVERING_TOWER / NOT_CANONICAL_FOUNDATION`

Date: `2026-08-24`

Researcher-ID: `EM-FREE-NEPS-239A6D`

Depends on:

- `NATIVE_ENTERPRISE_FILAMENT_PRIMORIAL_NEAREST_NEIGHBOR_ERROR_GRAPH_20260824.md`;
- `NATIVE_ENTERPRISE_FILAMENT_FINITE_QUOTIENT_CODE_CARDINALITY_TOWER_20260824.md`.

## 1. One generic channel step

Let

`M=6U`

be a primorial modulus and let q>3 be a new prime channel.  Set

`N=Mq=6Uq`.

Reduction modulo M gives a q^2-to-one code map

`C_k(N)->C_k(M)`.

This note classifies the same map on the minimum-distance error graphs.

## 2. Partner involutions commute with reduction

At modulus M the parity-layer partner maps are

`T_E^M(R,c)=(R+U,c)`,

`T_O^M(R,c)=(R+U,c+chi-3U)`.

At modulus N they are

`T_E^N(R,c)=(R+Uq,c)`,

`T_O^N(R,c)=(R+Uq,c+chi-3Uq)`.

Because q is odd,

`Uq=U mod 2U`,

and

`3Uq=3U mod 6U`.

Therefore reduction intertwines both involutions:

`red(T_E^N x)=T_E^M(red x)`,

`red(T_O^N x)=T_O^M(red x)`.

So the downward code map is a graph morphism on nearest-neighbor edges.

## 3. Odd code length

For odd k the nearest graph is a perfect matching.

Every base vertex has q^2 lifts, and the lifted `T_E` involution pairs them compatibly.  Hence every base matching edge has exactly

`q^2`

matching edges above it.

The generic channel acts as a trivial q^2-fold lift at the nearest-neighbor level.

## 4. Even code length

For even k:

- the base graph contains `M/3` cycles of length M;
- the high graph contains `N/3=Mq/3` cycles of length N=Mq.

Since the involutions commute with reduction, each high cycle maps into one base cycle.

The two-edge cycle advance at modulus N translates c by

`-(3Uq+chi)`.

Modulo M this is

`-(3U+chi)`,

which is exactly the base two-edge advance.

Therefore a high cycle of length Mq maps onto its base M-cycle with covering degree

`q`.

## 5. q by q decomposition

The number of high cycles divided by the number of base cycles is

`(Mq/3)/(M/3)=q`.

Thus over every base cycle there are exactly

`q`

distinct high cycles, and each wraps q times around the base.

Freeze:

`ONE GENERIC PRIME CHANNEL q`

`= q TRANSVERSE CYCLE LIFTS`

`x q LONGITUDINAL COVERING DEGREE`.

The product is the exact q^2 code-fiber multiplicity.

## 6. Iterated tower

For dimensions `d>=3`, each new prime `p_d` applies the same operation.

Starting from one error cycle at a lower dimension, a sequence of channels

`q_1,...,q_m`

creates

`product q_i`

parallel cycles, each with total covering degree

`product q_i`.

Thus the algebraic two-degree lift per channel becomes an exact graph-covering square:

`TRANSVERSE MULTIPLICITY = LONGITUDINAL DEGREE`.

## 7. Downward collapse

The reverse map collapses

- q parallel high cycles into one base cycle;
- q consecutive turns of each high cycle into one base turn.

This is a concrete high-dimensional downward-collapse mechanism generated without orthogonal spatial axes.

## 8. Prime-valued boundary

The graph covering concerns the full native quotient code.  Actual prime-island packets occupy a sparse subset of its vertices, and no uniformity of that subset across covering fibers is asserted here.

## 9. Boundary

Graph coverings are classical.  The research-specific result is the exact q-by-q realization of the native generic-channel lift on the primorial nearest-neighbor error geometry.
