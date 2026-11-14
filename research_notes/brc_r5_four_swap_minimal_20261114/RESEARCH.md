# R5: four-center recourse is possible after a single gap closure, and nine events are minimal

Date: 2026-11-14. Derived observer: one-dimensional strictly increasing **integer** event coordinates, consecutive gaps in {1,2,3}, radius-two nearest-index-center cover, exact total nearest-center distance. Frozen project-science lineage: `435e77af0d180eac32bd1f9c4c464bc4010b7551`. Prior R5 recourse definition and the exact lexicographic dynamic program: `research_notes/brc_r5_reconfiguration_20261114/RESEARCH.md` at `dcc59506f4282d8ae521dc5dc428402ec2999010`. This note proves an auxiliary finite-domain obstruction; it does **not** assert the four-swap obstruction occurs in the 954-event frozen R5 instance. Status: AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED.

## Proposition and quantifiers

Let `x=(x_0<...<x_{n-1})` have successive gaps in {1,2,3}. Let `y` be formed by replacing **one** gap of length 3 by 2, translating all event coordinates after that gap by -1, without relabelling event indices. For a center budget K, let `Opt_x(K)` denote all feasible K-element event-index center sets minimizing `C_x(T)=sum_i min_{j in T}|x_i-x_j|`, with feasibility `max_i min_{j in T}|x_i-x_j|<=2`. For `S in Opt_y(K)`, define `rho_x(S;K)=min_{T in Opt_x(K)} |S\T|`. Consider only cases where `J_x(K)=J_y(K)<+infinity`.

**Theorem (first four-replacement obstruction).** Among all such one-gap transitions with n<=8, every new optimum S obeys `rho_x(S;K)<=3`. At n=9 there exists a transition with the same optimal total cost but a new optimum requiring **four** replacements. Thus nine events is the smallest possible n for four-replacement recovery in the declared step-{1,2,3}, radius-two, single-gap, cost-preserving setting. In the further enumerated range n<=10, the largest rho is 4.

## Exact nine-event witness

Take

```
x = (0,3,5,6,8,10,12,13,15)
y = (0,2,4,5,7,9,11,12,14)
K = 4; gap closed = index 0 (zero-based)
```

By direct enumeration of the C(9,4)=126 four-center subsets (radius-two feasibility and integer cost), the **complete old optimal family** is

```
Opt_x(4) = {{0,2,4,7}, {0,2,5,7}},   J_x(4)=8.
```

The complete new optimum family has ten sets, including `S={1,3,6,8}`, and `J_y(4)=8`. The distance vectors for the old representatives are, respectively,
`(0,2,0,1,0,2,1,0,2)` and `(0,2,0,1,2,0,1,0,2)`, both summing to 8 and with maximum 2. Under y, S has distance vector `(2,0,1,0,2,2,0,1,0)`, summing to 8 with maximum 2. Under x the same S has distance vector `(3,0,1,0,2,2,0,1,0)`, so it is infeasible. Both old optimum sets are disjoint from S. Hence

```
rho_x(S;4) = 4,  although J_x(4) = J_y(4) = 8.
```

The entire new optimum family at this witness is
`{0,2,4,7}, {0,2,5,7}, {0,3,4,7}, {0,3,5,7}, {0,3,6,8}, {1,2,4,7}, {1,2,5,7}, {1,3,4,7}, {1,3,5,7}, {1,3,6,8}`.

## Finite exhaustion certificate and independent witness check

The accompanying standalone C++17 program enumerates **all** `3^(n-1)` gap words for every n from 2 to 10, each occurrence of gap 3 as a closure, every nonempty event-index subset as a candidate center set, and all K with unchanged finite old/new optimum costs. Every `S in Opt_y(K)` is compared with the entire `Opt_x(K)` via exact bit intersections. There is no sampling, floating point or theoretical bound extrapolated beyond n<=10.

The exact maxima, by n=2,3,4,5,6,7,8,9,10, are

```
(0,1,2,2,2,3,3,4,4)
```

The transition counts are `(1,6,27,108,405,1458,5103,17496,59049)`, total `83653`. The number of newly optimal K-sets explicitly compared is `4,263,983`, partitioned by n as `(1,16,131,826,4771,25944,135793,687790,3408711)`. Each transition count also independently follows from `(n-1)*3^(n-2)` since a designated gap must be 3 and the remaining n-2 gaps have three choices.

Each feasible subset is scored using its complete nearest-center distance vector; the minimum is selected per budget, and in a cost-preserving transition every newly optimal subset is compared with every old optimum (early exit is allowed only upon overlap K, which proves rho=0). This direct finite enumeration is an exact proof of the n<=8 part **conditional on correct execution of the provided elementary program**. The explicit n=9 witness admits a separate 126-subset hand-check or implementation-independent enumeration and is not dependent on the whole search. For n=8 the elementary cardinality bound alone is insufficient: disjoint four-subsets fit in eight indices, and the exhaustive model-specific exclusion is necessary.

The C++ enumerator compiled with `g++ -std=c++17 -O3` and executed locally through n=10. Independent Python `itertools.combinations` recomputation of the nine-event witness recovered the exact two old and ten new optimal K=4 sets, confirming `rho=4`. The resulting tabulation is in `EXACT_OUTPUT.json`.

## Meaning and next test

Earlier R5 evidence already proved a necessary two-swap example at n=4, and three-swap at n=7. This increment **invalidates any universal upper bound of three** replacements for a single closed gap, even when optimal total cost is unchanged. It does not show an unbounded replacement distance or establish the behavior for n>10, nor does it compute the max-min recourse of frozen gaps 15/17 across all 954-event backgrounds.

Next discriminating research: for n>=11, seek a constructive family with unbounded rho or prove a universal finite upper bound, preserving `max_{S in Opt_y} min_{T in Opt_x}` quantifier order; separately determine its corresponding frozen-R5 17-variable quotient. Do not confuse existence of a one-swap witness with recovery of every newly optimal configuration.

No protected ontology, original task input, Source CLAIM, Result or independent review was changed.
