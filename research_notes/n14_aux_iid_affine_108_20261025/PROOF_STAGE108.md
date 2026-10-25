# Stage108 — exact next Bellman support after Stage107 B saturation

**Status:** author computation-assisted exact-rational proof for an external ternary iid finite sequential test. No P000/X6-native transfer, native CLAIM, independent Driver review, or formal admission is asserted.

## Model and frozen frontier

P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6), full ordered-history randomization, stop by n=14. Define eP=P(decide Q), eQ=Q(decide P), tP=E_P(tau), tQ=E_Q(tau), and V14(alpha)=min_{eP,eQ<=alpha}max(tP,tQ). Fixed source snapshots: GLOBAL_KNOWLEDGE_V1 main 9f35cf43236aaf491ac0693f2bd3a35c22175e0e; enterprise-math main 9713f10774d8c0a64c64fb2bd9888bec5679f40d; Stage107 immutable author work a8d8ebd0fdb0b5a0d18d1302e6c53ca67a55be8d. P000 projection agrees with original Git blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc.

Stage107 endpoint:
alpha107=91588670614917102449/263775056922062880768,
V107=13541383133505475882195/1055100227688251523072.

## Exact theorem

For **every real** 0<=delta<=1457736575/2442361638167248896,

  V14(alpha107+delta) = V107 - (409248885/206588)*delta.

New endpoint:
alpha108=13084095824621807507/37682150988866125824,
V108=1934483126570299962385/150728603955464503296.

This exact supporting line is sharp: equality is impossible at any alpha>alpha108. Another supporting line may still continue the value function.

## Bellman proof and exact neighboring-face search

Let z=(n,a,b), rho(z)=2^(a+b)/3^a. For n<=14, with continuation omitted at n=14, set

  D(z)=min{K*rho(z) [decide P], L [decide Q],
           1+sum_{i=0}^2 P_i D(z+e_i) [continue]}.

For every ordered-history randomized policy, D(root)<=tP+L eP+K eQ<=max(tP,tQ)+(K+L)alpha.

At the former dual (K0,L0)=(778896/767,747576/767) the exact Bellman ties were A=(10,3,0) P/continue and B=(12,0,1) Q/continue. Freeze continuing at A and deciding Q at B and the unique minimizers elsewhere. A's P-versus-continue gap is

  G_A(K,L)=-7711/6912+(167/34992)K-(635/165888)L.

The ray (K,L)=(K0,L0)+h*(-635/165888,-167/34992) keeps A tied and decreases K+L. The continue-minus-Q gap at B changes at rate +767/35831808, so B becomes strictly Q-optimal. Exact affine policy-gap enumeration at every one of the 680 count states yields 853 candidate positive crossings and the **unique first** at

  h=42349837824/39613249; C=(11,5,4) with Q/continue.

The resulting dual is
K108=208946709/206588 >0,
L108=50075544/51647 >0,
Gamma=K108+L108=409248885/206588.

Direct exact backward Bellman enumeration at this dual finds exactly 1238 positive nonselected action gaps, zero negative, and only two tied alternative pairs: A P/continue and C Q/continue. Minimum strictly positive gap is 37821/1652704. Root dual value:

  D(root)=495598934898928452760465/707312394011255242752.

These finite exact counts are reproducible with the companion certificate and local primary author checker. The finite Bellman state quotient is sound for iid conditional continuation, but different ordered histories are retained for prefix mass and sharpness analysis.

## Ordered first-hit branch carrier and all-real primal

At the two ties, choose P at A with probability u, otherwise continue; choose Q at C with probability w, otherwise continue. All other actions are the unique strict Bellman minimizers. Ordered first-hit support:

  A: 120 distinct actual first-hit prefixes,
     P mass 390625/5971968, Q mass 390625/20155392;
  C: 2258 distinct actual first-hit prefixes,
     P mass 28225/195689447424, Q mass 28225/92876046336.

Exact continuation suffix moments (P-error,Q-error,P-time,Q-time) are

  R_A=(635/165888,10201/10368,7711/6912,1069/864);
  R_C=(1493/1536,7/576,239/192,167/144).

The two full ordered first-hit cones are disjoint. A is at depth 10 with counts (3,0) and C at depth 11 with counts (5,4): reaching C from A needs six added 0/1 observations in one step, which is impossible; C cannot precede A in time. Thus the root moments are affine in u,w with no u*w term.

At Stage107's endpoint (u*,0), u*=1115808042440821/1479206400000000. Moving to arbitrary u,w from this reference,

  Delta eP=xA*(u-u*)+xC*w,
  Delta eQ=yA*(u-u*)+yC*w,

where
  xA=-248046875/990677827584, yA=65234375/208971104256,
  xC=1213675/300578991243264, yC=-197575/53496602689536.

Equating errors gives the **exact and only** compensation relation

  w=(4930688000000/67761451)*(u-u*).

Along it,
  eP=eQ=alpha107+(20174609375/464527285420032)*(u-u*).

The whole nonnegative, legal-mixing segment runs from (u*,0) to

  (u_end,w_end)=(159404052982303/211315200000000, 1),

with u_end<1 and resulting error delta=1457736575/2442361638167248896. Its right-end exact root moments are

  (eP,eQ,tP,tQ)=(
   alpha108, alpha108,
   1934483126570299962385/150728603955464503296,
   38346074856588751535/3140179249072177152).

At both endpoints, tP>tQ; because the root moments are affine along the compensation segment, tP>tQ everywhere. Every chosen action minimizes Bellman cost at (K108,L108), and eP=eQ=alpha, hence the dual lower bound is attained for all real alpha in the stated interval.

## Sharpness

Were the *same* dual support equality attained beyond alpha108, positivity of K108,L108 would force both errors equal alpha, every action used on a positive-mass history to be Bellman-minimizing, and max(tP,tQ)=tP. The exhaustive Bellman check leaves only A and C as choices. Even arbitrary history-dependent randomization is captured by probability-weighted u,w averages, since exact first-hit Q/P ratios and suffix moments are common within each count state, and the two cones do not intersect. Therefore equality of errors still forces w=(4930688000000/67761451)*(u-u*). The bound w<=1 gives u<=u_end and alpha<=alpha108, contradiction. Finite-horizon randomized-policy compactness guarantees optimum attainment. Thus the support line is strictly below the optimum beyond the endpoint. Here **C, not A, saturates**.

## Verification, limits, follow-up

Two separately implemented exact rational author programs passed: the first runs bottom-up Bellman, affine-gap sweep and first-hit/suffix calculus; the second uses independently memoized top-down Bellman and **literal ordered-history DFS**, visiting 1,022,824 and 995,728 ordered nodes at the two endpoints. This is author-side cross-checking, not independent review. Local full evidence bundle also includes both programs, JSON certificate and exact byte manifests. No floating-point evidence supports the theorem.

NEXT: Stage109 must traverse the neighboring A-tie dual ray after C's Q probability saturates, certify the first new global Bellman tie (or prove an obstruction) and reconstruct a positive balancing interval. Do not promote this external iid result to the native X6 Cell world. Native control returned CONTROL_QUOTA and registration returned STATIC_READONLY_SCOPE_DENIED (operation_sent=false); native owner and CLAIM could not be verified. This path holds ordinary **author evidence only**, not a canonical research Result.
