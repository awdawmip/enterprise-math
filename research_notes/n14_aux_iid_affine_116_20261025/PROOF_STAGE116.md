# Stage116: exact optimal affine segment after Stage115 E saturation

Status: AUTHOR_EXACT_FINITE_PROOF. External auxiliary iid experiment, not a P000/X6/Heartbeat theorem. No native Owner, CLAIM, Result or independent Driver review verified. This run used GLOBAL_KNOWLEDGE_V1 main e87bad4c9c4f6b4e8748019209f29a67768a36db and Enterprise Math source main 1fbdc599d7504f5ee78279aa139768787d943a9d.

## Statement

For all randomized decisions and stopping rules on **full ordered histories** of <=14 independent ternary symbols, P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6), put eP=P(decide Q), eQ=Q(decide P), tP=E_P(tau), tQ=E_Q(tau) and V14(alpha)=inf_{eP,eQ<=alpha} max(tP,tQ). The Stage115 author-derived endpoint is

alpha115 = 900390060440962701793 / 2592933255351443128320,
V115 = 132635694365041929281069 / 10371733021405772513280.

**Theorem:** For K=37550061/41440, L=3296576/3885, S=K+L=6232589/3552 and eta=22731875/28581715777683456, for every **real** 0<=delta<=eta,

V14(alpha115+delta) = V115 - S*delta.

Consequently alpha116 = 900390062503198401793/2592933255351443128320 and V116 = 132635679890866772493569/10371733021405772513280. This supporting affine line is strictly below the optimum at **every** alpha>alpha116.

## Exact Bellman dual over every history

At count state s=(n,a,b) (a = number of symbols 0, b = number of symbols 1), the conditional likelihood ratio is R(s)=Q(s)/P(s)=2^(a+b)/3^a. In conditional P-units define at n<14

H(s)=min{ K*R(s) [decide P], L [decide Q], 1+H(n+1,a+1,b)/8+H(n+1,a,b+1)/24+5*H(n+1,a,b)/6 [continue] }.

At n=14 only the first two actions are permitted. An exhaustive Fraction recurrence over sum_{n=0}^{14} binom(n+2,2)=680 states finds exactly 1,238 strictly positive action gaps, none negative, min positive gap 200314681163/7919307325440 and precisely two ties:
D=(9,1,2): decide Q vs continue;
T=(14,7,4): decide P vs decide Q.
At T, R(T)=2048/2187 and K*R(T)=L. E=(12,4,1), formerly tied, is now uniquely decide P. Exact root:

H(0,0,0) = 529581447731753074942871/851289298734478786560 = V115 + (K+L)*alpha115.

Induction on the **full ordered-prefix tree**, allowing arbitrary history-dependent randomized actions, proves H(0,0,0)<=tP+L*eP+K*eQ. Count compression is used only for the iid conditional future law and these four finite-horizon moment observations. Therefore V14(alpha)>=H(0,0,0)-(K+L)*alpha for all alpha.

## First dual wall after Stage115

The previous dual point is K0=2533113/2734, L0=1181272/1367, where D and E tied. Choose Stage115 actions Qstop at D and Pstop at E to represent action values as affine rational forms in K,L. Keeping D tied and decreasing the slope K+L gives the exact ray:

K=K0-x, L=L0-(164096/214569)*x, x>=0.

All formerly positive action gaps are affine along this ray. The **unique first positive zero** of these gaps is x*=1155167973/56648480, at T for alternative Pstop; no other gap closes earlier. A separate direct 680-state Bellman recomputation at the resulting (K,L) verifies every global inequality; the ray sweep alone is not used as proof of optimality.

## Positive rational ordered-history carriers

At D decide Q with probability w, else continue; at terminal T decide P with probability u, else decide Q. E is uniquely Pstop. All other states take the new unique minimizing action. First arrival on literal ordered words with D continuing and E stopping has these exact masses:

D: 172 ordered histories; P-mass 671875/53747712; Q-mass 671875/20155392.
T: 9830 ordered histories; P-mass 614375/75144747810816; Q-mass 614375/80244904034304.

The cones are disjoint: from D at depth 9 with a=1, it is impossible to reach T at depth 14 with a=7 (requires 6 new zeros in 5 steps). T cannot precede D. From E at depth 12 a=4 to T at depth 14 a=7 also needs 3 zero outcomes in two steps. These are exact positive-rational labeled-history carriers (BRC-like interface), not signed amplitude cancellation.

Let M=(eP,eQ,tP,tQ). Because the cones are disjoint M(w,u) is **exactly affine** (no wu interaction). Its derivatives, checked by both direct recursion and an independently implemented literal ordered-history integer DFS, are

dw M = (593265625/5283615080448, -430671875/5015306502144, -34607609375/1981355655168, -17355203125/417942208512);
du M = (-614375/75144747810816, 614375/80244904034304, 0, 0).

Stage115 endpoint is realized at w0=374236473161181/1042086080000000, u=0, with both errors alpha115, tP=V115>tQ. Imposing eP=eQ gives the exact *legal* family

w(u) = w0 + (118943/1488694400)*u,  0<=u<=1.

Here 0<w0<w(1)=374319733261181/1042086080000000<1. Along the entire **continuous real** segment,

eP=eQ=alpha115 + eta*u,
tP=V115-(K+L)*eta*u,
tP>tQ.

The last inequality holds by strict positivity at both endpoints and affinity. These strategies use only Bellman minimizers and attain the global lower bound, proving the theorem.

## Strict right-end sharpness for arbitrary ordered-history policies

The finite randomized stopping-decision policy space is compact, so an optimum exists. If any alpha>alpha116 attained the same Bellman supporting line, K,L>0 would force both eP=eQ=alpha and all positive-mass actions to be minimizers. Only D and T may be mixed. At a fixed tied count state the P/Q likelihood ratio and conditional iid suffix response for these four moments are the same over every first-hit history. Any history-specific mixing can therefore be averaged with positive P-first-hit mass into parameters (w,u) in [0,1]^2, preserving all four moments. The disjoint cones ensure zero mixed term. Equality eP=eQ forces w=w0+(118943/1488694400)*u and alpha=alpha115+eta*u<=alpha116, a contradiction. Thus strictness follows.

## Executed evidence and boundaries

The local full script CHECKER_STAGE116.py passed exact Fraction Bellman, 680-state action inequalities and ray wall, 1,238 strict gaps, two ties, rational first-hit masses, full primal family and sharpness identities.
An independently implemented INTEGER ordered-history DFS recomputed all four deterministic corners; prefix visits were 862459/854719/862459/854719, and all moment derivatives plus zero interaction agreed. The local full files and raw logs are included in the user-accessible Stage116 reproduction ZIP. Code below is a *portable source-level* reproduction; GitHub file bytes should not be represented as remotely executed unless actually run.
No current native Owner/CLAIM/Result/Driver review was obtained: native tasks -> CONTROL_QUOTA; native session_start -> STATIC_READONLY_SCOPE_DENIED, operation_sent=false. No physics transfer or infinite-horizon claim.

Next: Stage117, after T saturates at Pstop probability 1 and D remains interior, continue along the D tie ray and resolve the next genuine wall, cone structure and constraints.
