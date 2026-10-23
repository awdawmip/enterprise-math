# Exact 54th affine interval of the N=14 auxiliary iid sequential test

**Date:** 2026-10-23. **Status:** Author-level exact finite-model proof, not independently Research-Driver reviewed, Lean-formalized, or a native Task CLAIM/Result. This auxiliary iid theorem is **not** a result about native BRC/X6/Heartbeat. P000 and ACTIVE worldview remain unchanged.

## Model, inheritance and exact theorem

Observations are iid over symbols 0,1,2 under P=(1/8,1/24,5/6) and Q=(1/12,1/12,5/6), with at most 14 samples. Arbitrary ordered-history-dependent randomized stopping/decision policies are allowed. Let eP=P(decide Q), eQ=Q(decide P), and tP,tQ be expected sample counts. Set V14(alpha)=inf max(tP,tQ) subject to eP,eQ<=alpha.

Inherit the author-checked 53rd right endpoint and complete deterministic first-stop table from research_notes/2026-10-23_N14_auxiliary_iid_53rd_exact_affine_AUTHOR_UNREVIEWED.md and its portable checker at prepublication source 437c23344107b562abc0df00aed580c269eb15d3:

alpha53=5171825786405386607/14900301753911083008,
V53=24752812514999692745/1862537719238885376,
s53=1059693964501931/1671168000000000.

The s53 mixture is the probability of immediate Q at B=(12,0,1). The previous A53=(10,8,2) tie has been fixed to immediate P, while earlier stop rules (including A51 and A52 fixed to Q) remain in effect.

**Theorem.** Put K54=19909275768/1359829, Gamma54=37704317472/1359829, eta54=25836751/4966767251303694336. For **every real 0<=delta<=eta54**,

`V14(alpha53+delta) = V53 - Gamma54*delta`.

The exact right endpoint and value are

alpha54=1292956446620724215/3725075438477770752,
V54=24752812246356430757/1862537719238885376.

The stated supporting line is no longer the optimum for any alpha>alpha54; the entire value function does not terminate here.

## Bellman certificate: global over all ordered histories

For x=(n,a,b) counting a zeros and b ones, the likelihood ratio is r(x)=Q(h)/P(h)=2^(a+b)/3^a. Define positive multipliers lambdaQ=K54 and lambdaP=72+8*K54/9=17795041704/1359829, hence lambdaP+lambdaQ=Gamma54. On all count states n<=14 compute the exact rational recursion

`D(x)=min{lambdaQ*r(x) [decide P], lambdaP [decide Q], 1+sum(P_i*D(child_i)) [continue if n<14]}`.

The 680 states give 1240 comparisons to nonchosen actions: 1238 strictly positive, zero negative, and exactly two zero ties, at A54=(7,3,4) (continue/Q) and B=(12,0,1) (continue/Q). The root identity is

D(root)=1435804691903091429843461929/148984282600876133056512
       =V53+Gamma54*alpha53.

Backwards conditioning on **each actual ordered history**, not assuming a count-Markov strategy, gives D(root)<=tP+lambdaP*eP+lambdaQ*eQ<=max(tP,tQ)+Gamma54*alpha under the two error constraints. Therefore V14(alpha)>=V53+Gamma54*(alpha53-alpha) globally.

## True first-stop reach and nested history

A54=(7,3,4) has 7!/(3!4!)=35 nominal ordered words, of which exactly 19 survive all inherited *first-stop* rules; 16 terminate earlier. Their unconditional masses are pA=19/169869312 and qA=19/35831808. At B exactly 12 words survive, with pB=48828125/725594112 and qB=48828125/362797056.

Conditional on continuation using all inherited deterministic stopping decisions, the quadruples (eP,eQ,tP,tQ) are

cA=(18868387/18874368,1465/35831808,1029439/786432,3540077/2985984),
cB=(63/64,1/144,9/8,13/12).

