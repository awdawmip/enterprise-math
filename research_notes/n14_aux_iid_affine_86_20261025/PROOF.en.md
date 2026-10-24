# Auxiliary N=14 iid sequential test: exact stage86 affine segment

**2026-10-25; author-level finite-model proof.** This is not a native BRC–Shor/X6/Heartbeat assertion, native TASK Result, independent Driver review, or Lean-formal proof. The complete local reproducibility bundle also contains a more verbose proof.

## Exact question and theorem

Ordered observations x_i in {0,1,2}, stopping time T<=14, distributions P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6). Full ordered-history randomized tests are admitted. Define eP=P(decide Q), eQ=Q(decide P), tP=E_P T, tQ=E_Q T and V14(alpha)=min max(tP,tQ) over tests with both errors <=alpha.

Consume the stage85 author endpoint and frozen stopping table, `alpha85=5172040863158315543/14900301753911083008`, `V85=24497784123642713729/1862537719238885376`; frozen predecessor `derive85.py` Git blob `1ffa81ccbca4f657e1dce7c032267e2ed5fee9d6`.

**Theorem.** For *every real* 0<=delta<=107421875/4736678363136,

V14(alpha85+delta) = V85 - 4356*delta.

The sharp right endpoint of this supporting affine segment is

alpha86=5172378783158315543/14900301753911083008,

V14(alpha86)=24313786683642713729/1862537719238885376.

## Global exact Bellman certificate

For count state (n,a,b), likelihood ratio Q/P=2^(a+b)/3^a; there are exactly sum_{n=0}^{14}(n+1)(n+2)/2=680 count states. Fix K86=2268, lambdaQ=2268, lambdaP=72+8*K86/9=2088, Gamma=lambdaP+lambdaQ=4356. Dividing weighted conditional risk by P-prefix mass yields Bellman costs: stop-P=lambdaQ*(Q/P), stop-Q=lambdaP; continue=1+sum_i P_i D(child_i). Use the predecessor selected actions with A85=(11,5,1) now stop P; A86=(12,3,0) and B=(12,0,1) select continue for dual evaluation.

`derive86.py` runs exact rational backward recursion over all 680 states: 1240 nonchosen action gaps, 1238 strict positives, zero negatives; the only two zero comparisons are A86 continue/stop-P and B continue/stop-Q, minimum strictly positive gap 5/432. The exact root is

D0=334196945189805356105/219122084616339456
  =V85+4356*alpha85.

Bellman induction remains valid for arbitrary decisions on each ordered prefix because conditional laws and likelihood ratios coincide at the same count state. It gives, for every test,

D0 <= tP+2088*eP+2268*eQ
   <= max(tP,tQ)+4356*alpha,

hence V14(alpha)>=D0-4356*alpha globally, not merely among count-adapted policies.

## Weighted history and suffix certificate

At A=A86=(12,3,0), all 220 nominal ordered prefixes are genuine first hits under the inherited stop map. Independent ordered DFS checks their masses

pA=107421875/1289945088, qA=107421875/4353564672.

If sampling continues at A, its conditional tuple (P-error,Q-error,extra P-time,extra Q-time) is RA=(1/576,143/144,25/24,13/12). Exactly 5 terminal suffix words occur, so immediate stopping truncates 220*5=1100 complete ordered words. This count is not a probability.

At B=(12,0,1), 12 nominal prefixes are all real first hits, with pB=48828125/725594112 and qB=48828125/362797056; continuation tuple RB=(63/64,1/144,9/8,13/12). The independent DFS `crosscheck86.py` verifies these identities and its 5 terminal suffix words.

A and B have the same depth n=12 but distinct count vectors: no single ordered path can visit both. All performance functionals are therefore *jointly affine* in the probabilities u of immediate P at A and s of immediate Q at B, with no u*s cross-term. History-dependent randomization within one count fiber collapses to one effective parameter because all prefixes there share likelihood ratio and conditional suffix laws.

## All-real feasible primal attainment

At stage85's baseline, u=0 and S=s85=22950702493354427/41779200000000000. Define exact positive quantities

X=pA*RA[P-error]=107421875/743008370688,
Y=qA*(1-RA[Q-error])=107421875/626913312768,
E=pB*(1-RB[P-error])=48828125/46438023168,
H=qB*RB[Q-error]=48828125/52242776064.

The two errors obey the *identities*

eP-alpha85 = -X*u + E*(s-S),

eQ-alpha85 = +Y*u - H*(s-S).

Setting s=S+h86*u with h86=(X+Y)/(E+H)=649/4080 therefore forces both errors equal to alpha85+eta86*u, where eta86=-X+E*h86=Y-H*h86=107421875/4736678363136>0. Randomization is feasible for **all** real u in [0,1]: 0<S<=s<=S+h86=9865487497784809/13926400000000000<1.

Exact endpoint forward calculations give

(tP-tQ)_{u=0}=2356622709392786305/3725075438477770752>0,

(tP-tQ)_{u=1}=724865489797595435/1241691812825923584>0.

Since tP-tQ is affine in u, tP>tQ throughout. Every positive-mass selected action is a Bellman minimizer, so tP+2088*eP+2268*eQ=D0 identically. Therefore max(tP,tQ)=tP=V85-4356*eta86*u. This attains the global lower bound continuously for all reals u, proving the theorem after u=delta/eta86. Rational interpolation checks in code are consistency checks, not the proof of continuum validity.

## Right-endpoint sharpness

If alpha>alpha86 attained the **same** affine support, both positive Lagrange multipliers force eP=eQ=alpha, and Bellman equality forces only the two tie states A and B to randomize: all other alternatives have strictly positive exact gaps. Within each same-count fiber, effective averaged u,s in [0,1] preserve errors and sampling time. Disjoint depth-12 cones force the identical affine error equations above. Equal errors then imply s=S+h86*u and alpha=alpha85+eta86*u<=alpha86, contradiction. Finite ordered-history randomized strategy spaces are compact, so a supposed equality limit cannot evade attainment. This proves sharpness of **this supporting line**, not nonexistence of subsequent optimal segments.

## Scope, reproducibility, continuation

`derive86.py` and `crosscheck86.py` were executed locally with Python Fraction; 680-state comparisons, first hits/suffixes and eight exact-rational interpolation checkpoints passed. Their inherited selected-action map is shared: **author-side, not independent Driver review**. Native control inventory returned `CONTROL_QUOTA`; native session_start returned `STATIC_READONLY_SCOPE_DENIED` / `operation_sent=false`; no Owner, CLAIM, or native Result has been asserted. No native BRC-only experiment was run.

The *unproved* next directional dual candidate after fixing A86 to immediate P is K87=26244/13, A87=(13,7,3), continue/stop-P. Determine true first-hit masses and words, suffix paths, cone overlap, exact error compensation, full Bellman gaps, all-real attainment/sharpness, or an exact obstruction. See `NEXT_TASK_PACKET_87.md`.
