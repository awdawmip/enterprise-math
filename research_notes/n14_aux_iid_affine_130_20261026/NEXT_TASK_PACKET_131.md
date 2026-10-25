# N14 Stage131 — next exact research unit (OPEN)

Mother question: the **external auxiliary** ternary iid sequential test P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6), N=14, randomized tests on all literal ordered histories, error caps eP,eQ<=alpha and minimax expected stopping time. No native P000/X6/Heartbeat model transfer is asserted.

The Stage130 **author-exact but Driver-unreviewed** endpoint is:

- alpha130 = 36696744084893090695/105616844785075617792;
- V130 = 660257040358974188827/52808422392537808896;
- B=(11,0,1) Q-stop probability w=23520936469043837/81438720000000000;
- T=(14,7,4) terminal P-choice probability v=1.

Stage131 is **DUAL_CANDIDATE_ONLY**, not a primal optimal interval. Exact affine gap scan from Stage130 (T fixed P, B Q/C tie preserved) follows dK=-1, dL=-112/129. The first positive gap closes at

- t = 48619197/4735810;
- K131 = 3787884/5905;
- L131 = 3551272/5905;
- new tie A=(12,7,3), P/continue;
- old tie B=(11,0,1), Q/continue.

Exact dual Bellman at this candidate: 680 states, exactly 1238 strictly positive nonchosen-action gaps, zero negatives, least strict gap 13530313/2204029440; Hroot=38329289789453267095823/86261060643965632512.

**First executable mathematical question:** Determine the actual first-hit positive rational ordered-word carriers to A and B under the Stage131 strict Bellman actions (with T always P). Analyze their path cones: B at (11,0,1) cannot be an ancestor of A at (12,7,3) because just one step remains to increase a from 0 to 7; A at n12 cannot precede B at n11. Verify both actual reachability masses rather than infer from combinatorial counts alone. Form the four corner observer vectors (eP,eQ,tP,tQ), show whether the mixed term vanishes, derive the balancing relation between the two stop probabilities, establish its full-real feasible interval and sharp right endpoint (or an exact obstruction). Cross-check with a separately implemented integer-weight DFS over literal histories.

Source/frozen evidence: Stage130 author proof and the two locally executed exact programs in sibling files. GLOBAL_KNOWLEDGE_V1 main@363cc21deb56c429a3d1304e62bde6fd4c35452e; P000 original Git blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc. Native task inventory still reports CONTROL_QUOTA and native session initiation STATIC_READONLY_SCOPE_DENIED/operation_sent=false; no CLAIM/Result or independent Driver acceptance is inferred.

Only advance to Stage131 theorem once the actual full-real primal and dual certificate is complete; a computed dual candidate is not an accepted research Result.
