# EC49FSP-W: exact native BRC two-parameter price-exchange wedge

Date: 2026-11-18. Independent portable research continuation of EC49FSO PR #2708 and EC49FSP PR #2712. The original BRC16943 scientific source remains pinned to fc0f038e7bfd12c886b4d37f900bfb770c0f61ab. This is the same system of 310 configurations, 141 distinct fully named response profiles, 228 original physically named observers, uniform prior and all complete deterministic adaptive identification trees.

## Exact continuous-parameter theorem

Let F(a,b,z)=141V(a,b,z)/t denote the globally optimal original-native identification cost; q32,q34,q140 have prices (1-a)t,(1-b)t,(1-z)t, and all remaining observations price t>0. Fix a=31/64. For every real b,z satisfying

27/64 <= b <= 29/64,  0 <= z <= 1/8,

the two orientations satisfy

D(b,z) := F(31/64,b,z) = 306 - 141(31/64) - 41b - 4z,

S(b,z) := F(b,31/64,z) = min{P0,P1},

P0 = 306 - 141(31/64) - 41b - 10z,

P1 = 303 - 141(31/64) - 32b - 17z.

Consequently the price-exchange penalty is exactly

D-S = 6z for 0 <= z <= (9b-3)/7,

D-S = 3 - 9b + 13z for (9b-3)/7 <= z <= 1/8.

The nontrivial separating line z=(9b-3)/7 joins (b,z)=(27/64,51/448) and (31/72,1/8). For b >= 31/72 the entire allowed interval z in [0,1/8] is in the first regime. Throughout the rectangle, the exchange penalty is strictly positive for every z>0. This proves a slanted two-dimensional native decision-policy phase boundary, beyond the single-value sharp crossing previously proved at b=27/64.

## Three complete source-native feasible witnesses

For a complete tree let (U,N32,N34,N140) count total named observation occurrences and individual occurrences over all 141 equally weighted profile paths. The direct plane comes from full original named tree (306,141,41,4), SHA256 ad7047debd6d04d3c076eef6d593b7de4d50879a671a439760d4d436210cc767. Swapped P0 uses (306,41,141,10), SHA256 db669e0116a1816bbf53fed6cb1bc07a4549ef9665637433e05c059936ff9742. Swapped P1 uses (303,32,141,17), SHA256 c43c37dfca7f748b0e4acadcd69c8be5e8c5bdeb3a0515c6c7e8c796250042e2. All are among six complete lossless JSON trees already persisted in PR #2712. Each was replayed using every original response of all 141 named profiles to a distinct singleton leaf. The witness tree affine cost is U-aN32-bN34-zN140.

## Exact exhaustive Bellman vertex certificates

For every non-singleton subset T of the 141 original profiles, exact native Bellman uses

Tcost(T) = min over original q that splits T of [ |T| * (1-d_q) + sum over response r Tcost(T intersection {profile:q(profile)=r}) ],

with Tcost(singleton)=0, discounts d32=a,d34=b,d140=z and all other dq=0. All 228 original named observations, not reduced anonymous sensors, remain available.

The following are the six distinct vertices of the two exact convex phase polygons. D and S are the **unrestricted full original native Bellman optima**.

| (b,z) | D exact | S exact | Swapped phase |
| --- | --- | --- | --- |
| (27/64,0) | 7053/32 | 7053/32 | P0 |
| (29/64,0) | 1753/8 | 1753/8 | P0 |
| (29/64,1/8) | 1749/8 | 1743/8 | P0 |
| (31/72,1/8) | 126461/576 | 126029/576 | P0=P1 |
| (27/64,51/448) | 49269/224 | 12279/56 | P0=P1 |
| (27/64,1/8) | 7037/32 | 14021/64 | P1 |

The EC49FSO full native source had already verified (27/64,0) and (27/64,51/448) in both orientations. This continuation evaluated the needed top-edge endpoints and interior tie point using the primary exact unrestricted all-228 Bellman solver. Six additional independent raw 94-family/CSV-decoder exact Bellman checks reproduced both orientations at the three z=1/8 vertices, with reached-state counts D/S: 10161/10143 at b=27/64, 10153/10142 at b=31/72, 10132/10078 at b=29/64. Distinct-decoder agreement is an implementation cross-check, not an independent Project Driver review.

## Rigorous all-real proof

Each complete named decision tree defines an affine total-cost plane valid at every admissible (a,b,z), so its cost is an upper bound on the unrestricted optimum F. The optimum F is the infimum of all such affine planes; hence F is jointly concave in its price variables.

For direct D, the single affine tree plane agrees with unrestricted exact Bellman at all four rectangle vertices. Any interior point is a convex combination of the four vertices. Concavity supplies the matching lower bound by the affine interpolation of the exact endpoint minima, and the feasible tree supplies the identical upper bound. Thus D is exactly its displayed affine plane over the whole rectangle.

For S, the P0-optimal convex polygon is the convex hull of vertices (27/64,0), (29/64,0), (29/64,1/8), (31/72,1/8), (27/64,51/448). The P1-optimal complementary triangle has vertices (27/64,51/448), (31/72,1/8), (27/64,1/8). Exact Bellman equals the corresponding candidate full tree plane at every polygon vertex. Concavity plus a convex decomposition of each point and its corresponding feasible witness therefore sandwich the unrestricted optimum exactly between equal affine expressions. This proves the two-piece formula throughout the complete rectangle for **all real** b,z, including the separating interface and outer boundary. No grid-fitting extrapolation is involved.

The difference formula follows by subtraction. On the separating line the two expressions agree because 7z=9b-3. At z=0, D=S; for positive z the difference is positive on both sides, with continuous matching at the boundary.

## Verification, identity, and next problem

Scope: AUTHOR_PROVED / EXACT_PRIMARY_FINITE_EXHAUSTIVE / INDEPENDENT_PARTIAL / NOT_REVIEWED. Frozen input and all original physical observer identities are preserved. Native observation-cost parameters are **not** heartbeat time. Historical researcher EM-DIRECT-8454C6, own SID MCP-44cfc4e6f2094f96861854ebefc77e84, Activity RA-ED136F89271FD89288F3E58D. Current execution_authorized=false; original control continuation request ended FAILED / CANONICAL_REJECTED: unknown current immutable task publication. This contribution is independent portable scientific evidence, not a new formal Task/CLAIM/Result/Review/Activity checkpoint.

Next: extend the slanted boundary to z>1/8, investigate the synchronized z=1/6 transition and prove a genuine three-variable polyhedral cell as a and b both vary; use the same 228-observer original-native model and precise frozen sources.
