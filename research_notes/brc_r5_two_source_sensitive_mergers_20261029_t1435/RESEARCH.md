# R5 | Two source-sensitive serial LR mergers: all-real Bellman no-compensation certificate

Date: 2026-10-29 Asia/Shanghai. Scientific status: AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING. Finite external two-measure model, not a native Heartbeat-X6 result.

## Frozen authority and prior work

Global-Knowledge-V1 main@492747015c4ecca1a20cbda12eb153667675cfca: entry/manual, original P000 (Git blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc) and matching P000_STARTUP, ACTIVE worldview, TASK and BRC/math/code research policies. Enterprise Math main@676457cb5967d41294862087fe3ab29e6f856250: AGENTS, current autonomous and portable research protocols. Prior author-side mathematical input: PR #1663, commit c9669b05bec9f28985f952c358931fc90830afaf, research_notes/brc_r5_serial_source_farkas_20261029_t1344/RESEARCH.md. Native service reports authority_granted=false; bounded active-owner read returned CONTROL_QUOTA. Prior session-start rejection STATIC_READONLY_SCOPE_DENIED, operation_sent=false, remains a genuine native boundary. No current canonical Source owner, CLAIM, Result, independent Driver decision or formal admission is inferred from the neutral author-side GitHub publication.

## Exact two-law experiment and BRC carrier

Two origins A/B each have initial P and Q mass 1/2 and likelihood ratio r=1 at t=1. FULL behavior sees origin and full path. Genuine seedless LR behavior sees only (t,r), no shared random seed; all local randomized behavior probabilities may be arbitrary real numbers. At t=1,2,3 choose stop+declare P, stop+declare Q or continue; t=4 forces declaration. Four-observer map O=(eP,eQ,TP,TQ)=(P[declare Q],Q[declare P],E_P[tau],E_Q[tau]).

Each continuation selects multiplier s in {1/2,1,3/2}, r'=rs. Let K_Q^i(t)=(p_i(t),1-2p_i(t),p_i(t)), K_P^i(t,s)=s K_Q^i(t,s). The rational table is:

| stage | p_A | p_B |
|---|---|---|
| t=1 | 1/4 | 1/8 |
| t=2 | 1/4 | 1/4 |
| t=3 | 65/256 | 63/256 |

Every P/Q transition is strictly positive and normalized: sum K_Q=1 and sum_s s K_Q=1. This makes the actual pathwise Radon-Nikodym likelihood product r. At collision (1,1) the A/B future kernels differ; at collision (3,3/4) they again differ, and each origin has two positive incoming ordered paths (1/2,3/2) and (3/2,1/2). Under an all-continue test policy, each A route has (Q,P)=(1/32,3/128), each B route has (1/64,3/256). Stage-one stop decisions change the mass that can reach the second merger: the two mergers serially interact. This is typed positive source/path BRC flow; averaging only at the explicitly defined four-observer readout is justified, not an assumption that histories are interchangeable.

## Theorem: no compensation after an unavoidable origin collision

Suppose a first unavoidable decision key (t,r) receives a fixed Q-origin distribution rho_i>0 summing to one. Choose ANY signed four-observer objective w=(a,b,c,d), let S=min(ar,b)+t(cr+d) be the immediate best declaration cost per conditional Q mass, and let C_i be the minimum FULL conditional cost if origin i must continue now, including optimal FULL control over the *entire later history*. Subsequent transition kernels can depend arbitrarily on origin and path, including further interacting source-sensitive LR mergers.

Then, for all real behavioral policies,

min_FULL(w·O) = sum_i rho_i min(S,C_i);
min_LR(w·O) >= min(S,sum_i rho_i C_i);

so the support gap is at least

G(w) = [sum_i rho_i |S-C_i| - |sum_i rho_i(S-C_i)|]/2 >= 0.

If both signs of S-C_i occur with positive rho mass, G(w)>0: NO downstream merger can cancel this first information advantage. When sum rho_i C_i>=S, immediate LR stopping attains the lower bound, so equality holds for the LR minimum. For a continue-favoring mean, a common LR-compatible conditional FULL-optimal tail is sufficient for equality as well.

Proof. The FULL class can choose stop/continue separately for each fixed incoming origin, and standard finite-horizon backward induction gives C_i. At the first key, any seedless LR policy must use one shared real continue probability u. After continuation its restricted conditional policies belong to the FULL class for each origin, hence its cost is >=(1-u)S+u sum_i rho_i C_i. Minimization over u in [0,1] gives min(S,sum rho_i C_i). The identity min(x,y)=(x+y-|x-y|)/2 and triangle inequality prove the claimed formula and strictness. The argument allows arbitrary later history-sensitive kernels. QED.

