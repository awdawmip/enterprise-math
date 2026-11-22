# R762JK — Complete 45→43 Port–Euler terminal reduction; conditional uniform k=0 ≤44

Date: 2026-11-22 (Asia/Shanghai).
Frozen scientific input: `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389`.
Model: composite 6-axis Port–Euler observer (15 pair-Ports, 20 triple supports), not signed native P000 triadic dynamics.
Authors' status: **AUTHOR_PROVED / EXACT_FINITE_RECALCULATION / NOT_REVIEWED**.
Predecessors: R762IR@74e40c74cdebeab4e72cc3d814c35386ca060e44 (GF(2) triangle reduction for nonessential supports and t≥11), R762JE@425bc56e0c42277aa063ce8eb94a07ead196415f (conditional uniform ≤45). Both are author-side, not independent mathematical admissions.

## Exact statement and observer

Let the axes be A={0,1,2,3,4,5}; Ports are 2-element subsets of A, supports are 3-element subsets. For support S={a,b,c}, its three allowed event edges join two of the Ports ab,ac,bc. A support-multiplicity vector n∈{0,1,2,3}^20 has N_{p,V}(n)>0 precisely if the selected edges form a connected, nonempty, all-even-degree multigraph with exactly the positive-degree Port set V and a distinguished Euler start p∈V. The observer records V, p, positivity of each support and its count modulo 2.

**Terminal theorem.** For every n with sum(n)=45 and N_{p,V}(n)>0 there exists a triple support j (n_j=3) for which N_{p,V}(n−2e_j)>0. In particular, a **43-event** witness retains the exact active Port set, p, all positive support labels and per-support parity. The new finite portion of this theorem is the 12 low-triple histograms below; the high-triple portion invokes R762IR as an author-proved dependency.

**Conditional uniform bound.** Under R762JE's established author-side ≤45 predecessor, every legal n∈{0,1,2,3}^20 has a witness h≤n of at most **44 events** with the same observer. Take its prior ≤45 witness; when equal to 45, apply the terminal theorem and obtain 43. This is the next author-side bound; it is not independent project acceptance.

## Algebraic completeness of the case split

Write (t,d,s,z) for counts of support labels with multiplicities 3,2,1,0. For 45 events:

    t+d+s+z = 20,    3t+2d+s = 45,
    s = t−5−2z,      d = 25−2t+z.

There are exactly **27** nonnegative integral histograms: **15 with t≥11**, where R762IR's nonessential-triangle reduction applies, and exactly **12 with 5≤t≤10**, listed below. Thus no terminal histogram is omitted.

## Reduction proof for a low-triple histogram

Let T be the t triple supports, M the inactive Ports. If some j∈T has an inactive Port, its three events are confined to the edge between its other two active Ports; deleting two parallel events preserves positive even degrees, support presence, parity and connectivity. Otherwise each triangle of T has all three Ports active.

Form the union of the t full support triangles on all 15 Ports. A triangle is *component-essential* when its deletion increases the number of connected components of this union (isolated Ports are included). If some j is not essential, the original R762IR proof applies: replace the three events of j with one, route the GF(2) parity discrepancy through the retained full-triangle component, reallocate each unchanged triple as a locally connected 3-edge triangle realization, and keep all other allocations. This retains exact degrees mod 2, positivity and connectivity; the cited constructive lemma is an inherited author-side dependency.

For the remaining all-essential T, enumerate every t-subset of the 20 support labels, compute exact component counts before/after each deletion, and reduce the survivors under all 720 S6 axis permutations. The exact orbit representative test exhausts the following additional choices: z absent supports, s singleton supports, and inactive Port sets M disjoint from all T triangles. When z=0 all 20 supports are positive, so M must be a matching of pair-Ports (two inactive Ports sharing an axis would leave a positive support with fewer than two active vertices); enumerate all 76 matchings of sizes 0–3. When z>0 enumerate *all* subsets of the Ports uncovered by T, including nonmatchings, and discard a choice only if a positive support has fewer than two active Ports, which makes any original event impossible.

