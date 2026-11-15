# R762BU — Sharp finite-hop common-depth repair for native X6 BRC endpoint observers

Research task: RS-X6-TRIADIC-CLOSURE-DYNAMICS, immutable publication TP2-8B7E13C5904A2D6F1142.
Date: 2026-11-16 (Asia/Shanghai). Status: AUTHOR-PROVED / EXACT FINITE VERIFICATION / NOT_REVIEWED.
Frozen source: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json and definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md.
Current behavioral policy read independently. Existing R762BL/BO/BT reused for coordinate observer, odd-step nonreturn and source-query distinctions.

## Population and exact observation

The primitive spatial action alphabet is the twelve signed steps ±e_i in Z^6. For a specified exact number m≥0 of primitive steps, the reachable endpoint population is

E_m = { z in Z^6 : ||z||_1 ≤ m, ||z||_1 ≡ m (mod 2) }.

This follows from the triangle inequality and parity; conversely a shortest path of ||z||_1 steps can be lengthened to m by opposite-step pairs. The chosen chart anchor does not assert an intrinsic origin.

For each 3-subset S of six axes, Obs_S(z) subtracts min_{i in S} z_i from each of its three selected signed components. Let D=(1,1,1,1,1,1), Δ=Z D, and r=can6(z)=z-(min_i z_i)D. The full family of 20 coordinate observers identifies exactly z modulo Δ. The omitted common depth h=min_i z_i is a composite X6 coordinate, not a seventh spatial dimension.

The object reduced in this paper is **coordinate endpoint identity for fixed m**, not ordered path history, BRC branch identity, force-sign history or an actual TRIADIC_CLOSURE_E admission event.

## Theorem A — three observers suffice for full relative information

For any chosen family H of 3-axis coordinate observers, put an undirected edge between two axis labels whenever some S in H contains both. The kernel of the joint observation is precisely the integer vectors constant on each connected component. Thus its kernel equals Δ if and only if the co-observation graph is connected.

At least 3 panels are necessary to connect all 6 axes: each triple joins at most 3 components and can reduce their number by at most 2. A valid 3-panel example is {123,124,156}.

Among all C(20,3)=1140 unordered three-panel families, precisely **480** are connected. Their exact incidence classification is:

| Sorted pairwise intersection sizes | Triple intersection | Count |
|---|---:|---:|
| 0,1,2 | 0 | 180 |
| 1,1,1 | 0 | 120 |
| 1,1,2 | 1 | 180 |

Proof of count: Connected triple families cover all six axes, hence (sum of their three pairwise intersection sizes) minus the triple intersection is exactly 3. With distinct three-element sets, the listed patterns exhaust the possibilities. For 0,1,2 choose an unordered disjoint 3+3 partition (10 choices) and a third triple of type 1+2 (18 choices). For 1,1,1 with no common element, choose the three pairwise shared labels, the three private labels and distribute them over three unlabeled panels: C(6,3)*3!*3!/3!=120. For 1,1,2 with one common element, choose the universal vertex (6), extra shared vertex (5), and an unordered pair of private vertices for the two doubly-overlapping panels: C(4,2)=6, yielding 180. Sum=480. □

These are native **coordinate** panels. The frozen FCC/K4 complete carrier-readout realization of only its four STAR selections is unchanged.

## Theorem B — exact arbitrary-m common-depth fiber and optimal repair

For every m≥0 define q_m=floor(m/3)+1.

1. The largest fiber of can6 restricted to E_m contains **exactly q_m signed endpoints**.
2. Therefore any finite supplement, combined with the entire relative coordinate observation, that distinguishes all endpoints in E_m needs at least q_m possible values, or ceil(log2 q_m) fixed-length bits.
3. The supplement z_1 modulo q_m is optimal: (can6(z), z_1 mod q_m) is injective on E_m. Any connected 3-panel family may replace all 20 panels.

Proof of upper bound: if z and w are in E_m and have identical relative observation, z-w=kD. Hence 6|k|=||z-w||_1≤||z||_1+||w||_1≤2m, giving |k|≤floor(m/3). Every fiber therefore has an integer interval of possible common depths with width at most floor(m/3), and any coordinate residue modulo q_m uniquely identifies its member.

Sharpness for all m: write m=3r+s with s∈{0,1,2} and j=0,...,r. If s=0 or s=2, set

