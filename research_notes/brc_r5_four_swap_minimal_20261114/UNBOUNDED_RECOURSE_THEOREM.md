# R5 — Unbounded worst-case recourse after closing one length-three gap

Date: 2026-11-14. Status: AUTHOR_PROVED, EXACT_INTEGER_CHECKED (K=2..50), NOT_REVIEWED. Scientific provenance: frozen R5 input `435e77af0d180eac32bd1f9c4c464bc4010b7551`; derived 1-D integer event-index center observer as in `research_notes/brc_r5_reconfiguration_20261114/RESEARCH.md` at `dcc59506f4282d8ae521dc5dc428402ec2999010`. The present theorem concerns a general finite family **not asserted to occur in the frozen 954-event instance**.

## Theorem (arbitrarily large recourse, one single-gap closure, unchanged optimum cost)

Fix any integer K >= 2. Let n=3K-2 and, indexing events by 0,...,n-1, put

```
x = (0,3,5,6,7,...,n+2)
y = (0,2,4,5,6,...,n+1).
```

These are strictly increasing integer event coordinates; the original consecutive steps are 3, 2, then 1 repeatedly. The only operation from x to y closes **the first** gap 3 to 2, translating later coordinates by -1, while preserving event labels. The covering radius is exactly 2. Every center is selected from event indices; for a K-element center subset U, feasibility is `max_i min_{j in U}|z_i-z_j|<=2` and its cost is `C_z(U)=sum_i min_{j in U}|z_i-z_j|`.

Define the two K-index center sets

```
T_K = {0,2,5,8,...,3K-4};  (unique old optimum)
S_K = {1,3,6,9,...,3K-3}. (a new optimum)
```

Then

```
Opt_x(K) = { T_K },   J_x(K)=J_y(K)=2K-1,
S_K in Opt_y(K),       T_K intersection S_K = empty,
rho_x(S_K;K) = min_{U in Opt_x(K)} |S_K\U| = K.
```

Consequently, for fixed radius 2, the steps {1,2,3}, exactly ONE gap shortening from 3 to 2 and NO change in minimum total cost, **there is no K-independent bound** on how many center replacements an arbitrarily chosen newly admitted optimum can require to return to the old optimal family. This is stronger than the nine-event minimal four-replacement witness proved in the accompanying RESEARCH.md.

## Proof

1. **Universal integer baseline.** With n distinct integer coordinates and K chosen event-index centers, exactly n-K noncenter events lie at distance at least one from every center. Thus C_z(U)>=n-K=2K-2. Equality would require every noncenter event to lie at distance exactly one from a selected center.

2. **Old lower bound.** In x, event 0 at coordinate 0 is more than radius two from every other event (the next coordinate is 3). It is a mandatory center in every feasible solution. If cost attained the integer baseline 2K-2, all noncenters would have distance one. Event 1 at coordinate 3 has **no** other event at distance one (neighbors at coordinates 0 and 5), so event 1 must also be selected. The remaining tail of 3K-4 events (indices 2,...,n-1, at coordinates 5,6,...,n+2) is beyond distance one from both first centers. With only K-2 remaining centers, each covering at most three consecutive tail events within distance one, at most 3K-6 tail events can attain distance at most one. This contradicts 3K-4>3K-6. Therefore J_x(K)>=2K-1.

3. **Old uniqueness at equality.** Suppose C_x(U)=2K-1. The center at index 0 remains mandatory. If index 1 were also selected, the same tail counting would force at least TWO tail noncenter events to have distance at least two. Their two units of excess over the integer baseline would imply cost >=2K, a contradiction. Thus index 1 is not selected, and, to cover it within radius two, index 2 (coordinate 5) is mandatory. Its distance is exactly two, using up the only excess unit above the baseline. Every other noncenter event must therefore have distance one. Event index 3 at coordinate 6 is covered by selected index 2, while the **remaining tail indices 4,...,n-1** number n-4=3K-6=3(K-2). They must be covered within distance one using precisely K-2 remaining centers. Since each center can cover at most three such unit-spaced tail indices, these centers must partition the tail into consecutive blocks of three. The first block {4,5,6} forces center 5; the next {7,8,9} forces center 8; and so on, ending at 3K-4. Therefore U=T_K uniquely. Directly, event 1 contributes distance two and every other noncenter contributes distance one, so T_K is feasible and C_x(T_K)=2K-1. This proves uniqueness and the exact old optimum.

4. **New lower bound.** In y, to achieve the integer baseline, events 0 (coordinate 0) and 1 (coordinate 2) each must be centers: neither has another event at distance one. With these two selected, the tail indices 2,...,n-1 at coordinates 4,5,...,n+1 again contain 3K-4 events; neither first center lies within distance one of any tail event. The other K-2 centers cover at most 3K-6 tail events within distance one. Hence J_y(K)>=2K-1.

5. **New attainment and disjointness.** The explicitly listed S_K covers y within radius two. It leaves event 0 at distance two and has all other noncenters at distance one, so C_y(S_K)=2K-1. The T_K indices are {0} together with 2 modulo 3, while S_K indices are {1} together with 0 modulo 3 starting at 3; they are disjoint. Since the entire old optimal family consists solely of T_K, `rho_x(S_K;K)=|S_K\T_K|=K`. QED.

The proof also covers the boundary K=2 (n=4). It uses integer distances, single-cut coordinates, the radius-two constraint, and event-index centers; it neither relies on a floating-point approximation nor infers a universal property of native X6 from this derived one-dimensional model.

## Reproduction and scope

Run `python3 VERIFY_UNBOUNDED_FAMILY.py > output.json`. The standalone program independently implements a sparse edge-path integer DP with complete cost-optimum counts and lexicographic maximum overlap, checks K=2..50 (n up to 148), and directly enumerates all K-subsets for K=2..6. Every tested case returned unique old optimum, cost `2K-1` at both endpoints, max old-optimum overlap with S equal to zero, and `rho=K`. The code was actually executed; the general-all-K theorem rests on the combinatorial proof above, **not** on the finite K<=50 check. Exact finite results are summarized in `EXACT_UNBOUNDED_FAMILY.json`. No independent review/Lean proof or formal Result acceptance is asserted.

## Next scientific question

Classify which additional restrictions on the event geometry, unique optimal centers, or boundary conditions restore a **uniform** reconfiguration bound; and, independently, calculate `max_{S in Opt_{B+i}(K)} min_{T in Opt_B(K)} |S\T|` for the actual frozen 954-event R5 gaps 15 and 17 across applicable budgets/backgrounds. The latter is an exact finite case, not an automatic corollary of the unrestricted family.
