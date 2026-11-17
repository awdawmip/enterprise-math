# EC49FSF — q32/q34 joint 3/8 discount and q140 variable discount: exact eight-phase native BRC theorem

Date: 2026-11-18. Scientific pin: `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`.
Status: AUTHOR_PROVED / TWO_EXACT_NATIVE_BELLMAN_IMPLEMENTATIONS / NOT_INDEPENDENTLY_REVIEWED.
Continuations: [EC49FSD #2675](https://github.com/awdawmip/enterprise-math/pull/2675) and [EC49FSE #2678](https://github.com/awdawmip/enterprise-math/pull/2678).

## Mathematical universe

Retain BRC class 16943, its 141 named distinct state profiles from 310 raw configurations, and all 228 physically named native observers with their original joint response partitions. Prior is uniform on the 141 profiles. Admissible objects are all complete finite deterministic adaptive identification trees on this exact native experiment; observer names are not quotient-collapsed. The model is a typed finite BRC observer experiment within Enterprise Math, not a claim about full Heartbeat physical dynamics. P000 is unchanged.

With price unit t>0, q32 and q34 cost 5t/8 each; q140 costs (1-z)t, 0<=z<=1; all others cost t. Define F(z)=141 V(z)/t where V(z) is the global optimal expected observation cost.

## Theorem — all real z in [0,1]

| z interval | F(z) | U | N32 | N34 | N140 | root | max depth |
|---|---|---:|---:|---:|---:|---:|---:|
| [0, 3/56] | 1901/8 - 8z | 304 | 36 | 141 | 8 | q34 | 4 |
| [3/56, 1/16] | 238 - 15z | 301 | 27 | 141 | 15 | q34 | 3 |
| [1/16, 1/6] | 1905/8 - 17z | 303 | 32 | 141 | 17 | q34 | 3 |
| [1/6, 5/14] | 1925/8 - 32z | 304 | 28 | 141 | 32 | q34 | 3 |
| [5/14, 3/8] | 1965/8 - 46z | 309 | 28 | 141 | 46 | q34 | 3 |
| [3/8, 2/5] | 2019/8 - 64z | 309 | 10 | 141 | 64 | q34 | 3 |
| [2/5, 77/192] | 2035/8 - 69z | 311 | 10 | 141 | 69 | q34 | 3 |
| [77/192, 1] | 1133/4 - 141z | 305 | 7 | 51 | 141 | q140 | 3 |

All formulas agree at interval boundaries. Exactly eight fixed complete-tree **affine cost types** are needed and sufficient on the whole z interval because the eight distinct open phases have different slopes. Multiple full trees may share a cost type.

### Exact Bellman boundary certificates

| z | 141V/t |
|---|---:|
| 0 | 1901/8 |
| 3/56 | 13283/56 |
| 1/16 | 3793/16 |
| 1/6 | 5647/24 |
| 5/14 | 12835/56 |
| 3/8 | 1827/8 |
| 2/5 | 9071/40 |
| 77/192 | 14509/64 |
| 1 | 569/4 |

All nine anchors were evaluated with exact rational/integer Bellman dynamic programming using two original-data reconstructions of all 228 named observer fibers. A full 141-profile deterministic witness tree was replayed for every affine phase, without repeating an observer on a state path. Machine JSON includes use counts, baseline observations, Bellman values, and source input pin. The accompanying Python rechecker uses the frozen raw-data bundle and the pre-existing source-specific decoders/solvers from prior research; the full independent local evidence bundle includes raw data, original solver files, witness trees and logs.

### Proof of the continuous-domain assertion

For a nonempty candidate set S of named profiles and informative observer q, let P_q denote q's original physical response partition. Singleton candidate sets have D(S)=0; larger sets satisfy the finite Bellman recurrence D(S)=min_q (|S| p_q(z)+sum_{B in P_q} D(S intersect B)). Every nonempty recursive child is a strict subset. A reduced complete tree T has total normalized cost C_T(z)=U(T)-(3/8)(N32(T)+N34(T))-z N140(T). Therefore the global optimum F(z)=min_T C_T(z) is concave and piecewise affine.

For each listed interval [l,r], the 141-profile witness T realizes the affine row cost for all z. Both independent exact Bellman procedures give F(l)=C_T(l) and F(r)=C_T(r). Concavity gives F(z)>=(1-theta)F(l)+theta F(r)=C_T(z) whenever z=(1-theta)l+theta r. Feasibility of T gives the reverse inequality F(z)<=C_T(z). Thus equality holds for every real z in [l,r], proving all eight intervals. Eight distinct strictly active slopes on open intervals require eight fixed affine strategy types; the eight witnesses attain this bound.

### New structural observation

At joint discount 3/8, any positive discount in q140 already improves optimum: F(0)=1901/8 and right derivative -8. The q140-root strategy becomes optimal at z=77/192, where the slope becomes -141. The earlier joint discount 1/4 yielded four phases, while 1/2 yielded eight; this exact intermediate slice exposes a sharper future two-parameter bifurcation problem.

## Validation and open work

Mathematical proof scope: the entire exact [0,1] real z interval *for this one fixed 3/8 joint-discount slice*. No external physical calibration, global three-price 3D theorem, or independent mathematical review is asserted. Exact boundary validation is finite-exhaustive via recursion over all admissible informative named observations; original-94-family checker cross-verifies the frozen first decoder. Next: find the first bifurcation in alpha within [1/4,3/8] using the triples (U,N32+N34,N140), certify proposed rational 2D vertices with exact Bellman and preserve the native observation identities.
