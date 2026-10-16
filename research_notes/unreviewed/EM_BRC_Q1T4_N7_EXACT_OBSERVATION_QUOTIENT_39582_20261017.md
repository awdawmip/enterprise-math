# BRC Q=1,T=4,n=7: exact finite observation quotient (UNREVIEWED)

Scientific status: COMPUTATION-ASSISTED FINITE THEOREM / UNREVIEWED / NOT_ADMITTED. This is an auxiliary labeled-source feedback model, not a P000 native X6 dynamics theorem.

## Frozen source inputs
- GLOBAL_KNOWLEDGE_V1 main@f6e70693ed2ff6809adec0a29d50025442092014 (bootstrap, manual, Enterprise Math project router, P000, ACTIVE worldview, BRC method and activity-registration procedure).
- enterprise-math main@14a109f3ab48a2b1a9f925e9b780ff17e5ab17f8 (portable research, ChatGPT ordinary control protocol).
- Previous conversation's Hamming-1,2,3,5,6,7 and same-histogram Hamming-4..7 evidence retained and rechecked.

## Model
State a ∈ {0,1,2,3,4}^7, seven labeled sources. Each move chooses excluded source j; adversary resets any i≠j to zero, including previously zero sources. Public feedback AFTER reset is whether remaining mass ≥4. A finite adaptive public policy P is safe for a when **every** legal hidden path terminates with strictly positive mass. Define a~b iff Safe_P(a)=Safe_P(b) for every finite policy P. Static profile Π(a) records seven positive-support bits and all 128 subset-threshold bits.

## Completed result
A_7(1,4) = #({0,1,2,3,4}^7 / ~) = **39,582** exactly. Every inequivalent pair is distinguishable by a policy of at most seven steps in this fixed finite model.

This turn completed the previously unclosed Hamming-4, cross-histogram scope:
- 20 directed change types, C(23,4)=8855 four-edge multisets; 85 are balanced, so 8770 cross-histogram change types.
- C(7,4)=35 choices of the three unchanged coordinates, giving 306,950 pair-orbits.
- 306,830 have explicit ≤7-step distinguishing policy certificates (all independently replayed in C++).
- 120 have identical full static profiles (analytic labelwise coupling).
- Zero unresolved and zero cross-profile permanent-equivalence exceptions in this H4 cross-histogram scope.

Independent **global** exhaustive pair-orbit audit over 25 ordered coordinate-pair types:
C(31,7)=2,629,575 oriented pair-orbits, all covered once:
- 2,628,124 distinguishing witnesses (all independently replayed on all legal hidden paths);
- 1,107 off-diagonal same-static-profile equivalents (all profiles recomputed);
- 14 off-diagonal cross-profile permanent-equivalence orbits (7 Hamming-2 and 7 Hamming-4, all 28 directions unbounded public-belief graph exhausted without truncation);
- 330 diagonal identity orbits.
No overlap or missing orbit. Full profile enumeration over 5^7=78,125 labeled states gives 42,949 profiles. Permuting the 14 proved blind-pair seeds under all 5040 source relabelings and unioning them performs 3,367 effective mergers: 42,949−3,367=39,582. All pair orbits have been classified, so there are no further merges and the upper bound becomes equality.

## Proof contract
Full static-profile equality preserves terminal-zero information and every post-reset feedback bit along each matched hidden path, hence gives equivalence. If an arbitrary feedback tree separates a safe state from an unsafe one, choose one zero-mass terminal path of the unsafe state as a feedback spine and end all off-spine branches immediately. Reset monotonicity preserves safety in the safe state. Thus single-spine policies suffice to detect all distinctions; finite unbounded belief-graph closure in both orientations certifies the 14 exceptions. All other inequivalent pairs have direct all-hidden-path policy witnesses, not mere bounded-search nonhits.

## Evidence and reproducibility
Portable, self-contained 190-file local evidence bundle:
EM_BRC_20261017_N7_EXACT_OBSERVATION_QUOTIENT_39582_COMPLETE_EVIDENCE.zip
SHA256: 6863645c866727ed4beb755cc891ccac87c4f18340ca96aaa1278b3d039160d3.
Contains generated H4 306,950 input orbits, 306,830 strategies, 120 static equal records, prior certified source inputs, all-orbit independent Python audit, global C++ replay of all 2,628,124 policies, 14 double-sided unlimited closure recomputations, and a separate profile-merging enumerator. This GitHub Markdown **does not** mean the ZIP bytes have been uploaded to GitHub; canonical evidence upload/readback is pending.

Most important check outputs:
- ALL_ORBIT_AUDIT: 2,629,575/2,629,575, one-to-one, 2,628,124 witness / 1,107 profile / 14 blindness / 330 identity.
- INDEPENDENT_CPP_REPLAY: PASS 2,628,124/2,628,124.
- UNBOUNDED_DOUBLE_CLOSURE: PASS 14 pairs, 28 orientations, none truncated.
- INDEPENDENT_QUOTIENT: 42,949 profiles, 3,367 merges, 39,582 components.
Local full report: EM_BRC_Q1T4_N7_EXACT_OBSERVATION_QUOTIENT_39582_20261017.md.

## Native authority and next research
GitHub account push capability is not an Enterprise Math session/Task owner claim. Gateway em_control_tasks returned CONTROL_QUOTA; em_session_start(RESEARCHER) returned STATIC_READONLY_SCOPE_DENIED and operation_sent=false. Active owner not fully verified; no canonical RA/CLAIM/Result/Driver approval. This report is an **unreviewed work branch only**.

Next distinct research units: (1) authenticate an authorized EM session and publish verified evidence as a formal Source result with independent Driver review; (2) formalize a small trusted exact-certificate checker for the complete 2,629,575-orbit cover and 14 no-distinguishing-policy closures; (3) seek analytic classification of the 14 blind pairs and parameters n,Q,T; (4) develop a separate proven observer-preserving bridge if applying any auxiliary statement to native P000 six-space-plus-time research. Preserve full source provenance, branch identities and residuals.

Global-Knowledge-Sync: main@f6e70693 / GLOBAL_KNOWLEDGE_V1
