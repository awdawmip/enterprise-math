# N=14 ternary IID: Stage231–233 exact full-real minimax intervals and asymmetric dual

Status: PORTABLE_AUTHOR_EXACT / UNREVIEWED / NOT_ADMITTED. 2026-10-28 Asia/Shanghai. External auxiliary IID model only; no P000-native X6/Cell-dynamics theorem follows. Prior Stage230 source: PR #1571 commit d802e13b1d7888a942ab17db38244fdbee983e0a.

## Problem and universal dual certificate

For N=14, P=(3,1,20)/24, Q=(2,2,20)/24, an arbitrarily randomized stopping/decision policy can use the entire ordered observation history and private independent randomness. Let eP=Pr_P(decide Q), eQ=Pr_Q(decide P), tP=E_P(observations), tQ=E_Q(observations), and V14(alpha)=inf_(eP,eQ<=alpha) max(tP,tQ). For count state s=(n,a,b), every ordered prefix has likelihood ratio r(s)=Q(prefix)/P(prefix)=2^(a+b)/3^a.

For independent nonnegative penalties lambdaP,lambdaQ, define B(s)=min{lambdaQ*r(s) [P decision], lambdaP [Q decision], 1+sum_j P_j B(s+j) [continue if n<14]}; H=B(0,0,0). Conditioning backwards on any complete ordered-history random policy proves tP+lambdaP*eP+lambdaQ*eQ>=H, hence V14(alpha)>=H-(lambdaP+lambdaQ)*alpha. This lower bound does not assume count-state sufficiency for all policies. A Bellman-tight policy with eP=eQ=alpha, tP>tQ attains it.

## Finite complete primal-face lemma

At each fixed count-state the likelihood ratio of *each surviving ordered prefix* (including hypothesis-independent action-coin likelihoods) is r(s). Thus action probabilities given the count state coincide under P and Q. Replacing them by those probabilities produces a count-state Markov policy with exactly the same P/Q occupancy measures and all four observations, by finite DAG induction. All minimizing policies can use only Bellman-minimizing actions at reached states, as nonminimal action gaps are strictly positive under full-support P. There are precisely two tied states at each of these three supports. The observations of their randomized Markov policies lie in the convex hull of four deterministic corner policies; conversely every mixture of those four complete policies is implementable by one random seed at the root.

Intersect the four-corner mixing simplex with eP-eQ=0. Every extreme point is a balanced deterministic corner or a mixture across a simplex edge whose endpoint error differences have opposite signs. Exact enumeration finds exactly THREE balanced edge vertices and no balanced deterministic corner at each support. Their smallest and largest common errors are the exhaustive limits of their balanced optimal faces. All four corners have tP>tQ. Mixing the two balanced endpoint policies yields every real alpha in each closed interval; dual equality follows because every corner is Bellman-tight. The executable Python Fraction certificate enumerates all 680 Bellman count states per stage, 1238 strictly positive nonminimal action gaps each, all four deterministic observations by rational suffix DP and a separate unmerged ordered integer-mass P/Q DFS, all balancing edges, dual contacts, strict time margins, and right-endpoint maximality. Actual independent ordered DFS visits: 15652, 15052, 14266, total 44970.

## Stage231: balancing coin saturates earlier than u=1

Equal penalties lambdaP=lambdaQ=33912/479; H=5990704895603323/100097158938624. Exactly two ties: (10,1,0) continue/P and (14,0,0) P/Q; min positive action gap=245/22992. Mixed finite-difference coefficient of the four corner vectors is identically zero because (10,1,0) cannot be an ancestor of terminal (14,0,0). Let u be the P-coin probability at (10,1,0), z be the Q-coin probability at the terminal. Equal errors require z(u)=550325289029/625000000000+(2513/20000)u. Its value at u=1 is 628856539029/625000000000 >1. Hence the exact legal range stops at u_max=10667815853/11218750000, z=1. The exhaustive balanced-face convex hull confirms this is the MAXIMAL common error of this fixed dual support.

For EVERY REAL 0<=delta<=25549418967935/14403960274157568,
V14(alpha230+delta)=V230-(67824/479)delta,
alpha230=14503202310215/40122452017152,
V230=7243830309143/835884417024.
New endpoint alpha231=109004146840315/300082505711616, V231=631291740495223/75020626427904. Endpoint P-minus-Q expected-time margins: 614896242623/835884417024 and 24919847539549/37510313213952, strictly positive.

## Stage232: asymmetric penalties and nonzero mixed term

The next scalar-K Bellman candidate K=562392/8039 has no balanced optimal-face point, so cannot be declared a primal minimax segment. With penalties lambdaP=3736/55, lambdaQ=41652/605, exact H=91814076904081/1580343975936. The only ties are (10,1,0) continue/P and (12,1,1) continue/Q, with 1238 positive nonminimal gaps (minimum 2/363). These states CAN be ancestors; the four-corner mixed vector is exactly
(-1123046875/1114512556032, 537109375/626913312768, 48828125/5159780352, 634765625/52242776064).
Thus affine independent-coin linearization would be wrong. Use the full four-corner convex hull instead. The maximal balanced point mixes deterministic bit policies 10 and 11 at the root with respective weights 29805570346/33662109375 and 3856539029/33662109375.

For EVERY REAL 0<=delta<=1666575794675/12770177743060992,
V14(alpha231+delta)=V231-(82748/605)delta.
New endpoint alpha232=7270819537255/20008983232512, V232=21002077276133/2501122904064. Exact P-minus-Q time margins left/right: 24919847539549/37510313213952 and 3311740924421/5002245808128.

## Stage233: second asymmetric support, still nonzero interaction

lambdaP=7768/115, lambdaQ=342/5, H=34724256851041/600791924736. The only ties are (9,1,0) continue/P and (12,1,1) continue/Q, with minimum positive action gap 5/552 among 1238. Mixed four-corner coefficient:
(-224609375/247669456896, 107421875/139314069504, 9765625/1146617856, 126953125/11609505792).
Balanced-face maximum mixes bit policies 01 and 11 with respective weights 27943542952/42846328125 and 14902785173/42846328125.

For EVERY REAL 0<=delta<=8569101474475/8467273689163776,
V14(alpha232+delta)=V232-(15634/115)delta.
New endpoint alpha233=1160041464109745/3183518045011968, V233=3286774073290327/397939755626496. Exact time margins: 3311740924421/5002245808128 at left and 512965541498779/795879511252992 at right. All three new supporting slopes are strictly increasing; adjacent endpoint alpha and V agree exactly.

## Reproducibility, BRC and limitations

Run python3 REPRO_STAGE231_233.py from the material directory. It writes complete certificate231_233.json and prints STAGE231_233_EXACT_PASS 44970. All arithmetic is exact Fraction; integer-mass DFS carries the full ordered branch history with separate PN=(3,1,20) and QN=(2,2,20) positive integer masses and applies denominator 24^14 only at stopping. The count-state quotient is justified *only* for declared finite-horizon stopping error/time observables by the Markovization lemma. This is typed BRC-compatible branch fidelity in an external auxiliary model; no X6-native embedding, dynamical correspondence, physical calibration, canonical CLAIM/Result or independent Driver acceptance was obtained. Next bounded mathematical unit: see NEXT_TASK_PACKET_234.md.

