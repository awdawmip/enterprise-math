# BRC-X6: explicit 29-bit / 13-term minimal native policy

**2026-11-09. Status:** AUTHOR_PROVED / EXACT_INTEGER_VERIFIED / UNREVIEWED / NOT_ADMITTED. This is an author-portable theorem, not a canonical Source Task Result or Driver acceptance.

**Frozen input:** `f42f2906d77f24085c123f3ccfe9667d41caa96d`. Native 96 ports, 6 labelled actions, 9 frozen signed joint-observer roots, source ports (6,7,28,29), exact 38 lawful deterministic policies `V`. Reuses an already validated 13-policy prefix from author evidence `b57db33df8b793cb856c45b0c84df0d0382fb730`; does not recredit the earlier discovery.

## Statement and exact witness

Let `C` be the 24x38 integer matrix, each column `c_v` registering one of six source-action labels in each of four native source rows. Take the 13 lawful policy IDs in frozen `V` order

```
IDS=(2,8,15,21,24,28,29,31,37,0,1,3,5)
```

Their original four-source action tuples are

```
(0,0,2,2),(1,0,3,2),(2,2,4,4),(3,3,5,5),
(4,4,0,0),(4,4,5,5),(4,5,0,1),(5,1,1,3),
(5,5,5,5),(0,0,0,0),(0,0,1,1),(0,0,4,4),
(0,1,2,3)
```

With weights `w_j=5^j` for `0<=j<=12`, the denominator `D=sum_j w_j=(5^13-1)/4=305175781` occupies **29 binary bits**. The full labelled source-action marginals `X=(sum_j w_j c_{v_j})/D` are exactly

```
X = 1/305175781 × [
  [304687501,         5,        25,       125,    19375,    468750],
  [ 60546881, 244218750,        25,       125,     3750,    406250],
  [  1969375,   9843750, 244140626,         5, 48828150,    393875],
  [  1953750,   9781250,         6, 244218750, 48828150,    393875]
]
```

All 24 entries are strictly positive, and the six numerators in each row sum exactly to D. Every listed native policy passes all nine frozen root-wise signed next-port/reward joint-observer relations, hence their convex mixture is lawful. **Theorem: minSupport(X)=13.**

## New native 13-minor bound 4

Define the exact 13-row coordinate chart `A=C[R,:]`, where

```
R=(0,1,2,3,4,5,18,19,20,21,22,6,10).
```

Exact integer row reduction confirms `rank(C)=rank(A)=13`. The first 11 rows are the vertex-edge incidence of the 12-vertex bipartite multigraph obtained by projecting each **labelled** legal policy to its pair of source-0 and source-3 actions, with one redundant vertex equation omitted. The last two rows retain original source-1 actions 0 and 4. Parallel edges remain distinct policies.

**Lemma:** for every 13-element subset `S` of the 38 labelled policy columns, `|det(A[:,S])|<=4`.

Proof: If the determinant is nonzero, the first 11 incidence rows must have rank 11, since the last two rows can increase rank by at most two. The 13 projected labelled edges therefore form a connected multigraph spanning all 12 vertices. Choose a spanning tree of 11 edges and the two remaining chords. The tree incidence minor has determinant ±1; integral elimination along each chord's unique tree path reduces the full 13x13 determinant, up to sign, to the determinant of the two *oriented fundamental-cycle signatures*. For a simple labelled cycle in consecutive edge order `e_0,...,e_{2k-1}`, put

```
sigma(cycle)=(
    sum_i (-1)^i*C[6,e_i],
    sum_i (-1)^i*C[10,e_i]
).
```

The case of two parallel labelled edges is a legitimate length-two cycle. Exhaustive integer DFS over all simple cycles, normalized by minimum vertex and orientation, yields **103653** labelled cycles, with exactly these 19 distinct signatures:

```
(-2,0),(-2,1),(-2,2),(-1,-1),(-1,0),(-1,1),(-1,2),
(0,-2),(0,-1),(0,0),(0,1),(0,2),
(1,-2),(1,-1),(1,0),(1,1),(2,-2),(2,-1),(2,0).
```

Checking all pairs of these 19 integer signatures gives
`max |sigma_1*tau_2-sigma_2*tau_1|=4`. Thus every possible fundamental-cycle pair has determinant magnitude <=4, proving the lemma. A second independent enumerator using a unique simple vertex graph and Cartesian expansion over parallel policy edges reproduces all 103653 cycles, their signature counts, and maximum 4. The two methods share the frozen policy input; this is author-side cross-checking, not independent Driver review.

## Exact 13-term minimality proof

The 13 chosen columns have full rank; indeed `det(A[:,IDS])=-1` by exact integer evaluation. Their 13-term positive convex representation proves `minSupport(X)<=13`.

Suppose X lay in the span of at most 12 lawful policies. Since the complete column rank is 13, extend these policies to twelve independent columns `T` while retaining X in their span. Then
```
0=det(A[:,T],A[:,D*X])
 =sum_(j=0)^12 5^j*d_j,
d_j=det(A[:,T],A[:,v_j]).
```
Each `d_j` is an integer with `|d_j|<=4` by the new lemma. Because the 13 selected `v_j` span 13 dimensions, at least one `d_j` is nonzero. For the largest such index `k`, the magnitude of `5^k*d_k` is at least `5^k`, while the sum of magnitudes of all lower-degree terms is at most `4*(5^k-1)/4=5^k-1`. Exact cancellation is impossible. Thus X has no representation on <=12 legal policy columns, even with rational signed coefficients, and **minSupport(X)=13**.

All 38 original policies and their full nine-root observer signatures remain the carrier; the source-0/source-3 graph is a faithful determinant *calculation*, not a replacement model or an erasure of joint observers.

## Reproduction and control boundary

Author-side reproducibility bundle: `BRC_X6_NATIVE_13_MINIMAL_29BIT_EXPLICIT_AUTHOR_PORTABLE_20261109.zip`, SHA-256 `c7a339cc3ed571f171d609e7c93cf2243a50cb745350c41d8cfee0ffa94217a1`. It includes `build_29bit.py`, `cycle_signature_bound.py`, `independent_cycle_signatures.py`, the frozen exact policy kernel, exact integer certificate `29BIT_13_SUPPORT_CERTIFICATE.json`, and the complete 103653-cycle signature-count certificate. These were re-extracted and all three programs executed successfully on 2026-11-09.

**Open next question:** the 24 signature pairs with absolute determinant 4 may not be jointly realizable as *fundamental* cycles of a 13-edge connected native policy support. Check this exact compatibility question; if none exist, the sharp universal minor bound improves to 3, enabling the analogous 27-bit radix-4 witness. That refinement is not claimed here.

**Source governance:** Parent `ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION`; D25 Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`, immutable publication `TP2-B6F4FC938FF94941C1B7`; scientific task and its LIFT observer unchanged. Current 2026-11-09 exact continuation response was read-only `SUCCEEDED`, route `REGISTER_NEW_SESSION_AND_CLAIM_CURRENT_PUBLICATION`, `execution_authorized=false`, no verified own private native session/CLAIM/run. No Source-native checkpoint, Result, review or theorem admission. Historical authentic UR V2 four-file bundle remains unlocated (94687 bytes, SHA-256 `4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76`); UR math is not repeated.

Status: **AUTHOR_PROVED / EXACT_FINITE_INTEGER_CERTIFICATE / GITHUB_AUTHOR_EVIDENCE / UNREVIEWED / NOT_ADMITTED**.
