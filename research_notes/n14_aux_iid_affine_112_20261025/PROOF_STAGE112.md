# Stage112 — exact real-affine optimum (external ternary iid N=14)

**Status:** AUTHOR_EXACT_FINITE_PROOF, two distinct author-side exact-rational checks. This is not a native Enterprise Math CLAIM/Result, independently approved Research Driver finding, or P000/X6/Heartbeat theorem.

**Fixed sources:** GLOBAL_KNOWLEDGE_V1 main@3eb70ebb18d1593932f92ad3cbb5c88db052c82f; Enterprise Math main@774e1d02b3c22f2054a16f8a48ab5c15fc7b6cf9; P000 canonical Git blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc. Consumed the Stage111 author proof in `research_notes/n14_aux_iid_affine_111_20261025/PROOF_STAGE111.md`, rather than repeating it.

## Precise model and theorem

Let P=(1/8,1/24,5/6) and Q=(1/12,1/12,5/6) be iid laws on symbols 0,1,2, with maximum stopping horizon N=14. Strategies may depend on the *complete ordered history*, may randomize at each visited history, stop by 14 and decide P or Q. Put eP=P(decide Q), eQ=Q(decide P), tP=E_P(tau), tQ=E_Q(tau), and V14(alpha)=inf_{eP,eQ <= alpha} max(tP,tQ).

Use the existing exact Stage111 endpoint:

- alpha111 = 13084629088533672707/37682150988866125824;
- V111 = 1930486964443856499985/150728603955464503296;
- at A=(10,3,0), immediate P-decision probability u0=199112072506703/211315200000000, otherwise continue;
- at F=(4,0,2) the action is deterministically Q-stop, with the remaining unique actions inherited from Stage111.

**Theorem:** For **every real** 0 <= delta <= eta112, where

eta112 = 152537125/130840802044674048,

the exact optimum is

V14(alpha111+delta) = V111 - (13995465/7696)*delta.

In particular, the new endpoint is

alpha112 = 13084629132464364707/37682150988866125824,

V112 = 1930486644885404154985/150728603955464503296.

The stated endpoint is sharp for **this supporting line**; the value function itself can continue after the endpoint.

## Global Bellman dual (no count-only restriction on competitors)

In count state s=(n,a,b), n observations with a zeros and b ones, the exact conditional likelihood is R(s)=Q/P=2^(a+b)/3^a. Fix

K112=50591871/53872, L112=2961024/3367,

and H(s)=min{K112*R(s), L112, 1+(1/8)H(n+1,a+1,b)+(1/24)H(n+1,a,b+1)+(5/6)H(n+1,a,b)}; delete the continuation action at n=14.

The exhaustive Fraction calculation covers all 680 count states and all 1240 nonchosen action comparisons. Precisely 1238 are strictly positive, 2 are zero, none negative; minimum positive slack 323/40404. Exactly two tie states:

- A=(10,3,0): P-stop / continue;
- T=(14,7,4): P-stop / Q-stop, already at the terminal horizon.

Every other minimizing action agrees with the Stage111 right-end policy. At root,

H(0,0,0)=33952339699463001562465/52698861350229639168
        =V111+(K112+L112)*alpha111,

and K112+L112=13995465/7696.

At each individual ordered prefix, iid conditional likelihoods depend on its counts and continuation has the same child conditionals; Bellman induction is therefore a valid lower bound for **every ordered-history strategy**, not only policies that choose actions by counts. In particular

H(root) <= tP + L112*eP + K112*eQ <= max(tP,tQ)+(K112+L112)*alpha.

## Positive rational BRC branch carrier, reachability and disjoint cones

Preserve literal ordered branch identity and positive rational P/Q masses until projecting onto the proved-sufficient count/moment observer. At fixed count state the Q/P ratio is constant across all its literal prefixes, so averaging history-specific randomization under P yields the *same* effective probability under Q; this is the only quotient used in sharpness.

At old tie A, 120 actual first-hit prefixes carry

mP(A)=390625/5971968; mQ(A)=390625/20155392.

At new terminal tie T, literal ordered DFS detects **10148** actual first-hit histories (not all 14!/(7!4!3!)=120120 nominal permutations). Exact total first-hit masses:

mP(T)=317125/37572373905408,
mQ(T)=317125/40122452017152.

No ordered path can visit both ties: after A=(10,3,0) there are only four further observations until T=(14,7,4), but T would require FOUR additional zeros and FOUR additional ones, impossible in four steps. T cannot precede A, being terminal. Therefore all four root moment/error functions are exactly affine in the two randomizations, with no mixed u*w term.

