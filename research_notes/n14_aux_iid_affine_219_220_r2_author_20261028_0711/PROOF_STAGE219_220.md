# Stage219–220: two exact full-real intervals for an auxiliary N=14 ternary-IID test

Classification: PORTABLE_AUTHOR_EXACT / UNREVIEWED / NOT_ADMITTED. This is author-side mathematical work, not Source CLAIM, canonical Result, independent Driver approval, Lean verification, native X6 dynamics or a change of P000.

## Exact model and statements

Each observation is IID under P=(3,1,20)/24 or Q=(2,2,20)/24. Any randomized stop-and-declare policy may use the entire ordered observation history and must stop by N=14. Define eP=P(declare Q), eQ=Q(declare P), tP=E_P(stopping time), tQ=E_Q(stopping time) and V14(alpha)=inf(max(tP,tQ): eP,eQ<=alpha).

Inherited Stage218 author-proved endpoint, from immutable commit 4de46d1ad9bec0b0412631505e3d89a340a3421a:
alpha218=7505060794177169429/21035720123168587776; V218=4093942756303281817/438244169232678912.

**Stage219 theorem.** K219=314587800/3377071 and H219=28050139715601809024924983/369995418708693051506688. For every real delta in [0,84426775/12173449145352192],

V14(alpha218+delta)=V218-(629175600/3377071)*delta.

Right endpoint alpha219=7505060940066636629/21035720123168587776 and V219=4093942190045241817/438244169232678912.

**Stage220 theorem.** K220=3936600/42443 and H220=10974818820832189621177/145315603708926492672. For every real delta in [0,42443/21035720123168587776],

V14(alpha219+delta)=V219-(7873200/42443)*delta.

Right endpoint alpha220=234533154377083721/657366253849018368 and V220=127935693438908681/13695130288521216.

Both theorems hold for irrational as well as rational delta and all history-dependent randomized decision policies.

## Universal dual bound

For a count triple s=(n,a,b), where a is the number of letter 0 observations and b the number of letter 1 observations, the exact per-history likelihood ratio is rho(s)=Q(h)/P(h)=2^(a+b)/3^a. For K>0 define the backward value

B_K(s)=min{ K*rho(s) [declare P], K [declare Q], 1+sum_j P_j B_K(next_j(s)) [continue if n<14] }.

Every feasible ordered history with state s has the same likelihood ratio and IID conditional suffix law. Induction over *the full ordered tree* shows that this count-state recurrence minimizes tP+K(eP+eQ) even among arbitrary ordered-history randomized policies: the three terminal/continue costs above are the exact conditional Lagrangian costs and randomization cannot improve their minimum. Therefore tP+K(eP+eQ)>=H_K=B_K(0,0,0) for all policies, hence V14(alpha)>=H_K-2K*alpha whenever eP,eQ<=alpha.

Exact rational enumeration covers sum_{n=0}^14 (n+1)(n+2)/2=680 count states at each K, with 1238 strictly positive action gaps and no negative gaps. The minimum positive gaps are 7442425/1641256506 at Stage219 and 22638313/3960441216 at Stage220. The *only* Bellman ties are (9,4,3): Q/continue and (14,0,0): P/Q for Stage219; (12,8,4): P/continue and (14,0,0): P/Q for Stage220. The origin Bellman values equal the stated exact H219 and H220.

## Primal construction for every real parameter

At each stage let u be the chance of selecting the first tie action at T=(9,4,3) (Q at Stage219) or T=(12,8,4) (P at Stage220), and let z be the chance of declaring P at Z=(14,0,0). Elsewhere select the unique Bellman-minimizing action. Evaluate all four deterministic corners (u,z) in {0,1}^2, recording O=(eP,eQ,tP,tQ).

