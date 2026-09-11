# Nollm dyadic-tail Q40 physical matching: identity capacity succeeds, two-step ×2 locality fails

Date: 2026-09-11  
Status: `RESEARCH_NOTE / FINITE_CERTIFICATE / NOT_FOUNDATION / NOT_RUNTIME_CHANGE`  
Research activity: `RA-nollm-multiplication-field-20260911-c6c82`

## Question

Continue the exact frontier from `nollm_hierarchical_dyadic_tail_20260911.md`: replace the Gray tail as auxiliary metadata by actual Nollm physical descendants. For the finite population

\[
1\le n<2^{16},\qquad b=8,
\]

use the published 96-sample Q40 `coverage_down` support and ask:

1. can every Gray-tail prefix be assigned injectively to one real physical descendant when one tail bit consumes two adjacent physical layer intervals?;
2. if identity capacity succeeds, do the arithmetic generators ×2 and ×5 remain local?;
3. if ×2 is imposed as a simultaneous physical-support constraint, what minimum tested coverage depth is locally feasible?

The previous multiplication-field lab was already published at commit `2cd3c7e320dbab68b4afc498a5f83273a078c431`; this note does not republish or overwrite it.

## BRC / carrier discipline

Population: all positive integers below `2^16`. Canonical identity remains the integer `n`, equivalently the complete hierarchical carrier `(base_cell,d,Gray-tail)` already verified in the predecessor note. Tail-prefix identity is never replaced by a count or total occupancy.

Serial composition: refine one Gray-tail bit at a time. Observer: exact Boolean support of the frozen Q40 `coverage_down` kernel; Q16 weights are not needed for this capacity question. Output: an injective child-prefix → physical-cell assignment at each physical depth. Future operations explicitly tested here are ×2 and ×5.

`REUSE_EXECUTED`: the existing dyadic annulus carrier and frozen Q40 transformation constants. `COMPOSE_APPLIED`: prefix identity is combined with real Q40 support before any geometric distance summary. Multi-to-one geometric candidates retain labeled child identities until matching. This is a finite certificate, not an infinite-scale theorem.

## 1. Two intervals per tail bit are enough for identity capacity on the full finite population

At tail level `k`, a left node is

\[
(\text{base cell},\; g(q)\bmod 2^k),
\]

and its structural parent is the same base cell with the lower `k-1` Gray prefix. The candidate right cells are all exact physical cells in the parent's two-step `coverage_down` support. Right-cell capacity is one.

Levels 1–5 admit deterministic complete bipartite matchings. Level 6 was harder computationally but not capacity-obstructed: there are 32,768 child prefixes and 59,830 available candidate cells. A scarcity-first greedy assignment placed 32,765 children; the remaining 3 were repaired by exact alternating augmenting paths, giving

\[
32768/32768
\]

matched at level 6.

Combining all levels gives exactly 65,535 distinct physical entries when the physical interval depth `2d` is part of the entry key. The depth histogram is

```text
0:  1,023
1:  1,024
2:  2,048
3:  4,096
4:  8,192
5: 16,384
6: 32,768
```

Thus, for this finite `L=16,b=8` population, the hierarchical repair coordinate can be geometrized without identity collisions using two real `coverage_down` intervals per Gray-tail bit.

This proves only existence for the stated finite population and frozen Q40 support. It does not prove a uniform Hall bound for unbounded `L`.

## 2. An arbitrary identity-perfect matching destroys arithmetic locality

Identity capacity is not enough.

For the deterministic complete placement obtained in the run:

- ×5 has 13,107 same-depth pairs. Hex-distance median is 10, p95 is 23, p99 is 29, and the maximum is 52.
- only 2,395 / 13,107 ×5 pairs lie within distance 4;
- ×2 has 511 same-depth pairs and all have distance exactly 2;
- ×2 has 32,256 depth-drop pairs, but only 437 source entries lie in the exact two-step `coverage_down` support of the physical entry representing `2n`:

\[
437/32256\approx 0.0135478671.
\]

So

\[
\text{injective physical identity embedding}
\not\Rightarrow
\text{generator-local physical embedding}.
\]

The next matching problem must therefore include arithmetic relations during placement, not audit them only afterwards.

## 3. Exact two-step ×2 + structural refinement is locally impossible already at tail level 1

For each level-1 child prefix `u`, require its physical cell to belong simultaneously to

1. the two-step `coverage_down` support of its structural Gray-prefix parent; and
2. the two-step support of the prefix determined by the exact arithmetic map `n -> 2n`.

The prefix target is well-defined on the finite population: every source prefix maps to one target prefix.

There are 5,396 level-1 child prefixes carrying an ×2 constraint. For 402 of them the two candidate supports are disjoint:

\[
S_2(Pu)\cap S_2(Fu)=\varnothing.
\]

Therefore no matching algorithm, greedy or exact, can satisfy both requirements with only two `coverage_down` intervals in these cases.

