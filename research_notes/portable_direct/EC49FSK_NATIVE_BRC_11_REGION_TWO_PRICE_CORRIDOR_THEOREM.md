# EC49FSK — Exact native BRC 11-region continuous price corridor

Date: 2026-11-18 · Science pin: `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab` · Status: AUTHOR_PROVED / EXACT_FINITE_CROSSCHECKED / NOT_REVIEWED.

## Statement
Use the original BRC16943 population: 310 raw configurations inducing 141 distinct *named joint profile* states, all 228 unmodified physical named observations and their response partitions, a uniform prior over those 141 profiles, and complete deterministic adaptive identification trees. This is an observer/readout computation in the existing project P000/Heartbeat World X6 setting; no separate native spatial ontology is introduced.

For all real `7/16 ≤ α ≤ 1/2`, `0 ≤ z ≤ 1`, and `t>0`, observations q32/q34 each cost `(1−α)t`, q140 costs `(1−z)t`, and all other named observations cost `t`. The optimum `V(α,z)` over **all** complete native identification trees satisfies

```
141 V(α,z)/t = min_{(U,Q,K)∈P} (U − Q α − K z),
P = {
 (303,173,17), (304,169,32), (305,173,29),
 (306,182,10), (309,169,46), (311,151,69),
 (311,169,51), (319,93,141), (308,182,22),
 (312,186,31), (315,151,77)
}.
```

Each triple is achieved by a provided full 141-profile native decision tree. Its components count total observation calls `U`, combined q32/q34 calls `Q`, and q140 calls `K`. There are exactly **11 positive-area convex optimality regions**, requiring **11 distinct fixed-tree price cost types** to cover the entire rectangle. The region areas sum exactly to `1/16`, the rectangle area. There are **22 rational vertices** in the exact region decomposition.

## New internal crossing data

| α | z | exact 141V/t |
|---|---|---|
| 25/54 | 1/6 | 5942/27 |
| 14/29 | 1/2 | 11809/58 |
| 23/47 | 15/47 | 9921/47 |
| 117/238 | 5/14 | 49859/238 |

At `α=1/2`, the optimal z breakpoints are `0,1/6,3/14,1/4,11/30,2/5,1/2,33/64,1`, recovering the eight-segment half-price theorem. The left boundary `α=7/16` recovers the previously verified EC49FSJ eight-segment theorem.

## Exact global proof

Let `S` be a non-singleton subset of named profiles and `S_(q,r)` the subset that yields the original native physical observation q's response r. At a fixed rational parameter vertex, with exact dimensionless observation prices `p_q`, the nonaveraged Bellman recurrence is
`T(S)=min_{q strictly splits S} (|S| p_q + sum_r T(S_(q,r)))`, `T({i})=0`.
Because every admissible split strictly decreases the finite state subset, this recursion exhausts all complete adaptive native trees. Multiply by the price denominators to use integer arithmetic. The full 228-observer exact Bellman optimum was checked at **each of the 22** polygon vertices.

All 11 supplied witness trees were replayed against the original 228×141 named-response matrix: each of 141 profiles reaches its correct named leaf, no observer repeats along one path, and the integral call counts agree with the stated triples. Each witness therefore has exact affine cost `U−Qα−Kz`. Exact rational pairwise half-plane clipping of these 11 affine functions partitions the rectangle into the 11 listed strictly positive-area polygons; the vertex set has size 22 and area sum is `1/16`. The full Bellman value equals the witness envelope at all 22 vertices.

The Bellman value is the pointwise infimum of affine costs of all complete trees, so it is jointly concave. On each witness polygon it is bounded above by the feasible witness plane, and bounded below by affine interpolation of its coincident certified vertex values; the two bounds match identically on that polygon. This proves the formula for **all real** parameters in the rectangle, including boundaries. The 11 exposed open regions have pairwise distinct gradients `(-Q,-K)`, which proves the 11-type minimum.

Of the 22 vertices, the nine on `α=7/16` reuse the independently certified exact EC49FSJ boundary. The other 13 (four new interior vertices plus nine on `α=1/2`) were recomputed by a **separate original-family decoder plus independent exact all-228 Bellman solver**, with 13/13 agreement. Full trees, rational vertex values, exact region area data, and replay validation appear in the accompanying machine certificate and lossless tree payload; the self-contained local handoff package also contains the frozen raw source, code and execution logs.

## Boundaries and continuation

This is a finite-model theorem with the stated uniform prior, named observer set and price assumptions. Preserve all native joint responses, multiplicities, and provenance; no factor-only reduction is used. Independent human mathematical review and formal Task/CLAIM/Result/Review admission remain pending. The historical researcher identity and Activity are provenance, not current execution authority.

Source continuation: `awdawmip/enterprise-math` PR #2691, immutable commit `54324197c6566c5e3ac17b530b0b744f2b473400`. Current scientific computation uses the same frozen input bytes. Next: combine adjoining corridors into a stratified `α∈[1/4,1/2]` atlas; find exact bifurcations and then unfreeze the q32/q34 equality to approach the fully independent `(a,b,z)` three-price geometry.
