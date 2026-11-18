# EC49FST — Exact upper BRC three-price prism and sharp boundary

Date: 2026-11-18. Frozen source: awdawmip/enterprise-math@fc0f038e7bfd12c886b4d37f900bfb770c0f61ab. Direct parent: EC49FSS PR #2721@60cd9583d556de6e9ee94c60471ffc19f5c4c47c. Status: AUTHOR_PROVED / EXACT_PRIMARY_10_ANCHORS / INDEPENDENT_2_ANCHORS / NOT_REVIEWED.

## Mathematical object and theorem

Retain all 310 original configurations, their 141 original named joint-response profiles with uniform prior on profiles, and all 228 original physically named deterministic observations. Allow every complete strict-splitting adaptive identification tree, without alias collapse. Prices of q32, q34 and q140 are (1-a)t, (1-b)t and (1-z)t; all other query prices are t>0. Define F(a,b,z)=141V(a,b,z)/t.

For **every real** a in [2/3,1], b in [27/64,29/64], z in [1/2,77/128], the unrestricted Bellman optima are

D(a,b,z) = F(a,b,z) = 316 - 141a - 43b - 30z,

S(a,b,z) = F(b,a,z) = min(315 - 141a - 10b - 77z, 318 - 141a - 10b - 82z).

For S, a discounts q34 and b discounts q32. The second S plane enters exactly at z=3/5. Consequently,

D-S = 1 - 33b + 47z for z in [1/2,3/5],
D-S = -2 - 33b + 52z for z in [3/5,77/128].

The positive difference is independent of a, with sharp minimum **611/64**, at b=29/64,z=1/2 for all a, and sharp maximum **983/64**, at b=27/64,z=77/128 for all a.

### Actual complete named tree witnesses

| Tree | Orientation | (U,N32,N34,N140) | Affine total cost |
| --- | --- | --- | --- |
| E (inherited) | direct | (316,141,43,30) | 316-141a-43b-30z |
| H (inherited) | swapped | (315,10,141,77) | 315-141a-10b-77z |
| K (new) | swapped | (318,10,141,82) | 318-141a-10b-82z |
| J (new challenger) | direct | (324,141,58,32) | 324-141a-58b-32z |

All J/K complete trees were regenerated and replayed over each of 141 named states against all original observation response vectors. Their compressed lossless data and full-byte SHA256 are preserved in COMPLETE_JK_TREES.json. E/H remain preserved in EC49FSS.

## Proof for the entire continuous prism

Each feasible original named-observer tree T has a total cost U(T)-aN32(T)-bN34(T)-zN140(T), affine in the three discounts. The unrestricted optimum, a pointwise infimum of feasible affine tree costs, is jointly concave, and does not exceed the cost of any feasible witness.

At a0=2/3, exact exhaustive original 228-observer rational Bellman DP gives E at all four vertices of the direct (b,z) rectangle [27/64,29/64] x [1/2,77/128]. The upper-right vertex also has a new J tie. By concavity the optimal cost inside the rectangle is at least the convex interpolation of these exact vertex costs, which equals the E affine plane. The feasible E tree supplies the matching upper bound. Thus D=E throughout the whole real rectangle.

For swapped orientation, subdivide that rectangle at z=3/5. On the six distinct vertices of [27/64,29/64] x {1/2,3/5,77/128}, unrestricted Bellman cost equals the feasible H plane in the first rectangle and feasible K plane in the second. By the same convex interpolation lower bound and feasible witness upper bound, S=H or K on each respective full rectangle.

Saturation lifting: a repeated fixed deterministic observation cannot strictly split an already conditioned response fiber, so every complete strict-splitting tree uses a given named query at most once per profile path. Accordingly 0<=Ni(T)<=141. If an optimal tree at discount a0 uses the a-discounted query on all 141 paths, any competing tree's cost can fall by at most 141(a-a0) as a increases, whereas this tree falls by exactly that amount. It remains globally optimal for every a>=a0. E uses q32 141 times, and H/K use q34 141 times in the swapped orientation. Hence the vertex-proved a0 formulas extend without interpolation error to all a in [2/3,1].

The 10 full DP anchors (4 direct and 6 swapped), their reached-subset counts, exact prices, two independent 94-family decoder checks, and new full tree hashes are in EXACT_CERTIFICATE.json. VERIFY_EC49FST.py recomputes all anchors, checks all 141 paths of J/K and checks the edge.

## A sharp new phase-entry obstruction

The direct challenger J has relative cost J-E=8-15b-2z. At b=29/64, this equals zero exactly at z=77/128 and is negative above that threshold. Thus **77/128 is the largest uniform z-height on the stated b interval for the specific E formula**, not a proven ceiling on further research. The unrestricted native Bellman value at (a,b,z)=(2/3,29/64,39/64) is 5895/32 with vector J=(324,141,58,32), improving on E by exactly 1/64. This is a complete original-model counterexample to extending the previous fixed strategy formula unchanged.

## Evidence, provenance, next work

Frozen input SHA256: master cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e; profile CSV a61a3ee4d2f13f9d216f52cd3529c72d395c1250bfb1d7ae96a1adf5a6837c1f. Native exact DP covered the unrestricted set of 228 named physical observations; no lossy observer compression. The independent decoder reproduced the direct J-tie and swapped K upper vertex. Further independent review remains NOT_REVIEWED.

Historical researcher EM-DIRECT-8454C6 and Activity RA-ED136F89271FD89288F3E58D retain their original provenance. Fresh 2026-11-18 exact lookup of RS-EC49AS returned SUCCEEDED / NO_CANONICAL_PUBLICATION_DIRECTORY at Source 4bad6b1294bfe8d74b8668a07f60ea9467fed3fd, a directory-level result, **not** a full live owner projection. This is independent portable research, not an authorized new CLAIM, native Activity checkpoint, Result or Review. P000 and frozen scientific inputs unchanged.

Next research unit: determine the complete new native Pareto fan for z>77/128. Locate the J entry surface and the phase containing the (332,141,62,42) challenger noted in EC49FSS; solve exact new vertices and sharp swap-gap extrema with complete original named observation paths, then obtain independent research review.