A54 occurs before old A51=(10,4,4). Among 3150 nominal A51 words, 1549 truly first-hit A51 under the 53rd inherited policy, and **19 of those traverse A54**. An immediate Q at A54 preempts these descendants. cA already incorporates the old deterministic Q at A51; A51 is NOT a third independent mixture. A54 and B are disjoint first-hit cylinders: A54 has three zeros, B has none, while counts are nondecreasing.

## Primal construction for the entire continuum

Let u∈[0,1] be the probability of immediate Q at A54 and s the probability of immediate Q at B, holding all other historical actions fixed. Set

X=pA*(1-cA.eP)=113639/3206175906594816,
Y=qA*cA.eQ=27835/1283918464548864,
E=pB*(1-cB.eP)=48828125/46438023168,
H=qB*cB.eQ=48828125/52242776064.

Relative to the 53rd endpoint (u=0,s=s53), exact first-hit decomposition gives

eP-alpha53=X*u+E*(s-s53),
eQ-alpha53=-Y*u-H*(s-s53).

Choose h54=(X+Y)/(E+H)=1201634119/41779200000000000 and s=s53-h54*u. Then the **identities**

eP=eQ=alpha53+eta54*u,
eta54=X-E*h54=H*h54-Y=25836751/4966767251303694336>0

hold for every real u∈[0,1]. The whole mixture is feasible:
0<s54=s53-h54=6623086977728539/10444800000000000<=s<=s53<1.

Exact forward and separately organized absorbing-backward recursions yield tP(u)=V53-Gamma54*eta54*u. Both sample means are affine in u because the A54/B cylinders do not overlap. Their differences at endpoints are

(tP-tQ)(0)=583572947328234467/1241691812825923584>0,
(tP-tQ)(1)=875360315426015843/1862537719238885376>0.

Thus tP>=tQ throughout, and the constructed strategy meets the global Bellman lower bound on the **whole continuum** (not just five test points). Setting delta=eta54*u proves the theorem.

## Sharpness for arbitrary history-dependent randomization

Suppose for alpha>alpha54 the same support line were attained. A minimizer exists by finite randomized-policy compactness. Since lambdaP and lambdaQ are positive, equality forces eP=eQ=alpha. Equality throughout the nonnegative Bellman slack decomposition excludes every strictly suboptimal action, leaving only the A54 and B ties. For histories ending at the same count state, conditional suffix laws and likelihood ratios coincide. Hence arbitrary ordered-history mixtures can be reduced, without changing risks, to effective u,s∈[0,1]. Both equal-error conditions then force s=s53-h54*u and alpha=alpha53+eta54*u<=alpha54, contradiction.

## Verification and next question

The supplied exact Fraction primary checker evaluates 680 states/1240 slacks, full inherited stop actions, true ordered first-hit reach, suffix risks, five rational mixtures, endpoint equalities and the next crossing. A second **author-side** checker enumerates all 3^7=2187 length-7 words, 3^12=531441 length-12 words and 3^10=59049 length-10 words, independently minimizes Bellman, computes four exact absorbing backward corners and verifies zero interaction plus five mixtures. Both pass, but share the declared inherited stop sets and are **not** independent Research Driver review. An initial assumed nested count was corrected using exhaustive enumeration: 1549 first-hit A51 words, of which 19 pass A54.

After fixing A54 to immediate Q, the next **dual candidate only** is K55=183708/13, A55=(12,7,2), with continue/immediate-P tie. The 55th first-hit reach, error balancing, full primal/dual interval, and right-endpoint sharpness have not been proved.

Global knowledge pin: awdawmip/chatgpt-global-knowledge@674c44f8c3c194a82c63f0bba6da995d1d307ad3 / GLOBAL_KNOWLEDGE_V1. Project prepublication source pin: awdawmip/enterprise-math@437c23344107b562abc0df00aed580c269eb15d3. Native control_tasks returned CONTROL_QUOTA; native session_start was denied STATIC_READONLY_SCOPE_DENIED (operation_sent=false). This standalone author note grants no native ownership, CLAIM, Result, review or Foundation status.
