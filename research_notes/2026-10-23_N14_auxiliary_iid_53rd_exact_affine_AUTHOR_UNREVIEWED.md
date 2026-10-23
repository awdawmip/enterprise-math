# Exact 53rd affine interval of the N=14 auxiliary iid sequential discrimination problem

**2026-10-23. Author-side exact finite-model result; no independent Research Driver approval, formal task CLAIM/Result, proof-assistant formalization, or native BRC/X6/Heartbeat equivalence.**

## Model, inherited endpoint, exact theorem

For iid ternary observations, under hypotheses P and Q respectively, let P=(1/8,1/24,5/6) and Q=(1/12,1/12,5/6), with at most N=14 observations. An arbitrary ordered-history-dependent randomized stopping/decision policy has errors eP=P(decide Q), eQ=Q(decide P) and sample means tP, tQ. Define V14(alpha)=inf max(tP,tQ) over eP,eQ <= alpha.

The 52nd endpoint, inherited from the author-checked source research_notes/2026-10-23_N14_auxiliary_iid_52nd_exact_affine_AUTHOR_UNREVIEWED.md (source commit fbe4038159c6601026c312a7b2f9d5fc3e0be7af), is

alpha52 = 1292956446600961517/3725075438477770752,
V52 = 24752812520708302205/1862537719238885376,
s52 = 264923490880289/417792000000000,

where s52 is the probability of deciding Q immediately at B=(12,0,1). The full inherited deterministic stop tree is specified in the companion exact verifier. In particular, earlier states A51=(10,4,4) and A52=(3,0,3) now terminate with Q at the inherited endpoint.

**Theorem.** Define K53=297764424/19019, Gamma53=563813280/19019 and eta53=19019/183954342640877568. For **every real** delta in [0,eta53],

V14(alpha52+delta) = V52 - Gamma53*delta.

The new sharp right endpoint and value are

alpha53 = 5171825786405386607/14900301753911083008,
V53 = 24752812514999692745/1862537719238885376.

The stated Bellman supporting line cannot remain optimal past alpha53. This does not say the value function terminates there.

## 1. Exact global Bellman-dual certificate

At count state x=(n,a,b), counting a zeros and b ones, the likelihood ratio Q(history)/P(history) equals r(x)=2^(a+b)/3^a. Set lambdaQ=K53=297764424/19019 and lambdaP=72+8*K53/9=266048856/19019, so lambdaP+lambdaQ=Gamma53.

For all 680 states with n<=14, recursively define

D(x)=min{lambdaQ*r(x) [stop P], lambdaP [stop Q], 1+sum_i P_i*D(child_i) [continue, n<14]}.

The finite exact Fraction checker enumerates 1240 nonselected-action comparisons against the inherited prescribed actions: exactly 1238 strict positive slacks, zero negative slacks and two ties only, at A53=(10,8,2) (continue/P) and B=(12,0,1) (continue/Q). It obtains

D(root)=21468457721702813719200575/2083741463659080056832
       =V52+Gamma53*alpha52.

Conditional minimization over actual ordered histories, including history-dependent randomization, yields D(root)<=tP+lambdaP*eP+lambdaQ*eQ<=max(tP,tQ)+Gamma53*alpha for eP,eQ<=alpha. Hence V14(alpha)>=V52+Gamma53*(alpha52-alpha) globally; no Markov-policy restriction is imposed.

## 2. Exact first-stop reach and suffixes

New tie state A53=(10,8,2) has 10!/(8!2!)=45 nominal ordered histories. Applying every earlier first-stop rule on all prefixes leaves **27 truly reachable histories** (18 already stopped), with unconditional masses under P and Q respectively:

pA=3/1073741824; qA=1/2293235712.

At B exactly 12 histories first hit, with pB=48828125/725594112 and qB=48828125/362797056. After continuing, the conditional quadruples (eP,eQ,tP,tQ) are

cA=(61/331776,20705/20736,14945/13824,75/64),
cB=(63/64,1/144,9/8,13/12).

An unordered multinomial terminal count would overcount the 18 already-stopped A53 paths. Ordered branch provenance must be retained, in the typed positive-rational weighted-branch sense (not a native-physics identification). A53 and B prefix cylinders are disjoint since A53 has 8 zeros and B has 0; therefore their randomization cross term vanishes.

## 3. Constructive primal strategy and balance

At A53 stop and decide **P** with probability u in [0,1] and otherwise continue; at B stop and decide **Q** with probability s and otherwise continue. Hold every other inherited action fixed. Define

X=pA*cA.eP=61/118747255799808,
Y=qA*(1-cA.eQ)=31/47552535724032,
E=pB*(1-cB.eP)=48828125/46438023168,
H=qB*cB.eQ=48828125/52242776064.

Compared with (u,s)=(0,s52), the exact errors are

eP-alpha52 = -X*u+E*(s-s52),
eQ-alpha52 = +Y*u-H*(s-s52).

Set s=s52+h53*u, with

h53=(X+Y)/(E+H)=13077/22282240000000.

Then E*h53-X=Y-H*h53=eta53>0, so **eP=eQ=alpha52+eta53*u for every real u in [0,1]**. The stopping probabilities remain feasible because

0<s52<=s<=s53=1059693964501931/1671168000000000<1.

Exact forward/absorbing recursions show tP(u)=V52-Gamma53*eta53*u. Both sample means are affine in u on the disjoint A53/B cylinders, and tP-tQ is strictly positive at both endpoints:

u=0: 291786475196600941/620845906412961792;
u=1: 583572947328234467/1241691812825923584.

Consequently max(tP,tQ)=tP for the whole continuum, and the constructed policy attains the global Bellman-dual lower bound. This proves the theorem, not merely a finite-grid numerical claim.

## 4. Sharpness against arbitrary histories

If the same support line were attained at alpha>alpha53, positivity of both multipliers forces eP=eQ=alpha. Bellman complementary slackness forces all reachable actions to be optimal. The exhaustive finite check shows only A53/B ties; all other actions are fixed. Even history-specific randomization at A53/B has, after likelihood weighting, effective mixture probabilities u,s in [0,1], since histories at the same count state have the same conditional suffix laws and likelihood ratio. Both error equalities therefore force s=s52+h53*u and alpha=alpha52+eta53*u<=alpha53, contradiction. A finite-horizon randomized-policy simplex is compact, so the infimum is attained; the line cannot continue beyond alpha53.

## 5. Evidence, scope and next question

The companion portable exact Python verifier checks the full 680-state/1240-action Bellman certificate, exact first-hit reach, rational suffixes, five rational randomization settings, exact endpoints, and the next dual candidate. A second author-side checker independently minimizes Bellman, enumerates all 3^10=59049 ordered words for reach, checks four absorbing-backward randomization corners and five test settings. Both use exact fractions; sharing the declared historical stop sets means they do **not** constitute an independent Research Driver review. Neither script uses native BRC/X6/Heartbeat dynamics.

After committing A53 to immediate P, the next **dual candidate only** is K54=19909275768/1359829, A54=(7,3,4), continue versus immediate Q; its full affine interval is not proved.

Knowledge snapshot: awdawmip/chatgpt-global-knowledge@674c44f8c3c194a82c63f0bba6da995d1d307ad3, with exact P000 original/projection blob match and ACTIVE worldview unchanged. Pre-publication project source: awdawmip/enterprise-math@fbe4038159c6601026c312a7b2f9d5fc3e0be7af. BRC reuse status REUSE_APPLIED to typed positive-rational branches with first-stop provenance, not to a physical transfer map. AUTHOR_UNREVIEWED; no CLAIM, no Result freeze and no Foundation/Working Truth promotion.
