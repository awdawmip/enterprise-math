# R5 — Exact nine-state pair quotient and 5,383 f=8 certificates

Status: AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED. Research source evidence, not formal CLAIM, Result, independent Review or native X6 identity equivalence.

## Model and frozen input

Science pin: `435e77af0d180eac32bd1f9c4c464bc4010b7551`; source table `EXACT_R5_ALL_101_BUDGETS.json` SHA256 `50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b`. Each of 256 named states has integer observation center N_h(k) for k=214,...,314, with physical query cost k. Correct real observations have |y-N_h(k)| ≤ τ/2; up to f arbitrary unmarked erroneous responses. L=25845652773852463277015040000 ≤ τ < U=58182461585441404127941754880.

Fix seven named context states H=(18,24,82,34,17,144,208). For each unordered pair x<y outside H use the **ordered nine-slot** game (18,24,82,34,17,x,144,208,y). All nine counters remain independent.

## Theorem 1 — exhaustive endpoint observation quotient

There are C(249,2)=30,876 pairs. At each endpoint τ, classify pairs by their exact ordered vector of inclusion-maximal correct-response support-mask families for all 101 actions. Class sizes:

| Endpoint | Classes | Redundant pair instances | Largest class |
| --- | ---: | ---: | ---: |
| L | 1,460 | 29,416 | 332 |
| U-1 | 2,026 | 28,850 | 308 |

Proof/completeness: for centers c_i, every maximal correct support is realized by a closed center-rooted window [c_j,c_j+τ]. Scan all 9 starts, deduplicate masks and remove proper subsets. Compute the directed relation (c_i≤c_j≤c_i+τ) with exact Python integers from the pinned table. The C++ classifier exhausts all 30,876 pairs and 101 budgets and groups *actual encoded signature strings*, comparing exact bytes (hashing is only indexing, not equality). An independent Python verifier checks the full no-overlap partition, 30,300 window-vs-doubled-endpoint support tests and 8,080 same-class comparisons per endpoint. It returns `PASS_R5_NINE_PAIR_ENDPOINT_QUOTIENT_CROSSCHECK`.

Exact support-signature identity at a given endpoint means identical f-error Bellman transition graphs and forced-first-action costs for **all integers f≥0** at that endpoint, under position-preserving named-slot correspondence. No native state labels are merged.

## Theorem 2 — exact 5,383 nine-state f=8 costs throughout the fifth interval

26 distinct U-1 signature-class representatives were solved with a nine-counter exact integer Bellman recurrence. All 26 return `EXACT cost=8335`. Their *disjoint* endpoint classes contain 5,383 of the 30,876 unordered pairs (17.43%). The full per-class inputs, output, memo state counts and class membership are recorded in `R5_NINE_26_RESULTS.json` and the local reproducibility package.

For every nine-state pair, its eight-state subset H∪{x} has previously verified C_8=8335 for every τ in [L,U). Therefore C_8(H∪{x,y};τ)≥8335. For each member of a solved U-1 class, exact signature identity gives C_8(U-1)=8335. Increasing τ cannot reduce the minimax cost; since the centers are integers, the observation family at all real τ<U is no harder than at U-1. Hence all 5,383 cases satisfy

**C_8(H∪{x,y};τ)=8335 for every real L≤τ<U.**

The full 256-state bound is unchanged: 8335≤C_8(full 256)≤8343.

The recurrence uses counters e_i∈{0,...,9}, with 9 eliminated, and T_S(e)_i=min(9,e_i+1[i∉S]). V(e)=0 when ≤1 slots remain live; otherwise V(e)=min_k(k+max_S V(T_S(e))). A positive-cost query having a self-loop may be omitted from unrestricted minimization. For identical complete support families only the cheapest physical budget is retained. Exact nine-slot masks use uint16_t; all Bellman costs are integers.

## Counterexample — one-slot eight-state equivalence is not stable under extension

The prior 53-class eight-slot quotient identifies x=0 and x=48 for the fixed context (18,24,82,34,17,x,144,208) throughout the fifth interval. Insert z=1 as a ninth named slot. At k=294 and τ=L:

- (18,24,82,34,17,0,144,208,1): maximal masks (511).
- (18,24,82,34,17,48,144,208,1): maximal masks (255,479).
- The original eight-slot signatures at that k and τ both equal (255).

The first nine centers fit within the L-width window, whereas the second has separated x=48 and z=1 extreme centers. Frozen center values N_0(294)=N_1(294)=296770704568869882883347578880 and N_48(294)=342162737216429487140162764800. Independent endpoint scanning verifies the masks. The single-slot contextual quotient cannot be squared without checking x–y joint observation relations.

## Evidence / reproduction / next question

The reproducibility package includes pinned table, the exact forward-matrix generator, exhaustive pair-class C++ program, Python independent verifier, 30,876-pair TSV partitions for each endpoint, nine-counter C++ exact solver, input builder, full 26-run log, JSON results and SHA256 manifest. For a direct reproduction: build the forward matrices from the pinned table; compile `pair_quotient.cpp`; run it for L and U-1; verify with `VERIFY_R5_NINE_PAIR_QUOTIENT.py`; compile `EXACT_NINE_SUBSET.cpp` and run `build_nine.py x y U` for the 26 listed representatives.

Remaining: 2,000 U-1 signature classes, containing 25,493 pairs. A single right-endpoint representative with C_8>8335 would lift the full 256-state lower bound. Alternatively seek a complete 256-state strategy below 8343. Do not rerun the already closed 249 single-state extensions.

Research provenance: `EM-DIRECT-4C3E47`; Activity `RA-F2257922D00B2FE4C4818DBD`; standalone portable research without new CLAIM/RUN. Mathematical independent review: NOT_REVIEWED.