## Full continuous feasible primal construction

Let u denote the probability of P-stop at A, otherwise continue. Let w denote the probability of Q-stop at terminal T, otherwise P-stop. Elsewhere follow the unique Bellman actions. At (u0,w=0) the previous Stage111 endpoint has eP=eQ=alpha111, tP=V111 and tQ=114606239754171547805/9420537747216531456.

Exact first-hit and forced-continuation suffix recurrences give these partial derivatives:

deP/du = -248046875/990677827584;
deQ/du = 65234375/208971104256;
dtP/du = -3012109375/41278242816;
dtQ/du = -417578125/17414258688;
deP/dw = 317125/37572373905408;
deQ/dw = -317125/40122452017152;
dtP/dw = dtQ/dw = 0 (T is terminal).

The **exact** balance eP=eQ reduces to

u(w)=u0+(306977/10565760000)*w; 0 <= w <= 1.

It remains feasible throughout: 0<u0<u(1)=66372737348901/70438400000000<1. Substitution gives

eP(w)=eQ(w)=alpha111+eta112*w,

tP(w)=V111-(13995465/7696)*eta112*w.

At w=1:
tP=1930486644885404154985/150728603955464503296;
tQ=114606233191003287805/9420537747216531456;
tP-tQ=32262304609783850035/50242867985154834432 > 0.

At w=0, tP>tQ already follows from Stage111, and both times are affine; hence tP>tQ at *every real* w in [0,1]. All selected actions are Bellman minimizing, so H(root)=tP+L112*eP+K112*eQ at every w. This meets the universal lower bound with equality and proves full global optimality for the entire real interval—not numerical interpolation.

## Sharpness against arbitrary ordered-history randomization

The finite history-tree realization-measure feasible set is compact. If the **same** supporting line were attained at alpha>alpha112, strictly positive K112,L112 force eP=eQ=alpha and Bellman-minimizing actions at every positive-mass visited prefix. The only ties are A and T. Conditional Q/P is constant among literal prefixes with the same count state, so their P-mass weighted randomization averages equally under Q; the A and T cones are disjoint. Every line-attaining history-dependent policy thus has equivalent aggregate parameters u,w in [0,1]. Balance necessarily gives u=u0+(306977/10565760000)*w and hence alpha=alpha111+eta112*w <= alpha112, a contradiction. This proves sharpness of the supporting face and makes no false assertion of termination of V14.

## Exact independent execution and limitations

Local primary exact Fraction recursion enumerated 680 Bellman states and 1240 alternatives, computed the forward weighted first-hit counts/masses and all four root moments at u,w=0/1, checked the zero interaction, endpoint identity and lower-bound equality, and scanned all affine gaps along the tie face. Independently written `INDEPENDENT_STAGE112.py` recomputed the Bellman recursion and root moments **backwards**, checked w=0,1/2,1, and enumerated 886309 *literal ordered prefixes* with A forced to stop to confirm T's 10148 first hits and both exact masses. The disjointness proof makes this A convention irrelevant to T. Both ran and returned PASS. The attached local research archive additionally preserves the complete main checker, independent code and original run transcripts.

These are two **author-side** exact implementations, not a clean-blind independent Driver or a formalized proof in a proof assistant. The finite exhaustive computation's theorem scope is precisely the external iid horizon-14 model, not native P000/X6/Heartbeat.

## Next successor: dual-only Stage113

Along the A-equality face L(K)=-185064/635+(21376/17145)*K, select Q-stop at T and decrease K from K112. Every nonchosen fixed-policy gap is affine. The next downward positive-gap zero is

K113=814106972531223/875100809116;
L113=189992854025880/218775202279.

The new tie is C=(5,2,3), Q-stop/continue; old A remains P-stop/continue. An independent Bellman evaluation at this point again gives 680 states, 1238 strictly positive gaps, and exactly two ties. This identifies **only** the dual candidate, *not* a Stage113 primal optimum. Next determine C's truly reachable ordered first hits and conditional suffixes, path-cone overlap, and balanced feasible interval; prove a full real segment and sharp endpoint or certify a zero-mass obstruction.

**Authority:** Native task listing returned `CONTROL_QUOTA`; session creation returned `STATIC_READONLY_SCOPE_DENIED` with `operation_sent=false`. No native owner, CLAIM, Result, Driver acceptance, or P000 transfer has been verified. GitHub author-side research storage is not a canonical Source claim.
