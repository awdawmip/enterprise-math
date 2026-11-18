# R5 — weighted optimal interior probes and exact endpoint-inclusive cost

Date: 2026-11-19. Scientific status: AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED.
Researcher provenance: EM-DIRECT-4C3E47, Activity RA-F2257922D00B2FE4C4818DBD.
Mode: independent portable continuation; no new formal CLAIM/RUN, Result, Review or native X6 assertion.

## Frozen inputs and predecessors

Frozen scientific source: `awdawmip/enterprise-math@435e77af0d180eac32bd1f9c4c464bc4010b7551`.
- `EXACT_R5_ALL_101_BUDGETS.json` SHA256 `50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b`;
- `interior_distinguishing_budget_witnesses.csv` SHA256 `3d2706270c490433b7c6fab8a4b606b570e771c27e35aed37260969225bacc32`;
- `stages_18.json` SHA256 `effa71cba1dd2811acc4593944b4af096db791612c25d8825aa01c388af54164`.
Original predecessor (fixed all-interval signatures): `a661f387ef8819ef95a7121d4e73e6b677f64ee5`.
Conditional 0/1/2 probes: `e4924e897e69b87e8ffe59a12ac3562d03e839f1`.
Adaptive uniform prior: `c9f75913e888ef568e16dee00f670adeddc26542`.

Domain: all `C(249,2)=30,876` named nine-slot pair instances `(18,24,82,34,17,x,144,208,y)`, `x<y` outside the fixed seven, 101 budgets `k=214,...,314`, and 18 exhaustive exact integer noise thresholds. The per-probe output is the complete indexed maximal-support tuple. The endpoint-equivalence class is given before optional interior probes, with the correct, preverified endpoint-to-full-class dictionary. The probe decision tree must distinguish every feasible full-interval daughter, including zero-prior daughters.

## Theorem 1 — exact available two-cut structure

For all 40 three-daughter endpoint-equivalence classes in the frozen population, let the three daughters be ordered `D0, D1, D2` so that stage-4 budget-214 separates `D0 | (D1,D2)`, while stage-8 budget-214 separates `(D0,D1) | D2`. Then across **all** 101 budgets and **all** 18 stages, every one-probe partition is one of exactly:

1. trivial, `(D0,D1,D2)`;
2. left cut, `D0 | (D1,D2)` — and only `(k=214, stage j=4,5,6,7)`;
3. right cut, `(D0,D1) | D2` — and only `(k=214, stage j=8,...,15)`.

In particular **no** allowed one-probe action isolates the middle daughter `D1`, and no allowed action gives a three-way split. All three-daughter classes have equal daughter sizes: 16 classes have `(1,1,1)`, and 24 have `(2,2,2)` (40 classes, 192 instance-members total).

Proof: reconstruct the 108 connected endpoint components from the immutable 620 cross-daughter witness edges. For each three-daughter class, use exact integer centers from the frozen table. At every `(k,j)`, enumerate closed windows `[left,left+tau_j]` over the nine centers, delete non-maximal indexed sets, and group the three daughter representatives by their tuple of maximal-support masks. The checker compares every resulting partition to the three listed templates, verifies the exact stage sets and daughter multiplicities, and rejects a one-action ternary or middle-isolating partition. The finite domain is exhausted by `40*101*18=72,720` class/action/stage comparisons; closed-window integer evaluations avoid floating point.

## Theorem 2 — arbitrary-prior optimal expected cost

Fix one of the forty three-daughter classes. Let `(p0,p1,p2)` be any nonnegative prior masses summing to one. Every valid decision tree must remain correct on all three daughters irrespective of prior probability. Then the minimum expected *additional* interior-probe cost is

`E*(p0,p1,p2) = 2 - max(p0,p2)`.

One optimal tree first makes stage-4 / k214 probe if `p0>=p2` (thus isolates `D0`), or stage-8 / k214 probe otherwise (thus isolates `D2`). If it hits the singleton daughter, stop; if not, make the other probe and stop.