For each locally eligible (T,Z,L,M), construct a candidate with one j∈T reduced from 3 to 1. The integer program uses 60 nonnegative event-edge counts, 15 degree/2 variables, exact per-support count equations, positive even active degrees, zero inactive degrees, and connectedness cuts as needed. SciPy/HiGHS is only a witness proposer. Every returned allocation is independently checked using **integer** equalities, the degree constraints, a 15-vertex BFS, and total event count **43**. Every enumerated eligible representative produced such an exact verified witness. Any S6 relabeling transports the verified allocation to its labelled family; every active p∈V is a valid Euler start. There is no interpolation, probability assumption or floating-point tolerance in certificate acceptance.

## Locally executed finite check: 2026-11-22

| (t,d,s,z) | All-essential T | S6 orbits | Exact integer witnesses | Labelled (T,Z,L,M) cases |
|---|---:|---:|---:|---:|
| (5,15,0,0) | 14,544 | 39 | 283 | 107,004 |
| (6,13,1,0) | 27,720 | 67 | 4,228 | 1,731,660 |
| (7,11,2,0) | 23,700 | 55 | 10,530 | 4,450,680 |
| (7,12,0,1) | 23,700 | 55 | 1,782 | 750,120 |
| (8,9,3,0) | 4,920 | 16 | 5,500 | 1,518,000 |
| (8,10,1,1) | 4,920 | 16 | 3,311 | 912,780 |
| (9,7,4,0) | 240 | 2 | 990 | 99,000 |
| (9,8,2,1) | 240 | 2 | 1,485 | 148,500 |
| (9,9,0,2) | 240 | 2 | 165 | 16,500 |
| (10,5,5,0) | 6 | 1 | 252 | 1,512 |
| (10,6,3,1) | 6 | 1 | 840 | 5,040 |
| (10,7,1,2) | 6 | 1 | 360 | 2,160 |
| **Total** | | | **29,726 / 29,726 PASS** | **9,742,956** |

The 10,530 checks for (7,11,2,0) were run as two disjoint orbit-index batches [0,25) and [25,55), with 5,928 and 4,602 witnesses. All other rows were executed in complete orbit ranges. For (7,12,0,1) and (8,10,1,1), respectively 363 and 121 locally impossible representative configurations were excluded by the explicit positive-support criterion; none is a purported legal witness. All 29,726 constructed allocations passed 43-event exact integer verification. The reported labelled count weights each orbit representative by its exact S6 orbit size. Numeric witness candidates were generated in the local Python+NumPy+SciPy/HiGHS environment, and the published generator makes each verification independently reproducible. No standalone packed table of 29,726 witnesses is attached; re-execution generates them.

The finite enumeration establishes the theorem at the declared Port–Euler observer, conditional on the prior nonessential-triangle lemma for the nonessential/high-t cases. The derived ≤44 bound additionally depends on R762JE's ≤45 predecessor. Both antecedents are already preserved at their immutable source commits; their mathematical review has not been completed.

## Next problems

1. Classify 44-event terminal configurations for an obstruction to 44→42 or prove the next reduction (which would yield an author-side ≤43 bound from this ≤44 result).
2. Independently audit R762IR's GF(2) reallocation lemma and the R762JA/JE inherited uniform-bound chain. Failure of an inherited assumption changes the dependent strength, not the validity of the exact finite 45-terminal certificates.
3. Preserve the separate native signed P000 Cell/Link/triadic-closure/time and BRC provenance map: the Port-Euler quotient collapses ordered event history and is not yet a residual-faithful native dynamics theorem. The k>0 four-event-support model retains its own bound.

## Control/publication boundary

This file is independent portable scientific evidence, not a formal CLAIM/PROGRESS/Result/Review or a current owner assertion. No modification of frozen scientific pins, P000 or ACTIVE worldview. All results are source-level author proof and reproducible arithmetic evidence pending independent mathematical review.
