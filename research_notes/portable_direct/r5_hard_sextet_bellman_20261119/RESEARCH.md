# R5: Exact native six-hypothesis Bellman certificate and 64 hard quartets

Date: 2026-11-19 (Asia/Shanghai). Scientific status: AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED. Independent portable research; no formal CLAIM, RUN, native Result or independent Review.

## Exact frozen input and scope

Unchanged science pin: awdawmip/enterprise-math@435e77af0d180eac32bd1f9c4c464bc4010b7551. Source EXACT_R5_ALL_101_BUDGETS.json, SHA-256 50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b. The scalar game has 256 separately named integer center sequences N_h(k), 101 physical query budgets k=214..314 (query cost k), correct real observations 2|y-N_h(k)| <= tau and at most f arbitrary unmarked errors. Robust endpoint tau*=U-1, U=58182461585441404127941754880. Existing exact open-envelope theorem shows the same worst-case game for unknown query-varying tau in [L,U). This result concerns the scalar observation readout and does not quotient native X6, Port, branch or provenance data.

## Result 1 — Exact six-state eight-error cost 8300

Select the named ordered subset H=(0,16,32,48,1,64). For a query k let F_k be the inclusion-maximal response supports in H; a bitmask's i-th bit names H[i]. Maximal supports suffice for minimax play: enlarging a correct-response support never makes the residual named-hypothesis identification game easier. Reconstructing maximal sets by (i) exact center-diameter windows and (ii) doubled real-interval endpoint sweeps gives identical families for all 101 actions.

All 101 physical actions are in exactly five families distinguished by their maximal support masks. The cheapest representatives and masks are:

| Cheapest action | Maximal response-support masks (decimal) |
| ---: | --- |
| 214 | 16, 47 |
| 222 | 63 (unhelpful full support) |
| 223 | 31, 32 |
| 295 | 6, 8, 49 |
| 296 | 2, 4, 8, 49 |

An action with only full support cannot force progress. Equal-family more expensive actions can be eliminated exactly. Consequently it suffices to solve the four-action game K={214,223,295,296}. This is a complete *six-hypothesis* reduction of the 101 physical actions, not a full 256-state action elimination.

Set e_i in {0,...,f+1} to the minimum mismatch count capped at f+1, with e_i<=f meaning that named hypothesis is live. For maximal mask S, let e[S]_i=min(f+1,e_i+1_{i not in S}). The exact Bellman recurrence is

    V_f(e) = 0                                            if at most one e_i <= f;
    V_f(e) = min_{k in K without a full-live support}
                  [ k + max_{S in F_k} V_f(e[S]) ]         otherwise.

An action admitting a full-live support permits an unchanged residual state, so it cannot be optimal for positive physical cost. Every other transition strictly increments at least one currently live mismatch counter. Thus the finite recursion is acyclic; complete memoization proves the fixed-f minimax value.

With f=8 at e=(0,0,0,0,0,0), the exact result is

    V_8(H) = 8300.

Root action upper/worst-branch values: k214 -> 8300; k223 -> 8300; k295 -> 8300; k296 -> 8301. The first three actions are optimal. Python cached 80,455 states including terminal states; independently implemented C++ cached 80,400 nonterminal states. Both computed the same root and all twelve values below.

Exact complete enumerations for 0<=f<=11:

| f | V_f(H) |
| ---: | ---: |
| 0 | 732 |
| 1 | 1678 |
| 2 | 2624 |
| 3 | 3570 |
| 4 | 4516 |
| 5 | 5462 |
| 6 | 6408 |
| 7 | 7354 |
| 8 | 8300 |
| 9 | 9246 |
| 10 | 10192 |
| 11 | 11138 |

All twelve match 732+946 f; extending that affine pattern to every f is an OPEN QUESTION, not established by finite computation.

## Result 2 — 64 disjoint hard quartets, exact for every f

For b=0..3 and a=0..15, define

    Q(b,a)={64b+a,64b+a+16,64b+a+32,64b+a+48}.

These are 64 pairwise disjoint four-hypothesis subsets covering all 256 labels. At every real tau in [L,U), physical action k=296 has pairwise disjoint correct-observation intervals on all four labels in each quartet, while at least one pair in each quartet has NO separating physical action cheaper than 296. There are only 18 threshold chambers because all pairwise integer center gaps within the allowed tau range have 17 critical thresholds. The frozen input verifies the assertion for 64*18=1152 chamber-cohort combinations, plus 64 robust endpoints.

The hard pair lower bound is 296*(2f+1). Repeating action 296 exactly 2f+1 times identifies the correct quartet label by strict majority even with f arbitrary unmarked corruptions, and without knowing the actual tau; it continues to work if tau varies between queries. Therefore, for every quartet, every integer f>=0 and all fixed or unknown varying tau in [L,U):

    V_f(Q(b,a)) = 296*(2f+1).

In particular V_8(Q)=5032. The exact six-state value 8300 is a 3268 budget-unit improvement over the strongest *pairwise-only* certificate on H; it explicitly detects a joint-support constraint.

## Full target, verification and continuation

Projection to a named subset gives a valid full-256 root lower bound. Thus this new six-state computation gives C_8*>=8300, stronger than the previous pair-only 5032; the pre-existing stronger independent 17-state 8335 certificate remains in force, so the best current enclosure is still

    8335 <= C_8* <= 8343.

Do not add the quartet costs: one physical query interrogates many named states simultaneously. Neither a quotient of the 256-state scalar game into quartets nor a native Port/X6 reduction is proved here.

Reproduction: run VERIFY_R5_HARD_SEXTET.py with EXACT_R5_ALL_101_BUDGETS.json and stages_18.json from the unchanged frozen-input bundle. It checks source SHA-256, all 101 support families by two exact constructions, 64 quartets over 18 chambers and at U-1, and complete Bellman values f=0..11; the separate C++ independent solver and local replay package are in the same handoff zip. The corresponding RESULT_R5_HARD_SEXTET.json is an exact computation summary, not a formal proof artifact or independent acceptance.

Next scientific unit: embed this 6-state exact kernel into the larger 7–17-state Bellman solver, obtain a rigorous subproblem lower bound strictly larger than 8335 if possible, or resolve the 8335..8343 gap by a full-game dual certificate. The all-f six-state affine conjecture is also available as a separate research direction.

Source status: independent scientific GitHub branch only; original Task/CLAIM owner unchanged, Activity linkage and independent review pending.