Proof: theorem 1 excludes a one-action terminal distinction of all daughters and excludes isolating `D1`. The first informative action can only isolate `D0` or `D2`; the complementary pair requires a second informative action under a correctness-for-all-daughters criterion. Hence a first probe isolating `Di` has expected cost `1+(1-p_i)=2-p_i`. Minimizing over `i=0,2` proves the formula and attainability. Any trivial first probe cannot improve this optimum.

Consequences:
- uniform daughters: `5/3` (reproduces the previous certificate);
- middle-heavy prior `(1/6, 2/3, 1/6)`: `11/6`;
- left-heavy prior `(2/3, 1/6, 1/6)`: `4/3`.

The loss relative to a hypothetical action that could isolate whichever daughter is largest is precisely `max(0, p1-max(p0,p2))`. This quantifies the observational residual: middle-daughter distinctions require composition of two cuts.

## Theorem 3 — explicit endpoint-inclusive workload of the specified method

Count one unit for one exact nine-slot maximal-support-family signature evaluation at a fixed `(k,tau)`; do **not** identify this with a physical Bellman query or with runtime. For all 30,876 frozen candidates:

| Defined computational plan | Exact number of signatures |
| --- | ---: |
| all 18 stages, all 101 budgets, all instances (naive exhaustive census) | 56,132,568 |
| both endpoints, all 101 budgets, all instances | 6,236,952 |
| conditional fixed 0/1/2 *additional* probes (total) | 640 |
| uniform-prior adaptive 0/1/2 *expected additional* probes (total) | 576 |
| specified endpoint-inclusive conditional fixed total | 6,237,592 |
| specified endpoint-inclusive adaptive expected total | 6,237,528 |

Arithmetic: `2*101*30876=6,236,952`, `18*101*30876=56,132,568`, `256+2*192=640`; using all equal-sized three-daughter class priors, `256+192*(5/3)=576`. The 64-probe saving is `64/6,237,592 = 8/779699`, or about **0.001026%** of the fixed endpoint-inclusive computation, versus 10% of additional probes alone.

The complete 18-stage oracle sweep uses `56,132,568/6,237,528 = 2,338,857/259,897` times the adaptive endpoint-inclusive expected signature count (about 8.99917), **conditional on already having a sound dictionary from endpoint class to correct interior decision plan**. Building, validating, caching, comparing and applying that dictionary has separate costs not included in this count. Reusing a fully materialized lookup table for exactly the same fixed instance population permits zero new support-signature calls: index lookup, storage, and table construction then dominate the accounting. A genuinely new oracle/input population requires its own evidence that the precomputed structural partition dictionary remains valid.

## Evidence and exact verification

`VERIFY_WEIGHTED_PROBES_AND_COST.py` is an independently authored Python 3 exact-integer enumerator using the three predecessor data files above; it reconstructs all 108 split components and enumerates every allowed probe for each three-daughter component. Reproduction on the frozen data returned:

`PASS_WEIGHTED_PROBES_AND_COST 40 219072 5/3 11/6 4/3 6236952 56132568 576 6237528`.

`RESULT_WEIGHTED_PROBES_AND_COST.json` preserves the exact counts, prior test cases, sample class witnesses, original input hashes, the full 40-anchor-list digest and workload assumptions. Source files and computed output remain author-checked; independent review remains `NOT_REVIEWED`.

## Open research frontier

1. For a new dataset, characterize exactly when the 40-class two-cut pattern and endpoint-class dictionary transport; preserve named-slot residuals and potential new internal split classes.
2. Measure actual wall time, integer precision, memory, signature generation, endpoint-dictionary construction and lookup costs before claiming speedups in an implementation.
3. Continue unresolved nine-state `C8>8335` lower-bound search independently of this observer-classification postprocessing. The full 256-state eight-error Bellman bounds remain `8335 <= C8* <= 8343`.

This note only concerns frozen indexed scalar observer signatures. It asserts no native X6 equivalence, BRC information-preserving map, formal RESULT freeze or mathematical review.
