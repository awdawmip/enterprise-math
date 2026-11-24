# R5: exponentially many switch-only joint optimizers without forced individual appended centers

2026-11-15 | AUTHOR_PROVED / EXACT_FINITE_CHECKED (m=0..6) / NOT_REVIEWED.

Scientific input remains frozen at `435e77af0d180eac32bd1f9c4c464bc4010b7551`. Base geometric construction: [N5_SWITCH_ONLY_Q_GEOMETRIC_THEOREM.md](../r5_future_residual_and_two_cut_order_20261115/N5_SWITCH_ONLY_Q_GEOMETRIC_THEOREM.md) at commit `d731c412868157a600ce0175527bf93f3873d5c4`. This is an *auxiliary one-dimensional integer observer*, not a native X6 result.

## Theorem and exact domain

For each integer m>=0, let n=5+2m ordered events have consecutive gaps (3,2,2,3,(3,1)^m). Contract the zero-based gaps a=0 and b=3 independently from length 3 to length 2. Choose exactly K=3+m center indices, cover every indexed event within radius rho=2 and minimize the sum of nearest-center integer distances. Let F0,Fa,Fb,Fab be the complete optimizer families under the four masks.

For j=0,...,m-1, let C_j={5+2j,6+2j}, and let H_m be the family of sets picking **exactly one index of each C_j**. Thus |H_m|=2^m. Define F_t^base for m=0, writing e.g. 024 for {0,2,4}:

- F0^base = {024}
- Fa^base = {024,034,124,134}
- Fb^base = {013,014,023,024}
- Fab^base = {013,014,023,024,034,123,124,134}.

For every m and every mask t:

1. **Exact family factorization:** F_t(m)={S union H : S in F_t^base, H in H_m}, with optimum J_t(m)=4+m.
2. **Exponentially growing residual:** P=(Fa intersect Fb) minus F0 is empty, whereas Q=Fab minus (Fa union Fb) is exactly {{1,2,3} union H : H in H_m}. Hence |Q|=2^m. The four optimizer counts are (2^m,4*2^m,4*2^m,8*2^m).
3. **No new joint arcs:** Build increasing-index optimal-center paths and label each arc by its center rank and endpoint indices, including start/sink arcs. Writing E_t for the union of the arcs of all F_t paths, E_ab(m)=E_a(m) union E_b(m). Every joint-only optimizer is obtained by switching existing singly-admissible arcs.
4. **No individually forced appended index:** For m>=1 and every j, either member of C_j occurs in exactly half of each optimizer family. The total number of events and chosen centers grows without bound, while every original gap is at most 3.

## Proof: coverage and strict center-budget accounting

The first appended pair is separated from the five-event prefix by a gap 3; consecutive appended pairs are likewise separated by gap 3. Contractions a,b lie *inside the prefix*, so all separators remain length 3 under every mask. Coverage radius 2 makes it impossible for an indexed center from one block to cover events in another block. Consequently each pair C_j needs at least one center. A pair with one center contributes exact nearest-center cost 1 (either member can be chosen); with two centers it contributes 0. For any globally feasible center set, each block's nearest distances depend only on its own centers.

In the base block with three centers, exhaustive evaluation of C(5,3)=10 candidate index sets under each mask yields the four complete families above, all with optimum cost 4. The base block with fewer than two centers is infeasible under every mask. With exactly two centers, it is infeasible under 0,a,b; under ab its exact optimum is cost 6, attained for example by {1,3}. All these finite claims are rechecked by the accompanying exact verifier.

The global budget K=3+m, with at least one center per appended pair, allows at most three prefix centers. Three prefix centers force one per pair; their optimal cost is 4+m and the complete optimizer family is exactly F_t^base times H_m. Two prefix centers are feasible only for ab. For m=0 they cannot exhaust the exact K=3 budget. For m>=1 there are m+1 centers for m pairs: one pair receives two and every other pair receives one, so the total cost is at least 6+(m-1)=m+5, strictly worse than 4+m. Thus every global optimum uses three prefix centers, proving item 1 for all m.

For the P/Q formula, the supports of S and H are disjoint, and the map (S,H) -> S union H is injective. Its second factor H_m is identical in all masks. Intersections, unions and set differences of the four optimizer families therefore commute with extension by H_m. The base has P=empty and Q={{1,2,3}}, giving item 2.

For arc equality, m=0 is the verified five-event base property E_ab=E_a union E_b. When m>0, extended paths have (i) base start and internal arcs; (ii) one boundary arc from base's last center to the first appended center; (iii) suffix-internal and terminal arcs. The base internal arc sets preserve union by the m=0 identity. Boundary arc support is the Cartesian product of the possible base-last indices and the two possible first appended centers; base-last-index support is read exactly from the base terminal arcs, so this also preserves union. All later suffix arcs are identical across masks, since each nonempty base path combines with all H_m. Therefore E_ab(m)=E_a(m) union E_b(m) for all m. Since each pair's two choices occur symmetrically and independently, item 4 follows.

## Executed reproducibility / scope

Run `python VERIFY_R5_PAIR_BLOCK_SWITCH_FAMILY.py > EXACT_R5_PAIR_BLOCK_FINITE_CHECKS.json`. The independent standard-library checker enumerates **all** C(n,K) center choices in each of four masks for m=0..6, checking coverage, exact integer cost, entire optimizer-family factorization, P/Q and rank-labeled arc supports. Observed status: `PASS_R5_NONISOLATING_PAIR_BLOCK_FAMILY`. At m=6: n=17, K=9, J=10, optimizer counts [64,256,256,512], |Q|=64. The arbitrary-m theorem follows from the proof above, not from finite sampling.

This strengthens the preceding forced-isolated-center extension: here no appended **index** is forced, and the number of joint-only optimizers grows exponentially. The construction still has radius-separated *blocks*. A geometrically connected non-block-separable unbounded construction, or a structural explanation for why the frozen 954-event cuts 8,9 forbid mixed-color paths, remains an open research problem.

No formal Task/CLAIM/Result/Review authority is asserted by this independent portable research note.
