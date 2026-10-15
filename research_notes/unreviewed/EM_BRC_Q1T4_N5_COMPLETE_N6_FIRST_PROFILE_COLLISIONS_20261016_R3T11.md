# EM / BRC Q=1,T=4 — complete n5 quotient; first n6 permanent collisions (UNREVIEWED)

2026-10-16. Canonical account input: GLOBAL_KNOWLEDGE_V1 main@051d8cb082117dd0195f6221748147c955bb2b77; EM research input main@fd14daa12045646ee5cc9068d54424707373a914. P000 verified and ACTIVE worldview read. This is an auxiliary labeled-source positive BRC model, not a native-X6 dynamical theorem. Native Researcher identity/owner authorization not obtained: dispatch CONTROL_QUOTA; native session_start blocked.

## Model
For n labeled sources with d_i in nonnegative integers, action G_j resets secretly ANY i!=j (including a previously reset source). AFTER the action, the sole feedback bit is b=[sum remnant>=4]. There is NO initial feedback. A policy may stop; terminal output is [EVERY hidden-choice history has remnant>=1]. Future finite feedback-adaptive policies induce equivalence. Clipping a_i=min(d_i,4) is exact. Full-subset static profile gives [sum_{i in S}a_i>=1] and [sum_{i in S}a_i>=4] for each survivor set S; it is sufficient but possibly nonminimal.

## Verified finite conclusions
n=5: static profiles P_5=1219, adaptive classes A_5=1219, maximal minimal separator length H_5=5. Exhausted 59,753 unordered pair orbits modulo simultaneous source permutation and swapping compared states: 342 identical profile, 59,411 distinct profile, ALL 59,411 have fully replayed feedback-spine separators of depth <=5. Exact minimal depth histogram k=0,1,2,3,4,5: [125,1374,6980,19190,24020,7722].

n=6: static profiles P_6=7290, adaptive classes A_6=7065 (<7290), maximal minimal separator length H_6=6. Exhausted 297,865 unordered pair orbits: 589 identical profile, 297,272 distinct-profile separable within 6, FOUR distinct-profile pairs not separable at any finite horizon:
  112233 ~ 121233
  112234 ~ 121234
  112233 ~ 221133
  112234 ~ 221134
Every digit is a labeled source's clipped mass. The full unbounded public-belief graph has 153,203,153,203 reachable nodes in EACH orientation, closes without separator; independently reproduced by Python frozenset BFS. The FOUR orbits account for exactly 675 profile merge edges, with 45 fibers of size 6 and 7020 singleton fibers. Fiber count is obtained by independent DSU over all 5^6=15625 clipped states. Exactly 15 choices of two mass3 labels, or 30 choices of one mass3 plus one mass4 label, times 6 allocations of (1,1,2,2) across remaining labels give the 45 size-six fibers. Thus A_6=7020+45=7065. Every other pair separates in <=6; the prior general lower bound H_n>=n gives H_6=6.

Therefore the earlier proposed all-n conjecture A_n=P_n for n>=4 is FALSE already at n=6; n5 equality does not carry over automatically.

## Completeness/certificate semantics
The remaining hidden state is an n-bit survivor mask. For each ordered pair of public beliefs (B_X,B_Y), each G_j has at most two feedback successors; every secret choice i!=j is enumerated. To distinguish safe X from unsafe Y it suffices to follow one unsafe Y public-feedback spine and STOP on any off-spine branch; X remains safe under prefix stopping since resetting masses is monotone nonincreasing. Hence legal paired-belief graph search is COMPLETE, provided G_j is used only when all its X successors are safe. On any supported Y bit, advance both beliefs. A Y-unsafe successor is a separator. Search both orientations. If the finite reachable graph closes without any separator, no finite policy separates the pair. n6 exceptional closures were unbounded and cross-checked independently. Source-label permutation and swapping of X,Y preserve existence of a separator in either direction, so unordered multisets of 25 ordered coordinate-pair types cover all initial pairs.

Evidence sources: check_profile_orbits.cpp; generate_witnesses.cpp; witnesses_n5.tsv (59411 direct replayed witnesses); check_orbits_n6.cpp; focused_n6.cpp; independent_n6_closure.py/json; count_n6_quotient.py; n6_quotient_result.json; run_n5.log; SHA256 manifest. Exact computation is author-checked, NOT an independent Driver mathematical acceptance, formal Source freeze, or P000 promotion.

## Unresolved
Classify all n>=7 adaptive blind fibers, first testing the appended-source families (112233,c)~(121233,c) for c=0..4. Investigate a symbolic feedback-masking residual criterion and prove/disprove H_n(1,4)=n for n>=7. Formally verify the 153/203-node closed transition graphs. Reuse state: REUSE_APPLIED for existing BRC static-threshold profile and feedback observer semantics; preserves positive branch support and labeled provenance.
