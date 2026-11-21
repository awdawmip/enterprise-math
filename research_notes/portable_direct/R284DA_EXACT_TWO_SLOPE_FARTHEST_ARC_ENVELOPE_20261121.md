# R284DA — Exact two-slope event envelope for the frozen Port farthest-arc observer

Date: 2026-11-21 (Asia/Shanghai)  
Status: **AUTHOR_PROVED / EXACT_FINITE_CERTIFIED / NOT_REVIEWED**  
Research mode: independent portable finite mathematics; historical line attribution `EM-DIRECT-20B766`, no live formal Task CLAIM asserted.

## Scientific input and provenance

Continue R284CZ (307 equal farthest-distance source-neighbor edges) without altering the 34-bit Port model. Reuse the immutable R284CO source generator `awdawmip/enterprise-math@acba2d8667903434aaa2a10720f43637fcc2421b:research_notes/portable_direct/R284CO_spectral_witness_checker.py`, Git blob `b46e0f682b58e47c27094b4bea6fa4e55119a3ee`. Its checked codeword SHA-256 is `b6ce76b2c08b9ec6b79ec83173befd2589928ca7c636643c3eaecd40405f4ff4`.

There are 65,536 distinct integer codewords in `[0,P)`, `P=17,179,869,143`, and 64 labeled circular arcs `A_i=[a_i,a_i+w_i]` (positive orientation, integer endpoints, `0<w_i<P/2`). For an integer site x define `d_i(x)=0` on the arc and the nearest circular endpoint distance outside it, and `D(x)=max_i d_i(x)`. Original matrix indices, rather than residue ordering, determine source neighbor edges (12 lower flips and differing-bit swaps).

## Theorem — exact two-slope event representation

For **any** finite family of positively oriented arcs on an integer circle of circumference P with `0<w_i<P`, each function `d_i(x)` on `0<=x<P` is the maximum of zero and its *applicable* affine branch. Fix an arc `(a,w)`. Its outside complement lifts to integer intervals

```text
b_k = a+w+kP,       e_k = a+(k+1)P,     k in {-1,0}.
mid_k = floor((b_k+e_k)/2).
[b_k,mid_k+1):     d(x)=x-b_k.
[mid_k+1,e_k+1):   d(x)=e_k-x.
```

Intersect these half-open intervals with `[0,P)`. The chosen midpoint convention is exact for integer x, including ties. Outside their union the arc distance is zero. Each lifted interval has slope +1 or -1 and a fixed integer intercept.

Build the sorted event coordinates of all segment starts/ends together with 0 and P. Within any elementary event slab `[t_j,t_{j+1})`, the set of active positive and negative branches is fixed. Let

```text
Cplus[j]  = max{-b : (+1,-b) is active in slab j}, or absent;
Cminus[j] = max{ e : (-1, e) is active in slab j}, or absent.
```

Then for **every integer** x in that slab, exactly

```text
D(x) = max(0, x+Cplus[j] if present, Cminus[j]-x if present).
```

*Proof.* For an x outside a particular arc, choose the unique lifted complement containing x. Its two endpoint distances are `x-b_k` and `e_k-x`; their minimum is the first branch on/before the integer midpoint, the second branch afterward. All other branches of that arc are inactive. For x on the arc, its distance is zero. Maximizing these valid branches across all arcs commutes with maximizing within the common slope class: at each slab, the largest +1 branch is `x+max(-b)`, and the largest -1 branch is `max(e)-x`. Including zero proves the formula. Endpoint and parity cases follow from the half-open convention.

**Complexity.** At most `4m` clipped branch segments, `8m+2` event positions (for m arcs). Sorting and a balanced multiset can construct the coefficient tables in `O(m log m)`, and each site uses one event predecessor search `O(log m)` followed by constant-size exact arithmetic. The accompanying small standard-library checker instead scans the active intercept set at each event: its preprocessing is `O(m²)`; its per-site query remains logarithmic. Source-index edge enumeration is still `O(E)`, `E=1,474,560` here.

## Frozen-model exact result

The actual 64 frozen arcs yield:

| Item | Exact count |
|---|---:|
| Clipped affine branch segments | 191 |
| Unique event positions, including 0 and P | 194 |
| Elementary event slabs | 193 |
| Adjacent slabs with identical coefficient pair merged | **65 coefficient runs** |
| Frozen codewords independently checked | 65,536 |
| Direct arc-distance evaluations required to construct the new farthest-distance profile | **0** |
| Independently executed baseline comparisons | 65,536 × 64 = 4,194,304 |
| Source mutation edges visited | 1,474,560 |
| Exact equal-`D` edges recovered | **307** |
| Distinct endpoints of equal-`D` edges | 612 |
| Additional direct distances needed for their unique winning labels | 612 × 64 = 39,168 |

The 307 equal-distance edges retain the exact R284CZ mutation partition: flip positions 0/1/2/4/6 give 3/14/228/16/45 respectively; swapping 0 and 1 gives 1; all other allowed classes give zero. The canonical ordered edge sequence with original source indices and winning arc labels reproduces SHA-256 `251a3ca8d2d72cf6f7ca19869f174eb9e370f330533e484faf13dcb2a68dab8b`.

Thus the complete 65,536-site farthest-distance profile and the entire 307-edge equality graph agree with an independently executed full 4,194,304-distance baseline, while the new evaluation uses the 193 event slabs/65 coefficient runs instead of 64 arc distances at each site. Identical edge-list digest also checks the original index orientation and arc labels.

The reference checker is `R284DA_envelope_checker.py` and the deterministic summary is `R284DA_envelope_certificate.json` in this directory. Both use Python unbounded integer arithmetic and the unchanged imported R284CO generator. This is an auxiliary Port observer theorem; no native X6 trajectory, P000 change, formal result promotion or independent review is claimed.

## Scope, retained residual and next question

The R284DA envelope preserves full integer farthest-distance values and the original matrix index of each codeword. It additionally recovers exact arc winner labels for candidate equal edges, rather than quotienting away label/source provenance. It does **not** reconstruct all 63 other order statistics `d_k`, so the previously certified global forced-rank and core-uniqueness results remain separately pinned (R284CW).

Next investigate a source-mutation solver that intersects the 65 coefficient runs with the actual determinant-difference formulas for each lower flip/swap, and solves the `+/-` branch equality equations **without enumerating all 1,474,560 edges**. Prove whether those equations generate exactly the 307 previously certified edges; preserve the four unforced edge identities and 303 absorbed edges via the existing `tau` evidence.

Project write is an independent scientific artifact under the portable protocol. Native Activity linkage requires its own original-session authorization and exact Source readback and is tracked separately.
