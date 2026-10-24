# N=14 auxiliary iid sequential discrimination: exact 78th affine segment

**Author-side mathematical result, 2026-10-24; not independently reviewed or natively CLAIMed.**

## Theorem and scope

Under iid laws P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6) with at most N=14 observations, let eP=P(decide Q), eQ=Q(decide P), tP,tQ the respective expected sample counts, and V14(alpha) the infimum of max(tP,tQ) over all (possibly ordered-history-dependent randomized) stopping rules with both errors at most alpha.

The inherited author-level endpoint is alpha77=5171945831199762833/14900301753911083008, V77=24565111516140071249/1862537719238885376, and balance Q-coin s77=23988151419202381/41779200000000000 at B=(12,0,1).

For **every real** 0<=delta<=eta78, with

eta78=64297685/413897270941974528,
Gamma78=82093429818/12859537,

**V14(alpha77+delta)=V77-Gamma78*delta.**

Consequently alpha78=5171945833514479493/14900301753911083008, and V78=3070638708629737543/232817214904860672. The 78th dual support line cannot attain the optimum beyond alpha78.

## Global Bellman lower bound

Count-state (n,a,b) records the number of 0 and 1 observations, with Q(w)/P(w)=2^(a+b)/3^a. For L=tP+lambdaP*eP+lambdaQ*eQ, set lambdaQ=K78=42971052258/12859537 and lambdaP=72+(8/9)K78=39122377560/12859537. At a state, immediate P costs lambdaQ*2^(a+b)/3^a, immediate Q costs lambdaP, and continuation (only n<14) costs 1+sum_i P_i D(child_i).

The exact backward Fraction recursion on all 680 states tests 1240 nonchosen action comparisons: 1238 strictly positive, zero negative. Exactly two ties exist: A78=(7,6,1) continue/P, and B=(12,0,1) continue/Q. Minimum positive gap: 20064950039/632071962624. Root D0=12562057052932436459305987297/5635617109281896077983744 = V77+Gamma78*alpha77. This statewise minimization applies also to arbitrary history-dependent randomized rules. Hence D0<=tP+lambdaP*eP+lambdaQ*eQ<=max(tP,tQ)+Gamma78*alpha for feasible policies, proving V14(alpha)>=D0-Gamma78*alpha.

## Ordered first hits and correct compensation

Freeze prior A77=(8,2,3) to Q; preserve inherited stage-77 stopping decisions. At A78, 7 nominal ordered histories exist, but only 5 genuinely first-reach it. Exact weighted masses pA=5/6291456, qA=5/35831808. At B there are 12 first-hit histories with pB=48828125/725594112, qB=48828125/362797056.

Inherited continuation suffixes (P-error,Q-error,P-extra-time,Q-extra-time) are:
RA=(923453/1146617856,5935061/5971968,56174843/47775744,2071663/1492992);
RB=(63/64,1/144,9/8,13/12).

A separate positive-weight ordered-history DFS finds 275 completed suffix words in 29 terminal states; early P at A truncates 5*275=1375 old completed paths. Path counts are not probabilities. A and B are mutually unreachable along one run (A has six 0s, B has none), so no coin-interaction cross terms appear.

At A stop and decide P with probability u; at B stop and decide Q with probability s. Define X=pA*RA.eP=4617265/7213895789838336; Y=qA*(1-RA.eQ)=184535/213986410758144; E=pB*(1-RB.eP)=48828125/46438023168; H=qB*RB.eQ=48828125/52242776064. Then Delta eP=-Xu+E(s-s77), Delta eQ=Yu-H(s-s77). Equality requires

s=s77+h78*u, h78=(X+Y)/(E+H)=526741223/696320000000000,

and produces common error alpha77+eta78*u. The two endpoint coins are strictly between 0 and 1. Exact (tP-tQ) at u=0 equals 2211861025576672651/3725075438477770752 and at u=1 equals 2211858463500674861/3725075438477770752, both positive. Every risk/time is affine in u; hence tP dominates and the selected tied actions attain Bellman lower bound throughout the real interval u in [0,1]. Seven rational interior/endpoint instances are checked directly, not used as a substitute for the affine proof.

## Sharpness and evidence boundary

Equality with the dual support line, since both multipliers are strictly positive, requires eP=eQ=alpha and every reached action be Bellman-minimizing. Only A and B admit mixing; arbitrary per-ordered-history mixing at one count state reduces to its P/Q-weighted effective coin because the likelihood ratio and suffix values are constant across its surviving histories. The cones are disjoint. Error equality fixes s=s77+h78*u and u<=1, giving alpha<=alpha78. Thus the old line is nonattaining for alpha>alpha78.

Two **author-side** exact-rational programs were executed locally: one backward/forward dynamic verifier and an ordered-word enumeration crosscheck. They share the inherited stopping table; this is not independent Research Driver approval. The original proof/source is pinned at Enterprise Math commit a4880ba6486d150077c3c8acbf99c7ded0fd6ebd, research_notes/n14_aux_iid_affine_77_20261024/. Global knowledge snapshot main@9fbf92bfcb95c7c022b3caa69839840bdef1d437. The auxiliary iid model has no established faithful mapping to native BRC/X6/Heartbeat dynamics. P000 and ACTIVE worldview are unchanged.

Native control returned CONTROL_QUOTA on task enumeration and STATIC_READONLY_SCOPE_DENIED (operation_sent=false) on new session creation; formal owner/CLAIM/Result is unverified. This GitHub publication is author-side evidence, not native task admission.

Unproved next candidate after freezing A78 to P: K79=776081412/242449 with tie A79=(8,4,0) continue/P. Verify independently, do not promote this conjectural endpoint to a theorem.