Those 402 prefix witnesses reduce to 236 distinct base-cell pairs; 166 pairs occur twice and 70 once. Every empty base-pair displacement is one of exactly six straight hex-distance-2 directions:

```text
( 0,-2): 47 distinct pairs
( 0, 2): 47
(-2, 0): 38
( 2, 0): 38
(-2, 2): 33
( 2,-2): 33
```

No empty pair in this finite base population occurs in the other distance-2 orientations. The obstruction is therefore directional/phase-specific for this Q40 refinement, not merely “hex distance 2 is too far.”

## 4. Three intervals remove the first-level empty-support obstruction, but independent level matching is not future-safe

Using equal-depth descendant supports from both parents:

| repeated `coverage_down` steps | constrained level-1 prefixes | empty common-descendant sets |
|---:|---:|---:|
| 1 | 5,396 | 5,092 |
| 2 | 5,396 | 402 |
| 3 | 5,396 | **0** |

At 3 steps the minimum common-support size is 2 in the recorded run, so a complete level-1 relation-aware matching exists; the deterministic scarcity-first assignment matched all 6,144 level-1 children.

However, if that valid current-level placement is frozen and the same three-step rule is applied at level 2, 5,439 of the 10,240 level-2 child prefixes have empty structural/×2 candidate intersections. Hence

\[
\text{perfect at level }k
\not\Rightarrow
\text{extendable to level }k+1.
\]

This turns the next problem into a coupled cross-level constraint-satisfaction / matching problem rather than independent Hall tests at each level.

A local free-cell hill-climb from one valid level-1 placement reduced the weighted level-2 empty count from 5,439 to 1,968 after 2,128 moves, but did not reach zero. This is a heuristic improvement only; it is neither a proof of feasibility nor impossibility.

## 5. Small local structure exists inside the future constraint graph

For the level-1 placement problem induced by level-2 structural/×2 relations, the abstract relation graph on the 6,144 level-1 prefix nodes splits into 1,024 small connected components of size 5–7, with node degree at most 2 in that relation graph. Candidate physical cells, however, are shared across many such components, so the global all-different constraint couples them again.

This suggests that future-aware search should exploit the small arithmetic components while coordinating candidate-cell capacity globally, rather than solve one giant undifferentiated matching.

## 6. Coding-level no-go: cyclic one-bit +1 locality and exact nested truncation cannot coexist

Consider any family of bijections

\[
g_d:\mathbb Z/2^d\mathbb Z\to\{0,1\}^d.
\]

Suppose both hold:

1. **cyclic one-bit increment:** `g_d(q)` and `g_d(q+1 mod 2^d)` differ in exactly one bit for every `q`;
2. **exact nested truncation:** deleting one fixed coordinate from `g_d(q)` always gives `g_{d-1}(q mod 2^{d-1})`.

Then the projected lower code changes exactly one bit on every increment because `g_{d-1}` is itself cyclic Gray. Since the full code is also allowed exactly one changed bit, the deleted coordinate cannot change on any cycle edge. It is therefore constant around the entire cycle, contradicting bijectivity, because the two lifts of each lower state must be distinguished.

Therefore these two requirements are incompatible.

This explains why a Gray encoding optimized for ×5 (`q -> q+1`) cannot simultaneously make a precision drop an exact delete-one-bit tree operation. It is only a coding-level obstruction. It does **not** by itself explain all physical ×2 failures, because the dyadic annulus base cell also changes under ×2.

## Status and smallest unresolved unit

Established for the exact finite `L=16,b=8` population and the frozen Q40 96-sample kernel:

- `PASS`: two real `coverage_down` intervals per Gray bit have enough finite capacity for a fully injective 65,535-identity physical embedding;
- `FAIL`: arbitrary identity-perfect matching preserves ×5/×2 locality;
- `NO-GO WITNESS`: two-step structural + exact ×2 locality has 402 empty level-1 candidate sets;
- `PASS`: three steps eliminate those first-level empty sets;
- `UNRESOLVED`: a globally future-safe three-step hierarchy satisfying injection plus ×2 relation constraints across all levels.

The next exact unit is to solve or falsify that coupled hierarchy. A second route worth comparing is whether the existing Nollm Bridge mechanism should carry the arithmetic relation rather than force both identities into a common local `coverage_down` descendant. That comparison must use the current Bridge contract and must not introduce a graph index or violate one-entry/one-Cell semantics.

## Reproduction

The accompanying `verify.py` exposes three modes so the large finite checks can be rerun independently:

```sh
python verify.py --mode identity --out identity.json
python verify.py --mode boundary --out boundary.json
python verify.py --mode future --out future.json
```

`boundary` and `future` are short runs; the full six-level identity solve is intentionally heavier. `results.json` records the executed finite certificates used by this note. Timing values are diagnostic only and are not mathematical claims.
