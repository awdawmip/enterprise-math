# X6 R94 — Complete low-T two-weight BRC phase diagram, including the post-wall winner

Date: 2026-11-22 (Asia/Shanghai). Evidence: SYMBOLIC_AUTHOR_PROOF / EXACT_FRACTION_AUTHOR_CHECK_PASS / NOT_INDEPENDENTLY_REVIEWED. Independent portable research only, with no formal CLAIM/PROGRESS/Result/Review.

Frozen scientific foundation: `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json`. Predecessors: R91–R93 (especially `research_notes/portable_direct/2026-11-22_x6_r93_lowT_sharp_wedge.md`). This concerns the *conditional positive-count fourth-order BRC star-moment histogram observer* with an unknown common additive offset. It does not provide a native P000 operation-preserving reduction of labeled Cell/Link/Port, full triadic events, residuals or heartbeat time.

## Definitions

For nonzero `a=(x,y,z)∈Z³`, identify `a` and `-a`, and define `q(a)=max(sum max(ai,0), sum max(-ai,0))`. Write the integer moments

```
u = x+3y+6z,   v = 3x+12y+30z,   h = 7x+39y+126z.
g = (|u|, |v|, |h|, |v-u|, |h-u|, |h-v|).
F(a;S,T) = max(g12/2, g13/(1+S), g14/(1+T),
                g23/(1+S), g24/(1+T), g34/(S+T)).
η*(p;S,T) = min_{a≠0, q(a)≤p} F(a;S,T).
```

All minima are over nonzero *integer* differences and `±` identifies orientations; no bounded q assumption is used in the proof. Set `1≤S<∞`, `0<T<1`, `p∈Z`, `p≥11` and

```
R=1/(1+T),   A=5+6T,   B=6+5T  (1<A<B),
s=(10,-5,1) with q=11,
b=(14,-9,2) with q=16,
c=(24,-14,3) with q=27,
e=(34,-19,4) with q=38.
```

## Theorem R94 (all S≥1, 0<T<1, all p≥11)

The *exact optimal value* is

```
η*(p;S,T) = R              if p≤26 or S≤B,
             6/(S+T)       if p≥27 and S>B.
```

All minimizing unoriented integer directions are exactly:

| Port budget | S<A | A≤S<B | S=B | S>B |
|---|---|---|---|---|
| 11≤p≤15 | {s} | {s} | {s} | {s} |
| 16≤p≤26 | {s} | {s,b} | {s,b} | {s,b} |
| p≥27 | {s} | {s,b} | {s,b,c} | {c} |

Consequently, the two earlier exact walls remain distinct: `S=A` introduces a tied direction once 16 Ports exist, while `S=B` is the Port-27 three-way junction, followed by a strict unique winner `c`. For `p≥27, S>B` the exact improvement over the former plateau is

```
R - η* = (S-6-5T)/((1+T)(S+T)) > 0.
```

This closes the previously open post-`B` optimal-value question in R93 and unifies the R91 low-T strip (`1≤S<5`) with the R93 low-T wedge (`S≥5`).

## Unbounded-lattice proof

First compute directly `F(s)=R` for `S≥1,0<T<1`. If `F(a)≤R`, two of its six inequalities imply `|h|≤1`, `|h-u|≤1`, and `|u|≤2R<2`, so `u,h∈{-1,0,1}`. The integral moment map has `v∈3Z`, `h≡u (mod 2)` and `h≡u+6v (mod 12)` (see R91's inverse map). These force `h=u` and `v=6m` for an integer `m`; substituting in the inverse moment map yields exactly

```
a = (10u-24m, -5u+14m, u-3m), u∈{-1,0,1}, m∈Z.
```

**Case 1: S≤B.** Then `|v|≤R(1+S)≤(7+5T)/(1+T)<7`. As `v=6m`, only `m=-1,0,1` remain. Up to sign, the nonzero possibilities are precisely `s,b,c,e`, with respective q values `11,16,27,38`. Their scores satisfy

```
F(s)=R,
F(b)=max(R,6/(1+S),5/(S+T)),
F(c)=6/(S+T),
F(e)≥7/(S+T)>R  [because S+T≤6(1+T)].
```

The `b` inequalities are equivalent to `S≥5+6T=A`: the additional `S≥5+4T` bound is weaker. The `c` inequality `F(c)≤R` is equivalent to `S≥6+5T=B`, hence equality only at `S=B` in this case. Since `s` is feasible for all `p≥11`, no `F<R` exists here and the table follows after q filtering.

**Case 2: S>B, p≤26.** Any *strict* improvement `F(a)<R` would force the two integral gaps `|h|<1` and `|h-u|<1`, so `h=u=0`. Solving the integer moment equations gives `a=kc` for a nonzero integer `k`, and `q(kc)=27|k|>26`; contradiction. Hence `η*=R`. At equality `F(a)=R`, the parameterization above still applies. For `|m|≥2`, `|x|=|10u-24m|≥38`; for `|m|=1`, only `b` has q≤26. Since `S>B>A`, b ties when p≥16. This yields both low-Port rows.

**Case 3: S>B, p≥27.** Now `F(c)=6/(S+T)<R`, and `c` is feasible. For any `a` with `F(a)≤F(c)<R`, the same two integer gaps yield `h=u=0`, hence `a=kc`. Homogeneity gives `F(kc)=|k|F(c)`, so precisely `±c` minimize. The Port requirement `q(c)=27` is exact. This proves the formula and all minimizers for every real S,T in the stated region. QED.

## Exact author crosscheck and next frontier

`x6_r94_complete_lowT_atlas_verify.py` uses exact `fractions.Fraction` comparisons and exhausts every unoriented integer direction with `q≤38` (95,133 directions), for `T=1/4,1/2,3/4`, eleven S values per T spanning `S=1,4,5`, both exact walls, their two sides, a remote high-S case, and Ports `11,15,16,26,27,38`. All 198 parameter/Port assertions pass over 5,844,069 actual in-budget direction comparisons; `x6_r94_complete_lowT_atlas_results.json` captures the reproducible summary. This finite test is a crosscheck of the symbolic all-integer argument, not a replacement for it.

Unfinished: extend the full two-dimensional atlas to T≥1, where the strict-integer-gap pinning changes; investigate whether the conditional BRC observer has a faithful operation-preserving relation to P000 native named-Ports, full triadic events, residuals and heartbeat-time trajectories. No frozen input or P000 ontology has been modified.

Control observation for this run: original task read `r2-20261122-0415-x6-task-read` and continuation `r2-20261122-0415-x6-continuation-read` both ended `FAILED / SOURCE_TREE_TRUNCATED`; current shared owner/claim authority is unverified. No formal write was made.
