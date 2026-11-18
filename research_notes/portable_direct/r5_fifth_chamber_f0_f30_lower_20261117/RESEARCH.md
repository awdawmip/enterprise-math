# R5 fifth noise chamber: exact five-mask lower bounds for f=0..30

Date: 2026-11-17. Scientific pin: 435e77af0d180eac32bd1f9c4c464bc4010b7551. Original 101x256 observer count-table SHA-256: 50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b. Status: AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED.

## Theorem (new finite-range lower bound)

For the frozen derived integer-count scalar observer, h ranges over the 256 named configurations, k over the 101 positive integer query costs 214,...,314, and each intact real response y satisfies |y-N_h(k)| <= eta. At most f responses may be arbitrary unmarked corruptions. C*_f(tau) is the optimal worst-case cumulative *physical query cost*, tau=2 eta.

For all real tau with
25845652773852463277015040000 <= tau < 58182461585441404127941754880,
and **each integer f=0,...,30**,

C*_f(tau) >= 735 + 950*f.

This extends the previous f=0..10 five-state certificate to f=11..30. It is a lower bound for the original 256-state game, not a full-game equality for f>7 or a universal-in-f proof.

The previously saved all-f constructive three-stage strategy, using budgets (296,223,216), supplies the separate upper bound C*_f(tau) <= 735+951f for every f>=0. Consequently the exact known bracket for f=8..30 is [735+950f,735+951f]; f=20 gives [19735,19755] and f=30 gives [29235,29265]. The earlier complete 256-state upper certificates establish equality for f<=7 only.

## Proof and exact finite certificate

Restrict the true configuration to the five **actual** masks H=(18,24,82,34,17). At tau equal to the chamber left endpoint L, every real answer y determines a compatibility subset of H. An inclusion-maximal subset appears inside a closed window of integer centers of width L whose left endpoint coincides with a center. Every other answer subset is contained in one maximal answer support; an adversary may choose the larger compatible subset.

For each of the 101 legal k, form the complete family of inclusion-maximal supports. Identical support families have equivalent effects on the five counters, so the cheapest representative dominates every more costly one. Exhaustive enumeration yields seven exact families, recorded with their actual costs in FIVE_STATE_ACTIONS_LEFT.txt:

- k=216: (2,13,16)
- k=223: (4,27)
- k=296: (8,23)
- k=214: (15,16)
- k=215: (2,29)
- k=221: (13,18)
- k=222: (31,).

Bit positions use the order H. The final support (31,) carries no useful information but is retained in the complete quotient. The existing predecessor Python verifier builds these supports from all 101 exact center lists; the local reproduction package includes a frozen-table SHA-checking independent action builder.

For fixed f, let e_h=min(f+1,number of responses incompatible with hypothesis h). A maximal answer support A induces T_A(e)_h=min(f+1,e_h+1[h not in A]). At most one h with e_h<=f is terminal. Otherwise the exact minimax value obeys

V_f(e)=min_k ( k + max_{A in MaxSupports(k)} V_f(T_A(e)) ).

An action with any possible self-loop T_A(e)=e is unusable in a finite worst-case-winning tree and may be skipped. Every retained transition strictly increases a live counter, making the finite integer recurrence acyclic. The included C++17 implementation packs five counters into 5-bit lanes: this is exact for 0<=f<=30 because the eliminated sentinel f+1<=31. Its keys are checked for full equality by unordered_map, not just a hash digest.

The executed exact root values were **V_f(0,0,0,0,0)=735+950f for every f=0,...,30**. At f=20 it visited 2,798,768 memoized states; at f=30, 18,202,476 states and 197,394,955 child evaluations. Earlier Python Bellman runs independently agree at f=11,...,17, while published five-mask checks agree at f=0,...,10. All answers, costs and inequalities are integer exact.

Restricting the true hypothesis makes the five-state game no harder than the full 256-state game, and enlarging tau cannot reduce the adversary's available answers. Thus each five-state root value at L is a valid lower bound over the whole specified real-noise interval. This proves the theorem.

## Reproduce and exact evidence boundary

Use the frozen input file EXACT_R5_ALL_101_BUDGETS.json from the project's R5 archive (SHA-256 above). The predecessor SHA-checking response-support code is VERIFY_R5_FIVE_STATE_LOWER.py in this same R5 PR. The accompanying FIVE_STATE_ACTIONS_LEFT.txt was regenerated from all 101 budgets at L, then supplied to VERIFY_R5_FIVE_STATE_FAST.cpp.

Compile: g++ -O3 -DNDEBUG -std=c++17 VERIFY_R5_FIVE_STATE_FAST.cpp -o check_r5
Run: ./check_r5 FIVE_STATE_ACTIONS_LEFT.txt 30

The full local handoff package additionally retains original pinned 25,856 count entries, the independent Python action generator, outputs for every f=0..30, and a SHA-256 manifest. The new result has no independent mathematical review or formal Lean admission. It makes no statement about lossless compression of native Heartbeat World X6 joint/provenance state; all quotient arguments are scoped to the declared derived scalar observer.

## Open problems and control scope

Determine whether the complete 256-mask f=8 cost is 8335, 8336,...,8343; construct a full-game upper strategy or improve the lower. Independently find an all-f symbolic adversary or a first violation of the affine lower pattern. This is independent portable GitHub research preservation; the commit alone creates no formal Task/CLAIM/Result/Review, owner right, Activity PROGRESS or P000 revision.