This general lower-bound theorem is stronger in scope than the previous R5 first-collision formula, which required a predictively lumpable downstream tail for exact equality; the new bound does not. In this explicit experiment it is exact.

## Exact two-source-sensitive instance

Choose w=(1,1,theta,theta), theta=27/496. Best immediate declaration at (t,r) costs S_t(r)=min(r,1)+t theta(r+1). For each origin i, use the FULL Bellman recursion V_4^i=S_4; V_t^i(r)=min{S_t(r), sum_s K_Q^i(t,s) V_{t+1}^i(rs)}.

At t=3, for r in {1/4,1/2,3/4,1,3/2,9/4}, both origins choose continue iff r=1. Exact stop-minus-continue margins at r=1 are A=287/15872, B=225/15872; at r=3/4 they are A=-4033/63488, B=-4095/63488. The remaining t=3 margins are strictly negative. At t=2 for r in {1/2,1,3/2}, both origins continue iff r=1. At r=1 the A/B margins are 799/31744,737/31744; at r=1/2 and 3/2 the margins are -81/992 and -73/992. Thus the *optimal downstream actions* align by LR key even though the t=3 *predictive kernels* differ. This is objective-specific action alignment, not predictive lumpability.

At the unavoidable first collision the exact stop and FULL-continuation values are

S=275/248;
C_A=68577/63488 < S;
C_B=144477/126976 > S;
(C_A+C_B)/2 = S+1/8192.

The theorem therefore gives the exact all-real minima:
min_FULL(w·O)=(C_A+S)/2=138977/126976;
min_LR(w·O)=S=275/248;
Delta(w)=1823/126976 >0.

An explicit FULL witness stops at t=1 and declares P for origin B, continues for origin A, then at t=2,3 continues iff r=1; when stopping, declares P for r>=1, Q for r<1; t=4 declares the same way. The exact observation is

O*=(449/4096,1599/2048,15/8,15/8).

Thus EVERY real seedless LR policy satisfies the integer Farkas supporting plane

496 eP + 496 eQ + 27 TP + 27 TQ >= 550,

whereas the FULL witness has the left side 138977/256, a strict gap 1823/256. The full/LR four-observer convex hulls are UNEQUAL. The L-infinity distance from this witness to every LR observer is at least 1823/(256*(496+496+27+27))=1823/267776. The required equal-convex-hull mother target is still OPEN, and this explicit two-sensitive-merger candidate is rejected.

## Exact validation, provenance, and scope

The accompanying actually executed standard-library Fraction verifier checks positive Q/P rows and likelihood moment identities; distinct source-dependent kernels at both collisions; four positive origin/path flows into the second merger; all exact FULL tail action signs; C_A/C_B and the FULL observer; and an independent exhaustive 1024-mask deterministic LR optimization (512 masks tie). The cost is multi-affine in the 10 independent LR local behavior variables because no key is visited twice along a trajectory; hence deterministic-mask minimization also covers all real behavioral probabilities. The primary universal proof is the Bellman/Jensen inequality above. EXACT_OUTPUT.txt is the verbatim program output. No floating-point or finite signed-direction sweep is used to assert convex-hull equality.

Related verified prior literature is Laroche & Tachet des Combes, On the Occupancy Measure of Non-Markovian Policies in Continuous MDPs, ICML/PMLR 2023 (https://proceedings.mlr.press/v202/laroche23a.html): classical state-occupancy Markovization does not apply automatically to a source-sensitive (t,r) quotient. Zhang & Jiang, Statistical Tractability of Off-policy Evaluation of History-dependent Policies in POMDPs, ICLR 2025 (https://proceedings.iclr.cc/paper_files/paper/2025/hash/64ae05e3f1a88ebac7f9263b69f4e702-Abstract-Conference.html), studies a different statistical problem. No literature novelty priority, empirical physics or native X6 transfer is claimed. The protected P000 and worldview are unchanged.

VERIFIED AUTHOR FRONTIER: a true source-sensitive second merger cannot compensate an unavoidable earlier collision with opposite signed FULL Bellman margins. The precise next research task is in NEXT_TASK.md; use this necessary inequality as a pruning criterion before expensive all-signed convex-hull equality and genuine real observer-image tests.
