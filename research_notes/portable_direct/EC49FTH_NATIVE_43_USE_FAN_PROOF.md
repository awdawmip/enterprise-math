# EC49FTH — Original-index BRC16943 lower three-price fan (new 43-use q140 phase)

**Status:** AUTHOR_PROVED / EXACT_ALL228_PRIMARY_24_ANCHORS / INDEPENDENT_RAW94_2 / FOUR_FULL_TREES / NOT_REVIEWED.  
**Date:** 2026-11-19. **Predecessor:** [EC49FTG PR #2766](https://github.com/awdawmip/enterprise-math/pull/2766).  
**Frozen scientific source:** `awdawmip/enterprise-math@fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. This is the same native original-index BRC16943 identification model (310 original configurations, 141 separately named joint-response profiles, all 228 physical observations), not a new P000 model. No profile or observation quotient was introduced.

## Exact claim

Let `(a,b,z)` be discounts on the positive baseline prices for original physical queries q32, q34, q140. Other query prices stay at the baseline `t>0`. For a complete native identifying decision tree with use vector `(U,N32,N34,N140)`, its normalized total cost `F=141 V/t` is `U-a N32-b N34-z N140`; after swapping the q32/q34 discounts, it is `U-b N32-a N34-z N140`. Define `D` and `S` as minima over *all* deterministic native decision trees on 228 original physical queries and 141 individually named leaves.

**For every real** `3/4≤a≤49/64`, `7/16≤b≤57/128`, `11/16≤z≤3/4`, the unrestricted global Bellman optima are exactly

```text
D(a,b,z) = min(
  329 -  36*a - 68*b - 141*z,   # Dmid: (329,36,68,141)
  334 - 141*a - 62*b -  45*z,   # D45 : (334,141,62,45)
  326 - 141*a - 47*b -  43*z)   # D43 : (326,141,47,43) NEW
S(a,b,z) = 332 - 141*a - 8*b - 105*z. # S105: native (332,8,141,105)
```

Three nonempty D-optimal cells have respectively `6,12,6` rational vertices, with `16` distinct D-vertex triples; S105 is optimal on the entire 8-corner box. The two **active** D switching sheets are

```text
Dmid = D45 : 96z = 105a - 6b - 5
D45  = D43 : 15b + 2z = 8
```

The `Dmid=D43` equation is `98z=3+105a-21b`, but no Dmid/D43 active common facet occurs in this box: the D45 cell separates them. At boundary ties, the named complete trees witness the exact optimal values. The D43 strategy uses q140 on only **43 of 141** named state paths, versus 45 for D45.

**Sharp, attained exchange gap bounds:**

```text
1229/64 ≤ D(a,b,z) - S(a,b,z) ≤ 187/8
```

Minimum witness `(3/4,57/128,11/16)` gives `(D,S)=(10861/64,301/2)`. Maximum witness `(49/64,7/16,3/4)` gives `(D,S)=(10571/64,9075/64)`.

## Proof with original-index native evidence

**Feasible upper bounds.** `Dmid`, `D45` and `S105` reuse the three original-index identifying trees from EC49FTG; `D43` is a newly calculated complete original-index Bellman tree at `(a,b,z)=(3/4,7/16,11/16)`. Directly replaying *all 141 labeled profiles* through each of four trees using the original 228 physical query response arrays proves that each leaf matches the exact original profile, no query repeats along a profile path, and every usage vector in the theorem is exact. Therefore the stated affine costs are achieved by feasible trees.

**Unrestricted vertex lower bounds.** Cut the box into closed convex cells where each displayed D-affine candidate is minimal; their vertex counts are `6,12,6`, with `16` distinct D anchor triples. Execute the integer-scaled exact unrestricted original-index Bellman recursion (every original query, every recursively visited nontrivial mask) at each D anchor, and independently under swapped prices at the 8 box corners. For **all 24** orientation-specific anchors the unrestricted Bellman optimum *equals* the displayed feasible affine candidate. The [machine certificate](EC49FTH_NATIVE_43_USE_FAN_CERT.json) lists the exact triples and values. Raw original 94-family input reconstructed by a separately implemented parser/Bellman independently yields `D(3/4,7/16,11/16)=1361/8` and `S(49/64,57/128,11/16)=9491/64`.

**Continuous-parameter argument.** The unrestricted optimal cost is the infimum of affine tree costs and hence is *jointly concave* in `(a,b,z)`. On any of the three convex D cells, a named feasible complete tree supplies an affine upper bound `L(p)`. At every vertex `v`, exact Bellman computation proves `B(v)=L(v)`. Every point `p` is a convex combination of these cell vertices, so `B(p)≥Σλ_v B(v)=Σλ_v L(v)=L(p)`; feasibility gives the reverse inequality. The same argument using the 8 corners and S105 proves the S formula throughout the full box. This establishes equality for all real parameters, not only rational anchors. On each D cell `D-S` is affine, and its exact rational vertex extrema yield the attained sharp gap bounds.

**Verifications performed:** 24/24 fresh exact all-228 original-index Bellman anchor executions; 2/2 new raw-94 independent reconstruction/Bellman anchor executions; 4/4 whole original-index native decision-tree replays covering 141/141 labeled profiles; precise rational vertex enumeration. Logs and the complete reproduction code, frozen inputs and 4 full native trees are retained in the EC49FTH self-contained evidence bundle. No formal assistant check or independent project mathematical review has been asserted.

Frozen input file SHA256:
- `frozen_original_master.txt`: `cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e`
- `EC49FPG_PROFILE.csv`: `a61a3ee4d2f13f9d216f52cd3529c72d395c1250bfb1d7ae96a1adf5a6837c1f`

## Research frontier and operational scope

This advances EC49FTG's lower z-face `3/4` to `11/16` and establishes a distinct, previously unrepresented 43-use q140 optimal region. Next: inspect the first new active original-index tree below `z=11/16`, and move the `a=49/64` face outward while preserving exact native query/state provenance.

This is independent portable research. It does not create an immutable Task, a CLAIM, an Activity checkpoint, a formal Result or an independent Review. The exact topic `RS-EC49AS` had `NO_CANONICAL_PUBLICATION_DIRECTORY` at the native Source snapshot inspected on 2026-11-18 21:58:58 UTC; ownership for a non-existent publication cannot be inferred from that query. The original Researcher SID `MCP-44cfc4e6f2094f96861854ebefc77e84` was observed as retained, with `execution_authorized=false`.