An exact Fraction conditional suffix DP and an independent, unmerged full ordered-word DFS with separate positive integer P/Q path masses produce identical four-corner observation vectors. These two computations cover 54,460 visited DFS nodes at Stage219 and 48,820 at Stage220, 103,280 total. The actual executable program PORTABLE_REPRO_STAGE219_220.py reruns the rational Bellman and full unmerged ordered-history checks without external dependencies, independently of the local primary source. It prints STAGE219_PORTABLE_EXACT_PASS 54460 and STAGE220_PORTABLE_EXACT_PASS 48820. Exact original source, per-corner certificates and logs also exist in the local reproducible evidence archive.

Both T states have b>0 whereas Z has b=0, and b cannot decrease along a history. Z is terminal. Thus neither tie can be encountered after the other on any single path. The mixed vector O11-O10-O01+O00 is exactly zero both by path ancestry and exact corner arithmetic. For all real u,z in [0,1] the observation vector is therefore affine: O(u,z)=O00+u(O10-O00)+z(O01-O00).

Solving eP=eQ gives, exactly,

z219(u)=659618660181452821/1638400000000000000 + (437333877/1024000000000000)*u,

z220(u)=659619359915656021/1638400000000000000 - (63601/327680000000000000)*u.

In both cases the values z(0),z(1) lie strictly inside (0,1), so each real u in [0,1] yields a legitimate randomized strategy. On this affine balanced family the common error increases strictly, covering [alpha218,alpha219] and [alpha219,alpha220], respectively, including all real points. At the two endpoints the positive differences tP-tQ are:

Stage219: 401994805549792921/438244169232678912 and 401995029685404121/438244169232678912.

Stage220: 401995029685404121/438244169232678912 and 4187448225889027/4565043429507072.

By affinity, tP>tQ for all u throughout each interval. Every selected action attains its Bellman minimum, so tP+K(eP+eQ)=H and max(tP,tQ)=tP=H-2K*alpha. The constructed strategies attain the universal lower bound, proving both claimed exact full-real optimum intervals. The left endpoints and dual contacts were checked as exact equalities.

## Stage221 — dual only

The exact first-switch scan from the Stage220 right-hand corner gives K221=208781064/2258455 and H221=1164595201473697679395993/15464917737881091440640. Its only ties are (6,2,2) Q/continue and (14,0,0) P/Q; 680 states, 1238 positive gaps, min positive 22638313/6585654780. H221=H220+2*alpha220*(K221-K220) and K221<K220. Consequently the Stage221 dual lower bound is strictly above the *fixed Stage220 support line* for alpha>alpha220; this is NOT a proof of Stage221 primal optimality. Similarly Stage220's contact and K220<K219 show strict-right nonoptimality of the fixed Stage219 support line.

## Source, scope, actual run, and authority

At 2026-10-28 in the automation's local research execution, exact rational primary implementations, two distinct bottom-up ordered-mass reference scripts, and both next-dual scanners ran successfully. The portable independent rerun printed the exact PASS lines quoted above. No floating-point tolerance was used. Count quotient sufficiency holds for this declared finite IID Bellman suffix functional only. Positive P/Q path masses and full ordered provenance implement the corresponding BRC-inspired branch-preservation discipline, but do NOT establish a native X6 observer-preserving bridge.

Pinned GLOBAL_KNOWLEDGE_V1 main@8fe3683083b0952641c3f34733a8acfeb2e18274; Enterprise Math main@e0a2e6012ebf28511cc1c3644ef87b65b66c6754; global P000 original blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc (matches the pinned projection); predecessor author evidence 4de46d1ad9bec0b0412631505e3d89a340a3421a.

The native current-owner query returned CONTROL_QUOTA; native session_start was denied STATIC_READONLY_SCOPE_DENIED with operation_sent=false. This publication is authorized GitHub portable author material only, with no native claim, Source Result or independent mathematical admission. The project's Heartbeat World has six native discrete spatial Cell dimensions and separately typed time; no physical realization or native-X6 correspondence is asserted.

Next task is NEXT_TASK_PACKET_221.md.