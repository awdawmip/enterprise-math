# EC49FTH appendix — exact native lower-z line through the 2D fan

Date: 2026-11-19. **AUTHOR_PROVED / EXACT_RATIONAL / INDEPENDENT_PARTIAL / NOT_REVIEWED**. This appendix is a disjoint additional claim, not a retroactive enlargement of the two-parameter rectangle in EC49FTH. Frozen science remains `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`, full 141 named profiles and all 228 original physical observers, with no P000 change.

Fix `a=3/4`, `b=7/16`, vary `5/8 ≤ z ≤ 3/4`. In units `F=141V/t`, unrestricted original and price-swapped Bellman minima are, for **all real z** in this interval,

```
D(z) = min(
  324-141a-47b-40z,    # D40: q140 usage 40
  326-141a-47b-43z,    # D43: q140 usage 43
  334-141a-62b-45z,    # D45: q140 usage 45
  329-36a-68b-141z     # Dmid: q140 usage 141
)
S(z) = min(
  324-141a-8b-93z,     # S93: 93 q140 paths
  332-141a-8b-105z     # S105: 105 q140 paths
)
```

The exposed direct-pricing switches occur **exactly** at `z=2/3`, `23/32`, and `569/768`. The swapped-pricing switch is `z=2/3`. At the lower endpoint `z=5/8`, additional distinct feasible full trees D30 with `(316,141,43,30)` and S82 with `(318,10,141,82)` tie for their respective global optima. Four distinct complete direct trees, two swapped trees and those extra boundary-tie trees were replayed on all 141 original named profile paths, preserving original observer indices.

The **sharp attained** price-swap gap range on this entire line is

```
257/16 ≤ D(z)-S(z) ≤ 1461/64.
```

The minimum occurs at `z=5/8` with exact Bellman `(D,S)=(2763/16,1253/8)`. The maximum occurs at `z=569/768` with `(D,S)=(42953/256,111327/768)`. The gap is continuous piecewise affine and its four sequential slopes are `53,62,60,-36`, so it increases to the final switching point and then decreases.

## Proof and computational scope

The four globally feasible original-pricing tree costs and two swapped-pricing costs give upper bounds everywhere. At the five exact direct-pricing endpoints `z∈{5/8,2/3,23/32,569/768,3/4}`, unrestricted all-228 rational Bellman equals the lower envelope. At the three swapped-pricing endpoints `z∈{5/8,2/3,3/4}`, unrestricted Bellman equals the corresponding S envelope. The exact values are:

| z | D (unrestricted) | S (unrestricted) |
|---|---|---|
| 5/8 | 2763/16 | 1253/8 |
| 2/3 | 8209/48 | 611/4 |
| 23/32 | 5401/32 | 4713/32 |
| 569/768 | 42953/256 | 111327/768 |
| 3/4 | 333/2 | 144 |

All five D and S entries in the table follow from source-backed primary exact calculations (earlier verified EC49FTG anchors reused at z=3/4, and EC49FTH evaluations elsewhere). Independent raw-94-derived Bellman additionally verified both orientations at z=5/8 and z=2/3. At z=2/3, a third S99 full tree is also optimal, illustrating a triple tie rather than an unproved uniqueness claim. Each candidate affine witness is optimal at the two endpoints of its stated segment. Bellman is concave as a minimum of feasible affine tree costs, so equality at the segment endpoints and the corresponding feasible witness proves equality at every real interior z. The slope analysis gives the sharp gap.

Reproducibility: the EC49FTH evidence archive includes frozen original arrays, an exact all-228 Bellman code, a separately decoded raw-94 Bellman implementation, decision trees and execution logs. Additional new original-index trees `D40,S93,D30,S82` and raw exact run outputs are included in the appendix evidence archive. The finite computation and continuous concavity proof apply only to the stated line; no separate mathematical reviewer or formal Result/Review is claimed.

**Next:** lift this lower-z line to a two-parameter polygonal neighborhood in `b`, especially the D40/D43 and S93/S105 simultaneous transition; then find the next original-index strategy below `z=5/8`.
