# R5 — Sharp adaptive unmarked-error costs in the first three positive-noise chambers

Date: 2026-11-17 (Asia/Shanghai). Frozen scientific pin: `435e77af0d180eac32bd1f9c4c464bc4010b7551`.
Status: AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED. This is the **derived 954-event scalar integer observer** with 256 effective closure masks and budgets 214–314, not an asserted native X6/BRC equivalence.

## Theorem (new)

An adaptive observer may query any integer budget 214≤k≤314, each query costing k, and must identify its mask despite at most f unmarked arbitrary real-valued corruptions. Intact observations are any real y satisfying |y−N_b(k)|≤eta. Let tau=2eta. For every integer f=0,...,20, the **exact minimum worst-case sum of queried budgets**, over adaptive strategies, is

| Inclusive tau lower bound | Exclusive tau upper bound | Optimal cost | Explicit ordered query budgets |
|---:|---:|---:|---|
| 0 | 76289178155959966960189440 | 731+945f | (294,223,214) |
| 76289178155959966960189440 | 3133722521542003559403356160 | 732+946f | (295,223,214) |
| 3133722521542003559403356160 | 13883516118328421520506880000 | 733+947f | (296,223,214) |

The constructed strategy provides the corresponding displayed formula as a **valid upper bound for every integer f≥0**. Matching sharp lower bounds are computationally certified here for all f≤20, inclusive. In particular the new f=1 values in the second and third chambers are 1678 and 1680, while the new f=20 values are 19652 and 19673.

## Upper proof — exact center decoding and adaptive confidence

For each row, write the ascending budgets (a,b,c) with a=214, b=223, c∈{294,295,296}. Exact integer inspection of all 256 masks establishes:
1. At each selected budget, **distinct** count centers have minimum adjacent gap at least the row's exclusive upper tau bound. Thus the closed eta-intervals of distinct centers are disjoint throughout the entire stated half-open chamber; every intact response decodes to its unique true center.
2. The three exact count centers jointly separate all 256 states, with minimum over distinct mask pairs of the maximum three-budget count difference equal to the upper tau endpoint in each chamber.

Query in descending order c,b,a. Given r remaining possible corruptions, sample a budget until a decoded symbol (or OTHER) has appeared r+1 times. At most r observations can be corrupt, so that symbol is necessarily the genuine center. If t responses were not that symbol, t errors have been spent, and the next budget starts with r−t remaining allowance. This step takes r+1+t observations.

For the remaining ordered budgets k_i,...,k_3 define F(i,r) as the maximum future sum for this strategy. The exact recurrence is
`F(i,r)=max_{0≤t≤r} ((r+1+t)k_i + F(i+1,r−t))`, with F(4,r)=0.
Since b≤2a and c≤b+2a, backward substitution shows the maximum at t=0 at the two earlier stages, giving `F(1,f)=S+f(S+a)` for S=a+b+c. This proves all-f constructive correctness and the three upper bounds.

## Lower proof — four-mask adversarial Bellman game

Restrict the adversary to four exact masks `H=(16,17,80,32)`, with mask 16 the base. The three alternatives have differences from base in disjoint source-budget windows (at each inclusive chamber lower endpoint):
- mask 17: 214–221, cheapest distinguishing budget 214;
- mask 80: 223–291 for stages 1–2, 223–290 for stage 3, cheapest 223;
- mask 32: 294–313 (stage 1), 295–313 (stage 2), or 296–313 (stage 3), cheapest respectively 294,295,296.

**Monotonicity within a chamber:** the lower-bound game is certified at its inclusive left boundary τ=L. For any larger τ in that chamber, every reading permitted at L is still permitted, so the same adversarial strategy remains a valid lower bound; no claim of unchanged full strong-window support at all intermediate τ is needed. At a budget where a leaf's error intervals intersect those of the base, the adversary can choose a common intact reading. Such queries cannot improve the worst-case lower bound. At a strongly distinguishing budget in one window, the other three star states have the same center; it implements one binary test of the associated leaf. An adversary may return either true center or an arbitrary third symbol. Any candidate strategy for the full 256-state problem therefore induces a strategy for this 4-mask star at no lower cost than its cheapest three tests.

For a cap `f+1`, retain the vector d_h of mismatches to each star hypothesis, clipped at f+1. Candidate h survives iff d_h≤f. On querying leaf j and receiving answer a∈{0,1,2}, update
`T_j(d,a)_h=min(f+1,d_h+1[a != 1[h==j]])`.
The exact Bellman value is 0 if at most one candidate survives, otherwise
`V_f(d)=min_{productive j}(k_j + max_{feasible a} V_f(T_j(d,a)))`.
An action with an admissible self-loop can be discarded from a finite worst-case optimum. Every remaining transition increases a finite capped mismatch vector, so this dynamic program is a complete exhaustive finite minimax certificate.

The executed exact Python verifier enumerated the whole Bellman state family separately for every integer f=0..20 in **each of all three chambers**, and found
`V_f(0,0,0,0)=S+f(S+214)`.
At f=20 there are **156,331** cached states per chamber. These lower bounds match the upper construction, establishing the stated exact optima.

## Validation, inputs and scientific scope

Local actually executed command:
`python VERIFY_R5_FIRST3_CHAMBERS_ADAPTIVE_F0_F20.py --full-table EXACT_R5_ALL_101_BUDGETS.json`.
Actual result: `PASS_R5_FIRST_THREE_NOISE_CHAMBERS_ADAPTIVE_F0_TO_F20`; runtime about 23 s on the local execution host. Exact arithmetic checks 25,856 count values (101×256) against the compact source witness, all 32,640 unordered pairs for each of three budget triples, 101 witness budgets, minimum distinct-center gaps and 63 complete Bellman evaluations.

Frozen original 101-budget table SHA-256:
`50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b`.
The full prior verified reproduction input is preserved in the 2026-11-17 R5 adaptive-unmarked-errors reproduction archive; the compact witness extraction and exact results accompany this note. The full source is derived from the prior fixed pinned R5 input. Program and compact certificate retain that pin, not the current mutable Source head.

**Frontier:** The fourth chamber starts at tau=13883516118328421520506880000. Here the same base/leaf witness still distinguishes mask16 from17 at budget 214, whereas the best noiseless-fault fixed tuple already uses 215. Consequently the simple three-leaf witness ceases to match that chamber's full lower cost; resolve its additional interacting state-pair obstruction with an adaptive high-noise Bellman formulation. A universal proof or falsifier for the all-f formula beyond 20 also remains open.

Researcher provenance in the predecessor R5 line: `EM-DIRECT-C52C70`, Activity `RA-E56F584D739D86CC48916236`. This note does not assert a newly authenticated formal R5 CLAIM, native Result, or independent mathematical review.
