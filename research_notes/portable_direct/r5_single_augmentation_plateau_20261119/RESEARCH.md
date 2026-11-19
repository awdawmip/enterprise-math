# R5: exact single-label augmentation plateau and zero-error residue split

Date: 2026-11-19 Asia/Shanghai. Status: AUTHOR_PROVED_FINITE_ENUMERATION / EXACT_INTEGER_CHECKED / NOT_REVIEWED. Independent scalar-observer research with no new formal CLAIM/RUN, Result or independent review.

## Frozen input and problem

Source: awdawmip/enterprise-math at commit 435e77af0d180eac32bd1f9c4c464bc4010b7551; EXACT_R5_ALL_101_BUDGETS.json has SHA-256 50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b. The scalar experiment contains 256 individually named hypotheses, 101 physical query actions k=214,...,314 (cost k), correct response intervals 2|y-N_h(k)| <= tau, and at most f unflagged arbitrary errors. Fix tau=U-1=58182461585441404127941754879 from the pinned stages_18.json. The earlier six-label certificate takes H=(0,16,32,48,1,64), yielding V_f(H)=732+946f by complete finite Bellman calculation for f=0,...,11.

## New exhaustive finite theorem

Let H_u=(0,16,32,48,1,64,u) for any of the 250 named labels u outside H. The following exact statements hold on the frozen scalar model:

**SA1 (eight-error augmentation plateau):** For every u not in H, V_8(H_u)=8300.

**SA2 (zero through eight errors):** For every u not in H and every integer 1<=f<=8, V_f(H_u)=732+946f. At zero errors, V_0(H_u)=733 if and only if 16 <= (u modulo 64) <= 47; otherwise V_0(H_u)=732. Among 250 additions, exactly 126 give 733 and 124 give 732.

These are complete *finite* findings across 250 named seven-label systems and 9 error budgets; they do not extend the affine formula to all f. No one-label extension of H can improve the six-label eight-error lower-bound witness of 8300. Any set containing H and having restricted eight-error value strictly greater than 8300 must contain at least 8 labels.

## Exact witness and proof method

For a query k and seven named hypothesis intervals, let F_k be the collection of inclusion-maximal 7-bit response-support masks. It is enough to enumerate the windows [N_h(k), N_h(k)+tau] starting at each integer center, because every nonempty common intersection has a witness at the maximum of its constituent interval left endpoints. As an independent check, enumerate doubled real-response endpoints 2*N_h(k)-tau and test membership via 2*N_h(k)-tau <= 2*y <= 2*N_h(k)+tau. Both methods produce exactly the same masks for all 250 x 101 = 25,250 action/augmentation pairs.

For an error vector e_i in {0,...,f+1} with live hypotheses e_i<=f, use the complete recurrence:

    V_f(e)=0 if at most one live named hypothesis.
    V_f(e)=min_k [k+max_{S in F_k} V_f(e^S)]
    e^S_i=min(f+1,e_i+1_{i not in S}).

In the minimization, omit any k for which some S contains every currently live label: its worst response leaves e unchanged, so strictly positive query cost cannot make it optimal. Every retained transition strictly increases at least one capped live error count, so the finite recursion is acyclic. For equal maximal-support families, keep only the cheapest physical action since the transitions are identical and its cost is lower. This is an exact observer-family quotient, not a quotient of named hypotheses or Port provenance.

The companion C++17 source uses exhaustive base-(f+2) packed-state memoization and exact integer costs. Every possible state reachable from the root is recursively evaluated. An action's branch scan may stop only after its accumulated lower bound cannot improve an already valid upper bound, so no optimal action is lost. The Python verification companion rebuilds both support representations independently, groups the price-aware action families, runs the C++ engine for every u and f=0,...,8, and emits the full 250-row result. It discovers 42 distinct complete seven-bit price-aware action signatures. The test returns:

    PASS_R5_SINGLE_AUGMENTATION added= 250 error_budgets= 9 exact_dps= 2250 support_cross_checks= 25250 signature_classes= 42 all_f8= 8300

A second, separately coded Python verifier applies the doubled-response construction, retains all 101 physical actions, and solves the f=0 problem by live-subset recursion. It independently confirms 124 values of 732 and 126 of 733, with exactly the residue criterion above. Independent Python tuple-state f=8 checks additionally confirmed the C++ value 8300 for additions u=2, u=17 and u=128.

## Interpretation and next question

The f=0 one-unit increase is a real joint-observation distinction for 126 labels; the associated single-label penalty disappears from minimax optimal cost for every tested f=1,...,8. This does NOT establish that a seventh hypothesis is observationally redundant or that the old six-label state is losslessly equivalent to the 256-label system.

The existing full-game enclosure remains 8335 <= C_8* <= 8343. This result supplies a precise search constraint: evaluate *joint* multi-label additions, beginning with pairs or larger sets selected by the 42 support-signature classes, and incorporate the existing 17-state 8335 lower-bound certificate. Full 256-root improvement, dynamic native signed Port readout and computational cost advantages require their own proofs/evidence.

## Reproduction, scope and provenance

Use the original SHA-pinned input and stages_18.json; compile SOLVE_R5_SINGLE_AUGMENTATION.cpp with g++ -O3 -std=c++17, then run VERIFY_R5_SINGLE_AUGMENTATION.py with the two input paths and the executable path. The checker generates RESULT_R5_SINGLE_AUGMENTATION.json and validates all 2250 roots. Run VERIFY_R5_SINGLE_AUGMENTATION_INDEPENDENT.py on the same inputs for the full independently checked f=0 census.

The 250-case computation is exact finite integer mathematics. It is author-checked and has not passed an independent mathematical review or a formal Task Result admission. Historical provenance: EM-DIRECT-4C3E47, Activity RA-F2257922D00B2FE4C4818DBD; this note itself grants no current execution capability and its Activity linkage may be completed separately.
