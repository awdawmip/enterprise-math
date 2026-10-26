# Stage153 — exact full-real optimal interval (external N14 auxiliary model)
Date: 2026-10-26. Status: AUTHOR_EXACT, SOURCE_ONLY, NOT_ADMITTED.

Frozen provenance: GLOBAL_KNOWLEDGE_V1 main@c7df6a7f96975759dc1b960a3e0c19134208dbcb; Enterprise Math main@5c8d97aa71aefa1fca7cb10db926634e5dc27aa9; Stage152 author proof/evidence commit 87435e0f38ccd9899837d66de86e4eba8889ee49. The Stage153 dual candidate at the latter source had NOT yet established a primal interval.

## Theorem
In the ternary IID sequential experiment with horizon N=14, P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6), allow arbitrary randomized policies depending on the COMPLETE ORDERED HISTORY. Denote eP=P(decide Q), eQ=Q(decide P), tP,tQ the two expected sample counts; let V14(alpha) minimize max(tP,tQ) subject to eP,eQ<=alpha.

Put
alpha152=18373003413933759925/52808422392537808896;
V152=318745538371909741813/26404211196268904448;
alpha153=18373341781933759925/52808422392537808896;
V153=318626572163909741813/26404211196268904448;
Delta=10326171875/1611585156022272.

For EVERY REAL 0<=delta<=Delta:
V14(alpha152+delta)=V152-(11954/17)*delta.
At alpha153 the optimum equals V153. For EVERY alpha>alpha153 the fixed Stage153 supporting line H(root)-(11954/17)*alpha lies STRICTLY below V14(alpha).

## Dual lower bound (680 exact Bellman states)
For state (n,a,b), Q/P likelihood ratio equals (2/3)^a 2^b. With K=5994/17, L=5960/17 define H by the three possible actions: P-stop cost K*(2/3)^a 2^b; Q-stop L; continue cost 1+sum_i P_i H(child_i) for n<14. All 680 states were evaluated with exact Fraction arithmetic. H(root)=79691642847444362851/310422953206480896. Precisely two Q/C ties remain, B=(11,0,1) and Z=(12,2,2); all 1238 other action gaps are positive, minimum 71917/33841152, with no negative gaps. Therefore H(root)<=tP+K eQ+L eP<=max(tP,tQ)+(K+L)*alpha for every policy feasible at alpha, proving V14(alpha)>=H(root)-(11954/17)*alpha.

## Complete ordered-history primal realization
B and Z are incomparable in the prefix order: B is at depth 11 with a=0, Z at depth 12 with a=2, and B cannot gain two a-hits in one step. Z cannot precede B. Thus no ordered history reaches both tied states, and there are no downstream ties. Strict Bellman continuations yield first-hit families:
B: 11 distinct ordered prefixes; P mass 107421875/1451188224; Q mass 107421875/725594112.
Z: 1555 distinct ordered prefixes; P mass 607421875/61917364224; Q mass 607421875/34828517376.

Distinct ordered prefixes at a common count state share the same P/Q likelihood ratio and conditional continuation; consequently any history-dependent tied-state coins have effective P-weighted mean stop-Q probabilities b,z in [0,1]. Because the first-hit families are disjoint, all Bellman-optimal four-coordinate observers (eP,eQ,tP,tQ) are exactly M00+b dB+z dZ, without a b*z cross term. Four deterministic corners were calculated by TWO DIFFERENT algorithms: (i) Fraction backward recursion over count states, and (ii) literal ordered-prefix integer DFS using P=(3,1,20)/24, Q=(1,1,10)/12. All 16 coordinates agree EXACTLY; mixed cross term equals (0,0,0,0). See verifier and certificate for exact four-corner vectors and 465880–475342 DFS visits per corner.

The exact error balancing equation is
b(z)=2686983670724537/2714624000000000-(9019/127248)*z.
For all real 0<=z<=1, b(z) lies strictly in (0,1). At z=1 b=7483735012173611/8143872000000000. The alpha(z)=eP=eQ and both tP(z),tQ(z) are affine. Their z=0 values reproduce (alpha152,V152), and at z=1 they give (alpha153,V153); alpha strictly increases by Delta. At z=0 the exact tP-tQ margin is 12253888791127786955/26404211196268904448>0, and at z=1 it is 36937438597383360865/79212633588806713344>0. Affinity makes tP>tQ for EVERY REAL intermediate z. Further, tP+K eQ+L eP=H(root) exactly at both endpoints, hence along the full line segment. Since alpha(z) spans the entire real interval, these policies attain the dual bound, proving the theorem.

## Strict right sharpness
Finite-horizon complete-history randomized strategies form a compact feasible set (equivalently mixtures over finitely many deterministic strategies), so optima are attained. Equality V14(alpha)=H(root)-(K+L)*alpha with K,L>0 would force eP=eQ=alpha, tP=max(tP,tQ), and Bellman-optimal actions at every reached history. Positive P probabilities and strict gaps leave only Q/C coins at B,Z; by the proved ordered-first-hit aggregation, their observations are M00+b dB+z dZ. Balance forces the displayed b(z). For z in [0,1], the maximal balanced alpha is alpha153, contradiction when alpha>alpha153. Hence strict inequality beyond alpha153. This does NOT prove Stage154's next supporting line.

## Evidence, limitations and next question
VERIFY_STAGE153.py recomputes the 680-state exact Bellman support, both distinct ordered/full-history observer algorithms, the 4 corners, first hits, balancing law, dual equality and strict tP dominance. certificate153.json holds the exact rational numeric witnesses. The companion downloadable portable bundle contains the complete original proof, source, captured stdout and SHA256. This is AUTHOR-level finite auxiliary mathematics, not independent Driver/Source acceptance and not a P000/native-X6 Cell or heartbeat theorem; preserve positive rational branch provenance and full history.

Next Stage154: saturate Z Q-stop, keep B Q/C equality, find next exact Bellman gap closure. If new first-hit sets have ancestor/descendant relation, retain mixed terms and conditional first-hit dependencies rather than silently treating coins as independent.