z^(j)=(j-r,j-r,j-r,j,j,j).

All r+1 endpoints share the same relative observer and have norm 3r, hence are realizable at length m by a shortest path (s=0) or one cancelling pair (s=2). If s=1, instead set

z^(j)=(j-r-1,j-r,j-r,j,j,j).

All r+1 states share the same relative observer and have norm 3r+1=m. Thus a common fiber attains q_m=r+1. The supplement lower bound and sharp residue construction follow. □

For m≤2, q_m=1 and no repair bits are needed. For m=3, q_m=2: **one parity bit of any chosen signed coordinate** is both sufficient and necessary. At m=6, the optimal residue alphabet has three values, not four; its fixed-length binary encoding uses two bits.

Exact finite-hop decoder: reconstruct r from differences supplied by a connected triple-observer graph and set min(r)=0. For candidate integer depth h, let z=r+hD. Check sum_i|r_i+h|≤m and the parity congruence to m, then select the unique feasible depth with (r_1+h) mod q_m equal to the stored residue. A finite candidate interval is -m≤h≤m-max_i r_i. The theorem proves uniqueness. For the known signed action z↦z±e_i and exact hop counter m↦m+1, decoding followed by updating and recoding yields an exact endpoint-state representation. It does not by itself preserve ordered histories on which other transitions may depend.

## Theorem C — exact m=3 loss and BRC multiplicities

There are 12^3=1728 ordered native signed three-step paths. They have exactly **304 distinct signed endpoints** but only **284 joint relative-coordinate observations**. Exactly 20 observation fibers each contain two distinct endpoints:

{H_S, -H_(S^c)} for each 3-subset S of the six axes, where H_S=sum_{i in S} e_i.

Example: (1,1,1,0,0,0) and (0,0,0,-1,-1,-1). Each endpoint of a pair has six ordered three-step realizations; the pair has 12 histories. All other 264 endpoints are singleton relative-coordinate fibers.

The complete positive path-counting BRC classification is:

| Endpoints in joint observer fiber | Ordered paths in fiber | Number of fibers | Total paths |
|---:|---:|---:|---:|
| 1 | 1 | 12 | 12 |
| 1 | 3 | 120 | 360 |
| 1 | 6 | 120 | 720 |
| 1 | 33 | 12 | 396 |
| 2 | 12 | 20 | 240 |
| total | | 284 | 1728 |

Proof: a three-step endpoint has L1 norm 1 or 3. At norm 3, single-axis ±3 gives 12 endpoints and one path each; supports ±2,±1 on two axes give 120 endpoints and three paths each; supports ±1 on three axes give 160 endpoints and six paths each. At norm 1 there are 12 endpoints ±e_i. Each has 3 orderings with same-axis backtracking and 5*6 orderings involving a cancellation on another axis, hence 33 paths each.

If distinct three-step endpoints z,w have the same full joint observation, then z-w=kD with 6|k|≤6. Thus k=±1, and equality in the triangle inequality forces ||z||_1=||w||_1=3. Coordinatewise the difference ±1 then forces complementary 3+3 patterns, yielding exactly the 20 stated pairs. The other endpoints remain separated. Forty support-three endpoints form the 20 pairs, each carrying 6+6 histories; the other 120 support-three states remain singleton. The table follows. □

The parity repair from Theorem B restores these **endpoint** identities. The native BRC ordered paths, sources, signed Port/Link identities and future-relevant updates are distinct carriers that are retained unless an independent scope-typed preservation theorem applies.

## Exact computation and next question

The companion R762BU_X6_BRC_CARRY_FIBERS_VERIFY.js enumerates all 1140 three-panel combinations, verifies 480 connected families and their types, reconstructs all signed endpoint/path counts by exact integer dynamic programming for m=0..9, checks every endpoint's mod-q_m recovery, and at m=3 checks all connected panel signatures against the full twenty-observer quotient. Its JSON output records every observed value; no floating-point approximation is used. The theorem for all m rests on the explicit proofs, not on finite extrapolation.

Next: read the actually admitted signed TRIADIC_CLOSURE_E Cell/Port/Link event predicate and V17/V29/V39 update semigroup at the frozen task pin. Determine whether native events can realize these observer panels and exactly which source, order, time and sign residuals must accompany the minimal endpoint carry. Project review: NOT_REVIEWED.