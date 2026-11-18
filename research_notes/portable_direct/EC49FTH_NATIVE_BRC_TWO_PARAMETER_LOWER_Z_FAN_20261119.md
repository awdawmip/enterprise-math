# EC49FTH — Exact lower-z BRC16943 two-price fan

Date: 2026-11-19. Status: **AUTHOR_PROVED / EXACT_RATIONAL / INDEPENDENT_PARTIAL / NOT_REVIEWED**. Predecessor: [EC49FTG PR #2766](https://github.com/awdawmip/enterprise-math/pull/2766). Frozen native scientific input: `awdawmip/enterprise-math@fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. The identification problem retains all 310 native configurations, 141 separately named response profiles, and all 228 original physical observations without quotienting. P000/ACTIVE worldview unchanged.

## Unrestricted optimal prices on a continuous rectangle

Fix q32 discount `a=3/4`; vary q34 discount `7/16 ≤ b ≤ 57/128` and q140 discount `11/16 ≤ z ≤ 3/4`. Other observations retain unit baseline `t`. Let `F=141V/t` equal the sum of observer prices on all 141 named identification paths. For a complete original-index decision tree with usage counts `(U,N32,N34,N140)`, original-pricing cost is `U-a*N32-b*N34-z*N140`; swapped-pricing cost exchanges the q32/q34 discounts.

**Theorem:** For every real `(b,z)` in this entire closed rectangle, the unrestricted native Bellman optima satisfy

```
D(b,z) = min(
  326 - 141*a - 47*b -  43*z,  # D43
  334 - 141*a - 62*b -  45*z,  # D45
  329 -  36*a - 68*b - 141*z   # Dmid
)
S(b,z) = 332 - 141*a - 8*b - 105*z;  # S105
a = 3/4 throughout
```

The switching boundaries are `z_43_45=(8-15b)/2` and `z_45_mid=(295-24b)/384`. The former meets the lower edge `z=11/16` at `b=53/120`; the latter meets the two vertical edges at `569/768` and `4549/6144`. D43, D45, Dmid have respectively triangular (3 vertices), pentagonal (5 vertices), and quadrilateral (4 vertices) full-dimensional optimality cells; their union has eight distinct direct-pricing vertices. The D43/Dmid equality does not form an exposed full-dimensional interface because D45 lies below them there. The swapped-pricing tree S105 is optimal everywhere in this rectangle.

The sharp and attained exchange-price gap bounds are

```
1229/64 ≤ D-S ≤ 1461/64.
```

The minimum is at `(b,z)=(57/128,11/16)`; maximum at `(7/16,569/768)`. The three direct-pricing cells have gap formulas respectively `-6-39b+62z`, `2-54b+60z`, `303/4-60b-36z`.

## Proof

1. **Feasibility**: Four full original-observer-index identification trees have usage vectors `D43=(326,141,47,43)`, `D45=(334,141,62,45)`, `Dmid=(329,36,68,141)`, `S105=(332,8,141,105)`. The D43 tree is newly exposed; the other three are inherited from EC49FTG. Replay over every one of 141 separately named source profiles confirms the exact correct leaf, with no repeated observer per profile path and all observer indices in 0..227. Thus these are four globally feasible affine upper bounds.
2. **Finite exact lower bounds**: Exact rational half-space intersection gives eight distinct direct-pricing optimality-cell vertices. The full unrestricted Bellman recursion over 228 native observations has been evaluated and matches the claimed D envelope at all eight vertices. The four corners of the swapped-pricing rectangle match S105. All 12 exact anchor coordinates and values are in the companion JSON; 4 selected points were also independently cross-checked with a raw-94-family observer reconstruction and separate exact Bellman code. The computational statement is confined to the fully enumerated finite 141-state/228-observer model.
3. **All real parameters**: The unrestricted optimum is the infimum of affine costs of feasible complete trees, hence is jointly concave in `(b,z)`. On each convex direct-pricing cell a complete feasible tree has affine cost `L` equal to the exact unrestricted Bellman optimum at all vertices `v_i`. For `p=Σλ_i v_i`, concavity gives `Bellman(p)≥Σλ_i Bellman(v_i)=L(p)`; feasibility gives `Bellman(p)≤L(p)`. Equality therefore holds throughout each cell, including irrational points and boundary ties. Four-corner concavity proves S105 on the full rectangle. As D-S is affine on each cell, evaluating its cell vertices yields the attained sharp gap bounds.

## Evidence, limitations, next problem

Frozen source SHA256: `frozen_original_master.txt=cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e`, `EC49FPG_PROFILE.csv=a61a3ee4d2f13f9d216f52cd3529c72d395c1250bfb1d7ae96a1adf5a6837c1f`. Evidence: 12/12 exact rational primary anchor observations (including inherited exact checks at prior frontier), 4/4 additional independent raw-94 checks, 4/4 complete native tree path replays. The companion certificate gives every anchor and cell vertex. A self-contained source/tree/code/log archive is retained as `EC49FTH_EXACT_NATIVE_BRC_2D_LOWER_PRICE_FAN_20261119.tar.xz` with the original 228-observer source and all four trees. The supplied verifier checks source hashes, original-index tree paths, rational geometry and optional full native Bellman reruns. Exact work is author-side, **not independently mathematically reviewed** and not formally admitted.

**Next:** Below `z=11/16`, search for the next native tree replacing D43 or S105; then allow `a` to vary around `3/4` to lift the current two-dimensional phases to a three-dimensional local region.

**Control:** Independent portable research only; no formal Task CLAIM, Activity checkpoint, Result, Review, Working Truth, or Foundation status claimed. Scientific pin remains frozen.
