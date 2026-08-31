# Native Enterprise typed incidence graph：complete finite-wheel connectivity classification

Status: `FREE_RESEARCH_EXACT_IFF_CLASSIFICATION / NOT_CANONICAL_FOUNDATION`

Date: `2026-08-23`

Researcher-ID: `EM-FREE-NEPS-239A6D`

Depends on:

- global typed-Cell seam prime-incidence no-go;
- mod-6 filament classification;
- mod-5 sharp-nine cut;
- all-q transparent-class theorem;
- finite-set CRT avoidance theorem.

## 1. Finite wheel graph

Let `M` be any positive squarefree integer with

`6 | M`.

On the fixed global typed-Cell elementary-incidence carrier, retain a Cell iff its integer label is coprime to M, and retain an elementary triangle iff all three Cell labels survive.

Call the resulting graph `G(M)`.

Only the prime support of M matters, so the squarefree assumption is merely normalization.

## 2. If 5 divides M, all components are uniformly finite

If `5|M`, then every Cell of `G(M)` is in particular coprime to 30.

Hence `G(M)` is a subgraph of the exact mod-30 eligibility graph.

The global typed-Cell sharp-nine theorem gives

`component_size <= 9`

for the mod-30 graph. Deleting additional vertices/triangles cannot increase component size.

Therefore

`5|M -> every component of G(M) has size <=9`.

## 3. If 5 does not divide M, an unbounded component survives

Assume `5` does not divide `M`.

Write the prime support as

`{2,3} union S`,

where every prime in finite S is at least 7.

For every `q in S`, the exact transparent-class theorem gives at least one residue `h_q mod q` such that the entire sigma-1 filament of transverse class h_q contains no q-divisible Cell.

By CRT choose h satisfying

`h=4 mod6`

and

`h=h_q mod q` for every `q in S`.

The constant-h sigma-1 filament is mod-6 eligible and simultaneously avoids every q in S. Hence every Cell on the infinite filament is coprime to M, and all rolling incidence triangles survive.

Thus `G(M)` has an unbounded connected component.

Therefore

`5 not divide M -> G(M) has an unbounded component`.

## 4. Exact iff theorem

Combining both directions:

`ALL COMPONENTS OF G(M) ARE UNIFORMLY FINITE  <=>  5 | M`,

for every finite squarefree wheel M with `6|M`.

Moreover, whenever `5|M`, the universal component bound is at most 9.

For `M=30` the bound 9 is sharp, and the actual prime graph itself also realizes a nine-Cell island.

## 5. Interpretation

The native incidence geometry turns divisibility by 5 into a deterministic percolation threshold for the entire family of finite arithmetic wheels containing 2 and 3.

Later prime channels may change densities and which individual islands survive, but no finite collection of them can substitute for the 5-channel in destroying long-range connectivity.

## 6. Prior-art boundary

Deterministic percolation and prime percolation are classical research topics (e.g. Vardi). This file does not claim novelty for deterministic percolation as a concept.

The research-specific object is the exact iff classification for this frozen typed Enterprise incidence graph and integer allocation.
